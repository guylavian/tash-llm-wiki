---
title: "Exchange Replication faied with Passive disconnected and resyn"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/328524/exchange-replication-faied-with-passive-disconnect
question_id: 328524
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Replication faied with Passive disconnected and resyn

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/328524/exchange-replication-faied-with-passive-disconnect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 4 exchange 2016 in a DAG setup. there are two sites with two exchange servers on each site. I had to rebuild the exch servers due to recent attack. Now when I ran add-mailboxdatabasecopy and it always fails with Passive Disconnected and resynchronizing message.  

I have deleted the DB and run Update-MailboxDatabaseCopy -Identity DB1\MBX1 - -DeleteExistingFiles with same result.  

test-replicationhealth shows below error   

server1: ClusterNetwork: Failed. network 'replicationDagnetwork01' has no network interface for server 'server2'. Correct the physical network configuration so that each mailbox server hasw exactly one interface on each subnet.  

get-databaseavailablitygroupNetwork shows:  

Name               : MapiDagNetworkDescription           

Subnets            : {{10.111.1.0/24,Up}, {10.112.1.0/24,Up}}  

Interfaces         : {{mbx1,Up,10.111.1.221}, {mbx3,Up,10.111.1.223}, {mbx2,Up,10.112.1.222}, {MBX4,Up,10.112.1.224}}  

MapiAccessEnabled  :True  

ReplicationEnabled : True  

IgnoreNetwork      : False  

Identity           : exchangedag\MapiDagNetwork  

IsValid            : True  

ObjectState        : New   

Name               : ReplicationDagNetwork01  

Description        :   

Subnets            : {{fe80::/64,Up}}  

Interfaces         : {{mbx1,Up,fe80::b83e:c6fb:15db:488%13}, {mbx2,Up,fe80::4888:b345:5731:b06b%16}}  

MapiAccessEnabled  : False  

ReplicationEnabled : True  

IgnoreNetwork      : False  

Identity           : exchangedag\ReplicationDagNetwork01  

IsValid            : True  

ObjectState        : New  

It seems that the ClusterNetwork has misconfiguration. I use one physical NIC card with both IPv4&6 enabled. It seem use IPV6 to replicate. The Database avalibility group IP address is 255.255.255.255.  

How can I fix this issue? Thanks.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-24*

Hi @alan gao  ,    

Please refer to the blog below and make sure your MAPI and Replication networks are configured properly:    

Network Adapter Configurations For DAG Members     

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Then run the following command to reassess the network configuration and check the result:    

```
Set-DatabaseAvailabilityGroup  -ManualDagNetworkConfiguration $true
```

Should the error persists, would you please have a check at the Event Viewer and see if there's any relevant events recorded out there?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
