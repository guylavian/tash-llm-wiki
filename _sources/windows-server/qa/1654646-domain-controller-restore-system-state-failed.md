---
title: "Domain controller restore system state failed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1654646/domain-controller-restore-system-state-failed
question_id: 1654646
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain controller restore system state failed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1654646/domain-controller-restore-system-state-failed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,

I have a windows server 2022 (on hyper-v) corrupted and need to restore.

As I have a backup HDD which 1 months ago, I  plug-in and the DC can startup normally. Then I perform the system state restore system state backup on yesterday. The wizard show complete with no error. However, the server cannot startup, even in safe mode or DSRM, it just reboot into recovery interface.

Any idea?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-12*

Hello,

Thank you for posting in Q&A forum.

Failure to start the virtual machine after a successful restore may be caused by the following failures:

-  The network adapter name is inconsistent with the new host

-  The saved state data of the original host and the new host conflict in computer configuration.

It is recommended to refer to the following links: Restored Hyper-V virtual machines won't start - Windows Server | Microsoft Learn

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
