---
title: "Core infrastructure documentation — pages 1241-1280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1241-1280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1241-1280
family: sccm
documentKind: "doc"
abstract: "ALTER DATABASE [CM_xxx] SET TRUSTWORTHY ON; For more information, see the TRUSTWORTHY database property. Enable the Service Broker: SQL ALTER DATABASE [CM_xxx] SET ENABLE_BROKER ７ Note You can't enable the Service Broker option on a database that's already part of an availabilit"
---

# Core infrastructure documentation — pages 1241-1280

<!-- p.1241 -->

        ALTER DATABASE [CM_xxx] SET TRUSTWORTHY ON;

     For more information, see the TRUSTWORTHY database property.

     Enable the Service Broker:

        SQL

        ALTER DATABASE [CM_xxx] SET ENABLE_BROKER

        ７ Note

        You can't enable the Service Broker option on a database that's already part of an
        availability group. You have to enable that option before adding it to the availability
        group.

     Configure the Service Broker priority:

        SQL

        ALTER DATABASE [CM_xxx] SET HONOR_BROKER_PRIORITY ON;
        ALTER DATABASE [CM_xxx] SET ENABLE_BROKER WITH ROLLBACK IMMEDIATE

Database verification script

Run the following SQL script to verify database configurations for both primary and secondary
replicas. Before you can fix an issue on a secondary replica, change that secondary replica to be
the primary replica.

  SQL

        SET NOCOUNT ON

        DECLARE @dbname NVARCHAR(128)

        SELECT @dbname = sd.name FROM sys.sysdatabases sd WHERE sd.dbid = DB_ID()

      IF (@dbname = N'master' OR @dbname = N'model' OR @dbname = N'msdb' OR @dbname
  = N'tempdb' OR @dbname = N'distribution' ) BEGIN
      RAISERROR(N'ERROR: Script is targeting a system database. It should be
  targeting the DB you created instead.', 0, 1)
      GOTO Branch_Exit;
      END ELSE
      PRINT N'INFO: Targeted database is ' + @dbname + N'.'

<!-- p.1242 -->

    PRINT N'INFO: Running verifications....'

    IF NOT EXISTS (SELECT * FROM sys.configurations c WHERE c.name = 'clr enabled'
AND c.value_in_use = 1)
    PRINT N'ERROR: CLR is not enabled!'
    ELSE
    PRINT N'PASS: CLR is enabled.'

    DECLARE @repltable TABLE (
    name nvarchar(max),
    minimum int,
    maximum int,
    config_value int,
    run_value int )

    INSERT INTO @repltable
    EXEC sp_configure 'max text repl size (B)'

    IF NOT EXISTS(SELECT * from @repltable where config_value = 2147483647 and
run_value = 2147483647 )
    PRINT N'ERROR: Max text repl size is not correct!'
    ELSE
    PRINT N'PASS: Max text repl size is correct.'

    IF NOT EXISTS (SELECT db.owner_sid FROM sys.databases db WHERE db.database_id
= DB_ID() AND db.owner_sid = 0x01)
    PRINT N'ERROR: Database owner is not sa account!'
    ELSE
    PRINT N'PASS: Database owner is sa account.'

    IF NOT EXISTS( SELECT * FROM sys.databases db WHERE db.database_id = DB_ID()
AND db.is_trustworthy_on = 1 )
    PRINT N'ERROR: Trustworthy bit is not on!'
    ELSE
    PRINT N'PASS: Trustworthy bit is on.'

    IF NOT EXISTS( SELECT * FROM sys.databases db WHERE db.database_id = DB_ID()
AND db.is_broker_enabled = 1 )
    PRINT N'ERROR: Service broker is not enabled!'
    ELSE
    PRINT N'PASS: Service broker is enabled.'

    IF NOT EXISTS( SELECT * FROM sys.databases db WHERE db.database_id = DB_ID()
AND db.is_honor_broker_priority_on = 1 )
    PRINT N'ERROR: Service broker priority is not set!'
    ELSE
    PRINT N'PASS: Service broker priority is set.'

    PRINT N'Done!'

    Branch_Exit:

<!-- p.1243 -->

Availability group configurations

Replica members
     The availability group must have one primary replica.

     Use the same number and type of replicas in an availability group that your version of
     SQL Server supports.

     You can use an asynchronous commit replica to recover your synchronous replica. For
     more information, see site database recovery options.

        ２ Warning

        Configuration Manager doesn't support failover to use the asynchronous commit
        replica as your site database. For more information, see Failover and failover modes
        (Always On availability groups).

Configuration Manager doesn't validate the state of the asynchronous commit replica to
confirm it's current. Use of an asynchronous commit replica as the site database can put the
integrity of your site and data at risk. This replica can be out of sync by design. For more
information, see Overview of SQL Server Always On availability groups.

Each replica member must have the following configuration:

     Use the default instance or a named instance.

        ７ Note

        Don't have a file share on the server that's the same name as the SQL Server instance
        name.

     The Connections in Primary Role setting is Allow all connections.

     The Readable Secondary setting is Yes.

     Enabled for Manual Failover

        ７ Note

        Configuration Manager supports using the availability group synchronous replicas
        when set to Automatic Failover. Set Manual Failover when:

<!-- p.1244 -->

           You run Configuration Manager setup to specify use of the site database in the
           availability group.
           You install any update to Configuration Manager. (Not just updates that apply to
           the site database).

     All members need the same seeding mode. Configuration Manager setup includes a
     prerequisite check to verify this configuration when creating a database through install or
     recovery.

        ７ Note

        When setup creates the database, and you configure automatic seeding, the
        availability group must have permissions to create the database. This requirement
        applies to both a new database or recovery. For more information, see Automatic
        seeding for secondary replica.

Replica member location
Either host all replicas in an availability group on-premises, or host them all on Microsoft Azure.
A group that includes an on-premises member and a member in Azure isn't supported.

  ７ Note

  If you're using an Azure virtual machine for the SQL Server, enable floating IP. For more
  information, see Configure a load balancer for a SQL Server Always On availability group
  in Azure virtual machines.

Configuration Manager setup needs to connect to each replica. When you set up an availability
group in Azure, and the group is behind an internal or external load balancer, open the
following default ports:

     RPC Endpoint Mapper: TCP 135

     SQL Server Service Broker: TCP 4022

     SQL over TCP: TCP 1433

After setup completes, these ports must stay open for Configuration Manager and replication
link analyzer.

<!-- p.1245 -->

You can use custom ports for these configurations. Use the same custom ports by the endpoint
and on all replicas in the availability group.

For SQL Server to replicate data between sites, create a load-balancing rule for each port in the
Azure load balancer. For more information, see Configure High Availability Ports for an internal
load balancer.

Listener
The availability group must have at least one availability group listener. When you configure
Configuration Manager to use the site database in the availability group, it uses the virtual
name of this listener. Although an availability group can contain multiple listeners,
Configuration Manager can only make use of one. For more information, see Create or
configure a SQL Server availability group listener.

File paths

When you run Configuration Manager setup to configure a site to use the database in an
availability group, each secondary replica server must have a SQL Server file path that's
identical to the file path for the site database files on the current primary replica. If an identical
path doesn't exist, setup fails to add the instance for the availability group as the new location
of the site database.

The local SQL Server service account must have Full Control permission to this folder.

The secondary replica servers only require this file path while you're using Configuration
Manager setup to specify the database instance in the availability group. After it completes
configuration of the site database in the availability group, you can delete the unused path
from secondary replica severs.

For example, consider the following scenario:

     You create an availability group that uses three SQL Servers.

     Your primary replica server is a new installation of SQL Server 2014. By default, it stores
     the database MDF and LDF files in C:\Program Files\Microsoft SQL
     Server\MSSQL12.MSSQLSERVER\MSSQL\DATA .

     You upgraded both of your secondary replica servers to SQL Server 2014 from previous
     versions. With the upgrade, these servers keep the original file path to store database
     files: C:\Program Files\Microsoft SQL Server\MSSQL10.MSSQLSERVER\MSSQL\DATA .

<!-- p.1246 -->

     Before moving the site database to this availability group, on each secondary replica
     server, create the following file path: C:\Program Files\Microsoft SQL
     Server\MSSQL12.MSSQLSERVER\MSSQL\DATA . This path is a duplicate of the path in use on the

     primary replica, even if the secondary replicas don't use this file location.

     You then grant the SQL Server service account on each secondary replica full control
     access to the newly created file location on that server.

     You can now successfully run Configuration Manager setup to configure the site to use
     the site database in the availability group.

Multi-subnet failover
You can enable the MultiSubnetFailover connection string keyword in SQL Server. You also
need to manually add the following values to the Windows Registry on the site server:

  Registry

  HKLM:\SOFTWARE\Microsoft\SMS\Identification
  HKLM:\SOFTWARE\Microsoft\SMS\SQL Server

  MSF Enabled : 1 (DWORD)

  ２ Warning

  Use of site server high availability and SQL Server Always On availability groups with
  multi-subnet failover doesn't provide the full capabilities of automatic failover for disaster
  recovery scenarios.

If you need to create an availability group with a member in a remote location, prioritize based
on the lowest network latency. High network latency can cause replication failures.

Limitations and known issues
The following limitations apply to all scenarios.

Unsupported SQL Server options and configurations
     Basic availability groups: Introduced with SQL Server 2016 Standard edition, basic
     availability groups don't support read access to secondary replicas. Configuration requires
     this access. For more information, see Basic SQL Server availability groups.

<!-- p.1247 -->

     Failover cluster instance: Failover cluster instances aren't supported for a replica you use
     with Configuration Manager. For more information, see SQL Server Always On failover
     cluster instances.

SQL Servers that host additional availability groups
When the SQL Server hosts one or more availability groups in addition to the group you use
for Configuration Manager, it needs specific settings at the time you run Configuration
Manager setup. These settings are also needed to install an update for Configuration Manager.
Each replica in each availability group must have the following configurations:

     Manual failover

     Allow any read-only connection

  ７ Note

  Configuration Manager supports using the availability group synchronous replicas when
  set to Automatic Failover. Set Manual Failover when:

       You run Configuration Manager setup to specify use of the site database in the
       availability group.
       You install any update to Configuration Manager. (Not just updates that apply to the
       site database).

Unsupported database use

Configuration Manager supports only the site database in an availability
group
Configuration Manager doesn't support the following databases in an availability group:

     Reporting database

     WSUS database

Pre-existing database
You can't use a new database created on the replica. When you configure an availability group,
restore a copy of an existing Configuration Manager database to the primary replica.

<!-- p.1248 -->

Setup errors in ConfigMgrSetup.log
When you run Configuration Manager setup to move a site database to an availability group, it
tries to process database roles on the secondary replicas of the availability group. The
ConfigMgrSetup.log file shows the following error:

ERROR: SQL Server error: [25000][3906][Microsoft][SQL Server Native Client 11.0][SQL

Server]Failed to update database "CM_AAA" because the database is read-only.

Configuration Manager Setup 1/21/2016 4:54:59 PM 7344 (0x1CB0)

These errors are safe to ignore.

Site expansion
If you configure the site database for a standalone primary site to use an availability group, you
can't expand the site to include a central administration site. If you try this process, it fails. To
expand the site, temporarily remove the primary site database from the availability group.

You don't need to make any changes to the configuration when adding a secondary site.

Changes for site backup

Backup database files
When a site database uses an availability group, run the built-in Backup Site server
maintenance task to back up common Configuration Manager settings and files. Don't use the
MDF or LDF files created by that backup. Instead, make direct backups of these database files
by using SQL Server.

You can still use the SQL Server back up, however you can't restore it directly to a SQL Server
Always On cluster. You need to restore it on a standalone server and move it back to SQL
Server Always On.

Transaction log
Set the recovery model of the site database to Full. This configuration is a requirement for
Configuration Manager use in an availability group. Plan to monitor and maintain the size of
the site database transaction log. In the full recovery model, the transactions aren't hardened
until it makes a full backup of the database or transaction log. For more information, see Back
up and restore of SQL Server databases.

<!-- p.1249 -->

Changes for site recovery
If at least one node of the availability group is still functional, use the site recovery option to
Skip database recovery (Use this option if the site database was unaffected).

Site recovery can recreate the database in an availability group. This process works with both
manual and automatic seeding.

   Tip

  When you run the setup/recovery wizard, the New Availability Group Database page only
  applies to manual seeding configurations. With automatic seeding, there's no shared
  database backup, so that page of the wizard isn't shown.

For more information, see Backup and recovery.

SQL AlwaysOn when BitLocker recovery data is encrypted in
the database
If using SQL AlwaysOn, see SQL AlwaysOn when BitLocker recovery data is encrypted in the
database for additional important and required steps and instructions.

Changes for reporting

Install the reporting service point
The reporting services point doesn't support using the listener virtual name of the availability
group. It also doesn't support hosting its database in an availability group.

     By default, the reporting services point installation sets the Site database server name to
     the virtual name that's specified as the listener. Change this setting to specify a computer
     name and instance of a replica in the availability group.

     To offload reporting and to increase availability when a replica node is offline, consider
     installing additional reporting services points on each replica node. Then configure each
     reporting services point to use its own computer name. When you install a reporting
     service point on each replica of the availability group, reporting can always connect to an
     active reporting point server.

Switch the reporting services point used by the console

<!-- p.1250 -->

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Reporting, and select the Reports node.

   2. In the ribbon, select Report Options.

   3. In the Report Options dialog box, select the reporting services point you want to use.

Next steps
This article describes the prerequisites, limitations, and changes to common tasks that
Configuration Manager requires when you use availability groups. For procedures to set up
and configure your site to use availability groups, see Configure availability groups.

<!-- p.1251 -->

Configure a SQL Server Always On
availability group for Configuration
Manager
06/12/2025

Applies to: Configuration Manager (current branch)

Use the information in this article to configure and manage a SQL Server Always On availability
group for the Configuration Manager site database. Before you start, be familiar with the
information to Prepare to use an availability group. Also be familiar with SQL Server
documentation that covers the use of availability groups and related procedures.

Create and configure an availability group
Use this procedure to create an availability group for Configuration Manager. Then move a
copy of the site database to that availability group.

   1. Use the following command to stop the Configuration Manager site:

      preinst.exe /stopsite

     For more information, see Hierarchy maintenance tool.

   2. Change the backup model for the site database from SIMPLE to FULL:

        SQL

        ALTER DATABASE [CM_xxx] SET RECOVERY FULL;

     Availability groups only support the FULL backup model. For more information, see View
     or change the recovery model of a database.

   3. Use SQL Server to create a full backup of your site database. Choose one of the following
     options:

             Will be member of your availability group: If you use this server as the initial
             primary replica member of the availability group, you don't need to restore a copy
             of the site database to this server or another in the group. The database is already in
             place on the primary replica. SQL Server replicates the database to the secondary
             replicas during a later step.

<!-- p.1252 -->

        Will not be a member of the availability group: Restore a copy of the site database
        to the server that will host the primary replica of the group.

  For more information, see the following articles in the SQL Server documentation:

        Create a full database backup
        Restore a database backup using SSMS

    ７ Note

    If you plan to move from an availability group to standalone on an existing replica,
    first remove the database from the availability group.

4. On the server that will host the initial primary replica of the group, use the New
  availability group wizard to create the availability group. In the wizard:

        On the Select Database page, select the database for your Configuration Manager
        site.

        On the Specify Replicas page, configure:

           Replicas: Specify the servers that will host secondary replicas.

           Listener: Specify the Listener DNS Name as a full DNS name, for example
            <listener_server>.fabrikam.com . When you configure Configuration Manager to

           use the database in the availability group, it uses this name.

        On the Select Initial Data Synchronization page, select Full. After the wizard creates
        the availability group, the wizard backs up the primary database and transaction log.
        Then the wizard restores them on each server that hosts a secondary replica.

           ７ Note

           If you don't use this step, restore a copy of the site database to each server that
           hosts a secondary replica. Then manually join that database to the group.

5. Check the configuration on each replica:

   a. Make sure the computer account of the site server is a member of the local
     Administrators group on each computer that's a member of the availability group.

  b. Run the verification script to confirm that the site database on each replica is correctly
     configured.

<!-- p.1253 -->

      c. If it's necessary to set configurations on secondary replicas, before you continue,
        manually fail over the primary replica to the secondary replica. You can only configure
        the database of a primary replica. For more information, see Perform a planned manual
        failover of an availability group in the SQL Server documentation.

   6. After all replicas meet the requirements, the availability group is ready to be used with
     Configuration Manager.

Configure a site to use the availability group
When installing a new site, after you have created and configured the availability group, direct
setup to use the FQDN of the availability group listener. If you used a custom port and named
instance, leave the instance name empty in the setup wizard and use the format FQDN of
listener, port number. For example, use listener.contoso.com, 1445 for a named instance that
doesn't use the default port of 1433.

If you moved an existing site database to an availability group you created and configured, use
Configuration Manager site maintenance to change the configuration with the below
instructions:

   1. Run Configuration Manager Setup: \BIN\X64\setup.exe from the Configuration Manager
     site installation folder.

   2. On the Getting Started page, select Perform site maintenance or reset this site, and then
     select Next.

   3. Select Modify SQL Server configuration, and then select Next.

   4. Reconfigure the following settings for the site database:

           SQL Server name: Enter the virtual name for the availability group listener. You
           configured the listener when you created the availability group. The virtual name
           should be a full DNS name, like <Listener_Server>.fabrikam.com .

           Instance: To specify the default instance for the listener of the availability group, this
           value must be blank. If the current site database runs on a named instance, clear the
           current named instance.

           Database: Leave the name as it appears. This name is the current site database.

   5. After you provide the information for the new database location, complete setup with
     your normal process and configurations.

<!-- p.1254 -->

  ） Important

  If BitLocker recovery data is encrypted in the database as described in Encrypt recovery
  data in the database, see SQL AlwaysOn when BitLocker recovery data is encrypted in
  the database for additional important and required steps and instructions.

Synchronous replica members
When your site database is hosted in an availability group, use the following procedures to add
or remove synchronous replica members. For more information about the supported type and
number of replicas, see Availability group configurations.

Add or remove a synchronous replica member
Run Configuration Manager setup to add or remove a synchronous replica member. The
following steps show how to add:

   1. Add a secondary replica using the SQL Server procedures.

      a. Add a secondary replica to an Always On availability group.

     b. Watch the status in SQL Server Management Studio. Wait for the availability group to
        return to full health.

   2. Run Configuration Manager setup, and select the option to modify the site.

   3. Specify the availability group listener name as the database name. If the listener uses a
     non-standard network port, specify that as well. This action causes setup to make sure
     each node is appropriately configured. It also starts a database recovery process.

Configuration Manager setup uses the SQL Server database move operation, and makes sure
the nodes are correctly configured.

Asynchronous replicas
You can use an asynchronous replica in the availability group that you use with Configuration
Manager. You don't need to run the configuration scripts required to configure a synchronous
replica, because an asynchronous replica isn't supported for the site database.

Configure an asynchronous commit replica

<!-- p.1255 -->

For more information, see Add a secondary replica to an availability group.

Use the asynchronous replica to recover your site
Use the asynchronous replica to recover your site database.

   1. Stop the active primary site to prevent additional writes to the site database. To stop the
     site, use the Hierarchy maintenance tool: preinst.exe /stopsite

   2. After you stop the site, use the asynchronous replica instead of a manually recovered
     database.

Stop using an availability group
Use the following procedure when you no longer want to host your site database in an
availability group. With this process, you'll move the site database back to a single instance of
SQL Server.

   1. Stop the Configuration Manager site by using the following command: preinst.exe
     /stopsite . For more information, see Hierarchy maintenance tool.

   2. Use SQL Server to create a full backup of your site database from the primary replica. For
     more information, see Create a full database backup.

   3. Use SQL Server to restore the site database backup to the server that will host the site
     database. For more information, see Restore a database backup using SSMS.

        ７ Note

        If the primary replica server for the availability group will host the single instance of
        the site database, skip this step.

   4. On the server that will host the site database, change the backup model for the site
     database from FULL to SIMPLE. For more information, see View or change the recovery
     model of a database.

   5. Run Configuration Manager Setup: \BIN\X64\setup.exe from the Configuration Manager
     site installation folder.

   6. On the Getting Started page, select Perform site maintenance or reset this site, and then
     select Next.

   7. Select Modify SQL Server configuration, and then select Next.

<!-- p.1256 -->

 8. Reconfigure the following settings for the site database:

        SQL Server name: Enter the name of the server that now hosts the site database.

        Instance: Specify the named instance that hosts the site database. If the database is
        on the default instance, leave this field blank.

        Database: Leave the name as it appears. This name is the current site database.

 9. After you provide the information for the new database location, complete setup with
   your normal process and configurations. When setup completes, the site restarts, and
   begins to use the new database location.

10. To clean up the servers that were members of the availability group, follow the guidance
   in Remove an availability group.

<!-- p.1257 -->

Use a SQL Server Always On failover
cluster instance for the site database
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can use a SQL Server Always On failover cluster instance to host the Configuration
Manager site database. Failover cluster instances provide failover support for the entire
instance of SQL Server and improve the reliability of the site database. However, it
doesn't provide additional processing or load-balancing benefits. Failover cluster
instances require the use of shared storage, which can be a single point of failure.
Degradation in performance can occur, because the site server must find the active
node of the failover cluster instance before it connects to the site database.

  ） Important

  To successfully set up of a failover cluster instance, use the documentation and
  procedures for SQL Server. For more information, see Always On Failover Cluster
  Instances (SQL Server).

Before you install Configuration Manager, prepare the failover cluster instance to
support Configuration Manager. For more information, see Prepare a clustered SQL
Server instance.

During Configuration Manager setup, the Windows Volume Shadow Copy Service writer
installs on each physical computer node of the Windows Server failover cluster. This
service supports the Backup Site Server maintenance task.

After the site installs, Configuration Manager checks for changes to the cluster node
each hour. Configuration Manager automatically manages any changes it finds that
affect its component installs. For example, a node failover or the addition of a new node
to the failover cluster instance.

Supported options
Configuration Manager supports the following options for failover cluster instances
used for the site database:

      A single instance cluster

<!-- p.1258 -->

  Multiple instance configurations

  Multiple active nodes

  Both a named or a default instance

Prerequisites
  The site database server must be remote from the site server. The cluster can't
  include the site server.

    ７ Note

    The Configuration Manager setup process doesn't block installation of the site
    server role on a computer with the Windows role for Failover Clustering. SQL
    Server Always On availability groups require this role, so previously you
    couldn't colocate the site database on the site server. With this change, you
    can create a highly available site with fewer servers by using an availability
    group and a site server in passive mode. For more information, see High
    availability options.

  Add the computer account of the site server to the local Administrators group of
  each server in the cluster.

  To support Kerberos authentication, enable the TCP/IP network communication
  protocol for the network connection of each cluster node. The Named pipes
  protocol isn't required, but can be used to troubleshoot Kerberos authentication
  issues. The network protocol settings are configured in SQL Server Configuration
  Manager, under SQL Server Network Configuration.

  There are specific certificate requirements when you use a failover cluster instance
  for the site database. For more information, see the following articles:

     Install a certificate in an Always On failover cluster instance configuration

     PKI certificate requirements for Configuration Manager

    ７ Note

    If you don't pre-provision a certificate in SQL Server, Configuration Manager
    creates and provisions a self-signed certificate for SQL Server.

<!-- p.1259 -->

Limitations

Installation and configuration
     Secondary sites can't use a failover cluster instance.

     When you specify a failover cluster instance, you can't set a custom file location for
     the site database.

SMS Provider
You can't install the SMS Provider on a failover cluster instance. It's also not supported
on a computer that runs as a node participating in the failover cluster instance.

Data replication options
If you use Distributed Views, you can't use a failover cluster instance to host the site
database.

Backup and recovery
Configuration Manager doesn't support System Center Data Protection Manager (DPM)
backup for failover cluster instances that use a named instance. It does support DPM
backup on failover cluster instances that use the SQL Server default instance.

Prepare a failover cluster instance
Here are the main tasks to complete to prepare your site database:

     Create the failover cluster instance to host the site database on an existing
     Windows Server failover cluster environment. For specific steps to install and set
     up a failover cluster instance, see the documentation specific to your version of
     SQL Server. For more information, see Create a new SQL Server Always On failover
     cluster instance.

     On each computer in the failover cluster instance, place a file in the root folder of
     each drive where you don't want Configuration Manager to install site
     components. Name the file NO_SMS_ON_DRIVE.SMS . By default, Configuration
     Manager installs some components on each physical node, to support operations
     such as backup.

<!-- p.1260 -->

     Add the computer account of the site server to the local Administrators group of
     each Windows Server failover cluster node.

     In the failover cluster instance, assign the sysadmin SQL Server role to the user
     account that runs Configuration Manager setup.

Install a new site
To install a site that uses a clustered site database, run Configuration Manager setup
following your normal process for installing a site. On the Database Information page,
specify the name of the failover cluster instance. The failover cluster instance name
replaces the name of a single computer that runs SQL Server.

  ） Important

  Make sure to use the name of the SQL Server Always On failover cluster instance,
  not the Windows Server failover cluster. If you use the Windows Server failover
  cluster name, the site database installs on the local hard drive of the active
  Windows Server failover cluster node. This configuration prevents successful
  failover if that node fails.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1261 -->

Custom locations for Configuration
Manager site database files
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager supports custom locations for SQL Server database files.

  ７ Note

  The option to specify non-default file locations isn't available when you use a SQL
  Server Always On failover cluster instance.

During setup of a new primary site or central administration site, you can:

      Specify non-default file locations for the site database: Configuration Manager
      setup then creates the site database using these locations.

      Specify the use of a pre-created SQL Server database that uses custom file
      locations: Configuration Manager setup then uses that pre-created database and
      its pre-configured file locations.

After setup, you can change the location of the site database files. This requires you to
stop the site and edit the file location in SQL Server:

   1. On the Configuration Manager site server, stop the SMS_Executive service.

   2. Move the database in SQL Server. For more information, see Move User Databases.

   3. After you complete the database file move, restart the SMS_Executive service on
      the Configuration Manager site server.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1262 -->

Configure role-based administration for
Configuration Manager
07/17/2025

Applies to: Configuration Manager (current branch)

In Configuration Manager, role-based administration combines security roles, security scopes,
and assigned collections to define the administrative scope for each administrative user. An
administrative scope includes the objects that an administrative user can view in the
Configuration Manager console and the tasks related to those objects that they have
permission to do.

If you're not yet familiar with these concepts, see Fundamentals of role-based administration.

Use the information in this article to create and configure role-based administration and
related security settings.

  ７ Note

  The procedures in this article assume that your administrative user is in a security role with
  the required permissions. For example, the Full Administrator or Security administrator
  roles.

   Tip

  Use the Role-based administration and auditing tool to help with the following actions:

           Model permissions for a new role that you want to create.
           Audit all existing administrative users, collections, and security scopes.
           Audit a specific user

Create custom security roles
Configuration Manager provides several built-in security roles. You can't change the
permissions of the built-in roles. If you require other roles, create a custom one. You might
create a custom role to grant administrative users other permissions that they require and
aren't included in a built-in role. By using a custom security role, you can assign them the least
required permissions. A custom role can help you avoid assigning a security role that grants
more permissions than they require.

<!-- p.1263 -->

How to create custom security roles
In the Configuration Manager console, go to the Administration workspace. Expand Security,
and then select the Security Roles node. Then use one of the following processes to create a
new security role:

Create a new custom security role by copying a built-in role
   1. Select an existing security role to use as the source for the new role.

   2. On the Home tab of the ribbon, in the Security Role group, select Copy. This action
     creates a copy of the source security role.

   3. In the Copy Security Role wizard, specify a Name for the new custom security role. The
     maximum length is 256 characters.

   4. Optional but recommended, specify a Description to summarize the purpose of this
     custom security role. The maximum length is 512 characters.

   5. Under Permissions, expand each object type to display the available permissions.

   6. To change a permission, select the drop-down list, and choose either Yes or No.

        Ｕ Caution

        When you configure a custom security role, only grant permissions that are required
        by the users assigned to this role. For example, the Modify permission for the
        Security Roles object allows assigned users to edit any accessible security role, even
        if they aren't assigned to that security role.

   7. After you configure the permissions, select OK to save the new security role.

Import a security role that was exported from another Configuration
Manager hierarchy

  ） Important

  Only import custom security role configuration files from a trusted source. When you
  export a custom security role, save it in a secure location. The XML files aren't digitally
  signed.

   1. On the Home tab of the ribbon, in the Create group, choose Import Security Role.

<!-- p.1264 -->

   2. Specify the XML file that contains the exported security role configuration. Select Open to
     complete the procedure and create the security role.

   3. After you import a custom security role, open its Properties. View the permissions to
     confirm they include the least required permissions for this role. Change any permissions
     that aren't required in this environment.

  ７ Note

  You can't export built-in security roles.

Configure security roles
You can modify the permissions for a custom security role, but you can't modify the built-in
security roles.

   1. In the Configuration Manager console, go to the Administration workspace, expand
     Security, and then select the Security Roles node.

   2. Select the custom security role that you want to modify or view.

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. On the General tab of the properties window, change the Name or Description if
     necessary.

   5. On the Administrative Users tab, view the users that are associated with this role. To
     change the assignment, go to the properties of the administrative user.

   6. On the Permissions tab, expand each object type to display the available permissions.

   7. To change a permission, select the drop-down list, and then choose either Yes or No.

        Ｕ Caution

        When you configure a custom security role, only grant permissions that are required
        by the users assigned to this role. For example, the Modify permission for the
        Security Roles object allows assigned users to edit any accessible security role, even
        if they aren't assigned to that security role.

   8. When you're done, select OK to save the custom security role.

<!-- p.1265 -->

Configure security scopes for an object
Manage security scopes from the securable object, not from the security scope. The only
properties you can change on a custom security scope is the name and description. You can't
modify the two built-in scopes. To change the name and description of a custom scope, you
need the Modify permission for the Security Scopes object.

When you create a new object in Configuration Manager, it's associated with each security
scope that's associated with the security roles of the account used to create the object. This
behavior occurs when those security roles provide the Create permission or Set Security Scope
permission. After you create an object, you can change the security scopes and assign it to
multiple scopes.

For example, you're assigned a security role that grants you permission to create a new
boundary group. That role is associated with the Admins security scope. When you create a
new boundary group, you've no option to assign specific security scopes. The Admins security
scope is automatically assigned to the new boundary group. After you save the new boundary
group, you can edit the security scopes for the boundary group.

For more information on how to add a scope for a user, see Modify the administrative scope of
an administrative user.

How to create a custom security scope
   1. In the Configuration Manager console, go to the Administration workspace, expand
     Security, and then select the Security Scopes node.

   2. On the Home tab of the ribbon, in the Create group, select Create Security Scope.

   3. In the Create Security Scope window, specify a Security scope name. The maximum
     length is 256 characters.

   4. Optional but recommended, specify a Description to summarize the purpose of this
     custom security scope. The maximum length is 512 characters.

   5. Select or remove administrative user assignments. You can change these after you create
     the security scope.

   6. To save the custom security scope, select OK.

How to configure security scopes for an object

<!-- p.1266 -->

   1. In the Configuration Manager console, select an object that supports being assigned to a
     security scope. For the list of supported objects, see Fundamentals of role-based
     administration - Security scopes.

   2. On the Home tab of the ribbon, in the Classify group, select Set Security Scopes.

     For a folder, go to the Folder tab of the ribbon. In the Actions group, select Set Security
     Scopes.

        ７ Note

        An item is searchable in folders outside of a user's security scope if that user shares a
        security scope with the person who created the object.

   3. In the Set Security Scopes window, select or clear the security scopes for this object.
     Select at least one security scope.

   4. Select OK to save the assigned security scopes.

Configure collections to manage security
There are no procedures to configure collections for role-based administration. Collections
don't have a role-based administration configuration. Instead, you assign collections to an
administrative user. To determine the actions that an administrative user can do to a collection
and its members, view the permissions for the Collection object type on the security role.

When an administrative user has permissions to a collection, they also have permissions to
collections that are limited to that collection. For example, your organization uses a collection
named All Desktops. There's also a collection named All North America Desktops that's
limited to the All Desktops collection. If an administrative user has permissions to All
Desktops, they have the same permissions to the All North America Desktops collection.

An administrative user can't use the Delete or Modify permissions on a collection that's
directly assigned to them. They can use these permissions on the collections that are limited to
that collection. In the previous example, the administrative user can delete or modify the All
North America Desktops collection, but they can't delete or modify the All Desktops
collection.

Create a new administrative user
To grant individuals or members of a security group access to manage Configuration Manager,
create an administrative user. Specify a Windows account of the user or user group. Assign

<!-- p.1267 -->

each administrative user to at least one security role and one security scope. You can also
assign collections to limit the administrative scope of the user or group.

  ７ Note

  If the administrative user is a member of the Protected Users global security group, they
  can only run the console for 4 hours at a time. After 4 hours, their kerberos authorization
  expires and can't be renewed. The console automatically closes and any unsaved work in
  progress is lost.

  Members of the Protected Users security group should monitor their time in the console
  and save or close any work in progress before 4 hours. After closing the console, re-launch
  it to continue working.

  For more information regarding the Protected Users security group, see Protected Users
  security group and Guidance about how to configure protected accounts.

How to create a new administrative user
   1. In the Configuration Manager console, go to the Administration workspace, expand
     Security, and then select the Administrative Users node.

   2. On the Home tab of the ribbon, in the Create group, select Add User or Group.

   3. Select Browse, and then select the user account or group to use for this new
     administrative user in Configuration Manager.

        ７ Note

        For console-based administration, you can only specify domain users or domain
        security groups as an administrative user.

   4. For the Associated security roles, select Add to open a list of the available security roles.
     Select one or more security roles, and then select OK.

   5. Choose one of the following options to define the securable object behavior for the new
     user:

             All instances of the objects that are related to the assigned security roles: This
             option has the following behaviors:
               Security scope: All
               Collections: All Systems and All Users and User Groups

<!-- p.1268 -->

                The security roles that you assign to the user define their access to objects.
                New objects that this user creates are assigned to the Default security scope.

              Only the instances of objects that are assigned to the specified security scopes
              and collections: This option has the following behaviors:
                Security scope: Default
                Collections: All Systems and All Users and User Groups
                These defaults maybe different, as the actual security scopes and collections are
                limited to those that are associated with the account that you use to create the
                administrative user.
                Add or Remove security scopes and collections to customize the administrative
                scope of this user.

        ） Important

        After you create the user, view its properties to select a third option, Associate
        assigned security roles with specific security scopes and collections. For more
        information, see Modify the administrative scope of an administrative user.

   6. Select OK to close the window and create the administrative user.

Modify the administrative scope of an
administrative user
You can modify the administrative scope of an administrative user by adding or removing
security roles, security scopes, and collections that are associated with the user. Each
administrative user must be associated with at least one security role and one security scope.
You might have to assign one or more collections to the administrative scope of the user. Most
security roles interact with collections and don't function correctly without an assigned
collection.

When you modify an administrative user, you can change the behavior for how securable
objects are associated with the assigned security roles. The three behaviors that you can select
are as follows:

     All instances of the objects that are related to the assigned security roles: This option
     associates the administrative user with the All scope, and the All Systems and All Users
     and User Groups collections. The security roles that are assigned to the user define
     access to objects.

<!-- p.1269 -->

     Only the instances of objects that are assigned to the specified security scopes and
     collections: This option associates the administrative user to the same security scopes
     and collections that are associated to the account you use to configure the administrative
     user. This option supports the addition or removal of security roles and collections to
     customize the administrative scope of the administrative user.

     Associate assigned security roles with specific security scopes and collections: This
     option lets you create specific associations between individual security roles and specific
     security scopes and collections for the user.

        ７ Note

        This option is available only when you modify the properties of an administrative
        user.

The current configuration for the securable object behavior changes the process that you use
to assign additional security roles. Use the following procedures that are based on the different
options for securable objects to help you manage an administrative user.

Use the following procedure to view and manage the configuration for securable objects for an
administrative user.

To view and manage the securable object behavior for an
administrative user
   1. In the Configuration Manager console, choose Administration.
   2. In the Administration workspace, expand Security, and then choose Administrative
     Users.
   3. Select the administrative user that you want to modify.
   4. On the Home tab, in the Properties group, choose Properties.
   5. Choose the Security Scopes tab to view the current configuration for securable objects
     for this administrative user.
   6. To modify the securable object behavior, select a new option for securable object
     behavior. After you change this configuration, see the appropriate procedure for further
     guidance to configure security scopes and collections, and security roles for this
     administrative user.
   7. Choose OK to complete the procedure.

Use the following procedure to modify an administrative user that has the securable object
behavior set to All instances of the objects that are related to the assigned security roles.

<!-- p.1270 -->

For option: All instances of the objects that are related to the
assigned security roles
   1. In the Configuration Manager console, choose Administration.

   2. In the Administration workspace, expand Security, and then choose Administrative
     Users.

   3. Select the administrative user that you want to modify.

   4. On the Home tab, in the Properties group, choose Properties.

   5. Choose the Security Scopes tab to confirm that the administrative user is configured for
     All instances of the objects that are related to the assigned security roles.

   6. To modify the assigned security roles, choose the Security Roles tab.

          To assign additional security roles to this administrative user, choose Add, check the
          box for each additional security role that you want to assign, and then choose OK.
          To remove security roles, select one or more security roles from the list, and then
          choose Remove.

   7. To modify the securable object behavior, choose the Security Scopes tab and choose a
     new option for the securable object behavior. After you change this configuration, see the
     appropriate procedure for further guidance to configure security scopes and collections,
     and security roles for this administrative user.

       ７ Note

       When the securable object behavior is set to All instances of the objects that are
       related to the assigned security roles, you can't add or remove specific security
       scopes and collections.

   8. Choose OK to complete this procedure.

Use the following procedure to modify an administrative user that has the securable object
behavior set to Only the instances of objects that are assigned to the specified security
scopes and collections.

For option: Only the instances of objects that are assigned to
the specified security scopes and collections
   1. In the Configuration Manager console, choose Administration.

<!-- p.1271 -->

   2. In the Administration workspace, expand Security, and then choose Administrative
     Users.

   3. Select the administrative user that you want to modify.

   4. On the Home tab, in the Properties group, choose Properties.

   5. Choose the Security Scopes tab to confirm that the user is configured for Only the
     instances of objects that are assigned to the specified security scopes and collections.

   6. To modify the assigned security roles, choose the Security Roles tab.

          To assign additional security roles to this user, choose Add, check the box for each
          additional security role that you want to assign, and then choose OK.
          To remove security roles, select one or more security roles from the list, and then
          choose Remove.

   7. To modify the security scopes and collections that are associated with security roles,
     choose the Security Scopes tab.

          To associate new security scopes or collections with all security roles that are
          assigned to this administrative user, choose Add and select one of the four options.
          If you select Security Scope or Collection, check the box for one or more objects to
          complete that selection, and then choose OK.
          To remove a security scope or collection, choose the object, and then choose
          Remove.

   8. Choose OK to complete this procedure.

Use the following procedure to modify an administrative user that has the securable object
behavior set to Associate assigned security roles with specific security scopes and collections.

For option: Associate assigned security roles with specific
security scopes and collections
   1. In the Configuration Manager console, choose Administration.

   2. In the Administration workspace, expand Security, and then choose Administrative
     Users.

   3. Select the administrative user that you want to modify.

   4. On the Home tab, in the Properties group, choose Properties.

<!-- p.1272 -->

5. Choose the Security Scopes tab to confirm that the administrative user is configured for
  Associate assigned security roles with specific security scopes and collections.

6. To modify the assigned security roles, choose the Security Roles tab.

       To assign additional security roles to this administrative user, choose Add. On the
       Add Security Role dialog box, select one or more available security roles, choose
       Add, and select an object type to associate with the selected security roles. If you
       select Security Scope or Collection, check the box for one or more objects to
       complete that selection, and then choose OK.

          ７ Note

          You must configure at least one security scope before the selected security
          roles can be assigned to the administrative user. When you select multiple
          security roles, each security scope and collection that you configure is
          associated with each of the selected security roles.

       To remove security roles, select one or more security roles from the list, and then
       choose Remove.

7. To modify the security scopes and collections that are associated with a specific security
  role, choose the Security Scopes tab, select the security role, and then choose Edit.

       To associate new objects with this security role, choose Add, and select an object
       type to associate with the selected security roles. If you select Security Scope or
       Collection, check the box for one or more objects to complete that selection, and
       then choose OK.

          ７ Note

          You must configure at least one security scope.

       To remove a security scope or collection that is associated with this security role,
       select the object, and then choose Remove.

       When you have finished modifying the associated objects, choose OK.

8. Choose OK to complete this procedure.

    Ｕ Caution

<!-- p.1273 -->

       When a security role grants administrative users the collection deployment
       permission, those administrative users can distribute objects from any security scope
       for which they have object read permissions, even if that security scope is associated
       with a different security role.

Automate with Windows PowerShell
You can use the following PowerShell cmdlets to automate some of these tasks:

Manage administrative users:

     Get-CMAdministrativeUser: Get an administrative user object.
     New-CMAdministrativeUser: Create a new administrative user.
     New-CMAdministrativeUserPermission: {{ Fill in the Synopsis }}
     Remove-CMAdministrativeUser: Remove an administrative user.

Manage roles and scopes on users:

     Add-CMSecurityRoleToAdministrativeUser: Add a security role to a user or group.
     Remove-CMSecurityRoleFromAdministrativeUser: Remove the association between a
     security role and an administrative user.
     Add-CMSecurityScopeToAdministrativeUser: Add a security scope to a user or group.
     Remove-CMSecurityScopeFromAdministrativeUser: Remove the association between a
     security scope and an administrative user.

Manage security roles:

     Copy-CMSecurityRole: Create a custom security role.
     Export-CMSecurityRole: Export a security role to an XML file.
     Get-CMSecurityRole: Get a security role.
     Import-CMSecurityRole: Import a security role from an XML file.
     Remove-CMSecurityRole: Remove custom security roles.
     Set-CMSecurityRole: Change configuration settings of a security role.

Manage permissions on security roles:

     Get-CMSecurityRolePermission: Get the permissions for a security role.
     Set-CMSecurityRolePermission: Configure a security role with specific permissions.

Manage security scopes:

     Get-CMSecurityScope: Get a security scope.
     New-CMSecurityScope: Create a security scope.

<!-- p.1274 -->

     Remove-CMSecurityScope: Remove a security scope.
     Set-CMSecurityScope: Configure a security scope.

Manage object security scope:

     Add-CMObjectSecurityScope: Add a security scope to an object.
     Get-CMObjectSecurityScope: Get the security scope for a Configuration Manager object.
     Remove-CMObjectSecurityScope: Remove a security scope from a Configuration Manager
     object.

Next steps
Role-based administration and auditing tool

Accounts used in Configuration Manager

<!-- p.1275 -->

Configure Azure services for use with
Configuration Manager
Article • 11/16/2023

Applies to: Configuration Manager (current branch)

Use the Azure Services Wizard to simplify the process of configuring the Azure cloud
services you use with Configuration Manager. This wizard provides a common
configuration experience by using Microsoft Entra web app registrations. These apps
provide subscription and configuration details, and authenticate communications with
Microsoft Entra ID. The app replaces entering this same information each time you set
up a new Configuration Manager component or service with Azure.

Available services
Configure the following Azure services using this wizard:

      Cloud Management: This service enables the site and clients to authenticate by
      using Microsoft Entra ID. This authentication enables other scenarios, such as:

         Install and assign Configuration Manager clients using Microsoft Entra ID for
         authentication

         Configure Microsoft Entra user Discovery

         Configure Microsoft Entra user Group Discovery

         Support certain cloud management gateway scenarios

            Tip

           For more information specific to cloud management, see Configure
           Microsoft Entra ID for cloud management gateway.

         App approval email notifications

      Log Analytics Connector: Connect to Azure Log Analytics. Sync collection data to
      Log Analytics.

        ） Important

<!-- p.1276 -->

        This article refers to the Log Analytics Connector, which was formerly called
        the OMS Connector. This feature was deprecated in November 2020. It's
        removed from Configuration Manager in version 2107. For more information,
        see Removed and deprecated features.

     Microsoft Store for Business: Connect to the Microsoft Store for Business. Get
     store apps for your organization that you can deploy with Configuration Manager.

     Administration Service Management: When configuring Azure Services, for
     enhanced security you can select Administration Service Management option.
     Selecting this option allows administrators to segment their admin privileges
     between cloud management and administration service. By enabling this option,
     access is restricted to only administration service endpoints. Configuration
     Management clients will authenticate to the site using Microsoft Entra ID. (version
     2207 or later)

        ７ Note

        Only CMG VMSS customers can enable administrative service management
        option. This option is not applicable for classic CMG customers.

Service details
The following table lists details about each of the services.

     Tenants: The number of service instances you can configure. Each instance must be
     a distinct Microsoft Entra tenant.

     Clouds: All services support the global Azure cloud, but not all services support
     private clouds, such as the Azure US Government cloud.

     Web app: Whether the service uses a Microsoft Entra app of type Web app / API,
     also referred to as a server app in Configuration Manager.

     Native app: Whether the service uses a Microsoft Entra app of type Native, also
     referred to as a client app in Configuration Manager.

     Actions: Whether you can import or create these apps in the Configuration
     Manager Azure Services Wizard.

                                                                           ﾉ   Expand table

<!-- p.1277 -->

 Service                     Tenants    Clouds            Web app   Native app   Actions

 Cloud management with       Multiple   Public, Private                          Import, Create
 Microsoft Entra discovery

 Log Analytics Connector     One        Public, Private                          Import

 Microsoft Store for         One        Public                                   Import, Create
 Business

About Microsoft Entra apps
Different Azure services require distinct configurations, which you make in the Azure
portal. Additionally, the apps for each service can require separate permissions to Azure
resources.

You can use a single app for more than one service. There's only one object to manage
in Configuration Manager and Microsoft Entra ID. When the security key on the app
expires, you only have to refresh one key.

When you create additional Azure services in the wizard, Configuration Manager is
designed to reuse information that's common between services. This behavior helps you
from needing to input the same information more than once.

For more information about the required app permissions and configurations for each
service, see the relevant Configuration Manager article in Available services.

For more information about Azure apps, start with the following articles:

     Authentication and authorization in Azure App Service
     Web Apps overview
     Basics of Registering an Application in Microsoft Entra ID
     Register your application with your Microsoft Entra tenant

Before you begin
After you decide the service to which you want to connect, refer to the table in Service
details. This table provides information you need to complete the Azure Service Wizard.
Have a discussion in advance with your Microsoft Entra administrator. Decide which of
the following actions to take:

     Manually create the apps in advance in the Azure portal. Then import the app
     details into Configuration Manager.

<!-- p.1278 -->

           Tip

          For more information specific to cloud management, see Manually register
          Microsoft Entra apps for the cloud management gateway.

     Use Configuration Manager to directly create the apps in Microsoft Entra ID. To
     collect the necessary data from Microsoft Entra ID, review the information in the
     other sections of this article.

Some services require the Microsoft Entra apps to have specific permissions. Review the
information for each service to determine any required permissions. For example, before
you can import a web app, an Azure administrator must first create it in the Azure
portal     .

When configuring the Log Analytics Connector, give your newly registered web app
contributor permission on the resource group that contains the relevant workspace. This
permission allows Configuration Manager to access that workspace. When assigning the
permission, search for the name of the app registration in the Add users area of the
Azure portal. This process is the same as when providing Configuration Manager with
permissions to Log Analytics. An Azure administrator must assign these permissions
before you import the app into Configuration Manager.

Start the Azure Services wizard
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Cloud Services, and select the Azure Services node.

   2. On the Home tab of the ribbon, in the Azure Services group, select Configure
     Azure Services.

   3. On the Azure Services page of the Azure Services Wizard:

         a. Specify a Name for the object in Configuration Manager.

     b. Specify an optional Description to help you identify the service.

         c. Select the Azure service that you want to connect with Configuration Manager.

   4. Select Next to continue to the Azure app properties page of the Azure Services
     Wizard.

Azure app properties

<!-- p.1279 -->

On the App page of the Azure Services Wizard, first select the Azure environment from
the list. Refer to the table in Service details for which environment is currently available
to the service.

The rest of the App page varies depending upon the specific service. Refer to the table
in Service details for which type of app the service uses, and which action you can use.

     If the app supports both import and creates actions, select Browse. This action
     opens the Server app dialog or the Client App dialog.

     If the app only supports the import action, select Import. This action opens the
     Import Apps dialog (server) or the Import Apps dialog (client).

After you specify the apps on this page, select Next to continue to the Configuration or
Discovery page of the Azure Services Wizard.

Web app
This app is the Microsoft Entra ID type Web app / API, also referred to as a server app in
Configuration Manager.

Server app dialog
When you select Browse for the Web app on the App page of the Azure Services
Wizard, it opens the Server app dialog. It displays a list that shows the following
properties of any existing web apps:

     Tenant friendly name
     App friendly name
     Service Type

There are three actions you can take from the Server app dialog:

     To reuse an existing web app, select it from the list.
     Select Import to open the Import apps dialog.
     Select Create to open the Create Server Application dialog.

After you select, import or create a web app, select OK to close the Server app dialog.
This action returns to the App page of the Azure Services Wizard.

Import apps dialog (server)

<!-- p.1280 -->

When you select Import from the Server app dialog or the App page of the Azure
Services Wizard, it opens the Import apps dialog. This page lets you enter information
about a Microsoft Entra web app that is already created in the Azure portal. It imports
metadata about that web app into Configuration Manager. Specify the following
information:

     Microsoft Entra tenant Name: The name of your Microsoft Entra tenant.
     Microsoft Entra tenant ID: The GUID of your Microsoft Entra tenant.
     Application Name: A friendly name for the app, the display name in the app
     registration.
     Client ID: The Application (client) ID value of the app registration. The format is a
     standard GUID.
     Secret Key: You have to copy the secret key when you register the app in Microsoft
     Entra ID.
     Secret Key Expiry: Select a future date from the calendar.
     App ID URI: This value needs to be unique in your Microsoft Entra tenant. It's in
     the access token used by the Configuration Manager client to request access to
     the service. The value is the Application ID URI of the app registration entry in the
     Microsoft Entra admin center.

After entering the information, select Verify. Then select OK to close the Import apps
dialog. This action returns to either the App page of the Azure Services Wizard, or the
Server app dialog.

  ） Important

  When you use an imported Microsoft Entra app, you aren't notified of an upcoming
  expiration date from console notifications.

Create Server Application dialog

When you select Create from the Server app dialog, it opens the Create Server
Application dialog. This page automates the creation of a web app in Microsoft Entra ID.
Specify the following information:

     Application Name: A friendly name for the app.

     HomePage URL: This value isn't used by Configuration Manager, but required by
     Microsoft Entra ID. By default this value is https://ConfigMgrService .

     App ID URI: This value needs to be unique in your Microsoft Entra tenant. It's in
     the access token used by the Configuration Manager client to request access to
