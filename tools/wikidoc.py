#!/usr/bin/env python3
"""
wikidoc.py — LLM-Wiki domain tooling for air-gapped SRE agents.

Two subcommands:

  generate   Convert a raw source file into ONE routable Markdown file by calling
             a local OpenAI-compatible LLM (e.g. Qwen via vLLM/Ollama/llama.cpp).
             Auto-validates the result before writing.

  validate   Validate one file or a tree against the routable-doc contract.
             Designed to run in CI (Woodpecker). Exit 0 = pass, 1 = fail.

Only hard dependency: PyYAML (near-universal, air-gap friendly).
No network needed for `validate`. `generate` talks only to your local endpoint.

Examples
--------
  # Validate everything routable in the repo (CI gate)
  python3 wikidoc.py validate --root . --strict

  # Validate a single file, machine-readable output for CI logs
  python3 wikidoc.py validate references/high-availability.md --json

  # Generate a routable KB file from a raw source, then validate it
  WIKIDOC_BASE_URL=http://localhost:8000/v1 WIKIDOC_MODEL=qwen3-27b \
  python3 wikidoc.py generate \
      --raw raw/kb-7135122.txt \
      --domain keycloak-admin --product RHBK --applies-to 26.6 \
      --type kb --provenance "7135122:public" \
      --out references/fips-argon2.md
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

try:
    import yaml  # PyYAML
except ImportError:  # pragma: no cover
    sys.stderr.write("ERROR: PyYAML required.  pip install pyyaml --break-system-packages\n")
    sys.exit(2)


# ---------------------------------------------------------------------------
# Contract definition (section-2 conventions encoded as a schema)
# ---------------------------------------------------------------------------

REQUIRED_KEYS = [
    "domain", "title", "product", "applies_to", "routable",
    "type", "inject", "authority", "source_provenance",
    "keywords", "last_verified",
]
ENUM_TYPE = {"runbook", "kb", "concept", "reference"}
ENUM_INJECT = {"full", "section"}
ENUM_AUTHORITY = {"internal-distilled", "upstream-verbatim"}
ENUM_VISIBILITY = {"public", "gated", "internal"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)

# Redaction heuristics — things that should never appear in a routable file.
SECRET_PATTERNS = [
    (re.compile(r"(?i)\b(password|passwd|secret|api[_-]?key|token)\s*[:=]\s*"
                r"(?!\*\*\*)(?!<)(?!\$\{)\S+"), "unredacted secret assignment"),
    (re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"), "JWT-like token"),
    (re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"), "raw IPv4 address"),
]
# FQDNs that are NOT the approved placeholder.
FQDN_RE = re.compile(r"\b(?:[a-z0-9-]+\.)+[a-z]{2,}\b", re.IGNORECASE)
FQDN_ALLOW = re.compile(r"(?i)(example\.internal|example\.com|localhost|k8s\.keycloak\.org|"
                        r"redhat\.com|keycloak\.org|github\.com|\.md$|\.so$|\.jar$|\.conf$)")

# Decision-tree signal for runbooks.
DECISION_TREE_RE = re.compile(r"^\s*(IF|ELIF|ELSE)\b", re.MULTILINE)
STOP_RE = re.compile(r"\b(STOP|DO NOT|escalate)\b", re.IGNORECASE)

# Directories whose contents are source/harvest only — must NOT be routable.
NON_ROUTABLE_DIR_HINTS = ("wiki/reference", "/raw/", "/harvest/")


# ---------------------------------------------------------------------------
# Result plumbing
# ---------------------------------------------------------------------------

class Finding:
    __slots__ = ("level", "code", "msg")

    def __init__(self, level: str, code: str, msg: str):
        self.level = level          # "error" | "warn"
        self.code = code
        self.msg = msg

    def as_dict(self):
        return {"level": self.level, "code": self.code, "msg": self.msg}


def _split_frontmatter(text: str):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    raw_fm, body = m.group(1), m.group(2)
    try:
        fm = yaml.safe_load(raw_fm)
    except yaml.YAMLError as e:
        return {"__yaml_error__": str(e)}, body
    return fm, body


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    rel = str(path).replace("\\", "/")
    is_source_dir = any(h in rel for h in NON_ROUTABLE_DIR_HINTS)

    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        return [Finding("error", "READ", f"cannot read file: {e}")]

    fm, body = _split_frontmatter(text)

    # Files in harvest/source dirs are allowed to have no frontmatter, but if
    # they DO declare routable:true that is a contract violation (context leak).
    if fm is None:
        if is_source_dir:
            return []  # source files need no frontmatter
        return [Finding("error", "NO_FRONTMATTER",
                        "routable file is missing YAML frontmatter")]

    if "__yaml_error__" in fm:
        return [Finding("error", "BAD_YAML", f"frontmatter not valid YAML: {fm['__yaml_error__']}")]

    routable = bool(fm.get("routable", False))

    if is_source_dir and routable:
        findings.append(Finding("error", "ROUTABLE_IN_SOURCE",
                                "file under a source/harvest dir must not be routable:true "
                                "(would leak raw docs into agent context)"))

    if not routable:
        # Non-routable but with frontmatter — minimal checks only.
        return findings

    # ---- required keys & enums -------------------------------------------
    for k in REQUIRED_KEYS:
        if k not in fm or fm[k] in (None, "", [], {}):
            findings.append(Finding("error", "MISSING_KEY", f"missing/empty required key: {k}"))

    if fm.get("type") not in ENUM_TYPE:
        findings.append(Finding("error", "ENUM_TYPE", f"type must be one of {sorted(ENUM_TYPE)}"))
    if fm.get("inject") not in ENUM_INJECT:
        findings.append(Finding("error", "ENUM_INJECT", f"inject must be one of {sorted(ENUM_INJECT)}"))
    if fm.get("authority") not in ENUM_AUTHORITY:
        findings.append(Finding("error", "ENUM_AUTH", f"authority must be one of {sorted(ENUM_AUTHORITY)}"))

    # ---- applies_to non-empty list ---------------------------------------
    at = fm.get("applies_to")
    if not isinstance(at, list) or not at:
        findings.append(Finding("error", "APPLIES_TO",
                                "applies_to must be a non-empty list (version-gating is mandatory)"))

    # ---- provenance ------------------------------------------------------
    prov = fm.get("source_provenance")
    has_gated = False
    if not isinstance(prov, list) or not prov:
        findings.append(Finding("error", "PROVENANCE",
                                "source_provenance must be a non-empty list (no orphan facts)"))
    else:
        for i, entry in enumerate(prov):
            if not isinstance(entry, dict) or "ref" not in entry or "visibility" not in entry:
                findings.append(Finding("error", "PROVENANCE_ENTRY",
                                        f"source_provenance[{i}] needs 'ref' and 'visibility'"))
                continue
            if entry["visibility"] not in ENUM_VISIBILITY:
                findings.append(Finding("error", "PROVENANCE_VIS",
                                        f"source_provenance[{i}].visibility must be one of "
                                        f"{sorted(ENUM_VISIBILITY)}"))
            if entry["visibility"] == "gated":
                has_gated = True

    # ---- last_verified is a real date ------------------------------------
    lv = fm.get("last_verified")
    lv_date = None
    if lv is not None:
        try:
            lv_date = lv if isinstance(lv, _dt.date) else _dt.date.fromisoformat(str(lv))
        except ValueError:
            findings.append(Finding("error", "DATE", "last_verified must be YYYY-MM-DD"))
    if lv_date and (_dt.date.today() - lv_date).days > 180:
        findings.append(Finding("warn", "STALE",
                                f"last_verified is {(_dt.date.today() - lv_date).days} days old "
                                "(re-verify against upstream)"))

    # ---- keywords sanity --------------------------------------------------
    kw = fm.get("keywords")
    if isinstance(kw, list) and not (3 <= len(kw) <= 12):
        findings.append(Finding("warn", "KEYWORDS",
                                f"keywords count is {len(kw)} (recommend 5-12 retrieval terms)"))

    # ---- body checks ------------------------------------------------------
    findings.extend(_check_body(fm, body))

    # ---- gated handling: gated source must point to a URL, not a fix ------
    if has_gated and "Resolution gated" not in body and "gated" not in body.lower():
        findings.append(Finding("warn", "GATED_BODY",
                                "frontmatter marks a gated source but body has no 'Resolution "
                                "gated — open <url>' pointer; verify no fix was fabricated"))

    return findings


def _check_body(fm: dict, body: str) -> list[Finding]:
    out: list[Finding] = []

    # redaction
    for pat, label in SECRET_PATTERNS:
        for m in pat.finditer(body):
            # IPv4 pattern also matches version strings like 26.2.10.0 — filter those.
            if label == "raw IPv4 address":
                octs = m.group(0).split(".")
                if any(int(o) > 255 for o in octs):
                    continue
            out.append(Finding("error", "REDACT",
                               f"possible {label}: '{m.group(0)[:48]}' "
                               "(use ***, example.internal, or a placeholder)"))
    # FQDNs that aren't the approved placeholders
    for m in FQDN_RE.finditer(body):
        tok = m.group(0)
        if FQDN_ALLOW.search(tok):
            continue
        if tok.endswith((".md", ".so", ".jar", ".conf", ".yaml", ".yml", ".sh", ".py", ".json")):
            continue
        out.append(Finding("warn", "FQDN",
                           f"non-placeholder hostname '{tok}' — confirm it is not internal"))

    # runbook must contain a hard decision tree with stop conditions
    if fm.get("type") == "runbook":
        if not DECISION_TREE_RE.search(body):
            out.append(Finding("error", "NO_DECISION_TREE",
                               "type:runbook must contain a hard decision tree (IF/ELIF/ELSE)"))
        elif not STOP_RE.search(body):
            out.append(Finding("warn", "NO_STOP",
                               "runbook decision tree has no STOP/DO NOT/escalate condition — "
                               "a model needs an explicit halt"))

    # kb files should follow Symptom/Cause/Fix
    if fm.get("type") == "kb":
        for needed in ("Symptom", "Cause", "Fix"):
            if needed not in body:
                out.append(Finding("warn", "KB_SHAPE",
                                   f"kb file is missing a '**{needed}:**' field"))
    return out


def _print_human(path: Path, findings: list[Finding]) -> None:
    if not findings:
        print(f"  OK    {path}")
        return
    errs = sum(1 for f in findings if f.level == "error")
    warns = sum(1 for f in findings if f.level == "warn")
    tag = "FAIL" if errs else "WARN"
    print(f"  {tag}  {path}  ({errs} error, {warns} warn)")
    for f in findings:
        mark = "✗" if f.level == "error" else "•"
        print(f"        {mark} [{f.code}] {f.msg}")


def cmd_validate(args) -> int:
    targets: list[Path] = []
    if args.path:
        targets = [Path(args.path)]
    else:
        root = Path(args.root)
        # Only validate routable areas by default unless --all is given.
        globs = ["**/*.md"] if args.all else ["references/**/*.md", "**/references/**/*.md"]
        seen = set()
        for g in globs:
            for p in root.glob(g):
                if p.is_file() and p not in seen:
                    seen.add(p)
                    targets.append(p)
        targets.sort()

    if not targets:
        sys.stderr.write("no Markdown files matched\n")
        return 1

    report = {}
    total_err = total_warn = 0
    for p in targets:
        f = validate_file(p)
        report[str(p)] = [x.as_dict() for x in f]
        total_err += sum(1 for x in f if x.level == "error")
        total_warn += sum(1 for x in f if x.level == "warn")
        if not args.json:
            _print_human(p, f)

    if args.json:
        print(json.dumps({"summary": {"files": len(targets),
                                       "errors": total_err,
                                       "warnings": total_warn},
                          "files": report}, ensure_ascii=False, indent=2))
    else:
        print(f"\n{len(targets)} file(s): {total_err} error(s), {total_warn} warning(s)")

    if total_err:
        return 1
    if args.strict and total_warn:
        return 1
    return 0


# ---------------------------------------------------------------------------
# Generation (calls a local OpenAI-compatible endpoint)
# ---------------------------------------------------------------------------

PROMPT_TEMPLATE = """# ROLE
You are a documentation engineer for an air-gapped SRE LLM-Wiki. You convert raw
source material into ONE routable Markdown file that a long-context SRE agent will
consume directly. Accuracy and traceability outrank completeness. You never invent
operational steps.

# OUTPUT CONTRACT
Emit ONLY the Markdown file (no code fences, no commentary). It MUST begin with YAML
frontmatter containing exactly these keys: domain, title, product, applies_to,
routable(=true), type, inject(full|section), authority(internal-distilled|
upstream-verbatim), source_provenance(list of {{ref, visibility}}), keywords(5-12),
last_verified(YYYY-MM-DD).

# HARD RULES
1. Every operational fact maps to a source_provenance entry. No orphan steps.
2. Keep only facts valid for APPLIES_TO; label version-specific steps inline.
3. Redact: secrets -> ***, hostnames -> example.internal, internal IPs -> placeholder.
4. Gated/insufficient source: DO NOT fabricate a fix. Emit "Resolution gated — open
   <url> with a Red Hat login." and set visibility: gated.
5. Internet-dependent steps get an inline "(Air-gap: stage in internal mirror first)".
6. Commands are atomic and self-contained.

# BODY STRUCTURE
- type=kb: per issue -> ### <id> — <title> / **Applies to:** / **Symptom:** /
  **Cause:** / **Fix:** (atomic, redacted) / **Relevant guide:** <sibling file>.
- type=runbook: numbered H2/H3; procedural sections use a HARD decision tree:
      ## <procedure>
      - IF <cond>: -> <action>; <what NOT to do>.
      - ELIF <cond>: -> STOP. <escalate + reason>.
      - ELSE: -> <action>; see <section>.
  Always give entry AND stop conditions.
- type=concept|reference: numbered hierarchy, one topic, snippets verbatim (redacted).

# INPUTS
DOMAIN: {domain}
PRODUCT: {product}
APPLIES_TO: {applies_to}
DOC_TYPE: {doctype}
PROVENANCE: {provenance}
TODAY: {today}

RAW_SOURCE:
<<<
{raw_source}
>>>

Emit the file now."""


def _llm_call(prompt: str, base_url: str, model: str, api_key: str,
              max_tokens: int, timeout: int) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {api_key}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise SystemExit(f"LLM endpoint error ({url}): {e}")
    return data["choices"][0]["message"]["content"]


def _strip_fences(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\n", "", t)
        t = re.sub(r"\n```\s*$", "", t)
    return t.strip() + "\n"


def cmd_generate(args) -> int:
    raw = Path(args.raw).read_text(encoding="utf-8")
    prompt = PROMPT_TEMPLATE.format(
        domain=args.domain, product=args.product,
        applies_to=json.dumps(args.applies_to),
        doctype=args.type, provenance=args.provenance,
        today=_dt.date.today().isoformat(), raw_source=raw,
    )
    base_url = args.base_url or os.environ.get("WIKIDOC_BASE_URL", "http://localhost:8000/v1")
    model = args.model or os.environ.get("WIKIDOC_MODEL", "qwen")
    api_key = os.environ.get("WIKIDOC_API_KEY", "not-needed")

    sys.stderr.write(f"[generate] calling {model} at {base_url} ...\n")
    out_text = _strip_fences(_llm_call(prompt, base_url, model, api_key,
                                       args.max_tokens, args.timeout))

    out_path = Path(args.out)
    tmp = out_path.with_suffix(out_path.suffix + ".tmp")
    tmp.write_text(out_text, encoding="utf-8")

    findings = validate_file(tmp)
    _print_human(tmp, findings)
    errs = sum(1 for f in findings if f.level == "error")
    if errs and not args.force:
        sys.stderr.write(f"[generate] {errs} contract error(s); not writing {out_path}. "
                         "Fix the source or re-run; use --force to keep the draft.\n")
        return 1
    tmp.replace(out_path)
    sys.stderr.write(f"[generate] wrote {out_path}\n")
    return 1 if errs else 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="wikidoc", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate", help="validate routable Markdown against the contract")
    v.add_argument("path", nargs="?", help="single file (omit to scan --root)")
    v.add_argument("--root", default=".", help="repo root to scan (default: .)")
    v.add_argument("--all", action="store_true",
                   help="scan every *.md, not just references/ (still skips source dirs)")
    v.add_argument("--strict", action="store_true", help="treat warnings as failures")
    v.add_argument("--json", action="store_true", help="machine-readable output")
    v.set_defaults(func=cmd_validate)

    g = sub.add_parser("generate", help="LLM-generate a routable file, then validate it")
    g.add_argument("--raw", required=True, help="path to raw source text")
    g.add_argument("--out", required=True, help="output .md path")
    g.add_argument("--domain", required=True)
    g.add_argument("--product", required=True)
    g.add_argument("--applies-to", dest="applies_to", required=True, nargs="+",
                   help="one or more versions, e.g. --applies-to 26.6 26.4")
    g.add_argument("--type", required=True, choices=sorted(ENUM_TYPE))
    g.add_argument("--provenance", required=True,
                   help='e.g. "7135122:public" or "internal-distilled:internal"')
    g.add_argument("--base-url", help="OpenAI-compatible endpoint (env WIKIDOC_BASE_URL)")
    g.add_argument("--model", help="model name (env WIKIDOC_MODEL)")
    g.add_argument("--max-tokens", type=int, default=4096)
    g.add_argument("--timeout", type=int, default=600)
    g.add_argument("--force", action="store_true", help="write even if validation fails")
    g.set_defaults(func=cmd_generate)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
