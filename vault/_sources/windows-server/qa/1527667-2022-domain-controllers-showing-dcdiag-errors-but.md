---
title: "2022 domain controllers showing dcdiag errors but replication works"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1527667/2022-domain-controllers-showing-dcdiag-errors-but
question_id: 1527667
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# 2022 domain controllers showing dcdiag errors but replication works

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1527667/2022-domain-controllers-showing-dcdiag-errors-but (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I just built two new 2022 domain controllers and I'm trying to resolve some errors showing in up in DCDIAG tests. Both machines are on the same server in the same virtual environment on the same network with no firewalls between them. Nothing is live yet,  the only use they have even gotten is when I added a user in AD to test replication and it does seem to work just fine, the user shows in up Users and Computers on the second DC quickly. Both servers have proper static IPs, gateway, each pointing to the other as primary DNS and themselves as secondary. I've run numerous REPADMIN test and both servers appear to pass all tests.
The major errors in DCDIAG are 1723, 1726 and 1753, I just can't seem to resolve them. I do get an event error of 4013 (DNS-Server-Service) once per reboot but DNS starts and is running shortly after that error. I've attached the DCDIAG output from DC1, DC2 pretty much shows the same thing.
dcdiag.log

## Answers

_No answers on this thread._
