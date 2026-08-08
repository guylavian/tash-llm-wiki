---
title: "Upgrading Domain Controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/106126/upgrading-domain-controllers
question_id: 106126
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Upgrading Domain Controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/106126/upgrading-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We're looking at upgrading most of our DCs which consists of both datacenter and remote sites DCs. We are looking to go from Windows 2008 R2, 2012 R2 to 2019. There are already a few 2016 DCs which were recently built for some remote sites.  

DNS are installed on all DCs. FSMO roles are on a primary DC in datacenter as well as KMS, etc. Nothing fancy.  

I'm putting together a high and low level design for my manager before we agree on the works. Please kindly advise your thoughts on the below.  

Local Sites:  

-  Build new Win2019 VM with the same host name (must) and IP (preferred) and leave it off the domain  

-  Demote DC and turn off the VM  

-  Spin up new DC, join it onto the domain and install all necessary roles. Promote it to a DC and ensure everything is ok  

-  Repeat this for other local sites  

-  Will also be enabling clients to locate the next closest DC in GPO as this isn't enabled  

-  Workstations are configured to use local DC as primary DNS and DC3 in datacenter fo secondary DNS  

Datacenter:  

We currently have 4 DCs and looking to reduce this down to 2. DC2 currently holds FSMO roles.  

-  All servers within datacenter are configured to use DC3 as primary DNS and DC4 as secondary DNS  

-  Build new VM with the same name as DC1. Demote existing DC1 and shut it down  

-  Join new VM (DC1) onto the domain and promote it to a DC  

-  Move FSMO roles from DC2 to new DC1  

-  Reconfigure all datacenter servers to use DC1 (will have new IP) as primary DNS and leave secondary DNS as is  

-  Build new VM with the same name as DC2. Demote existing DC2 and shut it down  

-  Join new VM (DC2) onto the domain and promote it to a DC  

-  Reconfigure secondary DNS on all servers to point to DC2  

-  Demote DC3 and DC4 and decommission  

-  Raise domain functional level from 2008 R2 to 2016. Don't think we can go to 2019 as we already have 2016 DCs?  

If everything is configured properly, is there an expected outage during any of the above steps? I understand that moving FSMO roles or decommissioning DCs should take things like NTP configured on PDC emulator or any specific services configured to a particular DC  into considerations, etc.  

Is anything else missing from the above or do steps need to be re-ordered?  

Thanks in advance,  

James.

## Answers

_No answers on this thread._
