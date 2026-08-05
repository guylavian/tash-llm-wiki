---
title: "sso login failed due to adfs of ios"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/598656/sso-login-failed-due-to-adfs-of-ios
question_id: 598656
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# sso login failed due to adfs of ios

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/598656/sso-login-failed-due-to-adfs-of-ios (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If you log in to iOS mobile devices or Safari with adfs, secondary authentication will be retracted and will fail.Chrome authentication with Android devices was successful. Android Device and Chrome Authentication Successful

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-25*

Thank you for your answer. I solved this problem.  

Stylesheet by language was the problem. I will now solve this problem.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-22*

I do not fully understand the scenario.  

What does the user experience look like? The user is not presented with a form to authenticate? The use is presented an authentication pop-up? Or does it fails when the user types username and password? Even if the password is correct? What are the error messages on the ADFS server if any? What are the security events generated on ADFS while trying (which would also implies you have enabled audit correctly on ADFS).
