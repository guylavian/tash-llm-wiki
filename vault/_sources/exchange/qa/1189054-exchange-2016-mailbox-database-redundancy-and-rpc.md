---
title: "Exchange 2016 Mailbox Database Redundancy and RPC issues after CU23 install"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1189054/exchange-2016-mailbox-database-redundancy-and-rpc
question_id: 1189054
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Mailbox Database Redundancy and RPC issues after CU23 install

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1189054/exchange-2016-mailbox-database-redundancy-and-rpc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have two Exchange 2016 servers in a DAG running on Server 2016. We installed CU23 this weekend and have been experiencing some issues since then. Initially we were unable to activate any databases on server 2 and were getting the following error:

`An Active Manager operation failed. Error: The database action failed. Error: An error occurred while trying to validate the specified database copy for possible activation. Error: server2: A server-side administrative operation has failed. The Microsoft Exchange Replication service may not be running on server server2.mydomain.local. Specific RPC error message: Error 0x6ba (The RPC server is unavailable) from cli_RpcsGetCopyStatusWithHealthState [Server: server2.mydomain.local] [Database: My DB02, Server: server1.mydomain.local]`

After restarting the Microsoft Exchange replication service on both servers I was able to activate databases on server 2 again but once they had been activated on that server, users with mailboxes on those databases were not able to open Outlook. Activating all of the mailboxes on server 1 and blocking activation on server 2 made them accessible again.

There are repeated Security-Kerberos errors in the System log on server 1:

`The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server server1$. The target name used was HTTP/server2.mydomain.local. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (mydomain.LOCAL) is different from the client domain (mydomain.LOCAL), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server`.

The SPNs look OK to me and there are no duplicates.

Get-MailboxDatabaseCopyStatus shows that there are healthy copies of all databases on both servers but there are numerous errors in the Application log on server 1 with ID 4374 from MSExchangeRepl saying:

`Database availability health check failed.`
`Database copy: My DB04`
`Redundancy count: 1`

Error: There were database availability check failures for database 'My DB04' that may be lowering its availability. Availability Count: 1. Expected Availability Count: 2. Detailed error(s): 

`server2:`
`The RPC to retrieve the status of database copy 'My DB04\Server2' failed. Error: A server-side administrative operation has failed. The Microsoft Exchange Replication service may not be running on server server2.mydomain.local. Specific RPC error message: Error 0x6ba (The RPC server is unavailable) from RpccGetCopyStatusEx4 [Server: server2.mydomain.local]`

Any ideas on what could be causing this and making us unable to activate mailboxdatabases on server2?

## Answers

_No answers on this thread._
