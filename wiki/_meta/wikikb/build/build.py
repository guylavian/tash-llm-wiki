"""build.py — ONE verb for the whole regen chain, so no step gets forgotten.

`python3 -m wikikb build` runs, in order:
    tags normalize --apply  ->  tags backfill --apply  ->  crosslink --apply
    ->  index  ->  tkg ingest  ->  lint
Each step is the real tool run as a subprocess (same interpreter, same CWD contract
as the dispatcher); the chain stops at the first non-zero exit. lint runs last so a
freshly-built wiki ends with its health report — its exit code is the build's.

Exists because index/crosslink/tags/manifest/tkg were five separately-remembered
commands and the routing index was chronically stale as a result. Stdlib only.
"""
import subprocess
import sys

sys.dont_write_bytecode = True

STEPS = [
    ["tags", "normalize", "--apply"],
    ["tags", "backfill", "--apply"],
    ["crosslink", "--apply"],
    ["index"],
    ["tkg", "ingest"],
    ["lint"],
    ["verify"],   # answer-time source verification — a MISMATCH (wrong cached number) fails the build
]


def main():
    for step in STEPS:
        print("build ▸ %s" % " ".join(step), flush=True)
        rc = subprocess.run([sys.executable, "-m", "wikikb"] + step).returncode
        if rc != 0:
            print("build ▸ FAILED at: %s (exit %d)" % (" ".join(step), rc))
            sys.exit(rc)
    print("build ▸ done — all steps clean")


if __name__ == "__main__":
    main()
