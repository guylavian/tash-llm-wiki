---
title: "Software requirements for Database Servers for SharePoint Server Subscription Edition - SharePoint Server"
description: "Introduces articles that describe software and other requirements for SharePoint Server Subscription Edition."
ms.topic: article
---
Note

Software requirements for Database Servers for SharePoint Server Subscription Edition

# Software requirements for Database Servers for SharePoint Server Subscription Edition

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Operating systems

## Operating systems

SharePoint Server Subscription Edition supports database servers deployed on the following operating systems:

- Windows Server 2019 Standard or Datacenter

- Windows Server 2022 Standard or Datacenter

- Windows Server 2025 Standard or Datacenter

SharePoint Server Subscription Edition supports database servers deployed with the following Windows Server installation options:

- Server with Desktop Experience

- Server Core

Database versions

## Database versions

SharePoint Server Subscription Edition supports the following database versions:

A Standard or Enterprise Edition of SQL Server for Windows that supports database compatibility level 150. This includes SQL Server 2019 Cumulative Update 5 (CU5) or later, SQL Server 2022, and any future version of SQL Server for Windows that supports database compatibility level 150. For more information about database compatibility levels, see Compatibility Certification and ALTER DATABASE (Transact-SQL) Compatibility Level.

Microsoft Azure SQL Managed Instance (MI). This is only supported if your SharePoint Server farm is hosted in Microsoft Azure. For more information, see Deploy SharePoint Server with Azure SQL Managed Instance.

Note

SQL Server products and all future SQL Server Cumulative Updates (CUs) are supported through the SQL Server product lifecycle.

Note

SQL Server Express isn't supported. Azure SQL Database (the non-Managed Instance DBaaS service) is also not supported for any SharePoint databases.

Additional resources

## Additional resources

- Last updated on 
		2023-06-05
