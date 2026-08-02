---
title: "ADFS authetication error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/277153/adfs-authetication-error
question_id: 277153
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS authetication error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/277153/adfs-authetication-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a site to login with adfs 2019   

I have already created the Relying party trust, but when I try to authenticate I receive this message in the event log  

invalid_response Invalid issuer in the Assertion/Response. Was 'http://adfshom.meusite.com/adfs/services/trust', but expected 'https://adfshom.meusite.com/adfs/services/trust'  

What can I do?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-02-18*

You need to correct the configuration of the application (the relying party). The URI of the ADFS farm is http://<FQDN of the ADFS farm>/adfs/services/trust not with https. It is a URI not a URL. It is just an identifier. There are no endpoint listening being it.
