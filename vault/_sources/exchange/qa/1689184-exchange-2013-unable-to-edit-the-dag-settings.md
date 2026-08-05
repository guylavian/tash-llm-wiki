---
title: "Exchange 2013 unable to edit the DAG settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1689184/exchange-2013-unable-to-edit-the-dag-settings
question_id: 1689184
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange 2013 unable to edit the DAG settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1689184/exchange-2013-unable-to-edit-the-dag-settings (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My environment is Exchange 2013 with a single CAS server and a DAG with two servers in the primary site and one server at the DR/secondary site. I am facing an issue where, when I try to edit the DAG properties, I receive the error message: "The Microsoft Replication service may not be running on server ABCD. Error: Error 0x6d9 (There are no more endpoints available from the endpoint mapper from the cli_RpccGetDBSeedStatus)."

I received the same error while creating a database copy on another server: "The seeding operation failed. Error: The Microsoft Replication service may not be running on server. Error: Error 0x6d9 (There are no more endpoints available from the endpoint mapper from the cli_RpccGetDBSeedStatus)."

The current situation is that the databases are now mounted, but when I switch the database from the primary server to the second server, Outlook disconnects and goes into a disconnected state.

I changed the File Share Witness path, but mistakenly added another one, and now two paths are showing for the File Share Witness.

This situation is quite messed up, and I need support to ensure the databases can smoothly transition from one server to another.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-03*

Hi @Innocent Heartvoice,

Welcome to the Microsoft Forum for technical support.

 

Thanks for your detailed description. The issue you are experiencing involves DAG (Database Availability Group) in Exchange 2013. Below I will give you some initial suggestions for the issue you are experiencing.

 

First, let's deal with the error message "The Microsoft Replication Service might not be running on server ABCD. Error: Error 0x6d9". This error is usually related to RPC connectivity. Here are some possible solutions:

-  Check RPC connectivity: Make sure that the Microsoft Exchange Active Directory Topology service on server ABCD can communicate via RPC. You can try to verify this error through a web logon. If it is a port issue, you may need to check the settings of the new router.

-  Check DNS records: Make sure that the DNS records are correct. Sometimes incorrect DNS records can cause this type of problem.

 

Next, let's resolve the "Seeding operation failed" issue. This is usually related to the DAG network configuration. Here are some steps:

-  In the Exchange Management Console (EAC), go to Servers > Database Availability Groups.

-  Confirm your DAG network configuration. You can manually configure the DAG network in the DAG network properties. If you can't find the manual configuration option in the EAC, you can use the Exchange Management Shell to run the following command to display the DAG network configuration settings and verify that the DAG network was successfully configured:   Get-DatabaseAvailabilityGroupNetwork <DAGNetworkName> | Format-List

-  Make sure the DAG network is configured correctly, including the IP address and subnet.

-  If you changed the file share witness path, make sure the path is correct. You can use the following command to view the current status of the DAG witness server:   Get-MailboxDatabaseCopyStatus -Server <ServerName>

Please feel free to contact me if you have any queries.

Best,

Jake Zhang

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-30*

Exchange 2013 is out of support. 

My recommendation is to not continue to troubleshoot this and build a new DAG using Exch 2019.

Then migrate your mailboxes and settings to the new servers

You can use the Deployment Asst to assist in the migration:

https://learn.microsoft.com/en-us/exchange/exchange-deployment-assistant?view=exchserver-2019
