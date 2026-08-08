---
title: "security policy in domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1035188/security-policy-in-domain-controller
question_id: 1035188
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# security policy in domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1035188/security-policy-in-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

how can Using group policy when putting pc to network to not allow local user access to desktop except for user join domain, and when disconnect the network allows local users to connect to the desktop??

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-05*

Yes, I mean when the PC is connected to the corporate network, you can log in using a user (domain) only and prevent the local user from logging in, and when you disconnect the PC from the corporate network, you can log in to a device using the local user.    

my question is can a policy or script be used to do this?
