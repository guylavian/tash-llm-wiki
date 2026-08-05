---
title: "ADFS 3.0 Customizing Update Password Page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/178000/adfs-3-0-customizing-update-password-page
question_id: 178000
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 3.0 Customizing Update Password Page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/178000/adfs-3-0-customizing-update-password-page (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have to customize the update password page for ADFS 3.0, such that after updating the password, custom message can be added, instead of the default message - "Your Password is successfully updated."  

I have tried updating "expiredNotification" element in the OnLoad.js file, but that is not doing the trick.  

Any pointers are greatly appreciated, as I am not getting any resources over the internet.  

Thanks,  

Amrita

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-03*

Hello Piaudonn,  

I tried to update the expiredNotification again, and it worked, however, in one of the environments, it is not reflecting.  

May be the issue is something else.  

I will check and report my findings...
