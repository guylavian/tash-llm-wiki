---
title: "Can a sketchy Exchange/Outlook user provoke this bounce back message? (let's say they don't have admin privileges)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/328227/can-a-sketchy-exchange-outlook-user-provoke-this-b
question_id: 328227
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Can a sketchy Exchange/Outlook user provoke this bounce back message? (let's say they don't have admin privileges)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/328227/can-a-sketchy-exchange-outlook-user-provoke-this-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys,    

I am currently doing business with a very sketchy individual (who is working for a huge corporation).    

This sketchy situation happened multiple times:    

Let's say that they know I have to send them a very important email just after 5PM. At 4:50PM my colleague sends them an unimportant email and the email reaches them correctly. However, when I get to send my important email at 5:01PM, it bounces back and I get this message:    

    

    

    

Let's say the user doesn't have admin privileges. What's the trick they use to provoke this message within minutes?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-24*

Hi @Stevee Duke   ,    

Well as Andy said, they may did something to fill the mailbox or decrease the quota...after a time like 5:00PM?    

I would think they are using task schedule & some rules to make this.    

It doesn't make sense if they don't mean to do this, but if they only want to reject your emails after a time why they dont use a notification. That's weird.    

Bests,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-23*

Only if they purposely put their own mailbox over the allowed receive quota.
