---
title: "ADFS and Migrating users to new Forest"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/662265/adfs-and-migrating-users-to-new-forest
question_id: 662265
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS and Migrating users to new Forest

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/662265/adfs-and-migrating-users-to-new-forest (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The scenario is  

We will be migrating users from Forest A to Forest B  

-  Two forests (with trusts)  

-  Exchange Hybrid (Mailboxes already in Forest B)  

-  ADFS server is on Windows 2019  

-  ADFS federated to Azure  

-  customized immutableID (will be migrated)  

-  38 Relying Trusts to internal and external resources  

-  5000+ users  

-  users will maintain their UPNs  

My question is around how to manage ADFS. Due to business requirements, we will be migrating users to Forest B in batches so not all users will be authenticating from the same Forest.  

As Azure uses a customized ImmutableID, I believe that ADFS will manage this via the trust. However, other federations are using UPN, mail addresses etc.  

What is the best solution?  

1:  

-  Single ADFS relying on Forest Trust  

-  Migrate users   

-  remove users from source forest  

2:  

-  New ADFS Farm in target Forest  

-  recreate all Relying Trusts  

Thank you

## Answers

_No answers on this thread._
