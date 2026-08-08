---
title: "How can I script moving a mailbox to Exchange Online without user intervention to enter the remote credentials?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1532606/how-can-i-script-moving-a-mailbox-to-exchange-onli
question_id: 1532606
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# How can I script moving a mailbox to Exchange Online without user intervention to enter the remote credentials?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1532606/how-can-i-script-moving-a-mailbox-to-exchange-onli (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to run a script unattended to find users with on-prem mailboxes and run the new-moverequest cmdlet to migrate the mailbox to Exchange Online.  I am running into issues when it calls for the Remote Credential with a login window popping up.  

Any ideas how I can achieve this?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-15*

Hi @Cara Coulee,

To run unattended scripts in Exchange Online Powershell, you can use Certificate based authentication (CBA) or app-only authentication.

For more details, please refer to this link:

App-only authentication for unattended scripts in Exchange Online PowerShell and Security & Compliance PowerShell

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
