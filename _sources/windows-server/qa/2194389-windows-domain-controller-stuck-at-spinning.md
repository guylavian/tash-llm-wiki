---
title: "Windows Domain Controller stuck at spinning"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194389/windows-domain-controller-stuck-at-spinning
question_id: 2194389
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-performance-system-performance"]
---
# Windows Domain Controller stuck at spinning

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194389/windows-domain-controller-stuck-at-spinning (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 3 - 2019 Windows DC's that are stuck at the spinning logo after a reboot and I cannot log in.  Any suggestions?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-20*

I'm so glad that I could provide some help here, it will be great to mark any useful answer so other can easily find it.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-08*

We fixed it by editing the domain controllers GPO to "Bypass Traverse Checking".

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-06*

If so, you can only try to repair the domain controller.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-01*

We had to edit the domain controllers GPO to "Bypass Traverse Checking".

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-01*

Hello

Thank you for posting in Microsoft Community forum.

Here are a few potential solutions: 

Safe Mode: When time permits, you might try booting, then press F8 at startup and try Safe Mode or Safe Mode with Networking to see if you can get further. 

System File Checker (SFC) and DISM: These are built-in Windows tools that can repair system files. You can run these commands from the Command Prompt in Safe Mode: 

-  sfc /scannow

-  DISM /Online /Cleanup-Image /RestoreHealth

-  Dism /Image:C: /Cleanup-Image /revertpendingactions

Check Group Policy Settings: If you recently modified a Group Policy setting, such as “Bypass Traverse Checking”, it could be causing the issue. You might want to revert any recent changes to see if that resolves the problem.

Best Regards,

Wesley Li
