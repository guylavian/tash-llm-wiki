---
title: "Path from Exchange 2019 on-oremise with ADFS and MFA to Exchange Hybrid with on-premise MFA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2155350/path-from-exchange-2019-on-oremise-with-adfs-and-m
question_id: 2155350
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Path from Exchange 2019 on-oremise with ADFS and MFA to Exchange Hybrid with on-premise MFA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2155350/path-from-exchange-2019-on-oremise-with-adfs-and-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

we are in the process of implementing Exchange Hybrid and have some questions:

At the starting point we had an on-premise Exchange environment composed by two Exchange Mailbox servers, hardware load balanced with ADFS and RCDevs integration MFA

We want to implement Office 365 Hybrid using our on-premise MFA appliance

We subscribed an Office 365 account and run the Entra Connect Sync wizard to syncronize a group of test users. Sync was fine.

Then we improved Office 365 login using our on-premise MFA RCDevs, so both on-premise and online users are using the same login process. This was working fine too.

Then we run the Exchange Hybrid Wizard, selecting Full Hybrid Configuration, with Exchange Modern Hybrid Topology

The wizard was fine but had a warning in the very end about Oauth was not enabled.

Doing some tests we found that a user whom mailbox was migrated from on-premise to Office365 was asked twice for MFA authentication, and some other issues like missing the integration with Teams calendar

In order to fix all these issues, we understand that we need to enable Hybrid Modern Authentication, leveraging on External Authentication Methods to keep using our on-premise MFA RCDevs

So we plan to switch from Exchange Modern Hybrid Topology to Exchange Classic Hybrid Topology

then implement Microsoft Entra ID External Authentication Method to enable MFA

and finally configure Hybrid Modern Authentication in Exchange on-premises

Do you thing that we are on the correct path to have a an Exchange Hybrid configuration fully configured and working, having some on-line and some on-premise mailboxes, same login process for both, and no issue with Teams calendar integration?

Once HMA will be configured, on-premise users will need any licence to use HMA (like Entra P1 or P2)? or only 365 mailboxes will need such license?

Thank you and best regards

## Answers

_No answers on this thread._
