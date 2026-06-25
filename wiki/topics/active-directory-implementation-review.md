---
title: Active Directory — Implementation Review (Evaluation-Lens MOC)
type: topic
domain: active-directory
slug: active-directory-implementation-review
summary: The evaluation lens and Map of Content for the active-directory brain — a rule → anti-pattern → symptom checklist across AD DS health areas (FSMO, replication, DNS, time/Kerberos, security/credential-theft, deployment/upgrade, virtualization/USN-rollback, LDAP hardening) plus a symptom → likely-cause reverse index the SRE agent uses to turn an alert into a cause page.
sources:
  - note:_sources/active-directory/fsmo-roles.md
  - web:https://learn.microsoft.com/windows-server/identity/ad-ds/ (Microsoft Learn — AD DS, fetched 2026-06-18)
provenance_extracted: 0
provenance_inferred: 62
provenance_ambiguous: 0
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

### FSMO roles

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Keep all five FSMO roles on reachable, healthy DCs; place Infrastructure Master off a GC in multi-domain forests | All roles dumped on one DC that dies; Infrastructure Master left on a GC | New users/computers cannot be created; unresolved `S-1-5-…` SIDs in cross-domain ACLs | [[fsmo-roles]] |
| Maintain a coherent time hierarchy with PDC Emulator as domain authority (<5 min skew) | PDC Emulator down or syncing from a bad NTP source; member clocks drift | `KRB_AP_ERR_SKEW`, intermittent logon failures, Kerberos ticket rejections | [[fsmo-roles]], [[windows-time-service]] |
| Keep RID Master online so DCs can refill RID pools before exhaustion | RID Master offline for extended periods; RID block size inflated with Unlock-ADAccount scripts | `Directory-Services-SAM` event 16656/16657/16658; "cannot allocate RID" object-creation failures | [[fsmo-roles]], [[rid-issuance-management]] |
| Schema Master and Domain Naming Master must be reachable during schema changes and domain add/remove | Schema Master offline during `adprep`; Domain Naming Master offline when adding a child domain | `adprep /forestprep` fails; `dcpromo` cannot add application partitions | [[fsmo-roles]], [[adprep-and-schema-updates]] |
| Seize (not transfer) FSMO roles only when the original holder is permanently lost; run metadata cleanup afterward | Role seizure without metadata cleanup leaves orphaned NTDS Settings objects | Lingering replication errors; misleading `netdom query fsmo` output | [[fsmo-roles]], [[ad-metadata-cleanup]] |

### Replication

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Size site links to reflect actual WAN costs; set replication schedules that allow changes to converge within an acceptable window | Default cost of 100 on all site links; 15-minute schedule across a slow WAN | Inter-site replication latency; password changes not propagating before Kerberos ticket expiry | [[site-links-and-replication-schedule]], [[ad-replication]] |
| KCC must produce valid connection objects between DCs in every site | Broken IP connectivity between sites; firewall blocking TCP 135 / RPC dynamic ports | `repadmin /showrepl` shows error 1753 (endpoint mapper); replication event 1396 | [[ad-replication]] |
| Remove lingering objects promptly; do not allow long-lived replication failures to accumulate divergent state | DC isolated from replication for longer than tombstone lifetime; snapshots applied to DCs outside hypervisor-aware tools | Event ID 1988 lingering objects; `repadmin /removelingeringobjects` required | [[ad-replication]], [[virtualized-domain-controllers]] |
| Use GC placement in each site to avoid cross-site GC lookups at logon | Single GC in headquarters; branch offices rely on WAN for GC contact | Slow logon across WAN; logon failures when WAN is down without UGMC enabled | [[global-catalog]], [[universal-group-membership-caching]] |
| Enable Universal Group Membership Caching in sites without a GC to tolerate GC outage | Sites without GC and without UGMC; UGMC enabled but cache refresh interval too long | Users cannot log on when GC unreachable; stale group membership resolving during logon | [[universal-group-membership-caching]], [[global-catalog]] |

### DNS

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Every DC must register SRV records under `_msdcs.<forest-root>` and be resolvable by all other DCs | DNS delegation for `_msdcs` missing; DCs pointing at non-AD-aware DNS servers | "No logon servers available"; DC Locator returns `ERROR_NO_SUCH_DOMAIN`; Event ID 2088 | [[dns-for-ad-ds]], [[dc-locator]] |
| All DCs should host or forward to AD-integrated DNS zones; zone replication scope must cover all DCs in forest | Standalone DNS server hosting AD zones with no AD integration; zone replication scoped to domain-only when forest-wide access is needed | DC cannot locate DCs in other domains; cross-forest trusts break on name resolution | [[dns-for-ad-ds]], [[dns-infrastructure-design]] |
| Primary DNS suffix must match the AD domain name (contiguous namespace); disjoint namespace requires explicit policy | Member computers joined with wrong primary DNS suffix; no `msDS-AllowedDNSSuffixes` policy set | SPN mismatches; LDAPS certificate hostname mismatch; Kerberos name-suffix routing broken | [[disjoint-namespace]], [[spn-and-upn-uniqueness]] |

### Time and Kerberos

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Configure the PDC Emulator to sync from a reliable external NTP source; all other DCs sync from the domain hierarchy | PDC Emulator syncing from its own VM host clock or a stratum-1 with high drift; `w32tm /resync /force` not run after PDC seizure | `KRB_AP_ERR_SKEW` (0x25); `STATUS_LOGON_FAILURE` with "time skew" detail | [[windows-time-service]], [[fsmo-roles]] |
| All domain-joined machines must stay within 5 minutes of DC time; configure GPO NTP policy explicitly | NTP GPO not applied to a subset of machines; VM snapshots restoring stale clocks | Intermittent Kerberos failures affecting only some machines; TGS requests rejected | [[windows-time-service]] |
| SPNs must be unique forest-wide; UPNs must be unique per UPN suffix | Duplicate SPNs set by legacy provisioning scripts; migrating accounts without SPN cleanup | Error 8467 / `ERROR_DS_SPN_VALUE_NOT_UNIQUE_IN_FOREST`; excessive LSASS CPU; Entra ID sync breaks | [[spn-and-upn-uniqueness]] |
| Reset `krbtgt` password twice (24h apart) as part of forest recovery or post-compromise remediation | Single reset of `krbtgt`; resetting too fast without waiting for replication convergence | Clients with valid TGTs cached from old key cannot authenticate until tickets expire; logon failures during the rotation window | [[krbtgt-reset]], [[ad-forest-recovery]] |

### Security / Credential theft

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Implement a three-tier administration model; Tier 0 credentials must never touch Tier 1/2 hosts | DA accounts used for daily workstation administration; jump servers shared across tiers | Pass-the-hash lateral movement from compromised workstation leads to DC access | [[tiered-administration-model]], [[credential-theft-and-attractive-accounts]] |
| Admin workstations must be dedicated, hardened hosts with no internet access or general productivity software | DA logged into shared terminal server; admins browsing the web from a host that also runs `ldp.exe` | Drive-by download on admin host; pass-the-hash via compromised jump server | [[secure-administrative-hosts]], [[tiered-administration-model]] |
| Minimize EA, DA, and BA group membership; use time-limited group membership for admin tasks | Hundreds of permanent DA accounts; service accounts running with DA rights; nested groups bloating BA | `DCSync` attack succeeds from a compromised DA; privilege escalation via overpopulated group | [[reducing-ad-attack-surface]], [[protected-accounts-and-groups]] |
| Enable Advanced Audit Policy on all DCs; monitor for high-value indicators of compromise | Legacy audit categories only; no forwarding to SIEM; `CrashOnAuditFail` not set | Event 4719 (audit disabled by attacker) missed; 84% of breaches had evidence in event logs not acted on | [[advanced-audit-policy]], [[monitoring-ad-for-compromise]] |
| Deploy software restriction policies / AppLocker on DCs and admin hosts to block unauthorized executables | No application allowlisting on DCs; web browser not restricted; legacy monitoring agents installed on DCs | Attacker tooling executed on DC after initial foothold; mimikatz runs unimpeded | [[software-restriction-policies]], [[secure-administrative-hosts]] |
| AdminSDHolder ACL is enforced every 60 min by SDProp; do not customize ACLs on protected groups directly | Custom delegation ACL set on a protected group; account removed from DA but `adminCount=1` orphan remains | SDProp overwrites custom ACL; OU-level delegation not applying to orphaned `adminCount=1` accounts | [[protected-accounts-and-groups]] |
| Monitor DA logons to non-DCs, unexpected group membership changes, and DCSync replication grants | No alerting on Event 4964 (special logon); no SIEM rule for Event 4728 (member added to DA) | Unauthorized access goes undetected; DCSync replication rights granted to non-DC account | [[monitoring-ad-for-compromise]], [[advanced-audit-policy]] |
| Enforce LDAP signing (`Require` at the DC) and LDAP channel binding before removing legacy clients | LDAP signing left at `None`; channel binding disabled to accommodate old scanners | Event ID 2886/2887 (unsigned LDAP); man-in-the-middle hijack of unsigned LDAP session | [[ldap-signing-and-channel-binding]] |
| Rotate local administrator passwords with Windows LAPS; never share a single local admin password across fleet | All machines share same built-in Administrator password; LAPS not deployed | Single compromised local admin hash enables lateral movement to entire fleet via pass-the-hash | [[windows-laps]] |

### Deployment and upgrade

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Run `adprep /forestprep` and `/domainprep` before introducing any DC at a higher OS version | Skipping `adprep` before adding first Server 2025 DC; running `adprep` as non-Schema Admin | `dcpromo`/`Install-ADDSDomainController` fails with schema version mismatch | [[adprep-and-schema-updates]], [[install-promote-domain-controller]] |
| Raise domain and forest functional levels only after all DCs are at or above the target OS version | FFL/DFL raised before demoting last legacy DC; FFL raised hoping it enables features not yet present | Functional level raise fails with "operation not allowed"; new features not available post-raise | [[ad-functional-levels]], [[upgrade-domain-controllers]] |
| Demote gracefully before decommissioning a DC; run metadata cleanup if forced removal was necessary | DC VM deleted without demotion; network cables pulled | Orphaned NTDS Settings object; `Access is denied` during subsequent metadata cleanup | [[demote-and-remove-dc]], [[ad-metadata-cleanup]] |
| Right-size DC hardware/VMs for domain object count and logon load; place at least two DCs per domain per site | Single DC per domain; DC RAM sized below `300 MB + (0.4 MB × number_of_objects)` baseline | LSASS paging on large domains; single DC failure causes site-wide logon outage | [[capacity-and-placement-planning]], [[ad-ds-deployment]] |
| Design OU structure to reflect administration, not org chart; apply delegation at OU level | OU hierarchy mirrors org chart, changes every quarter; delegation applied directly to objects | GPO link proliferation; delegation breaks on reorg; `adminCount=1` orphans from protected groups moved between OUs | [[ad-logical-structure-design]] |

### Virtualization and USN rollback

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Use only hypervisors that expose VM-GenerationID to DC guests; run Windows Server 2012+ as the guest OS | ESX/KVM not passing VMGenID; DC guest running Windows Server 2008 | USN rollback silent divergence; lingering objects accumulate without Event 2170 safeguard | [[virtualized-domain-controllers]], [[vm-generation-id-safe-restore]] |
| Never apply a hypervisor snapshot to a running DC without using safe-restore or VM-GenerationID-aware tooling | VMware snapshot applied to a running DC; snapshot rolled back to pre-join state | Event ID 2095 (`Dsa Not Writable = 0x4`); Event ID 1988 lingering objects from divergent USN | [[vm-generation-id-safe-restore]], [[virtualized-domain-controllers]] |
| Use VDC cloning (not snapshot) to rapidly provision additional DCs in a lab/DR scenario | Copying VHDX outside cloning workflow; deploying without `DCCloneConfig.xml` | Event ID 2162 (cloning failed); DC boots into DSRM instead of completing promotion | [[vdc-cloning]], [[virtualized-domain-controllers]] |

### LDAP hardening

| Rule | Anti-pattern | Symptom (observable fault) | Page |
|---|---|---|---|
| Require LDAP signing on all DCs (`ldapServerIntegrity = 2`); remove clients making unsigned simple binds | Legacy scanners or NAS appliances sending unsigned LDAP; signing left at `None` | Event 2886/2888 (highly vulnerable); MITM packet modification risk | [[ldap-signing-and-channel-binding]] |
| Enable LDAP channel binding on LDAPS connections; update clients to send CBT | SSL-wrapping LDAP proxy strips CBT; old .NET LDAP code not updated | Event 3039 (client does not support CBT); session hijack on LDAPS port 636 | [[ldap-signing-and-channel-binding]] |

---

## Reverse index — symptom → likely cause

Each signature is drawn from the `symptoms:` frontmatter of the referenced page.

| Observable symptom | Likely cause | Page(s) |
|---|---|---|
| `KRB_AP_ERR_SKEW` / `STATUS_LOGON_FAILURE` with time-skew detail | PDC Emulator clock drift or W32Time misconfiguration | [[windows-time-service]], [[fsmo-roles]] |
| "Cannot create user/computer", RID pool exhaustion — `Directory-Services-SAM` event 16656 / 16657 / 16658 | RID Master unreachable; RID pool inflated or global space near limit | [[rid-issuance-management]], [[fsmo-roles]] |
| Unresolved `S-1-5-…` SIDs in cross-domain ACLs | Infrastructure Master placed on a GC in a multi-domain forest | [[fsmo-roles]] |
| `replication.*1396` / `1753.*endpoint mapper` in DS event log | RPC endpoint mapper unreachable; broken site-link or firewall | [[ad-replication]] |
| `lingering object` / `repadmin /showrepl` reports USN rollback | DC isolated beyond tombstone lifetime; snapshot applied outside VMGenID-aware path | [[ad-replication]], [[virtualized-domain-controllers]] |
| `Event ID 2095.*previously acknowledged USN` / `Dsa Not Writable = 0x4` | USN rollback — snapshot applied to DC without VM-GenerationID safeguard | [[vm-generation-id-safe-restore]], [[virtualized-domain-controllers]] |
| `Event ID 2170.*Generation ID change has been detected` | VM snapshot or live-migration triggered safe-restore (informational, not an error) | [[vm-generation-id-safe-restore]] |
| `Event ID 1988.*lingering object` | Divergent USN after rollback or extended replication failure | [[virtualized-domain-controllers]], [[ad-replication]] |
| `Event ID 2162.*Virtual domain controller cloning failed` / boots to DSRM | VDC cloning prerequisites not met; `DCCloneConfig.xml` missing or malformed | [[vdc-cloning]] |
| `no logon servers available` / `DsGetDcName` failure / high DNS Query Failures/sec | SRV records not registered; `_msdcs` zone missing or unreachable | [[dc-locator]], [[dns-for-ad-ds]] |
| `Event ID 2088` (DNS event — DC could not be contacted via DNS) | `_msdcs` delegation missing; DNS server not AD-integrated | [[dns-for-ad-ds]] |
| `service logons fail` / SPN mismatch / LDAPS certificate hostname mismatch | Disjoint namespace — primary DNS suffix does not match AD domain name | [[disjoint-namespace]], [[spn-and-upn-uniqueness]] |
| Error 8467 / `ERROR_DS_SPN_VALUE_NOT_UNIQUE_IN_FOREST` / `event id 2974` | Duplicate SPN in forest; UPN collision | [[spn-and-upn-uniqueness]] |
| `pass-the-hash` / `pass-the-ticket` / `DCSync` / lateral movement alerts | Credential theft; DA credential cached on untrusted host; tier isolation not enforced | [[credential-theft-and-attractive-accounts]], [[tiered-administration-model]], [[secure-administrative-hosts]] |
| `privilege escalation` / DA group membership change (Event 4728) | Overpopulated DA/BA groups; protected group ACL bypassed | [[reducing-ad-attack-surface]], [[protected-accounts-and-groups]], [[monitoring-ad-for-compromise]] |
| `4719` (audit policy changed by attacker) / `STOP: C0000244` (audit failure crash) | Advanced audit policy not enforced; `CrashOnAuditFail` not set | [[advanced-audit-policy]] |
| DA account logged on to non-DC (Event 4964) / unauthorized service on DC | Tier 0 credentials used on Tier 1/2 host; no tiered admin policy | [[monitoring-ad-for-compromise]], [[tiered-administration-model]] |
| `unauthorized application installed on DC` / web browser launched on DC | No software restriction policy on DCs | [[software-restriction-policies]] |
| `Event ID 2886` / `2887` / `2888` (unsigned LDAP) | LDAP signing not enforced; legacy clients sending unsigned binds | [[ldap-signing-and-channel-binding]] |
| `Event ID 3039` / `3040` (channel binding token missing/mismatch) | LDAP channel binding not enabled; CBT stripped by SSL proxy | [[ldap-signing-and-channel-binding]] |
| `event 10031` / `STATUS_POLICY_CONTROLLED_ACCOUNT` / `0xC000A08B` | Windows LAPS policy error; LAPS password not rotated or expired | [[windows-laps]] |
| `adminCount=1` orphan — OU delegation not applying to account | Account removed from protected group but `adminCount` not cleared | [[protected-accounts-and-groups]] |
| `SDProp overwrites custom ACL` on privileged group | AdminSDHolder ACL being enforced every 60 min on customized group | [[protected-accounts-and-groups]] |
| `orphaned metadata.*NTDS Settings` / `Access is denied.*metadata cleanup` | DC forcibly removed without graceful demotion | [[demote-and-remove-dc]], [[ad-metadata-cleanup]] |
| `DNT limit reached` — `000020EF: SvcErr: DSID-0208044C problem 5012` | DC approaching 2.1 billion Distinguished Name Tag ceiling | [[ad-ds-maximum-limits]] |
| `0x00000b: LDAP_ADMIN_LIMIT_EXCEEDED` on group write | Nonlinked attribute (group membership) exceeding page limit on 8k DB | [[ad-ds-maximum-limits]], [[ad-database-and-32k-pages]] |
| `pass-the-hash lateral movement across member servers` / `DC compromise via unpatched application` | Attack surface not reduced; excessive privilege; unpatched OS | [[reducing-ad-attack-surface]], [[securing-active-directory]] |
| `forest-wide failure` / `all domain controllers` inoperable | Forest-level disaster; ransomware or bad schema change replicated everywhere | [[ad-forest-recovery]], [[krbtgt-reset]] |
| `adprep /forestprep` fails / schema version mismatch on DC promotion | `adprep` not run before first higher-version DC; run as non-Schema Admin | [[adprep-and-schema-updates]], [[install-promote-domain-controller]] |
| Functional level raise fails / new FL features not available | Legacy DC still in forest or domain at lower OS version | [[ad-functional-levels]], [[upgrade-domain-controllers]] |

---

## Domain map — pages by health area

### Foundation and structure
- [[active-directory-overview]] — domain model, objects, partitions, trust types
- [[ad-logical-structure-design]] — forest/domain/OU design principles
- [[forest-design-models]] — single vs. multiple forest models
- [[domain-design]] — domain planning and trust strategy
- [[organizational-unit-design]] — OU hierarchy and delegation design
- [[security-principals]] — users, groups, computers as security principals
- [[security-identifiers-sid]] — SID structure, well-known SIDs, SID history
- [[security-groups]] — scope (local/global/universal), nesting, token bloat
- [[special-identity-groups]] — Everyone, Authenticated Users, Creator Owner, etc.
- [[default-user-accounts]] — Administrator, Guest, KRBTGT built-ins

### Operations masters (FSMO)
- [[fsmo-roles]] — all five roles, placement, transfer, seize
- [[rid-issuance-management]] — RID pool lifecycle, global space safeguards

### Replication and topology
- [[ad-replication]] — multi-master model, connection objects, KCC, troubleshooting
- [[site-links-and-replication-schedule]] — cost, schedule, bridgeheads
- [[site-topology-design]] — site design principles, subnets, replication rings
- [[global-catalog]] — partial attribute set, GC placement per site
- [[universal-group-membership-caching]] — UGMC for sites without GC
- [[knowledge-consistency-checker]] — KCC algorithm and spanning tree

### DNS
- [[dns-for-ad-ds]] — SRV records, `_msdcs`, AD-integrated zones
- [[dns-infrastructure-design]] — zone delegation, forwarders, split-brain
- [[dc-locator]] — `DsGetDcName`, DNS-based vs. NetBIOS discovery
- [[disjoint-namespace]] — primary DNS suffix mismatch, remediation
- [[ad-integrated-dns-zones]] — zone replication scopes, dynamic update

### Time and authentication
- [[windows-time-service]] — W32Time hierarchy, NTP configuration, skew thresholds
- [[spn-and-upn-uniqueness]] — forest-wide uniqueness enforcement, error codes
- [[fine-grained-password-policies]] — PSOs, msDS-PasswordSettings objects

### Service accounts and identity
- [[delegated-managed-service-accounts]] — dMSA (Windows Server 2025+)
- [[kds-root-key]] — KDS root key creation and replication requirements
- [[group-managed-service-accounts]] — gMSA lifecycle, SPN binding
- [[default-user-accounts]] — built-in accounts and KRBTGT

### Security and hardening
- [[securing-active-directory]] — four-phase Microsoft security model
- [[tiered-administration-model]] — Tier 0/1/2 isolation
- [[credential-theft-and-attractive-accounts]] — pass-the-hash, pass-the-ticket, DCSync
- [[secure-administrative-hosts]] — dedicated admin workstations, PAW
- [[reducing-ad-attack-surface]] — privilege reduction, DC hardening, patch lifecycle
- [[protected-accounts-and-groups]] — AdminSDHolder, SDProp, `adminCount`
- [[monitoring-ad-for-compromise]] — key events, SIEM alert design
- [[advanced-audit-policy]] — subcategory configuration, `auditpol`, key event IDs
- [[software-restriction-policies]] — SRP and AppLocker on DCs and admin hosts
- [[ldap-signing-and-channel-binding]] — LDAP signing, CBT, Event IDs 2886–3040
- [[windows-laps]] — local admin password rotation, DSRM account management

### Deployment and lifecycle
- [[ad-ds-deployment]] — deployment prerequisites and planning
- [[install-promote-domain-controller]] — `Install-ADDSDomainController`, dcpromo
- [[adprep-and-schema-updates]] — `adprep /forestprep`, `/domainprep`, schema versioning
- [[ad-functional-levels]] — FFL/DFL table, unlock conditions, raise procedure
- [[upgrade-domain-controllers]] — in-place vs. swing migration, OS upgrade path
- [[demote-and-remove-dc]] — graceful demotion, forced removal, metadata cleanup
- [[ad-metadata-cleanup]] — `ntdsutil metadata cleanup`, post-seizure steps
- [[capacity-and-placement-planning]] — DC sizing, RAM formula, placement rules
- [[ad-admin-tools]] — RSAT, Active Directory Users and Computers, `ntdsutil`, `repadmin`

### Virtualization
- [[virtualized-domain-controllers]] — USN rollback, safe-restore safeguards
- [[vm-generation-id-safe-restore]] — VMGenID mechanism, safe-restore sequence
- [[vdc-cloning]] — clone prerequisites, `DCCloneConfig.xml`, cloning failures

### Advanced features
- [[read-only-domain-controller]] — RODC placement, credential caching policy, SYSVOL
- [[ad-recycle-bin]] — object recovery, tombstone vs. recycled-deleted state
- [[ad-database-and-32k-pages]] — NTDS.dit, ESE, 8k vs. 32k page format
- [[ad-ds-maximum-limits]] — DNT ceiling, nonlinked attribute limit, RID global space
- [[group-policy]] — GPO application, WMI filters, Group Policy modeling

### Disaster recovery
- [[ad-forest-recovery]] — forest-wide failure recovery procedure
- [[krbtgt-reset]] — double-reset procedure, timing, replication prerequisites

## See also
- [[sso-implementation-review]] — Keycloak / SSO domain equivalent of this MOC
- [[active-directory-overview]] — domain primer, objects, partitions, trust types
- [[securing-active-directory]] — security body with full four-phase model
- [[troubleshooting-index]] — cross-domain troubleshooting router
