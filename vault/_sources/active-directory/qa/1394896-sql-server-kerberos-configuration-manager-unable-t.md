---
title: "SQL Server - Kerberos Configuration Manager - Unable to connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1394896/sql-server-kerberos-configuration-manager-unable-t
question_id: 1394896
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# SQL Server - Kerberos Configuration Manager - Unable to connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1394896/sql-server-kerberos-configuration-manager-unable-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all -

I am currently working through replacing a development and production SQL server, moving from server 2012 to server 2022.

These two servers have the SQL Service running as an AD account. Thus, I have gone through and configured the proper SPNs in Active Directory and configured Kerberos Constrained Delegation.

Adding the SPN for the FQDN and hostname, with and without port (1433) on the AD account the SQL Service is running under.  Going to the delegation tab for that user account and adding the MSSQLSVC<hostname> and MSSQL<FQDN> with and without port.  Going to the AD Computer object of each of the two servers, to the delegation tab and adding the server that I am looking for these two servers to access via a cifs share.

When I login to SSMS from my PC to connect to these servers and run the query:

`use master`

`GO`

`SELECT COUNT(auth_scheme) as sessions_count, net_transport, auth_scheme`

`FROM sys.dm_exec_connections`

`GROUP BY net_transport, auth_scheme`

I can see that the my TCP connection has an auth_scheme as KERBEROS.

However, when I try to launch the Kerberos Configuration Manager and try to connect to the local host (leaving the server name, use name, and password blank - while on the server as an admin) - I get the following:

"Unable to connect to server, please ensure that the server name is correct, SQL Server is installed properly, and the user has administrator permissions.  If the problem persists, please contact Microsoft Support."

I am an administrator on the server, ran the application as administrator.  I'm not really sure where to look from here.  Any help or tips would be appreciated.

Thanks

Steve

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-02-09*

The answer to this is that you cannot use the Kerberos Configuration Manager and connect successfully to Windows 2022 or SQL 2022. The support stops at Windows 2019. There is nothing that Microsoft Support can do for you and nothing that you are doing wrong if the OS is > Windows 2019.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-09*

Supported Operating Systems
Windows Server 2008, Windows Server 2016, Windows 10, Windows Server 2012 R2, Windows Server 2008 R2 SP1, Windows Server 2012, Windows 7, Windows 8, Windows Server 2019
Supported SQL Server versions  

SQL Server 2008 through SQL Server 2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-18*

leaving the server name, use name, and password blank

You leave everything "blank", even the server name? How could the tool guess where to connect to?

Enter server name and select Windows auth for connecting to SQL Server.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-18*

Hi @stephenmbell  

Unable to connect to server, please ensure that the server name is correct, SQL Server is installed properly, and the user has administrator permissions. If the problem persists, please contact Microsoft Support.

I'd like to suggest you may open a ticket to Microsoft support and the engineers will give the professional advice and help resolve the issue.

Services Hub (microsoft.com)

Regards，

Zoe Hui

If the answer is helpful, please click "Accept Answer" and upvote it.
