---
title: "Windows LAPS didn't match password complexity and Password is now showing on the LAPS UI."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199136/windows-laps-didnt-match-password-complexity-and-p
question_id: 2199136
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Windows LAPS didn't match password complexity and Password is now showing on the LAPS UI.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199136/windows-laps-didnt-match-password-complexity-and-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone.

I've got a problem with my LAPS.

So, I implement LAPS one month ago, and it all works fine.

But then, I have an issue where some specific computers have no password shown when you check on LAPS UI.

I also have this problem where a password didn't meet the complexity. I set the password length to 12, but when I check on CMD using "net accounts,"  the password length is still 8.

I have make sure that there is no GPO/software interfering with LAPS.

Some computers are working fine, and some are experiencing those kinds of issues.

Can someone help me?

Thanks,

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-16*

Hello 

Good day!  

You can try to change the LAPS settings and reset the LAPS settings within the existing domain GPO.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-15*

Hi, Daisy.

I've tested :

Get-LapsADPassword -Identity MachineName -AsPlainText

And still it's doesn't match the length and complexity.

But recently, I tried to reset the Group Policy settings following this article :

https://woshub.com/reset-local-group-policies-settings-in-windows/

The LAPS are working normal (same complexity and length).

But is there any way to reset all the GPO Settings on All users? because if we reset manually one by one, It will takes a lot of time, since we have lots of endpoint.

And also if you know anything about reseting Group Policy Settings please tell me. since I don't know what impact will happen if I reset the Group Policy Settings.

Hope you understand what I'm saying, sorry for my bad English.

Thanks, 

Regards,

DaveyIC

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-08*

Hello  

Good day!  

There is a computers that applied LAPS but the password didn't match the length and complexity I set.

A: What is the password length in gpressult / h file?  

You can try to manually set the password of this machine to expire, and then regenerate a new password.

We also have a lot of new computers that after being implemented LAPS, the password is not showing on LAPS UI,

A: Please check if you can see the LAPS via Command below.

Get-LapsADPassword -Identity MachineName -AsPlainText  

Note: MachineName is your machine name.

Get started with Windows LAPS and Windows Server Active Directory | Microsoft Learn  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-07*

Hi Daisy,

Yes, they all are on the same OU, I already check the other GPO settings, and found out that there is no other Policy settings related to password.

Here is the detail about what happened.

-  There is a computers that works fine with LAPS

-  There is a computers that applied LAPS but the password didn't match the length and complexity I set.

We also have a lot of new computers that after being implemented LAPS, the password is not showing on LAPS UI,

But if we check on gpresult /r the LAPS GPO is applied.

FYI : They all on the same OU

Thanks,

Regards,

DaveyIC

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-07*

Hello DaveyIC,  

Thank you for posting in Microsoft Community forum.

Windows LAPS policy is configured via GPO setting, you can try to check the GPO setting with LAPS policy about this machine.  

For checking Computer Configuration within gpresult, we can follow steps below.

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check LAPS gpo setting (check password length and other settings) under "Computer Details". 

 Based on "I have an issue where some specific computers have no password shown when you check on LAPS UI", are working machine and nonworking machine in the same OU？

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
