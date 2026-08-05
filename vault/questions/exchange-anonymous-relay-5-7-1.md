---
title: "Why do my monitoring/scanner devices get \"550 5.7.1 Unable to relay\" and how do I fix it correctly?"
type: question
domain: exchange
slug: exchange-anonymous-relay-5-7-1
summary: A device that can't authenticate (scanner, monitoring tool, internal app) gets 550 5.7.1 Unable to relay because it's hitting a default Receive connector that doesn't grant anonymous-relay permissions; the fix is a dedicated, IP-restricted anonymous-relay Receive connector on Front End Transport — never adding relay rights to a default connector.
sources:
  - kb:exchange-exchange-servertoc-p1561-1600
  - kb:exchange-exchange-servertoc-p1841-1880
provenance:
  extracted: 6
  inferred: 1
  ambiguous: 0
question_tier: support-kb
tags: [exchange-mailflow, troubleshooting, security]
status: draft
updated: 2026-07-23
graph_community: "Exchange Server — Implementation Review (Evaluation-Lens MOC)"
---

# Why do my monitoring/scanner devices get "550 5.7.1 Unable to relay" and how do I fix it correctly?

⚠️ Out of corpus coverage — `exchange` holds `conceptual` only; this is a
`support-kb` question and that tier is not ingested; verify against the primary
source before treating this as a confirmed fix.

## Answer

**The device is being rejected by a Receive connector that has no anonymous-relay
permission for it — most likely a default connector, which is intentionally
restrictive.** The fix is a *dedicated* Receive connector scoped by IP, not a
change to a default connector.

**What the error means.** `5.7.1 Unable to relay` (or `Client was not
authenticated`) fires when "an application server or device is trying to relay
messages through Exchange" and either can't authenticate, or the target recipient
is restricted to authenticated senders
(`exchange-exchange-servertoc-p1841-1880.md:706-713`, extracted). You can reproduce
this manually with `telnet <server> 25` → `EHLO` → `MAIL FROM:` → `RCPT TO:`; a
successful anonymous relay returns `250 2.1.5 Recipient OK`, a blocked one returns
`550 5.7.1 Unable to relay` (`exchange-exchange-servertoc-p1561-1600.md:1865-1893`,
extracted).

**Why "just enable relay on the default connector" is the wrong move.** Open relay
— any source able to transparently re-route mail through your server — is
actively sought out by spammers and is exactly what an unrestricted relay-capable
connector becomes. The doc is explicit: **"Don't attempt to add anonymous relay
capability to the default Receive connectors that are created by Exchange"**
(`exchange-exchange-servertoc-p1561-1600.md:1518-1526`, extracted). Anonymous relay
is a legitimate, common need (internal web servers, monitoring tools, scanners
that can't authenticate) — it just has to be scoped to a dedicated connector.

**The correct procedure**
(`exchange-exchange-servertoc-p1561-1600.md:1518-1594`, extracted):

1. Create a **new, dedicated Receive connector** in the **Front End Transport
   service** (not the Transport service — Transport's own default connector
   listens on TCP 2525 for intra-org traffic and isn't the right place for this).
2. Restrict it to the specific network hosts (by IP) that legitimately need to
   relay — the connector with the most specific IP match wins when multiple
   connectors could apply on TCP 25.
3. Grant the minimum required permissions. Two ways: (a) add the `Anonymous`
   permission group plus `Ms-Exch-SMTP-Accept-Any-Recipient` to the `NT
   AUTHORITY\ANONYMOUS LOGON` principal, or (b) grant
   `ms-Exch-Accept-Headers-Routing`, `ms-Exch-SMTP-Accept-Any-Recipient`,
   `ms-Exch-SMTP-Accept-Any-Sender`, `ms-Exch-SMTP-Accept-Authoritative-Domain-Sender`,
   and `ms-Exch-SMTP-Submit` directly. Example from the source:
   ```powershell
   Set-ReceiveConnector "Anonymous Relay" -PermissionGroups AnonymousUsers
   ```
   (`exchange-exchange-servertoc-p1561-1600.md:1775`, extracted).
4. Note the tradeoff: hosts relaying anonymously through this connector are
   treated as anonymous senders, so their mail does **not** bypass antispam or
   message-size checks, and the sender address can't be resolved to a
   corresponding mailbox (`exchange-exchange-servertoc-p1561-1600.md:1576-1594`,
   extracted). If you instead want the device authenticated as a specific internal
   sender, use the client-submission/authenticated-relay pattern rather than the
   `AnonymousUsers` permission group (inferred — the source names this as the
   distinguishing tradeoff but doesn't spell out the alternative connector config
   in the range read; verify against "Client submission examples" in the same
   guide before implementing).

**Distinguishing from a different NDR.** If the recipient — not the sending
device — is the one restricted, you'll see the *same* `5.7.1` code but the cause
is "the recipient is configured to only accept messages from authenticated
(typically, internal) senders," which is a message-delivery-restriction setting
on the recipient's mailbox, not a Receive connector problem
(`exchange-exchange-servertoc-p1841-1880.md:710-713`, extracted). Check which side
(connector vs. recipient) before troubleshooting further — the log/NDR reason
text disambiguates.

## Contradictions / caveats
None found between the two sources; both describe the same 2016/2019/SE relay
model.

## References

**RH ground-truth (kb:)**
- `exchange-exchange-servertoc-p1561-1600` — "Use Telnet to test SMTP
  communication on Exchange servers" / "Allow anonymous relay on Exchange
  servers"
- `exchange-exchange-servertoc-p1841-1880` — enhanced SMTP status code reference
  table (permanent delivery failures)

**Wiki**
- [[exchange-mail-queues]] — queue types and NDR-code troubleshooting
- [[exchange-transport-pipeline]] — Front End Transport vs Transport service,
  why the dedicated connector must live in Front End Transport
- [[exchange-implementation-review]] — mail-flow rule/anti-pattern/symptom table

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[exchange-exchange-servertoc-p1561-1600|Exchange Server — pages 1561-1600]]
- [[exchange-exchange-servertoc-p1841-1880|Exchange Server — pages 1841-1880]]
<!-- crosslink:end -->
