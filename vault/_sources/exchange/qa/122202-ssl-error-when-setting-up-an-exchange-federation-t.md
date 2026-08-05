---
title: "SSL error when setting up an Exchange Federation Trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/122202/ssl-error-when-setting-up-an-exchange-federation-t
question_id: 122202
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# SSL error when setting up an Exchange Federation Trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/122202/ssl-error-when-setting-up-an-exchange-federation-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to setup an Exchange Federation Trust with our parent compnay.   

After opening the firewall holes, the source Federation Trust domain is getting an error when trying to connect.  

The user on the source Federation trust is presented with the SSL cert for the Exchange server when trying to browse free/busy calenders.  

I am thinking this is because the SSL cert presented is for the local Exchange server itself and not the autodiscover/external mail domain name.   

I can edit the IIS edit bindings section on the Exchange server websites but need clarification if this the right solution.  

Will assigning the external SSL cert to the Exchange IIS Backend or default website resolve the issue ?  

We cannot try the edit bindings without a change control as Production emails will be affected so need to run this after hours.

## Answers

_No answers on this thread._
