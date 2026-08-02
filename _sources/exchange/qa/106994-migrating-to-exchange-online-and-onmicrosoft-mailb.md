---
title: "Migrating to Exchange Online and onmicrosoft mailboxes cannot deliver to contact that goes to internal DNS zone not published externally"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/106994/migrating-to-exchange-online-and-onmicrosoft-mailb
question_id: 106994
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Migrating to Exchange Online and onmicrosoft mailboxes cannot deliver to contact that goes to internal DNS zone not published externally

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/106994/migrating-to-exchange-online-and-onmicrosoft-mailb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are migrating from Exchange 2010 to Exchane online.  Everything seems to going good so far, but we have an issue.  Out local domain is conotosocorp.com, but our public/email domain is contoso.com.  We have some Exchange contacts internally that point to alpha.contosocorp.com, but we do not own the public DNZ cone for contosocorp.com  I know this gets confusing, but what happens is someone that has been migrated to the cloud all of the sudden cannot send email to the contact that we have listed as alpha.contosocorp.co,, because we do not own that public domain?  

The issue is alpha.contosocorp.com is a contact for a SMTP server. So basically, I need to figure out a way to route email from office365 to a contact(internal server that it cannot route to publicly)  

If anyone has any idea on this, let me know.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-09-25*

@Heim, Dan       

Agree with AndyDavid. Since the alpha.contosocorp.com is not available from the Internet, we have to create a specific outbound connector to route emails to on-premises organization.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
