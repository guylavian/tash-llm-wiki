---
title: "Windows Server 2019 Domain Controller &amp; SBS 2011"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/79068/windows-server-2019-domain-controller-amp-sbs-2011
question_id: 79068
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Windows Server 2019 Domain Controller &amp; SBS 2011

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/79068/windows-server-2019-domain-controller-amp-sbs-2011 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, We have a Windows Server SBS 2011 Domain Controller which we are in the process of decommissioning. We have upgraded the Forest and Domain Functional Levels to Windows Server 2008 R2. We have also migrated the File Replication Service to DFS-R, and confirmed that it is in the eliminated state. When i go to prompt the Windows 2019 Server as a Domain Controller I receive a message which states "Verification of replica failed. The forest functional level is not supported. To install a Windows Server 2019 domain or domain controller, the forest functional level must be Windows Server 2008 or higher". All services are running as expected. ![20929-error.png][1] ![20877-dfsr.png][2] ![20857-fls.png][3] Any ideas why its still giving me an error. David [1]: /api/attachments/20929-error.png?platform=QnA [2]: /api/attachments/20877-dfsr.png?platform=QnA [3]: /api/attachments/20857-fls.png?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-31*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-27*

You're welcome.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-27*

ok. Cheers @Anonymous

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-27*

SERVER1 is multi-homed (RRAS role VPN?) multi-homing will always cause no end to grief for active directory DNS. Also remove the invalid DNS addresses from connection properties 194.74.65.68, 194.72.9.38 then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service.  

334-W19-SRV01 disable the unused network adapter  

I didn't look at other files since these are show stoppers. If problems persist after corrections then put up a new set of files to look at.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-27*

Please run;  

-  Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log  

-  repadmin /showrepl >C:\repl.txt  

-  ipconfig /all > C:\dc1.txt  

-  ipconfig /all > C:\dc2.txt  

then put unzipped text files up on OneDrive and share a link.
