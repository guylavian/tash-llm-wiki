---
title: "Printer GPO Not Applying policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1015577/printer-gpo-not-applying-policy
question_id: 1015577
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Printer GPO Not Applying policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1015577/printer-gpo-not-applying-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have created a GPO to install 2 printers to a security group.  It is not applying when I have the user in a nested OU. AD structure looks the below.  The issue when put the Sec group in the nested OU under Company Name, the policy does not apply. When I put the group in the Security Groups at the domain level it applies.  We mainly use the nested level for Security Groups, and only use the Security Groups at the domain level for the default groups (admins, domain admins, etc). Policy does apply if we use a specific user from the Users OU.    

Domain    

-Builtin    

-Computers    

-Company Name    

--Users    

--Computers    

-- Security Groups    

--Admin    

--Marketing    

-Domain Controllers    

-Security Group    

-System

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-23*

Hi,    

First you need to confirm what the link object of the GPO application you created is, and whether the corresponding object exists in the ADUC.    

Next, you need to check the security filtering under the Scope option, as well as the delegation settings.    

For nested OUs, you can see if the Block inheritance setting is turned on.    

Best Regards,    

Wesley Li
