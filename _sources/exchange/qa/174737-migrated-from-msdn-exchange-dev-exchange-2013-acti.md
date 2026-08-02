---
title: "[Migrated from MSDN Exchange Dev] Exchange 2013 active sync mobile phones information"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/174737/migrated-from-msdn-exchange-dev-exchange-2013-acti
question_id: 174737
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Exchange 2013 active sync mobile phones information

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/174737/migrated-from-msdn-exchange-dev-exchange-2013-acti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/aeda5579-0b78-40e2-a74f-43967875ef02/exchange-2013-active-sync-mobile-phones-information?forum=exchangesvrdevelopment   

On a on premise Exchange 2013 active sync is enabled. When we open a mailbox for a user and look at the phones tab we see the devices which have connected to exchange mailbox.  

When we look at the details there is information of the model and type of device (which in my opinion is not exactly what it is like the device name.  

The thing is there is a deviceid in the details of the phones but that number does not correspondent with the serial or imei of the Ipone in this case. Not with any Iphone it is corresponding.  

How can we now identify which phone is the phone the user at this moment has in sync because several users have more smartphones with activ sync so the date of sync is not enough?  

When we want to wipe a phone we must have the right phone to wipe...  

freddie

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-25*

Based on the official document, device IDs are not governed by any physical device ID. So we cannot identify mobile devices from device IDs. It's mentioned here: Device access policy.    

    

If your on-premises Exchange users use Outlook for mobile app, yes, the DeviceModel, DeviceType and UserAgent will be the same for iOS and Android. However, based on my knowledge, the most convenient way for us is to check the Last successful sync to identify. We can login and send an email from one device to check if the Last successful sync is updated immediately.     

If your users also use other native apps, we can identify easily with DeviceModel, DeviceType and UserAgent.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
