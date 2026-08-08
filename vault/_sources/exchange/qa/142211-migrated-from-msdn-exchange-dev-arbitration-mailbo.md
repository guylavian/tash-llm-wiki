---
title: "[Migrated from MSDN Exchange Dev]Arbitration mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/142211/migrated-from-msdn-exchange-dev-arbitration-mailbo
question_id: 142211
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Arbitration mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/142211/migrated-from-msdn-exchange-dev-arbitration-mailbo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

Hi Guys,  

I am seeking your advise regarding the Arbitration mailboxes. There are the following Arbitration mailboxes including System mailbox and Federation mailbox in Exchange 2010 in Hybrid environment. I need to delete the databases where arbitration mailboxes reside but I can not move them to different DB due to the following reason (inconsistent state). The databases have no mailboxes except arbitration mailboxes but the size is too big. I wanted to seek your advise that if I dismount the database and delete the large DB file and mount the DB then it will create a vey small DB size file but I do not know the repercussion whether is it safe to do or not. I am not worried about data as i dot not know if there is any data associated with arbitration mailboxes.  

Your expert advise will be highly appreciated.  

Regards  

NAV  

Name                      Alias                ServerName       ProhibitSendQuota  

SystemMailbox{1f05a927... SystemMailbox{1f0... exchange-1           unlimited  

WARNING: The object grammar.local/Users/SystemMailbox{1f05a927-f89d-4056-8e35-b8e90bdc0abf} has been corrupted, and it's in an inconsistent state.  

The following validation errors happened:  

WARNING: Database is mandatory on UserMailbox.  

WARNING: Database is mandatory on UserMailbox.  

FederatedEmail.4c1f4d8... FederatedEmail.4c... exchange-1           1 MB (1,048,576 bytes)  

WARNING: The object grammar.local/Users/FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042 has been corrupted, and it's in an inconsistent state.  

The following validation errors happened:  

WARNING: Database is mandatory on UserMailbox.  

WARNING: Database is mandatory on UserMailbox.  

SystemMailbox{e0dc1c29... SystemMailbox{e0d... exchange-2           unlimited  

Sarwar

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-28*

Hi Sarwar,  

1.According to the information you provide and the test in my lab environment, It’s may caused by your arbitration mailbox pointing to a unmounted or non-existing database.Please check your HomeMDB attribute of your arbitration mailbox in AD. If the HomeMDB attribute is the wrong path or "not set", you can run the following command line to set a correct path.

```
Get-Mailbox -Arbitration | Set-Mailbox -Arbitration -Database "NewDatabase"
```

2.In addition, you could delete the arbitration mailbox, and then run the first command line below to recreate the arbitration mailbox.

```
:\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD
```

Then run the following command lines to enable the mailbox:

```
Enable-Mailbox –Arbitration –Identity “FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042”  
Enable-Mailbox –Arbitration –Identity “SystemMailbox{1f05a927-8668-4003-adad-9b80758e86db}”  
Enable-Mailbox –Arbitration –Identity “SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}”
```

For more information:Exchange Server 2010: Recreate and enable missing arbitration user accounts and mailboxes

It’s should be noted that if the arbitration mailbox is missing in the organization, it will cause unexpected errors. And Exchange server 2010 reached its end of support on October 13, 2020, it's recommend to upgrade your Exchange server to new version.  

For more information Exchange 2010 end of support roadmap

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
