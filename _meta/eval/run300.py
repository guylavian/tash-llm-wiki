#!/usr/bin/env python3
"""run300.py — run the cases300.jsonl eval through `opencode run` in parallel, then grade.

Usage:
    python3 run300.py [--model opencode/deepseek-v4-flash-free] [--workers 4]
                      [--limit N] [--timeout 300] [--answers answers300.jsonl]

Resumable: already-answered ids are skipped, answers append as they finish.
cache-repeat cases run in a second phase (their originals must answer first).
Grade afterwards with:
    python3 grade300.py --cases cases300.jsonl --answers answers300.jsonl --json report300.json
"""
import argparse, json, pathlib, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = pathlib.Path(__file__).resolve().parent
WIKI = HERE.parent.parent
LOCK = threading.Lock()


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
    args = ap.parse_args()

    cases = [json.loads(l) for l in open(args.cases, encoding="utf-8") if l.strip()]
    out = pathlib.Path(args.answers)
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
                        fh.write(json.dumps({"id": c["id"], "answer": ans}, ensure_ascii=False) + "\n")
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
