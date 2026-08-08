---
title: "Upgrade From Exchange 2013 To Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/106570/upgrade-from-exchange-2013-to-exchange-2019
question_id: 106570
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Upgrade From Exchange 2013 To Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/106570/upgrade-from-exchange-2013-to-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,  

I'm planning to upgrade our mail system from 2013 to 2019, so I need your help to set a plan to perform this upgrade depend on our existing environment as below :  

1- Domain Server 2012 R2 .  

2 - Exchange 2013 with CU22 (2 Mail Box Server with DAG) .  

3 - 2 Cas Server (With Zen Load Balance ) .  

4 - 1 Archiving Server for mail box.  

so I need your help to perform this upgrade without stopping the existing mail system .

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-27*

Hi Ameen,  

"one server or two server "  

It depends on the number of resources and users, but you can start with one and upgrade your infrastructure. But, I advise you to start with a final infrastructure before making your migrations. This way, you can do the tests (example: high availability) before migrating your users.  

"can i add the exchange servers 2019 on the DAG".  

Good question :) I don't know whith Exchange 2013 but 2016 yes:  

https://support.microsoft.com/fr-fr/help/4488079/exchange-server-2016-allows-adding-exchange-server-2019-mailbox-server  

BUT, I prefer to start with clean installation with new DAG.  

Best  

jmb

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-27*

Thx for your help,  

-For the installation of Exchange 2019, does it need one server or two server (i mean for the role), or just two server and for DAG ?  

-  can i add the exchange servers 2019 on the DAG and copy the Database for the Exchange 2013 then move the mailboxes .  

best regards

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-25*

@Ameen Abu Saif      

Hi,    

In addition to Ashok’s answer,    

-  Exchange 2019 doesn’t support Outlook 2010 or previous versions. Please also check this document for more information in case there are other issues: Exchange Server supportability matrix    

-  You can move the mailboxes directly and don’t need to remove the Exchange 2013 DAG before and after migration.     

-  It is always recommended to backup to avoid data loss before migration.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-24*

Hi,  

-  Verify the active directory forest and domain functional level - minimum windows server 2012 R2  

-  Make sure, CAS servers are also in the same CU22, as the minimum CU required for coexistence is Exchange 2013 CU21 & above  

-  Install the Exchange 2019 latest CU  

-  Configure the certificates, URL's, connectors  

-  Create a test mailbox in Exchange 2019 and test the client connectivity and mail flow (internal/external/exchange 2013)  

-  Point the DNS records to the Exchange 2019 - For load balancer, both exchange 2013 & 2019 can be in the same load balanced namespace  

-  Move the mailboxes in batches  

-  Turn off exchange 2013 and monitor for a week - if all good, then perform the uninstallation  

Please also use the Exchange deployment assistant https://assistants.microsoft.com/  

https://techcommunity.microsoft.com/t5/exchange-team-blog/client-connectivity-in-an-exchange-2016-coexistence-environment/ba-p/603925  

For Archiving server, if its exchange, then archive mailbox can be moved along with the primary mailbox. If this a different product, then please check the supportability with Exchange 2019 and integrate accordingly

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-24*

Hello,  

You can see that:  

https://social.technet.microsoft.com/Forums/office/en-US/282b6f06-8831-4dfd-978a-24540c67dc6d/migrate-exchange-2013-to-2019?forum=Exch2019
