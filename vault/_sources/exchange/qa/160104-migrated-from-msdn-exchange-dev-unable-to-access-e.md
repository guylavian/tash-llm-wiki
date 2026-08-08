---
title: "[Migrated from MSDN Exchange Dev] Unable to access Exchange 2016 using Outlook 2016 after moving mailbox from 2010 Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/160104/migrated-from-msdn-exchange-dev-unable-to-access-e
question_id: 160104
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Unable to access Exchange 2016 using Outlook 2016 after moving mailbox from 2010 Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/160104/migrated-from-msdn-exchange-dev-unable-to-access-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

[MSDN thread link]  Unable to access Exchange 2016 using Outlook 2016 after moving mailbox from 2010 Exchange  

We have successfully moved some test users and their Exchange archives from a 2010 Server and Outlook client environment to a new Exchange 2016 Server environment, but we are then unable to use Outlook 2016 to access the mailboxes. Outlook 2010 can still be used to access the mailbox on the new Exchange 2016 Server though. OWA Works fine.  

We have been through a number of troubleshooting documents without success. We have tried changing the authentication types on the Exchange 2016 Servers and virtual directories without success.  

As Outlook 2010 is still working, we think the problem may be with the client.  

Any suggestions. We have tried many  suggested solutions so far!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-12*

Hi,    

What error did you get when failed login outlook 2016 client?    

To verify whether the issue is related to Exchange server or outlook client, check below points    

-  Please create a new mailbox in Exchange 2016 server, then login it with outlook 2016 client.    

-  Try using the ExRCA tool to check the result of Outlook connectivity    

-  Make sure in your Exchange 2010 and 2016 coexistence environment, have virtual directories and DNS records configured properly    

Your DNS records should point to the Exchange 2016 server, and virtual directories in 2010 and 2016 like below    

    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
