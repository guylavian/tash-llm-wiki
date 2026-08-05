---
title: "PowerShell with Exchange Online - After a number of requests to the Exchange Online server, he no longer seems to respond"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1297770/powershell-with-exchange-online-after-a-number-of
question_id: 1297770
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# PowerShell with Exchange Online - After a number of requests to the Exchange Online server, he no longer seems to respond

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1297770/powershell-with-exchange-online-after-a-number-of (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have a PowerShell script that uses an Azure AD account with an Exchange Online license (Plan 1) to connect.

The script works as follows: create a loop which, for each security group, retrieves the mailbox addresses (a second loop is performed if there is more than one mailbox per security group).

Next, retrieve the members of the security group forming list A and retrieve the members of the mailbox forming list B.

If a user is in list A but not in list B, we add him/her to the mailbox, otherwise we remove him/her from the mailbox.

My problem is that after a certain number of requests, the script seems to continue but receives no response from the Exchange Online server.

I think this is because I'm making too many requests.

Is there any way of increasing the number of requests I can make, and if so, how?

Thanks in advance,

Pablo COELHO DA SILVA

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-06-05*

Hi @Pablo COELHO DA SILVA,

Here is a Microsoft blog on this topic which may be helpful.

For your reference: Running PowerShell cmdlets for large numbers of users in Office 365

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
