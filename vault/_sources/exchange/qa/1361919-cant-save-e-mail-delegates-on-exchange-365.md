---
title: "Can't save e-mail delegates on Exchange 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1361919/cant-save-e-mail-delegates-on-exchange-365
question_id: 1361919
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Can't save e-mail delegates on Exchange 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1361919/cant-save-e-mail-delegates-on-exchange-365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Sir,

I can't save setting e-mail delegates on Exchange 365 for this group.

But another team I can do it.  

Please help to solve (  T-T)

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-08*

Hi @IT administrator,

Is this affected group a Microsoft 365 group or a distribution group?

Please connect to Exchange Online Powershell and run the following cmdlet to see if it works for you:

```
Add-RecipientPermission "Group Name here" -AccessRights SendAs -Trustee "user name here"
```

If the cmdlet does not work for you either, please post the error message if there is any.

If this group is a distribution group, please also try recreating it and see if it can help with this issue.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
