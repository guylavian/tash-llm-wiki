---
title: "Configure ADFS with Oracle WEBLogic"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/373405/configure-adfs-with-oracle-weblogic
question_id: 373405
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Configure ADFS with Oracle WEBLogic

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/373405/configure-adfs-with-oracle-weblogic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A necessary premise: I don't know oracle weblogic because I inherited the system and I'm studying it    

In my work environment I have to do a test to understand if it is possible to access external users to an application based on web logic.    

I tried a little to find out about but honestly I got lost.    

My architecture is as follows:    

1 server DC W2k12     

1 server 3ADFS  W2k12    

1 server weblogic     

In the image below weblogic config

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-13*

This worked for me:

https://weberheinz.com/2023/02/13/weblogic-sso-with-microsoft-adfs/

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-27*

That's not really an ADFS question (yet). Application configuration is specific for the app.
