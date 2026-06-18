---
title: Active Directory — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: active-directory
slug: active-directory-implementation-review
summary: The evaluation lens / Map of Content for the active-directory brain — a rule → anti-pattern → symptom checklist over AD DS health (FSMO, replication, DNS, time/Kerberos) plus a symptom → likely-cause reverse index the SRE agent uses to turn an alert into a cause page.
sources:
  - note:_sources/active-directory/fsmo-roles.md
  - web:https://learn.microsoft.com/windows-server/identity/ad-ds/ (Microsoft Learn — AD DS, fetched 2026-06-18)
provenance:
  extracted: 0
  inferred: 9
  ambiguous: 0
tags: [directory-services, troubleshooting, concept]
status: draft
updated: 2026-06-18
---

# Active Directory — Implementation Review (Evaluation-Lens MOC)

**The evaluation lens and lookup surface for the `active-directory` domain.** It
indexes AD health pages into a forward checklist (rule → anti-pattern → symptom)
and a reverse index (symptom → likely cause) so an alert can be turned into a cause
page. This is the AD analogue of [[sso-implementation-review]]; grow it as pages
land via INGEST.

---

## How to use this page

Read each row left to right: the **Rule** column states what a healthy AD must do;
the **Anti-pattern** column states the common misconfiguration; the **Symptom**
column names the observable ticket it produces; the **Page** column links the cause
page. To diagnose, jump to the [Reverse index](#reverse-index--symptom--likely-cause).

---

## Health checklist (AD DS)

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Keep all five FSMO roles on reachable, healthy DCs; place the Infrastructure Master off a Global Catalog in a multi-domain forest | All roles dumped on one DC that later dies; Infrastructure Master left on a GC | New users/computers cannot be created; unresolved `S-1-5-…` SIDs in cross-domain ACLs | [[fsmo-roles]] |
| Maintain a coherent time hierarchy with the PDC Emulator as the domain authority (<5 min skew) | PDC Emulator down or syncing from a bad NTP source; member clocks drift | `KRB_AP_ERR_SKEW`, intermittent logon failures, ticket rejections | [[fsmo-roles]] |
| Ensure RID Master is online so DCs can refill RID pools | RID Master offline for an extended period | RID-pool-exhaustion warnings; object-creation failures | [[fsmo-roles]] |

> More rows land as `replication`, `ad-dns`, `group-policy`, and `ad-authn` pages
> are ingested.

---

## Reverse index — symptom → likely cause

| Observable symptom | Likely cause | Page |
|---|---|---|
| `KRB_AP_ERR_SKEW` / clock-skew logon failures | PDC Emulator / time hierarchy broken | [[fsmo-roles]] |
| "Cannot create user/computer", RID pool exhausted | RID Master unreachable | [[fsmo-roles]] |
| Stale unresolved SIDs across domains | Infrastructure Master on a GC (multi-domain) | [[fsmo-roles]] |

## See also
- [[active-directory-overview]]
- [[fsmo-roles]]
