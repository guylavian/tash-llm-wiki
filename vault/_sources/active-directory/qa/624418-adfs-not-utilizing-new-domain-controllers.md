---
title: "ADFS not utilizing new domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/624418/adfs-not-utilizing-new-domain-controllers
question_id: 624418
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS not utilizing new domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/624418/adfs-not-utilizing-new-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have recently created two new Server 2019 domain controllers to replace two old Server 2012 DCs.  Before decommissioning the old DCs we have tested by shutting them down.  While they are shut down ADFS authentication fails with an error "There are currently no logon servers available to service the logon request."  When we turn the old DCs back on authentication works fine.  

The ADFS server has had is DNS settings changed to utilize DNS from the two new DCs, and furthermore with ping and nslookup commands I've been able to prove that it can resolve and contact domain hosts including all of the old and new DCs.  In particular, an nslookup of '_ldap._tcp.dc._msdcs.[domain]' specifically returns a list of all of the old and new domain controllers, so there seems no doubt that the server is aware of all the available DCs.  

The ADFS server and all the DCs are on the same AD site (we only have one site) and all on the same domain (we have only one domain).  If it's relevant, I can mention that all these servers all sit in our Azure tenant.  

Any ideas on why the ADFS server can not authenticate when the old DCs are offline, even though its DNS has discovered and can contact the new controllers?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-14*

Your troubleshooting tool will be nltest. Example with the contoso.com domain:  

```
nltest /DsGetDc:contoso.com /force
```

Untill the ouput of this is an up-and-running domain controllers, things will not work as expected.  

There is no reason to think the issue is ADFS specific, the OS is in charge of finding the closest domain controller. There is likely another underlying issue if that doesn't work at the moment. DNS config must be checked for sure. I would make sure that UDP port 389 on the new domain controllers are reachable from the ADFS servers.
