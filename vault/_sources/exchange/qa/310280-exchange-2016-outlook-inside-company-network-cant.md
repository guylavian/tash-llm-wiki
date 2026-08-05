---
title: "Exchange 2016 - Outlook inside company network CANT connect without Internet connection."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310280/exchange-2016-outlook-inside-company-network-cant
question_id: 310280
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 - Outlook inside company network CANT connect without Internet connection.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310280/exchange-2016-outlook-inside-company-network-cant (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Outlook inside company network (Intranet) can not load or connect to exchange 2016 automatically without aan internet connection. Both my lab exchange 2016 server and lab PC with outlook 2013 are on same network but without Internet it does not connect to exchange. When i turn Internet ON then it works. AutodiscoverServiceInternalURI for my CAS service is - https://autodiscover.domain.com/autodiscover/autodiscover.xml. I have also checked with https://serverfqdn/autodiscover/autodiscover.xml AutodiscoverServiceInternalURI is responsible for connecting within Intranet, correct ? What am i missing here ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi,    

Which URL is set for AutodiscoverServiceInternalURI actually?    

When you turn Internet OFF, pressing CTRL and right-click Outlook icon, select Test Email Autoconfiguration, typing the account and password, a normal test looks like:    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
