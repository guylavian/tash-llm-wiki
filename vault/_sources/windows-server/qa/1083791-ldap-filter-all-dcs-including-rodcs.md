---
title: "LDAP filter - all DCs including RODCs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1083791/ldap-filter-all-dcs-including-rodcs
question_id: 1083791
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# LDAP filter - all DCs including RODCs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1083791/ldap-filter-all-dcs-including-rodcs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, what is LDAPFilter for all DCs including RODCs? This one is only for R/W DCs:    

(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=8192))

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-10*

It seems this is what I am after:

Get-ADComputer -LDAPFilter "*(&(operatingSystem=server)(!description=Failover cluster virtual network name account)(!userAccountControl:1.2.840.113556.1.4.803:=2)((!primaryGroupID=516)(!primaryGroupID=521)))*" |  

Sort-Object -Property Name |  

Select-Object -ExpandProperty Name 1>$null -OutVariable memberServers

But still one SQL cluster name is listed ...

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-10*

(primaryGroupID=516) - for RW Domain Controllers    

(primaryGroupID=521) - for RODC
