---
title: "Idle time out GPO for Remote Desktop Services sessions not working in Windows 2019 servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/859904/idle-time-out-gpo-for-remote-desktop-services-sess
question_id: 859904
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Idle time out GPO for Remote Desktop Services sessions not working in Windows 2019 servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/859904/idle-time-out-gpo-for-remote-desktop-services-sess (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have configured GPO to Set time limit for active but idle Remote Desktop Services sessions. Policy has been set to disconnect sessions which are idle for more than 3 hours. But I am getting warning after 30 minutes itself. This GPO has been applied at OU level. Issue occurs only with Windows 2019 servers. Session time limits on Windows 2016 servers which are in the same OU works well. I ran gpresult /h on the affected servers. I could see session time limit policy is applied properly still sessions are getting disconnected after 30 minutes.   

Anyone came across this issue? Please assist me

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-06-02*

Hello @Pandi       

Does console or registry have a different setting?  see reference: Configuring RDP/RDS Sessions Limits (Timeouts) on Windows     

Both server 2019 and 2016 have exactly same group policy on remote desktop service?    

    

Best Regards    

Karlie    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.
