---
title: "Unusual Behavior using GPO PowerShell Scripts During Restart/Shutdown in Hyper-V – Need Help"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2200000/unusual-behavior-using-gpo-powershell-scripts-duri
question_id: 2200000
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Unusual Behavior using GPO PowerShell Scripts During Restart/Shutdown in Hyper-V – Need Help

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2200000/unusual-behavior-using-gpo-powershell-scripts-duri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have noticed strange behavior in Hyper-V. Group Policy is configured to execute PowerShell scripts for logon, logout, startup, and shutdown. The typical sequence of script execution is: startup → logon → logout → shutdown.

However, an issue arises when a restart is initiated while logged in (i.e., after startup and logon scripts have already been executed). Upon clicking the restart button from the GUI, the following occurs: after the logout and shutdown scripts run as expected, the startup script is executed and the logon script is triggered. This happens despite the fact that the lock screen is displayed after the restart, and no user has logged in yet.

This phenomenon consistently occurs when restarting or shutting down from the GUI while logged in. It does not occur when restarting via the command line using `shutdown /r /t 0` or shutting down with `shutdown /s /t 0`.

Why does Hyper-V behave in this inexplicable manner, executing the logon script in such cases?

Is it possible to configure something within the virtual machine to address this issue? Or are there specific Group Policies for script execution that could control this behavior? Could there be certain Registry entries that influence the shutdown or restart process to prevent this issue in Hyper-V? Alternatively, could the problem be resolved by modifying the startup or logon scripts, for instance, by adding conditions to verify if an actual login has occurred? Any ideas or suggestions to explain or resolve this behavior would be greatly appreciated.

***Move from Windows / Windows 10 / Performance and system failures***

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-30*

Hi,

Please see if checking the result of `query user` at the beginning of the logon script works. A user that has actually logged in has an active session on the VM.
