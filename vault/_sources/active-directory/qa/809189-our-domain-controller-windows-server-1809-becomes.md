---
title: "Our domain controller (Windows Server 1809) becomes unresponsive since January around every 2 weeks after the first logon of a user."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/809189/our-domain-controller-windows-server-1809-becomes
question_id: 809189
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Our domain controller (Windows Server 1809) becomes unresponsive since January around every 2 weeks after the first logon of a user.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/809189/our-domain-controller-windows-server-1809-becomes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Technet community,  

Since January we have the following problem on our first domain controller. It becomes unresponsive (or really really slow) after the first logon of a user around every two weeks.  

There's no task on the server that's triggered every 2 weeks. When it happens I can't do anything, I need to force the shutdown with the power button of the server. If I remember one time I could log my self on the server but nothing happens after it was impossible to do something. After the restart of the machine everything is fine and works without any problem.  

The last time before the problem the "WMI Performance Adapter" and  "Network Setup Service" were starting (and the time before "Network Setup Service" and "Windows Modules Installer"), but I'm not sure if it's relevant. The problem is that when it happens, I can't access the server to check something. It seems to be a sort of buffer overflow. On the physical server we can see the leds of the hdd  and NIC blinking really fast. There's no dump file because the server is still working (no blue or black screen). I am at the End of my Latin. We have System Center Operation Manager that could help us too, but the only information that I have, it's a timeout of the PowerShell scripts for the task management of SCOM on the server. Now I found a script to configure the Performance Monitor and create a log file with the infos, but I can't afford myself 2 weeks to wait the next problem. It could be a real problem if it happens when I'm not at the office.  

I'm aware about the problem with the KB5009557, KB5010791. I've followed this path too and we have applied the next cumulatives patch (February / March).  

I've already try to read every Windows event logs that I have and it's really time consuming. If you have an idea about a strategy for this problem you're welcome. I would like to find a solution before the end of the next 2 weeks if it's possible. Maybe I forget about something important to check, maybe I don't know really how to check Windows Server 2019.  

Could you please help me/us to find the right path to debug this Problem on the system?  

Thank you ahead.  

Joel T.  

Wuensch AG

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-12*

192412-dc2-20220412.txt192382-dcdiag-20220412.log192326-dc1-20220412.txt192383-repl-20220412.txt    

Hi Patrick,    

I've sent the files here, because they're smaller as 3MB.    

Thank you for your help,    

Regards,    

Joel.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-04-12*

Please run;  

`Dcdiag /v /c /d /e /s:%computername% >C:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`  

`ipconfig /all > C:\dc2.txt`  

`ipconfig /all > C:\dc3.txt`  

then put `unzipped` text files up on OneDrive and share a link.
