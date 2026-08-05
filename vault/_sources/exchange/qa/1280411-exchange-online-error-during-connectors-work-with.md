---
title: "Exchange online error during connectors work with my on-premises email servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1280411/exchange-online-error-during-connectors-work-with
question_id: 1280411
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange online error during connectors work with my on-premises email servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1280411/exchange-online-error-during-connectors-work-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi expert, 

I want to setup connectors work with my on-premises email servers.

and in my exchange Connectors I hit error for RecipientStatus:[{LED=550 5.1.10 RESOLVER.ADR.RecipientNotFound; Recipient ******@xxx.com not found by SMTP address lookup};{MSG=};{FQDN=};{IP=};{LRT=}]

log.txt

attached with the error message log. 

can someone help me, how I can solve this issue? 

thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-10*

Hi @ Kelvin Shee,

Just wondering if you created a remote mailbox on-premises for this recipient?

This issue occurs if the user was created in Microsoft 365 and the on-premises Exchange environment doesn't have objects for the user to reference.

 

You can refer to this link to create a remote mailbox on-prem, and then test whether sending mail is successful after directory synchronization:

NDR error 550 5.1.10 RESOLVER.ADR.RecipientNotFound - Exchange | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
