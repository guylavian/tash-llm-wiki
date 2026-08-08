---
title: "GPO Network Location"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/94432/gpo-network-location
question_id: 94432
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO Network Location

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/94432/gpo-network-location (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

In a company there are many shares and we prefer to use "Network Location" and not "Disk Mapping".    

In ths company there is DFS solution too, so every time I need to configure manually link to finally user to "aim" DFS path (In my case is "\company.local\shares")    

Is there a way to create this link (Network Location in File Explorer) automatically using Group Policy?     

All client are Windows 10 OS.    

    

Thank so much!    

Federico

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-14*

Dear @Leon Laude  ,    

thanks for your reply.    

I prefer use Network Map due to I would avoid to use letter that specify a disk (network path).    

I have found solution from this discussion: https://social.technet.microsoft.com/Forums/windowsserver/en-US/452028b2-d22a-42c1-9a1b-04b8e1f75281/group-policy-preference-network-locations-how-to-add-network-locations?forum=winserverGP    

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-15*

Hi,  

I am glad to hear that your issue was successfully resolved.  

If there is anything else we can do for you, please feel free to post in the forum.  

Have a nice day!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-14*

Hi @Federico Coppola  ,    

You can use Group Policies to map network drives, the location can be a normal Windows share, DFS share or a drive, this is entirely up to you.     

You can follow along the guide below:    

How To Map Network Drives With Group Policy (Complete Guide)    

----------    

(If the reply was helpful please don't forget to upvote or accept as answer, thank you)    

Best regards,    

Leon
