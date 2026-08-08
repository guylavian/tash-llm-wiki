---
title: "Windows Server 2008 Domain Controller won't start in Normal mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2795982/windows-server-2008-domain-controller-wont-start-i
question_id: 2795982
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Windows Server 2008 Domain Controller won't start in Normal mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2795982/windows-server-2008-domain-controller-wont-start-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I've been using these forums to get as far as I can, but I'm getting stuck now with not much light at the end of the tunnel, if anyone can offer some guidance or help?

Basically I have a domain controller (singular), on doing a long overdue AVG update and scan (the system isn't connected to the internet), the AVG software requested a reboot following the cleaning of some virus instances found, and then the station would
 not start up in normal mode again :(

The station starts up looking good and well, and gets to starting the Windows loading (with the scrolling bar), here it takes a while and then after a while the screen goes blank, the mouse curser will appear, then the station restarts. I can get into safe
 mode via F8, or else following a failed restart I get into the windows repair mode.

I've tried a few things now, to no real progress:

~ System Recovery from system back-up image (image was dated previous to the AVG scan).

~ Clean Boot: The server wouldn't get past the same stage as detailed above.

~ SFC /scannow, said was a success but no change.

~ chkdsk, all said was a success but no change.

~ Bootloader repair via bootrec.exe /fixmbr, etc. All said was a success but no change.

~ Boot logging, that didn't seem to reveal anything obvious.

~ Booting into DRSM and checking event logs, please see below for detail.

I have more information but haven't yet been able to get any further with the following:

-  On disabling the automatic restart I get the following blue screen error:

"STOP: c00002e2 Directory Services could not start because of the following error! The specified procedure could not be found. Error status: 0xc000007a. Please shutdown this system and reboot with DSRM, check the event log for more detailed information."
 . 

I followed the instructions and so far from the event logs it appears to be:

"ID7026 Boot-start or system-start driver(s) failed to load: spldr"

"ID1001 Software Protection Service failed to start. 0x80070002"

"ID1000 Faulty App: MILI2Service.exe Version 4.2.313.0, exception code 0xc000000d, fault id 0xa44"

But so far I haven't managed to find or read-up on this information.

-  At one point I did get the following from sfc /scannow: "there is a system repair pending which requires reboot to complete, restart windows and run SFC again". Although I haven't seen this again I am still intrigued by it.

Is any of the above recognisable as a known issue, or sound familiar at all? I'd really appreciate a more experienced opinion on the issue and possible ways to resolve it. I have lots more information if needed :)

Thank you,

Kev

## Answer (community) — community member

*upvotes: 0 · updated: 2017-12-01*

Hi,

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
