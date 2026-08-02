---
title: "How to configure Kerberos Authentication in Browser"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/706207/how-to-configure-kerberos-authentication-in-browse
question_id: 706207
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# How to configure Kerberos Authentication in Browser

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/706207/how-to-configure-kerberos-authentication-in-browse (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am aware as to how to configure but to do so in every Workstation IE / Chrome or any browser would be very laborious and waste of time. Is there any GPO which would configure the same rather then going to individual PCs and configuring. ?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-24*

Hello ManishChawda  

You can find the policy at:  

Userconfiguration> Preferences > Control Panel Settings > Internet Settings > enable Integrated Windows Authentication  

In this case, the port is removed, as the system will enable the authentication for the IP/domain independantly from which port the traffic is inbound/outbound.  

--If the reply is helpful, please Upvote and Accept as answer--
