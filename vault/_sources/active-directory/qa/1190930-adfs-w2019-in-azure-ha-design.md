---
title: "ADFS W2019 in Azure HA design"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190930/adfs-w2019-in-azure-ha-design
question_id: 1190930
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS W2019 in Azure HA design

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190930/adfs-w2019-in-azure-ha-design (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there we have a biz requirement to build ADFS w/ W2019, due to existing legacy components we won't be using AAD. 

FOr our ADFS build what we want to acheive is to build ADFS across 2 different Azure regions to delivery HA - we are considering either an Active- Standby design or Active-Active. Any suggestions on how this can be achieved? 

I understand due to the SQL requirements of ADFS having the ADFS run between 2 different Azure regions may increase complexity with the SQL and we can't use SQL PAAS either but would like to hear everyone's thoughts. Is SRM also an option? We are considering to look at Azure traffic manager to manage the A/A or A/S traffic.

This ADFS will be both internal and external facing so will need WAP as well.

## Answers

_No answers on this thread._
