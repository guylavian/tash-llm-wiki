---
title: "Active directory password - additional policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1653894/active-directory-password-additional-policy
question_id: 1653894
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Active directory password - additional policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1653894/active-directory-password-additional-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!

Can you tell me please, do I understand correctly that, as it was before and is still the case, it is impossible to configure different password policies for PCs and users in the AD domain via group policy (gpmc / gpedit)?

Even if you create a new OU and target it with a new policy with password settings, the new data will be displayed, but will not actually be applied, is that right? And the only working option for creating different password requirements - is FGPP

And what will happen if the “Domain password settings” policy is applied on the domain, indicating the necessary settings, and another policy is applied on the OU with DC, like “Domain Controller password settings”? Which settings will be applied and will there be any difference at all from the second policy for DC?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-10*

Not exactly.

The password policy defined in the Default Domain Policy GPO applies by default to domain accounts and local accounts on domain-joined computers. 

You can modify the password policy of local accounts on domain-joined computers by using GPOs linked to OUs where the domain-joined computers reside.

You can modify the password policy of individual domain accounts by using FGPP

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
