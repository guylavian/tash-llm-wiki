---
title: "Exchange online protection Anti-spam policy can't be whitelisted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1512103/exchange-online-protection-anti-spam-policy-cant-b
question_id: 1512103
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange online protection Anti-spam policy can't be whitelisted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1512103/exchange-online-protection-anti-spam-policy-cant-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If you use Exchange online protection, you have no ability to whitelist Emails or domains that Microsoft tags "High confidence phishing message action."  The option is here: https://security.microsoft.com/antispam
What online protection solutions are available if you don't want an Email blocked?
Are there other services available that allow you to configure what is blocked and not blocked?
Scenario: Someone uses icloud for their Emails and wants to send you a picture.  But because there is a lot of phishing on icloud, Microsoft forces all those Emails redirected to one emails address, which may be junk, the system admin, or nowhere.  Not only do you NOT get the Email, the best case is that the junk Email, which you probably don't have access to, is monitored and they forward you the Email someday.  You can't whitelist and get these Emails in the future because although there is on option to whitelist, it does not permit whitelisting of domains that Mircosoft Defender deems bad.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-01-25*

Your best option here is to submit it as a false positive as an admin:
https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/submissions-admin?view=o365-worldwide#report-good-email-to-microsoft
