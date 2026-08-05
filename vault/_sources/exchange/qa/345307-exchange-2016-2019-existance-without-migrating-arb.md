---
title: "Exchange 2016/2019 existance without migrating arbitration mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/345307/exchange-2016-2019-existance-without-migrating-arb
question_id: 345307
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016/2019 existance without migrating arbitration mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/345307/exchange-2016-2019-existance-without-migrating-arb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to test Exchange 2019 functionality and switch back to Exchange 2016 without being dedicated to keeping 2019 online in the event 2019 isn't functioning correctly.    

This would be done by changing port forwarding, internal DNS towards 2019 and then back to 2016.  

Can I do so without migrating the arbitration mailboxes?  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-26*

Thanks for the responses.  

I was able to have my 2019 server live without moving the arbitration mailboxes.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-07*

@Susan Dodds       

Yes, you could keep arbitration mailboxes on Exchange 2016. Here are my lab, I using Exchange 2019 as internet facing server without migrating any arbitration mailboxes to it:    

    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
