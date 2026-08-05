---
title: "Exchange active sync device info"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/174813/exchange-active-sync-device-info
question_id: 174813
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange active sync device info

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/174813/exchange-active-sync-device-info (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On a on premise Exchange 2013 active sync is enabled. When we open a mailbox for a user and look at the phones tab we see the devices which have connected to exchange mailbox.  

When we look at the details there is information of the model and type of device (which in my opinion is not exactly what it is like the device name.  

The thing is there is a deviceid in the details of the phones but that number does not correspondent with the serial or imei of the Ipone in this case. Not with any Iphone it is corresponding.  

How can we now identify which phone is the phone the user at this moment has in sync because several users have more smartphones with activ sync so the date of sync is not enough?  

When we want to wipe a phone we must have the right phone to wipe...

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-11-25*

You want to use Get-MobileDeviceStatistics    

https://learn.microsoft.com/en-us/powershell/module/exchange/get-mobiledevicestatistics?view=exchange-ps    

Thats the way you tell which devices are synced and the last sync time. That's all you can really check     

```
Get-MobileDeviceStatistics -Mailbox TonySmith
```
