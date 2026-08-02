---
title: "Azure ad connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1708012/azure-ad-connect
question_id: 1708012
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Azure ad connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1708012/azure-ad-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am thinking about enabling Azure Ad Connect.

Will Azure Ad Connect affect accounts that only exist on 365? 

What about accounts that already exist on 365 but have the same name on local ad? Will they merge?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-21*

Hi Administrator,

Thank you for posting in the Q&A Forums.

Does Azure AD Connect affect accounts that exist only on 365?

No. The primary purpose of Azure AD Connect is to synchronize users, groups, and objects from your local Active Directory (AD) to Azure Active Directory (Azure AD), which in turn integrates with services such as Office 365. It does not affect or change accounts created only in Azure AD or Office 365.

What about accounts that already exist on 365 but have the same name on the local AD? Will they merge?

No, they will not be merged.Azure AD Connect matches users in Local AD and Azure AD/Office 365 based on specific attributes (e.g., UserPrincipalName, Emailaddress, etc.) during the synchronization process. However, if matching is done based on names only (such as username or display name), name conflicts may occur.

In this case, Azure AD Connect handles it based on the configured synchronization rules. By default, it may mark one of the users as a Source Anchor Conflict or Hard Match Failed and retain the user in Azure AD/Office 365. AD/Office 365.

Best regards

NeuviJ

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2024-06-19*

Hello Administrator,

Thanks for your question.

Entra connect (new name for ad connect) installation has a few considerations. I'd first address your questions. If you have users in office 365 only and not in-premises Connect will not affect those users. However if there's a sync between on-prem and your cloud and it detects a match in UPN/Proxy it'll try to match the two users. Meaning if they're the same name/UPN it will try to match.

Pls note that Before you install Entra Connect, you have to go through all the list of prerequisites here: https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-prerequisites to determine if you even have the right setup available for an Entra connect install.

Regards,

Abiola

You can mark it 'Accept Answer' and upvote if this helped.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-19*

You will need to know somethings prio to do this connection.

What type of license you are about to use? Premium licenses have ability to "write back" and most comuns license no. It means, if you are using cheaper lic, you only will sync from on-prem to cloud. If premium lics you can sync on both directions.

Some reading about merging accounts - https://www.reddit.com/r/microsoft365/comments/scp0bl/merge_onpremise_ad_account_with_m365_account_and/
