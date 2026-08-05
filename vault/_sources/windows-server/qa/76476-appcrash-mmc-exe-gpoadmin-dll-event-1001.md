---
title: "Appcrash mmc.exe gpoadmin.dll event 1001"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/76476/appcrash-mmc-exe-gpoadmin-dll-event-1001
question_id: 76476
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Appcrash mmc.exe gpoadmin.dll event 1001

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/76476/appcrash-mmc-exe-gpoadmin-dll-event-1001 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Experiencing many APPCRASH errors on both DCs relating to mmc.exe and gpoadmin.dll.  No other modules are crashing with mmc.  This even happens after reboot and not opening MMC at all.  Group policies are being applied to clients without error.  Any help is appreciated.  

```
Fault bucket 1597587120586990667, type 4
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
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER154C.tmp.dmp
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER3827.tmp.WERInternalMetadata.xml
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER38F3.tmp.xml
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER3920.tmp.csv
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER3940.tmp.txt
\\?\C:\Users\mcAdmin\AppData\Local\Temp\WER3BF3.tmp.appcompat.txt
\\?\C:\ProgramData\Microsoft\Windows\WER\ReportQueue\AppCrash_mmc.exe_bd3e25626ecb758ca6a9952f72b41a1c7102136_e7efc520_cab_19753ebd\memory.hdmp

These files may be available here:
\\?\C:\ProgramData\Microsoft\Windows\WER\ReportArchive\AppCrash_mmc.exe_bd3e25626ecb758ca6a9952f72b41a1c7102136_e7efc520_0986613e

Analysis symbol: 
Rechecking for solution: 0
Report Id: fc8a71e5-b3de-4d1d-9e31-68544e224a8a
Report Status: 268435556
Hashed bucket: 1bb22658644e0201f62bc5059453a44b
Cab Guid: 0
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-06*

The same problem with English Windows Server 2019 Standard. Deployed 8 new DCs.  

GPO mmc console generally looks that it works fine.  

I can see this information in Application Events, Event ID; 1001  

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

Event ID; 1000  

Faulting application name: mmc.exe, version: 10.0.17763.1282, time stamp: 0xb86dd98f  

Faulting module name: GPOAdmin.dll, version: 10.0.17763.1282, time stamp: 0x768f8fa6  

Exception code: 0xc0000005  

Fault offset: 0x00000000000bb57b  

Faulting process id: 0x1f58  

Faulting application start time: 0x01d69bb99c4804ae  

Faulting application path: C:\Windows\system32\mmc.exe  

Faulting module path: C:\Windows\System32\GPOAdmin.dll  

Report Id: 531da7d9-69ed-439f-9729-ab4ac5d162ad  

Faulting package full name:   

Faulting package-relative application ID:  

I think that this is not coincidence, more admins experiences this behavior. Microsoft please fix it in some nice update. Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-01*

Using German Server 2019 Standard, installed from the following ISO: SW_DVD9_Win_Server_STD_CORE_2019_1809.2_64Bit_German_DC_STD_MLF_X22-18454.ISO  

I can confirm that this is a problem with Server 2019 Standard.  

GPO editing works, BUT when I close the Editor it throws an error every time.  

Don't tell me not to work on the server and to use a workstation, just fix it! Thank you!  

Installed 4 new DCs and EVERY DC (latest patches applied, DISM/SFC no problems) reports this error!  

Name der fehlerhaften Anwendung: mmc.exe, Version: 10.0.17763.1282, Zeitstempel: 0xb86dd98f  

Name des fehlerhaften Moduls: GPOAdmin.dll, Version: 10.0.17763.1282, Zeitstempel: 0x768f8fa6  

Ausnahmecode: 0xc0000005  

Fehleroffset: 0x00000000000bb57b  

ID des fehlerhaften Prozesses: 0xd48  

Startzeit der fehlerhaften Anwendung: 0x01d697d1c9623b49  

Pfad der fehlerhaften Anwendung: C:\Windows\system32\mmc.exe  

Pfad des fehlerhaften Moduls: C:\Windows\System32\GPOAdmin.dll  

Berichtskennung: eeadd893-0a83-426d-8a6d-ae889877dd98  

Vollständiger Name des fehlerhaften Pakets:   

Anwendungs-ID, die relativ zum fehlerhaften Paket ist:

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-26*

Hi Freddie,    

Welcome to Microsoft Q&A.    

Please help check below questions so we can narrow down the issue    

-  The OS version of the problematic DCs    

-  Is the problematic server a physical machine or virtual machine?    

-  Do we see the blue screen? What is the Bugcheck code?    

Try following methods to see if it helps:     

-  Disable FSRM on the DC    

-  Try reinstall the MMC    

-  Run following commands in an elevated command prompt    

sfc /scannow    

DISM.exe /Online /Cleanup-image /Restorehealth    

-  Check for available updates and security patches to keep your system updated.    

-  You can download the WinDbg Preview from Microsoft Store for dump analysis.    

Reference link —— Analyzing a Kernel-Mode Dump File with WinDbg    

https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/analyzing-a-kernel-mode-dump-file-with-windbg     

Please remember to mark the reply as answer if it helps.    

Best regards,    

Molly    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-25*

To rule out other issues I'd recommend not using a sys-prepped image. Better to stand one up from clean installation media, patch fully, join existing domain, then promo it (with the usual precautions of confirming domain health is 100% beforehand)  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-25*

Might try standing up a new domain controller as a test.
