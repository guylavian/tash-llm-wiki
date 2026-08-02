---
title: "Upgrade Domain COntroller from 2012R2 to 2019  keep same IP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/574599/upgrade-domain-controller-from-2012r2-to-2019-keep
question_id: 574599
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Upgrade Domain COntroller from 2012R2 to 2019  keep same IP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/574599/upgrade-domain-controller-from-2012r2-to-2019-keep (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,   

I have DCs across 6 sites, All DCs are 2012R2 and we need to upgrade them to 2019. For first DC in Domain which is the main DC and has all FSMO roles on it and also DHCP , I want to upgrade it but keep the same IP , this way I don`t need to update DNS IP across all Servers and devices. ( it will be hard to capture all devices and you might miss those have static DNS on them )   

Each site has 2 DC for failover and DHCP and DNS on them   

1.What is the best path  to upgrade DCs with same IP ?   

 2. I also want to move DHCP to separate server while I am performing this upgrade, the DHCP IP will change. is there any thing I need to be concerned about  other than DHCP Relay and shortening the lease of IPs ?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-11*

Thanks for the great article. How about dns  server migraton. can we create a seconaday zone then  migrate it ?    

any other ms article    

Regards    

Muthu
