---
title: "Aruba mail provider read in online exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2138782/aruba-mail-provider-read-in-online-exchange
question_id: 2138782
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Aruba mail provider read in online exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2138782/aruba-mail-provider-read-in-online-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,

a customer we are working with right now has Aruba as their mail provider, but uses an on-prem exchange server that synchronizes mail via a connector. So they read their mail from Outlook by connecting to the on-prem exchange server.

Having their Office Premium licenses, I would like them to read the email via online exchange but continuing to have Aruba as their provider.

Is it possible to do this without changing the current on-prem configuration?

If I change the DNS on the Aruba host will the on-prem server stop receiving mail?

Can the two configurations coexist?

Thanks so much in advance.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-31*

Hi,@Marco Massasso

Thanks for posting your question in the Microsoft Q&A forum.

Based on the information you've provided so far, I currently have some questions about the circumstances of your Exchange.

1.Do you currently only have On-pre Exchange?

2.If you want to use Exchange Online, why not consider migrating your entire mailbox to Exchange Online?  If users are all Online, there will be no need for a third party to perform maintenance; Microsoft is responsible for Exchange Online maintenance.

3.Can you describe what you're doing this for?
