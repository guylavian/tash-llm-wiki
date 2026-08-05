---
title: "MSExchangeServiceHost keeps crashing and restarting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166932/msexchangeservicehost-keeps-crashing-and-restartin
question_id: 1166932
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MSExchangeServiceHost keeps crashing and restarting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166932/msexchangeservicehost-keeps-crashing-and-restartin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I've been noticing that many servers in my org have the MSExchangeServiceHost service is crashing and restarting fairly regularly. Attached are two files, one being a sweep of all servers in my environment showing services in different states, using the Get-Service cmdlet across the org, with a 60 second break between Server54 and Server1. If you download it, should probably save it as a CSV so you can sort it. The second file is the 4999 events from one server, showing how fast it crashes and then restarts. Now, the pattern of events goes essentially like this:

EventID: 9000

Level: Information

Source: MSExchange Mid-Tier Storage

Message: [Process:Microsoft.Exchange.ServiceHost PID:14780 Thread:83] Successfully populated ServiceTopology. Reason to populate ServiceTopology = CacheNotPresent 

Event ID: 9000

Message: [Process:w3wp PID:30808 Thread:579] Successfully populated ServiceTopology. Reason to populate ServiceTopology = RefreshTimeout

Then event 4999, then several events saying that each Exchange role (Client, Mailbox, Transport) were installed, the several events about various servicelets being loaded, then an event saying the service was successfully started, and then some other events building on the idea that everything was successfully loaded/started.

There is a KB article that mentions something like this problem, but even after updating to the latest stuff, it still occurs. We also don't have any certificates that are soon expiring.

Is there a way to capture more information on what might be causing the crash?

ServiceHostUpAndDownAcrossOrg.txt

MSExchangeServiceHostCrashingEventLog.txt

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-20*

Hi，

we've updated all the servers now and the service hasn't been crashing

I'm glad to hear that you solved the problem and thanks for sharing.

Do you mean you updated all servers with cumulative updates and security updates?

If that's the case, we've taken a big detour.

As mentioned in the Knowledge Base mentioned in the original issue description, this incident occurred after the March 2022 security update was installed. We need to install the May Update to fix this issue.

That's why I asked you in the first round of responses if all servers are update to the latest version.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-17*

Well, we've updated all the servers now and the service hasn't been crashing, so maybe that was how to fix it. I'd still like to know why it causes the service to crash though. That's unfortunate.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-03*

Hi @Joseph Larrew  ,

I noticed that you have a large number of servers, are all servers updated to the latest version?

If you don't have any expired certificate on your system or any certificate that's about to expire, please follow these steps to remove the AsyncOperationNotification folder within the System mailbox to see if it can stop the Microsoft Exchange Services Host Service crashing：

 

1)      The user will need to have full access to arbitration mailbox

a.       Get-Mailbox -Arbitration "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}" | Add-MailboxPermission -User administrator -AccessRights FullAccess

2)      Run the Script from Exchange Command Shell login as the user with full permission assigned to arbitration mailbox

3)      Confirm all the messages are deleted

4)      Start the service MSExchangeServiceHost and confirm that it is not Crashing

5)      Revoke the full Access permission for the user

a.       Get-Mailbox -Arbitration "SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}" | Remove-MailboxPermission -User administrator -AccessRights FullAccess

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
