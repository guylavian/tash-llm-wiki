---
title: "Domain Controller setting pwdLastSet, Values : 0 at 1AM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1294988/domain-controller-setting-pwdlastset-values-0-at-1
question_id: 1294988
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Domain Controller setting pwdLastSet, Values : 0 at 1AM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1294988/domain-controller-setting-pwdlastset-values-0-at-1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,

It seems at 1AM daily our Domain Controller sets NT AUTHORITY\SYSTEM' Modified Properties : pwdLastSet, Values : 0

Is there a way to disable this or is this just flagged off last set date and it makes users reset on next login automatically?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-02*

Hello there,

This flag on an account may be an indication of a stale account or an account created without a password.

User accounts can be flagged with pwdlastset=0 under three conditions:

Where an account has been created but a password has not been assigned.

Where an account has been created and the administrator has assigned a password but selected the option to change password at next logon.

Where the administrator has selected the option to require a user to change their password at the next logon as part of managing that user’s account, such as after a password reset.

Review accounts where the attribute "pwdlastset" has a zero value https://learn.microsoft.com/en-us/services-hub/health/remediation-steps-ad/review-accounts-whose-attribute-pwdlastset-has-a-zero-value

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–
