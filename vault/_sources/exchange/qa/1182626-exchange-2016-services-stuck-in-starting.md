---
title: "exchange 2016 services stuck in starting"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1182626/exchange-2016-services-stuck-in-starting
question_id: 1182626
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# exchange 2016 services stuck in starting

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1182626/exchange-2016-services-stuck-in-starting (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi dear Expert 

our exchange services stuck in starting and we get below event 

"Process Microsoft.Exchange.Directory.TopologyService.exe (PID=4744) Forest xxx.xx Topology discovery failed, error details 

No Suitable Directory Servers Found in Forest xxx.xx Site Default-First-Site-Name and connected Sites.."

Please give me hand to fix my issue

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-21*

Hi @ramin sa  ，

Any changes were made in the environment right prior to the occurrence of this issue?  

Are there any other potentially relevant event logs recorded together with this one in the event viewer?  

What's the basic topology of your Exchange environment?

Please try adding the `MinSuitableServer` value and see if it can help.   

Reference: Event ID 2142 when Exchange services don't start

-  Locate Microsoft.Exchange.Directory.TopologyService.exe.config File , By Default It Should Be Under "C:\Program Files\Microsoft\Exchange Server\V15\Bin"

-  Open NotePad As Administrator & Then Open Microsoft.Exchange.Directory.TopologyService.exe.config File

-  Locate "Topology MinimumPrefixMatch"

-  Add MinSuitableServer = "1"

-  Save The File & Restart Microsoft Exchange Active Directory Topology Services.  

If the above doesn't work, please try enabling IPV6 on the primary server and check the result.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
