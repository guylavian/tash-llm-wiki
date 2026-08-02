---
title: "About IE GPO policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1533944/about-ie-gpo-policy
question_id: 1533944
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# About IE GPO policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1533944/about-ie-gpo-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Computer Policy GPO Management Templates > Windows Components > Internet Explorer ＞Internet Control Panel＞Security Page＞Intranet Zone Items within Allow websites to prompt for information using scripted windows - Prompt for information using scripted windows  

 I would like to ask you about the specifications below.   

-  Is the relevant item a setting that only affects Internet Explorer?   

→Is it also effective for Edge and Chrome?  

 *If you have a website that specifies the specifications or any verification results, it will be helpful.   

-  If it is registered as a trusted site, will it be treated as a valid setting even if it is not configured?  

 *If you have a website that specifies the specifications or any verification results, it will be helpful.  

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-16*

Let me know if you able to solve the issue or not.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-16*

For your first question -This setting does not directly affect Microsoft Edge or Google Chrome. Edge and Chrome have their own security settings and policies, separate from Internet Explorer. Changes made to Internet Explorer's settings won't automatically apply to Edge.

For your second question -If a website is registered as a trusted site, it may override Group Policy-configured security settings, such as the "Allow websites to prompt for information using scripted windows" option. However, this behavior can vary depending on your environment's specific configuration and the policies in place.
