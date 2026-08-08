---
title: "Distribution List Settings in Exchange Admin Center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2262282/distribution-list-settings-in-exchange-admin-cente
question_id: 2262282
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Distribution List Settings in Exchange Admin Center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2262282/distribution-list-settings-in-exchange-admin-cente (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are in the process of creating a distribution list in the Exchange Admin Center for internal communications only. I would like to know if there is an option to "Require that all senders are authenticated."

In the "Delivery Management" settings, the only options I see are: 

-  Only senders inside my organization 

-  Allow messages from people inside and outside my organization 

-  Restrict who can send messages to the group.

After conducting some research, it seems there are limitations with the GUI settings, and I may need to use PowerShell to implement the "Require that all senders are authenticated" option. I understand that DKIM and DMARC apply only to external emails, so they aren't relevant for internal communications. Additionally, we have enabled spoof protection for all key users in the anti-phishing policy in Microsoft Defender.

I would like to confirm whether "Require that all senders are authenticated" is an option for distribution lists, or if it is not necessary. If it is possible to set this up, I would appreciate guidance on how to do so.

Thank you for your assistance!

## Answers

_No answers on this thread._
