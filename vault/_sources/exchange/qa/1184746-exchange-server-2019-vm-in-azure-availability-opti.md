---
title: "Exchange Server 2019 VM in Azure - availability options"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1184746/exchange-server-2019-vm-in-azure-availability-opti
question_id: 1184746
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-virtual-machines", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server 2019 VM in Azure - availability options

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1184746/exchange-server-2019-vm-in-azure-availability-opti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

I would like to setup 2 x Exchange Server 2019 VMs in Azure but I am not sure which is the best availability option. 

The requirement is to have a HA on a different Zone on the same Region.

I can already see that Availability Zones won't do cos it's creating 3 x VMs in each zone so I won't be able to manage Exchange as a single server.

Availability Set also won't do as it will create the VMs on a different server rack but on the same Zone (unless I don't follow Avail Set config)

That leaves Virtual Machine Scale Set - but is this the best option for Exchange? 

Thanks!

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2023-02-27*

Hi

you need to think about this in terms of Exchange HA as opposed to VM HA. So you would need to put your 2 servers in a DAG configuration with a separate server acting as a Witness.

https://learn.microsoft.com/en-us/exchange/high-availability/deploy-ha?view=exchserver-2019

You would also need to have your AD extended into Azure as well.

However, some caution - unless you have an Enterprise Azure subscription, Port 25 will be blocked:

https://learn.microsoft.com/en-us/azure/virtual-network/troubleshoot-outbound-smtp-connectivity#enterprise-agreement

In my opinion, I would advise you to consider a move to M365/Exchange Online instead. Better stability and no management overhead of VMs/Availability/Security.

Hope this helps,

Thanks

Michael Durkan

-  If the reply was helpful please upvote and/or accept as answer as this helps others in the community with similar questions. Thanks!
