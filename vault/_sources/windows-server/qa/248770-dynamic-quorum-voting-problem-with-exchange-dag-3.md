---
title: "Dynamic quorum, voting problem with exchange dag 3 node"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/248770/dynamic-quorum-voting-problem-with-exchange-dag-3
question_id: 248770
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-high-availability-clustering-high-availability"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Dynamic quorum, voting problem with exchange dag 3 node

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/248770/dynamic-quorum-voting-problem-with-exchange-dag-3 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i read the topic and try by myself : https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/understand-quorum    

first i built a exchange dag with 2 node + witness     

i tried:    

```
(Get-Cluster).witnessDynamicWeight  
1
```

=> correct     

```
Get-ClusterNode | ft name, dynamicweight, state,id  
Name   DynamicWeight State Id  
----   ------------- ----- --  
EX1-DC             1    Up 1  
EX2-DC             1    Up 2
```

=> correct    

next, i add more 1 node into the DAG, now we have a DAG with 3node.    

```
(Get-Cluster).witnessDynamicWeight  
0
```

=> correct    

```
Get-ClusterNode | ft name, dynamicweight, state, id  
Name   DynamicWeight State Id  
----   ------------- ----- --  
EX1-DC             1    Up 1  
EX2-DC             1    Up 2  
EX3-DR             1    Up 3
```

=> still correct    

now, it is complex part, i tried to shutdown 1 node, as documented by microsoft (link above), i will have Scenario "Two nodes with a witness"    

here is result:    

```
Get-ClusterNode | ft name, dynamicweight, state,id  
Name   DynamicWeight State  Id  
----   ------------- -----  --  
EX1-DC             0  Down  1  
EX2-DC             0    Up  2  
EX3-DR             1    Up  3
```

=> i think i will have 2 voting hosts, not 1.    

```
(Get-Cluster).witnessDynamicWeight  
0
```

=> witness not vote?    

after that, i tried shutdown EX3-DR node, with 1 vote, if i shutdown the node, we have total 0 vote in cluster, but cluster still run? how??

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-02-03*

Hi @Tran Van Hoang   ,    

Good day!    

Thank you for sharing the information! Yes I’ve read the same article and I see it too.     

First of all, the conclusion is that it should be an expected behavior, you don’t need to worry about it.    

So sorry for the delay of this reply. I did many tests in these days, and I had experienced extremally the same things with you:    

I build a 3 node DAG and If shutdown EX2:    

     

Then I shutdown EX3:    

     

And if I remove vote from EX3:    

     

Also the WitnessDynamicWeight is 0.    

These above are using the DAG I created in Exchange.    

And here is the explanation:    

     

That’s exactly what we have experienced, and is also what the article explains.    

And I also test creating the cluster with the Windows Failover Cluster Manager. I added the FSW(File Share Witness) after creating it.    

Then the result is as expected:    

     

In both cases, the whole system maintained availability after two nodes shut down(one by one), though they used a different method: one is to add vote for witness, and the other one is to remove vote from a node.    

Bests,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-09*

Hi @Mico Mi  

let me recap:  

-  when 3 node is online, cluster is online

Get-ClusterNode | ft name, dynamicweight, state, id  

Name DynamicWeight State Id  

EX1-DC 1 Up 1  

EX2-DC 1 Up 2  

EX3-DR 1 Up 3

and

(Get-Cluster).witnessDynamicWeight  

0

-   When i shutdown node 1 (EX1-DC), cluster is online

Get-ClusterNode | ft name, dynamicweight, state, id  

Name DynamicWeight State Id  

EX1-DC 0 Down 1  

EX2-DC 0 Up 2  

EX3-DR 1 Up 3

and

(Get-Cluster).witnessDynamicWeight  

0

-   I continue shutdown 1 more node (EX3-DR), cluster is still online

Get-ClusterNode | ft name, dynamicweight, state, id  

Name DynamicWeight State Id  

EX1-DC 1 Down 1  

EX2-DC 1 Up 2  

EX3-DR 1 Down 3

and

(Get-Cluster).witnessDynamicWeight  

0

==> it does not match the scenarios described in https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/understand-quorum

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

Hi,

after that, i tried shutdown EX3-DR node, with 1 vote, if i shutdown the node, we have total 0 vote in cluster, but cluster still run?

Do you mean you shut down two nodes and the cluster still run in the test?  

Could you post the screenshot of Get-ClusterNode after shut down two nodes?

Best regards,  

Mico Mi

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-03*

i remember i declared a witness when i created the DAG. so i had 3 node + 1 witness    

    

and if i lost 1 node, now im here    

    

So, if I'm in the second case, then I have to get 2 votes from 2 live nodes + 1 vote from witness. Right?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-29*

Hi @Tran Van Hoang   ,    

After you shutdown the EX1-DC, does the witness server work correctly? I think you should check it first.    

Because your result is similar with 3 node DAG but the witness is shutdown. Improving Resilience of Exchange Server 2013 Database Availability Groups with Windows Server 2012 Cluster Dynamic Quorum    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
