---
title: "Unable to validate Hybrid Agent for Exchange usage"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/371060/unable-to-validate-hybrid-agent-for-exchange-usage
question_id: 371060
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Unable to validate Hybrid Agent for Exchange usage

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/371060/unable-to-validate-hybrid-agent-for-exchange-usage (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Morning folks,    

I'm having an odd issue with setting up an exchange hybrid configuration between exchange 2010 sp3 and exchange online via the latest version of the Microsoft Hybrid Configuration Wizard:    

    

I have also run a hybrid connectivity test to Microsoft 365 endpoints, and am getting an issue reported when testing against https://nexus.microsoftonline-p.com on port 443:     

    

All advise and direction is welcomed.    

Thanks,    

Mick

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-26*

Thanks for the advised and it has worked to allow the test to successfully complete.    

    

I've ran the Microsoft Hybird Config Wizard again however, I'm still getting the same error.    

Regrettably the error message has no relevant info I can use to trouble shoot in it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-26*

One trick is to force TLS 1.2:    

Can you run this command before performing the  hybrid connectivity test?    

```
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

Also, you have prob seen:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/hybrid-configuration-wizard-errors/the-underlying-connection-was-closed-error

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-26*

Can confirm TLS 1.2 is enabled.  

If it wasn't, the hybrid connectivity test would have reported a TLS error.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-26*

That looks like a TLS issue.  

Have you run through these docs and enabled TLS 1.2?  

https://jaapwesselius.com/2018/10/05/exchange-2010-and-tls-1-2/  

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-tls-guidance-part-1-getting-ready-for-tls-1-2/ba-p/607649
