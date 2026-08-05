---
title: "Question: windows active directory migration, Scenario: Windows active directory forest having multiple subdomain and tree. Forest Doman name is “company.com”"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/366123/question-windows-active-directory-migration-scenar
question_id: 366123
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Question: windows active directory migration, Scenario: Windows active directory forest having multiple subdomain and tree. Forest Doman name is “company.com”

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/366123/question-windows-active-directory-migration-scenar (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Scenario: Windows active directory forest having multiple subdomain and tree. Forest Doman name is “company.com” and the sub domain name is NA.Company.com, AP.company.com and so on.  

The tree domain name is “tree.com”  

Requirement: migrating one tree domain named “tree.com” to different forest with the same domain “tree.com”.   

Question: is it possible keep domain name and NetBIOS domain same,   

Is trust relationship can be created between domains.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-27*

HI,    

Current scenario:    

source domain and target domain having domain controllers from windows  version 2008/2012/2016/2019. (my source domain having dcs from all versions of windows and target also the same) is this scenario supported for admt migration of users and computers.    

i have referred the below MS articles.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/support-for-admt-and-pes

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-26*

HI,   

Thanks for your prompt response. I have shared the scenario and constraint associated with it to my team/customer. suggested for intermediate temp domain (third domain). checking for thirds party tool which can help in this type of scenario.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-22*

Thanks for the replay this means it is not possible to migrate domain from one forest to another forest with the same domain name and NetBIOS name.  

Here the requirement is  customer want to restructure the active directory forest due to merger, Keeping the same domain name while consolidating the forest. in case how we achieve the the objective by migrating to temp domain and again migrating to target domain having the same dns name and NetBIOS name, or is there any 3rd party tool is available. Please suggest.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-22*

Hi,    

When you use Active Directory Domains and Trusts to create a trust, you may receive the message “Operation failed. Parameter incorrect.” This issue may occur if you try to establish a trust relationship when the source domain and the target domain have one or more of the following identifiers that are the same:    

Security identifier (SID)    

Domain Name System (DNS) name    

Network basic input/output system (NetBIOS) name    

To resolve this issue, rename all conflicting identifiers before you try to create the trust    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779046(v=ws.10)?redirectedfrom=MSDN    

How Domain Rename Works    

Best Regards,
