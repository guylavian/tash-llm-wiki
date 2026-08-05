---
title: "Cannot access ECP on new Exchange 2019 server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1074713/cannot-access-ecp-on-new-exchange-2019-server
question_id: 1074713
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Cannot access ECP on new Exchange 2019 server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1074713/cannot-access-ecp-on-new-exchange-2019-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Just installed an Exchange 2019 server into an environment that contains two Exchange 2013 servers. The plan is to migrate to 2019 and decommission the 2013 servers. On the new server I am unable to log in to ECP. This is the error I get:

Configuration Error  

Description: An error occurred during the processing of a configuration file required to service this request. Please review the specific error details below and modify your configuration file appropriately.

Parser Error Message: Could not load file or assembly 'Microsoft.Exchange.HttpRedirectModules, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.

Source Error:

Line 36: <compilation defaultLanguage="c#" debug="false">  

Line 37: <assemblies>  

Line 38: <add assembly="Microsoft.Exchange.HttpRedirectModules, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />  

Line 39: </assemblies>  

Line 40: </compilation>

Source File: C:\inetpub\wwwroot\web.config Line: 38

Assembly Load Trace: The following information can be helpful to determine why the assembly 'Microsoft.Exchange.HttpRedirectModules, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' could not be loaded.

=== Pre-bind state information ===  

LOG: DisplayName = Microsoft.Exchange.HttpRedirectModules, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35  

(Fully-specified)  

LOG: Appbase = file:///C:/inetpub/wwwroot/  

LOG: Initial PrivatePath = C:\inetpub\wwwroot\bin

Calling assembly : (Unknown).

LOG: This bind starts in default load context.  

LOG: Using application configuration file: C:\inetpub\wwwroot\web.config  

LOG: Using host configuration file: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet.config  

LOG: Using machine configuration file from C:\Windows\Microsoft.NET\Framework64\v4.0.30319\config\machine.config.  

LOG: Post-policy reference: Microsoft.Exchange.HttpRedirectModules, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35  

LOG: Attempting download of new URL file:///C:/Windows/Microsoft.NET/Framework64/v4.0.30319/Temporary ASP.NET Files/root/e22c2559/92c7e946/Microsoft.Exchange.HttpRedirectModules.DLL.  

LOG: Attempting download of new URL file:///C:/Windows/Microsoft.NET/Framework64/v4.0.30319/Temporary ASP.NET Files/root/e22c2559/92c7e946/Microsoft.Exchange.HttpRedirectModules/Microsoft.Exchange.HttpRedirectModules.DLL.  

LOG: Attempting download of new URL file:///C:/inetpub/wwwroot/bin/Microsoft.Exchange.HttpRedirectModules.DLL.  

LOG: Attempting download of new URL file:///C:/inetpub/wwwroot/bin/Microsoft.Exchange.HttpRedirectModules/Microsoft.Exchange.HttpRedirectModules.DLL.  

LOG: Attempting download of new URL file:///C:/Windows/Microsoft.NET/Framework64/v4.0.30319/Temporary ASP.NET Files/root/e22c2559/92c7e946/Microsoft.Exchange.HttpRedirectModules.EXE.  

LOG: Attempting download of new URL file:///C:/Windows/Microsoft.NET/Framework64/v4.0.30319/Temporary ASP.NET Files/root/e22c2559/92c7e946/Microsoft.Exchange.HttpRedirectModules/Microsoft.Exchange.HttpRedirectModules.EXE.  

LOG: Attempting download of new URL file:///C:/inetpub/wwwroot/bin/Microsoft.Exchange.HttpRedirectModules.EXE.  

LOG: Attempting download of new URL file:///C:/inetpub/wwwroot/bin/Microsoft.Exchange.HttpRedirectModules/Microsoft.Exchange.HttpRedirectModules.EXE.

Here is what I've tried so far to fix this:  

-  Confirmed paths are correct in web.config files  

-  Used DependentAssemblyGenerator.exe to create sharedwebconfig.config in C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess, and C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy  

-  I've also done IISReset multiple times as well as rebooted the server

Is there anything else I can do to fix this or should I just open a case with Microsoft support?

## Answer (community) — Volunteer Moderator

*upvotes: 1 · updated: 2022-11-03*

Hi    

The ECP try to redirect you to the 2013's server. Please try with https://localhost/ecp?ExchClientVer=15.2    

In your error code you see Version=15.0.0.0, which is the 2013's version.    

That process happen as the admin mailbox is still inside the 2013, it's why Exchange redirect you, but with the tip above you can go in the ecp.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-09*

We've discovered that the virtual directories did not get created in IIS at all. We are working with Microsoft support on the issue.    

Thanks for the suggestions.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-04*

Does Exchange Management Shell work fine?    

Have you tried recreating the ECP and OWA virtual directories?    

The detailed steps are introduced in this link: Recreate virtual directories in Exchange Server.    

Please refer to the Recreate EcpVirtualDirectory and Recreate OwaVirtualDirectory part.    

Also, check this article for more insight - https://www.stellarinfo.com/blog/exchange-server-http-500-error-ecp/
