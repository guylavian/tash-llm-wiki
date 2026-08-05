---
title: "Migration from Exchange Server 2010 to Exchange Server 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/223547/migration-from-exchange-server-2010-to-exchange-se
question_id: 223547
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "MicrosoftVendor", "Mvp"]
---
# Migration from Exchange Server 2010 to Exchange Server 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/223547/migration-from-exchange-server-2010-to-exchange-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Good Day!  

May I ask for assistance on how can we upgrade the 2 x Exchange Server 2010 with CAS and MBX, 1 Exchange Server 2010 Edge Transport and it is DAG configured. We will upgrade this to Exchange Server 2013 with CAS and MBX role and we will configure also the DAG.  

Will it be ok if we will not migrate the Exchange Transport Server?  

Thanks in advance for your response.  

Best Regards,  

Raymond

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

Exchange Deployment Assistant tool is the best way for migration:    

https://learn.microsoft.com/en-us/exchange/exchange-deployment-assistant?view=exchserver-2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-18*

Hi All,  

Good Day!  

Sorry for the late response and thank you for your inputs.  

May we ask if there is an impact in exchange 2010 users that not yet migrated once we migrated the other users in Exchange 2013?  

Thanks,  

Raymond

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-11*

Hi anonymous user ,    

Will it be ok if we will not migrate the Exchange Transport Server?    

You don’t have to migrate the transport server.     

Since the Transport Server has been removed in Exchange 2013, the mailbox server includes client access protocols, transport services, mailbox databases, and Unified Messaging services. And the Front End Transport service is contained in CAS.     

    

You can follow the Exchange Deployment Assistant (the URL has been given by Andy) to do the installation and migration. It is a step-by-step guidance; I think it will better help you understand the entire workflow.    

As for the DAG configuration, you can build a new DAG on Exchange 2013 and then migrate mailboxes to the new DAG, this article could be helpful: Migrating an Exchange 2010 DAG to Exchange 2013    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

After you deployed the Exchange 2013 Edge Transport server, you will have to configure the Edge subscription on Exchange 2013 and remove the legacy subscription on Exchange 2010.    

In addition, I want to remind you that the coexistence and deployment should first meet the requirements described in Exchange 2013 system requirements.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-08*

Hi anonymous user     

Lots out there.     

I would start with the Exchange Deply Asst, it will walk you through all the steps    

https://assistants.microsoft.com/    

Also:    

https://practical365.com/ebooks/exchange-server-2010-to-2013-migration-guide/

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-01-08*

Hi anonymous user     

The tags openspecs-* are dedicated to support open specifications. You can find open specifications here: https://learn.microsoft.com/en-us/openspecs/    

Your question is not related to open specifications. For a better chance of getting an answer, I have removed the openspecs-office-exchange tag from your inquiry and have added the office-exchange-server-administration.    

Regards,    

Obaid Farooqi -MSFT
