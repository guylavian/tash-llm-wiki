---
title: "msExchHideFromAddresslist with Azure AD Connect - Schema update or not?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2280769/msexchhidefromaddresslist-with-azure-ad-connect-sc
question_id: 2280769
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# msExchHideFromAddresslist with Azure AD Connect - Schema update or not?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2280769/msexchhidefromaddresslist-with-azure-ad-connect-sc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have on premise Active Directory, never had on premise Exchange so we are missing the msExchHideFromAddresslist attribute on the user object.  Azure AD Connect is up and running.  We are not able to change the Hide From Address List option in Microsoft 365 Admin Center or Exchange Admin Center.

I have read that extending the on premise AD Schema is an option to solve this issue, if needed in combination with adjustement of the Azure AD Connect Synchronisation Rules.  But is this really needed?    

When using the Synchronisation rules editor I can see that the msExchHideFromAddresslist attribute is listed only in four Out to AAD Synchronisation Rules.  These are outbound.  The msExchHideFromAddresslist is not listed in any inbound rules.  Is it an option to uncheck the msExchHideFromAddresslist attributed in these rules?  What is the effect of this?  Will it make the Hide From Address list option in Microsoft 365 Admin Center or Exchange Admin Center editable again?

Kind Regards

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-06-03*

Well its not supported to not have a onprem Exchange Server when syncing unless you have met all the requriements:

https://learn.microsoft.com/en-us/exchange/decommission-on-premises-exchange

Otherwise, you would prob have to extend the Schema on-prem for Exchange and  create a custom rule in Connect:

https://learn.microsoft.com/en-us/answers/questions/2236487/msexchhidefromaddresslist-attribute-missing

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-06-03*

You would need to enable the Exchange Hybrid option in Entra Connect:

https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/reference-connect-sync-attributes-synchronized#exchange-online
