---
title: "Exchange 2016 CU18 - Need to AD prep?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/122808/exchange-2016-cu18-need-to-ad-prep
question_id: 122808
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
---
# Exchange 2016 CU18 - Need to AD prep?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/122808/exchange-2016-cu18-need-to-ad-prep (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,    

I have recently downloaded CU18.  Before installing, I have checked to see if there are any changes.  There are changes to the values in ADSI (objectVersion (Default) and objectVersion (Configuration)).  However, in another microsoft article, it stated no schema changes (https://learn.microsoft.com/en-us/exchange/plan-and-deploy/active-directory/ad-schema-changes?view=exchserver-2016).  Do I need to extend scheme and ADprep for CU18?      

Appreciate if someone can kindly advise me.  Thanks in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-19*

Hi All,  

I have not received any further notifications for my question posted, hence, I have missed out all the replies.  Thanks for the details information and advice given.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-12*

Hi  

Yes, if there are schema changes. If you do not do the AD prep up-front the setup does it for you.  

Just take note that there have been complaints about CU18 and shared mailboxes.
