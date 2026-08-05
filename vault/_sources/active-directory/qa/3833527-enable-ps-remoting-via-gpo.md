---
title: "Enable PS-Remoting via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3833527/enable-ps-remoting-via-gpo
question_id: 3833527
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Enable PS-Remoting via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3833527/enable-ps-remoting-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,

I have a bit of an issue.  I need to be able to Enter-PSSession across my domain, but it does not work until on the client computer I run Enable-PSRemoting from the end point.  I have GPO configured and have read 'guides' that all say to setup GPO the same so I have my GPO configured 'correctly', assuming these references are correct.

Here is what I have been referencing:

about_remote_Troubleshooting - MSC

Enter-PSSession - MSC

Enable-PSRemoting - MSC

PS Remoting FAQ - MSC

Server Academy

WOS Hub

Automation Admin

Enabling PSRemoting with a GPO | xkln.net

Here is my execution:

Test-NetConnection:

Test-WSMan:

On the client computer the GPO is applied, and I see it via GPRESULT /R.  I removed all other policies to ensure there is no interference.  The GPO is exactly like in these guides on how to allow it on the domain.  Firewall inbound, WinRM started and set to Automatic, I have IPV4 set to * for the WinRM service, I created a restricted access group and added it to Remote Management Users, and I even tried adding the Powershell command "Enable-PSRemoting -Force" to a startup script to see if that would make it work, and it doesn't.  

Not until I go to the end point, and run the command myself does it start to work.

From the end point:

Now from my computer:

Any assistance is very much appreciated!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-09*

Good Day 00Leavii,

I appreciate your time getting back to this thread, I am so glad to know that it is now fixed, thank you for sharing the resolution, it will help others in the community who are experiecing the same issue.

Have a wonderful day ahead and stay safe.

Sincerely,

Carlo T.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-09*

Thank you for the reply.  I believe I have this fixed now though.  Sorry for the incorrect placement.

For reference I needed to add the XML config to the registry key, which I got when I enabled psremoting, then copy pasted the given value to the GPO I created.

Here is the key:  HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WSMAN\Plugin\Microsoft.PowerShell

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-09*

Good Day 00Leavii,

My name is Carlo, I am also using Windows pc and community member like you.

This is a community forum for Home consumers for GPO related inquiries you can post it in this forum below where members are IT professionals.

https://social.technet.microsoft.com/Forums/en-...

Have a wonderful day ahead and stay safe.

Sincerely,

Carlo T.
