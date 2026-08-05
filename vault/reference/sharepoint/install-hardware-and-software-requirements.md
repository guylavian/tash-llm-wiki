---
title: "Hardware and software requirements for SharePoint Server 2016 - SharePoint Server"
type: reference
domain: sharepoint
slug: install-hardware-and-software-requirements
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/hardware-and-software-requirements
family: install
documentKind: "interactive-tutorial"
abstract: "Find out the minimum hardware and software requirements you need to install and run SharePoint Server 2016."
---

# Hardware and software requirements for SharePoint Server 2016 - SharePoint Server

Note

Hardware and software requirements for SharePoint Server 2016

# Hardware and software requirements for SharePoint Server 2016

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

If you contact Microsoft Customer Support Services about a production system that does not meet the minimum hardware specifications described in this article, support will be limited until the system is upgraded to the minimum requirements.

Hardware requirements: Location of physical servers

## Hardware requirements: Location of physical servers

Some enterprises have datacenters that are in close proximity to one another and connected by high-bandwidth fiber optic links. In this environment, you can configure the two datacenters as a single farm. This distributed farm topology is called a stretched farm. Stretched farms are supported for SharePoint Server 2016.

For a stretched farm architecture to work as a supported high-availability solution, the following prerequisites must be met:

There is a highly consistent intra-farm latency of <1 ms one way, 99.9% of the time over a period of ten minutes. (Intra-farm latency is commonly defined as the latency between the front-end web servers and the database servers.)

The bandwidth speed must be at least 1 gigabit per second.

To provide fault tolerance in a stretched farm, use the standard best practice guidance to configure redundant service applications and databases.

Note

The intra-farm latency of <1 ms one way, 99.9% of the time over a period of ten minutes is also required for SharePoint environments with servers that are located in the same datacenter. The bandwidth speed - in this case - should also be at least 1 gigabit per second.

Hardware requirements: SharePoint server installations

## Hardware requirements: SharePoint server installations

The following table lists minimum hardware requirements for installing and running SharePoint Server 2016 in a multiple server farm installation.

For all installation scenarios, you must have sufficient hard disk space for the base installation and sufficient space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, you must also have additional free disk space for day-to-day operations. In addition, maintain two times as much free space as you have RAM for production environments.

For information about hardware and software requirements for Microsoft SQL Server, see Hardware and Software Requirements for Installing SQL Server 2016 and 2017.

| Installation scenario | Deployment type and scale | RAM | Processor | Hard disk space |
| --- | --- | --- | --- | --- |
| Single server role that uses SQL Server | Development or evaluation installation of SharePoint Server 2016 with the minimum recommended services for development environments. Use the Single-Server farm role that will let you choose which service applications to provision. For additional information on Single-Server farm role, see Overview of MinRole Server Roles in SharePoint Server 2016 | 16 GB | 64-bit, 4 cores | 80 GB for system drive  
 100 GB for second drive |
| Single server role that uses SQL Server | Pilot or user acceptance test installation of SharePoint Server 2016 running all available services for development environments. | 24 GB | 64-bit, 4 cores | 80 GB for system drive  
 100 GB for second drive and additional drives |
| SharePoint server in a multiple server farm | Development or evaluation installation of SharePoint Server 2016 with a minimum number of services. | 12 GB | 64-bit, 4 cores | 80 GB for system drive  
 80 GB for second drive |
| SharePoint server in a multiple server farm | Pilot, user acceptance test, or production deployment of SharePoint Server 2016 running all available services. | 16 GB | 64-bit, 4 cores | 80 GB for system drive  
 80 GB for second drive and additional drives |

Deployment requirements: Farm Topology

## Deployment requirements: Farm Topology

For information about how to plan for a server deployment, see Planning for a MinRole server deployment in SharePoint Server 2016.

Software requirements for SharePoint Server 2016

## Software requirements for SharePoint Server 2016

The requirements in the following section apply to the following installations:

Server farm with a single server in the farm

Server farm with multiple servers in the farm

Note

Before you run the SharePoint prerequisite installer on Windows Server 2012 R2, you need to install Windows RT 8.1, Windows 8.1, and Windows Server 2012 R2 update: April 2014. The SharePoint prerequisite installer doesn't install this update for you.

Note

SharePoint Server 2016 supports drives that are formatted with the Resilient File System (ReFS). For additional information about ReFs, see Resilient File System Overview and Resilient File System

Important

SharePoint Server 2016 requires a minimum Active Directory domain and forest functional level of Windows Server 2003 (native). For more information about Active Directory functional levels, see Forest and Domain Functional Levels.

Important

SharePoint Server 2016 doesn't support single label domain names. For more information, see Information about configuring Windows for domains with single-label DNS names.

The Microsoft SharePoint Products Preparation Tool can assist you in the installation of the software prerequisites for SharePoint Server 2016. Ensure that you have an Internet connection because some prerequisites are installed from the Internet.

Minimum software requirements for SharePoint Server 2016

### Minimum software requirements for SharePoint Server 2016

This section provides minimum software requirements for each server in the farm.

Minimum requirements for a database server in a farm

#### Minimum requirements for a database server in a farm

One of the following:

A Standard or Enterprise Edition of SQL Server for Windows that supports database compatibility level 110. This includes SQL Server 2012, SQL Server 2014, SQL Server 2016, SQL Server 2017, SQL Server 2019, SQL Server 2022, and any future version of SQL Server for Windows that supports database compatibility level 110. For more information about database compatibility levels, see Compatibility Certification and ALTER DATABASE (Transact-SQL) Compatibility Level.

Microsoft Azure SQL Managed Instance (MI). This is only supported if your SharePoint Server farm is hosted in Microsoft Azure. For more information, see Deploy Azure SQL Managed Instance with SharePoint Servers 2016 and 2019.

Note

SQL Server products and all future public updates are supported through the SQL Server product lifecycle.

Note

To take advantage of any BI scenarios, you must have the latest Powerview and PowerPivot add-ins for Microsoft SQL Server 2016 RTM. To download the PowerPivot add-ins, see Microsoft® SQL Server® 2016 PowerPivot® for Microsoft SharePoint® 2016.

Note

SQL Server Express isn't supported. Azure SQL Database (the non-Managed Instance DBaaS service) is also not supported for any SharePoint databases.

One of the following server operating systems:

Windows Server 2012 R2 Standard or Datacenter

Windows Server 2016 Standard or Datacenter

Windows Server 2019 Standard or Datacenter

Minimum requirements for SharePoint servers in a farm

#### Minimum requirements for SharePoint servers in a farm

One of the following server operating systems:

Windows Server 2012 R2 Standard or Datacenter

Windows Server 2016 Standard or Datacenter

Windows Server 2019 Standard or Datacenter

Note

Installing the Office 2016 client and SharePoint Server 2016 on the same computer isn't supported.

Note

SharePoint Server 2016 only supports the "Server with Desktop Experience" installation option of Windows Server 2016 and Windows Server 2019. For additional information about Windows Server offerings, see Windows Server Semi-annual Channel Overview.

Note

SharePoint Server 2016 supports Windows Server 2019 starting with the Security Update for Microsoft SharePoint Enterprise Server 2016 (KB4011244), also known as the November 2017 Public Update for SharePoint Server 2016.  This update (or a newer Public Update for SharePoint Server 2016) must be installed before you can create a new SharePoint farm or join a server to an existing SharePoint farm using Windows Server 2019.

The Microsoft SharePoint Products Preparation Tool installs the following prerequisites on SharePoint servers in a farm:

Web Server (IIS) role

Application Server role

Microsoft .NET Framework version 3.5

Microsoft .NET Framework version 4.6

Important

Starting April 26, 2022, the .NET Framework team no longer supports .NET Framework 4.6. We recommend you upgrade to .NET Framework 4.6.2 or higher to remain supported.

Microsoft SQL Server 2012 Service Pack 1 Native Client

Microsoft WCF Data Services 5.6

Microsoft Identity Extensions

Microsoft Information Protection and Control Client (MSIPC)

Microsoft Sync Framework Runtime v1.0 SP1 (x64)

Windows Server AppFabric 1.1

Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB 3092423)

Microsoft ODBC Driver 11 for SQL Server

Visual C++ Redistributable Package for Visual Studio 2012

Visual C++ Redistributable Package for Visual Studio 2015

Note

The required software above will be supported when used by SharePoint via the SharePoint Product Lifecycle.

Minimum requirements for client computers

#### Minimum requirements for client computers

- A supported browser. For more information, see Plan browser support in SharePoint Server 2016.

Optional software supported in SharePoint Server 2016

## Optional software supported in SharePoint Server 2016

The optional software in this section is supported but isn't required to install or use SharePoint Server 2016. This software might be required by capabilities such as business intelligence.

| Environment | Optional software |
| --- | --- |
| Single server farm, front-end web servers, and application servers in a farm | .NET Framework Data Provider for SQL Server (part of Microsoft .NET Framework)  
  .NET Framework Data Provider for OLE DB (part of Microsoft .NET Framework)  
  Workflow Manager  
  You can install Workflow Manager on a dedicated computer.  
  Microsoft SQL Server 2008 R2 Reporting Services Add-in for Microsoft SharePoint Technologies  
  This add-in is used by Access Services for SharePoint Server 2016.  
  Microsoft SQL Server 2012 Data-Tier Application (DAC) Framework 64-bit edition  
  Microsoft SQL Server 2012 Transact-SQL ScriptDom 64-bit edition  
  Microsoft System CLR Types for Microsoft SQL Server 2012 64-bit edition  
  Microsoft SQL Server 2012 with SP1 LocalDB 64-bit edition  
  Microsoft Data Services for the .NET Framework 4 and Silverlight 4 (formerly ADO.NET Data Services)  
  Exchange Web Services Managed API, version 1.2  
  Microsoft SQL Server 2008 R2 Remote Blob Store which is part of the Microsoft SQL Server 2008 R2 Feature Pack  
  SQL Server 2008 R2 Analysis Services ADOMD.NET |

Links to applicable software

## Links to applicable software

To install Windows Server 2012 R2, SQL Server 2014 Service Pack 1 (SP1), or SharePoint Server 2016, you can go to the websites that are listed in this section. You can install most software prerequisites through the SharePoint Server 2016 Start page. The software prerequisites are also available from websites that are listed in this section. You can enable the Web Server (IIS) role and the Application Server role in Server Manager.

In scenarios where installing prerequisites directly from the Internet isn't possible, you can download the prerequisites and then install them from a network share. For more information, see Install prerequisites for SharePoint Server from a network share.

SharePoint Server 2016

Language Packs for SharePoint Server 2016

Windows Server 2012 R2

Windows Server 2016

Office 365 Enterprise

Microsoft SQL Server 2016

.NET Framework 4.6.2

Microsoft WCF Data Services 5.6

Microsoft Information Protection and Control Client (MSIPC)

Microsoft SQL Server 2012 Service Pack 4 (SP4) Native Client

Microsoft ODBC Driver 11 for SQL Server

Microsoft Sync Framework Runtime v1.0 SP1 (x64)

Windows Server AppFabric 1.1

Cumulative Update Package 7 for AppFabric 1.1 for Windows Server

Visual C++ Redistributable Package for Visual Studio 2012

Visual C++ Redistributable Package for Visual Studio 2015

Microsoft Silverlight 3

Exchange Web Services Managed API, version 1.2

Microsoft Identity Extensions

Prerequisite installer operations and command-line options

## Prerequisite installer operations and command-line options

The SharePoint Server 2016 prerequisite installer (prerequisiteinstaller.exe) installs the following software, if it hasn't already been installed on the target server, in the following order:

Application Server Role, Web Server (IIS) Role

Microsoft SQL Server 2012 SP1 Native Client

Microsoft ODBC Driver 11 for SQL Server

Microsoft Sync Framework Runtime v1.0 SP1 (x64)

Windows Server AppFabric 1.1

Microsoft Identity Extensions

Microsoft Information Protection and Control Client 2.1

Microsoft WCF Data Services 5.6

Microsoft .NET Framework 4.6

Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB 3092423)

Visual C++ Redistributable Package for Visual Studio 2012

Visual C++ Redistributable Package for Visual Studio 2015

You can run `prerequisiteinstaller.exe` at a command prompt with the following options. When you run `prerequisiteinstaller.exe` at a command prompt, you might be asked to restart the server one or more times during the installation process. After restarting, you should continue the prerequisite installation by running `prerequisiteinstaller.exe` with the `/continue` option.

`/?` displays command-line options.

`/continue` is used to tell the installer that it's continuing from being restarted.

`/unattended` indicates no user interaction.

The installer installs from the file that you specify in the command-line options described in the following list. In this list, < *file*> signifies the file from which you want to install. If you don't specify the < *file*> option, the installer downloads the file from the Internet and installs it. If the option doesn't apply to the current operating system, it's ignored.

**/SQLNCli:< *file*>** Install Microsoft SQL Server 2012 SP1 Native Client from <  *file*>.

**/IDFX11:< *file*>** Install Microsoft Identity Extensions from <  *file*>.

**/Sync:< *file*>** Install Microsoft Sync Framework Runtime SP1 v1.0 (x64) from <  *file*>.

**/AppFabric:< *file*>** Install Windows Server AppFabric from <  *file*> (AppFabric must be installed with the options /i CacheClient,CachingService,CacheAdmin /gac).

**/KB3092423:< *file*>** Install Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB3092423) from <  *file*>.

**/MSIPCClient:< *file*>** Install Microsoft Information Protection and Control Client from <  *file*>.

**/WCFDataServices56:< *file*>** Install Microsoft WCF Data Services 5.6 from <  *file*>.

**/ODBC:< *file*>** Install Microsoft ODBC Driver 11 for SQL Server from < *file*>.

**/DotNetFx:< *file*>** Install Microsoft .NET Framework 4.6 from < *file*>.

**/MSVCRT11:< *file*>** Install Visual C++ Redistributable Package for Visual Studio 2012 from <  *file*>.

**/MSVCRT14:< *file*>** Install Visual C++ Redistributable Package for Visual Studio 2015 from <  *file*>.

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
		2023-05-08
