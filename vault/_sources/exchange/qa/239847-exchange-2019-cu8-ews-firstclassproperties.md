---
title: "Exchange 2019 CU8 - EWS - FirstClassProperties"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/239847/exchange-2019-cu8-ews-firstclassproperties
question_id: 239847
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# Exchange 2019 CU8 - EWS - FirstClassProperties

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/239847/exchange-2019-cu8-ews-firstclassproperties (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

im trying to get exchange email items via EWS. Accessing One Mailbox with "FirstClassProperties" returns "No mailbox with such guid".

If we use a custom property set it just works fine. Any ideas?

THIS ONE - ERROR "No mailbox with such GUID"

$PropSet = New-object Microsoft.Exchange.WebServices.Data.PropertySet([Microsoft.Exchange.WebServices.Data.BasePropertySet]::FirstClassProperties)

$PSItem.Load($PropSet)

THIS ONE WORKS

$PropSet = New-object Microsoft.Exchange.WebServices.Data.PropertySet([Microsoft.Exchange.WebServices.Data.BasePropertySet]::IdOnly, `     [Microsoft.Exchange.WebServices.Data.ItemSchema]::Subject,`  

[Microsoft.Exchange.WebServices.Data.ItemSchema]::Body,  

[Microsoft.Exchange.WebServices.Data.ItemSchema]::Attachments,  

[Microsoft.Exchange.WebServices.Data.ItemSchema]::DateTimeSent,  

[Microsoft.Exchange.WebServices.Data.EmailMessageSchema]::Sender  

)

$PSItem.Load($PropSet)

Maybe anyone has an hint. On another mailbox both are working correctly. (Already recreated the mailbox)

Regards,

Mario

## Answers

_No answers on this thread._
