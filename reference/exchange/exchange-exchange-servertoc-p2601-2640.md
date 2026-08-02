---
title: "Exchange Server — pages 2601-2640"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2601-2640
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2601-2640
family: exchange
documentKind: "doc"
abstract: "Lagged copy enhancements Lagged copy enhancements include integration with Safety Net and automatic play down of log files in certain scenarios. Safety Net was introduced in Exchange 2013 to replace the Exchange 2010 feature known as the transport dumpster. Safety Net is similar"
---

# Exchange Server — pages 2601-2640

<!-- p.2601 -->

Lagged copy enhancements
Lagged copy enhancements include integration with Safety Net and automatic play down of
log files in certain scenarios. Safety Net was introduced in Exchange 2013 to replace the
Exchange 2010 feature known as the transport dumpster. Safety Net is similar to the transport
dumpster, in that it's a delivery queue that's associated with the Transport service on a Mailbox
server. This queue stores copies of messages that were successfully delivered to the active
mailbox database on the Mailbox server. Each active mailbox database on the Mailbox server
has its own queue that stores copies of the delivered messages. You can specify how long
Safety Net stores copies of the successfully delivered messages before they expire and are
automatically deleted.

Safety Net takes some responsibility from shadow redundancy in DAG environments. In DAG
environments, shadow redundancy doesn't need to keep another copy of the delivered
message in a shadow queue while it waits for the delivered message to replicate to the passive
copies of mailbox databases on the other Mailbox servers in the DAG. The copy of the
delivered message is already stored in Safety Net, so shadow redundancy can redeliver the
message from Safety Net if necessary.

With Safety Net, activating a lagged database copy becomes easier. For example, consider a
lagged copy that has a 2-day replay lag. In that case, you would configure Safety Net for a
period of 2 days. If you encounter a situation in which you need to use your lagged copy, you
can:

   1. Suspend replication to it.

   2. Copy it twice (to preserve the lagged nature of the database and to create an extra copy
       in case you need it).

   3. Take a copy and discard all the log files, except for those in the required range.

   4. Mount the copy, which triggers an automatic request to Safety Net to redeliver the last
       two days of mail.

With Safety Net, you don't need to hunt for where the point of corruption was introduced. You
get the last two days mail, minus the data ordinarily lost on a lossy failover.

Lagged copies can now care for themselves by invoking automatic log replay to play down the
log files in certain scenarios:

       When a low disk space threshold is reached

       When the lagged copy has physical corruption and needs to be page patched

<!-- p.2602 -->

     When there are fewer than three available healthy copies (active or passive only; lagged
     database copies are not counted) for more than 24 hours

In Exchange 2010, page patching wasn't available for lagged copies. In Exchange 2013 or later,
page patching is available for lagged copies through this automatic play down feature. If the
system detects that page patching is required for a lagged copy, the logs are automatically
replayed into the lagged copy to perform page patching. Lagged copies also invoke this auto
replay feature when a low disk space threshold has been reached, and when the lagged copy
has been detected as the only available copy for a specific period of time.

Lagged copy play down behavior is disabled by default, and can be enabled by running the
following command.

  PowerShell

  Set-DatabaseAvailabilityGroup <DAGName> -ReplayLagManagerEnabled $true

After being enabled, play down occurs when there are fewer than three copies. You can change
the default value of 3, by modifying the following DWORD registry value.

HKLM\Software\Microsoft\ExchangeServer\v15\Replay\Parameters\ReplayLagManagerNum
AvailableCopies

To enable play down for low disk space thresholds, you must configure the following registry
entry.

HKLM\Software\Microsoft\ExchangeServer\v15\Replay\Parameters\ReplayLagLowSpacePlay
downThresholdInMB

After configuring either of these registry settings, restart the Microsoft Exchange DAG
Management service for the changes to take effect.

As an example, consider an environment where a given database has four copies (three highly
available copies and one lagged copy), and the default setting is used for
ReplayLagManagerNumAvailableCopies. If a non-lagged copy is out-of-service for any reason
(for example, it is suspended, etc.) then the lagged copy will automatically play down its log
files in 24 hours.

Single copy alert enhancements
Ensuring that your servers are operating reliably and that your mailbox database copies are
healthy are primary objectives of daily Exchange messaging operations. You must actively
monitor the hardware, the Windows operating system, and the Exchange services.

<!-- p.2603 -->

But in an Exchange mailbox resiliency environment, it's important that you monitor the health
and status of the DAG and your mailbox database copies. It's especially vital to perform data
redundancy risk management and monitor for periods in which a replicated database is down
to just a single copy. This is critical in environments that don't use Redundant Array of
Independent Disks (RAID) and instead deploy JBOD configurations. In a RAID environment, a
single disk failure doesn't affect an active mailbox database copy. However, in a JBOD
environment, a single disk failure will trigger a database failover.

The CheckDatabaseRedundancy.ps1 script was introduced in Exchange 2010. As its name
implies, the purpose of the script was to monitor the redundancy of replicated mailbox
databases by validating that there is at least two configured, healthy, and current copies, and
to alert an administrator through event log generation when only a single healthy copy of a
replicated database exists. In this case, both active and passive copies are counted when
determining redundancy.

Single copy conditions include, but aren't limited to:

     Failure of an active copy to replicate to any passive copy.

     Failure of all passive copies, which includes FailedAndSuspended and Failed states in
     addition to healthy states where the copy is behind in log copying or replay. Lagged
     copies aren't considered behind if they're within 10 minutes in replaying their logs to
     their lag period.

     Failure of the system to accurately know the current log generation of the active copy.

Because it's a top priority for administrators to know when they're down to a single healthy
copy of a database, the CheckDatabaseRedundancy.ps1 script has been replaced with
integrated, native functionality that's part of managed availability's DataProtection Health Set.

The native functionality still alerts administrators through event log notifications, and to
distinguish Exchange 2013 or later alerts from Exchange 2010, Exchange now uses the
following Event IDs:

     Event 4138 (Red Alert)

     Event 4139 (Green Alert)

The native functionality has been enhanced to reduce alert noise that occurs when multiple
databases on the same server enter into a single copy condition. In Exchange 2010, single copy
alerts were generated on a per-database level. As a result, a server-wide issue that affected
multiple databases and multiple database copies could cause alert storms. Because several
failures are server-wide (for example, controller or memory problems), there was a good
chance that an alert storm would occur for each server incident.

<!-- p.2604 -->

Alerts are now generated on a per-server basis. When an outage affects an entire server and
data redundancy becomes at risk for multiple database copies, a single per-server alert is
generated.

DAG network auto-configuration
A DAG network is a collection of one or more subnets used for either replication traffic or MAPI
traffic. Each DAG contains a maximum of one MAPI network and zero or more replication
networks.

In Exchange 2010, the initial DAG networks (for example, DAGNetwork01 and DAGNetwork02)
were created by the system based on the subnets that were enumerated by the Cluster service.
If you had multiple networks and the interfaces for a specified network (for example, the MAPI
network) were on the same subnet, there was little additional configuration required. However,
if the interfaces for a specified network were on multiple subnets, you needed to perform a
task known as collapsing DAG networks.

In Exchange 2013 or later, collapsing DAG networks is no longer necessary. Exchange still uses
the same detection mechanisms to distinguish between the MAPI and replication networks, but
it now automatically collapses DAG networks as appropriate.

In addition, by default, DAG networks are now automatically managed by the system. To view
DAG network properties using the Exchange admin center (EAC), you must configure the DAG
for manual network control by modifying the properties of the DAG using EAC, or by using the
Set-DatabaseAvailabilityGroup cmdlet to set the ManualDagNetworkConfiguration parameter
to $true .

Changes to best copy selection
Best copy selection (BCS) is an internal algorithm process for finding the best copy of an
individual database to activate, given a list of potential copies for activation and their health
and status. Active Manager selects the best available (and unblocked) copy to become the new
active database copy when the existing active database copy fails or when an administrator
performs a targetless switchover. In Exchange 2010, the BCS process evaluated several aspects
of each database copy to determine the best copy to activate. These included:

     Copy queue length

     Replay queue length

     Database status

<!-- p.2605 -->

     Content index status

In Exchange 2013 or later, Active Manager performs the same BCS checks and phases to
determine replication health, but it now also includes the use of a constraint of the decreasing
order of health states. As a result of these changes, BCS is now called best copy and server
selection (BCSS).

BCSS includes several new health checks that are now part of the built-in managed availability
monitoring components in Exchange. There are four additional checks performed by Active
Manager (listed in the order in which they're performed):

   1. All Healthy: Checks for a server hosting a copy of the affected database that has all
     monitoring components in a healthy state.

   2. Up to Normal Healthy: Checks for a server hosting a copy of the affected database that
     has all monitoring components with Normal priority in a healthy state.

   3. All Better than Source: Checks for a server hosting a copy of the affected database that
     has monitoring components in a state that's better than the current server hosting the
     affected copy.

   4. Same as Source: Checks for a server hosting a copy of the affected database that has
     monitoring components in a state that's the same as the current server hosting the
     affected copy.

If BCSS is invoked as a result of a failover that's triggered by a managed availability monitoring
component (for example, via a Failover responder), an additional mandatory constraint is
enforced where the target server's component health must be better than the server on which
the failover occurred. For example, if a failure of Outlook on the web (formerly known as
Outlook Web App) triggers a managed availability failover via a Failover responder, BCSS must
select a server hosting a copy of the affected database on which Outlook on the web is healthy.

DAG Management Service
Exchange 2013 CU2 or later includes the Microsoft Exchange DAG Management Service
(MSExchangeDAGMgmt). This service contains the internal DAG monitoring functionality that
was previously inside the Microsoft Exchange Replication service (MSExchangeRepl).

DAGs without a cluster administrative access point
All DAGs on Exchange servers running Windows Server 2008 R2 or Windows Server 2012
require at least one IP address on every subnet included in the MAPI network. The IP

<!-- p.2606 -->

address(es) assigned to the DAG are used by the DAG's cluster with the cluster's administrative
access point (also known as the cluster network name) to enable name resolution and
connectivity to the cluster (or more precisely, connectivity to the cluster member that currently
owns the cluster core resource group) using the cluster name.

Windows Server 2012 R2 or later enables you to create a failover cluster without an
administrative access point. Windows failover clusters without administrative access points
have the following characteristics:

     No IP address is assigned to the cluster, so there's no IP Address Resource in the cluster
     core resource group.

     No network name is assigned to the cluster, so there's no Network Name Resource in the
     cluster core resource group.

     The name of the cluster isn't registered in DNS and the cluster name isn't resolvable on
     the network.

     A cluster name object (CNO) isn't created in Active Directory.

     You can't manage the Windows failover cluster using the Failover Cluster Management
     tool. Instead, you need to use Windows PowerShell and you need to run the PowerShell
     cmdlets against the individual cluster members.

Exchange 2013 SP1 or later running on Exchange on Windows Server 2012 R2 or later enables
you to create a DAG without a cluster administrative access point. For more information, see
Creating DAGs and Create a database availability group.

<!-- p.2607 -->

Database availability groups
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

A database availability group (DAG) is the base component of the Mailbox server high
availability and site resilience framework built into Microsoft Exchange Server. A DAG is a group
of up to 16 Mailbox servers that hosts a set of databases and provides automatic database-
level recovery from failures that affect individual servers or databases.

  ） Important

  All servers within a DAG must be running the same version of Exchange. For example, you
  can't mix Exchange 2013 servers and Exchange 2016 servers in the same DAG.

A DAG is a boundary for mailbox database replication, database and server switchovers and
failovers, and an internal component called Active Manager. Active Manager, which runs on
every Mailbox server, manages switchovers and failovers within DAGs. For more information
about Active Manager, see Active Manager.

Any server in a DAG can host a copy of a mailbox database from any other server in the DAG.
When a server is added to a DAG, it works with the other servers in the DAG to provide
automatic recovery from failures that affect mailbox databases, such as a disk, server, or
network failure.

  ７ Note

  For more information about creating DAGs, managing DAG membership, configuring DAG
  properties, creating and monitoring mailbox database copies, and performing switchovers,
  see Managing high availability and site resilience.

Database availability group lifecycle
DAGs leverage the concept of incremental deployment, which is the ability to deploy service
and data availability for all Mailbox servers and databases after Exchange is installed. After you
deploy Exchange Server Mailbox servers, you can create a DAG, add Mailbox servers to the
DAG, and then replicate mailbox databases between the DAG members.

  ７ Note

<!-- p.2608 -->

  It's supported to create a DAG that contains a combination of physical Mailbox servers
  and virtualized Mailbox servers, provided that the servers and solution comply with the
  Exchange Server system requirements and the requirements set forth in Exchange Server
  virtualization. As with all Exchange high availability configurations, you must ensure that
  all Mailbox servers in the DAG are sized appropriately to handle the necessary workload
  during scheduled and unscheduled outages.

A DAG is created by using the New-DatabaseAvailabilityGroup cmdlet. A DAG is initially created
as an empty object in Active Directory. This directory object is used to store relevant
information about the DAG, such as server membership information and some DAG
configuration settings. When you add the first server to a DAG, a failover cluster is
automatically created for the DAG. This failover cluster is used exclusively by the DAG, and the
cluster must be dedicated to the DAG. Use of the cluster for any other purpose isn't supported.

In addition to a failover cluster being created, the infrastructure that monitors the servers for
network or server failures is initiated. The failover cluster heartbeat mechanism and cluster
database are then used to track and manage information about the DAG that can change
quickly, such as database mount status, replication status, and last mounted location.

During creation, the DAG is given a unique name, and either assigned one or more static IP
addresses or configured to use Dynamic Host Configuration Protocol (DHCP), or created
without a cluster administrative access point. DAGs without an administrative access point can
be created only on servers running Exchange 2019, Exchange 2016, or Exchange 2013 Service
Pack 1 or later, with Windows Server 2012 R2 Standard or Datacenter edition. DAGs without
cluster administrative access points have the following characteristics:

     There is no IP address assigned to the cluster/DAG, and therefore no IP Address Resource
     in the cluster core resource group.

     There is no network name assigned to the cluster, and therefore no Network Name
     Resource in the cluster core resource group

     The name of the cluster/DAG is not registered in DNS, and it is not resolvable on the
     network.

     A cluster name object (CNO) is not created in Active Directory.

     The cluster cannot be managed using the Failover Cluster Management tool. It must be
     managed using Windows PowerShell, and the PowerShell cmdlets must be run against
     individual cluster members.

This example shows you how to use the Exchange Management Shell to create a DAG with a
cluster administrative access point that will have three servers. Two servers (EX1 and EX2) are

<!-- p.2609 -->

on the same subnet (10.0.0.0), and the third server (EX3) is on a different subnet (192.168.0.0).

  PowerShell

  New-DatabaseAvailabilityGroup -Name DAG1 -WitnessServer EX4 -
  DatabaseAvailabilityGroupIPAddresses 10.0.0.5,192.168.0.5
  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer EX1
  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer EX2
  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer EX3

The commands to create a DAG without a cluster administrative access point are very similar:

  PowerShell

  New-DatabaseAvailabilityGroup -Name DAG1 -WitnessServer EX4 -
  DatabaseAvailabilityGroupIPAddresses ([System.Net.IPAddress])::None
  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer EX1
  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer EX2
  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer EX3

The cluster for DAG1 is created when EX1 is added to the DAG. During cluster creation, the
Add-DatabaseAvailabilityGroupServer cmdlet retrieves the IP addresses configured for the
DAG and ignores the ones that don't match any of the subnets found on EX1. In the first
example above, the cluster for DAG1 is created with an IP address of 10.0.0.5, and 192.168.0.5 is
ignored. In the second example above, the value of the DatabaseAvailabilityGroupIPAddresses
parameter instructs the task to create a failover cluster for the DAG that does not have an
administrative access point. Thus, the cluster is created with an IP address or network name
resource in the core cluster resource group.

Then, EX2 is added, and the Add-DatabaseAvailabilityGroupServer cmdlet again retrieves the
IP addresses configured for the DAG. There are no changes to the cluster's IP addresses
because in EX2 is on the same subnet as EX1.

Then, EX3 is added, and the Add-DatabaseAvailabilityGroupServer cmdlet again retrieves the
IP addresses configured for the DAG. Because a subnet matching 192.168.0.5 is present on EX3,
the 192.168.0.5 address is added as an IP address resource in the cluster group. In addition, an
OR dependency for the Network Name resource for each IP address resource is automatically
configured. The 192.168.0.5 address will be used by the cluster when the cluster core resource
group moves to EX3.

For DAGs with cluster administrative access points, Windows failover clustering registers the IP
addresses for the cluster in the Domain Name System (DNS) when the Network Name resource
is brought online. In addition, when EX1 is added to the cluster, a cluster name object (CNO) is
created in Active Directory. The network name, IP address(es), and CNO for the cluster are not

<!-- p.2610 -->

used for DAG functions. Administrators and end users don't need to interface with or connect
to the cluster/DAG name or IP address for any reason. Some third-party applications connect
to the cluster administrative access point to perform management tasks, such as backup or
monitoring. If you do not use any third-party applications that require a cluster administrative
access point, and your DAG is running Exchange 2016 or Exchange 2019 on Windows Server
2012 R2, then we recommend creating a DAG without an administrative access point. This
simplifies DAG configuration, eliminates the need for one or more IP addresses, and reduces
the attack surface of a DAG.

DAGs are also configured to use a witness server and a witness directory. The witness server
and witness directory are either automatically configured by the system, or they can be
manually configured by the administrator. In the examples above, EX4 (a server that is not and
will not be a member of the DAG) is being manually configured as the DAG's witness server.

By default, a DAG is designed to use the built-in continuous replication feature to replicate
mailbox databases among servers in the DAG. If you're using third-party data replication that
supports the Third Party Replication API in Exchange Server, you must create the DAG in third-
party replication mode by using the New-DatabaseAvailabilityGroup cmdlet with the
ThirdPartyReplication parameter. After this mode is enabled, it can't be disabled.

After the DAG is created, Mailbox servers can be added to the DAG. When the first server is
added to the DAG, a cluster is formed for use by the DAG. DAGs make use of Windows failover
clustering technology, such as the cluster heartbeat, cluster networks, and the cluster database
(for storing data that changes, such as database state changes from active to passive or vice
versa, or from mounted to dismounted and vice versa). As each subsequent server is added to
the DAG, it's joined to the underlying cluster, the cluster's quorum model is automatically
adjusted by Exchange, and the server is added to the DAG object in Active Directory.

After Mailbox servers are added to a DAG, you can configure a variety of DAG properties, such
as whether to use network encryption or network compression for database replication within
the DAG. You can also configure DAG networks and create additional DAG networks.

After you add members to a DAG and configure the DAG, the active mailbox databases on
each server can be replicated to the other DAG members. After you create mailbox database
copies, you can monitor the health and status of the copies using a variety of built-in
monitoring tools. In addition, you can perform database and server switchovers.

Database availability group quorum models
Underneath every DAG is a Windows failover cluster. Failover clusters use the concept of
quorum, which uses a consensus of voters to ensure that only one subset of the cluster
members (which could mean all members or a majority of members) is functioning at one time.

<!-- p.2611 -->

Quorum isn't a new concept for Exchange Server. Highly available Mailbox servers in previous
versions of Exchange also use failover clustering and its concept of quorum. Quorum
represents a shared view of members and resources, and the term quorum is also used to
describe the physical data that represents the configuration within the cluster that's shared
between all cluster members. As a result, all DAGs require their underlying failover cluster to
have quorum. If the cluster loses quorum, all DAG operations terminate and all mounted
databases hosted in the DAG dismount. In this event, administrator intervention is required to
correct the quorum problem and restore DAG operations.

Quorum is important to ensure consistency, to act as a tie-breaker to avoid partitioning, and to
ensure cluster responsiveness:

     Ensuring consistency: A primary requirement for a Windows failover cluster is that each
     of the members always has a view of the cluster that's consistent with the other members.
     The cluster hive acts as the definitive repository for all configuration information relating
     to the cluster. If the cluster hive can't be loaded locally on a DAG member, the Cluster
     service doesn't start, because it isn't able to guarantee that the member meets the
     requirement of having a view of the cluster that's consistent with the other members.

     Acting as a tie-breaker: A quorum witness resource is used in DAGs with an even number
     of members to avoid split brain syndrome scenarios and to make sure that only one
     collection of the members in the DAG is considered official. When the witness server is
     needed for quorum, any member of the DAG that can communicate with the witness
     server can place a Server Message Block (SMB) lock on the witness server's witness.log
     file. The DAG member that locks the witness server (referred to as the locking node)
     retains an additional vote for quorum purposes. The DAG members in contact with the
     locking node are in the majority and maintain quorum. Any DAG members that can't
     contact the locking node are in the minority and therefore lose quorum.

     Ensuring responsiveness: To ensure responsiveness, the quorum model makes sure that,
     whenever the cluster is running, enough members of the distributed system are
     operational and communicative, and at least one replica of the cluster's current state can
     be guaranteed. No additional time is required to bring members into communication or
     to determine whether a specific replica is guaranteed.

DAGs with an even number of members use the failover cluster's Node and File Share Majority
quorum mode, which employs an external witness server that acts as a tie-breaker. In this
quorum mode, each DAG member gets a vote. In addition, the witness server is used to
provide one DAG member with a weighted vote (for example, it gets two votes instead of one).
The cluster quorum data is stored by default on the system disk of each member of the DAG,
and is kept consistent across those disks. However, a copy of the quorum data isn't stored on
the witness server. A file on the witness server is used to keep track of which member has the

<!-- p.2612 -->

most updated copy of the data, but the witness server doesn't have a copy of the cluster
quorum data. In this mode, a majority of the voters (the DAG members plus the witness server)
must be operational and able to communicate with each other to maintain quorum. If a
majority of the voters can't communicate with each other, the DAG's underlying cluster loses
quorum, and the DAG will require administrator intervention to become operational again. For
more information, see Datacenter switchovers and Restore-DatabaseAvailabilityGroup.

DAGs with an odd number of members use the failover cluster's Node Majority quorum mode.
In this mode, each member gets a vote, and each member's local system disk is used to store
the cluster quorum data. If the configuration of the DAG changes, that change is reflected
across the different disks. The change is only considered to have been committed and made
persistent if that change is made to the disks on half the members (rounding down) plus one.
For example, in a five-member DAG, the change must be made on two plus one members, or
three members total.

Quorum requires a majority of voters to be able to communicate with each other. Consider a
DAG that has four members. Because this DAG has an even number of members, an external
witness server is used to provide one of the cluster members with a fifth, tie-breaking vote. To
maintain a majority of voters (and therefore quorum), at least three voters must be able to
communicate with each other. At any time, a maximum of two voters can be offline without
disrupting service and data access. If three or more voters are offline, the DAG loses quorum,
and service and data access will be disrupted until you resolve the problem.

<!-- p.2613 -->

Exchange Server Active Manager
Article • 04/30/2025

APPLIES TO:        2016        2019    Subscription Edition

Microsoft Exchange Server includes a component called Active Manager that manages the high
availability platform that includes the database availability group (DAG) and mailbox database
copies. Active Manager runs inside the Microsoft Exchange Replication service
(MSExchangeRepl.exe) on all Mailbox servers. On Mailbox servers that aren't members of a
DAG, there is a single Active Manager role: Standalone Active Manager.

On servers that are members of a DAG, there are two Active Manager roles: Primary Active
Manager (PAM) and Standby Active Manager (SAM). PAM is the Active Manager role in a DAG
that decides which copies will be active and passive. PAM is responsible for getting topology
change notifications and reacting to server failures. The DAG member that holds the PAM role
is always the member that currently owns the cluster quorum resource (default cluster group).
If the server that owns the cluster quorum resource fails, the PAM role automatically moves to
a surviving server that takes ownership of the cluster quorum resource. In addition, if you need
to take the server that hosts the cluster quorum resource offline for maintenance or an
upgrade, you must first move the PAM to another server in the DAG. The PAM controls all
movement of the active designations between a database's copies. (Only one copy can be
active at any specified time, and that copy may be mounted or dismounted.) The PAM also
performs the functions of the SAM role on the local system (detecting local database and local
Information Store failures).

The SAM provides information on which server hosts the active copy of a mailbox database to
other components of Exchange that are running an Active Manager client component (for
example, Client Access or Transport services). The SAM detects failures of local databases and
the local Information Store. It reacts to failures by asking the PAM to initiate a failover (if the
database is replicated). A SAM doesn't determine the target of failover, nor does it update a
database's location state in the PAM. It will access the active database copy location state to
answer queries for the active copy of the database that it receives.

  ７ Note

  Exchange Server isn't a clustered application. Instead, it uses the cluster library functions
  implemented in clusapi.dll for cluster, group, cluster network (heartbeating), node
  management, cluster registry, and a few control code functions. In addition, Active
  Manager stores current mailbox database information (for example, active and passive
  data, and mounted data) in the cluster database (also known as the cluster registry).

<!-- p.2614 -->

  Although the information is stored directly in the cluster database, it isn't accessed directly
  by any other components.

In Exchange Server, the Microsoft Exchange Replication service periodically monitors the health
of all mounted databases. In addition, it also monitors the Extensible Storage Engine (ESE) for
any I/O errors or failures. When the service detects a failure, it notifies Active Manager. Active
Manager then determines which database copy should be mounted and what it requires to
mount that database. In addition, it tracks the active copy of a mailbox database (based on the
last mounted copy of the database) and provides the tracking results information to Client
Access services on the Mailbox server to which the client is connected.

Best Copy Selection
When a failure occurs that prevents access to the active copy of a replicated mailbox database,
Active Manager selects the best possible passive copy of the affected database to activate. This
process was known as best copy selection (BCS) in earlier versions of Exchange, and in
Exchange 2016 and Exchange 2019 it's known as best copy and server selection (BCSS). The
general process occurs in the following order:

   1. Managed availability or Active Manager detects a failure, or an administrator initiates a
     targetless switchover.

   2. The PAM runs the BCSS internal algorithm.

   3. A process called attempt copy last logs (ACLL) occurs, which tries to copy any missing log
     files from the server that hosted the active database copy prior to the failure or
     switchover.

   4. After the ACLL process has completed, the value of the AutoDatabaseMountDial for the
     Mailbox servers hosting copies of the database is compared with the copy queue length
     of the database being activated. At this point, either:

           The number of missing log files is equal to or less than the value of
           AutoDatabaseMountDial, in which case Step 5 occurs.

           The number of missing log files is greater than the value of AutoDatabaseMountDial,
           in which case Active Manager will try to activate next best available copy, if there is
           one.

   5. The PAM issues a mount request to the Microsoft Exchange Information Store via remote
     procedure call (RPC). At this point, either:

           The database mounts and is made available to clients.

<!-- p.2615 -->

           The database doesn't mount, and PAM performs steps 3 and 4 on the next best
           copy (if one is available).

In earlier versions of Exchange, the BCS process evaluated several aspects of each database
copy to determine the best copy to activate. These included:

     Copy queue length

     Replay queue length

     Database status

     Content index status

In Exchange Server, Active Manager runs through all of the same BCS checks and phases, but
now it also includes the use of a constraint of the decreasing order of health states. Specifically,
BCSS includes several new health checks that are part of the built in managed availability
monitoring components in Exchange Server. There are four additional checks performed by
Active Manager (listed in the order in which they are performed):

   1. All Healthy: Checks for a server hosting a copy of the affected database that has all
     monitoring components in a healthy state.

   2. Up to Normal Healthy: Checks for a server hosting a copy of the affected database that
     has all monitoring components with Normal priority in a healthy state.

   3. All Better than Source: Checks for a server hosting a copy of the affected database that
     has monitoring components in a state that's better than the current server hosting the
     affected copy.

   4. Same as Source: Checks for a server hosting a copy of the affected database that has
     monitoring components in a state that's the same as the current server hosting the
     affected copy.

If BCSS is invoked as a result of a failover that's triggered by a monitoring component (for
example, via a Failover responder), an additional mandatory constraint is enforced where the
target server's component health must be better than the server on which the failover
occurred. For example, if a failure of Outlook on the web triggers a failover via a Failover
responder, BCSS must select a server hosting a copy of the affected database on which
Outlook on the web is healthy.

Best copy selection process
With respect to database failures (not protocol failures), Active Manager begins the best copy
selection process by creating a list of database copies that are potential candidates for

<!-- p.2616 -->

activation. Any database copies that are unreachable or are administratively blocked from
activation are ignored and not used during the selection process. The order of the list depends
on the value of the AutoDatabaseMountDial:

      If the AutoDatabaseMountDial is configured with any value other than Lossless on all
      servers that host a copy of the database, Active Manager sorts the resulting list using the
      copy queue length as the primary key. The calculation is based on LastLogInspected (from
      the copy's point of view), so the list of potential copies is sorted by the highest value for
      LastLogInspected (which will be the copy with the lowest copy queue length). If necessary,
      Active Manager sorts the list a second time, using the value for activation preference as a
      secondary key to break any tie conditions where two or more passive copies have the
      same copy queue length. The copy with the lowest activation preference value has the
      higher priority on the list.

      If the AutoDatabaseMountDial is configured with a value of Lossless on any server that
      hosts a copy of the database, Active Manager sorts the resulting list in ascending order by
      using the value for activation preference as the primary key. In addition, when an
      administrator performs a lossless server or database switchover without specifying a
      target, Active Manager also sorts the resulting list in ascending order by using the value
      for activation preference as the primary key.

Next, Active Manager attempts to locate a mailbox database copy on the list that has a status
of Healthy, DisconnectedAndHealthy, DisconnectedAndResynchronizing, or SeedingSource,
and then evaluates the activation potential of each of the copies on the list by using an order
set of ten criteria. Active Manager determines if any of the candidates for activation meet the
first set of criteria:

      It has a content index with a status of Healthy.

      It has a copy queue length less than 10 log files.

      It has a replay queue length less than 50 log files.

If none of the database copies meets the first set of criteria, Active Manager tries to locate a
database copy that meets the second set of criteria:

      It has a content index with a status of Crawling.

      It has a copy queue length less than 10 log files.

      It has a replay queue length less than 50 log files.

If none of the database copies meets the second set of criteria, Active Manager tries to locate a
database copy that meets the third set of criteria:

<!-- p.2617 -->

     It has a content index with a status of Healthy.

     It has a replay queue length less than 50 log files.

If none of the database copies meets the third set of criteria, Active Manager tries to locate a
database copy that meets the fourth set of criteria:

     It has a content index with a status of Crawling.

     It has a replay queue length less than 50 log files.

If none of the database copies meets the fourth set of criteria, Active Manager tries to locate a
database copy that meets the fifth set of criteria:

     It has a replay queue length less than 50 log files.

If none of the database copies meets the fifth set of criteria, Active Manager tries to locate a
database copy that meets the sixth set of criteria:

     It has a content index with a status of Healthy.

     It has a copy queue length less than 10 log files.

If none of the database copies meets the sixth criteria, Active Manager tries to locate a
database copy that meets the seventh set of criteria:

     It has a content index with a status of Crawling.

     It has a copy queue length less than 10 log files.

If none of the database copies meets the seventh set of criteria, Active Manager tries to locate
a database copy that meets the eighth set of criteria:

     It has a content index with a status of Healthy.

If none of the database copies meets all of the eighth set of criteria, Active Manager tries to
locate a database copy that meets the ninth set of criteria:

     It has a content index with a status of Crawling.

If none of the database copies meets the ninth set of criteria, Active Manager tries to activate
any database copy with a status of Healthy, DisconnectedAndHealthy,
DisconnectedAndResynchronizing, or SeedingSource (the tenth set of criteria). If it can't find
any database copies that meet the tenth set of criteria, it isn't able to automatically activate a
database copy.

<!-- p.2618 -->

After one or more copies are located that meet one or more sets of criteria, the ACLL process
copies any log files from the original source to the potential new active copy. After the ACLL
process has completed, the PAM issues a mount request and either the database mounts and is
made available to clients, or the database doesn't mount and the PAM searches for the next
best copy (if one is available).

<!-- p.2619 -->

Datacenter Activation Coordination mode
in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

Datacenter Activation Coordination (DAC) mode is a property of a database availability group
(DAG). DAC mode is disabled by default but should be enabled for all DAGs with two or more
members that use continuous replication. DAC mode shouldn't be enabled for DAGs that use
third-party replication mode unless specified by the third-party vendor.

DAC mode is used to control the database mount on startup behavior of a DAG. This control is
designed to prevent split brain from occurring at the database level during a datacenter
switchback. Split brain, also known as split brain syndrome, is a condition that results in a
database being mounted as an active copy on two members of the same DAG that are unable
to communicate with one another. Split brain is prevented using DAC mode, because DAC
mode requires DAG members to obtain permission to mount databases before they can be
mounted.

For example, when a primary datacenter contains two DAG members and the witness server,
and a second datacenter contains two other DAG members, the DAG isn't in DAC mode. The
primary datacenter loses power, so you activate the DAG in the second datacenter. Eventually
power to the primary datacenter is restored, and the DAG members in the primary datacenter,
which had quorum before the power failure, will start up and mount their databases. Because
the primary datacenter was restored without network connectivity to the second datacenter,
and because the DAG wasn't in DAC mode, the active databases within the DAG enters a split
brain condition.

How DAC mode works
DAC mode includes a protocol called Datacenter Activation Coordination Protocol (DACP).
When DAC mode is enabled, DAG members won't automatically mount databases even if they
have quorum. Instead DACP is used to determine the current state of the DAG and whether
Active Manager should attempt to mount the databases.

You might think of DAC mode as an application level of quorum for mounting databases. To
understand the purpose of DACP and how it works, it's important to understand the primary
scenario it's intended to handle. Consider the two-datacenter scenario described above.
Suppose there's a complete power failure in the primary datacenter. In this event, all of the
servers and the WAN are down, so the organization makes the decision to activate the standby
datacenter. In almost all such recovery scenarios, when power is restored to the primary

<!-- p.2620 -->

datacenter, WAN connectivity is typically not immediately restored. This means that the DAG
members in the primary datacenter will power up, but they won't be able to communicate with
the DAG members in the activated standby datacenter. The primary datacenter should always
contain the majority of the DAG quorum voters, which means that when power is restored,
even in the absence of WAN connectivity to the DAG members in the standby datacenter, the
DAG members in the primary datacenter have a majority and therefore have quorum. This is a
problem because with quorum, these servers may be able to mount their databases, which in
turn would cause divergence from the actual active databases that are now mounted in the
activated standby datacenter.

DACP was created to address this issue. Active Manager stores a bit in memory (either a 0 or a
1) that tells the DAG whether it's allowed to mount local databases that are assigned as active
on the server. When a DAG is running in DAC mode, each time Active Manager starts up the bit
is set to 0, meaning it isn't allowed to mount databases. Because it's in DAC mode, the server
must try to communicate with all other members of the DAG that it knows to get another DAG
member to give it an answer as to whether it can mount local databases that are assigned as
active to it. The answer comes in the form of the bit setting for other Active Managers in the
DAG. If another server responds that its bit is set to 1, it means servers are allowed to mount
databases, so the server starting up sets its bit to 1 and mounts its databases.

But when you recover from a primary datacenter power outage where the servers are
recovered but WAN connectivity hasn't been restored, all of the DAG members in the primary
datacenter will have a DACP bit value of 0; and therefore none of the servers starting back up
in the recovered primary datacenter will mount databases, because none of them can
communicate with a DAG member that has a DACP bit value of 1.

DAC mode for DAGs with two members
DAGs with two members have inherent limitations that prevent the DACP bit alone from fully
protecting against application-level split brain syndrome. For DAGs with only two members,
DAC mode also uses the boot time of the DAG's witness server to determine whether it can
mount databases on startup. The boot time of the witness server is compared to the time when
the DACP bit was set to 1.

     If the time the DACP bit was set is earlier than the boot time of the witness server, the
     system assumes that the DAG member and witness server were rebooted at the same
     time (perhaps because of power loss in the primary datacenter), and the DAG member
     isn't permitted to mount databases.

     If the time that the DACP bit was set is more recent than the boot time of the witness
     server, the system assumes that the DAG member was rebooted for some other reason
     (perhaps a scheduled outage in which maintenance was performed or perhaps a system

<!-- p.2621 -->

     crash or power loss isolated to the DAG member), and the DAG member is permitted to
     mount databases.

  ） Important

  Because the witness server's boot time is used to determine whether a DAG member can
  mount its active databases on startup, you should never restart the witness server and the
  sole DAG member at the same time. Doing so may leave the DAG member in a state
  where it can't mount databases on startup. If this happens, you must run the Restore-
  DatabaseAvailabilityGroup cmdlet on the DAG. This resets the DACP bit and permits the
  DAG member to mount databases.

Other benefits of DAC mode
In addition to preventing split brain syndrome at the application level, DAC mode also enables
the use of the built-in site resilience cmdlets used to perform datacenter switchovers. These
include the following:

     Stop-DatabaseAvailabilityGroup

     Restore-DatabaseAvailabilityGroup

     Start-DatabaseAvailabilityGroup

Performing a datacenter switchover for DAGs that aren't in DAC mode involves using a
combination of Exchange tools and cluster management tools. For more information, see
Datacenter switchovers.

Enabling DAC mode
DAC mode can be enabled only by using the Exchange Management Shell. Specifically, you can
use the Set-DatabaseAvailabilityGroup cmdlet to enable DAC mode, as illustrated in the
following example.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG2 -DatacenterActivationMode DagOnly

In the preceding example, DAG2 is enabled for DAC mode.

For more information about enabling DAC mode, see Configure database availability group
properties and Set-DatabaseAvailabilityGroup.

<!-- p.2622 -->

<!-- p.2623 -->

Mailbox database copies in Exchange
Server
Article • 04/30/2025

APPLIES TO:        2016    2019        Subscription Edition

Microsoft Exchange Server leverages the concept of database mobility, which is Exchange-
managed database-level failovers. Database mobility disconnects databases from servers, adds
support for up to 16 copies of a single database, and provides a native experience for adding
database copies to a database.

Key characteristics
The key characteristics of mailbox database copies are:

      Up to 16 copies of an Exchange Server mailbox database can be created on multiple
      Mailbox servers, provided the servers are grouped into a database availability group
      (DAG), which is a boundary for continuous replication. Exchange Server mailbox
      databases can be replicated only to the same version Exchange Mailbox servers within a
      DAG. You can't replicate a database outside of a DAG, nor can you replicate an Exchange
      2016 or Exchange 2019 mailbox database to a server running Exchange 2013 or earlier.
      For detailed information about DAGs, see Database availability groups.

      All Mailbox servers in a DAG must be in the same Active Directory domain.

      Mailbox database copies support the concepts of replay lag time and truncation lag time.
      Appropriate planning must be performed before enabling these features.

      All database copies can be backed up using an Exchange-aware, Volume Shadow Copy
      Service (VSS)-based backup application.

      Database copies can be created only on Mailbox servers that don't host the active copy of
      a database. You can't create two copies of the same database on the same server.

      All copies of a database use the same path on each server containing a copy. The
      database and log file paths for a database copy on each Mailbox server must not conflict
      with any other database paths.

      Database copies can be created in the same or different Active Directory sites, and on the
      same or different network subnets.

      Database copies aren't supported between Mailbox servers with round trip network
      latency greater than 500 milliseconds (ms).

<!-- p.2624 -->

Mailbox database copies
You can create a mailbox database copy at any time. Mailbox database copies can be
distributed across Mailbox servers in a flexible and granular way.

You can create a mailbox database copy using the Add mailbox database copy wizard in the
Exchange admin center or by using the Add-MailboxDatabaseCopy cmdlet in the Exchange
Management Shell.

When creating a mailbox database copy, specify the following parameters:

     Identity: This parameter specifies the name of the database being copied. Database
     names must be unique within the Exchange organization.

     MailboxServer: This parameter specifies the name of the Mailbox server that will host the
     database copy. This server must be a member of the same DAG and must not already
     host a copy of the database.

Optionally, you can also specify:

     ActivationPreference: This parameter specifies the activation preference number, which is
     used as part of Active Manager's best copy selection process. It's also used to redistribute
     active mailbox databases throughout the DAG when using the
     RedistributeActiveDatabases.ps1 script. The value for the activation preference is a
     number equal to or greater than one, where one is at the top of the preference order. The
     position number cannot be larger than the number of mailbox database copies.

     ReplayLagTime: This parameter specifies the amount of time that the Microsoft Exchange
     Replication service should wait before replaying log files that are copied to the database
     copy. The format for this parameter is (Days.Hours:Minutes:Seconds). The default setting
     for this value is 0 seconds. The maximum allowable setting for this value is 14 days. The
     minimum allowable setting is 0 seconds. Setting the value for replay lag time to 0 turns
     off log replay delay.

     TruncationLagTime: This parameter specifies the amount of time that the Microsoft
     Exchange Replication service should wait before truncating log files that have replayed
     into a copy of the database. The time period begins after the log has been successfully
     replayed into the copy of the database. The format for this parameter is
     (Days.Hours:Minutes:Seconds). The default setting for this value is 0 seconds. The
     maximum allowable setting for this value is 14 days. The minimum allowable setting is 0
     seconds. Setting the value for truncation lag time to 0 turns off log truncation delay.

     SeedingPostponed: This parameter specifies that the task shouldn't automatically seed the
     database copy on the specified Mailbox server. This option is typically used when you

<!-- p.2625 -->

     intend to seed a new mailbox database copy by using an existing passive copy of the
     database (for example, adding a second copy of a specific database to a remote location).
     When you use this parameter, you must manually seed the database copy using the
     Update-MailboxDatabaseCopy cmdlet.

For more information about creating, using, and managing mailbox database copies, see
Manage mailbox database copies.

<!-- p.2626 -->

About AutoReseed
08/05/2025

APPLIES TO:        2016       2019        Subscription Edition

Automatic Reseed, or AutoReseed, is a feature that replaces standard actions administrators
take in response to a disk failure, or a database corruption event, or another issue that needs a
reseed of a database copy.

Overview of Autoreseed
In an AutoReseed configuration, a standardized storage presentation structure is used, and the
administrator picks the starting point. AutoReseed is about restoring redundancy as soon as
possible after a drive fails. This configuration involves using mount points to premap a set of
volumes (including spare volumes) and databases. If a disk is no longer available to the
operating system or a disk is no longer writable, the system allocates a spare volume. The
affected database copies are reseeded automatically.

   1. The Microsoft Exchange Replication service periodically scans for copies that have a status
     of FailedAndSuspended. If all database copies on a volume configured for AutoReseed
     are in a FailedandSuspended state for 15 consecutive minutes, the AutoReseed workflow
     is started.

   2. AutoReseed tries to resume the failed and suspended copies up to three times, with a 5-
     minute sleep in between each attempt. Sometimes, after a FailedandSuspended database
     copy is resumed, the copy remains in a Failed state. This issue can happen for various
     reasons, so this step is designed to handle those cases. AutoReseed automatically
     suspends a database copy that is Failed for 10 consecutive minutes to keep the workflow
     running. If the suspend and resume actions don't result in a healthy database copy, the
     workflow continues.

   3. When it finds a copy with that status, it does some prerequisite checks. For example, it
     verifies the following conditions:

             A spare disk is available.
             The database and its log files are configured on the same volume.
             The database and its log files are in the appropriate locations that match the
             required naming conventions.

   4. If the prerequisite checks pass successfully, the Disk Reclaimer function within the
     Microsoft Exchange Replication service allocates, remaps, and formats a spare disk

<!-- p.2627 -->

     according to the timelines in the upcoming table. AutoReseed attempts to assign a spare
     volume up to five times, with one hour sleep in between each try.

   5. Once a spare is assigned, AutoReseed does an InPlaceSeed operation using the
     SafeDeleteExistingFiles seeding switch. All databases that were on the affected disk are
     reseeded using the active copy of the database as the seeding source.

   6. After the seeding operation is completed, the Microsoft Exchange Replication service
     verifies that the newly seeded copy is healthy.

Once all retries are exhausted, the workflow stops. If, after three days, the database copy is still
FailedandSuspended, the workflow state is reset and it starts again from Step 1. This
reset/resume behavior is useful (and intentional) since it can take a few days to replace a failed
disk, controller, and so on.

At this point, if the failure was a disk failure, it would require manual intervention by an
operator or administrator to remove and replace the failed disk and reconfigure the
replacement disk as a spare.

AutoReseed is configured using three properties of the DAG. Two of the properties refer to the
two mount points that are in use. Exchange Server uses the fact that Windows Server allows
multiple mount points per volume. The AutoDagVolumesRootFolderPath property refers to the
mount point that contains all of the available volumes. This property includes volumes that
host databases and spare volumes. The AutoDagDatabasesRootFolderPath property refers to
the mount point that contains the databases. A third DAG property,
AutoDagDatabaseCopiesPerVolume, is used to configure the number of database copies per
volume.

An example AutoReseed configuration is illustrated here:

Example AutoReseed configuration

<!-- p.2628 -->

In this example, there are three volumes, two of which contains databases (VOL1 and VOL2),
and one of which is a blank, formatted spare (VOL3).

To configure AutoReseed:

   1. All three volumes are mounted under a single mount point. In this example, a mount
     point of C:\ExchVols is used. This configuration represents the directory used to get
     storage for Exchange databases.

   2. The root directory of the mailbox databases is mounted as another mount point. In this
     example, a mount point of C:\ExchDBs is used. Next, a directory structure is created so
     that a parent directory is created for the database. Under this parent directory, two
     subdirectories are created: one database file and one for the log files.

   3. Databases are created. The previous example illustrates a simple design using a single
     database per volume. Thus, on VOL1, there are three directories: the parent directory and
     two subdirectories (one for MDB1's database file, and one for its logs). Although not
     shown in the example image, on VOL2, there would also be three directories: the parent
     directory, alongside, a directory for MDB2's database file, and one for its log files.

In this configuration, if MDB1 or MDB2 is to experience a failure, a copy of the failed database
is automatically reseeded to VOL3.

Disk Reclaimer
The AutoReseed component that allocates and formats spare disks is called the Disk Reclaimer.
The Disk Reclaimer component automatically formats spare disks in preparation for automatic

<!-- p.2629 -->

reseeding at different intervals, depending on the state of the disk. In order for the Disk
Reclaimer to format a disk, certain conditions must be met:

     The Disk Reclaimer must be enabled. It's enabled by default, but it can be disabled using
     Set-DatabaseAvailabilityGroup.

     The volume must have a mount point in the root volumes path (by default,
     C:\ExchangeVolumes).

     The volume must not have any mount points in the database volumes path (by default,
     C:\ExchangeDatabases).

     If the volume contains any files, none of the files should be touched for 24 hours.

In addition to the above conditions, the Disk Reclaimer attempts to format a given volume
once a day. The following table describes the formatting behavior of the Disk Reclaimer.

In all examples, the disk is in one of the following states:

     Unformatted.
     Formatted but empty.
     Formatted but containing files that are untouched for 24 hours.

                                                                                              ﾉ    Expand table

 State of database copies                                                                         Formatting
                                                                                                  interval

 There are healthy active database copies in the local Active Directory site that can be          One day
 used as a seeding source.

 There are no healthy active database copies in the local Active Directory site that can be       Two days
 used as a seeding source.

 There are healthy active database copies in the local Active Directory site that can be          Two weeks
 used as a seeding source, but there are unknown files outside of the database file (EDB
 file) and log files.

 There are healthy active database copies in the local Active Directory site that can be          Two weeks
 used as a seeding source, but there are one or more database files (EDB files) for
 databases that aren't present in Active Directory.

<!-- p.2630 -->

MetaCacheDatabase (MCDB) setup
Article • 05/09/2025

APPLIES TO:        2016    2019      Subscription Edition

The MetaCacheDatabase (MCDB) feature is included in Exchange Server 2019. It allows a
database availability group (DAG) to be accelerated by utilizing solid state disks (SSDs). Manage-
MetaCacheDatabase.ps1 is an automation script created for Exchange Server administrators to

set up and manage MCDB instances in their Exchange 2019 DAGs.

After installing Exchange Server 2019, you can find Manage-MetaCacheDatabase.ps1 here:
drive:\Program Files\Microsoft\Exchange Server\V15\Scripts. To make the Manage-MCDB
CMDLet available in your Exchange Management Shell session, do the following:

  PowerShell

  cd $exscripts
  . .\Manage-MetaCacheDatabase.ps1

You use this script to configure MCDB prerequisites on a properly configured DAG, to enable or
disable MCDB, and to configure and repair MCDB on your servers.

SSD guidance
All SSDs used for MCDB need to be of the same capacity and type. A symmetrical configuration
between servers is required, which means there needs to be an identical number of SSDs in
each server, and the SSDs all need to be the same size.

  ７ Note

  The Manage-MCDB cmdlet will only work with devices exposed as MediaType SSD by
  Windows.

It's recommended to target a 1:3 ratio between SSD and HDD devices per server. Therefore,
deploy one SSD for every three HDDs. In order to avoid having to reduce the number of HDDs
in the server, consider using M.2 form factor SSDs.

Providing 5% to 6% of SSD capacity relative to total HDD capacity is sufficient for on-premises
deployments. For example, if your server contains 100 TB of HDD capacity for mailbox
databases, an allocation of 5 TB to 6 TB for SSD capacity is enough.

<!-- p.2631 -->

The SSDs you use should qualify for "mixed use" and support one drive write per day (DWPD)
or greater in terms of write endurance.

Prerequisites
The following prerequisites are required for successful configuration and use of MCDB:

   1. The DAG is configured for AutoReseed.

     For more information, see the following topics:

           AutoReseed

           Configure AutoReseed for a database availability group

   2. RAW SSD drives are installed with the same SSD count and size for each server in the
     DAG. Make sure that all SSDs are completely empty, unformatted, and not write-
     protected. To verify this, you can use DiskPart or Clear-Disk.

   3. Exchange Server 2019.

MCDB setup
The process of setting up MCDB can be broken down into four basic steps:

   1. Set the correct values for the DAG you want to enable for MCDB.

   2. Update Active Directory (AD) settings and wait for propagation (by running
     ConfigureMCDBPrerequisite ).

   3. Allow MCDB acceleration for each server of the DAG (by running ServerAllowMCDB ).

   4. Create the necessary infrastructure (Volumes, Mount Points) for MCDB on each server (by
     running ConfigureMCDBOnServer ).

   5. Let databases fail over to pick up the new settings.

After successful execution of all four steps, MCDB acceleration will begin for every database
instance with a corresponding MCDB instance.

The following sections describe how to utilize the Manage-MetaCacheDatabase.ps1 script to
achieve the above four steps.

<!-- p.2632 -->

Step 1: Configure proper values on the DAG you want to
enable MCDB for
These DAG parameters are used to calculate the proper MCDB size on your SSD drives:

     AutoDagTotalNumberOfDatabases: The number of databases in your DAG (for example,
     50).

     AutoDagDatabaseCopiesPerDatabase: The number of active and passive copies each
     individual database has.

     AutoDagTotalNumberOfServers: The number of servers within your DAG, so between 2
     and 16.

For example:

  PowerShell

  Set-DatabaseAvailabilityGroup testdag1 -AutoDagTotalNumberOfDatabases 20 -
  AutoDagDatabaseCopiesPerDatabase 4 -AutoDagTotalNumberOfServers 8

Step 2: Run Manage-MCDB -ConfigureMCDBPrerequisite
This parameter sets the Active Directory state for the DAG object. Full replication of the Active
Directory state is required before MCDB can function properly on all servers.

ParameterSetIdentifier:

     ConfigureMCDBPrerequisite

Parameters:

                                                                                     ﾉ   Expand table

 Parameter           Required    Description

 DagName             True        Name of the Database availability group.

 SSDSizeInBytes      True        The capacity in bytes of each SSD in the server to be used for MCDB.

 SSDCountPerServer   True        The count of SSD devices to be utilized for MCDB in each server.

Scope:

     DAG: ConfigureMCDBPrerequisite operates on a DAG object.

<!-- p.2633 -->

  ７ Note

  MCDB will utilize up to 95% of an SSD's physical capacity. The remaining 5% is kept free to
  account for file system and partition overhead, as well as for a small amount of additional
  buffer and over-provisioning.

Example:

  PowerShell

  Manage-MCDB -DagName TestDag1 -ConfigureMCDBPrerequisite -SSDSizeInBytes
  5242880000 -SSDCountPerServer 2

Step 3: Run Manage-MCDB -ServerAllowMCDB
This command sets the local state on each DAG member to allow/disallow MCDB population
and read acceleration.

ParameterSetIdentifier:

     ServerAllowMCDB

Parameters:

                                                                                          ﾉ   Expand table

 Parameter       Required   Description

 DagName         True       Name of the Database availability group.

 ServerName      True       Specifies the server to enable MetaCacheDatabase on.

 ForceFailover   Optional   This Boolean switch can be utilized to cause all databases on a server to fail
                            over. This is required to make all configuration changes take effect and to
                            begin utilizing MCDB after mount points and database instances have been

<!-- p.2634 -->

 Parameter     Required   Description

                          successfully created in Step 4: Run Manage-MCDB -ConfigureMCDBOnServer.
                          It's also needed to disable SSD acceleration.

Scope:

     Server: You need to run ServerAllowMCDB on each server in the DAG.

Examples:

  PowerShell

  Manage-MCDB -DagName TestDag1 -ServerAllowMCDB:$true -ServerName "exhs-5046"

  PowerShell

  Manage-MCDB -DagName TestDag1 -ServerAllowMCDB:$false -ServerName "exhs-5046" -
  ForceFailover $true

Step 4: Run Manage-MCDB -ConfigureMCDBOnServer
This command identifies unformatted SSD devices and formats them, and also creates the
necessary mount points on a server for hosting MCDB instances. This parameter set can also be
used to re-create mount points on a raw SSD that was added to replace a failed SSD.

ParameterSetIdentifier:

     ConfigureMCDBOnServer

Parameters:

                                                                                 ﾉ   Expand table

<!-- p.2635 -->

 Parameter        Required   Description

 DagName          True       Name of the Database availability group.

 ServerName       True       Specifies the server to identify unformatted SSD devices and create mount
                             points on.

 SSDSizeInBytes   True       This is the capacity, in bytes, of each SSD in the server to be used for MCDB.

Scope:

     Server: You need to run ConfigureMCDBOnServer on each server in the DAG.

Example:

  PowerShell

  Manage-MCDB -DagName TestDag1 -ConfigureMCDBOnServer -ServerName "exhs-4056" -
  SSDSizeInBytes 5242880000

<!-- p.2636 -->

After performing the previous three steps (configuring ConfigureMCDBPrerequisite,
ServerAllowMCDB, and ConfigureMCDBOnServer), the MCDB state will display as Storage
Offline. This means that the environment is prepared and ready for MCDB instances to be
created and populated. The next failover of the database instance causes the creation of the
MCDB instance and enable acceleration. The instances transition through the health states
shown in MCDB health states.

You can use the ServerAllowMCDB parameter set to cause fail overs of all DB instances present
on a given server. Alternatively, you can use the Move-ActiveMailboxDatabase cmdlet to
cause individual databases to fail over.

  PowerShell

  Manage-MCDB -DagName TestDag1 -ServerAllowMCDB:$true -ServerName "exhs-5046" -
  ForceFailover $true

MCDB health states
Use Get-MailboxDatabaseCopyStatus to query the state of the MCDB instances. There are five
states that an MCDB instance can be in, as shown in the following table:

<!-- p.2637 -->

                                                                                            ﾉ   Expand table

State            Description

Disabled         MCDB is turned off.

StorageOffline   Basic infrastructure is missing or inaccessible, such as mount points or file paths. This is
                 the state MCDB is in following an SSD failure.

Offline          Errors at the logical level, for example missing MCDB instances.

Initializing     Transient state, the system is determining what other state it should be in.

Healthy          Ready to serve requests.

<!-- p.2638 -->

Plan for high availability and site resilience
Article • 04/30/2025

APPLIES TO:        2016     2019     Subscription Edition

During the planning phase, the system architects, administrators, and other key stakeholders
should identify the business requirements and the architectural requirements for the
deployment; in particular, the requirements about high availability and site resilience.

There are general requirements that must be met for deploying these features, as well as
hardware, software, and networking requirements that must also be met.

General requirements
Before deploying a database availability group (DAG) and creating mailbox database copies,
make sure that the following system-wide recommendations are met:

      Domain Name System (DNS) must be running. Ideally, the DNS server should accept
      dynamic updates. If the DNS server doesn't accept dynamic updates, you must create a
      DNS host (A) record for each Exchange server. Otherwise, Exchange won't function
      properly.

      Each Mailbox server in a DAG must be a member server in the same domain.

      Adding an Exchange Mailbox server that's also a directory server to a DAG isn't
      supported.

      The name you assign to the DAG must be a valid, available, and unique computer name
      of 15 characters or less.

Hardware requirements
Generally, there are no special hardware requirements specific to DAGs or mailbox database
copies. The servers used must meet all of the requirements set forth in Exchange Server
prerequisites.

Storage requirements
Generally, there are no special storage requirements specific to DAGs or mailbox database
copies. DAGs don't require or use cluster-managed shared storage. Cluster-managed shared
storage is supported for use in a DAG only when the DAG is configured to use a solution that
leverages the Third Party Replication API built into Exchange Server.

<!-- p.2639 -->

Software requirements
Each member of a DAG must be running the same operating system. Exchange Server 2016 is
supported on the Windows Server 2012, Windows Server 2012 R2, and Windows Server 2016.
Exchange Server 2019 is supported on the Windows Server 2019 and Windows Server 2022
operating system. Within a specific DAG, all members must be running the same supported
operating system.

  ７ Note

  Support for Windows Server 2022 servers was introduced with Exchange Server 2019
  CU12 (2022H1).

In addition to meeting the prerequisites for installing Exchange Server, there are operating
system requirements that must be met. DAGs use Windows Failover Clustering technology, and
as a result, they require the Standard or Datacenter version of the Windows Server 2012,
Windows Server 2012 R2, Windows Server 2016, Windows Server 2019 or Windows Server 2022
operating systems.

Network requirements
There are specific networking requirements that must be met for each DAG and for each DAG
member. Each DAG must have a single MAPI network, which is used by a DAG member to
communicate with other servers (for example, other Exchange servers or directory servers), and
zero or more Replication networks, which are networks dedicated to log shipping and seeding.

In previous versions of Exchange, we recommended at least two networks (one MAPI network
and one Replication network) for DAGs. In Exchange 2016 and Exchange 2019, multiple
networks are supported, but our recommendation depends on your physical network topology.
If you have multiple physical networks between DAG members that are physically separate
from one another, then using a separate MAPI and Replication network provides additional
redundancy. If you have multiple networks that are partially physically separate but converge
into a single physical network (for example, a single WAN link), then using a single network
(preferably 10 gigabit Ethernet) for both MAPI and Replication traffic is recommended. This
provides simplicity for the network and the network path.

Consider the following when designing the network infrastructure for your DAG:

     Each member of the DAG must have at least one network adapter that's able to
     communicate with all other DAG members. If you're using a single network path, we
     recommend that you use a minimum of 1 gigabit Ethernet, but preferably 10 gigabit

<!-- p.2640 -->

Ethernet. In addition, when using a single network adapter in each DAG member, we
recommend that you design the overall solution with the single network adapter and
path in mind.

Using two network adapters in each DAG member provides you with one MAPI network
and one Replication network, with redundancy for the Replication network and the
following recovery behaviors:

  In the event of a failure affecting the MAPI network, a server failover will occur
  (assuming there are healthy mailbox database copies that can be activated).

  In the event of a failure affecting the Replication network, if the MAPI network is
  unaffected by the failure, log shipping and seeding operations will revert to use the
  MAPI network, even if the MAPI network has it's ReplicationEnabled property set to
  False. When the failed Replication network is restored to health and ready to resume
  log shipping and seeding operations, you must manually switch over to the Replication
  network. To change replication from the MAPI network to a restored Replication
  network, you can either suspend and resume continuous replication by using the
  Suspend-MailboxDatabaseCopy and Resume-MailboxDatabaseCopy cmdlets, or
  restart the Microsoft Exchange Replication service. We recommend using suspend and
  resume operations to avoid the brief outage caused by restarting the Microsoft
  Exchange Replication service.

Each DAG member must have the same number of networks. For example, if you plan on
using a single network adapter in one DAG member, all members of the DAG must also
use a single network adapter.

Each DAG must have no more than one MAPI network. The MAPI network must provide
connectivity to other Exchange servers and other services, such as Active Directory and
DNS.

Additional Replication networks can be added, as needed. You can also prevent an
individual network adapter from being a single point of failure by using network adapter
teaming or similar technology. However, even when using teaming, this doesn't prevent
the network itself from being a single point of failure. Moreover, teaming adds
unnecessary complexity to the DAG.

Each network in each DAG member server must be on its own network subnet. Each
server in the DAG can be on a different subnet, but the MAPI and Replication networks
must be routable and provide connectivity, such that:

  Each network in each DAG member server is on its own network subnet that's separate
  from the subnet used by each other network in the server.
