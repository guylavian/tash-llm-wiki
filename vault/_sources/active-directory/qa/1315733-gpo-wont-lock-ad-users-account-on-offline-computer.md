---
title: "GPO won't lock AD users' account on offline computer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1315733/gpo-wont-lock-ad-users-account-on-offline-computer
question_id: 1315733
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# GPO won't lock AD users' account on offline computer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1315733/gpo-wont-lock-ad-users-account-on-offline-computer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,  

I want to lock any AD users' account after XX invalid logon attempts, on offline computer.  

For that, I declared a laptop in an OU, and I applied this GPO:  

Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies > Account Lockout Policy

-  Reset account lockout counter after: 10 min  

-  Account lockout threshold: 10 invalid logon  

-  Account lockout duration: 30min  

The GPO state is applied and active in the Group Policy strategy, furthermore it appears in the local security policy settings in the Laptop.

Nevertheless, it seems to apply on local users' account only and not on AD users' account and that online or offline.

Did I miss something or it's impossible as is?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-23*

Hello

Thank you for your question and reaching out.

Only GPOs that are connected to the domain's root are permitted to contain your default account lockout policy. The majority of people advise incorporating it into your default domain policy.

Add the settings to your default domain policy or make a new policy at the domain root and add them there if you don't already have an account lockout policy linked to the domain root.

There can only be one GPO per domain that has an impact on account lockouts. Multiple GPOs at different OU levels are not permitted. (That's where fine-grained password policies and group policy preferences come into play, but that's a different discussion.

--If the reply is helpful, please Upvote and Accept as answer--
