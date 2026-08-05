---
title: "exchange hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/398385/exchange-hybrid
question_id: 398385
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/398385/exchange-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello:  

I have exchange 2016 and migrating mailboxes to exchange online.  Our MRS proxy(remote hostname) is in DMZ, which has limited bandwidth.  Unfortunately when we move mbx its creating pull connection through DMZ which is creating a bottleneck.  Is there any way to push the mbx traffic from on prem exchange to exchange online rather than exchange online pulling from on prem?  

thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-18*

Hi @det103   ,    

If you use the EAC to move mailboxes, cross-forest moves and onboarding remote move migrations are pull move types because the request is initiated from the target environment. We can't change the working mode of Exchange.    

For more information: Enable the MRS Proxy endpoint for remote moves    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-17*

Sorry, that architecture cant be changed. My only suggestion is not to use a Proxy with hybrid.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-17*

Just to add one more thing.  we have more outbound bandwidth rather than incoming on DMZ section.  So if possible we want to utilize outbound connection to exchange online..
