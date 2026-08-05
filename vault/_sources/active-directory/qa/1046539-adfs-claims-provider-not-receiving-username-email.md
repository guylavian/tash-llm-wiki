---
title: "ADFS Claims Provider not receiving username/email"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1046539/adfs-claims-provider-not-receiving-username-email
question_id: 1046539
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Claims Provider not receiving username/email

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1046539/adfs-claims-provider-not-receiving-username-email (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

GDay,    

I have an on-prem ADFS setup as below with SAML2,    

SP <=> ADFS <=> IDP    

When the SP initiates an authentication, the client can redirect to the IDP (configured as a Claims Provider) and authenticate himself.    

However, I need to pass any form of client identification with the redirection from ADFS to IDP.     

I can receive the NameID in ADFS (from SP => ADFS) but I cannot make the ADFS pass it beyond that to the IDP.    

I've tried setting up a static claims rule on Claims Provider to see if I can pass 'something', but with no success.    

```
=> issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Value = "******@company.com");
```

How do I get this working? I desperately need this for the SSO to work on my IDP side.     

I'm ok with any sort of method/hacks/claim rule whatsoever.    

Cheers.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2022-10-20*

You will need to following rules:    

-  On your IDP, a rule that sends to AD FS the Username and the Email address    

-  On AD FS:    

-  On the Claim Provider Trust for your IDP, you need to create a rule that passes through the Username and the Email address claims  

-  On the Relying Party Trust you need to create a rule that passes through the Username and the Email address claims  

The exact rules will depend on what you have configured on your IDP. If you know what your IDP is sending, we can help you creating all the pass-through rules.
