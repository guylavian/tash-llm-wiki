---
title: "Exchange 2016 activeSync Device not showing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/348246/exchange-2016-activesync-device-not-showing
question_id: 348246
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 activeSync Device not showing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/348246/exchange-2016-activesync-device-not-showing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I'm having an issue with mobile devices not connecting to their mailbox. We are on prem, Exchange 2016 CU 20.  

When I run Get-MobileDevice -mailbox xxx, nothing is returned  

When I run get-casmailbox "user", a few mobile devices IDs are in ActiveSyncAllowedDeviceIDs, same devices are in the AD attribute msExchAllowedMobileDeviceIDs.  

So I found an old article saying that the active devices list for a mailbox are saved in the mailbox information and in AD (sorry I lost the URL).  

So I deleted the mobile IDs in AD (cleared msExchAllowedMobileDeviceIDs), and yet they are listed in get-casmailbox "user" | fl ActiveSyncAllowedDeviceIDs, and it is not a DC replication issue, I checked against every DC.  

I'm lost, where are stored those information? How come those attributes are not synced, or how are they synced?  

Thank you in advance!

## Answers

_No answers on this thread._
