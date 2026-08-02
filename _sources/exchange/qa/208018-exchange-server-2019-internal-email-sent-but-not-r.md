---
title: "Exchange Server 2019: internal email sent but not received"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/208018/exchange-server-2019-internal-email-sent-but-not-r
question_id: 208018
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019: internal email sent but not received

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/208018/exchange-server-2019-internal-email-sent-but-not-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,  

I have just installed Exchange Server 2019 trial for a test in Windows Server 2019 evaluation  

I follow the guide at https://gallery.technet.microsoft.com/Exchange-Server-2019-Step-d6f6fc48  

After installation, I did a test send from local mailbox to another local mailbox in OWA, the email is sent out and saved in sent folder but it's not received in the destination mailbox's inbox.  

Do you know anyway I can fix this?  

Thanks for reading!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2020-12-23*

Hi @David Williams   ，    

Are there any error messages? NDRs or Event logs?    

Have you ever created mail flow rules to forward or reject without notifying anyone?    

And please confirm Exchange services are running normally.    

Please check the events in message tracking log, mail flow status, and queue status in EMS so we can do a further research.     

-  Get-MessageTrackingLog -Sender sender@keyman  .com -Recipient recipient@keyman  .com -Start “StartDate” -End “EndDate”-MessageSubject Subject    

     

If there are any failed events, use this command to see the details.    

Get-MessageTrackingLog -Sender sender@keyman  .com -Recipient recipient@keyman  .com -Start “StartDate” -End “EndDate”-MessageSubject Subject -EventID Failed | FL    

-  Test-MailFlow and check the MailFlowResult and MessageLatencyTime.    

     

-  Get-Queue and check the Status, MessageCount.    

     

Please take a screenshot and share them, and remember to cover your personal information.     

After researched some threads and documents, I found this issue may be related to DNS settings. Add your local DNS IP address to Internal DNS lookups and see if it works.    

-  Make sure your domain local DNS IP (not 127.0.0.1) is set on NIC of exchange server and nslookup is working fine and resolving.    

-  If you have set up secondary DNS IP in the NIC of Exchange server, remove it and restart Microsoft Exchange transport and Frontend transport service.    

-  Configure local DNS server IP on the exchange server’s DNS lookups.    

    a. Login to Exchange Admin Center(EAC), go to servers. Select your server and press edit.  

    b. Select DNS lookups -> Internal DNS lookups ->Custom settings and add your local DNS server IP like this:  

      

Here is a related thread, you can make a reference: Outlook Web App not receiving emails but sends emails    

Regards,    

Louis    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-26*

Hi everyone,  

I found the root cause.  

I checked many times and found that the RecipientStatus contains a SMTP error "501 5.1.4 Recipient address reserved by RFC 2606". In some threads I searched for this error, they said the domain .test (and others) is blocked for receiving email in Exchange Server. I got so surprised for this, and it's more surprised when there is no way to unblock it.  

He he, Microsoft is so special for this :)  

I did reinstall:  

-  The server 1 for Domain Controller and DNS Server 2019  

-  The server 2 for Exchange Server 2019  

-  They joined together in the domain controller.  

-  And certainly with a real .com domain  

and finally it works great. The internal test email is sent and received perfectly.  

I hope this may help someone later to save some time.  

Thanks for your help!  

David

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-25*

Hi ZhengqiLou-MSFT,    

Thanks very much for your help :)    

-  Follow your guide, I found that the Get-MessageTrackingLog command return a list and there are some HAREDIRECTFAIL and FAILED for the source SMTP    

-  The Get-MessageTrackingLog command return some details and the one below is an example:    

-----------------------------------------------------------------------------    

RunspaceId              : 8e1cd3dc-2244-4b1d-96bc-e1d4af6e9aac    

Timestamp               : 12/22/2020 9:28:06 AM    

ClientIp                : 192.168.159.133    

ClientHostname          : server    

ServerIp                : 192.168.159.133    

ServerHostname          : server.mylab.test    

SourceContext           :    

ConnectorId             : Intra-Organization SMTP Send Connector    

Source                  : SMTP    

EventId                 : FAIL    

InternalMessageId       : 25769803777    

MessageId               : <fe26fae9c3d540049a4a50b345fc2257@Naadi  .test>    

NetworkMessageId        : 96b02425-5c46-49d8-6134-08d8a6213736    

Recipients              : {officer2@Naadi  .test}    

RecipientStatus         : {[{LED=501 5.1.4 Recipient address reserved by RFC    

                          2606};{MSG=};{FQDN=server.mylab.test};{IP=192.168.159.133};{LRT=12/22/2020 2:28:06 AM}]}  

TotalBytes              : 8564    

RecipientCount          : 1    

RelatedRecipientAddress :    

Reference               : {<1bfe1f56-bf3a-4eb6-ab38-8b3c9d5fbccb@Testta  .mylab.test>}    

MessageSubject          : just a test    

Sender                  : officer@Naadi  .test    

ReturnPath              : officer@Naadi  .test    

Directionality          : Originating    

TenantId                :    

OriginalClientIp        :    

MessageInfo             : 2020-12-22T02:28:06.079Z;LSRV=server.mylab.test:TOTAL-HUB=0.369|SMR=0.113(SMRDI=0.009|SMRC=0    

                          .103(SMRCL=0.103))|CAT=0.146(CATMS=0.001|CATOS=0.120(CATSM=0.120(CATSM-Malware  

                          Agent=0.117|CATSM-Journal Agent=0.001))|CATRESL=0.001|CATORES=0.016(CATRS=0.016(CATRS-DLP  

                          Policy Agent=0.001|CATRS-Index Routing Agent=0.011))|CATORT=0.004(CATRT=0.004(CATRT-RMS  

                          Encryption Agent=0.002|CATRT-Journal  

                          Agent=0.002)))|UNK=0.001|QDM=0.070|SMSC=0.031(X-SMSDR=0.069)|SMS=0.001  

MessageLatency          :    

MessageLatencyType      : None    

EventData               : {[E2ELatency, 0.701], [ToEntity, Unknown], [FromEntity, Hosted], [MsgRecipCount, 1],    

                          [IncludeInSla, True], [Microsoft.Exchange.Transport.MailRecipient.RequiredTlsAuthLevel,  

                          Opportunistic], [IsSmtpResponseFromExternalServer, False], [DeliveryPriority, Normal],  

                          [AccountForest, mylab.test]}  

TransportTrafficType    : Email    

SchemaVersion           : 15.02.0221.012    

-----------------------------------------------------------------------------    

-  Test-MailFlow return FAILURE    

RunspaceId         : 8e1cd3dc-2244-4b1d-96bc-e1d4af6e9aac    

TestMailflowResult : FAILURE    

MessageLatencyTime : 00:00:00    

IsRemoteTest       : False    

Identity           :    

IsValid            : True    

ObjectState        : New    

-  DNS server is the same as Exchange Server, it can resolve perfect for all records. I also tried to delete MX record but it's still the same    

As you know what may be the root cause for this?
