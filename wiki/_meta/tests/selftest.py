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
PKG_TOOLS = {"kb", "route", "expand", "embed", "cost", "llm", "lint", "manifest", "index", "crosslink",
             "tags", "backfill", "corpus_to_vault", "docs_to_corpus", "migrate_native", "evaluate", "tkg"}


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

# 6. every kb: token resolves (crosslink reports no 'unresolved' line)
rc, out = run("crosslink.py")
check("crosslink 0 unresolved kb: tokens", rc == 0 and "unresolved" not in out, out[:160])

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

# 38. tkg tier (air-gap): importing it AND the optional Graphiti/Kuzu backend pulls NO third-party
# (kuzu/graphiti_core), and the backend is OFF by default (WIKI_TKG unset) — `available()` is config-only
# and must not import kuzu. Mirrors the online/ probe.
_tkg_err = ""
try:
    _saved_tkg = os.environ.pop("WIKI_TKG", None)
    import importlib as _il
    for _m in ("wikikb.tkg", "wikikb.tkg.model", "wikikb.tkg.store", "wikikb.tkg.tkg",
               "wikikb.tkg.versions", "wikikb.tkg.graphiti_backend"):
        _il.import_module(_m)
    from wikikb.tkg import graphiti_backend as _gb
    _no3p = "kuzu" not in sys.modules and "graphiti_core" not in sys.modules
    _off = (_gb.available() is False) and ("kuzu" not in sys.modules)   # available() must not import kuzu
except Exception as _e:                                                 # noqa: BLE001
    _no3p = _off = False
    _tkg_err = repr(_e)
finally:
    if _saved_tkg is not None:
        os.environ["WIKI_TKG"] = _saved_tkg
check("tkg: import (incl. backend) pulls no kuzu/graphiti_core; backend off when WIKI_TKG unset",
      _no3p and _off, _tkg_err or "third-party imported / backend on by default")

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

failed = [n for n, ok, _ in checks if not ok]
print(f"\n{len(checks) - len(failed)}/{len(checks)} checks passed")
sys.exit(1 if failed else 0)
