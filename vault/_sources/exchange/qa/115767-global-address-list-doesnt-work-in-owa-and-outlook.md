---
title: "Global Address list doesn't work in OWA and Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/115767/global-address-list-doesnt-work-in-owa-and-outlook
question_id: 115767
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Global Address list doesn't work in OWA and Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/115767/global-address-list-doesnt-work-in-owa-and-outlook (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody,    

I deployed exchange 2016 and everything was properly, after 2 years I'm facing with a problem.    

Global address list doesn't work properly    

1: When I want check (People--> Directory--> All users) it shows your request can't be completed right now. please try again later.    

2:When I want to check my Global address list in outlook I see this error " the operation could not be completed because an offline address book is not available. download a copy of the offline address book."    

I used Update-GlobalAddressList and I had some error but I fixed it however the problem is not solved.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-05*

Why updatding to CU15 rather than the newest CU? I would start with upgrading to CU18 first.    

What's the difference between old and new users?      

Are they in same database?    

Did you manually create GAL with IsDefaultGlobalAddressList to true?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
