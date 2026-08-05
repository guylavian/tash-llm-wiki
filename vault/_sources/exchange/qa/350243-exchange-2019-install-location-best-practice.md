---
title: "Exchange 2019 install location best practice"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/350243/exchange-2019-install-location-best-practice
question_id: 350243
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 install location best practice

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/350243/exchange-2019-install-location-best-practice (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

New Exchange 2019 install.  

Is it best practice to install Exchange on the C partition or create a new partition?    

What is the recommended capacity for this partition?  

Is there a reason to not store logs and the database on the same partition?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-11*

No, that would be a great solution. ( Main hard drive means database I assume)    

https://learn.microsoft.com/en-us/Exchange/plan-and-deploy/deployment-ref/storage-configuration?redirectedfrom=MSDN&view=exchserver-2019#best-practices-for-supported-storage-configurations

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-11*

Would there be any difficulty if the main virtual hard drive was on a raid 10 and the log virtual hard drive was on a raid 1?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-09*

The C: is perfectly fine. I prefer making it 500GB to account for diagnostic logging and the transport queue.  

The Logs and DB should NOT be on the same volume if this is a stand-alone server.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-09*

The first link gives conflicting answers as to whether installing on the c partition is recommended or not.  

Exchange 2019 is going to be on a Hyper-V vm located on a raid 10 and will all be on that virtual machine with a single virtual hard drive so I am looking at bet practice to partition a single virtual hard drive and install location on that virtual hard drive.  

This will be a exchange 2016/2019 coexistence and then eventually a single exchange 2019 server.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-09*

Hi @Susan Dodds      

Refer to the below thread discussed the similar issue best practice for Exchange installation path:    

Recommendation for Exchange 2016 default installation path    

Intalling on C or on a separate disk are both supported. Make sure you have meet the Exchange Server system requirements    

And Database Log File Best Practices / Microsoft Recommended Configuration    

Exchange Server 2016: Data and log files location    

The official document here introduces about Best practices for supported storage configurations    

Mailbox database and log volume co-location are not recommended in standalone architectures. In high availability architectures, there are two possibilities for this scenario:    

-  Single database per volume    

-  Multiple databases per volume    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
