---
title: "Issue installing Exchange 2010 SP3 Rollup 21 on SBS 2011"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/356052/issue-installing-exchange-2010-sp3-rollup-21-on-sb
question_id: 356052
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Issue installing Exchange 2010 SP3 Rollup 21 on SBS 2011

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/356052/issue-installing-exchange-2010-sp3-rollup-21-on-sb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am having the very same issue as in this post:  

https://social.technet.microsoft.com/Forums/exchange/en-US/08c8de69-e7c2-49ef-adb6-780c3392abb4/issue-installing-exchange-2010-sp3-rollup-21-on-sbs-2011  

Unfortunately the thread ends without any solution.  

I cannot install any RU on this Exchange 2010 SP3 with always the same issue as outlined in the post mentioned.  

Currently very critical with not being able to install the very critical RU32.  

I searched and tried lots of things, no solution yet.  

Any help available?  

Thanks a lot!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-16*

@Yuki Sun-MSFT       

You are perfectly right, I came across these topics.    

Sure, I used elevated CMD.    

And here are the log entries:    

```
Couldn't find local patch 'C:\Windows\Installer\32bae786.msp'. Looking for it at its source.  
Resolving Patch source.  
...  
SOURCEMGMT: Processing net source list.  
Note: 1: 1402 2: UNKNOWN\Net 3: 2   
Note: 1: 1706 2: -2147483647 3: Exchange2010-KB2961522-x64-EN.MSP   
SOURCEMGMT: Resolved source to: 'Exchange2010-KB2961522-x64-EN.MSP'  
Note: 1: 1314 2: Exchange2010-KB2961522-x64-EN.MSP   
Unable to create a temp copy of patch 'Exchange2010-KB2961522-x64-EN.MSP'.  
...  
Could not find source for missing patch {A93DA06F-A5B8-4DF8-8B3F-B285E014C659} -- orphaning this patch  
...  
Opening existing patch 'C:\Windows\Installer\1c2088c5.msp'.  
Note: 1: 2203 2: C:\Windows\Installer\1c2088c5.msp 3: -2147287038   
Couldn't find local patch 'C:\Windows\Installer\1c2088c5.msp'. Looking for it at its source.  
Resolving Patch source.  
...  
Note: 1: 1402 2: UNKNOWN\Net 3: 2   
Note: 1: 1706 2: -2147483647 3: Exchange2010-KB3184728-x64-en.MSP   
SOURCEMGMT: Processing media source list.  
SOURCEMGMT: Resolved source to: 'Exchange2010-KB3184728-x64-en.MSP'  
...  
Could not find source for missing patch {9B55849A-D0A7-4F16-978B-D4D389ADD022} -- orphaning this patch
```

KB2961522: This is RU 7    

KB3184728: This is RU 15    

Both are not available anymore, so I cannot do what is suggested in the Article you mentioned.    

Sorry, I was not exhaustive, this was what I meant in the previous post with "One last thing could be to provide to the installer the RU 7 and 15 which it might search. But these are not available anymore and it is not clear if this could be a solution?"    

Strange seems this line: "Note: 1: 1402 2: UNKNOWN\Net 3: 2 " which I cannot interpret...    

and    

"orphaning this patch" (it could be a hint that the installer "understands" the KB is not available and skipps it, but really I am not so sure)    

Please tell me if this helps or if you maybe need the full log or something else.    

Thanks a lot for your help, very much appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

Hello,  

unfortunately, this did not bring anything (installing without Virus Scan).  

Concerning the upgrade advice: this would be certainly the preferred solution within normal times.  

In these days, when companies are fighting for their sheer existence, it is for sure not the only sufficient solution to buy a new server, new software and pay for the migration.

The eventlog is not much different than in the post I mentioned:

```
EventID 1023
    Product: Microsoft Exchange Server - Update 'Update Rollup 32 for Exchange Server 2010 Service Pack 3 (KB5000978) 14.3.513.0' could not be installed. Error code 1603. Additional information is available in the log file C:\Users\....\AppData\Local\Temp\MSI4383c.LOG.
    Microsoft Exchange Server 
       Update Rollup 32 for Exchange Server 2010 Service Pack 3 (KB5000978) 14.3.513.0 
       1603 
       C:\Users\...\AppData\Local\Temp\MSI4383c.LOG 

    MSI4383c.LOG:
    The installer encountered an unexpected error while installing this package. This may indicate a problem with this package. The error code is 2771. The arguments are: AdminTools, , 
    === Logging stopped: 12.04.2021  13:44:24 ===
```

Searching for "Admin Tools" I found something about RegEntries that should show the different services  

e.g.  

HKLM/SOFTWARE/MICROSOFT/EXCHANGE/V14/ADMINTOOLS  

where Configured Version should be the same as UnpackedVersion.  

It is.

Then we see

```
Event ID1000 (Application Error)
```

```
Faulting application name: msiexec.exe, version: 5.0.7601.24460, time stamp: 0x5cd43bee
Faulting module name: msvcrt.dll, version: 7.0.7601.17744, time stamp: 0x4eeb033f
Exception code: 0xc0000005
Fault offset: 0x00000000000035e1
Faulting process id: 0x2408
Faulting application start time: 0x01d7315aafbe131f
Faulting application path: C:\Windows\System32\msiexec.exe
Faulting module path: C:\Windows\system32\msvcrt.dll
Report Id: f02b6659-9d4d-11eb-a27c-d4ae52c88221
```

Somewhere it is reported to repair the Faulting module msvcrt.dll by reinstalling the Visual C++ Redist.  

No positive effect.

(Re)starting the Windows Installer Service: no effect.

To summarize:  

-  VirusScan stop: no effect  

-  Checking Eventlog and applying possible solutions (admin tools): no effect  

-  reinstalling VC: no effect  

-  restarting Windows Installer: no effect.

One last thing could be to provide to the installer the RU 7 and 15 which it might search. But these are not available anymore and it is not clear if this could be a solution?

I would be grateful for ideas ...

Thanks a lot!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-14*

Hi @Milestone 02  ,    

As regards to the error indicated in the post you mentioned above, based on my personal experience, it's suggested to try temporarily disabling all Exchange-integrated antivirus or backup products in your environment if there are any and see whether it can be helpful.    

However, as is indicated in this blog, actually both SBS 2011 and Exchange 2010 are out of support right now, so if the above doen't work, I'd recommend planning to migrate SBS and exchange to mainsteam versions as soon as possible. Here are some links for your reference:    

Migrating from SBS 2011 to Windows Server 2016 and Exchange Server 2016    

Active Directory Migration from SBS 2008 or 2011 to Windows Server 2016    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
