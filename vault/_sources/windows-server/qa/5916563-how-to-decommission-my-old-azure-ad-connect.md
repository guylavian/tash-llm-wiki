---
title: "How to Decommission my old AZURE AD connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5916563/how-to-decommission-my-old-azure-ad-connect
question_id: 5916563
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# How to Decommission my old AZURE AD connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5916563/how-to-decommission-my-old-azure-ad-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an old Azure AD Connect server, and I've set up a new one on a different server while keeping the old one running. Now, I need to decommission the old server, but some user data is still being synced between both servers, and I can't stop the service to disconnect it. How can I separate the data and safely shut down the old AD Connect server?

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-20*

Hi Lloyd Hughes,

Has your issue been resolved yet? If it has, please consider accepting the answer as it helps others sharing the same problem benefit too. Thank you :)

Domic V.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-10*

Hi Lloyd Hughes,

Running dual active synchronization servers causes immediate data collisions in the cloud tenant. To resolve this, you must enable Staging Mode on the old server via the Microsoft Entra Connect configuration wizard. Staging Mode allows the old server to read local Active Directory data but explicitly halts all outbound export operations to Entra ID, neutralizing it as a source of conflict while keeping the data safely intact in its local database.

Once neutralized, verify that the new server has Staging Mode disabled so it acts as the sole authoritative exporter. To validate healthy data flow, navigate to the default installation path at `C:\Program Files\Microsoft Azure AD Sync\UIShell` and launch `miisclient.exe`. This executable opens the Synchronization Service Manager, a deep-level interface that allows you to monitor the Operations tab. Ensure that full imports and synchronizations are succeeding across both your local and cloud connectors. After confirming the new infrastructure is successfully updating user attributes on its own, launch the Windows Services console by typing `services.msc` into the run dialog on the legacy server. Locate the Microsoft Entra ID Sync service, technically registered as `ADSync`, and set its startup type to disabled before stopping it entirely. With the engine permanently halted, you can use the standard Programs and Features applet, accessible via `appwiz.cpl`, to cleanly uninstall Microsoft Entra Connect and safely complete the decommissioning of the old server.

Domic V.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-06-10*

Use a swing/parallel migration pattern and staging mode to cleanly switch over, then decommission the old server.

-  Verify the new Microsoft Entra Connect server is healthy

-  On the new server, open Microsoft Entra Connect → go to the Operations tab.

-  Confirm these operations have completed successfully with no errors:

-  Full Import on the Windows Server AD connector

-  Full Import on the Microsoft Entra connector

-  Full Synchronization on the Windows Server AD connector

-  Full Synchronization on the Microsoft Entra connector

-  If there are unexpected changes, follow the guidance in verify the configuration in staging mode to review and correct before cutover.

-  Ensure only one active sync server is exporting

-  The supported pattern is to have one active Microsoft Entra Connect server and optionally one staging server.

-  If both servers are currently exporting, switch the old server to staging mode so it no longer exports changes:

-  On the old server, open Microsoft Entra Connect → Additional tasks → Configure staging mode → enable staging mode (so it stops exporting).

-  Confirm that the new server is the only one with staging mode disabled and is exporting to Microsoft Entra ID.

-  Let the new server run and validate data

-  Allow the new server to run several sync cycles (or a full import/full sync if not already done) and verify that:

-  All expected users, groups, and attributes are present in Microsoft Entra ID.

-  No unexpected adds/deletes/attribute changes are occurring.

-  This is the same pattern described for swing migration and parallel deployment: run full import/full sync on the new server, verify, then switch active server.

-  Stop synchronization on the old server

-  Once satisfied that the new server is the authoritative and only exporting server:

-  Leave the old server in staging mode (no exports) for a grace period if rollback is needed.

-  After that period, stop the synchronization service on the old server and keep it stopped.

-  Decommission the old Microsoft Entra Connect server

-  When fully confident in the new server and no further use for the old one:

-  Uninstall Microsoft Entra Connect from the old server using Programs and Features.

-  Optionally shut down or repurpose the server.

-  This is analogous to the documented pattern for removing older sync tools (DirSync/AD Sync) once the new Microsoft Entra Connect instance is active.

Key points:

-  Only one Microsoft Entra Connect server should be actively exporting to Microsoft Entra ID at any time.

-  Use staging mode on the old server to stop exports without immediately uninstalling, then uninstall once the new server is validated.

References:

-  Microsoft Entra Connect: Upgrade from DirSync

-  Microsoft Entra Connect: Upgrade from a previous version to the latest

-  Decommission Azure AD Connect V1

-  Migrating from Microsoft Entra Connect to Microsoft Entra Cloud Sync
