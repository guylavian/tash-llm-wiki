---
title: "What is needed to make a Kerberos authentication to connect to SQL server?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1155353/what-is-needed-to-make-a-kerberos-authentication-t
question_id: 1155353
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# What is needed to make a Kerberos authentication to connect to SQL server?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1155353/what-is-needed-to-make-a-kerberos-authentication-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am trying to connect to the SQL server via Kerberos authentication by following this document, and I have two questions about the requirement of Kerberos authentication.

The first question

In the step "Service principal names" I follow the document "Register a Service Principal Name for Kerberos Connections" mentioned in this step, which tells me what the necessary permissions are.

However, after setting up the permissions, the automatic SPN registration still failed.

The process I setting up the permissions is:

-   Create a user `mssql-startup` in the OU of my domain with Active Directory Users and Computers.        

-   Right-click the SQL server computer and select Properties, and select the Security tab and click Advanced, and click Add    

-   Click Select a principal and enter the startup account `mssql-startup`, then click OK.    

-   Select "Validated write to service principal name", "Read servicePrincipalName" and "Write servicePrincipalName", then click OK.    

-   Click OK twice, and close Active Directory Users and Computers.

-   In the SQL server computer, open Sql Server Configuration Manager, right click the SQL Server, login with the startup account, then click OK to make it restart.    (sorry for the language isn't English)  

    

-   In the log of the SQL server, it says that the SPN failed to register.    

Is there any step wrong or missing?

The second question

The document also mentions that I can add a `userName`, and `password` to the connection string to make a Kerberos connection.

That confuse me, what do I really need to make a Kerberos authentication?  

Run `kinit` before the Kerberos authentication, specifying configuration files, or adding `userName`, and `password` to the connection string?

Therefore, I try these tests (Note: the SQL server startup account is Administrator due to question 1):

It seems in order to make a Kerberos connection, I only need to run `kinit` or specify `userName` and `password` to the connection string.

I know not specifying the JAAS configuration file will make it use the default value,  

and the default behavior of not specifying the Kerberos configuration file (krb5.conf) seems like is pointing to the default krb5.conf (e.g., /etc/krb5.conf in RHEL 8).

However, when I run a Java application (I use Camunda for testing) deployed with Docker container,  

it seems like adding `userName`, and `password` to the connection string (test case 7) is enough to make a Kerberos authentication since there's no krb5.conf in the container.

Does that mean if I specify `userName` (contains realm) and `password` to the connection string, I don't need to do anything else for Kerberos Authentication?  

I'm just worried that it run successfully by coincidence (something I don't know has been set up properly).

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-10*

I am not sure if your steps to grant Read/Write permissions to account are correct but you can use DSACL snippet to grant this permissions

```
dsacls <DomainName_of_Service_Account> /G SELF:RPWP;"servicePrincipalName"
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-09*

Hi @Kent010341       

I'm not an expert on Kerberos, but I've found some links for you that might help.    

Using Kerberos Configuration Manager for SPNs Validation    

Overview of Service Principal Name and Kerberos authentication in SQL Server    

Best regards,    

Li Hong    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our Documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
