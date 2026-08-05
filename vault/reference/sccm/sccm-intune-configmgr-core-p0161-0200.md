---
title: "Core infrastructure documentation — pages 161-200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0161-0200
family: sccm
documentKind: "doc"
abstract: "convenient reminder. Add it when you run Configuration Manager setup or later from within the Configuration Manager console. ７ Note Microsoft doesn't validate the expiration date you specify, and doesn't use this date for license validation. Use it as a reminder of your expirati"
---

# Core infrastructure documentation — pages 161-200

<!-- p.161 -->

convenient reminder. Add it when you run Configuration Manager setup or later from
within the Configuration Manager console.

  ７ Note

  Microsoft doesn't validate the expiration date you specify, and doesn't use this date
  for license validation. Use it as a reminder of your expiration date. This value is
  useful when Configuration Manager periodically checks for new software updates
  offered online. Your Software Assurance license status should be current to be
  eligible to use these additional updates.

To specify the Software Assurance expiration date
     When you run Setup from the Configuration Manager media, specify the value on
     the Product Key page of the Setup wizard.

     In the Configuration Manager console, in Hierarchy Settings, specify the value on
     the Licensing tab.

Licensing resources
To learn more about product licensing details, use the following resources.

Microsoft Volume Licensing Service Center (VLSC)
     Overview of VLSC

     Microsoft Volume Licensing Product Terms

     Volume license customers can get a summary of their licenses from the Volume
     License Service Center    . Go to the Licenses menu, and select Licenses Summary.

VLSC videos
     For training videos on how VLSC works, go to Microsoft Volume Licensing Service
     Center training and resources     and select How-to videos.

     Where to look up your active Software Assurance agreement          (starting at 43
     seconds)

<!-- p.162 -->

     How to get permissions for VLSC      . You can delegate VLSC read and write
     permissions to other people in your organization.

Next steps
Frequently asked questions for Configuration Manager branches and licensing

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.163 -->

Use the Configuration Manager client
software for extended interoperability with
future versions of a Current Branch site
Article • 05/08/2025

Applies to: Configuration Manager (current branch)

Business requirements might not allow you to regularly update the Configuration Manager
client on some devices. For example, you need to follow change management policies, or the
device is mission-critical. Accommodate these needs by installing a new client for long-term
use, called the extended interoperability client (EIC). Only use the EIC for specific devices that
can't be frequently updated, like kiosk or point-of-sale devices. Continue to use automatic
client upgrade for most of your clients.

How it works
Typically, when you install a new in-console update for Configuration Manager, clients
automatically update their client software so they can use those new features. With this
scenario, you still update to the current branch receiving the new features and updates. Most
devices update the Configuration Manager client software with each version update you install.
However, on a subset of critical systems that you don't want to receive client software updates,
you install the extended interoperability client. These clients don't install new client software
until you explicitly deploy a new version of the client software to them.

Supported versions
For more information on the current supported versions, see Support for Configuration
Manager current branch versions.

   Tip

  The EIC is supported for the client versions which are still in the supported list of
  Configuration Manager versions. For example, when Configuration Manager 2503 is the
  latest CB version, EIC supported client version can be on 2403.

Plan to update the extended interoperability client on devices that you manage with the
current branch before support for the client expires. To do so, download a new version of the
client from Microsoft, and then deploy that updated client software to your devices that use
the current extended interoperability client.

<!-- p.164 -->

How to use the EIC
   1. Add these devices to a collection, and exclude that collection from automatic client
      upgrades. For more information, see How to exclude clients from upgrade.

   2. Obtain a supported version of the EIC from the \SMSSETUP\Client folder of the
      Configuration Manager update installation media. Make sure that you copy the entire
      contents of the folder.

   3. Manually install the EIC on those devices. For more information, see Manually install the
      client.

Limitations
      Updates for the extended interoperability client software aren't available by using in-
      console updates. For more information on how to update the EIC, see How to upgrade an
      excluded client.

      The EIC only supports the following features:
           Software updates
           Hardware and software inventory
           Packages and programs

Next steps
How to exclude clients from upgrade

To make sure that clients are installed correctly on the devices you want, see How to monitor
clients.

<!-- p.165 -->

Introduction to the long-term servicing
branch of Configuration Manager
ﾃ     Summarize this article for me

Applies to: System Center Configuration Manager (Long-Term Servicing Branch)

The long-term servicing branch (LTSB) of Configuration Manager is a distinct branch that's
designed as an install option available to all customers. However, it's the only option for
customers who let lapse their Software Assurance (SA) or equivalent subscription rights for
Configuration Manager.

Based on Configuration Manager version 1606, the LTSB has reduced functionality when
compared to the current branch of Configuration Manager.

In some cases, the support lifecycle of a dependent component may end before the end of
support for the Configuration Manager LTSB itself. In such scenarios, Configuration Manager
LTSB continues to be supported through its defined end of support, provided that the reported
issue is not caused by the out-of-support dependent component.

     Tip

    The Configuration Manager LTSB isn't related to the System Center suite long-term
    servicing channel (LTSC). For more information, see Overview of System Center release
    options.

Features that aren't available
The current branch of Configuration Manager supports the following functionality that isn't
available when you use the LTSB:

      In-console updates that add new features and improvements.
      Support for newly released operating systems to use as site servers and clients.
      On-premises MDM
      The Windows servicing dashboard and servicing plans, including support for recent
      Windows versions.
      Support for future releases of Windows Server and Windows 10 LTSB
      Asset Intelligence
      Cloud-based distribution points
      Exchange Online as an Exchange Connector

<!-- p.166 -->

Although support for these features isn't available with the LTSB, some features remain visible
in the Configuration Manager console, but can't be selected or used.

Cloud integrations, as well as any features included with Configuration Manager current branch
version 1610 or later, aren't available to the LTSB. These features include, but aren't limited to
the following:

     Co-management
     Cloud management gateway
     Microsoft Entra integration
     Apps from the Microsoft Store for Business

Find LTSB documentation
The LTSB is based on current branch version 1606. Use the current branch documentation, with
caveats and limitations that are specific to the LTSB. Those caveats and limitations are identified
in the following articles:

     Install the LTSB
     Upgrade the LTSB to the current branch
     Supported configurations for the LTSB
     Manage the LTSB of Configuration Manager

When you reference current branch documentation for the LTSB, details that apply to version
1606 or earlier also apply to the LTSB. Features or details that are introduced with version 1610
or later aren't supported by the LTSB.

Licensing overview for the LTSB
Customers with active Software Assurance (SA) on Configuration Manager licenses, or with
equivalent subscription rights as of October 1, 2016, have rights to use the October 2016
version 1606 release of Configuration Manager. Customers with rights to Configuration
Manager on or after October 1, 2016, will find two licensed options upon installation: current
branch and long-term servicing branch (LTSB).

Customers that have perpetual rights to System Center Configuration Manager, or that allow
SA or subscription to lapse after October 1, can install the version of System Center
Configuration Manager LTSB that is current at the time of lapse.

For more information about these licenses, see the Complete terms and conditions for the
products you purchase through Microsoft Volume Licensing programs           .

<!-- p.167 -->

For more information about licensing for Configuration Manager branches, see Configuration
Manager licensing and branches.

Next Steps
If you decide that the Configuration Manager LTSB is the correct branch for your environment,
install a new LTSB site as part of a new hierarchy, or upgrade a System Center 2012
Configuration Manager site and hierarchy.

Last updated on 03/12/2026

<!-- p.168 -->

Supported Configurations for the Long-
Term Servicing Branch of System Center
Configuration Manager
Article • 10/04/2022

Applies to: System Center Configuration Manager (Long-Term Servicing Branch)

Use the information in this topic to understand what operating systems and product
dependencies are supported by the Long-Term Servicing Branch (LTSB) of Configuration
Manager. If not stated otherwise in this or the LTSB specific topics, the same
configurations and limitations that apply to the Current Branch version 1606 apply to
the LTSB. When conflicts occur, use the information that applies to the edition you are
using. Typically, the LTSB is more limited than the Current Branch.

General statement of support
The following products and technologies are supported by this branch of Configuration
Manager. However, their inclusion in this content does not express an extension of
support for any product or version beyond that product's individual support lifecycle.
Products that are beyond their support lifecycle are not supported for use with
Configuration Manager. For more information, visit the Microsoft Support Lifecycle
website and read the Microsoft Support Lifecycle Policy FAQ.

Additionally, products and product versions that are not listed in the following topics
are not supported unless they have been announced on the Enterprise Mobility +
Security Blog .

Limitations for future support: The LTSB has limited support for future server and client
operating systems and product dependencies. The platforms list for the LTSB is fixed for
the life of the release:

Windows:

      Only quality and security updates for Windows are supported.
      No support is added for current branches (CB), current branches for business
      (CBB), or LTSB of Windows 10.
      No support for new major versions of Windows Server.

SQL Server:

<!-- p.169 -->

     Only quality and security updates, or minor upgrades like service packs, is
     supported for SQL Server.
     No support for new major versions of SQL Server.

Site systems and servers
The LTSB supports the use of the following Windows computer operating systems as site
systems. Each operating system has the same requirements and limitations as the same
entry in Supported operating systems for site system servers. For example, the Server
Core installation of Windows 2012 R2 must be an x64 version, is only supported to host
a distribution point, and does not support PXE or Multicast.

Supported operating systems:

     Windows Server 2016
     Windows Server 2012 R2 (x64): Standard, Datacenter
     Windows Server 2012 (x64): Standard, Datacenter
     Windows 10 Enterprise 2015 LTSB (x86, x64)
     Windows 10 Enterprise 2016 LTSB (x86, x64)
     Windows 8.1 (x86, x64): Professional, Enterprise
     The Server Core installation of Windows Server 2012
     The Server Core installation of Windows Server 2012 R2

Client management
The following sections identify the client operating systems that you can manage with
the LTSB. The LTSB does not support the addition of new operating systems as
supported clients.

Windows computers
You can use the LTSB to manage the following Windows computer operating systems
with the Configuration Manager client software that is included with Configuration
Manager. For more information, see How to deploy clients to Windows computers.

Supported operating systems:

     Windows Server 2016
     Windows Server 2012 R2 (x64): Standard, Datacenter (Note 1)
     Windows Server 2012 (x64): Standard, Datacenter (Note 1)
     Windows Storage Server 2012 R2 (x64)

<!-- p.170 -->

     Windows Storage Server 2012 (x64)
     Windows 10 Enterprise 2015 LTSB (x86, x64)
     Windows 10 Enterprise 2016 LTSB (x86, x64)
     Windows 8.1 (x86, x64): Professional, Enterprise
     The Server Core installation of Windows Server 2012 R2 (x64) (Note 2)
     The Server Core installation of Windows Server 2012 (x64) (Note 2)

(Note 1) Datacenter releases are supported but not certified for Configuration Manager.
(Note 2) To support client push installation, the computer that runs this operating
system version must run the File Server role service for the File and Storage Services
server role. For information about installing Windows features on a Server Core
computer, see Install Server Roles and Features on a Server Core Server.

Windows Embedded
You can use the LTSB to manage the following Windows Embedded devices by installing
the client software on the device. For more information, see Planning for client
deployment to Windows Embedded devices.

Requirements and limitations:

     All client features are supported on supported Windows Embedded systems that
     do not have write filters enabled.

     Clients that use one of the following are supported for all features except power
     management:

        Enhanced Write Filters (EWF)

        RAM File-Based Write Filters (FBWF)

        Unified Write Filters (UWF)

     Before you can monitor detected malware on Windows Embedded devices based
     on Windows XP, you must install the Microsoft Windows WMI scripting package
     on the embedded device. Use Windows Embedded Target Designer to install this
     package. The WBEMDISP.DLL and WBEMDISP.TLB files must exist and be registered
     in the %windir%\System32\WBEM folder on the embedded device to ensure that
     detected malware is reported.

Supported operating systems:

     Windows 10 Enterprise 2016 LTSB (x86, x64)
     Windows 10 Enterprise 2015 LTSB (x86, x64)

<!-- p.171 -->

       Windows Embedded 8.1 Industry (x86, x64)

Exchange Server connector
The LTSB supports limited management of devices that connect to your Exchange Server
instance, without installing client software. For more information, see Manage mobile
devices with Configuration Manager and Exchange.

Requirements and limitations:

       Configuration Manager offers limited management for mobile devices. Limited
       management is available when you use the Exchange Server connector for
       Exchange Active Sync (EAS) capable devices that connect to a server running
       Exchange Server or Exchange Online.

       For more information about the management functions that Configuration
       Manager supports for mobile devices that the Exchange Server connector
       manages, see Choose a device management solution for Configuration Manager.

Supported versions of Exchange Server:

       Exchange Server 2010 SP1
       Exchange Server 2010 SP2
       Exchange Server 2013

  ７ Note

  The LTSB does not support the management of devices that connect through an
  online service, like Exchange Online (Microsoft 365).

Configuration Manager console
The LTSB supports the following operating systems to run the Configuration Manager
console. Each computer that hosts the console must have a minimum .NET Framework
version of 4.5.2 except for Windows 10, which requires a minimum of .NET Framework
4.6.

Supported operating systems:

       Windows Server 2016
       Windows Server 2012 R2 (x64): Standard, Datacenter
       Windows Server 2012 (x64): Standard, Datacenter

<!-- p.172 -->

     Windows 10 Enterprise 2016 LTSB (x86, x64)
     Windows 10 Enterprise 2015 LTSB (x86, x64)
     Windows 8.1 (x86, x64): Professional, Enterprise

SQL Server versions supported for the site
database and reporting point
The LTSB supports the following versions of SQL Server to host the site database and
reporting point. For each supported version, the same configuration requirements and
limitations that appear in Support for SQL Server versions for the current branch apply
to the LTSB. This support includes the use of a SQL Server Always On failover cluster
instance or an availability group.

Supported versions:

     SQL Server 2016: Standard, Enterprise
     SQL Server 2014 SP2: Standard, Enterprise
     SQL Server 2014 SP1: Standard, Enterprise
     SQL Server 2012 SP3: Standard, Enterprise
     SQL Server 2008 R2 SP3: Standard, Enterprise, Datacenter
     SQL Server 2016 Express
     SQL Server 2014 Express SP2
     SQL Server 2014 Express SP1
     SQL Server 2012 Express SP3

Support for Active Directory domains
All LTSB site systems must be members of a supported Windows Active Directory
domain. Support for Active Directory domains has the same requirements and
limitations as those that appear in Support for Active Directory domains, but is limited
to the following domain functional levels:

Supported levels:

     Windows Server 2008
     Windows Server 2008 R2
     Windows Server 2012
     Windows Server 2012 R2

<!-- p.173 -->

Additional support topics that apply to the
Long-Term Servicing Branch
The information in the following Current Branch topics apply to the LTSB:

     Size and scale numbers
     Site and site system prerequisites
     High availability options
     Recommended hardware
     Support for Windows features and networks
     Support for virtualization environments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.174 -->

Install and upgrade with the version
1606 baseline media
Article • 10/04/2022

Applies to: System Center Configuration Manager (long-term servicing branch)

When you run setup from the version 1606 baseline media for Configuration Manager,
you can install a long-term servicing branch site of System Center Configuration
Manager.

The baseline media is available on DVD as part of Microsoft System Center 2016, or
from the System Center Configuration Manager long-term servicing branch version
1606. To learn about baseline media, see Baseline and update versions.

When you use the version 1606 baseline media, the site you install or upgrade to is:

      A Current Branch site that is equivalent to a site that was first installed using the
      1511 baseline media, and then updated to version 1606 plus the 1606 hotfix rollup
      - KB3186654.
      An LTSB site that is equivalent to the Current Branch site that runs version 1606
      plus the 1606 hotfix rollup - KB3186654. The baseline media already includes the
      hotfix rollup. But, the LTSB doesn't support all of the features or capabilities
      available with the Current Branch, as detailed in Introduction to the Long-Term
      Servicing Branch of System Center Configuration Manager.

If you aren't familiar with the different branches of Configuration Manager, see Which
branch of Configuration Manager should I use.

Changes to Setup with the 1606 baseline media
The 1606 baseline media introduces the following changes to Setup for Configuration
Manager.

Branch and edition
When you run Setup, you're now presented with a Licensing page where you can select
the branch of Configuration Manager you want to install. You can choose either the
Current Branch or LTSB as a licensed installation, or you can choose an Evaluation
edition of the Current Branch as a non-licensed installation.

For more information, see Licensing and branches for Configuration Manager.

<!-- p.175 -->

Software Assurance expiration
During Setup, you have the option to enter the Software Assurance expiration date
value. This is an optional value that you can specify as a convenient reminder.

  ７ Note

  Microsoft does not validate the expiration date you enter and will not use this date
  for license validation. Instead, you can use it as a reminder of your expiration date.
  This is useful because Configuration Manager periodically checks for new software
  updates offered online, and your software assurance license status should be
  current to be eligible to use these additional updates.

     You can specify the date value on the Product Key page of the Setup Wizard when
     you run Setup from the Configuration Manager version 1606 baseline media.
     You can also specify this date by selecting Hierarchy Settings Properties >
     Licensing in the Configuration Manager console.

For more information, see "Software Assurance agreements" in Licensing and branches
for Configuration Manager.

Additional pre-upgrade configurations
Prior to starting an upgrade of System Center 2012 Configuration Manager to the LTSB,
you must take the following extra steps as part of pre-upgrade checklist.
Uninstall the site system roles that the LTSB doesn't support:

     Asset Intelligence synchronization point
     Microsoft Intune connector
     Cloud-based distribution points

For more information, see Upgrade to Configuration Manager.

New scripted installation options
The version 1606 baseline media supports a new unattended script file key for scripted
installations of a new top-level site. This applies to installing a new stand-alone primary
site or adding a central administration site as part of a site expansion scenario.

When using an unattended script to install a licensed branch, you must add the
following section, key names, and values to the Options section of your script. You don't

<!-- p.176 -->

need to use these values to script the install of an Evaluation edition of the Current
Branch:

SABranchOptions

     Key Name: SAActive
          Values: 0 or 1.
          Details: 0 installs a non-licensed Evaluation edition of Current Branch, and 1
          installs a licensed edition.

     CurrentBranch
          Values: 0 or 1.
          Details: 0 installs the Long-Term Servicing Branch, and 1 installs the Current
          Branch.

For example, to install a licensed Current Branch edition you would use:

Key Name: SABranchOptions

     SAActive = 1
     CurrentBranch = 1

  ） Important

  SABranchOptions only works with Setup from the baseline media. It does not apply
  when you run Setup from the CD.Latest folder of a site you previously installed
  using the version 1606 baseline media.

  SABranchOptions does not apply to scripted upgrades from System Center 2012
  Configuration Manager and always results in the Current Branch.

For more information, see Use a command line to install Configuration Manager sites.

Install a new site
When you use the 1606 baseline media to install a new site of either branch, use the site
planning, preparation, and installation procedures documented in the Installing
Configuration Manager sites topic with the addition of the following considerations for
Setup:

     During Setup you must choose the branch of Configuration Manager that you
     want to install, and you can specify details for your Software Assurance agreement.

<!-- p.177 -->

     All sites in the same hierarchy must run the same branch. It isn't supported to have
     a hierarchy with a mix of LTSB and Current Branch at different sites.
     New scripted installation. For more information, see "New scripted installation
     options" earlier in this article.

Expand a stand-alone primary site
You can expand a stand-alone primary site that runs the LTSB. The process is no
different than that used for a Current Branch site with one caveat:

     When installing the new central administration site, you must use Setup from the
     original source media you used to install the LTSB site. Running Setup from the
     CD.Latest folder for this scenario isn't supported.

For more information about expanding a site, see "Expand a stand-alone primary site" in
Install a site using the Setup Wizard.

Upgrade from System Center 2012
Configuration Manager
When you upgrade from System Center 2012 Configuration Manager, use the site
planning, preparation, and procedures as documented in the Upgrade to Configuration
Manager topic, but with the following changes:

Upgrade to the Current Branch:

     During Setup, you must choose the Current Branch, and you can specify details for
     your Software Assurance agreement.
     New scripted installation. For more information, see "New scripted installation
     options" earlier in this article.

Upgrade to the LTSB:

     Additional steps to following in the pre-upgrade checklist.
     During Setup you must choose the LTSB, and you can specify details for your
     Software Assurance agreement.
     You can only upgrade a site that runs System Center 2012 Configuration Manager
     with Service Pack 1, System Center 2012 Configuration Manager with Service Pack
     2, System Center 2012 R2 Configuration Manager with Service Pack 1, or System
     Center 2012 R2 Configuration Manager with no service pack.

<!-- p.178 -->

In-place upgrade paths for the 1606 baseline media
You can use the 1606 baseline media to upgrade the following to a licensed edition of
Configuration Manager:

     System Center 2012 R2 Configuration Manager with Service Pack 1
     System Center 2012 R2 Configuration Manager with no service pack (this requires
     the use of the baseline media for version 1606 that was rereleased on December
     15, 2016.)
     System Center 2012 Configuration Manager with Service Pack 2
     System Center 2012 Configuration Manager with Service Pack 1 (this requires the
     use of the baseline media for version 1606 that was rereleased on December 15,
     2016.)

You can also use this media to upgrade a non-licensed Evaluation edition of Current
Branch to a fully licensed version of the Current Branch.

This media doesn't support the upgrade of:

     Other versions of System Center 2012 Configuration Manager.
     Configuration Manager 2007 or earlier.
     A release candidate installation of Configuration Manager.

About the CD.Latest folder and the LTSB
The following are limitations on using the media that Configuration Manager creates in
the CD.Latest folder on the site server. These limits apply to sites that run the LTSB:

Media in the CD.Latest folder is supported for:

     Site recovery.
     Site maintenance.
     Installing other child primary sites.

Media in the CD.Latest folder isn't supported for:

     Installing a central administration site as part of a site expansion scenario.

For more information, see the CD.Latest folder.

Backup, recovery, and site maintenance for the
LTSB

<!-- p.179 -->

To back up, recover, or run site maintenance on a site that runs the LTSB, use the
guidance and procedures from Backup and recovery for Configuration Manager.

Use Configuration Manager Setup from the CD.Latest folder of the backup of your LTSB
site.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.180 -->

Manage the long term servicing branch
of Configuration Manager
Article • 10/04/2022

Applies to: System Center Configuration Manager (long term servicing branch)

When you use the long term servicing branch (LTSB) of Configuration Manager, there
are important changes that affect how you manage your infrastructure.

The LTSB is generally the same as current branch version 1606, with some exceptions
like cloud-attached features. Most tasks you use for planning, deployment,
configuration, and day-to-day management are the same.

For example, the LTSB supports the same number of sites, site types, clients, and general
infrastructure as the current branch. Use the same guidance for site and hierarchy
planning and design as the current branch. Some features are supported by both
branches, like software updates or OS deployment. Use the same guidance as the
current branch, with the understanding that there were feature changes since version
1606 of the current branch.

The following sections provide information about tasks that aren't similar between the
long term servicing branch and the current branch.

Updates and servicing
Only critical security updates are made available as in-console updates in the LTSB.

Regular updates for the current branch are visible in the console, but aren't made
available to the LTSB. They aren't downloaded and can't be installed.

To support in-console updates for critical security fixes, an LTSB site requires the use of
the service connection point. You can configure this site system role in offline or online
mode, the same as for the current branch. The LTSB collects and submits the same
diagnostic and usage data as the current branch.

The LTSB supports the use of the hotfix installer and the update registration tool, as
documented for the current branch.

For general information about updates and servicing, see Updates for Configuration
Manager.

<!-- p.181 -->

Changes for site expansion and the CD.Latest
folder
When you use the LTSB, and expand a stand-alone primary site with a new central
administration site (CAS), run setup and the source files from the version 1606 baseline
media. For the current branch, you run setup and use source files from the CD.Latest
folder.

Although you don't run setup for site expansion from the CD.Latest folder, continue to
use the CD.Latest folder for the following actions:

     Site recovery
     Install a new child primary site when your first LTSB site was a CAS

For more information about site expansion, see Expand a stand-alone primary site. For
more information about the CD.Latest folder, see The CD.Latest folder.

Recovery
When you recover a site, you must restore the site or site database to its original branch.
You can't recover a current branch site database to an LTSB installation, or an LTSB site
to a current branch installation.

Next steps
Upgrade the long-term servicing branch to the current branch

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.182 -->

Upgrade the long-term servicing branch
to the current branch
Article • 10/04/2022

Applies to: System Center Configuration Manager (Long-Term Servicing Branch)

Use this topic to learn how to upgrade (convert) a site and hierarchy that runs the Long-
Term Servicing Branch (LTSB) of Configuration Manager to the Current Branch.

When you have a current Software Assurance agreement (or similar licensing rights) that
grants you rights to use the Current Branch, you can convert your installation from the
LTSB to the Current Branch. This is a one-way conversion because there is no support for
converting a Current Branch site to the LTSB.

If you have multiple sites, you only need to convert the top-tier site of your hierarchy.
After the top-tier site is converted:

      Child primary sites automatically convert.
      You must manually update secondary sites from within the Configuration Manager
      console.

Run setup to convert the Long-Term Servicing
Branch
On the top-tier site of your hierarchy, you can run Configuration Manager setup from
qualifying baseline media and select Site maintenance. Then, when presented with the
licensing page, select the option for the Current Branch and complete the wizard.

When your site has converted to the Current Branch, previously unavailable features and
capabilities will be available for use.

  ７ Note

  Qualifying baseline media is a media that has a version that is equal to or later than
  your LTSB installation.

For example, because the LTSB is based on version 1606, you cannot use the baseline
1511 media to convert to the Current Branch. Instead, you run setup from the same
version 1606 baseline media that you used to install the LTSB site, and choose the

<!-- p.183 -->

licensing option for the Current Branch. Alternately, if a later baseline of the Current
Branch has been released, you can run setup from that baseline media.

For a list of baseline versions, see Baseline and update versions in Updates for
Configuration Manager.

Use the Configuration Manager console to
convert the long-term servicing branch
If your site runs the LTSB, you can use the following option in the Configuration
Manager console to convert to the Current Branch:

   1. In the console, go to Administration > Site Configuration > Sites, and then open
     Hierarchy Settings.

   2. In Hierarchy Settings, switch to the Licensing tab. Select the option to Convert to
     Current Branch, and then choose Apply.

When your site has converted to the Current Branch, previously unavailable features and
capabilities will be available for use.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.184 -->

Get ready for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the information in the following topics when you're ready to start planning your
Configuration Manager deployment:

      Design a hierarchy of sites for Configuration Manager

      Fundamentals of role-based administration for Configuration Manager

      Fundamental concepts for content management

      Understand how clients find site resources and services for Configuration Manager

      Prepare your network environment for Configuration Manager

      Supported configurations for Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.185 -->

Features and capabilities of
Configuration Manager
Article • 07/17/2024

Applies to: Configuration Manager (current branch)

This article summarizes the primary management features of Configuration Manager.
Each feature has its own prerequisites, and how you use each might influence the design
and implementation of your Configuration Manager hierarchy. For example, if you want
to deploy software updates to devices in your hierarchy, you need a software update
point site system role.

Co-management
Co-management is one of the primary ways to attach your existing Configuration
Manager deployment to the Microsoft 365 cloud. It enables you to concurrently manage
Windows devices by using both Configuration Manager and Microsoft Intune. Co-
management lets you cloud-attach your existing investment in Configuration Manager
by adding new functionality like conditional access. For more information, see What is
co-management?

Cloud-attached management
Use features like the cloud management gateway and Microsoft Entra ID to manage
internet-based clients.

For more information, see the following articles:

      Cloud management gateway overview
      Plan for Microsoft Entra ID
      Azure services

Real-time management
Use CMPivot to immediately query online devices, then filter and group the data for
deeper insights. Also use the Configuration Manager console to manage and deploy
Windows PowerShell scripts to clients. For more information, see CMPivot and Create
and run PowerShell scripts.

<!-- p.186 -->

Application management
Helps you create, manage, deploy, and monitor applications to a range of different
devices that you manage. Deploy, update, and manage Microsoft 365 Apps from the
Configuration Manager console. Additionally, Configuration Manager integrates with
the Microsoft Store for Business and Education to deliver cloud-based apps. For more
information, see Introduction to application management.

OS deployment
Deploy an in-place upgrade of Windows, or capture and deploy OS images. Image
deployment can use PXE, multicast, or bootable media. It can also help redeploy existing
devices using Windows Autopilot. For more information, see Introduction to OS
deployment.

Software updates
Manage, deploy, and monitor software updates in the organization. Integrate with
Windows Delivery Optimization and other peer caching technologies to help control
network usage. For more information, see Introduction to software updates.

Company resource access
Lets you give users in your organization access to data and applications from remote
locations. This feature includes Wi-Fi, VPN, email, and certificate profiles. For more
information, see Protect data and site infrastructure.

Compliance settings
Helps you to assess, track, and remediate the configuration compliance of client devices
in the organization. Additionally, you can use compliance settings to configure a range
of features and security settings on devices you manage. For more information, see
Ensure device compliance.

Endpoint Protection
Provides security, antimalware, and Windows Firewall management for computers in
your organization. This area includes management and integration with the following
Windows Defender suite features:

<!-- p.187 -->

     Windows Defender Antivirus
     Microsoft Defender for Endpoint
     Windows Defender Exploit Guard
     Windows Defender Application Guard
     Windows Defender Application Control
     Windows Defender Firewall

For more information, see Endpoint Protection.

Inventory
Helps you identify and monitor assets.

Hardware inventory
Collects detailed information about the hardware of devices in your organization. For
more information, see Introduction to hardware inventory.

Software inventory
Collects and reports information about the files that are stored on client computers in
your organization. For more information, see Introduction to software inventory.

Asset Intelligence
Provides tools to collect inventory data and monitor software license usage in your
organization. For more information, see Introduction to Asset Intelligence.

On-premises mobile device management
Enrolls and manages devices by using the on-premises Configuration Manager
infrastructure with the management functionality built into the device platforms. (Typical
management uses a separately installed Configuration Manager client.) This feature
currently supports managing Windows 10 Enterprise and Windows 10 Mobile devices.
For more information, see Manage mobile devices with on-premises infrastructure.

Power management
Manage and monitor the power consumption of client computers in the organization.
Configure power plans, and use Wake-on-LAN to do maintenance outside of business

<!-- p.188 -->

hours. For more information, see Introduction to power management.

Remote control
Provides tools to remotely administer client computers from the Configuration Manager
console. For more information, see Introduction to remote control.

Reporting
Use the advanced reporting capabilities of SQL Server Reporting Services from the
Configuration Manager console. This feature provides hundreds of default reports. For
more information, see Introduction to reporting.

Software metering
Monitor and collect software usage data from Configuration Manager clients. You can
use this data to determine whether software is used after it's installed. For more
information, see Monitor app usage with software metering.

Next steps
For more information about how to plan and install Configuration Manager to support
these management capabilities in your environment, see Get ready for Configuration
Manager.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.189 -->

What's new in Configuration Manager
incremental versions
Applies to: Configuration Manager (current branch)

Configuration Manager uses an in-console updates and servicing process. This update process
makes it easy to discover and install Configuration Manager updates. There are no more
service packs or cumulative update versions to track and install. You don't have to search for
the download of the most recent release or updates.

To update the product to a new version of the current branch, use the Configuration Manager
console install then. A few times each year, Microsoft releases new versions that include
product updates. Each version also introduces new features. When you install an update with
new features, you can choose to use those features. For more information, see Prepare to
install in-console updates for Configuration Manager.

Different update versions are identified by year and month. For example, version 1511
identifies November 2015 (the month when Configuration Manager current branch was first
released to manufacturing). Later updates have version names like 2107, which indicates an
update that was created in July 2021. These update versions are key to understanding the
incremental version of your Configuration Manager installation, and what features are available
to enable in your environment.

Supported versions
Refer to the Supported versions section of the Updates and Servicing page for the latest version
information.

Each update version remains in support for 18 months from its initial availability date. Stay
current with the most recent update version. For more information, see Support for
Configuration Manager current branch versions.

See also
Release notes

 Last updated on 12/08/2025

<!-- p.190 -->

What's new in version 2603 of Configuration
Manager current branch
Applies to: Configuration Manager (current branch)

Update 2603 for Configuration Manager current branch is available as an in-console update.
Apply this update on sites that run version 2409 or later.

Always review the latest checklist for installing this update. For more information, see Checklist
for installing update 2603. After you update a site, also review the Post-update checklist.

To take full advantage of new Configuration Manager changes, after you update the site, also
update clients to the latest version. New functionality appears in the Configuration Manager
console when you update the site and console, but the complete scenario isn't functional until
the client version is also the latest.

General enhancements
As part of Microsoft's Secure Future Initiative (SFI) the 2603 version of Configuration Manager
continues to focus on security, quality, and infrastructure modernization. For more information,
see the Microsoft Trust Center     . For a list of significant customer-reported issues resolved in this
release, see the Summary of changes in Configuration Manager version 2603 knowledge base
article.

Security improvements for Network Access Account
This update enhances security by improving access controls for the Network Access Account
(NAA). Access to NAA information is now restricted to supported OSD media task sequence
scenarios by enforcing additional permission requirements and removing legacy access paths to
reduce exposure and align with least privilege principles. For more information, see KB 37447175.

Weak ciphers disabled on Cloud Management Gateway
Weak DHE (Diffie-Hellman Ephemeral) cipher suites are now disabled on Cloud Management
Gateway (CMG) instances. Only TLS 1.3 (AES_256_GCM, AES_128_GCM) and TLS 1.2 ECDHE
ciphers remain enabled, improving the security posture of CMG connections.

<!-- p.191 -->

Additionally, the EnableCertPaddingCheck registry keys are now set by default on CMG Virtual
Machine Scale Set instances to mitigate CVE-2013-3900 (WinVerifyTrust Signature Validation
Vulnerability).

SQL Server 2025 support
SQL Server 2025 (RTM) is now a supported database platform for Configuration Manager sites,
including the central administration site, primary sites, and secondary sites. SQL Server 2025
Express is also supported for secondary sites. The recommended database compatibility level for
SQL Server 2025 is 160. For more information, see Support for SQL Server versions.

SQL Server Native Client dependency removed
All Configuration Manager components and site roles are updated to remove the dependency on
the deprecated SQL Server Native Client (sqlncli.msi). Customers can now safely uninstall sqlncli
from site systems. The product no longer includes sqlncli.msi in its redistributables.

SQL Server Management Objects updated
The Microsoft SQL Server Management Objects and Microsoft System CLR Types for SQL Server
are updated from the deprecated SQL Server 2014 versions to the SQL Server 2025 versions
(SMO 17).

PKI certificate support for site system-to-SQL
Server communication
Added support and testing for PKI certificates used in site system-to-SQL Server communication.
This includes proper handling of certificate trust, private key access, and BitLocker Management
portal registry thumbprint configuration.

ARM64 support improvements
     The Import-CMDriver PowerShell cmdlet now correctly includes ARM64 platform support
     when importing drivers from INF files. Previously, ARM64 was filtered out from the
     Supported Platforms list.
     Client push installation (CcmSetup) no longer fails with error code 0x80070643 on Windows
     11 ARM64 devices when upgrading from ConfigMgr 2409 or 2503.

Cloud Management Gateway improvements

<!-- p.192 -->

     The New-CMCloudManagementGateway PowerShell cmdlet now allows combining the -
     IsUsingExistingGroup $true parameter with -ServerAppClientId , enabling automated CMG

     deployment into existing Azure resource groups without requiring interactive credentials.
     CMG deployment error handling is improved to capture and display detailed Azure error
     response information when Attribute-Based Access Control (ABAC) conditions block role
     assignments.
     The CMG outbound traffic alert and "Total Outbound data" metric now work correctly for
     CMGv2 (Azure Virtual Machine Scale Sets-based) deployments.

Updated Feedback experience
The Configuration Manager console In-App Feedback feature is updated to support the new OCV
Feedback SDK with authenticated submissions. Both authenticated and offline feedback
submission modes are supported.

Deprecated and removed features
     An internal service required for device compliance checks will be deprecated in October
     2026. Following the deprecation, compliance checks in Software Center may fail in co-
     managed environments where the Compliance workload is managed by Intune. To prevent
     this issue, apply this update before October 2026.
     The deprecated Asset Intelligence synchronization point site role is removed from the site
     roles selection UI.
     The Software Update Health Troubleshooting Dashboard is hidden in this release due to
     performance issues in large environments.

New requirements
Management point requires internet access for Microsoft Entra
token validation
Starting in version 2603, the management point uses Microsoft Identity Service Essentials (MISE)
for Microsoft Entra token validation. This change requires the management point server to have
internet access. In previous versions, the management point could function without internet
access.

This requirement applies to environments that meet the following conditions:

     The site is configured to support Microsoft Entra joined users and devices

<!-- p.193 -->

        Clients authenticate using Microsoft Entra tokens, typically through a cloud management
        gateway (CMG)

  ７ Note

  Environments that only use on-premises Active Directory authentication without Microsoft
  Entra integration aren't affected by this requirement.

Identify the issue

If the management point server can't reach the required endpoints, the CCM_STS_ManagedBase.log
on the management point logs a MiseAuthenticationTicketProviderException with an underlying
network error. Look for the SocketException or HttpRequestException that indicates a network
connectivity failure, for example:

 text

 Microsoft.Identity.ServiceEssentials.Exceptions.MiseAuthenticationTicketProviderExcept
 ion: MISE12034: AuthenticationTicketProvider Name:AuthenticationTicketProvider
 System.Net.Sockets.SocketException: No connection could be made because the target
 machine actively refused it

  ） Important

  The MISE12034 exception can also appear for other reasons. This section specifically
  addresses the case where the underlying exception indicates a network connectivity
  problem, such as SocketException , HttpRequestException , or a connection timeout. Verify
  that the error message points to a network access issue before applying the resolution
  below.

Resolution: Allow access to Azure authentication endpoints

Ensure that the management point server can connect to Microsoft Entra authentication
endpoints in the system context. Allow the following URLs through the proxy and firewall:

        https://login.microsoftonline.com

        https://sts.windows.net

If the management point server uses a proxy, configure the proxy at the system level. For more
information, see Management point proxy configuration.

<!-- p.194 -->

For a full list of required endpoints, see Management point internet access requirements.

Next steps
As of May 27, 2026, version 2603 is globally available for all customers to install.

When you're ready to install this version, see Installing updates for Configuration Manager and
Checklist for installing update 2603.

   Tip

  To install a new site, use a baseline version of Configuration Manager.

  Learn more about:

         Installing new sites
         Baseline and update versions

For known significant issues, see the Release notes.

After you update a site, also review the Post-update checklist.

 Last updated on 06/12/2026

<!-- p.195 -->

What's new in version 2509 of
Configuration Manager current branch
Applies to: Configuration Manager (current branch)

Update 2509 for Configuration Manager current branch is available as an in-console update.
Apply this update on sites that run version 2403 or later.

Always review the latest checklist for installing this update. For more information, see Checklist
for installing update 2509. After you update a site, also review the Post-update checklist.

To take full advantage of new Configuration Manager changes, after you update the site, also
update clients to the latest version. New functionality appears in the Configuration Manager
console when you update the site and console, but the complete scenario isn't functional until
the client version is also the latest.

General enhancements
As part of Microsoft's Secure Future Initiative (SFI) the 2509 version of Configuration Manager
focuses on security and quality updates. For more information, see the Microsoft Trust
Center   . For a list of significant customer-reported issues resolved in this release, see the
Summary of changes in Configuration Manager version 2509 knowledge base article.

Windows 11 25H2 support
Windows 11, version 25H2 is supported for OS deployment and in-place upgrade scenarios.
For more information about Windows 11 25H2, see the Windows 11 release information.

Boot images can be automatically updated to use latest
Windows Boot Loader
A new checkbox, Use Windows Boot Loader signed with Windows UEFI CA 2023, is available in
the Data Source tab of boot image properties. When enabled, it updates the boot image to use
the boot loader signed with Windows UEFI CA 2023. The checkbox automates the mitigation
steps described in KB5025885       .

The new functionality only works on WDS-Less PXE-enabled Distribution Points.

WinPE is now boundary‑aware

<!-- p.196 -->

Starting in Configuration Manager 2509, Windows PE–based OSD scenarios now require
Boundary Group Management Point (MP) assignments.

     For a successful OSD deployment, the Boundary Group that the WinPE client belongs to
     must contain at least one Management Point.

     If no MP is associated with the client’s Boundary Group, WinPE will fail to retrieve policy.
     The smsts.log will show errors similar to the following:

        Failed to query Management Point locator Exiting TSMediaWizardControl :: GetPolicy.
        QueryMPLocator: no valid MP locations are received

Service Connection Tool improvements
The Service Connection Tool (SCT) is improved to provide better logging and error handling,
specifically in the following areas:

     More detailed information about the actions it performs is recorded in both the console
     and log file. Error and warning messages in the console are highlighted with colors for
     better visibility.
     The SCT explicitly checks for prerequisites and fails if they're not met.
     Customers are directed to explore the relevant logs, such as ServiceConnectionTool.log
     and ConfigMgrSetup.log, when there's an error.
     If there's a download failure, the SCT "Connect" step stops execution thus preventing
     importing incomplete Update Package payloads.

AdminService now rejects NTLM authentication
     AdminService now rejects NTLM authentication attempts. AdminService.log should write
     the below message when NTLM authentication is attempted:

  Rejecting NTLM authentication.

Known Issues
     Upgrade SQL 2012 or 2014 Express, Standard, Enterprise edition to SQL 2016 or latest
     version. VC++ Redistributable Version needs to be upgraded to latest version on
     Secondary sites. Download Latest Microsoft Visual C++ Redistributable Version        .

Microsoft ODBC redistributable

<!-- p.197 -->

      The Microsoft ODBC redistributable component is updated to version 18.4.1.1 on all Site
      servers and Management Points.

      ConfigMgrPreReq throws an error stalling the upgrade if it detects a version lower than
      18.4.4.1.

         INFO: Microsoft ODBC Driver 18 for SQL Server is installed but it is older than the
         required version.
         SQL client prerequisite missing for Configuration Manager setup.; Error; Install the
         Microsoft ODBC driver 18 for SQL setup from https://go.microsoft.com/fwlink/?
         linkid=2299909       . More information https://go.microsoft.com/fwlink/?
         linkid=2226618

Next steps
As of December 8, 2025, version 2509 is globally available for all customers to install.

When you're ready to install this version, see Installing updates for Configuration Manager and
Checklist for installing update 2509.

   Tip

  To install a new site, use a baseline version of Configuration Manager.

  Learn more about:

         Installing new sites
         Baseline and update versions

For known significant issues, see the Release notes.

After you update a site, also review the Post-update checklist.

 Last updated on 01/14/2026

<!-- p.198 -->

What's new in version 2503 of
Configuration Manager current branch
06/12/2025

Applies to: Configuration Manager (current branch)

Update 2503 for Configuration Manager current branch is available as an in-console update.
Apply this update on sites that run version 2309 or later.

Always review the latest checklist for installing this update. For more information, see Checklist
for installing update 2503. After you update a site, also review the Post-update checklist.

To take full advantage of new Configuration Manager changes, after you update the site, also
update clients to the latest version. New functionality appears in the Configuration Manager
console when you update the site and console, but the complete scenario isn't functional until
the client version is also the latest.

General enhancements
As part of Microsoft's Secure Future Initiative (SFI) the 2503 version of Configuration Manager
focuses on security and quality updates. For more information, see the Microsoft Trust
Center    . For a list of significant customer-reported issues resolved in this release, see the
Summary of changes in Configuration Manager version 2503 knowledge base article.

Known Issues
     Upgrade SQL 2012 or 2014 Express, Standard, Enterprise edition to SQL 2016 or latest
     version. VC++ Redistributable Version needs to be upgraded to latest version on
     Secondary sites. Download Latest Microsoft Visual C++ Redistributable Version           .

Microsoft ODBC redistributable
     The Microsoft ODBC redistributable component is updated to version 18.4.1.1 on all Site
     servers and Management Points.

     ConfigMgrPreReq will throw an error stalling the upgrade if it detects a version lower
     than that.

         INFO: Microsoft ODBC Driver 18 for SQL Server is installed but it is older than the
         required version.

<!-- p.199 -->

        SQL client prerequisite missing for Configuration Manager setup.; Error; Install the
        Microsoft ODBC driver 18 for SQL setup from https://go.microsoft.com/fwlink/?
        linkid=2299909     . More information https://go.microsoft.com/fwlink/?
        linkid=2226618

Next steps
As of April 23, 2025, version 2503 is globally available for all customers to install.

When you're ready to install this version, see Installing updates for Configuration Manager and
Checklist for installing update 2503.

   Tip

  To install a new site, use a baseline version of Configuration Manager.

  Learn more about:

        Installing new sites
        Baseline and update versions

For known significant issues, see the Release notes.

After you update a site, also review the Post-update checklist.

<!-- p.200 -->

What's new in version 2409 of
Configuration Manager current branch
ﾃ    Summarize this article for me

Applies to: Configuration Manager (current branch)

Update 2409 for Configuration Manager current branch is available as an in-console update.
Apply this update on sites that run version 2309 or later. This article summarizes the changes
and new features in Configuration Manager, version 2409.

Always review the latest checklist for installing this update. For more information, see Checklist
for installing update 2409. After you update a site, also review the Post-update checklist.

To take full advantage of new Configuration Manager features, after you update the site, also
update clients to the latest version. While new functionality appears in the Configuration
Manager console when you update the site and console, the complete scenario isn't functional
until the client version is also the latest.

Site infrastructure

Configuration Manager now supports SQL Extended
Protection for Authentication
Configuration Manager now supports SQL extended protection for authentication. It's a
security feature that enhances protection against MITM attacks, making SQL server more
secure when connections are made using extended protection. These enhancements
collectively reduce the risk of unauthorized access and protect sensitive data managed by the
SQL Server database engine.

For more information, see Connect to the Database Engine Using Extended Protection.

Introducing Centralized Search - Desired Workspace Selection
The centralized search box now enables the option to select the desired workspace for
searching. Users can easily refine their search results by selecting the desired workspace from
the dropdown menu.
