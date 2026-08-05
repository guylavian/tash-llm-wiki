#!/usr/bin/env python3
"""mode_probe.py — behaviour probe for the two OPERATION MODES and the background job runner.
stdlib only, no network (loopback only).

WHY: `WIKIKB_MODE` decides a security posture (whether an outbound-capable surface exists at all),
and posture claims that are only asserted in a docstring rot. This drives the REAL server over a
REAL loopback socket — the same pattern as upload_probe.py — so what is checked is the wire
behaviour, not a function in isolation.

Cases:
  A. airgapped (the default, nothing set)
     - /health reports mode=airgapped and capabilities.scrape=false
     - POST /scrape and GET /scrape/sources are BYTE-IDENTICAL to an unknown path, so an
       online-only surface is not fingerprintable on a sealed box
     - /openapi.json does not document /scrape (a spec that lists an endpoint answering "unknown
       path" would be a lying spec)
     - the write surface (/upload, /ingest) is a hidden 404 while --allow-upload is off
  B. online
     - /health reports mode=online and capabilities.scrape=true
     - the scrape paths now EXIST and answer 501 (the declared, not-yet-implemented seam)
     - /openapi.json documents them
  C. an unknown WIKIKB_MODE REFUSES TO START (exit 2) instead of falling back to a default
  D. the jobs surface: list shape, malformed id -> 400, unknown id -> 404
  E. the runner itself, in-process: FIFO execution, done/failed transitions with a captured log
     tail, and the coalescing rule

DELIBERATELY NOT TESTED HERE: an end-to-end ingest. Running the real chain would write to
corpora/, rewrite vault/reference/<domain>/ and regenerate the whole link graph — a probe must not
mutate the vault. Case E covers the runner with harmless READ-ONLY steps; case A/B/D cover the
HTTP surface; the chain's own three commands are covered by their own tools' dry-run paths.

Usage:  python3 wiki/_meta/tests/mode_probe.py
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

from wikikb import modes                       # noqa: E402 — must follow the sys.path bootstrap
from wikikb.serve import jobs as jobsmod       # noqa: E402

PY = sys.executable
ENV = {**os.environ, "PYTHONPATH": META + os.pathsep + os.environ.get("PYTHONPATH", ""),
       "PYTHONIOENCODING": "utf-8"}
ENV.pop("WIKIKB_MODE", None)                    # a mode inherited from the operator's shell would
                                                # silently invert case A; each case sets its own

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


def raw_request(port, method, path, body=None, headers=None, timeout=10):
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    try:
        hdrs = dict(headers or {})
        if body is not None and "Content-Length" not in hdrs:
            hdrs["Content-Length"] = str(len(body))
        conn.request(method, path, body=body, headers=hdrs)
        r = conn.getresponse()
        return r.status, r.read()
    finally:
        conn.close()


def start_server(port, mode=None, allow_upload=False, extra_env=None):
    env = dict(ENV)
    if mode is not None:
        env["WIKIKB_MODE"] = mode
    env.update(extra_env or {})
    args = [PY, "-m", "wikikb", "serve", "--port", str(port)]
    if allow_upload:
        args.append("--allow-upload")
    proc = subprocess.Popen(args, cwd=META, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)
    deadline = time.time() + 20
    up = False
    while time.time() < deadline and not up:
        if proc.poll() is not None:                     # died on startup — caller decides if that
            return proc                                  # is the expected outcome (case C)
        try:
            up = raw_request(port, "GET", "/health", timeout=1)[0] == 200
        except OSError:
            time.sleep(0.2)
    if not up:
        stop_server(proc)
        print("server on port %d never came up" % port)
        sys.exit(2)
    return proc


def stop_server(proc):
    """SIGINT where it exists (serve.py catches KeyboardInterrupt and closes the socket cleanly),
    terminate() elsewhere. Popen.send_signal on Windows accepts only SIGTERM/CTRL_*_EVENT and
    raises ValueError for SIGINT, so the fallback is what makes this probe runnable on the
    developer machine as well as in the Linux image."""
    if proc.poll() is None:
        try:
            proc.send_signal(signal.SIGINT)
        except (ValueError, OSError, AttributeError):
            proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()


# --- A. airgapped -------------------------------------------------------------------------------

def run_airgapped():
    port = free_port()
    proc = start_server(port)                            # no WIKIKB_MODE at all: the default path
    try:
        status, body = raw_request(port, "GET", "/health")
        h = json.loads(body) if status == 200 else {}
        check("airgapped: /health reports mode=airgapped, capabilities.scrape=false",
              h.get("mode") == modes.AIRGAPPED and h.get("capabilities", {}).get("scrape") is False
              and h.get("capabilities", {}).get("ingest") is True,
              "body=%r" % body[:200])

        unknown_get = raw_request(port, "GET", "/no-such-path")
        got = raw_request(port, "GET", "/scrape/sources")
        check("airgapped: GET /scrape/sources byte-identical to an unknown GET path",
              got == unknown_get and got[0] == 404, "scrape=%r unknown=%r" % (got, unknown_get))

        unknown_post = raw_request(port, "POST", "/no-such-path", body=b"{}")
        got = raw_request(port, "POST", "/scrape", body=b"{}")
        check("airgapped: POST /scrape byte-identical to an unknown POST path",
              got == unknown_post and got[0] == 404, "scrape=%r unknown=%r" % (got, unknown_post))

        status, body = raw_request(port, "GET", "/openapi.json")
        spec = json.loads(body) if status == 200 else {}
        check("airgapped: /openapi.json omits the scrape paths, keeps jobs+ingest",
              "/scrape" not in spec.get("paths", {})
              and "/jobs/{id}" in spec.get("paths", {})
              and "/ingest/{domain}" in spec.get("paths", {}),
              "paths=%r" % sorted(spec.get("paths", {})))

        # write surface off: /ingest hidden exactly like /upload already is
        got = raw_request(port, "POST", "/ingest/keycloak", body=b"")
        check("uploads disabled: POST /ingest hidden (404, identical to unknown POST path)",
              got == unknown_post, "ingest=%r unknown=%r" % (got, unknown_post))
    finally:
        stop_server(proc)


# --- B. online ----------------------------------------------------------------------------------

def run_online():
    port = free_port()
    proc = start_server(port, mode=modes.ONLINE)
    try:
        status, body = raw_request(port, "GET", "/health")
        h = json.loads(body) if status == 200 else {}
        check("online: /health reports mode=online, capabilities.scrape=true",
              h.get("mode") == modes.ONLINE and h.get("capabilities", {}).get("scrape") is True,
              "body=%r" % body[:200])

        status, body = raw_request(port, "POST", "/scrape", body=b"{}")
        obj = json.loads(body) if status == 501 else {}
        check("online: POST /scrape mounted, answers 501 (declared seam, not yet implemented)",
              status == 501 and "scrape" in (obj.get("seam") or ""),
              "status=%s body=%r" % (status, body[:200]))

        status, _ = raw_request(port, "GET", "/scrape/sources")
        check("online: GET /scrape/sources mounted, answers 501", status == 501, "status=%s" % status)

        status, body = raw_request(port, "GET", "/openapi.json")
        spec = json.loads(body) if status == 200 else {}
        check("online: /openapi.json documents /scrape and /scrape/sources",
              "/scrape" in spec.get("paths", {}) and "/scrape/sources" in spec.get("paths", {}),
              "paths=%r" % sorted(spec.get("paths", {})))

        # the modes are ADDITIVE: nothing airgapped serves may be missing here
        status, _ = raw_request(port, "GET", "/route?q=keycloak+ldap")
        check("online: the airgapped surface is still fully present (/route answers 200)",
              status == 200, "status=%s" % status)
    finally:
        stop_server(proc)


# --- C. a typo must refuse to start ---------------------------------------------------------------

def run_bad_mode():
    port = free_port()
    proc = start_server(port, mode="onlien")
    try:
        rc = proc.wait(timeout=20)
    except subprocess.TimeoutExpired:
        stop_server(proc)
        check("unknown WIKIKB_MODE refuses to start (exit 2)", False, "server kept running")
        return
    err = (proc.stderr.read() or "")
    check("unknown WIKIKB_MODE refuses to start (exit 2, names the valid modes)",
          rc == 2 and "REFUSED" in err and "airgapped" in err, "rc=%s err=%r" % (rc, err[-200:]))


# --- D. the jobs surface --------------------------------------------------------------------------

def run_jobs_surface():
    port = free_port()
    # Uploads ON so the write surface is mounted, but auto-ingest OFF so NOTHING can queue a real
    # chain against the live vault while this probe is talking to the server.
    proc = start_server(port, allow_upload=True, extra_env={"WIKIKB_AUTO_INGEST": "0"})
    try:
        status, body = raw_request(port, "GET", "/jobs")
        obj = json.loads(body) if status == 200 else {}
        check("/jobs returns {jobs:[], stats:{}} with no worker started",
              status == 200 and isinstance(obj.get("jobs"), list) and "pending" in (obj.get("stats") or {})
              and obj["stats"]["worker"] is False,
              "status=%s body=%r" % (status, body[:200]))

        status, _ = raw_request(port, "GET", "/jobs/not-a-job-id")
        check("/jobs/<malformed> -> 400", status == 400, "status=%s" % status)

        status, _ = raw_request(port, "GET", "/jobs/deadbeefcafe")
        check("/jobs/<unknown but well-formed> -> 404", status == 404, "status=%s" % status)

        status, body = raw_request(port, "GET", "/health")
        h = json.loads(body)
        check("/health separates mode capability from process state (uploads on, auto_ingest off)",
              h.get("uploads") is True and h.get("auto_ingest") is False, "body=%r" % body[:200])

        # Endpoint is mounted and semantically gated — an undeclared domain is rejected BEFORE
        # anything is queued, which is what lets this case run without touching the vault.
        status, _ = raw_request(port, "POST", "/ingest/no-such-domain", body=b"")
        check("POST /ingest/<undeclared domain> -> 400 (nothing queued)", status == 400,
              "status=%s" % status)
    finally:
        stop_server(proc)


# --- E. the runner, in-process ---------------------------------------------------------------------

def run_runner():
    # Coalescing, with the worker deliberately not draining: a live worker would race us to
    # RUNNING and make the assertion flaky.
    r = jobsmod.Runner(start_worker=False)
    j1, c1 = r.submit(jobsmod.Job("ingest", [("noop", ["route", "x"])], domain="d",
                                  coalesce_key=("ingest", "d")))
    j2, c2 = r.submit(jobsmod.Job("ingest", [("noop", ["route", "x"])], domain="d",
                                  coalesce_key=("ingest", "d")))
    j3, c3 = r.submit(jobsmod.Job("ingest", [("noop", ["route", "x"])], domain="other",
                                  coalesce_key=("ingest", "other")))
    check("runner: a second queued ingest for the same domain coalesces into the first",
          not c1 and c2 and j2.id == j1.id and not c3 and j3.id != j1.id,
          "c=(%s,%s,%s) ids=(%s,%s,%s)" % (c1, c2, c3, j1.id, j2.id, j3.id))
    check("runner: coalescing leaves one pending job per domain, not three",
          r.stats()["pending"] == 2, "stats=%r" % r.stats())

    # Real execution, with READ-ONLY steps only (`route` just scores a query against taxonomy.md).
    live = jobsmod.Runner()
    ok, _ = live.submit(jobsmod.Job("probe", [("route", ["route", "keycloak ldap"])]))
    bad, _ = live.submit(jobsmod.Job("probe", [("boom", ["route"]),           # missing arg -> non-zero
                                               ("never", ["route", "x"])]))
    deadline = time.time() + 60
    while time.time() < deadline and (ok.state in (jobsmod.QUEUED, jobsmod.RUNNING)
                                      or bad.state in (jobsmod.QUEUED, jobsmod.RUNNING)):
        time.sleep(0.2)
    check("runner: a clean job reaches done with a per-step exit/seconds/log record",
          ok.state == jobsmod.DONE and len(ok.results) == 1 and ok.results[0]["exit"] == 0
          and "seconds" in ok.results[0], "state=%s results=%r" % (ok.state, ok.results))
    check("runner: a failing step marks the job failed and STOPS the chain (later steps never run)",
          bad.state == jobsmod.FAILED and len(bad.results) == 1 and bad.results[0]["exit"] != 0
          and bad.error and "never" not in [r["step"] for r in bad.results],
          "state=%s results=%r error=%r" % (bad.state, bad.results, bad.error))
    check("runner: a failed step captures a bounded log tail",
          isinstance(bad.results[0].get("log"), list)
          and len(bad.results[0]["log"]) <= jobsmod.MAX_LOG_LINES,
          "log=%r" % bad.results[0].get("log"))

    d = ok.to_dict()
    check("runner: to_dict is JSON-serializable (it is served over HTTP)",
          json.dumps(d) and d["id"] == ok.id and d["state"] == jobsmod.DONE)


# --- F. the airgapped egress guard ------------------------------------------------------------------

def run_egress_guard():
    """The scraper must refuse at the CALL, not only by not being routed — a mis-wired future path
    must not be able to reach the network from a sealed box (modes.py, property 2)."""
    from wikikb.scrape import scrape as scrapemod
    saved = os.environ.get(modes.ENV_VAR)
    try:
        os.environ.pop(modes.ENV_VAR, None)
        try:
            scrapemod.fetch("https://example.invalid/x")
            check("airgapped: scrape.fetch() refuses at the call site", False, "no raise")
        except modes.ModeError:
            check("airgapped: scrape.fetch() refuses at the call site (ModeError, before any socket)", True)
        except NotImplementedError:
            check("airgapped: scrape.fetch() refuses at the call site", False,
                  "raised NotImplementedError — the mode guard did not run FIRST")
        os.environ[modes.ENV_VAR] = modes.ONLINE
        try:
            scrapemod.fetch("https://example.invalid/x")
            check("online: scrape.fetch() passes the mode guard (then NotImplementedError)", False,
                  "no raise")
        except NotImplementedError:
            check("online: scrape.fetch() passes the mode guard, then NotImplementedError (the seam)", True)
        except modes.ModeError as e:
            check("online: scrape.fetch() passes the mode guard", False, str(e))
    finally:
        if saved is None:
            os.environ.pop(modes.ENV_VAR, None)
        else:
            os.environ[modes.ENV_VAR] = saved


def main():
    print("=" * 78)
    print("MODE PROBE — WIKIKB_MODE=airgapped|online, the jobs surface, and the ingest runner")
    print("=" * 78)
    run_airgapped()
    run_online()
    run_bad_mode()
    run_jobs_surface()
    run_runner()
    run_egress_guard()
    failed = [n for n, ok in checks if not ok]
    print("-" * 78)
    print("%d/%d passed%s" % (len(checks) - len(failed), len(checks),
                              "" if not failed else "  — FAILURES ABOVE"))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
