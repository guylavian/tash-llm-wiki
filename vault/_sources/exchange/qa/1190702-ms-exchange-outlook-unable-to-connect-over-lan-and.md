---
title: "MS exchange Outlook unable to connect over LAN and same working with external network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190702/ms-exchange-outlook-unable-to-connect-over-lan-and
question_id: 1190702
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# MS exchange Outlook unable to connect over LAN and same working with external network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190702/ms-exchange-outlook-unable-to-connect-over-lan-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question



## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-20*

Hi @ramesh ,

Let me confirm with you first, are you using Exchange on-prem or Exchange Online? Please try the following suggestions:

-  If you have VPN/proxy/firewall enabled, please disable them and reopen Outlook.

-  Please check if NCSI active probing is disabled. Disabling the NCSI on your computer will trigger the “We are unable to connect right now” error in Microsoft Outlook.

Paste the path below into the address bar of Registry Editor, find the EnableActiveProbing entry and make sure its Value data is set to 1.

“HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\NlaSvc\Parameters\Internet\EnableActiveProbing”  (make sure that you launch the registry editor with admin rights)

 

For reference: "We are unable to connect right now" error when users try to activate Microsoft 365 Apps for enterprise.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
