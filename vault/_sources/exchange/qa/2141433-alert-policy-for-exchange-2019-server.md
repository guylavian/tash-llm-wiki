---
title: "Alert Policy for Exchange 2019 Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2141433/alert-policy-for-exchange-2019-server
question_id: 2141433
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Alert Policy for Exchange 2019 Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2141433/alert-policy-for-exchange-2019-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to set up an alert policy for our exchange server when a user sends out more than 150 emails in one day, but I'm only finding instructions for Office 365.

How would I go about this?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-08*

Hi @Audra,

Welcome to the Microsoft Q&A platform!

Based on your description, to set up an alert policy for your Exchange Server (e.g. Exchange 2019) to notify you when a user sends more than 150 emails in a day, you can follow these steps:

-  Log in to your Exchange Admin Center.

-  In the left pane, select Mail Flow.

-  Click Alert Policies, and then click New Alert Policy.

-  Configure the alert policy:

-  Provide a name for your policy (e.g. "High Email Volume Alert").

-  (Optional) Enter a description for the policy.

-  Set the conditions for the alert. In this example, you want to set a threshold when a user sends more than 150 emails in a day.

-  Specify the threshold (150 emails) and the time period (1 day).

-  Select the Notification Options:

-  Decide if you want to receive email notifications when the alert is triggered.

-  Select the recipients who should receive these notifications.

-  Review your settings and click Save to create the alert policy.

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
