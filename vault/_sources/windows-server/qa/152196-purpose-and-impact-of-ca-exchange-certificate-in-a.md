---
title: "Purpose and impact of CA Exchange certificate in a PKI environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/152196/purpose-and-impact-of-ca-exchange-certificate-in-a
question_id: 152196
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Purpose and impact of CA Exchange certificate in a PKI environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/152196/purpose-and-impact-of-ca-exchange-certificate-in-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning everyone,  

I set up an OCSP in a 2-tiers PKI infrastructure :  

The OCSP is in error in pkiview.msc. To get it "green" in pkiview.msc, I had to delete and recreate the CA Exchange certificate (certutil -cainfo xchg).   

-  Is it normal ? (I mean, the usual way to do).  

-  Should I watch any side effect on the PKI when I delete and recreate this CA Exchange certificate ?  

-  What is the purpose of this CA Exchange certificate ? I understand it is to manage the archival of the certificate private key from the workstation to the KRA. I don't understand why it is involved with the OCSP.  

Thank you for your time

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

Thank you again for your answer :)
