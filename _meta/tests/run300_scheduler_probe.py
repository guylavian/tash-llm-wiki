#!/usr/bin/env python3
"""Fast deterministic regression for run300's bounded timeout circuit."""
import importlib.util
import pathlib
import threading
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("run300", ROOT / "_meta/eval/run300.py")
run300 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run300)


def main():
    cases = [{"id": "c%d" % i} for i in range(6)]
    started, persisted = [], []
    lock = threading.Lock()
    def fake(c):
        with lock:
            started.append(c["id"])
        time.sleep(0.01 if c["id"] in {"c0", "c1"} else 0.03)
        return "[RUN-ERROR] timeout 1s" if c["id"] in {"c0", "c1"} else "ok"
    opened = run300.run_bounded(cases, 2, fake,
                                lambda c, ans: persisted.append((c["id"], ans)), 2)
    assert opened
    assert {"c0", "c1"}.issubset(dict(persisted))
    assert set(started).issubset({"c0", "c1", "c2"})
    assert set(started) == set(dict(persisted))
    remaining = [c for c in cases if c["id"] not in dict(persisted)]
    resumed = []
    assert not run300.run_bounded(remaining, 1, lambda c: "ok",
                                  lambda c, ans: resumed.append(c["id"]), 2)
    assert resumed == [c["id"] for c in remaining]
    print("PASS scheduler opens, drains, does not refill, and resumes remaining IDs")


if __name__ == "__main__":
    main()
