---
title: "Active Directory Seperation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/208658/active-directory-seperation
question_id: 208658
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Active Directory Seperation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/208658/active-directory-seperation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

I have a scenario where currently customer have contoso.com as their root domain and all the users and objects are part of that domain. And all the applications are ad authentication and single sign on configured.  

Requirements –  

Customer wants to segregate the AD domain created for each group companies and mange the users/objects and still use the centralized applications as it is.  

Host name of all the group companies assets should change to new domain.  

Login to domain should use respective group company domain.  

What all options available to achieve this and what will be the pros and cons.  

Regards,  

Anil Kumar

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-24*

We can help you troubleshoot why GPO is not applied or help configure GPO, but the premise is to know what settings you are using.  

AD provides users with hundreds of GPO settings, and can even customize GPO settings. But ADteam cannot understand the role of all GPOs.  

It is recommended that you consult your GPO administrator whether the settings related to this have been configured.  

The following link shares all the settings under Administrative Templates for your reference:  

https://admx.help/  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-23*

Hi  

You have many choice if you want segregate AD objects of each group companies:  

-  Keep the same forest and domain , you create A Organisation Unit for each companies to separate objects , set delegation for each OU . The member of domain admins have permission to manage all domain objects.This design is recommended in order to simplify the active directory infrastructure in case where have only one team to manage the active directory of all companies group. You don't need to migrate objects to another domain  

-  Create new forest with multiple child domains, each company will have its own child domain. It can be useful if each company has its own team to manage its domain,and you don't need to create manually trust between child domains, the trust between child and parent domain will be created automatically Only members of domain admin in root domain can have permission on all child domains, and you need to migrate objects to target domain.  

-  Create a forest for each company, create trust between all forests if need it, in this design each company can manage its own forest if it has its own team. You have to migrate object to target domain (using admt tools for exemple).  

Please don't forget to mark this reply as answer if it help you to fix your issue
