---
title: "Exchange PrepareAllDomains doesn't seem to work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1528545/exchange-preparealldomains-doesnt-seem-to-work
question_id: 1528545
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Exchange PrepareAllDomains doesn't seem to work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1528545/exchange-preparealldomains-doesnt-seem-to-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I'm building a lab for testing migrations of Exchange.  

I am building a Exchange 2013 server at the moment.  I've updated the schema.  I've preparedAD.    

When I run PrepareAllDomains nothing is happening in subdomains.  

The structure is one root domain with one subdomain.  On the same network 192.1...   

All replication is good with DC's.  Permissions are correct.  I'm using the default root Administrator account.  

Is there a reason this is not running for the subdomain?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-09*

I need to stop using the defaul adminitrator for labs.  :)
After using a new account with correct rights it worked.
Lesson don't use default Domain Admin account.
