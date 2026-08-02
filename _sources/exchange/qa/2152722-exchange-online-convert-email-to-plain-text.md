---
title: "Exchange Online - Convert email to Plain-Text"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2152722/exchange-online-convert-email-to-plain-text
question_id: 2152722
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online - Convert email to Plain-Text

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2152722/exchange-online-convert-email-to-plain-text (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,

I hope someone can help me.

I have an email address - let say "@my-business.com" - and I'm redirecting all messages to "@external.com" to manage all the orders. "******@external.com" is located on a platform where for security HTML in emails is blocked. Therefore some redirected emails containing links embedded in pictures/logos/buttons/etc after redirection are not shown on the external platform and the links are cut out/missing.

I was asked to check out if there is possibility to configure an Exchange Online rule that will target all emails sent to "@my-business.com" address, then converted to Plain-Text and then redirected to "@external.com".

Does Exchange Online offer something like that. Or maybe Remote Domains in Exchange.

If yes, can someone please provide configuration steps?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2026-04-07*

In Exchange Online, you can convert an email to plain text either manually or by changing settings.

For a single email, open it in Microsoft Outlook (desktop or web), go to formatting options, and switch the message format from HTML to Plain Text before sending.

To make all emails plain text by default, go to Outlook settings → Mail → Compose and reply, and set the message format to Plain Text.

For admins using Exchange Online (via Microsoft 365), you can also configure mail flow rules to enforce plain-text formatting for specific users or domains.

This helps improve compatibility, reduce formatting issues, and enhance security by avoiding embedded scripts or styling. For more practical workflow tips like this, you can also explore resources on univik.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-30*

Yes, you should be able to achieve that in Exchange Online. If you only want this behavior for a single recipient, create a mail contact for it, then toggle the setting 

```
New-MailContact -Name orders -ExternalEmailAddress ******@external.com
Set-MailContact ******@external.com -MessageBodyFormat Text
```

Alternatively, you can do this on the domain level, via the New-RemoteDomain cmdlet. Details can be found for example here: https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/message-format-and-transmission
