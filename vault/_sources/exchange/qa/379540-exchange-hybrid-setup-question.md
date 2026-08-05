---
title: "Exchange hybrid setup question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/379540/exchange-hybrid-setup-question
question_id: 379540
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange hybrid setup question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/379540/exchange-hybrid-setup-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I have two question about exchange hybrid option.    

There are classic and modern hybrid option, I found this article is some what useful    

But it does not answer all my questions.    

Here is my situation, I have on-prem exchange 2019 servers, there are 3 of them and it is clustered (DAG), requirement is setup hybrid only, so that teams can see employees' free busy info and show availability information correctly. We will not utilize office 365 (exchange online) to receive and send external emails.    

We will not move any mailboxes to the exchange online. The only reason we want to setup the exchange hybrid is to sync free/busy info for teams.    

Q1, I went to an office 365 class and the instructor said only way to make the free/busy info to be synced to exchange online is to perform modern full sync, however it will sync (duplicate) users' mailboxes to exchange online the reason is that when on-prem exchange goes fubar I can immediately use the exchange online, is this true? if it is true how do I prevent it from happening.    

Q2, What is the most important difference between classic and modern hybrid?? the technet web site does not really say anything about it.    

My question is simply, how do I sync only free busy info to exchange online?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-02*

You have to use full Hybrid if you want calendar integration - which I assume you do  :)    

https://learn.microsoft.com/en-us/microsoftteams/exchange-teams-interact
