---
title: "Unable to join domain. My Active Directory Domain Name is same as the company web domain."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/759709/unable-to-join-domain-my-active-directory-domain-n
question_id: 759709
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Unable to join domain. My Active Directory Domain Name is same as the company web domain.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/759709/unable-to-join-domain-my-active-directory-domain-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I try to join my local domain which has same name as Website the system responds as   

```
An Active Directory Domain Controller (AD DC) for the domain "domain name" could not be contacted.
```

pinging domain name returns public IP address of the website and not the server IP address.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-03-04*

I'd check the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
