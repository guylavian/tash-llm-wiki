---
title: "Exchange 2016 receive connector drops connections"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2279821/exchange-2016-receive-connector-drops-connections
question_id: 2279821
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 receive connector drops connections

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2279821/exchange-2016-receive-connector-drops-connections (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there!  

Exchange 2016.  

I've created receive connector (FrontEnd, port: 12825) with "Require TLS" option enabled. TLS-certificate is configured and it's trusted by clients  

While testing I've encountered weird behavior.  

Some applications was able succesfully connect to this connector and succesfully send a messages.  

But one of application - can't. In SMTP receive logs I see "235 2.7.0 Authentication successful", but then "Remote(SocketError)".  

Here is the SMTP-receive log fragment with error (from "Bad application")  

And here is log  with successfully messages sent (from "Good application")

It seems pretty equal, except last string.   

What can cause such behavior?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-29*

What version of TLS is enforced on the 2016 server? Hopefully 1.2 and that the sending server that is failing supports that.
