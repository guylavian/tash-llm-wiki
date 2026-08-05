---
title: "Exchange Online Migration Batch Fails (Hybrid)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166646/exchange-online-migration-batch-fails-hybrid
question_id: 1166646
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange Online Migration Batch Fails (Hybrid)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166646/exchange-online-migration-batch-fails-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Exchange Online Team,

Anyone encounter this error? Do you have advised what configuration and settings needs to check? The environment is with federated trust.

Any thoughts? Any advice is much appreciated.

Thanks,

GCE

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-03*

Hello Jame,

Firewall changes has fix the issue. Appreciate your support.

Thanks,

GCE

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-03*

Hi @GCE ,

I would suggest you try to disable MRS proxy and enable it again:

```
Get-WebServicesVirtualDirectory | Set-WebServicesVirtualDirectory -MRSProxyEnabled $false
Get-WebServicesVirtualDirectory | Set-WebServicesVirtualDirectory -MRSProxyEnabled $true
```

If could, I also suggest you try to disable firewall temporarily for check whether this issue caused by firewall configuraton.

If the above methods do not work, you could also refer to this case: Error : Migrating on-prem mailbox to exchange online

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
