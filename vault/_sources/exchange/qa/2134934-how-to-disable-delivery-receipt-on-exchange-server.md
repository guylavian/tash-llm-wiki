---
title: "How to disable Delivery Receipt on Exchange Server 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2134934/how-to-disable-delivery-receipt-on-exchange-server
question_id: 2134934
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to disable Delivery Receipt on Exchange Server 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2134934/how-to-disable-delivery-receipt-on-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to know how to turn off Delivery Receipt  On Prem Exchange.

Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-23*

Hi @CC,

Welcome to the Microsoft Q&A platform!

According to your description, to disable delivery receipts on Exchange Server 2016, you can follow the steps below:

-  Log in to your Exchange admin center.

-  In the left pane, click Mail flow.

-  Click the + icon to create a new rule.

-  Configure the rule:

-  Name the rule (for example, "Disable delivery receipts").

-  Under "If this rule applies", select "Message type is", and then select "Read receipts".

-  Under "Do the following", select "Delete the message without notifying anyone".

-  Click Save to apply the rule.

This rule will prevent delivery receipts from being sent from your Exchange Server 2016.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
