---
title: "Gmail migration to Exchange Online: forwarding address exception"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/268863/gmail-migration-to-exchange-online-forwarding-addr
question_id: 268863
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Gmail migration to Exchange Online: forwarding address exception

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/268863/gmail-migration-to-exchange-online-forwarding-addr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we are migrating mailboxes from Gmail to Exchange Online.    

We see that all emails were migrated, but the migration prosses finished with an error:    

Unable to use primary Gmail forwarding address exception. Disallowed Forwarding Address Permanent Exception. Could not use the primary address as the forwarding address "user@keyman  .com". Please select a different target delivery domain.    

What does it mean and how to fix it?    

Thank you!

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-12*

Hello Joyceshen-MSFT,  

thank you for your answer.  

the email addresses in the CSV file are correct. All email items were successfully migrated, we can see them in Exchange OWA, but migration tasks still shows status - failed, because of the error above.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-12*

Hi @Anahaym      

Are you following the steps list in the official document which introduces about Migrate consumer Google Workspace (formerly G Suite) mailboxes to Microsoft 365 or Office 365    

And according to your error information above, please check that your migration file has the correct Microsoft 365 or Office 365 email address in the EmailAddress column.    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-23*

Hi,

I also faced the same error:

Couldn't use the primary address as the forwarding address "****m". Please select a different target delivery domain. --> The requested forwarding address is not allowed. --> The web server responded with a 400 Bad Request error.  Uri: https://www.googleapis.com/gmail/v1/users/**m/settings/forwardingAddresses

And from the looks of it all emails went fine. 

I am able to send email from microsoft account and recieve email as well.

What is error?
