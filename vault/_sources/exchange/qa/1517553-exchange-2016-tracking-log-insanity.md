---
title: "Exchange 2016 Tracking Log Insanity"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1517553/exchange-2016-tracking-log-insanity
question_id: 1517553
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 Tracking Log Insanity

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1517553/exchange-2016-tracking-log-insanity (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our Exchange Server was recently downgraded from 2010 to 2016.  This is what I'm experiencing when trying to use the terrible tracking logs on 2016:

-  The fields are all wrong according to MS documentation.  "Client-IP" is actually "clientip", "Connector-ID" is actually "connectorid", etc.  Had to find this information from 3rd parties.

-  The clientIP is showing the Exchange server, the "OriginalClientIP" will only show the IP if it doesn't use a custom receive connector.  Why??

-  The connectorID will only show Hubtransport connections, which makes the tracking logs absolutely useless when trying to find the IP of the sender / which exact receive connector it uses.  Why??  Any way to fix this to show the actual frontend used WITHOUT digging through protocol logs?

-  Even weirder is when an outside user sends over TLS/587, the clientIP shows up (horray) but the connectorID shows the default  hubtransport connector that uses port 465.  Why??   Exchange 2010 tracking logs just worked without these freakish anomolies.  Am I doing something wrong here or is this just how it is with Exchange now (broken/useless logging)?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-30*

Hi, I understand your frustration with the changes in tracking Log in Exchange Server 2016 and I did some research, unfortunately, these issues seem to be inherent to the way Exchange Server 2016 handles trace logs. For current detailed information about the tracking log of exchange2016, you could refer to the document Message tracking | Microsoft Learn.
