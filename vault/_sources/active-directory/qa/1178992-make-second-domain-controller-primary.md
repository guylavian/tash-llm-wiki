---
title: "Make Second Domain Controller Primary"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1178992/make-second-domain-controller-primary
question_id: 1178992
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Make Second Domain Controller Primary

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1178992/make-second-domain-controller-primary (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 2 domain controllers, Primary is Windows Server 2012 and the secondary Domain Controller is Windows Server 2022. Primary successfully replicates to Secondary without issues and visa versa if I make changes in Secondary. I want to decommission the Primary DC, I followed the steps to transfer all 5 FSMO roles to secondary and now secondary is supposed to be Primary.

All servers see the secondary DC and it is listed as a DNS in ipconfig/all. When I shutdown the old 2012 DC, I Could not access any of the servers with domain name only IP. I tried flushing DNS but that did not help. I turned old server back on and was able to access my servers again but some servers had issues with RDP but are okay now.

Did I miss a step to make the 2022 server a Primary DC so old one can be decommissioned? do I have to make any changes on DNS Management?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-02-09*

No need to remove the domain controller. You can freely transfer roles as needed at any time.

Step-By-Step: Migrating Active Directory FSMO Roles From Windows Server 2012 R2 to 2016

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-11*

Can you post the results of dcdiag /v /e  and repladmin /replsummary

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

DHCP is handled by our Meraki Security Appliance and I have set the DC IPs on the appliance.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-02-09*

Technically there is no primary or secondary/backup domain controllers since windows server 2000. All domain controllers are equal. 

Ensure :

BOTH are global catalog servers 

Ensure DNS is set up correctly for all client systems and other servers and devices. What is correctly? That ONLY the new DC is listed for DNS.

Ensure DNS servers are set up correctly. What does correctly mean? https://www.ajtek.ca/guides/domain-controller-dns-in-an-active-directory-environment/

Yes... You need to set this up even though you are getting rid of one. After it is gone, you can then adjust the DNS on the one left standing. 

If your old DC is providing DHCP services (likely), you will need to ensure that your new DC is setup to supply DHCP, is enabled, and authorized in the domain to give addresses to clients. Then unauthorize the old server and wait or force all clients to reregister their IPs.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-08*

Make sure you updated DHCP server to hand out new address, also check that all statically assigned members have DNS on connection properties updated with correct addresses.  Also check the event logs for clues.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
