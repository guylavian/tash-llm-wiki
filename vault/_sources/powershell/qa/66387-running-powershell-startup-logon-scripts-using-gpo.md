---
title: "Running PowerShell Startup (Logon) Scripts Using GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/66387/running-powershell-startup-logon-scripts-using-gpo
question_id: 66387
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Running PowerShell Startup (Logon) Scripts Using GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/66387/running-powershell-startup-logon-scripts-using-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,

There are two user accounts, one is Administrator; another is normal user.

-   AD Domain: Windows Server 2019 with GPO <Running PowerShell Logon Scripts>

-   Client: Windows 10: (A) Use Administrator to login the AD Domain: GPO works well and add registry to HKLM; (B) Use normal User to login the AD Domain: GPO something went wrong and failed to add registry to HKLM.

The (B) situation: I copy the PowerShell to Windows 10 Client and perform the script, I got the error message:

New-Item : Access to the registry key  

'HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\OneDrive' is denied.  

At C:\Users\alanb\Desktop\Handling_OneDrive_REG.ps1:47 char:58  

-  ... HKLM:\Software\Policies\Microsoft" | New-Item -Name "OneDrive" -Force  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : PermissionDenied: (HKEY_LOCAL_MACH...rosoft\OneDrive:S  

tring) [New-Item], UnauthorizedAccessException  

-  FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShel  

l.Commands.NewItemCommand

New-ItemProperty : Cannot find path 'HKLM:\Software\Policies\Microsoft\OneDrive'  

because it does not exist.  

At C:\Users\alanb\Desktop\Handling_OneDrive_REG.ps1:50 char:5  

-  New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\OneDriv ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : ObjectNotFound: (HKLM:\Software...rosoft\OneDrive:Str  

ing) [New-ItemProperty], ItemNotFoundException  

-  FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.NewItemProp  

ertyCommand

New-ItemProperty : Cannot find path 'HKLM:\Software\Policies\Microsoft\OneDrive'  

because it does not exist.  

At C:\Users\alanb\Desktop\Handling_OneDrive_REG.ps1:51 char:5  

-  New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\OneDriv ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : ObjectNotFound: (HKLM:\Software...rosoft\OneDrive:Str  

ing) [New-ItemProperty], ItemNotFoundException  

-  FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.NewItemProp  

ertyCommand

New-ItemProperty : Cannot find path 'HKLM:\Software\Policies\Microsoft\OneDrive'  

because it does not exist.  

At C:\Users\alanb\Desktop\Handling_OneDrive_REG.ps1:52 char:5  

-  New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\OneDriv ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : ObjectNotFound: (HKLM:\Software...rosoft\OneDrive:Str  

ing) [New-ItemProperty], ItemNotFoundException  

-  FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.NewItemProp  

ertyCommand

I also setup some settings as the following:

-   the NTFS “Read & Execute” permissions for the Domain Computers group in the ps1 file permissions

-   setup Computer Configuration -> Administrative Templates -> System -> Group Policy section. Enable the “Configure Logon Script Delay” policy and specify a delay in minutes before starting the logon scripts (sufficient to complete the initialization and load all necessary services). --> 1-2 minutes.

-   The security settings for running the PowerShell script can be configured via the “Turn On Script Execution” policy (in the GPO Computer Configuration section -> Administrative Templates -> Windows Components -> Windows PowerShell) --> Allow all scripts (unrestricted)

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2020-08-14*

Hi,    

From what you mentioned above, the error was caused by the permission.    

Or you can considered to run the script by the schedule task ,and you can assign permission through the schedule task GPO as following,then when the task was running , it will run as system:    

      

You can also select run it once or not  as your requirement :    

    

Best Regards,

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-08-13*

Shouldn't you be using a registry-based policy setting to do this instead of logon scripts? Logon scripts run in the context of the user, and users shouldn't be altering policy settings.  

See one of these:  

Set-GPPrefRegistryValue  

Set-GPRegistryValue

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-08-13*

It looks like the "normal user" does not have access to the Registry key  'HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\OneDrive'  

Maybe it's worth a try to allow the user the access to the Registry key.  

Maybe this is helpful.  

Regards  

Andreas Baumgarten  

(Please don't forget to Accept as answer if the reply is helpful)
