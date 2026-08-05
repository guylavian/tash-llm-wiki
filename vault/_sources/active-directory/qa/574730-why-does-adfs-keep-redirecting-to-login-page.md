---
title: "Why does ADFS keep redirecting to login page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/574730/why-does-adfs-keep-redirecting-to-login-page
question_id: 574730
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Why does ADFS keep redirecting to login page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/574730/why-does-adfs-keep-redirecting-to-login-page (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The ADFS service account should use the Kerberos AD account property ‘not require pre-authentication’ After setting this, everything worked normally again. Is this a security risk?  

Why do I need to set this property in order to make it work reliably?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-02*

Yes it is a security risk. You should not do it. And, it is very strange that it would fix your problem...  

There are few more or less well known causes for this type of behavior, ranging from certificates misconfiguration (either on the ADFS server itself or on a load balancer device on the front of it) to permissions missing on the service account in AD, to browser configuration issues...  

The starting point is to gather data :)  

-  Can you repro for any users? or just some users?  

-  Is that affecting only FBA authentication? Can it work with SSO for example (when there are no user prompts)?  

-  Do you see failure event in the security logs of your ADFS server and on your DC when it doesn't work?
