---
title: "Exchange OnPrem 2019 not sending auto reply for Message Size Exceed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664990/exchange-onprem-2019-not-sending-auto-reply-for-me
question_id: 1664990
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange OnPrem 2019 not sending auto reply for Message Size Exceed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664990/exchange-onprem-2019-not-sending-auto-reply-for-me (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Sending email form my Yahoo and Gmail and it goes through our Spam Filter, but Exchange gives it a ROUTING  FAIL event as the message size of 20MB exceeds the users limits.  The problem is , I dont get a reply from my exchange to my  Yahoo or Gmail that the email was undeliverable.  Nothing is in our QUEUE.  Please help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-13*

Hi @Wes K,

Welcome to the Microsoft Forum for technical support.

Based on your description, I would like to confirm with you: except Yahoo and Gmail email accounts, do other external account have similar problems?

If not, it may be caused by the account types of Yahoo and Gmai.

If so, the problem may be caused by the Barracuda spam filter. It is recommended that you temporarily turn off this feature and retest to see if the problem persists. 

In addition, I recommend that you configure the Postmaster address in your environment to confirm whether an NDR is generated. The Postmaster General is responsible for receiving copies of NDRs and handling issues.

For how to configure the Postmaster address, you can refer to the following steps:

-  Log in to the local Exchange admin center.

-  Click Mail Flow>Send Connector>...>Organization transport settings.

-  Fill in the external postmaster address.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-10*

I would look at the "spam filter"
