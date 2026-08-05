---
title: Exchange Server — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: exchange
slug: exchange-implementation-review
summary: The evaluation lens and Map of Content for the exchange brain — a rule → anti-pattern → symptom checklist across mail flow, queues, recipients, DAG/HA, client access, certificates, anti-spam/malware, and hybrid, plus a symptom → likely-cause reverse index.
sources:
  - kb:exchange-exchange-servertoc-p1521-1560
  - kb:exchange-exchange-servertoc-p1721-1760
  - kb:exchange-exchange-servertoc-p1841-1880
  - kb:exchange-exchange-servertoc-p1561-1600
  - kb:exchange-exchange-servertoc-p2601-2640
  - kb:exchange-exchange-servertoc-p0241-0280
  - kb:exchange-exchange-servertoc-p2921-2960
  - kb:exchange-exchange-servertoc-p3041-3080
provenance:
  extracted: 4
  inferred: 18
  ambiguous: 0
tags: [exchange-mailflow, exchange-ha, troubleshooting, security]
status: draft
updated: 2026-07-23
graph_community: "Exchange Server — Implementation Review (Evaluation-Lens MOC)"
---

# Exchange Server — Implementation Review (Evaluation-Lens MOC)

**The evaluation lens and lookup surface for the `exchange` domain.** It indexes
mail-flow, HA, and security health into a forward checklist (rule → anti-pattern →
symptom) and a reverse index (symptom → likely cause), mirroring
[[active-directory-implementation-review]] and [[sso-implementation-review]]. Grow
it as more of `reference/exchange/` is synthesized.

---

## How to use this page

Read each row left to right: **Rule** states what a healthy Exchange deployment
must do; **Anti-pattern** states the common misconfiguration; **Symptom** names
the observable ticket it produces; **Page** links the cause page. To diagnose,
jump to the [Reverse index](#reverse-index--symptom--likely-cause).

---

## Health checklist

### Mail flow and transport

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Create an explicit outbound Send connector before expecting Internet mail flow — none exists by default | Assuming outbound mail "just works" after install; no Send connector created | Outbound mail silently never leaves the organization | [[exchange-transport-pipeline]] |
| Match a Send connector's HELO/EHLO FQDN to the domain's public MX record | Send connector FQDN left blank/mismatched from MX; DNS-vs-smart-host routing misconfigured | `4.4.7` "Message delayed"/"Queue expired" NDRs | [[exchange-mail-queues]], [[exchange-transport-pipeline]] |
| Scope Receive connector relay permissions tightly to known internal/application hosts | Application server sends anonymous mail against a connector that doesn't permit relay from it | `550 5.7.1 Unable to relay` | [[exchange-mail-queues]] |
| Clear stale Outlook autocomplete entries after recreating a deleted mailbox | Mailbox deleted and recreated; users still address old X.500/LegacyExchangeDN cache entries | `5.1.1 User unknown` / `RESOLVER.ADR.ExRecipNotFound` NDRs | [[exchange-mail-queues]] |
| Monitor and manually clear the poison message queue — it never self-resolves | Poison message queue ignored because it's "usually empty" and doesn't surface in queue tools until populated | Messages stuck indefinitely; server/service instability traced to a bad message | [[exchange-mail-queues]] |

### Recipients

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use explicit recipient types (not ad hoc AD group edits) so EAC/Shell bulk operations and permission scoping stay correct | Mail-enabled group edited directly in AD without going through Exchange management, or a non-universal mail group assumed creatable in modern Exchange | Recipient doesn't appear/behave as expected in EAC; group mail-enabling silently fails | [[exchange-recipient-types]] |
| Grant the narrowest delegate permission that satisfies the need (Send on Behalf < Send As < Full Access) | Full Access granted where Send As or Send on Behalf Of would suffice | Delegate can read/modify mailbox contents beyond what the task required | [[exchange-recipient-types]] |

### High availability (DAG)

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Keep all DAG members on the identical Exchange version | Mixing Exchange versions across DAG members (e.g. 2013 and 2016) | DAG creation/member-add fails or replication breaks | [[exchange-database-availability-groups]] |
| Size and monitor the underlying failover cluster's quorum | Witness server unreachable, network partition, or insufficient voters left standing | Cluster loses quorum; **every mounted database in the DAG dismounts** | [[exchange-database-availability-groups]] |
| Never enable Windows NLB on a server that's also a DAG member | Windows Network Load Balancing enabled alongside Microsoft Clustering Services on the same Mailbox server | Clustering/DAG functionality breaks — the two services cannot coexist | [[exchange-database-availability-groups]], [[exchange-client-access-namespace]] |
| Set `AutoDatabaseMountDial` deliberately, not left at a default that doesn't match your replication topology | `AutoDatabaseMountDial` left at a setting that mounts a passive copy before logs have caught up | Data loss window after failover / unexpected mount behavior | [[exchange-database-availability-groups]] |

### Client access and certificates

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use one SSL certificate consistently across all Client Access-hosting Mailbox servers so login cookies decrypt anywhere | Different certificates per server; load balancer routes a resumed session to a server that can't decrypt the cookie | Users unexpectedly re-prompted for credentials on failover/reconnect | [[exchange-client-access-namespace]], [[exchange-certificates]] |
| Choose SAN vs wildcard certificates deliberately based on how many hostnames/subdomain levels you actually publish | Wildcard cert assumed to cover a different subdomain level, or a SAN cert issued without a needed hostname | TLS validation failure on a published service URL | [[exchange-certificates]] |
| Validate Autodiscover SCP publishing and connectivity from both internal and external/wireless networks | SCP `ServiceBindingInfo` FQDN not reachable from the network client is actually on | Outlook/ActiveSync clients fail to auto-configure | [[exchange-client-access-namespace]] |

### Anti-spam / anti-malware

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Order SCL thresholds correctly (Delete > Reject > Quarantine > Junk Email folder) | Threshold values set out of order, or a mailbox-level override silently masking the org policy | Legitimate mail deleted instead of quarantined, or spam bypassing filtering entirely | [[exchange-antispam-antimalware]] |
| Keep the Malware Agent's engine/definition updates flowing (hourly, outbound TCP 80) | Outbound HTTP to Microsoft's update endpoint blocked by firewall | Stale malware definitions; new malware not caught | [[exchange-antispam-antimalware]] |

### Hybrid

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Move fully to Hybrid Modern Auth once Exchange Hybrid is configured, rather than running legacy ADFS-based Modern Auth alongside it | ADFS-based Modern Auth left in place after enabling Exchange Hybrid instead of migrating to HMA | Inconsistent/duplicate auth prompts; hybrid auth edge cases | [[exchange-hybrid-deployment]] |
| Re-run the Hybrid Configuration Wizard after any Auth-relevant change | HCW run once at initial hybrid setup and never revisited | Hybrid free/busy or mail flow breaks silently after an auth-side change | [[exchange-hybrid-deployment]] |

---

## Reverse index — symptom → likely cause

| Observable symptom | Likely cause | Page(s) |
|---|---|---|
| `550 5.7.1 Unable to relay` | Receive connector doesn't permit relay from the source host/network | [[exchange-mail-queues]] |
| `550 5.1.1 User unknown` / `RESOLVER.ADR.ExRecipNotFound` | Recipient address wrong, or stale Outlook autocomplete entry after mailbox recreation | [[exchange-mail-queues]] |
| `4.4.7` — "Message delayed" / "Queue expired" NDR | Send connector routing (DNS vs smart host) misconfigured, or HELO/EHLO FQDN mismatched from the public MX record | [[exchange-mail-queues]], [[exchange-transport-pipeline]] |
| `poison message queue` non-empty and growing | A malformed message or a buggy transport agent is crashing message processing | [[exchange-mail-queues]] |
| Cluster loses quorum / mass database dismount across a DAG | Witness server unreachable or network partition beneath the DAG's failover cluster | [[exchange-database-availability-groups]] |
| DAG creation or member add fails | Mixed Exchange versions across DAG members | [[exchange-database-availability-groups]] |
| Clustering/DAG breaks after enabling NLB on a Mailbox server | Windows NLB and Microsoft Clustering Services enabled on the same server (unsupported combination) | [[exchange-database-availability-groups]], [[exchange-client-access-namespace]] |
| Users re-prompted for credentials on load-balancer failover | Client Access-hosting servers using different SSL certificates | [[exchange-client-access-namespace]], [[exchange-certificates]] |
| `Content Filter agent quarantined` a legitimate message | SCL Quarantine threshold set too low, or mailbox-level SCL override misconfigured | [[exchange-antispam-antimalware]] |
| Malware definitions stale / new malware not caught | Outbound TCP 80 to the definition-update endpoint blocked | [[exchange-antispam-antimalware]] |
| Hybrid free/busy or mail flow breaks after an auth change | Hybrid Configuration Wizard not re-run after an Auth-relevant change | [[exchange-hybrid-deployment]] |

---

## Domain map — pages by area

### Mail flow
- [[exchange-transport-pipeline]] — Front End/Transport/Mailbox Transport/Edge services, connectors
- [[exchange-mail-queues]] — queue types, ESE queue database, NDR codes

### Recipients
- [[exchange-recipient-types]] — recipient types, delegate permissions

### High availability
- [[exchange-database-availability-groups]] — DAG, Active Manager, quorum, activation preference

### Client access and security
- [[exchange-client-access-namespace]] — session affinity, load balancing, Autodiscover
- [[exchange-certificates]] — certificate sourcing and identity-matching methods
- [[exchange-antispam-antimalware]] — Content Filter SCL, Malware Agent

### Migration
- [[exchange-hybrid-deployment]] — HCW, Microsoft Entra Connect, Hybrid Modern Auth

## See also
- [[exchange-overview]] — domain primer, architecture, spine
- [[active-directory-implementation-review]] — Active Directory domain equivalent of this MOC
- [[sso-implementation-review]] — Keycloak / SSO domain equivalent of this MOC

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[exchange-exchange-servertoc-p1521-1560|Exchange Server — pages 1521-1560]]
- [[exchange-exchange-servertoc-p1721-1760|Exchange Server — pages 1721-1760]]
- [[exchange-exchange-servertoc-p1841-1880|Exchange Server — pages 1841-1880]]
- [[exchange-exchange-servertoc-p1561-1600|Exchange Server — pages 1561-1600]]
- [[exchange-exchange-servertoc-p2601-2640|Exchange Server — pages 2601-2640]]
- [[exchange-exchange-servertoc-p0241-0280|Exchange Server — pages 241-280]]
- [[exchange-exchange-servertoc-p2921-2960|Exchange Server — pages 2921-2960]]
- [[exchange-exchange-servertoc-p3041-3080|Exchange Server — pages 3041-3080]]
<!-- crosslink:end -->
