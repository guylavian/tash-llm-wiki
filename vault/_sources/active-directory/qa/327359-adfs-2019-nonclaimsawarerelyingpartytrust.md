---
title: "ADFS 2019 NonClaimsAwareRelyingPartyTrust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327359/adfs-2019-nonclaimsawarerelyingpartytrust
question_id: 327359
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 2019 NonClaimsAwareRelyingPartyTrust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327359/adfs-2019-nonclaimsawarerelyingpartytrust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are currently having a problem accessing NonClaimsAware RelyingPartyTrust. We publish TFS externally and receive many error messages from event 12027 on the ADFS server. Only that the password or the username is not wrong! Access then also works, but before that access is very often denied. I suspect that the error is to be found in some temporal relationship between TGT and tokens from ADFS. Does anyone know such behavior? MfG Marcel

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-10*

Similar issue here, was there ever a resolution found?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-26*

I am using ADFS 2019. The WAPS are a domain member. The delegation to the WAP computer accounts contains the HTTP SPN's of the Sharepoint server. A HA proxy (passthrough) is used as a load balancher between the WAPs and ADFS. All servers are in the same domain. The configuration works 90%  

This is the event that I get:  

Web Application Proxy encountered an unexpected error while processing the request.  

Error: The user name or password is incorrect.  

 (0x8007052e)  

I have only noticed these errors since I connected my adfs to a syslog server. before i had thought that users really entered their passwords incorrectly. But that is definitely wrong - users enter their password correctly  

Marcel
