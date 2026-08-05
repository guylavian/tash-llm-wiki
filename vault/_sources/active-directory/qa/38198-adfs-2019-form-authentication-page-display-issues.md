---
title: "ADFS 2019 Form authentication page display issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/38198/adfs-2019-form-authentication-page-display-issues
question_id: 38198
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 2019 Form authentication page display issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/38198/adfs-2019-form-authentication-page-display-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI, I deployed ADFS 2019, and everything started to be normal. The form page displayed normally, but I don't know whether anyone has ever encountered this phenomenon after restarting the server. Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-06-23*

What displays the development console in the browser? Maybe you can see that a CSS is missing.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-06-22*

Do you have the same issue in other browsers (just to avoid any cache). Furhter, did you change anything on the theme of ADFS.  

You can check with Powershell  

```
Get-AdfsWebTheme
```

If not set to default, I suggest to change back
