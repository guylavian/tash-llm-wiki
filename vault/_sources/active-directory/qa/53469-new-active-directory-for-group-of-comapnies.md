---
title: "New active directory for group of comapnies"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/53469/new-active-directory-for-group-of-comapnies
question_id: 53469
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# New active directory for group of comapnies

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/53469/new-active-directory-for-group-of-comapnies (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The situation - one group of small comapnies.  

The main DC will be located at the cloud.  

each company will have 1 dc or 2  in office replicated from cloud.  

what is the best way to implement the new active directory ?  

each company with separate domain? one domain with OU's?  

I want each company to have admin domain separated and a master admin ...  

and to allow specific users from one company to access other resources in other company.  

Which way is more secure/reliable ?  

I want to create admin for each company so the admin will be able to install softwares/ change premmisions only for specific company and still have super admin - which   

option is more easy to manage?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-07-29*

Hello,    

Thank you for posting here.    

Based on the description, we can set up root domain with DCs and child domains with DCs.     

Root domain is the headquarters. Each sub company is in a child domain so that each company has admin domain separated.    

For more information, we can refer to the links below.     

Child domain Benefits in large environment    

https://social.technet.microsoft.com/Forums/en-US/0d8321ed-c0b7-4f60-902e-8fdfa76f95ae/child-domain-benefits-in-large-environment?forum=winserverDS    

Install a New Windows Server 2012 Active Directory Child or Tree Domain (Level 200)    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-a-new-windows-server-2012-active-directory-child-or-tree-domain--level-200-?redirectedfrom=MSDN    

How Domains and Forests Work    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc783351(v=ws.10)?redirectedfrom=MSDN    

Best Regards,    

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-28*

You should most likely ask your question in the Active Directory forum located at https://learn.microsoft.com/en-us/answers/topics/windows-active-directory.html  That is where the Active Directory experts are.    

They are better equipped to discuss pros and cons of the different configurations you are asking about.
