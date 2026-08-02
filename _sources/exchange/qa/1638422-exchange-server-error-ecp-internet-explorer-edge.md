---
title: "Exchange server error ECP internet explorer Edge"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1638422/exchange-server-error-ecp-internet-explorer-edge
question_id: 1638422
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange server error ECP internet explorer Edge

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1638422/exchange-server-error-ecp-internet-explorer-edge (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Since a few mouths ago i cant open ECP from the browser of my exchange server,  

we have 4 servers the front end with mail transport role cant open ECP by browser, but the other two exchange servers with only database roles opens normally.  

What could it be?  

We have exchange server 2016  

Version 15.1 (Build 2507.6)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-23*

Hello @André Cruz,

I have a few questions for you based on your problem description:

-  Are all four of your servers the same version?

-  Did you do anything (like an update) before you couldn't open the ECP?

-  Apart from the ECP, can you open the OWA page?

-  Have you tried any other browsers to open ECP? is it properly accessible using the server's FQDN?

I have a couple of initial suggestions for your question so far:

1.You can uninstall and reinstall the .msp file by running the update from an administrative command prompt and then restarting the server.

2.Clear your browser cache and cookies. update your browser to the latest version. Or try to visit in no-trace mode.

If the problem persists, feel free to message me and I'll be happy to help!
