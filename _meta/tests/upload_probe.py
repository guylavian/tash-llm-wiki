#!/usr/bin/env python3
"""upload_probe.py — behaviour probe for PUT /upload/<domain>/<filename> (serve.py). stdlib only,
no network (loopback only).

WHY: the trust-boundary checklist (CLAUDE.md, PLAN-graphify-pdf-upload.md Phase 2) lives entirely
inside do_PUT/do_upload; this drives the REAL server over a REAL loopback socket (not the do_upload
function in isolation), so what's asserted is the actual HTTP framing — status codes, Content-Length
handling, connection lifecycle — not a mock of it. Mirrors selftest.py's #49 "serve smoke" pattern
(ephemeral port, poll /health, SIGINT -> clean exit) but as its own script since it needs two server
instances (disabled vs --allow-upload) and http.client (not urllib) for raw, unnormalized request paths.

Two servers, spawned in turn on ephemeral loopback ports:
  1. WITHOUT --allow-upload  — PUT must be byte-identical (status + body) to an unknown GET path, so
     a disabled upload surface is unfingerprintable (a conditional do_PUT would leak a stdlib 501).
  2. WITH --allow-upload     — happy-path store, traversal-path rejection, oversize-Content-Length
     rejection (must not hang), non-%PDF-body rejection (415), duplicate-upload rejection (409).

Any file this probe stores under _sources/keycloak/_raw/pdfs/ is removed in a `finally` — the raw
tier is immutable ground truth, so a stray probe artifact left behind would violate that.

Usage:  python3 wiki/_meta/tests/upload_probe.py
Exit code: 0 = all pass, 1 = a case failed, 2 = a server never came up.
"""
import http.client
import json
import os
import signal
import socket
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))      # _meta/tests
META = os.path.dirname(HERE)                            # _meta
sys.path.insert(0, META)  # test bootstrap: make `import wikikb` importable
# WIKI comes from wikikb.paths — the ONE definition. Re-deriving it here as
# `os.path.dirname(META)` silently broke when content moved under <repo>/vault/ (2026-08-05),
# and it also ignored WIKIKB_VAULT_ROOT, so a sandboxed run probed the live tree.
from wikikb import paths as _paths  # noqa: E402 — must follow the sys.path bootstrap
WIKI = str(_paths.WIKI)
PY = sys.executable
ENV = {**os.environ, "PYTHONPATH": META + os.pathsep + os.environ.get("PYTHONPATH", "")}

PROBE_DOMAIN = "keycloak"                               # declared in taxonomy.md, corpus-backed but
                                                         # the _raw/ drop convention is domain-shape-agnostic
PROBE_NAME = "zz-upload-probe-%d.pdf" % os.getpid()     # unique per run; never collides with a real drop
PROBE_DIR = os.path.join(WIKI, "_sources", PROBE_DOMAIN, "_raw", "pdfs")
PROBE_PATH = os.path.join(PROBE_DIR, PROBE_NAME)
PDF_BYTES = b"%PDF-1.4\n%% upload_probe.py fixture\n"

checks = []


def check(name, ok, detail=""):
    checks.append((name, ok))
    print("  %s  %s%s" % ("PASS" if ok else "FAIL", name, ("  — " + detail) if detail and not ok else ""))


def free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def raw_request(port, method, path, body=None, headers=None, timeout=5):
    """http.client, not urllib — it sends `path` on the wire EXACTLY as given, with no ../ or
    percent-decoding normalization, so a traversal attempt reaches the server unmangled."""
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    try:
        conn.request(method, path, body=body, headers=headers or {})
        r = conn.getresponse()
        return r.status, r.read()
    finally:
        conn.close()


def start_server(port, allow_upload):
    args = [PY, "-m", "wikikb", "serve", "--port", str(port)]
    if allow_upload:
        args.append("--allow-upload")
    proc = subprocess.Popen(args, cwd=META, env=ENV, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    deadline = time.time() + 5
    up = False
    while time.time() < deadline and not up:
        try:
            status, _ = raw_request(port, "GET", "/health", timeout=0.5)
            up = status == 200
        except OSError:
            time.sleep(0.2)
    if not up:
        stop_server(proc)
        print("server on port %d never came up" % port)
        sys.exit(2)
    return proc


def stop_server(proc):
    if proc.poll() is None:
        proc.send_signal(signal.SIGINT)
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()


def cleanup():
    try:
        if os.path.isfile(PROBE_PATH):
            os.remove(PROBE_PATH)
    except OSError:
        pass
    # Only remove pdfs/ and _raw/ if THIS probe emptied them out again — never touch
    # _sources/<domain>/ itself (pre-existing, may hold real hand-authored notes).
    for d in (PROBE_DIR, os.path.dirname(PROBE_DIR)):
        try:
            if os.path.isdir(d) and not os.listdir(d):
                os.rmdir(d)
        except OSError:
            pass


def run_disabled():
    port = free_port()
    proc = start_server(port, allow_upload=False)
    try:
        put_status, put_body = raw_request(port, "PUT", "/upload/%s/x.pdf" % PROBE_DOMAIN, body=PDF_BYTES)
        get_status, get_body = raw_request(port, "GET", "/no-such-path")
        check("disabled server: PUT /upload byte-identical (status+body) to an unknown GET path",
              put_status == get_status == 404 and put_body == get_body,
              "put=(%s,%r) get=(%s,%r)" % (put_status, put_body, get_status, get_body))
    finally:
        stop_server(proc)


def run_enabled():
    port = free_port()
    proc = start_server(port, allow_upload=True)
    try:
        # happy path
        status, data = raw_request(port, "PUT", "/upload/%s/%s" % (PROBE_DOMAIN, PROBE_NAME), body=PDF_BYTES)
        obj = json.loads(data) if status == 201 else {}
        stored_ok = obj.get("stored") == os.path.relpath(PROBE_PATH, WIKI) and "next" in obj
        on_disk = os.path.isfile(PROBE_PATH) and open(PROBE_PATH, "rb").read() == PDF_BYTES
        check("happy path: 201 + stored/next, file lands under _sources/<domain>/_raw/pdfs/",
              status == 201 and stored_ok and on_disk, "status=%s body=%r on_disk=%s" % (status, data, on_disk))

        # traversal path rejected — raw ".." in the request-target, never normalized by http.client,
        # so UPLOAD_RE simply fails to match (its groups exclude "/") and it falls into the same
        # hidden 404 as the disabled case; nothing is ever written outside _sources/.
        status, data = raw_request(port, "PUT", "/upload/%s/../../etc/passwd.pdf" % PROBE_DOMAIN, body=PDF_BYTES)
        check("traversal path rejected (unmatched -> hidden 404, no write)",
              status == 404, "status=%s body=%r" % (status, data))

        # oversize Content-Length rejected WITHOUT hanging — declare > the 50 MB cap but only send a
        # few real bytes; the server must 413 off the header alone, never blocking on rfile.read().
        t0 = time.time()
        status, data = raw_request(port, "PUT", "/upload/%s/oversize-probe.pdf" % PROBE_DOMAIN, body=b"tiny",
                                   headers={"Content-Length": str(50 * 1024 * 1024 + 1)})
        elapsed = time.time() - t0
        check("oversize Content-Length -> 413, no hang",
              status == 413 and elapsed < 4.0, "status=%s elapsed=%.2fs body=%r" % (status, elapsed, data))

        # non-%PDF body rejected
        status, data = raw_request(port, "PUT", "/upload/%s/not-a-pdf-probe.pdf" % PROBE_DOMAIN, body=b"hello world")
        check("non-%PDF body -> 415", status == 415, "status=%s body=%r" % (status, data))

        # duplicate upload rejected — same filename as the happy-path upload above, O_EXCL -> 409
        status, data = raw_request(port, "PUT", "/upload/%s/%s" % (PROBE_DOMAIN, PROBE_NAME), body=PDF_BYTES)
        check("duplicate upload -> 409, no overwrite", status == 409, "status=%s body=%r" % (status, data))
    finally:
        stop_server(proc)


def main():
    print("=" * 70)
    print("UPLOAD PROBE — PUT /upload/<domain>/<filename>  (probe file: %s)" % PROBE_NAME)
    print("=" * 70)
    try:
        run_disabled()
        run_enabled()
    finally:
        cleanup()
    failed = [n for n, ok in checks if not ok]
    print("-" * 70)
    print("%d/%d passed%s" % (len(checks) - len(failed), len(checks), "" if not failed else "  — FAILURES ABOVE"))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
