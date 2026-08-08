---
title: "Core infrastructure documentation — pages 721-760"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0721-0760
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0721-0760
family: sccm
documentKind: "doc"
abstract: "First, determine the installed .NET versions. For more information, see Determine which versions and service pack levels of .NET Framework are installed. Install .NET updates Install the .NET updates so you can enable strong cryptography. Some versions of .NET Framework might re"
---

# Core infrastructure documentation — pages 721-760

<!-- p.721 -->

First, determine the installed .NET versions. For more information, see Determine which
versions and service pack levels of .NET Framework are installed.

Install .NET updates
Install the .NET updates so you can enable strong cryptography. Some versions of .NET
Framework might require updates to enable strong cryptography. Use these guidelines:

     NET Framework 4.6.2 and later supports TLS 1.1 and TLS 1.2. Confirm the registry
     settings, but no additional changes are required.

        ７ Note

        Starting in version 2107, Configuration Manager requires Microsoft .NET
        Framework version 4.6.2 for site servers, specific site systems, clients, and the
        console. If possible in your environment, install the latest version of .NET
        version 4.8.

     Update NET Framework 4.6 and earlier versions to support TLS 1.1 and TLS 1.2. For
     more information, see .NET Framework versions and dependencies.

     If you're using .NET Framework 4.5.1 or 4.5.2 on Windows 8.1, Windows Server
     2012 R2, or Windows Server 2012, it's highly recommended that you install the
     latest security updates for the .Net Framework 4.5.1 and 4.5.2 to ensure TLS 1.2 can
     be enabled properly.

     For your reference, TLS 1.2 was first introduced into .Net Framework 4.5.1 and 4.5.2
     with the following hotfix rollups:
        For Windows 8.1 and Server 2012 R2: Hotfix rollup 3099842
        For Windows Server 2012: Hotfix rollup 3099844

Configure for strong cryptography
Configure .NET Framework to support strong cryptography. Set the SchUseStrongCrypto
registry setting to DWORD:00000001 . This value disables the RC4 stream cipher and
requires a restart. For more information about this setting, see Microsoft Security
Advisory 296038.

Make sure to set the following registry keys on any computer that communicates across
the network with a TLS 1.2-enabled system. For example, Configuration Manager clients,
remote site system roles not installed on the site server, and the site server itself.

<!-- p.722 -->

For 32-bit applications that are running on 32-bit OSs and for 64-bit applications that
are running on 64-bit OSs, update the following subkey values:

  Registry

  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v2.0.50727]
        "SystemDefaultTlsVersions" = dword:00000001
        "SchUseStrongCrypto" = dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319]
        "SystemDefaultTlsVersions" = dword:00000001
        "SchUseStrongCrypto" = dword:00000001

For 32-bit applications that are running on 64-bit OSs, update the following subkey
values:

  Registry

  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v2.0.50727]
        "SystemDefaultTlsVersions" = dword:00000001
        "SchUseStrongCrypto" = dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v4.0.30319]
        "SystemDefaultTlsVersions" = dword:00000001
        "SchUseStrongCrypto" = dword:00000001

  ７ Note

  The SchUseStrongCrypto setting allows .NET to use TLS 1.1 and TLS 1.2. The
   SystemDefaultTlsVersions setting allows .NET to use the OS configuration. For

  more information, see TLS best practices with the .NET Framework.

Next steps
     Enable TLS 1.2 on the site servers and remote site systems
     Common issues when enabling TLS 1.2

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.723 -->

How to enable TLS 1.2 on the site
servers and remote site systems
Article • 06/20/2024

Applies to: Configuration Manager (Current Branch)

When enabling TLS 1.2 for your Configuration Manager environment, start with enabling
TLS 1.2 for the clients first. Then, enable TLS 1.2 on the site servers and remote site
systems second. Finally, test client to site system communications before potentially
disabling the older protocols on the server side. The following tasks are needed for
enabling TLS 1.2 on the site servers and remote site systems:

      Ensure that TLS 1.2 is enabled as a protocol for SChannel at the operating system
      level
      Update and configure the .NET Framework to support TLS 1.2
      Update SQL Server and client components
      Update Windows Server Update Services (WSUS)

For more information about dependencies for specific Configuration Manager features
and scenarios, see About enabling TLS 1.2.

Ensure that TLS 1.2 is enabled as a protocol for
SChannel at the operating system level
For the most part, protocol usage is controlled at three levels, the operating system
level, the framework or platform level, and the application level. TLS 1.2 is enabled by
default at the operating system level. Once you ensure that the .NET registry values are
set to enable TLS 1.2 and verify the environment is properly utilizing TLS 1.2 on the
network, you may want to edit the SChannel\Protocols registry key to disable the older,
less secure protocols. For more information on disabling TLS 1.0 and 1.1, see
Configuring Schannel protocols in the Windows Registry.

Update and configure the .NET Framework to
support TLS 1.2

Determine .NET version

<!-- p.724 -->

First, determine the installed .NET versions. For more information, see Determine which
versions and service pack levels of .NET Framework are installed.

Install .NET updates
Install the .NET updates so you can enable strong cryptography. Some versions of .NET
Framework might require updates to enable strong cryptography. Use these guidelines:

     NET Framework 4.6.2 and later supports TLS 1.1 and TLS 1.2. Confirm the registry
     settings, but no additional changes are required.

        ７ Note

        Starting in version 2107, Configuration Manager requires Microsoft .NET
        Framework version 4.6.2 for site servers, specific site systems, clients, and the
        console. If possible in your environment, install the latest version of .NET
        version 4.8.

     Update NET Framework 4.6 and earlier versions to support TLS 1.1 and TLS 1.2. For
     more information, see .NET Framework versions and dependencies.

     If you're using .NET Framework 4.5.1 or 4.5.2 on Windows 8.1, Windows Server
     2012 R2, or Windows Server 2012, it's highly recommended that you install the
     latest security updates for the .Net Framework 4.5.1 and 4.5.2 to ensure TLS 1.2 can
     be enabled properly.

     For your reference, TLS 1.2 was first introduced into .Net Framework 4.5.1 and 4.5.2
     with the following hotfix rollups:
        For Windows 8.1 and Server 2012 R2: Hotfix rollup 3099842
        For Windows Server 2012: Hotfix rollup 3099844

Configure for strong cryptography
Configure .NET Framework to support strong cryptography. Set the SchUseStrongCrypto
registry setting to DWORD:00000001 . This value disables the RC4 stream cipher and
requires a restart. For more information about this setting, see Microsoft Security
Advisory 296038.

Make sure to set the following registry keys on any computer that communicates across
the network with a TLS 1.2-enabled system. For example, Configuration Manager clients,
remote site system roles not installed on the site server, and the site server itself.

<!-- p.725 -->

For 32-bit applications that are running on 32-bit OSs and for 64-bit applications that
are running on 64-bit OSs, update the following subkey values:

  Registry

  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v2.0.50727]
        "SystemDefaultTlsVersions" = dword:00000001
        "SchUseStrongCrypto" = dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319]
        "SystemDefaultTlsVersions" = dword:00000001
        "SchUseStrongCrypto" = dword:00000001

For 32-bit applications that are running on 64-bit OSs, update the following subkey
values:

  Registry

  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v2.0.50727]
        "SystemDefaultTlsVersions" = dword:00000001
        "SchUseStrongCrypto" = dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v4.0.30319]
        "SystemDefaultTlsVersions" = dword:00000001
        "SchUseStrongCrypto" = dword:00000001

  ７ Note

  The SchUseStrongCrypto setting allows .NET to use TLS 1.1 and TLS 1.2. The
   SystemDefaultTlsVersions setting allows .NET to use the OS configuration. For

  more information, see TLS best practices with the .NET Framework.

Update SQL Server and client components
Microsoft SQL Server 2016 and later support TLS 1.1 and TLS 1.2. Earlier versions and
dependent libraries might require updates. For more information, see KB 3135244: TLS
1.2 support for Microsoft SQL Server   .

Secondary site servers need to use at least SQL Server 2016 Express with Service Pack 2
(13.2.50.26) or later.

SQL Server Native Client

  ７ Note

<!-- p.726 -->

  KB 3135244      also describes requirements for SQL Server client components.

Make sure to also update the SQL Server Native Client to at least version SQL Server
2012 SP4 (11.*.7001.0). This requirement is a prerequisite check (warning).

Configuration Manager uses SQL Server Native Client on the following site system roles:

     Site database server
     Site server: central administration site, primary site, or secondary site
     Management point
     Device management point
     State migration point
     SMS Provider
     Software update point
     Multicast-enabled distribution point
     Asset Intelligence update service point
     Reporting services point
     Enrollment point
     Endpoint Protection point
     Service connection point
     Certificate registration point
     Data warehouse service point

Enable TLS 1.2 at-scale using Automanage
Machine Configuration and Azure Arc
Automatically configures TLS 1.2 across both client and server for machines running in
Azure, on-prem, or multi-cloud environments. To get started configuring TLS 1.2 across
your machines, connect them to Azure using Azure Arc-enabled servers, which comes
with the Machine Configuration prerequisite by default. Once connected, TLS 1.2 can be
configured with point-and-click simplicity by deploying the built-in policy definition in
Azure Portal: Configure secure communication protocols (TLS 1.1 or TLS 1.2) on
Windows servers     . The policy scope can be assigned at the subscription, resource
group, or management group level, as well as exclude any resources from the policy
definition.

After the configuration has been assigned, the compliance status of your resources can
be viewed in detail by navigating to the Guest Assignments page and scoping down to
the impacted resources.

<!-- p.727 -->

For a detailed, step-by-step tutorial, see Consistently upgrade your server TLS protocol
using Azure Arc and Automanage Machine Configuration .

Update Windows Server Update Services
(WSUS)
TLS 1.2 is supported by default for WSUS on all currently supported version of Windows
Server.

To support TLS 1.2 in earlier versions of WSUS, install the following update on the WSUS
server:

     For WSUS server that's running Windows Server 2012, install update 4022721       or
     a later rollup update.

     For WSUS server that's running Windows Server 2012 R2, install update 4022720
     or a later rollup update.

  ７ Note

  On October 10th, 2023, Windows Server 2012 and Windows Server 2012 R2
  entered the Extended Support Updates phase. Microsoft will no longer provide
  support for Configuration Manager site servers or roles installed to these Operating
  Systems. For more information, see Extended Security Updates and Configuration
  Manager.

Next steps
     Common issues when enabling TLS 1.2

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.728 -->

Common issues when enabling TLS 1.2
Article • 11/16/2023

This article provides advice for common issues that occur when you enable TLS 1.2
support in Configuration Manager.

Unsupported platforms
The following client platforms are supported by Configuration Manager but aren't
supported in a TLS 1.2 environment:

      Apple OS X
      Windows devices managed with on-premises MDM

Reports don't show in the console
If reports don't show in the Configuration Manager console, make sure to update the
computer on which you're running the console. Update the .NET Framework, and enable
strong cryptography.

FIPS security policy enabled
If you enable the FIPS security policy setting for either the client or a server, Secure
Channel (Schannel) negotiation can cause them to use TLS 1.0. This behavior happens
even if you disable the protocol in the registry.

To investigate, enable Secure Channel event logging, and then review Schannel events in
the system log. For more information, see Restrict the use of certain cryptographic
algorithms and protocols in Schannel.dll.

SQL Server communication failure
If SQL Server communication fails and returns an SslSecurityError error, verify the
following settings:

      Update .NET Framework, and enable strong cryptography on each machine
      Update SQL Server on the host server
      Update SQL Server client components on all systems that communicate with SQL.
      For example, the site servers, SMS provider, and site role servers.

<!-- p.729 -->

Configuration Manager client communication
failures
If the Configuration Manager client doesn't communicate with site roles, verify that you
updated Windows to support TLS 1.2 for client-server communication by using
WinHTTP. Common site roles include distribution points, management points, and state
migration points.

Reporting services point fails and returns an
expected error
If the reporting services point doesn't configure reports, check the SRSRP.log for the
following error entry:

The underlying connection was closed: An expected error occurred on a receive.

To resolve this issue, follow these steps:

   1. Update .NET Framework, and enable strong cryptography on all relevant
     computers.

   2. After you install any updates, restart the SMS_Executive service.

Service connection point upload failures
If the service connection point doesn't upload data to SCCMConnectedService, update
the .NET Framework, and enable strong cryptography on each computer. After you
make the changes, remember to restart the computers.

Configuration Manager console displays Intune
onboarding dialog box
If the Intune onboarding dialog box appears when the console tries to connect to the
Microsoft Intune admin center, update the .NET Framework, and enable strong
cryptography on each computer. After you make the changes, remember to restart the
computers.

<!-- p.730 -->

Configuration Manager console displays failure
to sign in to Azure
When you try to create applications in Microsoft Entra ID, if the Azure Services
onboarding dialog box immediately fails after you select Sign in, update the .NET
Framework, and enable strong cryptography. After you make the changes, remember to
restart the computers.

Configuration Manager cloud services and TLS
1.2
The Azure virtual machines used by the cloud management gateway support TLS 1.2.
Supported client versions automatically use TLS 1.2.

The SMSAdminui.log may contain an error similar to the following example:

  Log

  Microsoft.ConfigurationManager.CloudBase.AAD.AADAuthenticationException
  Service returned error. Check InnerException for more details
  at
  Microsoft.ConfigurationManager.CloudBase.AAD.AADAuthenticationContext.GetAAD
  AuthResultObject
  ...
  Microsoft.IdentityModel.Clients.ActiveDirectory.AdalServiceException
  Service returned error. Check InnerException for more details
  at
  Microsoft.IdentityModel.Clients.ActiveDirectory.AuthenticationContext.RunAsy
  ncTask
  ...
  System.Net.WebException
  The underlying connection was closed: An unexpected error occurred on a
  receive.
  at System.Net.HttpWebRequest.GetResponse

In the System EventLog, SChannel EventID 36874 may be logged with the following
description: An TLS 1.2 connection request was received from a remote client
application, but none of the cipher suites supported by the client application are
supported by the server. The TLS connection request has failed.

Additional resources
     Transport layer security (TLS) best practices with the .NET Framework

<!-- p.731 -->

     KB 3135244: TLS 1.2 support for Microsoft SQL Server
     Cryptographic controls technical reference

Next steps
     Enable TLS 1.2 on clients
     Enable TLS 1.2 on the site servers and remote site systems

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.732 -->

Security documentation
Configuration Manager is secure by default. Learn more about how to configure and use
features to help keep your environment secure.

  Fundamentals

  ｅ OVERVIEW
  Security in Configuration Manager

  Role-based administration

  Plan

  ｂ GET STARTED
  Plan for security

  Certificates overview

  Configure security

  Resources

  ｉ REFERENCE
  Enable TLS 1.2

  Cryptographic controls technical reference

  Accounts

  Ports

  Feature guidance

  ｐ CONCEPT

<!-- p.733 -->

OS deployment

App management

Software update management

<!-- p.734 -->

Evaluate Configuration Manager by
building your own lab environment
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Learn how to create a lab environment to evaluate Configuration Manager for use in
your organization.

Configuration Manager is a complex and powerful tool to manage your users, devices,
and software. It's a good idea to thoroughly evaluate Configuration Manager before full
deployment, so that you can marry conceptual understanding with hands-on exercises.

This guide is primarily meant for admins who are evaluating the use of Configuration
Manager in corporate environments:

      Admins who want a solution to fully manage PCs, servers, and mobile devices

      Admins in high-security industries that require the security of on-premises device
      management with the flexibility of cloud-based device management

      Admins who want to manage the scaling-up of their on-premises server
      architecture

What this lab does
The main goal of creating this lab environment is to give you the general knowledge to
start working with Configuration Manager, and to enhance your understanding of
Configuration Manager. You'll walk through an expedited assembly of the current
version of Configuration Manager, by using two servers:

      One that hosts Active Directory, the domain controller, and the DNS server

      One that hosts Configuration Manager and all associated SQL Server components

Client machines are installed within Hyper-V. The lab itself can also be run as a fully
virtualized system on a single server.

What this lab does not do
This lab will not take you through all Configuration Manager scenarios. It is not
designed to be immediately migrated into an active environment.

<!-- p.735 -->

When you build this lab, you will have a functional environment to work in. But this
environment will not be optimized for factors like system performance, hard disk space
management, and SQL Server storage.

Recommended reading before you build the
lab
There is a wealth of content available in Documentation for Configuration Manager. We
recommend that you read the following topics from this library before you start to build
the lab:

     Learn core concepts about the Configuration Manager console, end-user portals,
     and example scenarios in Introduction to Configuration Manager.

     Learn about the primary management capabilities of Configuration Manager in
     Features and capabilities of Configuration Manager.

     Bolster your knowledge with Fundamentals of Configuration Manager.

     Learn the importance of security roles in Fundamentals of role-based
     administration for Configuration Manager.

     Learn about content management in Concepts for content management.

     Learn how to successfully support daily tasks throughout your deployment in
     Understand how clients find site resources and services for Configuration Manager.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.736 -->

Set up a Configuration Manager lab
Article • 01/12/2024

Applies to: Configuration Manager (current branch)

Following the guidance in this topic will enable you to set up a lab for evaluating
Configuration Manager with simulated real-life activities.

  ７ Note

  Microsoft offers a pre-configured version of this lab using an evaluation version of
  Configuration Manager. For more information, see Microsoft Intune and
  Configuration Manager evaluation lab kit .

Core components
Setting up your environment for Configuration Manager requires some core
components to support the installation of Configuration Manager.

      The lab environment uses Windows Server 2012 R2, into which we'll install
      Configuration Manager.

      You can download an evaluation version of Windows Server 2012 R2 from the
      Evaluation Center   .

      Consider modifying or disabling Internet Explorer Enhanced Security Configuration
      in order to more easily access some of the downloads referenced throughout the
      course of these exercises. For more information, see Internet Explorer: Enhanced
      Security Configuration.

      The lab environment uses SQL Server 2012 SP2 for the site database.

      You can download an evaluation version of SQL Server 2012 from the Microsoft
      Download Center     .

      SQL Server has Supported versions of SQL Server that must be met for use with
      Configuration Manager.

         Configuration Manager requires a 64-bit version of SQL Server to host the site
         database.

         SQL_Latin1_General_CP1_CI_AS as the SQL Collation class.

<!-- p.737 -->

        Windows authentication, rather than SQL Server authentication, is required.

        A dedicated SQL Server instance is required.

        Don't limit the system addressable memory for SQL Server.

        Configure the SQL Server service account to run using a low rights domain user
        account.

        You must install SQL Server reporting services.

        Intersite communications use the SQL Server Service Broker on default port
        TCP 4022.

        Intrasite communications between the SQL Server database engine and select
        Configuration Manager site system roles use default port TCP 1433.

     The domain controller uses Windows Server 2008 R2 with Active Directory
     Domain Services installed. The domain controller also functions as the host for the
     DHCP and the DNS servers for use with a fully qualified domain name.

     For more information, see overview of Active Directory Domain Services.

     Hyper-V is used with a few virtual machines to verify that the management steps
     taken in these exercises are functioning as expected. A minimum of three virtual
     machines is recommended, with Windows 10 installed.

     For more information, see overview of Hyper-V.

     Administrator permissions will be required for all of these components.

        Configuration Manager requires an administrator with local permissions within
        the Windows Server environment

        Active Directory requires an administrator with permissions to modify the
        schema

        Virtual machines require local permissions on the machines themselves

Though not required for this lab, you can review Supported configurations for
Configuration Manager for additional information on requirements for implementing
Configuration Manager. Refer to documentation for software versions other than those
referenced here.

Once you have installed all of these components, there are other steps you must take to
configure your Windows environment for Configuration Manager:

<!-- p.738 -->

Prepare Active Directory content for the lab
For this lab, you'll create a security group, then add a domain user to it.

     Security group: Evaluation

         Group scope: Universal

         Group type: Security

     Domain user: ConfigUser

     Under normal circumstances, you wouldn't grant universal access to all users
     within your environment. You're doing so with this user in order to streamline
     bringing your lab online.

The next steps required to enable Configuration Manager clients to query Active
Directory Domain Services to locate site resources are listed over the next procedures.

Create the System Management container
Configuration Manager won't automatically create the required System Management
container in Active Directory Domain Services when the schema is extended. Therefore,
you'll create this for your lab. This step will require you to install ADSI Edit.

Ensure that you're logged on as an account that has Create All Child Objects permission
on the System Container in Active Directory Domain Services.

To create the System Management container:
   1. Run ADSI Edit, and connect to the domain in which the site server resides.

   2. Expand Domain<computer fully qualified domain name>, expand
     <distinguished name>, right-click CN=System, click New, and then click Object.

   3. In the Create Object dialog box, select Container, and then click Next.

   4. In the Value box, type System Management, and then click Next.

   5. Click Finish to complete the procedure.

Set security permissions for the System
Management container

<!-- p.739 -->

Grant the site server's computer account the permissions that are required to publish
site information to the container. You'll use ADSI Edit for this task as well.

  ） Important

  Confirm that you are connected to the site server's domain prior to beginning the
  following procedure.

To set security permissions for the System Management container:
   1. In the console pane, expand the site server's domain, expand DC=<server
     distinguished name>, and then expand CN=System. Right-click CN=System
     Management, and then click Properties.

   2. In the CN=System Management Properties dialog box, click the Security tab, and
     then click Add to add the site server computer account. Grant the account Full
     Control permissions.

   3. Click Advanced, select the site server's computer account, and then click Edit.

   4. In the Apply onto list, select This object and all descendant objects.

   5. Click OK to close the ADSI Edit console and complete the procedure.

     For more information, see Extend the Active Directory schema for Configuration
     Manager

Extend the Active Directory schema using
extadsch.exe
You'll extend the Active Directory schema for this lab, as this allows you to use all
Configuration Manager features and functionality with the least amount of
administrative overhead. Extending the Active Directory schema is a forest-wide
configuration that is done one time per forest. Extending the schema permanently
modifies the set of classes and attributes in your base Active Directory configuration.
This action is irreversible. Extending the schema allows Configuration Manager to access
components that will allow it to function most effectively within your lab environment.

  ） Important

<!-- p.740 -->

  Ensure that you are logged on to the schema master domain controller with an
  account that is a member of the Schema Admins security group. Attempting to use
  alternate credentials will fail.

To extend the Active Directory schema using extadsch.exe:
   1. Create a backup of the schema master domain controller's system state. For more
     information about backing up master domain controller, see Windows Server
     Backup

   2. Navigate to \SMSSETUP\BIN\X64 in the installation media.

   3. Run extadsch.exe.

   4. Verify that the schema extension was successful by reviewing the extadsch.log
     located in the root folder of the system drive.

     For more information, see Extend the Active Directory schema for Configuration
     Manager.

Other required tasks
You'll also need to complete the following tasks prior to installation.

Create a folder for storing all downloads

There will be multiple downloads required for components of the installation media
throughout this exercise. Before beginning any installation procedures, determine a
location that won't require you to move these files until you wish to decommission your
lab. A single folder with separate subfolders to store these downloads is recommended.

Install .NET and activate Windows Communication Foundation

You'll need to install two .NET Frameworks: first, .NET 3.5.1 and then .NET 4.5.2+. You'll
also need to activate Windows Communication Foundation (WCF). WCF is designed to
offer a manageable approach to distributed computing, broad interoperability, and
direct support for service orientation, and simplifies development of connected
applications through a service-oriented programming model. For more information, see
What Is Windows Communication Foundation?.

To install .NET and activate Windows Communication Foundation:

<!-- p.741 -->

   1. Open Server Manager, then navigate to Manage. Click Add Roles and Features to
     open the Add Roles and Features Wizard.

   2. Review the information provided in the Before You Begin panel, then click Next.

   3. Select Role-based or feature-based installation, then click Next.

   4. Select your server from the Server Pool, then click Next.

   5. Review the Server Roles panel, then click Next.

   6. Add the following Features by selecting them from the list:

           .NET Framework 3.5 Features
              .NET Framework 3.5 (includes .NET 2.0 and 3.0)

           .NET Framework 4.5 Features

              .NET Framework 4.5

              ASP.NET 4.5

              WCF Services

                   HTTP Activation

                   TCP Port Sharing

   7. Review the Web Server Role (IIS) and Role Services screen, then click Next.

   8. Review the Confirmation screen, then click Next.

   9. Click Install and verify that the installation completed properly in the Notifications
     pane of Server Manager.

 10. After the base installation of .NET completes, navigate to the Microsoft Download
     Center       to obtain the web installer for the .NET Framework 4.5.2. Click the
     Download button, then Run the installer. It will automatically detect and install the
     required components in your selected language.

Enable BITS, IIS, and RDC

The Background Intelligent Transfer Service (BITS) is used for applications that need to
transfer files asynchronously between a client and a server. By metering the flow of the
transfers in the foreground and background, BITS preserves the responsiveness of other
network applications. It will also automatically resume file transfers if a transfer session
is interrupted.

<!-- p.742 -->

You'll install BITS for this lab, as this site server will also be used as a management point.

Internet Information Services (IIS) is a flexible, scalable web server that can be used to
host anything on the web. It's used by Configuration Manager for many site system
roles. For additional information on IIS, review Websites for site system servers.

Remote Differential Compression (RDC) is a set of APIs that applications can use to
determine if any changes have been made to a set of files. RDC enables the application
to replicate only the changed portions of a file, keeping network traffic to a minimum.

To enable BITS, IIS, and RDC site server roles:

   1. On your site server, open Server Manager. Navigate to Manage. Click Add Roles
     and Features to open the Add Roles and Features Wizard.

   2. Review the information provided in the Before You Begin panel, then click Next.

   3. Select Role-based or feature-based installation, then click Next.

   4. Select your server from the Server Pool, then click Next.

   5. Add the following Server Roles by selecting them from the list:

           Web Server (IIS)

              Common HTTP Features

                 Default Document

                 Directory Browsing

                 HTTP Errors

                 Static Content

                 HTTP Redirection

              Health and Diagnostics

                 HTTP Logging

                 Logging Tools

                 Request Monitor

                 Tracing

           Performance

<!-- p.743 -->

  Static Content Compression

  Dynamic Content Compression

Security

  Request Filtering

  Basic Authentication

  Client Certificate Mapping Authentication

  IP and Domain Restrictions

  URL Authorization

  Windows Authentication

Application Development

  .NET Extensibility 3.5

  .NET Extensibility 4.5

  ASP

  ASP.NET 3.5

  ASP.NET 4.5

  ISAPI Extensions

  ISAPI Filters

  Server Side Includes

FTP Server
  FTP Service

Management Tools

  IIS Management Console

  IIS 6 Management Compatibility

     IIS 6 Metabase Compatibility

     IIS 6 Management Console

     IIS 6 Scripting Tools

<!-- p.744 -->

                 IIS 6 WMI Compatibility

              IIS 6 Management Scripts and Tools

              Management Service

   6. Add the following Features by selecting them from the list:

           Background Intelligent Transfer Service (BITS)
              IIS Server Extension

           Remote Server Administration Tools

              Feature Administration Tools

              BITS Server Extensions Tools

   7. Click Install and verify that the installation completed properly in the Notifications
     pane of Server Manager.

By default, IIS blocks several types of file extensions and locations from access by HTTP
or HTTPS communication. To enable these files to be distributed to client systems, you'll
need to configure request filtering for IIS on your distribution point. For more
information, see IIS Request Filtering for distribution points.

To configure IIS filtering on distribution points:
   1. Open IIS Manager and select the name of your server in the sidebar. This will take
     you to the Home screen.

   2. Verify that Features View is selected at the bottom of the Home screen. Navigate
     to IIS and open Request Filtering.

   3. In the Actions pane, click Allow File Name Extension...

   4. Type .msi into the dialog box and click OK.

Installing Configuration Manager
You'll create a Determine when to use a primary site to manage clients directly. This will
allow your lab environment to support management for Site system scale of potential
devices.
During this process, you'll also install the Configuration Manager console, which will be
used to manage your evaluation devices going forward.

<!-- p.745 -->

Before you begin the installation, launch the Prerequisite Checker on the server using
Windows Server 2012 to confirm that all settings have been correctly enabled.

To download and install Configuration Manager:

   1. Navigate to the Evaluation Center       page to download the newest evaluation
     version of Configuration Manager.

   2. Decompress the download media into your predefined location.

   3. Follow the installation procedure listed at Install a site using the Configuration
     Manager Setup Wizard. Within that procedure, you'll input the following:

                                                                                  ﾉ   Expand table

      Step in site installation   Selection
      procedure

      Step 4: the Product Key     Select Evaluation.
      page

      Step 7: Prerequisite        Select Download required files and specify your predefined
      Downloads                   location.

      Step 10: Site and           - Site code:LAB
      Installation Settings       - Site name:Evaluation
                                  - Installation folder: specify your predefined location.

      Step 11: Primary Site       Select Install the primary site as a stand-alone site, then click
      Installation                Next.

      Step 12: Database           - SQL Server name (FQDN): input your FQDN here.
      Installation                - Instance name: leave this blank, as you'll use the default
                                  instance of SQL Server that you previously installed.
                                  - Service Broker Port: leave as default port of 4022.

      Step 13: Database           Leave these settings as default.
      Installation

      Step 14: SMS Provider       Leave these settings as default.

      Step 15: Client             Confirm that All site system roles accept only HTTPS
      Communication Settings      communication from clients isn't selected

      Step 16: Site System        Input your FQDN and confirm that your selection of All site
      Roles                       system roles accept only HTTPS communication from clients
                                  is still deselected.

<!-- p.746 -->

Enable publishing for the Configuration
Manager site
Each Configuration Manager site publishes its own site-specific information to the
System Management container within its domain partition in the Active Directory
schema. Bidirectional channels for communication between Active Directory and
Configuration Manager must be opened to handle this traffic. You'll also additionally
enable Forest Discovery to determine certain components of your Active Directory and
network infrastructure.

To configure Active Directory forests for publishing:
   1. In the bottom-left corner of the Configuration Manager console, click
     Administration.

   2. In the Administration workspace, expand Hierarchy Configuration, then click
     Discovery Methods.

   3. Select Active Directory Forest Discovery and click Properties.

   4. In the Properties dialog box, select Enable Active Directory Forest Discovery.
     Once this is active, select Automatically create Active Directory site boundaries
     when they are discovered. A dialog box will appear that states Do you want to
     run full discovery as soon as possible? Click Yes.

   5. In the Discovery Method group at the top of the screen, click Run Forest
     Discovery Now, then navigate to Active Directory Forests in the sidebar. Your
     Active Directory forest should be shown in the list of discovered forests.

   6. Navigate to the top of the screen, to the General tab.

   7. In the Administration workspace, expand Hierarchy Configuration, then click
     Active Directory Forests.

To enable a Configuration Manager site to publish site information
to your Active Directory forest:

   1. In the Configuration Manager console, click Administration.

   2. You'll configure a new forest that hasn't yet been discovered.

   3. In the Administration workspace, click Active Directory Forests.

<!-- p.747 -->

   4. On the Publishing tab of the site properties, select your connected forest, then
     click Ok to save the configuration.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.748 -->

Create a Configuration Manager lab in
Azure
Article • 10/04/2022

Applies to: Configuration Manager (current branch, technical preview branch)

This guide describes how to build a Configuration Manager lab environment in
Microsoft Azure. It uses Azure templates to simplify and automate the creation of a lab
using Azure resources. Two Azure templates are provided:

      Configuration Manager technical preview Azure template installs the latest version
      of the Configuration Manager technical preview branch.
      Configuration Manager current branch Azure template installs the evaluation of
      the latest version of Configuration Manager current branch.

For more information, see Configuration Manager on Azure.

Prerequisites
This process requires an Azure subscription in which you can create the following
objects:

      Two Standard_B2s virtual machines for domain controller, management point, and
      distribution point.
      Zero to three virtual machines for client devices.
      One Standard_B2ms virtual machine for the primary site server and the SQL Server
      database server
      If you choose to create a hierarchy, one other Standard_B2ms virtual machine for
      the central administration site.
      Standard_LRS storage account.

   Tip

  To help determine potential costs, see the Azure pricing calculator     .

Process
   1. Go to the Configuration Manager technical preview template        or Configuration
      Manager current branch template      .

<!-- p.749 -->

2. Select Deploy to Azure, which opens the Azure portal.

3. Complete the Azure quickstart template with the following information:

       Basics

          Subscription: The name of the subscription in which to create the VMs

          Resource group: Select a resource group to use for these VMs

          Location: Select an Azure data center to host this lab environment

       Settings

          Prefix: The prefix name of the machines. For more information, see Azure
          VM info.

          Admin Username: The name of a user on the VMs with administrative
          rights. You use this user to sign in to the VMs.

          Admin Password: The password must meet the Azure complexity
          requirements. For more information, see adminPassword.

          Configuration: You can choose "Standalone" or "Hierarchy". This setting is
          available for the current branch template only.

    ） Important

    The following settings are required by Azure. Use the default values. Don't
    change these values.

          _artifacts Location: The location of the scripts for this template

          _artifacts Location Sas Token: The sasToken is required to access the
          artifacts location

          Location: The location for all resources

    ７ Note

    If you edited the Azure template before you deployed it, then you need to
    change the _artifactsLocation value.

<!-- p.750 -->

             For the technical preview template, the value is
              https://raw.githubusercontent.com/Azure/azure-quickstart-

             templates/master/application-workloads/sccm/sccm-

             technicalpreview/azuredeploy.json

             For the current branch template, the value is
              https://raw.githubusercontent.com/Azure/azure-quickstart-

             templates/master/application-workloads/sccm/sccm-

             currentbranch/azuredeploy.json

   4. Read the terms and conditions. If you agree, select I agree to the terms and
     conditions stated above. Then select Purchase to continue.

Azure validates the settings, and then begins the deployment. Check the status of the
deployment in the Azure portal.

  ７ Note

  The process can take 2-4 hours. Even when the Azure portal shows successful
  deployment, configuration scripts continue to run. Don't restart the VMs during the
  process.

To see the status of the configuration scripts, connect to the <prefix>PS01 server, and
view the following file: %windir%\TEMP\ProvisionScript\PS01.json . If it shows all steps as
complete, the process is done.

  ７ Note

  When you use the current branch template, it uses the CAS.json file at the same
  location on the <prefix>CS01 server.

To connect to the VMs, first get from the Azure portal the public IP addresses for each
VM. When you connect to the VM, the domain name is contoso.com . Use the credentials
that you specified in the deployment template. For more information, see How to
connect and log on to an Azure virtual machine running Windows.

Azure VM info
All VMs have the following specifications:

<!-- p.751 -->

     150 GB of disk space
     Both a public and private IP address. The public IPs are in a network security group
     that only allows remote desktop connections on TCP port 3389.

The prefix that you specified in the deployment template is the VM name prefix. For
example, if you set "contoso" as the prefix, then the domain controller machine name is
contosoDC .

<prefix>DC01

     Active Directory domain controller
     Standard_B2s, which has two processors and 4 GB of memory
     Windows Server 2022 Datacenter edition

Windows features and roles
     Active Directory Domain Services (ADDS)
     .NET
     Remote Differential Compression (RDC)

<prefix>PS01

     Standard_B2ms, which has two processors and 8 GB of memory
     Windows Server 2019 Datacenter edition
     SQL Server
     Windows 10 ADK with Windows PE
     Configuration Manager primary site

Windows features and roles

     .NET
     Remote Differential Compression (RDC)
     Internet Information Service (IIS)

<prefix>DPMP01

     Standard_B2s, which has two processors and 4 GB of memory
     Windows Server 2019 Datacenter edition
     Distribution point
     Management point

<!-- p.752 -->

Windows features and roles
     .NET
     Remote Differential Compression (RDC)
     Internet Information Service (IIS)
     Background intelligent transfer service (BITS)

<prefix>CL01

     Only for Configuration Manager current branch evaluation template
     Windows 10
     Configuration Manager client

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.753 -->

Technical preview for Configuration
Manager
Article • 11/29/2024

Applies to: Configuration Manager (technical preview branch)

This article provides details about the monthly technical preview branch of
Configuration Manager. The technical preview introduces new functionality that
Microsoft is working on. It introduces new features that aren't yet included in the
current branch of Configuration Manager. These features might eventually be included
in an update to the current branch. Before we finalize the features, we want you to try
them out and give us feedback.

Because this release is a technical preview, details and functionality are subject to
change.

This information applies to all versions of the Configuration Manager technical preview
branch. This article lists each new feature along with the technical preview version in
which it first appears. For example, version 2201 for January ( 01 ) of 2022 ( 22 ). Separate
articles dedicated to each preview version detail the individual features.

For information about what's new in the current branch of Configuration Manager, see
What's new in Configuration Manager incremental versions.

   Tip

  You can use RSS to be notified when this page is updated. For more information,
  see How to use the docs.

Requirements and limitations

  ） Important

  The technical preview is licensed for use only in a lab environment. Microsoft may
  not provide support services and certain features may not be available in technical
  previews. Additionally, technical preview software may have reduced or different
  security, privacy, accessibility, availability, and reliability standards relative to
  commercially provided software.

<!-- p.754 -->

For most product prerequisites, use the information in the Supported configurations.
The following exceptions apply to the technical preview branch:

     Each install is active for 360 days before it becomes inactive.

     English is the only language supported.

     It only supports the following setup command-line parameters:
        /silent
        /testdbupgrade

     The service connection point installs to online mode. It doesn't support offline
     mode.

       ７ Note

       You may need to allow specific internet URLs, some of which are specific to
       the technical preview branch. For more information, see Internet access
       requirements.

     The separate articles for each specific version of the technical preview include
     additional limitations or requirements, as applicable.

     The following features aren't supported with the technical preview branch:

        Migration to or from this preview branch.

        Upgrade to this preview branch.

        Site recovery from the cd.latest folder.

     There's no support for updating to current branch from this preview branch.

       ７ Note

       When updates are available for a preview version, you still find and install
       them from the Updates and Servicing node of the Configuration Manager
       console. For a video of the in-console upgrade process, see Installing
       Configuration Manager update packages          on youtube.com.

     It only supports a standalone primary site. There's no support for a central
     administration site, multiple primary sites, or secondary sites.

<!-- p.755 -->

The technical preview branch of Configuration Manager supports the following products
and technologies:

     Unless otherwise noted, the technical preview branch supports the same versions
     of SQL Server as the current branch. For more information, see Supported SQL
     Server versions.

     The site supports up to 10 clients, which can run any supported client OS version.

  ７ Note

  The inclusion of these products in this content doesn't imply an extension of
  support for a version that's beyond its support lifecycle. Configuration Manager
  doesn't support products that are beyond their support lifecycle. For more
  information, see Microsoft Lifecycle Policy     .

Install and update
The Configuration Manager technical preview branch for lab use is distinct from the
Configuration Manager current branch for production use.

First install a baseline version of the technical preview branch. After installing a baseline
version, then use in-console updates to bring your installation up to date with the most
recent preview version. Typically, new versions of the technical preview are available
each month.

Microsoft supports each technical preview version up until three successive versions are
available. For example, when version 1908 released, version 1904 was no longer in
support. Versions 1905, 1906, and 1907 remained in support. When a baseline falls out
of support, it's still supported for installing a new technical preview site, assuming you
immediately update to a supported version. The older baseline is supported until a new
baseline version is available. Update to the latest available version from the baseline,
and then repeat the update process until you install the latest technical preview version.

   Tip

  When you install an update to the technical preview, you update your preview
  installation to that new technical preview version. A technical preview installation
  never has the option to upgrade to a current branch installation. It also never
  receives updates from the current branch release.

<!-- p.756 -->

  Several times throughout the year, there are technical preview branch and current
  branch versions with the same version number. For example, there is a technical
  preview version 2006 and a current branch version 2006.

Active baseline versions
Install a baseline version for up to one year after its release. When you install a new
technical preview site, use the latest baseline version:

     Technical preview version 2411

Download a baseline version from the Evaluation Center       .

Providing feedback
We love to hear your feedback about the new features in the technical preview. For
more information, see Product feedback.

If you have ideas about new features you would like to see, let us know! Submit new
ideas and vote on the ideas by others: Feedback for Configuration Manager        .

Features in the most recent version
The following features are available with the most recent Configuration Manager
technical preview version:

Technical preview version 2411
     Operating System support added for Windows 11 24H2 and Windows Server 2025
     Enhanced Security for CMG
     SQL 2012 and 2014 support is deprecated
     Software metering support in Arm64 devices

  ７ Note

  Features that were available in a previous version of the technical preview remain
  available in later versions. Similarly, features that are added to the Configuration
  Manager current branch remain available in the technical preview branch.

<!-- p.757 -->

Features in recent technical previews
The following features were released with previous versions of the Configuration
Manager technical preview branch since the latest current branch version:

   Tip

  When a new current branch version is available, features that are available in that
  version are listed in the latest What's new article. For more information, see What's
  new in incremental versions.

Technical preview version 2405
     Introducing Centralized Search - Desired Workspace Selection
     BitLocker support in Arm devices
     Configuration Manager now support SQL Extended Protection for Authentication
     Performance Enhancement of policy processing and collection evaluation

  ７ Note

  Features that were available in a previous version of the technical preview remain
  available in later versions. Similarly, features that are added to the Configuration
  Manager current branch remain available in the technical preview branch.

Technical preview version 2401
     Automated diagnostic Dashboard for Software Update Issues
     Introducing Centralized Search box: Effortlessly Find What You Need in the
     Console!
     HTTPS or Enhanced HTTP should be enabled for client communication from this
     version of Configuration Manager
     Microsoft Azure Active Directory re-branded to Microsoft Entra ID
     Enhancement in Deploying Software Packages with Dynamic Variables
     Enabling Auto-Image Patching for CMG Virtual Machine Scale Sets
     Window 11 Readiness dashboard to support Windows 23H2
     Windows Server 2012/2012 R2 operating system site system roles are not
     supported from this version of Configuration Manager
     Upgrade to CM 2403 is blocked if CMG V1 is running as a cloud service (classic)
     Improvements to Bitlocker

<!-- p.758 -->

Technical preview version 2311
   Folder support for Scripts node in Software Library
   New parameter SoftwareUpdateO365Language is added to Save-
   CMSoftwareUpdate cmdlet
   Support for ARM64 Operating System Deployment
   Resource access profiles and deployments will block Configuration manager
   upgrade
   WildCard Support added in Defender Exploit Guard policy for Controlled Folders

Technical preview version 2307
   Windows 11 Edition Upgrade using Configuration Manager policy settings
   Windows 11 Upgrade Readiness Dashboard
   Option to schedule scripts' runtime
   External service notification Run details from Azure Logic application
   Maintenance window creation using PS cmdlet
   Update Orchestrator Service (USO) for Windows 11 22H2 or later with windows
   native reboot experience

Technical preview version 2305
   OSD preferred MP option for PXE boot scenario
   New Site Maintenance task “Delete Aged Task Execution Status Messages” is now
   available on primary servers to cleanup data older than 30 days or configured
   number of days
   CMG creation using 3rd PartyApp via Console
   CMG creation using 3rd Party ServerApp via PowerShell
   Attack Surface Reduction (ASR) capability now marks Server SKU as compliant only
   after enforcement
   Enhancing security for External service notifications URL
   Enable Bitlocker through ProvisionTS
   Client certificate state in console (self-signed) to match state in control panel(PKI)

Technical preview version 2303
   SQL Server 2022 version support added for Configuration Manager
   Dark theme extended to one customer voice (OCV) wizard
   Prerequisites for the site server roles now include ODBC driver for SQL Server

<!-- p.759 -->

Technical preview version 2302
   Dark theme extended to delete secondary site wizard
   Enable Windows features introduced via Windows servicing that are off by default

Technical preview version 2301
   Removing Microsoft Store for Business and Education new config capability
   Update to the default value of supersedence age in months for software updates
   Microsoft Configuration Manager product branding
   Improvements to Cloud Sync (Collections to Microsoft Entra group
   Synchronization) feature

Technical preview version 2211
   Authorization failure message in admin service now shown in Status message
   viewer
   Network Access Account (NAA) account usage alert
   Improvements to Cloud Sync (Collections to Microsoft Entra group
   Synchronization) feature

Technical preview version 2210
   Featured Apps in Software Center

Technical preview version 2209
   Improvements to the console
   Improvements to the dark theme
   Other Updates

Technical preview version 2208
   Intune RBAC for tenant attached devices
   Dark theme is now extended to additional dashboards

Technical preview version 2207
   Distribution point content migration

<!-- p.760 -->

   Improvements to Configuration Manager policies for Microsoft Defender
   Application Guard
   PowerShell release notes preview

Technical preview version 2206
   Default site boundary group behavior to support cloud source selection
   PowerShell release notes preview

Technical preview version 2205
   Offset for reoccurring monthly maintenance window schedules
   Improvements to cloud management gateway (CMG) workflow
   Script execution timeout for compliance settings
   Microsoft Defender for Endpoint onboarding for Windows Server 2012 R2 and
   Windows Server 2016
   PowerShell release notes preview

Technical preview version 2204
   Administration Service Management option
   Folders for automatic deployment rules (ADRs)

Technical preview version 2203
   Dark theme for the console
   Escrow BitLocker recovery password to the site during a task sequence
   PowerShell release notes preview

Technical preview version 2202
   Delete collection references
   Pre-download content for available software updates
   Added folder support for nodes in the Software Library
   New client health checks
   Improvements to implicit uninstall
   Improvements for sending feedback
   Improvements to Management Insights
   Improvements to dashboards
   ADR scheduling improvements for deployments
