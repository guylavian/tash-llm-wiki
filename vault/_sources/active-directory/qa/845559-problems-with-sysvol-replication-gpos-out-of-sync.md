---
title: "Problems with SYSVOL replication, GPOs out of sync?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/845559/problems-with-sysvol-replication-gpos-out-of-sync
question_id: 845559
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Problems with SYSVOL replication, GPOs out of sync?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/845559/problems-with-sysvol-replication-gpos-out-of-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have recently undertaken upgrading all our AD DCs to Windows 2019 as we had a mix of 2012 & 2016.  

I started this since we replaced our old file servers (running Server 2008R2!) with Windows 2019 file servers and since doing so the replication between them seemed to not be quite right.  

Main issue I have discovered is that in the GPO Console all our DCS are locked into the state "replication in progress".  

There are so many articles out there describing how to troubleshoot this that I really have no idea where to start.  

Any help that can be offered is most appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-12*

Can you post the results of the Dcdiag.. Also are you seeing any errors in the event logs. Please see the following article as well on manually checking the health of GPO's... https://www.windowstechno.com/group-policy-health-check-on-specific-domain-controller/

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-12*

Hi @Simon@PMA       

You can use the test below to confirm the extent of the issues with sysvol\GPO replication.    

https://nettools.net/how-to-test-gpos-as-gpotool-is-no-longer-available/    

You can then check the status of the sysvol share with the following article:    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

Sorry I didn't see you attachments, DC03-SRV is having issues talking to PDC-SRV and DC02-SRV, I would check if the other DCs are having the same issue, to confirm if the connectivity issues is just limited to DC03-SRV or other DCs are having problem.  If all the DCs are all having the issue, I would try restarting the DFS services on DC02-SRV and PDC-SRV to see if this fixes it.    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-12*

And below is the output from the repadmin /showrepl command:

Repadmin: running command /showrepl against full DC localhost  

XYZADSite1\PDC-SRV  

DSA Options: IS_GC  

Site Options: (none)  

DSA object GUID: 55fd8035-dd0c-4d90-a193-3857b99cde76  

DSA invocationID: e37f6943-daa3-4eb2-9b0f-2b1f4ead41b9

==== INBOUND NEIGHBORS ======================================

DC=DOMAIN,DC=XYZ,DC=CO,DC=UK  

XYZADSite1\DC02-SRV via RPC  

DSA object GUID: 0b55054b-4dd0-4960-bd33-a52e0c7c8f79  

Last attempt @ 2022-05-12 10:25:40 was successful.  

XYZADSite2\DC03-SRV via RPC  

DSA object GUID: 468379ff-8883-498d-aa4e-84b8ca5dde70  

Last attempt @ 2022-05-12 10:29:09 was successful.  

XYZADSite1\DC01-SRV via RPC  

DSA object GUID: 451b6403-1dad-4c40-86e5-3007eb4f7329  

Last attempt @ 2022-05-12 10:30:39 was successful.

CN=Configuration,DC=DOMAIN,DC=XYZ,DC=CO,DC=UK  

XYZADSite1\DC02-SRV via RPC  

DSA object GUID: 0b55054b-4dd0-4960-bd33-a52e0c7c8f79  

Last attempt @ 2022-05-12 09:59:11 was successful.  

XYZADSite1\DC01-SRV via RPC  

DSA object GUID: 451b6403-1dad-4c40-86e5-3007eb4f7329  

Last attempt @ 2022-05-12 10:27:27 was successful.  

XYZADSite2\DC03-SRV via RPC  

DSA object GUID: 468379ff-8883-498d-aa4e-84b8ca5dde70  

Last attempt @ 2022-05-12 10:29:09 was successful.

CN=Schema,CN=Configuration,DC=DOMAIN,DC=XYZ,DC=CO,DC=UK  

XYZADSite1\DC01-SRV via RPC  

DSA object GUID: 451b6403-1dad-4c40-86e5-3007eb4f7329  

Last attempt @ 2022-05-12 09:59:11 was successful.  

XYZADSite1\DC02-SRV via RPC  

DSA object GUID: 0b55054b-4dd0-4960-bd33-a52e0c7c8f79  

Last attempt @ 2022-05-12 09:59:12 was successful.  

XYZADSite2\DC03-SRV via RPC  

DSA object GUID: 468379ff-8883-498d-aa4e-84b8ca5dde70  

Last attempt @ 2022-05-12 10:29:09 was successful.

DC=DomainDnsZones,DC=DOMAIN,DC=XYZ,DC=CO,DC=UK  

XYZADSite1\DC01-SRV via RPC  

DSA object GUID: 451b6403-1dad-4c40-86e5-3007eb4f7329  

Last attempt @ 2022-05-12 09:59:44 was successful.  

XYZADSite1\DC02-SRV via RPC  

DSA object GUID: 0b55054b-4dd0-4960-bd33-a52e0c7c8f79  

Last attempt @ 2022-05-12 09:59:47 was successful.  

XYZADSite2\DC03-SRV via RPC  

DSA object GUID: 468379ff-8883-498d-aa4e-84b8ca5dde70  

Last attempt @ 2022-05-12 10:29:09 was successful.

DC=ForestDnsZones,DC=DOMAIN,DC=XYZ,DC=CO,DC=UK  

XYZADSite1\DC01-SRV via RPC  

DSA object GUID: 451b6403-1dad-4c40-86e5-3007eb4f7329  

Last attempt @ 2022-05-12 09:59:12 was successful.  

XYZADSite1\DC02-SRV via RPC  

DSA object GUID: 0b55054b-4dd0-4960-bd33-a52e0c7c8f79  

Last attempt @ 2022-05-12 09:59:12 was successful.  

XYZADSite2\DC03-SRV via RPC  

DSA object GUID: 468379ff-8883-498d-aa4e-84b8ca5dde70  

Last attempt @ 2022-05-12 10:29:09 was successful.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-11*

Can you please post the results of the following commands: dcdiag /v /e   & repadmin /showrepl
