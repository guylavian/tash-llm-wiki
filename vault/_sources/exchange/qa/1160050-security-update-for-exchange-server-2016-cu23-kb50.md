---
title: "Security Update For Exchange Server 2016 CU23 (KB5019077) - UNINSTALL Options"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160050/security-update-for-exchange-server-2016-cu23-kb50
question_id: 1160050
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Security Update For Exchange Server 2016 CU23 (KB5019077) - UNINSTALL Options

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160050/security-update-for-exchange-server-2016-cu23-kb50 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello folks,

Quick question. On one Exchange 2016 CU23 with the Oct 2022 security update (KB5019077) server I've got an issue and looking for direction.

While obtaining info for our security folks, under Programs/Programs and Features/Installed Updates, in a hurry I went to highlight the "security update for Exchange server....." and it kicked off the uninstall. It was not at the program level, and I haven't rebooted. Still running fine, however I'm looking for information regarding the current state. ***After a restart, is it just the security update (Exchange2016-KB5019077-x64-en.exe) that un-installed, leaving the base CU23 in tact? At which point I can restart, re-install and be back to normal?

Regards,

Darrell

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-01-13*

Hi Darrell,

If Exchange (mail flow and client access) is still working, you should be fine.

You can restart and see if any issue occurs.

While since KB5019077 was released in Oct 2022, I would recommend installing the latest Jan 2023 Security Update instead.

Please refer to this link: Released: January 2023 Exchange Server Security Updates

Also note that there have been some known issues which you may need to pay attention to:

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
