---
title: "Cross Domain Authentication with ADFS (no domain trust)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/230246/cross-domain-authentication-with-adfs-no-domain-tr
question_id: 230246
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Cross Domain Authentication with ADFS (no domain trust)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/230246/cross-domain-authentication-with-adfs-no-domain-tr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everybody,  

yesterday i was asked whether it is possible to establish a cross domain authentication with ADFS.  

Scenario:  

-  Two different Windows Domains (A & B) without any trust configuration  

-  Network access between Domains is established with IPSec Site2Site (all ports needs to be opened separately)  

-  One specific Windows Service on a server in Domain A has to use an AD Account from Domain B for logon (Windows Service -> Logon -> This Account -> Account from Domain B)  

Our partner doesn´t want to establish a domain trust due to security reasons and is therefore asking, if we could realize this athentication process through ADFS?  

ADFS is quite new to me and i´m not sure if this scenario is even possible with ADFS?  

Kind regards,  

Björn

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-01-14*

You could use ADFS yes, as long as the application can use a federation protocol for authnetication.  

ADFS does not interact with IPSec though. It is network agnostic.   

You would have two options:  

-  Deploy ADFS in domain A, deploy ADFS in domain B, create a trust between the two (this does not require network connectivity, you can do it with exporting importing files). The user will have to be able to do IPSec though.  

-  Deploy ADFS in domain A only and create an LDAP provider for the domain B. User won't have SSO but they will be able to use their own account. In that scenario, not only the users will still need to do IPSec ontheir own, but the ADFS serverwill also need to do IPSec to reach the DCs on the other side.
