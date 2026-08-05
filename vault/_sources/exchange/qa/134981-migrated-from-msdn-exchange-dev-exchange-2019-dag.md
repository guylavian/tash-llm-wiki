---
title: "[Migrated from MSDN Exchange Dev]  Exchange 2019 DAG DAC-mode datacenter activation failover"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/134981/migrated-from-msdn-exchange-dev-exchange-2019-dag
question_id: 134981
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# [Migrated from MSDN Exchange Dev]  Exchange 2019 DAG DAC-mode datacenter activation failover

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/134981/migrated-from-msdn-exchange-dev-exchange-2019-dag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/cc146b07-adb6-431c-bc04-1fd701568579/exchange-2019-dag-dacmode-datacenter-activation-failover?forum=exchangesvrdevelopment    

Hi!    

Having issues to fail over my environment in test-disaster scenario when my main datacenter goes offline and i need to activate DR-datacenter.     

Summary:    

DatabaseAvailabilityGroup: DAG01    

Members: Exchange2019-01, Exchange2019-02    

DAC-mode: DagOnly    

Main Datacenter    

Exchange2019-01 (Primary) (Holds all databases with activationprefernce 1)    

FSW01 (Primary FSW)    

DR-Datacenter    

Exchange2019-02 (Passive) (Holds passive databasecopys)    

FSW02 (Alternate FSW)    

I am testing a disaster scenario with the following actions    

Shutdown Exchange2019-01 and FSW01    

Exchange2019-02 gets out of votes and dismounts databases which is expected.    

Restore process followed from Microsoft Documentation in the link i provided with the commands that comes with DAC-mode.    

Stop-DatabaseAvailabilityGroup -Identity  DAG01 -Mailboxserver Exchange2019-01 -ConfigurationOnly    

net stop clussvc    

Restore-DatabaseAvailabilittGroup -Identity DAG01    

(This command should evict Exchange2019-01 from the cluster and change to Alternate FSW then start up the cluster)    

i have tried the restore command a couple of times but no success    

Error:    

An error occured while attempting a cluster operation. Error: Cluster API Failed:    

OpenByNames (servername) failed for each server. Specific exceptions: 'An error occured while attempting a cluster operation. Error: Cluster API failed: "OpenCluster(servername) failed with 0x6d9    

Error: There are no more endpoints available from the endpoint mapper"'    

hxxps://learn.microsoft.com/en-us/Exchange/high-availability/manage-ha/datacenter-switchovers?view=exchserver-2019    

Best regards Johan

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-26*

Same Problem(  

Unable to complete Datacenter Switchover procedure on exchange 2019  

Same errors and steps, Nothing helps

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

What will you get if running the following command:    

Get-DatabaseAvailabilityGroup -Identity DAG | fl name,servers,startedmailboxservers,stoppedmailboxservers    

If Exchange19-02 is listed in stoppedmailboxservers, I think you've stopped wrong mailbox servers. You should specify the ActiveDirectorySite when running Stop-DatabaseAvailabilityGroup.    

Now please try the following steps:    

1   Stop the correct servers:     

Stop-DatabaseAvailabilityGroup -Identity DAG -ActiveDirectorySite Exchange-A -ConfigurationOnly:$TRUE     

2   Start the servers in the second datacenter:    

Start-DatabaseAvailabilityGroup -Identity DAG -ActiveDirectorySite Exchange-B    

3   Stop-Service ClusSvc    

4   Restore-DatabaseAvailabilityGroup -Identity DAG -ActiveDirectorySite Exchange-B -Confirm:$FALSE    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
