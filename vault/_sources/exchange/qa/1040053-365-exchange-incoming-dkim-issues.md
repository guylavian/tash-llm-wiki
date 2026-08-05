---
title: "365 Exchange incoming DKIM issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1040053/365-exchange-incoming-dkim-issues
question_id: 1040053
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# 365 Exchange incoming DKIM issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1040053/365-exchange-incoming-dkim-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My company has an on-prem exchange with DKIM signing configured for multiple tenants.  These emails arrive to Gmail and Outlook.com inboxes with a verified DKIM signature.  However, in 365 exchange when viewing the header for the email, it's reported that DKIM is "None".  It looks like it's completely stripping the DKIM signature.  DKIM is set to relaxed/relaxed. Has anybody run into this issue?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2022-10-08*

How is DKIM applied? An agent on the Exchange Servers or outbound through another hop or 3rd party?    

Is the path the same for all domains? Can you verify that messages to 365 are getting a DKIM sig on the way outbound?

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-07*

Yes, I've searched the entire header and even checked Explorer in the 365 Defender Admin portal.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2022-10-07*

hmmm, havent seen that. the DKIM sig can be stamped in multiple places in a header. I know it sounds stupid, but have you checked the entire header to see if its set elsewhere?

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-07*

I'm talking about incoming DKIM for 365 tenants (separate from our on-prem).  We are an MSP and manage multiple companies.  We have DKIM signing configured for outbound from OUR on-prem exchange.  When the emails arrive at 365 inboxes, it is reported that there is no DKIM when I have verified through multiple other email services that it exists.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2022-10-07*

DKIM signing set where? In 365? If so, then messages sent from the on-prem Exchange Servers to 365 dont go outbound from 365 tenant and wont get a DKIM signature.
