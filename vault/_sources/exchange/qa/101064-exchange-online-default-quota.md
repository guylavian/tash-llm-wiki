---
title: "Exchange online default quota"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/101064/exchange-online-default-quota
question_id: 101064
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange online default quota

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/101064/exchange-online-default-quota (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Until recently we had a default mailbox quota which was intentionally set lower than the Microsoft default. For some reason this has vanished recently and reverted to the default (no idea why - has anyone else experienced this?)  

Can anyone point me in the direction of how to change the default back to what we want it to be? I have already dealt with the existing mailboxes, so it's just for those created from now on.  

This KB: https://support.microsoft.com/en-au/help/2490230/how-to-set-exchange-online-mailbox-sizes-and-limits-in-the-office-365  

Shows how to change the limits for mailboxes which exist, but I don't want to have to do this every time I create new mailboxes - they need to be created at the size we want them, as they were until recently.  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-21*

Thanks! Seems to have worked OK otherwise - just set up a test mailbox and it was given the correct limit.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-21*

Thanks. So I tried this:

Get-MailboxPlan | Set-MailboxPlan -ProhibitSendQuota 11GB -ProhibitSendReceiveQuota 12GB -IssueWarningQuota 10GB

And I got the followign error (I am using an admin account) - have I got the synax wrong somewhere?

The operation on mailbox "ExchangeOnlineDeskless-" failed because it's out of the current user's write scope. The value of properties  

'IssueWarningQuota,ProhibitSendQuota,ProhibitSendReceiveQuota' exceeds the maximum allowed for user 'ExchangeOnlineDeskless-' with license  

'BPOS_S_Deskless'.  

-  CategoryInfo : InvalidOperation: (ExchangeOnlineD...:ADObjectId) [Set-MailboxPlan], InvalidOperationException  

-  FullyQualifiedErrorId : [Server=,TimeStamp=21/09/2020 12:43:41] [FailureCategory=Cmdlet-InvalidOperationException] A35C8BB3,  

Microsoft.Exchange.Management.RecipientTasks.SetMailboxPlan  

-  PSComputerName : outlook.office365.com

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-21*

You need to set it on the mailbox plan level, via Set-MailboxPlan:  

```
Get-MailboxPlan | Set-MailboxPlan -ProhibitSendReceiveQuota 49.5GB
```
