#!/usr/bin/env python3
"""cost_probe.py — O(1) behaviour probe for the cost layer (analogue of gate_probe.py). stdlib only.

Tests BEHAVIOUR, not a real model: no LiteLLM call, no socket. It asserts the load-bearing contracts
the optional online tier rests on (COUNCIL-DIRECTIVES.md):
  - BF-9: the budget gate raises cost.BudgetExceeded on an over-budget value, and is silent on/under it.
  - BF-8: cost.parse_response extracts a WELL-FORMED dict from a STUBBED response object with NO
          KeyError/exception — including when `_hidden_params` is absent or missing keys, and when
          `usage` is an attribute object OR a plain dict.
  - degradation: cost.price_usd returns (None,'unpriced/local') offline; count_tokens returns an int.

Exit: 0 all pass · 1 a case failed (CI gate).

Usage:  python3 wiki/_meta/tests/cost_probe.py
"""
import os
import sys

META = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # _meta/tests -> _meta
sys.dont_write_bytecode = True
sys.path.insert(0, META)               # test bootstrap: make `import wikikb` importable
from wikikb.online import cost  # the real module under test

checks = []


def check(name, ok, detail=""):
    checks.append((name, ok))
    print("  %s  %s%s" % ("PASS" if ok else "FAIL", name, ("  — " + detail) if detail and not ok else ""))


# ---- stub response objects (shapes LiteLLM can return) --------------------------------------

class _Usage:
    def __init__(self, p, c):
        self.prompt_tokens, self.completion_tokens = p, c


class _Resp:
    """Attribute-style response with optional _hidden_params."""
    def __init__(self, usage=None, hidden=None, choices_text=None):
        if usage is not None:
            self.usage = usage
        if hidden is not None:
            self._hidden_params = hidden
        if choices_text is not None:
            self.choices = [type("C", (), {"message": type("M", (), {"content": choices_text})()})()]


# 1. BF-9 — budget gate raises over budget, silent at/under, no-op when limit None.
try:
    cost.check_budget(10.0, 5.0, "tokens")
    check("budget raises over limit", False, "did not raise")
except cost.BudgetExceeded:
    check("budget raises over limit", True)
check("budget silent at/under limit", cost.check_budget(5.0, 5.0) is False and cost.check_budget(3.0, 5.0) is False)
check("budget no-op when limit None", cost.check_budget(1e9, None) is False)

# 2. BF-8 — parse_response well-formed + NO KeyError across response shapes.
EXPECT = {"gen_prompt_tok", "gen_completion_tok", "gen_cost_usd", "gen_latency_ms", "cached", "price_tag"}

# 2a. usage as attribute object, NO _hidden_params (the local-model case)
try:
    d = cost.parse_response(_Resp(usage=_Usage(120, 30)), model="ollama/qwen2.5:32b", latency_ms=42.0)
    ok = (set(d) == EXPECT and d["gen_prompt_tok"] == 120 and d["gen_completion_tok"] == 30
          and d["gen_latency_ms"] == 42.0 and d["cached"] is False and d["gen_cost_usd"] is None)
    check("parse_response: attr usage, no _hidden_params -> unpriced/local, no KeyError", ok, str(d))
except Exception as e:
    check("parse_response: attr usage, no _hidden_params", False, "raised %r" % e)

# 2b. usage as dict + _hidden_params with cache_hit but no response_cost
try:
    d = cost.parse_response(_Resp(usage={"prompt_tokens": 5, "completion_tokens": 7},
                                  hidden={"cache_hit": True}), model="ollama/x")
    ok = (set(d) == EXPECT and d["gen_prompt_tok"] == 5 and d["cached"] is True)
    check("parse_response: dict usage + partial _hidden_params, no KeyError", ok, str(d))
except Exception as e:
    check("parse_response: dict usage + partial _hidden_params", False, "raised %r" % e)

# 2c. empty/garbage response -> all None, no exception
try:
    d = cost.parse_response(object(), model=None)
    ok = set(d) == EXPECT and d["gen_prompt_tok"] is None and d["gen_cost_usd"] is None
    check("parse_response: empty response -> all None, no exception", ok, str(d))
except Exception as e:
    check("parse_response: empty response", False, "raised %r" % e)

# 2d. BF-8/B1: a non-numeric usage token must NOT crash — it is coerced to None.
try:
    d = cost.parse_response(_Resp(usage=_Usage("n/a", 3)), model="ollama/x")
    ok = set(d) == EXPECT and d["gen_prompt_tok"] is None and d["gen_completion_tok"] == 3
    check("parse_response: non-numeric usage token -> None, no crash (B1)", ok, str(d))
except Exception as e:
    check("parse_response: non-numeric usage token", False, "raised %r" % e)

# 2e. usage present but a field missing; _hidden_params a non-dict -> still well-formed, no crash.
try:
    d = cost.parse_response(_Resp(usage={"completion_tokens": 9}, hidden=[1, 2, 3]), model="ollama/x")
    ok = (set(d) == EXPECT and d["gen_prompt_tok"] is None and d["gen_completion_tok"] == 9
          and d["cached"] is False)
    check("parse_response: missing pt + non-dict _hidden_params, no crash", ok, str(d))
except Exception as e:
    check("parse_response: missing pt + non-dict hidden", False, "raised %r" % e)

# 3. degradation — price_usd offline + count_tokens int.
pu = cost.price_usd("ollama/qwen2.5:32b", 100, 50)
check("price_usd offline -> (None,'unpriced/local')", pu == (None, "unpriced/local"), str(pu))
check("count_tokens returns int", isinstance(cost.count_tokens("hello world"), int))

print("-" * 70)
failed = [n for n, ok in checks if not ok]
print("%d/%d passed%s" % (len(checks) - len(failed), len(checks), "" if not failed else "  — FAILURES ABOVE"))
sys.exit(1 if failed else 0)
