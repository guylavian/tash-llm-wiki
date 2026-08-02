---
title: "How To Completely Migrate Active directory of On-Prem Domain \"abc.local\" to a Domain controller in Azure having new domain \"xyz.co.uk\", so I can manage Active directory from Azure DC only. And decom the On Prem Domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1535720/how-to-completely-migrate-active-directory-of-on-p
question_id: 1535720
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How To Completely Migrate Active directory of On-Prem Domain "abc.local" to a Domain controller in Azure having new domain "xyz.co.uk", so I can manage Active directory from Azure DC only. And decom the On Prem Domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1535720/how-to-completely-migrate-active-directory-of-on-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys,  

I have an on-prem environment running domain controller with domain "abc.local" and I want to migrate all the contents of this DC to The Azure VM DC which is running a different domain "xyz.co.uk". I couldn't find any documentation that would completely replicate/merge the on-prem objects including group policies to the Azure domain.  

There was ADDS which came close to achieving this but it can only be used to replicate on an existing domain, not a different domain.  

Also, I have a site-to-site connection established so Azure VM DC and On-Prem DC can communicate with each other.  

Can anyone suggest me the procedure to migrate this "abc.local" AD to Azure DC with new domain "xyz.co.uk"

## Answers

_No answers on this thread._
