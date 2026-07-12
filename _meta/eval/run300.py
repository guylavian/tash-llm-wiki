#!/usr/bin/env python3
"""run300.py — run the cases300.jsonl eval through `opencode run` in parallel, then grade.

Usage:
    python3 run300.py [--model opencode/deepseek-v4-flash-free] [--workers 4]
                      [--limit N] [--timeout 300] [--answers answers300.jsonl]
                      [--new-run] [--overwrite]

Cohort identity (consensus 2026-07-12 — resume must never mix experiments):
    Every run writes a sidecar manifest `<answers>.manifest.json` (run_id, model, cases
    sha256+count, git commit + dirty flag, started_utc, workers, timeout, isolation) and stamps
    every answer row with {run_id, model}. Resuming an existing answers file requires the
    manifest to exist and match on model + cases hash; any mismatch exits 2. `--new-run` starts
    a FRESH timestamped answers path (never touches the existing one); `--overwrite` explicitly
    truncates the existing path + manifest. grade300.py rejects mixed-run_id cohorts.

Resumable: already-answered ids are skipped, answers append as they finish.
cache-repeat cases run in a second phase (their originals must answer first).
Grade afterwards with:
    python3 grade300.py --cases cases300.jsonl --answers <answers.jsonl> --json report300.json
"""
import argparse, datetime, hashlib, json, pathlib, subprocess, sys, threading, time, uuid
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = pathlib.Path(__file__).resolve().parent
WIKI = HERE.parent.parent
LOCK = threading.Lock()
MANIFEST_SCHEMA = "run300/1"


def _git(*args):
    try:
        p = subprocess.run(["git", *args], capture_output=True, text=True, cwd=str(WIKI), timeout=10)
        return p.stdout.strip() if p.returncode == 0 else None
    except Exception:
        return None


def build_manifest(args, cases_path):
    blob = pathlib.Path(cases_path).read_bytes()
    return {
        "schema": MANIFEST_SCHEMA,
        "run_id": (datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
                   + "-" + uuid.uuid4().hex[:8]),
        "model": args.model,
        "cases_sha256": hashlib.sha256(blob).hexdigest(),
        "cases_count": sum(1 for l in blob.splitlines() if l.strip()),
        "git_commit": _git("rev-parse", "HEAD"),
        "git_dirty": bool(_git("status", "--porcelain")),
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "workers": args.workers,
        "timeout": args.timeout,
        "isolation": "none",   # WI-4 (per-case workspace isolation) will set its own value
    }


def manifest_path(answers_path):
    return pathlib.Path(str(answers_path) + ".manifest.json")


def _refuse(msg):
    print("refusing resume: " + msg, file=sys.stderr)
    sys.exit(2)


def _load_manifest(mp):
    """Parse + shape-check a cohort manifest; any defect is a refusal (exit 2), never a crash."""
    try:
        man = json.loads(mp.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        _refuse("unreadable manifest %s (%s). Use --new-run or --overwrite." % (mp, e))
    if not isinstance(man, dict) or man.get("schema") != MANIFEST_SCHEMA:
        _refuse("manifest %s has wrong/missing schema (want %r). Use --new-run or --overwrite."
                % (mp, MANIFEST_SCHEMA))
    for key in ("run_id", "model", "cases_sha256"):
        if not isinstance(man.get(key), str) or not man[key].strip():
            _refuse("manifest %s missing/invalid %r. Use --new-run or --overwrite." % (mp, key))
    return man


def _check_existing_rows(out, man):
    """Every existing row must belong to THIS cohort before we append to it — a stamped stranger
    row would corrupt the cohort silently until grading. Refusal (exit 2) happens BEFORE any
    worker launches, not after an expensive run."""
    try:
        lines = out.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        _refuse("unreadable answers file %s (%s)" % (out, e))
    for ln, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            _refuse("%s line %d is not valid JSON" % (out, ln))
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            _refuse("%s line %d is not an answer row" % (out, ln))
        if row.get("run_id") != man["run_id"] or row.get("model") != man["model"]:
            _refuse("%s line %d is stamped run_id=%r/model=%r but the manifest says %r/%r — "
                    "mixed cohort. Use --new-run." % (out, ln, row.get("run_id"),
                    row.get("model"), man["run_id"], man["model"]))


def _establish(out, fresh):
    """Atomically stand up a new cohort: manifest + an (empty) answers file, so zero-work runs
    (--limit 0, empty banks) still leave a complete, gradeable cohort on disk."""
    manifest_path(out).write_text(json.dumps(fresh, indent=1), encoding="utf-8")
    out.touch()
    return out, fresh


def resolve_cohort(args, cases_path):
    """Decide (answers_path, manifest) honoring resume/--new-run/--overwrite. Exits 2 on any
    identity mismatch — a cohort manifest is useless if resume can silently mix experiments."""
    out = pathlib.Path(args.answers)
    if args.new_run:                            # fresh timestamped path; never touches the old one
        fresh = build_manifest(args, cases_path)
        out = out.with_name(out.stem + "-" + fresh["run_id"] + out.suffix)
        if out.exists():
            print("--new-run target %s already exists (improbable collision) — rerun" % out,
                  file=sys.stderr)
            sys.exit(2)
        return _establish(out, fresh)
    mp = manifest_path(out)
    if out.exists() and not args.overwrite:
        if not mp.exists():
            _refuse("%s exists but has no manifest (legacy/unknown cohort). Use --new-run for a "
                    "fresh cohort or --overwrite to replace it." % out)
        man = _load_manifest(mp)
        fresh = build_manifest(args, cases_path)
        for key in ("model", "cases_sha256"):
            if man.get(key) != fresh[key]:
                _refuse("manifest %s mismatch (manifest=%r, now=%r). Use --new-run or --overwrite."
                        % (key, man.get(key), fresh[key]))
        _check_existing_rows(out, man)
        return out, man                          # same cohort — resume under the ORIGINAL run_id
    fresh = build_manifest(args, cases_path)     # new file, or explicit --overwrite
    if args.overwrite:
        out.write_text("", encoding="utf-8")
    return _establish(out, fresh)


def ask(case, model, timeout):
    for attempt in (1, 2):
        try:
            r = subprocess.run(
                ["opencode", "run", "-m", model, case["question"]],
                capture_output=True, text=True, timeout=timeout, cwd=str(WIKI))
            out = r.stdout.strip()
            if out:
                return out
            err = (r.stderr or "").strip()[-300:]
        except subprocess.TimeoutExpired:
            err = f"timeout {timeout}s"
        time.sleep(5 * attempt)  # ponytail: fixed backoff; free-tier rate limits are the ceiling
    return f"[RUN-ERROR] {err}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="opencode/deepseek-v4-flash-free")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, help="run only the first N pending cases (smoke run)")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--cases", default=str(HERE / "cases300.jsonl"))
    ap.add_argument("--answers", default=str(HERE / "answers300.jsonl"))
    grp = ap.add_mutually_exclusive_group()
    grp.add_argument("--new-run", action="store_true", dest="new_run",
                     help="start a FRESH cohort on a timestamped answers path (never touches the old one)")
    grp.add_argument("--overwrite", action="store_true",
                     help="explicitly truncate the existing answers file + manifest and start over")
    args = ap.parse_args()

    cases = [json.loads(l) for l in open(args.cases, encoding="utf-8") if l.strip()]
    out, manifest = resolve_cohort(args, args.cases)
    print(f"cohort {manifest['run_id']} (model {manifest['model']}) -> {out}")
    done = set()
    if out.exists():
        done = {json.loads(l)["id"] for l in open(out, encoding="utf-8") if l.strip()}

    def run_phase(phase_cases, label):
        pending = [c for c in phase_cases if c["id"] not in done]
        if args.limit is not None:
            remaining = args.limit - len(done)
            pending = pending[:max(0, remaining)]
        if not pending:
            return
        print(f"{label}: {len(pending)} to run ({args.workers} workers, model {args.model})")
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {ex.submit(ask, c, args.model, args.timeout): c for c in pending}
            for n, fut in enumerate(as_completed(futs), 1):
                c = futs[fut]
                ans = fut.result()
                with LOCK:
                    with open(out, "a", encoding="utf-8") as fh:
                        fh.write(json.dumps({"id": c["id"], "answer": ans,
                                             "run_id": manifest["run_id"],
                                             "model": manifest["model"]}, ensure_ascii=False) + "\n")
                    done.add(c["id"])
                flag = " ERR" if ans.startswith("[RUN-ERROR]") else ""
                print(f"  [{n}/{len(pending)}] {c['id']}{flag}  ({time.time()-t0:.0f}s elapsed)", flush=True)

    firsts = [c for c in cases if c["type"] != "cache-repeat"]
    repeats = [c for c in cases if c["type"] == "cache-repeat"]
    run_phase(firsts, "phase 1 (originals)")
    run_phase(repeats, "phase 2 (cache-repeats)")

    errs = sum(1 for l in open(out, encoding="utf-8")
               if l.strip() and json.loads(l)["answer"].startswith("[RUN-ERROR]"))
    print(f"done: {len(done)}/{len(cases)} answered, {errs} run-errors -> {out}")
    print(f"grade: python3 {HERE/'grade300.py'} --cases {args.cases} --answers {out} --json {HERE/'report300.json'}")


if __name__ == "__main__":
    main()
