---
title: "Active Directory Administrative Center issues with Defender"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2125061/active-directory-administrative-center-issues-with
question_id: 2125061
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Administrative Center issues with Defender

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2125061/active-directory-administrative-center-issues-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

We've recently switched to Defender for Endpoint on our Domain Controllers and everythings been fine, but we noticed, it now takes very long to open Active Directory Administrative Center, and when ever we do, antimalware service executable spikes to 60% cpu usage. It does this on 3 separate servers. Funnily enough, while Active directory admin center is loading for what seems like 20 mins, its process has 0% cpu usage

I tried all of the bellow actions, one after the other, testing after each:

-Added to path exclusions:   

Active Directory Administrative Center executable "dsac.exe"   

As well as a few related files:   

dsac.exe.config   

dsacls.exe   

dsacn.dll

-Added to process exclusions:   

dsac.exe   

dsacls.exe

-Excluded all of the above files from attack surface reduction rules  

 -Turned off attack surface reduction   

-Turned off real-time protection   

-Turned off behavior monitoring   

-Turned off monitor file and program activity   

-Turned off process scanning

I've run out of things to turn off! All of the above is currently still turned off and excluded and the issue persists? Nothing else is causing antimalware service executable to behave like this. Any thoughts?

Thanks guys,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-03*

Hello,

 

Thank you for posting in Q&A forum.

To further troubleshoot this issue, please kindly try below steps:

-  Check Microsoft Protection logs under path: C:\ProgramData\Microsoft\Windows Defender\Support and search for any information related.

2.Use Windows Performance Recorder to capture performance logs and identify the issue.

3.Open Task Manager > Details > right-click on MsMpEng.exe > select Set affinity > set a maximum CPU usage limit for the antimalware service executable.

 

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.
