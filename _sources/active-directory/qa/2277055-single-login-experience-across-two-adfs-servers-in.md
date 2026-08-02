---
title: "Single Login Experience Across Two ADFS Servers in Different Organisations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2277055/single-login-experience-across-two-adfs-servers-in
question_id: 2277055
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Single Login Experience Across Two ADFS Servers in Different Organisations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2277055/single-login-experience-across-two-adfs-servers-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm setting up a self-hosted SharePoint environment that authenticates through our primary ADFS server (ADFS-A). Some users need to authenticate using credentials from a partner organisation's ADFS server (ADFS-B).

My goal is to configure the authentication flow so users only see ONE login page (the ADFS-A page), even when they're using ADFS-B credentials. I want to avoid users being redirected to the ADFS-B login page.

Currently, users are being bounced from the ADFS-A login screen to the ADFS-B login screen in an infinite loop, which breaks the login process. I need ADFS-A to handle the authentication with ADFS-B behind the scenes.

I've tried configuring Home Realm Discovery and various federation trust settings without success.

In short, Is it possible to configure ADFS-A to proxy authentication to ADFS-B without showing the ADFS-B login page to end users? If so, what's the recommended approach?

Thanks in advance.

## Answers

_No answers on this thread._
