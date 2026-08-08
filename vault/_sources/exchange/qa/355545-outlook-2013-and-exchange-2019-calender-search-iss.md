---
title: "Outlook 2013 and Exchange 2019 calender search issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/355545/outlook-2013-and-exchange-2019-calender-search-iss
question_id: 355545
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Outlook 2013 and Exchange 2019 calender search issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/355545/outlook-2013-and-exchange-2019-calender-search-iss (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

we have a problem with Outlook 2013 (RDS Session, Online Mode) Calendar Search and Exchange 2019 (CU6-CU8 tested).    

Note: Outlook 2013 is currently still necessary due to compatibility with existing applications. Therefore, an OL 2016 or higher cannot be used at this time.    

The search in the calendar works very strangely. When entering search terms (directly in the calendar on the right side of the corner), entries are only displayed to a small extent - many entries are missing.    

If I go through the "advanced search" then all entries will be displayed. See picture (only in german, but show the issue).    

    

It affects all users (20) - no exceptions.    

For me, this would be primarily a question of indexation. That's why we reindexed all mailboxes in Exchange 2019, with no visible success.    

Now my question would be, what else is wrong here? Is the effect known if necessary?    

Thank you for your tips.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-13*

Hello Oliver,  

I've been facing this before.. back then, we found out, that the indexer did not include the path to the .ost file.  

If you have already checked and corrected that, here's a blog article about FAST and WDS, maybe this give's you some hints:  

https://techcommunity.microsoft.com/t5/outlook-global-customer-service/how-outlook-2016-utilizes-exchange-server-2016-fast-search/ba-p/381195  

I hope this helps...  

KR, Alex
