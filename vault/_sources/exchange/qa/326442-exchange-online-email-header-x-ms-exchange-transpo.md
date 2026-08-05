---
title: "Exchange (online) email header \"X-MS-Exchange-Transport-Forked: True\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/326442/exchange-online-email-header-x-ms-exchange-transpo
question_id: 326442
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange (online) email header "X-MS-Exchange-Transport-Forked: True"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/326442/exchange-online-email-header-x-ms-exchange-transpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hiya!  

At my workplace we mandate that emails are encrypted with SMIME certificates. This is only for internal emails as we are aware many external recipients often have issues opening signed or encrypted emails.  

In passing my manager suggested that I put a mailflow/transport rule in that would enforce this.  

With a lot of trial and error I believe that I got this functioning correctly. Test results below.  

Internal to internal unencrypted - Blocked  

Internal to internal encrypted - allowed  

Internal to internal & external unencrypted - allowed.  

The third scenario was complicated as it became clear that each email was being enumerated against the rules individually rather than collectively. So found it hard to find a condition/exception that allowed me to identify this specific recipient scenario.  

Comparing the headers of the different scenarios the third scenario I noted "X-MS-Exchange-Transport-Forked: True". This is what I eventually ended up using as an exception to my mail blocking rule and appears to be working ok.  

My issue though, is that I am having a hard time locating documentation on specifically what this header is, how it's used, and what the values represent.  

In this instance it appears to mark an email that is sent both internally and to a separate domain, which is what I want... But I want to make sure I fully understand this and am not going to break something down the line.  

TLDR  

What is this header?  

How is it used?  

What do the values represent?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-23*

Hi @zerasar      

According to my search, seems not finding the official document which introduces about the message header X-MS-Exchange-Transport-Forked, and I my previous thread, it's hard to mark the message send to both internal and external recipients. Just like this: Exhange 2010 limiting message size for internal users only    

The rule works fine when a message is sent to internal or external ONLY.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-22*

Forking an email traditionally is the same as bifurcation    

https://learn.microsoft.com/en-us/exchange/mail-flow/mail-routing/recipient-resolution?view=exchserver-2019#bifurcation    

$True, well, seems apparent :) - If the message is forked  - split- bifurcated- two copies created - then I expect to see that set to true.    

in this case, the message was forked ( bifurcated)  between internal and external users.
