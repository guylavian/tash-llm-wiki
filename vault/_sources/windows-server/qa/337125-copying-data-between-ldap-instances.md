---
title: "Copying Data between LDAP instances"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/337125/copying-data-between-ldap-instances
question_id: 337125
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Copying Data between LDAP instances

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/337125/copying-data-between-ldap-instances (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI ,  

I have created LDAP replication between old 2008 server and new 2016 server.  

In new server replica of old server has been installed and due to some issue replication is not working and its been stuck for almost a week and solution is not very handy.  

what if i create a new AD LDS instance in new server and is there a way to copy LDAP data from old server to new without replication?  

LDAP is a new topic for me. so any guidance will be much appreciated.  

thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-06*

Hi,    

Thank you for your reply!    

Based on your descriptions, to restore your AD in your new server, you should actually use full system state backup instead of just adamntds.dit file. You can try to use the steps in the part "Restore Active Directory Domain Controller from a System State Backup" in the article below:    

http://woshub.com/restore-active-directory-dc-from-backup/    

(Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.)    

After you restore your server successfully, you can use the previous replication way that you conducted to see it it works this time.    

Thank you for your patience!    

Best regards    

Joann    

--------------------------------------------------------------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-31*

Hi,    

Thank you for your posting!    

Based on your descriptions, I suggest you can provide me with more details about your failed replication, such as the error code and message, whether you have successfully completed replication but you cannot connect to your replicated data, or you failed to complete LDAP replication itself?    

In addition, you stated that you have tried some solutions to solve your issue but they seems to be not so handy. If it is convenient, can you tell me some more details about the solutions you have tried and why and how you felt they were unreliable?    

The more details you can tell me, the better I can help you. With limited informatin, I can hardly be sure that you can solve your issue if you create a new AD LDS instance in new server and re-replicate data.    

Look forward for your reply!    

Best regards    

Joann    

--------------------------------------------------------------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
