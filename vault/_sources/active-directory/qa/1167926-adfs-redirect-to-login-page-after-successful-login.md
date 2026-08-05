---
title: "ADFS Redirect to login page after successful login authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167926/adfs-redirect-to-login-page-after-successful-login
question_id: 1167926
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS Redirect to login page after successful login authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167926/adfs-redirect-to-login-page-after-successful-login (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a ADFS with 2 trusted AD forest, the forest that the ADFS Server belongs to can login and go to the appropriate page, but when enter another user credential at another AD forest, that will redirect to login page, but sometime the problem disappear and exist again after reboot the ADFS Server.

What is the problem?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-07*

Check if the Kerberos Pre-Authentication is failing due to incompatible encryption types:-

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos

Try to configuring these for AES128 AES256 and RC4 and then re-enable pre-authentication on the service account, ADFS login/authentication worked correctly.
