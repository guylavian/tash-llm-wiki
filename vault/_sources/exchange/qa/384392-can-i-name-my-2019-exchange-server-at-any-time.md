---
title: "Can I name my 2019 exchange server at any time?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/384392/can-i-name-my-2019-exchange-server-at-any-time
question_id: 384392
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Can I name my 2019 exchange server at any time?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/384392/can-i-name-my-2019-exchange-server-at-any-time (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I am migrating from Exchange 2013to Exchange 2019.  

Can I run through the install and all migrations and then name my new exchange 2019 the same as the previous exchange 2013 device name?  

So mail1 = 2013, while new exchange is default name...do the install, migration and then rename new exchange mail1.  

Can that be done?  

Or do I have to pick a new mail server name and stick with it?  

We just have a bunch of references to the mail1 name and I'd like to skip finding all the references.  

Thanks in advance.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-05-06*

If this was the first 2019 server, that is expected. Do you really need to reinstall?  

Otherwise, I would bring up a new 2019 server instead with the name you want and move the 2019 arbitration mailboxes to it, then you can remove the first 2019 server  

get-mailbox -arbitration | new-moverequest -targetDB <New2019DB>  

I would not move the 2019 arbitration mailboxes to the 2013 server.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

haha...lets hope...  

so I haven't done anything yet, so lest say I will be leaving the name as is...  

I just tried a few cmds and they don't return anything...  

Get-Mailbox -server New server  

Get Mailbox - database new server database  

Just returns me to the next line, no data at all...is that to be expected?  

I assumed there would be something due to the error....  

Oh, and to get out of the precheck, can I just click teh X in the upper right corner and I'm good?
