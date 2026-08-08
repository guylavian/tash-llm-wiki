---
title: "Active Directory Forests publishing status failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2150288/active-directory-forests-publishing-status-failed
question_id: 2150288
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active Directory Forests publishing status failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2150288/active-directory-forests-publishing-status-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

Active Directory Forests publishing status is under failed state. 

Please help what are logs to be checked and how to solve the issue.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-23*

Hi, @Boopathi S

Thank you for posting in Microsoft Q&A forum.

Actions for Active Directory Forest Discovery are recorded in the following logs:

All actions, except actions related to publishing, are recorded in the ADForestDisc.Log file in the <InstallationPath>\Logs folder on the site server.

Active Directory Forest Discovery publishing actions are recorded in the hman.log and sitecomp.log files in the <InstallationPath>\Logs folder on the site server.

For more details:

https://learn.microsoft.com/en-us/mem/configmgr/core/servers/deploy/configure/about-discovery-methods#bkmk_aboutForest

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Add comment".

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-22*

Try the following:

-  Verify Permissions on the System Management Container:

-  Ensure that the SCCM site server's computer account has Full Control permissions on the System Management container in Active Directory. This permission must apply to "This object and all descendant objects." To set this:

-  Open ADSI Edit.

-  Navigate to the System Management container.

-  Right-click the container, select Properties, and go to the Security tab.

-  Add the SCCM site server's computer account and grant it Full Control.

-  Click Advanced, select the added account, and ensure the permission applies to "This object and all descendant objects."

-  Check for Incorrect Credentials:

-  If you're using a specific user account for publishing (instead of the site server's computer account), verify that the username and password are correct. Errors such as `HRESULT=0x8007052E` in logs indicate incorrect credentials. To resolve:

-  Navigate to Administration > Hierarchy Configuration > Active Directory Forests in the SCCM console.

-  Right-click the relevant forest and select Properties.

-  Under the Publishing tab, update the account credentials.

-  Extend the Active Directory Schema:

-  If the Active Directory schema hasn't been extended for SCCM, the site server may fail to publish information. To extend the schema:

-  Run the `extadsch.exe` tool found in the SCCM installation media on a server with Schema Admin rights.

-  After extending, verify that the schema extension was successful by checking the `extadsch.log` file, typically located in the root of the system drive.

-  Review SCCM Logs for Specific Errors:

-  Examine the `SiteComp.log` and `hman.log` files on the SCCM site server for detailed error messages related to publishing. Common errors include:

-  `Win32 error = 5`: Indicates insufficient permissions.

-  `Could not connect to the RootDSE container in Active Directory. HRESULT=0x8007052E`: Points to incorrect credentials.

-  These logs provide insights into the root cause of the publishing failure.

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
