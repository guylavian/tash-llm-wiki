---
title: "How to set PowerShell eventlog max size in a GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/569717/how-to-set-powershell-eventlog-max-size-in-a-gpo
question_id: 569717
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-powershell"]
---
# How to set PowerShell eventlog max size in a GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/569717/how-to-set-powershell-eventlog-max-size-in-a-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there.  

I need to set the PowerShell event log in Windows max size in a GPO.  

I allready got the Eventlog Max size for: Application, Security, Setup, and System down in the: "Windows Components/Event Log Services" area  

My google foo has run out for this one.   

Please help me out wise people :-)  

Kind regards  

Thomas....

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-29*

Hi there,

Can you give this a try?

Open the registry editor and go to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\<log_name>.  

For example: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Directory Service  

Set the MaxSize to the required decimal value (in bytes).

If the reply is helpful, please Upvote and Accept it as an answer

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-28*

GPO does not have out of the box ADMX/ADML file for PowerShell Event logs. If you can build your own ADML/ADMX or find some template, that can solve your problem.
