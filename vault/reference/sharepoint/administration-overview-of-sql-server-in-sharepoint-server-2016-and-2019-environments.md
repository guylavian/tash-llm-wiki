---
title: "Overview of SQL Server in a SharePoint Server 2016 environment - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-overview-of-sql-server-in-sharepoint-server-2016-and-2019-environments
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/overview-of-sql-server-in-sharepoint-server-2016-and-2019-environments
family: administration
documentKind: "concept-article"
abstract: "Learn about the SharePoint Server relationship with SQL Server and how you can interact with the databases."
---

# Overview of SQL Server in a SharePoint Server 2016 environment - SharePoint Server

Note

Overview of SQL Server in SharePoint Server 2016 and 2019 environments

# Overview of SQL Server in SharePoint Server 2016 and 2019 environments

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

The minimum requirements for a database server in SharePoint Servers 2016 and 2019 are as follows:

**SharePoint Server 2016**

64-bit edition of Microsoft SQL Server 2014 with Service Pack 1 (SP1)

Microsoft SQL Server 2016

Microsoft SQL Server 2017 RTM

**SharePoint Server 2019**

Microsoft SQL Server 2016

Microsoft SQL Server 2017 RTM

Note

SQL Server Express isn't supported with SharePoint Servers 2016 and 2019.  

SQL Server 2017 on Linux isn't supported with SharePoint Servers 2016 and 2019.

Depending on the installed version, you can use specific features of SQL Server, such as reporting and business intelligence (BI) with SharePoint Server 2016. For more information, see Hardware and software requirements for SharePoint Server 2016.

SharePoint Server 2016 supports the following:

SQL Server 2016 Reporting Services (SSRS)

SQL Server 2016 Analysis Services (SSAS)

SharePoint Server 2019 supports the following:

SQL Server 2016 Reporting Services (SSRS)

SQL Server 2016 Analysis Services (SSAS)

Note

SQL Server Reporting Services integration with SharePoint Server 2019 is no longer supported. For more information, see Reporting Services Report Server (SharePoint Mode) and Supported combinations of SharePoint and Reporting Services server.

You can use the Report Viewer web part that has much of the same functionality as integrated mode. For more information, see Add the Report Viewer web part to a web page and Report Viewer web part on a SharePoint site - Reporting Services.

Note

If you want to use Microsoft SQL Server Power Pivot for SharePoint or Microsoft Power View for SharePoint for BI solutions you must install the Power Pivot or Power View add-ins for SQL Server 2016 RTM. The SQL Server 2014 (SP1) Power Pivot for SharePoint and Power View for SharePoint BI solutions don't work with SharePoint Server 2016.

SharePoint Servers 2016 and 2019 and the SQL Server database engine

## SharePoint Servers 2016 and 2019 and the SQL Server database engine

The SharePoint Server 2016 application is built on the SQL Server database engine. Most content and settings in SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM are stored in relational databases. The following table shows the databases that SharePoint Servers 2016 and 2019 use.

| **Database type** | **Description** |
| --- | --- |
| Configuration | The Configuration database and Central Administration content database are called configuration databases. They contain data about farm settings such as the databases that are used, Internet Information Services (IIS) web sites or web applications, solutions, Web Part packages, site templates, default quota, and blocked file types. A farm can only have one set of configuration databases. |
| Content | Content databases store all site content:  
  Site documents, such as files in document libraries  
  List data  
  Web Part properties  
 Data for apps for SharePoint  
  Data and objects for Project Server 2016 
  User names and permissions  
  Each web application can contain many content databases. Each site collection can be associated with only one content database, although a content database can be associated with many site collections. |
| Service application | Databases for service applications store the data that service applications use. |

For a full list of all of the databases that support SharePoint Servers 2016 and 2019, see Database types and descriptions in SharePoint Server. The **Quick reference guide: SharePoint Servers 2016 and 2019 Databases**, is available to download as either a PDF or Visio file.

Working with the SQL Server databases that support SharePoint Servers 2016 and 2019

## Working with the SQL Server databases that support SharePoint Servers 2016 and 2019

The databases that support SharePoint Server 2016 are either created automatically with the SharePoint Products Configuration Wizard or manually by database administrators when they configure SharePoint Server.

Microsoft doesn't support directly querying or modifying the databases that support SharePoint Servers 2016 and 2019. In SharePoint Servers 2016 and 2019 the Usage and Health Data Collection database does support schema modifications.

SharePoint Server 2019 doesn't support multi-tenancy so service application databases in partitioned mode can't be attached. Additionally, service applications databases in partitioned mode can't be created from Central Administration.

The SQL Server databases that support SharePoint Server 2016 are subject to sizing limitations and to configuration recommendations that aren't standard for SQL Server. For more information, see Storage and SQL Server capacity planning and configuration (SharePoint Server).

SharePoint Server 2016 and SQL Server 2014 with Service Pack 1 (SP1)

## SharePoint Server 2016 and SQL Server 2014 with Service Pack 1 (SP1)

SQL Server 2014 (SP1) provides greater performance, availability, and manageability with SharePoint Server 2016 than SQL Server 2014. While you can't use SQL Server Power Pivot for SharePoint or Power View for SharePoint with SQL Server 2014 (SP1), you can use some business intelligence solutions with SharePoint Server 2016. For example, you can install Office Online Server to use Excel Online.

For more information, see Features Supported by the Editions of SQL Server 2014. For detailed information about Office Online Server, see Configure Office Online Server for SharePoint Server 2016.

High Availability Solutions

### High Availability Solutions

We recommend Always On Availability Groups and Always On Failover Cluster Instances for high availability in SQL Server 2014 Reporting Services (SP1). Other high availability solutions are database mirroring, and log shipping. Both Always On Availability Groups and Failover Cluster Instances solutions require and use Windows Server Failover Clustering (WSFC).

Note

We recommend that you use Always On Availability Groups instead of database mirroring for your high availability solution with SQL Server 2014 (SP1), SQL Server 2016, and SQL Server 2017 RTM for SharePoint Servers 2016 and 2019. For more information, see Overview of SQL Server High-Availability Solutions.

For more information, see Always On Availability Groups (SQL Server), and Prerequisites, Restrictions, and Recommendations for Always On Availability Groups (SQL Server). For information about high availability for SQL Server Reporting Services, see High Availability (Reporting Services).

Log Shipping

#### Log Shipping

SQL Server Log shipping provides a disaster recovery solution for single primary databases and multiple secondary databases where each are located on separate instances of SQL Server. Log shipping backs up the transaction log on the production server, copies the log to the backup or secondary instances, and is then available to restore the log backup. You can then configure alerts to notify you when the production server fails. Then you can fail over from the production server to the backup servers so if the production server fails one of the backup or secondary servers can be brought online to act as the production server. For more information, see About Log Shipping (SQL Server).

Reporting Services SharePoint mode

### Reporting Services SharePoint mode

When you set up Reporting Services with SharePoint Server 2016 you create a report server. The report server is the central component of Reporting Services. This component contains two processing engines and a set of unique extensions that handle authentication, data processing, rendering, and delivery operations.

For more information, see Supported Combinations of SharePoint and Reporting Services Server and Add-in (SQL Server 2016). The following levels of integration are provided when you run a report server in integrated mode with SharePoint Server 2016.

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

SharePoint mode in SQL Server 2016 is a SharePoint shared service that you configure in either the SharePoint Central Administration website or by using Reporting Services SharePoint mode, Microsoft PowerShell cmdlets. SharePoint mode supports SharePoint Server 2016 backup and restore for SQL Server Reporting Services service application and Unified Logging Service (ULS) trace logs. SharePoint mode also supports claims-based authentication.

SharePoint mode requires that a report server component of Reporting Services must run within a SharePoint Server farm. This means that a SharePoint application server must exist with the Reporting Services shared service installed and at least one Reporting Services service application.

For more information, see Reporting Services Report Server (SharePoint Mode), Reporting Services Report Server, and PowerShell cmdlets for Reporting Services SharePoint Mode.

SQL Server 2016

### SQL Server 2016

SQL Server 2016 provides business intelligence solutions for SharePoint Server 2016. The SharePoint mode of SQL Server 2016 provides features for SQL Server Analysis Services and SQL Server Reporting Services. For more information, see Features Supported by the Editions of SQL Server 2016.

When you install SQL Server 2016 Analysis Services (SSAS) and SQL Server 2016 Reporting Services (SSRS) in a SharePoint Server 2016 farm the following business intelligence solutions are available:

SQL Server 2016 Power Pivot

SQL Server 2016 Power View

Reporting Services interactive report designer that runs on Power Pivot or Analysis Services tabular data models

The following SharePoint Server 2016 business intelligence features are available when you upgrade to SQL Server 2016 RTM:

Power Pivot Gallery

Scheduled Data Refresh

Workbooks as a Data Source

Power Pivot Management Dashboard

Power View reports

Power View Subscriptions

Report Alerting

For more info, download the new Deploying SQL Server 2016 PowerPivot and Power View in SharePoint 2016 white paper. For details about configuring and deploying business intelligence in a multiple server SharePoint Server 2016 farm, download Deploying SQL Server 2016 PowerPivot and Power View in a Multi-Tier SharePoint 2016 Farm.

For more info, see Supported Combinations of SharePoint and Reporting Services Server and Add-in (SQL Server 2016) and Install SQL Server 2016 Business Intelligence Features.

Power Pivot for SharePoint

### Power Pivot for SharePoint

SQL Server 2016 RTM is required to deploy Power Pivot for SharePoint 2016. Power Pivot for SharePoint 2016 is an add-in that is available in the SQL Server 2016 RTM Feature Pack. SQL Server 2016 Analysis Services must be run in SharePoint mode. This provides a server that hosts Power Pivot data in a SharePoint farm. For more information, see Install Analysis Services in Power Pivot Mode. The server that hosts Power Pivot for SharePoint 2016 can be outside a SharePoint Server 2016 farm.

SQL Server 2016 Analysis Services provides three modes for analysis, Multidimensional, Tabular, and Power Pivot for SharePoint. Note that each server mode is independent of the others, and each supports a type of analytical database that only runs in that modality. For more information about SQL Server 2016 Analysis Services, see Analysis Services.

To configure Power Pivot for SharePoint you can use the Power Pivot for SharePoint 2013 Configuration tool, the SharePoint Central Administration website, or Microsoft PowerShell cmdlets. The following table lists each method and describes the process:

| **Power Pivot for SharePoint Configuration method** | **Description** |
| --- | --- |
| Power Pivot for SharePoint 2016 Configuration Tool | Evaluates an existing installation and determines what needs to be configured in the SharePoint farm and Power Pivot for SharePoint and then configures everything required. |
| SharePoint Server 2016 Central Administration | Central Administration provides the SQL Server Power Pivot Service Application that you create to access the Power Pivot Management Dashboard for your BI farm. |
| Microsoft PowerShell cmdlets | Provides cmdlets that you can use to build PowerShell script files (.ps1) and automate the configuration process for Power Pivot for SharePoint. |

Power View for SharePoint

### Power View for SharePoint

Power View is a feature included with Microsoft SQL Server 2016 Reporting Services Add-in for Microsoft SharePoint. Install SQL Server 2016 Reporting Services Add-in for SharePoint, and then configure the servers for integration. When you deploy Power View for SharePoint you can create and interact with views of data from data models that are based on Power Pivot workbooks that are published in a Power Pivot Gallery, or tabular models that are deployed to SSAS. You can also create and view reports from SSRS on SharePoint document libraries. All Power View reports provide multiple views that feature tiles, slicers, chart filters, and visualizations. For more information, see What's New in Reporting Services (SSRS).

See also

## See also

Other Resources

#### Other Resources

Supported Combinations of SharePoint and Reporting Services Server and Add-in (SQL Server 2016)

What's New in SQL Server 2016

Deprecated and Discontinued SQL Server Features in SQL Server 2016

What's New (Analysis Services)

Analysis Services

Features Supported by the Editions of SQL Server 2014

Deprecated Database Engine Features in SQL Server 2014

Additional resources

## Additional resources

- Last updated on 
		2023-02-21
