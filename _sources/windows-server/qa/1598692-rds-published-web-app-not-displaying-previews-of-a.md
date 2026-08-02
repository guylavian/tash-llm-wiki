---
title: "RDS Published Web App not displaying previews of application windows"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1598692/rds-published-web-app-not-displaying-previews-of-a
question_id: 1598692
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# RDS Published Web App not displaying previews of application windows

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1598692/rds-published-web-app-not-displaying-previews-of-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, The error my users experience involves published Remote App applications not displaying previews of application windows when users hover over or click on the taskbar icons, showing only the app icon instead. This issue affects all users and does not occur in full RDP sessions, impacting the productivity of users who need to have many windows of the same application open. The problem started after updates over the weekend of November 25/26th. The troubleshooting efforts have included reviewing\modifying RDP file configurations and investigating potential causes related to recent updates or SSL issues. A specific update, KB5031984, has been identified as the most likely cause based on its installation times across RDS/Util servers.  Reverting the KB is one option, but highly risky and not preferred.  Is there a way to permanently fix this please, anyone?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-27*

Hello,

You can try blew command in your server: (it will help if there is any broken component, ensure you are connected to internet)

a. sfc /scannow

b. DISM /Online /Cleanup-image /RestoreHealth

Besides, you can deploy a new server with the latest version and have a test. If the issue is fixed in the latest version, you can update your servers to the latest release version.

If the Answer is helpful, please click "Accept Answer" and upvote it.
