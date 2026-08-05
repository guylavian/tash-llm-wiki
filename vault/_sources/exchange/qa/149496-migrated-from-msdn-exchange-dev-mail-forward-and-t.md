---
title: "[Migrated from MSDN Exchange Dev] Mail Forward and (Transport) Rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/149496/migrated-from-msdn-exchange-dev-mail-forward-and-t
question_id: 149496
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Mail Forward and (Transport) Rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/149496/migrated-from-msdn-exchange-dev-mail-forward-and-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/71f68818-e4e8-416d-81ac-0b1a1a2b3d67/mail-forward-and-transport-rules?forum=exchangesvrdevelopment  

We have a mailbox where we need to forward the emails received to it to an external party.   

Mail Forwarding was configured in a standard way through the Exchange Admin Center (O365):  

-  Mail contact created with external e-mail address  

-  Mailbox configured for Mail Forwarding (Mailbox Features > Mail Flow > Enable Forwarding (Deliver messages to both forwarding address and mailbox) > Select Mail Contact  

This configuration has been verified and is working correctly.  

As the external party cannot handle emails with Sensitivity tag "private" a (Transport) Rule was created on the Exchange Admin Center (O365):  

If mail is being sent the mailbox and the Sensitivity header contains "private" or "company-confidential, we change the message header 'Sensitivity' towards 'Normal'.  

However, this seems to have an impact on the mails that are being delivered to the mailbox (messages are delivered to both forwarding address and mailbox), but the external party is still receiving the mails flagged as private.  

Are Mail Forwarding rules being applied before Transport Rules are being applied ? How can we correct the configuration to remove the private flag.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-03*

What transport rule do you created? You can post the screenshot here, and don't forget to cover your personal information. I will do more test in my environment to see if the issue can be reproduced.    

Please also check the message tracing logs for the message forwarded to external users, to see if the event Transport rule is generated. In general, the transport rule should be applied to the redirected message before it leaves your organization.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
