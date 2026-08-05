---
title: "Overlapping networks / Active Directory interforest migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/637766/overlapping-networks-active-directory-interforest
question_id: 637766
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Overlapping networks / Active Directory interforest migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/637766/overlapping-networks-active-directory-interforest (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are about to begin inteforest Active Directory migration.    

Both Forests are single-domain, all Domain Controllers on both domains are running Windows Server 2019. Source domain has 3000 AD user accounts, hundreds of domain-joined servers, 15000 AD security groups.    

Our plan in nutshell:    

Setup DNS name resolution cross domains    

Setup two-way Forest Trust    

Install ADMT server on target domain    

create new AD user accounts in target domain in advance and migrate mailboxes    

Merge SID history of source domain user accounts to user accounts in target domain    

Migrate all security groups    

Migrate all servers    

Workstations will be re-imaged and not migrated    

Decommission source domain    

Problem:    

We now know that several IP subnets overlap between companies. Telecom team plans to resolve this by using NAT firewall between company networks. Microsoft does not recommend using NAT.     

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/support-for-active-directory-over-nat    

Telecom team don't accept idea of start changing IP addresses to make NAT option un-needed :)    

Initial workaround is to deploy one (or more) target Domain Controller to source domain network and connect it to rest of DCs  using VPN tunnel. But I guess that requires to install 2nd NIC on Domain Controllers.     

I have never faced scenario where network between source and target domain overlap. How have you managed similar this kind of situation?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-15*

I suppose you can map network 1 and network 2 IP ranges to a virtual IP range and sort this out.  

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-24*

Hi @Anonymous       

It is possible to use NAT to complete a migration, I've done a few, they are just a little more complicated.  The main issue you have to overcome is naming resolution and making sure that DNS requests between domains resolves to the correct NAT'd address.    

The best way to achieve this is to use a single crossing point between domain, if your ADs are geo-diverse, you will have to route all DNS traffic back to a single site.  You will need both NAT and DNS rewrite to support this, most enterprise grade firewall support these features.  If not there are a few Linux service that can do this as well.     

As for your approach, it looks ok but I'm not a fan of using SID history. I can't remember how many domains I've look at where SID history still exists years after the migration has been completed.  The main reason SID history remains in place, is that the removal of SID history is usually the last task to be completed, and as a result it doesn't happen because the project runs out of time, money, or fear that things will break once SID history is removed.  SID History hides problems with permissions that have not been remediated, and you only find these once you remove SID history.  My suggest would be to invest the time up front to remediate the permissions between domains, then test access as part of your pilot migrations.  Yes this will take more time up front however, you will be able to identify and fix issues as they happen, rather than the big bang approach when you remove SID history.    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-24*

Thanks Dave. I know multihome DC is not a good idea. But I would like to know more what are real life problems that may occur during AD migration if NAT is used between networks.   

I suspect that NAT may affect negative to client computers when they attempt to access server resources in other domain.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-23*

But I guess that requires to install 2nd NIC on Domain Controllers.  

Multihoming a domain controller will always cause no end to grief for active directory DNS
