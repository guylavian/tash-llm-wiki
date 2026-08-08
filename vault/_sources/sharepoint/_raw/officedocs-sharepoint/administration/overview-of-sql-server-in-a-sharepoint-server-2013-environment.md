---
title: "Overview of SQL Server in a SharePoint Server 2013 environment - SharePoint Server"
description: "Learn about the SharePoint Server relationship with SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, and SQL Server 2014 and how you can interact with the databases."
ms.topic: concept-article
---
Note

Overview of SQL Server in a SharePoint Server 2013 environment

# Overview of SQL Server in a SharePoint Server 2013 environment

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server 2013 supports several versions of SQL Server. Depending on the installed version, you can use specific features of SQL Server, such as reporting and business intelligence (BI).

Note

SharePoint Foundation 2013 does not support BI features, which require SharePoint Server 2013.

The minimum requirements for a database server in SharePoint Server 2013 are SQL Server 2008 R2 with Service Pack 1 (SP1) or SQL Server 2012, or SQL Server 2014 64-bit versions. To use the business intelligence (BI) tools in SharePoint Server 2013 you must install SQL Server 2012 with Service Pack 1 (SP1) or SQL Server 2014, 64-bit version. For more information, see Hardware and software requirements for SharePoint Server 2016.

SharePoint Server 2013 and the SQL Server database engine

## SharePoint Server 2013 and the SQL Server database engine

The SharePoint Server 2013 application is built on the SQL Server database engine. Most content and settings in SQL Server 2008 R2 with Service Pack 1 (SP1), SQL Server 2012, and SQL Server 2014 are stored in relational databases. The following table shows the databases that SharePoint Server 2013 uses.

| **Database type** | **Description** |
| --- | --- |
| Configuration | The Configuration database and Central Administration content database are called configuration databases. They contain data about farm settings such as the databases that are used, Internet Information Services (IIS) web sites or web applications, solutions, Web Part packages, site templates, default quota, and blocked file types. A farm can only have one set of configuration databases. |
| Content | Content databases store all site content:  
  Site documents, such as files in document libraries  
  List data  
  Web Part properties  
  Data for apps for SharePoint  
  User names and permissions  
  Each web application can contain many content databases. Each site collection can be associated with only one content database, although a content database can be associated with many site collections. |
| Service application | Databases for service applications store the data that service applications use. |

For a full list of all of the databases that support SharePoint Server, see Database types and descriptions in SharePoint Server. For a graphical representation of the databases that support SharePoint Server 2013, see Databases that support SharePoint 20113.

Working with the SQL Server databases that support SharePoint Server 2013

## Working with the SQL Server databases that support SharePoint Server 2013

The databases that support SharePoint Server 2013 are either created automatically with the SharePoint Products Configuration Wizard or by database administrators when they manually configure SharePoint Server 2013.

Microsoft doesn't support directly querying or modifying the databases that support SharePoint Server. In SharePoint Server the Usage and Health Data Collection database does support schema modifications.

The SQL Server databases that support SharePoint Server 2013 are subject to sizing limitations and to configuration recommendations that aren't standard for SQL Server. For more information, see Storage and SQL Server capacity planning and configuration (SharePoint Server).

SQL Server 2008 R2 with Service Pack 1 (SP1)

## SQL Server 2008 R2 with Service Pack 1 (SP1)

SQL Server 2008 R2 introduced Power Pivot for SharePoint and Power Pivot for Excel 2010 for SharePoint business intelligence capability through integration with SharePoint Server 2010. Both SQL Server Analysis Services and SQL Server Reporting Services can run in the same SharePoint Server farm. SQL Server 2008 R2 with Service Pack 1 (SP1) introduced various new features and fixed many SQL Server 2008 R2 issues. For more information, see "1.0 What's New in Service Pack 1" in Microsoft SQL Server 2008 R2 SP1 Release Notes.

SQL Server Reporting Services in SharePoint Integrated Mode

### SQL Server Reporting Services in SharePoint Integrated Mode

SQL Server 2008 R2 Reporting Services supports two types of SharePoint integration. Full integration relies on the SharePoint integrated mode. Partial integration relies on two Web Parts, Report Explorer and Report Viewer, which you must install on a SharePoint site and point to a remote report server instance. For more information, see Overview of Reporting Services and SharePoint Technology Integration and Planning for SharePoint Integration.

Note

Reporting Services supports SharePoint integrated mode using SharePoint Server 2013 only.

When you set up Reporting Services with SharePoint Server 2013, you create a report server. The report server is the central component of Reporting Services. This component contains two processing engines and a set of unique extensions that handle authentication, data processing, rendering, and delivery operations.

Note

When you configure a report server to run with SharePoint Server 2013 in integrated mode you must install the SQL Server 2012 Reporting Services add-in or later on a SharePoint front-end web server. > SQL Server 2008 R2 is the minimum version and is not supported when you use SQL Server 2012 Reporting Services or SQL Server 2014 Reporting Services.

For more information, see Supported Combinations of SharePoint and Reporting Services Components. The following levels of integration are provided when you run a report server in integrated mode with SharePoint Server 2013.

Shared storage

Shared security

Same site access for all business documents such as reports, report models, and shared data sources

When Reporting Services runs in SharePoint integrated mode, both the SharePoint content and report server databases store content and metadata. The following table shows the report server data that each database stores.

| **Name of database** | **Report server data** |
| --- | --- |
| SharePoint content | Primary storage for the following data:  
  Published reports  
  Report models  
  Shared data sources  
  Resources  
  Properties  
  Permissions |
| SharePoint configuration | All report server configuration settings that you make in Central Administration including:  
  Report server URL  
  Report server Reporting Services account information  
  Information about the authentication provider that is used on the server  
  Site-level settings that limit or enable report history and logging |
| Report server | Internal copies of report content and metadata, which are also stored in the SharePoint content database, and the following report data:  
  Schedules  
  Subscriptions  
  Snapshots for report history or report execution |
| Report server Temp | Temporary data, including the following:  
  Session data  
  Temporary snapshots created for subscription processing, interactive reporting, or report caching as a performance improvement |

Reporting Services data alerts are available to inform recipients of changes in report data.

For more information, see Storing and Synchronizing Report Server Content With SharePoint Databases

SQL Server 2012 and SQL Server 2014

## SQL Server 2012 and SQL Server 2014

SQL Server 2012 with SP1 and SQL Server 2014 provide business intelligence solutions for SharePoint Server 2013. The SharePoint mode of SQL Server 2012 provides features for SQL Server Analysis Services and SQL Server Reporting Services. In addition, the SharePoint mode provides SQL Server BI features in SharePoint Server 2013. For more information, see Features Supported by the Editions of SQL Server 2012 and Features Supported by the Editions of SQL Server 2014.

Note

SharePoint Foundation 2013 does not support SQL Server BI features.

High Availability Solutions

### High Availability Solutions

We recommend Always On Availability Groups for high availability in SQL Server 2012 Reporting Services and SQL Server 2014 Reporting Services. Other high availability solutions are Always On Failover Cluster Instances, database mirroring, and log shipping. Both Always On Availability Groups and Failover Cluster Instances solutions require and use Windows Server Failover Clustering (WSFC).

Note

We recommend that you use Always On Availability Groups instead of database mirroring for your high availability solution with SQL Server 2012 or SQL Server 2014 and SharePoint Server 2013. For more information, see Overview of SQL Server High-Availability Solutions.

For more information, see Always On Availability Groups (SQL Server), and Prerequisites, Restrictions, and Recommendations for Always On Availability Groups (SQL Server).

Reporting Services SharePoint mode

### Reporting Services SharePoint mode

SharePoint mode in SQL Server 2012 Reporting Services and SQL Server 2014 Reporting Services is a SharePoint Server 2013 shared service that you configure in either the SharePoint Central Administration website or by using Reporting Services SharePoint mode Microsoft PowerShell cmdlets. For more information, see PowerShell cmdlets (Reporting Services SharePoint Mode). SharePoint mode supports SharePoint Server 2013 backup and restore for SQL Server Reporting Services service application and Unified Logging Service (ULS) trace logs. SharePoint mode also supports claims-based authentication. For more information, see the "SharePoint Mode" section of What's New (Reporting Services). For more information about the SharePoint Microsoft PowerShell cmdlets for ULS, see Logging and events cmdlets in SharePoint 2013.

SharePoint mode requires that a report server component of Reporting Services must run within a SharePoint Server farm. This means that a SharePoint application server must exist with the Reporting Services shared service installed and at least one Reporting Services service application.

For more information, see Reporting Services Report Server (SSRS) and Reporting Services Report Server (SharePoint Mode).

Business intelligence features

### Business intelligence features

Note

SharePoint Foundation 2013 does not support BI features, which require SharePoint Server 2013.

When you install SQL Server 2012 Analysis Services (SSAS) and SQL Server 2012 Reporting Services (SSRS) in a SharePoint Server 2013 farm the following business intelligence features are enabled:

SQL Server 2012 Power Pivot for SharePoint 2013

Power View for SharePoint 2013

Reporting Services interactive report designer that runs on Power Pivot or Analysis Services tabular data models

The xVelocity in-memory analytics engine in SQL Server 2012 supports both self-service BI and corporate BI. For more information, see xVelocity in SQL Server 2012.

For more information, see Best practices for SQL Server in a SharePoint Server farm, Install SQL Server BI Features with SharePoint 2013 (SQL Server 2012 SP1), and Install SQL Server BI Features with SharePoint (PowerPivot and Reporting Services).

For more information, see Install SQL Server BI Features with SharePoint (PowerPivot and Reporting Services).

Power Pivot for SharePoint 2013

### Power Pivot for SharePoint 2013

SQL Server 2012 with SP1 is required to deploy Power Pivot for SharePoint 2013. Power Pivot for SharePoint 2013 is a SharePoint Server service application that becomes available when Analysis Services runs in SharePoint mode. This provides a server that hosts Power Pivot data in a SharePoint farm. SQL Server 2012 Analysis Services provides three modes for analysis, Multidimensional, Tabular, and Power Pivot for SharePoint. Each server mode is independent of the others, and each supports a type of analytical database that only runs in that modality. For more information about SQL Server 2012 Analysis Services (SSAS), see Analysis Services. For more information about SQL Server 2014 Analysis Services, see Analysis Services. The server that hosts Power Pivot for SharePoint 2013 can be outside a SharePoint Server 2013 farm.

To configure Power Pivot for SharePoint you can use the SharePoint Central Administration website, the Power Pivot for SharePoint 2013 Configuration tool, or Microsoft PowerShell cmdlets. The following table lists each method and describes the process:

| **Power Pivot for SharePoint Configuration method** | **Description** |
| --- | --- |
| SharePoint Server 2013 Central Administration | Provides all available options to configure the Power Pivot for SharePoint service application. |
| Power Pivot for SharePoint 2013 Configuration Tool | Evaluates an existing installation and determines what needs to be configured in the SharePoint farm and Power Pivot for SharePoint and then configures everything required. |
| Microsoft PowerShell cmdlets | Provides cmdlets that you can use to build PowerShell script files (.ps1) and automate the configuration process for Power Pivot for SharePoint. |

The Power Pivot for SharePoint 2013 add-in enables PowerPivot Gallery, Schedule Data Refresh, and the PowerPivot Management Dashboard in Central Administration. For more information, see PowerPivot for SharePoint (SSAS).

See also

## See also

Other Resources

#### Other Resources

Supported Combinations of SharePoint and Reporting Services Components

What's New (Analysis Services)

Features Supported by the Editions of SQL Server 2014

Deprecated Database Engine Features in SQL Server 2014

Additional resources

## Additional resources

- Last updated on 
		2024-12-02
