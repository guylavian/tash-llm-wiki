---
title: Exchange's Active Directory Dependency — Migration, Restore, and Repointing
type: topic
domain: exchange
slug: exchange-ad-dependency-migration-restore
summary: Exchange stores its own configuration and per-recipient pointers inside Active Directory, so AD schema/forest migrations, DC restores, and DC repointing all carry a real risk of silently breaking Exchange — a coupling five separate community threads hit without a clean, vendor-confirmed fix.
sources:
  - web:https://learn.microsoft.com/en-us/answers/questions/1076916/exchange-migration-failure-active-directory-proper (Microsoft Q&A, fetched 2026-07-25)
  - web:https://learn.microsoft.com/en-us/answers/questions/1128493/how-to-properly-restore-a-domain-controller-and-ex (Microsoft Q&A, fetched 2026-07-25)
  - web:https://learn.microsoft.com/en-us/answers/questions/1168575/move-request-active-directory-homedb-property-does (Microsoft Q&A, fetched 2026-07-25)
  - web:https://learn.microsoft.com/en-us/answers/questions/1193796/migrating-active-directory-and-pointing-exchange-t (Microsoft Q&A, fetched 2026-07-25)
  - web:https://learn.microsoft.com/en-us/answers/questions/1371168/about-restoring-active-directory-when-restoring-ex (Microsoft Q&A, fetched 2026-07-25)
provenance_extracted: 8
provenance_inferred: 3
provenance_ambiguous: 1
tags: [exchange-recipients, migration, troubleshooting]
status: draft
updated: 2026-07-25
---

# Exchange's Active Directory Dependency — Migration, Restore, and Repointing

**Exchange isn't just a client of Active Directory — recipient mailbox pointers and
server topology settings live *inside* AD, so migrating, restoring, or repointing AD
without accounting for Exchange's dependency on it is a recurring, largely
unresolved source of tickets in the community.**

## Community Q&A (upstream)

All five threads below are Microsoft Q&A community threads, not vendor support
statements — **none of them has an accepted answer, and none of the questions carries an upvote** (one answer — the MVP reply in web:1193796 — did pick up a single upvote), so
treat every claim here as unverified community guidance to be checked against
vendor documentation, not a confirmed fix (inferred: this framing spans all five
threads, none of which states it explicitly).

### Migration: `homeMDB`/`homeDB` not writeable

Two threads hit the same error class during a cross-version mailbox move: an
Exchange 2016 on-prem migration failed with *"Active Directory property 'homeMDB'
is not writeable on recipient"* even after the asker toggled inheritable AD
permissions on the object, and the thread got no answer at all
(web:1076916). A near-identical error — *"Active Directory homeDB property does not
support recording in the recipient"* — hit an Exchange 2007→2013 `Move-Request` for
a subset of mailboxes, again after resetting ADUC permissions with no luck
(web:1168575). For the 1168575 thread, two respondents (a community user and a
Microsoft Moderator) converged on the same next step: confirm that **every server
running Exchange in the organization is a member of the `Exchange Servers` and
`Exchange Trusted Subsystem` security groups** in Active Directory Users and
Computers, under "Microsoft Exchange Security Groups" — group *membership* drift,
not object-level ACLs, was the thing to check (web:1168575). The Moderator's
follow-up also probed scope ("does this affect *some* or *all* mailboxes?") before
prescribing the fix, which matters diagnostically — a subset-only failure points at
an object/OU-level permission or group-membership gap rather than a
directory-wide misconfiguration. **Neither thread confirms the fix actually
resolved the error** — 1168575 has no accepted answer and 1076916 got no answer at
all, so it's plausible the two reports share a symptom but not a root cause
(inferred — the threads don't compare notes with each other).

### Repointing Exchange to a new AD server after an AD migration

After migrating to a new Windows Server 2019 AD environment, one admin found their
Exchange 2019 server's `DefaultGlobalCatalogsForAllForests`,
`DefaultPreferredDomainControllers`, and
`DefaultConfigurationDomainControllersForAllForests` settings still pointed at the
old AD server, even after already repointing `DefaultGlobalCatalog`,
`PreferredDomainControllerForDomain`, `DefaultConfigurationDomainController`, and
the `UserPreferred*` equivalents (web:1193796). An **MVP-affiliated** answer (the
strongest-weighted authorship in this whole theme) proposed explicit commands to
force the remaining settings:

```
Set-AdServerSettings -DefaultGlobalCatalog 'new-AD-server'
Set-AdServerSettings -PreferredServer 'new-AD-server'
Set-ExchangeServer -Identity 'your-Exchange-server' -StaticConfigDomainController 'new-AD-server'
```

(web:1193796) — but immediately caveated "please test before [applying]". A second
community reply directly **rebutted** this in the same thread: it claims
`Set-AdServerSettings` "has no modifiable default parameters," that hardcoding a
domain controller in Exchange is **not recommended**, that `Get-ExchangeServer | fl
Name,domain` should return `$null` on a healthy topology-following config, and that
the better verification is to shut down the old DC for a few days and watch for
Application-log **event ID 2080** to confirm Exchange auto-discovered the new DC
(web:1193796). **This is a genuine, unresolved disagreement** between an
MVP-authored answer and a community rebuttal in the same thread — see
Contradictions below (ambiguous).

### Restoring a DC (and Exchange) from backup

One admin running 3 DCs (one holding all FSMO roles) alongside Exchange 2013, ahead
of a planned migration to Exchange 2019, asked whether rolling back *just* the
FSMO-role DC via Windows Server Backup authoritative restore would be enough to
undo a failed migration, or whether *all* DCs would need rolling back — reasoning
(their own, unconfirmed premise) that "Exchange stores the configuration on the
controller" (web:1128493). **The thread got no answer.** A related, later thread
asked essentially the reverse question after an in-place 2013→2019 upgrade and
2013 uninstall: could you get back to 2013 by restoring **Active Directory itself**
alongside an Exchange 2013 backup? The asker had previously been told (in a linked,
separate thread) that uninstalling Exchange 2013 deletes the AD attributes/
containers Exchange used, so restoring Exchange alone likely wouldn't work — an
"in-house expert" then suggested that restoring **AD together with** the Exchange
2013 backup could restore the original state (web:1371168). The only reply is the
asker's own follow-up, thanking an off-thread contact and stating the AD-backup
approach is *"theoretically"* workable *if* Active Directory is healthy — but
explicitly **untested**, to be tried in a dev environment first (web:1371168). No
thread in this theme reaches a confirmed, reproduced fix for a DC/AD restore
alongside Exchange.

## Body

Across all five threads, the underlying shape is the same: Exchange extends the AD
schema at install and keeps its own configuration container plus per-recipient
attributes (`homeMDB`/`homeDB`, DC/GC preference settings) inside the directory,
and membership in the `Exchange Servers`/`Exchange Trusted Subsystem` security
groups gates whether an Exchange server can read/write those objects — so an AD-side
change (a forest/domain migration, a DC restore, or simply repointing Exchange at a
different DC) can silently break Exchange in ways that only surface later, on a
specific operation like a mailbox move or a Send/Receive attempt (inferred —
stitched from the pattern common to all five threads, not stated as a unified rule
by any one of them). None of the five threads produced a Microsoft-employee-
authored, accepted, or reproduced-working answer; the strongest single piece of
evidence is the MVP-affiliated command set in web:1193796, and even that drew an
immediate community rebuttal in the same thread.

## Contradictions / caveats

**Ambiguous — hardcode vs. auto-discover the DC (web:1193796).** An MVP-affiliated
answer recommends explicitly setting `Set-AdServerSettings -DefaultGlobalCatalog` /
`-PreferredServer` and `Set-ExchangeServer -StaticConfigDomainController` to force
Exchange onto the new AD server, while a second community reply in the *same*
thread says Exchange should be left to auto-discover topology changes and that
hardcoding a DC is unsupported, offering `Get-ExchangeServer | fl Name,domain`
returning `$null` and Application event ID 2080 as the way to confirm auto-adoption
instead. Neither side is a Microsoft support statement; if you hit this, verify
against current Exchange Server documentation on Active Directory topology
discovery before hardcoding anything.

**Unresolved — `homeMDB`/`homeDB` not writeable (web:1076916, web:1168575).** Two
threads report the same error signature on different migration paths (2016 native
migration vs. 2007→2013 `Move-Request`); only one got a proposed fix (Exchange
security-group membership), and neither thread confirms the fix worked. Treat the
security-group check as a first thing to verify, not a guaranteed root cause.

**Untested — restoring AD alongside Exchange (web:1128493, web:1371168).** Neither
thread has a vendor-confirmed procedure for coordinating a DC/AD restore with an
Exchange restore or rollback; the only lead (web:1371168) is explicitly
self-described as theoretical and unconfirmed by its own author.

## See also
- [[exchange-overview]]
- [[exchange-recipient-types]]
- [[exchange-hybrid-deployment]]
- [[exchange-implementation-review]]
- [[global-catalog]]
- [[fsmo-roles]]
- [[ad-forest-recovery]]
