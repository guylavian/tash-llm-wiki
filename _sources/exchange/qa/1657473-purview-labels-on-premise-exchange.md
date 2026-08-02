---
title: "Purview Labels On Premise Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657473/purview-labels-on-premise-exchange
question_id: 1657473
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-information-protection", "office-exchange-office-exchange-server-management"]
---
# Purview Labels On Premise Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657473/purview-labels-on-premise-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I posted this in the Exchange Online group but they suggested I try here instead so:

With the recent changes to the Azure Information Protection agent being discontinued we're experiencing a problem we never had before, at least we believe the two are connected. I'll explain our environment a little first:

 

-  Azure enterprise agreement with all users having E5 licenses

-  All users use Exchange online for most day to day business

-  Sensitivity Labels deployed to all users

-  A small number of users also have access to an on-premise Exchange server used for very specific business needs. This Exchange server is not federated with Exchange online and has a separate local Active Directory to hold the user accounts. Essentially it's an on-prem only setup as the data it holds is not allowed to be stored in the cloud

-  Users of the on-prem Exchange have both their email accounts configured in the same Outlook profile

 

Up until the recently users of the on-prem Exchange where able to pick from the labels published in Purview and use them when sending email from either their on-prem or online Exchange account but now when changing the from address field in Outlook to the on-prem one they lose access to the sensitivity button (becomes greyed out).

 

Is this change expected? Is there something we can do to bring back the sensitivity button in Outlook when sending from the on-prem account? I've installed the new Purview Information Protection agent and tried making changes to UseOfficeForLabelling and AIPException but nothing gives us back the sensitivity button.

 

Thanks

## Answers

_No answers on this thread._
