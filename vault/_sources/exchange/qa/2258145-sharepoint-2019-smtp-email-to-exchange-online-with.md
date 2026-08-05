---
title: "SharePoint 2019 SMTP Email to Exchange Online without Basic Auth"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2258145/sharepoint-2019-smtp-email-to-exchange-online-with
question_id: 2258145
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# SharePoint 2019 SMTP Email to Exchange Online without Basic Auth

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2258145/sharepoint-2019-smtp-email-to-exchange-online-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an existing SharePoint 2019 on-premises server with SMTP service installed locally that currently relays mail to Exchange Online. With the deprecation of Basic Authentication we need an alternative. As we understand it, SharePoint 2019 doesn't support OAuth and Exchange Online doesn't support Windows Integrated Authentication. What would be the recommended approach for continuing to use Exchange Online with SharePoint 2019?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-20*

SharePoint 2019 does not support OAuth2 (and neither does SharePoint SE) so we need an alternative to the IIS SMTP server that can use OAuth to connect to Exchange Online. If it acts as an SMTP server then SharePoint 2019 should be able to send mail to it. We are still looking for recommendations.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-15*

Hi,You could use SMTP Auth using TLS. A mailbox with minimal license like Exchange online P1excluding MFA. TLS to be enabled/supported on SharePoint. SMTP connection settings to be used as authenticated, TLS with valid certificate.  Dedicated inbound connector, recipient limits to be considered.

References:

SMTP Auth - https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission

Outgoing email configuration on SharePoint - https://learn.microsoft.com/en-us/sharepoint/administration/outgoing-email-configuration?tabs=CASEfarm%2CSEfarm%2CCASEweb%2CSEweb

Exchange online limits - https://learn.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits

If the above suggestion helps, please click on 'Accept answer' and 'upvote' it.
