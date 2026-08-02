---
title: Windows Time Service (W32Time)
type: entity
domain: active-directory
slug: windows-time-service
summary: The W32Time service maintains clock synchronization across the domain hierarchy, with the PDC emulator as the authoritative time source; a skew exceeding 5 minutes breaks Kerberos authentication.
sources:
  - kb:ad-ds-understand-fsmo-roles
  - kb:ad-ds-virtualized-domain-controller-architecture
  - kb:ad-ds-join-computer-to-domain
  - kb:ad-ds-virtualized-domain-controllers-hyper-v
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-fsmo-roles (Microsoft Learn — Flexible Single Master Operations roles in Windows Server, fetched 2026-06-18)
  - web:https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture (Microsoft Learn — Virtualized Domain Controller Architecture, fetched 2026-06-18)
provenance_extracted: 3
provenance_inferred: 8
provenance_ambiguous: 0
symptoms:
  - "KRB_AP_ERR_SKEW"
  - "The Kerberos client received a KRB_AP_ERR_SKEW error"
  - "0xC000006D STATUS_LOGON_FAILURE.*time skew"
tags: [ad-authn, directory-services, troubleshooting, concept]
status: draft
updated: 2026-07-02
graph_community: "Active Directory Replication & Site Topology"
---

# Windows Time Service (W32Time)

**The Windows Time Service (W32Time) synchronizes clocks across a domain hierarchy; the PDC emulator FSMO is the authoritative time source, and a clock skew beyond 5 minutes breaks Kerberos.**

## Body

W32Time implements the **Network Time Protocol (NTP)** subset used by Windows domain members and domain controllers to maintain synchronized clocks (inferred from the W32Time/NTP relationship and domain-hierarchy behavior).

### Synchronization hierarchy

The domain forms a time synchronization tree:

1. **Domain members** (workstations and member servers) synchronize from the DC that authenticates them.
2. **Domain controllers** (non-PDC) synchronize from the domain's PDC emulator.
3. **PDC emulator** is the authoritative time source for the domain (inferred — the PDC emulator FSMO is the Kerberos/time master by design). It should be configured to synchronize from an external NTP source (hardware appliance or public pool).
4. In a multi-domain forest, child-domain PDC emulators synchronize from the root domain's PDC emulator (inferred).

Because the [[fsmo-roles]] PDC emulator is the apex of this hierarchy, its failure or misconfiguration propagates time drift to the entire domain (inferred).

### Kerberos 5-minute skew requirement

Kerberos protocol requires that the clocks of the client, KDC (DC), and target service be within **5 minutes** of each other. If the skew exceeds 5 minutes, the KDC or target service rejects the ticket with **KRB_AP_ERR_SKEW**. This is a security mechanism to prevent ticket-replay attacks (inferred — the 5-minute window is a Kerberos RFC requirement, not a Windows-specific choice).

Common causes of KRB_AP_ERR_SKEW in AD environments:

- PDC emulator not configured to sync from a reliable external NTP source.
- VM snapshotting or restoring a DC without Hyper-V time-sync awareness (see [[virtualized-domain-controllers]] and [[vm-generation-id-safe-restore]]).
- Isolated branch DC (RODC) whose PDC emulator path is unavailable for a long period.
- A clock jump on a newly promoted DC before W32Time has converged (inferred).

### Configuration

W32Time is configured via Group Policy (Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options, or the dedicated W32TM templates) or the command-line tool **w32tm.exe**:

```
w32tm /config /manualpeerlist:"time.windows.com" /syncfromflags:manual /reliable:YES /update
w32tm /resync /force
```

On the PDC emulator, set an external NTP source. On all other DCs, leave the default `NT5DS` source (sync from domain hierarchy) (inferred — standard best-practice configuration).

## Contradictions / caveats

- The 5-minute window is not configurable in standard Kerberos deployments and should not be widened; fix the clock, not the tolerance.
- Hypervisor time synchronization can fight W32Time on virtualized DCs. Microsoft recommends disabling Hyper-V time sync integration on the VM hosting the PDC emulator and letting it sync from an external NTP source. On all other virtualized DCs, Hyper-V time sync from the host plus W32Time from the domain hierarchy both remain active — W32Time wins when slewing corrections in normal operation (inferred).
- Windows Server 2016 introduced **accurate time** improvements (sub-millisecond accuracy on supported hardware) and the **leap second** support capability, available at Windows Server 2016+ forest functional level.

## Reference notes
- [[ad-ds-understand-fsmo-roles]]
- [[ad-ds-virtualized-domain-controller-architecture]]

## See also
- [[fsmo-roles]]
- [[virtualized-domain-controllers]]
- [[vm-generation-id-safe-restore]]
- [[read-only-domain-controller]]
- [[ad-replication]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[ad-ds-understand-fsmo-roles|Flexible Single Master Operations roles in Windows Server]]
- [[ad-ds-virtualized-domain-controller-architecture|Virtualized Domain Controller Architecture]]
- [[ad-ds-join-computer-to-domain|Join a computer to a domain]]
- [[ad-ds-virtualized-domain-controllers-hyper-v|Virtualizing domain controllers with Hyper-V]]
<!-- crosslink:end -->
