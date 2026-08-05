---
title: "How to get Exchange self signed certificate for Samsung email account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2263161/how-to-get-exchange-self-signed-certificate-for-sa
question_id: 2263161
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to get Exchange self signed certificate for Samsung email account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2263161/how-to-get-exchange-self-signed-certificate-for-sa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to get Exchange self signed certificate for Samsung email account.

Exchange email will not work without valid certificate.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-05-05*

Hi Martyn Cann,

Thank you for posting your question in the Microsoft Q&A forum.

The self-signed certificate isn't automatically trusted by client computers and mobile devices, we have to manually add this certificate to the trusted root certificate store on all client computers and devices.

In general, we suggest using certificate issued by a commercial CA for client connection which could be trusted by devices automatically.

You can check this article for more information about these different types of digital certificates:

Digital certificates overview

If your organization requires to use Exchange self-signed certificate for client connection, you may need to export this certificate from Exchange server, import and add it to the trusted root certificate store on Samsung device manually. Please notice that not all mobile devices allow changes to the trusted root certificate store, you may contact the Samsung support side to confirm if it’s supported or how to add self-signed certificate to the trusted root certificate store.

For how to export Exchange certificate, please check these steps: Export a certificate from an Exchange server | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
