---
title: "query on transport rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1504269/query-on-transport-rule
question_id: 1504269
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# query on transport rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1504269/query-on-transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All
I am using exchange 2016 hybrid environment. we create users in onprem and migrate to online.I have 100 users and these 100 users have two accounts in AD, lets say ******@contoso.com is a regular account with E5 license and ******@contoso.com is just an AD user which is synced to Azure ******@consoto.com doesnot have a valid mailbox or license. when any email is triggered to ******@contoso.com the email should be forwarded or redirected to ******@contoso.com. is it possible to achieve this using transport rule. in one transport rule i want to add 100 users like the below as i cannot create 100 rules. if it is possible do i need to create transport rule in exchange onprem or online.

```
when email is received to ******@contoso.com, the email should be forwarded or redirect to ******@contoso.com 
when email is received to ******@contoso.com, the email should be forwarded or redirect to ******@contoso.com 
when email is received to ******@contoso.com, the email should be forwarded or redirect to ******@contoso.com
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-01-21*

You would need 100 rules so not practical. 
It better to set forwarding on each mailbox in Exchange Online to the specific SMTP Address.
https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/configure-email-forwarding
