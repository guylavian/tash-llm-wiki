---
title: "Exchange hybrid configuration wizard stuck: no shared domain names has been detected within the exchange online and on-prem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1183578/exchange-hybrid-configuration-wizard-stuck-no-shar
question_id: 1183578
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange hybrid configuration wizard stuck: no shared domain names has been detected within the exchange online and on-prem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1183578/exchange-hybrid-configuration-wizard-stuck-no-shar (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We need to set up exchange hybrid for our environment for the first time.

Currently the HCW gets stuck at hybrid domains page with the following message.

"no shared domain names has been detected within the exchange online and on-prem......"

We are using exchange server 2016 cu23.

We have already run AD connect and synced users successfully to azure AD

The domain is already verified in office365 and added as accepted domain in exchange server

Our local domain is: contoso.fabrikam.com, this is where exchange server is joined.

our users use emails with contoso.com domain

contoso.com is set up as accepted and authoritative domain in exchange server.

contoso.com is verified in office365 as accepted domain and authoritative.

contoso.com is added in active directory in forward lookup zone

contoso.com is added in Active directory as suffix domain.

what could be the issue

attached is the error

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-27*

Hi Benard,  

I'm having the same problem; did you get it resolved?

Thanks

Mahmoud

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-24*

Hi @Benard Mwanza ，

Just wondering if the domain (contoso.com) verified in O365 is the domain name registered/purchased in the domain registration provider.

Also, do you have SSL certificates issued by trusted certificate authorities installed on its Web/Exchange servers? This is to initiate a secure session with the browser.

 

The prerequisites for configuring a hybrid deployment are as follows:

Hybrid deployment prerequisites | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
