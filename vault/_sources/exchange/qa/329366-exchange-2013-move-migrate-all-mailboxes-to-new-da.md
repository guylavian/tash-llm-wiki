---
title: "Exchange 2013 Move/Migrate all mailboxes to new DAG"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/329366/exchange-2013-move-migrate-all-mailboxes-to-new-da
question_id: 329366
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 Move/Migrate all mailboxes to new DAG

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/329366/exchange-2013-move-migrate-all-mailboxes-to-new-da (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

My environment : 3 Exchange 2013 CU23 servers (both CAS + Mailbox roles) in 1 DAG , Windows server 2008 R2 : ex01 , ex02 , ex03 .    

ex01 and ex02 are same hardware configuration.    

ex03 hardware is more powerful then ex01 and ex02    

I'm going to purchase a new server (ex04) with same hardware as server ex03 and I attempt to restructure my Exchange environment : 2 Exchange 2013 CU23 servers (both CAS + Mailbox roles) in 1 DAG , Windows server 2012 R2 : ex03 , ex04    

I do some search:    

-  Exchange 2013 support OS to Window Server 2012 R2    

-  We cannot perform a in-place upgrade of operation system from Windows server 2008 R2 to Windows server 2012 R2 on a server running Exchange 2013    

-  all the servers in the DAG have to be the same O/S    

So I have to Move/Migrate all mailboxes from DAG1 (ex01 , ex02) to DAG2 (ex03 , ex04):    

-  Remove all the databases from Ex03 and remove the server from the current DAG    

-  Rebuild Ex03 with 2012R2    

-  Then create a new DAG with Ex03 and Ex04 running the same O/S and create new databases and replicate them between the 2 servers    

-  Move mailboxes from EX01 and Ex02 to the new servers (03/04) ( including arbitration mailboxes!)    

-  Remove the old databases on 01 and 02 when everything is moved and remove the servers from the old DAG    

-  Remove the old DAG    

I have some concerns :    

-  I have 1000+ mailboxes distributed through 7 databases , hosting email for multiple domains.    

-  I have SAN cert with multiple Subject Alt Names : webmail.mydomain.com , autodiscover.domain1.com , autodiscover.domain2.com ... set up on current DAG    

-  It takes about 2 weeks to move all mailboxes from old DAG to new one.    

-  New DAG and Exchange servers (ex03 , ex04) are same Active Directory domain with old DAG (ex01 , ex02)    

    --> I can setup Virtual Directory URLs , IIS certificate on new DAG same as old DAG, add A record for webmail.mydomain.com , autodiscover.domain1.com , autodiscover.domain2.com ... point to ex03 , ex04 IP addresses also ?  

--> MS Outlook on users computers will connect to new Mailbox servers after Migration Batches complete ? (Because user mailbox's information stored at Active Directory will be updated automatically)    

Users can use email normally when Migration Batches running ? Will they notice any interruptions/downtime ?    

How about arbitration mailboxes ? This is my arbitration mailboxes :    

```
Get-MailboxDatabase | Get-Mailbox -Arbitration | fl Name,ServerName,Database  
          
     Name       : SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}  
     ServerName : ex01  
     Database   : Mailbox Database 1  
          
     Name       : SystemMailbox{1f05a927-38a2-412b-9fd4-3f182479f5f7}  
     ServerName : ex01  
     Database   : Mailbox Database 1  
          
     Name       : SystemMailbox{e0dc1c29-89c3-4034-b678-e6c29d823ed9}  
     ServerName : ex01  
     Database   : Mailbox Database 1  
          
     Name       : Migration.8f3e7716-2011-43e4-96b1-aba62d229136  
     ServerName : ex01  
     Database   : Mailbox Database 1  
          
     Name       : FederatedEmail.4c1f4d8b-8179-4148-93bf-00a95fa1e042  
     ServerName : ex01  
     Database   : Mailbox Database 1
```

Should I move them at first or last after all mailboxes are moved ?    

How about the Recoverable Items folder ? Will it be moved together with mailbox ?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-25*

Hi KyleXu, thanks for your reply.  

So Recoverable Items folder , interruptions/downtime concerns are temporarily put aside .  

About Virtual Directory URLs :

You cannot point one record to two IP addresses

I can do that, for now , webmail.mydomain.com is point to 3 Ex server IP addresses (even so autodiscover.domain1.com , autodiscover.domain2.com ...) , they work fine.

I think I have 3 options here :  

-  Create new DNS record (autodiscover , owa , ews , ecp , oab , activesync ...) for new Exchange servers  

-  Switch DNS from old one to new one right after configuring service URLs for new DAG server  

--> the user has not been moved will use CAS on new Exchange servers (ex3 , ex4) , connect to database on old Exchange servers (ex1 , ex2)  

--> the user has been moved will use CAS and connect to database on new Exchange servers (ex3 , ex4)  

-  Switch DNS record at the last step  

--> the user has been moved will use CAS on old Exchange servers (ex1 , ex2) , connect to database on new Exchange servers (ex3 , ex4)  

--> the user has not been moved will use CAS and connect to database on old Exchange servers (ex1 , ex2)

About arbitration mailboxes , I don't want to recreate them on new Exchange server. As I now there are 5 arbitration mailboxes created by default when installing Exchange first time , 1 mailbox is for generating GAL/OAB , 4 others mailboxes are for other reasons ...  

When installing new Exchange server I won't run "Setup.exe /PrepareAD /IAcceptExchangeServerLicenseTerms" so they won't recreate 5 arbitration mailboxes , so :  

--> If I switch DNS from old one to new one right after configuring service URLs for new DAG server , the user has been moved will use CAS and connect to database on new Exchange servers (ex3 , ex4) --> they don't have GAL/OAB ?  

--> I should switch DNS record at the last step (after all mailboxes are moved , arbitration mailboxes are moved) so the user has been moved will use CAS on old Exchange servers (ex1 , ex2) and they can use GAL/OAB normally ?
