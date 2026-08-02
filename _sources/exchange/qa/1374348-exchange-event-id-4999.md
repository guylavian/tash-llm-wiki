---
title: "exchange event ID 4999"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374348/exchange-event-id-4999
question_id: 1374348
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange event ID 4999

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374348/exchange-event-id-4999 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Watson report about to be sent for process id: 11880, with parameters: E12, c-RTL-AMD64, 15.02.1258.025, w3wp#MSExchangeSyncAppPool, MSExchange ActiveSync, Microsoft.Exchange.AirSync.Common.SchemaConverter.Entity.EntityContentProperty.get_MIMEData, UnexpectedCondition:NotImplementedException, 76de, 15.02.1258.025.
ErrorReportingEnabled: False 
exData=|exHResult=|exStacktrace=at Microsoft.Exchange.AirSync.Common.SchemaConverter.Entity.EntityContentProperty.get_MIMEData()
   at Microsoft.Exchange.AirSync.Common.SchemaConverter.AirSync.AirSyncContentProperty.InternalCopyFrom(IProperty sourceProperty)
   at Microsoft.Exchange.AirSync.Common.SchemaConverter.AirSync.AirSyncContent14Property.InternalCopyFrom(IProperty sourceProperty)
   at Microsoft.Exchange.AirSync.Common.SchemaConverter.AirSync.FlexibleSchemaStrategy.ExecuteCopyProperty(IProperty srcProperty, AirSyncProperty dstAirSyncProperty)
   at Microsoft.Exchange.AirSync.Common.SchemaConverter.AirSync.AirSyncDataObject.CopyFrom(IProperty srcRootProperty)
   at Microsoft.Exchange.AirSync.MailboxItemFetchProvider.BuildResponse(XmlNode responseNode)|exTargetSite=MSExchange ActiveSync Microsoft.Exchange.AirSync.Common.SchemaConverter.Entity.EntityContentProperty.get_MIMEData|exSource=|exMessage=|exComplete=
```

I have a three nodes DAG Exchange server system,the version is exchange 2019 CU13, and deploy  latest SU （2023-8-16）,Now ,event viewer report many error of 4999, I donnt know what`s the problem

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-25*

Hi @ 姚黎忠 ，

According to the error message, these id 4999 events are related to ActiveSync.

Are any users complaining about problems with ActiveSync or using Exchange mailboxes on mobile devices?

This error can occur for several reasons, such as corrupted files, misconfigured settings, or incompatible updates.

However, when I query in the post of the security update for August, no other users report similar issues.

Therefore, I recommend that you continue to observe that if no users report problems synchronizing mailboxes with mobile devices, you can ignore this event for now.

Here's a similar discussion for your reference:

Lot of eventID 4999 related to ActiveSync on my Exchange Servers - Microsoft Community Hub

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
