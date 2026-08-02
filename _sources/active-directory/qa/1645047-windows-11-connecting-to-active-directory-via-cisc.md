---
title: "Windows 11 connecting to Active Directory via Cisco AnyConnect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1645047/windows-11-connecting-to-active-directory-via-cisc
question_id: 1645047
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Windows 11 connecting to Active Directory via Cisco AnyConnect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1645047/windows-11-connecting-to-active-directory-via-cisc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm going to start with the question here and if I need to move this elsewhere, I can.  

We have just started deploying Windows 11.  We have a couple of users that it is working well for, however, just this week two new computers were unable to access their homeshare via our login script.  When I run the set command, the logonserver variable is populated but homedrive and homeshare is not.  Everything works fine in Windows 10 and Windows 7.  The network environment (AD) has not changed, AnyConnect has not changed, just the introduction of Windows 11 (hence the reason I started this discussion in this group).  Has anyone run into anything like this recently?

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2025-02-21*

I ended up needing to switch away from %HOMESHARE% and to \SERVERNAME\SHARE%USERNAME% because Win11 couldn't process %HOMESHARE%.  Win10 handled it just fine though.
