---
title: "IP-less DAG and NIC Issues in Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2073973/ip-less-dag-and-nic-issues-in-exchange-server
question_id: 2073973
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# IP-less DAG and NIC Issues in Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2073973/ip-less-dag-and-nic-issues-in-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone!

I have IP-less Database Availability Group in my Exchange Server 2019 with DC & DR site. The DAG network is worked smoothly but after adding an additional NIC for database backup, I've encountered the following Issue:

-  When checking the network health, I receive errors indicating that there is multiple network interfaces configured for registration in DNS for the DAG, and both NIC/ subnets is "Misconfigured”, but servers’ status is “UP”.

-  Mail sends by the backup’s NIC

After changing the network adapter priorities mail sends by the Mapi Network, and it was expected.

To fix the Dag network misconfigured issue, I have unchecked the “Register this connection’s addresses in DNS” checkbox in NIC and below attached.

After unchecking it, DAG automatically dictated the backup’s network as “Replication DAG Network” and misconfigured issue is solved. Then I attempting to remove the (backup NIC / Replication DAG Network) with Remove-DatabaseAvailabilityGroupNetwork, I receive the following error:

'Remove-DatabaseAvailabilityGroupNetwork' is disabled because database availability group 'EXNEWDAG' is configured for automatic network configuration.

Goals:

-  I want to keep the automatic DAG configuration and ensure that only the MapiDagNetwork is used for both MAPI and replication.

-  I would like guidance on how to properly disable or exclude the backup NIC from affecting the DAG without switching to manual configuration.

Questions:

-  Is there a way to configure the DAG to ignore the backup NIC while keeping automatic network configuration?

-  What steps should I take to resolve the "Misconfigured" state for the MapiDagNetwork?

Any help or guidance would be greatly appreciated!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-20*

Hi,

Welcome to Microsoft Q&A community!

Steps to Achieve Your Goals:

-  Configure the DAG to Ignore the Backup NIC:

To ensure the DAG ignores the backup NIC while keeping automatic network configuration, you can follow these steps:

-  Uncheck DNS Registration: As you’ve already done, uncheck the “Register this connection’s addresses in DNS” checkbox for the backup NIC.

-  Disable Replication on Backup NIC: Ensure that the backup NIC is not used for replication. You can do this by setting the replication property to `False` for the backup NIC.

Here’s a PowerShell command to disable replication on the backup NIC:

```
Set-DatabaseAvailabilityGroupNetwork -Identity EXNEWDAG\BackupNetwork -ReplicationEnabled $false
```

-  Resolve the “Misconfigured” State for the MapiDagNetwork:

To resolve the “Misconfigured” state for the MapiDagNetwork, follow these steps:

-  Verify Subnets: Ensure that the subnets for the MapiDagNetwork are correctly configured and do not overlap with other networks.

-  Check Network Interfaces: Make sure that the network interfaces associated with the MapiDagNetwork are correctly configured.

You can use the following PowerShell command to check the configuration of the MapiDagNetwork:

```
Get-DatabaseAvailabilityGroupNetwork -Identity EXNEWDAG\MapiDagNetwork | Format-List
```

If you need to adjust the subnets or network interfaces, you can use the `Set-DatabaseAvailabilityGroupNetwork` cmdlet. For example:

```
Set-DatabaseAvailabilityGroupNetwork -Identity EXNEWDAG\MapiDagNetwork -Subnets 192.168.1.0/24
```
