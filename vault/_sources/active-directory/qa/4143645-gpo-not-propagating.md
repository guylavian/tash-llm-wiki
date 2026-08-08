---
title: "GPO not propagating"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4143645/gpo-not-propagating
question_id: 4143645
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# GPO not propagating

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4143645/gpo-not-propagating (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I believe I know why but I would like it confirmed because I cannot find any official reference

Inherited AD network and need to convince some admins.

Issue

* Some older GPOs seem to be working but just created a new one in test and it didn't enforce my chosen settings.

Background

* Functional AD level: W2008

* Domain controller: W2012

* Majority of servers: W2016

Troubleshooting

* I created a test OU and linked the GPO there.

* Tried enforcing the GPO to the OU

* RSOP says that the policy applied properly but when I check the local policy, I can change it, disable it.

* I've tried forcing it with gpupdate /force and a restart to no avail

* Tried modifying an existing GPO and it didn't take effect

* Replication is working

* There's no GPO higher in the tree that's overwriting my setting

Yes I know that:

* Domain controllers should ideally be equal or higher than your servers

* Functional level should be at least the level of your most modern DC

Can anyone please confirm or give me a sanity check:  

We need to raise our functional level because its causing issues with GPO inheritance?  Is there a reference that I haven't found?  I want my ammo to convince the admins.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2023-07-26*

H Batsy_Beyond,

I am Dave, I will help you with this.

I apologize, Community is just a consumer forum, due to the scope of your question (AD and Server) can you please post this question to our sister forum on Microsoft Q&A (The System Distractors and IT Pro Forum)

Over there you will have access to a host of AD and Server experts and will get a knowledgeable and quick answer to this question.

https://learn.microsoft.com/en-us/answers/tags/...
