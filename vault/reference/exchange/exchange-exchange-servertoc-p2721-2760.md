---
title: "Exchange Server — pages 2721-2760"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2721-2760
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2721-2760
family: exchange
documentKind: "doc"
abstract: "Create a database availability group network in Exchange Server 07/23/2025 APPLIES TO: 2016 2019 Subscription Edition You can use the EAC or the Exchange Management Shell to create a DAG network. Looking for other management tasks related to DAGs? Check out Manage database avail"
---

# Exchange Server — pages 2721-2760

<!-- p.2721 -->

Create a database availability group
network in Exchange Server
07/23/2025

APPLIES TO:      2016      2019      Subscription Edition

You can use the EAC or the Exchange Management Shell to create a DAG network.

Looking for other management tasks related to DAGs? Check out Manage database availability
groups.

What do you need to know before you begin?
     Estimated time to complete: 1 minute

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Database availability groups"
     entry in the High availability and site resilience permissions topic.

     You can create a DAG network only when automatic network configuration has been
     disabled for a DAG. For detailed steps about how to disable automatic network
     configuration for a DAG, see Configure database availability group properties.

     When creating a DAG network, you must assign unique subnets that aren't in use by
     another DAG network. If you use subnets that are assigned to an existing DAG network,
     they will be removed from that DAG network and added to the newly created DAG
     network.

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to create a database availability group
network
   1. In the EAC, go to Servers > Database Availability Groups.

<!-- p.2722 -->

   2. Select the DAG you want to configure, and then click    .

   3. On the new database availability group network page, provide the following
     information:

           Database availability group network name: Use this field to type a name for the
           network that's unique in the DAG.

           Description: Use this field to provide a text description of the DAG network.

           Subnets: Use this field to associate one or more subnets with the DAG network. Click
               to add a subnet, click   to edit a subnet, and click minus (-) to remove a subnet.

   4. Click Save to create the DAG network.

Use the Exchange Management Shell to create a
database availability group network
This example creates the network ReplicationDagNetwork02 with a subnet of 10.0.0.0 and a
bitmask of 8 in the DAG DAG1. Replication is enabled for the network, and an optional
description of the network is also being added.

  PowerShell

  New-DatabaseAvailabilityGroupNetwork -DatabaseAvailabilityGroup DAG1 -Name
  ReplicationDagNetwork02 -Description "Replication network 2" -Subnets 10.0.0.0/8 -
  ReplicationEnabled:$True

How do you know this worked?
To verify that you've successfully created a DAG network, do one of the following:

     In the EAC, navigate to Servers > Database Availability Groups. Select the appropriate
     DAG, and the newly created DAG network is displayed in the details pane.

     In the Exchange Management Shell, run the following command to verify the DAG
     network was created and to display DAG network configuration information.

        PowerShell

        Get-DatabaseAvailabilityGroupNetwork <DAGNetworkName> | Format-List

<!-- p.2723 -->

For more information
Set-DatabaseAvailabilityGroupNetwork

Get-DatabaseAvailabilityGroupNetwork

New-DatabaseAvailabilityGroupNetwork

Remove-DatabaseAvailabilityGroupNetwork

<!-- p.2724 -->

Manage database availability group
membership in Exchange Server
07/23/2025

APPLIES TO:      2016     2019      Subscription Edition

When you add a server to a database availability group (DAG), the server works with the other
DAG members to provide automatic database-level recovery from database, server, or network
failures. When you remove a server from a DAG, the server is no longer automatically protected
from failures.

Looking for other management tasks related to DAGs? Check out Manage database availability
groups.

What do you need to know before you begin?
     Estimated time to complete: 5 minutes per server

     To open the Exchange admin center (EAC), see Exchange admin center in Exchange
     Server. To open the Exchange Management Shell, see Open the Exchange Management
     Shell.

     DAGs use Windows Failover Clustering (WFC) technologies. Each Mailbox server that's a
     member of a DAG is also a node in the underlying cluster used by the DAG. As a result, at
     any specific time, a Mailbox server can be a member of only one DAG. Because DAGs use
     WFC technology, all servers added to a DAG must be running the same operating system:
     either Windows Server 2008 R2 Enterprise or Datacenter Edition, or the Standard or
     Datacenter Edition of Windows Server 2012 or Windows Server 2012 R2.

     To add Mailbox servers running Windows Server 2012, you must pre-stage the cluster
     name object (CNO) for the DAG. To add Mailbox servers running Windows Server 2012
     R2, and your DAG doesn't have an administrative access point, then you don't to pre-
     stage a CNO. DAGs without administrative access points don't have CNOs. For detailed
     steps, see Pre-stage the cluster name object for a database availability group.

     Before you can add members to a DAG, you must first create a DAG. For detailed steps,
     see Create a database availability group.

     You must remove all replicated database copies from the server before you can remove it
     from a DAG.

<!-- p.2725 -->

     You need to be assigned permissions before you can perform this procedure or
     procedures. To see what permissions you need, see the "Database availability groups"
     entry in the High availability and site resilience permissions article.

     For information about keyboard shortcuts that might apply to the procedures in this
     article, see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange Server forum at Exchange | Exchange
  Server | Management.

Use the EAC to manage database availability group
membership
  1. In the EAC, go to Servers > Database Availability Groups.

  2. Select the DAG you want to configure, and then select        .

           To add one or more Mailbox servers to the DAG, select        , select the servers from
           the list, select Add, and then select OK.

           To remove one or more Mailbox servers from the DAG, select the servers, and then
           select the minus (-) icon.

  3. Select Save to save the changes.

  4. When the task completes successfully, select Close.

Use the Exchange Management Shell to manage
database availability group membership
This example adds the Mailbox server MBX1 to the DAG DAG1.

  PowerShell

  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer MBX1

This example removes the Mailbox server MBX1 from the DAG DAG1. Before running this
command, make sure that no replicated databases exist on the Mailbox server.

<!-- p.2726 -->

  PowerShell

  Remove-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer MBX1

This example removes the configuration settings for the Mailbox server MBX4 from the DAG
DAG2. MBX4 is expected to be offline for an extended period. Its configuration is removed
from the DAG to establish quorum with the remaining online DAG members.

  PowerShell

  Remove-DatabaseAvailabilityGroupServer -Identity DAG2 -MailboxServer MBX4 -
  ConfigurationOnly

How do you you successfully managed DAG
membership?
To verify you successfully managed DAG membership, do one of the following steps:

     In the EAC, navigate to Servers > Database Availability Groups. The current DAG
     membership is displayed in the Member Servers column.

     In the Exchange Management Shell, run the following command to display DAG
     membership information.

        PowerShell

        Get-DatabaseAvailabilityGroup <DAGName> | Format-List Servers

For more information
Add-DatabaseAvailabilityGroupServer

Remove-DatabaseAvailabilityGroupServer

<!-- p.2727 -->

Configure database availability group
properties in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

The Exchange Management Shell enables you to configure DAG properties that aren't available
in the EAC, such as alternate witness server and alternate witness directory information, the TCP
port used for replication, and datacenter activation coordination (DAC) mode.

What do you need to know before you begin?
      Estimated time to complete: 1 minute

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Database availability groups"
      entry in the High availability and site resilience permissions topic.

      DAG property values are stored in both Active Directory and the cluster database.
      However, some properties are stored only in the cluster database. As a result, the
      underlying cluster for the DAG must be running and have quorum to set the properties
      for:

         ReplicationPort

         NetworkCompression

         NetworkEncryption

         DiscoverNetworks

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Use the EAC to configure database availability
group properties

<!-- p.2728 -->

  1. In the EAC, go to Servers > Database Availability Groups.

  2. Select the DAG you want to configure and click      .

  3. Use the General page to view DAG membership and operational status, and to configure
     the DAG's witness server, witness directory, and automatic network configuration:

           Witness server: The host name or fully qualified domain name (FQDN) of the
           witness server for the DAG. Although this is a required property for all DAGs, the
           witness server is used when there is an even number of DAG members and the
           quorum model in use by the cluster is Node and File Share Majority.

           Witness directory: The full path of the directory used to store the witness.log file on
           the witness server. Although this is a required property for all DAGs, the witness
           directory is used only when the DAG's witness server is in use.

           Database availability group members: A read-only field that displays a list of DAG
           members and their current operational status.

           Configure database availability group networks manually: A check box that you
           select when you want to configure all DAG networks manually. When the check box
           is clear, the system configures DAG networks automatically based on network
           interface configuration, and the Set-DatabaseAvailabilityGroupNetwork and New-
           DatabaseAvailabilityGroupNetwork cmdlets are disabled for the DAG.

  4. Use the IP addresses page to view and modify the IP addresses assigned to the DAG:

           Select an existing IP address and click   to modify it.

           Select an existing IP address and click the minus icon (delete) to remove it.

           Enter an IP address and click    to add it to the DAG.

  5. Click Save to save any changes that were made.

Use the Exchange Management Shell to configure
database availability group properties
This example sets the witness directory to C:\DAG1DIR for the DAG DAG1.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -WitnessDirectory C:\DAG1DIR

<!-- p.2729 -->

This example preconfigures an alternate witness server of MBX3 and an alternate witness
directory of C:\DAGFileShareWitnesses\DAG1.contoso.com for the DAG DAG1.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -AlternateWitnessDirectory
  C:\DAGFileShareWitnesses\DAG1.contoso.com -AlternateWitnessServer MBX3

This example configures the DAG DAG1 to use Dynamic Host Configuration Protocol (DHCP) to
obtain an IP address.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -DatabaseAvailabilityGroupIPAddresses
  0.0.0.0

This example configures the DAG DAG1 to use a static IP address of 10.0.0.8.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -DatabaseAvailabilityGroupIPAddresses
  10.0.0.8

This example configures the multi-subnet DAG DAG1 with multiple static IP addresses.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -DatabaseAvailabilityGroupIPAddresses
  10.0.0.8,10.0.1.8

This example configures the DAG DAG1 for DAC mode.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -DatacenterActivationMode DagOnly

This example configures the replication port for the DAG DAG1 to be 63132.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -ReplicationPort 63132

  ７ Note

<!-- p.2730 -->

  After changing the default replication port for a DAG, you must manually modify the
  Windows Firewall exceptions on each member of the DAG to allow communication to
  occur over the specified port.

How do you know this worked?
To verify that you've successfully configured the DAG, do the following:

     In the Exchange Management Shell, run the following command to display DAG
     configuration settings and verify the DAG was configured successfully.

       PowerShell

        Get-DatabaseAvailabilityGroup <DAGName> | Format-List

For more information
Create a database availability group

Remove a database availability group

Create a database availability group network

Manage database availability group membership

Get-DatabaseAvailabilityGroup

Set-DatabaseAvailabilityGroup

<!-- p.2731 -->

Manage mailbox database copies
08/05/2025

APPLIES TO:      2016     2019      Subscription Edition

In Exchange Server, you can use the Exchange Management Console (EAC) or the Exchange
Management Shell to add mailbox database copies after a database availability group (DAG) is
created, configured, and populated with Mailbox server members.

Managing database copies
After multiple copies of a database are created, you can use the EAC or the Exchange
Management Shell to do the following tasks:

     Monitor the health and status of each copy.
     Do other management tasks associated with database copies. For example:
        Suspend or resume a database copy.
        Seed a database copy.
        Monitor database copies.
        Configure database copy settings
        Remove a database copy.

Suspending and resuming database copies
For a variety of reasons, such as performing planned maintenance, you might need to suspend
and resume continuous replication activity for a database copy. In addition, some
administrative tasks, such as seeding, require that you first suspend a database copy. We
recommend that you suspend all replication activity when the path for the database or its log
files is being changed. You can suspend and resume database copy activity by using the EAC,
or by running the Suspend-MailboxDatabaseCopy and Resume-MailboxDatabaseCopy
cmdlets in the Exchange Management Shell. For detailed steps about how to suspend or
resume continuous replication activity for a database copy, see Suspend or resume a mailbox
database copy.

Seeding a database copy
Seeding, also known as updating, is when a blank database or a copy of the production
database, is added to the target copy location on another Mailbox server in the same DAG as
the active database. This database becomes the baseline database for the copy maintained by
that server.

<!-- p.2732 -->

Depending on the situation, you can seed a database by using an automatic process or a
manual process that you initiate. When a database copy is added, the copy is automatically
seeded, if the target server and its storage are properly configured. To manually seed a
database copy and don't want automatic seeding to occur when creating the copy, you can use
the SeedingPostponed parameter on the Add-MailboxDatabaseCopy cmdlet.

Database copies rarely need to be reseeded after the initial seeding. However, if reseeding is
necessary, or to manually seed a database copy instead of having the system automatically
seed the copy, you have two options:

     Use the Update Mailbox Database Copy wizard in the EAC.
     Use the Update-MailboxDatabaseCopy cmdlet in the Exchange Management Shell.

Before seeding a database copy, you must first suspend the mailbox database copy. For
detailed steps about how to seed a database copy, see Update a mailbox database copy.

After a manual seed operation is complete, replication for the seeded mailbox database copy is
automatically resumed. If you don't want replication to automatically resume, you can use the
ManualResume parameter on the Update-MailboxDatabaseCopy cmdlet.

Choosing what to seed
When you perform a seed operation, you can choose to:

     Seed the mailbox database copy.
     Seed the content index catalog for the mailbox database copy.
     Seed both the database copy and the content index catalog copy.

The default behavior of the Update Mailbox Database Copy wizard and the Update-
MailboxDatabaseCopy cmdlet is to seed both the mailbox database copy and the content
index catalog copy.

To seed just the mailbox database copy without seeding the content index catalog, use the
DatabaseOnly parameter on the Update-MailboxDatabaseCopy cmdlet.

To seed just the content index catalog copy, use the CatalogOnly parameter on the Update-
MailboxDatabaseCopy cmdlet.

Selecting the seeding source
You can use any healthy database copy as the seeding source for another copy of that
database. This option is particularly useful when you have a DAG extended across multiple
physical locations.

<!-- p.2733 -->

For example, consider the following four-member DAG deployment:

     MBX1 and MBX2 are located in Portland, Oregon.
     MBX3 and MBX4 are located in New York, New York.
     A mailbox database named DB1 is active on MBX1.
     There are passive copies of DB1 on MBX2 and MBX3.

When adding a copy of DB1 to MBX4, you can use the copy on MBX3 as the source for
seeding. This option avoids seeding over the wide area network (WAN) link between Portland
and New York.

To use a specific copy as a source for seeding when adding a new database copy, you can do
the following steps:

     Use the SeedingPostponed parameter on the Add-MailboxDatabaseCopy cmdlet to add
     the database copy. Otherwise, the database copy is explicitly seeded using the active
     copy of the database as the source.

     You can specify the source server to use in the Update Mailbox Database Copy wizard in
     the EAC, or you can use the SourceServer parameter on the Update-
     MailboxDatabaseCopy cmdlet to specify the desired source server for seeding.

     In the previous example, you would specify MBX3 as the source server. Otherwise, the
     database copy is explicitly seeded from the active copy of the database.

Seeding and networks
In addition to selecting a specific source server for seeding a mailbox database copy, you can
also use the Exchange Management Shell to specify which DAG networks to use. You can
override the DAG network's compression and encryption settings during the seed operation.

You can specify the networks to use for seeding by using the Network parameter on the
Update-MailboxDatabaseCopy cmdlet and specify the DAG networks that you want to use. If
you don't use the Network parameter, the system uses the following default behavior for
selecting a network to use for the seeding operation:

     If the source server and target server are on the same subnet and a replication network
     that includes the subnet is configured, the replication network is used.

     If the source server and target server are on different subnets, even if a replication
     network containing those subnets is configured, the client (MAPI) network is used for
     seeding.

<!-- p.2734 -->

     If the source server and target server are in different datacenters, the client (MAPI)
     network is used for seeding.

At the DAG level, DAG networks are configured for encryption and compression. The default
settings use encryption and compression only for communications on different subnets. If the
source and target are on different subnets and the DAG is configured with the default values
for NetworkCompression and NetworkEncryption, you can override these values by using the
NetworkCompressionOverride and NetworkEncryptionOverride parameters on the Update-
MailboxDatabaseCopy cmdlet.

Seeding process
When you begin a seeding process by using the Add-MailboxDatabaseCopy or Update-
MailboxDatabaseCopy cmdlets, the following tasks are performed:

   1. Database properties from Active Directory are read to validate the specified database and
     servers, and to verify that the source and target servers are running Exchange Server,
     they're both members of the same DAG, and that the specified database isn't a recovery
     database. The database file paths are also read.

   2. Preparations occur for reseed checks from the Microsoft Exchange Replication service on
     the target server.

   3. The Microsoft Exchange Replication service on the target server checks for the presence
     of database and transaction log files in the file directories read by the Active Directory
     checks in step 1.

   4. The Microsoft Exchange Replication service returns the status information from the target
     server to the administrative interface from where the cmdlet was run.

   5. If all preliminary checks pass, you're prompted to confirm the operation before
     continuing. If you confirm the operation, the process continues. If an error is encountered
     during the preliminary checks, the error is reported and the operation fails.

   6. The seed operation is started from the Microsoft Exchange Replication service on the
     target server.

   7. The Microsoft Exchange Replication service suspends database replication for the active
     database copy.

   8. The Microsoft Exchange Replication service updates the state information for the
     database to reflect a status of Seeding.

<!-- p.2735 -->

 9. If the target server doesn't already have the directories for the target database and log
   files, they're created.

10. A TCP request to seed the database is passed from the Microsoft Exchange Replication
   service on the target server to the Microsoft Exchange Replication service on the source
   server. This request and the subsequent communications for seeding the database occur
   on a DAG network configured as a replication network.

11. The Microsoft Exchange Replication service on the source server initiates an Extensible
   Storage Engine (ESE) streaming backup via the Microsoft Exchange Information Store
   service interface.

12. The Microsoft Exchange Information Store service streams the database data to the
   Microsoft Exchange Replication service.

13. The database data is moved from the source server's Microsoft Exchange Replication
   service to the target server's Microsoft Exchange Replication service.

14. The Microsoft Exchange Replication service on the target server writes the database copy
   to a temporary directory located in the main database directory called temp-seeding.

15. The streaming backup operation on the source server ends when the end of the database
   is reached.

16. The write operation on the target server completes, and the database is moved from the
   temp-seeding directory to the final location. The temp-seeding directory is deleted.

17. On the target server, the Microsoft Exchange Replication service proxies a request to the
   Microsoft Exchange Search service to mount the content index catalog for the database
   copy, if it exists. If there are existing out-of-date catalog files from a previous instance of
   the database copy, the mount operation fails, which triggers the need to replicate the
   catalog from the source server. Likewise, if the catalog doesn't exist on a new instance of
   the database copy on the target server, a copy of the catalog is required. The Microsoft
   Exchange Replication service directs the Microsoft Exchange Search service to suspend
   indexing for the database copy while a new catalog is copied from the source.

18. The Microsoft Exchange Replication service on the target server sends a seed catalog
   request to the Microsoft Exchange Replication service on the source server.

19. On the source server, the Microsoft Exchange Replication service requests the directory
   information from the Microsoft Exchange Search service and requests that indexing is
   suspended.

20. The Microsoft Exchange Search service on the source server returns the search catalog
   directory information to the Microsoft Exchange Replication service.

<!-- p.2736 -->

 21. The Microsoft Exchange Replication service on the source server reads the catalog files
     from the directory.

 22. The Microsoft Exchange Replication service on the source server moves the catalog data
     to the Microsoft Exchange Replication service on the target server using a connection
     across the replication network. After the read is complete, the Microsoft Exchange
     Replication service sends a request to the Microsoft Exchange Search service to resume
     indexing of the source database.

 23. If there are any existing catalog files on the target server in the directory, the Microsoft
     Exchange Replication service on the target server deletes them.

 24. The Microsoft Exchange Replication service on the target server writes the catalog data to
     a temporary directory called CiSeed.Temp until the data is completely transferred.

 25. The Microsoft Exchange Replication service moves the complete catalog data to the final
     location.

 26. The Microsoft Exchange Replication service on the target server resumes search indexing
     on the target database.

 27. The Microsoft Exchange Replication service on the target server returns a completion
     status.

 28. The final result of the operation is passed to the administrative interface from which the
     cmdlet was called.

Configuring database copies
After a database copy is created, you can view and modify its configuration settings when
needed. You can view some configuration information by examining the Properties page for a
database copy in the EAC. You can also use the Get-MailboxDatabase and Set-
MailboxDatabaseCopy cmdlets in the Exchange Management Shell to view and configure
database copy settings. For example, replay lag time, truncation lag time, and activation
preference order. For detailed steps about how to view and configure database copy settings,
see Configure mailbox database copy properties.

Using replay lag and truncation lag options
Mailbox database copies support the use of a replay lag time and a truncation lag time, both of
which are configured in minutes. Setting a replay lag time enables you to take a database copy
back to a specific point in time. Setting a truncation lag time enables you to use the logs on a
passive database copy to recover from the loss of log files on the active database copy.

<!-- p.2737 -->

Because both of these features result in the temporary buildup of log files, using either of them
affects your storage design.

Replay lag time

Replay lag time is a mailbox database copy property that specifies the amount of time, in
minutes, to delay log replay for the database copy. The replay lag timer starts when a log file is
replicated to the passive copy and successfully passes inspection. By delaying the replay of logs
to the database copy, you have the capability to recover the database to a specific point in
time in the past. A mailbox database copy configured with a replay lag time greater than zero
is referred to as a lagged mailbox database copy, or simply, a lagged copy.

A strategy that uses database copies and the litigation hold features in Exchange Server can
provide protection against a range of failures that would ordinarily cause data loss. However,
these features can't provide protection against data loss due to logical corruption. Although
logical corruption is rare, it can cause data loss. Lagged copies are designed to prevent loss of
data due to logical corruption. Generally, there are two types of logical corruption:

     Database logical corruption: The database pages checksum matches, but the data on the
     pages is wrong logically. This situation occurs when ESE attempts to write a database
     page. Although the operating system returns a success message, the data is either never
     written to the disk or it's written to the wrong place. This condition is referred to as a lost
     flush. To prevent lost flushes from losing data, ESE includes a lost flush detection
     mechanism in the database along with a page patching feature (single page restore).

     Store logical corruption: Data is added, deleted, or manipulated in a way that the user
     doesn't expect. Non-Microsoft applications generally cause these cases. It's generally
     considered corruption in the sense that the user views it as corruption. The Exchange
     store considers the transaction that produced the logical corruption to be a series of valid
     MAPI operations. The litigation hold feature in Exchange Server provides protection from
     store logical corruption (because it prevents content from being permanently deleted by
     a user or application). However, there might be scenarios where a user mailbox becomes
     so corrupted that it would be easier to restore the database to a point in time prior to the
     corruption, and then export the user mailbox to retrieve uncorrupted data.

The combination of database copies, hold policy, and ESE single page restore leaves only the
rare but catastrophic store logical corruption case. Your decision on whether to use a database
copy with a replay lag (a lagged copy) depends on which non-Microsoft applications you use
and your organization's history with store logical corruption.

If you choose to use lagged copies, be aware of the following implications for their use:

<!-- p.2738 -->

     The replay lag time is an administrator-configured value. By default, replay lag time is
     disabled.

     The replay lag time setting has a default setting of zero days, and a maximum setting of
     14 days.

     Lagged copies aren't considered highly available copies. Instead, they're designed for
     disaster recovery purposes, to protect against store logical corruption.

     The greater the replay lag time set, the longer the database recovery process. It might
     take several hours to recover a database due to:
        The number of log files to be replayed.
        The speed at which your hardware can replay them.

     We recommend that you determine whether lagged copies are critical for your overall
     disaster recovery strategy. If using them is critical to your strategy, we recommend using
     multiple lagged copies, or using a redundant array of independent disks (RAID) to protect
     a single lagged copy, if you don't have multiple lagged copies. If you lose a disk or if
     corruption occurs, you don't lose your lagged point in time.

     Lagged copies can't be patched with the ESE single page restore feature. If a lagged copy
     encounters database page corruption (for example, a -1018 error), the copy needs to be
     reseeded. Reseeding loses the lagged aspect of the copy.

If you want the database to replay all log files and make the database copy current, then
activating and recovering a lagged mailbox database copy is an easy process. If you want to
replay log files up to a specific point in time, the process is more difficult because you have to
manually manipulate log files and run Exchange Server Database Utilities (Eseutil.exe).

For detailed steps about how to activate a lagged mailbox database copy, see Activate a
lagged mailbox database copy.

Truncation lag time

Truncation lag time is the property of a mailbox database copy that specifies the time in
minutes to delay log deletion for the database copy after the log file has been replayed into
the database copy. The truncation lag timer starts when a log file has been replicated to the
passive copy, successfully passed inspection, and has been successfully replayed into the copy
of the database. By delaying the truncation of log files from the database copy, you have the
capability to recover from failures that affect the log files for the active copy of the database.

Database copies and log truncation

<!-- p.2739 -->

Log truncation works the same in Exchange 2016 and Exchange 2019 as it did in Exchange
2010. Truncation behavior is determined by the replay lag time and truncation lag time settings
for the copy.

The following criteria must be met for a database copy's log file to be truncated when lag
settings are left at their default values of 0 (disabled):

     The log file is successfully backed up or circular logging is enabled.
     The log file must be below the checkpoint (the minimum log file required for recovery) for
     the database.
     All other lagged copies inspected the log file.
     All other copies (except lagged copies) replayed the log file.

The following criteria must be met for truncation to occur for a lagged database copy:

     The log file must be below the checkpoint for the database.
     The log file must be older than ReplayLagTime + TruncationLagTime.
     The log file is truncated on the active copy.

In Exchange Server, log truncation doesn't occur on an active mailbox database copy when one
or more passive copies are suspended. If planned maintenance activities are going to take an
extended period of time (for example, several days), you might have considerable log file
buildup. To prevent the log drive from filling up with transaction logs, you can remove the
affected passive database copy instead of suspending it. When the planned maintenance is
completed, you can re-add the passive database copy.

Exchange Server now has a feature called loose truncation that is disabled by default. During
normal operations, each database copy keeps logs that need to be shipped to other database
copies until all copies of a database confirm:

     They replayed the log files (passive copies).
     They received the log files (lagged copies) .

This behavior is the default log truncation behavior. If a database copy goes offline for some
reason, the log files begin accumulating on the disks used by the other copies of the database.
If the affected database copy remains offline for an extended period, this can cause the other
database copies to run out of disk space.

Truncation behavior is different when loose truncation and circular logging are enabled. Each
database copy tracks its own free disk space and applies loose truncation behavior if free space
gets low.

     For the active copy, the oldest straggler (the passive database copy that is farthest behind
     in log replay) is ignored and truncation respects the oldest remaining passive copies. The

<!-- p.2740 -->

     active database copy is where global truncation is calculated.

     For a passive copy, if space gets low, it independently truncates its log files using the
     configured parameters described later in the Registry Value table. The passive copies
     attempt to respect the truncation decision made on the active copy. Despite the
     implication of the name MinCopiesToProtect, Exchange only ignores the oldest known
     straggler at the time truncation is run.

When the offline database is brought back online, its missing log files deleted from the other
healthy copies, and its database copy status is FailedAndSuspended. In this event, if
Autoreseed is configured, the affected copy is automatically reseeded. If Autoreseed isn't
configured, the database copy needs to be manually seeded by an administrator.

If circular logging is disabled, loose truncation respects any backups taken. Loose truncation
doesn't remove log files that aren't backed up.

Truncation is a recommended feature for preferred architecture where backups aren't used and
circular logging is enabled.

The required number of healthy copies, the free disk space threshold, and the number of logs
to keep are all configurable parameters. By default, the free disk space threshold is 204800 MB
(200 GB), and the number of logs to keep is 100,000 (100 GB) for passive copies, and 10,000 (10
GB) for active copies.

Enabling loose truncation and configuring loose truncation parameters is performed by editing
the Windows registry on each DAG member. There are three registry values that can be
configured, that are all stored under
HKLM\Software\Microsoft\ExchangeServer\v15\BackupInformation. The BackupInformation
key the following DWORD values don't exist by default and must be manually created. The
DWORD registry values under BackupInformation are described in the following table:

                                                                                    ﾉ   Expand table

 Registry Value                                   Description                   Default Value

 LooseTruncation_MinCopiesToProtect               This key is used to enable    0
                                                  loose truncation. It
                                                  represents the number of
                                                  passive copies to protect
                                                  from loose truncation on
                                                  the active copy of a
                                                  database. Setting the value
                                                  of this key to 0 disables
                                                  loose truncation.

<!-- p.2741 -->

 Registry Value                                    Description                      Default Value

 LooseTruncation_MinDiskFreeSpaceThresholdInMB     Available disk space (in MB)     If this registry value
                                                   threshold for triggering         isn't configured, the
                                                   loose truncation. If free disk   default value used by
                                                   space falls below this value,    loose truncation is
                                                   loose truncation is              200 GB.
                                                   triggered.

 LooseTruncation_MinLogsToProtect                  The minimum number of            If this registry value
                                                   log files to retain on healthy   isn't configured, then
                                                   copies whose logs are            default values of
                                                   being truncated. If this         100,000 for passive
                                                   registry value is configured,    database copies and
                                                   then the configured value        10,000 for active
                                                   applies to both active and       database copies is
                                                   passive copies.                  used.

When using the LooseTruncation_MinLogsToProtect registry value, the behavior is different for
active and passive database copies

     Active: The number of extra logs retained preceding those logs required by the protected
     passive copies and the required range of the active copy.
     Passive: The number of logs maintained from the latest available log. One tenth of this
     number is also used to maintain logs before the required range of this passive copy.

The two limits are in place to ensure that lagged database copies don't take up too much
space, since their required range is typically very large.

Database activation policy
There are scenarios where you might want to create a mailbox database copy and prevent the
system from automatically activating that copy. For example, after a failure:

     You deploy one or more mailbox database copies to an alternate or standby datacenter.
     You configure a lagged database copy for recovery purposes.
     You're doing maintenance or a server upgrade.

In each of the preceding scenarios, you have database copies that you don't want the system
to activate automatically. To prevent the system from automatically activating a mailbox
database copy, you can configure the copy to be blocked (suspended) for activation.

This configuration allows the system to maintain the currency of the database through log
shipping and replay, but prevents the system from automatically activating and using the copy.
An administrator must manually activate copies blocked for activation.

<!-- p.2742 -->

You can set the DatabaseCopyAutoActivationPolicy parameter to Blocked for:

     An entire server by using the Set-MailboxServer cmdlet.
     An individual database copy by using the Set-MailboxDatabaseCopy cmdlet.

For more information about configuring database activation policy, see Configure activation
policy for a mailbox database copy.

Effect of mailbox moves on continuous replication
On a very busy mailbox database with a high log generation rate, there is a greater chance for
data loss if replication to the passive database copies can't keep up with log generation. One
scenario that can introduce a high log generation rate is mailbox moves. Exchange Server
includes a Data Guarantee API that's used by services such as the Exchange Mailbox
Replication service (MRS) to check the health of the database copy architecture based on the
value of the DataMoveReplicationConstraint parameter that was set by the system or an
administrator. Specifically, the Data Guarantee API can be used to:

     Check replication health: Confirms that the prerequisite number of database copies is
     available.

     Check replication flush: Confirms that the required log files are replayed against the
     prerequisite number of database copies.

When executed, the API returns the following status information to the calling application:

     Retry: Signifies that there are transient errors that prevent a condition from being
     checked against the database.

     Satisfied: Signifies that the database meets the required conditions or the database isn't
     replicated.

     NotSatisfied: Signifies that the database doesn't meet the required conditions. In
     addition, information is provided to the calling application as to why the NotSatisfied
     response was returned.

The value of the DataMoveReplicationConstraint parameter for the mailbox database
determines how many database copies should be evaluated as part of the request. The
DataMoveReplicationConstraint parameter has the following possible values:

     None : When you create a mailbox database, this value is set by default. When this value is

     set, the Data Guarantee API conditions are ignored. This setting should be used only for
     mailbox databases that aren't replicated.

<!-- p.2743 -->

      SecondCopy : This is the default value when you add the second copy of a mailbox

     database. When this value is set, at least one passive database copy must meet the Data
     Guarantee API conditions.

      SecondDatacenter : When this value is set, at least one passive database copy in another

     Active Directory site must meet the Data Guarantee API conditions.

      AllDatacenters : When this value is set, at least one passive database copy in each Active

     Directory site must meet the Data Guarantee API conditions.

      AllCopies : When this value is set, all copies of the mailbox database must meet the Data

     Guarantee API conditions.

Check Replication Health

When the Data Guarantee API is executed to evaluate the health of the database copy
infrastructure, several items are evaluated.

In all scenarios, the passive database copy must meet the following conditions:

     Be healthy.

     Have a replay queue within 10 minutes of the replay lag time.

     Have a copy queue length less than 10 logs.

     Have an average copy queue length less than 10 logs. The average copy queue length is
     computed based on the number of times the application queried the database status.

                                                                                       ﾉ   Expand table

 If the DataMoveReplicationConstraint          Then, for a given database...
 parameter is set to...

 SecondCopy                                    At least one passive database copy for a replicated
                                               database must meet the previously described conditions.

 SecondDatacenter                              At least one passive database copy in another Active
                                               Directory site must meet the previously described
                                               conditions.

 AllDatacenters                                The active copy must be mounted, and a passive copy in
                                               each Active Directory site must meet the previously
                                               described conditions.

 AllCopies                                     The active copy must be mounted, and all passive
                                               database copies must meet the previously described

<!-- p.2744 -->

 If the DataMoveReplicationConstraint            Then, for a given database...
 parameter is set to...

                                                 conditions.

Check Replication Flush
The Data Guarantee API can also be used to validate that a prerequisite number of database
copies have replayed the required transaction logs. This is verified by comparing the last log
replayed timestamp with that of the calling service's commit timestamp (in most cases, this is
the timestamp of the last log file that contains required data) plus an extra five seconds (to
deal with system time clock skews or drift). If the replay timestamp is greater than the commit
timestamp, the DataMoveReplicationConstraint parameter is satisfied. If the replay timestamp is
less than the commit timestamp, the DataMoveReplicationConstraint isn't satisfied.

Before moving large numbers of mailboxes to or from replication databases within a DAG, we
recommend that you configure the DataMoveReplicationConstraint parameter on each mailbox
database according to the following table:

                                                                                         ﾉ   Expand table

 If you're deploying...         Set DataMoveReplicationConstraint to...

 Mailbox databases that         None
 don't have any database
 copies

 A DAG within a single          SecondCopy
 Active Directory site

 A DAG in multiple              SecondCopy
 datacenters using a
 stretched Active Directory
 site

 A DAG that spans two           SecondDatacenter
 Active Directory sites, and
 you have highly available
 database copies in each site

 A DAG that spans two           SecondCopy
 Active Directory sites, and    The Data Guarantee API doesn't guarantee data being committed until the
 you have only lagged           log file is replayed into the database copy. Due to the nature of the
 database copies in the         database copy being lagged, this constraint fails the move request, unless
 second site                    the lagged database copy ReplayLagTime value is less than 30 minutes.

<!-- p.2745 -->

 If you're deploying...             Set DataMoveReplicationConstraint to...

 A DAG that spans three or           AllDatacenters
 more Active Directory sites,
 and each site contain highly
 available database copies

Balancing database copies
Due to the inherent nature of DAGs, as the result of database switchovers and failovers, active
mailbox database copies change hosts several times throughout a DAG's lifetime. As a result,
DAGs can become unbalanced in terms of active mailbox database copy distribution. The
following table shows an example of a DAG that has four databases with four copies of each
database (for a total of 16 databases on each server) with an uneven distribution of active
database copies.

                                                                                   ﾉ    Expand table

 Server   Number of             Number of             Number of       Number of        Preference
          active                passive               mounted         dismounted       count list
          databases             databases             databases       databases

 EX1      5                     11                    5               0                4, 4, 3, 5

 EX2      1                     15                    1               0                1, 8, 6, 1

 EX3      12                    4                     12              0                13, 2, 1, 0

 EX4      1                     15                    1               0                1, 1, 5, 9

In the preceding example, there are four copies of each database, and therefore, only four
possible values for activation preference (1, 2, 3, or 4). The Preference count list column shows
the count of the number of databases with each of these values. For example, on EX3, there are
13 database copies with an activation preference of 1, two copies with an activation preference
of 2, one copy with an activation preference of 3, and no copies with an activation preference
of 4.

As you can see, this DAG isn't balanced in terms of the number of active databases hosted by
each DAG member, the number of passive databases hosted by each DAG member, or the
activation preference count of the hosted databases.

You can use the RedistributeActiveDatabases.ps1 script to balance the active mailbox databases
copies across a DAG. This script moves databases between their copies in an attempt to have
an equal number of mounted databases on each server in DAG. If required, the script also
attempts to balance active databases across sites.

<!-- p.2746 -->

The script provides two options for balancing active database copies within a DAG:

       BalanceDbsByActivationPreference: When this option is specified, the script attempts to
       move databases to their most preferred copy (based on activation preference) without
       regard to the Active Directory site.

       BalanceDbsBySiteAndActivationPreference: When this option is specified, the script
       attempts to move active databases to their most preferred copy, while also trying to
       balance active databases within each Active Directory site.

After running the script with the first option, the preceding unbalanced DAG becomes
balanced, as shown in the following table.

                                                                                           ﾉ    Expand table

 Server    Number of        Number of             Number of           Number of                Preference
           active           passive               mounted             dismounted               count list
           databases        databases             databases           databases

 EX1       4                12                    4                   0                        4, 4, 4, 4

 EX2       4                12                    4                   0                        4, 4, 4, 4

 EX3       4                12                    4                   0                        4, 4, 4, 4

 EX4       4                12                    4                   0                        4, 4, 4, 4

As shown in the preceding table, this DAG is now balanced in terms of number of active and
passive databases on each server and activation preference across the servers.

The following table lists the available parameters for the RedistributeActiveDatabases.ps1
script.

                                                                                           ﾉ    Expand table

 Parameter                                    Description

 DagName                                      Specifies the name of the DAG you want to rebalance. If this
                                              parameter is omitted, the DAG of which the local server is a
                                              member is used.

 BalanceDbsByActivationPreference             Specifies that the script should move databases to their most
                                              preferred copy without regard to the Active Directory site.

 BalanceDbsBySiteAndActivationPreference      Specifies that the script should attempt to move active
                                              databases to their most preferred copy, while also trying to
                                              balance active databases within each Active Directory site.

<!-- p.2747 -->

 Parameter                             Description

 ShowFinalDatabaseDistribution         Specifies that a report of current database distribution is
                                       displayed after redistribution is complete.

 AllowedDeviationFromMeanPercentage    Specifies the allowed variation of active databases across
                                       sites, expressed as a percentage. The default is 20%. For
                                       example, if there were 99 databases distributed between
                                       three sites, the ideal distribution would be 33 databases in
                                       each site. If the allowed deviation is 20%, the script attempts
                                       to balance the databases so that each site has no more than
                                       10% more or less than this number. 10% of 33 is 3.3, which is
                                       rounded up to 4. Therefore, the script attempts to have
                                       between 29 and 37 databases in each site.

 ShowDatabaseCurrentActives            Specifies that the script produce a report for each database
                                       detailing how the database was moved and whether it's now
                                       active on its most-preferred copy.

 ShowDatabaseDistributionByServer      Specifies that the script produce a report for each server
                                       showing its database distribution.

 RunOnlyOnPAM                          Specifies that the script run only on the DAG member that
                                       currently has the PAM role. The script verifies it's being run
                                       from the PAM. If it isn't being run from the PAM, the script
                                       exits.

 LogEvents                             Specifies that the script logs an event (MsExchangeRepl event
                                       4115) containing a summary of the actions.

 IncludeNonReplicatedDatabases         Specifies that the script should include non-replicated
                                       databases (databases without copies) when determining how
                                       to redistribute the active databases. Although non-replicated
                                       databases can't be moved, they might affect the distribution
                                       of the replicated databases.

 Confirm                               The Confirm switch can be used to suppress the confirmation
                                       prompt that appears by default when this script is run. To
                                       suppress the confirmation prompt, use the syntax -
                                       Confirm:$False. You must include a colon (:) in the syntax.

RedistributeActiveDatabases.ps1 examples
This example shows the current database distribution for a DAG, including preference count
list.

   PowerShell

<!-- p.2748 -->

  RedistributeActiveDatabases.ps1 -DagName DAG1 -ShowDatabaseDistributionByServer |
  Format-Table

This example redistributes and balances the active mailbox database copies in a DAG using
activation preference without prompting for input.

  PowerShell

  RedistributeActiveDatabases.ps1 -DagName DAG1 -BalanceDbsByActivationPreference -
  Confirm:$False

This example redistributes and balances the active mailbox database copies in a DAG using
activation preference, and produces a summary of the distribution.

  PowerShell

  RedistributeActiveDatabases.ps1 -DagName DAG1 -BalanceDbsByActivationPreference -
  ShowFinalDatabaseDistribution

Monitoring database copies
You can view a variety of information, including copy queue length, replay queue length, status,
and content index state information, by examining the details of a database copy in the EAC.
You can also use the Get-MailboxDatabaseCopyStatus cmdlet in the Exchange Management
Shell to view a variety of status information for a database copy.

  ７ Note

  A database copy is your first defense if a failure occurs that affects the active copy of a
  database. It's therefore critical to monitor the health and status of database copies to
  ensure that they're available when needed.

For more information about monitoring database copies, see Monitor database availability
groups.

Removing a database copy
A database copy can be removed at any time by using the EAC or by using the Remove-
MailboxDatabaseCopy cmdlet in the Exchange Management Shell. After removing a database
copy, you must manually delete any database and transaction log files from the server from

<!-- p.2749 -->

which the database copy is being removed. For detailed steps about how to remove a database
copy, see Remove a mailbox database copy.

Database switchovers
The Mailbox server that hosts the active copy of a database is referred to as the mailbox
database master. The process of activating a passive database copy changes the mailbox
database master for the database and turns the passive copy into the new active copy. This
process is called a database switchover. In a database switchover, the active copy of a database
is dismounted on one Mailbox server and a passive copy of that database is mounted as the
new active mailbox database on another Mailbox server. When performing a switchover, you
can optionally override the database mount dial setting on the new mailbox database master.

You can quickly identify which Mailbox server is the current mailbox database master by
reviewing the right-hand column under the Database Copies tab in the EAC. You can perform a
switchover by using the Activate link in the EAC, or by using the Move-ActiveMailboxDatabase
cmdlet in the Exchange Management Shell.

There are several internal checks performed before a passive copy is activated. In some cases,
the database switchover is blocked or canceled. In other cases, you can use cmdlets to move or
skip over some checks.

     The status of the database copy is checked. If the database copy is in a failed state, the
     switchover is blocked. You can override this behavior and bypass the health check by
     using the SkipHealthChecks parameter of the Move-ActiveMailboxDatabase cmdlet. This
     parameter lets you move the active copy to a database copy in a failed state.

     The active database copy is checked to see if it's currently a seeding source for any
     passive copies of the database. If the active copy is currently being used as a source for
     seeding, the switchover is blocked. You can override this behavior and bypass the seeding
     source check by using the SkipActiveCopyChecks parameter of the Move-
     ActiveMailboxDatabase cmdlet. This parameter allows you to move an active copy that's
     being used as a seeding source. Using this parameter causes the seeding operation to be
     cancelled and considered failed.

     The copy queue and replay queue lengths for the database copy are checked to ensure
     their values are within the configured criteria. Also, the database copy is verified to ensure
     that it isn't currently in use as a source for seeding. If the values for the queue lengths are
     outside the configured criteria, or if the database is currently used as a source for
     seeding, the switchover is blocked. You can override this behavior and bypass these
     checks by using the SkipLagChecks parameter of the Move-ActiveMailboxDatabase

<!-- p.2750 -->

     cmdlet. This parameter allows a copy to be activated that has replay and copy queues
     outside of the configured criteria.

     The state of the search catalog (content index) for the database copy is checked. If the
     search catalog isn't up to date, is in an unhealthy state, or is corrupt, the switchover is
     blocked. You can override this behavior and bypass the search catalog check by using the
     SkipClientExperienceChecks parameter of the Move-ActiveMailboxDatabase cmdlet. This
     parameter causes this search to skip the catalog health check. If the search catalog for the
     database copy you're activating is in an unhealthy or unusable state and you use this
     parameter to skip the catalog health check and activate the database copy, you need to
     either crawl or seed the search catalog again.

When you perform a database switchover, you also have the option of overriding the mount
dial settings configured for the server that hosts the passive database copy being activated.
Using the MountDialOverride parameter of the Move-ActiveMailboxDatabase cmdlet instructs
the target server to override its own mount dial settings and use the settings specified by the
MountDialOverride parameter.

For detailed steps about how to perform a switchover of a database copy, see Activate a
mailbox database copy.

<!-- p.2751 -->

Add a mailbox database copy in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

When you add a copy of a mailbox database, continuous replication is automatically enabled
between the existing database and the database copy. Database copies are automatically
assigned an identity in the format of < DatabaseName>\< HostMailboxServerName>. For
example, a copy of the database DB1 that's hosted on the server MBX3 would be DB1\MBX3.

Looking for other management tasks related to mailbox database copies? Check out Manage
mailbox database copies.

What do you need to know before you begin?
      Estimated time to complete this task: 2 minutes, plus the time to seed the database copy,
      which depends on a variety of factors, such as the size of the database, the speed,
      available bandwidth and latency of the network, and storage speeds.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox database copies" entry
      in the High availability and site resilience permissions topic.

      The active copy of the database must be mounted.

      The specified Mailbox server must not already host a copy of the database.

      The path for the database copy and its log files must be available on the selected Mailbox
      server.

      The server hosting the active copy and the server that will host the passive copy must be
      in the same database availability group (DAG). The DAG must also have quorum and be
      healthy.

      If you're adding the second copy of a database (for example, creating the first passive
      copy of the database), circular logging must not be enabled for the specified mailbox
      database. If circular logging is enabled, you must first disable it. After the mailbox
      database copy has been added, circular logging can be enabled. After circular logging is
      enabled for a replicated mailbox database, continuous replication circular logging (CRCL)
      is used instead of JET circular logging. If you're adding the third or subsequent copy of a
      database, CRCL can remain enabled.

<!-- p.2752 -->

     For information about keyboard shortcuts that may apply to the procedures in this topic,
     see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Use the EAC to add a mailbox database copy
   1. In the EAC, go to Servers > Databases.

   2. Select the database that you want to copy, click More (the three dots to the right of the
     Refresh icon), and then click Add database copy.

   3. On the add mailbox database copy page, click Browse..., select the Mailbox server that
     will host the database copy, and then click OK.

   4. Optionally, configure the Activation preference number for the database copy.

   5. Click More options... to designate the database copy as a lagged database copy by
     configuring a replay lag time, or to postpone automatic seeding of the database copy.

   6. Click Save to save the configuration changes and add the mailbox database copy.

   7. Click OK to acknowledge any messages that appear.

Use the Exchange Management Shell to add a
mailbox database copy
This example adds a copy of mailbox database DB1 to the Mailbox server MBX3. Replay lag
time and truncation lag time are left at the default values of zero, and the activation preference
is configured with a value of 2.

  PowerShell

  Add-MailboxDatabaseCopy -Identity DB1 -MailboxServer MBX3 -ActivationPreference 2

This example adds a copy of mailbox database DB2 to the Mailbox server MBX4. Replay lag
time and truncation lag time are left at the default values of zero, and the activation preference
is configured with a value of 5 . In addition, seeding is being postponed for this copy so that it

<!-- p.2753 -->

can be seeded using a local source server instead of the current active database copy, which is
geographically distant from MBX4.

  PowerShell

  Add-MailboxDatabaseCopy -Identity DB2 -MailboxServer MBX4 -ActivationPreference 5
  -SeedingPostponed

This example adds a copy of mailbox database DB3 to the Mailbox server MBX5. Replay lag
time is set to 3 days, truncation lag time is left at the default value of zero, and the activation
preference is configured with a value of 4 .

  PowerShell

  Add-MailboxDatabaseCopy -Identity DB3 -MailboxServer MBX5 -ReplayLagTime
  3.00:00:00 -ActivationPreference 4

How do you know this worked?
To verify that you have successfully created a mailbox database copy, do one of the following:

     In the EAC, navigate to Servers > Databases. Select the database that was copied. In the
     Details pane, the status of the database copy and its content index are displayed, along
     with the current copy queue length.

     In the Exchange Management Shell, run the following command to verify the mailbox
     database copy was created and is healthy.

        PowerShell

        Get-MailboxDatabaseCopyStatus <DatabaseCopyName>

     The Status and Content Index State should both be Healthy.

For more information
Mailbox database copies

Manage mailbox database copies

<!-- p.2754 -->

Configure mailbox database copy
properties in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019       Subscription Edition

Each mailbox database copy has its own properties, which you can configure. These properties
include the amount of time, if any, for replay lag and truncation lag, and the activation
preference number. For more information about replay lag, truncation lag and, the activation
preference number, see Manage mailbox database copies.

What do you need to know before you begin?
      Estimated time to complete this task: 1 minute

      To open the Exchange Admin Center (EAC), see Exchange admin center in Exchange
      Server. To open the Exchange Management Shell, see Open the Exchange Management
      Shell.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox database copies" entry
      in the High availability and site resilience permissions topic.

      For information about keyboard shortcuts that applies to the procedures in this topic, see
      Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online         , or Exchange Online Protection .

Use the EAC to configure mailbox database copy
properties
   1. In the EAC, go to Servers > Databases.

   2. Select the database you want to configure.

   3. In the Details pane, under Database Copies, click View details for the desired database
      copy, and then view or configure the following:

<!-- p.2755 -->

Database: Displays the name of the selected database.

Mailbox server: Displays the name of the Mailbox server that hosts the selected
database copy.

Content index state: Displays the current state of the content index for the selected
database copy.

Status: Displays the current status of the selected database copy.

Copy queue length: Indicates the number of log files waiting to be copied to the
selected database copy. This field is relevant only for passive database copies.

Replay queue length: Indicates the number of log files waiting to be replayed into
the selected database copy. This field is relevant only for passive database copies.

Error messages: Displays any error messages for database copies that have a status
of Failed or Failed and Suspended .

Latest available log time: Displays the date and time stamp of the most recently
generated log file on the active copy of the database. This field is relevant only for
passive database copies. On active database copies (replicated and stand-alone),
this field displays never.

Last inspected log time: Displays the date and time stamp of the last log file
inspected by the LogInspector on the selected database copy. This field is relevant
only for passive database copies. On active database copies (replicated and stand-
alone), this field displays never.

Last copied log time: Displays the date and time stamp of the last log file copied by
the LogCopier on the selected database copy. This field is relevant only for passive
database copies. On active database copies (replicated and stand-alone), this field
displays never.

Last replayed log time: Displays the date and time stamp of the last log file
replayed by the LogReplayer into the selected database copy. This field is relevant
only for passive database copies. On active database copies (replicated and stand-
alone), this field displays never.

Activation preference number: Displays the activation preference number. This is
used as part of Active Manager's best copy selection process, and used to balance
the DAG by redistributing active mailbox databases throughout the DAG via the
DAG's PreferenceMoveFrequency property. This property defines the frequency
(measured in time) when the Microsoft Exchange Replication service rebalances

<!-- p.2756 -->

           database copies by performing a lossless switchover that activates the copy with an
           activation preference number of 1. The value for activation preference is a number
           equal to or greater than 1, where 1 is at the top of the preference order. The number
           can't be larger than the number of copies of the mailbox database.

           Replay lag time (days): Displays the amount of time that the Microsoft Exchange
           Information Store service should wait before replaying log files copied by the
           Microsoft Exchange Replication service to the passive database copy. Setting this
           parameter to a value greater than 0 creates a lagged database copy. The default
           setting for this value is 0 days. The maximum allowable value for this setting is 14
           days. The minimum allowable value is 0 days, and setting this value to 0 disables
           replay lag.

Use the Exchange Management Shell to configure
mailbox database copy properties
This example configures a mailbox database copy with an activation preference number of 3.

  PowerShell

  Set-MailboxDatabaseCopy -Identity DB3\EX3 -ActivationPreference 3

This example configures a copy of the database DB1 hosted on Server1 with a replay lag time
and truncation lag time of 1 day, and an activation preference number of 2.

  PowerShell

  Set-MailboxDatabaseCopy -Identity DB1\Server1 -ReplayLagTime 1.0:0:0 -
  TruncationLagTime 1.0:0:0 -ActivationPreference 2

How do you know this worked?
To verify that you successfully configured a mailbox database copy, do one of the options:

     In the EAC, navigate to Servers > Databases. Select the appropriate database, and in the
     Details pane, click View details to view the database copy properties.

     In the Exchange Management Shell, run the following command to display configuration
     information for a database copy.

        PowerShell

<!-- p.2757 -->

      Get-MailboxDatabaseCopyStatus <DatabaseCopyName> | Format-List

For more information
Set-MailboxDatabaseCopy

Get-MailboxDatabaseCopyStatus

Get-MailboxDatabase

<!-- p.2758 -->

Move the mailbox database path for a
mailbox database copy in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

If the mailbox database being moved is replicated to one or more mailbox database copies,
you must follow the procedure in this topic to move the mailbox database path. All copies of a
mailbox database must be located in the same path on each server that hosts a copy. For
example, if database DB1 is located at C:\mountpoints\DB1 on server EX1, copies of DB1 on
servers EX2, EX3, and so on, must also be located at C:\mountpoints\DB1.

  ７ Note

  After you create a new mailbox database, you can move it to another volume, folder,
  location, or path by using either the EAC or the Exchange Management Shell. For step-by-
  step instructions about how to move the database path for a non-replicated mailbox
  database, see Manage mailbox databases in Exchange Server.

Looking for other management tasks related to mailbox database copies? Check out Managing
mailbox database copies.

What do you need to know before you begin?
      Estimated time to complete this task: 2 minutes, plus the time to move the data, which
      depends on a variety of factors, such as the size of the database, the speed, available
      bandwidth and latency of the network, and storage speeds.

      You need to be assigned permissions before you can perform this procedure or
      procedures. To see what permissions you need, see the "Mailbox database copies" entry
      in the High availability and site resilience permissions topic.

      To perform the move operation, the database must be temporarily dismounted, making it
      inaccessible to all users. If the database is currently dismounted, it isn't remounted upon
      completion.

      To perform the move operation, replication for the database must be disabled for all
      copies. It's not enough to suspend replication; you must disable it by using the Remove-
      MailboxDatabaseCopy cmdlet to remove the database copies.

<!-- p.2759 -->

   For information about keyboard shortcuts that may apply to the procedures in this topic,
   see Keyboard shortcuts in the Exchange admin center.

  Tip

 Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
 Server , Exchange Online     , or Exchange Online Protection .

Use the Exchange Management Shell to move a
replicated mailbox database to a new path

 ７ Note

 You can't use the Exchange admin center (EAC) to move a replicated mailbox database to
 a new path.

 1. Note any replay lag or truncation lag settings for all copies of the mailbox database being
   moved. You can obtain this information by using the Get-MailboxDatabase cmdlet, as
   shown in this example.

      PowerShell

      Get-MailboxDatabase DB1 | Format-List *lag*

 2. If circular logging is enabled for the database, it must be disabled before proceeding. You
   can disable circular logging for a mailbox database by using the Set-MailboxDatabase
   cmdlet, as shown in this example.

      PowerShell

      Set-MailboxDatabase DB1 -CircularLoggingEnabled $false

 3. Remove all mailbox database copies for the database being moved. For detailed steps,
   see Remove a mailbox database copy. After all copies are removed, preserve the database
   and transaction log files from each server from which the database copy is being
   removed by moving them to another location. These files are being preserved so the
   database copies don't require re-seeding after they have been re-added.

 4. Move the mailbox database path to the new location. For detailed steps, see Move a
   mailbox database path.

<!-- p.2760 -->

      ） Important

      During the move operation, the database being moved must be dismounted. Until
      the move is complete, this process will cause an interruption in service and an
      outage for all users with mailboxes on the database being moved. After the move
      operation completes, the database is automatically mounted.

 5. Create the necessary folder structure on each Mailbox server that previously contained a
   passive copy of the moved mailbox database. For example, if you moved the database to
   C:\mountpoints\DB1, you must create this same path on each Mailbox server that will
   host a mailbox database copy.

 6. After creating the folder structure, move the passive copy of the mailbox database and its
   log stream to the new location. These are the files that were left from and preserved after
   Step 3. Repeat this process for each database copy that was removed in Step 3.

 7. Add all of the database copies that were removed in Step 3. For detailed steps, see Add a
   mailbox database copy.

 8. On each server that contains a copy of the mailbox database being moved, run the
   following command to stop and restart the content index services.

      PowerShell

      Restart-Service MSExchangeFastSearch

 9. Optionally, enable circular logging by using the Set-MailboxDatabase cmdlet, as shown in
   this example.

      PowerShell

      Set-MailboxDatabase DB1 -CircularLoggingEnabled $true

10. Reconfigure any previously set values for replay lag time and truncation lag time by using
   the Set-MailboxDatabaseCopy cmdlet, as shown in this example.

      PowerShell

      Set-MailboxDatabaseCopy DB1\MBX2 -ReplayLagTime 00:15:00

11. As each copy is added, we recommend that you verify the health and status of the copy
   prior to adding the next copy. You can verify the health and status by:
