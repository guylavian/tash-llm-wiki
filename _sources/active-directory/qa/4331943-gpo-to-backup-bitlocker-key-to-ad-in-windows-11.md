---
title: "GPO to backup BitLocker key to AD in Windows 11"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4331943/gpo-to-backup-bitlocker-key-to-ad-in-windows-11
question_id: 4331943
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# GPO to backup BitLocker key to AD in Windows 11

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4331943/gpo-to-backup-bitlocker-key-to-ad-in-windows-11 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey all,

I'm starting a Windows 11 pilot in my enterprise. I've just started and have 5 or 6 Windows 11 machines out there. One of the things we have in place for Windows 10 is the GPO that enables BitLocker, requiring it to back up to AD before encryption. This works great on the Windows 10 machines. We've also tested the key that was created/saved when the device was Windows 10 then upgraded to 11 later. This all works as advertised.

However, the few computers that are imaged Windows 11 are not acting quite the same. Those computers are receiving and applying the same GPO as the Windows 10, except the Key isn't saving to AD. The encryption completes despite the failure to save the key.

Does anyone have an idea why the Windows 11 machines falsely believe the key is backed up to AD?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-07*

Good day Hart-Wolf! I am glad to be able to provide assistance to you today. I would suggest to post this query to our neighbor forum from the link below. They are more oriented on with regards to this type queries/issues and there will be IT Pros/System Admins/Server Admins/AD Admins who are available that will be able to fulfill your query as we are more of home/personal consumer based forum.

https://docs.microsoft.com/en-us/answers/topics...

Regards,

Paul R.
