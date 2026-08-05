---
title: "Bitlocker encryption level not syncing with GPO settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3225526/bitlocker-encryption-level-not-syncing-with-gpo-se
question_id: 3225526
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
---
# Bitlocker encryption level not syncing with GPO settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3225526/bitlocker-encryption-level-not-syncing-with-gpo-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a weird issue, it happens with each laptop I deploy when encrypting via Bitlocker. I have set GPO encryption level to XTS-AES 256. 

I have a very simple build for deployment so my process is pull out of box, join to domain, move computer to proper OU, turn on Bitlocker ...and then some other steps.

The issue is that gpresult shows the specific bitlocker GPO is applied to the computer, but each time, every time, the first time I turn on bitlocker for a new computer, it defaults to 128 bit encryption. I have to stop the encryption, and restart it, before
 it takes the XTS-AES 256. I usually do a gpupdate /force and restart also, so I'm not sure if that plays a role in "fixing" or if it's just the fact i have to start the first one, cancel and turn it on again. I'll test that in my next deployment; In my latest
 build before even attempting encryption, I did gpupdate /force 2 times, with 2 restarts, but again still first time turning on bitlocker, only 128 bit encryption.

## Answer (community) — community member

*upvotes: 1 · updated: 2019-07-15*

So, just did a new build out of the box. 

Joined Domain

verified with gpresult that bitlocker policy applied

activated Bitlocker - only 128 bit encryption

stopped activation right away

re-activated, this time shows 256

Why?

also noted that first activation did not show Run Bitlocker system Check, it did ask during second activation.

very strange, what am I missing?
