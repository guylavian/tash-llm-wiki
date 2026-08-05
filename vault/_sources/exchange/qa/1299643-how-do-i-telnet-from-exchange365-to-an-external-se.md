---
title: "How do I telnet from Exchange365 to an external server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1299643/how-do-i-telnet-from-exchange365-to-an-external-se
question_id: 1299643
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How do I telnet from Exchange365 to an external server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1299643/how-do-i-telnet-from-exchange365-to-an-external-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am trouble shooting issues with our auto-replies to a specific domain. Here are the details:

-  The domain we send to can receive email from any internal account that are user generated (this is what we want)

-  When a user from the outside domain sends an email to our Exchange365 server, and the receiving account has the Out of Office auto-reply turned on, the auto-reply is sent out from our Exchange365 server... twice. The first response fails immediately, and a second goes out. This second one then sits in the queue as pending, until it fails (length of time varies). When the message fails, it does so without a response from the outside email server, and doing a trace for the email comes up with nothing showing the auto-reply was ever sent.

In working with the outside domain (they have been good to work with thus far) I also tested sending through an email to an account that would fail, and their system reported an NDR to my work account.

In their questioning, they have asked for me to telnet from the Exchange365 server to their server and provide the details of the handshake. I have not found a means to telnet from our Exchange365 server, or find any page that shows what I am being asked to do, with the exception of having an on prem exchange server (we do not have one).

Is it possible to telnet from Exchange 365 to an outside server so I can help those troubleshooting at Yahoo?

Thank you

Ken

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-06-06*

not possible. You do not have direct access to the 365 servers. 

If you are experiencing an issue, then the path forward is to open a ticket with 365 support.
