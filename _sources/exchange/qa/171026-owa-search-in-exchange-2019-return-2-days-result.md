---
title: "OWA search in exchange 2019 return 2 days result"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/171026/owa-search-in-exchange-2019-return-2-days-result
question_id: 171026
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# OWA search in exchange 2019 return 2 days result

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/171026/owa-search-in-exchange-2019-return-2-days-result (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

there is a new exchnage 2019 which recently our users are migrated to this new server , prblem is that in web mail OWA when search something , it return the result for since 2 days before and the search critira is for all dates.  

I  already reset the windows serach services   

as I google the issue , for older exchange server there was an folder in DB directory which by delete the path search index was rebuilt but for exchange 2019 it is redesign and there no index foldr inside DB directory anymore.  

any suggestion , i have try it on diffrent client and result is same in organization for all.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-23*

Hi @b3hrad   ,  

You mentioned that you have try it on different client, does it include the Outlook client? Do you try to search in cache mode and online mode separately?  

-  Could you see emails from two days ago in OWA?  

-  Please try to select a specific time range to see if you can see all emails in a specific range.  

  

-  Please run the following command to check the database stauts:    Get-MailboxDatabaseCopyStatus | fl contentIndexstate  

4.Please check and restart the Microsoft Exchange Search service and Microsoft Exchange Search Host Controller service.  

5.Please try to migrate users to another new database to see if users can search successfully.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
