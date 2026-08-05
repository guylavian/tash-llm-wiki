---
title: "Microsoft.Exchange.WebServices.Data.EmailMessage error \"The operation can't be performed because the item is out of date. Reload the item and try again\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1685346/microsoft-exchange-webservices-data-emailmessage-e
question_id: 1685346
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 23
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Microsoft.Exchange.WebServices.Data.EmailMessage error "The operation can't be performed because the item is out of date. Reload the item and try again"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1685346/microsoft-exchange-webservices-data-emailmessage-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have been using Microsoft Exchange Web Services for a couple of years in my asp.net c# system and had no issues.

Last week 1 customer started getting below error, then yesterday another customer and 2 more today!

Microsoft.Exchange.WebServices.Data.EmailMessage error "The operation can't be performed because the item is out of date. Reload the item and try again"

Could you please advise why this may happen and what possible ways are to resolve this?

Regards & Thanks,

David

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-06-04*

Via support apparently this issue is being tracked as EX796633 but it's not appearing in Service Health for me in admin.microsoft.com. Is it appearing for anyone else?

Here's what I received from MS support:

-  Issue ID: EX796633

-  Title: Some users can’t send email messages from mailboxes through the EWS API

-  User Impact: Users are experiencing difficulties sending email messages from mailboxes via the EWS API.

-  Current Status: Our team is diligently reviewing the information provided by support to determine the next steps in our troubleshooting process.

-  Scope of Impact: Your organization may be affected by this event, particularly if some of your users are attempting to send emails from mailboxes using the EWS API.

-  Next Update: We will provide further updates by Wednesday, May 29, 2024, at 4:30 PM UTC.

## Answer (community) — community member

*upvotes: 1 · updated: 2024-05-28*

We are having the same issues since Thursday, May 23. Some mails are sent, while others are not, with the above error-message.

Using Microsoft.Exchange.WebServices.dll with Version 2.2.1.0!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-24*

Same issues in my environment. using Microsoft.Exchange.WebServices 2.2.0 and Exchange.WebServices.Managed.Api 2.2.1.1

Any estimates on fixing the issue ?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-24*

Any updates about this problem?
