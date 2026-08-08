---
title: "Exchange Server — pages 2641-2680"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2641-2680
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2641-2680
family: exchange
documentKind: "doc"
abstract: "Each DAG member server's MAPI network can communicate with each other DAG member's MAPI network. Each DAG member server's Replication network can communicate with each other DAG member's Replication network. There is no direct routing that allows heartbeat traffic from the Repli"
---

# Exchange Server — pages 2641-2680

<!-- p.2641 -->

        Each DAG member server's MAPI network can communicate with each other DAG
        member's MAPI network.

        Each DAG member server's Replication network can communicate with each other DAG
        member's Replication network.

        There is no direct routing that allows heartbeat traffic from the Replication network on
        one DAG member server to the MAPI network on another DAG member server, or vice
        versa, or between multiple Replication networks in the DAG.

     Regardless of their geographic location relative to other DAG members, each member of
     the DAG must have round trip network latency no greater than 500 milliseconds between
     each other member. As the round trip latency between two Mailbox servers hosting
     copies of a database increases, the potential for replication not being up to date also
     increases. Regardless of the latency of the solution, customers should validate that the
     networks between all DAG members is capable of satisfying the data protection and
     availability goals of the deployment. Configurations with higher latency values may
     require special tuning of DAG, replication, and network parameters, such as increasing the
     number of databases or decreasing the number of mailboxes per database, to achieve the
     desired goals.

     Round trip latency requirements may not be the most stringent network bandwidth and
     latency requirement for a multi-datacenter configuration. You must evaluate the total
     network load, which includes client access, Active Directory, transport, continuous
     replication, and other application traffic, to determine the necessary network
     requirements for your environment.

     DAG networks support Internet Protocol version 4 (IPv4) and IPv6. IPv6 is supported only
     when IPv4 is also used; a pure IPv6 environment isn't supported. Using IPv6 addresses
     and IP address ranges is supported only when both IPv6 and IPv4 are enabled on that
     computer, and the network supports both IP address versions. If Exchange Server is
     deployed in this configuration, all server roles can send data to and receive data from
     devices, servers, and clients that use IPv6 addresses.

     Automatic Private IP Addressing (APIPA) is a feature of Windows that automatically
     assigns IP addresses when no Dynamic Host Configuration Protocol (DHCP) server is
     available on the network. APIPA addresses (including manually assigned addresses from
     the APIPA address range) aren't supported for use by DAGs or by Exchange Server.

DAG name and IP address requirements
During creation, each DAG is given a unique name, and either assigned one or more static IP
addresses, or configured to use DHCP. Regardless of whether you use static or dynamically

<!-- p.2642 -->

assigned addresses, any IP address assigned to the DAG must be on the MAPI network.

Each DAG running on Windows Server 2012 requires a minimum of one IP address on the
MAPI network. A DAG requires additional IP addresses when the MAPI network is extended
across multiple subnets. DAGs running on Windows Server 2012 R2, Windows Server 2016,
Windows Server 2019 or Windows Server 2022 that are created without a cluster administrative
access point do not require an IP address.

The following figure illustrates a DAG where all nodes in the DAG have the MAPI network on
the same subnet.

DAG with MAPI network on same subnet

In this example, the MAPI network in each DAG member is on the 172.19.18. x subnet. As a
result, the DAG requires a single IP address on that subnet.

The next figure illustrates a DAG that has a MAPI network that extends across two subnets:
172.19.18. x and 172.19.19. x.

DAG with MAPI network on multiple subnets

In this example, the MAPI network in each DAG member is on a separate subnet. As a result,
the DAG requires two IP addresses, one for each subnet on the MAPI network.

Each time the DAG's MAPI network is extended across an additional subnet, an additional IP
address for that subnet must be configured for the DAG. Each IP address that's configured for
the DAG is assigned to and used by the DAG's underlying failover cluster. The name of the DAG
is also used as the name for the underlying failover cluster.

At any specific time, the cluster for the DAG will use only one of the assigned IP addresses.
Windows Failover Clustering registers this IP address in DNS when the cluster IP address and
Network Name resources are brought online. In addition to using an IP address and network
name, a cluster name object (CNO) is created in Active Directory. The name, IP address, and
CNO for the cluster are used internally by the system to secure the DAG and for internal

<!-- p.2643 -->

communication purposes. Administrators and end users don't need to interface with or
connect to the DAG name or IP address.

  ７ Note

  Although the cluster's IP address and network name are used internally by the system,
  there is no hard dependency in Exchange Server that these resources be available. Even if
  the underlying cluster's administrative access point (for example, its IP address and
  Network Name resources) is offline, internal communication still occurs within the DAG by
  using the DAG member server names. However, we recommend that you periodically
  monitor the availability of these resources to ensure that they aren't offline for more than
  30 days. If the underlying cluster is offline for more than 30 days, the cluster CNO account
  may be invalidated by the garbage collection mechanism in Active Directory.

Network adapter configuration for DAGs
Each network adapter must be configured properly based on its intended use. A network
adapter that's used for a MAPI network is configured differently from a network adapter that's
used for a Replication network. In addition to configuring each network adapter correctly, you
must also configure the network connection order in Windows so that the MAPI network is at
the top of the connection order. For detailed steps about how to modify the network
connection order, see Modify the protocol bindings and network provider order.

MAPI network adapter configuration
A network adapter intended for use by a MAPI network should be configured as described in
the following table.

                                                                                 ﾉ   Expand table

 Networking features                                                  Settings

 Client for Microsoft Networks                                        Enabled

 QoS Packet Scheduler                                                 Optionally enabled

 File and Printer Sharing for Microsoft Networks                      Enabled

 Internet Protocol version 6 (TCP/IP v6)                              Enabled

 Internet Protocol version 4 (TCP/IP v4)                              Enabled

 Link-Layer Topology Discovery Mapper I/O Driver                      Enabled

<!-- p.2644 -->

 Networking features                                                Settings

 Link-Layer Topology Discovery Responder                            Enabled

The TCP/IP v4 properties for a MAPI network adapter are configured as follows:

     The IP address for a DAG member's MAPI network can be manually assigned or
     configured to use DHCP. If DHCP is used, we recommend using persistent reservations for
     the server's IP address.

     The MAPI network typically uses a default gateway, although one isn't required.

     At least one DNS server address must be configured. Using multiple DNS servers is
     recommended for redundancy.

     The Register this connection's addresses in DNS check box should be selected.

Replication network adapter configuration
A network adapter intended for use by a Replication network should be configured as
described in the following table.

                                                                               ﾉ   Expand table

 Networking features                                                Settings

 Client for Microsoft Networks                                      Disabled

 QoS Packet Scheduler                                               Optionally enabled

 File and Printer Sharing for Microsoft Networks                    Disabled

 Internet Protocol version 6 (TCP/IP v6)                            Enabled

 Internet Protocol version 4 (TCP/IP v4)                            Enabled

 Link-Layer Topology Discovery Mapper I/O Driver                    Enabled

 Link-Layer Topology Discovery Responder                            Enabled

The TCP/IP v4 properties for a Replication network adapter are configured as follows:

     The IP address for a DAG member's Replication network can be manually assigned or
     configured to use DHCP. If DHCP is used, we recommend using persistent reservations for
     the server's IP address.

<!-- p.2645 -->

     Replication networks typically don't have default gateways, and if the MAPI network has a
     default gateway, no other networks should have default gateways. Routing of network
     traffic on a Replication network can be configured by using persistent, static routes to the
     corresponding network on other DAG members using gateway addresses that have the
     ability to route between the Replication networks. All other traffic not matching this route
     will be handled by the default gateway that's configured on the adapter for the MAPI
     network.

     DNS server addresses shouldn't be configured.

     The Register this connection's addresses in DNS check box shouldn't be selected.

Witness server requirements
A witness server is a server outside a DAG that's used to achieve and maintain quorum when
the DAG has an even number of members. DAGs with an odd number of members don't use a
witness server. All DAGs with an even number of members must use a witness server. The
witness server can be any computer running Windows Server. There is no requirement that the
version of the Windows Server operating system of the witness server matches the operating
system used by the DAG members.

Quorum is maintained at the cluster level, underneath the DAG. A DAG has quorum when the
majority of its members are online and can communicate with the other online members of the
DAG. This notion of quorum is one aspect of the concept of quorum in Windows failover
clustering. A related and necessary aspect to quorum in failover clusters is the quorum resource.
The quorum resource is a resource inside a failover cluster that provides a means for arbitration
leading to cluster state and membership decisions. The quorum resource also provides
persistent storage for storing configuration information. A companion to the quorum resource
is the quorum log, which is a configuration database for the cluster. The quorum log contains
information such as which servers are members of the cluster, what resources are installed in
the cluster, and the state of those resources (for example, online or offline).

It's critical that each DAG member have a consistent view of how the DAG's underlying cluster
is configured. The quorum acts as the definitive repository for all configuration information
relating to the cluster. The quorum is also used as a tie-breaker to avoid split-brain syndrome.
Split brain syndrome is a condition that occurs when DAG members can't communicate with
each other but are running. Split brain syndrome is prevented by always requiring a majority of
the DAG members (and in the case of DAGs with an even number of member, the DAG witness
server) to be available and interacting for the DAG to be operational.

Planning for site resilience

<!-- p.2646 -->

Every day, more businesses recognize that access to a reliable and available messaging system
is fundamental to their success. For many organizations, the messaging system is part of the
business continuity plans, and their messaging service deployment is designed with site
resilience in mind. Fundamentally, many site resilient solutions involve the deployment of
hardware in a second datacenter.

Ultimately, the overall design of a DAG, including the number of DAG members and the
number of mailbox database copies, will depend on each organization's recovery service level
agreements (SLAs) that cover various failure scenarios. During the planning stage, the
solution's architects and administrators identify the requirements for the deployment, including
in particular the requirements for site resilience. They identify the locations to be used and the
required recovery SLA targets. The SLA will identify two specific elements that should be the
basis for the design of a solution that provides high availability and site resilience: the recovery
time objective and the recovery point objective. Both of these values are measured in minutes.
The recovery time objective is how long it takes to restore service. The recovery point objective
refers to how current the data is after the recovery operation has completed. An SLA may also
be defined for restoring the primary datacenter to full service after its problems are corrected.

The solution's architects and administrators will also identify which set of users require site
resilience protection, and determine if the multiple site solution will be an active/passive or
active/active configuration. In an active/passive configuration, no users are normally hosted in
the standby datacenter. In an active/active configuration, users are hosted in both locations,
and some percentage of the total number of databases within the solution has a preferred
active location in a second datacenter. When service for the users of one datacenter fails, those
users are activated in the other datacenter.

Constructing the appropriate SLAs often requires answering the following basic questions:

     What level of service is required after the primary datacenter fails?

     Do users need their data or just messaging services?

     How rapidly is data required?

     How many users must be supported?

     How will users access their data?

     What is the standby datacenter activation SLA?

     How is service moved back to the primary datacenter?

     Are the resources dedicated to the site resilience solution?

<!-- p.2647 -->

By answering these questions, you begin to shape a site resilient design for your messaging
solution. A core requirement of recovery from site failure is to create a solution that gets the
necessary data to the backup datacenter that hosts the backup messaging service.

Certificate planning
There are no unique or special design considerations for certificates when deploying a DAG in
a single datacenter. However, when extending a DAG across multiple datacenters in a site
resilient configuration, there are some specific considerations with respect to certificates.
Generally, your certificate design will depend on the clients in use, as well as the certificate
requirements by other applications that use certificates. But there are some specific
recommendations and best practices you should follow with respect to the type and number of
certificates.

As a best practice, you should minimize the number of certificates you use for your Exchange
servers and reverse proxy servers. We recommend using a single certificate for all of these
service endpoints in each datacenter. This approach minimizes the number of certificates that
are needed, which reduces both cost and complexity for the solution.

For Outlook Anywhere clients, we recommend that you use a single subject alternative name
(SAN) certificate for each datacenter, and include multiple host names in the certificate. To
ensure Outlook Anywhere connectivity after a database, server, or datacenter switchover, you
must use the same Certificate Principal Name on each certificate, and configure the Outlook
Provider Configuration object in Active Directory with the same Principal Name in Microsoft-
Standard Form (msstd). For example, if you use a Certificate Principal Name of
mail.contoso.com, you would configure the attribute as follows.

  PowerShell

  Set-OutlookProvider EXPR -CertPrincipalName "msstd:mail.contoso.com"

Some applications that integrate with Exchange have specific certificate requirements that may
require using additional certificates. Exchange Server can co-exist with Office Communications
Server (OCS). OCS requires certificates with 1024-bit or greater certificates that use the OCS
server name for the Certificate Principal Name. Because using an OCS server name for the
Certificate Principal Name would prevent Outlook Anywhere from working properly, you would
need to use an additional and separate certificate for the OCS environment.

Network planning
In addition to the specific networking requirements that must be met for each DAG, as well as
for each server that's a member of a DAG, there are some requirements and recommendations

<!-- p.2648 -->

that are specific to site resilience configurations. As with all DAGs, whether the DAG members
are deployed in a single site or in multiple sites, the round-trip return network latency between
DAG members must be no greater than 500 milliseconds. In addition, there are specific
configuration settings that are recommended for DAGs that are extended across multiple sites:

     MAPI networks should be isolated from Replication networks: Windows network
     policies, Windows firewall policies, or router access control lists (ACLs) should be used to
     block traffic between the MAPI network and the Replication networks. This configuration
     is necessary to prevent network heartbeat cross talk.

     Client-facing DNS records should have a Time to Live (TTL) value of 5 minutes: The
     amount of downtime that clients experience is dependent not just on how quickly a
     switchover can occur, but also on how quickly DNS replication occurs and the clients
     query for updated DNS information. DNS records for all Exchange client services,
     including Outlook on the web (formerly known as Outlook Web App), Exchange
     ActiveSync, Exchange Web Services, Outlook Anywhere, SMTP, POP3, and IMAP4 in both
     the internal and external DNS servers should be set with a TTL of 5 minutes.

     Use static routes to configure connectivity across Replication networks: To provide
     network connectivity between each of the Replication network adapters, use persistent
     static routes. This is a quick and one-time configuration that's performed on each DAG
     member when using static IP addresses. If you're using DHCP to obtain IP addresses for
     your Replication networks, you can also use it to assign static routes for the replication,
     thereby simplifying the configuration process.

General site resilience planning
In addition to the requirements listed above for high availability, there are other
recommendations for deploying Exchange Server in a site resilient configuration (for example,
extending a DAG across multiple datacenters). What you do during the planning phase will
directly affect the success of your site resilience solution. For example, poor namespace design
can cause difficulties with certificates, and an incorrect certificate configuration can prevent
users from accessing services.

To minimize the time it takes to activate a second datacenter, and allow the second datacenter
to host the service endpoints of a failed datacenter, the appropriate planning must be
completed. The following are examples:

     The SLA goals for the site resilience solution must be well understood and documented.

     The servers in the second datacenter must have sufficient capacity to host the combined
     user population of both datacenters.

<!-- p.2649 -->

The second datacenter must have all services enabled that are provided in the primary
datacenter (unless the service isn't included as part of the site resilience SLA). This
includes Active Directory, networking infrastructure (for example, DNS or TCP/IP),
telephony services (if Unified Messaging in Exchange 2016 is in use), and site
infrastructure (such as power or cooling).

For some services to be able to service users from the failed datacenter, they must have
the proper server certificates configured. Some services don't allow instancing (for
example, POP3 and IMAP4) and only allow the use of a single certificate. In these cases,
either the certificate must be a SAN certificate that includes multiple names, or the
multiple names must be similar enough so that a wildcard certificate can be used
(assuming the security policies of the organization allows the use of wildcard certificates).

The necessary services must be defined in the second datacenter. For example, if the first
datacenter has three different SMTP URLs on different transport servers, the appropriate
configuration must be defined in the second datacenter to enable at least one (if not all
three) transport server to host the workload.

The necessary network configuration must be in place to support the datacenter
switchover. This might mean making sure that the load balancing configurations are in
place, that global DNS is configured, and that the Internet connection is enabled with the
appropriate routing configured.

The strategy for enabling the DNS changes necessary for a datacenter switchover must be
understood. The specific DNS changes, including their TTL settings, must be defined and
documented to support the SLA in effect.

A strategy for testing the solution must also be established and factored into the SLA.
Periodic validation of the deployment is the only way to guarantee that the quality and
viability of the deployment doesn't degrade over time. After the deployment is validated,
we recommend that the part of the configuration that directly affects the success of the
solution be explicitly documented. In addition, we recommend that you enhance your
change management processes around those segments of the deployment.

<!-- p.2650 -->

Deploying high availability and site
resilience in Exchange Server
08/05/2025

APPLIES TO:       2016        2019    Subscription Edition

Microsoft Exchange Server uses the concept known as incremental deployment for both high
availability and site resilience. You install two or more Exchange Mailbox servers as stand-alone
servers, and then incrementally configure them and mailbox databases for high availability and
site resilience, as needed.

Overview of the deployment process
While the actual steps used by each organization might vary slightly, the overall process for
deploying Exchange Server in a highly available or site resilient configuration is generally the
same. After performing the necessary planning and design tasks for building and deploying a
database availability group (DAG) and creating mailbox database copies, you would:

   1. Create a DAG. For detailed steps, see Create a database availability group. It's important
     to note that all servers within a DAG must be running the same version of Exchange. For
     example, you can't mix Exchange 2013 and Exchange 2016 servers in the same DAG.

   2. If necessary, pre-stage the cluster name object (CNO). Pre-staging the CNO is required
     when deploying a DAG with Mailbox servers running Windows Server 2012. If you're
     deploying a DAG without an administrative access point using Mailbox servers running
     Windows Server 2012 R2, then you don't need to pre-stage a CNO. Pre-staging is also
     required in environments where computer account creation is restricted or where
     computer accounts are created in a container other than the default computers container.
     For detailed steps, see Pre-stage the cluster name object for a database availability group.

   3. Add two or more Mailbox servers to the DAG. For detailed steps, see Manage database
     availability group membership.

   4. Configure the DAG properties as needed:

      a. Optionally configure DAG encryption and compression, replication port, DAG IP
        addresses, and other DAG properties. For detailed steps, see Configure database
        availability group properties.

      b. Enable Datacenter Activation Coordination (DAC) mode for the DAG. This action has
        the following benefits:

<!-- p.2651 -->

             Protects the DAG from database-level split brain conditions during switchback to
             the primary datacenter after a datacenter switchover.
             Enables the use of the built-in DAG recovery cmdlets.

        For more information, see Datacenter Activation Coordination mode.

   5. Add mailbox database copies across Mailbox servers in the DAG. For detailed steps, see
     Add a mailbox database copy.

Example deployment: four-member DAG in two
datacenters
This example details how Contoso, Ltd. is configuring and deploying a four-member DAG
extended across two physical locations: Boston and Oklahoma City.

Base infrastructure
Each location contains the infrastructure elements that are necessary to operate a messaging
infrastructure based on Exchange Server, namely:

     Directory services (either Active Directory or Active Directory Domain Services (AD DS))

     Domain Name System (DNS) name resolution

     Multiple Exchange servers running Client Access services

     Multiple Exchange Mailbox servers

The following figure illustrates the Contoso configuration.

<!-- p.2652 -->

Network configuration
As illustrated in the previous figure, the solution involves the use of multiple subnets and
multiple networks. Each Mailbox server in the DAG has two network adapters on separate
subnets. In each Mailbox server, one network adapter is used for the MAPI network (192.168. x.
x) and one network adapter is used for the Replication network (10.0. x. x). Only the MAPI
network provides connectivity to Active Directory, DNS services, other Exchange servers, and
clients. The adapter used for the Replication network in each member provides connectivity
only to the Replication network adapters in the other members of the DAG.

The settings for each network adapter in each node are detailed in the following table.

                                                                                 ﾉ     Expand table

 Name                         IPv4 address         Subnet mask           Default gateway

 MBX1 (MAPI)                  192.168.1.4          255.255.255.0         192.168.1.1

 MBX2 (MAPI)                  192.168.1.5          255.255.255.0         192.168.1.1

<!-- p.2653 -->

 Name                         IPv4 address       Subnet mask           Default gateway

 MBX3 (MAPI)                  192.168.2.4        255.255.255.0         192.168.2.1

 MBX4 (MAPI)                  192.168.2.5        255.255.255.0         192.168.2.1

 MBX1 (Replication)           10.0.1.4           255.255.255.0         None

 MBX2 (Replication)           10.0.1.5           255.255.255.0         None

 MBX3 (Replication)           10.0.2.4           255.255.255.0         None

 MBX4 (Replication)           10.0.2.5           255.255.255.0         None

As shown in the preceding table, adapters used for Replication networks don't use default
gateways. To provide network connectivity between each of the Replication network adapters,
Contoso uses persistent static routes, which they configure by using the Netsh.exe tool.

To configure routing for the Replication network adapters on MBX1 and MBX2, the following
command was run on each server.

  PowerShell

  netsh interface ipv4 add route 10.0.2.0/24 <NetworkName> 10.0.1.254

To configure routing for the Replication network adapters on MBX3 and MBX4, the following
command was run on each server.

  PowerShell

  netsh interface ipv4 add route 10.0.1.0/24 <NetworkName> 10.0.2.254

The following network settings are also configured:

     The Register this connection's addresses in DNS check box is selected for each DAG
     member's MAPI network adapter, and cleared for each Replication network adapter.

     At least one DNS server address is configured for each DAG member's MAPI network
     adapter, and none are configured for the Replication network adapters. For redundancy,
     Contoso is using multiple DNS server addresses for their MAPI network adapters.

     Contoso doesn't use the Windows Firewall, so they turned it off on their servers.

After the network adapters are configured, Contoso is ready to create a DAG and add the
Mailbox servers to the DAG.

<!-- p.2654 -->

Database availability group creation and configuration
The administrator decided to create a Windows PowerShell command-line interface script that
performs several tasks:

     It uses the New-DatabaseAvailabilityGroup cmdlet to create the DAG. Because BOSTON is
     considered to be the primary datacenter, Contoso chose to use a witness server in the
     same datacenter, namely, MBX5.

     It uses the Set-DatabaseAvailabilityGroup cmdlet to preconfigure an alternate witness
     server and alternate witness directory in case a datacenter switchover is ever necessary.

     It uses the Add-DatabaseAvailabilityGroupServer cmdlet to add each of the four Mailbox
     servers to the DAG.

     It uses the Set-DatabaseAvailabilityGroup cmdlet to configure the DAG for DAC mode. For
     more information about DAC mode, see Datacenter Activation Coordination mode.

The following are the commands used in the script:

  PowerShell

  New-DatabaseAvailabilityGroup -Name DAG1 -WitnessServer MBX5 -WitnessDirectory
  C:\DAGWitness\DAG1.contoso.com -DatabaseAvailabilityGroupIPAddresses
  192.168.1.8,192.168.2.8

The preceding command creates the DAG DAG1, configures MBX5 to act as the witness server,
configures a specific witness directory (C:\DAGWitness\DAG1.contoso.com), and configures two
IP addresses for the DAG (one for each subnet on the MAPI network).

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -AlternateWitnessDirectory
  C:\DAGWitness\DAG1.contoso.com -AlternateWitnessServer MBX10

The preceding command configures DAG1 with the following settings:

     Use MBX10 as an alternate witness server.
     Use an alternate witness directory on MBX10 with the same path as MBX5.

   Tip

  Using the same path isn't required. Contoso is using the same path to standardize their
  configuration.

<!-- p.2655 -->

  PowerShell

  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer MBX1

  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer MBX3

  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer MBX2

  Add-DatabaseAvailabilityGroupServer -Identity DAG1 -MailboxServer MBX4

The previous commands take the following actions:

     Add each of the Mailbox servers, one at a time, to the DAG.
     Install the Windows Failover Clustering component on each Mailbox server (if it isn't
     already installed).
     Create a failover cluster.
     Join each Mailbox server to the newly created cluster.

  PowerShell

  Set-DatabaseAvailabilityGroup -Identity DAG1 -DatacenterActivationMode DagOnly

The preceding command enables DAC mode for the DAG.

Mailbox databases and mailbox database copies
After creating the DAG and adding the Mailbox servers to the DAG, Contoso prepares to create
mailbox databases and mailbox database copies. To meet their criteria for failure resistance,
Contoso is planning to configure each mailbox database with three non-lagged database
copies, and one lagged database copy. The lagged copy has a configured log replay delay of
three days.

This configuration provides a total of four copies for each database (one active, two non-
lagged passives, and a lagged passive). Contoso plans on having four active databases per
server. Therefore the Contoso solution contains 16 total database copies.

As shown in the following figure, Contoso is taking a balanced approach to their database
layout.

Database copy layout for Contoso, Ltd

<!-- p.2656 -->

Each Mailbox server hosts an active mailbox database copy, two non-lagged passive database
copies, and one lagged passive database copy. The lagged copy of each active mailbox
database is hosted on a Mailbox server in the other site.

To create this configuration, the administrator runs several commands.

On MBX1, run the following commands.

  PowerShell

  Add-MailboxDatabaseCopy -Identity DB1 -MailboxServer MBX2

  Add-MailboxDatabaseCopy -Identity DB1 -MailboxServer MBX4

  Add-MailboxDatabaseCopy -Identity DB1 -MailboxServer MBX3 -ReplayLagTime
  3.00:00:00 -SeedingPostponed
  Suspend-MailboxDatabaseCopy -Identity DB1\MBX3 -SuspendComment "Seed from MBX4" -
  Confirm:$False

  Update-MailboxDatabaseCopy -Identity DB1\MBX3 -SourceServer MBX4

<!-- p.2657 -->

  Suspend-MailboxDatabaseCopy -Identity DB1\MBX3 -ActivationOnly

On MBX2, run the following commands.

  PowerShell

  Add-MailboxDatabaseCopy -Identity DB2 -MailboxServer MBX1
  Add-MailboxDatabaseCopy -Identity DB2 -MailboxServer MBX3

  Add-MailboxDatabaseCopy -Identity DB2 -MailboxServer MBX4 -ReplayLagTime
  3.00:00:00 -SeedingPostponed

  Suspend-MailboxDatabaseCopy -Identity DB2\MBX4 -SuspendComment "Seed from MBX3" -
  Confirm:$False

  Update-MailboxDatabaseCopy -Identity DB2\MBX4 -SourceServer MBX3

  Suspend-MailboxDatabaseCopy -Identity DB2\MBX4 -ActivationOnly

On MBX3, run the following commands.

  PowerShell

  Add-MailboxDatabaseCopy -Identity DB3 -MailboxServer MBX4

  Add-MailboxDatabaseCopy -Identity DB3 -MailboxServer MBX2

  Add-MailboxDatabaseCopy -Identity DB3 -MailboxServer MBX1 -ReplayLagTime
  3.00:00:00 -SeedingPostponed

  Suspend-MailboxDatabaseCopy -Identity DB3\MBX1 -SuspendComment "Seed from MBX2" -
  Confirm:$False

  Update-MailboxDatabaseCopy -Identity DB3\MBX1 -SourceServer MBX2

  Suspend-MailboxDatabaseCopy -Identity DB3\MBX1 -ActivationOnly

On MBX4, run the following commands.

  PowerShell

  Add-MailboxDatabaseCopy -Identity DB4 -MailboxServer MBX3

  Add-MailboxDatabaseCopy -Identity DB4 -MailboxServer MBX1

  Add-MailboxDatabaseCopy -Identity DB4 -MailboxServer MBX2 -ReplayLagTime
  3.00:00:00 -SeedingPostponed

  Suspend-MailboxDatabaseCopy -Identity DB4\MBX2 -SuspendComment "Seed from MBX1" -

<!-- p.2658 -->

  Confirm:$False

  Update-MailboxDatabaseCopy -Identity DB4\MBX2 -SourceServer MBX1

  Suspend-MailboxDatabaseCopy -Identity DB4\MBX2 -ActivationOnly

In the preceding Add-MailboxDatabaseCopy examples, we didn't use the ActivationPreference
parameter, because the task automatically increments the activation preference number with
each copy added:

     The original database always has a preference number of 1.
     The first copy added is automatically assigned a preference number of 2.
     Assuming no copies are removed, the next copy added is automatically assigned a
     preference number of 3, and so on.

So, in the preceding Add-MailboxDatabaseCopy examples:

     The passive copy in the same datacenter as the active copy has an activation preference
     number of 2.
     The non-lagged passive copy in the remote datacenter has an activation preference
     number of 3.
     The lagged passive copy in the remote datacenter has an activation preference number of
     4.

Although there are two copies of each active database across the WAN in the other location,
seeding over the WAN was only performed once. Contoso uses the Exchange Server ability to
use a passive copy of a database as the source for seeding.

     Using the Add-MailboxDatabaseCopy cmdlet with the SeedingPostponed parameter
     prevents the task from automatically seeding the new database copy being created.
     The administrator can suspend the un-seeded copy.
     Using the Update-MailboxDatabaseCopy cmdlet with the SourceServer parameter, the
     administrator can specify the local copy of the database as the source of the seeding
     operation.

As a result, seeding of the second database copy added to each location happens locally and
not over the WAN.

  ７ Note

  In the preceding example, the non-lagged database copy is seeded over the WAN. That
  copy is used to seed the lagged copy of the database in the same datacenter as the non-
  lagged copy.

<!-- p.2659 -->

Contoso configured one of the passive copies of each mailbox database as a lagged database
copy to provide protection against the extremely rare but catastrophic case of database logical
corruption. As a result, the administrator is configuring the lagged copies as blocked for
activation by using the Suspend-MailboxDatabaseCopy cmdlet with the ActivationOnly
parameter. This configuration ensures that the lagged database copies aren't activated if a
database or server failover occurs.

Validating the solution
After the solution is deployed and configured, the administrator performs several tasks that
validate the solution's readiness before moving production mailboxes to the databases in the
DAG. The solution should be tested and inspected using several methods, including failure
simulations. To validate the solution, the administrator performs several tasks.

To verify the overall health of the DAG, the administrator runs the Test-ReplicationHealth
cmdlet. This cmdlet checks several aspects of the replication and replay status to provide
information about each Mailbox server and database copy in the DAG.

To verify replication and replay activity, the administrator runs the Get-
MailboxDatabaseCopyStatus cmdlet. This cmdlet can provide real-time status information
about a specific mailbox database copy or for all mailbox database copies on a specific server.
For more information about monitoring the health and status of replicated databases in a DAG,
see Monitor database availability groups.

To verify that switchovers work as expected, the administrator uses the Move-
ActiveMailboxDatabase cmdlet to perform a series of database switchovers and server
switchovers. When these tasks complete successfully, the administrator uses the same cmdlet
to move the active database copies back to their original locations.

To verify the expected behaviors in various failure scenarios, the administrator performs several
tasks that either simulate failures or actually cause failures to occur. For example, the
administrator might:

     Unplug the power cord on MBX1, which triggers a server failover. The administrator then
     verifies that DB1 becomes active on another server (preferably MBX2, based on the
     activation preference values).

     Unplug the network cable for the MAPI network adapter on MBX2, which triggers a server
     failover. The administrator then verifies that DB2 becomes active on another server
     (preferably MBX1, based on the activation preference values).

     Take the disk used by the active copy of DB3 offline, which triggers a database failover.
     The administrator then verifies that DB3 becomes active on another server (preferably

<!-- p.2660 -->

      MBX4, based on activation preference values).

An organization might test other failure scenarios, based on the business needs. After
simulating a single failure (such as pulling the power plug), and verifying the solution's
recovery behavior, the administrator might revert the solution back to its original configuration.
In some cases, the solution might be tested for multiple concurrent failures. Ultimately, your
solution test plan dictates whether the solution is reverted back to its original configuration
after each failure simulation.

In addition, an administrator might decide to disconnect the network connection between the
two datacenters, which simulates a site failure. Performing a datacenter switchover is a much
more involved and coordinated process; however, we recommend the process if the solution
being deployed is intended to provide site resilience for the messaging services and data.

Transitioning to operations
After the solution is deployed, it can be extended further using incremental deployment. At this
point, management of the solution would also transition to operation processes, in which the
following tasks would be performed:

      Monitor the health and status of DAGs and mailbox database copies. For more
      information, see Monitor database availability groups.

      Perform database switchovers as needed. For detailed steps about how to perform a
      database switchover, see Activate a mailbox database copy.

For more information about managing the solution, see Managing high availability and site
resilience.

<!-- p.2661 -->

Managing high availability and site
resilience in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

After you build, validate, and deploy a Microsoft Exchange Server high availability or site
resilience solution, the solution transitions from the deployment phase to the operational
phase of the overall solution lifecycle. The operational phase consists of several tasks, and all
tasks are related to one of the following areas: database availability groups (DAGs), mailbox
database copies, performing proactive monitoring, and managing switchovers and failovers.

Database availability group management
The operational management tasks associated with DAGs include:

      Creating one or more DAGs: Creating a DAG is typically a one-time procedure performed
      during the deployment phase of the solution lifecycle. However, there may be reasons for
      creating DAGs that occur during the operational phase, for example:

         The DAG is configured for third-party replication mode, and you want to revert to
         using continuous replication. You can't convert a DAG back to continuous replication;
         you need to create a DAG.

         You have servers in multiple domains. All members of the same DAG must also be
         members of the same domain.

      Managing DAG membership: Managing DAG members is an infrequent task typically
      performed during the deployment phase of the solution lifecycle. However, because of
      the flexibility provided by incremental deployment, managing DAG membership may also
      be performed throughout the solution lifecycle.

      Configuring DAG properties: Each DAG has various properties that can be configured as
      needed. These properties include:

         Witness server and witness directory: The witness server is a server outside the DAG
         that acts as a quorum voter when the DAG contains an even number of members. The
         witness directory is a directory created and shared on the witness server for use by the
         system in maintaining a quorum.

         IP addresses: Each DAG will have one or more IPv4 addresses, and optionally, one or
         more IPv6 addresses. The IP addresses assigned to the DAG are used by the DAG's

<!-- p.2662 -->

   underlying cluster. The number of IPv4 addresses assigned to the DAG equals the
   number of subnets that comprise the MAPI network used by the DAG. You can
   configure the DAG to use static IP addresses or to obtain addresses automatically by
   using Dynamic Host Configuration Protocol (DHCP).

   Datacenter Activation Coordination mode: Datacenter Activation Coordination mode
   is a property setting on a DAG that's designed to prevent split-brain conditions at the
   database level, in a scenario in which you're restoring service to a primary datacenter
   after a datacenter switchover has been performed. For more information about
   Datacenter Activation Coordination mode, see Datacenter Activation Coordination
   mode.

   Alternate witness server and alternate witness directory: The alternate witness server
   and alternate witness directory are values that you can preconfigure as part of the
   planning process for a datacenter switchover. These refer to the witness server and
   witness directory that will be used when a datacenter switchover has been performed.

   Replication port: By default, all DAGs use TCP port 64327 for continuous replication.
   You can modify the DAG to use a different TCP port for replication by using the
   ReplicationPort parameter of the Set-DatabaseAvailabilityGroup cmdlet.

   Network discovery: You can force the DAG to rediscover networks and network
   interfaces. This operation is used when you add or remove networks or introduce new
   subnets. Rediscovery of all DAG networks can be forced by using the DiscoverNetworks
   parameter of the Set-DatabaseAvailabilityGroup cmdlet.

   Network compression: By default, DAGs use compression only between DAG networks
   on different subnets. You can enable compression for all DAG networks or for seeding
   operations only, or you can disable compression for all DAG networks.

   Network encryption: By default, DAGs use encryption only between DAG networks on
   different subnets. You can enable encryption for all DAG networks or for seeding
   operations only, or you can disable encryption for all DAG networks.

Shutting down DAG members: The Exchange Server high availability solution is
integrated with the Windows shutdown process. If an administrator or application
initiates a shutdown of a Windows server in a DAG that has a mounted database that's
replicated to one or more DAG members, the system will try to activate another copy of
the mounted databases prior to allowing the shutdown process to complete. However,
this new behavior doesn't guarantee that all of the databases on the server being shut
down will experience a lossless activation. As a result, it's a best practice to perform a
server switchover prior to shutting down a server that's a member of a DAG.

<!-- p.2663 -->

For detailed steps about how to create a DAG, see Create a database availability group. For
detailed steps about how to configure DAGs and DAG properties, see Configure database
availability group properties. For more information about each of the preceding management
tasks, and about managing DAGs in general, see Manage database availability groups.

Mailbox database copy management
The operational management tasks associated with mailbox database copies include:

     Adding mailbox database copies: When you add a copy of a mailbox database,
     continuous replication is automatically enabled between the existing database and the
     database copy.

     Configuring mailbox database copy properties: You can configure a variety of properties,
     such as the database activation policy, the amount of time, if any, for replay lag and
     truncation lag, and the activation preference for the database copy.

     Suspending or resuming a mailbox database copy: You can suspend a mailbox database
     copy in preparation for seeding, or for other forms of maintenance. You can also suspend
     a mailbox database copy for activation only. This configuration prevents the system from
     automatically activating the copy as a result of a failure, but it still allows the system to
     keep the database copy up to date with log shipping and replay.

     Updating a mailbox database copy: Updating, also known as seeding, is the process in
     which a copy of a mailbox database is added to another Mailbox server. This becomes the
     baseline database for the copy. After the initial first seed of the baseline database copy,
     only in rare circumstances will the database need to be seeded again.

     Activating a mailbox database copy: Activating is the process of designating a specific
     passive copy as the new active copy of a mailbox database. This process is referred to as a
     switchover. For more information, see "Switchovers and Failovers" later in this topic.

     Removing a mailbox database copy: Occasionally, it may be necessary to remove a
     mailbox database copy. For example, you can't remove a Mailbox server from a DAG until
     all mailbox database copies are removed from the server. In addition, you must remove
     all copies of a mailbox database before you can change the path for a mailbox database.

For detailed steps about how to add a mailbox database copy, see Add a mailbox database
copy. For detailed steps about how to configure mailbox database copies, see Configure
mailbox database copy properties. For more information about each of the preceding
management tasks, and about managing mailbox database copies in general, see Manage
mailbox database copies. For detailed steps about how to remove a mailbox database copy,
see Remove a mailbox database copy.

<!-- p.2664 -->

Proactive monitoring
Making sure that your servers are operating reliably and that your database copies are healthy
are key objectives for daily messaging operations. Exchange Server includes a number of
features that can be used to perform a variety of health monitoring tasks for DAGs and mailbox
database copies, including:

     Get-MailboxDatabaseCopyStatus

     Test-ReplicationHealth

     Crimson channel event logging

In addition to monitoring the health and status, it's also critical to monitor for situations that
can compromise availability. For example, we recommend that you monitor the redundancy of
your replicated databases. It's critical to avoid situations where you're down to a single copy of
a database. This scenario should be treated with the highest priority and resolved as soon as
possible.

For more detailed information about monitoring the health and status of DAGs and mailbox
database copies, see Monitor database availability groups.

Switchovers and failovers
A switchover is a manual process in which an administrator manually activates one or more
mailbox database copies. Switchovers, which can occur at the database or server level, are
typically performed as part of preparation for maintenance activities. Switchover management
involves performing database or server switchovers as needed. For example, if you need to
perform maintenance on a Mailbox server in a DAG, you would first perform a server
switchover so that the server didn't host any active mailbox database copies. For detailed steps
about how to perform a database switchover, see Activate a mailbox database copy.
Switchovers can also be performed at the datacenter level.

A failover is the automatic activation by the system of one or more database copies in reaction
to a failure. For example, the loss of a disk drive in a RAID-less environment will trigger a
database failover. The loss of the MAPI network or a power failure will trigger a server failover.

<!-- p.2665 -->

Manage database availability groups in
Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019      Subscription Edition

A database availability group (DAG) is a set of upto 16 Exchange Mailbox servers that provide
automatic, database-level recovery from a database/server/network failure. DAGs use
continuous replication and a subset of Windows failover clustering technologies to provide
high availability and site resilience. Mailbox servers in a DAG monitor each other for failures.
When a Mailbox server is added to a DAG, that server works with the other servers in the DAG
to provide automatic, database-level recovery from database failures.

When you create a DAG, it's initially empty. When you add the first server to a DAG, a failover
cluster is automatically created for the DAG. In addition, the infrastructure that monitors the
servers for network or server failures is initiated. The failover cluster heartbeat mechanism and
cluster database are then used to track and manage information about the DAG which can
change quickly, such as database mount status, replication status, and last-mounted location.

Creating DAGs
A DAG can be created using the New Database Availability Group wizard in the Exchange
admin center (EAC), or by running the New-DatabaseAvailabilityGroup cmdlet in the Exchange
Management Shell. When you create a DAG, you provide a name for the DAG, and optional
witness server and witness directory settings. In addition, you can assign one or more IP
addresses to the DAG, either by using static IP addresses or by allowing the DAG to be
automatically assigned the necessary IP addresses using Dynamic Host Configuration Protocol
(DHCP). You can manually assign IP addresses to the DAG by using the
DatabaseAvailabilityGroupIpAddresses parameter. If you omit this parameter, the DAG attempts
to obtain an IP address by using a DHCP server on your network.

If you're creating a DAG that will contain Mailbox servers that are running Windows Server
2012 R2, you also have the option of creating a DAG without a cluster administrative access
point. In that case, the cluster won't have a cluster name object (CNO) in Active Directory, and
the cluster core resource group won't contain a network name resource or an IP address
resource.

For detailed steps about how to create a DAG, see Create a database availability group.

When you create a DAG, an empty object representing the DAG with the name you specified
and an object class of msExchMDBAvailabilityGroup are created in Active Directory.

<!-- p.2666 -->

DAGs use a subset of Windows failover clustering technologies in Windows Server 2008 R2 or
later, such as the cluster heartbeat, cluster networks, and cluster database (for storing data that
changes or can change quickly, such as database state changes from active to passive or the
reverse, or from mounted to dismounted or the reverse). Therefore, you can create DAGs only
on Exchange Mailbox servers installed on supported versions of Windows that include
Windows failover clustering.

  ７ Note

  The failover cluster created and used by the DAG must be dedicated to the DAG. The
  cluster can't be used for any other high availability solution or for any other purpose. For
  example, the failover cluster can't be used to cluster other applications or services. Using a
  DAG's underlying failover cluster for purposes other than the DAG isn't supported.

DAG witness server and witness directory
When you create a DAG, you need to specify a name for the DAG no longer than 15 characters
that's unique within the Active Directory forest. In addition, each DAG is configured with a
witness server and witness directory. The witness server and its directory are used only when
there's an even number of members in the DAG, and only for quorum purposes. You don't
need to create the witness directory in advance. Exchange automatically creates and secures
the directory for you on the witness server. The witness directory shouldn't be used for any
purpose other than for the DAG witness server.

  ７ Note

  In the database mirroring topology, you can have a third server called the "witness". The
  witness server enables automatic failover from principal to mirror server or vice-versa.
  Unlike principal and mirror servers, the witness server doesn't serve the database. The role
  of the witness is to verify whether a given partner server is up and functioning. Supporting
  automatic failover is the only function for witness server, and it identifies which server
  holds the principal copy and which server holds the mirror copy of the database.

The requirements for the witness server are as follows:

     The witness server can't be a member of the DAG.

     The witness server must be in the same Active Directory forest as the DAG.

     The witness server must be running Windows Server 2008 or later.

<!-- p.2667 -->

     A single server can serve as a witness for multiple DAGs. However, each DAG requires its
     own witness directory.

Regardless of which server is used as the witness server, if the Windows Firewall is enabled on
the intended witness server, you must enable the Windows Firewall exception for File and
Printer Sharing. The witness server uses SMB port 445.

  ） Important

  If the witness server you specify isn't an Exchange 2010 or later server, you must add the
  Exchange Trusted Subsystem universal security group (USG) to the local Administrators
  group on the witness server prior to creating the DAG. These security permissions are
  necessary to ensure that Exchange can create a directory and share on the witness server
  as needed.

Neither the witness server nor the witness directory needs to be fault tolerant or use any form
of redundancy or high availability. There's no need to use a clustered file server for the witness
server or employ any other form of resiliency for the witness server. There are several reasons
for this. With larger DAGs (for example, six members or more), several failures are required
before the witness server is needed. Because a six-member DAG can tolerate as many as two
voter failures without losing quorum, it would take as many as three voters failing before the
witness server would be needed to maintain a quorum. Also, if there's a failure that affects your
current witness server (for example, you lose the witness server because of a hardware failure),
you can use the Set-DatabaseAvailabilityGroup cmdlet to configure a new witness server and
witness directory (provided you have a quorum).

  ７ Note

  You can also use the Set-DatabaseAvailabilityGroup cmdlet to configure the witness
  server and witness directory in the original location if the witness server lost its storage or
  if someone changed the witness directory or share permissions.

Witness server placement considerations
The placement of a DAG's witness server will depend on your business requirements and the
options available to your organization. Exchange now includes support for new DAG
configuration options that aren't recommended or aren't possible in Exchange 2010. These
options include using a third location, such as a third datacenter, a branch office, or a Microsoft
Azure virtual network.

<!-- p.2668 -->

The following table lists general witness server placement recommendations for different
deployment scenarios.

                                                                                       ﾉ    Expand table

 Deployment Scenario                    Recommendations

 Single DAG deployed in a single        Locate witness server in the same datacenter as DAG members
 datacenter

 Single DAG deployed across two         Locate witness server on a Microsoft Azure virtual network to
 datacenters; no additional locations   enable automatic datacenter failover, or
 available                              Locate witness server in primary datacenter

 Multiple DAGs deployed in a single     Locate witness server in the same datacenter as DAG members.
 datacenter                             Additional options include:
                                              Using the same witness server for multiple DAGs
                                              Using a DAG member to act as a witness server for a
                                              different DAG

 Multiple DAGs deployed across two      Locate witness server on a Microsoft Azure virtual network to
 datacenters                            enable automatic datacenter failover, or
                                        Locate witness server in the datacenter that is considered
                                        primary for each DAG. Additional options include:

                                              Using the same witness server for multiple DAGs
                                              Using a DAG member to act as a witness server for a
                                              different DAG

 Single or Multiple DAGs deployed       In this configuration, the witness server should be located in the
 across more than two datacenters       datacenter where you want the majority of quorum votes to
                                        exist.

When a DAG has been deployed across two datacenters, you can now use a third location for
hosting the witness server. If your organization has a third location with a network
infrastructure that is isolated from network failures that affect the two datacenters in which
your DAG is deployed, then you can deploy the DAG's witness server in that third location,
thereby configuring your DAG with the ability to automatically failover databases to the other
datacenter in response to a datacenter-level failure event. If your organization only has two
physical locations, you can use a Microsoft Azure virtual network as a third location to place
your witness server.

Specifying a witness server and witness directory during DAG creation

<!-- p.2669 -->

When you create a DAG, you must provide a name for the DAG. You can optionally also specify
a witness server and witness directory.

When you create a DAG, the following combinations of options and behaviors are available:

     You can specify only a name for the DAG, and leave the Witness server and Witness
     directory fields blank. In this scenario, the wizard searches the local Active Directory site
     for a Client Access server that doesn't have the Mailbox server installed, and it
     automatically creates the default directory (%SystemDrive%:\DAGFileShareWitnesses\
     <DAGFQDN>) and default share (<DAGFQDN>) on that server and uses that Client
     Access server as the witness server. For example, consider the witness server CAS3 on
     which the operating system has been installed onto drive C. A DAG named DAG1 in the
     contoso.com domain would use a default witness directory of
     C:\DAGFileShareWitnesses\DAG1.contoso.com, which would be shared as
     \CAS3\DAG1.contoso.com.

     You can specify a name for the DAG, the witness server that you want to use, and the
     directory you want created and shared on the witness server.

     You can specify a name for the DAG and the witness server that you want to use, and
     leave the Witness directory field blank. In this scenario, the wizard creates the default
     directory on the specified witness server.

     You can specify a name for the DAG, leave the Witness server field blank, and specify the
     directory you want created and shared on the witness server. In this scenario, the wizard
     searches for a Client Access server that doesn't have the Mailbox server installed, and it
     automatically creates the specified DAG on that server, shares the directory, and uses that
     Client Access server as the witness server.

When a DAG is formed, it initially uses the Node Majority quorum model. When the second
Mailbox server is added to the DAG, the quorum is automatically changed to a Node and File
Share Majority quorum model. When this change occurs, the DAG's cluster begins using the
witness server for maintaining quorum. If the witness directory doesn't exist, Exchange
automatically creates it, shares it, and provisions the share with full control permissions for the
CNO computer account for the DAG.

  ７ Note

  Using a file share that's part of a Distributed File System (DFS) namespace isn't supported.

If Windows Firewall is enabled on the witness server before the DAG is created, it may block the
creation of the DAG. Exchange uses Windows Management Instrumentation (WMI) to create
the directory and file share on the witness server. If Windows Firewall is enabled on the witness

<!-- p.2670 -->

server and there are no firewall exceptions configured for WMI, the New-
DatabaseAvailabilityGroup cmdlet fails with an error. If you specify a witness server, but not a
witness directory, you receive the following error message:

The task was unable to create the default witness directory on server <Server Name>.

Please manually specify a witness directory.

If you specify a witness server and witness directory, you receive the following warning
message:

Unable to access file shares on witness server '<ServerName>'. Until this problem is
corrected, the database availability group may be more vulnerable to failures. You can

use the Set-DatabaseAvailabilityGroup cmdlet to try the operation again. Error: The

network path was not found.

If Windows Firewall is enabled on the witness server after the DAG is created but before servers
are added, it may block the addition or removal of DAG members. If Windows Firewall is
enabled on the witness server and there are no firewall exceptions configured for WMI, the
Add-DatabaseAvailabilityGroupServer cmdlet displays the following warning message:

Failed to create file share witness directory 'C:\DAGFileShareWitnesses\DAG_FQDN' on
witness server '<ServerName>'. Until this problem is corrected, the database availability

group may be more vulnerable to failures. You can use the Set-DatabaseAvailabilityGroup
cmdlet to try the operation again. Error: WMI exception occurred on server

'<ServerName>': The RPC server is unavailable. (Exception from HRESULT: 0x800706BA)

To resolve the preceding errors and warnings, do one of the following steps:

     Manually create the witness directory and share on the witness server, and assign the
     CNO for the DAG full control for the directory and share.

     Enable the WMI exception in Windows Firewall.

     Disable Windows Firewall.

DAG membership
After a DAG has been created, you can add servers to or remove servers from the DAG using
the Manage Database Availability Group wizard in the EAC, or the Add-
DatabaseAvailabilityGroupServer or Remove-DatabaseAvailabilityGroupServer cmdlets in the
Exchange Management Shell. For detailed steps about how to manage DAG membership, see
Manage database availability group membership.

<!-- p.2671 -->

  ７ Note

  Each Mailbox server that's a member of a DAG is also a node in the underlying cluster
  used by the DAG. As a result, at any point of time, a Mailbox server can be a member of
  only one DAG.

If the Mailbox server being added to a DAG doesn't have the failover clustering component
installed, the method used to add the server (for example, the Add-
DatabaseAvailabilityGroupServer cmdlet or the Manage Database Availability Group wizard)
installs the failover clustering feature.

When the first Mailbox server is added to a DAG, the following events occur:

     The Windows failover clustering component is installed, if it isn't already installed.

     A failover cluster is created using the name of the DAG. This failover cluster is used
     exclusively by the DAG, and the cluster must be dedicated to the DAG. Use of the cluster
     for any other purpose isn't supported.

     A CNO is created in the default computers container.

     The name and IP address of the DAG is registered as a Host (A) record in Domain Name
     System (DNS).

     The server is added to the DAG object in Active Directory.

     The cluster database is updated with information on the databases mounted on the
     added server.

In a large or multiple site environment, especially those in which the DAG is extended to
multiple Active Directory sites, you must wait for Active Directory replication of the DAG object
containing the first DAG member to complete. If this Active Directory object isn't replicated
throughout your environment, adding the second server may cause a new cluster (and a new
CNO) to be created for the DAG. This creation is because the DAG object appears empty from
the perspective of the second member being added, thereby causing the Add-
DatabaseAvailabilityGroupServer cmdlet to create a cluster and a CNO for the DAG, even
though these objects already exist. To verify that the DAG object containing the first DAG server
has been replicated, use the Get-DatabaseAvailabilityGroup cmdlet on the second server
being added to verify that the first server you added is listed as a member of the DAG.

When the second and subsequent servers are added to the DAG, the following events occur:

     The server is joined to the Windows failover cluster for the DAG.

<!-- p.2672 -->

     The quorum model is automatically adjusted:

        A Node Majority quorum model is used for DAGs with an odd number of members.

        A Node and File Share Majority quorum model is used for DAGs with an even number
        of members.

     The witness directory and share are automatically created by Exchange when needed.

     The server is added to the DAG object in Active Directory.

     The cluster database is updated with information about mounted databases.

  ７ Note

  The quorum model change should happen automatically. However, if the quorum model
  doesn't automatically change to the proper model, you can run the Set-
  DatabaseAvailabilityGroup cmdlet with only the Identity parameter to correct in the
  quorum settings for the DAG.

Pre-staging the cluster name object for a DAG
The CNO is a computer account created in Active Directory and associated with the cluster's
Name resource. The cluster's Name resource is tied to the CNO, which is a Kerberos-enabled
object that acts as the cluster's identity and provides the cluster's security context. The
formation of the DAG's underlying cluster and the CNO for that cluster is performed when the
first member is added to the DAG. When the first server is added to the DAG, remote
PowerShell contacts the Microsoft Exchange Replication service on the Mailbox server being
added. The Microsoft Exchange Replication service installs the failover clustering feature (if it
isn't already installed) and begins the cluster creation process. The Microsoft Exchange
Replication service runs under the LOCAL SYSTEM security context, and it's under this context
in which cluster creation is performed.

  Ｕ Caution

  If your DAG members are running Windows Server 2012, you must pre-stage the CNO
  prior to adding the first server to the DAG. If your DAG members are running Windows
  Server 2012 R2, and you create a DAG without a cluster administrative access point, then a
  CNO won't be created, and you don't need to create a CNO for the DAG.

In environments where computer account creation is restricted, or where computer accounts
are created in a container other than the default computers container, you can pre-stage and

<!-- p.2673 -->

provision the CNO. You create and disable a computer account for the CNO, and then do either
of the following steps:

     Assign full control of the computer account to the computer account of the first Mailbox
     server you're adding to the DAG.

     Assign full control of the computer account to the Exchange Trusted Subsystem USG.

Assigning full control of the computer account to the computer account of the first Mailbox
server you're adding to the DAG ensures that the LOCAL SYSTEM security context will be able
to manage the pre-staged computer account. Assigning full control of the computer account
to the Exchange Trusted Subsystem USG can be used instead because the Exchange Trusted
Subsystem USG contains the machine accounts of all Exchange servers in the domain.

For detailed steps about how to pre-stage and provision the CNO for a DAG, see Pre-stage the
cluster name object for a database availability group.

Removing servers from a DAG
Mailbox servers can be removed from a DAG by using the Manage Database Availability Group
wizard in the EAC or the Remove-DatabaseAvailabilityGroupServer cmdlet in the Exchange
Management Shell. Before a Mailbox server can be removed from a DAG, all replicated mailbox
databases must first be removed from the server. If you attempt to remove a Mailbox server
with replicated mailbox databases from a DAG, the task fails.

There are scenarios in which you must remove a Mailbox server from a DAG before performing
certain operations. These scenarios include:

     Performing a server recovery operation: If a Mailbox server that's a member of a DAG is
     lost, or otherwise fails and is unrecoverable and needs replacement, you can perform a
     server recovery operation using the Setup /m:RecoverServer switch. However, before you
     can perform the recovery operation, you must first remove the server from the DAG using
     the Remove-DatabaseAvailabilityGroupServer cmdlet with the ConfigurationOnly
     parameter.

     Removing the database availability group: There may be situations in which you need to
     remove a DAG (for example, when disabling third-party replication mode). If you need to
     remove a DAG, you must first remove all servers from the DAG. If you attempt to remove
     a DAG that contains any members, the task fails.

Configuring DAG properties

<!-- p.2674 -->

After servers have been added to the DAG, you can use the EAC or the Exchange Management
Shell to configure the properties of a DAG, including the witness server and witness directory
used by the DAG, and the IP addresses assigned to the DAG.

Configurable properties include:

     Witness server: The name of the server that you want to host the file share for the file
     share witness. We recommend that you specify a Client Access server as the witness
     server. This naming enables the system to automatically configure, secure, and use the
     share, as needed, and enables the messaging administrator to be aware of the availability
     of the witness server.

     Witness directory: The name of a directory that will be used to store file share witness
     data. This directory will automatically be created by the system on the specified witness
     server.

     Database availability group IP addresses: One or more IP addresses must be assigned to
     the DAG, unless the DAG members are running Windows Server 2012 R2 and you're
     creating a DAG without an IP address. Otherwise, the DAG's IP addresses can be
     configured using manually assigned static IP addresses, or they can be automatically
     assigned to the DAG using a DHCP server in your organization.

The Exchange Management Shell enables you to configure DAG properties that aren't available
in the EAC, such as DAG IP addresses; network encryption and compression settings; network
discovery; the TCP port used for replication; and alternate witness server and witness directory
settings; and to enable Datacenter Activation Coordination mode.

For detailed steps about how to configure DAG properties, see Configure database availability
group properties.

DAG network encryption
DAGs support the use of encryption by leveraging the encryption capabilities of the Windows
Server operating system. DAGs use Kerberos authentication between Exchange servers.
Microsoft Kerberos security support provider (SSP) EncryptMessage and DecryptMessage APIs
handle encryption of DAG network traffic. Microsoft Kerberos SSP supports multiple encryption
algorithms. (For the complete list, see section 3.1.5.2, "Encryption Types" of Kerberos Protocol
Extensions.) The Kerberos authentication handshake selects the strongest encryption protocol
supported in the list: typically Advanced Encryption Standard (AES) 256-bit, potentially with an
SHA Hash-based Message Authentication Code (HMAC) to maintain integrity of the data. For
more information, see HMAC      .

<!-- p.2675 -->

Network encryption is a property of the DAG and not of the DAG network. You can configure
DAG network encryption using the Set-DatabaseAvailabilityGroup cmdlet in the Exchange
Management Shell. The possible encryption settings for DAG network communications are
shown in the following table:

                                                                                       ﾉ   Expand table

 Setting           Description

 Disabled          Network encryption isn't used.

 Enabled           Network encryption is used on all DAG networks for replication and seeding.

 InterSubnetOnly   Network encryption is used on DAG networks when replicating across different
                   subnets. This setting is the default setting.

 SeedOnly          Network encryption is used on all DAG networks for seeding only.

DAG network compression
DAGs support built-in compression. When compression is enabled, DAG network
communication uses XPRESS, which is the Microsoft implementation of the LZ77 algorithm.
This compression is the same type of compression used in many Microsoft protocols, in
particular, MAPI RPC compression between Microsoft Outlook and Exchange.

As with network encryption, network compression is also a property of the DAG and not of the
DAG network. You configure DAG network compression by using the Set-
DatabaseAvailabilityGroup cmdlet in the Exchange Management Shell. The possible
compression settings for DAG network communications are shown in the following table:

                                                                                       ﾉ   Expand table

 Setting           Description

 Disabled          Network compression isn't used.

 Enabled           Network compression is used on all DAG networks for replication and seeding.

 InterSubnetOnly   Network compression is used on DAG networks when replicating across different
                   subnets. This setting is the default setting.

 SeedOnly          Network compression is used on all DAG networks for seeding only.

DAG networks

<!-- p.2676 -->

A DAG network is a collection of one or more subnets used for either replication traffic or MAPI
traffic. Each DAG contains a maximum of one MAPI network and zero or more replication
networks. In a single network adapter configuration, the network is used for both MAPI and
replication traffic. Although a single network adapter and path is supported, we recommend
that each DAG have a minimum of two DAG networks. In a two-network configuration, one
network is typically dedicated for replication traffic, and the other network is used primarily for
MAPI traffic. You can also add network adapters to each DAG member and configure additional
DAG networks as replication networks.

  ７ Note

  When using multiple replication networks, there's no way to specify an order of
  precedence for network use. Exchange randomly selects a replication network from the
  group of replication networks to use for log shipping.

In Exchange 2010, manual configuration of DAG networks was necessary in many scenarios. By
default, in later versions of Exchange, DAG networks are automatically configured by the
system. Before you can create or modify DAG networks, you must first enable manual DAG
network control by running the following command:

  PowerShell

  Set-DatabaseAvailabilityGroup <DAGName> -ManualDagNetworkConfiguration $true

After you've enabled manual DAG network configuration, you can use the New-
DatabaseAvailabilityGroupNetwork cmdlet in the Exchange Management Shell to create a
DAG network. For detailed steps about how to create a DAG network, see Create a database
availability group network.

You can use the Set-DatabaseAvailabilityGroupNetwork cmdlet in the Exchange Management
Shell to configure DAG network properties. For detailed steps about how to configure DAG
network properties, see Configure database availability group network properties. Each DAG
network has required and optional parameters to configure:

     Network name: A unique name for the DAG network of upto 128 characters.

     Network description: An optional description for the DAG network of upto 256
     characters.

     Network subnets: One or more subnets entered using a format of IPAddress/Bitmask (for
     example, 192.168.1.0/24 for Internet Protocol version 4 (IPv4) subnets;
     2001:DB8:0:C000::/64 for Internet Protocol version 6 (IPv6) subnets).

<!-- p.2677 -->

     Enable replication: In the EAC, select the checkbox to dedicate the DAG network to
     replication traffic and to block MAPI traffic. Clear the checkbox to prevent replication
     from using the DAG network and to enable MAPI traffic. In the Exchange Management
     Shell, use the ReplicationEnabled parameter in the Set-DatabaseAvailabilityGroupNetwork
     cmdlet to enable and disable replication.

  ７ Note

  Disabling replication for the MAPI network doesn't guarantee that the system won't use
  the MAPI network for replication. When all configured replication networks are offline,
  failed, or otherwise unavailable, and only the MAPI network remains (which is configured
  as disabled for replication), the system uses the MAPI network for replication.

The initial DAG networks (for example, MapiDagNetwork and ReplicationDagNetwork01)
created by the system are based on the subnets enumerated by the Cluster service. Each DAG
member must have the same number of network adapters, and each network adapter must
have an IPv4 address (and optionally, an IPv6 address as well) on a unique subnet. Multiple
DAG members can have IPv4 addresses on the same subnet, but each network adapter and IP
address pair in a specific DAG member must be on a unique subnet. In addition, only the
adapter used for the MAPI network should be configured with a default gateway. Replication
networks shouldn't be configured with a default gateway.

For example, consider DAG1, a two-member DAG where each member has two network
adapters (one dedicated for the MAPI network and the other for a replication network).
Example IP address configuration settings are shown in the following table:

Example network adapter settings

                                                                                  ﾉ    Expand table

 Server-network adapter              IP address/subnet mask              Default gateway

 EX1-MAPI                            192.168.1.15/24                     192.168.1.1

 EX1-Replication                     10.0.0.15/24                        Not applicable

 EX2-MAPI                            192.168.1.16                        192.168.1.1

 EX2-Replication                     10.0.0.16                           Not applicable

In the following configuration, there are two subnets configured in the DAG: 192.168.1.0 and
10.0.0.0. When EX1 and EX2 are added to the DAG, two subnets will be enumerated and two
DAG networks will be created: MapiDagNetwork (192.168.1.0) and ReplicationDagNetwork01
(10.0.0.0). These networks will be configured, as shown in the following table:

<!-- p.2678 -->

Enumerated DAG network settings for a single-subnet DAG

                                                                                ﾉ     Expand table

 Name                      Subnets          Interfaces        MAPI access      Replication
                                                              enabled          enabled

 MapiDagNetwork            192.168.1.0/24   EX1               True             True
                                            (192.168.1.15)
                                            EX2
                                            (192.168.1.16)

 ReplicationDagNetwork01   10.0.0.0/24      EX1 (10.0.0.15)   False            True
                                            EX2 (10.0.0.16)

To complete the configuration of ReplicationDagNetwork01 as the dedicated replication
network, disable replication for MapiDagNetwork by running the following command:

  PowerShell

  Set-DatabaseAvailabilityGroupNetwork -Identity DAG1\MapiDagNetwork -
  ReplicationEnabled:$false

After replication is disabled for MapiDagNetwork, the Microsoft Exchange Replication service
uses ReplicationDagNetwork01 for continuous replication. If ReplicationDagNetwork01
experiences a failure, the Microsoft Exchange Replication service reverts to using
MapiDagNetwork for continuous replication. Returning to MapiDagNetwork is done
intentionally by the system to maintain high availability.

DAG networks and multiple subnet deployments
In the preceding example, even though there are two different subnets in use by the DAG
(192.168.1.0 and 10.0.0.0), the DAG is considered a single-subnet DAG because each member
uses the same subnet to form the MAPI network. When DAG members use different subnets
for the MAPI network, the DAG is referred to as a multi-subnet DAG. In a multi-subnet DAG, the
proper subnets are automatically associated with each DAG network.

For example, consider DAG2, a two-member DAG where each member has two network
adapters (one dedicated for the MAPI network and the other for a replication network), and
each DAG member is located in a separate Active Directory site, with its MAPI network on a
different subnet. Example IP address configuration settings are shown in the following table:

Example network adapter settings for a multi-subnet DAG

<!-- p.2679 -->

                                                                                        ﾉ     Expand table

 Server-network adapter                  IP address/subnet mask                 Default gateway

 EX1-MAPI                                192.168.0.15/24                        192.168.0.1

 EX1-Replication                         10.0.0.15/24                           Not applicable

 EX2-MAPI                                192.168.1.15                           192.168.1.1

 EX2-Replication                         10.0.1.15                              Not applicable

In the following configuration, there are four subnets configured in the DAG: 192.168.0.0,
192.168.1.0, 10.0.0.0, and 10.0.1.0. When EX1 and EX2 are added to the DAG, four subnets will
be enumerated, but only two DAG networks will be created: MapiDagNetwork (192.168.0.0,
192.168.1.0) and ReplicationDagNetwork01 (10.0.0.0, 10.0.1.0). These networks will be
configured as shown in the following table:

Enumerated DAG network settings for a multi-subnet DAG

                                                                                        ﾉ     Expand table

 Name                      Subnets             Interfaces         MAPI access          Replication
                                                                  enabled              enabled

 MapiDagNetwork            192.168.0.0/24      EX1                True                 True
                           192.168.1.0/24      (192.168.0.15)
                                               EX2
                                               (192.168.1.15)

 ReplicationDagNetwork01   10.0.0.0/24         EX1 (10.0.0.15)    False                True
                           10.0.1.0/24         EX2 (10.0.1.15)

DAG networks and iSCSI networks
By default, DAGs perform discovery of all networks detected and configured for use by the
underlying cluster. This discovery includes that of any Internet SCSI (iSCSI) networks in use as a
result of using iSCSI storage for one or more DAG members. As a best practice, iSCSI storage
should use dedicated networks and network adapters. These networks shouldn't be managed
by the DAG or its cluster, or be used as DAG networks (MAPI or replication). Instead, these
networks should be manually disabled from use by the DAG so that they can be dedicated to
iSCSI storage traffic. To disable iSCSI networks from being detected and used as DAG networks,
configure the DAG to ignore any currently detected iSCSI networks using the Set-
DatabaseAvailabilityGroupNetwork cmdlet, as shown in this example:

<!-- p.2680 -->

  PowerShell

  Set-DatabaseAvailabilityGroupNetwork -Identity DAG2\DAGNetwork02 -
  ReplicationEnabled:$false -IgnoreNetwork:$true

This command will also disable the network for use by the cluster. Although the iSCSI networks
will continue to appear as DAG networks, they won't be used for MAPI or replication traffic
after running the above command.

Configuring DAG members
Mailbox servers that are members of a DAG have some properties specific to high availability
that should be configured as described in the following sections:

     Automatic database mount dial

     Database copy automatic activation policy

     Maximum active databases

Automatic database mount dial
The AutoDatabaseMountDial parameter specifies the automatic database mount behavior after
a database failover. You can use the Set-MailboxServer cmdlet to configure the
AutoDatabaseMountDial parameter with any of the following values:

     BestAvailability : If you specify this value, the database automatically mounts

     immediately after a failover if the copy queue length is less than or equal to 12. The copy
     queue length is the number of logs recognized by the passive copy that needs to be
     replicated. If the copy queue length is more than 12, the database doesn't automatically
     mount. When the copy queue length is less than or equal to 12, Exchange attempts to
     replicate the remaining logs to the passive copy, and mounts the database.

     GoodAvailability : If you specify this value, the database automatically mounts

     immediately after a failover if the copy queue length is less than or equal to six. The copy
     queue length is the number of logs recognized by the passive copy that needs to be
     replicated. If the copy queue length is more than six, the database doesn't automatically
     mount. When the copy queue length is less than or equal to six, Exchange attempts to
     replicate the remaining logs to the passive copy and mounts the database.

     Lossless : If you specify this value, the database doesn't automatically mount until all logs

     generated on the active copy have been copied to the passive copy. This setting also
     causes the Active Manager best copy selection algorithm to sort potential candidates for
