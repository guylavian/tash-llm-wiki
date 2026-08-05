---
title: "Move Domain Controllers to an isolated site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/118165/move-domain-controllers-to-an-isolated-site
question_id: 118165
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Move Domain Controllers to an isolated site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/118165/move-domain-controllers-to-an-isolated-site (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,  

We are in the process of Active directory modernization where we are upgrading our active directory from 2012 R2 to 2019...part of this exercise is to also find the static IP address that are reaching to the legacy domain controllers before demoting them. The logic behind this is to find the servers which are only reaching out to a single domain controller and update there DNS settings to point to the new 2019 domain controllers...Before doing the demotion we wanted to suppress the DC and check if there are application or services in the environment which are getting effected by it...One way of doing this is to suppress the srv record of the domain controllers but we don't want to do this as we have faced issue with this practice before....The other option that we got to know was about moving the domain controller to an isolated site which will do the replication but will stop the client/server traffic to the domain controller....What we wanted to know was how can we isolate a site and make this happen without firewall or vlan or re-IPing the domain controllers...Please, suggest.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-08*

According to your description, our original purpose is to find out those clients whose DNS server points to the DC that will be demote. Because we are worried that the client cannot complete the DNS query normally after the DC is demote.    

In response to this original problem, there are two situations:    

To If we are using a static DNS server, we can promote a new DC and use the IP address of the old DC, so that we can ensure that the client's DNS server is always in a working state. We can test one before proceeding with a broader upgrade. The steps refer to the following connections:    

https://serverfault.com/questions/675329/reuse-old-domain-controller-ip-addresshttps://redmondmag.com/articles/2019/06/24/replace-aging-domain-controller.aspx    

If we are using DHCP, refer to the last step described in the following connection step 20    

https://learn.microsoft.com/zh-cn/archive/blogs/canitpro/step-by-step-adding-a-windows-server-2012-domain-controller-to-an-existing-windows-server-2003-network?WT.mc_id=CANITPRO-blog-abartolo    

Finally, for how can we isolate a site, I don’t know what your definition of isolate is. It can be manually moved to the corresponding site in AD sites and services. After the client is restarted or the cache is cleared, the client of the original site will no longer Initiate verification and query requests to this DC. They will relocate other DCs in the original site

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-08*

Are you asking to use firewall for this?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-07*

It may be doable with some work. At a bare minimum you'll need these ports open between domain controllers.  

389/TCP/UDP	LDAP  

636/TCP		LDAP SSL  

3268/TCP	LDAP GC  

3269/TCP	LDAP GC SSL  

53/TCP/UDP	DNS  

445/TCP		SMB  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-07*

We don't wanted to shutdown the DC and wanted to move it to another site for achieving this. It should be like the replication should work fine, after the movement

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-10-06*

How long is your testing going to last? The much simpler method is to just power off the domain controller to check the effect. These tools may also be useful.    

https://learn.microsoft.com/en-us/sysinternals/downloads/adinsight    

https://learn.microsoft.com/en-us/sysinternals/downloads/tcpview    

--please don't forget to Accept as answer if the reply is helpful--
