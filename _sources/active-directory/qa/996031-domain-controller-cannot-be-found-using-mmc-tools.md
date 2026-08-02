---
title: "Domain controller cannot be found using mmc tools"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/996031/domain-controller-cannot-be-found-using-mmc-tools
question_id: 996031
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Domain controller cannot be found using mmc tools

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/996031/domain-controller-cannot-be-found-using-mmc-tools (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two single domain forest with a forest trust without selective authentication and forest wide.    

The trust is working and validated on both sides.    

When I try to add a global group of DomainA into DomainB domain local Group sometimes it works and sometimes not. With powershell it works without any issues:    

$Group1 = Get-ADGroup -Identity "CN=AccessTier1,OU=Access Tiers,OU=Groups,OU=ict,DC=domaina,DC=local" -Server "dc1-domaina.local"    

$Group2 = Get-ADGroup -Identity "CN=App_Test,OU=Citrix,OU=security,OU=Groups,OU=_Customer,DC=domainb,DC=local" -Server "dc1-domainb.local"    

Add-ADGroupMember -Identity $Group2 -Members $Group1 -Server "dc1-domainb.local"    

I have used prtquery and all AD ports are listening in the remote domain.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-06*
