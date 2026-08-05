---
title: "Windows Server 2022 Domain Controller failing to install Windows Updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188020/windows-server-2022-domain-controller-failing-to-i
question_id: 2188020
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 6
qa_tags: ["windows-business-windows-server-devices-deployment-install-windows-updates-features-roles"]
---
# Windows Server 2022 Domain Controller failing to install Windows Updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188020/windows-server-2022-domain-controller-failing-to-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi:

I have a Windows Server 2022 Domain Controller that is failing to install Windows Updates.  The latest update I've tried is KB5037422, which I downloaded from the Updates Catalog, file: windows10.0-kb5037422-x64_22f9c64db01978f109c6336a4ece8d381f07f75d.msu.  

Event Viewer records error: Installation Failure: Windows failed to install the following update with error 0x8024200B: Update for Windows (KB5037422).

For troubleshooting, I've already tried:

-  Ran troubleshooter for Win. Update (fixed issue, see screenshot) 

-  Ran sfc /scannow (no issues) 

-  Ran DISM /Online /Cleanup-Image /RestoreHealth (ran successfully) 

-  Deleted contents of C:/Windows/SoftwareDistribution folder

Any ideas how to get the latest Cumulative Update installed?

Thanks,

Bob H.

## Answer (community) — community member

*upvotes: 1 · updated: 2024-04-28*

A repair installation fixed the issue.  Ran setup.exe from the Windows Server 2022 ISO and selected to keep files.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-13*

Tried resetting WU components but didn't solve the issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-08*

Hello Bob_701,

have you installed the latest servicing stack update (ADV990001 - Security Update Guide - Microsoft - Latest Servicing Stack Updates) before install the KB5037422?

Hope it helps.

Best regards,

Lei

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-08*

Hi

Please try the URL below.

HOW to reset windows update components in windows - Microsoft Community
