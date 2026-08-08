---
title: "domain controller on public IP subnet"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/710751/domain-controller-on-public-ip-subnet
question_id: 710751
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# domain controller on public IP subnet

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/710751/domain-controller-on-public-ip-subnet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi i have deployment to integrate on prem AD and GOV cloud, i have to deploy additional tree domain within existing forest, but in gov cloud i have public ip segment on which will be sit two new DC. Networks on prem is private A class but cloud has public subnet. Network is fully routed with any any comunications btween dcs on headoffice and cloud. Is that supported scenario to have public subnet on DCs?. Cloud network i think will be not exposed to public internet.  

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-02*

HI DSPatrick, network guy suggest me that network 100.74.xx.xx is private so no problem I have already setup tree domain to the root forest, but have question about default zone _msdcs.root.forest.net. Domain controllers is replicating fine but on new tree domain controller DNS this zone is missing. When I check _msdcs.root.forest.net on root domain, zone is configured to only replicate all domain controlers in this domain (for windows 2000 compatibility), its necessary to change replication of this zone to all domain controller in forest ? Is there some chance to broke something. On root domain is bunch of old w2008r2 controllers and others is w2016. Its safe to change this?  

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-01-26*

Ok but I will rather to use normal private adress space for placing DCs, so i will be ask to reconfigure network to comply with RFC.  

Thanks Patrick

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-01-26*

Hi DSPatrick that range is in 100.74.xxx.xxx range it seems that its a private range can be this adress space used on AD DNS?  

 Shared address space[5] for communications between a service provider and its subscribers when using a carrier-grade NAT.  

https://en.wikipedia.org/wiki/IPv4_shared_address_space

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-26*

No, this isn't going to work. All domain members must use domain DNS to find and logon to domain so you'll need to use a VPN.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
