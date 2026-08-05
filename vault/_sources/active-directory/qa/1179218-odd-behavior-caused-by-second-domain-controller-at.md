---
title: "Odd behavior caused by second Domain Controller at remote site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179218/odd-behavior-caused-by-second-domain-controller-at
question_id: 1179218
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Odd behavior caused by second Domain Controller at remote site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179218/odd-behavior-caused-by-second-domain-controller-at (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is one for the ages.  I added a second domain controller at a remote site, there had been only one there.  No roles exist on those DC.  The original one there is a 2016 DC.  I added a 2022 DC back in December and let it  just sit there a while, with the anticipation of getting rid of the 2016 when we are ready to upgrade the FSMO role holders at our main site to 2022 as well.  And retire the 2016 boxes.  Our main site has two 2016 DC holding the roles.

Apparently an issue started to reappear unbeknownst to me where old deleted objects started to reappear in AD.  I don't know the details on the objects, but years ago before my time on this network there was a similar issue and a case was opened with Microsoft who determined the problem was having that second domain controller at the remote site, it was demoted and problem solved.  This was when the domain was 2008, pre-recycle bin.  Functional level is now 2016 and sure enough, that second DC was demoted and removed yesterday and the problem solved.

It seems like a bunch of hogwash to me.  How could a second DC cause such an issue?  Has anyone heard of such a problem or something similar?  Thanks for any insights.  I'm not comfortable with a single DC at that location and it makes for upgrading a little bit trickier.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-10*

did this actually post?  i thought i was in the Directory Services forum but looks like it was migrated?  Just not used to a MS question sitting unanswered a whole day people are usually all over them :)
