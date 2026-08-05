---
title: "Domain Controller Errors || Advertising, DFSREvent, NetLogons"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/861740/domain-controller-errors-advertising-dfsrevent-net
question_id: 861740
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Errors || Advertising, DFSREvent, NetLogons

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/861740/domain-controller-errors-advertising-dfsrevent-net (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

205072-dcdiag-testdns.txt205054-dcdiag.txt    

Our recently added windows server 2022 domain controller failed to join workstations. While running the DCDIAG, we have observed failures on Advertising, DFSREvent, NetLogons    

Attached diag results for reference. Requesting your guidance to resolve this issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-07*

Thanks. It is working fine now

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-24*

@Anonymous   Thanks for the response.    

Our DC is not multihomed and there is no public DNS server IP's.     

While checking the member DC, we can see there is no shares for sysvol and netlogon. And the domain controller holding the FSMO roles, there is no issues.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-05-24*

I'd check the domain controller is not multi-homed, check that domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
