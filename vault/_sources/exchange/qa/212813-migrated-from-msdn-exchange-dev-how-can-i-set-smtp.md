---
title: "[Migrated from MSDN Exchange Dev]How can I set Smtpreceive log maxage?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/212813/migrated-from-msdn-exchange-dev-how-can-i-set-smtp
question_id: 212813
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# [Migrated from MSDN Exchange Dev]How can I set Smtpreceive log maxage?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/212813/migrated-from-msdn-exchange-dev-how-can-i-set-smtp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/2508cfaf-b11b-400a-9fe4-db57e4d32496/how-can-i-set-smtpreceive-log-maxage?forum=exchangesvrdevelopment  

Hi all  

I am running Exchange 2016.   

I want to save log its path is "c:\program files\microsoft\exchange server\15\transportroles\logs\frontend\protocollog\smtpreceive"  more than 3month.   

How can I set Smtpreceive log maxage? What is the cmdlet?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-29*

Hi,    

You can use the following cmdlet in EMS:    

Set-FrontEndTransportService “Server” -ReceiveProtocolLogMaxAge dd.hh:mm:ss    

     

Note this command only affects Receive connectors of Front End Transport service on Mailbox servers.    

     

And the Parameter “ReceiveProtocolLogMaxAge” is:    

     

And I think this doc will be helpful: Use the Exchange Management Shell to configure the protocol log settings on an Exchange server and more parameters: Set-TransportService.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
