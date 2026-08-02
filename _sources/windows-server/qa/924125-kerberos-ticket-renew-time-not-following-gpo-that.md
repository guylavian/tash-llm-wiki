---
title: "kerberos ticket renew time not following GPO that should set it to 7 days"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/924125/kerberos-ticket-renew-time-not-following-gpo-that
question_id: 924125
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# kerberos ticket renew time not following GPO that should set it to 7 days

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/924125/kerberos-ticket-renew-time-not-following-gpo-that (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

It came to my attention that klist on our AD-joined machines has the same end time, as the renew time:    

Start Time: 7/12/2022 7:58:16 (local)    

End Time: 7/12/2022 17:58:16 (local)    

Renew Time: 7/12/2022 17:58:16 (local)    

However, in our Default Domain Policy, we have the usual defaults set: 10 hours for the "Maximum lifetime for user ticket" value, and 7 days for the "Maximum lifetime for user ticket renewal" value. There are no other kerberos policies in our domain that I know of, and running gpresult and rsop, does not show kerberos related settings settings.    

As a test, I tried changing the renewal time to 8 days, and the end time to 9 hours in the Default Domain Policy, just to see if that change would appear. It did not; they're still set to 10 hours.    

I need to figure out why all my clients don't have the "renew time" set to 7 days from now, as the GPO is telling them to.    

I only found 2 other threads about this, and none of them have answers. Except for me, it's even worse because every single of one of the workstations I've checked (both Windows Server 2016, and Windows 10) has the same problem with the end time, and renew time, both being set to 10 hours.    

https://social.technet.microsoft.com/Forums/windows/en-US/a14bcdbb-4f30-4866-a7e4-db3862532dbe/kerberos-maximum-lifetime-for-user-ticket-renewal-not-being-applied?forum=winserverGP    

https://social.technet.microsoft.com/Forums/office/en-US/cde9406a-37b6-4328-abd7-b5d30f3450da/kerberos-tgt-ticket-renewuntil-time-set-to-same-as-end-time?forum=winserversecurity

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-16*

Found the solution. I was blocking inheritance into my Domain Controller OU because I previously had a half dozen random GPOs linked at the root, and I didn't want them applying to the DCs. I've done cleanup since then and now, and now I am back to only having the DDP linked at the root. So I figured it was now safe to remove the "Block Inheritance" checkbox from the Domain Controller OU.

On a hunch, I did a klist purge, then gave myself a new ticket. Now my renew date is 7 days, exactly as it is defined in the DDP.

Hope this might help other people.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-13*

hi. sorry, this is not related to bitlocker at all. this is about kerberos tickets.
