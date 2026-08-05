---
title: "Newly created Active Directory Users not showing in Exchange Admin Center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194586/newly-created-active-directory-users-not-showing-i
question_id: 2194586
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 7
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Newly created Active Directory Users not showing in Exchange Admin Center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194586/newly-created-active-directory-users-not-showing-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I create an ADuser in active directory, but this user is not found it in the Exchange Admin Center to create a mailbox for this account, after a long time (I cannot determine this time, arround 1-2hour) we can find it in ECP and then create the mailbox ok.

This is the same situation when I enable-remotemailbox for this user for using O365 mailbox, enable-remotemailbox failed because ADuser is not found in Exchange server right after creating ADuser.

We have a hybrid environment with an exchange on-premises and Office 365.

I think there is a problem between AD server and Exchange and causing delay in synchronization

How can i troubleshoot for this case?

Thank

## Answer (community) — community member

*upvotes: 1 · updated: 2023-10-06*

Hello Da HoVan,  

Thank you for posting in Microsoft Community forum.  

I mainly focus on the question or issue related to local AD.  

For the question in this thread, I will give some suggestions from AD side.  

1.How many Domain Controllers are there in your domain? If you have more than one Domain Controller in your AD domain, you can try to check AD replication status after you created new users. If there is no any error within the command result, it means AD replication is OK.  

repadmin /showrepl >C\rep1.txt 

repadmin /replsum >C\rep2.txt 

repadmin /showrepl * /csv >c:\repsum.csv  

Or you can check if this new user is replicated to all other Domain Controllers manually (check on DC one by one if your DCs are not so many).  

2.Whether your Domain Controllers are put in different sites? If so, you can force AD replication after new user was created.  

![](https://learn-attachment.microsoft.com/api/attachments/e2209145-b9fb-4c94-a582-579fb47d0cfa?platform=QnA"https://social.technet.microsoft.com/Forums/office/en-US/55c24c18-364e-44f9-8aa7-d2d2400a233b/new-ad-users-not-immediatly-visible-in-exchange-admin-center" title="social.technet.microsoft.com" rel="ugc nofollow">[56c8-b9eb-b80-96da] (microsoft.com)

Newly created Active Directory Users not showing in Exchange Admin Center - Microsoft Q&A  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-23*

Hello Da HoVan,  

Thank you for your reply.   

Is the problem (Newly created Active Directory Users not showing in Exchange Admin Center) in the original post resolved?  

Is this a new problem (I realize that when the script with cmdlet enable-remotemailbox run as schedule it get the error even it run as administrator) different than the problem in the original post?  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-20*

Hi,

I realize that when the script with cmdlet enable-remotemailbox run as schedule it get the error even it run as administrator. But when run manually it works fine. 

How can i troubleshoot it?

regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-09*

Hello Da HoVan,  

Thank you for your reply.  

You can run commands on PDC.  

repadmin /showrepl >C\rep1.txt

repadmin /replsum >C\rep2.txt

repadmin /showrepl * /csv >c:\repsum.csv  

The replication in our system is having issue because we have 2 sites with 2 AD additional server broken(current status is Tombstones ), other Primary & Additional AD server still work fine, Could this be the cause?  

A: Not sure if the AD replication caused the issue.  

However, you can try to fix the AD replication issue and then check if the issue is related to AD replication.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-07*

Hi,

Thank for your response , I guess so, but how to check the replication successfully before enableing mailbox using powershell command? Because i write automation script for creating ADUser and then active mailbox + assign license O365 for this user after.

Before enabling mailboxes, we need to ensure ADUser is synchronized between AD and Exchange

The replication in our system is having issue because we have 2 sites with 2 AD additional server broken(current status is Tombstones ), other Primary & Additional AD server still work fine, Could this be the cause?

regards,
