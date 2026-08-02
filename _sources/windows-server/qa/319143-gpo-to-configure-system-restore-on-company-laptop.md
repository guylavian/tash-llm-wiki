---
title: "GPO to configure System Restore on company laptop"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/319143/gpo-to-configure-system-restore-on-company-laptop
question_id: 319143
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO to configure System Restore on company laptop

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/319143/gpo-to-configure-system-restore-on-company-laptop (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

I would create a Group Policy to manage System Restore on all company laptops.    

Domain Controllers are Win 2016 DataCenter and laptop are Windows 10 Professional.    

I found this guide:    

https://www.tenforums.com/tutorials/99782-enable-disable-system-restore-windows.html    

I have a doubt:    

Is there a way to set "Disk Space Usage"?    

    

Best regards    

Federico Coppola

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-21*

Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SystemRestore\cfg

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-21*

Thanks for your suggestions.  

Best regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-19*

Dear @Anonymous       

I would set for example that all clients must have 10GB of storage (Laptop SSD) for System Restore Point.    

Is it possibile?    

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-18*

Hi,    

Welcome to share here!    

If you mean to limit the Disk Quotas, you can refer to the following way:    

Go to Computer Configuration\Administrative Templates\System\Disk Quotas. Using the following policies to configure the Max usage :    

    

If i misunderstand you ,please feel free to let me know.
