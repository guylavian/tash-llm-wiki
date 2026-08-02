---
title: "Microsoft Entra Connect - Transfer to new server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5915278/microsoft-entra-connect-transfer-to-new-server
question_id: 5915278
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Entra Connect - Transfer to new server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5915278/microsoft-entra-connect-transfer-to-new-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,

I've a situation where I don't have any kind of access to my old DC as it was decommissioned  recently. Unfortunately, I forgot to get a policy backup from Entra connect and now I need to set up and configure it on the new DC.

So I don't have any backups, and not even access to old DC here.

What can I do now to properly install and configure Entra Connect on the new DC without breaking anything.

(I saw in some places to install this on Staging mode and making it active later, but I'm not sure)

Need your expertise on this.

Thanks,

Leo

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2026-06-09*

Can you move to Entra Cloud Sync instead?

https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync

Microsoft is going to force you to move to it soon anyway, I would start now.

https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide

## Answer (community) — community member

*upvotes: 0 · updated: 2026-06-09*

Use a new Microsoft Entra Connect installation on the new server and treat it as a fresh deployment, but follow staging-mode and swing-migration best practices to avoid breaking the existing Microsoft Entra ID objects.

A safe approach in this situation is:

-  Plan for a swing/staging deployment

-  Use a new Windows Server as the new Entra Connect server.

-  The recommended pattern is to have one active server and one staging server (swing migration). The staging server is prepared and validated before being made active.

-  This pattern is explicitly recommended when upgrading or rebuilding, and also applies when the old server is gone and configuration cannot be exported.

-  Install Microsoft Entra Connect in staging mode

-  During installation on the new server, select staging mode.

-  In staging mode, the server:

-  Performs imports and synchronizations from on-premises AD and Microsoft Entra ID.

-  Does not export changes to Microsoft Entra ID.

-  Does not run password hash sync or password writeback, even if selected.

-  This allows building and testing the configuration without affecting production data.

-  Rebuild configuration carefully

-  Because there is no backup of the old configuration, recreate:

-  Forest connections.

-  Domain/OU filtering.

-  Optional features (password sync, password writeback, etc.).

-  The sync engine does not store authoritative state; it reconstructs from AD and Microsoft Entra ID. The sourceAnchor attribute is used to join existing on-premises and cloud objects. As long as the same sourceAnchor values are used, the new server will match existing objects instead of creating duplicates.

-  If the previous server had custom sync rules, these must be recreated manually (there is no export to reuse in this case).

-  Run full import and full synchronization in staging mode

-  Let the new server run a full import and full sync while still in staging mode.

-  This builds the connector space and allows verifying that the configuration does not introduce unexpected changes.

-  Use the guidance under “Verify the configuration of a server” (from the staging-mode documentation) to check pending exports and confirm that the changes are what is expected before enabling exports.

-  Validate before going active

-  Review pending exports to Microsoft Entra ID to ensure no destructive or unexpected changes (for example, mass deletes or attribute resets).

-  If unexpected changes appear, adjust filtering or rules, run another sync cycle, and re-verify until the results look correct.

-  Disable staging mode to make the new server active

-  Once satisfied with the configuration and pending changes, disable staging mode on the new server.

-  When staging mode is disabled:

-  The server starts exporting changes.

-  Password sync and password writeback (if enabled) become active.

-  The server then becomes the active production sync server.

-  Plan for disaster recovery going forward

-  After the new active server is stable, consider adding a second server in staging mode for fault tolerance and disaster recovery.

-  A staging server continuously imports and syncs but does not export, so it can quickly take over if the active server fails.

-  Avoid “rogue” old servers

-  If any old Entra Connect server reappears later (for example, a restored VM), fully decommission it (uninstall Entra Connect or permanently delete the VM). Old servers can become “rogue” and overwrite current Microsoft Entra data with outdated information if they can still connect to Microsoft Entra ID.

This process allows safely rebuilding Entra Connect on a new server without access to the old DC or configuration backup, while minimizing risk to existing Microsoft Entra ID objects.

References:

-  Microsoft Entra Connect: Staging server and disaster recovery

-  Microsoft Entra Connect: Upgrade from a previous version to the latest

-  Import and export Microsoft Entra Connect configuration settings

-  Move Microsoft Entra Connect database from SQL Server Express to remote SQL Server
