---
title: "Can I use LDAP lookup on machines removed from AD?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1202509/can-i-use-ldap-lookup-on-machines-removed-from-ad
question_id: 1202509
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["msc-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Can I use LDAP lookup on machines removed from AD?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1202509/can-i-use-ldap-lookup-on-machines-removed-from-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When we get machine back from users we hold them for a period of time. During that time we remove them from AD and SCCM. Someone users need us to access and grab a file or folder off the old machine. Since it is no longer on the domain can we still use the LDAP tool to lookup the local admin password? If not what other options do we have to access the machine or rejoin it to the domain?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-12*

If you haven't deleted the computer object, then you should be able to still read LAPS password for the machine.   This does assume that the local admin password was not change when it was removed from the domain.
