---
title: "FSMO Rolemstaer dependency with AD Trust"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/714680/fsmo-rolemstaer-dependency-with-ad-trust
question_id: 714680
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# FSMO Rolemstaer dependency with AD Trust

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/714680/fsmo-rolemstaer-dependency-with-ad-trust (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We are observing below error in one of the application coincidently after replacing the FSMO Role master. However we have retained the IP address of FSMO Role master to new Domain Controller.  

Login failed. The login is from an untrusted domain and cannot be used with Windows authentication  

Error is observed when application is trying to connect DB which is in other AD Forest.  

-  Are there any dependency of AD Trust with FSMO role master?  

-  We dont see any hardcoding of old DC name  

-  AD Trust record also doesnt have any DC name, it is just having the target Domain name, so dont think Trust relationship uses any DC name.  

Appreciate any thoughts in this  

Regards  

Mahesh

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-16*

Thanks all, this is resolved and cleared that there is  no dependency of Trust Relationship with FSMO Role master.  

However, ensure to check that how the DNS resolution is configured in remote Domain for Trust relationship.  

In our case Hard coding was with static DNS forwarder in remote Domain which caused the issue after replacing FSMO role master.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-01-29*

Hi @Mahesh Aralelemath   ,    

please take a look here: https://learn.microsoft.com/en-us/azure/active-directory-domain-services/concepts-forest-trust#tdo-password-changes    

A trust has a trusting and a trusted side. On the trusted side, any writable domain controller can be used for the process. On the trusting side, the PDC emulator performs the password change.    

In my opinion it means: The FSMO role PDC Emulator is required in an infrastructure with trusted domains.    

Did you move the FSMO roles to another DC before deleting the old DC/re-installing the DC? The DNS entries, like cthivierge described above should be checked.    

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Regards    

Andreas Baumgarten
