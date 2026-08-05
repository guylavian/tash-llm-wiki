---
title: "[Migrated from MSDN Exchange Dev]Exchange Admin Center Comes Up Blank Page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/197185/migrated-from-msdn-exchange-dev-exchange-admin-cen
question_id: 197185
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Exchange Admin Center Comes Up Blank Page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/197185/migrated-from-msdn-exchange-dev-exchange-admin-cen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.  

[MSDN Link]  

Exchange Admin Center Comes Up Blank Page  

[Original post]  

OS: Windows Server 2016  

Domain: Windows Server 2016  

Exchange Version: Exchange 2016  

Issue: Exchange Admin Tools do not open after install  

Troubleshooting: I have checked all the services they look good.  I have added my Server admins group to the Server Management Group In the Microsoft Exchange Security Groups.  I tried this tech note.  https://support.microsoft.com/en-us/help/2971270/blank-page-after-login-exchange-eac-owa-ecp. None of it worked.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-14*

Hi,    

Are you able to open Exchange Management Shell?Is there any error message?    

If you can open EMS successfully,please run the following commands to recreate the EAC and OWA virtual directories.    

```
Remove -EcpVirtualDirectory -Identity 'Server01\owa (Default Web Site)'  
New-EcpVirtualDirectory -InternalUrl 'https:///ecp' -WebSiteName 'Default Web Site'  
      
Remove -OwaVirtualDirectory -Identity 'Server01\owa (Default Web Site)'  
New-OwaVirtualDirectory -InternalUrl 'https:///owa' -WebSiteName 'Default Web Site'
```

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
