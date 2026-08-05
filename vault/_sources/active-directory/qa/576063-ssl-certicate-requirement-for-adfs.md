---
title: "SSL Certicate requirement for ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/576063/ssl-certicate-requirement-for-adfs
question_id: 576063
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# SSL Certicate requirement for ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/576063/ssl-certicate-requirement-for-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I am completely a beginner at ADFS setup and have deployment queries.    

We have a single Active Directory environment(Abc.com). in this environment, we have users whose logon Names are of different Suffixes like user@jaswant  .com/ user@xyz  .com /etc. Deploying One Adfs farm with 2 ADFS servers and there are 2 Web application proxy servers deployed to forward requests to ADFS servers. Application is hosted outside the network then users will log in with their email addresses.    

Now, Do I need a different ADFS certificate for different Suffixes or a Single Wild Card certificate with Primary Active Directory forest domain abc.com     

Need help on the same.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-06*

The requirement of the suffixes being in the certificate is solely for ADFS Device Registration (which let's say it, is very rarely used nowaday as Azure AD joined and Hybrid Azure AD joined are the prefered way for registration and these do not leverage the ADFS Device Registration). So unless you want to use that feature, you can use whatever name you want for your ADFS server as long as the name can be resolved both externally and internally (they will have to resolve to different IP addresses, but that's a different topic, do ask if you need more info on that though). Just be be clear, if your users are in abc.com and xyz.com you can absolutely use a def.net for your ADFS (so something like fs.def.net for the FQDN of the farm).
