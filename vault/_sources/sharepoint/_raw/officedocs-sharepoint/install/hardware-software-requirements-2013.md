---
title: "Hardware and software requirements for SharePoint 2013 - SharePoint Server"
description: "Lists the minimum hardware and software requirements to install and run SharePoint."
ms.topic: interactive-tutorial
---
Note

Hardware and software requirements for SharePoint 2013

# Hardware and software requirements for SharePoint 2013

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

If you contact Microsoft Customer Support Services about a production system that does not meet the minimum hardware specifications described in this document, support will be limited until the system is upgraded to the minimum requirements.

Important

Some of the hardware requirement values in this article are based on test results from SharePoint 2010 Products and still apply to SharePoint 2013. This article will be updated with appropriate values and republished when new data becomes available. Hardware requirement values obtained from SharePoint 2010 Products that are listed in this article do not apply to search in SharePoint 2013.
This article links to SharePoint 2010 Products guidance where that guidance is still valid. The SharePoint 2010 Products guidance is not applicable for search in SharePoint 2013 because the search architecture has changed significantly.
The hardware and software requirements in this article refer to physical and virtual servers in a SharePoint farm.

Overview

## Overview

SharePoint 2013 provides for several installation scenarios. Currently, these installations include single server with built-in database installations, single-server farm installations, and multiple-server farm installations. This article describes the hardware and software requirements for SharePoint 2013 in each of these scenarios.

Hardware and software requirements for other SharePoint 2013 capabilities

## Hardware and software requirements for other SharePoint 2013 capabilities

If you plan to use capabilities that are offered through SharePoint 2013 or through other integration channels, such as SQL Server or Exchange Server, you also need to meet the hardware and software requirements that are specific to that capability. The following list provides links to hardware and software requirements for some SharePoint 2013 capabilities:

Hardware and software requirements (Project Server 2013)

For eDiscovery, each front-end web server must have the Exchange Web Services Managed API, version 1.2 installed. For more information, see the following articles:

Configure eDiscovery in SharePoint Server

Configure Exchange for SharePoint eDiscovery Center

Hardware requirements for search in SharePoint Server 2013:

Step 3: Which hardware requirements should I be aware of?

Hardware requirements for search topologies for Internet sites

Mobile device browsers supported in SharePoint 2013

Hardware requirements—location of physical servers

## Hardware requirements—location of physical servers

Some enterprises have data centers that are located in close proximity to one another and are connected by high-bandwidth fiber optic links. In this environment, it's possible to configure the two data centers as a single farm. This distributed farm topology is called a stretched farm. Stretched farms for SharePoint 2013 are supported as of April 2013.

For a stretched farm architecture to work as a supported high-availability solution, the following prerequisites must be met:

There's a highly consistent intra-farm latency of <1ms one way, 99.9% of the time over a period of ten minutes. (Intra-farm latency is commonly defined as the latency between the front-end web servers and the database servers.)

The bandwidth speed must be at least 1 gigabit per second.

To provide fault tolerance in a stretched farm, use the standard best practice guidance to configure redundant service applications and databases. For more information, see Create a high availability architecture and strategy for SharePoint Server.

Hardware requirements—web servers, application servers, and single server installations

## Hardware requirements—web servers, application servers, and single server installations

The values in the following table are minimum values for installations on a single server with a built-in database and for web and application servers that are running SharePoint 2013 in a multiple server farm installation.

For all installation scenarios, you must have sufficient hard disk space for the base installation and sufficient space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, you must also have additional free disk space for day-to-day operations. In addition, maintain two times as much free space as you have RAM for production environments. For more information, see Capacity management and sizing for SharePoint Server 2013.

| **Installation Scenario** | **Deployment type and scale** | **RAM** | **Processor** | **Hard disk space** |
| --- | --- | --- | --- | --- |
| Single server with a built-in database or single server that uses SQL Server | Development or evaluation installation of SharePoint Server 2013 or SharePoint Foundation 2013 with the minimum recommended services for development environments. For information, see Minimum recommended services for development environments. | 8 GB | 64-bit, 4 cores | 80 GB for system drive |
| Single server with a built-in database or single server that uses SQL Server | Development or evaluation installation of SharePoint Server 2013 or SharePoint Foundation 2013 running Visual Studio 2012 and the minimum recommended services for development environments. For information, see Minimum recommended services for development environments. | 10 GB | 64-bit, 4 cores | 80 GB for system drive |
| Single server with a built-in database or single server that uses SQL Server | Development or evaluation installation of SharePoint Server 2013 running all available services. | 24 GB | 64-bit, 4 cores | 80 GB for system drive |
| Web server or application server in a three-tier farm | Pilot, user acceptance test, or production deployment of SharePoint Server 2013 or SharePoint Foundation 2013. | 12 GB | 64-bit, 4 cores | 80 GB for system drive |

Hardware requirements—database servers

## Hardware requirements—database servers

The requirements in the following table apply to database servers in environments that have multiple servers in the farm.

Note

The requirements listed in this section also apply to SQL Server 2014.

| **Component** | **Minimum requirement** |
| --- | --- |
| Processor | 64-bit, 4 cores for small deployments (fewer than 1,000 users)  
  64-bit, 8 cores for medium deployments (between 1,000 to 10,000 users) |
| RAM | 8 GB for small deployments (fewer than 1,000 users)  
  16 GB for medium deployments (between 1,000 to 10,000 users)  
  For large deployments over 10,000 users, see the "Estimate memory requirements" section in Storage and SQL Server capacity planning and configuration (SharePoint Server 2010). This document doesn't apply to search in SharePoint 2013.  
  These values are larger than those recommended as the minimum values for SQL Server because of the distribution of data that is required for a SharePoint 2013 environment. For more information about SQL Server system requirements, see Hardware and Software Requirements for Installing SQL Server 2008 R2. |
| Hard disk | 80 GB for system drive  
 Hard disk space depends on how much content that you have in your deployment. For information about how to estimate the amount of content and other databases for your deployment, see Storage and SQL Server capacity planning and configuration (SharePoint Server 2010). |

Software requirements

## Software requirements

The requirements in the following section apply to the following installations:

Single server with built-in database

Server farm with a single server in the farm

Server farm with multiple servers in the farm

Important

SharePoint 2013 requires a minimum Active Directory domain and forest functional level of Windows Server 2003 (native). For more information about Active Directory functional levels, see Forest and Domain Functional Levels.

Important

SharePoint 2013 does not support single label domain names. For more information, see Information about configuring Windows for domains with single-label DNS names.

The Microsoft SharePoint Products Preparation Tool can assist you in the installation of the software prerequisites for SharePoint 2013. Ensure that you have an Internet connection, because some prerequisites are installed from the Internet. For more information about how to use the Microsoft SharePoint Products Preparation Tool, see Install SharePoint 2013 across multiple servers for a three-tier farm and Install SharePoint 2013 across multiple servers for a three-tier farm.

Note

SQL Server 2014 requires the May 2014 Cumulative Update to be installed. To install the May 2014 Cumulative Update see Updates to SharePoint 2013.

Note

SQL Server 2016 or higher is not supported.

Minimum software requirements

### Minimum software requirements

This section provides minimum software requirements for each server in the farm.

Minimum requirements for a database server in a farm:

Note

SQL Server products and all future public updates and service packs are supported through the SQL Server product lifecycle.

One of the following:

The 64-bit edition of SQL Server 2014 (requires May 2014 cumulative update for SharePoint Server 2013).

The 64-bit edition of Microsoft SQL Server 2012.

The 64-bit edition of SQL Server 2008 R2 Service Pack 1

A 64-bit edition of Windows Server, for supported combinations of Windows Server and SQL Server, see Using SQL Server in Windows 8 and later versions of Windows operating system.

The SharePoint parsing process crashes in Windows Server 2008 R2 (KB 2554876)

FIX: IIS 7.5 configurations aren't updated when you use the ServerManager class to commit configuration changes (KB 2708075)

Hotfix: ASP.NET (SharePoint) race condition in .NET 4.5 RTM:

Windows Server 2008 R2 SP1 (KB 2759112)

Windows Server 2012 (KB 2765317)

Microsoft .NET Framework version 4.5

Minimum requirements for a single server with built-in database:

Note

Windows Server 2016 or higher is not supported.

One of the following server operating systems:

Windows Server 2008 R2 Service Pack 1 (SP1) Standard, Enterprise, or Datacenter

Windows Server 2012 Standard or Datacenter

Windows Server 2012 R2 Standard or Datacenter

Note

Windows Server 2012 R2 is only supported on a SharePoint Server 2013 Service Pack 1 environment. For more information about Windows Server 2012 R2 support, see SharePoint 2013 SP1 support in Windows Server 2012 R2.

Note

Installing Office 2013 and SharePoint Server 2013 on the same computer is not supported.

The SharePoint parsing process crashes in Windows Server 2008 R2 (KB 2554876)

FIX: IIS 7.5 configurations aren't updated when you use the ServerManager class to commit configuration changes (KB 2708075)

Hotfix: ASP.NET (SharePoint) race condition in .NET 4.5 RTM:

Windows Server 2008 R2 SP1 (KB 2759112)

Windows Server 2012 (KB 2765317)

The Setup program installs the following prerequisite for a single server with built-in database:

- Microsoft SQL Server 2008 R2 SP1 - Express Edition

The Microsoft SharePoint Products Preparation Tool installs the following prerequisites for a single server with built-in database:

Web Server (IIS) role

Application Server role

Microsoft .NET Framework version 4.5

Microsoft WCF Data Services 5.0

SQL Server 2008 R2 SP1 Native Client

Microsoft Information Protection and Control Client (MSIPC)

Microsoft Sync Framework Runtime v1.0 SP1 (x64)

Windows Management Framework 3.0 which includes Microsoft PowerShell 3.0

Windows Identity Foundation (WIF) 1.0 and Microsoft Identity Extensions (previously named WIF 1.1)

Windows Server AppFabric

Cumulative Update Package 1 for Microsoft AppFabric 1.1 for Windows Server (KB 2671763)

Note

The required software above will be supported when used by SharePoint via the SharePoint Product Lifecycle.

Minimum requirements for front-end web servers and application servers in a farm:

Note

Windows Server 2016 or higher is not supported.

One of the following server operating systems:

Windows Server 2008 R2 Service Pack 1 (SP1) Standard, Enterprise, or Datacenter

Windows Server 2012 Standard or Datacenter

Windows Server 2012 R2 Standard or Datacenter

Note

Windows Server 2012 R2 is only supported on a SharePoint Server 2013 Service Pack 1 environment. For more information about Windows Server 2012 R2 support, see SharePoint 2013 SP1 support in Windows Server 2012 R2.

The SharePoint parsing process crashes in Windows Server 2008 R2 (KB 2554876)

FIX: IIS 7.5 configurations aren't updated when you use the ServerManager class to commit configuration changes (KB 2708075)

Hotfix: ASP.NET (SharePoint) race condition in .NET 4.5 RTM:

Windows Server 2008 R2 SP1 (KB 2759112)

Windows Server 2012 (KB 2765317)

The Microsoft SharePoint Products Preparation Tool installs the following prerequisites for front-end web servers and application servers in a farm:

Web Server (IIS) role

Application Server role

Microsoft .NET Framework version 4.5

SQL Server 2008 R2 SP1 Native Client

Microsoft WCF Data Services 5.0

Microsoft Information Protection and Control Client (MSIPC)

Microsoft Sync Framework Runtime v1.0 SP1 (x64)

Windows Management Framework 3.0 which includes Microsoft PowerShell 3.0

Windows Identity Foundation (WIF) 1.0 and Microsoft Identity Extensions (previously named WIF 1.1)

Windows Server AppFabric

Cumulative Update Package 1 for Microsoft AppFabric 1.1 for Windows Server (KB 2671763)

Minimum requirements for client computers

#### Minimum requirements for client computers

- A supported browser. For more information, see Plan browser support in SharePoint 2013. For information on browsers supported on mobile devices, see Mobile device browsers supported in SharePoint 2013.

Minimum recommended services for development environments

#### Minimum recommended services for development environments

The following are the minimum SharePoint 2013 services and service applications that are recommended for development environments:

App Management service application

Central Administration web site

Claims to Windows Token service (C2WTS)

Distributed cache service

Microsoft SharePoint Foundation 2013 Site and Subscription Settings service

Secure Store Service

User Profile service application (SharePoint Server 2013 only)

Optional software

## Optional software

The optional software in this section is supported but isn't required to install or use SharePoint 2013. This software might be required by capabilities such as business intelligence. For more information about system requirements for other capabilities, see Hardware and software requirements for other SharePoint 2013 capabilities.

| **Environment** | **Optional software** |
| --- | --- |
| Single server with built-in database, front-end web servers, and application servers in a farm | .NET Framework Data Provider for SQL Server (part of Microsoft .NET Framework)  
  .NET Framework Data Provider for OLE DB (part of Microsoft .NET Framework)  
  Workflow Manager  
  You can install Workflow Manager on a dedicated computer.  
  Microsoft SQL Server 2008 R2 Reporting Services Add-in for Microsoft SharePoint Technologies  
  This add-in is used by Access Services for SharePoint Server 2016.  
  Microsoft SQL Server 2012 Data-Tier Application (DAC) Framework 64-bit edition  
  Microsoft SQL Server 2012 Transact-SQL ScriptDom 64-bit edition  
  Microsoft System CLR Types for Microsoft SQL Server 2012 64-bit edition  
  Microsoft SQL Server 2012 with Service Pack 1 (SP1) LocalDB 64-bit edition  
  Microsoft Data Services for the .NET Framework 4 and Silverlight 4 (formerly ADO.NET Data Services)  
  Exchange Web Services Managed API, version 1.2  
  Microsoft SQL Server 2008 R2 Remote Blob Store which is part of the Microsoft SQL Server 2008 R2 Feature Pack  
  SQL Server 2008 R2 Analysis Services ADOMD.NET  
  KB 2472264  
  If you're running a geo-distributed deployment and your servers are running Windows Server 2008 R2, then installing KB 2472264 can optimize network latency in a dedicated datacenter network. For more information, and to download the software, see You can't customize some TCP configurations by using the netsh command in Windows Server 2008 R2. |
| Client computer | Windows 7  
  For information about how to use Windows 7 with SharePoint 2013 in a development environment, see Start: Set up the development environment for SharePoint 2013.  
  Silverlight 3  
  Office 2016  
  Microsoft Office 2010 with Service Pack 2 
  Microsoft Office 2007 with Service Pack 2 
  Microsoft Office for Mac 2011 with Service Pack 1  
  Microsoft Office 2008 for Mac version 12.2.9  
  Support ends April 9, 2013. |

Links to applicable software

## Links to applicable software

To install Windows Server 2008 R2 SP1, Windows Server 2012, SQL Server, or SharePoint 2013, you can go to the web sites that are listed in this section. You can install most software prerequisites through the SharePoint 2013 Start page. The software prerequisites are also available from web sites that are listed in this section. You can enable the Web Server (IIS) role and the Application Server role in Server Manager.

In scenarios where installing prerequisites directly from the Internet isn't possible you can download the prerequisites and then install them from a network share. For more information, see Install prerequisites for SharePoint Server from a network share.

Windows 7 and Windows Server 2008 R2 Service Pack 1 (SP1) (KB 976932)

Microsoft SharePoint Server 2013

Microsoft SharePoint Foundation 2013

Microsoft 365 Enterprise

The SharePoint parsing process crashes in Windows Server 2008 R2 (KB 2554876)

FIX: IIS 7.5 configurations aren't updated when you use the ServerManager class to commit configuration changes (KB 2708075)

Hotfix: ASP.NET (SharePoint) race condition in .NET 4.5 RTM:

- Windows Server 2012 and Windows 8 (KB 2765317)

Windows Server 2012, Datacenter Edition or Standard Edition

Microsoft SQL Server 2008 R2 Service Pack 1

Microsoft .NET Framework version 4.5

Microsoft SQL Server 2008 R2 SP1 - Express Edition

Workflow Manager

WCF Data Services 5.0 for OData

Microsoft Information Protection and Control Client (MSIPC)

Windows Management Framework 3.0 which includes Microsoft PowerShell 3.0

Microsoft Sync Framework Runtime v1.0 SP1 (x64)

Windows Identity Foundation 1.0 for Windows Server 2008 R2

Windows Identity Extensions for Windows Server 2008 R2

Windows Server AppFabric

Cumulative Update Package 1 for Microsoft AppFabric 1.1 for Windows Server (KB 2671763)

Microsoft SQL Server 2008 R2 Feature Pack which includes the Microsoft SQL Server 2008 R2 SP1 Native Client and the SQL Server Remote BLOB Store

Microsoft SQL Server 2008 R2 SP1 Feature pack which includes Microsoft SQL Server 2008 R2 ADOMD.NET

Microsoft Silverlight 3

Exchange Web Services Managed API, version 1.2

Microsoft SQL Server 2012 Native Client 64-bit edition - ENU\x64\sqlncli.MSI

Microsoft SQL Server 2012 Data-Tier Application (DAC) Framework 64-bit edition - ENU\x64\dacframework.msi

Microsoft SQL Server 2012 Transact-SQL ScriptDom 64-bit edition - SQLDOM.msi

Microsoft System CLR Types for Microsoft SQL Server 2012 64-bit edition - SQLSysClrTypes.msi

Microsoft SQL Server 2012 with Service Pack 1 (SP1) LocalDB 64-bit edition, which is also a component of SQL Server 2012 with Service Pack 1 (SP1) Express - ENU\x64\SqlLocalDB.msi

Microsoft SQL Server 2014

Prerequisite installer operations and command-line options

## Prerequisite installer operations and command-line options

The SharePoint 2013 prerequisite installer (prerequisiteinstaller.exe) installs the following software, if it hasn't already been installed on the target server, in this order:

Microsoft .NET Framework version 4.5

Windows Management Framework 3.0

Application Server Role, Web Server (IIS) Role

Microsoft SQL Server 2008 R2 SP1 Native Client

Windows Identity Foundation (KB974405)

Microsoft Sync Framework Runtime v1.0 SP1 (x64)

Windows Identity Extensions

Microsoft Information Protection and Control Client

Microsoft WCF Data Services 5.0

Windows Server AppFabric

Cumulative Update Package 1 for Microsoft AppFabric 1.1 for Windows Server (KB 2671763)

You can run prerequisiteinstaller.exe at a command prompt with the following options. When you run prerequisiteinstaller.exe at a command prompt, you may be asked to restart the server one or more times during the installation process. After rebooting, you should continue the prerequisite installation by running prerequisiteinstaller.exe with the `/continue` option.

`/?` Display command-line options

`/continue` is used to tell the installer that it's continuing from a restart

`/unattended` No user interaction

The installer installs from the file that you specify in the command-line options described in the following list. In this list, < *file*> signifies the file from which you want to install. If you don't specify the < *file*> option, the installer downloads the file from the Internet and installs it. If the option doesn't apply to the current operating system, it's ignored.

**/SQLNCli:< *file*>** Install Microsoft SQL Server 2008 SP1 Native Client from <  *file*>

**/PowerShell:< *file*>** Install Windows Management Framework 3.0 from <  *file*>

**/NETFX:< *file*>** Install Microsoft .NET Framework version 4.5 from <  *file*>

**/IDFX:< *file*>** Install Windows Identity Foundation (KB974405) from <  *file*>

**/IDFX11:< *file*>** Install Windows Identity Foundation v1.1 from <  *file*>

**/Sync:< *file*>** Install Microsoft Sync Framework Runtime SP1 v1.0 (x64) from <  *file*>

**/AppFabric:< *file*>** Install Windows Server AppFabric from <  *file*> (AppFabric must be installed with the options /i CacheClient,CachingService,CacheAdmin /gac)

**/KB2671763:< *file*>** Install Microsoft AppFabric 1.1 for Windows Server (AppFabric 1.1) from <  *file*>

**/MSIPCClient:< *file*>** Install Microsoft Information Protection and Control Client from <  *file*>

**/WCFDataServices:< *file*>** Install Microsoft WCF Data Services from <  *file*>

Installation options

### Installation options

Certain prerequisites are installed by the prerequisite installer with specific options. Those prerequisites with specific installation options are listed below with the options that are used by the prerequisite installer.

Windows AppFabric

/i CacheClient,CachingService,CacheAdmin /gac

Microsoft WCF Data Services

/quiet

The prerequisite installer creates log files at %TEMP%\prerequisiteinstaller.<date>.<time>.log. You can check these log files for specific details about all changes the installer makes to the target computer.

Additional resources

## Additional resources

- Last updated on 
		2024-12-02
