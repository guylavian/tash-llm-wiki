---
title: "Hardware and software requirements for SharePoint Server 2019 - SharePoint Server"
type: reference
domain: sharepoint
slug: install-hardware-and-software-requirements-2019
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/install/hardware-and-software-requirements-2019
family: install
documentKind: "interactive-tutorial"
abstract: "Find out the minimum hardware and software requirements you need to install and run SharePoint Server 2019."
---

# Hardware and software requirements for SharePoint Server 2019 - SharePoint Server

Note

Hardware and software requirements for SharePoint Server 2019

# Hardware and software requirements for SharePoint Server 2019

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

Important

If you contact Microsoft Customer Support Services about a production system that does not meet the minimum hardware specifications described in this article, support will be limited until the system is upgraded to the minimum requirements.

Hardware requirements

## Hardware requirements

Location of physical servers

### Location of physical servers

Some enterprises have datacenters that are in close proximity to one another and connected by high-bandwidth fiber optic links. In this environment, you can configure the two datacenters as a single farm. This distributed farm topology is called a stretched farm. Stretched farms are supported for SharePoint Server 2019.

For a stretched farm architecture to work as a supported high-availability solution, the following prerequisites must be met:

- A highly consistent intra-farm latency of <1 ms one way and 99.9% of the time over a period of ten minutes. (Intra-farm latency is commonly defined as the latency between the front-end web servers and the database servers.)

- The bandwidth speed must be at least 1 gigabit per second.

To provide fault tolerance in a stretched farm, use the standard best practice guidance to configure redundant service applications and databases.

Note

The intra-farm latency of <1 ms one way, 99.9% of the time over a period of ten minutes is also required for SharePoint environments with servers that are located in the same datacenter. The bandwidth speed should also be in this case at least 1 gigabit per second.

SharePoint Servers and MinRole installations

### SharePoint Servers and MinRole installations

The values in the following table are minimum values for installations on servers that are running SharePoint Server 2019 in a multiple server farm installation.

For all installation scenarios, you must have sufficient hard disk space for the base installation and sufficient space for diagnostics such as logging, debugging, creating memory dumps, and so on. For production use, you must also have additional free disk space for day-to-day operations. In addition, maintain two times as much free space as you have RAM for production environments.

For information about hardware and software requirements for Microsoft SQL Server 2016 or higher, see Hardware and Software Requirements for Installing SQL Server.

| **Installation scenario** | **Deployment type and scale** | **RAM** | **Processor** | **Hard disk space** |
| --- | --- | --- | --- | --- |
| Single server role that uses SQL Server | Development or evaluation installation of SharePoint Server 2019 with the minimum recommended services for development environments. Use the Single-Server Farm role and choose which service applications to provision. For more information on the Single-Server Farm role, see Overview of MinRole Server Roles in SharePoint Server. | 16 GB | 64-bit, 4 cores | 80 GB for system drive  
 100 GB for second drive |
| Single server role that uses SQL Server | Pilot or user acceptance test installation of SharePoint Server 2019 running all available services for development environments. | 24 GB | 64-bit, 4 cores | 80 GB for system drive  
 100 GB for second drive and additional drives |
| Web server or application server in a three-tier farm | Development or evaluation installation of SharePoint Server 2019 with a minimum number of services. | 12 GB | 64-bit, 4 cores | 80 GB for system drive  
 80 GB for second drive |
| Web server or application server in a three-tier farm | Pilot, user acceptance test, or production deployment of SharePoint Server 2019 running all available services. | 16 GB | 64-bit, 4 cores | 80 GB for system drive  
 80 GB for second drive and additional drives |

Deployment requirements: Farm Topology

## Deployment requirements: Farm Topology

For information about how to plan for a server deployment, see Planning for a MinRole server deployment in SharePoint Server 2019.

Software requirements for SharePoint Server 2019

## Software requirements for SharePoint Server 2019

The requirements in the following section apply to the following installations:

- Server farm with a single server in the farm

- Server farm with multiple servers in the farm

Note

SharePoint Server 2019 supports drives that are formatted with the Resilient File System (ReFS). For more information about ReFs, see Resilient File System Overview and Resilient File System

Important

SharePoint Server 2019 requires a minimum Active Directory domain and forest functional level of Windows Server 2003 (native). For more information about Active Directory functional levels, see Forest and Domain Functional Levels.

Important

SharePoint Server 2019 does not support single label domain names. For more information, see Information about configuring Windows for domains with single-label DNS names.

The Microsoft SharePoint Products Preparation Tool can assist you in the installation of the software prerequisites for SharePoint Server 2019. Ensure that you have an Internet connection because some prerequisites are installed from the Internet.

Minimum software requirements for SharePoint Server 2019

### Minimum software requirements for SharePoint Server 2019

This section provides minimum software requirements for each server in the farm.

Minimum requirements for a database server in a farm

#### Minimum requirements for a database server in a farm

One of the following server operating systems:

- Windows Server 2016 Standard or Datacenter (Desktop Experience)

- Windows Server 2019 Standard or Datacenter (Desktop Experience)

- Windows Server 2022 Standard or Datacenter (Desktop Experience)

Ensure at least one of the following requirements is met:

A Standard or Enterprise Edition of SQL Server for Windows that supports database compatibility level 130. This includes SQL Server 2016, SQL Server 2017, SQL Server 2019, SQL Server 2022, and any future version of SQL Server for Windows that supports database compatibility level 130. For more information about database compatibility levels, see Compatibility Certification and ALTER DATABASE (Transact-SQL) Compatibility Level.

Microsoft Azure SQL Managed Instance (MI). This is only supported if your SharePoint Server farm is hosted in Microsoft Azure. For more information, see Deploy Azure SQL Managed Instance with SharePoint Servers 2016 and 2019.

Note

SQL Server products and all future public updates are supported through the SQL Server product lifecycle.

Note

SQL Server Express is not supported. Azure SQL Database (the non-Managed Instance DBaaS service) is also not supported for any SharePoint databases.

Minimum requirements for SharePoint servers in a farm

#### Minimum requirements for SharePoint servers in a farm

One of the following server operating systems:

- Windows Server 2016 Standard or Datacenter (Desktop Experience)

- Windows Server 2019 Standard or Datacenter (Desktop Experience)

- Windows Server 2022 Standard or Datacenter (Desktop Experience)

Note

We don't support installing or upgrading SharePoint 2019 RTM on a server that previously hosted a prerelease version of SharePoint. A new server build is required to host SharePoint 2019 RTM.

Note

We don't support installing the Office 2019 client and SharePoint Server 2019 on the same computer.

Note

The minimum supported version is Office 2010 client.

Important

The Microsoft SharePoint Products Preparation Tool might not be able to install **Microsoft .NET Framework version 3.5** automatically. In this case you need to manually install the **.NET Framework 3.5 Features** Windows feature as a prerequisite using the Windows Server installation media.

The Microsoft SharePoint Products Preparation Tool installs the following prerequisites on SharePoint servers in a farm:

- Web Server (IIS) role

- Windows Process Activation Service feature

- Microsoft .NET Framework version 3.5

- Microsoft .NET Framework version 4.7.2

Note

If you have the November 2022 Public Update for SharePoint Server 2019 or a newer Public Update, then you can remove the Microsoft SQL Server 2012 Service Pack 4 Native Client as it is no longer required. For more information, see Description of the security update for SharePoint Server 2019: November 8, 2022 (KB5002294).

- Microsoft WCF Data Services 5.6

- Microsoft Identity Extensions

- Microsoft Information Protection and Control Client 2.1 (MSIPC)

- Microsoft Sync Framework Runtime v1.0 SP1 (x64)

- Windows Server AppFabric 1.1

- Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB 3092423)

- Visual C++ Redistributable Package for Visual Studio 2012

Note

The required software above will be supported when used by SharePoint via the SharePoint Product Lifecycle.

Minimum requirements for client computers

#### Minimum requirements for client computers

A supported browser is required for client computers. For more information, see Plan browser support in SharePoint Server 2019.

Manually configure Windows Server Roles and Features

## Manually configure Windows Server Roles and Features

To manually configure the required Windows Server Roles and Features, you can use one of two methods:

- Server Manager

- Microsoft PowerShell

To configure by using Server Manager, see Install or Uninstall Roles, Role Services, or Features

**To configure by using PowerShell:**

From a PowerShell command prompt window, type:

```
Install-WindowsFeature NET-HTTP-Activation,NET-Non-HTTP-Activ,NET-WCF-Pipe-Activation45,NET-WCF-HTTP-Activation45,Web-Server,Web-WebServer,Web-Common-Http,Web-Static-Content,Web-Default-Doc,Web-Dir-Browsing,Web-Http-Errors,Web-App-Dev,Web-Asp-Net,Web-Asp-Net45,Web-Net-Ext,Web-Net-Ext45,Web-ISAPI-Ext,Web-ISAPI-Filter,Web-Health,Web-Http-Logging,Web-Log-Libraries,Web-Request-Monitor,Web-Http-Tracing,Web-Security,Web-Basic-Auth,Web-Windows-Auth,Web-Filtering,Web-Performance,Web-Stat-Compression,Web-Dyn-Compression,Web-Mgmt-Tools,Web-Mgmt-Console,WAS,WAS-Process-Model,WAS-NET-Environment,WAS-Config-APIs,Windows-Identity-Foundation,Xps-Viewer -IncludeManagementTools -Verbose
```

Note

Some Windows features being installed are "Features On Demand (FOD)", which are downloaded from Windows Update. If the computer doesn't have access to Windows Update, you can specify local installation files by adding the **Source** parameter and pointing to the `\sources\sxs` folder on the Windows Server installation media.

For example: -Source D:\sources\sxs

Optional software supported in SharePoint Server 2019

## Optional software supported in SharePoint Server 2019

The optional software in this section is supported but isn't required to install or use SharePoint Server 2019. This software might be required by capabilities such as business intelligence.

| **Environment** | **Optional software** |
| --- | --- |
| Single server farm, front-end web servers, and application servers in a farm | .NET Framework Data Provider for SQL Server (part of Microsoft .NET Framework)  
  .NET Framework Data Provider for OLE DB (part of Microsoft .NET Framework)  
  SharePoint Workflow Manager  
  You can install SharePoint Workflow Manager on a dedicated computer.  
  Microsoft SQL Server 2008 R2 Reporting Services Add-in for Microsoft SharePoint Technologies  
  This add-in is used by Access Services for SharePoint Server 2019.  
  Microsoft SQL Server 2012 Data-Tier Application (DAC) Framework 64-bit edition  
  Microsoft SQL Server 2012 Transact-SQL ScriptDom 64-bit edition  
  Microsoft System CLR Types for Microsoft SQL Server 2012 64-bit edition  
  Microsoft SQL Server 2012 with SP1 LocalDB 64-bit edition  
  Microsoft Data Services for the .NET Framework 4 and Silverlight 4 (formerly ADO.NET Data Services)  
  Exchange Web Services Managed API, version 1.2 |

Links to applicable software

## Links to applicable software

To install Windows Server 2016 or higher, SQL Server 2016 or higher, or SharePoint Server 2019, you can go to the websites that are listed in this section. You can install most software prerequisites through the SharePoint Server 2019 Start page. The software prerequisites are also available from websites that are listed in this section. You can enable the Web Server (IIS) role in Server Manager.

In scenarios where installing prerequisites directly from the Internet isn't possible, you can download the prerequisites and then install them from a network share. For more information, see Install prerequisites for SharePoint Server from a network share.

- SharePoint Server 2019

- Language Packs for SharePoint Server 2019

- Microsoft .NET Framework version 4.7.2

- Microsoft WCF Data Services 5.6

- Microsoft Information Protection and Control Client (MSIPC)

- Microsoft SQL Server 2012 SP4 Feature Pack - Native Client \x64\sqlncli.msi

- Microsoft Sync Framework Runtime v1.0 SP1 (x64)

- Windows Server AppFabric 1.1

- Cumulative Update Package 7 for AppFabric 1.1 for Windows Server

- Visual C++ Redistributable Package for Visual Studio 2012

- Visual C++ Redistributable Package for Visual Studio 2017

- Exchange Web Services Managed API, version 1.2

- Microsoft Identity Extensions

Prerequisite installer operations and command-line options

## Prerequisite installer operations and command-line options

The SharePoint Server 2019 prerequisite installer (`prerequisiteinstaller.exe`) installs the following software, if it hasn't already been installed on the target server, in the following order:

- Web Server (IIS) Role

- Microsoft SQL Server 2012 SP4 Native Client

- Microsoft Sync Framework Runtime v1.0 SP1 (x64)

- Windows Server AppFabric 1.1

- Microsoft Identity Extensions

- Microsoft Information Protection and Control Client 2.1\

- Microsoft WCF Data Services 5.6

- Microsoft .NET Framework 4.7.2

- Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB 3092423)

- Visual C++ Redistributable Package for Visual Studio 2012

- Visual C++ Redistributable Package for Visual Studio 2017

You can run `prerequisiteinstaller.exe` at a command prompt with the following options. When you run `prerequisiteinstaller.exe` at a command prompt, you might be asked to restart the server one or more times during the installation process. After restarting, you should continue the prerequisite installation by running `prerequisiteinstaller.exe` with the `/continue` option.

- `/?` displays command-line options.

- `/continue` is used to tell the installer that it's continuing from being restarted.

- `/unattended` indicates no user interaction.

The installer installs from the file that you specify in the command-line options described in the following list. In this list, <*file*> signifies the file from which you want to install. If you don't specify the <*file*> option, the installer downloads the file from the Internet and installs it. If the option doesn't apply to the current operating system, it's ignored.

- **/SQLNCli:<*file*>** Install Microsoft SQL Server 2012 SP4 Native Client from <*file*>.

- **/Sync:<*file*>** Install Microsoft Sync Framework Runtime SP1 v1.0 (x64) from <*file*>.

- **/AppFabric:<*file*>** Install Windows Server AppFabric from <*file*> (AppFabric must be installed with the options /i CacheClient,CachingService,CacheAdmin /gac).

- **/IDFX11:<*file*>** Install Microsoft Identity Extensions from <*file*>.

- **/MSIPCClient:<*file*>** Install Microsoft Information Protection and Control Client from <*file*>.

- **/KB3092423:<*file*>** Install Cumulative Update Package 7 for Microsoft AppFabric 1.1 for Windows Server (KB3092423) from <*file*>.

- **/WCFDataServices56:<*file*>** Install Microsoft WCF Data Services 5.6 from <*file*>.

- **/DotNet472:<*file*>** Install Microsoft .NET Framework 4.7.2 from <*file*>.

- **/MSVCRT11:<*file*>** Install Visual C++ Redistributable Package for Visual Studio 2012 from <*file*>.

- **/MSVCRT141:<*file*>** Install Visual C++ Redistributable Package for Visual Studio 2017 from <*file*>.

Installation options

### Installation options

Certain prerequisites are installed by the prerequisite installer with specific options. Those prerequisites with specific installation options are listed below with the options that are used by the prerequisite installer.

Windows AppFabric: /i CacheClient,CachingService,CacheAdmin /gac

Microsoft WCF Data Services: /quiet

The prerequisite installer creates log files at `%TEMP%\prerequisiteinstaller.\<date\>.\<time\>.log`. You can check these log files for specific details about all changes the installer makes to the target computer.

Additional resources

## Additional resources

- Last updated on 
		2023-09-01
