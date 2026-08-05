---
title: "Exchange Server 2016 Not receiving emails from \"@us.af.mil\" or other military email addresses"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/289343/exchange-server-2016-not-receiving-emails-from-@us
question_id: 289343
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server 2016 Not receiving emails from "@us.af.mil" or other military email addresses

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/289343/exchange-server-2016-not-receiving-emails-from-@us (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, My business uses an On-Prem Exchange Server 2016 on Windows Server 2016 for email. Some of our users are in regular communication with the branches of the US military. Recently, one of our users noticed that we aren't receiving email from military email addresses. Other users have confirmed this suspicion. There are no issues with email delivery with any other email hosting providers such as gmail. Any help would be greatly appreciated

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-26*

Hi,    

Which log of receive connector did you check? It should be Default Frontend <ServerName> or the one if you created to replace Default Frontend.    

If you can't find any clues in Message tracking log and Protocol log, and it's not rejected by firewall, you should contact the sender side to confirm if the message is sending succesfully.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-25*

So that's the key point. If those messages arent making it to you, then its up to the sender to prove your org accepted it in their logs.  

if a NDR exists, then even better.  

Having said all that, does Exchange accept mail directly from the internet or is there a SMTP gateway that accepts it first, then routes to Exchange?
