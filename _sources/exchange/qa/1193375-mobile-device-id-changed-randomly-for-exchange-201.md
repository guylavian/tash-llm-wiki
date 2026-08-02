---
title: "Mobile device ID changed randomly for Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193375/mobile-device-id-changed-randomly-for-exchange-201
question_id: 1193375
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Mobile device ID changed randomly for Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193375/mobile-device-id-changed-randomly-for-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

During the past month, I have encountered users' devices being quarantined by our Exchange 2016 despite it being approved previously for Exchange access. Upon investigation, I observed that the physical device is still the same (tallying the serial number of the physical device against my records), but the device ID in Exchange is different (attached picture as shown).  

All affected users are using Microsoft Outlook on various Android smartphones. As of now, it is time consuming as I have to verify each user's phone physically to make sure that is the same device that I had previously approved.

 s

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-31*

I have confirmed via a support case that this is expected and nobody should rely on device id for access rules. It can and will change and they cannot say how, why, or when. Could be tomorrow, could be years from now. No way to know.

Instead just allow the Outlook device string (at the cost of security!), move to exchange online, or use Hybrid Modern Authentication.

Unbelievable.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-27*

That expected. The Device ID changes with Outlook Mobile:

https://learn.microsoft.com/en-us/exchange/clients/outlook-for-ios-and-android/manage-devices?view=exchserver-2019#device-access-policy
