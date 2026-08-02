---
title: "[MCM] Problem after the migration of our ADCS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2282915/mcm-problem-after-the-migration-of-our-adcs
question_id: 2282915
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-application"]
---
# [MCM] Problem after the migration of our ADCS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2282915/mcm-problem-after-the-migration-of-our-adcs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone, 

Before explaining our current issue, here is a quick overview of our MCM infrastructure. We have one site spread across three servers: 1 internal Management/Distribution Point (MGT/DP), 1 Database (DB) server, 1 internal DP, and another 1 DP used for external clients.

Currently, we are experiencing global issues with our MCM servers. Yesterday, following the migration of our ADCS to another server, everything initially appeared to be working fine. MCM seemed to function properly that same day, even after manually renewing the existing certificates via "certlm.msc". However, this morning, the situation changed significantly. We are now unable to properly launch the Software Center (on clients), it no longer displays our custom theme, and new software applications are not shown. Additionally, when performing a bare-metal deployment via PXE Boot, the MCM client (Configuration Manager & Software Center) appears to install, but it fails to apply its configuration, and none of the software from the task sequence is being installed. When reviewing the log files on our MGT/DP servers, we observed the following errors (translated from French to English): 

The management point control manager has detected that the user service is not responding to HTTP requests. The HTTP status code and text are 12175, . 

Possible cause: Internet Information Services (IIS) is not running or is not configured to listen on the ports used by the site. 
Solution: Verify that the designated website is configured to use the same ports as those used by the site. 
Possible cause: The designated website is disabled in IIS. 
Solution: Verify that the designated website is enabled and functioning correctly. 
Possible cause: The application pool identity for the user service does not have the necessary logon privileges. 
Solution: Ensure that the application pool for the user service is configured to run under the Network Service account. 
Possible cause: ASP.NET is not installed. 
Solution: Make sure to select ASP.NET 4.5 or later under Web Server – Application Development and Features in Windows Server. 
Possible cause: The ASP.NET application is not functioning properly. 
Solution: Navigate to http(s)://localhost/CMUserService_WindowsAuth/ApplicationViewService.asmx on the local server machine and follow the error instructions.

Here’s what we’ve done so far:

-  Re-renewed our certificates (Web Server, DP, and Client but NOT the ones on our DB).

-  Verified that the correct certificates were in place on ISS after their renewal (by checking the validity dates).

-  Renewed the "SMS Issuing" certificate from "Administration >> Security >> Certificates" (based on online recommendations suggesting it might help, spoiler alert it didn't.).

-  Cleared the Windows Certificate Services cache using "certutil".

-  (And of course) rebooted each server.

Is there something we might have overlooked? We're unsure what else to check. We appreciate any help or guidance you can provide. Thank you!

## Answers

_No answers on this thread._
