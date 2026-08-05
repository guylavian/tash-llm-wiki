---
title: "Active Directory VM in Azure and NSG Rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1111115/active-directory-vm-in-azure-and-nsg-rules
question_id: 1111115
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-virtual-machines", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active Directory VM in Azure and NSG Rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1111115/active-directory-vm-in-azure-and-nsg-rules (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We have a few AD VMs on prem, and would like to extend AD to Azure with VMs.    

We have a site to site VPN between on prem and Azure.    

I've set up the VMs in Azure that will eventually be hosting AD on Server 2022.  My question is regarding NSG Rules.    

There is decent documentation about Inbound ports required to be open for AD replication and authentication, and I have configured those inbound NSG rules so clients and on prem ADDS servers can communicate with the servers hosted in Azure.    

What I'm not too clear on is whether I need to create Outbound NSG rules so my AD server in Azure can communicate back to on premises ADDS servers.  For example:    

Would I need to create an outbound rule for "Azure AD VM subnet x.x.x.x" to destination port 389(LDAP) "On Prem AD VM subnet y.y.y.y"     

This is just an example, but wanted to know if I would need to do this for each port outbound, or if outbound is unrestricted by default.    

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-01*

Thanks for that information.    

So with that said, we will have a deny all inbound rule before the default rules, so we're only allowing inbound from specific IP ranges.    

If I wanted to follow the same logic for Outbound (denying outbound except for specific IPs), would the same question apply? Would I need outbound rules for the AD VM in Azure to talk to our on prem AD VM for replication and authentication?
