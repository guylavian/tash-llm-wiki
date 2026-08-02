---
title: "[Migrated from MSDN Exchange Dev]Clean up Exchange server after migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/139097/migrated-from-msdn-exchange-dev-clean-up-exchange
question_id: 139097
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Clean up Exchange server after migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/139097/migrated-from-msdn-exchange-dev-clean-up-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.  

We migrated Exchange 2010 from Domain A to a new Exchange 2016 server in Domain B, then decommissioned the Exchange 2010 server according to a guide I found on a TechNet forum. There's a 2 way trust so Domain A users can use the Exchange server in Domain B. I'm still finding some remnants of Exchange in Domain A AD that I would like to clean up if I can including:  

Microsoft Exchange System Objects  

Microsoft Exchange Security Groups  

Can all of the msExch... attributes be removed from user objects and the 'showInAddressBoox' which causes an error when copying users if it's not blank.  

Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

Hi ,    

What do you mean by the copy user error?    

-  If you have completely deactivated Exchange 2010, you can delete the remaining "Microsoft Exchange System Objects" and "Microsoft Exchange System Groups" of Exchange 2010 through ADSI.    

Use ADSI, connect to “Default Naming Context”, navigate to the following objects and Delete them:    

DC=Domain,DC=Com -> OU=Microsoft Exchange Security Groups    

DC=Domain,DC=Com -> CN=Microsoft Exchange System Objects    

-  Regarding the attributes of the user object, I want to confirm with you what your specific migration process is like? Now your environment is that Exchange 2010 has been completely decommissioned, and all mailboxes have been migrated to the new Exchange 2016. But are the AD users associated with these mailboxes still in Domain A?    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
