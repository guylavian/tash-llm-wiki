---
title: "Expired sessions are not being deleted from the ASP.NET Session State database (SharePoint Server) - SharePoint Server"
description: "Learn how to resolve the SharePoint Health Analyzer rule: Expired sessions are not being deleted from the ASP.NET Session State database, for SharePoint Server."
ms.topic: troubleshooting
---
Note

Expired sessions are not being deleted from the ASP.NET Session State database (SharePoint Server)

# Expired sessions are not being deleted from the ASP.NET Session State database (SharePoint Server)

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** Expired sessions are not being deleted from the ASP.NET Session State database.

**Summary:** If expired sessions are not deleted, the server that hosts the ASP.NET Session State database may run out of disk space and the SharePoint farm may cease to function.

**Cause:** One or more of the following might be causing this:

The SQL Server Agent service was stopped.

SQL Server Express is installed.

Important

You cannot run the SQL Server Agent service on an instance of SQL Server Express.

**Resolution: Start the SQL Server Agent service**

Verify that the user account that is performing this procedure is a member of the Administrators group on the database server that is hosting the ASP.NET Session State database.

In **SQL Server Configuration Manger**, start the **SQL Server Agent service**.

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
