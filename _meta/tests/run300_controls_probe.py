#!/usr/bin/env python3
"""Regression probe for manifest-commit snapshot isolation."""
import importlib.util
import pathlib
import shutil
import sys
import uuid

ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("run300", ROOT / "_meta/eval/run300.py")
run300 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run300)


def main():
    commit = run300._git("rev-parse", "HEAD")
    run_id = "probe-" + uuid.uuid4().hex
    base = run300.materialize_cohort_snapshot({"run_id": run_id, "git_commit": commit})
    case = None
    try:
        assert (base / ".wikikb-commit").read_text().strip() == commit
        target = base / "README.md"
        before = target.read_bytes()
        case = run300.build_case_snapshot("isolation", base)
        copied = case / "README.md"
        copied.write_text("case-local mutation\n", encoding="utf-8")
        filed = case / "questions" / "probe-filed-page.md"
        filed.write_text("case-local question\n", encoding="utf-8")
        assert target.read_bytes() == before
        assert (ROOT / "README.md").read_bytes() == before
        assert not (base / "questions" / "probe-filed-page.md").exists()
        assert not (ROOT / "questions" / "probe-filed-page.md").exists()
        print("PASS manifest snapshot is commit-marked and case writes are isolated")
    finally:
        if case:
            shutil.rmtree(case, ignore_errors=True)
        if base:
            base.chmod(0o755)
            for p in base.rglob("*"):
                try:
                    p.chmod(0o755 if p.is_dir() else 0o644)
                except OSError:
                    pass
            shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    main()
