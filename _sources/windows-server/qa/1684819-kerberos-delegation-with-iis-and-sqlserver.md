---
title: "Kerberos Delegation with IIS and SQLServer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1684819/kerberos-delegation-with-iis-and-sqlserver
question_id: 1684819
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other", "windows-development-iis"]
answer_author_roles: ["Q&A User"]
---
# Kerberos Delegation with IIS and SQLServer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1684819/kerberos-delegation-with-iis-and-sqlserver (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have the following environment:

-  Domain controller DomCtrl Win2016   Delegation in AD: Do not trust this computer for delegation

-  Member server Sqlserver: Win2016 with SQLServer 2019   Delegation in AD: Do not trust this computer for delegation   The SQLService runs under a domain account with the Kerberos SPNs

-  MSSQLSvc/sqlserver.vagintern3.local

-  MSSQLSvc/sqlserver.vagintern3.local:1433

-  Member server Webserver Win2016 with IIS   Delegation in AD: Trust this computer to delegate to any service (Kerberos only)   The ApplicationPool runs with the pool identity.

A .NetCore web application with Windows authentication runs on the IIS server, which uses a trusted connection to the SQL server. A user UserA of the web application is therefore authenticated to the web application with his AD account UserA.

The aim is for the connection from the web application on the web server to the SQL server to be established via the user's user account UserA. This means that the authentication of the user UserA on the WebApplication is passed on to the SQL server. Since according to the documentation this only works via Kerberos, I carried out the Kerberos configuration described above.

Unfortunately, the web application connects to the computer account WebServer$ - and not with the user UserA.

Does somebody has any idea?

Thank you and best regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-18*

Hello everyone,   

it took a while - but now it's solved:

-  The SPNs above must be set up for the SQL services account

-  The delegation settings on the web server must match the SQL services account SPNs:

-  Option: Trust this computer for delegation to specified services only

-  Option: Use any authentication protocol

-  Option: Services to which the account can present delegated credentials:

   The AspNet.Core web app must support Windows authentication (also set additionally in IIS) and the SQL server requests must be personalized with the HttpContext.

Best regards, 

Volkhard

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-22*

IIS also needs to be configured to use windows authentication and the negotiate provider. Then you need to configure Kerberos support in the asp.net core app. 

To call the SqlServer with the browsers client, you need to impersonate the user on the thread connecting to SqlServer. You will want to disable pooling because you need a fresh connection from the thread. See

https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-8.0&tabs=visual-studio

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-22*

Hi，volkhardv

It looks like your SQL server service has successfully registered SPNs in the domain. 

Here are the possible solutions:

-  Use the following command in PowerShell: 

```
Get-ADUser UserA -Properties
```

Check the `AccountNotDelegated` property in the output to ensure its value is `False`. 

If it is 'True', you will need to: 

-  Locate the user account UserA that needs to be modified in AD. 

-  Right-click on the user account, and then select "Properties". 

-  In the user properties window, switch to the "Account" tab. 

-  Find the checkbox for "Account is sensitive and cannot be delegated". 

-  If the "Account is sensitive and cannot be delegated" is checked, uncheck it.

2.Change the identity of the application pool: 

If currently set to "Network Service", "Local System", or "ApplicationPoolIdentity", it should be changed to use a specific domain account. 

-  Click the "..." button next to the "Identity" property. 

-  Select the "Custom account" option, then click "Set". 

-  Enter the username and password of the domain account with delegation permissions. 

-  Confirm and apply changes.

Confirm the delegation permissions for the domain account: 

-  Ensure that the domain account you have configured for the application pool has the correct delegation permissions set up in Active Directory. 

-  In the Active Directory Users and Computers management console, find the account and open its properties. 

-  Check the "Delegation" tab to make sure "Trust this user for delegation to any service (Kerberos only)" is enabled or delegation has been configured for specified services (e.g., SQL Server).

3.Ensure that the time is synchronized within five minutes between all clients, servers, and domain controllers.

Best Regards,

Mikey Qiao

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
