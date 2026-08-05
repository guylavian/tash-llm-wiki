---
title: "Detecting ADFS servcie provider error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/996395/detecting-adfs-servcie-provider-error
question_id: 996395
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Detecting ADFS servcie provider error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/996395/detecting-adfs-servcie-provider-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Recently we enabled a relying party trust with an external service provider. Everything has worked fine up until recently when we encountered an error from the service provider when our SSO users authenticated with ADFS. The users got a token that was passed to the service provider but then we got a 500 error from the service provider.     

We were curious if there's a way the user could be redirected to a static page if they don't get to the service provider site. The error actually occurred after the login happened and we didn't resolve the error via ADFS, the service provider had to resolve it. The site was not offline it just wasn't processing login tokens.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-09-12*

Very hard to tell what's going on without having more data such as the actual request (whether it is in a trace or in the logs).    

When applications are using an SP-Initiated flow, the user will get redirected to the SP after a successful logon even if a token wasn't issued.    

But you can't redirect to different endpoints. It is up to the user agent to follow HTTP POST and HTTP redirect URLs defined in the Relying Party Trust.
