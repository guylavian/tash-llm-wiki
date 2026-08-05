---
title: Why does content distribution to a remote distribution point fail with error 0x8007052e?
type: question
domain: sccm
slug: sccm-content-distribution-fails-0x8007052e
summary: distmgr.log shows CContentDefinition::TotalFileSizes / CSendFileAction::SendFiles / CSendFileAction::SendContent all failing with 0x8007052e, paired with Event ID 4625 on the content-library host, because Configuration Manager incorrectly uses the remote site system's Site System Installation Account to authenticate to the remote content library share — the documented workaround is a matching local account on that server, not a content-library rebuild.
sources:
  - kb:sccm-troubleshoot-mem-configmgr-p0121-0160
provenance_extracted: 6
provenance_inferred: 1
provenance_ambiguous: 0
question_tier: support-kb
tags: [troubleshooting, sccm-core]
status: draft
updated: 2026-07-23
graph_community: "Configuration Manager (SCCM) — Implementation Review (Evaluation-Lens MOC)"
---

# Why does content distribution to a remote distribution point fail with error 0x8007052e?

**`distmgr.log` logs a chain of three failures — `CContentDefinition::TotalFileSizes failed;
0x8007052e`, `CSendFileAction::SendFiles failed; 0x8007052e`, `CSendFileAction::SendContent
failed; 0x8007052e` — because Configuration Manager authenticates to the *remote* content library
share using the wrong account: it incorrectly reuses the Site System Installation Account
configured for the remote site system, which that server's local security doesn't recognize
(extracted, `sccm-troubleshoot-mem-configmgr-p0121-0160.md:17-21,46-48`).**

## Body

### The observed signal

The error chain appears verbatim in `distmgr.log`:

```
CContentDefinition::TotalFileSizes failed; 0x8007052e
CSendFileAction::SendFiles failed; 0x8007052e
CSendFileAction::SendContent failed; 0x8007052e
```
(`sccm-troubleshoot-mem-configmgr-p0121-0160.md:17-21`)

Alongside it, **Event ID 4625** (a Security-log logon failure, Audit Failure) is recorded on the
server hosting the content library, naming the account that failed to log on
(`sccm-troubleshoot-mem-configmgr-p0121-0160.md:23-38`). The note explicitly flags that the
account shown in that event — `FABRIKAM\<AccountName>` in the example — represents the **Site
System Installation Account** for the remote DP, not an ordinary user
(`sccm-troubleshoot-mem-configmgr-p0121-0160.md:41-44`).

### Root cause

The note states the cause directly: **"This issue occurs because Configuration Manager
incorrectly uses the Site System Installation Account for the remote site system to connect to
the remote content library."** (extracted, `sccm-troubleshoot-mem-configmgr-p0121-0160.md:46-48`).
It is a Configuration Manager authentication-path bug, not a network, permissions-design, or
content-corruption problem — so re-running content distribution, checking firewall rules, or
rebuilding the content library will not fix it.

### The documented workaround

1. Create a **local account** on the server that hosts the content library
   (`sccm-troubleshoot-mem-configmgr-p0121-0160.md:55`).
2. Give that local account the **same name** as the Site System Installation Account configured
   for the remote site system (`sccm-troubleshoot-mem-configmgr-p0121-0160.md:56-57`).
3. Grant that new local account access to the content library folder
   (`sccm-troubleshoot-mem-configmgr-p0121-0160.md:58`).

This enables pass-through (local-account) authentication instead of the mis-targeted domain
account, working around the failure
(`sccm-troubleshoot-mem-configmgr-p0121-0160.md:60-61`).

If `DistMgr.log` instead shows **SQL Server authentication** errors (not just content-library file
transfer errors), the note points to a related, separate workaround for the site system
installation account being misused against the **SQL Server database** connection rather than the
content-library share (inferred — the note treats these as two distinct symptoms of the same
underlying account-misuse class: `sccm-troubleshoot-mem-configmgr-p0121-0160.md:63-65`).

## Contradictions / caveats

The corpus does not give a fixed-in-version note for this issue — it's filed as a workaround, not
a resolved bug, so it should be re-tested on newer Configuration Manager builds before assuming
it's still required. `tiers-covered: [conceptual, support-kb]` for `sccm` per `_meta/taxonomy.md`
— this question is `support-kb` tier (a documented known issue), which **is** covered, so no
out-of-coverage banner applies.

## See also
- [[sccm-distribution-points]]
- [[sccm-site-hierarchy]]
- [[sccm-implementation-review]]

## References

**RH ground-truth:**
- `kb:sccm-troubleshoot-mem-configmgr-p0121-0160` — Configuration Manager troubleshooting, "Welcome — pages 121-160" (content distribution failures, cause, and workaround)

**Wiki pages:**
- [[sccm-distribution-points]] — content library, boundary groups, and this failure signature
- [[sccm-implementation-review]] — reverse index entry for `0x8007052e` / Event 4625

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[sccm-troubleshoot-mem-configmgr-p0121-0160|Welcome — pages 121-160]]
<!-- crosslink:end -->
