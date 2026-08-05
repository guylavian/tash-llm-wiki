---
title: "Microsoft Exchange Transport services auto stop in Window Server 2016 Standard"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2087476/microsoft-exchange-transport-services-auto-stop-in
question_id: 2087476
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange Transport services auto stop in Window Server 2016 Standard

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2087476/microsoft-exchange-transport-services-auto-stop-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The Microsoft Exchange Transport services will auto stopped

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-10-04*

Hello @PPDHIT

To troubleshoot and resolve the issue of Microsoft Exchange Transport services automatically stopping on Windows Server 2016 Standard, follow these steps:

Step 1: Check Event Viewer

-  Open the Event Viewer on the server.

-  Navigate to Windows Logs > Application and Windows Logs > System.

-  Look for any error messages or warnings related to the Exchange Transport service. Note down any error codes or messages.

Step 2: Verify Service Dependencies

-  Open Services (type `services.msc` in the Run dialog).

-  Locate Microsoft Exchange Transport service.

-  Right-click and select Properties.

-  Check the Dependencies tab to ensure all dependent services are running.

Step 3: Check Disk Space and Performance

-  Ensure there is sufficient disk space on the drive where Exchange is installed.

-  Check CPU and memory usage to ensure the server is not under heavy load.

Step 4: Review Exchange Logs

-  Navigate to the Exchange installation directory, typically `C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\Logs`.

-  Review the logs for any errors or warnings that might indicate why the service is stopping.

Step 5: Update Exchange and Windows

-  Ensure that both Exchange Server and Windows Server are up to date with the latest patches and updates.

-  Use Windows Update and Exchange Update Rollups to apply any pending updates.

Step 6: Check Antivirus/Firewall Settings

-  Ensure that antivirus or firewall settings are not blocking or interfering with the Exchange Transport service.

-  Add exceptions for Exchange processes if necessary.

Step 7: Restart the Service

-  In the Services window, right-click on Microsoft Exchange Transport and select Start.

-  Monitor the service to see if it stops again.

Step 8: Rebuild Transport Queue Database

-  If the issue persists, consider rebuilding the transport queue database:

-  Stop the Microsoft Exchange Transport service.

-  Navigate to `C:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\data\Queue`.

-  Rename the `Queue` folder to `Queue.old`.

-  Start the Microsoft Exchange Transport service. A new queue database will be created.

If this answers your query, do click `Accept Answer` and Up-Vote for the same. And, if you have any further query do let us know.
