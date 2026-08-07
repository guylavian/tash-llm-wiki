#!/usr/bin/env python3
"""cron.py — the scheduled-harvest timer. stdlib only; opens no socket itself.

Runs INSIDE the serve process as one daemon thread that, on each tick, submits a scrape+ingest job
per watchlist domain to the SAME serialized runner the upload path uses (`serve/jobs.py`). It does
not fetch anything and does not write to the vault — it only decides *when*, which is why it can be
tested without a network.

WHY AN IN-PROCESS TIMER RATHER THAN A SYSTEM CRONTAB. The chain a tick fires regenerates whole-vault
artifacts (`build` rewrites the indexes, the crosslink graph and the tkg store), so it MUST be
serialized against the ingest jobs an upload queues. A system crontab entry would run a second,
independent process that knows nothing about the in-flight job and would interleave writes to the
same generated files. Going through `jobs.RUNNER` means the scheduler inherits the one-worker
guarantee, the coalescing rule, and the stop-at-first-failure contract for free. (An external
crontab calling `POST /scrape` is still perfectly fine — it lands in the same queue.)

CONFIGURATION — env, per the deployment model (`.env` configures the container):

    WIKIKB_SCRAPE_CRON=0 3 * * *     5-field cron, an @macro, or an interval (`6h`, `90m`, `1d`).
                                     Default: `0 3 * * *` (daily at 03:00 local time).
    WIKIKB_SCRAPE_CRON_ENABLED=1     Default ON, per the spec. `POST /scrape/cron {"enabled":false}`
                                     flips it at RUNTIME without a restart.

THE TOGGLE IS RUNTIME-ONLY, AND THAT IS DELIBERATE. Flipping it does not rewrite `.env`: a process
that edits its own configuration file makes "what will this container do when it restarts?"
unanswerable from the config. So the env var is the boot default and the endpoint is the live
override — `GET /scrape/cron` reports both, so the difference is never invisible.

A BAD SCHEDULE DOES NOT KILL THE SERVER. Unlike `WIKIKB_MODE` (a security posture, where a typo
must refuse to start), a malformed cron expression disables the timer and is reported by
`GET /scrape/cron` and in the startup log. The distinction: getting the mode wrong can open a
socket you believed was sealed; getting the schedule wrong means a harvest does not run, which is
visible in the status endpoint and harmless to everything else the server does.
"""
import os
import threading
import time

MINUTE, HOUR, DOM, MONTH, DOW = range(5)
FIELD_RANGES = ((0, 59), (0, 23), (1, 31), (1, 12), (0, 7))     # dow: 0 and 7 are both Sunday
FIELD_NAMES = ("minute", "hour", "day-of-month", "month", "day-of-week")
MONTH_NAMES = {n: i + 1 for i, n in enumerate(
    ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"))}
DOW_NAMES = {n: i for i, n in enumerate(("sun", "mon", "tue", "wed", "thu", "fri", "sat"))}
MACROS = {
    "@yearly": "0 0 1 1 *", "@annually": "0 0 1 1 *", "@monthly": "0 0 1 * *",
    "@weekly": "0 0 * * 0", "@daily": "0 0 * * *", "@midnight": "0 0 * * *",
    "@hourly": "0 * * * *",
}
DEFAULT_SCHEDULE = "0 3 * * *"
HORIZON_DAYS = 400          # a spec matching nothing within a year (e.g. "0 0 30 2 *") is a config
                            # error, and reporting "never" beats scanning forward forever


class CronError(ValueError):
    """A schedule this module cannot parse. Reported to the operator; never fatal to the server."""


# --- parsing -------------------------------------------------------------------------------------

def _field(spec, idx):
    """One cron field -> the set of matching values. Handles `*`, `a`, `a-b`, `*/n`, `a-b/n`,
    comma lists, and the three-letter month/day names."""
    lo, hi = FIELD_RANGES[idx]
    out = set()
    for part in spec.split(","):
        part = part.strip().lower()
        if not part:
            raise CronError("empty %s field" % FIELD_NAMES[idx])
        step = 1
        if "/" in part:
            part, _, step_s = part.partition("/")
            if not step_s.isdigit() or int(step_s) < 1:
                raise CronError("bad step %r in the %s field" % (step_s, FIELD_NAMES[idx]))
            step = int(step_s)
        if part in ("*", ""):
            a, b = lo, hi
        elif "-" in part[1:]:
            a_s, _, b_s = part.partition("-")
            a, b = _value(a_s, idx), _value(b_s, idx)
        else:
            a = b = _value(part, idx)
            if step > 1:                 # `5/15` is read as `5-59/15`, matching Vixie cron
                b = hi
        if a > b:
            raise CronError("reversed range %r in the %s field" % (part, FIELD_NAMES[idx]))
        out.update(range(a, b + 1, step))
    if idx == DOW and 7 in out:
        out.add(0)                       # 7 and 0 both mean Sunday
        out.discard(7)
    return out


def _value(tok, idx):
    tok = tok.strip().lower()
    if idx == MONTH and tok in MONTH_NAMES:
        return MONTH_NAMES[tok]
    if idx == DOW and tok in DOW_NAMES:
        return DOW_NAMES[tok]
    if not tok.isdigit():
        raise CronError("bad value %r in the %s field" % (tok, FIELD_NAMES[idx]))
    v = int(tok)
    lo, hi = FIELD_RANGES[idx]
    if not lo <= v <= hi:
        raise CronError("%s out of range in the %s field (%d-%d)" % (tok, FIELD_NAMES[idx], lo, hi))
    return v


def parse_interval(spec):
    """`30m` / `6h` / `1d` / `900s` -> seconds, else None.

    Not cron syntax, and supported anyway because "every 6 hours" is what an operator actually wants
    for a harvest and expressing it as `0 */6 * * *` is both easy to get wrong and subtly different
    (that one fires at fixed clock hours, not every 6 hours since start).
    """
    s = (spec or "").strip().lower()
    if len(s) < 2 or not s[:-1].isdigit():
        return None
    n, unit = int(s[:-1]), s[-1]
    mult = {"s": 1, "m": 60, "h": 3600, "d": 86400}.get(unit)
    if not mult or n < 1:
        return None
    secs = n * mult
    if secs < 60:
        raise CronError("interval %r is below the 60s floor (a harvest is minutes of work)" % spec)
    return secs


class Schedule:
    """A parsed schedule — either 5 cron fields or a fixed interval. `next_after(t)` is the only
    thing the scheduler asks it."""

    def __init__(self, spec):
        self.spec = (spec or "").strip()
        self.interval = None
        self.fields = None
        raw = MACROS.get(self.spec.lower(), self.spec)
        if not raw:
            raise CronError("empty schedule")
        secs = parse_interval(raw)
        if secs:
            self.interval = secs
            return
        parts = raw.split()
        if len(parts) != 5:
            raise CronError("expected 5 cron fields (min hour dom mon dow), an @macro, or an "
                            "interval like `6h` — got %r" % self.spec)
        self.fields = [_field(p, i) for i, p in enumerate(parts)]

    def __str__(self):
        return self.spec

    def matches(self, tm):
        """Does this local-time struct match? DOM/DOW use the standard cron OR rule: when BOTH are
        restricted, either one matching is enough (so `0 0 1 * mon` is "the 1st, and every Monday",
        not their intersection)."""
        mn, hr, dom, mon, dow = self.fields
        if tm.tm_min not in mn or tm.tm_hour not in hr or (tm.tm_mon) not in mon:
            return False
        # time.struct_time: tm_wday is Monday=0..Sunday=6; cron wants Sunday=0.
        cron_dow = (tm.tm_wday + 1) % 7
        dom_restricted = len(dom) < 31
        dow_restricted = len(dow) < 7
        if dom_restricted and dow_restricted:
            return tm.tm_mday in dom or cron_dow in dow
        if dom_restricted:
            return tm.tm_mday in dom
        if dow_restricted:
            return cron_dow in dow
        return True

    def next_after(self, now=None):
        """The next firing time strictly after `now` (epoch seconds), or None within the horizon.

        Minute-stepping in LOCAL time via time.localtime, so a DST shift is handled by the platform
        rather than by arithmetic here. The cost is bounded by HORIZON_DAYS; the loop skips a whole
        day at a time when the date fields cannot match, which keeps a monthly schedule cheap.
        """
        if self.interval:
            return (now if now is not None else time.time()) + self.interval
        t = int(now if now is not None else time.time())
        t = t - (t % 60) + 60                        # the start of the next minute
        limit = t + HORIZON_DAYS * 86400
        while t < limit:
            tm = time.localtime(t)
            if self.matches(tm):
                return float(t)
            # Cheap skip: when the DATE cannot match, jump to the next midnight instead of walking
            # 1440 minutes through a day that is already excluded.
            mn, hr, dom, mon, dow = self.fields
            date_ok = tm.tm_mon in mon and (
                (tm.tm_mday in dom or (tm.tm_wday + 1) % 7 in dow) if len(dom) < 31 and len(dow) < 7
                else (tm.tm_mday in dom if len(dom) < 31 else ((tm.tm_wday + 1) % 7 in dow if len(dow) < 7 else True)))
            if not date_ok:
                t += (24 - tm.tm_hour) * 3600 - tm.tm_min * 60
                continue
            t += 60
        return None


# --- runtime state --------------------------------------------------------------------------------

def env_schedule():
    return (os.environ.get("WIKIKB_SCRAPE_CRON") or DEFAULT_SCHEDULE).strip() or DEFAULT_SCHEDULE


def env_enabled():
    """The BOOT default. On unless explicitly switched off — the spec's "default is on"."""
    return (os.environ.get("WIKIKB_SCRAPE_CRON_ENABLED") or "1").strip().lower() \
        not in ("0", "false", "no", "off")


class Scheduler:
    """The timer thread. One instance per process (`SCHEDULER` below).

    Like `jobs.Runner`, NOTHING starts at import — the thread spawns in `start()`, which `serve.py`
    calls from `main()` after it has decided the process is really going to serve. A probe importing
    this module must not acquire a background timer that starts submitting harvests.
    """

    def __init__(self, spec=None, enabled=None, submit=None):
        self.spec_raw = spec if spec is not None else env_schedule()
        self.error = None
        try:
            self.schedule = Schedule(self.spec_raw)
        except CronError as e:
            self.schedule, self.error = None, str(e)
        self.env_default = env_enabled() if enabled is None else bool(enabled)
        self._enabled = self.env_default
        self._submit = submit                # injected in tests; defaults to the real job chain
        self._lock = threading.Lock()
        self._wake = threading.Event()
        self._thread = None
        self._stop = False
        self.next_run = None
        self.last_run = None
        self.last_result = None
        self.runs = 0

    # --- control ---
    def start(self):
        """Spawn the timer thread. Idempotent; a no-op when the schedule failed to parse (there is
        nothing to wait for, and a thread that can never fire would just hide the error)."""
        if self.schedule is None or (self._thread and self._thread.is_alive()):
            return self
        self._recompute()
        self._thread = threading.Thread(target=self._loop, name="wikikb-scrape-cron", daemon=True)
        self._thread.start()
        return self

    def stop(self):
        self._stop = True
        self._wake.set()

    def set_enabled(self, enabled):
        """Flip the timer at runtime. Returns the status dict the endpoint answers with."""
        with self._lock:
            self._enabled = bool(enabled)
        self._recompute()
        self._wake.set()                    # a disable takes effect now, not at the next tick
        return self.status()

    @property
    def enabled(self):
        with self._lock:
            return self._enabled

    def _recompute(self):
        self.next_run = (self.schedule.next_after() if (self.schedule and self.enabled) else None)

    def status(self):
        """What `GET /scrape/cron` answers.

        `enabled` (live) and `env_default` (boot) are reported SEPARATELY so an operator can see
        that a running override differs from what a restart would give them — the runtime toggle
        deliberately does not rewrite the env.
        """
        return {
            "enabled": self.enabled,
            "env_default": self.env_default,
            "schedule": self.spec_raw,
            "kind": ("interval" if self.schedule and self.schedule.interval else
                     "cron" if self.schedule else "invalid"),
            "error": self.error,
            "running": bool(self._thread and self._thread.is_alive()),
            "next_run": self.next_run,
            "next_run_iso": (time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(self.next_run))
                             if self.next_run else None),
            "last_run": self.last_run,
            "last_run_iso": (time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(self.last_run))
                             if self.last_run else None),
            "last_result": self.last_result,
            "runs": self.runs,
        }

    # --- the loop ---
    def _loop(self):
        while not self._stop:
            if not self.enabled or self.schedule is None:
                self.next_run = None
                self._wake.wait(60)          # poll slowly while disabled; a toggle sets the event
                self._wake.clear()
                if self.enabled:
                    self._recompute()
                continue
            if self.next_run is None:
                self._recompute()
                if self.next_run is None:
                    self.error = self.error or ("schedule %r matches no time within %d days"
                                                % (self.spec_raw, HORIZON_DAYS))
                    self._wake.wait(3600)
                    self._wake.clear()
                    continue
            wait = max(0.0, self.next_run - time.time())
            # Capped waits so a toggle, a clock change, or a shutdown is noticed promptly instead of
            # after however many hours the next firing happens to be away.
            if self._wake.wait(min(wait, 60)):
                self._wake.clear()
                self._recompute()
                continue
            if time.time() < self.next_run:
                continue
            self._fire()
            self._recompute()

    def _fire(self):
        self.last_run = time.time()
        self.runs += 1
        try:
            self.last_result = (self._submit or _default_submit)()
        except Exception as e:              # noqa: BLE001 — the timer must outlive one bad tick;
            self.last_result = {"error": str(e)}   # a dead scheduler thread would silently stop
                                                    # every future harvest with nothing to notice it


def _default_submit():
    """Queue one scrape+ingest job per watchlist domain. Imported lazily so this module stays
    importable (and unit-testable) without the serve package."""
    from wikikb.serve import jobs as jobsmod
    from wikikb.scrape import sources as srcmod
    doms = srcmod.domains(enabled_only=True)
    if not doms:
        return {"queued": [], "note": "watchlist is empty"}
    queued = []
    for d in doms:
        try:
            job, coalesced = jobsmod.submit_scrape(d, detail={"trigger": "cron"})
            queued.append({"domain": d, "job_id": job.id, "coalesced": coalesced})
        except RuntimeError as e:           # queue full — report it, keep scheduling the rest
            queued.append({"domain": d, "error": str(e)})
    return {"queued": queued}


SCHEDULER = Scheduler()
