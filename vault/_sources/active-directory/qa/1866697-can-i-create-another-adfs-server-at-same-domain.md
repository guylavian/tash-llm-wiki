---
title: "Can I create another ADFS server at same domain?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1866697/can-i-create-another-adfs-server-at-same-domain
question_id: 1866697
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Can I create another ADFS server at same domain?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1866697/can-i-create-another-adfs-server-at-same-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an ADFS Server (WID) and ADFS proxy 2.0 Running on Windows Server 2008 R2 in a single domain exampledomain.com.

The client needs to recreate or migrate this solution to Windows Server 2022.

My plan is create another solution in the same domain and network, using ADFS different URL's Name, and differents hostnames and ip's.

-  Create 1 VM with WS2K22 and install ADFS Roll.

-  Create 1 VM with WS2K22 and install ADFS Proxy Roll.

-  Configure in both VM's a new SSL Certificate.

-  Migrate the relaying party trust one by one (From ADFS 2008 to ADFS 2022)

is it possible to have two adfs servers at the same domain?

Best Regards.

## Answers

_No answers on this thread._
