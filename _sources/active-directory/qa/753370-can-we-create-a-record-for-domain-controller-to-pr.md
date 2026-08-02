---
title: "Can we create A record for Domain Controller to provide LDAP authentication to DotNet Applications"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/753370/can-we-create-a-record-for-domain-controller-to-pr
question_id: 753370
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Can we create A record for Domain Controller to provide LDAP authentication to DotNet Applications

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/753370/can-we-create-a-record-for-domain-controller-to-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I am looking for solution where I want to provide the LDAP configuration to one of our Application for authentication purpose, as of now we have provided IP address of our domain controller, but we want the redundancy in terms of authentication.  

I searched some articles where it says that we can use Domain name instead of Domain Controller IP/hostname but our application is not supported this, so is it feasible to create A record for Domain Controllers as below ?  

DC 1: 192.168.1.1  -Current Record  

DC2:  192.168.1.2  -Current Record  

A Record: LDAP.xyz.com ---192.168.1.1 and LDAP.xyz.com ----192.168.1.2  

Will that work, Hope this will not break anything to current AD environment.  

Thanks  

Mukesh

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-02-28*

DNS records already exist for your domain controllers in active directory so adding more static records isn't going to make a difference. Assuming the windows instance the application runs from is domain joined then windows will know the name resolution. We don't know anything about how the application works internally. You may need to contact the application developer about a solution.   

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
