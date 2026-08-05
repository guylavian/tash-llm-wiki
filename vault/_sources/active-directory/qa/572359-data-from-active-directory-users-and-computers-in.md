---
title: "data from active directory users and computers in not available from domain contoller because the specified directory service attribute or value does not exist"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/572359/data-from-active-directory-users-and-computers-in
question_id: 572359
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# data from active directory users and computers in not available from domain contoller because the specified directory service attribute or value does not exist

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/572359/data-from-active-directory-users-and-computers-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi  

I was making some changes to my domain today and mistakenly i deny read permission of authenticated users in my domain in active directory users and computers console and now i cant open this console and i have this error :  

data from active directory users and computers in not available from domain contoller because the specified directory service attribute or value does not exist  

how can i change this permission from another way like command or powershell?

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2021-09-30*

Hi @Saeed Abdollahi  ,    

Just did some testing on my test domain, dsacls doesn't provide the ability to remove a specific ace that has been set. You will need to use ldp to remove the deny permission.    

If you open ldp connect and bind to your ad    

Select tree from the view menu and select you default NC    

In the tree pane right click on the root of your domain and select advanced, security descriptor    

In the dialog check all nt authority/authenticated users entries to find the deny permission    

When you find the offending deny permission, delete it and then update    

This worked in my test domain.    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-30*

Hi @Saeed Abdollahi  ,    

At what OU level in AD did you set the deny permissions, was it at the root of the domain or a lower level?    

Have look at the dsacls command to see if you can list the permissions, details here https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771151(v=ws.11)    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-30*

Hello @Saeed Abdollahi  

You can use CMD as Domain Administrator:

icacls C:\Temp\ACL /T /C /grant DOMAIN\<GroupName>:F

```
a sequence of simple rights:  
        N - no access  
        F - full access  
        M - modify access  
        RX - read and execute access  
        R - read-only access  
        W - write-only access  
        D - delete access
```

Hope this helps with your query,

--If the reply is helpful, please Upvote and Accept as answer--
