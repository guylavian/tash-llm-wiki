---
title: "Outlook 2019 wont connect to Exchange Server via the WAN"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/272225/outlook-2019-wont-connect-to-exchange-server-via-t
question_id: 272225
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Outlook 2019 wont connect to Exchange Server via the WAN

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/272225/outlook-2019-wont-connect-to-exchange-server-via-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Cannot connect outlook 2019 to Exchange Server via the LAN or WAN.  

I do have a good understanding of Exchange but this one is odd. The Exchange works fine but these two below errors are causing the issue. I just cannot connect outlook. It accepts the user name and password connecting using Auto discovery but just will not complete the final stage and says cannot contact outlook. There must be a certificate issue or DNS problem however this is only happening for a newly connected outlook to exchange server.   

One thing i have noticed is when i do a SRV Lookup using MXToolbox its says DNS Record Published	DNS Record not found. Would this prevent me from connecting to Outlook.  

I'm guessing this is an advanced issue and the person that could only answer this is an advanced Exchange technical person.   

Please help   

Event 2004   

Unable to find the certificate with thumbprint 474EA690EA7D53AC565309AEC2C715C96A87B5B2 in the current computer or the certificate is missing private key. The certificate is needed to sign the outgoing token.  

Event 1009  

The indexing of mailbox database Mailbox Database 1870481387 encountered an unexpected exception. Error details: Microsoft.Exchange.Search.Core.Abstraction.OperationFailedException: The component operation has failed. ---> Microsoft.Exchange.Search.Core.Abstraction.CatalogReseedException: Some of the notifications for database '9db666cb-c07d-451c-86f7-3244e772c684 (Mailbox Database 1870481387)' are missing. Requesting a reseed.  

   at Microsoft.Exchange.Search.Engine.SearchFeedingController.DetermineFeederStateAndStartFeeders()  

   at Microsoft.Exchange.Search.Engine.SearchFeedingController.InternalExecutionStart()  

   at Microsoft.Exchange.Search.Core.Common.Executable.InternalExecutionStart(Object state)  

   --- End of inner exception stack trace ---  

   at Microsoft.Exchange.Search.Core.Common.Executable.EndExecute(IAsyncResult asyncResult)  

   at Microsoft.Exchange.Search.Engine.SearchRootController.ExecuteComplete(IAsyncResult asyncResult)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-19*

Hi JoyZang,  

Thank you very much for that and just to let you know I have followed exactly what you suggested and yes it has corrected the problem !!!! cannot thank you enough as other advice I received did not correct the problem.  

 The odd thing was it said the certificate was there and ok but clearly it wasn't the case plus now the done what you said the thumbprint has changed and i can now connect Outlook from the LAN and WAN with no problems.  

Thanks a million   

Neil

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-16*

Hi Zoy Thanks for the reply.  

I am using exchange 2013   

The odd this is all can access prior to December can access emails via OWA and outlook on the LAN and WAN. The problem arises when you try and connect a  user to a new machine. Indeed i am an administrator and i have installed a clean version of win 10 pro installed outlook but cannot connect to exchange . I can connect using OWA no problem at all. The problem is either a trust issue or like you say a certificate problem.  

No one who is connected to the domain with an account is having a problem as they already have the trust relationship in place.   

I think what will be useful if i send you a copy of the exchange servers application log events, you may be able to determine the exact problem.[68457-application-log-16-02-20221.txt][1]  

do you have an email i could send the application log to please   

i think a new certificate maybe required if this is the case do you have a step by step guide please . See what you think with the application logs , there maybe something you spot that is the cause.
