---
title: "Removing dead Server 2003 Exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2751312/removing-dead-server-2003-exchange-server
question_id: 2751312
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Removing dead Server 2003 Exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2751312/removing-dead-server-2003-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a 2010 Exchange server that I am prepping to migrate to new 2016 exchange, when running the install for 2016 I got the following message.

"

Error:

One or more servers in the existing organization are running Exchange 2000 Server or Exchange Server 2003. Installation can't proceed until all Exchange 2000 or Exchange 2003 servers are removed.

For more information, visit: http://technet.microsoft.com/library(EXCHG.150)/ms.exch.setupreadiness.Exchange2000or2003PresentInOrg.asp

I did read the articles about deleting the object in ADSIEdit but I guess I just need to confirm is there any other way to verify that this server was properly decommissioned before I delete the object, I was told it was uninstalled and physically removed
 from the racks, mind you I am inheriting this environment with very little knowledge of how things were promoted and demoted here.

Also when deleting the object I noticed I have an Exchange Administrative Group as well as a First Administrative Group, should I delete the entire First Administrative Group since it contains just the old 2003 exchange server.

Thank you

## Answers

_No answers on this thread._
