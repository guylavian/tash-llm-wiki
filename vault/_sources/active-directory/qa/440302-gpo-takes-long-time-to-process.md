---
title: "GPO takes long time to process"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/440302/gpo-takes-long-time-to-process
question_id: 440302
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO takes long time to process

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/440302/gpo-takes-long-time-to-process (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello community,    

For some employees, we have the problem that the total GPO processing take an extremely long time.    

The processing of the GPO components (Group Policy Environment, Registry, Services, ...) takes up to 21 seconds (screenshot at the bottom of the post).    

The screenshot is taken from Group Policy Result Wizard.    

This error is reproducible (while running gpupdate) and also occurs if the user uses a different domain controller.    

The error does not happen to everyone - not even with users and computers that are in the same AD OU.    

To log the error, I have already created the registry entry GPSvcDebugLevel.    

https://social.technet.microsoft.com/wiki/contents/articles/4506.group-policy-debug-log-settings.aspx    

I have added an excerpt from the log file when processing the “Group Policy Envorinment” (gpsvc.log).    

Here you can see that step takes just under 21 seconds.    

```
GPSVC(1ed0.2dc8) 09:03:47:804 LogExtSessionStatus: Successfully logged Extension Session data  
GPSVC(1ed0.2dc8) 09:03:47:817 ProcessGPOList: lpGPOInfo->lpGPInfoHandle->dwExtnCount is 2 for Group Policy Environment.  
GPSVC(1ed0.2dc8) 09:04:09:000 IsSecureCachingDisabled: secureCachingState = 2.
```

In order to expand the log additionally, I configured further logs via GPO.    

Computer Configuration> Administrative Templates> System> Group Policy> Logging and tracing    

Here I have set and activated the event logging to Informational, Warning and Errors for all available settings.    

In this log (computer.log) you can see that these steps are the time-consuming steps.    

```
2021-06-17 09: 03: 47.825 [pid = 0x1ed0, tid = 0x2dc8] Licensing subsystem initialized.  
2021-06-17 09: 03: 51.927 [pid = 0x1ed0, tid = 0x2dc8] User information initialized.  
2021-06-17 09: 04: 08.960 [pid = 0x1ed0, tid = 0x2dc8] Variable% ComSpec% = "C: \ WINDOWS \ system32 \ cmd.exe"
```

What else can I do to narrow down the error or to fix it?    

Attachments:    

106536-computer.log    

106555-gpsvc.log

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2021-06-18*

Hello @Alexander  ,

Thank you for posting here.

From the information provided above, it seems all GPO settings are applied successfully.

For the possible reasons why some GPOs takes long time to process:

1.The performance of the client machine  

2.Domain network performance

You can try to troubleshoot from the above two aspects.

Hope the information above is also helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-02*

Hello @Alexander  ,    

Thank you for your update.    

Based on your test below. I think the issue is related to GPO.    

    

You mentioned earlier，two machines with the same hardware, one has a problem and the other has no problem, then according to my understanding, the hardware of the machine is the same, the problem may be related to the operating system or the software or any application in the operating system.     

You can try to perform clean boot on the problematic machine and check if the issue persists.    

How to perform a clean boot in Windows    

https://support.microsoft.com/en-us/topic/how-to-perform-a-clean-boot-in-windows-da2f9573-6eec-00ad-2f8a-a97a1807f3dd    

If the issue disappears in clean boot mode, then maybe the third app or service caused the issue.    

Hope the information above is also helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-28*

Just give a try by renaming registry.pol file - "C:\Windows\system32\GroupPolicy\Machine\Registry.pol"  

then run gpupdate /force  

restart the machine

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-24*

Hello @Alexander  ,

Thank you for your update.

It seems one/more GPO settings caused the issue.

You can check as below:

Test 1  

1.Create a test domain user in domain (not in any OU). Right click domain name -> New->User (I mean this new test user applies no GPO setting except Default Domain Policy).  

2.Logon this problematic machine using this new test user and check if the issue persists.

Test 2  

1.Move this problematic machine from OU to domain temporarily if possible.

2.Logon this problematic machine using this new test user and check if the issue persists.

Hope the information above is also helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-22*

Hello @Alexander  ,    

Thank you for your reply.    

Based on my knowledge, you can try the Windows built-in Performance Monitor tool.    

    

For more information about Performance Monitor tool, please refer to links below.    

Windows Performance Monitor Overview    

https://techcommunity.microsoft.com/t5/ask-the-performance-team/windows-performance-monitor-overview/ba-p/375481    

Introducing the new Performance Monitor for Windows    

https://techcommunity.microsoft.com/t5/windows-admin-center-blog/introducing-the-new-performance-monitor-for-windows/ba-p/957991    

Hope the information above is also helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
