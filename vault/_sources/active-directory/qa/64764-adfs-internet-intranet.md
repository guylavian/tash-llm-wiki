---
title: "Adfs internet / intranet"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/64764/adfs-internet-intranet
question_id: 64764
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Adfs internet / intranet

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/64764/adfs-internet-intranet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi we are using adfs with WAP. Internal and external Users are always connecting via WAP Top the adfs, so we can’t use Intranet ( that means a web application proxy is not present in front of AD FS) and "Extranet" in the Access rules to divide between incoming Users. Intranet/Extranet does not refer to internal or external subnets in adfs Access rules from my understanding.  

What we want to achieve is that Users with a specific external IP dont need to do MFA,  but for the rest of the Users with various ips it is needed.  

Tried a lot of different configuraion today with specific Networks in Access rules. Mayen it is Not possible bedaure the Src ip is always the wap on adfs ?

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

You shouldn't be exposing ADFS directly to the internet but you can do some of this you want to require MFA by location in Azure AD. We have workshops to help move off ADFS https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480 & https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
