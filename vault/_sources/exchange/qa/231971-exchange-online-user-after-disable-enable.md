---
title: "Exchange online user after disable/enable"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/231971/exchange-online-user-after-disable-enable
question_id: 231971
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange online user after disable/enable

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/231971/exchange-online-user-after-disable-enable (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have problem user with Exchange online E1 license. We appeared that the user was temporary Disabled and then enabled again. Office 365 user is working fine and syncing with hybrid environment, when we go to Exchange Online Admin page no user mailbox. Tried to re add E1 license multiple times and resync user but nothing wont work.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

Hi @Dominykas Šivickas   ,    

How did you disable this user mailbox？    

Could you see it in the Active users in Microsoft 365 admin center?    

How long did you check after enabling the user mailbox? According to my test, I delete a user mailbox and recovery it. After waiting for about 12 hours, I could view it in the EAC, and the function of the user's mailbox was normal during this period.    

Please run the following command to confirm user mailbox.    

```
Get-Mailbox –Identity <>
```

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-15*

Define "temporary"? If more than 30 days have passed, the mailbox cannot be recovered/reconnected. If its less than 30, just give it some time to reconnect.  

It also depends on how you "disabled" it, if you removed the license or removed the user object altogether, etc.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-15*

@Dominykas Šivickas       

An EOA subscription can be purchased separately for each mailbox that requires either the inactive mailbox or archive feature.    

Refer to the Exchange Online service description    

----------    

Please don’t forget to `Accept the answer` and `up-vote` wherever the information provided helps you, this can be beneficial to other community members.
