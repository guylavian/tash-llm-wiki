---
title: "domain controllers not syncing and root doamin and sub-domain are not syncing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5915827/domain-controllers-not-syncing-and-root-doamin-and
question_id: 5915827
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor", "Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# domain controllers not syncing and root doamin and sub-domain are not syncing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5915827/domain-controllers-not-syncing-and-root-doamin-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

During a failure we restored a DC (the PDC) in the sub-domain after a less than an hour downtime, this has caused numerous errors and replication is no longer replicating. "repadmin" show a few access denied errors. There are ldap errors (error 82). We see " The target principal name is incorrect." during "repadmin /showrepl * /errorsonly".  And during "repadmin /syncall" , we see access denied on a number of DCs. Any help would be appreciated. Thank you

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 1 · updated: 2026-06-10*

Hi Bryant, Paul

When a DC is restored from an older backup or a virtual machine snapshot, its state is reverted to the past. This introduces two critical risks:

-  Secure Channel Mismatch: The Machine Account Password or Inter-Domain Trust Password on the restored DC no longer matches the current Active Directory database. This breaks Kerberos authentication, preventing the DC from decrypting service tickets (resulting in "Target principal name is incorrect" and Access Denied errors).

-  USN Rollback: If the restore method is unsupported, the Update Sequence Number (USN) reverts, completely breaking Active Directory replication and risking database corruption.

Please follow the Action Plan below to isolate the issue and safely recover the environment.

============================

Action Plan:

Phase 1: Isolate and Check for USN Rollback (Mandatory)

You must verify the database integrity of the restored DC before making any password changes.

-  Isolate the DC: On the restored DC, open an elevated Command Prompt and run:

-  Net stop netlogon

-  Check Event Logs: Open Event Viewer -> Applications and Services Logs -> Directory Service.

-  Filter for Event ID 2095:

-  If Event 2095 is present: A USN Rollback has occurred.

-  If Event 2095 is not present: This might be a Kerberos/Secure Channel mismatch.

-  Check Registry Key on the restore DC:

-  Registry subkey: HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\NTDS\Parameters

-  Registry entry: Dsa Not Writable

-  Value: 0x4 (Which indicated that the domain controller is USN rollback)

-  Reference: How to detect and recover from a USN rollback in Windows Server

============================

Phase 2: Fix the issue based on the observation

Option A: Recovering from USN Rollback (Event 2095 Present)

Do not attempt to force replication. The database on this DC is corrupted.

-  Seize FSMO Roles: If the failed DC holds any FSMO roles, log on to a Healthy DC and use ntdsutil to seize them. DO NOT perform this on the failed DC.

-  Reference: Transfer or seize Operation Master roles - Windows Server | Microsoft Learn

-  Metadata Cleanup: From a Healthy DC, use Active Directory Users and Computers (ADUC) or ntdsutil to delete and demote the failed DC object to clean up lingering metadata.

-  Reference: Clean up Active Directory domain controller server metadata

-  Rebuild: Reinstall the OS, rejoin the domain, and promote the server as a new DC.

Option B: Fixing Secure Channel Mismatch - Target Principal Name is incorrect (No Event 2095)

Restore the broken Kerberos authentication flow on the restored DC.

-  Purge Tickets and Reset Machine Password: Run the following commands sequentially on the restored DC via an elevated Command Prompt:

-  net stop kdc

-  klist -li 0x3e7 purge

-  netdom resetpwd /server:<Healthy_DC_Name> /userd:<Domain_Name><Domain_Admin> /passwordd:* 

-  net start kdc

-  net start netlogon

-  shutdown /r /t 0

-  Reference: Target Principal Name is incorrect when manually replicating data between domain controllers - Windows Server | Microsoft Learn

-  Validate Replication: Once the server reboots, verify inbound and outbound replication:

-  repadmin /showrepl

-  repadmin /syncall /AdeP

-  Reset Inter-Domain Trust (If necessary): If internal replication succeeds but cross-domain queries to the parent domain still return Access Denied, reset the trust password:

-  netdom trust <Sub_Domain> /Domain:<Parent_Domain> /reset /UserD:<Parent_Admin> /PasswordD:* /UserO:<Sub_Admin> /PasswordO:*

============================

If this helps resolve your problem, please consider hitting "Accept Answer" so other users facing this failure can easily find the solution!

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-10*

Hello Bryant, Paul,

The errors you’re seeing, such as “access denied,” LDAP error 82, and “The target principal name is incorrect”, are consistent with Active Directory replication problems that often occur after restoring a domain controller. When a DC is restored, its secure channel and Kerberos tickets can become out of sync, which leads to authentication failures during replication.

Here are a few steps you can take:

-  Verify that the restored DC’s computer account is healthy in Active Directory Users and Computers.

-  Run `nltest /sc_verify:<domain>` to confirm the secure channel is working between the DCs.

-  Check that the service principal names (SPNs) for the domain controllers are correct; mismatched SPNs often trigger the “target principal name is incorrect” error.

-  Use `repadmin /replsummary` to identify which DCs are failing and whether the issue is isolated to the restored server.

-  If corruption is suspected, consider removing the restored DC from the domain and performing a clean promotion to rejoin it.

These errors are usually resolvable by repairing the secure channel and ensuring SPNs are properly registered. Once corrected, replication should resume normally across the root and sub-domain.

I hope this guidance helps you move forward with stabilizing your environment. If you find this answer useful, please hit “accept answer” so I know it addressed your concern.

Jason.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-06-09*

Restoring a PDC emulator DC from backup in an Active Directory domain or sub-domain can easily break secure replication if the restored DC’s view of the directory (including its own identity and partners) is out of date. The symptoms described match two specific replication problems:

-  Error -2146893022 / 0x80090322: “The target principal name is incorrect.”

-  Access denied / LDAP error 82 and general replication failures between DCs.

Use the following focused steps to restore secure replication.

-  Focus first on the “target principal name is incorrect” error

This error indicates a Kerberos/SPN mismatch between source and destination DCs. The documented resolution is to verify that the destination DC is resolving the correct DC identity (GUID and FQDN) to the correct IP, and that no stale or conflicting name records exist.

On an affected destination DC:

-  Run `IPCONFIG /ALL` and note all DNS servers configured (primary, secondary, tertiary). These are the DNS servers the DC uses for locating replication partners.

-  Run `REPADMIN /SHOWREPS | MORE` and locate the inbound neighbor entries that are failing with “The target principal name is incorrect.” Record:

-  The source DC name

-  The DSA object GUID of the source DC’s NTDS Settings object

-  On the destination DC, open the HOSTS file:

-  Start > Run > `Notepad %systemroot%\system32\drivers\etc\hosts`

-  Remove any host-to-IP mappings that reference the source DC’s single-label or FQDN (these can override DNS and cause SPN mismatches).

-  Save the file.

-  Run `nbtstat -R` to refresh the NetBIOS name cache.

-  Flush DNS client cache on the destination DC:

-  `ipconfig /flushdns`

-  For each DNS server IP noted in step 1, verify the GUID-based CNAME record resolves correctly:

-  `nslookup -type=CNAME <source-DC-NTDS-GUID>._msdcs.<forest-root-DNS-name> <DNS-Server-IP>`

-  Confirm that the returned CNAME ultimately resolves to the correct source DC FQDN and IP.

-  Check for duplicate or stale A/AAAA records for the source DC on each DNS server:

-  `nslookup -type=A+AAAA <source-DC-FQDN> <DNS-Server-IP>`

-  Ensure only the correct IP is returned.

-  Confirm NetBIOS name matches the IP:

-  `nbtstat -A <IP-returned-by-nslookup>`

-  The name returned should be the source DC.

If any of these checks fail (wrong IP, stale records, HOSTS overrides), correct them and then re-run `repadmin /showrepl` and a targeted `repadmin /replicate` between the affected DC pair.

-  Handle transient topology and naming-context issues

After a restore and role changes, replication topology may be in flux. This can temporarily produce additional errors (for example, 8452 “The naming context is in the process of being removed or is not replicated from the specified server”). In such cases:

-  Avoid running `repadmin /syncall` repeatedly while topology is converging. This is explicitly recommended to prevent forcing replication between DCs that do not yet agree on source/partition relationships.

-  If a specific naming context (partition) is failing with 8452, and the cause is a topology change (for example, FSMO role moved, links not yet built), allow time for KCC to recalculate and build the correct links.

-  When manually forcing replication, ensure the chosen source DC actually has a replica link for the naming context on the destination DC. If not, select a different source DC that is a valid partner for that partition.

-  Address access denied and LDAP 82 / endpoint issues

The combination of access denied, LDAP error 82, and “no more endpoints available from the endpoint mapper” typically indicates that the restored DC is not fully functional as a domain controller, or that secure RPC/Kerberos communication is broken.

Key checks on the restored PDC and any DC reporting these errors:

-  Verify the DC is fully functional as a domain controller:

-  Confirm the Active Directory Installation Wizard completed successfully.

-  Ensure the SYSVOL folder is shared and the full file structure exists under `%SystemRoot%\Sysvol\Sysvol\<Domain_name>\Policies`.

-  If SYSVOL is not shared or the structure is incomplete, the DC is effectively broken and may need to be demoted and re-promoted rather than repaired in place.

-  From the affected DC, test network resource access:

-  `net view \\<PDC-name>`

-  If this fails with “Access denied” but `net view \\<PDC-IP>` succeeds, this again points to name/SPN/DNS issues that must be corrected as in section 1.

-  Run `repadmin /showreps` locally on each DC and note:

-  Errors 1753 (“There are no more endpoints available from the endpoint mapper”).

-  Errors 5 (“Access is denied”).
     These indicate RPC endpoint or security issues between DCs.

-  For access denied replication errors (status 5):

-  Confirm that the DC computer accounts have not been rolled back to a previous password state that no longer matches their partners (a risk after restoring from backup).

-  If a DC’s secure channel is broken beyond repair, the supported approach is often to demote and re-promote that DC rather than attempt to fix the computer account manually.

-  Decide whether to keep or rebuild the restored PDC

Because the PDC emulator was restored from backup, its view of the directory and its own secrets may be inconsistent with the rest of the domain. If, after DNS/SPN cleanup and endpoint checks, replication still fails with access denied and target principal name errors, the safest route is often:

-  Transfer the PDC FSMO role (and any other FSMO roles) to a healthy DC in the same domain, if possible.

-  Demote the restored DC cleanly if it is still partially functional, or perform metadata cleanup if it cannot be demoted.

-  Re-promote a new DC in that site/domain and allow it to replicate from a healthy partner.

This avoids lingering security and replication inconsistencies that can be difficult to fully diagnose after an out-of-date restore of a DC.

-  If further assistance is needed

If replication failures persist after DNS/SPN cleanup and, where necessary, demotion/re-promotion of broken DCs, collect detailed logs for support using the documented TSS collection for Active Directory replication issues and engage Microsoft support.

References:

-  Active Directory replication error -2146893022 (0x80090322): The target principal name is incorrect

-  Error "Target Principal Name is incorrect" when manually replicating data between domain controllers

-  Domain controller is not functioning correctly

-  Replication error 1753 There are no more endpoints available from the endpoint mapper

-  How to troubleshoot Active Directory replication error 5 in Windows Server: Access is denied

-  The naming context is in the process of being removed or is not replicated from the specified server

-  Troubleshooting AD Replication error 1908: Could not find the domain controller for this domain

-  Gather information by using TSS for Active Directory replication issues
