---
title: "Need to get more LDAP event logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195352/need-to-get-more-ldap-event-logs
question_id: 2195352
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Need to get more LDAP event logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195352/need-to-get-more-ldap-event-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to get additional LDAP events created in the event viewer.  Is this URL the correct one to get the information I seek?   AD and LDS diagnostic event logging - Windows Server | Microsoft Learn  We have a timekeeping application that keeps failing every so often (Kronos is the application).  There has been speculation that LDAP is causing this issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-25*

Hi Glen,

Yes, the URL you provided is a good resource for learning about AD and LDS diagnostic event logging in Windows Server. To get additional LDAP events in the event viewer, you can enable diagnostic event logging for LDAP in the Active Directory Domain Services (AD DS) or Active Directory Lightweight Directory Services (AD LDS) instance that you are using. This will allow you to see more detailed information about LDAP operations and potentially help you diagnose the issue with your Kronos application. You can follow the steps outlined in the Microsoft Learn article to enable diagnostic event logging for LDAP.

Best regards

Qiuyang
