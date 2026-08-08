---
title: "Printer Server 2022 Print Nightmare GPO issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1034767/printer-server-2022-print-nightmare-gpo-issue
question_id: 1034767
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-print-jobs"]
answer_author_roles: ["Q&A User"]
---
# Printer Server 2022 Print Nightmare GPO issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1034767/printer-server-2022-print-nightmare-gpo-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a new Server 2022 Print environment and are currently seeing an issue where all users are being prompted regularly to update the drivers and because they are not administrators UAC stops them from printing. We got around this issue pre server 2022 by forcefully installing the driver as an admin via an SCCM job but this doesn't seem to work for Server 2022.    

We have implemented the GPO which should isolate that server as being trusted to install print drivers from but it's not working as expected and we are stuck. Does anyone have any experience with this issue as a google search hasn't brought much back on this problem.     

We have print servers on Server 2019 which do no show    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-04*

The policy you reference does not override the requirement on the client system for administrative access in order to install the software from the server.
