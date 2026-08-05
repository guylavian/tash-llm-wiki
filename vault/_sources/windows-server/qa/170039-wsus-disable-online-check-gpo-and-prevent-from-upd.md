---
title: "Wsus disable online check gpo and prevent from updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/170039/wsus-disable-online-check-gpo-and-prevent-from-upd
question_id: 170039
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Wsus disable online check gpo and prevent from updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/170039/wsus-disable-online-check-gpo-and-prevent-from-upd (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone  

How to do that:  

All our computers (windows 10) uses WSUS as a default update server and that is ok for us.   

To prevent users from checking online updates when they are outside the company we set gpo :  

-  Computer Configuration/Administrative Templates/System/Internet Communication Management/Internet Communication settings  

Turn off access to all Windows Update features = Enabled  

But crucial for us is to how modify wsus gpo to achieve:  

when user is outside the company then can check updates, download and install(security, important) but not to get and install "big" updates like version updates (1903>recent 20H2)  

thx

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-25*

Hi  

Thx for advice but one question  

If i exclude machine from wsus company policy and  add machine to this policy above  

Does my computer would be allowed to download and install other updates automatically?
