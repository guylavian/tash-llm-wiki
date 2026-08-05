---
title: "MS EXCHANGE 2013 OWA WORKS BUT ECP BLANK PAGE"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/195059/ms-exchange-2013-owa-works-but-ecp-blank-page
question_id: 195059
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# MS EXCHANGE 2013 OWA WORKS BUT ECP BLANK PAGE

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/195059/ms-exchange-2013-owa-works-but-ecp-blank-page (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,  

I am writing regarding a problem I have on my Exchange server 2013 after updating to CU23.  

Owa and outlook work perfectly, but ECP shows blank page after giving username and password.  

I doesnt work with mail link, or internally using localhost on my ClientAcess servers.  

I have two mail role servers and two client access role servers.  

The mail servers have the exchange back end configured and the two ClientAcess servers have default web site configured on IIS.  

I have deleted the ECP virtual directories, and recreated them. I have run UPDATECAS.ps1  

The bindings are good, the same on the two SItes "Default Web site" and  "Exchange Back end"  

There are not any errors on EVENT regarding this except "a fatal alert was received from the remote endpoint 46" I dont know if it is related.  

Can anyone tell me another fix to this problem.  

Thanks in advance   

L.GASHI

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-14*

Hi @luan gashi  ,    

To add to the suggestions provided by AshokM, it's also recommended to test with different browsers like IE or Edge to help eliminate if the issue is related to particular browsers.    

Besides, aside from the UPDATECAS.ps1, you can try running the UpdateConfigFiles.ps1 as well and see how it goes.     

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-13*

Hi,    

Can you check if the "Microsoft Exchange" certificate has been selected on the Exchange Backend website on https 444 binding on both the mailbox servers?    

What happens if you try logging with https://localhost/ecp on the mailbox server?    

Since you have re-created the ECP virtual directory, can you check the authentication are set as the default?    

https://learn.microsoft.com/en-us/exchange/clients/default-virtual-directory-settings?view=exchserver-2019    

Event description which has been mentioned is for source ".NET"  or "Exchange"? If so, could you please share the complete error    

If the above suggestion helps, please click on "Accept Answer" and upvote it
