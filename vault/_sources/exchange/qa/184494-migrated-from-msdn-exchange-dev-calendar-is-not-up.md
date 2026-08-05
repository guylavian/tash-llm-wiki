---
title: "[Migrated from MSDN Exchange Dev] Calendar is not updating when in cache mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/184494/migrated-from-msdn-exchange-dev-calendar-is-not-up
question_id: 184494
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Calendar is not updating when in cache mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/184494/migrated-from-msdn-exchange-dev-calendar-is-not-up (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange have been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link] Calendar is not updating when in cache mode  

[Original post]  

Hi   

We have a shared calendar that is used by many users .  

One user is only having the issue that the calendar is not updating when he is in cache mode , when he is online everything updated fine but the problem is that his mailbox is big and that caused performance issue .  

Any idea ?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-22*

Hi Yukisun  

I already created a new profile and set it up for one month and still having the issue .

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-15*

Hi Yukisun   

Yes I tried what you mentioned and still having the same problem .

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-07*

Hi   

Any updates on this ?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-03*

Hi,    

Is this issue only affecting one particular user, while the others who have access to the shared calendar can see the up-to-date calendar?     

If this describes the situation, I'd like to suggest trying to clear the checkbox of "Download shared folders" via File > Account Settings > Account settings > double click the account > More Settings > Advanced  , then restart Outlook and check the result:    

    

If the issue persists, you may consider recreating a new Outlook profile for the problematic user and see if there would be any improvement.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
