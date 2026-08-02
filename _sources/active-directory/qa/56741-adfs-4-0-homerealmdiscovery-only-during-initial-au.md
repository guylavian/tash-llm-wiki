---
title: "ADFS 4.0 - HomeRealmDiscovery only during initial authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/56741/adfs-4-0-homerealmdiscovery-only-during-initial-au
question_id: 56741
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 4.0 - HomeRealmDiscovery only during initial authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/56741/adfs-4-0-homerealmdiscovery-only-during-initial-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a central ADFS 2016 server, multiple claims providers (all ADFS).  All authentication is handled by the other ADFS servers, nothing is done with the local ActiveDirectory claims provider.  

Current behavior:  Every time a user logs into any application/Relying Party, they are shown the home realm discovery screen.  This occurs every time a user accesses a new relying party, even if they still have an active session with the central ADFS server  This is frustrating.  

Expected behavior:  if a user with an active ADFS session clicks a link to a second RP, the user should not be shown Home Realm Discovery again.  I would expect the initial HRD selection to persist for the duration of the active session only.  

It appears that the HRDCookie could be used, but I would need the HRDCookieLifeTime to be set to less than 1 day - preferably expiring at the end of the user session.  

Can this be done with the ADFS configuration, or do I need to break out my Javascript book and start manipulating cookies with a new webtheme?  

Any ideas?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-04*

I believe the HRD cookie will be created by ADFS if it is the IDP authenticated the user. In your case it seems that the user is authenticated outside of ADFS.  

If users are always coming from the same IDP, you could customized the relying party trust to redirect directly:  

```
Set-AdfsRelyingPartyTrust -TargetName TestApp -ClaimsProviderName @("CustomCP1")
```

I think there is an option to configure how the HRD will work between two ADFS servers (configurable with Set-AdfsclaimsProviderTrust). I'll try to find out more about that if the first suggestion isn't a good fit.
