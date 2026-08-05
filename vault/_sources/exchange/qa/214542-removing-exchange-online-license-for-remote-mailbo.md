---
title: "Removing Exchange Online license for remote mailbox(O365)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/214542/removing-exchange-online-license-for-remote-mailbo
question_id: 214542
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Removing Exchange Online license for remote mailbox(O365)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/214542/removing-exchange-online-license-for-remote-mailbo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

As per the article - https://learn.microsoft.com/en-us/powershell/module/exchange/disable-remotemailbox?view=exchange-ps    

It says that you first need to remove the Exchange Online license for the mailbox. Otherwise, the mailbox won't be removed. Then only use disable-remotemailbox cmdlet to remove a cloud-based mailbox but keep the associated on-premises user account.    

So my question is after removing Exchange Online license, do I also have to wait for directory synchronization to be completed/finished before using the Disable-RemoteMailbox cmdlet to remove mailbox from cloud(O365)?    

Kindly answer specific to the above mentioned question and share Microsoft article that describes the situation.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-01*

Hello Team,

I have once concern in my users situation he did not migrate but did create 13 cloud mailboxes with license which includes Teams. 

There is no data in cloud Mailboxes and teams is syncing with cloud one and has no data but they want  it to sync with On-prem mailboxes.

So now user wants to delete the cloud mailboxes or delete or disable and want Teams to sync with On-prem mailboxes. 

I believe if I remove the License Teams app will also be disabled and deleted which user does not want to. 

User only wants to delete cloud mailboxes. 

Please help me in proceeding further on the same.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-07*

Is it possible to remove the Exchange Online license for the mailbox when the O365 Exchange licence has been assigned as part of a bundle - such as Microsoft 365 A3 for faculty? Or does the whole bundle have to be removed?
