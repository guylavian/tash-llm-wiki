---
title: "Parent/Child domains and Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1134393/parent-child-domains-and-exchange
question_id: 1134393
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Parent/Child domains and Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1134393/parent-child-domains-and-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am about to carry out some work and just want to clarify if it will achieve what I want and there will no adverse effects. Here is my scenario:    

Parent domain - Server 2016    

```
- Exchange 2019 (this is the live production environment)
```

child domain - server 2016    

```
- Child Domain member ready for exchange 2019
```

Both domains are on the same subnet and are at the same site. DNS is working perfectly between the two and the DHCP servers are in the parent domain.    

I am about to install Exchange 2019 on a server in the child domain. How will this effect Exchange/Email in the parent domain? Ideally, I want the child domain email to be completely separate from the parent.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-21*

Hi all, thanks a lot for your respond.    

I did the installation already for child domain exchange but the ecp keep directing to the parent exchange not to the new child one. any ideas what should i do to separate the child exchange from the parent one.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-20*

Hi @Mohamed Zakaria Amer   ,    

Agree with Andy, installing Exchange 2019 in a child domain doesn't affect its parent domain.    

To install Exchange Server in a child domain, you need to run the "prepare" command line on the root domain.    

Here is a similar thread for you reference. Although it is Exchange server 2013, but it’s same to Exchange server 2019:    

How to Install Exchange Server in Child Domain Server (microsoft.com)    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
