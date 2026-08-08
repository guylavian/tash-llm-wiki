---
title: "member Active Directory direct to Local CMOS Clock"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187878/member-active-directory-direct-to-local-cmos-clock
question_id: 2187878
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# member Active Directory direct to Local CMOS Clock

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187878/member-active-directory-direct-to-local-cmos-clock (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Microsoft,

Currently PDC uses NTP External: for example ntp-dyp.com but DC members use local CMOS which causes DC members to have a different time from the PDC server. How can we make the time on DC members follow the PDC server time?

Here are the member times DC

please help

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-02*

Hello anakPembelajar,

Thank you for posting in Microsoft Community forum.

 You can refer to this similar thread to configure time sync non-PDC (including DCs, other member servers, client machines and workstations.

How do I configure an NTP server in group policy? - Microsoft Q&A

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
