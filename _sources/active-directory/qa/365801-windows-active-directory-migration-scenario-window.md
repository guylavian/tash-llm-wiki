---
title: "windows active directory migration  Scenario: Windows active directory forest having multiple subdomain and tree. Forest Doman name is “company.com” and the sub domain name is NA.Company.com, AP.company.com and so on. The tree domain name is “tree.com”"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/365801/windows-active-directory-migration-scenario-window
question_id: 365801
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# windows active directory migration  Scenario: Windows active directory forest having multiple subdomain and tree. Forest Doman name is “company.com” and the sub domain name is NA.Company.com, AP.company.com and so on. The tree domain name is “tree.com”

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/365801/windows-active-directory-migration-scenario-window (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Scenario: Windows active directory forest having multiple subdomain and tree. Forest Doman name is “company.com” and the sub domain name is NA.Company.com, AP.company.com and so on.  

The tree domain name is “tree.com”  

Requirement: migrating one tree domain named “tree.com” to different forest with the same domain “tree.com”.   

Question: is it possible keep domain name and NetBIOS domain same,   

Is trust relationship can be created between domains.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-28*

Hi,  

I hope things are going well on your end. Since I have not heard from you, I assume you are quite busy and may not be able to make progress on this issue at this time.   

Based on this status of this case, I will go ahead to temporarily mark it as inactive at this time.  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-26*

Hi,  

How are things going? Could you please send me an update so that we can continue to work on this problem and resolve it ? Thanks for your help.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-22*

Hi Venkatta,    

Thank you for posting in our forum    

>>>Is it possible keep domain name and NetBIOS domain same,Is trust relationship can be created between domains.    

You cannot delegate the creation of trusts to any user who is not a member of the Domain Admins or Enterprise Admins groups. Even though you can grant a user the Create TDO (Trusted Domain Object) right or the Delete TDO right in the System container of a domain, the user will not be granted the right to create a trust.    

When you are logged on locally to a domain controller and you try to create a new trust by using Active Directory Domains and Trusts, the operation may be unsuccessful and you may receive the message “Access denied.” This issue occurs only if you are logged on locally to the domain controller as an ordinary user (meaning that the user is not logged on as Administrator or as a member of any administrative groups for the domain). By default, ordinary users are blocked from logging on locally to a domain controller unless Group Policy is modified to permit this.    

Give you an article, the content of the article is more detailed, you can refer to the link below：    

reference： https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc779046(v=ws.10)?redirectedfrom=MSDN    

Hope this information can help you    

Best wishes    

Vicky
