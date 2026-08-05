---
title: "[Migrated from MSDN Exchange Dev]STOREDRV.Deliver.Exception:MessageSubmissionExceededException.MapiExceptionMaxSubmissionExceeded"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/134852/migrated-from-msdn-exchange-dev-storedrv-deliver-e
question_id: 134852
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]STOREDRV.Deliver.Exception:MessageSubmissionExceededException.MapiExceptionMaxSubmissionExceeded

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/134852/migrated-from-msdn-exchange-dev-storedrv-deliver-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.

There is a mixed Exchange 2016 + 2019. User2016 sends a collection update to multiple users, including one located at Exch2019. The collection update contains various attachments, the total volume of which is far from the specified limits. Sometimes everything goes well, sometimes the sender receives an NDR from user2019:

```
Возникла проблема в работе почтового ящика получателя. Попробуйте отправить сообщение еще раз. Если проблема возникнет снова, обратитесь к своему администратору электронной почты.
```

The messagetrackinglog contains the following information:

RunspaceId : fd7aa30d-e181-4e38-9596-1fcebce885db  

Timestamp : 07.10.2020 19:27:20  

ClientIp :  

ClientHostname : EXCH003  

ServerIp :  

ServerHostname :  

SourceContext : 08D8648A8359CDFE;2020-10-07T16:27:19.546Z  

ConnectorId :  

Source : STOREDRIVER  

EventId : DELIVERFAIL  

InternalMessageId : 5613522257399  

MessageId : <966589f34fc64df393093159f7b2cd94@keyman  .ru>  

NetworkMessageId : dba64124-8586-4350-42a0-08d86addd4d3  

Recipients : {user2019@keyman  .ru}  

RecipientStatus : {STOREDRV.Deliver.Exception:MessageSubmissionExceededException.MapiExceptionMaxSubmissionExceeded; Failed to process message due to a permanent exception with message Cannot save changes made to an item to store. 16.55847:E9000000, 17.43559:000000006C01000000000000  

0000000000000000, 20.52176:020F93820400401080030400, 20.50032:020F93827417401080030400, 0.35180:80030400, 255.23226:80030400, 255.27962:0A000000, 255.27962:25000000, 255.17082:DA040000, 0.27745:D41C0000, 4.21921:DA040000, 255.27962:FA000000, 255.1494:00000000, 5.59  

176:000000194C696D69746174696F6E001005000780, 5.34600:1722872843757272656E7453697A65000F010480, 1.49178:C182C000, 1.42792:00000000, 4.45082:DA040000, 1.63016:25000000, 4.39640:DA040000, 8.45434:9B6A1E3D7D67184FACAC19343DBFFFCC66312D61, 5.10786:0000000031352E30322E3  

03635392E3030343A532D4E534B30312D455843483030333A62373335383938362D636238342D343463362D393266312D6139393662643436623261610000000000, 255.1750:80030400, 255.31418:80030400, 0.22753:80030400, 255.21817:DA040000, 0.17361:80030400, 4.19665:DA040000, 0.37632:80030400, 4  

.37888:DA040000 [Stage: OnCreatedEvent][Agent: Meeting Message Processing Agent][DestinationFolder: ][DestinationFolderId: LgAAAACXVORnK2sDSKu+4/7o5d1oAQCgq0ueOiyzRbx7Xopzj0T3AAAAAAEMAAAB]}  

TotalBytes : 12846608  

RecipientCount : 1  

RelatedRecipientAddress :  

Reference :  

MessageSubject : Заседание + Материалы во вложении.  

Sender : user2016@keyman  .ru  

ReturnPath : user2016@keyman  .ru  

Directionality : Originating  

TenantId :  

OriginalClientIp :  

MessageInfo : 2020-10-07T16:27:05.907Z;SRV=exch-14.domain.local:TOTAL-SUB=0.524|SA=0.048|MTSS-PEN=0.477(MTSSD-PEN=0.477(MTSSDA=0.004|MTSSDC=0.396|SDSSO-PEN=0.045 (SMSC=0.008|MTSSDM-PEN=0.036)));SRV=EXCH003.domain.local:TOTAL-DEL=1.111|SMR=0.172(SMRDI=0.172)|D-PEN=0.938  

(SDDSINI=0.023|SDDSPCR=0.085(SDDCC=0.085)|SDDSPCS=0.003(SDDOS=0.002)|SDDPM=0.081(SDDPM-Conversations Processing Agent=0.033|SDDPM-Mailbox Rules Agent=0.002|SDDPM-Meeting Message Processing Agent=0.002|SDDPM-Index Delivery Agent=0.041)|SDDSCMG=0.359(SDDCMM=0.002)|SD  

DCM=0.383(SDDCM-Meeting Message Processing Agent-INC=0.383))  

MessageLatency :  

MessageLatencyType : None  

EventData : {[E2ELatency, 14.578], [DeliveryPriority, Low], [PrioritizationReason, AMS:12689884/1048576|ARC:83/500], [AccountForest, domain.local]}  

TransportTrafficType : Email  

SchemaVersion : 15.02.0659.004

RunspaceId : fd7aa30d-e181-4e38-9596-1fcebce885db  

Timestamp : 07.10.2020 19:27:20  

ClientIp : 172.18.97.33  

ClientHostname : EXCH003  

ServerIp : 172.18.97.33  

ServerHostname : EXCH003.domain.local  

SourceContext :  

ConnectorId : Intra-Organization SMTP Send Connector  

Source : SMTP  

EventId : FAIL  

InternalMessageId : 5613522257399  

MessageId : <966589f34fc64df393093159f7b2cd94@keyman  .ru>  

NetworkMessageId : dba64124-8586-4350-42a0-08d86addd4d3  

Recipients : {user2019@keyman  .ru}  

RecipientStatus : {[{LED=554 5.2.0 STOREDRV.Deliver.Exception:MessageSubmissionExceededException.MapiExceptionMaxSubmissionExceeded; Failed to process message due to a permanent exception with message Cannot save changes made to an item to store. 16.55847:E9000000, 17.43559:00000000  

6C010000000000000000000000000000, 20.52176:020F93820400401080030400, 20.50032:020F93827417401080030400, 0.35180:80030400, 255.23226:80030400, 255.27962:0A000000, 255.27962:25000000, 255.17082:DA040000, 0.27745:D41C0000, 4.21921:DA040000, 255.27962:FA000000, 255.149  

4:00000000, 5.59176:000000194C696D69746174696F6E001005000780, 5.34600:1722872843757272656E7453697A65000F010480, 1.49178:C182C000, 1.42792:00000000, 4.45082:DA040000, 1.63016:25000000, 4.39640:DA040000, 8.45434:9B6A1E3D7D67184FACAC19343DBFFFCC66312D61, 5.10786:00000  

00031352E30322E303635392E3030343A532D4E534B30312D455843483030333A62373335383938362D636238342D343463362D393266312D6139393662643436623261610000000000, 255.1750:80030400, 255.31418:80030400, 0.22753:80030400, 255.21817:DA040000, 0.17361:80030400, 4.19665:DA040000, 0.3  

7632:80030400, 4.37888:DA040000 [Stage: OnCreatedEvent][Agent: Meeting Message Processing Agent]};{MSG=};{FQDN=EXCH003.domain.local};{IP=172.18.97.33};{LRT=07.10.2020 16:27:19}]}  

TotalBytes : 12846608  

RecipientCount : 1  

RelatedRecipientAddress :  

Reference : {<22954c5f-3b39-468c-b4ad-a699c496db85@EXCH003.domain.local>}  

MessageSubject : Заседание + Материалы во вложении.  

Sender : user2016@keyman  .ru  

ReturnPath : user2016@keyman  .ru  

Directionality : Originating  

TenantId :  

OriginalClientIp :  

MessageInfo : 2020-10-07T16:27:05.907Z;LSRV=EXCH003.domain.local:TOTAL-HUB=5.117|SMR=3.938(SMRDI=3.723|SMRC=0.214(SMRCL=0.214|X-SMRCR=0.209))|CAT=0.003(CATRESL=0.001)|UNK=0.034|QDM=0.005|SMSC=0.013(X-SMSDR=0.005)|SMS=1.115(SMSMBXD=0.966)  

MessageLatency :  

MessageLatencyType : None  

EventData : {[E2ELatency, 14.588], [ToEntity, Unknown], [FromEntity, Hosted], [MsgRecipCount, 43], [IncludeInSla, False], [SlaExclusionReason, AccMsgSizeThresholdExceeded], [Microsoft.Exchange.Transport.MailRecipient.RequiredTlsAuthLevel, Opportunistic], [IsSmtpResponseFromExt  

ernalServer, False], [DeliveryPriority, Low], [PrioritizationReason, AMS:12689884/1048576|ARC:83/500], [AccountForest, domain.local]}  

TransportTrafficType : Email  

SchemaVersion : 15.02.0659.004

For user2019@keyman  .ru:

-  no inbox rules

-  no delegates

-  the mailbox moved to another database

-  check mailbox for error

-  DestinationFolderId: LgAAAACXVORnK2sDSKu+4/7o5d1oAQCgq0ueOiyzRbx7Xopzj0T3AAAAAAEMAAAB from error is "Inbox" folder

-  no other problem with mailbox

All limits set to 50Mb

Quotas:

```
[PS] C:\Windows\system32>Get-MailboxStatistics ******@domain.ru |fl *  

DeletedItemCount                               : 20725  
ItemCount                                      : 18084  
TotalDeletedItemSize                           : 3.118 GB (3,348,028,809 bytes)  
TotalItemSize                                  : 11.32 GB (12,153,100,324 bytes)  

[PS] C:\Windows\system32>Get-Mailbox ******@domain.ru |fl *quo*  

ProhibitSendQuota            : Unlimited  
ProhibitSendReceiveQuota     : Unlimited  
RecoverableItemsQuota        : 30 GB (32,212,254,720 bytes)  
RecoverableItemsWarningQuota : 20 GB (21,474,836,480 bytes)  
CalendarLoggingQuota         : 6 GB (6,442,450,944 bytes)  
UseDatabaseQuotaDefaults     : True  
IssueWarningQuota            : Unlimited  
RulesQuota                   : 256 KB (262,144 bytes)  
ArchiveQuota                 : 100 GB (107,374,182,400 bytes)  
ArchiveWarningQuota          : 90 GB (96,636,764,160 bytes)
```

Dumpster:

```
[PS] C:\Windows\system32>Get-MailboxFolderStatistics -identity ******@domain.ru -folderscope recoverableitems |ft -a identity, foldersize, FolderAndSubfolderSize, ItemsInFolderAndSubfolders, DeletedItemsInFolderAndSubfolders, DeletedItemsInFolder, ItemsInFolder  

Identity                         FolderSize                     FolderAndSubfolderSize         ItemsInFolderAndSubfolders DeletedItemsInFolderAndSubfolders DeletedItemsInFolder ItemsInFolder  
--------                         ----------                     ----------------------         -------------------------- --------------------------------- -------------------- -------------  
******@domain.ru\Recoverable Items 0 B (0 bytes)                  3.118 GB (3,348,028,809 bytes)                      20728                                 0                    0             0  
******@domain.ru\Calendar Logging  81.9 MB (85,875,166 bytes)     81.9 MB (85,875,166 bytes)                            883                                 0                    0           883  
******@domain.ru\Deletions         3.038 GB (3,262,153,643 bytes) 3.038 GB (3,262,153,643 bytes)                      19845                                 0                    0         19845  
******@domain.ru\Purges            0 B (0 bytes)                  0 B (0 bytes)                                           0                                 0                    0             0  
******@domain.ru\Versions          0 B (0 bytes)                  0 B (0 bytes)                                           0
```

Limit on mailbox level increased:

```
[PS] C:\Windows\system32>Get-Mailbox ******@domain.ru |fl *maxrec*  

MaxReceiveSize : 100 MB (104,857,600 bytes)
```

at the moment of error Warning in Application log

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Problem only for some users on Exchange 2019 (not one).  

Users use outlook client.  

-  NDR message dont contain any information about error. The error is visible in messagetrackinglog  

-  It can be seen from the messagetrackinglogs that no transport rules apply to this message.  

-  All limits are set to 50Mb  

-  From messagetracking: TotalBytes : 12846608 This is much less than the maximum value 50Mb.  

-  The error occurs during the delivery phase to Exchange. Outlook it has nothing to do with it  

-  "ProhibitSendQuota", "ProhibitSendReceiveQuota" and "IssueWarningQuota" on Database are set to 29Gb, 30Gb, 28Gb

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Hi,  

Does this problem occur to only one user?  

Did you send and receive email by Outlook client?  

1.In the DNR email you received, is there have common enhanced status codes? If possible, please share with us, but please pay attention to covering your personal information.  

2.Please check if there have any related transport rules in your Exchange server.  

3.All the limits you mentioned are 50M, referring to organizational limits, connector limits? If you have not checked, please run the following command line to check.

```
Get-TransportConfig | ft MaxSendSize, MaxReceiveSize  
Get-SendConnector | ft Name, MaxMessageSize  
Get-ReceiveConnector | ft Name, MaxmessageSize
```

4.Based on my knowledge, For any message size limit, you need to set a value that's larger than the actual size you want enforced. This accounts for the Base64 encoding of attachments and other binary data. Base64 encoding increases the size of the message by approximately 33%, so the value you specify should be approximately 33% larger than the actual message size you want enforced. So please try to set up a lager limit and restart the Microsoft Exchange information store service. Then send a test email again. Please note that restart the Microsoft Exchange information store service could it may affect the actual use of users, so please restart when no one is using it.  

For more information: Types of message size limits  

5.Outlook limits the total size of attachments to 20MB. So please make sure that the size of attachments and emails you send are smaller than your settings.  

For more information: Attachment size exceeds the allowable limit error when you add a large attachment to an email message in Outlook  

6.I noticed that the values of "ProhibitSendQuota", "ProhibitSendReceiveQuota" and "IssueWarningQuota" of Exchange 2019 user mailboxes are all Umlimited. Does this mailbox use the default configuration of the database where it is located? Please check the size of the mailbox to confirm whether the mailbox still has qutoa。

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
