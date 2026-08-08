---
title: "Exchange 2013 - upgrade OS to Window Server 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/322079/exchange-2013-upgrade-os-to-window-server-2012-r2
question_id: 322079
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 - upgrade OS to Window Server 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/322079/exchange-2013-upgrade-os-to-window-server-2012-r2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

My environment : 3 Exchange 2013 CU23 servers (both CAS + Mailbox roles) in 1 DAG , Windows server 2008 R2 : ex01 , ex02 , ex03 .  

ex01 and ex02 are same hardware configuration.  

ex03 hardware is more powerful then ex01 and ex02  

I'm going to purchase a new server (ex04) with same hardware as server ex03 and I attempt to restructure my Exchange environment : 2 Exchange 2013 CU23 servers (both CAS + Mailbox roles) in 1 DAG , Windows server 2012 R2 : ex03 , ex04  

I do some search:  

-  Exchange 2013 support OS to Window Server 2012 R2  

-  We cannot perform a in-place upgrade of operation system from Windows server 2008 R2 to Windows server 2012 R2 on a server running Exchange 2013  

So here my plan :  

-  Install Windows server 2012 R2 and Exchange server 2013 CU23 on new server ex04  

-  Join ex04 into DAG --> DAG has 4 members : ex01 , ex02 , ex03 (Windows server 2008 R2) and ex04 (Windows server 2012 R2)  

-  Let ex04 holds all mailbox databases (mount/active copies) , remain ex servers hold passive copies  

-  Remove all mailbox databases copies from ex01 , ex02 , ex03  

-  Remove ex01 , ex02 , ex03 from DAG , decommission them  

-  Install Windows server 2012 R2 and Exchange 2013 CU23 on ex03 , join it to DAG again, add mailbox databases copies to ex03 ...  

But I concern about step 2 : I remember that I read somewhere Exchange 2013 DAG must be running the same operating system ?  

Please give me some advice , thank you very much.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-24*

Hi @Jack Chuong  ,    

But I concern about step 2 : I remember that I read somewhere Exchange 2013 DAG must be running the same operating system ?    

Based on my research, yes, each DAG member must be running the same operating system. Here are some similar links for your reference:    

DAG with different OS versions    

Can I have an Exch2016 DAG with mixed OS versions?    

Then as in this thread we are mainly discussing about the diffrent OS version of DAG members as indicated by the initial post and it has been resolved in Andy's reply, I'd recommend accecpting his post as answer to close this up. Then for your new questions about the specific concerns when moving the mailboxes, it would be best if you try to open up a new thread for it. In this way, it will make answer searching in the forum easier and be beneficial to other community members as well. Thanks for your understanding.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-22*

Hi AndyDavid, thank you for your reply  

As your suggest what I have to do is Move/Migrate all mailboxes from DAG1 (ex01 , ex02) to DAG2 (ex03 , ex04)  

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
