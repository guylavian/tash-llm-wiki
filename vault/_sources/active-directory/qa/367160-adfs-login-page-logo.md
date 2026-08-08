---
title: "ADFS login page logo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/367160/adfs-login-page-logo
question_id: 367160
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS login page logo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/367160/adfs-login-page-logo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys,     

I always changed the company logo following this document:    

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/change-the-company-logo-on-the-ad-fs-sign-in-page    

But yesterday running this command Set-AdfsWebTheme -TargetName default -Logo @{path="c:\Contoso\logo.png"} nothing happen also if seems to be executed correctly because no errors  appear on PowerShell.    

Any Idea?     

Thanks :)

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-04-26*

But your cmdLet is targeting the "default" theme where your active theme is "custom".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-14*

Here you are bro!  

Set-AdfsWebTheme -TargetName custome -Logo @{path="c:\CustomWebTheme\logo\logo.png"}

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-04-22*

The command is right and should work right away.  

Maybe you are using a custom webtheme already? You can run  

```
Get-AdfsWebConfig
```

And see what's the active one.
