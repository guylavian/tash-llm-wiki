---
title: Seize FSMO roles after catastrophic loss of primary DC (PDC Emulator + RID Master)
type: question
domain: active-directory
slug: fsmo-seize-after-primary-dc-loss
status: draft
summary: When the primary-site DC holding the PDC Emulator and RID Master roles is destroyed and unrecoverable, seize both roles onto a surviving secondary DC via PowerShell or ntdsutil, then clean up the dead DC's metadata, reset time configuration, and manage the RID pool.
sources:
  - kb:ad-ds-ad-forest-recovery-seizing-operations-master-role
  - kb:ad-ds-manage-fsmo-roles
  - kb:ad-ds-ad-forest-recovery-perform-initial-recovery
  - kb:ad-ds-ad-forest-recovery-cleaning-metadata-of-removed-dcs
  - kb:ad-ds-managing-rid-issuance
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/manage-fsmo-roles
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-seizing-operations-master-role
provenance:
  extracted: 14
  inferred: 3
  ambiguous: 0
question_tier: scenarios
updated: 2026-07-12
---

# Seize FSMO roles after catastrophic loss of primary DC (PDC Emulator + RID Master)

> ⚠️ Out of corpus coverage — `active-directory` holds `conceptual` only; this is a `scenarios` question and that tier is not ingested; verify against the primary source.

**Scenario:** A catastrophic power loss destroys the primary-site Domain Controller that held both the **PDC Emulator** and **RID Master** FSMO roles. A secondary Domain Controller exists at another site. The destroyed DC cannot be recovered.

This is **not** a full [[ad-forest-recovery]] (only one DC is lost, the rest of the forest is healthy). The corrective steps are: seize the FSMO roles onto a surviving DC, clean up the destroyed DC's metadata, configure time synchronization, and manage the RID pool.

---

## Step 1 — Verify the FSMO roles cannot be transferred gracefully

A graceful **transfer** (using `Move-ADDirectoryServerOperationMasterRole` *without* `-Force`) requires the current role holder to be online and reachable. Since the primary site DC is destroyed, PowerShell will fail with an RPC/unreachable error. You must **seize** (force-transfer) the roles instead.

```powershell
# Confirm the DC is unreachable
Test-Connection DC1.corp.contoso.com -Count 1
```

When the target is confirmed dead, proceed to seizure.

---

## Step 2 — Seize the FSMO roles onto a surviving DC

### Method A: PowerShell with `-Force` (recommended)

On the surviving secondary DC (or any Domain Admin workstation with RSAT), run:

```powershell
# Seize both roles in one command
Move-ADDirectoryServerOperationMasterRole -Identity "DC2" -OperationMasterRole PDCEmulator,RIDMaster -Force
```

The `-Force` flag tells the cmdlet to proceed even though the current holder is unreachable. After seizure, the roles are now held by `DC2`.

To verify:
```powershell
Get-ADDomainController -Filter * | Select-Object Name, OperationMasterRoles
```

Or:
```
netdom query fsmo
```

### Method B: ntdsutil (legacy, works on any Windows Server)

```
ntdsutil
  roles
    connections
      connect to server DC2.corp.contoso.com
      quit
    seize pdc
    seize rid master
    quit
  quit
```

When seizing the **RID Master**, ntdsutil will attempt to synchronize with a replication partner before accepting the role. Because the DC may be isolated during this process, it will prompt:

> *"This computer cannot synchronize with a partner. Do you want to continue?"*

Click **Yes** — the sync will complete after the DC is connected to the network.

> **Critical rule:** Once FSMO roles are seized from a destroyed DC, **never resurrect the original DC** — reintroducing the old holder would cause a split-brain / lingering-object conflict (see [[fsmo-roles]]).

---

## Step 3 — Clean up metadata of the destroyed DC

The destroyed DC's objects (NTDS Settings, server object, computer object) remain in AD and the replication topology. These orphaned references cause replication errors and can prevent the RID Master from issuing new RID pools (event ID 16650).

### GUI method (automatic metadata cleanup)

Use **Active Directory Users and Computers** (dsa.msc) with RSAT:

1. Enable **Advanced Features** (View → Advanced Features).
2. Navigate to the **Domain Controllers** OU.
3. Right-click the destroyed DC object → **Delete**.
4. Check: *"This Domain Controller is permanently offline and can no longer be demoted using DCPROMO."*
5. Confirm. The NTDS Settings object, server object, and computer object are automatically cleaned up.

Alternatively, use **Active Directory Sites and Services** (dssite.msc):

1. Expand the site → **Servers** → right-click the destroyed DC → **Delete**.
2. Confirm deletion of NTDS Settings and server object.

### Command-line method (ntdsutil)

```cmd
ntdsutil
  metadata cleanup
    connections
      connect to server DC2.corp.contoso.com
      quit
    remove selected server DC1.corp.contoso.com
    quit
  quit
```

Verify the destroyed DC no longer appears in the Domain Controllers OU and has no NTDS Settings object in Sites and Services.

---

## Step 4 — Raise and invalidate the RID pool

After seizing the RID Master role:

1. **Raise the available RID pool by 100,000** to prevent SID collisions with security principals that may have been created on the destroyed DC after the last backup but never replicated out. This is critical if new accounts may have been created on the destroyed DC that have not been seen by the rest of the forest.

   See [Raising the value of available RID pools](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-raise-rid-pool).

2. **Invalidate the current RID pool** on the surviving DC (now RID Master) if a system state restore was not performed. This forces the DC to request a fresh RID pool upon next security principal creation. After invalidation, the first attempt to create a new object with a SID will fail — simply retry; the retry triggers a new RID pool allocation and succeeds.

   See [Invalidating the current RID pool](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-invaildate-rid-pool).

> **Note:** Until metadata of the destroyed DC is cleaned up, the RID Master will refuse to issue new RID pools and log event ID 16650. Event ID 16648 confirms success after cleanup.

---

## Step 5 — Configure Windows Time Service on the new PDC Emulator

The PDC Emulator is the authoritative time source for the domain. After seizure, configure the new PDC Emulator to synchronize time from an external reliable time source (the specific peerlist below is an example, not from the corpus — inferred):

```cmd
w32tm /config /manualpeerlist:"pool.ntp.org,0x8" /syncfromflags:MANUAL /update
w32tm /resync
```

Verify:
```
w32tm /query /status
```

> A clock skew exceeding 5 minutes breaks Kerberos authentication across the domain — this step is urgent (see [[windows-time-service]] and [[dns-for-ad-ds]]).

---

## Step 6 — Verify replication and DNS health

- Run `repadmin /replsum` to confirm all surviving DCs are replicating.
- Run `dcdiag /v` to check for errors.
- If DNS was AD-integrated, remove NS records of the destroyed DC from the `_msdcs` and domain DNS zones (metadata cleanup may remove SRV records automatically). To force DNS cleanup:
  ```cmd
  nltest.exe /dsderegdns:DC1.corp.contoso.com
  ```

---

## Step 7 — Deploy a replacement DC in the primary site

Once the forest is stable:

1. Deploy a fresh Windows Server in the primary site.
2. Install the AD DS role:
   ```powershell
   Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
   ```
3. Promote as a replica DC:
   ```powershell
   Install-ADDSDomainController -DomainName "corp.contoso.com" -SiteName "Primary-Site"
   ```

> **Do not** restore the destroyed DC from backup — it holds outdated FSMO data. Always rebuild from scratch (see [[install-promote-domain-controller]]).

---

## Summary of required credentials (inferred)

| Action | Required group |
|---|---|
| Seize PDC Emulator | Domain Admins |
| Seize RID Master | Domain Admins |
| Clean up metadata | Domain Admins |
| Configure time | Local Administrator on the PDCe |

---

## References

### Microsoft Learn (ground truth)

- [Transfer FSMO roles in Windows Server](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/manage-fsmo-roles)
- [AD Forest Recovery — Seize an operations master role](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-seizing-operations-master-role)
- [AD Forest Recovery — Perform initial recovery](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery)
- [AD Forest Recovery — Clean metadata of removed writable DCs](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-cleaning-metadata-of-removed-dcs)
- [Managing RID Issuance](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/Managing-RID-Issuance)

### Wiki / vault

- [[fsmo-roles]] — the five single-master roles and seize vs. transfer semantics
- [[ad-forest-recovery]] — the full forest-recovery procedure (this scenario doesn't require it, but shares sub-steps)
- [[demote-and-remove-dc]] — metadata cleanup and forced removal
- [[install-promote-domain-controller]] — deploying new replica DCs
- [[rid-issuance-management]] — RID pool mechanics, 90% ceiling, and 31-bit unlock
- [[windows-time-service]] — W32Time hierarchy and PDCe role
- [[ad-metadata-cleanup]] — cleaning up orphaned DC objects

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-ad-forest-recovery-seizing-operations-master-role|AD Forest Recovery]]
- [[ad-ds-manage-fsmo-roles|Transfer Flexible Single Master Operations roles in Windows Server]]
- [[ad-ds-ad-forest-recovery-perform-initial-recovery|Active Directory Forest Recovery]]
- [[ad-ds-ad-forest-recovery-cleaning-metadata-of-removed-dcs|AD Forest Recovery]]
- [[ad-ds-managing-rid-issuance|Managing RID Issuance]]
<!-- crosslink:end -->
