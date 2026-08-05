---
title: "Problem adding additional Windows Server 2022 ADFS Proxy (WAP) server to existing farm"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/907913/problem-adding-additional-windows-server-2022-adfs
question_id: 907913
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Problem adding additional Windows Server 2022 ADFS Proxy (WAP) server to existing farm

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/907913/problem-adding-additional-windows-server-2022-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to add a new Windows Server 2022 ADFS Proxy server in Azure for a new Windows Server 2022 ADFS Server. The existing ADFS Farm is running on Windows Server 2012 R2. I am getting the below error while deploying the proxy:    

An error occurred when attempting to establish a trust relationship with the federation service. Error: Unauthorized. Verify that the service account has administrative access on the target Federation Server.    

I tried disabling TLS 1.3 but did not help.

## Answer (community) — community member

*upvotes: 1 · updated: 2023-03-13*

I upgraded the ADFS Farm behavior level and that solved the issue. It disconnected all my Windows Server 2012 ADFS nodes but then I was able the join my Windows Server 2022 WAP to the farm.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-06-29*

And the same account works when you add a 2012 R2 WAP server to this farm?    

I have not seen this situation before. Usually, the upgrade path is the opposite. First update the AD FS servers and then the WAPs. Not sure if that combination of WAP/backend was even tested. Is there a reason why you want to upgarde the WAP but not the AD FS servers?
