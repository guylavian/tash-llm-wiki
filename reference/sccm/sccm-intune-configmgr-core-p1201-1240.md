---
title: "Core infrastructure documentation — pages 1201-1240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1201-1240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1201-1240
family: sccm
documentKind: "doc"
abstract: "Example of using boundary groups Procedures for boundary groups Feedback Was this page helpful?  Yes  No Provide product feedback Example of using boundary groups Article • 10/04/2022 Applies to: Configuration Manager (current branch) The following example uses a client search"
---

# Core infrastructure documentation — pages 1201-1240

<!-- p.1201 -->

     Example of using boundary groups

     Procedures for boundary groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1202 -->

Example of using boundary groups
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The following example uses a client searching for content from a distribution point. This
example can be applied to other site system roles that use boundary groups.

Create three boundary groups that don't share boundaries or site system servers:

      Group BG_A with distribution points DP_A1 and DP_A2

      Group BG_B with distribution points DP_B1 and DP_B2

      Group BG_C with distribution points DP_C1 and DP_C2

Add the network locations of your clients as boundaries to only the BG_A boundary
group. Then configure relationships from that boundary group to the other two
boundary groups:

      Configure distribution points for the first neighbor group (BG_B) to be used after
      10 minutes. This group contains distribution points DP_B1 and DP_B2. Both are
      well connected to the first group's boundary locations.

      Configure the second neighbor group (BG_C) to be used after 20 minutes. This
      group contains distribution points DP_C1 and DP_C2. Both are across a WAN from
      the other two boundary groups.

      Also add to the default site boundary group another distribution point that's on
      the site server. This server is your least preferred content source location, but it's
      centrally located to all your boundary groups.

      Example of boundary groups and fallback times:

<!-- p.1203 -->

                                                                                       

With this configuration:

     The client begins searching for content from distribution points in its current
     boundary group (BG_A). It searches each distribution point for two minutes, and
     then switches to the next distribution point in the boundary group. The client's
     pool of valid content source locations includes DP_A1 and DP_A2.

     If the client fails to find content from its current boundary group after searching for
     10 minutes, it then adds the distribution points from the BG_B boundary group to
     its search. It then continues to search for content from a distribution point in its
     combined pool of servers. This pool now includes servers from both the BG_A and
     BG_B boundary groups. The client continues to contact each distribution point for
     two minutes, and then switches to the next server in its pool. The client's pool of
     valid content source locations includes DP_A1, DP_A2, DP_B1, and DP_B2.

     After another 10 minutes (20 minutes total), if the client still hasn't found a
     distribution point with content, it expands its pool to include available servers from
     the second neighbor group, boundary group BG_C. The client now has six
     distribution points to search: DP_A1, DP_A2, DP_B2, DP_B2, DP_C1, and DP_C2. It

<!-- p.1204 -->

     continues changing to a new distribution point every two minutes until it finds
     content.

     If the client hasn't found content after a total of 120 minutes, it falls back to
     include the default site boundary group as part of its continued search. Now the
     pool includes all distribution points from the three configured boundary groups,
     and the final distribution point located on the site server. The client then continues
     its search for content, changing distribution points every two minutes until content
     is found.

By configuring the different neighbor groups to be available at different times, you
control when specific distribution points are added as a content source location. The
client uses fallback to the default site boundary group as a safety net for content that
isn't available from any other location.

Next steps
Procedures for boundary groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1205 -->

How to configure boundary groups for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article includes procedures on how to view and configure boundary groups. Before
you begin, make sure you understand boundary group concepts. For more information,
see Boundary groups.

Show boundary groups for devices
To help you better identify and troubleshoot device behaviors with boundary groups,
you can view the boundary groups for specific devices. In the Devices node or when you
show the members of a Device Collection, add the Boundary Group(s) column to the
list view.

      If a device is in more than one boundary group, the value is a comma-separated
      list of boundary group names.

      The data updates when the client makes a location request to the site, or at most
      every 24 hours.

      If a client is roaming and not a member of a boundary group, the value is blank.

  ７ Note

  This information is site data and only available on primary sites. You won't see a
  value for this column when you connect the Configuration Manager to a central
  administration site (CAS). For more information, see Types of data.

Create a boundary group
   1. In the Configuration Manager console, go to the Administration workspace,
      expand Hierarchy Configuration, and select the Boundary Groups node.

   2. On the Home tab, in the Create group, select Create Boundary Group.

   3. In the Create Boundary Group dialog box, on the General tab, specify a Name for
      this boundary group. Optionally include a Description.

<!-- p.1206 -->

   4. Select OK to save the new boundary group, or continue to the next section to
     configure the boundary group.

Configure a boundary group
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Hierarchy Configuration, and select the Boundary Groups node.

   2. Select the boundary group you want to modify, and select Properties in the
     ribbon. This action opens the boundary group Properties window.

Configure the following settings:

     Add or remove boundaries
     Configure site assignment and select site system servers
     Configure fallback behavior
     Configure boundary group options

Add or remove boundaries
In the boundary group Properties window, use the General tab to modify the
boundaries that are members of this boundary group:

     To add boundaries, select Add. In the Add Boundaries window, select the check
     box for one or more boundaries, and select OK.

     To remove boundaries, select the boundary in the list, and select Remove.

Configure site assignment and select site system servers
To modify the site assignment and associated site system server configuration, switch to
the References tab in the boundary group Properties window.

     To enable this boundary group for use by clients for site assignment, select Use
     this boundary group for site assignment. Then select a site from the Assigned site
     dropdown list. For more information, see Site assignment.

     To associate available site system servers with this boundary group, select Add. The
     Add Site Systems window only lists servers that have supported site system roles.
     Select the check box for one or more servers, and select OK. It adds them as
     associated site system servers for this boundary group.

<!-- p.1207 -->

       ７ Note

       You can select any combination of available site systems from any site in the
       hierarchy. Selected site systems are listed on the Site Systems tab in the
       properties of each boundary that's a member of this boundary group.

     To remove a server from this boundary group, select the server and then select
     Remove.

       ７ Note

       To stop use of this boundary group for associating site systems, remove all
       servers listed as associated site system servers.

Configure fallback behavior
To configure fallback behavior, switch to the Relationships tab in the boundary group
Properties window.

     To create a relationship with another boundary group:

        Select Add. In the Fallback Boundary Groups window, select the boundary
        group to configure.

        Set a fallback time for the following site system roles:

           Distribution point

           Software update point

           Management point

             ７ Note

             For example, you open the Properties window for the Branch Office
             boundary group. In the Fallback Boundary Groups window, you select
             the Main Office boundary group. You set the distribution point fallback
             time to 20 . When you save this configuration, clients in the Branch
             Office boundary group will start searching for content from the
             distribution points in the Main Office boundary group after 20 minutes.

<!-- p.1208 -->

        To prevent fallback to a specific boundary group, select the boundary group,
        and then select Never fallback for the type of site system role. This action can
        include the default site boundary group.

     To modify the configuration of an existing relationship, select the boundary group
     in the list, and select Change. This action opens the Fallback Boundary Groups
     window for just this boundary group.

     To remove a relationship, select the boundary group in the list, and select Remove.

For more information, see Fallback.

Configure boundary group options
To configure options for clients in this boundary group, switch to the Options tab. For
more information, see Boundary group options.

     Allow peer downloads in this boundary group: This option is enabled by default.
     The management point provides clients a list of content locations that includes
     peer sources.

        During peer downloads, only use peers within the same subnet: This setting is
        dependent upon the one above. If you enable this option, the management
        point only includes in the content location list peer sources that are in the same
        subnet as the client.

        Prefer distribution points over peers within the same subnet: By default, the
        management point prioritizes peer cache sources at the top of the list of
        content locations. This setting reverses that priority for clients in the same
        subnet as a peer cache source.

     Prefer cloud based sources over on-premises sources: A common scenario is if
     you have a branch office with a faster internet link, you can prioritize cloud content
     and policy. This behavior includes cloud management gateways (CMG) or
     Microsoft Update.

       ７ Note

       Starting in version 2203, this setting also applies for software update
       scanning. To reduce the performance impact of this change, existing clients
       don't automatically switch to a cloud-based software update point. For more
       information, see Boundary groups and software update points.

<!-- p.1209 -->

Configure a fallback site for automatic site
assignment
If clients aren't in a boundary group with an assigned site, assign them to this site when
they're installed.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. On the Home tab of the ribbon, in the Sites group, select Hierarchy Settings.

   3. On the General tab, select the checkbox to Use a fallback site. Then select a site
     from the Fallback site drop-down list.

   4. Select OK to save the configuration.

For more information, see Site assignment.

Enable use of preferred management points
For more information, see Preferred management points.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. On the Home tab of the ribbon, in the Sites group, select Hierarchy Settings.

   3. On the General tab, select Clients prefer to use management points specified in
     boundary groups.

   4. Select OK to save the configuration.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1210 -->

High availability options for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article describes how to deploy Configuration Manager using options that maintain
a high level of available service.

The following Configuration Manager options support high availability:

      Configure any central administration or primary site with an additional site server
      in passive mode.

      Configure a SQL Server Always On availability group for the site database at
      primary sites and the central administration site.

      Sites support multiple instances of site system roles that provide important
      services to clients. For example, management points and distribution points.

      Central administration sites and primary sites support the backup of the site
      database. The site database stores all the configurations for sites and clients. The
      sites in a hierarchy share this configuration data.

      Built-in site recovery options can reduce server downtime. These advanced options
      simplify recovery when you have a hierarchy with a central administration site.

      Clients can automatically remediate typical issues without administrative
      intervention.

      Sites generate alerts about clients that fail to submit recent data, which alerts
      administrators to potential problems.

      Configuration Manager provides several built-in reports and dashboards. Use
      these to identify problems and trends before they become problems for server or
      client operations.

Configuration Manager includes several features that provide near real-time service. If
these features are critical to meet your business requirements, plan and configure your
sites and hierarchies for high availability. For example:

      Client notification actions, such as restart, start Windows Defender scans, or
      remote desktop.

<!-- p.1211 -->

     State-based messages for monitoring features such as software updates and
     endpoint protection.

     Scripts

     CMPivot

Other features of Configuration Manager don't provide real-time service. These features
include, but aren't limited to, client settings, hardware and software inventory, software
deployments, and compliance settings. Expect them to operate with some data latency.
It's unusual for most scenarios that involve a temporary interruption of service to
become a critical problem. To minimize downtime, maintain autonomy of operations,
and provide a high level of service, configure your sites and hierarchies with high
availability in mind.

For example, Configuration Manager clients typically operate autonomously by using
known schedules and configurations for operations, and schedules to submit data to the
site for processing.

     When clients can't contact the site, they cache data to be submitted until they can
     contact the site.

     Clients that can't contact the site continue to operate. They use the last known
     schedules and cached information, until they can contact the site and receive new
     policies. For example, a client may keep a previously downloaded application that
     they must run or install.

     The site monitors its site systems and clients for periodic status updates. It can
     generate alerts when these components fail to register.

     Built-in reports provide insight to ongoing operations, historical operations, and
     current trends. Configuration Manager also supports state-based messages that
     provide near real-time information for ongoing operations.

High availability for sites and hierarchies

Use a site server in passive mode
Install an additional site server in passive mode for a central administration or primary
site. The site server in passive mode is in addition to your existing site server in active
mode. A site server in passive mode is available for immediate use, when needed. For
more information, see Site server high availability.

<!-- p.1212 -->

Use a remote content library
Move the site's content library to a remote location that provides highly available
storage. This feature is a requirement for site server high availability. For more
information, see Configure a remote content library for the site server.

Centralize content sources
All software content in Configuration Manager requires a package source location on
the network. Use centralized, highly available storage to host a common package source
location for all content.

Use a SQL Server Always On solution for the site database
Configuration Manager supports the following SQL Server Always On solutions for the
site database:

     Host the site database at primary sites and the central administration site in an
     availability group. For more information, see Prepare to use a SQL Server Always
     On availability group.

     Use a failover cluster instance for the database at a central administration site or
     primary site. For more information, see Use a SQL Server Always On failover cluster
     instance.

Secondary sites can't use SQL Server Always On, and don't support backup or
restoration of their site database. Recover a secondary site by reinstalling the secondary
site from its parent primary site.

Deploy a hierarchy of sites with a central administration
site, and one or more child primary sites
This configuration can provide fault tolerance when your sites manage overlapping
segments of your network. It also offers an additional recovery option to use the
information in the shared database available at another site, to rebuild the site database
at the recovered site. Use this option to replace a failed or unavailable backup of the
failed site's database.

Create regular backups at central administration sites and
primary sites

<!-- p.1213 -->

When you create and test a regular site backup, this makes sure that you have the data
necessary to recover a site. You also practice recovering a site in the minimal amount of
time.

Install multiple instances of site system roles
When you install multiple instances of critical site system roles, you provide redundant
points of contact for clients. For example, multiple management points and distribution
points provide redundant service in the event that a specific server is offline.

Install multiple instances of the SMS Provider at a site
The SMS Provider provides the point of administrative contact for one or more
Configuration Manager consoles. To provide redundancy for contact points to
administer your site and hierarchy, install multiple SMS Providers.

High availability for site system roles
At each site, you deploy site system roles to provide the services that you want clients to
use at that site. The site database contains the configuration information for the site and
for all clients. Use one or more of the available options to provide for high availability of
the site database, and the recovery of the site and site database if needed.

Redundancy for important site system roles
        Distribution point

        Management point

        Software update point

        State migration point

To provide redundancy for reporting on sites and clients, install multiple instances of the
reporting services point.

Failover support for a software update point in a network load balancing (NLB) cluster
was deprecated in version 1702. For more information, see Removed and deprecated
features. To provide redundancy for software update points, use software update point
switching. This allows clients to connect to a new software update point server if one
fails or becomes unavailable. For more information, see Software update point switching

<!-- p.1214 -->

Built-in site backup
Configuration Manager includes a built-in backup task to help you back up your site and
critical information on a regular schedule. Additionally, the Configuration Manager
setup wizard supports site restoration actions to help you restore a site to operations.

Publishing to Active Directory Domain Services and DNS
Configure each site to publish data about the site to Active Directory Domain Services
and DNS. This publishing enables clients to identify the most accessible server on the
network. Clients also use it to identify when new site system servers are available to
provide important services, such as management points.

SMS Provider and Configuration Manager console
Configuration Manager supports installing multiple SMS Providers on separate servers
as multiple access points for the console. If one SMS Provider server is offline, you can
still view and manage sites and clients.

When a Configuration Manager console connects to a site, it connects to an instance of
the SMS Provider at that site. The instance of the SMS Provider is randomly selected. If
the selected SMS Provider isn't available, you have the following options:

     Reconnect the console to the site. Each new connection request is randomly
     assigned an instance of the SMS Provider. It's possible that the new connection is
     assigned an available instance.

     Connect the console to a different Configuration Manager site and manage the
     configuration from that connection. This option introduces a slight delay of
     configuration changes of no more than a few minutes. After the SMS Provider for
     the site is online, reconnect your Configuration Manager console directly to the
     site that you want to manage.

Install the Configuration Manager console on multiple computers for use by
administrators. Each SMS Provider supports connections from more than one console.

Management point
Install multiple management points at each primary site, and enable the sites to publish
site data to your Active Directory infrastructure, and to DNS.

<!-- p.1215 -->

Multiple management points help to load-balance the use of any single management
point by multiple clients. Also consider installing one or more database replicas for
management points. This configuration decreases the processor-intensive operations of
the management point. It also increases the availability of this critical site system role.

Secondary sites only support installation of one management point, which must be
located on the secondary site server. Management points at secondary sites aren't
considered to have a highly available configuration.

  ７ Note

  Devices managed by on-premises mobile device management connect to only one
  management point at a primary site. The management point is assigned by
  Configuration Manager to the mobile device during enrollment and then doesn't
  change. When you install multiple management points and enable more than one
  for mobile devices, the management point that's assigned to a mobile device client
  is non-deterministic.

  If the management point that a mobile device client uses becomes unavailable, you
  must resolve the problem with that management point or wipe the mobile device
  and re-enroll the mobile device so that it can be assigned to an operational
  management point that is enabled for mobile devices.

Distribution point
Install multiple distribution points, and deploy content to multiple distribution points.
Add more than one distribution point per boundary group to make sure clients get
several options in their content request. Configure boundary group relationships so that
they have a predicable fallback behavior to another boundary group or content-enabled
cloud management gateway. For more information, see Configure boundary groups.

High availability for clients

Client operations are autonomous
Configuration Manager client autonomy includes the following behaviors:

     Clients don't require continuous contact with any specific site system servers. They
     use known configurations to perform preconfigured actions on a schedule.

<!-- p.1216 -->

     Clients can use any available instance of a site system role that provides services to
     clients. They attempt to contact known servers until they locate an available server.

     Clients can run inventory, software deployments, and similar scheduled actions
     independent of direct contact with site system servers.

     Clients that are configured to use a fallback status point can submit details to the
     fallback status point when they can't communicate with a management point.

Clients can repair themselves
Clients automatically remediate most typical issues without direct administrative
intervention.

     Periodically, clients self-evaluate their status. They take action to remediate typical
     problems by using a local cache of remediation steps and source files for repairs.

     When a client fails to submit status information to its site, the site can generate an
     alert. Administrative users that receive these alerts can take immediate action to
     restore the normal operation of the client.

Clients cache information to use in the future
When a client communicates with a management point, the client can obtain and cache
the following information:

     Client settings

     Client schedules

     Information about software deployments and a download of the software the
     client is scheduled to install, when the deployment is configured for this action.

When a client can't contact a management point, the clients locally cache the status,
state, and client information they report to the site. The client transfers this data after it
establishes contact with a management point.

Client can submit status to a fallback status point
When you configure a client to use a fallback status point, you provide an additional
point of contact for the client to submit important details about its operation. Clients
that are configured to use a fallback status point continue to send status about their

<!-- p.1217 -->

operations to that site system role even when the client can't communicate with a
management point.

Central management of client data and client identity
The site database, rather than the individual client, retains important information about
each client's identity, and associates that data to a specific computer, or user.

     The client source files on a computer can be uninstalled and reinstalled without
     affecting the historical records for the computer where the client is installed.

     Failure of a client computer doesn't affect the integrity of the information that's
     stored in the database. This information can remain available for reporting.

Options for sites and site system roles that
aren't highly available
Several site systems don't support multiple instances at a site or in the hierarchy. This
information can help you prepare for these site systems going offline.

Asset intelligence synchronization point (hierarchy)

  ） Important

  Starting in November 2021, this feature of Configuration Manager is deprecated.
  For more information, see Asset intelligence deprecation.

This site system role isn't considered mission critical and provides optional functionality
in Configuration Manager. If this site system goes offline, use one of the following
options:

     Resolve the reason for the site system to be offline.

     Uninstall the role from the current server, and install the role on a new server.

Endpoint protection point (hierarchy)
This site system role isn't considered mission critical and provides optional functionality
in Configuration Manager. If this site system goes offline, use one of the following
options:

<!-- p.1218 -->

     Resolve the reason for the site system to be offline.

     Uninstall the role from the current server, and install the role on a new server.

Enrollment point (site)
This site system role isn't considered mission critical and provides optional functionality
in Configuration Manager. If this site system goes offline, use one of the following
options:

     Resolve the reason for the site system to be offline.

     Uninstall the role from the current server, and install the role on a new server.

Enrollment proxy point (site)
This site system role isn't considered mission critical and provides optional functionality
in Configuration Manager. However, you can install multiple instances of this site system
role at a site, and at multiple sites in the hierarchy. If this site system goes offline, use
one of the following options:

     Resolve the reason for the site system to be offline.

     Uninstall the role from the current server, and install the role on a new server.

When you have more than one enrollment proxy server in a site, use a DNS alias for the
server name. When you use this configuration, DNS round robin provides some fault
tolerance and load balancing for when users enroll their mobile devices.

Fallback status point (site or hierarchy)
This site system role isn't considered mission critical and provides optional functionality
in Configuration Manager. If this site system goes offline, use one of the following
options:

     Resolve the reason for the site system to be offline.

     Uninstall the role from the current server, and install the role on a new server.
     Because clients are assigned the fallback status point during client installation, you
     need to modify existing clients to use the new site system server.

Service connection point (hierarchy)

<!-- p.1219 -->

While this site system role is critical for keeping Configuration Manager current branch
up to date, it's generally not used frequently. If this system goes offline, use one of the
following options:

     Resolve the reason for the site system to be offline.

     Uninstall the role from the current server, and install the role on a new server.

See also
     Supported configurations

     Recommended hardware

     Supported operating systems for site system servers

     Site and site system prerequisites

     Site failure impacts

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1220 -->

Site server high availability in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Historically, you could add redundancy to most of the roles in Configuration Manager
by having multiple instances of these roles in your environment. Except for the site
server itself. High availability for the site server role is a Configuration Manager-based
solution to install another site server in passive mode. The central administration site
(CAS) and child primary sites can have another site server in passive mode. The site
server in passive mode can be on-premises or cloud-based in Azure.

This feature brings the following benefits

      Redundancy and high availability to the site server role
      More easily change the hardware or OS of the site server
      More easily move your site server to Azure IaaS

The site server in passive mode is in addition to your existing site server that is in active
mode. A site server in passive mode is available for immediate use, when needed.
Include this other site server as part of your overall design for making the Configuration
Manager service highly available.

A site server in passive mode:

      Uses the same site database as your site server in active mode.
      Doesn't write data to the site database when it's in passive mode.
      Uses the same content library as your site server in active mode.

To make the site server in passive mode become active, you manually promote it. This
action switches the site server in active mode to be the site server in passive mode. The
site system roles that are available on the original active mode server remain available
so long as that computer is accessible. Only the site server role is switched between
active and passive modes.

Microsoft Core Services Engineering and Operations used this feature to migrate their
CAS to Microsoft Azure. For more information, see the Microsoft IT Showcase article          .

Supported configurations

<!-- p.1221 -->

   Configuration Manager supports site servers in passive mode in a hierarchy. The
   CAS and child primary sites can have another site server in passive mode.

   The site server in passive mode can be on-premises or cloud-based in Azure.

     ７ Note

     A cloud-based site server in passive mode uses Azure infrastructure as a
     service (IaaS). For more information, see the following articles:
        Azure virtual machines (for cloud-based infrastructure)
        FAQ for Configuration Manager on Azure

Prerequisites

Active Directory
   Both site servers must be joined to the same Active Directory domain.

   If you've extended the Active Directory schema for Configuration Manager, both
   site servers need Full Control permissions to Active Directory's System - System
   Management container and all descendant objects.

General configurations for both site servers
   Both site servers can run different OS or service pack versions, as long as both are
   supported by Configuration Manager.

   Don't host the service connection point role on either site server configured for
   high availability. If it's currently on the original site server, remove it, and install it
   on another site system server. For more information, see About the service
   connection point.

Configurations for the site server in passive mode
   Must meet the prerequisites for installing a primary site.
      This requirement includes components like .NET Framework, Remote Differential
      Compression, and the Windows ADK. For the complete list, see Site and site
      system prerequisites.

     ７ Note

<!-- p.1222 -->

        Make sure to install the SQL Server Native Client. If you don't install it, the
        prerequisite checker during Configuration Manager setup will report an error
        about missing SQL Server permissions.

     Must have its computer account in the local Administrators group on the site
     server in active mode.

     Must install using source files that match the version of the site server in active
     mode.

     Can't have a site system role from any site installed on it before you install the site
     server in passive mode role.

     Make sure the computer account for the site server in passive mode has the same
     permissions as the site server in active mode. For example, it may need permission
     to content source files, such as boot image source directories.

Permissions for the site system installation account
By default, many customers use the site server's computer account to install new site
systems. The requirement is then to add the site server's computer account to the local
Administrators group on the remote site system. If your environment uses this
configuration, make sure to add the computer account of the new site server to this
local group on all remote site systems. For example, all remote distribution points.

The more secure and recommended configuration is to use a service account for
installing the site system. The most secure configuration is to use a local service account.
If your environment uses this configuration, no change is needed.

For more information, see Site system installation account and Elevated permissions.

Content library
The site content library must be on a remote network share. Both site servers need Full
Control permissions to the share and its contents. For more information, see Configure
a remote content library for the site server.

     The site server computer account needs Full control permissions to the network
     path to which you're moving the content library. This permission applies to both
     the share and the file system. No components are installed on the remote system.

     The site server can't have the distribution point role. The distribution point also
     uses the content library, and this role doesn't support a remote content library.

<!-- p.1223 -->

     After moving the content library, you can't add the distribution point role to the
     site server.

Site database
Both site servers must use the same site database.

     The database can be remote from each site server. The Configuration Manager
     setup process doesn't block installation of the site server role on a computer with
     the Windows role for Failover Clustering. SQL Server Always On availability groups
     require this role, so previously you couldn't colocate the site database on the site
     server. With this change, you can create a highly available site with fewer servers
     by using an availability group and a site server in passive mode. Only an active
     server can be installed to a node in an Always On availability group. Passive servers
     must be installed to standalone servers that do not have any existing site roles on
     them.

     The SQL Server that hosts the site database can use a default instance, named
     instance, failover cluster instance, or an availability group.

     Both site servers need the sysadmin security role on the instance of SQL Server
     that hosts the site database. The original site server should already have these
     roles, so add them for the new site server. For example, the following SQL script
     adds these roles for the new site server VM2 in the Contoso domain:

       SQL

       USE [master]
       GO
       CREATE LOGIN [contoso\vm2$] FROM WINDOWS WITH DEFAULT_DATABASE=
       [master], DEFAULT_LANGUAGE=[us_english]
       GO
       ALTER SERVER ROLE [sysadmin] ADD MEMBER [contoso\vm2$]
       GO

     Both site servers need access to the site database on the instance of SQL Server.
     The original site server should already have this access, so add it for the new site
     server. For example, the following SQL script adds a login to the CM_ABC database
     for the new site server VM2 in the Contoso domain:

       SQL

       USE [CM_ABC]
       GO
       CREATE USER [contoso\vm2$] FOR LOGIN [contoso\vm2$] WITH

<!-- p.1224 -->

    DEFAULT_SCHEMA=[dbo]
    GO

  The site server in passive mode is configured to use the same site database as the
  site server in active mode. The site server in passive mode only reads from the
  database. It doesn't write to the database until after it's promoted to active mode.

Limitations
  Only a single site server in passive mode is supported at each site.

  Passive site servers cannot be installed to nodes in the Always On availability group
  hosting the Configuration Manager database and must be installed on standalone
  servers. Moving a passive site server into the Always On availability group after
  installation is not currently supported.

  A site server in passive mode isn't supported at a secondary site.

    ７ Note

    Secondary sites are still supported under a primary site with highly available
    site servers.

  Promotion of the site server in passive mode to active mode is manual. There's no
  automatic failover.

  Site system roles can't be installed on the new server before you add the site
  server in passive mode.

    ７ Note

    After it installs the site server in passive mode, you can add additional roles as
    necessary. For example, a management point at a primary site.

  For roles like the reporting point that use a database, host the database on a
  server that's remote from both site servers.

  The Configuration Manager console doesn't automatically install on the site server
  in passive mode.

Add a site server in passive mode

<!-- p.1225 -->

For more information on the general process of adding roles, see Install site system
roles.

   1. In the Configuration Manager console, go to the Administration workspace,
         expand Site Configuration, select the Sites node, and select Create Site System
         Server in the ribbon.

   2. On the General page of the Create Site System Server Wizard, specify the server to
         host the site server in passive mode. The server you specify can't host any site
         system roles before installing a site server in passive mode.

   3. On the System Role Selection page, select only Site server in passive mode.

           ７ Note

           The wizard performs the following initial prerequisite checks on this page:

                 The selected server isn't a secondary site server
                 The selected server isn't already a site server in passive mode
                 The site's content library is in a remote location

           If these initial prerequisite checks fails, you can't continue past this page of
           the wizard.

   4. On the Site Server In Passive Mode page, provide the following information that's
         used to run setup and install the site server role on the specified server:

              Choose one of the following options:

                 Copy installation source files over the network from the site server in
                 active mode: This option creates a compressed package and sends it to
                 the new site server.

                 Use the source files at the following location on the site server in passive
                 mode: For example, a local path to which you already copied the source
                 files. Make sure this content is the same version as the site server in active
                 mode.

                 (Recommended) Use the source files at the following network location:
                 Specify the path directly to the contents of the CD.Latest folder from the
                 site server in active mode. For example, \\Server\SMS_ABC\CD.Latest
                 where "Server" is the name of the site server in active mode, and "ABC" is
                 the site code.

<!-- p.1226 -->

           Specify the local path at which to install Configuration Manager on the new
           site server. For example: C:\Program Files\Configuration Manager

   5. Complete the wizard. Configuration Manager then installs the site server in passive
     mode on the specified server.

For detailed installation status, in the console go to the Monitoring workspace, and
select the Site Server Status node. The state for the site server in passive mode displays
as Installing. For more detailed information, select the server and select Show Status.
This action opens the Site Server Installation Status window. When the process is
complete, the state shows OK for both servers.

For more information on the setup process, see Flowchart - Set up a site server in
passive mode.

After you add a site server in passive mode, see both site servers on the Nodes tab in
the Sites node of the console.

All Configuration Manager site server components are in standby on the site server in
passive mode. The Windows services are still running.

Site server promotion
Similarly as with backup and recovery, plan and practice your process to change site
servers. Consider the following points in your promotion plan:

     Practice a planned promotion, where both site servers are online. Also practice an
     unplanned failover, by forcibly disconnecting or shutting down the site server in
     active mode.

     Determine your operational processes during failover, and what to communicate
     with other Configuration Manager administrators.

     Before a planned promotion:

        Check the overall status of the site and site components. Make sure everything
        is healthy as normal for your environment.

        Check content status for any packages actively replicating between sites.

        Check secondary site status and site replication.

        Don't start any new content distribution jobs or maintenance on child or
        secondary site servers.

<!-- p.1227 -->

          ７ Note

          If file or database replication between sites is in progress during failover,
          the new site server may not receive the replicated content. If this happens,
          redistribute the software content after the new site server is active. For
          database replication, you may need to reinitialize a secondary site after
          failover.

        Reduce or remove other scheduled activities at the same time. For example,
        don't plan to promote a site server immediately after updating the site to a new
        version. Site update includes other tasks that can potentially conflict with the
        site server promotion.

           Tip

          Here's an example of how other activities can conflict with site server
          promotion:
             Monday: Update the site to the latest version. Enable automatic client
             upgrade with client piloting.
             Tuesday: Promote the site server in passive mode to be the active site
             server.

          By Wednesday or Thursday, this action may cause all clients to upgrade,
          not just the pilot collection. This behavior can cause significant network
          usage and unexpected load on the distribution points.

        If you enable the pre-production client, review the known issue with site server
        high availability. For more information, see Pre-production client and site server
        high availability.

Process to promote the site server in passive mode to
active mode
This section describes how to change the site server in passive mode to active mode. To
access the site and make this change, you need to be able to access an instance of the
SMS Provider. For more information, see Use multiple SMS Providers.

  ） Important

<!-- p.1228 -->

  If all instances of the SMS Provider are offline, you can't connect to the site as no
  provider is available. When you add the site server in passive mode, setup installs
  an instance of the SMS Provider on this server.

  The Configuration Manager console requests the list of available SMS Providers
  from WMI on the site server. When you install multiple SMS Providers at a site, the
  site randomly assigns each new connection request to use an installed SMS
  Provider. You can't specify the SMS Provider location to use with a specific
  connection session. If your console is unable to connect to the site because the
  current site server is offline, specify the other site server in the Site Connection
  window.

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node. Select the site, and then
     switch to the Nodes tab. Select the site server in passive mode, and then select
     Promote to active in the ribbon. Select Yes to confirm and continue.

   2. Refresh the console node. The Status column for the server you're promoting
     displays in the Nodes tab as Promoting.

   3. After the promotion is complete, the Status column shows OK for both the new
     site server in active mode, and for the new site server in passive mode. The Server
     Name column for the site now displays the name of the new site server in active
     mode.

For detailed status, go to the Monitoring workspace, and select the Site Server Status
node. The Mode column identifies which server is Active or Passive. When you promote
a server from passive mode to active mode, select the site server that you're promoting
to active, and then choose Show Status from the ribbon. This action opens the Site
Server Promotion Status window that displays more details about the process.

When a site server in active mode switches over to passive mode, only the site system
role is made passive. All other site system roles that are installed on that computer
remain active and accessible to clients.

For more information on the planned promotion process, see Flowchart - Promote site
server (planned).

Unplanned failover
If the current site server in active mode is offline, the site server for promotion tries to
contact the current site server in active mode for 30 minutes. If the offline server comes

<!-- p.1229 -->

back before this time, it's successfully notified, and the change proceeds gracefully.
Otherwise the site server for promotion forcibly updates the site configuration for it to
be active. If the offline server comes back after this time, it first checks the current state
in the site database. It then proceeds with demoting itself to the site server in passive
mode.

During this 30-minute waiting period, the site has no site server in active mode. Clients
still communicate with client-facing roles such as management points, software update
points, and distribution points. Users can install software that's already deployed. No
site administration is possible in this time period. For more information, see Site failure
impacts.

If the offline server is damaged such that it can't return, delete this site server from the
console. Then create a new site server in passive mode to restore a highly available
service.

For more information on the unplanned failover process, see Flowchart - Promote site
server (unplanned).

Other tasks after site server promotion
After switching site servers, you don't have to do most of the other tasks as are
necessary when recovering a site. For example, you don't need to reset passwords or
reconnect your Microsoft Intune subscription.

The following steps may be required if necessary in your environment:

     If you import PKI certificates for distribution points, reimport the certificate for
     affected servers. For more information, see Regenerate the certificates for
     distribution points.

     If you integrate Configuration Manager with the Microsoft Store for Business,
     reconfigure that connection. For more information, see Manage apps from the
     Microsoft Store for Business.

     Recreate OSD bootable media and prestaged media in non-PKI environments.

     In non-PKI environments, you may need to update the self-signed certificate on
     PXE-enabled distribution points. Do this action in the properties of the distribution
     point on the Communication tab. Make changes to the self-signed certificate date
     or time.

Daily monitoring

<!-- p.1230 -->

When you have a site server in passive mode, monitor it daily. Make sure its Status
remains OK and is ready for use. In the Configuration Manager console, go to the
Monitoring workspace, and select the Site Server Status node. View both site servers
and their current status. Also view status in the Administration workspace. Expand Site
Configuration, and select the Sites node. Select the site, and then switch to the Nodes
tab.

  ７ Note

  When you update the site to a new version of Configuration Manager, it also
  updates the site server in passive mode.

Remove a site server in passive mode
The process to remove a site server in passive mode is the same as any site system role.
Remove the Site server role from the server in passive mode. For more information, see
Procedure to remove a site system role.

When you remove any other site system role, the site component manager ( sitecomp )
processes the request. When you remove a site server in passive mode, the failover
manager processes the request. For status, monitor the SMS_FAILOVER_MANAGER
component.

Next steps
Flowchart - Set up a site server in passive mode Flowchart - Promote site server
(planned) Flowchart - Promote site server (unplanned)

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1231 -->

Flowchart - Set up a site server in
passive mode
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This flowchart diagram shows the process by which the site sets up a site server in
passive mode. For more information, see the following articles:

      Site server high availability
      Flowchart - Promote site server (planned)
      The content library
      Flowchart - Manage content library

<!-- p.1232 -->

<!-- p.1233 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1234 -->

Flowchart - Promote site server
(planned)
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This flowchart diagram shows the process by which a site server in passive mode is
promoted to the site server in active mode. In this example, the administrator plans for
the promotion process. Both servers are online and fully functional. For more
information, see the following articles:

      Site server high availability
      Flowchart - Set up a site server in passive mode

<!-- p.1235 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1236 -->

Flowchart - Promote site server
(unplanned)
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This flowchart diagram shows the process by which a site server in passive mode is
promoted to the site server in active mode when the current site server in active mode is
offline. In this example, the current site server in active mode isn't fully operational, for
example it is disconnected from the network or powered off. For more information, see
the following articles:

      Site server high availability
      Flowchart - Promote site server (planned)
      Flowchart - Set up a site server in passive mode

<!-- p.1237 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1238 -->

Prepare to use a SQL Server Always On
availability group with Configuration
Manager
06/12/2025

Applies to: Configuration Manager (current branch)

Use this article to prepare Configuration Manager to use a SQL Server Always On availability
group for the site database. This feature provides a high availability and disaster recovery
solution.

Configuration Manager supports using availability groups:

     At primary sites and the central administration site.
     On-premises, or in Microsoft Azure.

When you use availability groups in Microsoft Azure, you can further increase availability of
your site database by using Azure availability sets. For more information on Azure availability
sets, see Manage the availability of virtual machines.

  ） Important

  Before you continue, be comfortable with configuring SQL Server and availability groups.
  This article references the SQL Server documentation library with more information and
  procedures.

Supported scenarios
The following scenarios are supported for using availability groups with Configuration
Manager. For more information and procedures for each scenario, see Configure availability
groups for Configuration Manager.

     Create an availability group for use with Configuration Manager
     Configure a site to use the availability group
     Add or remove synchronous replica members from an availability group that hosts a site
     database
     Configure or recover a site from an asynchronous commit replicas
     Move a site database out of an availability group to a default or named instance of a
     standalone SQL Server

<!-- p.1239 -->

Prerequisites
The following prerequisites apply to all scenarios. If additional prerequisites apply to a specific
scenario, they're detailed with that scenario.

Configuration Manager accounts and permissions

Installation account
The account you use to run Configuration Manager setup must be:

     A member of the local Administrators group on each computer that's a member of the
     availability group.
     A sysadmin on each instance of SQL Server that hosts the site database.

Site server to replica member access

The computer account of the site server must be a member of the local Administrators group
on each computer that's a member of the availability group.

SQL Server

Version

Each replica in the availability group must run a version of SQL Server that's supported by your
version of Configuration Manager. When supported by SQL Server, different nodes of an
availability group can run different versions of SQL Server. For more information, see
Supported SQL Server versions for Configuration Manager.

Edition
Use an Enterprise edition of SQL Server.

Account
Each instance of SQL Server can run under a domain user account (service account) or a non-
domain account. Each replica in a group can have a different configuration.

     Use an account with the lowest possible permissions. For more information, see Security
     considerations for a SQL Server installation.

<!-- p.1240 -->

     For more information on configuring service accounts and permissions for SQL Server,
     see Configure Windows service accounts and permissions.

     To use a non-domain account, you must use certificates. For more information, see Use
     certificates for a database mirroring endpoint (Transact-SQL).

     For more general information, see Create a database mirroring endpoint for availability
     groups.

Database

Configure the database on a new replica

Only make these configurations on a primary replica. To configure a secondary replica, first fail
over the primary to the secondary. This action makes the secondary the new primary replica.

Configure the database of each replica with the following settings:

     Enable CLR Integration:

        SQL

        sp_configure 'show advanced options', 1;
        GO
        RECONFIGURE;
        GO
        sp_configure 'clr enabled', 1;
        GO
        RECONFIGURE;
        GO

     For more information, see CLR integration.

     Set Max text repl size to 2147483647 :

        SQL

        EXECUTE sp_configure 'max text repl size (B)', 2147483647

     Set the database owner to the SA account. You don't need to enable this account.

     Turn ON the TRUSTWORTHY setting:

        SQL
