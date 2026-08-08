---
title: "Exchange queues confusion"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/150019/exchange-queues-confusion
question_id: 150019
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange queues confusion

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/150019/exchange-queues-confusion (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in the process of replacing our Exchange 2013 server with a 2016 one. The server is purely a transport server, no mailboxes are stored on there as all of our accounts are Office 365. All we need it for is to pass messages from things like scan to email, SQL report email and for our web server to be able to send email to internal and external recipients.  

Everything is working fine, however I am a little confused by how the servers are handling messages addressed to external recipients. If I scan a document and email it to an external address I can see it hit the new Exchange server because that's what the source is pointing to, but then it sends some messages to the old server which then either sends it back to the new one or sends it out. Messages sent back to the new server then get sent out.  

Why are they doing this and how can I get it to route everything out via the new server?  

I can't just switch off the old server, we have some SQL queries that are hard coded to send to the old servers IP address, these are being worked on to update where they are sent to but this is going to take some time to complete.  

To reiterate, messages can be seen routing to the new server, they are then sent to the old server which either bounces them back to the new server or sends them to the external recipient. Messages sent back to the new server are then sent to the recipient. There does not seem to be any pattern to which ones are bounced around, I sent multiple emails from a printer to the same gmail address, some passed through the new server and out, others bounced to the old server then out while the remainder went to the new server, old server, new server and out.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-03*

Both servers were listed as sources on the send connector. I have now removed the old one. Thank you for the information
