---
title: "Microsoft Exchange Transport Service doesn't start after Cumilative Update 15.1.2507.32"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1350314/microsoft-exchange-transport-service-doesnt-start
question_id: 1350314
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Microsoft Exchange Transport Service doesn't start after Cumilative Update 15.1.2507.32

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1350314/microsoft-exchange-transport-service-doesnt-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Yesterday I have installed Cumliative Update "15.1.2507.32" on our Exchange Server 2016. After the update we couldn't send and receive emails. I checked the Event Logs and found this error logs:

-  "Failed to start listening (Error: 10048). Binding: 0.0.0.0:2525."

-  "The address is already in use. Binding: 0.0.0.0:2525.". 

-  "Inbound direct trust authentication failed for certificate %1. The source IP address of the server that tried to authenticate to Microsoft Exchange is [%2]. Make sure EdgeSync is running properly."

And Microsoft Exchange Transport Service couldn't start. 

I have noticed that Port 2525 is used by "microsoft.exchange.directory.topologyservice". After stopping it, MS Exchange Service could start and we can send and recive emails. But restarting Windows, "microsoft.exchange.directory.topologyservice" takes Port 2525 again. 

Could you please help to solve this issue? Hope to hear from you very soon.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-25*

Any news on this - i recently had this on EX2016(Windows Server 2016) fully patched.

Is there a fix to prevent this behaviour?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-07*

The same issue happened on my exchange 2016 Version 15.1 (Build 2308.8) from few days ago.

"Failed to start listening (Error: 10048). Binding: 0.0.0.0:2525."

The transport service needs this port for hub transport. 

Recently no hotfix was installed.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-08-25*

Hi Yuki Sun,

Yesterday after reboot, Port 2525 was used by another service, I have found and stopped that service and then i could start Transport service, then I restarted the Windows again, but this time it didn't happen. it happens after 1-2 reboots. 

We have installed Exchange SU Aug V2 directly, V1 was installed, because it was hidden in WSUS Server. I have checked that Microsoft says, if SU Aug V2 is already installed, there is no need to install SU Aug V1. I am not sure, if we needed to install SU Aug V1.

I run the Healthchecker script, everything is green, there is no errors and vulnerabilities.

But I don't know why after some reboots, Port 2525 is used by another service, it happended after SU Aug V2.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-08-25*

Hi @Elvin Mammadov ,

After the reboot, now Port 2525 is used by other service.

I tried running the aforementioned command in my Exchange 2019 environment and Port 2525 is used by "EdgeTransport":  

Aside from the Exchange Transport Service, have you checked the status of the other Exchange services? Can you also run `Test-ServiceHealth` to check the result?  

It happened after the last August update for Exchange Server 2016.

Which version of the Aug SU did you install, V1 or V2? You can run the Exchange Health Checker to see if any additional steps might be needed in your current setup. More information about the Aug SU, you can take a look at the following blog:  

Re-release of August 2023 Exchange Server Security Update packages

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
