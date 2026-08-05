---
title: "I cannot control Print Servers on Active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164750/i-cannot-control-print-servers-on-active-directory
question_id: 1164750
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-print-jobs", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# I cannot control Print Servers on Active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164750/i-cannot-control-print-servers-on-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Environment: I have a domain server which contains Active Directory, and I want to add another server to this active directory and the purpose of adding that server is for print management. I can add the server but I cannot control the printers on that server.

Issue: I want to connect my print server to my main server. I can add the server by typing the IP address or the name. but I cannot control the print server printers ,see the printers from my main server, or add them.

Note: As I noticed, the spool folder for the added print server is empty

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-31*

The user account running Print Management Console must be an administrator,  or been given some administrative rights on the new print server.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-27*

Hi,

When you connect locally on new server PRNT-SERVER-2 do you have the same behavior ?

Please don't forget to mark helpful answer as accepted
