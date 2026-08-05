---
title: "Running diskpart on startup using GPO startup script throws COM service error on Windows Server 2025"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2261413/running-diskpart-on-startup-using-gpo-startup-scri
question_id: 2261413
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Running diskpart on startup using GPO startup script throws COM service error on Windows Server 2025

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2261413/running-diskpart-on-startup-using-gpo-startup-scri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Experts,

I'm trying to create a Windows Server 2025 template for use in cloud. I have added an startup script called extendvol.bat to "Startup" GPO which runs diskpart tool to extend the system volume to the maximum amount of space available on the disk when computer is starting up. However, the script doesn't work.

I have accomplished this goal on Windows Server 2019 and 2022 just the same way and it works fine on those versions of Windows Server. However, when I do this for Windows Server 2025, it doesn't work.

I have added the script to the following path in GP - Computer Configuration -> Windows Settings -> Scripts -> Startup Scripts.

I have tested the script by running it as "Local System" user using psexec" tool and it works fine. However, when it gets executed upon computer startup, the diskpart tool throws the following error message which is logged into a file:

`DiskPart encountered an error starting the COM services.`

I have also tried making the virtual disk service to start automatically but didn't help.

As the same script works on previous versions of Windows Server, there should be a change in 2025 that prevents diskpart to run successfully before computer is fully started.

Any direction to fix the issue will be highly appreciate.

Thanks in advance.

## Answers

_No answers on this thread._
