---
title: "2 ADFS in 1 domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/402509/2-adfs-in-1-domain
question_id: 402509
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# 2 ADFS in 1 domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/402509/2-adfs-in-1-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we have several departments within one domain of Active Directory. Each department has its own tenant office365. In two departments, we want to set up a hybrid, the login method - ADFS.  

Let us assume that:  

domain - domain.com  

department1 - UPN in the format @ department1.com  

dzial2 - UPN in the format @ department2.com  

I was thinking about 2 ADFS:  

adfs1: adfs.department1.com  

adfs2: adfs.department2.com  

Can we have two independent adfs within one domain and route so that people from upn @ department1.com connect to adfs.department1.com and people from upn @ department2.com connect to adfs.department2.com?  

Is there any other better way for people from two separate O365 tenants to authenticate themselves with ADFS?

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-01-22*

We have workshops to help move off ADFS https://techcommunity.microsoft.com/t5/community-events-list/microsoft-workshops-how-to-successfully-migrate-away-from-ad-fs/m-p/3668480 & https://www.microsoft.com/en-us/security/business/identity-access/upgrade-adfs
