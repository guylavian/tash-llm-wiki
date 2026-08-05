---
title: "Windows Server 2012 R2 Exchange 2016 server Blue Screens after disabling TLS/SSL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1138530/windows-server-2012-r2-exchange-2016-server-blue-s
question_id: 1138530
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Windows Server 2012 R2 Exchange 2016 server Blue Screens after disabling TLS/SSL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1138530/windows-server-2012-r2-exchange-2016-server-blue-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. I have a Windows Server 2012 R2 with Exchange Server 2016 installed with Exchange2016-KB5019758-x64-en.exe installed. I am attempting to harden the server so that I can install Extended Protection Extended Protectionhttps://microsoft.github.io/CSS-Exchange/Security/Extended-Protection/  . I followed the article at https://learn.microsoft.com/en-us/Exchange/exchange-tls-configuration?view=exchserver-2019  and https://learn.microsoft.com/en-us/Exchange/exchange-tls-configuration?view=exchserver-2016  to harden the server. I followed the article in the steps it outlines and I notice that once I run the CiperSuitesOrder.reg and reboot, the server blue screens with  System Thread Exception Not Handled (NETIO.SYS) . I was able to recover it using last known good configuration but that doesn't solve my issue as I need to disable these protocols. This server is a VM running on VMWare 7.0  ESXi with the latest VMWare patches and VMWTools installed on the guest VM.  I found others with the same issue but did not find any resolution to the issue.    

I ran SFC /SCANNOW and it did not find any issues. I ran a CHKDSK and that also resulted in not finding any issues.     

I did a lot of looking on the internet and could not find a solution to the issue.    

I ran bluescreenview but it did not find any .DMP files. I have it set to automatic memory dump.  I changed it to small memory dumps and reran the file CiperSuitesOrder.reg and rebooted. Again it Blue Screened.  But it just sat at 0% for many hours until I finally just rebooted the server and it went into Automatic Repair where I did advanced and rebooted and selected Last Known Good to get the server back up and running.    

I booted back into Windows and in the System event log I have event ID 46 with error Volmgr "Crash Dump initialization failed!"     

Any ideas on how I can fix this?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-29*

I re-enabled TLS 1.0 and then ran the registry fix that was causing the BSOD. I rebooted and still get a BSOD, so it is not RDP causing the issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-29*

Hi,    

Thank you for posting your query.    

Kindly follow the steps provided below to resolve your issue.    

To answer your query it may be caused by some applications on the server still trying to use the disabled protocols.    

For example, if Remote Desktop service is installed on the server, disabling TLS 1.0 may affect the service.    

Here is an Microsoft document: RDS Connection Broker or RDMS fails after you disable TLS 1.0 in Windows Server    

Also a TechNet case link for your reference: (Event ID: 36871) RDP to Windows 2012 Server    

Go to this link for your reference and other troubleshooting procedures https://learn.microsoft.com/answers/questions/345906/a-fatal-error-occurred-while-creating-an-ssl-clien.html    

https://learn.microsoft.com/en-us/exchange/exchange-tls-configuration    

----------------------------------------------------------------------------------------------------------------    

If the answer is helpful kindly click "Accept as Answer" and up vote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-29*

Please run the DM log collector and post a share link into this thread using one drive, drop box, or google drive.    

(make sure that links are available without logon and that no terms and conditions links need to be clicked)    

If the server can run the V2 log collector it can collector more useful log files for troubleshooting.    

https://www.tenforums.com/bsod-crashes-debugging/2198-bsod-posting-instructions.html    

https://www.elevenforum.com/t/bsod-posting-instructions.103/    

.    

.    

.    

.    

.    

Please remember to vote and to mark the replies as answers if they help.    

On the bottom of each post there is:    

Propose as answer = answered the question    

On the left side of each post there is /\ with a number: click = a helpful post    

.    

.    

.    

.    

.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-27*

No one has any ideas or answers?
