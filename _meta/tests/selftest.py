#!/usr/bin/env python3
"""selftest.py — offline smoke test for the wiki tooling. stdlib only, no network.

A tripwire against silent breakage from the content-mutating tools (corpus_to_vault,
backfill, crosslink, index) and the kb/lint/cost/llm/graph changes. Runs each tool and
asserts the invariants that "looks fine by eye" doesn't catch. Exit 0 = all pass, 1 = failure.

Tools run as `python -m wikikb.<tool>` (the package replaces the old flat _meta/bin/ scripts);
this test lives under _meta/tests/ and puts _meta/ on sys.path so `import wikikb` works without
a pip install (the standard test bootstrap).

    python3 wiki/_meta/tests/selftest.py
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))     # _meta/tests
META = os.path.dirname(HERE)                           # _meta
WIKI = os.path.dirname(META)                           # wiki
PKG = os.path.join(META, "wikikb")                     # the package dir (was _meta/bin)
REF = os.path.join(WIKI, "reference")
PY = sys.executable
sys.path.insert(0, META)                               # test bootstrap: make `import wikikb` importable
_ENV = {**os.environ, "PYTHONPATH": META + os.pathsep + os.environ.get("PYTHONPATH", "")}
checks = []

# package tools run via the `python -m wikikb <tool>` DISPATCHER — layout-independent, so the harness
# need not know which subpackage a tool lives in (and won't break if a tool changes group). eval->evaluate.
PKG_TOOLS = {"kb", "route", "expand", "embed", "cost", "llm", "lint", "manifest", "index", "crosslink", "livebank", "verify",
             "tags", "backfill", "corpus_to_vault", "docs_to_corpus", "pdf_to_corpus", "adoc_to_corpus", "migrate_native",
             "evaluate", "tkg"}


def run(name, *args, env=None):
    """Run a package tool via the dispatcher (`python -m wikikb <tool>`) or a tests/ script, from _meta/."""
    base = name[:-3] if name.endswith(".py") else name
    if base == "eval":
        base = "evaluate"
    cmd = ([PY, "-m", "wikikb", base] if base in PKG_TOOLS else [PY, os.path.join(HERE, name)]) + list(args)
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=META, env=env or _ENV)
    return p.returncode, p.stdout + p.stderr


def check(name, ok, detail=""):
    checks.append((name, ok, detail))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f"  — {detail}" if detail and not ok else ""))


# 1. kb reads the vault reference tier and reports a domain with notes
rc, out = run("kb.py", "domains")
m = re.search(r"keycloak\s+(\d+)\s+notes", out)
n_kb = int(m.group(1)) if m else 0
check("kb domains lists keycloak with notes", rc == 0 and n_kb > 0, f"rc={rc} n={n_kb}")

# 2. kb search returns ranked hits
rc, out = run("kb.py", "--domain", "keycloak", "search", "dpop sender constrained", "--limit", "3")
check("kb search returns hits", rc == 0 and "hit(s)" in out, out[:120])

# 3. abstract ranking signal is present in reference notes (regression guard for #4)
abstracts = 0
refdir = os.path.join(REF, "keycloak")
if os.path.isdir(refdir):
    for fn in os.listdir(refdir):
        if fn.endswith(".md") and not fn.startswith("_"):
            with open(os.path.join(refdir, fn), encoding="utf-8") as fh:
                if re.search(r"^abstract:", fh.read(), re.M):
                    abstracts += 1
check("reference notes carry abstract:", abstracts > 0, f"{abstracts} notes with abstract")

# 4. lint has no ERRORS (exit 0 under --strict)
rc, out = run("lint.py", "--strict")
check("lint --strict is clean (no errors)", rc == 0, out[-200:])

# 5. routing + reference indexes are not stale
rc, out = run("index.py", "--check")
check("index --check up to date", rc == 0, out[-200:])

# 6. every kb: token resolves (crosslink reports no 'unresolved kb:' line). ref:/guide: misses
# print on their own line and are a REPORT (mis-tiered names on pages), not this invariant.
rc, out = run("crosslink.py")
check("crosslink 0 unresolved kb: tokens", rc == 0 and "unresolved kb:" not in out, out[:160])

# 6b. resolve_any extends the resolver to ref: (curated references/ guide, path-qualified — three
# stems collide with page slugs) and guide: (the generated per-guide _ref index note), exact-name
# only; resolve() itself stays kb:-only so tkg's CITES edge set is untouched by construction.
from wikikb.build import crosslink as _cxr
_idx, _refs = _cxr.build_ref_index(), _cxr.build_refs_index()
_r_ref = _cxr.resolve_any("ref:server-configuration.md", "keycloak", _idx, _refs)
_r_gd = _cxr.resolve_any("guide:server_administration_guide", "keycloak", _idx, _refs)
check("crosslink resolve_any: ref:/guide: resolve exactly, misses stay None, resolve() kb:-only",
      _r_ref is not None and _r_ref["slug"] == "references/server-configuration"
      and _r_gd is not None and _r_gd["slug"] == "_ref-keycloak-server_administration_guide"
      and _cxr.resolve_any("ref:no-such-guide.md", "keycloak", _idx, _refs) is None
      and _cxr.resolve_any("guide:server_configuration", "keycloak", _idx, _refs) is None
      and _cxr.resolve("ref:server-configuration.md", "keycloak", _idx) is None,
      f"ref={_r_ref} guide={_r_gd}")

# 6c. ref:/guide: regression invariant (Codex veto finding #2): unresolved ref:/guide: citations on
# TRACKED pages must EQUAL the committed page<TAB>token PAIR baseline — observed-minus-baseline is a
# new regression (new token, or a legacy token spreading), baseline-minus-observed is a stale entry
# (debt was fixed: shrink the baseline in the same commit, so a later reintroduction fails too).
# Untracked pages (a live eval run files questions/ concurrently) are excluded; no git -> skip.
_bl_path = os.path.join(META, "eval", "crosslink-unresolved.baseline.txt")
_baseline = {ln.strip() for ln in open(_bl_path, encoding="utf-8")
             if ln.strip() and not ln.startswith("#")} if os.path.exists(_bl_path) else set()
try:
    _tracked = set(subprocess.run(["git", "ls-files", "topics", "entities", "questions"],
                                  capture_output=True, text=True, cwd=WIKI).stdout.split())
except Exception:  # noqa: BLE001 — copied-without-.git vaults: skip, never false-fail
    _tracked = None
if _tracked:
    _cx_idx, _cx_refs = _cxr.build_ref_index(), _cxr.build_refs_index()
    _observed = set()
    for _d in _cxr.PAGE_DIRS:
        _full = os.path.join(WIKI, _d)
        for _fn in sorted(os.listdir(_full)) if os.path.isdir(_full) else []:
            if not _fn.endswith(".md") or _fn == "README.md" or f"{_d}/{_fn}" not in _tracked:
                continue
            _m = _cxr.FM_RE.match(open(os.path.join(_full, _fn), encoding="utf-8").read())
            if not _m:
                continue
            _pfm = _cxr.top_fields(_m.group(1))
            for _t in _cxr.source_tokens(_m.group(1)):
                if (_t.startswith(("ref:", "guide:"))
                        and not _cxr.resolve_any(_t, _pfm.get("domain"), _cx_idx, _cx_refs)):
                    _observed.add(f"{_d}/{_fn}\t{_t}")
    _new_misses, _stale = _observed - _baseline, _baseline - _observed
    check("crosslink: unresolved ref:/guide: page+token pairs EQUAL committed baseline",
          not _new_misses and not _stale,
          f"{len(_new_misses)} new: " + "; ".join(sorted(_new_misses)[:5])
          + f" | {len(_stale)} stale (shrink the baseline): " + "; ".join(sorted(_stale)[:5]))

# 7. no orphan reference notes (every body note linked by a group index)
body, linked = set(), set()
if os.path.isdir(refdir):
    for fn in os.listdir(refdir):
        if fn.endswith(".md") and not fn.startswith("_"):
            body.add(fn[:-3])
        if fn.startswith("_ref-") and fn.endswith(".md"):
            with open(os.path.join(refdir, fn), encoding="utf-8") as fh:
                linked |= {t.strip() for t in re.findall(r"\[\[([^\]|#]+)", fh.read())}
orphans = body - linked
check("0 orphan reference notes", len(orphans) == 0, f"{len(orphans)} orphans e.g. {list(orphans)[:3]}")

# 8. gated pointer index exists and is non-empty
gated = os.path.join(refdir, "_gated-kb-index.md")
gok = os.path.exists(gated) and open(gated, encoding="utf-8").read().count("\n## ") > 0
check("gated KB index present + non-empty", gok)

# 9. reference-tier integrity: no drift vs _meta/reference.lock.json
rc, out = run("corpus_to_vault.py", "--verify")
check("reference tier matches integrity lock (no hand-edits)", rc == 0, out.strip()[-400:])

# 10. Phase-3 dense layer is OPTIONAL: kb --hybrid must still return hits when the embedding
# library / vendored model / index is absent (graceful degradation, no hard dep)
rc, out = run("kb.py", "--domain", "keycloak", "search", "dpop sender constrained", "--hybrid", "--limit", "2")
check("kb --hybrid degrades to lexical (no model)", rc == 0 and "hit(s)" in out, out[:160])

# 10b. Model-drift gate (5b fix): the index stamps a model fingerprint; stamp_ok must REJECT a
# mismatched stamp (else dense_rank silently cosines the query against another model's vectors) and
# stay backward-compatible with a stampless legacy index. Pure dict logic — no torch needed.
from wikikb.retrieval import embed as _embed
check("embed model-drift gate rejects a mismatched fingerprint",
      _embed.stamp_ok({"model_fingerprint": "sha256:deadbeefdeadbeef"}) is False,
      "stamp_ok accepted a bogus fingerprint — silent wrong retrieval possible")
check("embed model-drift gate is backward-compatible (no stamp -> pass)",
      _embed.stamp_ok({}) is True, "stampless legacy index was rejected")

# 11. Provenance gate — FAITHFUL: uses lint.page_gate_verdict() (the SAME rule lint --strict and the
# LangGraph gate node use), NOT the old inline copy that read the nested `_provenance` key and so
# silently missed the 50/52 reviewed pages on the native FLAT provenance schema (the BF-10 leak).
# One reviewed page is a DELIBERATE, documented non-fix — the gate's "first catch"
# (c9500-issu-svl-blackhole-nsf-gr; CLAUDE.md "let the page be its first catch"); it is the baseline,
# and lint --strict (#4) already reds on it. This check fails only on a NEW flagged reviewed page.
from wikikb.quality import lint as _lint
_BASELINE_GATE = {"c9500-issu-svl-blackhole-nsf-gr"}   # documented deliberate non-fix (also in #4)
gate = []
for _d, _slug, _path in _lint.page_files():
    _fm = _lint.parse_frontmatter(open(_path, encoding="utf-8").read())
    if not _fm or _fm.get("status") != "reviewed":
        continue
    if _lint.page_gate_verdict(_fm) and _slug not in _BASELINE_GATE:
        gate.append(_slug)
check("provenance gate: no NEW reviewed page with bad provenance (faithful via page_gate_verdict)",
      not gate, f"{len(gate)} NEW offender(s): " + ", ".join(gate[:5]))

# ---------------------------------------------------------------------------------------------
# LiteLLM/LangGraph/cost MIGRATION checks (additive). NOTE: the suite has TWO PRE-EXISTING reds
# unrelated to this migration — check #4 (lint --strict rc=1, from the deliberately-unfixed ISSU
# page's provenance gate: extracted==0 + reviewed&inferred>=extracted — the gate's documented
# "first catch"; missing `tags:` are NOTES, not errors, and don't affect strict rc) and check #6
# (crosslink: ~12 unresolved kb: tokens / gated solution ids). The migration's bar is "no NEW
# failures vs that recorded baseline" (COUNCIL-DIRECTIVES.md BF-2), not a green suite.
# ---------------------------------------------------------------------------------------------

# 12. Phase-0 (BF-1/BF-2): eval output is BYTE-IDENTICAL to the committed golden fixtures, with the
# cost seam wired in. Run with WIKI_LLM scrubbed + no tokenizer so the measured path can't leak.
_clean_env = {k: v for k, v in _ENV.items() if k not in ("WIKI_LLM", "WIKI_LLM_ALLOW_REMOTE")}


def _run_eval(variant):
    p = subprocess.run([PY, "-m", "wikikb", "evaluate"] + variant,
                       capture_output=True, text=True, cwd=META, env=_clean_env)
    return p.returncode, p.stdout + p.stderr


for _variant, _fixture in (([], "baseline.eval.out"), (["--route"], "baseline.eval.route.out"),
                           (["--graph"], "baseline.eval.graph.out")):
    _gp = os.path.join(META, "eval", _fixture)
    _golden = open(_gp, encoding="utf-8").read() if os.path.exists(_gp) else None
    _rc, _out = _run_eval(_variant)
    check("eval %s byte-identical to golden" % (" ".join(_variant) or "(default)"),
          _rc == 0 and _golden is not None and _out == _golden, f"rc={_rc} match={_out == _golden}")

# 13. Phase-0 (BF-1): cost.proxy_tokens is FLOAT (never floors) — the byte-identical invariant's root.
from wikikb.online import cost as _cost
check("cost.proxy_tokens is float (preserves eval float arithmetic)",
      _cost.proxy_tokens(17003) == 17003 / 4 and isinstance(_cost.proxy_tokens(10), float),
      f"proxy_tokens(17003)={_cost.proxy_tokens(17003)}")

# 14. Phase-0 (BF-9): the context-cost budget gate fails CI (exit 3) on a too-low budget, and the
# default run is unaffected (exit 0). Cost regressions now fail alongside recall.
_rc_tiny, _ = run("eval.py", "--budget-tokens", "1")
_rc_ok, _ = run("eval.py", "--budget-tokens", "100000000")
check("eval --budget-tokens gates (exit 3 tiny / 0 ample)", _rc_tiny == 3 and _rc_ok == 0,
      f"tiny={_rc_tiny} ample={_rc_ok}")

# 15. Degradation: cost is stdlib-safe (imports + reports with the optional measured deps absent).
_rc_cost, _out_cost = run("cost.py", "--status")
check("cost --status stdlib-safe (degrades, exit 0)", _rc_cost == 0 and "cost:" in _out_cost, _out_cost[:120])

# 16. Phase-1/2 (network tripwire): the cost+llm token/price/gateway paths open NO socket and do NO
# DNS. Block socket.socket + create_connection + getaddrinfo (the DNS arm is C-level and bypasses a
# socket-only patch — Phase-1 review #1), then exercise the cost AND llm offline paths.
_trip = (
    "import socket\n"
    "def _block(*a, **k):\n raise AssertionError('SOCKET/DNS in cost/llm path')\n"
    "socket.socket = _block\n"
    "socket.create_connection = _block\n"
    "socket.getaddrinfo = _block\n"
    "import sys; sys.path.insert(0, %r)\n"
    "from wikikb.online import cost, llm\n"
    "cost.count_tokens('proof of possession token binding', 'qwen2.5-32b')\n"
    "cost.proxy_tokens(1234)\n"
    "cost.status_str()\n"
    "cost.price_usd('ollama/qwen2.5:32b', 10, 5)\n"
    "llm.available(); llm.status_str()\n"
    "llm.complete([{'role': 'user', 'content': 'x'}])\n"
    "print('NO_SOCKET_OK')\n"
) % META
_pt = subprocess.run([PY, "-c", _trip], capture_output=True, text=True, cwd=META, env=_ENV)
check("cost+llm paths open no socket/DNS (network tripwire)",
      _pt.returncode == 0 and "NO_SOCKET_OK" in _pt.stdout, (_pt.stdout + _pt.stderr)[-200:])

# 17. Phase-1: with no tokenizer vendored, count_tokens == the chars/4 heuristic — the measured
# (vendored) tier must not leak a different number into a no-tokenizer environment.
_txt = "proof of possession token binding"
check("count_tokens degrades to chars/4 heuristic (no tokenizer)",
      not _cost.available("qwen2.5-32b") and _cost.count_tokens(_txt, "qwen2.5-32b") == len(_txt) // 4,
      f"available={_cost.available('qwen2.5-32b')} n={_cost.count_tokens(_txt, 'qwen2.5-32b')}")

# 18. Phase-2 (BF-8/BF-9): the cost behaviour probe (budget gate + defensive response parsing).
_rc_cp, _out_cp = run("cost_probe.py")
check("cost_probe passes (budget + defensive parse)", _rc_cp == 0, _out_cp[-160:])

# 18b. Phase-2 (upload trust boundary): the upload probe drives a REAL server over a REAL loopback
# socket (disabled -> byte-identical 404; enabled -> happy path + traversal/oversize/non-PDF/duplicate
# rejections), analogue of cost_probe.py above. Cleans up its own probe artifact in a `finally`.
_rc_up, _out_up = run("upload_probe.py")
check("upload_probe passes (disabled 404-identical + enabled trust-boundary checklist)",
      _rc_up == 0, _out_up[-300:])

# 18c. Phase-3 (fabricated-citation class): answer-side identifier grounding — a distinctive
# identifier asserted in the ANSWER but absent from the cited context is flagged loudly (+
# ungrounded_identifiers state field), never served silent. Analogue of gate_probe.py.
_rc_fp, _out_fp = run("fabrication_probe.py")
check("fabrication_probe passes (answer-side identifier grounding, query/context exemptions)",
      _rc_fp == 0, _out_fp[-300:])

# 19. Phase-2: llm is stdlib-safe and OFF by default (no litellm installed -> inactive, exit 0).
_rc_llm, _out_llm = run("llm.py", "--status")
check("llm --status stdlib-safe (off by default, exit 0)", _rc_llm == 0 and "llm:" in _out_llm, _out_llm[:120])

# 20. Air-gap: NO module-scope third-party import anywhere in the wikikb package (incl. graph/) — every
# heavy dep must be lazy (inside a function), so `import wikikb.<tool>` stays stdlib-safe.
_BANNED = re.compile(r"^(import|from)\s+(litellm|langchain|langgraph|tokenizers|sentence_transformers|numpy)\b")
_offenders = []
for _root, _dirs, _files in os.walk(PKG):       # the wikikb package, incl. graph/ subpackage
    if "__pycache__" in _root:
        continue
    for _fn in sorted(_files):
        if _fn.endswith(".py"):
            with open(os.path.join(_root, _fn), encoding="utf-8") as _fh:
                for _i, _l in enumerate(_fh, 1):
                    if _BANNED.match(_l):
                        _offenders.append(f"{os.path.relpath(os.path.join(_root, _fn), PKG)}:{_i}")
check("no module-scope 3rd-party import in wikikb/ (incl. graph/, lazy-only)", not _offenders, ", ".join(_offenders))

# 21. Phase-2 (BF-6): the loopback gate — local model+endpoint OK; bare cloud id / non-loopback host
# blocked (unless the WIKI_LLM_ALLOW_REMOTE double opt-in). Tests the gate logic directly (no litellm).
from wikikb.online import llm as _llm
_gate_ok = (_llm._is_local("ollama/qwen2.5:32b", "http://127.0.0.1:11434") is True
            and _llm._is_local("openai/served", "http://127.0.0.1:8000/v1") is True
            and _llm._is_local("gpt-4o", None) is False
            and _llm._is_local("openai/gpt-4o", "https://api.openai.com") is False)
_blocked = True
if os.environ.get("WIKI_LLM_ALLOW_REMOTE") != "1":   # only meaningful without the opt-in active
    _blocked = False
    try:
        _llm._enforce_local("gpt-4o", None)
    except _llm.RemoteBlocked:
        _blocked = True
check("llm loopback gate: local ok, cloud blocked (BF-6)", _gate_ok and _blocked,
      f"gate_ok={_gate_ok} blocked={_blocked}")

# 22. Degradation: llm.complete returns None when off/unavailable and NEVER raises (the dense_rank
# contract) — so callers transparently fall back to their extractive answer.
try:
    _none = _llm.complete([{"role": "user", "content": "x"}])
    check("llm.complete returns None when off/unavailable (never raises)", _none is None, repr(_none))
except Exception as _e:
    check("llm.complete returns None when off/unavailable (never raises)", False, f"raised {_e!r}")

# 23. Phase-3: eval --measure-llm runs OFFLINE -> exit 0, the recall portion is byte-identical to the
# golden (the measured block is strictly APPENDED), and it prints 'n/a (offline)'.
_gdef = open(os.path.join(META, "eval", "baseline.eval.out"), encoding="utf-8").read()
_rc_m, _out_m = _run_eval(["--measure-llm"])
check("eval --measure-llm offline (recall byte-identical + n/a offline)",
      _rc_m == 0 and _out_m.startswith(_gdef) and "LLM-CALL COST" in _out_m and "n/a (offline)" in _out_m,
      f"rc={_rc_m} prefix={_out_m.startswith(_gdef)}")

# 24. Faithfulness/air-gap (P3 exit test): importing the evaluate module pulls in ONLY the retrieval
# tools (kb/route/expand/embed + cost), NEVER litellm/langgraph/langchain — the recall path is
# independent of the LLM/graph tier. (cost.measure imports llm lazily; run_measure is never run at import.)
_imp = (
    "import sys; sys.path.insert(0, %r)\n"
    "import wikikb.quality.evaluate\n"
    "bad = [m for m in ('litellm', 'langgraph', 'langchain') if m in sys.modules]\n"
    "print('LEAKED:' + ','.join(bad) if bad else 'CLEAN_IMPORTS')\n"
) % META
_pi = subprocess.run([PY, "-c", _imp], capture_output=True, text=True, cwd=META, env=_ENV)
check("importing evaluate pulls in no litellm/langgraph (recall path clean)",
      _pi.returncode == 0 and "CLEAN_IMPORTS" in _pi.stdout, (_pi.stdout + _pi.stderr)[-200:])

# 25. Phase-2 (A1): llm.complete must merge a caller-passed max_tokens/temperature WITHOUT a kwarg
# collision (the built-in --probe passes max_tokens=8). litellm is absent, so inject a FAKE litellm
# to exercise the real kwarg-merge + completion call (the absent-lib path can't catch this).
_fake = (
    "import sys, types, os\n"
    "fake = types.ModuleType('litellm')\n"
    "fake.telemetry = True; fake.suppress_debug_info = False; fake.success_callback = []\n"
    "calls = {}\n"
    "def _completion(**kw):\n"
    "    calls.update(kw)\n"
    "    return type('R', (), {'choices': [type('C', (), {'message': type('M', (), {'content': 'pong'})()})()]})()\n"
    "fake.completion = _completion\n"
    "sys.modules['litellm'] = fake\n"
    "os.environ['WIKI_LLM'] = 'local'; os.environ['WIKI_LLM_MODEL'] = 'ollama/qwen2.5:32b'\n"
    "sys.path.insert(0, %r)\n"
    "from wikikb.online import llm\n"
    "r = llm.complete([{'role': 'user', 'content': 'x'}], max_tokens=8)\n"
    "assert r is not None, 'kwarg collision returned None'\n"
    "assert calls.get('max_tokens') == 8, calls\n"
    "assert llm.text_of(r) == 'pong', llm.text_of(r)\n"
    "print('A1_OK')\n"
) % META
_pf = subprocess.run([PY, "-c", _fake], capture_output=True, text=True, cwd=META, env=_ENV)
check("llm.complete merges caller kwargs without collision (A1, fake litellm)",
      _pf.returncode == 0 and "A1_OK" in _pf.stdout, (_pf.stdout + _pf.stderr)[-200:])

# 26. Phase-4: wikikb.graph.query_graph imports STDLIB-SAFE — langgraph is imported only inside the
# factory, so importing the module never pulls in langgraph/litellm (the air-gap invariant).
_gimp = (
    "import sys; sys.path.insert(0, %r)\n"
    "import wikikb.graph.query_graph as q\n"
    "bad = [m for m in ('langgraph', 'litellm', 'langchain') if m in sys.modules]\n"
    "print('LEAKED:' + ','.join(bad) if bad else ('HAS_BUILDER' if hasattr(q, 'build_query_graph') else 'NO_BUILDER'))\n"
) % META
_pgi = subprocess.run([PY, "-c", _gimp], capture_output=True, text=True, cwd=META, env=_ENV)
check("graph.query_graph imports stdlib-safe (no eager langgraph/litellm)",
      _pgi.returncode == 0 and "HAS_BUILDER" in _pgi.stdout, (_pgi.stdout + _pgi.stderr)[-200:])

# 27. Phase-4 (BF-4): lint.gate_banner fires ALL FIVE arms and is clean when sound — the single
# consolidated gate the LangGraph gate_node imports (no re-implementation / no prose<->graph drift).
_h2 = _lint.gate_banner({"slug": "x", "provenance_extracted": "0", "provenance_inferred": "2"})
_h3 = _lint.gate_banner({"slug": "x", "status": "reviewed", "provenance_extracted": "2", "provenance_inferred": "3"})
_h4 = _lint.gate_banner({"slug": "x", "status": "needs-review", "provenance_extracted": "5", "provenance_inferred": "1"})
_lL = _lint.gate_banner({"slug": "x", "status": "draft", "provenance_extracted": "2", "provenance_inferred": "4"})
_h1 = _lint.gate_banner({"slug": "x", "status": "reviewed", "provenance_extracted": "5", "provenance_inferred": "1"},
                        question_tier="support-kb", covered=["conceptual"])
_cl = _lint.gate_banner({"slug": "x", "status": "reviewed", "provenance_extracted": "9", "provenance_inferred": "1"},
                        question_tier="conceptual", covered=["conceptual"])
_arms = (bool(_h2) and bool(_h3) and any("H4" in r for r in _h4) and any("(L)" in r for r in _lL)
         and any("H1" in r for r in _h1) and not _cl)
check("lint.gate_banner fires all 5 arms (H1-H4 + L), clean when sound (BF-4)", _arms,
      f"h2={bool(_h2)} h3={bool(_h3)} h4={_h4} L={_lL} h1={_h1} clean={_cl}")

# 28. Phase-4 (BF-10): the gate, applied to a REAL page via lint.parse_frontmatter (NEVER a hand-built
# dict), flags the documented ISSU page — proving the flat-key path the old #11 leak missed.
_issu = os.path.join(WIKI, "questions", "c9500-issu-svl-blackhole-nsf-gr.md")
if os.path.isfile(_issu):
    _ifm = _lint.parse_frontmatter(open(_issu, encoding="utf-8").read())
    check("gate_banner flags the ISSU page via parse_frontmatter (faithful, BF-10)",
          bool(_lint.gate_banner(_ifm)), "expected non-empty banner")
else:
    check("gate_banner flags the ISSU page via parse_frontmatter (faithful, BF-10)", True, "(page absent — skipped)")

# 29. Phase-4: a graph node's ranking == the CANONICAL evaluate.rank() ordering — the node WRAPS the
# real tool, it does not re-implement it (faithfulness). Compared against evaluate.rank() (the
# (-score, version) ordering kb/eval use), so a tiebreaker drift is caught.
from wikikb.graph import nodes as _gn
from wikikb.quality import evaluate as _eval
_q = "dpop sender constrained token"
_rs = _gn.route_node({"query": _q})
_rs.update(_gn.retrieve_node({**_rs, "query": _q, "k": 5}))
_node_ids = [cid for cid, _ in _rs.get("candidates", [])]
_canon = [nid for nid, _ln in _eval.rank(_rs.get("domain"), _q)][:5]
check("graph retrieve_node ranking == evaluate.rank() canonical ordering (faithful)", _node_ids == _canon,
      f"node={_node_ids[:3]} canon={_canon[:3]}")

# 30. Phase-4: synthesize_node OFFLINE -> deterministic extractive fallback (no model call), banner
# prepended when present. Proves the graph degrades gracefully with the gateway off.
_syn = _gn.synthesize_node({"query": "x", "candidates": [("note-a", "body text"), ("note-b", "more")],
                            "banner": ["status: needs-review (H4)"]})
check("synthesize_node offline -> extractive fallback + banner (graceful)",
      "extractive fallback" in _syn.get("answer", "") and "note-a" in _syn["answer"] and _syn["answer"].startswith("⚠️"),
      _syn.get("answer", "")[:80])

# 31. Phase-5: wikikb.graph.ingest_graph imports STDLIB-SAFE (langgraph only inside the factory).
_iimp = (
    "import sys; sys.path.insert(0, %r)\n"
    "import wikikb.graph.ingest_graph as g\n"
    "bad = [m for m in ('langgraph', 'litellm', 'langchain') if m in sys.modules]\n"
    "print('LEAKED:' + ','.join(bad) if bad else ('HAS_BUILDER' if hasattr(g, 'build_ingest_graph') else 'NO'))\n"
) % META
_pig = subprocess.run([PY, "-c", _iimp], capture_output=True, text=True, cwd=META, env=_ENV)
check("graph.ingest_graph imports stdlib-safe (no eager langgraph)",
      _pig.returncode == 0 and "HAS_BUILDER" in _pig.stdout, (_pig.stdout + _pig.stderr)[-200:])

# 32. Phase-5 (BF-11): lint --status prints the LLM spend table (from the ledger if present, else a
# notice) and exits cleanly. Non-status output is unchanged (the table lives only under --status).
_rc_ls, _out_ls = run("lint.py", "--status")
check("lint --status shows the LLM spend table (BF-11)",
      _rc_ls == 0 and "LLM spend" in _out_ls, _out_ls[-160:])

# 33. Phase-5 (BF-11): lint.py has NO module-scope cost/llm import — LINT/STATUS stays stdlib-only and
# green even when the online tier was never installed (the ledger read is a direct JSON read).
_lint_src = open(os.path.join(PKG, "quality", "lint.py"), encoding="utf-8").read()
check("lint.py has no module-scope cost/llm import (BF-11)",
      not re.search(r"(?m)^(?:import|from wikikb(?:\.online)? import)\s+(?:cost|llm)\b", _lint_src))

# 34. Phase-5: the INGEST nodes round-trip OFFLINE (delta -> extract -> provenance -> record, dry-run)
# — manifest is read-only with apply=False, extract degrades to an extractive draft (no model).
from wikikb.graph import ingest_graph as _ig
_ist = _ig.delta_node({})
if _ist.get("current"):
    _ist.update(_ig.extract_node({**_ist}))
    _ist.update(_ig.provenance_node({**_ist}))
    _ist.update(_ig.record_node({**_ist, "apply": False}))
    _ok_ing = (_ist.get("current") is None and len(_ist.get("done", [])) >= 1
               and "extractive" in str(_ist.get("drafts", {})))
else:
    _ok_ing = True   # empty delta (all sources recorded) is a valid terminal state
check("ingest nodes round-trip offline (delta->extract->provenance->record, dry-run)",
      _ok_ing, "done=%s" % str(_ist.get("done"))[:80])

# 35. Restructure: legacy flat _meta/bin/ is GONE, and the package + concern-subpackages + tests are present.
# tkg/ is the temporal-knowledge-graph tier (stdlib core + optional Graphiti/Kuzu accelerator).
_SUBPKGS = ("retrieval", "build", "corpus", "quality", "online", "graph", "tkg")
check("restructure: _meta/bin/ removed, wikikb/ package + 7 subpackages + tests/ present",
      not os.path.isdir(os.path.join(META, "bin")) and os.path.isfile(os.path.join(PKG, "__init__.py"))
      and os.path.isfile(os.path.join(PKG, "paths.py")) and os.path.isdir(HERE)
      and all(os.path.isfile(os.path.join(PKG, g, "__init__.py")) for g in _SUBPKGS),
      "bin exists / package files / a subpackage __init__ missing")

# 36. Restructure (guard): NO bare OR un-grouped sibling import survives — every intra-package import of
# a module that lives in a subpackage must be `from wikikb.<group> import X`. A bare `import tags` or an
# un-grouped `from wikikb import tags` would ModuleNotFoundError under `python -m wikikb.<tool>` and,
# inside a try/except, SILENTLY disable a validator (the exact regression the review caught). `paths`
# alone is top-level, so `from wikikb import paths` is allowed; bare `import paths` is not.
# Built DYNAMICALLY from the tree (not a hand-maintained list) so a NEW module added to any subpackage
# is automatically covered — no blind spot. paths/__init__/__main__ are top-level package infra, excluded.
_SUBPKG_MODS = tuple(sorted(
    _fn[:-3] for _r, _d, _fs in os.walk(PKG) if "__pycache__" not in _r
    for _fn in _fs
    if _fn.endswith(".py") and _fn not in ("__init__.py", "__main__.py", "paths.py")))
_alt = "|".join(_SUBPKG_MODS)
_bare = re.compile(r"^\s*import (%s|paths)\b" % _alt)                 # a bare sibling import (always wrong)
_ungrouped = re.compile(r"^\s*from wikikb import (%s)\b" % _alt)      # must be `from wikikb.<group> import`
_bad_sib = []
for _root, _dirs, _files in os.walk(PKG):
    if "__pycache__" in _root:
        continue
    for _fn in sorted(_files):
        if _fn.endswith(".py"):
            with open(os.path.join(_root, _fn), encoding="utf-8") as _fh:
                for _i, _l in enumerate(_fh, 1):
                    if _bare.match(_l) or _ungrouped.match(_l):
                        _bad_sib.append("%s:%d" % (os.path.relpath(os.path.join(_root, _fn), PKG), _i))
check("no bare/un-grouped sibling import in wikikb/ (must be `from wikikb.<group> import X`)",
      not _bad_sib, ", ".join(_bad_sib))

# 37. Restructure: the `python -m wikikb <tool>` __main__ dispatcher resolves + runs a tool (deep-
# research flagged pkg-level `-m` invocation as worth a targeted test; this locks it). Run from _meta/
# so the package is importable via the CWD-prepend, the documented no-install pattern.
_pd = subprocess.run([PY, "-m", "wikikb", "kb", "domains"], capture_output=True, text=True, cwd=META, env=_ENV)
check("`python -m wikikb <tool>` dispatcher runs a tool (CWD-prepend, no install)",
      _pd.returncode == 0 and "keycloak" in _pd.stdout, (_pd.stdout + _pd.stderr)[-160:])

# 38. tkg tier (air-gap): the optional Graphiti/Kuzu backend was DELETED 2026-07-05 (Kuzu archived
# upstream; the backend was verified inert with zero consumers — see wiki/CLAUDE.md). Assert the module
# is actually GONE (not just unused), the remaining tkg tier still imports pulling NO third-party
# (kuzu/graphiti_core), and `tkg graph-status` still runs clean without it — the JSON store is the sole
# canonical backend now.
_tkg_err = ""
try:
    _saved_tkg = os.environ.pop("WIKI_TKG", None)
    import importlib as _il
    try:
        _il.import_module("wikikb.tkg.graphiti_backend")
        _gone = False
    except ModuleNotFoundError:
        _gone = True
    for _m in ("wikikb.tkg", "wikikb.tkg.model", "wikikb.tkg.store", "wikikb.tkg.tkg", "wikikb.tkg.versions"):
        _il.import_module(_m)
    _no3p = "kuzu" not in sys.modules and "graphiti_core" not in sys.modules
except Exception as _e:                                                 # noqa: BLE001
    _no3p = _gone = False
    _tkg_err = repr(_e)
finally:
    if _saved_tkg is not None:
        os.environ["WIKI_TKG"] = _saved_tkg
_rc_gs, _out_gs = run("tkg", "graph-status")
check("tkg: graphiti_backend module is GONE; remaining tkg tier imports pull no kuzu/graphiti_core; "
      "graph-status runs clean without it",
      _gone and _no3p and _rc_gs == 0,
      _tkg_err or "backend still importable / third-party leaked / graph-status rc=%d" % _rc_gs)

# 39. tkg model: deterministic build + the R4 temporal invariant — structural edges carry NO dates;
# version-temporal edges carry valid_from + precision and NEVER valid_until (no supersession inference).
_tkg2_err = ""
try:
    from wikikb.tkg import model as _tm, store as _ts
    _g1, _g2 = _tm.build_graph(), _tm.build_graph()
    _det = _ts.graph_to_dict(_g1) == _ts.graph_to_dict(_g2)
    _r4 = all((e.valid_from and e.valid_until is None and e.valid_from_precision)
              if e.kind == _tm.VERSION_TEMPORAL
              else (e.valid_from is None and e.valid_until is None)
              for e in _g1.edges)
    _has_struct = any(e.kind == "structural" for e in _g1.edges)
except Exception as _e:                                                 # noqa: BLE001
    _det = _r4 = _has_struct = False
    _tkg2_err = repr(_e)
check("tkg: deterministic build + R4 invariant (structural=no dates; version-temporal=valid_from+precision)",
      _det and _r4 and _has_struct, _tkg2_err or "non-deterministic or R4 violated")

# 40. tkg CLI: all five verbs run via the `python -m wikikb tkg <verb>` dispatcher against the JSON store.
_v_ok, _v_bad = True, ""
for _verb in (("ingest", "--stdout"), ("graph-status",), ("cross-domain-query",),
              ("provenance-trace", "dpop"), ("temporal-query", "--as-of", "26.2")):
    _rc, _o = run("tkg", *_verb)
    if _rc != 0:
        _v_ok, _v_bad = False, "%s -> rc=%d %s" % (_verb[0], _rc, _o[-100:])
        break
check("tkg: all five CLI verbs run via `python -m wikikb tkg ...` (exit 0)", _v_ok, _v_bad)

# 40a. tkg ingest idempotence (regression guard): `tkg ingest` writes the JSON store wholesale
# (store.save_store overwrites, never appends), so two consecutive real CLI ingests must report the
# SAME node+edge counts — the doubling bug this used to guard against lived only in the REMOVED
# Kuzu/Graphiti backend (checks #38/#39 already prove build_graph() is deterministic in-memory; this
# is the cheap CLI-level tripwire over the actual write-to-disk path).
_rc_i1, _out_i1 = run("tkg", "ingest")
_rc_i2, _out_i2 = run("tkg", "ingest")


def _tkg_counts(out):
    _n = re.search(r"nodes:\s*(\d+)", out)
    _e = re.search(r"edges:\s*(\d+)", out)
    return (int(_n.group(1)) if _n else None, int(_e.group(1)) if _e else None)


_counts1, _counts2 = _tkg_counts(_out_i1), _tkg_counts(_out_i2)
check("tkg ingest idempotence: two consecutive `tkg ingest` runs report identical node+edge counts",
      _rc_i1 == 0 and _rc_i2 == 0 and _counts1 == _counts2 and None not in _counts1,
      f"rc1={_rc_i1} rc2={_rc_i2} counts1={_counts1} counts2={_counts2}")

# 40b. tkg supersession (rule R3, deterministic): _successor_slug picks the same-family strictly-newer
# candidate under a url_tail (a primary that lags a newer harvest is flagged), returns None for the newest,
# ignores a different family, and every Source node carries the superseded_by attr (None ⇒ current).
_sup_err = ""
try:
    from wikikb.tkg import model as _sm
    _cands = [{"slug": "g-26-0", "version": "26.0", "primary": False, "family": "rhbk"},
              {"slug": "g-26-2", "version": "26.2", "primary": True, "family": "rhbk"},
              {"slug": "g-26-4", "version": "26.4", "primary": False, "family": "rhbk"},
              {"slug": "g-7-6", "version": "7.6", "primary": False, "family": "rhsso"}]
    _sup_ok = (_sm._successor_slug(_cands, "rhbk", "26.2") == "g-26-4"      # lagging primary -> successor
               and _sm._successor_slug(_cands, "rhbk", "26.4") is None      # newest -> nothing supersedes
               and _sm._successor_slug(_cands, "rhsso", "7.6") is None)     # cross-family ignored
    _sg = _sm.build_graph()
    _sup_attr = all("superseded_by" in n.attrs for n in _sg.nodes.values() if n.label == "Source")
except Exception as _e:                                                     # noqa: BLE001
    _sup_ok = _sup_attr = False
    _sup_err = repr(_e)
check("tkg: supersession _successor_slug derives same-family newer note; Source nodes carry superseded_by",
      _sup_ok and _sup_attr, _sup_err or "successor logic or attr missing")

# 40c. expand --as-of (M1 temporal wiring): _asof_filter drops a version-temporal note introduced AFTER
# the as-of point but NEVER a structural/undated note (omit-not-fabricate). Uses the tkg store/in-memory
# build; expand() itself is untouched so the eval golden stays byte-identical.
_af_err = ""
try:
    from wikikb.retrieval import expand as _ex
    _later = "rhbk-26-6-multi-cluster-introduction"   # version-temporal, valid_from 2026-06-03
    _struct = "zzz-undated-structural-note"            # not in the graph -> undated -> never filtered
    _r = {"notes_seed": {_later, _struct}, "notes_closure": {_later, _struct}}
    _af_line = _ex._asof_filter(_r, "keycloak", "26.0")   # 26.0 -> 2024-11-21, before 2026-06-03
    _af_ok = (_af_line is not None and _later not in _r["notes_seed"] and _struct in _r["notes_seed"])
except Exception as _e:                                                     # noqa: BLE001
    _af_ok = False
    _af_err = repr(_e)
check("expand --as-of filters a later-version note, never a structural one (M1)", _af_ok, _af_err)

# 41. Faithfulness eval: module imports clean, cases file is valid JSONL, and the scoring logic
# is stdlib-safe (no LLM needed for the infrastructure check). The full eval run with WIKI_LLM=local
# is the separate faithfulness_probe.py (analogous to gate_probe.py vs selftest.py).
from wikikb.quality import faithfulness as _ff
_faith_cases = os.path.join(META, "eval", "faithfulness_cases.jsonl")
_faith_ok = os.path.isfile(_faith_cases)
_faith_n = 0
if _faith_ok:
    try:
        _faith_cases_loaded = _ff.load_cases(_faith_cases)
        _faith_n = len(_faith_cases_loaded)
        _faith_ok = _faith_n > 0
    except Exception as _e:
        _faith_ok = False
        _faith_err = repr(_e)
check("faithfulness eval: module imports + cases valid (%d cases)" % _faith_n, _faith_ok, "")

# 42. Phase-5 routing lever (litellm.Router, OSS): complete_routed exists and DEGRADES to a no-op
# when <2 models are configured — single-model config must build no Router (today's behavior). Pure
# config check; opens no socket and needs no litellm (env off -> _router returns None either way).
from wikikb.online import llm as _llm
_route_ok = hasattr(_llm, "complete_routed") and _llm._router({"model": "ollama/x"}) is None \
    and _llm._router({"model_small": "ollama/s"}) is None        # one of the pair missing -> no-op
check("llm routing: complete_routed degrades to single-model when <2 models configured", _route_ok, "")

# 43. openshift brain (ADD DOMAIN): declared in taxonomy, has a routing index, and its raw notes-first
# tier is grep-retrievable. The whole-loop proof that the new domain stands up like the others.
_tax = open(os.path.join(META, "taxonomy.md"), encoding="utf-8").read()
_osh_idx = os.path.join(WIKI, "index.openshift.md")
_osh_decl = "- domain: openshift" in _tax
_osh_indexed = os.path.isfile(_osh_idx) and "openshift-overview" in open(_osh_idx, encoding="utf-8").read()
_osh_src = os.path.isdir(os.path.join(WIKI, "_sources", "openshift"))
_osh_refdir = os.path.join(WIKI, "reference", "openshift")
_osh_corpus = os.path.isdir(_osh_refdir) and len([f for f in os.listdir(_osh_refdir)
                                                  if f.endswith(".md")]) > 1000   # corpus-backed
import importlib as _il
import importlib.util  # noqa: F401  # `_il.util` needs the submodule imported explicitly (was previously
                                     # a side effect of graphiti_backend.py, deleted 2026-07-05)
_adoc_ok = _il.util.find_spec("wikikb.corpus.adoc_to_corpus") is not None
check("openshift domain: declared + indexed + corpus-backed (>1000 ref notes) + adoc harvester present",
      _osh_decl and _osh_indexed and _osh_src and _osh_corpus and _adoc_ok, "")

# 43b. pdf_to_corpus harvester: pure-stdlib path (.txt wins over .pdf; image-only PDFs are a LOUD
# skip, never an empty record), record matches the corpus_to_vault contract, page markers survive,
# and the emitted url tail round-trips as a resolvable kb: crosslink token.
import tempfile as _tf
from wikikb.corpus import pdf_to_corpus as _p2c, corpus_to_vault as _c2v
from wikikb.build import crosslink as _cx
with _tf.TemporaryDirectory() as _td:
    open(os.path.join(_td, "guide.txt"), "w").write("Guide Title Line\nbody one\fpage two body")
    open(os.path.join(_td, "guide.pdf"), "wb").write(b"%PDF-1.4 garbage")   # .txt must win
    open(os.path.join(_td, "scan.pdf"), "wb").write(b"%PDF-1.4 garbage")    # must be skipped loudly
    _recs, _bodies, _skipped, _methods = _p2c.build(_td, "pdfx", "pdf://pdfx", "pdfx", "1", None, "doc", 0)
    _r = _recs[0] if _recs else {}
    _contract = all(k in _r for k in ("title", "url", "family", "documentKind", "abstract",
                                      "body_status", "body_file")) and _r.get("body_status") == "fetched"
    _body = _bodies.get(_r.get("body_file"), "")
    _markers = "<!-- p.1 -->" in _body and "<!-- p.2 -->" in _body
    with _tf.TemporaryDirectory() as _ref:
        os.makedirs(os.path.join(_ref, "pdfx"))
        _obt, _c2v.body_text = _c2v.body_text, lambda d, r: _bodies[r["body_file"]]
        open(os.path.join(_ref, "pdfx", "pdfx-1-guide.md"), "w").write(
            _c2v.render_note("pdfx", _r, "pdfx-1-guide"))
        _c2v.body_text = _obt
        _oref, _cx.REF = _cx.REF, _ref
        _hit = _cx.resolve("kb:guide", "pdfx", _cx.build_ref_index())
        _cx.REF = _oref
    check("pdf_to_corpus: .txt precedence + loud skip + contract + page markers + kb: token resolves",
          len(_recs) == 1 and _methods.get("guide") == "txt" and len(_skipped) == 1
          and _skipped[0][0] == "scan" and _contract and _markers
          and bool(_hit) and _hit["slug"] == "pdfx-1-guide",
          f"recs={len(_recs)} methods={_methods} skipped={_skipped} hit={_hit}")

# 44. Citation-grounding gate: a distinctive env-var-shaped claim absent from the domain corpus is
# flagged (the SSO_HTTPS_CIPHER_SUITES fabrication class), and a claim tagged (inferred) is skipped.
# This is the CONTENT arm of the citation contract, complementing the provenance-COUNT gate (H2/H3).
from wikikb.quality import lint as _lint
_fab = _lint.ungrounded_citations("# T\n\nSet the `FAKE_NONEXISTENT_ENVVAR_XYZ` variable to enable it.\n",
                                  {"domain": "keycloak"})
_skip = _lint.ungrounded_citations("# T\n\nSet `FAKE_NONEXISTENT_ENVVAR_XYZ` (inferred).\n",
                                   {"domain": "keycloak"})
check("citation grounding: flags ungrounded env-var claim, skips (inferred)",
      ("FAKE_NONEXISTENT_ENVVAR_XYZ" in _fab) and not _skip, repr((_fab, _skip)))

# 45. BM25 sanity: build_idf on a tiny 3-rec fixture — a rarer term (df=1) gets a strictly higher idf
# than a term shared by every doc (df=3), and both stay non-negative (Lucene/ES smoothing never
# goes negative, unlike the classic Robertson-Sparck-Jones form — see kb.build_idf's docstring).
from wikikb.retrieval import kb as _kb
_tiny_recs = [
    {"title": "alpha widget", "abstract": "", "_body": "alpha widget shared term"},
    {"title": "beta widget", "abstract": "", "_body": "beta widget shared term"},
    {"title": "gamma widget", "abstract": "", "_body": "gamma widget shared term"},
]
_idf = _kb.build_idf(_tiny_recs)
_rare, _common = _idf.get("alpha", -1.0), _idf.get("shared", -1.0)
check("BM25 build_idf: rarer term (df=1) has strictly higher idf than a common term (df=3), both >= 0",
      _rare > _common >= 0, f"rare(alpha)={_rare} common(shared)={_common}")

# 46. evaluate --min-recall gates exactly like --budget-tokens: exit 3 on an unreachable bar, exit 0
# on a trivial one. Default run (no --min-recall) is untouched — the gate only fires when passed.
_rc_hi, _ = run("eval.py", "--min-recall", "99")
_rc_lo, _ = run("eval.py", "--min-recall", "1")
check("eval --min-recall gates (exit 3 unreachable / 0 trivial)", _rc_hi == 3 and _rc_lo == 0,
      f"hi={_rc_hi} lo={_rc_lo}")

# 47. Cite-parse unit (graph/nodes.synthesize_node): monkeypatch wikikb.online.llm IN-PROCESS (no fake
# litellm needed — synthesize_node calls llm.complete_routed/llm.text_of directly) to cover the 3 real
# paths offline can't exercise: a real cite parsed out of a bogus one, zero cites -> the model's prose
# is WITHHELD entirely (2026-07 audit fix — grounding failure used to still serve the fabricated prose
# behind a banner), and a None answer -> the deterministic extractive fallback.
from wikikb.graph import nodes as _nodes
from wikikb.online import llm as _llmmod
_orig_complete_routed, _orig_text_of = _llmmod.complete_routed, _llmmod.text_of
try:
    _cite_cands = [("noteA", "body a"), ("noteB", "body b")]
    _llmmod.complete_routed = lambda messages, tier=None, **kw: "FAKE_RESP"

    _llmmod.text_of = lambda resp: "X [cite: noteA]. [cite: bogus]"
    _o1 = _nodes.synthesize_node({"query": "q", "candidates": _cite_cands})
    _c1 = (_o1["used"] == ["noteA"] and _o1["grounding_fail"] is False
           and _o1["grounding_basis"] == {"cited_ids": ["noteA"],
                                           "basis": "cited-full-bodies+query"})

    _llmmod.text_of = lambda resp: "no citations anywhere in this answer"
    _o2 = _nodes.synthesize_node({"query": "q", "candidates": _cite_cands})
    _c2 = (_o2["used"] == [] and _o2["grounding_fail"] is True
           and _o2["answer"].startswith("⚠️ Ungrounded synthesis")
           and "ungrounded synthesis withheld" in _o2["answer"]
           and "noteA" in _o2["answer"] and "noteB" in _o2["answer"]
           and "no citations anywhere in this answer" not in _o2["answer"])  # the fabricated prose must NOT reach the reader

    _llmmod.text_of = lambda resp: None
    _o3 = _nodes.synthesize_node({"query": "q", "candidates": _cite_cands})
    _c3 = (_o3["used"] == ["noteA", "noteB"] and "[extractive fallback" in _o3["answer"]
           and _o3["grounding_basis"]["basis"] == "not-checked-extractive-fallback")
finally:
    _llmmod.complete_routed, _llmmod.text_of = _orig_complete_routed, _orig_text_of
check("synthesize_node cite-parse: real cite drops bogus id, no-cite -> prose withheld (not served), None -> extractive",
      _c1 and _c2 and _c3, f"c1={_c1} c2={_c2} c3={_c3}")

# 47b. Loud fallback reason (2026-07 audit fix): when WIKI_LLM is meant to be active but the gateway
# returns no answer (dead endpoint / empty content), the extractive fallback must say WHY instead of
# staying silent about it — monkeypatch mode()/load_config()/complete_routed() to simulate "on but dead".
_orig_mode, _orig_load_config = _llmmod.mode, _llmmod.load_config
try:
    _llmmod.complete_routed = lambda messages, tier=None, **kw: None      # gateway: dead endpoint
    _llmmod.text_of = lambda resp: None
    _llmmod.mode = lambda: "local"
    _llmmod.load_config = lambda: {"model": "ollama/qwen2.5:3b", "api_base": "http://127.0.0.1:11434"}
    _o4 = _nodes.synthesize_node({"query": "q", "candidates": _cite_cands})
    _c4 = ("[extractive fallback" in _o4["answer"]
           and "gateway returned no answer: http://127.0.0.1:11434" in _o4["answer"])
finally:
    _llmmod.complete_routed, _llmmod.text_of = _orig_complete_routed, _orig_text_of
    _llmmod.mode, _llmmod.load_config = _orig_mode, _orig_load_config
check("synthesize_node fallback names the reason when WIKI_LLM is on but the gateway is dead", _c4,
      _o4.get("answer", "")[:120])

# 47c. WI-7: public_result is the ONE serializer — grounding status ALWAYS structured (D3), strict
# withholds. No pipeline run needed: feed synthetic final states straight to the serializer.
from wikikb.graph import ask as _askmod
_clean_st = {"answer": "all good", "used": ["n1"], "grounding_fail": False,
             "ungrounded_identifiers": [], "orchestrator": "linear"}
_bad_st = {"answer": "⚠️ warned\n\nprose with FAKE_ENV_VAR", "used": ["n1"], "grounding_fail": False,
           "ungrounded_identifiers": ["FAKE_ENV_VAR"],
           "grounding_basis": {"cited_ids": ["n1"], "basis": "cited-full-bodies+query"}}
_pr1 = _askmod.public_result("q", _clean_st, [], strict=False)
_pr2 = _askmod.public_result("q", _bad_st, [], strict=False)     # flag-default: served, flagged
_pr3 = _askmod.public_result("q", _bad_st, [], strict=True)      # strict: withheld
_pr4 = _askmod.public_result("q", {"answer": "x", "used": [], "grounding_fail": True}, [], strict=True)
_always = ("withheld", "ungrounded_identifiers", "grounding_basis", "grounding_fail", "guard", "banner")
_c_shape = all(k in _pr for _pr in (_pr1, _pr2, _pr3, _pr4) for k in _always)
_c_flagdef = _pr2["withheld"] is False and _pr2["answer"].startswith(_bad_st["answer"]) \
    and _pr2["ungrounded_identifiers"] == ["FAKE_ENV_VAR"]
_c_strict = _pr3["withheld"] is True and "FAKE_ENV_VAR" not in _pr3["answer"].split("ungrounded_identifiers=")[0] \
    and "withheld by strict grounding mode" in _pr3["answer"] \
    and _pr4["withheld"] is True and "withheld by strict grounding mode" in _pr4["answer"]
_c_clean = (_pr1["withheld"] is False and _pr1["ungrounded_identifiers"] == []
            and _pr1["answer"].startswith("all good")
            and "### RH ground-truth" in _pr1["answer"] and "### Wiki" in _pr1["answer"])
_preexisting = _askmod.public_result(
    "q", {"answer": "x\n\n## References\n- ref:leak [[leak]]", "used": [],
          "grounding_fail": False, "graph_pages": ["real-page"]},
    [{"id": "real-note", "source": "https://example.invalid"}], strict=False)
_c_canonical = ("## References (canonical)" in _preexisting["answer"]
                and "`ref:real-note`" in _preexisting["answer"]
                and "[[real-page]]" in _preexisting["answer"])
_env_key = "WIKI_STRICT_GROUNDING"
_env_prev = os.environ.get(_env_key)
try:
    os.environ[_env_key] = "1"
    # tri-state precedence: explicit False must BEAT env=1 (per-call wins); None defers to env
    _c_env = (_askmod.strict_default() is True
              and _askmod.resolve_strict(None) is True
              and _askmod.resolve_strict(False) is False
              and _askmod.public_result("q", _bad_st, [], strict=_askmod.resolve_strict(False))["withheld"] is False)
    os.environ.pop(_env_key)
    _c_env = _c_env and _askmod.strict_default() is False \
        and _askmod.resolve_strict(None) is False and _askmod.resolve_strict(True) is True
finally:
    if _env_prev is not None:
        os.environ[_env_key] = _env_prev
    else:
        os.environ.pop(_env_key, None)
# per-surface explicit-false parsing: serve ?strict= tri-state and the CLI --no-strict opt-out
from wikikb.serve import serve as _srvmod
_c_parse = (_srvmod._parse_strict(None) is None and _srvmod._parse_strict("1") is True
            and _srvmod._parse_strict("true") is True and _srvmod._parse_strict("0") is False
            and _srvmod._parse_strict("false") is False)
import argparse as _argparse
_cli_p = _argparse.ArgumentParser()
_cli_p.add_argument("--strict", action=_argparse.BooleanOptionalAction, default=None)
_c_cli = (_cli_p.parse_args([]).strict is None and _cli_p.parse_args(["--strict"]).strict is True
          and _cli_p.parse_args(["--no-strict"]).strict is False)
check("public_result (WI-7): always-structured grounding fields, flag-default serves+flags, "
      "strict withholds on ungrounded ids AND grounding_fail, tri-state precedence "
      "(explicit False beats env=1) on env/serve-param/CLI",
      _c_shape and _c_flagdef and _c_strict and _c_clean and _c_canonical
      and _c_env and _c_parse and _c_cli,
      f"shape={_c_shape} flagdef={_c_flagdef} strict={_c_strict} clean={_c_clean} "
      f"canonical={_c_canonical} env={_c_env} parse={_c_parse} cli={_c_cli}")

# 47d. Premise-correction dropout fix (manual session #4, RID Block Size): deterministic premise
# extraction fixtures on the four 2026-07-12 manual-session questions, then the premise gate
# matrix: filled table -> clean; missing table (the dropout) -> premise_unaddressed + strict
# withhold; invalid verdict word -> premise_verdict_invalid; fabricated correction number ->
# premise_correction_ungrounded; no premises / extractive fallback -> today's behavior, no flags.
from wikikb.quality import lint as _plint
_S4 = ("I set RID Block Size to 50,000 on our RID master, since the global RID space is capped "
       "at 2^31 anyway - how many pool allocations until we exhaust it?")
_S2 = ("Our security team wants to harden RHBK 26 against a flood of half-open login attempts "
       "filling the cache. Is there a way to cap how many concurrent authentication sessions a "
       "single browser/root session can hold, what is the default, and how do I change it?")
_S1 = "What is back-channel logout in OpenID Connect?"
_S3 = "What is the precedence of RHBK's four configuration sources?"
_p4 = _plint.extract_premises(_S4)
_p4_toks = {t for p in _p4 for t in p["tokens"]}
_c_fx = (len(_p4) == 2 and {"50,000", "2^31"} <= _p4_toks and "RID Block Size" in _p4_toks
         and len(_plint.extract_premises(_S1)) == 0 and len(_plint.extract_premises(_S3)) == 0
         and all(p["tokens"] for p in _plint.extract_premises(_S2)))
_pg_cands = [("ad-ds-managing-rid-issuance",
              "the global RID space was limited to 2^30 (or 1,073,741,823) total RIDs ... the "
              "2^31 bit can be unlocked ... cannot be reverted ... RID Block Size ... 15,000")]
_tbl_good = ("## Premise check\n| # | User's claim | Corpus says | Verdict |\n|---|---|---|---|\n"
             "| 1 | RID Block Size to 50,000 | values above 15,000 are clamped | CORRECTED |\n"
             "| 2 | capped at 2^31 | default cap is 2^30; 2^31 only via irreversible unlock | CORRECTED |\n"
             "\nanswer prose [cite: ad-ds-managing-rid-issuance]")
_tbl_badverdict = _tbl_good.replace("| CORRECTED |\n| 2", "| WRONG-ISH |\n| 2")
_tbl_fabnum = _tbl_good.replace("default cap is 2^30", "default cap is 2^37")
_g_good = _plint.premise_gate(_tbl_good, _p4, _pg_cands, _S4)
_g_drop = _plint.premise_gate("prose only, model dropped the table [cite: x]", _p4, _pg_cands, _S4)
_g_bad = _plint.premise_gate(_tbl_badverdict, _p4, _pg_cands, _S4)
_g_fab = _plint.premise_gate(_tbl_fabnum, _p4, _pg_cands, _S4)
_c_gate = (_g_good == [] and {f["flag"] for f in _g_drop} == {"premise_unaddressed"}
           and len(_g_drop) == 2
           and any(f["flag"] == "premise_verdict_invalid" for f in _g_bad)
           and any(f["flag"] == "premise_correction_ungrounded"
                   and "2^37" in f.get("tokens", []) for f in _g_fab)
           and _plint.premise_gate("anything", [], _pg_cands, _S4) == [])
# plumbing: premise_flags surface in public_result; strict withholds ONLY on premise_unaddressed
_st_drop = {"answer": "x", "used": ["n1"], "grounding_fail": False, "ungrounded_identifiers": [],
            "premise_flags": [{"flag": "premise_unaddressed", "premise": "capped at 2^31"}]}
_st_inv = {"answer": "x", "used": ["n1"], "grounding_fail": False, "ungrounded_identifiers": [],
           "premise_flags": [{"flag": "premise_verdict_invalid", "premise": "p"}]}
_pr_d0 = _askmod.public_result("q", _st_drop, [], strict=False)
_pr_d1 = _askmod.public_result("q", _st_drop, [], strict=True)
_pr_i1 = _askmod.public_result("q", _st_inv, [], strict=True)
_c_plumb = (_pr_d0["withheld"] is False and _pr_d0["premise_flags"] == _st_drop["premise_flags"]
            and _pr_d1["withheld"] is True
            and _pr_i1["withheld"] is False and "premise_flags" in _pr_i1)
check("premise gate (session-4 dropout class): extraction fixtures 4/4, gate matrix "
      "(clean/drop/bad-verdict/fabricated-correction/empty), public_result plumbing + strict "
      "withhold on premise_unaddressed only",
      _c_fx and _c_gate and _c_plumb,
      f"fx={_c_fx} gate={_c_gate} plumb={_c_plumb} p4={[p['tokens'] for p in _p4]} "
      f"drop={_g_drop} bad={_g_bad} fab={_g_fab}")

# 48. lint H1-banner helper: has_out_of_coverage_banner is lenient on markdown decoration (blockquote
# or heading) but strict on content — the ⚠️ line must mention "coverage".
_plain_body = "# Title\n\nJust a normal paragraph, no banner here.\n"
_bq_body = "# Title\n\n> ⚠️ **Out of corpus coverage** — verify against the primary source.\n"
_heading_body = "# ⚠️ Out of corpus coverage\n\nBody text.\n"
check("lint.has_out_of_coverage_banner: false on plain body, true on blockquote/heading banner",
      not _lint.has_out_of_coverage_banner(_plain_body) and _lint.has_out_of_coverage_banner(_bq_body)
      and _lint.has_out_of_coverage_banner(_heading_body), "")

# 49. serve smoke: start `wikikb serve` on an ephemeral loopback port, poll /health up to ~5s, hit
# /ask, then SIGINT and expect the clean exit serve.main()'s try/except KeyboardInterrupt gives — all
# within 5s (kill + fail the check on timeout, never hang the suite).
import json as _json
import signal as _signal
import socket as _socket
import time as _time
import urllib.request as _urlreq

_srv_sock = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
_srv_sock.bind(("127.0.0.1", 0))
_srv_port = _srv_sock.getsockname()[1]
_srv_sock.close()
_srv = subprocess.Popen([PY, "-m", "wikikb", "serve", "--port", str(_srv_port)],
                        cwd=META, env=_ENV, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
_health_ok, _ask_ok, _exit_ok, _srv_detail = False, False, False, ""
try:
    _health = None
    _deadline = _time.time() + 5
    while _time.time() < _deadline and _health is None:
        try:
            with _urlreq.urlopen("http://127.0.0.1:%d/health" % _srv_port, timeout=0.5) as _r:
                _health = _json.loads(_r.read().decode())
        except Exception:
            _time.sleep(0.2)
    _health_ok = bool(_health) and _health.get("status") == "ok" and "keycloak" in (_health.get("domains") or [])
    if _health_ok:
        with _urlreq.urlopen(
                "http://127.0.0.1:%d/ask?q=how+do+I+enable+dpop&domain=keycloak" % _srv_port, timeout=10) as _r:
            _ask_obj = _json.loads(_r.read().decode())
            # WI-7: /ask returns the shared public_result shape — grounding always structured
            _ask_ok = all(k in _ask_obj for k in ("answer", "withheld", "ungrounded_identifiers"))
    _srv.send_signal(_signal.SIGINT)
    try:
        _exit_ok = _srv.wait(timeout=5) == 0
    except subprocess.TimeoutExpired:
        _srv.kill()
        _exit_ok = False
except Exception as _e:                                    # noqa: BLE001
    _srv_detail = "exception: %r" % _e
finally:
    if _srv.poll() is None:
        _srv.kill()
_srv_detail = _srv_detail or f"health_ok={_health_ok} ask_ok={_ask_ok} exit_ok={_exit_ok}"
check("serve smoke: /health ok+keycloak, /ask has answer, SIGINT -> clean exit 0",
      _health_ok and _ask_ok and _exit_ok, _srv_detail)

# 50. mcp smoke: spawn `wikikb mcp` over stdio pipes and run the JSON-RPC handshake (initialize ->
# notifications/initialized -> tools/list -> tools/call ask), then close stdin (EOF) and expect the
# clean exit main()'s plain `for line in sys.stdin` loop gives — all bounded by a select-based
# readline timeout so a hang never blocks the suite.
import selectors as _selectors


def _mcp_readline(proc, timeout=5):
    sel = _selectors.DefaultSelector()
    sel.register(proc.stdout, _selectors.EVENT_READ)
    ready = sel.select(timeout)
    sel.close()
    return proc.stdout.readline() if ready else None


_mcp = subprocess.Popen([PY, "-m", "wikikb", "mcp"], cwd=META, env=_ENV,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
_mcp_init_ok, _mcp_list_ok, _mcp_ask_ok, _mcp_exit_ok, _mcp_detail = False, False, False, False, ""
try:
    _mcp.stdin.write(_json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize"}) + "\n")
    _mcp.stdin.flush()
    _resp = _json.loads(_mcp_readline(_mcp) or "{}")
    _mcp_init_ok = _resp.get("result", {}).get("serverInfo", {}).get("name") == "wikikb"

    _mcp.stdin.write(_json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")
    _mcp.stdin.flush()

    _mcp.stdin.write(_json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}) + "\n")
    _mcp.stdin.flush()
    _resp = _json.loads(_mcp_readline(_mcp) or "{}")
    _mcp_list_ok = len(_resp.get("result", {}).get("tools", [])) == 4

    _mcp.stdin.write(_json.dumps({
        "jsonrpc": "2.0", "id": 3, "method": "tools/call",
        "params": {"name": "ask", "arguments": {"question": "how do I enable dpop", "domain": "keycloak"}},
    }) + "\n")
    _mcp.stdin.flush()
    _resp = _json.loads(_mcp_readline(_mcp, timeout=10) or "{}")
    _mcp_text = (_resp.get("result", {}).get("content") or [{}])[0].get("text", "")
    _mcp_ask_obj = _json.loads(_mcp_text or "{}")
    # WI-7: mcp ask returns the shared public_result shape — grounding always structured
    _mcp_ask_ok = all(k in _mcp_ask_obj for k in ("answer", "withheld", "ungrounded_identifiers"))

    _mcp.stdin.close()
    try:
        _mcp_exit_ok = _mcp.wait(timeout=5) == 0
    except subprocess.TimeoutExpired:
        _mcp.kill()
        _mcp_exit_ok = False
except Exception as _e:                                    # noqa: BLE001
    _mcp_detail = "exception: %r" % _e
finally:
    if _mcp.poll() is None:
        _mcp.kill()
_mcp_detail = _mcp_detail or (f"init_ok={_mcp_init_ok} list_ok={_mcp_list_ok} "
                               f"ask_ok={_mcp_ask_ok} exit_ok={_mcp_exit_ok}")
check("mcp smoke: initialize serverInfo.name=wikikb, tools/list has 4 tools, ask has answer, "
      "EOF -> clean exit 0",
      _mcp_init_ok and _mcp_list_ok and _mcp_ask_ok and _mcp_exit_ok, _mcp_detail)

# 51. Judge tier (advisory-only, Brief J): has_judge() is False by default (no model_judge configured /
# litellm absent here), and complete_routed(tier='judge') DEGRADES to the single-model complete() path
# (no crash) when only cheap/hard are configured — the Router has no 'judge' model group to route to,
# so router.completion(model='judge', ...) raises and is caught, falling back exactly like today. Fake
# litellm injected in-process (same style as the cite-parse check #47), restored in `finally`.
import types as _types
from wikikb.online import llm as _llm
_calls, _j_err = [], ""
_has_judge_default = None
_saved_litellm = sys.modules.get("litellm")
_saved_load_cfg = _llm.load_config
_saved_wiki_llm = os.environ.get("WIKI_LLM")
try:
    _has_judge_default = _llm.has_judge()      # real env: litellm absent -> False regardless of config

    _fake = _types.ModuleType("litellm")
    _fake.telemetry = True
    _fake.suppress_debug_info = False
    _fake.success_callback = []

    def _fake_completion(**kw):
        _calls.append(("single", kw))
        return type("R", (), {"choices": [type("C", (), {"message": type("M", (), {"content": "single"})()})()]})()
    _fake.completion = _fake_completion

    class _FakeRouter:
        def __init__(self, model_list, fallbacks, telemetry=False):
            self.groups = {m["model_name"] for m in model_list}

        def completion(self, model, messages, **kw):
            _calls.append(("routed", model))
            if model not in self.groups:
                raise ValueError("no model group %r" % model)
            return type("R", (), {"choices": [type("C", (), {
                "message": type("M", (), {"content": "routed-" + model})()})()]})()
    _fake.Router = _FakeRouter
    sys.modules["litellm"] = _fake
    os.environ["WIKI_LLM"] = "local"
    _llm.load_config = lambda: {"model": "ollama/x", "model_small": "ollama/s", "model_large": "ollama/l"}

    _resp = _llm.complete_routed([{"role": "user", "content": "x"}], tier="judge")
    _j_ok = (_resp is not None and _llm.text_of(_resp) == "single"
             and _calls[:1] == [("routed", "judge")] and len(_calls) == 2 and _calls[1][0] == "single")
except Exception as _e:                                                    # noqa: BLE001
    _j_ok = False
    _j_err = repr(_e)
finally:
    _llm.load_config = _saved_load_cfg
    if _saved_wiki_llm is None:
        os.environ.pop("WIKI_LLM", None)
    else:
        os.environ["WIKI_LLM"] = _saved_wiki_llm
    if _saved_litellm is None:
        sys.modules.pop("litellm", None)
    else:
        sys.modules["litellm"] = _saved_litellm
check("llm judge tier: has_judge() False by default; complete_routed(tier='judge') degrades to "
      "single-model complete() when no judge group exists (no crash)",
      _has_judge_default is False and _j_ok,
      _j_err or f"has_judge_default={_has_judge_default} calls={_calls}")

# NN. verify (self-healing core): the 2026-07-05 sizing-incident fixture MUST flag its wrong cached
# number as MISMATCH (exit 2), and the real, corrected page + full corpus must be MISMATCH-clean
# (exit 0). This is the wrong-cached-number regression net.
_vf = subprocess.run([PY, "-m", "wikikb", "verify", "--file",
                      os.path.join(META, "eval", "fixtures", "verify-sizing-incident.md")],
                     capture_output=True, text=True, cwd=META, env=_clean_env)
_vp = subprocess.run([PY, "-m", "wikikb", "verify", "--page", "rhbk-oscp-scaling-resources"],
                     capture_output=True, text=True, cwd=META, env=_clean_env)
check("verify: incident fixture -> MISMATCH exit 2; corrected sizing page -> exit 0",
      _vf.returncode == 2 and "MISMATCH" in _vf.stdout and "120" in _vf.stdout
      and _vp.returncode == 0,
      f"fixture rc={_vf.returncode} page rc={_vp.returncode}")

# NN. verify (FIX-A regression, 2026-07-05 audit): a claim hard-wrapped across a markdown line
# break ("The default" / "`terminationGracePeriodSeconds` is 30 seconds") must still bind — the
# claim's own physical line carried only ONE shared context token with the source, one short of
# the >=2 lenient-bind floor, until paragraph-joining (FIX C) restored the full sentence. Must be
# VERIFIED (grounded, exit 0), never UNGROUNDED/MISMATCH.
_vg = subprocess.run([PY, "-m", "wikikb", "verify", "--page",
                      "terminationgraceperiodseconds-zero-sigterm", "--json"],
                     capture_output=True, text=True, cwd=META, env=_clean_env)
try:
    _vg_j = _json.loads(_vg.stdout)
    _vg_ok = (_vg.returncode == 0 and _vg_j.get("verified", 0) >= 1
              and _vg_j.get("mismatch", 0) == 0)
except Exception:                                                          # noqa: BLE001
    _vg_ok = False
check("verify: cross-line-wrap claim (terminationGracePeriodSeconds:30s) binds -> VERIFIED",
      _vg_ok, f"rc={_vg.returncode} out={_vg.stdout[:200]}")

# NN. context truncation: every drop is explicit and machine-readable; tabular cuts retain their
# distinct incident marker, prose/skipped candidates use the generic marker, and all-fit bytes stay.
from wikikb.graph import nodes as _tnodes
_tbl = ("\n\n| Workload | Req/s | vCPU |\n|---|---|---|\n| Password login | 15 | 1 |\n"
        "| Client credential grant | 200 | 1 |\n")
_cut = _tbl.index("| Client credential grant | 200") + len("| Client credential grant | 20")
_tbody = "x" * (8000 - len("[n1]\n") - _cut) + _tbl
_tctx, _tids = _tnodes._assemble_context([("n1", _tbody)], return_truncated=True)
_tt1 = len(_tctx) <= _tnodes.CTX_CHARS
_tt2 = all(ln.rstrip().endswith("|") for ln in _tctx.splitlines() if ln.startswith("|"))
_tt3 = ("truncated mid-table" in _tctx and "context truncated — open" not in _tctx
        and "n1" in _tctx.splitlines()[-1] and _tids == ["n1"])
_tt4 = _tnodes._assemble_context([("n1", "alpha"), ("n2", "beta")]) == "[n1]\nalpha\n\n[n2]\nbeta"
_pctx, _pids = _tnodes._assemble_context([("prose-note", "prose line\n" * 100)], limit=180,
                                          return_truncated=True)
_tt5 = "[…context truncated — open prose-note for the full note]" in _pctx and _pids == ["prose-note"]
_sctx, _sids = _tnodes._assemble_context([("skipped-note", "x" * 500), ("kept-note", "ok")], limit=120,
                                          return_truncated=True)
_tt6 = "[…context truncated — open skipped-note for the full note]" in _sctx \
    and "[skipped-note]\n" not in _sctx and "[kept-note]\nok" in _sctx and _sids == ["skipped-note"]
_tsyn = _tnodes.synthesize_node({"query": "q", "candidates": [("prose-note", "prose line\n" * 1000)]})
_tt7 = _tsyn.get("truncated_ids") == ["prose-note"]
check("context truncation: table-specific marker, generic prose/skipped markers + ids, all-fit bytes",
      _tt1 and _tt2 and _tt3 and _tt4 and _tt5 and _tt6 and _tt7,
      f"t1={_tt1} t2={_tt2} t3={_tt3} t4={_tt4} t5={_tt5} t6={_tt6} t7={_tt7}")

# NN+1. Fair-share context budgeting (2026-07 audit fix — confirmed failure: a 47k-char rank-1 note
# starved out every other candidate, including the one holding the correct answer). Each candidate
# must now get SOME context before any one of them gets all of it.
_big_line = "context filler line with representative words and numbers 12345.\n"
_huge_body = _big_line * 700                             # far bigger than any fair share of 8000 chars
_small_fact = "THE ANSWER IS 42 (distinctive fact that must not be evicted)"
_fs_ctx = _tnodes._assemble_context([("big1", _huge_body), ("small2", _small_fact)])
_fs_small_present = "THE ANSWER IS 42" in _fs_ctx and "[small2]" in _fs_ctx
_fs_big_present = "[big1]" in _fs_ctx and _big_line in _fs_ctx    # rank-1 got SOME real content, not zero
_fs_capped = len(_fs_ctx) <= _tnodes.CTX_CHARS
check("fair-share context budgeting: a huge rank-1 note no longer evicts a smaller candidate",
      _fs_small_present and _fs_big_present and _fs_capped,
      f"len={len(_fs_ctx)} small={_fs_small_present} big={_fs_big_present}")

# NN. live-query bank (the acceptance gate raised 2026-07-05; regraded 2026-07-05 to grade the ANSWER
# TEXT ONLY, not answer+candidate-bodies — see wikikb/quality/livebank.py). Run OFFLINE (WIKI_LLM
# stripped by _clean_env), so every case hits the deterministic extractive fallback and has NO real
# model prose to grade a fact claim against: every case is expected to land UNGRADED, never PASS/FAIL
# on facts. What the offline run DOES still assert, unconditionally: exit 0, 100% of GATE checks
# passing (expect_gate is graded independently of fact-grading and a mismatch is always a FAIL), and
# zero graded-fact failures (a FAIL row whose gate_ok is True, i.e. the fact-grading path actually
# failed something — impossible offline unless a case's answer stopped being an extractive/withheld
# shape). UNGRADED is tolerated and reported explicitly, never counted as a pass.
from wikikb.quality import livebank as _lbmod
_lb = subprocess.run([PY, "-m", "wikikb", "livebank", "--ci", "--min-pass", "100", "--json"],
                     capture_output=True, text=True, cwd=META, env=_clean_env)
_lb_cases = len(_lbmod.load_cases())
import json as _json_lb
try:
    _lb_json = _json_lb.loads(_lb.stdout)
    _lb_results = _lb_json.get("results", [])
except Exception:
    _lb_json, _lb_results = {}, []
_lb_gate_ok = all(r.get("gate_ok") for r in _lb_results) if _lb_results else False
_lb_fact_fails = [r for r in _lb_results if r.get("outcome") == "FAIL" and r.get("gate_ok")]
_lb_n_ungraded = sum(1 for r in _lb_results if r.get("outcome") == "UNGRADED")
check("livebank: 24-case bank valid + ci subset offline -> exit 0, 100% GATE pass, zero graded-fact "
      "failures (UNGRADED tolerated + reported)",
      _lb.returncode == 0 and _lb_cases == 24 and bool(_lb_results) and _lb_gate_ok and not _lb_fact_fails,
      f"rc={_lb.returncode} cases={_lb_cases} n_results={len(_lb_results)} gate_ok={_lb_gate_ok} "
      f"fact_fails={[r['id'] for r in _lb_fact_fails]} ungraded={_lb_n_ungraded}")

# The same offline run must NOT satisfy the production fact-coverage floor: all cases are UNGRADED,
# so --min-graded 1 exits 4 even though vacuous --min-pass 100 and every gate check still pass.
_lb_floor = subprocess.run([PY, "-m", "wikikb", "livebank", "--ci", "--min-pass", "100",
                            "--min-graded", "1", "--json"],
                           capture_output=True, text=True, cwd=META, env=_clean_env)
try:
    _lb_floor_json = _json_lb.loads(_lb_floor.stdout)
except Exception:
    _lb_floor_json = {}
check("livebank: offline --min-graded 1 exits 4 (zero gradable facts cannot satisfy sign-off)",
      _lb_floor.returncode == 4 and _lb_floor_json.get("n_graded") == 0
      and _lb_floor_json.get("n_ungraded", 0) > 0,
      f"rc={_lb_floor.returncode} graded={_lb_floor_json.get('n_graded')} "
      f"ungraded={_lb_floor_json.get('n_ungraded')}")

# NN+1. grade300 completeness gate (WI-1, consensus 2026-07-12): a partial or malformed cohort must
# exit 2, a complete clean cohort 0, a complete cohort with a hard-gate (refusal) failure 1. Uses a
# 2-case synthetic minibank in a temp dir — grade300 is pure stdlib and fast, so this is cheap.
import json as _g3json
import tempfile as _g3tmp
_G3 = os.path.join(META, "eval", "grade300.py")
with _g3tmp.TemporaryDirectory() as _g3d:
    _g3cases = os.path.join(_g3d, "cases.jsonl")
    with open(_g3cases, "w", encoding="utf-8") as _fh:
        _fh.write(_g3json.dumps({"id": "t-001", "type": "lexical", "domain": "keycloak",
                                 "question": "q1", "expected_slugs": [], "gold_facts": []}) + "\n")
        _fh.write(_g3json.dumps({"id": "t-002", "type": "fabrication", "domain": "keycloak",
                                 "question": "q2", "fabricated_token": "KC_FAKE_VAR",
                                 "must_refuse": True, "expected_slugs": [], "gold_facts": []}) + "\n")
    def _g3run(rows):
        _ans = os.path.join(_g3d, "answers.jsonl")
        with open(_ans, "w", encoding="utf-8") as _fh:
            for r in rows:
                _fh.write(_g3json.dumps(r) + "\n")
        _p = subprocess.run([PY, _G3, "--cases", _g3cases, "--answers", _ans],
                            capture_output=True, text=True, cwd=META)
        return _p.returncode, _p.stdout + _p.stderr
    _REFUSE = "KC_FAKE_VAR does not exist in the corpus"
    _rc_empty, _ = _g3run([])                                                    # empty cohort
    _rc_partial, _ = _g3run([{"id": "t-001", "answer": "an answer"}])            # missing t-002
    _rc_runerr, _ = _g3run([{"id": "t-001", "answer": "an answer"},
                            {"id": "t-002", "answer": "[RUN-ERROR] timeout"}])   # sentinel != answer
    _rc_wsrunerr, _ = _g3run([{"id": "t-001", "answer": "an answer"},
                              {"id": "t-002", "answer": "   [RUN-ERROR] timeout"}])  # ws-prefixed sentinel
    _rc_null, _ = _g3run([{"id": "t-001", "answer": None},
                          {"id": "t-002", "answer": _REFUSE}])                   # null answer
    _rc_dup, _ = _g3run([{"id": "t-001", "answer": "x"}, {"id": "t-001", "answer": "y"},
                         {"id": "t-002", "answer": _REFUSE}])                    # duplicate id
    _rc_unknown, _ = _g3run([{"id": "t-001", "answer": "an answer"},
                             {"id": "t-002", "answer": _REFUSE},
                             {"id": "t-999", "answer": "stray"}])                # unknown id
    _rc_nonobj, _ = _g3run(["just a string", {"id": "t-001", "answer": "an answer"},
                            {"id": "t-002", "answer": _REFUSE}])                 # non-object row
    _rc_clean, _ = _g3run([{"id": "t-001", "answer": "an answer"},
                           {"id": "t-002", "answer": _REFUSE}])
    _rc_gate, _ = _g3run([{"id": "t-001", "answer": "an answer"},
                          {"id": "t-002", "answer": "KC_FAKE_VAR sets the fake variable."}])
check("grade300 exit taxonomy: empty/partial/[RUN-ERROR]/ws-sentinel/null/dup/unknown/non-object -> 2, "
      "complete+clean -> 0, refusal-fail -> 1",
      (_rc_empty, _rc_partial, _rc_runerr, _rc_wsrunerr, _rc_null, _rc_dup, _rc_unknown, _rc_nonobj,
       _rc_clean, _rc_gate) == (2, 2, 2, 2, 2, 2, 2, 2, 0, 1),
      f"empty={_rc_empty} partial={_rc_partial} runerr={_rc_runerr} ws={_rc_wsrunerr} null={_rc_null} "
      f"dup={_rc_dup} unknown={_rc_unknown} nonobj={_rc_nonobj} clean={_rc_clean} gatefail={_rc_gate}")

# NN+1a. WI-8 substitution bank grading is REPORT-ONLY: a complete cohort exits 0 even when every
# correction FAILS (rationalized answers), the scoreboard reports CORRECTED n/m, the _meta header
# row is skipped as a case, and corrected() is boundary-aware for substring real⊂fake pairs.
with _g3tmp.TemporaryDirectory() as _g3d:
    _sb_cases = os.path.join(_g3d, "cases-sub.jsonl")
    with open(_sb_cases, "w", encoding="utf-8") as _fh:
        _fh.write(_g3json.dumps({"_meta": True, "bank": "rationalized-substitution",
                                 "authorship": "same-family — NOT independent"}) + "\n")
        _fh.write(_g3json.dumps({"id": "s-001", "type": "substitution", "domain": "keycloak",
                                 "question": "q", "substituted_token": "KC_DATABASE_PASSWORD",
                                 "real_token": "KC_DB_PASSWORD", "expected_slugs": [],
                                 "gold_facts": [], "must_correct": True}) + "\n")
        _fh.write(_g3json.dumps({"id": "s-002", "type": "substitution", "domain": "active-directory",
                                 "question": "q", "substituted_token": "userAccountControlFlags",
                                 "real_token": "userAccountControl", "expected_slugs": [],
                                 "gold_facts": [], "must_correct": True}) + "\n")
    def _sbrun(rows):
        _ans = os.path.join(_g3d, "answers.jsonl")
        with open(_ans, "w", encoding="utf-8") as _fh:
            for r in rows:
                _fh.write(_g3json.dumps(r) + "\n")
        _p = subprocess.run([PY, _G3, "--cases", _sb_cases, "--answers", _ans],
                            capture_output=True, text=True, cwd=META)
        return _p.returncode, _p.stdout + _p.stderr
    # all rationalized (fake treated as real) -> STILL exit 0 (report-only), CORRECTED 0/2
    _rc_rat, _out_rat = _sbrun([
        {"id": "s-001", "answer": "KC_DATABASE_PASSWORD sets the DB password."},
        {"id": "s-002", "answer": "userAccountControlFlags is the bitmask you flip."}])
    # one true correction; s-002's answer echoes only the FAKE token — the substring real token
    # inside that echo must NOT be credited (boundary-awareness)
    _rc_mix, _out_mix = _sbrun([
        {"id": "s-001", "answer": "KC_DATABASE_PASSWORD does not exist; the real option is KC_DB_PASSWORD."},
        {"id": "s-002", "answer": "userAccountControlFlags does not exist in the corpus."}])
check("grade300 substitution bank (WI-8): report-only (all-rationalized still exit 0, CORRECTED 0/2), "
      "_meta header skipped, boundary-aware substring credit (CORRECTED 1/2 on mixed)",
      _rc_rat == 0 and "CORRECTED 0/2 (report-only)" in _out_rat
      and _rc_mix == 0 and "CORRECTED 1/2 (report-only)" in _out_mix,
      f"rat_rc={_rc_rat} mix_rc={_rc_mix} rat_line={[l for l in _out_rat.splitlines() if 'substitution' in l]} "
      f"mix_line={[l for l in _out_mix.splitlines() if 'substitution' in l]}")

# NN+1a2. corrected() identifier-boundary matrix (Codex review catches, WI-8 cycle 1): a fake that
# is a PREFIX of the real must not blank the real's occurrence (--proxy-header → --proxy-headers),
# a longer flag must not credit a shorter real (--dest-directory vs --dest-dir), and a
# sentence-ending period is a boundary while dots INSIDE spec.field tokens still match.
import importlib.util as _cu
_cspec = _cu.spec_from_file_location("_g3mod", _G3); _g3mod = _cu.module_from_spec(_cspec)
_cspec.loader.exec_module(_g3mod)
_contract_good = """## References\n### RH ground-truth\n- `ref:n`\n### Wiki\n- [[p]]"""
_contract_empty = """## References\n### RH ground-truth\n- No verified RH ground-truth source was cited.\n### Wiki\n- No synthesized Wiki page was used."""
_contract_leak = """## References\n- `ref:n` [[p]]"""
_contract_one = """## References\n### RH ground-truth\n- `ref:n`"""
check("grade300 contract: labeled evidence and explicit-empty groups pass; unlabeled leakage and "
      "missing group fail",
      _g3mod.contract(_contract_good) and _g3mod.contract(_contract_empty)
      and not _g3mod.contract(_contract_leak) and not _g3mod.contract(_contract_one), "")
_cm = [
    ("--proxy-header does not exist; use --proxy-headers", "--proxy-headers", "--proxy-header", True),
    ("--destination-dir does not exist; use --dest-directory please", "--dest-dir", "--destination-dir", False),
    ("KC_DATABASE_PASSWORD does not exist; the real option is KC_DB_PASSWORD.",
     "KC_DB_PASSWORD", "KC_DATABASE_PASSWORD", True),
    ("spec.serviceAccountIssuerURL does not exist; read spec.serviceAccountIssuer.",
     "spec.serviceAccountIssuer", "spec.serviceAccountIssuerURL", True),
    # asymmetric dot boundaries (Codex cycle-2 catches): dotted-path continuations never credit
    ("spec.serviceAccountIssuerURL does not exist; use status.spec.serviceAccountIssuer",
     "spec.serviceAccountIssuer", "spec.serviceAccountIssuerURL", False),
    ("spec.serviceAccountIssuerURL does not exist; use spec.serviceAccountIssuer.extra",
     "spec.serviceAccountIssuer", "spec.serviceAccountIssuerURL", False),
]
_cm_bad = [(a[:40], w, _g3mod.corrected(a, r, f)) for a, r, f, w in _cm if _g3mod.corrected(a, r, f) != w]
check("corrected() boundary matrix: fake-prefix-of-real credited, longer-flag not credited, "
      "sentence period is a boundary, dotted tokens match", not _cm_bad, f"bad={_cm_bad}")

# NN+1b. run300 cohort identity (WI-3): zero-work runs still establish a complete cohort on disk;
# resume refuses foreign row stamps, malformed manifests, and --new-run/--overwrite conflicts;
# grade300 treats a non-string run_id as MALFORMED. All with --limit 0, so no model is invoked.
_R3 = os.path.join(META, "eval", "run300.py")
with _g3tmp.TemporaryDirectory() as _r3d:
    _r3cases = os.path.join(_r3d, "cases.jsonl")
    with open(_r3cases, "w", encoding="utf-8") as _fh:
        _fh.write(_g3json.dumps({"id": "t-001", "type": "lexical", "domain": "keycloak",
                                 "question": "q1", "expected_slugs": [], "gold_facts": []}) + "\n")
    _r3a = os.path.join(_r3d, "a.jsonl")
    def _r3run(*extra):
        _p = subprocess.run([PY, _R3, "--cases", _r3cases, "--answers", _r3a, "--model", "m-A",
                             "--limit", "0", "--allow-dirty", *extra],
                            capture_output=True, text=True, cwd=META)
        return _p.returncode
    _rc_new = _r3run()                                           # establish cohort, zero work
    _r3_file_exists = os.path.isfile(_r3a)                       # answers file must exist already
    _rc_resume = _r3run()                                        # clean resume
    with open(_r3a, "a", encoding="utf-8") as _fh:               # a row stamped by a STRANGER run
        _fh.write(_g3json.dumps({"id": "t-001", "answer": "x", "run_id": "stranger", "model": "m-A"}) + "\n")
    _rc_stranger = _r3run()
    os.unlink(_r3a); open(_r3a, "w").close()
    with open(_r3a + ".manifest.json", "w", encoding="utf-8") as _fh:
        _fh.write("{not json")                                   # corrupt manifest
    _rc_badman = _r3run()
    _rc_conflict = _r3run("--new-run", "--overwrite")            # mutually exclusive flags
    # grade300: non-string run_id is malformed, not a crash
    _r3g = os.path.join(_r3d, "g.jsonl")
    with open(_r3g, "w", encoding="utf-8") as _fh:
        _fh.write(_g3json.dumps({"id": "t-001", "answer": "an answer", "run_id": 42}) + "\n")
    _rc_intrid = subprocess.run([PY, _G3, "--cases", _r3cases, "--answers", _r3g],
                                capture_output=True, text=True, cwd=META).returncode
check("run300 cohort identity: zero-work establishes file, clean resume, stranger-row/bad-manifest "
      "refusals, flag conflict, grade300 non-string run_id -> (0,True,0,2,2,2,2)",
      (_rc_new, _r3_file_exists, _rc_resume, _rc_stranger, _rc_badman, _rc_conflict, _rc_intrid)
      == (0, True, 0, 2, 2, 2, 2),
      f"new={_rc_new} exists={_r3_file_exists} resume={_rc_resume} stranger={_rc_stranger} "
      f"badman={_rc_badman} conflict={_rc_conflict} intrid={_rc_intrid}")

# NN+2. the committed legacy cohort is explicitly incomplete — grading it must exit 2, never 0.
_leg = os.path.join(META, "eval", "answers300-partial-legacy.jsonl")
_p = subprocess.run([PY, _G3, "--cases", os.path.join(META, "eval", "cases300.jsonl"),
                     "--answers", _leg], capture_output=True, text=True, cwd=META)
check("grade300 legacy partial cohort (137/300) exits 2 (incomplete), scoreboard still prints",
      os.path.isfile(_leg) and _p.returncode == 2 and "INCOMPLETE" in _p.stdout and "answered" in _p.stdout,
      f"rc={_p.returncode}")

failed = [n for n, ok, _ in checks if not ok]
print(f"\n{len(checks) - len(failed)}/{len(checks)} checks passed")
sys.exit(1 if failed else 0)
