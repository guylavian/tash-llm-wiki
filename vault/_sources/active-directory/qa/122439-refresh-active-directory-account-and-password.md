---
title: "Refresh Active Directory Account and Password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/122439/refresh-active-directory-account-and-password
question_id: 122439
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Refresh Active Directory Account and Password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/122439/refresh-active-directory-account-and-password (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We migrated a client's domain from 2008R2 to 2016 (we also replaced the hardware).  Because of COVID-19, the commissioning of the new system will be delayed for 6 months.  We will keep the new system running maintained until installation.  How would I "refresh" Active Directory passwords?  As, the "old system" will continue to have users change their passwords every 60 days. The systems are in two disconnected locations.  

Thanks

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2020-10-11*

Not sure what is meant? Sounds like new domain controllers were added then isolated? If the new ones will stay isolated then I'd simply demote the new ones until needed. There's no advantage in keeping them if isolated.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-11*

My suggestion? Don't even have the newer DCs powered on until they are installed in the new location; different password policies on different systems will more than likely cause sync problems between the two sets of systems.
