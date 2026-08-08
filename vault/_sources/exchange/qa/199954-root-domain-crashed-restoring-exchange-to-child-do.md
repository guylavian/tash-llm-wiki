---
title: "Root domain crashed. Restoring exchange to child domain possible?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199954/root-domain-crashed-restoring-exchange-to-child-do
question_id: 199954
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Root domain crashed. Restoring exchange to child domain possible?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199954/root-domain-crashed-restoring-exchange-to-child-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Exchange is installed in a Child domain. exchange, child domain and root domain crashed. Root domain cannot be restored since backup is not available. child domain and DC can be restored. whether Exchange can be restored to child domain with root domain freshly built.  

Cheers  

Priya

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-17*

Hi @Priya Jayaraman   ,    

According to my research, the root domain can only be restored through backup. If it cannot be restored, the newly created root domain cannot form a root-child domain environment with the previous child domain. So you could restore the DC, then rebuilt the root-child domain environment, Since most Exchange server settings are stored in Active Directory, you could prepare Schema/AD/AD schema and prerequisites on the child domain, then you could run the /Mode:RecoverServer switch in unattended mode to recover the Exchange server.    

For the specific steps and requirements of recover Exchange server, you can refer to: Recover Exchange servers    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

Agree with AshokM, and if you do not have all the required information for rebuild the server, our DigiScope product will allow you to direct inject/migrate from offline EDB(s) to any production Exchange server  

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-16*

Hi,  

Please find the below suggestions to my knowledge,  

I would suggest to install a new Exchange server once the root domain and child domain are built. If the root domain is newly built, then it will not have any Exchange information and bringing back the same exchange will have issues with communicating to the Active directory. So, in my opinion, build the root domain, restore the child domain, make sure AD replication and domain controllers are healthy. Install new exchange following the pre-requisites, active directory requirements, etc. Create the mailboxes and let the users use the new mailboxes. Create the recovery database, restore the databases from the backup, create the restore requests. Once the restore requests are completed, users will get their data back. Alternatively, if its limited number of users, you can go PST conversion from EDB files using third party tools and import the PST to the user mailboxes.  

If the above suggestion helps, please click on "Accept Answer" and upvote it.
