---
title: "Exchange Hybrid Address book"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2128419/exchange-hybrid-address-book
question_id: 2128419
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Hybrid Address book

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2128419/exchange-hybrid-address-book (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an hybrid exchange organization with a single forest exchange Org and Exchange Online.

On the on-prem AD we have hundreds of "contacts" objects that users with mailbox on the on-prem servers can see in their GAL and users on Exchange Online don't.

Do we need to sync also the contacts with entra ID to have the users with mailbox on Exchange online to see them on the GAL ? Is it the same for all the distribution groups defined on AD ?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-10*

Hello, @Stefano Colombo,

Welcome to the Microsoft Q&A platform!

Yes, to ensure that users with mailboxes on Exchange Online can see the contacts in their Global Address List (GAL), you need to sync those contact objects from your on-premises Active Directory (AD) to Entra ID. This synchronization will make the contacts available in the GAL for both on-premises and Exchange Online users. 

For more information, please click on https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/concept-azure-ad-connect-sync-user-and-contacts for reference.

The same applies to distribution groups. If you want users on Exchange Online to see and use the distribution groups defined in your on-premises Active Directory, you need to synchronize these groups with Microsoft Entra ID as well. This ensures that all users, regardless of where their mailbox is hosted, have access to the same GAL.

If the answer is helpful please click on ACCEPT ANSWER as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
