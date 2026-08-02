---
title: "Outlook365 Merges contacts from multiple Exchange accounts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/368777/outlook365-merges-contacts-from-multiple-exchange
question_id: 368777
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Outlook365 Merges contacts from multiple Exchange accounts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/368777/outlook365-merges-contacts-from-multiple-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a situation.  

Outlook 365, domain workstation, 2 exchange accounts - 1 from the domain in which workstation joined, 1 from another forest.  

Two mailboxes are created:  

******@domainA.com, ******@domainB.com. The usernames (exchange aliases) are the same for both domains.  

The address book and GAL on domainA.com are updated less frequently than in domainB.com.  

We have faced an issue, when working on account in domainA.com (in the upper section of message or meeting creation resides the domainA.com account) we started to search the ******@domainA.com, but Outlook gave us an GAL entry from domainB.com (because on that moment GAL for domainA.com was not updated on the client).  

How can we avoid such a problem in the future? So the Outlook can not take entries from GAL domainB.com when working with domainA.com account?  

Right now I've only one solution for this - to change aliases in the domainB.com so that they do not equal aliases in the domainA.com, but it's very uncomfortable to make about 100 manual changes in the AD/Exchange.

## Answers

_No answers on this thread._
