#!/usr/bin/env bash
# claude-marathon.sh — run a long Claude Code task, survive usage-limit cuts.
#
# Usage — lives in _meta/ but must still be RUN FROM THE REPO ROOT: the log and the
# `_meta/DEEP-RESEARCH-STATE.md` checkpoint path below are both relative to the cwd.
#   _meta/claude-marathon.sh          # research only
#   _meta/claude-marathon.sh fix      # research + implement P0 fixes
#
# What it does:
#   1. Starts `claude -p "/deep-research-wiki ..."` on Sonnet.
#   2. If the run dies on a usage limit, parses the reset time from the
#      "...limit reached|<epoch>" message and sleeps until then (+2 min).
#   3. Probes with a cheap Haiku "ping" until the API answers again.
#   4. Resumes the SAME session with --continue; the command's checkpoint
#      file (_meta/DEEP-RESEARCH-STATE.md) makes the resume cheap.
#   5. Stops only when the agent prints <<DEEP-RESEARCH-COMPLETE>>.
#
# NOTE: uses --dangerously-skip-permissions so the run is unattended.
# Run it only inside this repo, on a branch.

set -u
ARGS="${*:-}"
CMD="/deep-research-wiki${ARGS:+ $ARGS}"
MODEL="sonnet"            # cheap by default; never opus
PROBE_MODEL="haiku"       # cheapest probe
SENTINEL="<<DEEP-RESEARCH-COMPLETE>>"
LOG="deep-research-$(date +%Y%m%d-%H%M%S).log"
MAX_ITER=200
FALLBACK_WAIT=900         # 15 min when no reset timestamp is parseable
PROBE_INTERVAL=600        # re-probe every 10 min while still limited
BUFFER=120                # safety margin after the reset epoch

run_claude() {            # $1 = prompt, $2 = new|continue
  local flags=(-p --model "$MODEL" --dangerously-skip-permissions)
  [ "$2" = "continue" ] && flags+=(--continue)
  claude "${flags[@]}" "$1" 2>&1
}

probe() { claude -p --model "$PROBE_MODEL" "ping" >/dev/null 2>&1; }

wait_for_limits() {
  local out="$1" epoch now wait
  # Claude Code headless prints e.g. "Claude AI usage limit reached|1789000000"
  epoch=$(grep -oE 'limit reached\|[0-9]+' <<<"$out" | grep -oE '[0-9]+$' | head -1)
  if [ -n "${epoch:-}" ]; then
    now=$(date +%s)
    wait=$(( epoch - now + BUFFER ))
    (( wait < 60 )) && wait=60
    echo "[marathon] limit hit — reset at $(date -d "@$epoch" 2>/dev/null || echo "epoch $epoch"); sleeping ${wait}s" | tee -a "$LOG"
    sleep "$wait"
  else
    echo "[marathon] limit hit — no reset time found; sleeping ${FALLBACK_WAIT}s" | tee -a "$LOG"
    sleep "$FALLBACK_WAIT"
  fi
  until probe; do
    echo "[marathon] still limited; probing again in ${PROBE_INTERVAL}s" | tee -a "$LOG"
    sleep "$PROBE_INTERVAL"
  done
  echo "[marathon] limits are back — resuming" | tee -a "$LOG"
}

mode="new"
for i in $(seq 1 "$MAX_ITER"); do
  echo "[marathon] iteration $i ($mode) — $(date)" | tee -a "$LOG"
  if [ "$mode" = "new" ]; then
    out=$(run_claude "$CMD" new); rc=$?
  else
    out=$(run_claude "Resume: read _meta/DEEP-RESEARCH-STATE.md and continue from the recorded step. Do not redo completed steps." continue); rc=$?
  fi
  printf '%s\n' "$out" >> "$LOG"

  if grep -qF "$SENTINEL" <<<"$out"; then
    echo "[marathon] DONE after $i iteration(s). Log: $LOG"
    exit 0
  fi

  if [ $rc -ne 0 ] || grep -qiE 'usage limit|rate.?limit|limit reached|overloaded|credit balance' <<<"$out"; then
    wait_for_limits "$out"
  else
    # Ended without sentinel and without a limit message (context cut, crash) — just resume.
    echo "[marathon] session ended without sentinel (rc=$rc) — resuming in 30s" | tee -a "$LOG"
    sleep 30
  fi
  mode="continue"
done

echo "[marathon] hit MAX_ITER=$MAX_ITER without sentinel — check $LOG"
exit 1
