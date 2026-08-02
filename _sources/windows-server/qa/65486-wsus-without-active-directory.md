---
title: "WSUS without Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/65486/wsus-without-active-directory
question_id: 65486
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# WSUS without Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/65486/wsus-without-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Team  

I want to Configuration Windows Server Update Services (WSUS) without Active Directory,  

WSUS Server is not connect with AD, i will not connect AD.   

i want to patch update windows 10, server 2012, server 2016 by WSUS without AD.  

Please share microsoft documents and client working methods and diagram.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-08-26*

Hello MarufHossain-3174,

Please refer to the following steps to try if the issue will be resolved:

-   Apply the below policy on the Windows Server 2012:  

    [Turn off access to all Windows Update features]  

    (Location: Local Computer Policy\Computer Comfiguration\Administrative Templates\System\Internet Communication Management\Internet Communication settings)  

    Reference Picture:  

    

```
2.
```

Apply the below policy on the Windows Server 2016:  

[Do not allow update deferral policies to cause scans against Windows Update]  

(Location: Local Computer Policy\Computer Comfiguration\Administrative Templates\Windows Components\Windows Update)

Reference Picture:  

-   Update the Local Computer Policy on the clients  

    We could open CMD as administrator and enter `gpupdate/force` command to update the Local Computer Policy

- 

Approve the KB4571694 for the Windows Server 2016 client.  

Due to the KB4103723 has been replaced by other updates, I recommended to install 2020-08 Cumulative Update for Windows Server 2016 for x64-based Systems (KB4571694)  

Reference picture:  

If there are any updates about the above solutions, please let me know.

If the response is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-08-25*

Dear Rita & Team  

Please advice this issue, I hope early solutions from your end.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-18*

Dear Team  

Thanks A Lot for your advice  

I was shared my wsus client environment Windows 10, Server 2012 r2 & Server 2016 connect WSUS without domain. my WSUS in Server 2016  

Note: Patch updating only Windows 10 but patch is not downloading and updating server 20 r2 & server 2016.  

Please following the error message:  

2018-05 Cumulative Update for Windows Server 2016 for x64-based Systems (KB4103723) - Error 0x80244019  

(KB4562561) - Error 0x80244019  

Please advice me  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Hi.  

Perhaps you want to deploy easily with a registry key since your computers are not in the domain and GPO is not so easily managed.  

The target group line below should be already created in the WSUS Server.  

The two lines with http - you should have a reachable wsus server on http and change the lines coresponding to your addresses.  

You can change anything not wanted below.  

Windows Registry Editor Version 5.00  

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate]  

"ElevateNonAdmins"=dword:00000000  

"TargetGroup"="WSUSManagedPCs"  

"TargetGroupEnabled"=dword:00000001  

"WUServer"="http://mywsusserver.local:80"  

"WUStatusServer"="http://mywsusserver.local:80"  

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU]  

"AUOptions"=dword:00000004  

"AUPowerManagement"=dword:00000001  

"AutoInstallMinorUpdates"=dword:00000001  

"DetectionFrequency"=dword:0000000a  

"DetectionFrequencyEnabled"=dword:00000001  

"IncludeRecommendedUpdates"=dword:00000001  

"NoAUAsDefaultShutdownOption"=dword:00000001  

"NoAUShutdownOption"=dword:00000001  

"NoAutoRebootWithLoggedOnUsers"=dword:00000001  

"NoAutoUpdate"=dword:00000000  

"RebootRelaunchTimeout"=dword:0000000a  

"RebootRelaunchTimeoutEnabled"=dword:00000001  

"RescheduleWaitTime"=dword:0000000a  

"RescheduleWaitTimeEnabled"=dword:00000001  

"ScheduledInstallDay"=dword:00000000  

"ScheduledInstallTime"=dword:00000003  

"UseWUServer"=dword:00000001
