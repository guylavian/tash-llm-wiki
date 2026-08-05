---
title: "Unable to Uninstall Exchange server 2016 in a Windows server 2025"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2145972/unable-to-uninstall-exchange-server-2016-in-a-wind
question_id: 2145972
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to Uninstall Exchange server 2016 in a Windows server 2025

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2145972/unable-to-uninstall-exchange-server-2016-in-a-wind (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have recently performed an in-place upgrade to the Exchange server (Which was running Windows server 2016) to the Windows server 2025. The upgrade went smoothly. We then tried uninstalling the Exchange server role, considering we are entirely into the M365. However, we encountered a problem where the readiness check threw an error, as shown below.

Error:

The following error was generated when "$error.Clear(); 

```
if (Get-Service MpsSvc* | ?{$_.Name -eq 'MpsSvc'})

      {

        Set-Service MpsSvc -StartupType Automatic

        Start-SetupService -ServiceName MpsSvc

      }

    " was run: "Microsoft.PowerShell.Commands.ServiceCommandException: Service 'Windows Defender Firewall (MpsSvc)' cannot be configured due to the following error: Access is denied ---> System.ComponentModel.Win32Exception: Access is denied
```

The Windows Defender service is running already, and I'm using an enterprise admin account (in AD), which is also a member of the OrganisManagement Group in AD. We need to remove the Exchange server app from the server, and then we can remove the trace of Exchange in AD.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-14*

Hi @BMcclane ，

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, when you uninstall the Exchange server role, the readiness check throws an error. To identify the cause of the issue more accurately, can you provide and try the following information:

-  Can you confirm that you have logged on to the server using a domain administrator user account and not a local administrator user account? And you need to open the PowerShell console with "Run as Administrator" permissions.

-  Have you shut down EMS and any other programs that may delay the uninstall process (for example, .NET assemblies, antivirus software, and backup agents)?

-  You can try to create a brand new Exchange user mailbox, and the user needs to be a member of the Domain Admins, Enterprise Admins, Schema Admins, Organization Admins, and Local Admins groups on the affected workstation, then log on to the workstation and try to uninstall Exchange again.

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne
