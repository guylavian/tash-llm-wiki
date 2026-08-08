---
title: "GHOST SID active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1376189/ghost-sid-active-directory
question_id: 1376189
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# GHOST SID active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1376189/ghost-sid-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I instal a windows 10 PC and I use ghost software copy the image form this pc

I use the image to install other pcs and rename their computer name.

Then I add these computers to the domain.Their computers have diffrent computers' names.

What would be the impact of this action？Are there any hidden dangers?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-26*

Hello

Thank you for your question and reaching out.

If you are using same copy of Windows to multiple computers then please add sysprep so that SID will be reset for each new computer.

https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11

--If the reply is helpful, please Upvote and Accept as answer--
