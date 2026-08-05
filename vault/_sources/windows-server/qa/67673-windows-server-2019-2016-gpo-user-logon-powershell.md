---
title: "Windows Server 2019/ 2016 GPO - User Logon Powershell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/67673/windows-server-2019-2016-gpo-user-logon-powershell
question_id: 67673
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows Server 2019/ 2016 GPO - User Logon Powershell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/67673/windows-server-2019-2016-gpo-user-logon-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey there,  

I attempt to config GPO to add a Registry data in Client desktop when user login to the Domain. my Server is windows server 2019 and 2016, my client is windows 10. normally it is simple thing, but I face the problem. I found out an article on the internet (http://woshub.com/running-powershell-startup-scripts-using-gpo/) and then follow it in my environment. Unfortunately, it turns out all settings are not applied to client's desktop when the user is belonged to Domain Users not in Domain Admins/ Administrators Group. I mean the user is belonged to Domain Admins/ Administrators Group, everything works well. my question is there is any solution on it could let me solve it out ASAP?  

My scenario is when you logon the domain, will be applied new GPO and PowerShell will put a data into client's registry.  

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2020-08-16*

Hi,    

Why not deploy directly a GPO that make the desired changes instead of using PS script ?    

    

Regards,    

Youssef Saad

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-17*

Hi,    

Based on my understanding , if the powershell script is the change the registry , the users need the permission . And in a Logon script, we can't modify the permission.    

You can considered to use a task schedule GPO to do this or consider the method YoussefSaad provided.    

For more details you can refer to the following link:    

https://learn.microsoft.com/en-us/answers/questions/66387/running-powershell-startup-logon-scripts-using-gpo.html    

Best Regards,
