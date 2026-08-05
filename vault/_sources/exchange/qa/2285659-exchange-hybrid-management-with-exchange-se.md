---
title: "Exchange hybrid management with Exchange SE?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2285659/exchange-hybrid-management-with-exchange-se
question_id: 2285659
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange hybrid management with Exchange SE?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2285659/exchange-hybrid-management-with-exchange-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All

I was wondering if anybody had anymore information regarding the following scenario now that Exchange SE is going to be available?

The scenario is: All mailboxes from a Exchange 2019 server have been migrated up to Office 365. The Exchange 2019 server is in place with the free hybrid licensing, and the only functionality being used is the hybrid management of the mailboxes that have been migrated. And also the email relay functionality within Exchange.

My question is if the CU is ran to upgrade the Exchange server to SE, will a subscription be required to get updates to the Exchange Server? Or will the hybrid licensing cover this as before? As no mailboxes will be present on the server, only relay and management.

Thanks for any assistance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-23*

Hi Both

Thanks for your help. So just to confirm even though the user mailboxes have been migrated (and have A3 licenses etc) will licenses (other than the free hybrid license) be required to able to receive updates to Exchange SE?

Thanks again for your help

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-19*

Hi Marc Edwards

Thank you for reaching out via the Microsoft Q&A forum and highlighting this topic. With the upcoming availability of Exchange Server Subscription Edition (SE), it's certainly a timely and relevant discussion. 

Although this subject falls slightly outside my usual area of expertise, I’ve taken the initiative to explore it through several trusted sources. From what I’ve gathered, it seems that the free hybrid license remains supported in Exchange SE, as long as the server is dedicated solely to hybrid management and email relay, and meets the specified requirements. 

I recommend reviewing this article Upgrading your organization from current versions to Exchange Server SE | Microsoft Community Hub. It clearly outlines that Exchange SE allows the use of the hybrid license. 

Please note that in order to receive future updates, including security patches and cumulative updates, a valid subscription or Software Assurance (SA) is required. 

To summarize: 

-  You may upgrade to Exchange SE via a cumulative update without purchasing an additional license, as long as the server is used solely for hybrid and relay purposes. 

-  However, to remain eligible for ongoing updates, a valid subscription will be necessary. 

We hope the details provided will assist you effectively.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-06-19*

Hi, see. IOW, you should be ok with just the hybrid license in your scenario

https://techcommunity.microsoft.com/blog/exchange/upgrading-your-organization-from-current-versions-to-exchange-server-se/4241305
