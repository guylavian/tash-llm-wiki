---
title: "How to Enable or Disable Legacy Exchange Tokens in a Tenant"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2116527/how-to-enable-or-disable-legacy-exchange-tokens-in
question_id: 2116527
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-development-routing-development-other", "office-exchange-online"]
---
# How to Enable or Disable Legacy Exchange Tokens in a Tenant

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2116527/how-to-enable-or-disable-legacy-exchange-tokens-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to disable the legacy Exchange access token in my tenant as part of migrating my add-in to MS Graph. I want to ensure nothing is left using this technology. According to the dev blog post: 

Updates on Deprecating Legacy Exchange Online Tokens for Outlook Add-ins

the development team mentioned there will be a PowerShell tool for this. What kind of tool will it be, and where can it be downloaded?

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-16*

I ran the command to disable exchange tokens, But I still see getCallBackTokenAsync generating tokens. 

```
Set-AuthenticationPolicy –BlockLegacyExchangeTokens -Identity "LegacyExchangeTokens"
```
