---
title: "KERBEROS LOCAL KEY DISTRIBUTION CENTER START PENDING ..."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2157045/kerberos-local-key-distribution-center-start-pendi
question_id: 2157045
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# KERBEROS LOCAL KEY DISTRIBUTION CENTER START PENDING ...

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2157045/kerberos-local-key-distribution-center-start-pendi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have built three brand new Windows 2025 Servers with the latest updates.

On all three of them I see that the service KERBEROS LOCAL KEY DISTRIBUTION CENTER START PENDING but it never turns into the RUNNING STATE. If I try to manually start the service, all the options are greyed out.

I'm not sure if this is just a glitch the service showing as starting but it is actually running as I don't notice any issues with the server etc. but maybe there is something wrong. I'm just worried that once I remove my old Windows 2019 server where all the services are running fine, that I could start having issues with user authentication or similar.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-13*

I have checked my Windows server 2019 vs the Windows server 2025 and this is what I found:

On the Windows server 2025, after promoting to a Domain Controller, two services exist:

-  Kerberos Key Distribution Center - RUNNING - set to start AUTOMATICALLY

-  Kerberos Local Key Distribution Center - STARTING - set to start AUTOMATICALLY

However, this Local Key service will never start and will show up as error under Server manager.

On the Windows server 2019, after promoting to a Domain Controller, only one service exists:

-  Kerberos Key Distribution Center - RUNNING - set to start AUTOMATICALLY

So, what I believe is that during the promotion process on the Windows server 2025, the Kerberos Local Key Distribution Center Service was supposed to be removed, but it wasn't as I'm suspecting this to be a glitch on the new Windows server 2025. When I set the Kerberos Local Key Distribution Center Service to MANUAL start, all the errors disappear as the service will not attempt to start automatically anymore, and I can still log on to the machine using local or domain accounts.

If I'm correct, I would hope MS can fix this with their updates, but it's been 2 months and it hasn't been fixed.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-06*

Hello,

Please check the following configuration:

Check service dependencies: Use the Service Manager to view the dependencies of the Kerberos KDC service and ensure that all dependent services are running.

Run the System File Checker: Run the Command Prompt as an administrator and enter the command "sfc /scannow" to scan and repair any damaged system files.

Check and fix permission issues: Ensure that the current user account has sufficient permissions to start and manage the Kerberos KDC service. You can try logging in as an administrator and attempting to start the service again.

Clear cache files: Try deleting the cache files of Server Manager. The paths may include C:\Users\username\AppData\Roaming\Microsoft\Windows\ServerManager\Cache and C:\Windows\Temp\ServerManager.exe (Note: Please back up important data before deletion).

View the Event Viewer: Check the error logs related to the Kerberos KDC service in the Windows Event Viewer, which may provide more clues about the root cause of the problem.

I hope the information above is helpful.

Best regards

Zunhui

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
