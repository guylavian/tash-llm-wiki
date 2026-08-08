---
title: "Active Directory Admin Center Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/366061/active-directory-admin-center-error
question_id: 366061
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Admin Center Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/366061/active-directory-admin-center-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an issue using Active Directory Admin Center on windows 10 20H2. Anytime I open it, it just says active directory admin center must close due to unknown error. Never had this till recently. This only happens on one windows 10 pc. I can go to another windows pc and AD Admin works fine.  

Also I have found at the same time this issue started now when using network application or accessing a network share I get prompted for my username and password. When I enter my credentials everything works fine for those. I did not have to login to these before. I only get this issue on one pc. If I use another pc with AD Admin it works fine.  

I ran  Test-ComputerSecureChannel and returned True in powershell  

here are the logs  

```
Application: dsac.exeFramework Version: v4.0.30319Description: The process was terminated due to an unhandled exception.Exception Info: System.ComponentModel.Win32ExceptionException Info: System.Security.Authentication.InvalidCredentialException at System.Net.Security.NegoState.ProcessReceivedBlob(Byte[], System.Net.LazyAsyncResult) at System.Net.Security.NegoState.StartSendBlob(Byte[], System.Net.LazyAsyncResult) at System.Net.Security.NegoState.StartSendBlob(Byte[], System.Net.LazyAsyncResult) at System.Net.Security.NegoState.ProcessAuthentication(System.Net.LazyAsyncResult) at System.Net.Security.NegotiateStream.AuthenticateAsClient(System.Net.NetworkCredential, System.String, System.Net.Security.ProtectionLevel, System.Security.Principal.TokenImpersonationLevel) at System.ServiceModel.Channels.WindowsStreamSecurityUpgradeProvider+WindowsStreamSecurityUpgradeInitia tor.OnInitiateUpgrade(System.IO.Stream, System.ServiceModel.Security.SecurityMessageProperty ByRef)Exception Info: System.ServiceModel.Security.SecurityNegotiationException

Fault bucket 1718350914684673182, type 5
Event Name: CLR20r3
Response: Not available
Cab Id: 0

Problem signature:
P1: dsac.exe
P2: 6.2.19041.1
P3: 95f4ee37
P4: dsac
P5: 6.2.19041.1
P6: 95f4ee37
P7: 657
P8: 0
P9: R0XNCPQBFLSQZBLWT1YW2LT3NYQDONJU
P10:

Attached files:
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER549A.tmp.dmp
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER573A.tmp.WERInternalMetadata.xml
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER576A.tmp.xml
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER5778.tmp.csv
\\?\C:\ProgramData\Microsoft\Windows\WER\Temp\WER57B7.tmp.txt

These files may be available here:
\\?\C:\ProgramData\Microsoft\Windows\WER\ReportArchive\AppCrash_dsac.exe_769452718ee2a354462e94c46dce7318bc5ae033_ae1faa26_dbd44350-515d-4dfd-b2e1-a8d001daef96

Analysis symbol:
Rechecking for solution: 0
Report Id: 62c388d6-e983-4a93-b3e1-bd9eead8d3a5
Report Status: 268435456
Hashed bucket: 3f59cba5f4db3b58e7d8cf0d7d3f5c9e
Cab Guid: 0
Faulting application name: dsac.exe, version: 10.0.19041.1, time stamp: 0x95f4ee37
Faulting module name: KERNELBASE.dll, version: 10.0.19041.804, time stamp: 0x0e9c5eae
Exception code: 0xe0434352
Fault offset: 0x000000000002d759
Faulting process id: 0x3064
Faulting application start time: 0x01d72fa29770f7d9
Faulting application path: C:\WINDOWS\system32\dsac.exe
Faulting module path: C:\WINDOWS\System32\KERNELBASE.dll
Report Id: 62c388d6-e983-4a93-b3e1-bd9eead8d3a5
Faulting package full name:
Faulting package-relative application ID:
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-30*

As best I can tell the ports are open  

As for powershell no I dont know I was hoping you or someone would.   

I tried Test-ComputerSecureChannel  that came back true.   

I am just guessing at this point.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-29*

I installed this a few years ago it had worked fine until recently. Originally I installed by downloading it. When I had the current issue I uninstalled it reinstalled via windows add remove feature. The ports needed are open. As I mentioned in my original post AD Admin is not the only issue, when I go to some network shares, or use Computer management to connect to another machine I get prompted to login   

and I can login, however before I had this issue I never had to login to those things, and if I do that from another pc I am not prompted either.   

Are there any powershell commands I can run to view settings and see if something is wrong?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-29*

Hello @GT  ,    

Thank you for your update.    

Would you please tell us how did you install the RSAT?    

Via Setting on the machine or download the RSAT tool and install it? You try two methods.    

Please check all the AD ports should be open from this machine to DC, so that client can locate DC to authenticate.    

Active Directory and Active Directory Domain Services Port Requirements    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)?redirectedfrom=MSDN    

Active Directory Replication over Firewalls    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727063(v=technet.10)?redirectedfrom=MSDN    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

Thanks for the help, and yes to all your questions. I have had this issue for several months, lots of changes and updates since the issue occurred no way to pin point when it started really. I have already tried several times to uninstall and reinstall AD client to no avail.   

My issue effects more than just the Active Directory client. For instance if I want to use computer management to connect to another pc   

I am prompted for my username and password, If I try to access certain shares on the network I get prompted for username and password.   

This was not the case before, I would not get prompted when trying to do these things.   

When I enter my credentials these things do work but not AD client.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-22*

Hello @GT  ,    

Thank you for posting here.    

1-Is your windows 10 20H2 with Active Directory Admin Center installed a domain-joined client?    

2-If so, did you install Windows Administrative Tools like Active Directory Administrative Center as below on this machine?    

    

3-Did you make any change on this machine before this issue occurs?    

4-Did you logon this windows 10 20H2 using domain Administrator account?    

I suggest we can uninstall Active Directory Administrative Center and reinstall it to see if it helps if possible.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou
