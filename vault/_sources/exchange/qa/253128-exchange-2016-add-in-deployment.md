---
title: "Exchange 2016 Add-in deployment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/253128/exchange-2016-add-in-deployment
question_id: 253128
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Add-in deployment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/253128/exchange-2016-add-in-deployment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

When I trying to add a add-in in Exchange 2016 CU7 ECP through the XML file I get an error like below:  

error  

Method not found: 'Microsoft.Exchange.WebServices.Data.GetClientExtensionResponse Microsoft.Exchange.WebServices.Data.ExchangeService.GetClientExtension(Microsoft.Exchange.WebServices.Data.StringList, Boolean, Boolean, System.String, Microsoft.Exchange.WebServices.Data.StringList, Microsoft.Exchange.WebServices.Data.StringList, Boolean, Boolean)'.  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-03*

Hi,  

I don't have "Web Services Managed API" on my server. I installed "Web Services Managed API 2.2" but nothing changed.  

Also there is no releated error log in Event log, I just find information log.  

Current User: 'S-1-5-21-957102307-2811433378-2019603151-500'  

Exchange Control Panel finished an Async web request in the thread 16.  

Command: 'GetList_PreLoad'

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-02*

Do you have Exchange Web Services Managed API installed on your exchange server? Try to uninstall and reboot.    

CU7 is too old, would you update to latest CU?    

Can you find any related error in Event Log?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
