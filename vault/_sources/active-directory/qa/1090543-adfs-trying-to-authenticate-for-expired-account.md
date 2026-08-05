---
title: "ADFS trying to authenticate for expired account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1090543/adfs-trying-to-authenticate-for-expired-account
question_id: 1090543
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS trying to authenticate for expired account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1090543/adfs-trying-to-authenticate-for-expired-account (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

In the logs adfs trying to authenticate for expired account     

Event id : 4625    

I Could see lots login failed attempts for multiple expired accounts     

I’m seeing the logs in the both dc and Adfs server    

These account are not disabled in the AD    

What is this logs denotes and why it’s generating anonymously?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-11-19*

It looks like the account is expired, not disabled.    

Check if the account has an expiration date in AD:
