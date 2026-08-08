---
title: "How to overwrite old GPO's"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/817846/how-to-overwrite-old-gpos
question_id: 817846
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# How to overwrite old GPO's

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/817846/how-to-overwrite-old-gpos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently created a GPO to Lock the computer Screens (Windows Server 2019). We wanted to enforce it for some of the groups we have in our AD, but accidently applied it for authenticated users for alittle bit. We removed the apply permissions for authenticated users and set it to read only. Since then the GPO has been applying for everyone(authenticated users). What is the best solution to undo these settings? Also, what are the next steps? Any help works!

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-04-19*

Setting a policy to "Not configured" means you are not configuring any policy, and so the client settings will remain set to whatever they are currently set to. If you wanted to revert the settings back to defaults you may have to determine what those default settings were, and then create a policy to assign those settings, or in some cases deleting the setting from registry changes an object to "Not configured"  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-19*

@Anonymous   We have the policy enabled for the groups we want. But, the authenticated users have read only access. Is this necessary to give them read only? I read online that you have to so it applies to the groups you want to apply the GPO to. But, when we made the GPO the authenticated users had the "apply group policy" checked at first, so it applied to them (we did not notice that it applied to them). Now we want to revert those changes. What is the best way to do it?
