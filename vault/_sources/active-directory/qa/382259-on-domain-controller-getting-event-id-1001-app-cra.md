---
title: "On Domain controller getting event ID 1001 - App Crash"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/382259/on-domain-controller-getting-event-id-1001-app-cra
question_id: 382259
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# On Domain controller getting event ID 1001 - App Crash

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/382259/on-domain-controller-getting-event-id-1001-app-cra (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows Error Reporting  

error id :1001  

Fault bucket , type 0  

Event Name: CbsPackageServicingFailure2  

Response: Not available  

Cab Id: 0  

Problem signature:  

P1: 10.0.17763.1690  

P2: Package_for_RollupFix  

P3: 17763.1697.1.9  

P4: amd64  

P5: unknown  

P6: 80073701  

P7: Resolve  

P8: Absent  

P9: Installed  

P10: WindowsUpdateAgent  

Attached files:  

\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WERC5FC.tmp.WERInternalMetadata.xml  

These files may be available here:  

\?\C:\ProgramData\Microsoft\Windows\WER\ReportQueue\Critical_10.0.17763.1690_8952fdfd9772292d8147e4356c809c3b382c61a9_00000000_13e508af  

Analysis symbol:   

Rechecking for solution: 0  

Report Id: 7055a08f-e055-43cb-89d2-d3a2138c3750  

Report Status: 4196  

Hashed bucket:   

Cab Guid: 0

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-10*

Just checking if there's any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-05*

Any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-05*

Hi,  

Based on my research, the 1001 event is logged by the Windows Error Reporting infrastructure for all reports (for example, application crashes, hangs, and generic reports).  

https://social.technet.microsoft.com/wiki/contents/articles/3116.event-id-1001-windows-error-reporting.aspx  

What's the actual problem when you use the DCs?  

Are there any errors in the output of the command following?   

Dcdiag /v >c:\dcdiag1.log      

Repadmin /showrepl >C:\repl.txt   

Repadmin /showreps *   

If no errors in the output, the issue may not relate to the domain service.  

Best Regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-04*

There are no replication errors identified in the DC,   

getting the error 1001 for random issues as well, PFB  

Fault bucket , type 0  

Event Name: APPCRASH  

Response: Not available  

Cab Id: 0  

Problem signature:  

P1: mmc.exe  

P2: 10.0.17763.1282  

P3: b86dd98f  

P4: GPOAdmin.dll  

P5: 10.0.17763.1282  

P6: 768f8fa6  

P7: c0000005  

P8: 00000000000bb57b  

P9:   

P10:   

Attached files:  

\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WEREE03.tmp.dmp  

\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WEREF2D.tmp.WERInternalMetadata.xml  

\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WEREF3E.tmp.xml  

\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WEREF3C.tmp.csv  

\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WEREF4C.tmp.txt  

\?\C:\Users\adm-gobry\AppData\Local\Temp\WEREF6F.tmp.appcompat.txt  

\?\C:\ProgramData\Microsoft\Windows\WER\ReportQueue\AppCrash_mmc.exe_bd3e25626ecb758ca6a9952f72b41a1c7102136_e7efc520_cab_467def7a\memory.hdmp  

These files may be available here:  

\?\C:\ProgramData\Microsoft\Windows\WER\ReportQueue\AppCrash_mmc.exe_bd3e25626ecb758ca6a9952f72b41a1c7102136_e7efc520_cab_467def7a  

Analysis symbol:   

Rechecking for solution: 0  

Report Id: 83c43c9d-1d8a-498b-9984-7983d515b66a  

Report Status: 100  

Hashed bucket:   

Cab Guid: 0

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-04*

Not a lot to go on but the simplest / safest solution may be to stand up a new one for replacement.    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new 2019?, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to Accept as answer if the reply is helpful--
