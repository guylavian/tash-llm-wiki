---
title: "TLS 1.2 supportable Ciphers for Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/425138/tls-1-2-supportable-ciphers-for-exchange-2016
question_id: 425138
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# TLS 1.2 supportable Ciphers for Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/425138/tls-1-2-supportable-ciphers-for-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,    

I have Exchange 2016 environment, for improving security we have disabled SSL 2.0, SSL3.0, TLS 1.0 and TLS 1.1 protocols. Now this environment running on TLS 1.2, recently I have performed SSL Report scan on https://www.ssllabs.com/ seams everything showing fine with A+ rating certificate from SSL Labs, But I have observed few weak Ciphers under TLS 1.2(Please check the attached image for more details of Weak ciphers).    

Can we remediate these weak ciphers? Is it harmful to any exchange functionalities? Please assist on this.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-07*

Hi @RamaRaju Chennu  ,    

The following highly detailed Microsoft blog posts might be helpful:    

-  Exchange TLS & SSL Best Practices    

-  Exchange Server TLS guidance, part 1: Getting Ready for TLS 1.2    

-  Exchange Server TLS guidance Part 2: Enabling TLS 1.2 and Identifying Clients Not Using It    

-  Exchange Server TLS guidance Part 3: Turning Off TLS 1.0/1.1    

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Best regards,    

Leon
