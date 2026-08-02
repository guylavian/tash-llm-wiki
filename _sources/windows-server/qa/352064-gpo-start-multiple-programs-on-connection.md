---
title: "GPO:Start multiple programs on connection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/352064/gpo-start-multiple-programs-on-connection
question_id: 352064
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO:Start multiple programs on connection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/352064/gpo-start-multiple-programs-on-connection (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys,  

I have a RDP setup with RDCB and RDSH servers. Now I have enabled a GPO for restricting users Desktop and Start menu by using following policy.  

User Configuration >> Administrative Templates >> Windows Components >> Remote Desktop Services >> Remote Desktop Session Host >> Remote Session Environment >>  Start a program on connection policy  

Everything is working as expected now the problem is I need a provide users to open Windows Explorer. Now is there any way to run explorer or any shortcut to open Downloads folder for users.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-12*

Hello @Ajith Borra      

You may configure a gpo for required users and set the policy : Run these programs at user logon    

    

Best Regards    

Karlie    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
