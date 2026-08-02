---
title: "Exchange 2019 Visual C++ prerequisite"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289515/exchange-2019-visual-c-prerequisite
question_id: 1289515
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2019 Visual C++ prerequisite

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289515/exchange-2019-visual-c-prerequisite (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We will soon be migrating our on-prem Exchange servers from 2019. I see that Visual C++ 2012 and 2013 are prerequisites for the install. We've recently removed 2012 from all of our servers because it is end of life. Does Exchange 2019 really require VC++ 2012 or can we install a newer version instead? If it is still required for the install can it be removed after Exchange is installed?

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-23*

Hi Kenny Stern,

I do not recommend that you remove Visual C++ 2012, the correct VC version will affect the use of some Exchange functions, especially preparing Active Directory when installing and updating requires the correct version of VC to avoid unexpected errors.

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2019

Best Regards,

Dezhi

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation](https://aka.ms/msftqanotifications)"https://aka.ms/msftqanotifications)") to enable e-mail notifications if you want to receive the related email notification for this thread.
