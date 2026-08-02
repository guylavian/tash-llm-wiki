---
title: "Cluster Error on Exchange 2016 after DR site power failure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179297/cluster-error-on-exchange-2016-after-dr-site-power
question_id: 1179297
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Cluster Error on Exchange 2016 after DR site power failure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179297/cluster-error-on-exchange-2016-after-dr-site-power (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have Exchange 2016 enterprise, four nodes, two at primary office and two at DR site, configured with IP less DAG. Two file share witness, one at Primary and other one at DR site. We were using DR site as primary for exchange, means all MBDB's are mounted at DR site. Recently, we had sudden power failure at DR site and exchange went down.

When power resumed after an hour, I changed file share witness to Primary office and failover all DB's to primary site. there was a continuous power interruption at DR site during this failover process, however I was managed to bring Exchange back online. Now when everything back to normal at DR site, I noticed that my DAG AD object is disappeared, not seeing under AD deleted items. however, when I run cluster validation of each node it is still showing my DAG is online. 2nd, One of my cluster validation file share witnesses is pointing to the old file share witness that we were using for Exchange 2010. Obviously all 2010 files share witness servers decommissioned and deleted from AD.

 

Errors:

The "Cluster Group" does not contain a Network Name resource. The cluster will have to be managed by connecting to the node names.

 

The "Cluster Group" contains one or more resources that are not recommended to be in the group. This group is used for management of the cluster, and it is not recommended to add any other resources to this group. The following is a list of resources that are not required for failover cluster manager and therefore not recommended to be in this group:

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

Thank you Andy, appreciate your prompt response. 

do i just have to run ?

 Set-DatabaseAvailabilityGroup 

Also if it gets messed up what are the chances the whole email system going down ? 

Also any idea why is my Alternate Witness server doesn't show up from my DR site which went down, show up ny-gtfs-vm01 which is main site.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

Thank you Andy, appreciate your answers. 

Also do you think there's a possibility of brining down whole email system by doing the above

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-09*

You can try this:

Simply run 

```
Set-DatabaseAvailabilityGroup
```

then check:

```
Get-ClusterQuorum
```

and see if the old FSW is removed.

if not, you can set with 

```
Set-ClusterQuorum -NodeAndFileShareMajority \\fileserver\fsw
```

\FQDNofWitnessServer\FQDNOfDAG

If that gets messed up afterwards, reset your FSW using the Exchange powershell:

https://learn.microsoft.com/en-us/powershell/module/exchange/set-databaseavailabilitygroup?view=exchange-ps

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-09*

Please check

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-09*

Hi there.

For the first issue, that is expected  :) IP Less Dags do not have a CNO

https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/pre-stage-dag-cnos?view=exchserver-2019

for the second issue:

```
Get-ClusterQuorum

Get-DatabaseAvailabilityGroup  | FL WitnessServer
```

what does it show?
