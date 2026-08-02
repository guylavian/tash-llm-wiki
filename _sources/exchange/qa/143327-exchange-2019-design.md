---
title: "Exchange 2019 design"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/143327/exchange-2019-design
question_id: 143327
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 design

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/143327/exchange-2019-design (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I upgraded my 2010 Exchange environment to 2019. My 2010 environment had 1 CAS & 2 Mailbox servers setup with a DAG. No Edge server.   

My new Exchange 2019 environment has 2 Mailbox servers with a DAG. There is no Edge server, but I am starting to see that this configuration cannot work without one. Otherwise, if one Mailbox servers goes down, how does traffic get routed to the other Mailbox server. Even with the DAG working correctly, if a reboot my main Mailbox server all internal Outlook clients go offline until the server is back up.  I was hoping to not use an Edge server to keep things very simple.   

I think I made an error in this design, and wonder if someone could point me in the right direction.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

I realized there is an internal DNS A record pointing the hostname of external Exchange URL to internal Exchange1 server. I added another A record with same URL pointing to Exhange2 server & enabled DNS Round Robin. Now I can reboot either Exchange server without Outlook client disconnects.   

I still think I will need the Edge server, though.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-29*

You said Outlook clients go offline, do you mean mail flow stops or mailbox cannot be accessed?    

When you rebooting the mail server, please check if the database that was activated on mail server is mounted on the second server.    

If yes, login to OWA and test if you can open those mailbox (of the database that was activated on mail server)    

If you mean mail flow stops, did you get any NDR message?     

Can you see the message in Sent Items? When searching message tracking log, any event info?    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
