#!/usr/bin/env python3
"""domains_probe.py — behaviour probe for the domain-declaration CRUD (wikikb/build/domains.py and
the /domains HTTP surface). stdlib only, NO network beyond loopback.

It never touches the live vault: every case runs against a TEMP vault created by
`WIKIKB_VAULT_ROOT` + `wikikb bootstrap`, so a failure here can't leave a half-declared domain in
the real taxonomy.

What it covers, and why each case earns its place:

  A. Round-trip through ALL FOUR EXISTING READERS. domains.py is the write side of a file that
     tags.load_domains / route._domain_areas / coverage.load_tiers_covered / index.domain_meta each
     parse independently, with their own regexes and — critically — two different ideas of where a
     domain's NAME comes from (coverage keys off the `### heading`, the rest off `- domain:`). A
     block any one of them stops seeing is a domain that lints but cannot route, or routes but has
     no coverage tier and so silently never fires the gate's H1 arm. This is the case that fails if
     the emitted shape ever drifts.
  B. The file itself: add-then-remove is BYTE-IDENTICAL (so the operation is reversible, not
     approximately reversible), CRLF is preserved (the vault is edited in Obsidian on Windows),
     trailing `#` comments survive an unrelated patch (several of them carry the justification for a
     domain's coverage tier), and a no-op patch does not rewrite the file.
  C. The rules: the NAME is not patchable, an unknown area is refused rather than invented, an
     undescribed new area is refused, an unknown tier/shape is refused, a duplicate is refused.
  D. Removal safety: it REFUSES while pages still declare the domain, and even forced it deletes no
     page and no immutable note.
  E. The HTTP surface over a real loopback socket: reads are open, writes are hidden behind
     --allow-upload with the same unfingerprintable 404 the rest of the write surface uses, and the
     status codes mean what they say (201/200/404/409).

Usage:  python3 wiki/_meta/tests/domains_probe.py
Exit code: 0 = all pass, 1 = a case failed, 2 = a server never came up.
"""
import http.client
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
sys.path.insert(0, META)  # test bootstrap: make `import wikikb` importable

VAULT = tempfile.mkdtemp(prefix="wikikb-domains-probe-")
os.environ["WIKIKB_VAULT_ROOT"] = VAULT                 # BEFORE importing wikikb.paths
os.environ["WIKIKB_MODE"] = "airgapped"                 # the surface is mode-independent; pin it anyway

from wikikb import bootstrap                            # noqa: E402
from wikikb import paths                                # noqa: E402
from wikikb.build import domains                        # noqa: E402

PY = sys.executable
ENV = {**os.environ, "PYTHONPATH": META + os.pathsep + os.environ.get("PYTHONPATH", "")}
DOM = "probe-tech"
AREAS = {"probe-alpha": "the first probe area — widgets, gadgets and their configuration",
         "probe-beta": "the second probe area — probe transport and probe routing"}

checks = []


def check(name, ok, detail=""):
    checks.append(bool(ok))
    print("  %s  %s%s" % ("PASS" if ok else "FAIL", name, "" if ok else "\n        -> %s" % detail))


def seed():
    bootstrap.ensure_startup(label="domains_probe")
    return str(paths.TAXONOMY)


# --- A. the four readers --------------------------------------------------------------------------

def case_readers(tax):
    print("\nA. every existing taxonomy reader sees a domain written by domains.py")
    domains.add(DOM, list(AREAS), shape="corpus-backed",
                tiers_covered=["conceptual", "support-kb"],
                new_areas=AREAS, path=tax)

    from wikikb.build import tags
    from wikikb.quality import coverage
    from wikikb.retrieval import route
    from wikikb.build import index as indexmod

    check("tags.load_domains() (what lint validates every page's domain: against)",
          DOM in tags.load_domains(tax), sorted(tags.load_domains(tax)))
    check("route._domain_areas() (the router's keyword profile)",
          route._domain_areas(tax).get(DOM) == list(AREAS), route._domain_areas(tax).get(DOM))
    check("coverage.load_tiers_covered() (the Confidence gate's H1 arm — keys off the ### heading)",
          coverage.load_tiers_covered(tax).get(DOM) == ["conceptual", "support-kb"],
          coverage.load_tiers_covered(tax).get(DOM))
    indexmod.TAXONOMY = tax                        # module-level path; the only reader without a param
    meta = indexmod.domain_meta().get(DOM) or {}
    check("index.domain_meta() (shape + review-moc for the generated per-domain index)",
          meta.get("shape") == "corpus-backed"
          and meta.get("review-moc") == "%s-implementation-review" % DOM, meta)
    check("the ### heading and the `- domain:` line agree (a mismatch is a domain the gate can't see)",
          not domains.get(DOM, tax).get("header_mismatch"))
    check("the raw tier was created (_sources/<domain>/ — where uploads and scrapes land)",
          os.path.isdir(os.path.join(VAULT, "_sources", DOM)))
    check("no page, no index and no reference note was invented",
          not os.path.exists(os.path.join(VAULT, "index.%s.md" % DOM))
          and not os.listdir(os.path.join(VAULT, "topics")))


# --- B. the file ----------------------------------------------------------------------------------

def case_file(tax):
    print("\nB. the taxonomy file")
    crlf_tax = os.path.join(VAULT, "crlf-taxonomy.md")
    with open(tax, encoding="utf-8") as fh:
        body = fh.read()
    with open(crlf_tax, "w", encoding="utf-8", newline="") as fh:
        fh.write(body.replace("\n", "\r\n"))
    before = open(crlf_tax, "rb").read()
    domains.add("probe-temp", ["probe-alpha"], path=crlf_tax)
    mid = open(crlf_tax, "rb").read()
    check("CRLF is preserved (the vault is hand-edited in Obsidian on Windows)",
          mid.count(b"\r\n") == mid.count(b"\n") and mid.count(b"\r\n") > before.count(b"\r\n"))
    domains.remove("probe-temp", path=crlf_tax, force=True)
    check("add then remove leaves the file BYTE-IDENTICAL (the operation is really reversible)",
          open(crlf_tax, "rb").read() == before)

    # a trailing `# …` comment on a field is the recorded REASON for a coverage decision
    with open(tax, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    for i, line in enumerate(lines):
        if line.startswith("- tiers-covered:") and DOM in "\n".join(lines[max(0, i - 6):i]):
            lines[i] = line + "   # NOTHING INGESTED YET — keep conceptual until real content lands"
            break
    with open(tax, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    domains.update(DOM, path=tax, shape="notes-first")
    kept = (domains.get(DOM, tax).get("comments") or {}).get("tiers-covered")
    check("an unrelated patch PRESERVES a field's trailing comment (it justifies a gate decision)",
          kept and "NOTHING INGESTED YET" in kept, kept)

    mtime = os.path.getmtime(tax)
    time.sleep(0.02)
    _, changed = domains.update(DOM, path=tax, shape="notes-first")
    check("a no-op patch reports changed:[] and does NOT rewrite the file",
          changed == [] and os.path.getmtime(tax) == mtime, "changed=%s" % changed)


# --- C. the rules ---------------------------------------------------------------------------------

def case_rules(tax):
    print("\nC. what is refused, and why")

    def refuses(label, fn, needle=None):
        try:
            fn()
            check(label, False, "accepted")
        except domains.DomainError as e:
            check(label, needle is None or needle in str(e), str(e))

    refuses("the NAME is not patchable (it is every page's domain: and reference/<name>/)",
            lambda: domains.update(DOM, path=tax, domain="something-else"), "identity")
    refuses("a duplicate declaration is refused",
            lambda: domains.add(DOM, ["probe-alpha"], path=tax), "already declared")
    refuses("an area outside the flat ## Areas union is refused, not invented",
            lambda: domains.add("probe-x", ["no-such-area"], path=tax), "not in the `## Areas`")
    refuses("a new area with no description is refused (an undescribed area routes nothing)",
            lambda: domains.add("probe-x", ["probe-gamma"],
                                new_areas=[{"area": "probe-gamma"}], path=tax), "description")
    refuses("an unknown coverage tier is refused (the gate's vocabulary is fixed)",
            lambda: domains.add("probe-x", ["probe-alpha"], tiers_covered=["everything"], path=tax))
    refuses("an unknown shape is refused",
            lambda: domains.add("probe-x", ["probe-alpha"], shape="whatever", path=tax))
    refuses("a single-letter name is refused (coverage.py's regex needs 2+ chars — the strictest reader wins)",
            lambda: domains.add("x", ["probe-alpha"], path=tax))
    refuses("an unknown patch field is named rather than silently ignored",
            lambda: domains.update(DOM, path=tax, tears_covered=["conceptual"]), "not updatable")
    refuses("patching a domain that does not exist",
            lambda: domains.update("probe-absent", path=tax, shape="notes-first"), "no such domain")


# --- D. removal safety ----------------------------------------------------------------------------

def case_removal(tax):
    print("\nD. removal never deletes knowledge")
    page = os.path.join(VAULT, "topics", "probe-overview.md")
    with open(page, "w", encoding="utf-8") as fh:
        fh.write("---\ntitle: Probe overview\ntype: topic\ndomain: %s\nslug: probe-overview\n"
                 "summary: probe\nstatus: draft\n---\n\n# Probe overview\n" % DOM)
    ref = os.path.join(VAULT, "reference", DOM)
    os.makedirs(ref, exist_ok=True)
    note = os.path.join(ref, "probe-note.md")
    with open(note, "w", encoding="utf-8") as fh:
        fh.write("# immutable ground truth\n")

    try:
        domains.remove(DOM, path=tax)
        check("removal REFUSES while pages still declare the domain", False, "removed anyway")
    except domains.DomainError as e:
        check("removal REFUSES while pages still declare the domain (they would all fail lint)",
              "still in use" in str(e), str(e))

    entry = domains.remove(DOM, path=tax, force=True)
    check("forced removal drops the declaration", domains.get(DOM, tax) is None)
    check("...but keeps the page (withdrawing knowledge is Operation: RETRACT, not a config edit)",
          os.path.isfile(page))
    check("...and keeps the immutable reference note", os.path.isfile(note))
    check("...and reports what it kept", ref in (entry.get("kept") or []), entry.get("kept"))
    os.remove(page)


# --- E. the HTTP surface --------------------------------------------------------------------------

def free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def req(port, method, path, body=None, timeout=10):
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    try:
        raw = json.dumps(body).encode() if body is not None else None
        conn.request(method, path, body=raw,
                     headers={"Content-Type": "application/json"} if raw else {})
        r = conn.getresponse()
        data = r.read()
        try:
            return r.status, json.loads(data)
        except ValueError:
            return r.status, data
    finally:
        conn.close()


def start_server(port, allow_upload):
    args = [PY, "-m", "wikikb", "serve", "--port", str(port)]
    if allow_upload:
        args.append("--allow-upload")
    proc = subprocess.Popen(args, cwd=META, env=ENV, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True)
    deadline = time.time() + 8
    while time.time() < deadline:
        try:
            if req(port, "GET", "/health", timeout=0.5)[0] == 200:
                return proc
        except OSError:
            time.sleep(0.2)
    stop_server(proc)
    print("server on port %d never came up" % port)
    sys.exit(2)


def stop_server(proc):
    if proc.poll() is None:
        try:
            proc.send_signal(signal.SIGINT)
        except (ValueError, OSError, AttributeError):
            proc.terminate()          # Windows Popen.send_signal rejects SIGINT (see upload_probe)
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


def case_http_readonly():
    print("\nE1. HTTP without --allow-upload: reads open, writes unfingerprintable")
    port = free_port()
    proc = start_server(port, allow_upload=False)
    try:
        status, body = req(port, "GET", "/domains")
        check("GET /domains is open (a read changes nothing)",
              status == 200 and isinstance(body.get("domains"), list), "%s %s" % (status, body))
        unknown = req(port, "GET", "/no-such-path")
        for method, path, payload in (("POST", "/domains", {"domain": "probe-http", "areas": ["probe-alpha"]}),
                                      ("PATCH", "/domains/probe-http", {"shape": "notes-first"}),
                                      ("DELETE", "/domains/probe-http", None)):
            got = req(port, method, path, payload)
            check("%s %s is byte-identical to an unknown path when uploads are off"
                  % (method, path), got == unknown, "%s vs %s" % (got, unknown))
    finally:
        stop_server(proc)


def case_http_write():
    print("\nE2. HTTP with --allow-upload: the CRUD")
    port = free_port()
    proc = start_server(port, allow_upload=True)
    name = "probe-http"
    try:
        status, body = req(port, "POST", "/domains",
                           {"domain": name, "areas": ["probe-alpha", "probe-gamma"],
                            "shape": "notes-first", "tiers-covered": ["conceptual"],
                            "new_areas": {"probe-gamma": "a third probe area — probe storage"}})
        check("POST /domains -> 201 with the stored declaration",
              status == 201 and body.get("added", {}).get("domain") == name, "%s %s" % (status, body))
        status, body = req(port, "GET", "/health")
        check("the new domain shows up in GET /health immediately (no restart)",
              name in (body.get("domains") or []), body.get("domains"))
        status, body = req(port, "GET", "/domains/" + name)
        check("GET /domains/<name> returns it with a usage block",
              status == 200 and body["usage"]["pages"] == 0, "%s %s" % (status, body))
        status, body = req(port, "POST", "/domains", {"domain": name, "areas": ["probe-alpha"]})
        check("a duplicate POST -> 409 Conflict", status == 409, "%s %s" % (status, body))
        status, body = req(port, "PATCH", "/domains/" + name, {"tiers-covered": ["conceptual", "scenarios"]})
        check("PATCH is partial and reports what moved",
              status == 200 and body["changed"] == ["tiers-covered"]
              and body["updated"]["shape"] == "notes-first", "%s %s" % (status, body))
        status, body = req(port, "PATCH", "/domains/" + name, {"tiers-covered": ["conceptual", "scenarios"]})
        check("a no-op PATCH -> changed:[] with an explicit note",
              status == 200 and body["changed"] == [] and "note" in body, body)
        status, body = req(port, "PATCH", "/domains/" + name, {"domain": "renamed"})
        check("PATCH cannot rename (the name is identity) -> 400 with the reason",
              status == 400 and "identity" in body.get("error", ""), "%s %s" % (status, body))
        status, body = req(port, "PATCH", "/domains/probe-absent", {"shape": "notes-first"})
        check("PATCH on an undeclared domain -> 404", status == 404, "%s %s" % (status, body))
        # domains.update()'s signature takes the taxonomy FILE as `path`; the handler must not let a
        # request body reach it, or a caller could redirect the write to any file the process opens.
        escape = os.path.join(VAULT, "escaped.md")
        status, body = req(port, "PATCH", "/domains/" + name,
                           {"path": escape, "shape": "corpus-backed"})
        check("a body key that collides with the writer's `path` parameter is refused by name",
              status == 400 and "path" in body.get("error", "") and not os.path.exists(escape),
              "%s %s" % (status, body))
        status, body = req(port, "DELETE", "/domains/" + name)
        check("DELETE -> 200, and says what it kept",
              status == 200 and body.get("removed", {}).get("domain") == name and "note" in body,
              "%s %s" % (status, body))
        status, body = req(port, "GET", "/domains/" + name)
        check("...and it is gone", status == 404, "%s %s" % (status, body))
        status, body = req(port, "GET", "/openapi.json")
        paths_ = (body or {}).get("paths", {})
        check("/openapi.json documents the surface it actually serves",
              "/domains" in paths_ and "/domains/{domain}" in paths_
              and set(paths_["/domains/{domain}"]) == {"get", "patch", "delete"},
              sorted(paths_.get("/domains/{domain}", {})))
    finally:
        stop_server(proc)


def main():
    print("=" * 78)
    print("DOMAINS PROBE — CRUD over vault/taxonomy.md  (temp vault: %s)" % VAULT)
    print("=" * 78)
    try:
        tax = seed()
        case_readers(tax)
        case_file(tax)
        case_rules(tax)
        case_removal(tax)
        case_http_readonly()
        case_http_write()
    finally:
        shutil.rmtree(VAULT, ignore_errors=True)
    failed = len(checks) - sum(checks)
    print("-" * 78)
    print("%d/%d passed%s" % (sum(checks), len(checks), "" if not failed else "  — FAILURES ABOVE"))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
