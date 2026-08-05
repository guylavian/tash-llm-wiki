---
title: "Domain Controllers Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/781336/domain-controllers-migration
question_id: 781336
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controllers Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/781336/domain-controllers-migration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Friends,   

Please help.   

We are a big organisation with 1600 + Users.   

Now I am planning to migrate two Domain Controllers (server 2012 r2) dc01 (192.168.2.45) and dc02(192.168.2.46) to two Server 2019 boxes.   

In order to have less impact on updating Appliance and other windows servers' DNS entries, my plan is:   

-  Demote DC02, remove it and power off the server.   

-  Set up a new DC03 server 2019 box with the same IP with DC02. And set up as secondary DC server.   

-  Migrate FSMO roles to DC03 as primary DC server. So, DC03 becomes domain master.   

-  Migrate DHCP from DC01 to DC 03. Demote DC01 and power off.   

-  Set up DC04 server 2019 and set up as secondary domain for load balancing etc.  

-  Done  

Can we practically do this?   

Thanks a lot,  

ML

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-03-22*

The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

Yes, your plan sounds good. You can also check in between steps in case some cleanup were necessary to remove remnants of demoted one.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

It's also recommended to confirm domain health is 100% (dcdiag, repadmin tools) before starting and precautionary in between steps.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
