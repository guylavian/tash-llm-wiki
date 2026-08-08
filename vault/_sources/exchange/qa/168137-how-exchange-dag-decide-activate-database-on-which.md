---
title: "how exchange DAG decide activate database on which server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168137/how-exchange-dag-decide-activate-database-on-which
question_id: 168137
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# how exchange DAG decide activate database on which server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168137/how-exchange-dag-decide-activate-database-on-which (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a little bit confuse about exchange DAG

As I know, quorum role will decide PAM on which server. and PAM will decide which copy is the active copy.  

-  if I have 4 servers in DAG and a witnes server. 2 DAG members down (include the quorum role member). the remaining 2 members got the same "quorum data" , how witness determine which member should get the vote?  

-  if I have 4 servers in DAG and a witnes server. 2 DAG members down (include the quorum role member). The most updated quorum data is on the member which is down. and the remaining 2 member not the most updated. the DAG will donw ?

-   if I have 5 member in DAG, 2 member down (include quorum role). how the decide which member will get the quorum role ?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-20*

Hi @Jerry Su   ,    

I agree with what Andy said.    

When a failure occurs that prevents access to the active copy of a replicated mailbox database, Active Manager selects the best possible passive copy of the affected database to activate. The specific steps you could refer to the “Best Copy Selection” in the second link provide by Andy.    

When you add a database copy, you can set the parameter "ActivationPreference", the ActivationPreference parameter value is used as part of Active Manager's best copy selection process and to redistribute active mailbox databases throughout the DAG when using the RedistributeActiveDatabases.ps1 script. The value for the activation preference is a number equal to or greater than 1, where 1 is at the top of the preference order. The preference number can't be larger than the number of copies of the mailbox database.    

For more information you could refer to: Parameters    

In addition, this article about Switchovers and failovers may help you better understand the whole process    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-19*

-  The witness doesn't decide anything. The PAM ( Quorum Owner) locks the file share on the Witness to ensure it can access it in case its vote is needed to keep a majority of voters across the cluster and keep the databases mounted. The "Quorum Role Member" (PAM)  would not be down. It would just move to one of the two servers still up in your scenario.    

-  Same as your first question. There is no "Most updated quorum data" on the member that is down. if 2 of 4 server are down, then the quorum owner role moves to a running server. If that doesn't happen, there are bigger problems in the cluster and probably would have problems way before the 2 members went down.    

-  If you have 5 members in the DAG, the same concepts apply - except the File Share Witness is not used. The PAM role will move to one of the three remaining running servers in the cluster.    

-  IF using DAC Mode, then, yes, if you reboot all the servers at the same time, no database will mount until all the servers are up, services running and they communicate with each other.     

DAC mode includes a protocol called Datacenter Activation Coordination Protocol (DACP). When DAC mode is enabled, DAG members won't automatically mount databases even if they have quorum. Instead DACP is used to determine the current state of the DAG and whether Active Manager should attempt to mount the databases.    

https://learn.microsoft.com/en-us/exchange/high-availability/database-availability-groups/dac-mode?view=exchserver-2019#how-dac-mode-works    

More info:    

https://learn.microsoft.com/en-us/exchange/high-availability/database-availability-groups/active-manager?view=exchserver-2019

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-19*

one more thing, if the DAC mode is enabled, and all the servers reboot is same time, no database will mount after reboot ?
