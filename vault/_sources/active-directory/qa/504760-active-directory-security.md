---
title: "Active Directory Security"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/504760/active-directory-security
question_id: 504760
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# Active Directory Security

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/504760/active-directory-security (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I am working on a security guideline for Active Directory, however I haven't found a good reference to establish: (1) Minimum length for administrator password in AD and, (2) Expiration time of administrator accounts in AD  

Do you know a best practice for these parameters?  

Thanks  

Regards

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-08-07*

Hi @Gilberto Fernandez Garza   , thanks for the post.    

Password and Account security guidelines is differ base on the organisation security and  compliance requirements.    

standards like NIST, CIS, ISO are some of the security framework and guidelines for improving overall security and compliance based on org needs..     

Generally I would recommend to rename the default administrator account in AD to something to non obvious usernames instead of  administrator and the rest will be configured through AD password policy domain level. Set password length to 14 with expiration of 60 days. Again this will change based on org needs and there are multiple other  policy setting needs to be considering while setting the password policy for better security.
