---
title: "Core infrastructure documentation — pages 241-280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0241-0280
family: sccm
documentKind: "doc"
abstract: "Removed and deprecated items for Configuration Manager clients Article • 10/04/2022 Applies to: Configuration Manager (current branch) This article describes products and operating systems that are removed from support for Configuration Manager clients, or will be removed in a f"
---

# Core infrastructure documentation — pages 241-280

<!-- p.241 -->

Removed and deprecated items for
Configuration Manager clients
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article describes products and operating systems that are removed from support for
Configuration Manager clients, or will be removed in a future update (deprecated). It
provides early notice about future changes that might affect your use of Configuration
Manager.

This information may change in the future. It might not include each deprecated feature,
product, or operating system.

Deprecated client operating systems
Unless noted otherwise, each supported OS is supported as a Configuration Manager
client until the extended support end date of that OS version. For more information
about extended support end dates, see the Microsoft Support Lifecycle         . If
Configuration Manager support for an OS ends before the extended support end date,
this article lists a deprecation date and support removal date for that OS.

The following OS versions are deprecated as a Configuration Manager client. You can
still use them now, but Microsoft plans to end support in the future.

                                                                         ﾉ       Expand table

 OS version                Deprecation first announced            Support removed

 macOS (all versions)      January 2022                           December 31, 2022

Unsupported client operating systems
The following OS versions are no longer supported.

                                                                         ﾉ       Expand table

<!-- p.242 -->

 OS version                                  Deprecation first   Support
                                             announced           removed

 Windows CE 7.0                              July 19, 2019       Version 2006

 Windows 10 Mobile                           July 19, 2019       Version 2006

 Windows 10 Mobile Enterprise                July 19, 2019       Version 2006

 Windows 7                                                       January 14, 2020

 Windows Server 2008                                             January 14, 2020

 Windows Server 2008 R2                                          January 14, 2020

 Linux and UNIX                              March 22, 2018      Version 1902

 Windows 8: Professional, Enterprise         January 12, 2016    Version 1802

 Windows Embedded 8 Pro                      January 12, 2016    Version 1802

 Windows Embedded 8 Industry                 January 12, 2016    Version 1802

 Windows XP Embedded                         July 10, 2015       Version 1702

 Includes all XP-based embedded operating
 systems

 Windows Vista                               July 10, 2015       Version 1511

 Windows Server 2003 R2                      July 10, 2015       Version 1511

 Windows Server 2003                         July 10, 2015       Version 1511

 Windows XP                                  July 10, 2015       Version 1511

 macOS X 10.6 - 10.8                         July 10, 2015       Version 1511

 Windows Mobile 6.0 - 6.5                    July 10, 2015       Version 1511

 Nokia Symbian Belle                         July 10, 2015       Version 1511

 Windows CE 5.0 - 6.0                        July 10, 2015       Version 1511

See also
For more information, see the following articles:

     Supported OS versions for clients and devices

     Microsoft Support Lifecycle

<!-- p.243 -->

     Support for current branch versions of Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.244 -->

Supported configurations for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

As an on-premises solution, Configuration Manager makes use of your servers, clients,
network configurations, and other products like Microsoft Intune, SQL Server, and Azure.

This information can help you identify key configurations, requirements, and limitations.
Use it to plan, deploy, and maintain a functional Configuration Manager deployment.
This information is specific to the infrastructure for Configuration Manager sites,
hierarchies, and managed devices.

When a Configuration Manager feature or capability requires more specific
configurations, see the feature-specific documentation. It's supplemental to the more
general configuration details.

The products and technologies described in these articles are supported by
Configuration Manager. However, their inclusion in this content doesn't imply an
extension of support for any product beyond that product's individual support lifecycle.
Products that are beyond their support lifecycle aren't supported for use with
Configuration Manager. This statement includes any products that are covered under
the Extended Security Updates (ESU) program. For more information about Extended
Security Updates in Configuration Manager, see Supported OS versions for clients and
devices for Configuration Manager.

  ７ Note

  For more general information, see the Microsoft Support Lifecycle.

Products and product versions that aren't listed in these articles aren't supported with
Configuration Manager unless they're announced on the Configuration Manager blog            .
The content on this blog may precede an update to this documentation.

      Site and site system prerequisites: Learn about required configurations on a
      Windows Server to support different site types and site system roles.

      Supported operating systems for site system servers: Learn about which operating
      systems you can use as a site server or site system server.

<!-- p.245 -->

     Supported operating systems for clients and devices: Learn about which operating
     systems you can manage with Configuration Manager. These include Windows,
     Windows Embedded, macOS, and mobile devices.

     Support for Windows 11 and Support for Windows 10: Learn about the Windows
     11 and Windows 10 versions that are supported as clients.

     Support for the Windows ADK: Learn about the Windows Assessment and
     Deployment Kit (Windows ADK) version that are supported with Configuration
     Manager current branch for OS deployment.

     Supported operating systems for the console: Learn about which operating
     systems can host the Configuration Manager console.

     Support for SQL Server versions: Learn about which versions of SQL Server can
     host the site database and reporting database. It also includes required and
     optional configurations that you can use with SQL Server.

     High-availability options: Learn about the options you can implement when
     designing your environment to help maintain a high level of available service for
     Configuration Manager.

     Support for Active Directory domains: Learn about the supported Active Directory
     domain configurations that Configuration Manager requires and supports.

     Support for Windows features and networks: Learn about supported Windows
     technologies and limitations for use with Configuration Manager. For example,
     Windows BranchCache and data deduplication.

     Support for virtualization environments: Learn more about how to use supported
     virtual machine technologies.

     FAQ for Configuration Manager on Azure: Answers to common questions about
     using Configuration Manager on an Azure environment.

Use the following articles to understand Configuration Manager size, scale, and
performance:

     Size and scale numbers: Learn about how many sites, roles per site, and clients are
     supported in different hierarchy designs.

     Recommended hardware: Learn about guidelines that can help you identify the
     right hardware and configurations to host your Configuration Manager sites and
     key services.

<!-- p.246 -->

     Site size and performance guidelines: Site size-related performance test results,
     methodology, and guidance.

     Site size and performance FAQ: Answers to common Configuration Manager
     questions about site sizing and performance.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.247 -->

Site and site system prerequisites for
Configuration Manager
Article • 03/25/2024

Applies to: Configuration Manager (current branch)

Windows-based computers require specific configurations to support their use as
Configuration Manager site system servers.

For some products, like Windows Server Update Services (WSUS) for the software
update point, you need to refer to the product documentation to identify additional
prerequisites and limitations for use. Only configurations that directly apply for use with
Configuration Manager are included here.

General requirements and limitations
The following requirements apply to all site system servers:

      Each site system server must use a 64-bit OS. The only exception is the distribution
      point site system role, which you can install on some 32-bit operating systems.

      Site systems aren't supported on Server Core installations of any OS. An exception
      is that Server Core installations are supported for the distribution point. For more
      information, see Supported operating systems for Configuration Manager site
      system servers.

      After a site system server is installed, it's not supported to change:

         The domain name of the domain where the site system computer is located
         (also called a domain rename).

         The domain membership of the computer.

         The name of the computer.

         If you must change any of these items, first remove the site system role from
         the computer. Then reinstall the role after the change is complete. For changes
         affecting the site server, first uninstall the site. Then reinstall the site after the
         change is complete.

      Site system roles aren't supported on an instance of a Windows Server cluster. The
      only exception is the site database server. For more information, see Use a SQL

<!-- p.248 -->

      Server Always On failover cluster instance for the site database.

      The Configuration Manager setup process doesn't block installation of the site
      server role on a computer with the Windows role for Failover Clustering. SQL
      Server Always On availability groups require this role, so previously you couldn't
      colocate the site database on the site server. With this change, you can create a
      highly available site with fewer servers by using an availability group and a site
      server in passive mode. For more information, see High availability options.

      It's not supported to change the startup type or "Log on as" settings for any
      Configuration Manager service. If you do, you might prevent key services from
      running correctly.

.NET version requirements
Starting in version 2303, site servers and specific site systems require Microsoft .NET
Framework version 4.8 Before you run setup to install or update the site, first update
.NET and restart the system.

  ７ Note

  .NET Framework version 4.6.2 is preinstalled with Windows Server 2016. Later
  versions of Windows are preinstalled with a later version of the .NET Framework.

  .NET Framework version 4.8 is required for 2403 upgrade.

  For more information, see .NET Framework system requirements.

Site server
If the site server doesn't have any collocated roles that require .NET, it still requires .NET,
but setup doesn't automatically install it. Make sure the site server itself has at least .NET
version 4.6.2. If possible, install .NET 4.8.

Site systems

  ） Important

  If you're upgrading from System Center 2012 Configuration Manager R2 Service
  Pack 1, you need to manually verify that remote site systems have at least .NET

<!-- p.249 -->

  version 4.6.2. Configuration Manager current branch setup skips the check in this
  scenario.

During Configuration Manager setup, if site systems have a version earlier than 4.6.2,
you'll see a prerequisite check warning. This check is a warning instead of an error,
because setup will install version 4.6.2. When .NET updates, it usually requires Windows
to restart. Site systems will send status message 4979 when a restart is required.
Configuration Manager suppresses the restart; the system doesn't restart automatically.

The behavior will differ for different types of site roles that require .NET:

     The following site system roles support in-place upgrade of .NET. After upgrading
     .NET, if a restart is required, it sends status message 4979. The role keeps running
     with the earlier .NET version. After Windows restarts, the role starts using the new
     .NET version.
        Asset Intelligence synchronization point
        Management point
        Service connection point
        Data warehouse service point

     The following site systems roles uninstall and reinstall when .NET is upgraded.
     During site update, site component manager removes the role, and then updates
     .NET. If a restart is required, it sends status message 4979. After restart, site
     component manager reinstalls the role with the new .NET version. The role could
     be unavailable while it waits for you to restart the server.
        SMS Provider for the administration service
        Certificate registration point
        Enrollment point
        Enrollment proxy point
        Reporting services point
        Software update point

  ７ Note

  Currently, you still need to enable the Windows feature for .NET Framework 3.5 on
  site systems that require it.

If site systems have at least version 4.6.2 but earlier than version 4.8, you'll also see a
prerequisite check warning. We recommend that you install the latest version of .NET
version 4.8 to get the latest performance and security improvements. Configuration

<!-- p.250 -->

Manager setup doesn't automatically install .NET version 4.8. A later version of
Configuration Manager will require .NET version 4.8.

There's also a new management insight to recommend site systems that don't yet have
.NET version 4.8 or later.

Managing system restarts for .NET updates
Whether you update .NET before updating the site, or set up updates it, .NET may
require a restart to complete its installation. After .NET Framework is installed, it may
require other updates. These updates may also require the server to restart.

If you need to manage the device restarts before you update the site, use the following
recommended process:

   1. Install the latest baseline .NET version. For example, install .NET version 4.8.
   2. Restart the server.
   3. Scan for software updates and install the latest .NET cumulative update.
   4. Restart the server.
   5. Update the site to the latest current branch version.

Central administration site and primary site
servers
For more information on all prerequisites including permissions, see Prerequisites for
installing a primary site or a CAS. The following sections detail the prerequisite
components that you need to install or enable.

Windows Server roles and features for the site server
     .NET Framework 3.5

     Remote Differential Compression

     When you use a software update point on a server other than the site server, install
     the WSUS Administration Console on the site server.

.NET Framework for the site server
     Enable the Windows feature for .NET Framework 3.5.

<!-- p.251 -->

     Install a supported version of the .NET Framework. For more information, .NET
     version requirements.

Windows ADK for the site server
     Before you install or upgrade a central administration site or primary site, install
     the version of the Windows Assessment and Deployment Kit (ADK) that's required
     by the version of Configuration Manager you're installing or upgrading to. For
     more information, see Support for the Windows ADK.

     For more information about this requirement, see Infrastructure requirements for
     OS deployment.

Visual C++ Redistributable for the site server
     Starting in version 2107, Configuration Manager installs the Microsoft Visual C++
     2015-2019 redistributable package (14.28.29914.0) on each computer that installs
     a site server. In version 2103 and earlier, it installs the Visual C++ 2013 version
     (12.0.40660.0).

     The CAS and primary sites require both the x86 and x64 versions of the applicable
     redistributable file.

SQL ODBC driver for the site server
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the site server
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

  ） Important

<!-- p.252 -->

  Do not uninstall SQL server native client, we still need for certain roles.

Secondary site server

Windows Server roles and features for the secondary site
server
     .NET Framework 3.5

     Remote Differential Compression

.NET Framework for the secondary site server
     Enable the Windows feature for .NET Framework 3.5.

     Install a supported version of the .NET Framework. For more information, .NET
     version requirements.

Visual C++ Redistributable for the secondary site server
     Starting in version 2107, Configuration Manager installs the Microsoft Visual C++
     2015-2019 redistributable package (14.28.29914.0) on each computer that installs
     a secondary site server. In version 2103 and earlier, it installs the Visual C++ 2013
     version (12.0.40660.0).

     Secondary sites require only the x64 version.

Default site system roles for the secondary site server
By default, a secondary site installs a management point and a distribution point. Make
sure that the secondary site server meets the prerequisites for these site system roles.

SQL ODBC driver for the secondary site server
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

<!-- p.253 -->

SQL Server Native Client for the secondary site server
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Database server

Remote Registry service for the site database server
During installation of the Configuration Manager site, enable the Remote Registry
service on the computer that hosts the site database.

SQL Server for the site database server
     Before you install a CAS or primary site, install a supported version of SQL Server
     to host the site database. For more information, see Supported SQL Server
     versions.

     Before you install a secondary site:

        You can install a supported version of SQL Server.

        You can choose to have Configuration Manager install SQL Server Express. Make
        sure that the server meets the requirements to run SQL Server Express.

SQL ODBC driver for the database server
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the site database server
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration

<!-- p.254 -->

Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

SMS Provider server

Windows ADK for the SMS Provider
     The server where you install an instance of the SMS Provider must have a
     supported version of the Windows ADK. For more information, see Support for the
     Windows ADK.

     For more information about this requirement, see Infrastructure requirements for
     operating system deployment.

Windows Server roles and features for the SMS Provider
Web Server (IIS): Every provider attempts to install the administration service. This
service has a dependency on IIS to bind a certificate to HTTPS port 443. Configuration
Manager uses IIS APIs to check this certificate configuration. If you configure the site for
Enhanced HTTP, Configuration Manager uses IIS APIs to bind the site-generated
certificate. Unless the server already has a PKI-based certificate, the site automatically
uses the site's self-signed certificate.

.NET Framework for the SMS Provider
If you're using the administration service, the server that hosts the SMS Provider role
requires .NET 4.5 or later. Starting in version 2107, this role requires .NET version 4.6.2,
and version 4.8 is recommended. For more information, .NET version requirements.

SQL ODBC driver for the SMS Provider
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the SMS Provider

<!-- p.255 -->

When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Asset Intelligence synchronization point

  ） Important

  Starting in November 2021, this feature of Configuration Manager is deprecated.
  For more information, see Asset intelligence deprecation.

.NET Framework for the AISP
Install a supported version of the .NET Framework. For more information, .NET version
requirements.

SQL ODBC driver for the AISP
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the AISP
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Certificate registration point

  ２ Warning

  Starting in version 2203, the certificate registration point is no longer supported.
  For more information, see Frequently asked questions about resource access

<!-- p.256 -->

  deprecation.

Windows Server roles and features for the CRP
     .NET Framework
        HTTP Activation

IIS configuration for the CRP
     Application Development:

        ASP.NET 3.5 (and automatically selected options)

        ASP.NET 4.5 (and automatically selected options)

     IIS 6 Management Compatibility:

        IIS 6 Metabase Compatibility

        IIS 6 WMI Compatibility

.NET Framework for the CRP
Install a supported version of the .NET Framework. For more information, .NET version
requirements.

SQL ODBC driver for the CRP
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the CRP
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

<!-- p.257 -->

Data warehouse service point
For more information on the prerequisites for this role, see The data warehouse service
point.

.NET Framework for the DWSP
Install a supported version of the .NET Framework. For more information, .NET version
requirements.

SQL Server for the DWSP
The data warehouse database requires SQL Server 2012 or later. The edition can be
Standard, Enterprise, or Datacenter. The SQL Server version for the data warehouse
doesn't need to be the same as the site database server or the reporting services point.

Distribution point

Windows Server roles and features for the DP
     Remote Differential Compression

  ７ Note

  When the distribution point transfers content, it transfers using the Background
  Intelligent Transfer Service (BITS) built into Windows. The distribution point role
  doesn't require the optional BITS IIS Server Extension feature to be installed,
  because the client doesn't upload information to it.

IIS configuration for the DP

     Application Development:
         ISAPI Extensions

     Security:
         Windows Authentication

     IIS 6 Management Compatibility:

         IIS 6 Metabase Compatibility

<!-- p.258 -->

        IIS 6 WMI Compatibility

By default, IIS uses request filtering to block several file name extensions and folder
locations from access by HTTP or HTTPS communication. On a distribution point, this
configuration prevents clients from downloading packages that have blocked extensions
or folder locations. For more information, see IIS request filtering for distribution points.

Distribution points require that IIS allows the following HTTP verbs:

     GET
     HEAD
     PROPFIND

Visual C++ Redistributable for the DP
     Starting in version 2107, Configuration Manager installs the Microsoft Visual C++
     2015-2019 redistributable package (14.28.29914.0) on each computer that hosts a
     distribution point. In version 2103 and earlier, it installs the Visual C++ 2013
     version (12.0.40660.0).

     The version that's installed depends on the computer's platform (x86 or x64).

Add PXE support for the DP
There are two options to support PXE on a distribution point:

     Enable the Configuration Manager PXE responder without Windows Deployment
     Service.

     Install and configure the Windows Deployment Services (WDS) Windows Server
     role.

        ７ Note

        WDS installs and configures automatically when you enable a distribution
        point to support PXE.

For more information, see Install and configure distribution points.

Add multicast support for the DP

<!-- p.259 -->

     Install and configure the Windows Deployment Services (WDS) Windows Server
     role.

        ７ Note

        WDS installs and configures automatically when you enable a distribution
        point to support multicast.

     Make sure the SQL Server Native Client is installed and up to date. For more
     information, see Prerequisite checks - SQL Server Native Client.

Endpoint Protection point

Windows Server roles and features for the endpoint
protection point
     .NET Framework 3.5

     Windows Defender features (Windows Server 2016 or later)

SQL ODBC driver for the endpoint protection point
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the endpoint protection
point
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Enrollment point

<!-- p.260 -->

 ） Important

 With the deprecation of on-premises MDM and the Configuration Manager client
 for macOS, this site system role is also deprecated. For more information, see
 Removed and deprecated features for Configuration Manager.

Windows Server roles and features for the enrollment
point
    .NET Framework 3.5

      HTTP Activation (and automatically selected options)

      ASP.NET 4.5

      Windows Communication Foundation (WCF) Services

IIS configuration for the enrollment point
    Common HTTP Features:
      Default Document

    Application Development:

      ASP.NET 3.5 (and automatically selected options)

      .NET Extensibility 3.5

      ASP.NET 4.5 (and automatically selected options)

      .NET Extensibility 4.5

    IIS 6 Management Compatibility:
      IIS 6 Metabase Compatibility

.NET Framework for the enrollment point
    Enable the Windows feature for .NET Framework 3.5.

    Install a supported version of the .NET Framework. For more information, .NET
    version requirements.

Computer memory for the enrollment point

<!-- p.261 -->

     The computer that hosts this site system role must have a minimum of 5% of the
     computer's available memory free to enable the site system role to process
     requests.

     When this site system role is collocated with another site system role that has this
     same requirement, this memory requirement for the computer doesn't increase,
     but remains at a minimum of 5%.

SQL ODBC driver
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Enrollment proxy point

  ） Important

  With the deprecation of on-premises MDM and the Configuration Manager client
  for macOS, this site system role is also deprecated. For more information, see
  Removed and deprecated features for Configuration Manager.

Windows Server roles and features for the enrollment
proxy point
     .NET Framework 3.5

IIS configuration for the enrollment proxy point

<!-- p.262 -->

     Common HTTP Features:

        Default Document

        Static Content

     Application Development:

        ASP.NET 3.5 (and automatically selected options)

        ASP.NET 4.5 (and automatically selected options)

        .NET Extensibility 3.5

        .NET Extensibility 4.5

     Security:
        Windows Authentication

     IIS 6 Management Compatibility:
        IIS 6 Metabase Compatibility

.NET Framework for the enrollment proxy point
     Enable the Windows feature for .NET Framework 3.5.

     Install a supported version of the .NET Framework. For more information, .NET
     version requirements.

Computer memory for the enrollment proxy point
     The computer that hosts this site system role must have a minimum of 5% of the
     computer's available memory free to enable the site system role to process
     requests.

     When this site system role is colocated with another site system role that has this
     same requirement, this memory requirement for the computer doesn't increase,
     but remains at a minimum of 5%.

Fallback status point

Windows Server roles and features for the FSP
Depending upon the version of Windows Server, enable one of the following features:

<!-- p.263 -->

     BITS Server Extensions and the automatically selected options
     Background Intelligent Transfer Services (BITS) and the automatically selected
     options

IIS configuration
The default IIS configuration is required with the following additions:

     IIS 6 Management Compatibility:
        IIS 6 Metabase Compatibility

Management point

Windows Server roles and features for the MP
Depending upon the version of Windows Server, enable one of the following features:

     BITS Server Extensions and the automatically selected options
     Background Intelligent Transfer Services (BITS) and the automatically selected
     options

IIS configuration for the MP
     Application Development:
        ISAPI Extensions

     Security:
        Windows Authentication

     IIS 6 Management Compatibility:

        IIS 6 Metabase Compatibility

        IIS 6 WMI Compatibility

To make sure that clients can successfully communicate with a management point, make
sure IIS allows the following HTTP verbs:

     GET
     POST
     CCM_POST
     HEAD
     PROPFIND

<!-- p.264 -->

.NET Framework for the MP
Install a supported version of the .NET Framework. For more information, .NET version
requirements.

SQL ODBC driver for the MP
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the MP
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Reporting services point

.NET Framework for the RSP
Install a supported version of the .NET Framework. For more information, .NET version
requirements.

SQL Server Reporting Services for the RSP
     Install and configure at least one instance of SQL Server to support SQL Server
     Reporting Services.

     The instance that you use for SQL Server Reporting Services can be the same
     instance you use for the site database.

     The instance that you use can be shared with System Center products. The System
     Center products can't have restrictions for sharing the instance of SQL Server.

SQL ODBC driver for the RSP

<!-- p.265 -->

Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the RSP
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Service connection point

.NET Framework for the SCP
     Enable the Windows feature for .NET Framework 3.5.

     Install a supported version of the .NET Framework. For more information, .NET
     version requirements.

Visual C++ Redistributable for the SCP
     Starting in version 2107, Configuration Manager installs the Microsoft Visual C++
     2015-2019 redistributable package (14.28.29914.0) on the service connection
     point. In version 2103 and earlier, it installs the Visual C++ 2013 version
     (12.0.40660.0).

SQL ODBC driver for the SCP
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the SCP

<!-- p.266 -->

When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Software update point

Windows Server roles and features for the SUP
     .NET Framework 3.5

     The default IIS configuration is required.

.NET Framework for the SUP
     Enable the Windows feature for .NET Framework 3.5.

     Install a supported version of the .NET Framework. For more information, .NET
     version requirements.

Windows Server Update Services (WSUS) for the SUP
Install the WSUS server role. For more information, see Plan for software updates.

  ７ Note

  When you use a software update point on a remote site system, install the WSUS
  Administration Console on the site server.

SQL ODBC driver for the SUP
Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the SUP

<!-- p.267 -->

When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

State migration point

Windows Server roles and features for the SMP
     .NET Framework 3.5

        HTTP Activation (and automatically selected options)

        ASP.NET 4.5

IIS configuration for the SMP
     Common HTTP Features:
        Default Document

     Application Development:

        ASP.NET 3.5 (and automatically selected options)

        .NET Extensibility 3.5

        ASP.NET 4.5 (and automatically selected options)

        .NET Extensibility 4.5

     IIS 6 Management Compatibility:
        IIS 6 Metabase Compatibility

.NET Framework for the SMP
     Enable the Windows feature for .NET Framework 3.5.

     Install a supported version of the .NET Framework. For more information, .NET
     version requirements.

SQL ODBC driver for the SMP

<!-- p.268 -->

Starting in version 2309, Configuration Manager requires the installation of the ODBC
driver for SQL server as a prerequisite. This prerequisite is required when you create a
new site or update an existing one. Configuration Manager doesn't manage the
updates for the ODBC driver. Ensure that this component is up to date.

For more information, see Prerequisite checks - SQL ODBC driver for SQL Server.

SQL Server Native Client for the SMP
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Make sure this component is up to
date. For more information, see Prerequisite checks - SQL Server Native Client.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.269 -->

Supported operating systems for
Configuration Manager site system
servers
Article • 12/19/2024

Applies to: Configuration Manager (current branch)

This article details the Windows versions that you can use to host a Configuration
Manager site or site system role.

Windows Server 2025
Applies to Datacenter: Azure Edition, Standard and Datacenter editions

Site servers:

      Central administration site
      Primary site
      Secondary site

Site system servers:

      Certificate registration point
      Cloud management gateway connection point
      Data warehouse service point
      Distribution point Note 1
      Endpoint Protection point
      Fallback status point
      Management point
      Reporting services point
      Service connection point
      Site database server Note 2
      SMS Provider
      Software update point
      State migration point

Windows Server 2022
Applies to Datacenter: Azure Edition, Standard and Datacenter editions

<!-- p.270 -->

Site servers:

     Central administration site
     Primary site
     Secondary site

Site system servers:

     Asset Intelligence synchronization point
     Certificate registration point
     Cloud management gateway connection point
     Data warehouse service point
     Distribution point Note 1
     Endpoint Protection point
     Enrollment point
     Enrollment proxy point
     Fallback status point
     Management point
     Reporting services point
     Service connection point
     Site database server Note 2
     SMS Provider
     Software update point
     State migration point

Windows Server 2019
Applies to Standard and Datacenter editions

Site servers:

     Central administration site
     Primary site
     Secondary site

Site system servers:

     Asset Intelligence synchronization point
     Certificate registration point
     Cloud management gateway connection point
     Data warehouse service point
     Distribution point Note 1
     Endpoint Protection point

<!-- p.271 -->

     Enrollment point
     Enrollment proxy point
     Fallback status point
     Management point
     Reporting services point
     Service connection point
     Site database server Note 2
     SMS Provider
     Software update point
     State migration point

Windows Server 2016
Applies to Standard and Datacenter editions

Site servers:

     Central administration site
     Primary site
     Secondary site

Site system servers:

     Asset Intelligence synchronization point
     Certificate registration point
     Cloud management gateway connection point
     Data warehouse service point
     Distribution point Note 1
     Endpoint Protection point
     Enrollment point
     Enrollment proxy point
     Fallback status point
     Management point
     Reporting services point
     Service connection point
     Site database server Note 2
     SMS Provider
     Software update point
     State migration point

Windows Storage Server 2016

<!-- p.272 -->

Site system server:

     Distribution point Note 1

Windows Server 2012/2012 R2
Applies to Standard and Datacenter

On October 10th, 2023, Windows Server 2012 and Windows Server 2012 R2 entered the
Extended Support Updates phase. Microsoft will no longer provide support for
Configuration Manager site servers or roles installed to these Operating Systems. For
more information, see Extended Security Updates and Configuration Manager.

   Tip

  Starting in Configuration Manager 2309, you'll be notified when performing a site
  upgrade about site systems with operating systems that are past the end of
  support date.

  Starting in Configuration Manager 2403 you'll be blocked from performing a site
  upgrade if any site systems are detected with operating systems that are past the
  end of support date. For more information, see Extended Security Updates and
  Configuration Manager.

Client OS versions
The following client OS versions are supported for use as a distribution point Note 1:

     Windows 11

     For more information on supported build versions and editions, see Support for
     Windows 11.

     Windows 10 (x86, x64)

     For more information on supported build versions and editions, see Support for
     Windows 10.

This support has the following limitation:

     Distribution points on this OS don't support PXE or multicast with the default
     Windows Deployment Services. You can PXE-enable a distribution point on this OS

<!-- p.273 -->

     with the option to Enable a PXE responder without Windows Deployment
     Service. For more information, see Install and configure distribution points.

Server core installations
The server core installation of the following server OS versions is supported for use as a
distribution point:

     Windows Server 2025
     Windows Server 2022
     Windows Server 2019
     Windows Server, version 1809
     Windows Server, version 1803
     Windows Server, version 1709
     Windows Server 2016

This support has the following limitation:

     Distribution points on this OS don't support PXE or multicast with the default
     Windows Deployment Services. You can PXE-enable a distribution point on this OS
     with the option to Enable a PXE responder without Windows Deployment
     Service. For more information, see Install and configure distribution points.

General notes

Extended Security Updates for Windows Server 2012 and
Windows Server 2012 R2
On October 10th, 2023, Windows Server 2012 and Windows Server 2012 R2 will enter
the Extended Support Updates phase. Microsoft will no longer provide support for
Configuration Manager site servers or roles installed to these Operating Systems. For
more information, see Extended Security Updates and Configuration Manager.

Note 1: Distribution points
Distribution points support several different configurations that each have different
requirements. In some cases, these configurations support installation not only on
servers, but on client operating systems. For more information, see Manage content and
content infrastructure.

<!-- p.274 -->

Note 2: Site database servers
Site database servers aren't supported on a read-only domain controller (RODC). For
more information, see SQL Server security considerations: Installing SQL Server on a
domain controller.

Additionally, secondary site servers aren't supported on any domain controller.

Next steps
Supported SQL Server versions

See also:

     Recommended hardware
     Site and site system prerequisites
     Size and scale numbers

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.275 -->

Supported OS versions for clients and
devices for Configuration Manager
Applies to: Configuration Manager (current branch)

Configuration Manager supports installing client software on Windows computers.

General requirements and limitations
Review the following requirements and limitations for all clients:

     Changing the startup type or Log on as settings for any Configuration Manager service isn't
     supported. This change can prevent key services from running correctly.

Windows computers
To manage the following Windows OS versions, use the client that's included with Configuration
Manager. For more information, see How to deploy clients to Windows computers.

Supported client OS versions
     Windows 11 (starting in Configuration Manager version 2107)

        ７ Note

        You can continue to use Microsoft Endpoint Manager to manage devices running
        Windows 11 the same as with Windows 10. For more information, including some
        known issues, see Support for Windows 11.

     Windows 10

     For more information, see Support for Windows 10.

For more information on the versions of the Windows Assessment and Deployment Kit (Windows
ADK) that Configuration Manager current branch supports, see Support for the Windows ADK.

Azure Virtual Desktop

<!-- p.276 -->

Azure Virtual Desktop is a desktop and app virtualization service that runs on Microsoft Azure.
You can use Configuration Manager to manage these virtual devices running Windows in Azure.

Similar to a terminal server, some of these virtual devices allow multiple concurrent active user
sessions. To help with client performance, Configuration Manager disables user policies on any
device that allows these multiple user sessions. Even if you enable user policies, the client
disables them by default on these devices, which include Windows Enterprise multi-session and
terminal servers.

The client only disables user policy when it detects this type of device during a new installation.
For an existing client of this type that you update to this version, the previous behavior persists.
On an existing device, it configures the user policy setting even if it detects that the device allows
multiple user sessions.

If you require user policy in this scenario, and accept any potential performance impact, use client
settings to enable user policy. In the Client Policy group, configure the following setting: Enable
user policy for multiple user sessions.

Starting in version 2006, the Windows 10 Enterprise multi-session platform is available in the list
of supported OS versions on objects with requirement rules or applicability lists. Starting in
version 2107, the Windows 11 Enterprise multi-session platform is available.

  ７ Note

  If you previously selected the top-level platform, this action automatically selected all child
  platforms. New platforms aren't automatically selected. For example, if you want to add
  Windows 10 Enterprise multi-session, manually select it under the Windows 10 platform.

For more information, see the following articles:

     Support for virtualization environments
     Manage Configuration Manager clients in a virtual desktop infrastructure (VDI)

Supported server OS versions
     Windows Server 2025: IoT, Standard, Datacenter, Datacenter: Azure Edition (starting in
     Configuration Manager version 2409)

     Windows Server 2022: IoT, Standard, Datacenter, Datacenter: Azure Edition (starting in
     Configuration Manager version 2107)

<!-- p.277 -->

        Windows Server IoT 2022 for Storage is not supported

     Windows Server 2019: IoT, Standard, Datacenter
        Windows Server IoT 2019 for Storage is not supported

     Windows Server 2016: Standard, Datacenter

     Windows Storage Server 2016: Workgroup, Standard, IoT

     Windows Server 2012 R2 (x64): Standard, Datacenter Extended Security Updates

     Windows Storage Server 2012 R2 (x64) Extended Security Updates

     Windows Server 2012 (x64): Standard, Datacenter Extended Security Updates

     Windows Storage Server 2012 (x64) Extended Security Updates

Server Core

The following versions specifically refer to the Server Core installation of the OS. Note 2

Windows Server semi-annual channel versions are Server Core installations, such as Windows
Server, version 1809. As a Configuration Manager client, they're supported the same as the
associated Windows 11 or Windows 10 semi-annual channel version. For more information, see
Support for Windows 11 or Support for Windows 10.

     Windows Server 2025 (x64) Note 1 (starting in version 2409)

     Windows Server 2022 (x64) Note 1 (starting in version 2107)

     Windows Server 2019 (x64) Note 1

     Windows Server 2016 (x64) Note 1

     Windows Server 2012 R2 (x64) Note 1 Extended Security Updates

     Windows Server 2012 (x64) Note 1 Extended Security Updates

Note 1

To support client push installation, add the File Server service of the File and Storage Services
server role. For more information about installing Windows features on Server Core, see Install
roles, role services, and features by using Windows PowerShell cmdlets.

Note 2

<!-- p.278 -->

The Software Center app isn't supported on any version of Windows Server Core.

Windows Embedded computers
Manage Windows Embedded devices by installing the Configuration Manager client on the
device. For more information, see Planning for client deployment to Windows Embedded devices.

Requirements and limitations
     All client features are supported on Windows Embedded systems that don't have write
     filters enabled.

     Clients that use one of the following are supported for all features except power
     management:

        Enhanced Write Filters (EWF)

        RAM File-Based Write Filters (FBWF)

        Unified Write Filters (UWF)

Supported OS versions
     Windows 11 Enterprise

     Windows 11 IoT Enterprise Note 4

     Windows 10 Enterprise (x86, x64)

     Windows 10 IoT Enterprise (x86, x64) Note 4

Note 4: Windows IoT Enterprise

This version includes the long-term servicing channel (LTSC). For more information, see Overview
of Windows 10 IoT Enterprise.

Extended Security Updates and Configuration Manager
The Extended Security Updates (ESU) program is a last resort option for customers who need to
run certain legacy Microsoft products past the end of support. For example, Windows 10. It
includes Critical and/or Important security updates (as defined by the Microsoft Security

<!-- p.279 -->

Response Center (MSRC)     ) for a maximum of three years after the product's End of Extended
Support date.

Products that are beyond their support lifecycle aren't supported for use with Configuration
Manager. This includes any products that are covered under the ESU program. Security updates
released under the ESU program will be published to Windows Server Update Services (WSUS).
These updates will appear in the Configuration Manager console. While ESU-covered products
are not supported operating systems in Configuration Manager1, any supported version of
Configuration Manager current branch can be used to deploy and install ESU security updates for
Windows Server 2012, Windows Server 2012 R2, and Windows 102. For details on supported
Windows 10 editions under the ESU program, see the Extended Security Updates FAQ. No further
support is offered for computers running Windows 7 or Windows Server 2008/ 2008 R2, including
customers with an additional further year of ESU support as noted in KB4522133

Client management features not related to Windows software update management or OS
deployment will no longer be tested on the operating systems covered under the ESU program
and we don't guarantee that they'll continue to function. It's highly recommended to upgrade or
migrate to a current version of the operating systems as soon as possible to receive client
management support.

  ） Important

  1. "Not Supported" means these operating systems are not considered supported platforms
  for all general features of Configuration Manager.

  The only supported scenarios are:

       Deployment of ESU security updates.
       For ESU-enabled Windows 10 devices, upgrade to Windows 11 via a Windows 11
       Feature Update.
       For any Windows 10 device, upgrade to Windows 11 via Microsoft Configuration
       Manager Operating System Deployment (OSD).

  2. If ConfigMgr product fixes are required for ESU functionality, they will only be made
  available in the latest released version of Configuration Manager current branch and will not
  be backported to earlier supported versions.

   Tip

<!-- p.280 -->

  Starting in Configuration Manager 2010, you'll be notified in-console about devices with
  operating systems that are past the end of support date and that are no longer eligible to
  receive security updates. For more information, see Console notifications. This information
  is provided for your convenience and only for use internally within your company. You
  should not solely rely on this information to confirm update or license compliance. Be sure
  to verify the accuracy of the information provided to you.

Mac computers

  ） Important

  Starting in January 2022, this feature of Configuration Manager is deprecated. The macOS
  client installation package isn't available for new deployments, but existing deployments are
  supported until December 31, 2022.

  Migrate management of macOS devices to Microsoft Intune:

     1. First, uninstall the Configuration Manager client for macOS. For more information, see
       Uninstalling the Mac client.
     2. Then enroll the device to Intune. For more information, see Deployment guide:
       Manage macOS devices in Microsoft Intune.

Manage Apple Mac computers with the Configuration Manager client for macOS.

For more information, see How to deploy clients to Macs.

Requirements and limitations for macOS
     Installing or running the Configuration Manager client for macOS on computers under an
     account other than root isn't supported. Doing so can prevent key services from running
     correctly.

Supported versions
     macOS Big Sur (11) (requires Configuration Manager client for macOS version 5.0.9000.1002
     or later)

     macOS Catalina (10.15) (requires Configuration Manager client for macOS version
     5.0.8742.1000 or later)
