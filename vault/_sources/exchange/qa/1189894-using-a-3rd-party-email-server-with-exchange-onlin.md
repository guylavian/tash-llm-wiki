---
title: "Using a 3rd party email server with Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189894/using-a-3rd-party-email-server-with-exchange-onlin
question_id: 1189894
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
---
# Using a 3rd party email server with Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189894/using-a-3rd-party-email-server-with-exchange-onlin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Our client currently uses an on-prem 3rd party email server (FortiMail, non-Microsoft) with approx. 2000 mailboxes and is planning migration to Exchange Online later in the future. This system also does security filtering. Some mailboxes (around 60) are already in Exchange Online. MX is pointing to an on-prem 3rd party email server. They would like to consolidate mail flow by pointing MX record to Exchange Online so that all email traffic flows through Exchange Online through the use of inbound and outbound connectors, that route traffic to and from a 3rd party email server. 

Our implementation partner says that in order to do so, we need EOP licenses for all on-prem users. We do not want any EOP filtering to be applied for these on-prem users. They sent us the Exchange Server FAQ article below: 

https://www.microsoft.com/en/microsoft-365/exchange/microsoft-exchange-licensing-faq-email-for-business

 If I have some users hosted in Exchange Online, and some users on-premises, can I point my MX record at Microsoft 365 instead of my on-premises servers? If so, do I need Exchange Online Protection subscriptions for the on-premises users?

You can point your MX record to Exchange Online in a hybrid deployment. In this scenario, Exchange Online Protection (EOP) provides anti-spam and anti-malware filtering on inbound mail for the on-premises users, so these on-premises users require EOP subscriptions.

My understanding is that this statement is only true for Exchange Hybrid scenarios, what excludes a 3rd party mail servers, so we should not need any additional licenses for the scenario I outlined above.

Can someone please provide some more information about this?

Thanks

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-17*

Hi @ Michael Novak ,

Based on our research, all emails flowing through Exchange Online do not require an additional EOP license subscription.

So you don't need to provide it for all local users.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
