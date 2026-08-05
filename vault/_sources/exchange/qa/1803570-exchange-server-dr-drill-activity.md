---
title: "Exchange Server DR-Drill activity"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1803570/exchange-server-dr-drill-activity
question_id: 1803570
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange Server DR-Drill activity

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1803570/exchange-server-dr-drill-activity (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Expertise,

I have an Exchange mail setup in both DC (DCMBX01, DCMBX02) and DR (DRMBX03, DRMBX04) environments. Here, I have a Database Availability Group (DAG) configured with different witness servers for DC and DR. I want to perform a DR Drill Activity to verify that if the DC site servers go down suddenly (due to power cut or other reasons), the DR site can handle the mail solution properly. Specifically, I need to check if the databases will automatically move and become active on the DR site without manual intervention, as I want to simulate a real disaster scenario.

What process should I follow at the DAG level to verify this real scenario? If the databases fail or dismount, how can I ensure they become active and move to the DR site without accessing the DC site? Please provide guidelines and the necessary steps for this process.

Thank you.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-07-08*

To perform a DR (Disaster Recovery) drill activity for your Exchange environment with Database Availability Groups (DAGs), follow these steps to simulate a scenario where the DC (Data Center) site becomes unavailable, and ensure the databases failover and become active on the DR (Disaster Recovery) site automatically:

-  Verify that your DAG is healthy and there are no existing issues reported in Exchange Management Console (EMC) or Exchange Admin Center (EAC).

-  Confirm that the network configuration between DC and DR sites is properly set up for DAG communication, including replication network and MAPI network.

-  Ensure that the Witness Server and Witness Directory are configured correctly for both the DC and DR DAG configurations.

4.Power off or isolate the Exchange servers in the DC site to simulate a failure scenario.

-  Monitor the status of the databases within the DAG.

-  Use Exchange Management Shell (EMS) to check the status of databases and their copies: 

```
Get-MailboxDatabaseCopyStatus -Identity 
```

-  Look for any databases that have failed or dismounted.

6.Exchange DAG is designed to automatically handle failover scenarios based on predefined criteria like network connectivity and database health.

```
- Wait for Exchange to detect the failure and initiate automatic failover to the DR site.
```

7.After failover, verify that databases have been activated on servers in the DR site.

```
- Use EMS to check the active mailbox database copies:

   ```

   Get-MailboxDatabase -Server  | ft Name,Server,ActivationPreference,DatabaseCopies

   ```
```

8.Ensure that databases are active on DRMBX03 and DRMBX04 (DR site servers).

9.Send test emails to verify that mail flow is operational through the DR site.

```
- Monitor message queues and delivery reports to confirm that emails are being sent and received successfully.
```

10.Check Exchange Server event logs on servers in the DR site for any alerts or warnings related to DAG failover and database activation.

11.Once the drill is completed and documented, power on the DCMBX01 and DCMBX02 servers to restore normal operation.

12.Review the results of the drill to identify any areas for improvement in the DR setup or procedures.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-07-08*

Unless the File Share Witness is in a 3rd  datacenter, there will be no automatic failover between the two datacenters where the servers are.

You would need to do a manual switchover:

https://learn.microsoft.com/en-us/exchange/high-availability/manage-ha/datacenter-switchovers?view=exchserver-2019

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-08*

Hi @Dipto Adhikary,

Welcome to the Microsoft Q&A platform!

Performing a Disaster Recovery (DR) drill for an Exchange Server Database Availability Group (DAG) involves simulating a failure in your primary data center (DC) and ensuring that your secondary data center (DR) can take over automatically. Below are the steps you should follow to verify this scenario and ensure a seamless transition of databases from DC to DR:

Preparation

-  Verify DAG and Database Replication Health: Ensure that your DAG and database replication are healthy before you begin the DR drill. Use the following PowerShell commands:

    Get-DatabaseAvailabilityGroup -Identity DAGName | Format-List

    Get-MailboxDatabaseCopyStatus

    Test-ReplicationHealth

-  Confirm Witness Server Configuration: Ensure that the witness servers for both DC and DR are properly configured and accessible. This is crucial for maintaining quorum during the failover.

-  Documentation and Backup: Document your current configuration and take necessary backups of critical data.

Execution

-  Simulate DC Site Failure:

    - You can simulate the DC failure by disconnecting the network, shutting down the servers (DCMBX01, DCMBX02), or any method that mimics a sudden outage.

-  Monitor DAG:

    - Check the status of the DAG after the DC site goes offline. The Quorum should be maintained using the witness server configured for the DR site.

-  Failover Procedure:

    - The Automatic Database Mount Dial (ADMD) setting on your DAG influences automatic failover. Ensure it is configured to allow automatic mounting.

    - Use the following command to check and set ADMD if necessary:

      Get-DatabaseAvailabilityGroup -Identity DAGName | Select-Object *AutoDatabaseMountDial

      Set-DatabaseAvailabilityGroup -Identity DAGName -AutoDatabaseMountDial BestAvailability

    - Since you are simulating a real disaster scenario, monitor the event logs and replication status to ensure databases mount automatically.

-  Verify Active Copies in DR:

    - After the failover, verify that the databases have been mounted in the DR site using:

      Get-MailboxDatabaseCopyStatus

      Get-MailboxDatabase | Select-Object Name, Mounted, ActiveServer

Post-DR Drill

-  Review Logs and Health:

    - Check the event logs and replication health to ensure there were no errors during the failover process.

-  Bring DC Site Back Online:

    - Restore connectivity/power to the DC servers and ensure they rejoin the DAG and replication resumes.

-  Rebalance Databases:

    - Optionally, you may want to rebalance the databases back to your DC site or distribute them according to your standard operating procedures:

      Move-ActiveMailboxDatabase -Server DCMBX01 -ActivateOnServerPreference

    - Ensure the content index status is healthy before rebalance:

      Get-MailboxDatabaseCopyStatus | Select-Object Name, ContentIndexState

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
