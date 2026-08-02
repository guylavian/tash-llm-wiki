---
title: "Active Directory Replication Problems ERROR >60 days            4 /  10   40  (8606) Insufficient attributes were given to create an object."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/760456/active-directory-replication-problems-error-60-day
question_id: 760456
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
---
# Active Directory Replication Problems ERROR >60 days            4 /  10   40  (8606) Insufficient attributes were given to create an object.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/760456/active-directory-replication-problems-error-60-day (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 3 domain controllers, single site. dc1, dc2, dc3.  

dc1 and dc2 are in the same VLAN x.x.130.22, x.x.130.23  

dc3 in a different VLAN x.x.140.20  

dc1 is set to replicate with dc2 and dc3 automatticaly generated  

dc2 is set to replicate with dc1 and dc3 automattically generated  

dc3 is set to replicate with dc2 and dc1 automattically generated.  

However there is an extra replication record with dc3 ntds settings written in the   

following format.  

NTDS Settings for dc3 looks like below.  

```
Name                                                             server     from site
                            dc1        default-first-site
 dc2                                                                 dc2        default-first-site
 dc2CNF:            dc2        default-first-site
```

dc1 is the fsmo holder  

Replication is properly working between dc1 and dc2.  

prefered dns for dc3 is set to ip of dc1  

dcdiag passes between dc1 and dc2  

dcdiag fails for dc3  

I run a tool LOL, to remove stale objects, however there is no replication to dc3  

The tool reported 6 objects, two are servers which are active, the remaining 4 is clients computers.  

The source server was the pdc, so i removed the 4 client computers and left the servers. I rerun the tool again   

to detect lingering objects,right now, NO lingering objects detected.   

`I also noticed at the root of my forward look up zone, _msdcs.mydomain.local folder is missing `   

I also examined each dns server, `msdc folder` under `mydomain.local` and i can see CNAME record for already decommissioned DC04. CNAME for  

dc3 has a timestamp updated on 2rd march of 2022.  

repadmin /syncall /adep completes well without errors  

`repadmin /replsum for dc3   (8606) Insufficient attributes were given to create an object. This object may not exist because it may have been deleted and already garbage collected.`  

repadmin /showrepl returns same kind of errors shown in repadmin /replsum   

I'm having issues with name resolution, where IP is resolving to wrong computer name from reverse look up zones.  

I initiated scavenge stale records for all dns servers, but still the issues is persisting.  

The environment was initially set up by another person, i'm just working to resolve this issue.  

what is wrong with my ad ds replication?

## Answers

_No answers on this thread._
