---
title: "Exchange HCW using 2 Exchange 2016 edge servers (stmp1.domain.com and smtp2.domain.com)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1159797/exchange-hcw-using-2-exchange-2016-edge-servers-st
question_id: 1159797
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange HCW using 2 Exchange 2016 edge servers (stmp1.domain.com and smtp2.domain.com)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1159797/exchange-hcw-using-2-exchange-2016-edge-servers-st (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

Looking for some Exchange hybrid configuration wizard guidance.

Scenario:

EWS published using hybrid.domain.com

2x Edge Servers configured using dedicated FQDNs - edge1.domain.com and edge2.domain.com

If I want high availability for SMTP/Edge role with Ex hybrid how can I achieve it? 

Can I run HCW twice pointing to each edge FQDN (edge1.domain.com and edge2.domain.com)? If this is not possible, is there any other method available?

Another question I have is when HCW asks for Organization FQDN, it will be always EWS URL, correct?

Thanks in advance

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-01-12*

Hi @Syed Azhar,

You can refer to this guide to deploy a classic hybrid deployment:

Create a hybrid deployment with the Hybrid Configuration wizard | Microsoft Learn

 

And adding an Edge Transport server in the hybrid environment can refer to this article:

Edge Transport servers with hybrid deployments | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
