---
title: "Best Practices for Active directory Disaster Recovery site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196399/best-practices-for-active-directory-disaster-recov
question_id: 2196399
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Best Practices for Active directory Disaster Recovery site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196399/best-practices-for-active-directory-disaster-recov (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello every one, I created new AD in DR "Site B", it will use if main Active Directory located in "Site A" fail, Our workstations and Servers have secondary "Site B" ip in DNS setting, is it nessesary to create new site in Active Directory site and servers and set subnets? I have checked disastery and it work normally, speed between sites is 1gbit/s and distance about 300 km, AS I understood site creation and subnets need for schedule replication, but we do not have any issue now because data is several kbts.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-17*

Hi FaridAhmedov,

Have a nice day!

What do you mean by first site failure? By failure do you mean failing after performing some operation?

Best regards

Neuvi Jiang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-16*

additional question if I create subnets for first site(it will include servers, workstations) if my first site fail my second site will not prevent authentifications?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-13*

Hi FaridAhmedov,

If the first one can't be successfully configured, then I suggest you create a new site.

Best regards

Neuvi Jiang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-13*

Ok if i use second only as dr ad if my first ad fail should i create site?because i need it only in my first site a users i do not have any servers amd users in site b

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-13*

Hi FaridAhmedov,

Thank you for posting in the Microsoft Community Forums.

Whether or not you need to create a new site and set up subnets in Active Directory depends on your specific needs and network architecture.

Here are a few points to consider:

Replication requirements: If your plan is to have Site B's AD database become a backup for Site A and you want it to be automatically synchronized in the event of a failover, then you need to set up the appropriate sites and subnets in Active Directory Sites and Services. site and subnet in Active Directory Sites and Services. This way, DFS replication or other AD replication mechanisms can optimize replication based on the topology between sites.

Network latency and bandwidth: Although you mentioned 1 Gbit/s between sites, a distance of 300 kilometers may cause some network latency. Latency is an important consideration in Active Directory replication because it affects the efficiency of replication. By properly configuring sites and subnets, you can ensure that replication traffic is routed more efficiently between sites.

Failover and recovery plan: Creating new sites and setting up subnets is necessary if you have a clear failover and recovery plan that relies on Active Directory site settings.

Simplify administration: Grouping servers and clients into different sites and subnets can make administration easier and more intuitive. For example, you can more easily see which servers and clients are located in which site, as well as the replication and communication status between them.

Best regards

Neuvi Jiang
