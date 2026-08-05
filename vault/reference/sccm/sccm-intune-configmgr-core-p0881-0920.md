---
title: "Core infrastructure documentation — pages 881-920"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0881-0920
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0881-0920
family: sccm
documentKind: "doc"
abstract: "Setup was unable to verify remote IIS settings. IIS common components aren't installed on the site server. Case-insensitive collation on SQL Server Applies to: Site database server The SQL Server installation uses a case-insensitive collation, such as SQL_Latin1_General_CP1_CI_A"
---

# Core infrastructure documentation — pages 881-920

<!-- p.881 -->

     Setup was unable to verify remote IIS settings. IIS common components aren't
     installed on the site server.

Case-insensitive collation on SQL Server
Applies to: Site database server

The SQL Server installation uses a case-insensitive collation, such as
SQL_Latin1_General_CP1_CI_AS.

Central administration site server administrative rights on
expand primary site
Applies to: Central administration site

When you expand a primary site to a hierarchy, the computer account of the central
administration site server has Administrator rights on the standalone primary site
server.

Check for a cloud management gateway (CMG) as a cloud
service (classic)
Applies to: Central administration site, primary site

Starting in version 2403, this error displays if you have a cloud management gateway
(CMG) deployed with the classic cloud service. The option to deploy a CMG as a cloud
service (classic) is deprecated. All CMG deployments should use a virtual machine scale
set. If you have a CMG deployed with the classic cloud service, you can convert it to a
virtual machine scale set deployment before upgrade. For more information, see
Convert a CMG to a virtual machine scale set.

Client version on management point computer
Applies to: Management point

You're installing the management point on a server that doesn't have a different version
of the Configuration Manager client installed.

Cloud management gateway on the expanded primary
site

<!-- p.882 -->

Applies to: Central administration site

When you expand a primary site to a hierarchy, the cloud management gateway (CMG)
role isn't installed on the standalone primary site.

Connection to SQL Server on central administration site
Applies to: Primary site

The user account that runs Configuration Manager setup on the primary site to join an
existing hierarchy has the sysadmin role on the SQL Server instance for the central
administration site.

Custom client agent settings have NAP enabled
Applies to: Central administration site, primary site

There are no custom client settings that enable network access protection (NAP).

Data warehouse service point on the expanded primary
site
Applies to: Central administration site

When you expand a primary site to a hierarchy, the data warehouse service point role
isn't installed on the standalone primary site.

Dedicated SQL Server instance
Applies to: Central administration site, primary site, secondary site

You configured a dedicated instance of SQL Server to host the Configuration Manager
site database.

If another site uses the instance, you must select a different instance for the new site.
You can also uninstall the other site, or move its database to a different instance for the
SQL Server.

Default client agent settings have NAP enabled
Applies to: Central administration site, primary site

The default client settings don't enable network access protection (NAP).

<!-- p.883 -->

Domain membership (error)
Applies to: Central administration site, primary site, secondary site, SMS Provider, SQL
Server

The Configuration Manager computer is a member of a Windows domain.

Endpoint Protection point on the expanded primary site
Applies to: Central administration site

When you expand a primary site to a hierarchy, the Endpoint Protection point role isn't
installed on the standalone primary site.

Existing Configuration Manager server components on
server
Applies to: Central administration site, primary site, secondary site

A site server or site system role isn't already installed on the server selected for site
installation.

Existing stand-alone primary site for version and site
code
Applies to: Central administration site, primary site

The primary site you plan to expand is a standalone primary site. It has the same version
of Configuration Manager, but a different site code than the central administration site
to be installed.

Enable site system roles for HTTPS or Enhanced HTTP
Applies to: central administration site, primary site

Starting in version 2403, if your site is configured to allow HTTP communication without
enhanced HTTP, you'll see this error. To improve the security of client communications,
in the future Configuration Manager will require HTTPS communication or enhanced
HTTP.

This check looks at the following settings:

<!-- p.884 -->

   1. In the Configuration Manager console, go to the Administration workspace,
        expand Site Configuration, and select the Sites node.

   2. Select a site, and then in the ribbon select Properties.

   3. Switch to the Communication Security tab.

        Configure one of the following options:

             HTTPS only: This site setting requires that all site systems that use IIS use
             HTTPS. These site systems need a server authentication certificate, and clients
             need a client authentication certificate. For more information, see Plan a
             transition strategy for PKI certificates.

             HTTPS or EHTTP and Use Configuration Manager-generated certificates for
             EHTTP site systems: This combination of settings enables Enhanced HTTP.

  ７ Note

  If you see this error when updating the central administration site, it may be
  because of a child primary site.

Firewall exception for SQL Server
Applies to: Central administration site, primary site, secondary site, management point

The Windows Firewall is disabled or a relevant Windows Firewall exception exists for SQL
Server.

Allow Sqlservr.exe or the required TCP ports to be accessed remotely. By default, SQL
Server listens on TCP port 1433, and the SQL Server Service Broker (SSB) uses TCP port
4022.

Free disk space on site server
Applies to: Central administration site, primary site, secondary site

To install the site server, it must have at least 15 GB of free disk space. If you install the
SMS Provider on the same server, it needs an additional 1 GB of free space.

IIS service running
Applies to: Management point, distribution point

<!-- p.885 -->

IIS is installed and running on the server for the management point or distribution point.

Incompatible collection references
Applies to: Central administration site

During an upgrade, collections reference only other collections of the same type.

Match collation of expand primary site
Applies to: Central administration site

When you expand a primary site to a hierarchy, the site database for the standalone
primary site has the same collation as the site database at the central administration
site.

Maximum text replication size for SQL Server Always On
availability groups
Applies to: Site database server

When using an availability group, the max text repl size setting must be properly
configured. For more information, see Prepare to use an availability group.

Microsoft Intune Connector on the expanded primary site
Applies to: Central administration site

When you expand a primary site to a hierarchy, the Microsoft Intune Connector role isn't
installed on the standalone primary site.

Microsoft Remote Differential Compression (RDC) library
registered
Applies to: Central administration site, primary site, secondary site

The RDC library is registered on the Configuration Manager site server.

Microsoft Windows Installer
Applies to: Central administration site, primary site, secondary site

<!-- p.886 -->

Verifies the Windows Installer version.

When this check fails, setup wasn't able to verify the version, or the installed version
doesn't meet the minimum requirement of Windows Installer 4.5.

Microsoft Store for Business deprecation alert
Applies to: Central administration site, primary site

Starting in 2211, if you have a Microsoft Store for Business Connector configured, you
will see this warning while performing the upgrade. This is in conjunction with the
deprecation announcement made here.

Minimum .NET Framework version for Configuration
Manager console
Applies to: Configuration Manager console

Microsoft .NET Framework 4.0 is installed on the Configuration Manager console
computer.

Minimum .NET Framework version for Configuration
Manager site server
Applies to: Central administration site, primary site, secondary site

.NET Framework 3.5 is installed or enabled on the Configuration Manager site server.

Minimum .NET Framework version for SQL Server Express
edition installation for Configuration Manager secondary
site
Applies to: Secondary site

.NET Framework 4.0 is installed or enabled on the Configuration Manager secondary site
server. This version is required by SQL Server Express.

ODBC driver for SQL Server
Applies to: new site or when updating an existing one

<!-- p.887 -->

Configuration Manager requires the installation of the ODBC driver for SQL server as a
prerequisite.

Parent database collation
Applies to: Primary site, secondary site

The collation of the site database matches the collation of the parent site's database. All
sites in a hierarchy must use the same database collation.

Parent site replication status
Applies to: Central administration site, primary site

The replication status of the parent site is Replication active (state 125).

Pending system restart
Applies to: Central administration site, primary site, secondary site

Before you run setup, another program requires the server to be restarted.

To see if the computer is in a pending restart state, it checks the following registry
locations:

      HKLM:Software\Microsoft\Windows\CurrentVersion\Component Based
     Servicing\RebootPending

      HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto

     Update\RebootRequired

      HKLM:SYSTEM\CurrentControlSet\Control\Session Manager,

     PendingFileRenameOperations

      HKLM:Software\Microsoft\ServerManager, CurrentRebootAttempts

Primary FQDN
Applies to: Central administration site, primary site, secondary site, site database server

The NetBIOS name of the computer matches the local hostname in the fully qualified
domain name (FQDN).

<!-- p.888 -->

Read-only domain controller
Applies to: Central administration site, primary site, secondary site

Site database servers and secondary site servers aren't supported on a read-only
domain controller (RODC).

For more information, see Installing SQL Server on a domain controller.

Resource access policies are no longer supported
Applies to: CAS, primary site

Starting in version 2403, resource access policies workspace is removed and is no longer
supported. The co-management resource access workload is defaulted to Intune.

Remove the certificate registration point site system role and all policies for company
resource access features:

     Certificate profiles
     VPN profiles
     Wi-Fi profiles
     Windows Hello for Business settings
     Email profiles
     The co-management resource access workload

For more information, see Frequently asked questions about resource access
deprecation.

For more information on removing the certificate registration point role, see Remove a
site system role.

Required SQL Server collation
Applies to: Central administration site, primary site, secondary site

The instance for SQL Server is configured to use the SQL_Latin1_General_CP1_CI_AS
collation.

If the Configuration Manager site database is already installed, this check also applies to
the database. For information about changing your SQL Server instance and database
collations, see SQL Server collation and unicode support.

<!-- p.889 -->

If you're using a Chinese OS and require GB18030 support, this check doesn't apply. For
more information about enabling GB18030 support, see International support.

Required version of Microsoft .NET Framework (error)
Applies to: CAS, primary site, secondary site

This rule checks if the .NET Framework is at least version 4.6.2. You'll see this error if the
system has less than version 4.6.2.

Starting in version 2111, Configuration Manager requires Microsoft .NET Framework
version 4.6.2 for site servers, specific site systems, clients, and the console. If possible in
your environment, .NET version 4.8 is recommended. A later version of Configuration
Manager will require .NET version 4.8. Before you run setup to install or update the site,
first update .NET and restart the system. For more information, Site and site system
prerequisites.

  ７ Note

  Third-party add-ons that use Microsoft .NET Framework and rely on Configuration
  Manager libraries also need to use .NET 4.6.2 or later. For more information, see
  External dependencies require .NET 4.6.2.

  To determine the systems that need to be updated, review the
  ConfigMgrPrereq.log found on the system drive of the computer.

  ） Important

  If you're upgrading from System Center 2012 Configuration Manager R2 Service
  Pack 1, you need to manually verify that remote site systems have at least .NET
  version 4.6.2. Configuration Manager current branch setup skips the check in this
  scenario.

Server service is running
Applies to: Central administration site, primary site, secondary site

The Server service is started and running.

Setup source folder

<!-- p.890 -->

Applies to: Secondary site

The computer account for the secondary site has the following permissions to the setup
source folder and share:

     Read NTFS file system permissions

     Read share permissions

  ７ Note

  If you use administrative shares, for example, C$ and D$, the secondary site
  computer account must be an Administrator on the server.

Setup source version
Applies to: Secondary site

The Configuration Manager version in the specified source folder for the secondary site
installation matches the Configuration Manager version of the primary site.

Site code in use
Applies to: Primary site

The specified site code isn't already in use in the Configuration Manager hierarchy.
Specify a unique site code for this site.

Site server computer account administrative rights
Applies to: Primary site, site database server

The site server computer account has Administrator rights on the SQL Server and
management point.

Site server FQDN length
Applies to: Central administration site, primary site, secondary site

The length of the FQDN of the site server.

Site server in passive mode on the expanded primary site

<!-- p.891 -->

Applies to: Central administration site

When you expand a primary site to a hierarchy, the site server in passive mode role isn't
installed on the standalone primary site.

SMS Provider in same domain as site server
Applies to: SMS Provider

Any instance of the SMS Provider is in the same domain as the site server.

Software update point in NLB configuration
Applies to: Software update point

The site isn't using network load balancing (NLB) with any virtual locations for active
software update points.

Software update point using a load balancer
Applies to: Software update point

Configuration Manager doesn't support software update points on network (NLB) or
hardware load balancers (HLB).

SQL ODBC driver for SQL Server
Applies to: Central administration site, primary site, secondary site

Configuration Manager requires the installation of the ODBC driver for SQL server as a
prerequisite. This prerequisite is required when you create a new site or update an
existing one.

SQL Server Always On availability groups
Applies to: Site database server

When using an availability group, the server must meet the minimum requirements. For
more information, see Prepare to use an availability group.

SQL Server Always On availability group configured for
readable secondaries

<!-- p.892 -->

Applies to: Site database server

When using an availability group, check the secondary read state of the replicas.

SQL Server Always On availability group configured for
manual failover
Applies to: Site database server

When using an availability group, configure the replicas for manual failover.

SQL Server Always On availability group replicas on
default instance
Applies to: Site database server

When using an availability group, replicas are on the default instance.

SQL Server Always On availability group replicas must all
have the same seeding mode
Applies to: Site database server

When using an availability group, you need to configure replicas with the same seeding
mode.

SQL Server Always On availability group replicas must be
healthy
Applies to: Site database server

When using an availability group, replicas are in a healthy state.

SQL Server configuration for site upgrade
Applies to: Site database server

The SQL Server meets the minimum requirements for site upgrade. For more
information, see Supported SQL Server versions.

SQL Server edition

<!-- p.893 -->

Applies to: Site database server

SQL Server at the site isn't SQL Server Express.

SQL Server Express database size on secondary site
Applies to: Secondary site

Starting in version 2107, this check will fail if the amount of replicated data from the
primary site will exceed the 10-GB size limit of SQL Server Express. For more
information, see Configuration Manager site sizing and performance FAQ.

SQL Server Express on secondary site
Applies to: Secondary site

SQL Server Express can successfully install on the secondary site server.

SQL Server on the secondary site server
Applies to: Secondary site

SQL Server is installed on the secondary site server. You can't install SQL Server on a
remote site system for a secondary site.

  ２ Warning

  This check only applies when you select to have setup use an existing instance of
  SQL Server.

SQL Server service running account
Applies to: Central administration site, primary site, secondary site

The sign-in account for the SQL Server service isn't a local user account or LOCAL
SERVICE.

Configure the SQL Server service to use a valid domain account, NETWORK SERVICE, or
LOCAL SYSTEM.

SQL Server site database consistency

<!-- p.894 -->

Applies to: Site database server

Verify database consistency.

SQL Server sysadmin rights
Applies to: Site database server

The user account that runs Configuration Manager setup has the sysadmin role on the
SQL Server instance that you selected for site database installation. This check also fails
when setup is unable to access the instance for the SQL Server to verify permissions.

SQL Server sysadmin rights for reference site
Applies to: Site database server

The user account that runs Configuration Manager setup has the sysadmin role on the
SQL Server role instance that you selected as the reference site database. SQL Server
sysadmin role permissions are required to modify the site database.

SQL Server TCP port
Applies to: Site database server

TCP is enabled for the SQL Server instance, and is set to use a static port.

SQL Server version
Applies to: Site database server

A supported version of SQL Server is installed on the specified site database server.

For more information, see Support for SQL Server versions.

Unsupported OS for Configuration Manager console
Applies to: Configuration Manager console

Install the Configuration Manager console on computers that run a supported OS
version.

For more information, see the Supported OS versions for the Configuration Manager
console.

<!-- p.895 -->

Unsupported OS for site server
Applies to: Central administration site, primary site, secondary site, Configuration
Manager console, management point, distribution point

The server runs a supported OS version.

For more information, see Supported OS versions for Configuration Manager site system
servers.

Unsupported site system role: out of band service point
Applies to: Primary site

The out of band service point site system role isn't installed.

Unsupported site system role: system health validation
point
Applies to: Primary site

The system health validation point site system role isn't installed.

Unsupported upgrade path
Applies to: Central administration site, primary site

All site servers in the hierarchy meet the Configuration Manager minimum version that's
required for upgrade.

USMT installed
Applies to: Central administration site, primary site (standalone only)

The User State Migration Tool (USMT) component of the Windows Assessment and
Deployment Kit (ADK) for Windows is installed.

Validate FQDN of SQL Server
Applies to: Site database server

You specified a valid FQDN for the SQL Server computer.

<!-- p.896 -->

Verify central administration site version
Applies to: Primary site

The central administration site has the same version of Configuration Manager.

Verify database consistency
Applies to: Central administration site, primary site

Verifies consistency of the site database in SQL Server.

Windows Deployment Tools installed
Applies to: SMS Provider

The Windows Deployment Tools component of the Windows ADK is installed.

Windows Failover Cluster
Applies to: Site server, management point, distribution point

Server with the site server, management point, or distribution point roles aren't part of a
Windows Cluster.

The Configuration Manager setup process doesn't block installation of the site server
role on a computer with the Windows role for Failover Clustering. SQL Server Always On
availability groups require this role, so previously you couldn't colocate the site database
on the site server. With this change, you can create a highly available site with fewer
servers by using an availability group and a site server in passive mode. For more
information, see High availability options.

Windows PE installed
Applies to: SMS Provider

The Windows Preinstallation Environment (PE) component of the Windows ADK is
installed.

Windows Server 2012/R2 lifecycle
Applies to: Central administration site, primary site, secondary site

<!-- p.897 -->

Starting in version 2403, this error displays if you have site systems running a version of
Windows Server that is out of support. The support lifecycle for Windows Server 2012
and Windows Server 2012 R2 ended on October 10, 2023. Plan to upgrade the OS on
your site servers. For more information, see the following blog post: Know your options
for SQL Server 2012 and Windows Server 2012 end of support         .

Warnings

Active Directory domain functional level
Applies to: Central administration site, primary site

The Active Directory domain and forest functional level is a minimum of Windows Server
2008 R2. For more information, see Support for Active Directory domains.

Administrative rights on distribution point
Applies to: Distribution point

The user account running setup has Administrator rights on the distribution point.

Administrative rights on management point
Applies to: Management point, distribution point

The computer account of the site server has Administrator rights on the management
point and distribution point.

Administrative share (site system)
Applies to: Management point

The required administrative shares are present on the site system computer.

Application compatibility
Applies to: Central administration site, primary site

Current applications are compliant with the application schema.

Backlogged inboxes

<!-- p.898 -->

Applies to: Central administration site, primary site

The site server is processing critical inboxes in a timely fashion. Inboxes don't contain
files older than one day.

It checks the following inbox folders:

      despoolr.box\receive\*.i??

      despoolr.box\receive\*.s??

      despoolr.box\receive\*.nil

      schedule.box\requests\*.sr?

To resolve this warning, check whether the despooler and scheduler site system
components are running.

BITS installed
Applies to: Management point

The Background Intelligent Transfer Service (BITS) is installed and enabled in IIS.

Check for site system roles associated with deprecated or
removed features
Applies to: Central administration site, primary site

Starting in version 2203, this warning appears if there are site system roles installed for
deprecated features that will be removed in a future release. Remove the following site
system roles:

     Enrollment point
     Enrollment point proxy

For more information, see Remove a site system role.

The device management point is also deprecated. It's a management point that you
allow for mobile and macOS devices. You can entirely remove the role, or you can
reconfigure the management point. On the properties of the management point site
system role, disable the option to Allow mobile devices and Mac Computer to use this
management point, This option effectively turns the device management point into a

<!-- p.899 -->

regular management point. For more information, see Configure roles for on-premises
MDM.

Check if the site uses Microsoft Operations Management
Suite (OMS) Connector
Applies to: Central administration site, primary site

Starting in version 2103, this check warns about the presence of the Log Analytics
connector for Azure Monitor. (This feature is called the OMS Connector in the Azure
Services wizard.)

Check if the site uses Upgrade Readiness cloud service
connector
Applies to: Central administration site, primary site

The Upgrade Readiness service is retired as of January 31, 2020. For more information,
see Windows Analytics retirement on January 31, 2020.

If your Configuration Manager site had a connection to Upgrade Readiness, you need to
remove it and reconfigure clients. For more information, see Remove Upgrade Readiness
connection.

If you ignore this prerequisite warning, Configuration Manager setup automatically
removes the Upgrade Readiness connector.

Check if the site uses the asset intelligence
synchronization point role
Applies to: Central administration site, primary site

Starting in version 2203, this warning displays if you have the asset intelligence
synchronization point site system role. The asset intelligence feature is deprecated and
will be removed in a future release. Remove the asset intelligence synchronization point
role. For more information, see Remove a site system role.

Cloud management gateway requires either token-based
authentication or an HTTPS management point
Applies to: Cloud management gateway

<!-- p.900 -->

With some versions of Configuration Manager, you can't use an HTTP management
point with the cloud management gateway (CMG). Either configure the CMG for HTTPS,
or configure the site for enhanced HTTP. For more information, see Overview of cloud
management gateway.

Configuration for SQL Server memory usage
Applies to: Site database server

SQL Server is configured for unlimited memory use. Configure SQL Server memory to
have a maximum limit.

Distribution point package version
Applies to: Distribution points

All distribution points in the site have the latest version of software distribution
packages.

Domain membership (warning)
Applies to: Management point, distribution point

The Configuration Manager computer is a member of a Windows domain.

Desktop Analytics is being retired
Desktop Analytics will be retired on November 30, 2022. Check out the new reports in
the Microsoft Intune admin center. For more information see:
https://go.microsoft.com/fwlink/?linkid=2186861       .

Firewall exception for SQL Server (standalone primary
site)
Applies to: Primary site (standalone only)

The Windows Firewall is disabled, or a relevant Windows Firewall exception exists for
SQL Server.

Allow Sqlservr.exe or the required TCP ports to be accessed remotely. By default, SQL
Server listens on TCP port 1433, and the Server Service Broker (SSB) uses TCP port 4022.

<!-- p.901 -->

Firewall exception for SQL Server for management point
Applies to: Management point

The Windows Firewall is disabled, or a relevant Windows Firewall exception exists for
SQL Server.

IIS HTTPS configuration
Applies to: Management point, distribution point

IIS website has bindings for the HTTPS communication protocol.

When you install site roles that require HTTPS, configure IIS site bindings on the
specified server with a valid public key infrastructure (PKI) certificate.

Invalid discovery records
Applies to: central administration site

There are discovery records that are no longer valid. These records will be marked for
deletion.

Network Access Account (NAA) account usage alert
Applies to: central administration site, Primary site

If your site is configured with NAA account, you'll see this warning. To improve the
security of distribution points configured with NAA account, review the existing
accounts and their relevant permissions. If it has more than minimal required
permission, then remove and add a minimal permission account. Don't configure any
administrator level permission accounts on the NAA. If the site server is configured with
HTTPS / EHTTP, it recommended removing NAA account, which is unused.

For more information, see the description of this permissions-for-the-network-access-
account.

Network access protection (NAP) is no longer supported
Applies to: Primary site

There are no software updates that are enabled for NAP.

<!-- p.902 -->

NTFS drive on site server
Applies to: Primary site

The disk drive is formatted with the NTFS file system. For better security, install site
server components on disk drives formatted with the NTFS file system.

Pending configuration item policy updates
Applies to: Primary site

You may see this warning if you have many application deployments and at least one of
them requires approval.

You have two options:

     Ignore the warning and continue with the update. This action causes higher
     processing on the site server during the update as it processes the policies. You
     may also see more processor load on the management point after the update.

     Revise one of the applications that has no requirements or a specific OS
     requirement. Pre-process some of the load on the site server at that time. Review
     objreplmgr.log, and then monitor the processor on the management point. After
     the processing is complete, update the site. There will still be some additional
     processing after the update, but less than if you ignore the warning with the first
     option.

Pending system restart on the remote SQL Server
Applies to: remote SQL Server

Before you run setup, another program requires the server to be restarted.

To see if the computer is in a pending restart state, it checks the following registry
locations:

      HKLM:Software\Microsoft\Windows\CurrentVersion\Component Based

     Servicing\RebootPending

      HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto

     Update\RebootRequired

      HKLM:SYSTEM\CurrentControlSet\Control\Session Manager,
     PendingFileRenameOperations

<!-- p.903 -->

      HKLM:Software\Microsoft\ServerManager, CurrentRebootAttempts

PowerShell 2.0 on site server
Applies to: Primary site with Exchange connector

Windows PowerShell 2.0 or a later version is installed on the site server for the
Configuration Manager Exchange Connector.

Recommended version of Microsoft .NET Framework
Applies to: CAS, primary site, secondary site

This rule checks if the .NET Framework is at least version 4.8. You'll see this warning if
the system has at least version 4.6.2, but less than version 4.8.

Starting in version 2107, Configuration Manager requires Microsoft .NET Framework
version 4.6.2 for site servers, specific site systems, clients, and the console. If possible in
your environment, .NET version 4.8 is recommended. A later version of Configuration
Manager will require .NET version 4.8. Before you run setup to install or update the site,
first update .NET and restart the system. For more information, Site and site system
prerequisites.

Remote connection to WMI on secondary site
Applies to: Secondary site

Setup can establish a remote connection to WMI on the secondary site server.

Required version of Microsoft .NET Framework (warning)
Applies to: CAS, primary site, secondary site

In version 2107, this rule checks if the .NET Framework is at least version 4.6.2. You'll see
this warning if the system has less than version 4.6.2.

  ） Important

  Starting in version 2111, if this check fails, it returns an error instead of a warning.
  To determine the systems that need to be updated, review the
  ConfigMgrPrereq.log found on the system drive of the computer.

<!-- p.904 -->

Configuration Manager requires Microsoft .NET Framework version 4.6.2 for site servers,
specific site systems, clients, and the console. If possible in your environment, .NET
version 4.8 is recommended. A later version of Configuration Manager will require .NET
version 4.8. Before you run setup to install or update the site, first update .NET and
restart the system. For more information, Site and site system prerequisites.

Schema extensions
Applies to: Central administration site, primary site

The Active Directory schema has been extended. If it's extended, the version of the
schema extensions that were used.

Configuration Manager doesn't require Active Directory schema extensions for site
server installation. Microsoft recommends them for the full use of all Configuration
Manager features. For more information about the advantages of extending the schema,
see Prepare Active Directory for site publishing.

Share name in package
Applies to: Central administration site, primary site

Packages don't have invalid characters in the share name, such as # .

Site system to SQL Server communication
Applies to: Secondary site, management point

The account that you configured to run the SQL Server service for the site database
instance has a valid service principal name (SPN) in Active Directory Domain Services.
Register a valid SPN in Active Directory to support Kerberos authentication.

SQL Server 2012 lifecycle
Applies to: CAS, primary site, secondary site

This rule warns for the presence of SQL Server 2012. The support lifecycle for SQL Server
2012 ends on July 12, 2022. Plan to upgrade database servers in your environment,
including SQL Server Express at secondary sites.

For more information, see Removed and deprecated for site servers: SQL Server.

<!-- p.905 -->

SQL Server change tracking cleanup
Applies to: Site database server

Check if the site database has a backlog of SQL Server change tracking data.

Manually verify this check by running a diagnostic stored procedure in the site database.
First, create a diagnostic connection to your site database. The easiest method is to use
SQL Server Management Studio's Database Engine Query Editor, and connect to admin:
<instance name> .

In a dedicated administrator connection query window, run the following commands:

  SQL

  USE <ConfigMgr database name>
  EXEC spDiagChangeTracking

Depending upon the size of your database and the backlog size, this stored procedure
could run in a few minutes or several hours. When the query completes, you see two
sections of data related to the backlog. First look at CT_Days_Old. This value tells you
the age (days) of the oldest entry in your syscommittab table. It should be five days,
which is the Configuration Manager default value. Don't change this default value. At
times of heavy data processing or replication, the oldest entry in syscommittab could be
over five days. If this value is above seven days, run a manual cleanup of change
tracking data.

To clean up the change tracking data, run the following command in the dedicated
administration connection:

  SQL

  USE <ConfigMgr database name>
  EXEC spDiagChangeTracking @CleanupChangeTracking = 1

This command starts a cleanup of syscommittab and all of the associated side tables. It
can run in several minutes or several hours. To monitor its progress, query the vLogs
view. To see the current progress, run the following query:

  SQL

  SELECT * FROM vLogs WHERE ProcedureName = 'spDiagChangeTracking'

<!-- p.906 -->

SQL Server Express version on secondary site
Applies to: Secondary site

Starting in version 2103, if you have a secondary site that uses SQL Server Express
edition, this check warns if the version is earlier than SQL Server 2016 with service pack 2
(13.0.5026.0). If Configuration Manager didn't install SQL Server Express, then setup
skips this check. Setup looks for the presence of the CONFIGMGRSEC instance.

Microsoft recommends that you keep SQL Server Express up to date. For more
information, see Security for site administration.

SQL Server Native Client
When you install a new site, Configuration Manager automatically installs SQL Server
Native Client as a redistributable component. After the site is installed, Configuration
Manager doesn't upgrade SQL Server Native Client. Updating the SQL Server Native
Client may require a restart, which can impact the site install process.

This check makes sure the site server has a supported version of the SQL Server Native
Client. The prerequisite check doesn't verify the version of the SQL Server Native Client
on remote site systems.

The minimum version is SQL Server 2012 SP4 ( 11.*.7001.0 ). This SQL Server Native
Client version supports TLS 1.2. For more information, see the following articles:

     TLS 1.2 support for Microsoft SQL Server

     How to enable TLS 1.2 for Configuration Manager

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

<!-- p.907 -->

     Endpoint Protection point
     Service connection point
     Certificate registration point
     Data warehouse service point

SQL Server process memory allocation
Applies to: Site database server

SQL Server reserves a minimum of 8 GB of memory for the central administration site
and primary site, and a minimum of 4 GB of memory for the secondary site.

For more information, see SQL Server memory configuration options.

  ７ Note

  This check isn't applicable to SQL Server Express on a secondary site. This edition is
  limited to 1 GB of reserved memory.

SQL Server security mode
Applies to: Site database server

SQL Server is configured for Windows authentication security.

Unsupported site system OS version for upgrade
Applies to: Primary site, secondary site

Site system roles other than distribution points are installed on servers running
Windows Server 2012 or later.

For more information, see Supported operating systems for Configuration Manager site
system servers.

  ７ Note

  This check can't resolve the status of site system roles installed in Azure or for the
  cloud storage used by Microsoft Intune. Ignore warnings for these roles as false
  positives.

<!-- p.908 -->

Upgrade Assessment Toolkit is unsupported
Applies to: Central administration site, primary site

The Upgrade Assessment Toolkit isn't installed. For more information, see Removed and
deprecated features.

Verify site server permissions to publish to Active
Directory
Applies to: Central administration site, primary site, secondary site

The computer account for the site server has Full Control permissions to the System
Management container in the Active Directory domain.

For more information, see Prepare Active Directory for site publishing.

  ７ Note

  If you manually verify the permissions, you can ignore this warning.

Windows Remote Management (WinRM) v1.1
Applies to: Primary site, Configuration Manager console

WinRM 1.1 is installed on the primary site server or the Configuration Manager console
computer to run the out-of-band management console.

WinRM is automatically installed with all versions of Windows currently supported. For
more information, see Installation and configuration for Windows Remote Management.

WSUS on site server
Applies to: Central administration site, primary site

A supported version of Windows Server Update Services (WSUS) is installed on the site
server.

When you use a software update point on a server other than the site server, you must
install the WSUS Administration Console on the site server. For more information about
WSUS, see Windows Server Update Services.

<!-- p.909 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.910 -->

Resources for installing Configuration
Manager sites
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The following articles can help you install Configuration Manager or add sites to your
existing Configuration Manager hierarchy.

      Prepare to install sites

      This article offers essential information that can help you install a site to a new or
      existing hierarchy. Information includes when to choose non-default source files,
      limitations that apply to all sites, and optional actions you can take to help simplify
      your tasks when you install more than one site.

      Prerequisites for installing sites

      Learn about the user rights and permissions your account must have to install a
      site and related prerequisites for each type of site you can install.

      Install sites using the Setup Wizard

      This article walks you through the site installation wizard. It provides details about
      options that might not be clear in the wizard user interface.

      Install sites using a command line and script

      Learn how to create a site installation script, and how to use it for unattended site
      installs.

      Install the Configuration Manager console

      This article has guidance on how to install the Configuration Manager console on a
      computer on which you're not installing a site.

      Upgrade an evaluation installation to a full installation

      Read this article when you're ready to upgrade your evaluation site to a fully
      licensed Configuration Manager site.

Feedback

<!-- p.911 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.912 -->

Prepare to install Configuration
Manager sites
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To prepare for a successful deployment of one or more Configuration Manager sites,
become familiar with the details in this article. These steps can save you time during
installation of multiple sites and help prevent missteps that might result in the need to
reinstall one or more sites.

   Tip

  When managing Configuration Manager site and hierarchy infrastructure, the terms
  upgrade, update, and install are used to describe three separate concepts. To learn
  how each term is used, see About upgrade, update, and install.

Options for installing different types of sites
When you install a new Configuration Manager site, the version of the source files that
you can use depends on the version of sites that are already in the hierarchy (if any). The
installation methods that you can use depend on the type of site you want to install.

Before installing a site, make sure you have planned your hierarchy, and that you
understand the type of site you want to install. For more information, see Design a
hierarchy of sites.

First site
The first site that you install in a hierarchy will be either a stand-alone primary site or a
central administration site.

Installation media: To install a central administration site or a stand-alone primary site
as the first site in a new hierarchy, you must use a baseline version of Configuration
Manager. Do not install the first site of a new hierarchy by using updated source files
from the CD.Latest folder of any site.

Installation method: You can install either type of site by using the Configuration
Manager Setup Wizard, or you can configure a script to use with a scripted command-

<!-- p.913 -->

line installation.

Additional sites
After the initial site is installed, you can add more sites at any time. You have the
following options for adding sites (up to supported limits):

                                                                                 ﾉ   Expand table

 Site that you have       Additional site type you can install

 Central                  Child primary site
 administration site

 Child primary site       Secondary site

 Stand-alone primary      Secondary site (you can expand the primary site, which converts the
 site                     stand-alone primary site to a child primary site)

Installation media: When you install a central administration site to expand a stand-
alone primary site, or if you install a new child primary site in an existing hierarchy, you
must use installation media (that contains source files) that matches the version of the
existing site or sites.

  ） Important

  If you have installed in-console updates that have changed the version of the
  previously installed sites, do not use the original installation media. Instead, in that
  scenario, use source files from the CD.Latest folder of an updated site.
  Configuration Manager requires you to use source files that match the version of
  the existing site that your new site will connect to.

A secondary site must be installed from the Configuration Manager console. This way,
secondary sites are always installed by using source files from the parent primary site.

Installation method: The method you use to install additional sites depends on the type
of site you want to install.

        Add a central administration site: You can use the Configuration Manager Setup
        Wizard or a scripted command line to install the new central administration site as
        a parent site to your existing stand-alone primary site. For more information, see
        Expanding a stand-alone primary site.

<!-- p.914 -->

     Add a child primary site: You can use the Configuration Manager Setup Wizard or
     a command-line installation to add a child primary site below a central
     administration site.
     Add a secondary site: Use the Configuration Manager console to install a
     secondary site as a child site below a primary site. Other methods are not
     supported for adding secondary sites.

Common tasks to complete before starting an
installation
     Understand the hierarchy topology you will use for your deployment
     For more information, see Design a hierarchy of sites for Configuration Manager.

     Prepare and configure individual servers to meet prerequisites and supported
     configurations for use with Configuration Manager
     For more information, see Site and site system prerequisites.

     Install and configure SQL Server to host the site database
     For more information, see Support for SQL Server versions for Configuration
     Manager.

     Prepare your network environment to support Configuration Manager
     For more information, see Configure firewalls, ports, and domains to prepare for
     Configuration Manager.

     If you will use a public key infrastructure (PKI), prepare your infrastructure and
     certificates
     For more information, see PKI certificate requirements for Configuration Manager.

     Install the latest security updates on computers you will use as site servers or
     site system servers, and when necessary, restart them

About site names and site codes
Site codes and site names are used to identify and manage the sites in a Configuration
Manager hierarchy. In the Configuration Manager console, the site code and site name
are displayed in the <site code> - <site name> format. Every site code that you use in
your hierarchy must be unique. If the Active Directory schema is extended for
Configuration Manager and your sites are publishing data, the site codes used within an
Active Directory forest must be unique even if they are used in a different Configuration
Manager hierarchy or if they have been used in earlier Configuration Manager

<!-- p.915 -->

installations. Be sure to carefully plan your site codes and site names before you deploy
your hierarchy.

Specify a site code and site name
When you run Configuration Manager Setup, you are prompted for a site code and site
name for the central administration site, and for each primary site and secondary site
installation. A site code must uniquely identify each site in the hierarchy. Because the
site code is used in folder names, never use the following names for the site code, which
include names reserved for Configuration Manager and Windows:

     AUX
     CON
     NUL
     PRN
     SMS
     ENV

  ７ Note

  Configuration Manager Setup does not verify that a site code is not already in use.

To enter the site code for a site when you're running Configuration Manager Setup, you
must enter three alphanumeric characters. Only the letters A through Z and the numbers
0 through 9, in any combination, are allowed in site codes. The sequence of letters or
numbers has no effect on the communication between sites. For example, it is not
necessary to name a primary site ABC and a secondary site DEF.

The site name is a friendly name identifier for the site. You can only use the characters A
through Z, a through z, 0 through 9, and the hyphen (-) in site names.

  ） Important

  A change of the site code or site name after you install the site is not supported.

Reuse a site code
Site codes cannot be used more than one time in a Configuration Manager hierarchy for
a central administration site or for a primary site, even if the original site and site code
have been uninstalled. If you reuse a site code, you risk having object ID conflicts in your

<!-- p.916 -->

hierarchy. You can reuse the site code for a secondary site if that secondary site and the
site code are no longer in use in your Configuration Manager hierarchy or in the Active
Directory forest.

Limits and restrictions for installed sites
Before you install a site, it's important to understand the following limitations that apply
to sites and site hierarchies:

     After running Setup, you cannot change the following site properties without
     uninstalling the site and then reinstalling it by using the new values:
        Program Files installation directory
        Site code
        Site description
     When your hierarchy includes a central administration site:
        Configuration Manager does not support moving a child primary site out of a
        hierarchy to create a stand-alone primary site or to attach it to a different
        hierarchy. Instead, uninstall the child primary site, and then reinstall it as a new
        stand-alone primary site or as a child site of the central administration site of a
        different hierarchy.

Optional steps before running Setup
Manually run Setup Downloader

To download the updated Setup files for Configuration Manager, you can run Setup
Downloader. If the computer where you will run Setup is not connected to the Internet,
or if you expect to install multiple site servers, consider using Setup Downloader to
download the required updates to Setup. Here's additional information:

     By default, Setup connects to the Internet to download updated Setup files.
     By default, the files are stored in the Redist folder.
     You can direct Setup to a location on your network where you have previously
     stored a copy of these files.

Manually run Prerequisite Checker

To identify and fix problems before you run Setup to install a site and before you install
a site system role on a server, you can run Prerequisite Checker. Prerequisite Checker
helps ensure that the computer meets the requirements to host the site or site system
role. Here's additional information:

<!-- p.917 -->

     By default, Setup runs Prerequisite Checker.
     If there are any errors, Setup stops until the issue is fixed.

Identify optional ports

You can identify optional ports for site systems and clients to use. Here's additional
information:

     By default, site systems and clients use predefined ports to communicate.
     During Setup, you can configure alternate ports.

For more information, see Ports used.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.918 -->

Prerequisites for installing Configuration
Manager sites
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you begin a site installation, learn about the prerequisites for installing the
different types of Configuration Manager sites.

Primary sites and the central administration
site
The following prerequisites apply to installing one of the following types:

      A central administration site (CAS) as the first site of a hierarchy
      A stand-alone primary site
      A child primary site

If you're installing a CAS as part of a hierarchy expansion, see the section for Expanding
a stand-alone primary site.

Prerequisites for installing a primary site or a CAS
      The necessary Windows Server roles, features, and Windows components must be
      installed. For more information, see Site system prerequisites

      The user account that installs the site must have the following permissions:

         Administrator on the following servers:
            The site server
            Each SQL Server that hosts the site database
            Each instance of the SMS Provider for the site

         Sysadmin on the instance of SQL Server that hosts the site database

           ） Important

           When Configuration Manager setup finishes, the site server computer
           account still needs sysadmin permissions to SQL Server. Don't remove the
           SQL Server sysadmin permissions from this account.

<!-- p.919 -->

          For more information on the need for these permissions after setup is
          complete, see Accounts: Elevated permissions.

     If you're installing a primary site, you may also need Administrator permissions on
     additional servers. For example, where you install the initial management point and
     distribution point, if not on the site server.

     If you're installing a new child primary site below a CAS, you need the following
     additional permissions:

        Administrator on the site server that hosts the CAS

        Administrator on the SQL Server that hosts the CAS site database

        Role-based administration permissions within Configuration Manager that are
        equivalent to the security role of Infrastructure Administrator or Full
        Administrator

     Use the correct installation source files, and run setup from that location. For
     information about the correct source files to use to install different types of sites,
     see Prepare to install site: Options for installing different types of sites.

     The site server needs access to the latest setup files from Microsoft. Use one of the
     following methods:

        Before you start the install, download and store a copy of these files on your
        local network. For more information, see Setup Downloader.

        If a local copy of these files isn't available, the site server needs access to the
        internet. It downloads these files from Microsoft during the installation. For
        more information, see Internet access requirements.

     The site server and site database server must meet all prerequisite configurations.
     Before starting Configuration Manager setup, manually run Prerequisite Checker to
     identify and fix problems.

Prerequisites to expand a stand-alone primary site
A stand-alone primary site must meet the following prerequisites before you can
expand it into a hierarchy with a CAS:

Source file version matches site version

<!-- p.920 -->

Install the new CAS using media from a CD.Latest folder that matches the version of the
stand-alone primary site. To make sure the versions match, use the source files found in
the CD.Latest folder on the stand-alone primary site.

For more information about the correct source files to use to install different sites, see
Prepare to install sites: Options for installing different types of sites.

Stop active migration from another hierarchy
You can't configure the stand-alone primary site to migrate data from another
Configuration Manager hierarchy. Stop active migration to the stand-alone primary site
from other Configuration Manager hierarchies and remove all configurations for
migration. These configurations include:

     Migration jobs that haven't completed
     Data gathering
     The configuration of the active source hierarchy

This configuration is necessary because Configuration Manager migrates data from the
top-level site of the hierarchy. When you expand a stand-alone primary site, the
configurations for migration don't transfer to the CAS.

After you expand the stand-alone primary site, if you reconfigure migration at the
primary site, the CAS runs the migration jobs.

For more information about how to configure migration, see Configure source
hierarchies and source sites for migration.

Computer account as Administrator
Add the computer account of the server that hosts the new CAS to the Administrators
group on the stand-alone primary site server.

To successfully expand the stand-alone primary site, the computer account of the new
CAS needs Administrator permissions on the stand-alone primary site. This account
requires these permissions only during site expansion. When site expansion finishes, you
can remove the account from the user group on the primary site.

Installation account permissions
The user account that runs Configuration Manager setup to install the new CAS needs
role-based administration permissions at the stand-alone primary site.
