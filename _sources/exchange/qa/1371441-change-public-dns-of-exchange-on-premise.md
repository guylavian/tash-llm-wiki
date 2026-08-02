---
title: "Change public DNS of Exchange On Premise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1371441/change-public-dns-of-exchange-on-premise
question_id: 1371441
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Change public DNS of Exchange On Premise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1371441/change-public-dns-of-exchange-on-premise (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We just migrated one of our companies to Cloud only, due to history everything in our environment is based on this company. One of these things is the exchange domain name. For the moment our exchange internal + External is exchange.company... and this is in use by all our other companies and holding company.

As this company migrated to cloud only I would like to change this to exchange.holdingcompany..., I have the needed certificate and domain name but I am wondering what the impact for our users is as every pc, mobile phone is using exchange.company...

Current setup is as followed:

-  Exchange.company... ==> Redirect to OnPrem Server

-  Autodiscovery.company... ==> Redirect to Exchange Online.

-  Other Company ==> Service Publishing in External + Internal DNS to redirect Autodiscover to exchange.company...

So if all these entries are changed to exchange.holdingcompany... and exchange is configured to use exchange.holdingcompany... how will client devices react?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-26*

Hi @ Michiel Cornille - Real United,

To change the on-prem external DNS records, you need to make sure that the users’ primary email addresses are updated to the new domain name.

You can use the email address policy to bulk edit users in your organization :Procedures for email address policies in Exchange Server | Microsoft Learn

Then, for user mailboxes after the email address change, I recommend that you recreate the Outlook profile.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
