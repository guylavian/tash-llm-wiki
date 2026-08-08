---
title: "Software update management documentation — pages 41-80"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0041-0080
family: sccm
documentKind: "doc"
abstract: "the Windows Server 2012 product. If a software update applies to Windows Server 2012 and Windows Server 2012 Datacenter Edition, both products are in the site database. Configure the product settings only on the top-level site. The product settings aren't configured on the softw"
---

# Software update management documentation — pages 41-80

<!-- p.41 -->

the Windows Server 2012 product. If a software update applies to Windows Server 2012
and Windows Server 2012 Datacenter Edition, both products are in the site database.

Configure the product settings only on the top-level site. The product settings aren't
configured on the software update point for child sites because the software updates
metadata is replicated from the top-level site. The more products that you select, the
longer it takes to synchronize the software updates metadata.

  ） Important

  Configuration Manager stores a list of products and product families that you
  choose from when you first install the software update point. Products and product
  families that are released after Configuration Manager is released might not be
  available to select until you complete synchronization. The synchronization process
  updates the list of available products and product families from which you can
  choose. Clear all products before you synchronize software updates for the first
  time. After the initial synchronization, select the desired products, and then rerun
  synchronization.

Supersedence rules
Typically, a software update that supersedes another software update does one or more
of the following actions:

     Enhances, improves, or updates the fix that was provided by one or more
     previously released updates.

     Improves the efficiency of the superseded update file package, which is installed
     on clients if the update is approved for installation. For example, the superseded
     update might contain files that are no longer relevant to the fix or to the operating
     systems that are supported by the new update. Those files aren't included in the
     superseding file package of the update.

     Updates newer versions of a product. In other words, it updates versions that are
     no longer applicable to older versions or configurations of a product. Updates can
     also supersede other updates if modifications were made to expand language
     support. For example, a later revision of a product update for Microsoft 365 Apps
     might remove the support for an older OS, but it might add additional support for
     new languages in the initial update release.

In the properties for the software update point, specify that the superseded software
updates are immediately expired. This setting prevents them from being included in new

<!-- p.42 -->

deployments. It also flags the existing deployments to indicate that they contain one or
more expired software updates. Or specify a period of time before the superseded
software updates are expired. This action allows you to continue to deploy them.

Consider the following scenarios in which you might need to deploy a superseded
software update:

     A superseding software update supports only newer versions of an OS. Some of
     your client computers run earlier versions of the OS.

     A superseding software update has more restricted applicability than the software
     update it supersedes. This behavior would make it inappropriate for some clients.

     If a superseding software update wasn't approved for deployment in your
     production environment.

Configuration Manager can automatically expire superseded updates based on a
schedule you choose. You can specify the supersedence rules behavior for feature
updates separately from non-feature updates. The default setting is to wait 3 months
before expiring a superseded update. The 3 month default is to give you time to verify
the update is no longer needed by any of your client computers. It's recommended that
you don't assume that superseded updates should be immediately expired in favor of
the new, superseding update. You can display a list of the software updates that
supersede the software update on the Supersedence Information tab in the software
update properties.

Languages
The language settings for the software update point allow you to configure:

     The languages for which the summary details (software updates metadata) are
     synchronized for software updates
     The software update file languages that are downloaded for software updates

Software update file

Configure languages for the Software update file setting in the properties for the
software update point. This setting provides the default languages that are available
when you download software updates at a site. Modify the languages that are selected
by default each time that the software updates are downloaded or deployed. During the
download process, the software update files for the configured languages are
downloaded to the deployment package source location, if the software update files are
available in the selected language. Next, they're copied to the content library on the site

<!-- p.43 -->

server. Then they're distributed to the distribution points that are configured for the
package.

Configure the software update file language settings with the languages that are most
often used in your environment. For example, clients in your site use mostly English and
Japanese for Windows or applications. There are few other languages that are used at
the site. Select only English and Japanese in the Software Update File column when you
download or deploy the software update. This action allows you to use the default
settings on the Language Selection page of the deployment and download wizards.
This action also prevents unneeded update files from being downloaded. Configure this
setting at each software update point in the Configuration Manager hierarchy.

Summary details
During the synchronization process, the summary details information (software updates
metadata) is updated for software updates in the languages that you specify. The
metadata provides information about the software update, for example:

     Name
     Description
     Products that the update supports
     Update classification
     Article ID
     Download URL
     Applicability rules

Configure the summary details settings only on the top-level site. The summary details
aren't configured on the software update point on child sites because the software
updates metadata is replicated from the central administration site by using file-based
replication. When you select the summary details languages, select only the languages
that you need in your environment. The more languages that you select, the longer it
takes to synchronize the software updates metadata. Configuration Manager displays
the software updates metadata in the locale of the OS in which the Configuration
Manager console runs. If the localized properties for the software updates aren't
available in the locale of this OS, the software updates information displays in English.

  ） Important

  Select all of the summary details languages that you need. When the software
  update point at the top-level site synchronizes with the synchronization source, the
  selected summary details languages determine the software updates metadata that
  it retrieves. If you modify the summary details languages after synchronization ran

<!-- p.44 -->

  at least one time, it retrieves the software updates metadata for the modified
  summary details languages only for new or updated software updates. The
  software updates that have already been synchronized aren't updated with new
  metadata for the modified languages unless there's a change to the software
  update on the synchronization source.

Maximum run time
You can specify the maximum amount of time a software update installation has to
complete. You can specify the maximum run time for the following:

     Maximum run time for Windows feature updates (minutes)
       Feature updates - An update that is in one of these three classifications:
          Upgrades
          Update rollups
          Service packs

     Maximum run time for Office 365 updates and non-feature updates for
     Windows (minutes)
       Non-feature updates - An update that isn't a feature upgrade and whose
       product is listed as one of the following:
          Windows 11
          Windows 10 (all versions)
          Windows Server 2012 R2
          Windows Server 2016
          Windows Server 2019
          Office 365

     Maximum run time for all other software updates outside these categories such
     as third-party updates (minutes): The default maximum run time of these updates
     varies depending on when the update first synchronized into the environment and
     the Configuration Manager version. Use the cart below to determine the maximum
     runtime value for these updates:

                                                                         ﾉ   Expand table

      2203 or later                                             2103, 2107, or   2010
                                                                2111

      The maximum run time for all other software updates is    60 minutes       10
      customizable. The default is 60 minutes.                                   minutes

<!-- p.45 -->

        ） Important
           This setting only changes the maximum runtime for new updates that are
           synchronized in by SUP. It doesn't change the run time on existing updates
           that synchronized before the run time was modified. For instance, if Update
           1 was first synchronized into a 2111 environment, then it's maximum run

           time is 60 minutes. You then upgrade the environment to version 2203 and
           set the maximum run time to 30 minutes. Update 1 retains it's 60 minute
           runtime. However, when a new update, Update 2 , synchronizes in, it is
           given the new 30 minute run time.
           If you need to change the maximum run time of an update manually, you
           can configure the software update settings for it.

Plan for a software updates maintenance
window
Add a maintenance window dedicated for software updates installation. This action lets
you configure a general maintenance window and a different maintenance window for
software updates. When you configure both a general maintenance window and
software updates maintenance window, clients install software updates only during the
software updates maintenance window.

You can change this behavior and allow software updates to install during a general
maintenance window. For more information about this client setting, see Software
updates client settings.

For more information about maintenance windows, see How to use maintenance
windows.

Restart options for Windows 10 clients after
software update installation
When a software update that requires a restart is deployed and installed using
Configuration Manager, the client schedules a pending restart and displays a restart
dialog box.

When there's a pending restart for a Configuration Manager software update, the
option to Update and Restart and Update and Shutdown is available on Windows 10

<!-- p.46 -->

computers in the Windows power options. After using one of these options, the restart
dialog doesn't display after the computer restarts. In certain circumstances, the
operating system may remove the pending restart options. This can happen if the Fast
Startup feature in Windows 10 is enabled. For more information, see Updates may not
be installed with Fast Startup in Windows 10 .

Evaluate software updates after a servicing
stack update
Starting in version 2002, Configuration Manager detects if a servicing stack update (SSU)
is part of an installation for multiple updates. When an SSU is detected, it's installed first.
After install of the SSU, a software update evaluation cycle runs to install the remaining
updates. This change allows a dependent cumulative update to be installed after the
servicing stack update. The device doesn't need to restart between installs, and you
don't need to create an additional maintenance window. SSUs are installed first only for
non-user initiated installs. For instance, if a user initiates an installation for multiple
updates from Software Center, the SSU might not be installed first. Installation of SSUs
first isn't available for Windows Server operating systems when using Configuration
Manager version 2002. This functionality was added in Configuration Manager version
2006 for Windows Server operating systems.

If you have non-Windows updates like Office or third-party updates on the same
deadline and they require a restart after installation, cumulative updates might not
install right after the SSU because the computer required a restart before doing a full
scan again. This can be achieved by selecting the If any update in this deployment
requires a system restart, run update deployment evaluation cycle after restart
checkbox in deployment settings.

Next steps
Once you plan for software updates, see Prepare for software updates management.

For more information about managing Windows as a service, see Fundamentals of
Configuration Manager as a service and Windows as a service.

Feedback
Was this page helpful?    Yes      No

<!-- p.47 -->

Provide product feedback

<!-- p.48 -->

Prerequisites for software updates in
Configuration Manager
Article • 06/21/2024

Applies to: Configuration Manager (current branch)

This article lists the prerequisites for software updates in Configuration Manager. For
each of the prerequisites, the external dependencies and internal dependencies are
listed in separate tables.

Software update dependencies that are
external to Configuration Manager
The following sections list the external dependencies for software updates.

Internet Information Services
Internet Information Services (IIS) must be installed on the site system servers to run the
software update point, the management point, and the distribution point. For more
information, see Prerequisites for site system roles.

Windows Server Update Services
Windows Server Update Services (WSUS) is needed for software updates
synchronization and for the software updates applicability scan on clients. The WSUS
server must be installed before you create the software update point role. The following
versions of WSUS are supported for a software update point:

      WSUS 10.0.14393 (role in Windows Server 2016) (2023-02 Cumulative Update, or a
      later cumulative update)
      WSUS 10.0.17763 (role in Windows Server 2019) (Requires Configuration Manager
      1810 or later) (2023-02 Cumulative Update, or a later cumulative update)
      WSUS 10.0.20348 (role in Windows Server 2022) (2023-02 Cumulative Update, or a
      later cumulative update)

  ７ Note

<!-- p.49 -->

        On October 10th, 2023, Windows Server 2012 and Windows Server 2012 R2
        entered the Extended Support Updates phase. Microsoft will no longer
        provide support for Configuration Manager site servers or roles installed to
        these Operating Systems. For more information, see Extended Security
        Updates and Configuration Manager.

        Starting March 28, 2023, on-premises Windows 11, version 22H2 devices will
        receive quality updates via the Unified Update Platform (UUP). The 2023-02
        cumulative update is required for UUP to work. If you're unable to install
        these updates, you can manually add the required MIME types for UUP to
        the WSUS server. If you encounter a Cannot add duplicate collection entry
        of type 'mimeMap' error, see Cannot add duplicate collection entry of type

        mimeMap.

        When you have multiple software update points at a site, ensure that they're
        all running the same version of WSUS.

WSUS Administration Console
The WSUS Administration Console is required on the Configuration Manager site server
when the software update point is on a remote site system server and WSUS isn't
already installed on the site server.

  ） Important

        The WSUS version on the site server must be the same as the WSUS version
        that's running on the software update points.
        Don't use WSUS Administration Console to configure WSUS settings.
        Configuration Manager connects to the instance of WSUS that is running on
        the software update point and configures the appropriate settings.

Windows Update Agent
The Windows Update Agent (WUA) client is required on clients so that they can connect
to the WSUS server. WUA retrieves the list of software updates that must be scanned for
compliance.

<!-- p.50 -->

When you install Configuration Manager, the latest version of WUA is downloaded.
Then, when you install the Configuration Manager client, WUA is upgraded if necessary.
If the installation fails, you must use a different method to upgrade WUA.

Software update dependencies that are internal
to Configuration Manager
The following sections list the internal dependencies for software updates in
Configuration Manager.

Management points
Management points transfer information between client computers and the
Configuration Manager site. The management points are required for software updates.

Software update points
You must install a software update point on the WSUS server to deploy software
updates in Configuration Manager. For more information, see Install and configure a
software update point.

Distribution points
Distribution points are required to store the content for software updates. For more
information about how to install distribution points and manage content, see Manage
content and content infrastructure.

Client settings for software updates
Software updates are enabled for clients by default. There are other available settings
that control how and when clients assess compliance for the software updates and
control how the software updates are installed.

For more information, see the following articles:

     Client settings for software updates

     Software updates client settings

  ） Important

<!-- p.51 -->

  Beginning with the September 2020 cumulative update, HTTP-based WSUS servers
  will be secure by default. A client scanning for updates against an HTTP-based
  WSUS will no longer be allowed to leverage a user proxy by default. If you still
  require a user proxy despite the security trade-offs, a new software updates client
  setting is available to allow these connections. For more information about the
  changes for scanning WSUS, see September 2020 changes to improve security for
  Windows devices scanning WSUS           . To ensure that the best security protocols are
  in place, we highly recommend that you use the TLS/SSL protocol to help secure
  your software update infrastructure.

Reporting services points
The reporting services point site system role can display reports for software updates.
This role is optional but recommended. For more information about how to create a
reporting services point, see Configuring reporting.

Next steps
Prepare for software updates management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.52 -->

Best practices for software updates in
Configuration Manager
Article • 02/11/2025

Applies to: Configuration Manager (current branch)

This article includes best practices for software updates in Configuration Manager. The
information is sorted into best practices for initial installation and for ongoing
operations.

Installation best practices
Use the following best practices when you install software updates in Configuration
Manager.

Use a shared WSUS database for software update points
When you install more than one software update point at a primary site, use the same
WSUS database for each software update point in the same Active Directory forest. If
you share the same database, it significantly mitigates, but doesn't completely eliminate,
the client and the network performance impact that you might experience when clients
switch to a new software update point. A delta scan still occurs when a client switches to
a new software update point that shares a database with the old software update point,
but the scan is much smaller than it would be if the WSUS server has its own database.
For more information about software update point switching, see Software update point
switching.

  ） Important

  Also share the local WSUS content folders when you use a shared WSUS database
  for software update points.

For more information on sharing the WSUS database, see the following blog posts:

      How to implement a shared SUSDB for Configuration Manager software update
      points

      Considerations for multiple WSUS instances sharing a content database when
      using Configuration Manager.

<!-- p.53 -->

When Configuration Manager and WSUS use the same
SQL Server, configure one to use a named instance and
the other to use the default instance
When the Configuration Manager and WSUS databases share the same instance of SQL
Server, you can't easily determine the resource usage between the two applications. Use
different SQL Server instances for Configuration Manager and WSUS. This configuration
makes it easier to troubleshoot and diagnose resource usage issues that might occur for
each application.

Specify the "Store updates locally" setting
When you install WSUS, select the setting to Store updates locally. This setting causes
WSUS to download the license terms that are associated with software updates. It
downloads the terms during the synchronization process and stores them on the local
hard drive for the WSUS server. If you don't select this setting, client computers might
fail compliance scans for software updates that have license terms. The WSUS
Synchronization Manager component of the software update point verifies that this
setting is enabled every 60 minutes, by default.

Configure your software update points to use TLS/SSL
Configuring Windows Server Update Services (WSUS) servers and their corresponding
software update points to use TLS/SSL may reduce the ability of a potential attacker to
remotely compromise a client and elevate privileges. To ensure that the best security
protocols are in place, we highly recommend that you use the TLS/SSL protocol to help
secure your software update infrastructure. For more information, see the Configure a
software update point to use TLS/SSL with a PKI certificate tutorial.

Operational Best Practices
Use the following best practices when you use software updates:

Limit software updates to 1000 in a single software
update deployment
Limit the number of software updates to 1000 in each software update deployment.
When you create an automatic deployment rule, verify that the specified criteria doesn't

<!-- p.54 -->

result in more than 1000 software updates. If you manually deploy software updates,
don't select more than 1000 updates.

Create a new software update group each time an ADR
runs for "Patch Tuesday" and for general deployments
There's a limit of 1000 software updates in a deployment. When you create an
automatic deployment rule (ADR), you specify whether to use an existing update group
or create a new update group each time the rule runs. If you specify criteria in an ADR
that results in multiple software updates, and the rule runs on a recurring schedule,
create a new software update group each time the rule runs. This behavior prevents the
deployment from surpassing the limit of 1000 software updates per deployment.

Use an existing software update group for ADRs for
Endpoint Protection definition updates
When you use an ADR to deploy Endpoint Protection definition updates on a frequent
basis, always use an existing software update group. Otherwise, the ADR potentially
creates hundreds of software update groups over time. Definition update publishers
typically set definition updates to expire when they're superseded by four newer
updates. Therefore, the software update group that's created by the ADR never contains
more than four definition updates for the publisher: one active, and three superseded.

See Also
Plan for software updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.55 -->

Security and privacy for software
updates in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic contains security and privacy information for software updates in
Configuration Manager.

Security best practices for software updates
Use the following security best practices when you deploy software updates to clients:

      Don't change the default permissions on software update packages.

      By default, software update packages are set to allow administrators Full Control
      and users to have Read access. If you change these permissions, it might allow an
      attacker to add, remove, or delete software updates.

      Control access to the download location for software updates.

      The computer accounts for the SMS Provider, the site server, and the
      administrative user who will actually download the software updates to the
      download location require Write access to the download location. Restrict access
      to the download location to reduce the risk of attackers tampering with the
      software updates source files in the download location.

      In addition, if you use a UNC share for the download location, secure the network
      channel by using IPsec or SMB signing to prevent tampering of the software
      updates source files when they're transferred over the network.

      Use UTC for evaluating deployment times.

      If you use local time instead of UTC, users could potentially delay installation of
      software updates by changing the time zone on their computers

      Enable SSL on WSUS and follow the best practices for securing Windows Server
      Update Services (WSUS).

      Identify and follow the security best practices for the version of WSUS that you use
      with Configuration Manager.

<!-- p.56 -->

     For more information on enabling SSL, see the Configure a software update point
     to use TLS/SSL with a PKI certificate tutorial.

       ） Important

       If you configure the software update point to enable SSL communications for
       the WSUS server, you must configure virtual roots for SSL on the WSUS server.

     Enable CRL checking.

     By default, Configuration Manager doesn't check the certificate revocation list
     (CRL) to verify the signature on software updates before they're deployed to
     computers. Checking the CRL each time a certificate is used offers more security
     against using a certificate that has been revoked, but it introduces a connection
     delay and incurs additional processing on the computer performing the CRL check.

     For more information about how to enable CRL checking for software updates, see
     How to enable CRL checking for software updates.

     Configure WSUS to use a custom website.

     When you install WSUS on the software update point, you have the option to use
     the existing IIS Default Web site or to create a custom WSUS website. Create a
     custom website for WSUS so that IIS hosts the WSUS services in a dedicated virtual
     website instead of sharing the same web site that is used by the other
     Configuration Manager site systems or other applications.

     For more information, see Configure WSUS to use a custom web site.

Privacy information for software updates
Software updates scans your client computers to determine which software updates you
require, and then sends that information back to the site database. During the software
updates process, Configuration Manager might transmit information between clients
and servers that identify the computer and logon accounts.

Configuration Manager maintains state information about the software deployment
process. State information isn't encrypted during transmission or storage. State
information is stored in the Configuration Manager database and it's deleted by the
database maintenance tasks. No state information is sent to Microsoft.

The use of Configuration Manager software updates to install software updates on client
computers might be subject to software license terms for those updates, which is

<!-- p.57 -->

separate from the Software License Terms for Configuration Manager. Always review and
agree to the Software Licensing Terms prior to installing the software updates by using
Configuration Manager.

Configuration Manager doesn't implement software updates by default and requires
several configuration steps before information is collected.

Before you configure software updates, consider your privacy requirements.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.58 -->

Prepare for software updates
management
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before the compliance assessment data of the software update displays in the
Configuration Manager console and before you can deploy software updates to client
computers, you must complete the steps in the following sections.

Step 1: Install a software update point
The software update point is required on the central administration site, or stand-alone
primary site, and on primary sites to enable the software updates compliance
assessment and to deploy software updates to clients. The software update point is
optional on secondary sites. For details, see Install a software update point

Step 2: Synchronize Software Updates
Software updates synchronization is the process of retrieving the software updates
metadata that meets the criteria that you configure. Software updates are not displayed
in the Configuration Manager console until you synchronize software updates. For
details, see Synchronize software updates.

Step 3: Configure classifications and products
to synchronize
Perform this configuration on the central administration site or stand-alone primary site.
After you synchronize software updates the first time, Configuration Manager retrieves
an updated list of classifications and products. Now, you can select from the new
options in the Software Update Point Component properties. After you configure the
new classifications and products, repeat step 2 to start software updates synchronization
to retrieve software updates metadata for the new criteria. For details, see Configure
classifications and products to synchronize.

Step 4: Manage settings for software updates

<!-- p.59 -->

After you synchronize software updates, verify Configuration Manager client settings,
group policy configurations, and software updates settings before you deploy software
updates. For details, see Manage settings for software updates.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.60 -->

Install and configure a software update
point
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

  Before you install the software update point site system role (SUP), you must verify
  that the server meets the required dependencies and determines the software
  update point infrastructure on the site. For more information about how to plan for
  software updates and to determine your software update point infrastructure, see
  Plan for software updates.

The software update point is required on the central administration site and on the
primary sites to enable software updates compliance assessment and to deploy software
updates to clients. The software update point is optional on secondary sites. The
software update point site system role must be created on a server that has WSUS
installed. The software update point interacts with the WSUS services to configure the
software update settings and to request synchronization of software updates metadata.
When you have a Configuration Manager hierarchy, install and configure the software
update point on the central administration site first, then on child primary sites, and
then optionally, on secondary sites. When you have a stand-alone primary site, not a
central administration site, install and configure the software update point on the
primary site first, and then optionally, on secondary sites. Some settings are only
available when you configure the software update point on a top-level site. There are
different options that you must consider depending on where you installed the software
update point.

  ） Important

        You can install more than one software update point on a site. The first
        software update point that you install is configured as the synchronization
        source, which synchronizes the updates from Microsoft Update or from the
        upstream synchronization source. The other software update points on the
        site are configured as replicas of the first software update point. Therefore,
        some settings are not available after you install and configure the initial
        software update point.

<!-- p.61 -->

          It isn't supported to install the software update point site system role on a
          server that has been configured and used as a standalone WSUS server or
          using a software update point to directly manage WSUS clients. Existing
          WSUS servers are only supported as upstream synchronization sources for the
          active software update point. See Synchronize from an upstream data source
          location

You can add the software update point site system role to an existing site system server
or you can create a new one. On the System Role Selection page of the Create Site
System Server Wizard or Add Site System Roles Wizard, depending on whether you
add the site system role to a new or existing site server, select Software update point,
and then configure the software update point settings in the wizard. The settings are
different depending on the version of Configuration Manager that you use. For more
information about how to install site system roles, see Install site system roles.

Use the following sections for information about the software update point settings on
a site.

Proxy server settings
You can configure the proxy server settings on different pages of the Create Site System
Server Wizard or Add Site System Roles Wizard depending on the version of
Configuration Manager that you use.

      You must configure the proxy server, and then specify when to use the proxy
      server for software updates. Configure the following settings:

          Configure the proxy server settings on the Proxy page of the wizard or on the
          Proxy tab in Site system Properties. The proxy server settings are site system
          specific, meaning that all site system roles use the proxy server settings that you
          specify.

          Specify whether to use the proxy server when Configuration Manager
          synchronizes the software updates and when it downloads content by using an
          automatic deployment rule. Configure the software update point proxy server
          settings on the Proxy and Account Settings page of the wizard or on the Proxy
          and Account Settings tab in Software update point Properties.

          The Use a proxy when downloading content by using automatic deployment
          rules setting is available but it isn't used for a software update point on a

<!-- p.62 -->

        secondary site. Only the software update point on the central administration
        site and primary site downloads content from the Microsoft Update page.

        By default, the Local System account for the server on which an automatic
        deployment rule was created is used to connect to the Internet and download
        software updates when the automatic deployment rules run. When this account
        doesn't have access to the Internet, software updates fail to download and the
        following entry is logged to ruleengine.log: Failed to download the update
        from internet. Error = 12007. Configure the credentials to connect to the proxy
        server when the Local System account doesn't have Internet access.

WSUS settings
You must configure WSUS settings on different pages of the Create Site System Server
Wizard or Add Site System Roles Wizard depending on the version of Configuration
Manager that you use, and in some cases, only in the properties for the software update
point, also known as Software Update Point Component Properties. Use the information
in the following sections to configure the WSUS settings.

  ） Important

  To ensure that the best security protocols are in place, we highly recommend that
  you use the TLS/SSL protocol to help secure your software update infrastructure.
  Beginning with the September 2020 cumulative update, HTTP-based WSUS servers
  will be secure by default. A client scanning for updates against an HTTP-based
  WSUS will no longer be allowed to leverage a user proxy by default. If you still
  require a user proxy despite the security trade-offs, a new software updates client
  setting is available to allow these connections. For more information about the
  changes for scanning WSUS, see September 2020 changes to improve security for
  Windows devices scanning WSUS        .

WSUS port settings
You must configure the WSUS port settings on the Software Update Point page of the
wizard or in the properties of the software update point. Use the following procedure to
determine the port settings used by WSUS:

Determine the port settings used in IIS

   1. On the WSUS server, open Internet Information Services (IIS) Manager.

<!-- p.63 -->

   2. Expand Sites, select the WSUS Administration site, and then select Bindings from
     the Actions pane. In the Site Bindings dialog, the HTTP and HTTPS port values are
     displayed in the Port column.

Configure SSL communications to WSUS
To ensure that the best security protocols are in place, we highly recommend that you
use the TLS/SSL protocol to help secure your software update infrastructure. You can
configure SSL communication on the Software Update Point page of the wizard or on
the General tab in the properties of the software update point. Before you select, the
option to Require SSL communication to the WSUS server for your SUP, ensure that
you've enabled SSL communication on the WSUS servers.

For more information about how to use SSL, see Decide whether to configure WSUS to
use SSL and Configure a software update point to use TLS/SSL with a PKI certificate.

Allow cloud management gateway traffic
You can enable a software update point to accept communication from clients on the
internet via a cloud management gateway (CMG). For more information about this
setting, see Configure client-facing roles for CMG traffic.

Adjust the download speed to use the unused network
bandwidth (Windows LEDBAT)
(Introduced in version 2203)

Starting in Configuration Manager version 2203, you can enable Windows Low Extra
Delay Background Transport (LEDBAT) for your software update points that run Windows
Server 2016 or later. LEDBAT adjusts download speeds during client scans against WSUS
to help control network congestion.

If a site system has both the distribution point and software update point roles, you can
configure LEDBAT independently on the roles. For example, if you only enable LEDBAT
on the distribution point role, the software update point role doesn't inherit the same
configuration.

To use LEDBAT for your SUPs that run Windows Server 2016 or later, enable the Adjust
the download speed to use the unused network bandwidth (Windows LEDBAT) setting
from one of the following locations:

     On the Software Update Point page of the install software update point wizard

<!-- p.64 -->

        In the General tab of the software update point properties

For more general information on Windows LEDBAT, see Fundamental concepts for
content management.

WSUS Server Connection Account
You can configure an account to be used by the site server when it connects to WSUS
that runs on the software update point. When you don't configure this account, the
Configuration Manager uses the computer account for the site server to connect to
WSUS. Configure the WSUS Server Connection Account on the Proxy and Account
Settings page of the wizard, or on the Proxy and Account Settings tab in Software
update point Properties. You can configure the account in different places of the wizard
depending on the version of Configuration Manager that you use.

For more information about Configuration Manager accounts, see Accounts used.

Synchronization source
You can configure the upstream synchronization source for software updates
synchronization on the Synchronization Source page of the wizard, or on the Sync
Settings tab in Software Update Point Component Properties. Your options for the
synchronization source vary depending on the site.

Use the following table for the available options when you configure the software
update point at a site.

                                                                             ﾉ    Expand table

 Site                                  Available synchronization source options

 - Central administration site         - Synchronize from the Microsoft Update website
 - Stand-alone primary site            - Synchronize from an upstream data source location
                                       - Do not synchronize from Microsoft Update or upstream
                                       data source

 - Additional software update points   - Synchronize from an upstream data source location
 at a site
 - Child primary site
 - Secondary site

The following list provides more information about each option that you can use as the
synchronization source:

<!-- p.65 -->

     Synchronize from Microsoft Update: Use this setting to synchronize software
     updates metadata from Microsoft Update. The central administration site must
     have Internet access; otherwise, synchronization will fail. This setting is available
     only when you configure the software update point on the top-level site.

          When there's a firewall between the software update point and the Internet, the
          firewall might need to be configured to accept the HTTP and HTTPS ports that
          are used for the WSUS Web site. You can also choose to restrict access on the
          firewall to limited domains. For more information about how to plan for a
          firewall that supports software updates, see Configure firewalls.

          If you're sharing the WSUS database, be aware that Configuration Manager
          randomly chooses the software update point between the front-end WSUS
          servers. Ensure that the internet access requirements are met for each of the
          WSUS servers. If internet access requirements aren't met, then sync failures can
          occur. You may see different software update points at the top-level site syncing
          with Microsoft.

     Synchronize from an upstream data source location: Use this setting to
     synchronize software updates metadata from the upstream synchronization
     source. The child primary sites and secondary sites are automatically configured to
     use the parent site URL for this setting. You have the option to synchronize
     software updates from an existing WSUS server. Specify a URL, such as
     https://WSUSServer:8531 , where 8531 is the port that is used to connect to the
     WSUS server.

     Do not synchronize from Microsoft Update or upstream data source: Use this
     setting to manually synchronize software updates when the software update point
     at the top-level site is disconnected from the Internet. For more information, see
     Synchronize software updates from a disconnected software update point.

You can also configure whether to create WSUS reporting events on the
Synchronization Source page of the wizard or on the Sync Settings tab in Software
Update Point Component Properties. Configuration Manager doesn't use these events;
therefore, you'll normally choose the default setting Do not create WSUS reporting
events.

Synchronization schedule
Configure the synchronization schedule on the Synchronization Schedule page of the
wizard or in the Software Update Point Component Properties. This setting is configured
only on the software update point at the top-level site.

<!-- p.66 -->

If you enable the schedule, you can configure a recurring simple or custom
synchronization schedule. When you configure a simple schedule, the start time is based
on the local time for the computer that runs the Configuration Manager console at the
time when you create the schedule. When you configure the start time for a custom
schedule, it's based on the local time for the computer that runs the Configuration
Manager console.

   Tip

       Schedule software updates synchronization to run by using a time-frame that
       is appropriate for your environment. One typical scenario is to set the
       software updates synchronization schedule to run shortly after the Microsoft
       regular security update release on the second Tuesday of each month, which
       is commonly referred to as Patch Tuesday. Another typical scenario is to set
       the software updates synchronization schedule to run daily when you use
       software updates to deliver the Endpoint Protection definition and engine
       updates.
       When you choose not to enable software updates synchronization on a
       schedule, you can manually synchronize software updates from the All
       Software Updates or Software Update Groups node in the Software Library
       workspace. For more information, see synchronize software updates.

Supersedence rules
Configure the supersedence settings on the Supersedence Rules page of the wizard or
on the Supersedence Rules tab in Software Update Point Component Properties. You
can configure the supersedence rules only on the top-level site. You can also specify the
supersedence rules behavior for feature updates separately from non-feature updates.

  ７ Note

  The Supersedence Rules page of the wizard is available only when you configure
  the first software update point at the site. This page is not displayed when you
  install additional software update points.

On this page, you can specify when superseded software updates are expired in
Configuration Manager, which prevents them from being included in new deployments
and flags the existing deployments to indicate that the superseded software updates

<!-- p.67 -->

contain one or more expired software updates. You can specify a period of time before
the superseded software updates are expired, which allows you to continue to deploy
them. For more information, see Supersedence rules.

The default setting is to wait 3 months before expiring a superseded update. The 3
month default is to give you time to verify the update is no longer needed by any of
your client computers. It's recommended that you don't assume that superseded
updates should be immediately expired in favor of the new, superseding update. You
can display a list of the software updates that supersede the software update on the
Supersedence Information tab in the software update properties.

WSUS Maintenance
Configuration Manager can automatically run the most common WSUS maintenance
tasks for you. For more information about these tasks, see Software updates
maintenance.

Maximum run time
You can specify the maximum amount of time a software update installation has to
complete. You can specify the maximum run time for the following:

     Maximum run time for Windows feature updates (minutes)
        Feature updates - An update that is in one of these three classifications:
           Upgrades
           Update rollups
           Service packs

     Maximum run time for Office 365 updates and non-feature updates for
     Windows (minutes)
        Non-feature updates - An update that isn't a feature upgrade and whose
        product is listed as one of the following:
           Windows 11
           Windows 10 (all versions)
           Windows Server 2012 R2
           Windows Server 2016
           Windows Server 2019
           Office 365

     Maximum run time for all other software updates outside these categories such
     as third-party updates (minutes): The default maximum run time of these updates

<!-- p.68 -->

     varies depending on when the update first synchronized into the environment and
     the Configuration Manager version. Use the cart below to determine the maximum
     runtime value for these updates:

                                                                           ﾉ   Expand table

      2203 or later                                               2103, 2107, or   2010
                                                                  2111

      The maximum run time for all other software updates is      60 minutes       10
      customizable. The default is 60 minutes.                                     minutes

        ） Important
          This setting only changes the maximum runtime for new updates that are
          synchronized in by SUP. It doesn't change the run time on existing updates
          that synchronized before the run time was modified. For instance, if Update
          1 was first synchronized into a 2111 environment, then it's maximum run

          time is 60 minutes. You then upgrade the environment to version 2203 and
          set the maximum run time to 30 minutes. Update 1 retains it's 60 minute
          runtime. However, when a new update, Update 2 , synchronizes in, it is
          given the new 30 minute run time.
          If you need to change the maximum run time of an update manually, you
          can configure the software update settings for it.

Classifications
Configure the classifications settings on the Classifications page of the wizard, or on the
Classifications tab in Software Update Point Component Properties. For more
information about software update classifications, see Update classifications.

   Tip

        The Classifications page of the wizard is available only when you configure
        the first software update point at the site. This page is not displayed when you
        install additional software update points.
        When you first install the software update point on the top-level site, clear all
        of the software updates classifications. After the initial software updates
        synchronization, configure the classifications from an updated list, and then

<!-- p.69 -->

       re-initiate synchronization. This setting is configured only on the software
       update point at the top-level site.

Products
Configure the product settings on the Products page of the wizard, or on the Products
tab in Software Update Point Component Properties.

   Tip

       The Products page of the wizard is available only when you configure the first
       software update point at the site. This page is not displayed when you install
       additional software update points.
       When you first install the software update point on the top-level site, clear all
       of the products. After the initial software updates synchronization, configure
       the products from an updated list, and then re-initiate synchronization. This
       setting is configured only on the software update point at the top-level site.

Languages
Configure the language settings on the Languages page of the wizard, or on the
Languages tab in Software Update Point Component Properties. Specify the languages
for which you want to synchronize software update files and summary details. The
Software Update File setting is configured at each software update point in the
Configuration Manager hierarchy. The Summary Details settings are configured only on
the top-level software update point. For more information, see Languages.

  ７ Note

  The Languages page of the wizard is available only when you install the software
  update point at the central administration site. You can configure the Software
  Update File languages at child sites from the Languages tab in Software Update
  Point Component Properties.

Third party updates

<!-- p.70 -->

You can enable third party updates for Configuration Manager clients. When you Enable
third party software updates in the SUP component properties, the SUP will download
the signing certificate used by WSUS for third party updates. This option isn't available
during install of the software update point, and should be configured after the SUP is
installed. To enable the client settings for third party updates, see the About client
settings article.

Next steps
You installed the software update point starting at the top-most site in your
Configuration Manager hierarchy. Repeat the procedures in this article to install the
software update point on child sites.

Once you have your software update points installed, go to synchronize software
updates.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.71 -->

Synchronize software updates
Article • 07/25/2023

Applies to: Configuration Manager (current branch)

Software update synchronization in Configuration Manager is the process of retrieving
the software update metadata that meets the criteria that you configure. This includes
specific products, classifications, and languages. Typically, the software update point on
the central administration site, or on a stand-alone primary site, retrieves the metadata
from Microsoft Update. Then, the top-level site will send a synchronization request to
other sites. When a site receives the synchronization request from the parent site, the
software update point for the site retrieves software updates metadata from its
upstream synchronization source. For more information about software update
synchronization process, see Software updates synchronization.

You configure software update synchronization to run on a schedule in the properties
for the software update point at the top-level site. Once you configure the
synchronization schedule, you'll typically not change the schedule as part of normal
operations. However, you can manually initiate software update synchronization when
it's necessary.

  ７ Note

  Software update points must be connected to their upstream synchronization
  source to synchronize software updates. When a software update point is
  disconnected from its upstream synchronization source, you can use the export and
  import method to synchronize software updates. For more information, see
  Synchronize software updates from a disconnected software update point.

Schedule software updates synchronization
When you configure a schedule for software updates synchronization, the top-level
software update point starts synchronization with Microsoft Update at the scheduled
date and time. The custom schedule allows you to synchronize software updates on a
date and time when the demands of the Windows Server Update Services (WSUS)
server, site server, and network are low. For example, you can set the schedule so that
software updates are synchronized every week at 2:00 AM. During the scheduled
synchronization, all changes to the software updates metadata since the last scheduled

<!-- p.72 -->

synchronization are inserted into the site database. This includes new software updates
metadata or metadata that has been modified, removed, or is now expired.

Use the following procedures on the top-level site to schedule software updates
synchronization.

To schedule software updates synchronization

   1. In the Configuration Manager console, click Administration.

   2. In the Administration workspace, expand Site Configuration, and then click Sites.

   3. In the results pane, click the central administration site or stand-alone primary site.

   4. On the Home tab, in the Settings group, expand Configure Site Components, and
     then click Software Update Point.

   5. In the Software Update Point Component Properties dialog box, select Enable
     synchronization on a schedule, and then specify the synchronization schedule.

Manually start software updates
synchronization
You can manually initiate software updates synchronization on the top-level site in the
Configuration Manager console from the All Software Updates node in the Software
Library workspace.

Use the following procedures on the top-level site to manually initiate software updates
synchronization.

To manually start software updates synchronization

   1. In the Configuration Manager console that is connected to the central
     administration site or stand-alone primary site, click Software Library.

   2. In the Software Library workspace, expand Software Updates and click All
     Software Updates or Software Update Groups.

   3. On the Home tab, in the All Software Updates group, click Synchronize Software
     Updates. Click Yes in the dialog box to confirm that you want to initiate the
     synchronization process.

<!-- p.73 -->

     After you initiate the synchronization process on the software update point, you
     can monitor the synchronization process from the Configuration Manager console
     for all software update points in your hierarchy. Use the following procedure to
     monitor the software updates synchronization process.

Monitor software updates synchronization
After you initiate the synchronization process, you can use the Configuration Manager
console to monitor the process for all software update points in your hierarchy. Use the
following procedure to monitor the software update synchronization process. For more
information about monitoring software updates, including the synchronization process,
see Monitor software updates.

To monitor the software updates synchronization process
   1. In the Configuration Manager console, click Monitoring.

   2. In the Monitoring workspace, click Software Update Point Synchronization Status.

     The software update points in your Configuration Manager hierarchy are displayed
     in the results pane. From this view, you can monitor the synchronization status for
     all software update points. When you want more detailed information about the
     synchronization process, you can review the wsyncmgr.log file that is located in
     <ConfigMgrInstallationPath>\Logs on each site server.

Import updates from the Microsoft Update
Catalog
The top-level Software Update Point uses WSUS to get information about software
updates from Microsoft into Configuration Manager. Occasionally, you might need an
update that doesn't automatically synchronize into WSUS for your selected products
and classifications but is available in the Microsoft Update Catalog   . Updates that don't
automatically synchronize into WSUS are typically meant to resolve highly specific
issues. Usually if an update is available in the catalog, you can import it into WSUS. You
can then synchronize it into Configuration Manager and deploy it like any other update.

To import an update from the Microsoft Update Catalog
The Import Updates action in WSUS was built using ActiveX, which is now deprecated.
This import functionality within WSUS has been replaced with a PowerShell script. The

<!-- p.74 -->

script allows you to import a single update, or multiple updates, from the catalog site
into WSUS.

   1. Use the instructions and PowerShell script from the WSUS and the Microsoft
     Update Catalog site article to import updates into WSUS for your top-level
     software update point. There isn't a need to import into WSUS for child sites. The
     top-level software update point will synchronize the updates to the child sites.
   2. Once the import is completed, in the Configuration Manager console, go to the
     Software Library workspace, expand Software Updates, and select the All
     Software Updates node.
   3. Select Synchronize Software Updates to synchronize the newly imported updates
     into Configuration Manager.

Next steps
After you synchronize software updates for the first time, or after there are new
classifications or products available, you must configure the new classifications and
products to synchronize software updates with the new criteria.

After you synchronize software updates with the criteria that you need, manage settings
for software updates.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.75 -->

Configure classifications and products
to synchronize
Article • 06/20/2024

Applies to: Configuration Manager (current branch)

Software updates metadata is retrieved during the synchronization process in
Configuration Manager based on the settings that you specify in the Software Update
Point component properties. After you synchronize software updates for the first time,
or when new products and classifications are released, you must go to the properties to
select the new items. Use the following procedure to configure classifications and
products to synchronize.

  ７ Note

  Use the procedure from this section only on the top-level site.

To configure classifications and products to
synchronize
   1. In the Configuration Manager console, navigate to Administration > Site
      Configuration > Sites.

   2. Select the central administration site or the stand-alone primary site.

   3. On the Home tab, in the Settings group, click Configure Site Components, and
      then click Software Update Point.

   4. On the Classifications tab, specify the software update classifications for which you
      want to synchronize software updates.

      Every software update is defined with an update classification that helps to
      organize the different types of updates. During the synchronization process, the
      software updates metadata for the specified classifications are synchronized.
      Configuration Manager provides the ability to synchronize software updates with
      the following update classifications:

            Critical Updates: Specifies a widely released fix for a specific problem that
            addresses a critical, non-security-related bug.

<!-- p.76 -->

       Definition Updates: Specifies a widely released and frequent software update
       that contains additions to a product's definition database.
       Feature Packs: Specifies new product functionality that is first distributed
       outside of a product release and that's typically included in the next full
       product release.
       Security Updates: Specifies a widely released fix for a product-specific,
       security-related vulnerability.
       Service Packs: Specifies a tested, cumulative set of all hotfixes, security
       updates, critical updates, and updates that are applied to a product.
       Additionally, service packs may contain additional fixes for problems that are
       found internally since the release of the product.
       Tools: Specifies a utility or feature that helps to complete one or more tasks.
       Update Rollups: Specifies a tested, cumulative set of hotfixes, security
       updates, critical updates, and updates that are packaged together for easy
       deployment. An update rollup generally addresses a specific area, such as a
       security or product component.
       Updates: Specifies a widely released fix for a specific problem. An update
       addresses a non-critical, non-security-related bug.
       Upgrade: Specifies an upgrade for Windows 10 or later features and
       functionality. These updates are also known as feature updates for Windows
       operating systems. All versions of WSUS running on currently supported
       versions of Windows Server support the Upgrade classification.

    ７ Note

    You can select the Include Microsoft Surface drivers and firmware updates
    checkbox to synchronize Microsoft Surface drivers. All software update points
    must run Windows Server 2016 or later to successfully synchronize Surface
    drivers. If you enable a software update point on a computer running
    Windows Server 2012 after you enable Surface drivers, the scan results for the
    driver updates are not accurate. This results in incorrect compliance data
    displayed in the Configuration Manager console and in Configuration
    Manager reports. For more information, see Manage Surface drivers with
    Configuration Manager.

5. On the Products tab, specify the products for which you want to synchronize
  software updates, and then click Close.

       Configuration Manager stores a list of products and product families from
       which you can choose when you first install the software update point.
       Products and product families that are released after Configuration Manager

<!-- p.77 -->

   is released might not be available to select until you complete software
   updates synchronization, which updates the list of available products and
   product families from which you can choose.

   The metadata for each software update defines the products for which the
   update is applicable. A product is a specific edition of an operating system or
   application, such as Windows Server 2012. A product family is the base
   operating system or application from which the individual products are
   derived. An example of a product family is Windows, of which Windows
   Server 2012 is a member. You can specify a product family or individual
   products within a product family. The more products that you select, the
   longer it takes to synchronize software updates.

   When software updates are applicable to multiple products, and at least one
   of the products was selected for synchronization, all of the products appear
   in the Configuration Manager console even if some products weren't
   selected. For example, if Windows Server 2012 is the only operating system
   that you selected, and if a software update applies to Windows 8 and
   Windows Server 2012, both products are displayed in the Configuration
   Manager console.

７ Note

Windows 10, version 1903 and later was added to Microsoft Update as its
own product rather than being part of the Windows 10 product like earlier
versions. This change caused you to do a number of manual steps to ensure
that your clients see these updates. We've helped reduce the number of
manual steps you have to take for the new product in Configuration Manager
version 1906.

When you have the Windows 10 product selected for synchronization, the
following actions occur automatically:

     The Windows 10, version 1903 and later product is added for
     synchronization.
     Automatic Deployment Rules containing the Windows 10 product will
     be updated to include Windows 10, version 1903 and later.
     Servicing plans are updated to include the Windows 10, version 1903
     and later product.

<!-- p.78 -->

Configuring products for versions of Windows
10

Windows 10, version 1909
Windows 10, version 1909 shares a common core operating system with Windows 10,
version 1903. Both of these versions are serviced with the same cumulative updates. For
more information about Windows 10, version 1909, see the Windows 10, version 1909
delivery options    blog post.

To make sure both your Windows 10 version 1909 and Windows 10, version 1903 clients
install updates from Configuration Manager:

     Approve updates for both the 1909 and 1903 versions of Windows 10.
        The updates have different titles and applicability rules for each OS version.
        Approving each update per version and architecture of the OS maintains the
        normal approval process for admins.
     The cumulative update installation files are the same for both the 1909 and 1903
     versions of Windows 10.
        Configuration Manager will only download the update source files once.

Feature Updates for Windows 10, version 1909
When you approve feature updates for Windows 10, version 1909, there are a few
different options you'll see:

     Windows 10, version 1903 clients are offered an Enablement Package        , released
     November 12, 2019.

        The enablement package is a small, quick to install file that activates the
        Windows 10, version 1909 features and restarts the device.

        Prerequisites for the enablement package include:
           A minimum cumulative update of KB4517389 , released October 8, 2019.
           A minimum servicing stack update of KB4520390        , released September 24,
           2019.

        This update, like any other Feature Update, isn't available for import from the
        Microsoft Update Catalog     .

        The update will automatically synchronize with WSUS if you have the Windows
        10, version 1903 and later product and Upgrades classification selected for

<!-- p.79 -->

        synchronization.

        In the Configuration Manager console, go to the Software Library workspace,
        expand Windows Servicing, and select the All Windows Feature Updates node.
        Search for the terms "enablement" or "4517245".

            Tip

           Since these are feature updates, they aren't in the All Software Updates
           node.

     Windows 10, version 1809 and earlier clients are upgraded with a single direct
     feature update.
        This is just like all other previous installations for Feature Updates that you've
        done for Windows 10.

  ７ Note

  Both the enablement package and the traditional feature update for Windows 10,
  version 1909 will show as "Installed" in reporting, regardless of which path was
  used to install it.

Windows 10, version 1903 and later
Windows 10, version 1903 and later was added to Microsoft Update as its own product
rather than being part of the Windows 10 product like earlier versions. This change
caused you to do a number of manual steps to ensure that your clients see these
updates. We've helped reduce the number of manual steps you have to take for the new
product in Configuration Manager version 1906.

Windows 10, version 1903 and later with Configuration Manager
version 1906

When you update to Configuration Manager version 1906 and have the Windows 10
product selected for synchronization, the following actions occur automatically:

     The Windows 10, version 1903 and later product is added for synchronization.
     Automatic Deployment Rules containing the Windows 10 product will be updated
     to include Windows 10, version 1903 and later.

<!-- p.80 -->

        Servicing plans are updated to include the Windows 10, version 1903 and later
        product.

Windows 10, version 1903 and later with Configuration Manager
version 1902
If you're using Configuration Manager 1902 with Windows 10, version 1903 clients,
you'll need to:

        Select the Windows 10, version 1903 and later product for synchronization.
        Update any Automatic Deployment Rules for Windows 10, version 1903 clients.
        Update Servicing plans for Windows 10, version 1903 clients.

Windows Insider Program
You can service and update devices running Windows Insider Preview builds with
Configuration Manager. This change means you can manage these devices without
changing your normal processes or enabling Windows Update for Business. You can
download Feature Updates and Cumulative Updates for Windows Insider Preview builds
into Configuration Manager just like any other Windows update or upgrade. For more
information, see the Publishing pre-release Windows Feature Updates to WSUS          blog
post.

For more information about support for Windows Insider in Configuration Manager, see
Support for Windows 11.

Prerequisites
        Configuration Manager environment that's configured for software update
        management.
        Windows devices running Windows Insider Preview build.
        A collection containing the Windows Insider devices.

Enable Windows Insider upgrades and updates
You need to enable the products and classifications for Windows Insider upgrades and
updates. Feature Updates, Cumulative updates, and other updates for Windows Insider
are under the Windows Insider Pre-Release product category.

   1. In the Configuration Manager console, navigate to Administration > Site
        Configuration > Sites.
