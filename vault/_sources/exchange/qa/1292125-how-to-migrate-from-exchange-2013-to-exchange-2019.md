---
title: "how to migrate from exchange 2013 to exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1292125/how-to-migrate-from-exchange-2013-to-exchange-2019
question_id: 1292125
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
---
# how to migrate from exchange 2013 to exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1292125/how-to-migrate-from-exchange-2013-to-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

On a un serveur exchange 2013 installé sur windows server 2012 R2, sur un serveur HP ProLiant DL380 Gen9. 

We want to migrate to exchange 2019..

just wanna ask what we need exactly to migrate. prérequis

## Answer (community) — community member

*upvotes: 2 · updated: 2023-05-29*

Hi @SLAMA Nadhem  ，

You can follow the steps below.

-  Make sure your exchange 2013 server is updated to the latest cumulative update (CU23), then download the latest version of exchange 2019 on the new Windows server belonging to the same ad site and install the prerequisites for exchange 2019. Finally, Prepare Active Directory and complete the installation of the exchange 2019 and mailbox role.

-  Next you need to configure the Exchange 2019 URL based on the namespace, configure the automatic discovery SCP for internal clients, configure the 2019 database for the default OAB, configure the Exchange 2019 certificate, and configure the connector.

-  Finally, you can start to migrate your mailboxes, before that you can do some necessary tests. Examples include connecting to archive mailboxes, using public folders, and delegation scenarios. Test Outlook, Free/Busy, Outlook on the web, ActiveSync, Out of Office, and any custom or third-party applications. And after pointing SCP to Exchange 2019, you can move the arbitration mailbox, move the administrator mailbox, and move the mailbox. (Note that before doing any migration operations, please make necessary backups.)

-  Turn off exchange 2013 and monitor for a week - if all good, then perform the uninstallation.

More details can be found in the link below.

Best Practices for Migrating from Exchange Server 2013 to Exchange Server 2019 - Microsoft Community Hub

This link can help you step by step according to your specific needs.

https://setup.microsoft.com/exchange/deployment-assistant

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in [our documentation]](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-29*

You would have to move the mailbox databases and the corresponding logs for each database away from the server (keep the copy somewhere safe, just in case), format, reinstall with Windows 2012 R2 OS, followed by patching with all the outstanding patches, including those for other software deployed on the server (set these options within Windows Update additional settings).

Follow the Exchange Deployment Assistant  to migrate exchange 2013 to exchange 2019.

And Step by guide on Step by Step guide to migrate Exchange 2013 to 2019  for your reference.

Don't skip on the new server to install the latest security updates. 

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.
