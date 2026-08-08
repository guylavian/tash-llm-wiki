---
title: "Removing and adding a URLACL ends with error (ADFS)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1282616/removing-and-adding-a-urlacl-ends-with-error-adfs
question_id: 1282616
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Removing and adding a URLACL ends with error (ADFS)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1282616/removing-and-adding-a-urlacl-ends-with-error-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody,

A customer has a problem with ADFS which we are investigating. The ADFS service runs under a domain account DOMAIN\Sys-ADFS. However, netsh http show urlacl shows reservations for http://+:80/, http://+:443/ and others for an account NT SERVICE\adfssrv.

When we try to remove that via netsh http delete urlacl url=http://+:80/, we get error 2, "the system cannot find the file specified" (translated from german in my own words).

When we try to add it view netsh http add urlacl url=http://+:80/ user=DOMAIN\Sys-ADFS, we get error 183, "a file cannot be created when it already exists".

So, deletion says, it was NOT there, whereas addition says, it was ALREADY there.

Can somebody clarify this?

a) Why can't we neither remove nor add the urlacl?

b) Is there a reason why NT SERVICE\adfssrv is used as the account for the existing urlacl?

Best Regards,

Stefan Falk

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-22*

Hello, is anybody reading here?
