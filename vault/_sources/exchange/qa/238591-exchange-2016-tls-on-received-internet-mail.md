---
title: "Exchange 2016 TLS on received internet mail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/238591/exchange-2016-tls-on-received-internet-mail
question_id: 238591
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 TLS on received internet mail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/238591/exchange-2016-tls-on-received-internet-mail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We have a customer who is having issues receiving email from someone on the internet. They have a single Exchange 2016 server and internet mail is delivered directly to that server (no 3rd part mail service, or other devices in the way like an Edge server).  

This is kind of an out of the box server config, so default receive connectors answering on server.domain.local.  

I was wondering the best way to get TLS working (For those on the internet who are using it) while allowing people not using TLS to keep working.  

As we can't change the name the default connector is answering with, I assume the best bet would be to add a new NIC/IP and create a new receive connector listening on that, leaving the default connector alone. We can then set up TLS on that using a name that matches the 3rd party certificate.  

If anyone has any ideas or can steer me right, that would be great.  

Thanks  

J

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-29*

Thanks for this info (sorry, notifications didn't come through).  

Unfortunately it looks like it is not working for whatever reason. I guess I need to do some more digging in to this to work out why it is failing.  

I did look at the option of adding a second NIC (or IP) and then creating a new connector so I can rename the connector to use the 3rd party cert.  

But I think before going down that road, I need to find out what is causing the problem if it SHOULD work.  

Cheers
