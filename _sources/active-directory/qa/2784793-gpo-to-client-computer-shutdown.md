---
title: "GPO to client computer shutdown"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2784793/gpo-to-client-computer-shutdown
question_id: 2784793
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 5
qa_tags: []
---
# GPO to client computer shutdown

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2784793/gpo-to-client-computer-shutdown (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have windows 2016 server and client pcs are windows 10. I want to shutdown client pc when it idle for 1 hour. I have applied below gpo settings but it can't work. Some one help to resolved it.

Computer Configuration >> Preferences >> Control Panel Setting >> Schedule Task

Task Tab 

Name : Shutdown  

Run: %SystemRoot%\System32\shutdown.exe  

Arguments : -f -s  

Start in : C:\Windows\System32

Schedule Tab   

Daily 6:00 am

Setting Tab

Tick mark on only start the task if the computer has been idle for at least 60 minutes  

Common Tab  

Item-level targeting >> OU=***,DC=***,DC=local  

Computer in OU

## Answer (community) — community member

*upvotes: 1 · updated: 2018-03-08*

Hi,

Your Windows 10 question is more complex than what is typically answered in the Microsoft Answers forums. It is better suited for the IT Pro audience on TechNet. To get an accurate resolution, please post your question in the
TechNet Group Policy forum.

Let us know if you have other concerns.
