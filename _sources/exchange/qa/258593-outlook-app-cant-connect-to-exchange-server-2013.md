---
title: "Outlook app can't connect to exchange server 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/258593/outlook-app-cant-connect-to-exchange-server-2013
question_id: 258593
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Outlook app can't connect to exchange server 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/258593/outlook-app-cant-connect-to-exchange-server-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I get this error in outlook app connection to your mail server timed out But i use gmail app it work fine i also have used the test tool from microsoft testconnectivity.microsoft.com and the test show Exchange ActiveSync was tested successfully So i am not sure what the problem is?

## Answer (community) — community member

*upvotes: 1 · updated: 2021-06-25*

Same issue here. Adroid native email app connects to new exchange 2013 CU23 install without issue but the outlook for mobile app on the same device fails to connect to server.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-31*

I'm having the EXACT same issue. The Gmail app works right away and the Outlook app throws a time out. That is, when trying to add an account. And since you cannot create an account, the troubleshooting steps as described in troubleshoot-activesync-with-exchange-server are in vain - there's nothing logged.    

As for those troubleshooting steps; I tried them anyway, but I get stuck on EASInspectorFiddler. I downloaded the file, but it doesn't contain any .dll file. Furthermore, the document says "Configure the ActiveSync device to use this workstation as a proxy server" but I don't have a clue how to do that?    

To me it looks like there's something wrong with the Outlook app. And troubleshooting is pretty painful, so I hope there's a simple fix?    

Simon
