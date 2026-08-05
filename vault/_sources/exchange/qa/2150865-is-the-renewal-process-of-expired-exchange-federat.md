---
title: "Is the renewal process of expired exchange federation certificate exactly the same for both 2013 and 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2150865/is-the-renewal-process-of-expired-exchange-federat
question_id: 2150865
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Is the renewal process of expired exchange federation certificate exactly the same for both 2013 and 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2150865/is-the-renewal-process-of-expired-exchange-federat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is the recommended process for the renewal of Exchange 2013 Federation Certificate:  https://learn.microsoft.com/en-us/exchange/renew-the-federation-certificate-exchange-2013-help  I am looking to confirm if this can also, without adjustment, be applied to Exchange 2016, please.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-27*

Hello, @Alec Negus,

Welcome to the Microsoft Q&A platform!

The renewal process for the Exchange Federation Certificate is quite similar for both Exchange 2013 and Exchange 2016. The steps outlined in the guide you provided for Exchange 2013 can generally be applied to Exchange 2016 as well, just as it described in this document: Exchange 2016 - Hybrid - Exchange Delegation Federation certificate expired | Microsoft Community Hub.

However, there are a few minor differences to be aware of:

-  Exchange Management Shell: The commands and procedures in the Exchange Management Shell remain largely the same.

-  Exchange Admin Center (EAC): For Exchange 2016, some certificate management tasks have been removed from the EAC in later cumulative updates (CU23 and beyond). You may need to rely more on the Exchange Management Shell for these tasks.

If you need the specific documentation for Exchange 2016, please refer to Renew an Exchange Server certificate | Microsoft Learn.

Should you need more help on this, you can feel free to post back. 

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
