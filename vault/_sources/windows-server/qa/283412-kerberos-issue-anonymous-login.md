---
title: "Kerberos Issue - Anonymous Login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/283412/kerberos-issue-anonymous-login
question_id: 283412
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-tsql", "sql-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Kerberos Issue - Anonymous Login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/283412/kerberos-issue-anonymous-login (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a linked server that connects one SQL Server to another SQL Server. For two weeks now there has been an error when testing the connection;   

Login failed for user 'NT AUTHORITY\ANONYMOUS LOGON'. (.Net SqlClient Data Provider)  

I have posted about this issue when I first received the user was complaining about it. The projected solution was to manually register the SPN. Our environment already has SPN registered to the service account names for each of the servers. Below are the ways me and my team troubleshooted:   

-  Used the Kerberos Configuration tool to check if there were any issues with SPNs. Yes there was in fact an issue with multiple SPNs which were shown as "Misplaced" in the Kerberos tool. So we updated the SPN's and the status returned to "Good"  

-  Checked CMD -setspn -l to view the list of the services and the service we are looking for with the correct port number is one of the service account under the SPN.   

-  Restarted the SQL Server services to make sure the updates take full effect.   

-   Used DMV to find out the authentication scheme being used. Kerberos authentication is being used.   

-  Queried the data the user has requested to see that the anonymous issue is still present.   

-  Tested the connection to the linked server and the anonymous issue is still present.   

-  Checked the error log to see an error that states:   

The SQL Server Network Interface library could not register the SPN [XXXX] for the SQL Server service. Windows return code: 0x2098, state 15. Failure to register a SPN might cause integrated authentication to use NTLM instead of Kerberos.   

-  I have notified the Windows AD team to check the delegation status. He has confirmed that the delegation is set to: 'Trust this user for delegation to any service (Kerberos only)'   

I am running out of ideas on how much further I can troubleshoot or where the problem lies. If anyone has any other idea, please feel to share and give some feedback. Thank you in advance.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-22*

The SPN is registered when you install SQL Server, and normally never needs changed.  The warning in the log file, just means the user running the SQL Server service was not able to verify the SPN exists.  Usually because it does not have permissions.  This is NOT an indication of a problem and likely has nothing to do with your issue.    

These problems almost always fall into a "double hop" issue, delegation or multiple domains.  Without knowing more about your login situation and how your systems are setup, it is hard to guess.  

What account did they set delegation on?  Did you restart the SQL Server Database Service after setting delegation?  

I suggest you start here:  

https://www.mssqltips.com/sqlservertip/2312/understanding-when-sql-server-kerberos-delegation-is-needed/

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-23*

Hi,

>The SQL Server Network Interface library could not register the SPN [XXXX] for the SQL Server service. Windows return code: 0x2098, state 15. Failure to register a SPN might cause integrated authentication to use NTLM instead of Kerberos.

This is an informational message and not actually an error. And seeing this information is not sure that Kerberos will not be used. I believe you check the DMV (auth_scheme in sys.dm_exec_connections) and find that Kerberos has been used.  

There are two scenarios in which you will see this message. Check the article for more details.

>Login failed for user 'NT AUTHORITY\ANONYMOUS LOGON'. (.Net SqlClient Data Provider)

Your scenario seems to be a typical double-hop authentication scenario, that is, the front-end client connects to the linked server on SQL Server 1 in the middle and finally accesses the back-end SQL Server 2 to obtain data. The double-hop authentication requires Kerberos technology. Make sure selected the "Be made using the login's current security context" option when create the link server and configuring security.

Please check the following posts.  

https://stackoverflow.com/questions/12462674/sql-server-returns-error-login-failed-for-user-nt-authority-anonymous-logon

You need to turn off the "Account is sensitive and cannot be delegated" property of the domain account used by the client to connect to SQL Server in AD, so that it can do delegation.
