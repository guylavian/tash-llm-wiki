---
title: "When we install Exchange Server 2016 (CU23) but all existing database are dismount. and show error active manager operation failed mapiExceptionNoaccess: unable to mount database"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1274907/when-we-install-exchange-server-2016-cu23-but-all
question_id: 1274907
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# When we install Exchange Server 2016 (CU23) but all existing database are dismount. and show error active manager operation failed mapiExceptionNoaccess: unable to mount database

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1274907/when-we-install-exchange-server-2016-cu23-but-all (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We tried check step and prerequisite everything are work fine and successful and then all database exchange server 2010 SP3 with (Rollup 32) are dismount but we try to mount database again but show error occur active manager operation failed mapiExceptionNoaccess: unable to mount database (hr=0x80070005) and we try to check legacy Exchange 2003/2007 garbage object but not found on adsiedit.msc (Exchange organization) or anything else. please help us to found out more solution.Untitled.png

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2024-10-15*

we try to find out this solution

-  check permission on exchange server database via adsiedit.msc and check inherit default persmission of each database. 

-  verify and check replicate to all DC to another site

-  prepare schema and install exchange server 2016 again and everything are work fine.

hope this help :)

Best Regarsds,

Ronnachai Chintan

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-03*

Hi Ronnachai Chintan,

1.Please try to run IPconfig /all to check whether your DNS is the IP of DC.

2.Please check whether the exchange can communicate with DC normally.

3.Has your exchange2016 been installed normally and can it run successfully?

4.What version is your DC, did anything change to the DC when you installed exchange2016?

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-03*

There can be multiple reasons for this error:

-  Missing transaction log files 

-  Exchange Information Store unable to start 

-  Not enough free disk space on the database or log file volume

-  Exchange “Dirty Shutdown” 

-  Corrupt Exchange Database Files

Also, check this detailed article for help, and let me know if you are able to solve the issue or not - How to resolve unable to mount database (hr=0x80004005, ec=1108)
