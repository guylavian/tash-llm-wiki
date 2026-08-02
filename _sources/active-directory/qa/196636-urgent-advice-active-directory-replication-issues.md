---
title: "Urgent Advice --- Active Directory Replication Issues across Sites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/196636/urgent-advice-active-directory-replication-issues
question_id: 196636
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Urgent Advice --- Active Directory Replication Issues across Sites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/196636/urgent-advice-active-directory-replication-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We apparently appear to be having some replication issues across several sites in our network. We have 5 total sites with the Site-1 being the main site and where the FSMO holder is housed. Changes appear to be moving across the other sites in AD since I can see changes at all locations, but if I do a repmadin /replsum, at Site-1, we get almost everything looking good, except for the status of one location. It just doesn't show up in the Source DSA or Dest DSA? This is Site-3. Not sure why that doesn't show up in there?

Now if I go to either Site 2,3,4 or 5, I see errors for each of the other 3 sites. I don't get an error for Site-1, just the others,

For example, If I do a repadmin /replsum at Site-2, I'll get:

Source DSA largest delta fails/total %% error  

server1/Site1 22m:49s 0 / 10 0  

server2/Site1 58m:35s 0 / 15 0  

server3/Site1 22m:34s 0 / 10 0  

Server/Site-4 08m:08s 0 / 5 0  

Server/Site-2 14m:01s 0 / 5 0

Destination DSA largest delta fails/total %% error  

server2/Site-1 08m:27s 0 / 15 0  

server3/Site-1 23m:09s 0 / 15 0  

server4/Site-1 59m:20s 0 / 10 0  

Server/Site-2 03m:31s 0 / 5 0

Experienced the following operational errors trying to retrieve replication info  

rmation:  

58 - Server/Site-3  

58 - Server/Site-4  

58 - Server/Site-5

If I go to Site-3 -- I'll see pretty close to the same thing, with errors at sites 2, 4 and 5 at the bottom with the Error 58.  

Only at Site-3 do I not also see it in the "Destination DSA" section like I do for all of the other sites. Maybe that's a separate issue for that server/site.

My question is are those sites just not supposed to talk to the other sites? I see some other sites getting the information to one or two others sites, but not all of them?

Also, is all of this setup in the Sites and Services -- Site -- Server -- NTDS Settings? Or is that for something else?

sorry -- I've never totally 100% understood these settings and information. I feel like I know most of it, but am just not understanding what's happening and what's it's showing. I'm also seeing some errors in repadmin /showrepl on Sites 2,3,4 and 5. Site-1, the main site seems ok, other than it's missing Server1/Site-3.

ource DSA largest delta fails/total %% error  

server1/Site1 22m:49s 0 / 10 0  

server2/Site1 58m:35s 0 / 15 0  

server3/Site1 22m:34s 0 / 10 0  

Server/Site-4 08m:08s 0 / 5 0  

Server/Site-2 14m:01s 0 / 5 0

Destination DSA largest delta fails/total %% error  

server2/Site-1 08m:27s 0 / 15 0  

server3/Site-1 23m:09s 0 / 15 0  

server4/Site-1 59m:20s 0 / 10 0  

server/Site-4 11m:24s 0 / 5 0  

server/Site-5 12m:38s 0 / 5 0  

Server/Site-2 03m:31s 0 / 5 0

No Site-3 on that repadmin /replsum from the main Site-1 server.

Based on all of this, what do you think it's causing these issues?

dcdaig also shows some issues:

The attempt to establish a replication link for the following writable directory partition failed.  

A warning event occurred. EventID: 0x80000785

As well as:

REPLICATION-RECEIVED LATENCY WARNING  

Server/Site-4: Current time is 2020-12-13 16:11:41.  

DC=ForestDnsZones,DC=Domain,DC=local  

Last replication received from server/site-3 at  

2020-09-16 23:41:20  

WARNING: This latency is over the Tombstone Lifetime of 60  

days!  

Last replication received from server/site-5 at  

2020-11-01 13:35:13  

DC=DomainDnsZones,DC=Domain,DC=local  

Last replication received from server/site-3 at  

2020-09-16 23:41:20  

WARNING: This latency is over the Tombstone Lifetime of 60  

days!  

Last replication received from server/site-5 at  

2020-11-01 13:35:13  

CN=Schema,CN=Configuration,DC=Domain,DC=local  

Last replication received from server/site-3 at  

2020-09-16 23:41:20  

WARNING: This latency is over the Tombstone Lifetime of 60  

days!  

Last replication received from server/site-5 at  

2020-11-01 13:35:13  

CN=Configuration,DC=Domain,DC=local  

Last replication received from server/site-3 at  

2020-09-16 23:41:20  

WARNING: This latency is over the Tombstone Lifetime of 60  

days!  

Last replication received from server/site-5 at  

2020-11-01 13:35:13  

DC=Domain,DC=local  

Last replication received from server/site-3 at  

2020-09-16 23:41:20  

WARNING: This latency is over the Tombstone Lifetime of 60  

days!  

Last replication received from server/site-5 at  

2020-11-01 13:35:12

Sorry -- I know this was a lot, but I think it's all inter-related?  

Thanks a TON for any help on figuring this out!!

Appreciate it!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

I have a question -- just digging into the Bridgehead server aspect. There doesn't appear to be a "bridgehead" server setup at each location -- do you think that would cause this issue?  

thanks again for all your help!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

Yea nothing has changed -- all of these sites are connected via a site-to-site VPN. No issues between any of the sites, and like I said, they implement all the changes that I push out from the main site?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-14*

I've turned off the firewalls on all of the servers  

Its unlikely a windows firewall issue. I'd check the routing hardware allows the ports to flow the mentioned traffic. Then since the domain controller is tombstoned demote, reboot, promo it again.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-14*

Yes, I've turned off the firewalls on all of the servers so that shouldn't be an issue.   

Does that make sense why sites-2,3,4 and 5 are not talking to each other but are to the main site?  

Also, it talks about Site-5, but that sever seems to be showing up fine?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-13*

I'd check the ports required are flowing between networks.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

Some general info here on site links bridge.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts#BKMK_7    

since tombstone has been exceeded you'll need to demote, reboot, promo the domain controller.    

--please don't forget to Accept as answer if the reply is helpful--
