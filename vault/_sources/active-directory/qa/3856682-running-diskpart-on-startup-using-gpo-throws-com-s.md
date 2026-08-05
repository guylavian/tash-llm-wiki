---
title: "Running diskpart on startup using GPO throws COM service error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3856682/running-diskpart-on-startup-using-gpo-throws-com-s
question_id: 3856682
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
answer_author_roles: ["Volunteer Moderator"]
---
# Running diskpart on startup using GPO throws COM service error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3856682/running-diskpart-on-startup-using-gpo-throws-com-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,

I'm trying to create a Windows Server 2025 template for use in cloud. I have added an startup script called extendvol.bat to "Startup" GPO which runs diskpart tool to extend the system volume to the maximum amount of space available on the disk when computer is starting up. However, the script doesn't work. 

I have accomplished this goal on Windows Server 2019 and 2022 just the same way and it works fine on those versions of Windows Server. However, when I do this for Windows Server 2025, it doesn't work. 

I have added the script to the following path in GP - Computer Configuration -> Windows Settings -> Scripts -> Startup Scripts.

I have tested the script by running it as "Local System" user using psexec" tool and it works fine. However, when it gets executed upon computer startup, the diskpart tool throws the following error message which is logged into a file:

"DiskPart encountered an error starting the COM services."

I have also tried making the virtual disk service to start automatically but didn't help.

As the same script works on previous versions of Windows Server, there should be a change in 2025 that prevents diskpart to run successfully before computer is fully started.

Any direction to fix the issue will be highly appreciate.

Thanks in advance.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2025-04-26*

Hi,

The Microsoft Answers community is a forum for home users. Given the scope of your question, the Q&A forum might be the best place to discuss this issue.

https://learn.microsoft.com/en-us/answers/questions/

Microsoft Q&A has IT Pros and system administrators who can best assist with this question.

You may also try this question on StackOverflow.

https://stackoverflow.com/
