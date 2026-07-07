"""conftest.py — make the uninstalled `wikikb` package importable under pytest.

The standard no-install test bootstrap: put `_meta/` on sys.path so `from wikikb import …` resolves
when running `python -m pytest` from anywhere. The standalone probes (selftest.py / gate_probe.py /
gate_page_probe.py / cost_probe.py) also insert it themselves, so they run via
`python3 wiki/_meta/tests/<probe>.py` without pytest. No pip install required (the air-gap model).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # _meta/
