---
title: "Best Sequence to decommission AADC and Exchange hybrid after migrate one of the domain to Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/369042/best-sequence-to-decommission-aadc-and-exchange-hy
question_id: 369042
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Best Sequence to decommission AADC and Exchange hybrid after migrate one of the domain to Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/369042/best-sequence-to-decommission-aadc-and-exchange-hy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,    

Our AD and On-premise exchange server have multidomain user mailbox. We setup AADC and Exchange hybrid to migrate one of the domain to exchange online.    

Now, the migration is completed. All of that domain mailbox are moved to Exchange online. We need to disconnect the relationship of on-premise exchange and exchange online. And both EXO and on-premise exchange mailbox should sent to others and internet normally.     

I study this documents but not fit our scenario (https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange).      

What is the best sequence on our case? Do below sequence correct?    

Change that domain MX record to EXO > Remove Exchange Hybrid server > Disable directory sync to convert sync user to cloud user > Remove AADC ?    

Thank     

Chong

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-26*

@KyleXu-MSFT  ,    

Thanks. Then do I need to run "Remove-HybridConfiguration" in my case? As we won't migrate remain domain user to o365    

Thanks    

Chong
