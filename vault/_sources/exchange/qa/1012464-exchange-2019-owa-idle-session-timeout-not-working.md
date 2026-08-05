---
title: "Exchange 2019 OWA idle session timeout not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1012464/exchange-2019-owa-idle-session-timeout-not-working
question_id: 1012464
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Exchange 2019 OWA idle session timeout not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1012464/exchange-2019-owa-idle-session-timeout-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I have a problem in exchange 2019 on-premise environement. I configure owa session timeout using bellow methods but none of them not working at all.    

1- Set-OrganizationConfig -ActivityBasedAuthenticationTimeoutInterval 00:5:00    

2- Some regisistery key in server    

any solution?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-19*

The Set-OrganizationConfig cmdlet is used to set the Activity-Based Authentication Timeout for OWA. For detailed syntax, see the TechNet article Set-OrganizationConfig.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-09-18*

Hi Hossein,    

Can you check if you have enabled it via this command?    

```
Get-OrganizationConfig | Fl -ActivityBasedAuthentication*
```

If not set it to Enabled  `set-OrganizationConfig -ActivityBasedAuthenticationTimeoutEnabled $true`    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
