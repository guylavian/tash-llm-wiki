---
title: "Hybrid exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1010018/hybrid-exchange-server
question_id: 1010018
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Hybrid exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1010018/hybrid-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Please clear my concept.    

If companies have On-premise exchange server then on which cases companies need to do hybrid deployment. What is the benefits of hybrid deployment rather than cutover migration?    

In hybrid deployment one user has mailbox on both sides (onpremise and exchange online). What is the benefits of this kind of scenario. thanks      

Regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-16*

Hi @HASSAN BIN NASIR DAR       

The reason you might be in a hybrid situation is you have on-premises solutions that require having a local Active Directory. (an example may be is that you have applications that require LDAP or a File Share where you still use local AD accounts).    

Then you would use Azure AD Connect to ensure that local Exchange accounts (AD Accounts) are also migrated to Microsoft 365 Azure AD.    

If you don't have local on-premises applications that require a local AD then it would be safe to say to just cutover completely to Microsoft 365 (Azure AD and Exchange Online).    

------------------------------------------------------    

If this is helpful please accept answer.
