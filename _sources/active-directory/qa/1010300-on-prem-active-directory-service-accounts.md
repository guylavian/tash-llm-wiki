---
title: "On-Prem Active directory service accounts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1010300/on-prem-active-directory-service-accounts
question_id: 1010300
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# On-Prem Active directory service accounts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1010300/on-prem-active-directory-service-accounts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Is there a way to identify an windows Active Directory service account and where it is been used and for which service?    

Regards,    

Saras.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-17*

Hi,    

From an AD object stand point there is no difference between a normal user and a service account.  Depending on your environment, usually the naming convention for the accounts is used to identify them, or a separate OU for service accounts.    

Using only the native AD tools the only way to identify where accounts have logged on from is the event logs on the domain controllers and you will need to enable auditing to see this information, see this page - https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events     

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-16*

Hi,    

Thank you for your question and reaching out.     

I understand that you wanted to identify a Windows Active Directory service account and where it is been used and for which service. However, Microsoft is strict when it comes to accounts and we cannot double-check that on our end. Instead, your option here is to check it on your end using the steps from this link: https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/service-accounts-on-premises    

-------------------------------------------------------------------------------------------    

If the reply was helpful, please don’t forget to Upvote or Accept as answer. Thank you!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-09-16*

Maybe this one helps.    

https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
