---
title: "Core infrastructure documentation — pages 1561-1600"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1561-1600
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1561-1600
family: sccm
documentKind: "doc"
abstract: "Reference for maintenance tasks in Configuration Manager Article • 10/04/2022 Applies to: Configuration Manager (current branch) This article lists the details for each of the Configuration Manager site maintenance tasks. Each entry specifies the site types where the task is ava"
---

# Core infrastructure documentation — pages 1561-1600

<!-- p.1561 -->

Reference for maintenance tasks in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article lists the details for each of the Configuration Manager site maintenance
tasks. Each entry specifies the site types where the task is available, and whether it's
enabled by default.

For more information, see Set up maintenance tasks.

Tasks

Backup Site Server
Use this task to create a backup of your critical information to restore a site and the
Configuration Manager database. For more information, see Back up a Configuration
Manager site.

                                                                              ﾉ   Expand table

 Site type                                                    Status

 Central administration site                                  Enabled

 Primary site                                                 Not enabled

 Secondary site                                               Not available

Check Application Title with Inventory Information
Use this task to maintain consistency of software titles between software inventory and
the Asset Intelligence catalog. For more information, see Introduction to Asset
Intelligence.

                                                                              ﾉ   Expand table

 Site type                                                    Status

 Central administration site                                  Enabled

<!-- p.1562 -->

 Site type                                                    Status

 Primary site                                                 Not available

 Secondary site                                               Not available

Clear Undiscovered Clients

   Tip

  You may also see this task in the console named Clear Install Flag.

Use this task to remove the installed flag for clients that don't submit a Heartbeat
Discovery record during the Client Rediscovery period. The installed flag prevents
automatic client push installation to a computer that might have an active Configuration
Manager client. The default value is 21 days.

  ） Important

  Make sure this value is greater than the interval for Heartbeat discovery, which by
  default is seven days. Otherwise, clients will unnecessarily reinstall.

                                                                              ﾉ   Expand table

 Site type                                                    Status

 Central administration site                                  Not available

 Primary site                                                 Not enabled

 Secondary site                                               Not available

Delete Aged Application Request Data
Use this task to delete aged application requests from the database. For more
information, see Create and deploy an application.

                                                                              ﾉ   Expand table

 Site type                                                    Status

 Central administration site                                  Not available

<!-- p.1563 -->

 Site type                                                  Status

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Unused Application Revisions
Use this task to delete application revisions that are no longer referenced. For more
information, see How to revise and supersede applications.

                                                                             ﾉ   Expand table

 Site type                                                   Status

 Central administration site                                 Enabled

 Primary site                                                Enabled

 Secondary site                                              Not available

Delete Aged Client Download History
Use this task to delete historical data about the download source used by clients. The
site uses download source information to populate the Client Data Sources dashboard.

                                                                             ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Client Operations
Use this task to delete from the site database all aged data for client operations. For
example, this data includes the following operations:

     Aged or expired client notifications, like download requests for machine or user
     policy

<!-- p.1564 -->

     Endpoint Protection, like requests by an administrative user for clients to run a
     scan or download updated definitions
     Run Scripts status results

                                                                               ﾉ   Expand table

 Site type                                                     Status

 Central administration site                                   Enabled

 Primary site                                                  Enabled

 Secondary site                                                Not available

Delete Aged Client Presence History
Use this task to delete history information about the online status of clients recorded by
client notification. It deletes information for clients with status that's older than the
specified time. For more information, see How to monitor clients.

                                                                               ﾉ   Expand table

 Site type                                                     Status

 Central administration site                                   Enabled

 Primary site                                                  Enabled

 Secondary site                                                Not available

Delete Aged Cloud Management Gateway Traffic Data
Use this task to delete from the site database all aged data about the traffic that passes
through the cloud management gateway. This data includes:

     The number of requests
     Total request bytes
     Total response bytes
     Number of failed requests
     Maximum number of concurrent requests

                                                                               ﾉ   Expand table

<!-- p.1565 -->

 Site type                                                    Status

 Central administration site                                  Enabled

 Primary site                                                 Enabled

 Secondary site                                               Not available

Delete Aged CMPivot Results
Use this task to delete from the site database aged information from clients in CMPivot
queries. For more information, see CMPivot for real-time data.

                                                                              ﾉ   Expand table

 Site type                                                   Status

 Central administration site                                 Not available

 Primary site                                                Enabled

 Secondary site                                              Not available

Delete Aged Collected Diagnostic Files
Use this task to delete collected diagnostic files. Collected client logs are stored
according to the software inventory file collection settings. The files are stored on the
site server in the Inboxes\sinv.box\FileCol directory. Delete Aged Collected Diagnostic
Files uses a default value of 14 days when looking for diagnostic files to clean up and
doesn't affect other collected files. This maintenance task is enabled by default and was
introduced in Configuration Manager version 2010. Earlier Configuration Manager
versions use the Delete Aged Collected Files task for deleting client diagnostic files.

                                                                              ﾉ   Expand table

 Site type                                                   Status

 Central administration site                                 Not available

 Primary site                                                Enabled

 Secondary site                                              Not available

Delete Aged Collected Files

<!-- p.1566 -->

Use this task to delete from the database aged information about collected files. This
task also deletes the collected files from the site server folder structure at the selected
site. By default, the five most-recent copies of collected files are stored on the site server
in the Inboxes\sinv.box\FileCol directory. For more information, see Introduction to
software inventory.

                                                                              ﾉ   Expand table

 Site type                                                    Status

 Central administration site                                  Not available

 Primary site                                                 Enabled

 Secondary site                                               Not available

Delete Aged Computer Association Data
Use this task to delete from the database aged OS deployment computer association
data. This information is used when restoring user state during a task sequence. For
more information, see Manage user state.

                                                                              ﾉ   Expand table

 Site type                                                    Status

 Central administration site                                  Not available

 Primary site                                                 Enabled

 Secondary site                                               Not available

Delete Aged Console Connection Data
This task deletes data from the site database about console connections to the site.

                                                                              ﾉ   Expand table

 Site type                                                    Status

 Central administration site                                  Enabled

 Primary site                                                 Enabled

 Secondary site                                               Not available

<!-- p.1567 -->

Delete Aged Delete Detection Data
Use this task to delete aged data from the database that has been created by extraction
views. It deletes old data change information used by external systems extracting data
from the database.

                                                                             ﾉ   Expand table

 Site type                                                   Status

 Central administration site                                 Enabled

 Primary site                                                Enabled

 Secondary site                                              Not available

Delete Aged Device Wipe Record
Use this task to delete from the database aged data about mobile device wipe actions.
For more information, see Protect data with remote wipe, lock, or passcode reset.

                                                                             ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Discovery Data
Use this task to delete aged discovery data from the database. This data can include
records from:

     Heartbeat discovery
     Network discovery
     Active Directory discovery methods: System, User, and Group

This task also removes aged devices marked as decommissioned. When this task runs at
a site, data associated with that site is deleted, and those changes replicate to other
sites. For more information, see Run discovery.

<!-- p.1568 -->

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Distribution Point Usage Stats
Use this task to delete from the database aged data for distribution points that has been
stored longer than a specified time.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Enabled

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Endpoint Protection Health Status History
Data
Use this task to delete from the database aged status information for Endpoint
Protection (EP). For more information, see How to monitor Endpoint Protection.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Enrolled Devices
Use this task to delete from the site database the aged data about mobile devices that
haven't reported any information to the site for a specified time.

<!-- p.1569 -->

This task applies to devices that are enrolled with Configuration Manager on-premises
MDM. For more information on these devices, see Supported operating systems for
clients and devices.

                                                                          ﾉ   Expand table

 Site type                                                Status

 Central administration site                              Not available

 Primary site                                             Not enabled

 Secondary site                                           Not available

Delete Aged Exchange Partnership

   Tip

    You may also see this task in the console named Delete Aged Devices
    Managed by the Exchange Server Connector.

Use this task to delete aged data about mobile devices managed by the Exchange
Server connector. The site deletes this data according to the Ignore mobile devices that
are inactive for more than (days) setting on the Discovery tab of the Exchange Server
connector properties. For more information, see Manage mobile devices with
Configuration Manager and Exchange.

                                                                          ﾉ   Expand table

 Site type                                                Status

 Central administration site                              Not available

 Primary site                                             Enabled

 Secondary site                                           Not available

Delete Aged Inventory History
Use this task to delete from the database inventory data that has been stored longer
than a specified time. For more information, see How to use Resource Explorer to view

<!-- p.1570 -->

hardware inventory.

                                                                             ﾉ    Expand table

 Site type                                                   Status

 Central administration site                                 Not available

 Primary site                                                Enabled

 Secondary site                                              Not available

Delete Aged Log Data
Use this task to delete from the database aged log data used for troubleshooting. This
data isn't related to Configuration Manager component operations.

  ） Important

  By default, this task runs daily at each site. At a central administration site and
  primary sites, the task deletes data that's older than 30 days. When you use SQL
  Server Express at a secondary site, make sure that this task runs daily and deletes
  data that's inactive for seven days.

                                                                             ﾉ    Expand table

 Site type                                                              Status

 Central administration site                                            Enabled

 Primary site                                                           Enabled

 Secondary site                                                         Enabled

Delete Aged Notification Server History
This task deletes aged client presence history.

                                                                             ﾉ    Expand table

 Site type                                                    Status

 Central administration site                                  Enabled

<!-- p.1571 -->

 Site type                                                    Status

 Primary site                                                 Enabled

 Secondary site                                               Not available

Delete Aged Notification Task History
Use this task to delete from the site database information about client notification tasks.
This task applies to data that hasn't been updated for a specified time. For more
information, see Client notifications.

                                                                              ﾉ   Expand table

 Site type                                                   Status

 Central administration site                                 Not available

 Primary site                                                Enabled

 Secondary site                                              Not available

Delete Aged Passcode Records
Use this task at the top-level site of your hierarchy to delete aged Passcode Reset data
for Windows Phone devices. Passcode Reset data is encrypted, but does include the PIN
for devices. By default, this task is enabled, and deletes data that is older than one day.

                                                                              ﾉ   Expand table

 Site type                                                    Status

 Central administration site                                  Enabled

 Primary site                                                 Enabled

 Secondary site                                               Not available

Delete Aged Replication Data
Use this task to delete from the database aged data about database replication between
Configuration Manager sites. When you change the configuration of this maintenance
task, the configuration applies to each applicable site in the hierarchy. For more
information, see Monitor database replication.

<!-- p.1572 -->

                                                                            ﾉ   Expand table

 Site type                                                            Status

 Central administration site                                          Enabled

 Primary site                                                         Enabled

 Secondary site                                                       Enabled

Delete Aged Replication Summary Data
Use this task to delete from the site database aged replication summary data when it
hasn't been updated for a specified time. For more information, see Monitor database
replication.

                                                                            ﾉ   Expand table

 Site type                                                            Status

 Central administration site                                          Enabled

 Primary site                                                         Enabled

 Secondary site                                                       Enabled

Delete Aged Scenario Health History
Use this task to delete from the database aged data for scenario health activity. For
more information, see Monitor scenario health.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Enabled

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Software Metering Data
Use this task to delete from the database aged data for software metering that has been
stored longer than a specified time. For more information, see Software metering.

<!-- p.1573 -->

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Software Metering Summary Data
Use this task to delete from the database aged summary data for software metering
that's been stored longer than a specified time. For more information, see Software
metering.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Status Messages
Use this task to delete from the database aged status message data as configured in
status filter rules. For more information, see Monitor the status system.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Enabled

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Threat Data
Use this task to delete from the database aged Endpoint Protection threat data that's
been stored longer than a specified time. For more information, see Endpoint

<!-- p.1574 -->

Protection.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Unknown Computers
Use this task to delete information about unknown computers from the site database
when it hasn't been updated for a specified time. For more information, see Prepare for
unknown computer deployments.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged User Device Affinity Data
Use this task to delete aged User Device Affinity data from the database. For more
information, see Link users and devices with user device affinity.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Aged Task Execution Status Messages

<!-- p.1575 -->

Use this task to delete added task execution status messages on primary site servers. By
default, it has been set to run on Saturday and delete the data older than 30 days. It
does so by cleaning up [dbo].TaskExecutionStatus table.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Duplicate System Discovery Data
Use this task to delete from the site database any duplicate records generated by
system discovery.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Enabled

 Primary site                                               Not available

 Secondary site                                             Not available

Delete Expired MDM Bulk Enroll Package Records
Use this task to delete old Bulk Enrollment certificates and corresponding profiles after
the enrollment certificate has expired. For more information, see Create certificate
profiles.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Enabled

 Primary site                                               Enabled

 Secondary site                                             Not available

<!-- p.1576 -->

Delete Inactive Client Discovery Data
Use this task to delete from the database discovery data for inactive clients. The site
marks clients as inactive when the client is flagged as obsolete and by configurations
that are made for client status.

This task operates only on resources that are Configuration Manager clients. It's
different than the Delete Aged Discovery Data task, which deletes any aged discovery
data record. When this task runs at a site, it removes the data from the database at all
sites in a hierarchy. For more information, see How to configure client status.

  ） Important

  When it's enabled, configure this task to run at an interval greater than the
  Heartbeat Discovery schedule. This configuration enables active clients to send a
  Heartbeat Discovery record to mark their client record as active so this task doesn't
  delete them.

                                                                             ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Not enabled

 Secondary site                                             Not available

Delete Obsolete Alerts
Use this task to delete from the database expired alerts that have been stored longer
than a specified time. For more information, see Configure alerts.

                                                                             ﾉ   Expand table

 Site type                                                   Status

 Central administration site                                 Enabled

 Primary site                                                Enabled

 Secondary site                                              Not available

<!-- p.1577 -->

Delete Obsolete Client Discovery Data
Use this task to delete obsolete client records from the database. A record that's marked
as obsolete has usually been replaced by a newer record for the same client. The newer
record becomes the client's current record. For information about discovery, see Run
discovery.

  ） Important

  When it's enabled, configure this task to run at an interval greater than the
  Heartbeat Discovery schedule. This configuration enables the client to send a
  Heartbeat Discovery record that correctly sets the obsolete status.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not available

 Primary site                                               Not enabled

 Secondary site                                             Not available

Delete Obsolete Forest Discovery Sites and Subnets
Use this task to delete data about Active Directory sites, subnets, and domains. It
removes data that the site hasn't discovered by the Active Directory Forest Discovery
method in the last 30 days. This task removes the discovery data, but doesn't affect
boundaries that you create from this discovery data. For more information, see Run
discovery.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Enabled

 Primary site                                               Enabled

 Secondary site                                             Not available

Delete Orphaned Client Deployment State Records

<!-- p.1578 -->

Use this task to periodically purge the table that contains client deployment state
information. This task cleans up records associated with obsolete or decommissioned
devices.

                                                                            ﾉ   Expand table

 Site type                                                 Status

 Central administration site                               Not available

 Primary site                                              Enabled

 Secondary site                                            Not available

Evaluate Collection Members
You configure the Collection Membership Evaluation as a site component. For more
information, see Site components.

                                                                            ﾉ   Expand table

 Site type                                                 Status

 Central administration site                               Not available

 Primary site                                              Enabled

 Secondary site                                            Not available

Monitor Keys
Use this task to monitor the integrity of the Configuration Manager database primary
keys. A primary key is a column or a combination of columns that uniquely identifies
one row. The key distinguishes the row from any other row in a Microsoft SQL Server
database table.

                                                                            ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Enabled

 Primary site                                               Enabled

 Secondary site                                             Not available

<!-- p.1579 -->

Rebuild Indexes
Use this task to rebuild the Configuration Manager database indexes. An index is a
database structure that's created on a database table to speed up data retrieval. For
example, searching an indexed column is often much faster than searching a column
that isn't indexed.

To improve performance, the Configuration Manager database indexes are frequently
updated to remain synchronized with the constantly changing data that's stored in the
database. This task:

     Rebuilds indexes when they are more than 10% fragmented
         For indexes that are less than 30% fragmented, the index is reorganized
         For indexes that are greater than 30% fragmented, the index is rebuilt

                                                                           ﾉ   Expand table

 Site type                                                  Status

 Central administration site                                Not enabled

 Primary site                                               Not enabled

 Secondary site                                             Not enabled

Summarize Installed Software Data
Use this task to summarize the data from collected asset intelligence software
information through the hardware inventory to merge multiple records into one general
record. Data summarization can compress the amount of data that's stored in the
Configuration Manager database. For more information, see Configure Asset
Intelligence maintenance tasks.

                                                                           ﾉ   Expand table

 Site type                                                 Status

 Central administration site                               Not available

 Primary site                                              Enabled

 Secondary site                                            Not available

Summarize Software Metering File Usage Metering Data

<!-- p.1580 -->

Use this task to summarize the data from multiple records for software metering file
usage into one general record. Data summarization can compress the amount of data
that's stored in the Configuration Manager database.

To summarize software metering data and to conserve disk space in the database, use
this task with the Summarize Software Metering Monthly Usage Data task. For more
information, see Software metering.

                                                                          ﾉ   Expand table

 Site type                                                Status

 Central administration site                              Not available

 Primary site                                             Enabled

 Secondary site                                           Not available

Summarize Software Metering Monthly Usage Data
Use this task to summarize the data from multiple records for software metering
monthly usage into one general record. Data summarization can compress the amount
of data that's stored in the Configuration Manager database.

To summarize software metering data and to conserve space in the database, use this
task with the Summarize Software Metering File Usage Data task. For more
information, see Software metering.

                                                                          ﾉ   Expand table

 Site type                                                Status

 Central administration site                              Not available

 Primary site                                             Enabled

 Secondary site                                           Not available

Update Application Available Targeting
Use this task to have Configuration Manager recalculate the mapping of policy and
application deployments to resources in collections. When you deploy policy or
applications to a collection, Configuration Manager creates an initial mapping between
the objects that you deploy and the collection members.

<!-- p.1581 -->

These mappings are stored in a table for quick reference. When a collections
membership changes, the site updates these stored mappings to reflect those changes.
However, it's possible for these mappings to fall out of sync. For example, if the site fails
to properly process a notification file, that change might not be reflected in a change to
the mappings. This task refreshes that mapping based on current collection
membership.

                                                                             ﾉ   Expand table

 Site type                                                   Status

 Central administration site                                 Not available

 Primary site                                                Enabled

 Secondary site                                              Not available

Update Application Catalog Tables
This task exists in the site, but isn't used. The application catalog is no longer supported.

See also
Maintenance tasks

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1582 -->

Modify your Configuration Manager
infrastructure
Applies to: Configuration Manager (current branch)

After you install one or more sites, you might have need to modify configurations or take actions
that affect your infrastructure.

Manage the SMS provider
The SMS provider provides the point of administrative contact for one or more Configuration
Manager consoles. When you install multiple SMS providers, you can provide redundancy for
contact points to administer your site and hierarchy.

At each Configuration Manager site, you can rerun setup to:

     Add an additional instance of the SMS provider. Each additional instance of the SMS
     provider must be on a separate computer.

     Remove an instance of the SMS provider. To remove the last SMS provider for a site, you
     must uninstall the site.

Monitor the installation or removal of the SMS provider by viewing the ConfigMgrSetup.log in
the root folder of the site server on which you run setup.

Before you modify the SMS provider at a site, see Plan for the SMS provider.

Manage the SMS provider configuration for a site
   1. Run Configuration Manager Setup from \BIN\X64\setup.exe in the Configuration Manager
     site installation folder.

   2. On the Getting Started page, select Perform site maintenance or reset this site.

   3. On the Site Maintenance page, select Modify SMS provider configuration.

   4. On the Manage SMS providers page, select one of the following options:

           Add a new SMS provider: Specify the FQDN for a computer to host the SMS provider
           that doesn't currently host it.

<!-- p.1583 -->

           Uninstall the specified SMS provider: Select the name of the computer from which
           you want to remove the SMS provider.

         Tip

        To move the SMS provider between two computers, first install it to the new computer.
        Then remove it from the original location. There's no option to move the SMS provider
        between computers.

After the setup wizard finishes, the SMS provider configuration is complete. In the site Properties,
on the General tab, verify the computers that have an SMS provider installed for a site.

Manage the Configuration Manager console
The following tasks help you manage the Configuration Manager console:

     To modify the language that displays in the Configuration Manager console, see the
     Manage Configuration Manager console language section.

     To install additional consoles, see Install Configuration Manager consoles.

     To configure DCOM permissions to enable consoles that are remote from the site server, see
     the Configure DCOM permissions for remote Configuration Manager consoles section.

     To modify administrative permissions to limit what users can see and do in the console, see
     Modify the administrative scope of an administrative user.

Manage Configuration Manager console language
During site server installation, the Configuration Manager console installation files and supported
language packs for the site are copied to the \Tools\ConsoleSetup subfolder of the Configuration
Manager installation path on the site server.

     When you start the Configuration Manager console installation from this folder on the site
     server, it copies the Configuration Manager console and supported language pack files to
     the computer.

     When a language pack is available for the current language setting on the computer, the
     Configuration Manager console opens in that language.

<!-- p.1584 -->

     If the associated language pack isn't available for the Configuration Manager console, the
     console opens in English (United States).

For example, you install the Configuration Manager console from a site server that supports
English, German, and French. If you open the Configuration Manager console on a computer with
a configured language setting of French, the console opens in French. If you open the
Configuration Manager console on a computer with a configured language of Japanese, the
console opens in English because the Japanese language pack isn't available.

Each time the Configuration Manager console opens:

     It determines the configured language settings for the computer
     Verifies whether an associated language pack is available for the Configuration Manager
     console
     Opens the console by using the appropriate language pack

When you want to open the Configuration Manager console in English regardless of the
configured language settings on the computer, remove or rename the language pack files on the
computer.

Use the following procedures to start the Configuration Manager console in English regardless of
the configured locale setting on the computer.

Install an English-only version of the Configuration Manager console
on computers

   1. In Windows Explorer, browse to \Tools\ConsoleSetup\LanguagePack in the Configuration
     Manager installation path.

   2. Rename the .msp and .mst files. For example, you could change <file name>.MSP to <file
     name>.MSP.disabled.

   3. Install the Configuration Manager console on the computer.

       ） Important

       When new server languages are configured for the site server, the .msp and .mst files
       are recopied to the LanguagePack folder, and you must repeat this procedure to install
       new Configuration Manager consoles in only English.

<!-- p.1585 -->

Temporarily disable a console language on an existing Configuration
Manager console installation

   1. On the computer that is running the Configuration Manager console, close the
     Configuration Manager console.

   2. In Windows Explorer, browse to <ConsoleInstallationPath>\Bin\ on the Configuration
     Manager console computer.

   3. Rename the appropriate language folder for the language that is configured on the
     computer. For example, if the language settings for the computer were set for German, you
     could rename the de folder to de.disabled.

   4. To open the Configuration Manager console in the language that is configured for the
     computer, rename the folder to the original name. For example, rename de.disabled to de.

Configure DCOM permissions for remote consoles
The user account that runs the Configuration Manager console requires permission to access the
site database by using the SMS provider. However, an administrative user who uses a remote
Configuration Manager console also requires Remote Activation DCOM permissions on:

     The site server computer

     Each computer that hosts an instance of the SMS provider

The security group named SMS Admins grants access to the SMS provider on a computer, and
can also be used to grant the required DCOM permissions. This group is local to the computer
when the SMS provider runs on a member server. It's a domain local group when the SMS
provider runs on a domain controller.

  ） Important

  The Configuration Manager console uses WMI to connect to the SMS provider, and WMI
  internally uses DCOM. If the Configuration Manager console runs on a computer other than
  the SMS provider computer, it requires permissions to activate a DCOM server on the SMS
  provider computer. By default, Remote Activation is granted only to the members of the
  built-in Administrators group.

  If you allow the SMS Admins group to have Remote Activation permission, a member of this
  group could attempt DCOM attacks against the SMS provider computer. This configuration

<!-- p.1586 -->

  also increases the attack surface of the computer. To mitigate this threat, carefully monitor
  the membership of the SMS Admins group.

Use the following procedure to configure each central administration site (CAS), primary site
server, and each computer where the SMS provider is installed to grant remote Configuration
Manager console access for administrative users.

Configure DCOM permissions for remote Configuration
Manager console connections
   1. As an administrator on the target computer, run Dcomcnfg.exe to open Component
     Services.

   2. Expand Component Services, expand Computers, and then select My Computer. On the
     Action menu, select Properties.

   3. In the My Computer Properties window, switch to the COM Security tab. In the Launch and
     Activation Permissions section, select Edit Limits.

   4. In the Launch and Activation Permissions window, select Add.

   5. In the Select Users, Computers, Service Accounts, or Groups window, in the Enter the
     object names to select field, type SMS Admins , and then select OK.

        Tip

       To locate the SMS Admins group, you might have to change the setting: From this
       Location. This group is local to the computer when the SMS provider runs on a
       member server, and is a domain local group when the SMS provider runs on a domain
       controller.

   6. In the Permissions for SMS Admins section, to allow remote activation, select the Allow
     column for the Remote Activation row.

   7. Select OK to save changes and close all windows.

Your computer is now configured to allow remote Configuration Manager console access to
members of the SMS Admins group.

<!-- p.1587 -->

Repeat this procedure on each SMS provider computer that supports remote Configuration
Manager consoles.

Modify the site database configuration
After you install a site, you can modify the configuration of the site database and site database
server. Run Configuration Manager setup on a CAS server or primary site server to make changes.
You can move the site database to a new instance of SQL Server on the same computer, or to a
different computer that runs a supported version of SQL Server. These changes aren't supported
for the database configuration at secondary sites.

For more information about the limits of support, see Support policy for manual database
changes in a Configuration Manager environment       .

  ７ Note

  When you modify the database configuration for a site, Configuration Manager restarts or
  reinstalls Configuration Manager services on the site server and remote site system servers
  that communicate with the database.

Modify the database configuration
Run Configuration Manager setup on the site server, and select the option Perform site
maintenance or reset this site. Then select the Modify SQL Server configuration option. You can
change the following site database configurations:

     The Windows-based server that hosts the database.

     The instance of SQL Server in use on a server that hosts the SQL Server database.

     The database name.

     SQL Server port in use by Configuration Manager.

     SQL Server Service Broker port in use by Configuration Manager.

  ） Important

  The Modify SQL Server configuration maintenance path doesn't run the SQL Server
  collation prerequisite check that a new install or upgrade performs. Before you continue,

<!-- p.1588 -->

  verify that the target SQL Server instance and the site database both use the required
  collation, SQL_Latin1_General_CP1_CI_AS. Moving or pointing the site to an instance or
  database that uses a different collation can corrupt data and cause site failures that might
  not appear immediately. The only exceptions are the two China GB18030 collations. For
  more information, see SQL Server instance and database collations and International
  support. To verify the configuration, run the verification script.

Move the site database
If you move the site database, also review the following configurations:

     When you move the site database to a new computer, add the computer account of the site
     server to the local Administrators group on the computer that runs SQL Server. If you use a
     SQL Server Always On failover cluster instance for the site database, add the computer
     account to the local Administrators group of each Windows Server cluster node computer.

     When you move the database to a new instance on SQL Server, or to a new SQL Server
     computer, enable common language runtime (CLR) integration. Use SQL Server
     Management Studio to connect to the instance of SQL Server that hosts the site database.
     Then run the following stored procedure as a query: sp_configure 'clr enabled',1;
     reconfigure

     Confirm the target SQL Server instance and site database use the required collation before
     you move. This maintenance path doesn't enforce the collation prerequisite check, so verify
     it yourself by running the verification script. For details, see the collation requirement in the
     Modify the database configuration section.

     Make sure the new SQL Server has access to the backup location. When you use a UNC for
     storing your site database backup, after moving the database to a new server, make sure
     the computer account of the new SQL Server has write permissions to the UNC location.
     This configuration includes when you move to a SQL Server Always On availability group or
     a failover cluster instance.

  ） Important

  Before you move a database that has one or more database replicas for management points,
  first remove the database replicas. After you complete the database move, you can

<!-- p.1589 -->

  reconfigure database replicas. For more information, see Database replicas for
  management points.

Verify SQL Server configuration before you move the site database

Before you run Modify SQL Server configuration, use SQL Server Management Studio to
connect to the target site database, and run the following verification script against the site
database ( CM_<sitecode> ), not the master database. Resolve every ERROR: line before you
continue. Both the SQL Server instance and the site database must use the
SQL_Latin1_General_CP1_CI_AS collation. This script also confirms the other configurations that

Configuration Manager requires for the site database.

 SQL

 SET NOCOUNT ON

 DECLARE @dbname NVARCHAR(128)

 SELECT @dbname = sd.name FROM sys.sysdatabases sd WHERE sd.dbid = DB_ID()

 IF (@dbname = N'master' OR @dbname = N'model' OR @dbname = N'msdb' OR @dbname =
 N'tempdb' OR @dbname = N'distribution' ) BEGIN
     RAISERROR(N'ERROR: Script is targeting a system database. It should be targeting
 the site database instead.', 0, 1)
     GOTO Branch_Exit;
 END ELSE
     PRINT N'INFO: Targeted database is ' + @dbname + N'.'

 PRINT N'INFO: Running verifications....'

 IF CONVERT(NVARCHAR(128), SERVERPROPERTY('Collation')) <>
 N'SQL_Latin1_General_CP1_CI_AS'
      PRINT N'ERROR: SQL Server instance collation is ' + CONVERT(NVARCHAR(128),
 SERVERPROPERTY('Collation')) + N' (must be SQL_Latin1_General_CP1_CI_AS)!'
 ELSE
      PRINT N'PASS: SQL Server instance collation is SQL_Latin1_General_CP1_CI_AS.'

 IF CONVERT(NVARCHAR(128), DATABASEPROPERTYEX(@dbname, 'Collation')) <>
 N'SQL_Latin1_General_CP1_CI_AS'
      PRINT N'ERROR: Database collation is ' + CONVERT(NVARCHAR(128),
 DATABASEPROPERTYEX(@dbname, 'Collation')) + N' (must be
 SQL_Latin1_General_CP1_CI_AS)!'
 ELSE
      PRINT N'PASS: Database collation is SQL_Latin1_General_CP1_CI_AS.'

 IF NOT EXISTS (SELECT * FROM sys.configurations c WHERE c.name = 'clr enabled' AND
 c.value_in_use = 1)
      PRINT N'ERROR: CLR is not enabled!'
 ELSE

<!-- p.1590 -->

      PRINT N'PASS: CLR is enabled.'

 DECLARE @repltable TABLE (
     name nvarchar(max),
     minimum int,
     maximum int,
     config_value int,
     run_value int )

 INSERT INTO @repltable
 EXEC sp_configure 'max text repl size (B)'

 IF NOT EXISTS(SELECT * from @repltable where config_value = 2147483647 and run_value
 = 2147483647 )
      PRINT N'ERROR: Max text repl size is not correct!'
 ELSE
      PRINT N'PASS: Max text repl size is correct.'

 IF NOT EXISTS (SELECT db.owner_sid FROM sys.databases db WHERE db.database_id =
 DB_ID() AND db.owner_sid = 0x01)
      PRINT N'ERROR: Database owner is not sa account!'
 ELSE
      PRINT N'PASS: Database owner is sa account.'

 IF NOT EXISTS( SELECT * FROM sys.databases db WHERE db.database_id = DB_ID() AND
 db.is_trustworthy_on = 1 )
      PRINT N'ERROR: Trustworthy bit is not on!'
 ELSE
      PRINT N'PASS: Trustworthy bit is on.'

 IF NOT EXISTS( SELECT * FROM sys.databases db WHERE db.database_id = DB_ID() AND
 db.is_broker_enabled = 1 )
      PRINT N'ERROR: Service broker is not enabled!'
 ELSE
      PRINT N'PASS: Service broker is enabled.'

 IF NOT EXISTS( SELECT * FROM sys.databases db WHERE db.database_id = DB_ID() AND
 db.is_honor_broker_priority_on = 1 )
      PRINT N'ERROR: Service broker priority is not set!'
 ELSE
      PRINT N'PASS: Service broker priority is set.'

 PRINT N'Done!'

 Branch_Exit:

Manage the SPN for the site database server
You can choose the account that runs SQL Server services for the site database:

     When the services run with the computers system account, it automatically registers the
     service principal name (SPN) for you.

<!-- p.1591 -->

     When the services run with a domain local user account, manually register the SPN. The SPN
     allows SQL Server clients and other site systems to authenticate with Kerberos. Without
     Kerberos authentication, communication to the database might fail.

For more information about SPNs and Kerberos connections, see Register a service principal
name for Kerberos connections.

Register an SPN for the SQL Server service account of the site database server by using the
Setspn tool. Run Setspn as a Domain Administrator on a computer in the same domain as the
SQL Server.

The following procedures are examples of how to manage the SPN for the SQL Server service
account. For more information about Setspn, see Setspn Overview.

Manually create a domain user SPN for the SQL Server
service account
   1. Open a command prompt as an administrator.

   2. Enter a valid command to create the SPN for both the NetBIOS name and the FQDN:

       ） Important

       When you create an SPN for a SQL Server Always On failover cluster instance, specify
       the virtual name of the failover cluster instance as the SQL Server computer name.

          NetBIOS name: setspn -A MSSQLSvc/<SQL Server computer name>:<port>
          <Domain\Account>

          For example: setspn -A MSSQLSvc/sqlserver:1433 contoso\sqlservice

          FQDN: setspn -A MSSQLSvc/<SQL Server FQDN>:<port> <Domain\Account>

          For example: setspn -A MSSQLSvc/sqlserver.contoso.com:1433 contoso\sqlservice

       ７ Note

       The command to register an SPN for a SQL Server named instance is the same as that
       you use when you register an SPN for a default instance. The only exception is that the
       port number must match the port that the named instance uses.

<!-- p.1592 -->

Verify the domain user SPN is registered correctly
   1. Open a command prompt as an administrator.

   2. Enter the following command: setspn -L <domain\SQL Server service account>

     For example: setspn -L contoso\sqlservice

   3. Review the registered ServicePrincipalName. Make sure that you created a valid SPN for
     the SQL Server.

Change the SQL Server service account from local system to a
domain user account
   1. Create or select a domain or local system user account that you want to use as the SQL
     Server service account.

   2. Open SQL Server Configuration Manager.

   3. Select SQL Server Services, and then open SQL Server<INSTANCE NAME>.

   4. Switch to the Log on tab. Select This account, and then enter the user name and password
     for the domain user account from step 1.

   5. Confirm the service account change and restart the SQL Server service.

Run a site reset
When a site reset runs at a CAS or primary site, the site:

     Reapplies the default Configuration Manager file and registry permissions

     Reinstalls all site components and all site system roles

Secondary sites don't support site reset.

You can manually reset a site. They can also run automatically after you modify the site
configuration. For example:

     If there has been a change to the accounts used by Configuration Manager components,
     consider a manual site reset. This action makes sure the site components update to use the
     new account details.

<!-- p.1593 -->

     If you modify the client or server languages at a site, Configuration Manager automatically
     runs a site reset. The site requires a reset to use the new languages.

  ７ Note

  A site reset doesn't reset access permissions to non-Configuration Manager objects.

What happens during a site reset
When a site reset runs:

   1. Setup stops and restarts the SMS_SITE_COMPONENT_MANAGER service and the thread
     components of the SMS_EXECUTIVE service.

   2. Setup removes and recreates the site system share folder and the SMS Executive
     component on the local computer and on remote site system computers.

   3. Setup restarts the SMS_SITE_COMPONENT_MANAGER service, which installs the
     SMS_EXECUTIVE and the SMS_SQL_MONITOR services.

Site reset restores the following objects:

     The SMS or NAL registry keys, and any default subkeys under these keys.

     The Configuration Manager file directory tree, and any default files or subdirectories in this
     file directory tree.

Prerequisites for site reset
The account that you use to reset a site must have the following permissions:

     To reset the CAS:

        A local Administrator on the CAS server

        Privileges that are equivalent to the Full Administrator role-based administration security
        role

     To reset a primary site:

        A local Administrator on the primary site server

<!-- p.1594 -->

          Privileges that are equivalent to the Full Administrator role-based administration security
          role

          If the primary site is in a hierarchy with a CAS, this account must also be a local
          Administrator on the CAS server.

Limitations for a site reset
If the hierarchy is configured to support testing client upgrades in a pre-production collection,
you can't use a site reset to change the server or client language packs at sites.

Run a site reset
   1. Start Configuration Manager setup on the site server by using one of the following
        methods:

            On the Start menu, select Configuration Manager Setup.

            In the directory for the Configuration Manager installation media, open
             \SMSSETUP\BIN\X64\setup.exe . Make sure this version is the same as the site version.

            In the directory where Configuration Manager is installed, open \BIN\X64\setup.exe .

   2. On the Getting Started page, select Perform site maintenance or reset this site.

   3. On the Site Maintenance page, select Reset site with no configuration changes.

   4. Select Yes to begin the site reset.

Manage language packs at a site
After a site installs, you can change the server and client language packs that are in use.

Server language packs
Applies to: Configuration Manager console installations, new installations of applicable site system
roles

After you update the server language packs at a site, you can add support for the language packs
to Configuration Manager consoles.

To add support for a server language pack to a Configuration Manager console, install the
Configuration Manager console from the ConsoleSetup folder on a site server that includes the

<!-- p.1595 -->

language pack that you want to use. If the Configuration Manager console is already installed,
you must first uninstall it to enable the new installation to identify the current list of supported
language packs.

Client language packs
Changes to the client language packs update the client installation source files. New client
installations and upgrades add support for the updated list of client languages.

After you update the client language packs at a site, install each client that will use the language
packs by using source files that include the client language packs.

For more information about the client and server languages that Configuration Manager
supports, see Language Packs.

Modify the supported language packs at a site
   1. Start Configuration Manager setup on the site server by using one of the following
     methods:

           On the Start menu, select Configuration Manager Setup.

           In the directory for the Configuration Manager installation media, open
           \SMSSETUP\BIN\X64\setup.exe . Make sure this version is the same as the site version.

           In the directory where Configuration Manager is installed, open \BIN\X64\setup.exe .

   2. On the Getting Started page, select Perform site maintenance or reset this Site.

   3. On the Site Maintenance page, select Modify language configuration.

   4. On the Prerequisites Downloads page, select one of the following options:

           Download required files: Acquire updates to language packs.

           Use previously downloaded files: Use previously downloaded files that include the
           language packs you want to add to the site.

   5. On the Server Language Selection page, select the server languages this site supports.

   6. On the Client Language Selection page, select the client languages that this site supports.

   7. Complete the wizard to modify language support at the site.

<!-- p.1596 -->

         ７ Note

         Configuration Manager initiates a site reset which also reinstalls all site system roles at
         the site.

Modify the database server alert threshold
By default, Configuration Manager generates alerts when free disk space on a site database
server is low:

      Generate a warning when there's 10 GB or less of free disk space
      Generate a critical alert when there's 5 GB or less of free disk space

You can modify these values or disable alerts for each site:

   1. In the Configuration Manager console, go to the Administration workspace, expand Site
      Configuration, and select the Sites node.

   2. Select the site that you want to configure. In the ribbon, select Properties.

   3. Switch to the Alert tab, and then edit the settings.

Uninstall sites and hierarchies
You may need to uninstall a Configuration Manager site system role, site, or hierarchy. For more
information, see Uninstall roles, sites, and hierarchies.

Starting in version 2002, you can also remove the CAS from a hierarchy, but keep the primary site.
For more information, see Remove the CAS.

 Last updated on 07/14/2026

<!-- p.1597 -->

The CD.Latest folder for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager has a process to deliver updates to the product from within the
Configuration Manager console. To support this new method of updating Configuration
Manager, a new folder is created named CD.Latest . This folder contains a copy of the
Configuration Manager installation files for the updated version of your site.

The CD.Latest folder contains a folder named Redist , which contains the
redistributable files that setup downloads and uses. These files are matched to the
version of Configuration Manager files found in that CD.Latest folder. When you run
Setup from a CD.Latest folder, you must use files that are matched to that version of
Setup. You can either direct Setup to download new and current files from Microsoft, or
direct Setup to use the files from the Redist folder included in the CD.Latest folder.

Baseline media doesn't include a Redist folder. The site doesn't create a Redist folder
until you install an in-console update. In the meantime, use the Redist folder that you
used when installing sites from the baseline media.

   Tip

  Make sure the redistributable files you use are current. If you haven't recently
  downloaded redistributable files, plan to allow Setup to do so from Microsoft.

The following scenarios create or update the CD.Latest folder on a central
administration site or primary site server:

      When you install an update or hotfix from within the Configuration Manager
      console, the site creates or updates the folder in the Configuration Manager
      installation folder.

      When you run the built-in Configuration Manager backup task, the site creates or
      updates the folder under the designated backup folder location.

      When you install a new site using baseline media, the site creates the CD.Latest
      folder.

<!-- p.1598 -->

Supported scenarios
The source files from the CD.Latest folder are supported for the following scenarios:

Backup and recovery
To recover a site, use the source files from a CD.Latest folder that matches your site.
When you run a site backup using the built-in site backup task, the CD.Latest folder is
included as part of the backup.

     When you reinstall a site as part of a site recovery, you install the site from the
     CD.Latest folder included in your backup. This action installs the site using the file

     versions that match your site backup and site database.

        If you don't have access to the correct CD.Latest folder version, get the
        CD.Latest folder with the correct file versions by installing a site in a lab

        environment. Then update that site to match the version you want to recover.

        If you don't have the correct CD.Latest folder and its contents available, you
        can't recover a site. In this circumstance, you need to reinstall the site.

     When you don't have a CD.Latest folder, but do have a working child primary site
     or central administration site, you can use that site as a reference site for a site
     recovery.

Install a child primary site
When you want to install a new child primary site below a central administration site
that has installed one or more in-console updates, use Setup and the source files from
the CD.Latest folder from the central administration site. This process uses installation
source files that match the version of the central administration site. For more
information, see Use the Setup Wizard to install sites.

Expand a stand-alone primary site
When you expand a stand-alone primary site by installing a new central administration
site, use Setup and the source files from the CD.Latest folder from the primary site. This
process uses installation source files that match the version of the primary site. For more
information, see Expand a stand-alone primary site.

Install a secondary site

<!-- p.1599 -->

When you want to install a new secondary site below a primary site that has installed
one or more in-console updates, use the source files from the CD.Latest folder from the
primary site.

For more information, see Install a secondary site.

Unsupported scenarios
The updated CD.Latest source files aren't supported for:

     Installing a new site for a new hierarchy
     Upgrading a Microsoft System Center 2012 Configuration Manager site to
     Configuration Manager current branch
     Installing Configuration Manager clients
     Installing Configuration Manager consoles

Next steps
Updates for Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1600 -->

Upgrade on-premises infrastructure that
supports Configuration Manager
Applies to: Configuration Manager (current branch)

Use the information in this article to help you upgrade the server infrastructure that runs
Configuration Manager.

     If you want to upgrade from an earlier version to Configuration Manager, current branch,
     see Upgrade to Configuration Manager.

     If you want to update your Configuration Manager, current branch, infrastructure to a new
     version, see Updates for Configuration Manager.

Upgrade the OS of site systems
Configuration Manager supports the in-place upgrade of the server OS that hosts a site server
and any site system role, in the following situations:

     If Configuration Manager still supports the resulting service pack level of Windows, it
     supports in-place upgrade to a later Windows Server service pack.

     In-place upgrade from:

        Windows Server 2022 to Windows Server 2025

        Windows Server 2019 to Windows Server 2022 or 2025

        Windows Server 2016 to Windows Server 2019, 2022, or 2025

        Windows Server 2012 R2 to Windows Server 2016, 2019, or 2025

        Windows Server 2012 to Windows Server 2016

To upgrade a server, use the upgrade procedures provided by the OS you're upgrading to. See
the following articles:

     Windows Server Upgrade Center

     Upgrade and conversion options for Windows Server 2016
