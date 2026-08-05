---
title: "Windows Update GPO settings not apply"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2615694/windows-update-gpo-settings-not-apply
question_id: 2615694
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Windows Update GPO settings not apply

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2615694/windows-update-gpo-settings-not-apply (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

I need your help for a problem with a Windows Update agent installed on a Windows Server 2008 R2 Datacenter. The problem is about changing the update source of the agent. I did this operation like...a thousand time before without encounter a problem like
 this.

So here is the detail :

-  I'm working with NAT, so I had the NAT from our WSUS to the hosts file to ease configuration. For example, imagine the name of wsus is updateserver.

-  Check in IE by typing "http://updateserver" : OK, great.

-  Next, gpedit.msc > Computer Configuration > Administrative Templates > Windows components > Windows Update  > Specify intranet Microsoft update service location. Enable and set both parameters with "http://updateserver".

-  Go to Windows Update > Check for updates > Error 8024402C. But, most important, I have "You receive updates : For Windows only."

 instead of "Managed by your system administrator".

-  Go to Windows Update log file to see what really happened when I check for updates :

2014-02-21    06:32:05:525     860    5bc    Misc    WARNING: Send failed with hr = 80072ee7.  

2014-02-21    06:32:05:525     860    5bc    Misc    WARNING: SendRequest failed with hr = 80072ee7. Proxy List used: <(null)> Bypass List used : <(null)> Auth Schemes used : <>  

2014-02-21    06:32:05:525     860    5bc    Misc    WARNING: WinHttp: SendRequestUsingProxy failed for <http://www.update.microsoft.com/v9/windowsupdate/redir/muv4wuredir.cab>. error 0x8024402c  

2014-02-21    06:32:05:525     860    5bc    Misc    WARNING: WinHttp: SendRequestToServerForFileInformation MakeRequest failed. error 0x8024402c  

2014-02-21    06:32:05:525     860    5bc    Misc    WARNING: WinHttp: SendRequestToServerForFileInformation failed with 0x8024402c  

2014-02-21    06:32:05:525     860    5bc    Misc    WARNING: WinHttp: ShouldFileBeDownloaded failed with 0x8024402c

It seems like the server is asking the wrong server...

I tried the "old way" by editing the registry, but it doesn't help.

I also used the "Fix it portable" to run the microsoft diagnostic tool for windows update and... It doesn't work either.

Issues found :

Windows Update error 0x80070005 - Not fixed (but fixed when you click view report details, so it's fixed but it's not... ok, my brain almost did a BSOD at this point)

Problems installing recent updates - Not fixed

Some security settings are missing or have been changed - Fixed

Check for missing or corrupt files - Fixed

Service registration is missing or corrupt - Fixed

Problems installing recent updates - Fixed

SFC Output is good by the way...

I tried a lot of things but I don't have any idea left. :(

Please help me :'( Thank you in advance

## Answer (community) — community member

*upvotes: 0 · updated: 2014-02-21*

Bonjour,

Sur les forums français, on poste en français.

De plus, ton problème concerne Server 2008.

Merci de poser ta question en français sur le forum Technet compétent

http://social.technet.microsoft.com/Forums/fr-fr/home?forum=windowsserver2008fr&filter=alltypes&sort=lastpostdesc
