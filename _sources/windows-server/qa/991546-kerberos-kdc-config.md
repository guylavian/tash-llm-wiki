---
title: "Kerberos KDC Config"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/991546/kerberos-kdc-config
question_id: 991546
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Kerberos KDC Config

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/991546/kerberos-kdc-config (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm really new to kerberos config, sorry if this is a stupid question!    

In the Kerberos krb05 config file, I have KDC pointing to a single IP address for our domain controller.    

Recently that DC failed causing some issues.  So I am trying to point to a group of DCs to give some failover.    

I can point to a DNS with a few DCs behind it which will do the job.  But I'm trying to find out if I can just point to the root DNS, which by our design always points to the primary DC.      

So could the KDC and default_domain value be the same?    

Thanks

## Answers

_No answers on this thread._
