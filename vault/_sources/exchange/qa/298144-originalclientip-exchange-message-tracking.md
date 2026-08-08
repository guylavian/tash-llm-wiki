---
title: "OriginalClientIP Exchange Message Tracking"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/298144/originalclientip-exchange-message-tracking
question_id: 298144
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# OriginalClientIP Exchange Message Tracking

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/298144/originalclientip-exchange-message-tracking (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Before we put our Exchange server behind our F5 Load Balancer, we used to see the original ClientIP in the message tracking logs. But now since the Load Balancer is using NAT we no longer see the client IP. Regarding HTTP / Web we have a solution by using the XFF header within IIS/F5, but the question is can we do something for the SMTP protocol, so that we can also tracking applications that connect via SMTP to send mail?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-07*

The X-forward is not relevant to SMTP, only to IIS/Web.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-04*

See:  

https://dirteam.com/bas/2020/08/24/field-notes-make-the-actual-source-client-ip-visible-for-a-load-balanced-smtp-service/  

https://devcentral.f5.com/s/question/0D51T00006i7YW1/how-to-configure-f5-smtp-vip-to-show-client-ip
