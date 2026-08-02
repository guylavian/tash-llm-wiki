---
title: "Core infrastructure documentation — pages 1121-1160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1121-1160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1121-1160
family: sccm
documentKind: "doc"
abstract: "To use most discovery methods, you must enable the method at a site, and set it up to search specific network or Active Directory locations. When it runs, it queries the specified location for information about devices or users that Configuration Manager can manage. When a disco"
---

# Core infrastructure documentation — pages 1121-1160

<!-- p.1121 -->

To use most discovery methods, you must enable the method at a site, and set it up to
search specific network or Active Directory locations. When it runs, it queries the
specified location for information about devices or users that Configuration Manager
can manage. When a discovery method successfully finds information about a resource,
it puts that information into a file called a discovery data record (DDR). That file is then
processed by a primary or central administration site. Processing of a DDR creates a new
record in the site database for newly discovered resources, or updates existing records
with new information.

Some discovery methods can generate a large volume of network traffic, and the DDRs
they produce can result in a significant use of CPU resources during processing.
Therefore, plan to use only those discovery methods that you require to meet your
goals. You might start by using only one or two discovery methods, and then later
enable additional methods in a controlled manner to extend the level of discovery in
your environment.

After discovery information is added to the site database, the information then
replicates to each site in the hierarchy, regardless of where it was discovered or
processed. Therefore, while you can set up different schedules and settings for discovery
methods at different sites, you might run a specific discovery method at only a single
site. This reduces the use of network bandwidth through duplicate discovery actions,
and reduces the processing of redundant discovery data at multiple sites.

You can use discovery data to create custom collections and queries that logically group
resources for management tasks. For example:

     Pushing client installations, or upgrading.

     Deploying content to users or devices.

     Deploying client settings and related configurations.

About discovery data records
DDRs are files created by a discovery method. They contain information about a
resource you can manage in Configuration Manager, such as computers, users, and in
some cases, network infrastructure. They are processed at primary sites or at central
administration sites. After the resource information in the DDR is entered into the
database, the DDR is deleted, and the information replicates as global data to all sites in
the hierarchy.

The site at which a DDR is processed depends on the information it contains:

<!-- p.1122 -->

     DDRs for newly discovered resources that are not in the database are processed at
     the top-level site of the hierarchy. The top-level site creates a new resource record
     in the database, and assigns it a unique identifier. DDRs transfer by file-based
     replication until they reach the top-level site.

     DDRs for previously discovered objects are processed at primary sites. Child
     primary sites do not transfer DDRs to the central administration site when the DDR
     contains information about a resource that is already in the database.

     Secondary sites do not process DDRs, and always transfer them by file-based
     replication to their parent primary site.

DDR files are identified by the .ddr extension, and have a typical size of about 1 KB.

Get started with discovery:
Before using the Configuration Manager console to set up discovery, you should
understand the differences among the methods, what they can do, and for some, their
limitations.

The following topics can build a foundation that will help you use discovery methods
successfully:

     About discovery methods for Configuration Manager

     Select discovery methods to use for Configuration Manager

Then, when you understand the methods you want to use, find guidance to set up each
method in Configure discovery methods for Configuration Manager.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1123 -->

About discovery methods for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager discovery methods find different devices on your network,
devices and users from Active Directory, or users from Microsoft Entra ID. To efficiently
use a discovery method, you should understand its available configurations and
limitations.

Active Directory forest discovery
Configurable: Yes

Enabled by default: No

Accounts you can use to run this method:

      Active Directory forest account (user defined)

      Computer account of the site server

Unlike other Active Directory discovery methods, Active Directory forest discovery
doesn't discover resources that you can manage. Instead, this method discovers network
locations that are configured in Active Directory. It can convert those locations into
boundaries for use throughout your hierarchy.

When this method runs, it searches the local Active Directory forest, each trusted forest,
and other forests that you configure in the Active Directory Forests node of the
Configuration Manager console.

Use Active Directory forest discovery to:

      Discover Active Directory sites and subnets, and then create Configuration
      Manager boundaries based on those network locations.

      Identify supernets that are assigned to an Active Directory site. Convert each
      supernet into an IP address range boundary.

      Publish to Active Directory Domain Services (AD DS) in a forest when publishing to
      that forest is enabled. The specified Active Directory forest account must have
      permissions to that forest.

<!-- p.1124 -->

You can manage Active Directory forest discovery in the Configuration Manager console.
Go to the Administration workspace and expand Hierarchy Configuration.

     Discovery Methods: Enable Active Directory forest discovery to run at the top-level
     site of your hierarchy. You can also specify a schedule to run discovery. Configure it
     to automatically create boundaries from the IP subnets and Active Directory sites
     that it discovers. Active Directory forest discovery can't run at a child primary site
     or at a secondary site.

     Active Directory Forests: Configure the other forests to discover, specify each
     Active Directory forest account, and configure publishing to each forest. Monitor
     the discovery process. Add IP subnets and Active Directory sites as Configuration
     Manager boundaries and members of boundary groups.

To configure publishing for Active Directory forests for each site in your hierarchy,
connect your Configuration Manager console to the top-level site of your hierarchy. The
Publishing tab in an Active Directory site's Properties dialog box can show only the
current site and its child sites. When publishing is enabled for a forest, and that forest's
schema is extended for Configuration Manager, the following information is published
for each site that is enabled to publish to that Active Directory forest:

      SMS-Site-<site code>

      SMS-MP-<site code>-<site system server name>

      SMS-SLP-<site code>-<site system server name>

      SMS-<site code>-<Active Directory site name or subnet>

  ７ Note

  Secondary sites always use the secondary site server computer account to publish
  to Active Directory. If you want secondary sites to publish to Active Directory,
  ensure that the secondary site server computer account has permissions to publish
  to Active Directory. A secondary site cannot publish data to an untrusted forest.

  Ｕ Caution

  When you uncheck the option to publish a site to an Active Directory forest, all
  previously published information for that site, including available site system roles,
  is removed from Active Directory.

<!-- p.1125 -->

Actions for Active Directory Forest Discovery are recorded in the following logs:

     All actions, except actions related to publishing, are recorded in the
     ADForestDisc.Log file in the <InstallationPath>\Logs folder on the site server.

     Active Directory Forest Discovery publishing actions are recorded in the hman.log
     and sitecomp.log files in the <InstallationPath>\Logs folder on the site server.

For more information about how to configure this discovery method, see Configure
discovery methods.

Active Directory group discovery
Configurable: Yes

Enabled by default: No

Accounts you can use to run this method:

     Active Directory group discovery account (user defined)

     Computer account of the site server

   Tip

  In addition to the information in this section, see Common features of Active
  Directory group, system, and user discovery.

Use this method to search Active Directory Domain Services to identify:

     Local, global, and universal security groups.

     The membership of groups.

     Limited information about a group's member computers and users, even when
     another discovery method hasn't previously discovered those computers and
     users.

This discovery method is intended to identify groups and the group relationships of
members of groups. By default, only security groups are discovered. If you want to also
find the membership of distribution groups, you must check the box for the option
Discover the membership of distribution groups on the Option tab in the Active
Directory Group Discovery Properties dialog box.

<!-- p.1126 -->

Active Directory group discovery doesn't support the extended Active Directory
attributes that can be identified by using Active Directory system discovery or Active
Directory user discovery. Because this discovery method isn't optimized to discover
computer and user resources, consider running this discovery method after you have
run Active Directory system discovery and Active Directory user discovery. This
suggestion is because this method creates a full discovery data record (DDR) for groups,
but only a limited DDR for computers and users that are members of groups.

You can configure the following discovery scopes that control how this method searches
for information:

     Location: Use a location if you want to search one or more Active Directory
     containers. This scope option supports a recursive search of the specified Active
     Directory containers. This process searches each child container under the
     container that you specify. It continues until no more child containers are found.

     Groups: Use groups if you want to search one or more specific Active Directory
     groups. You can configure Active Directory Domain to use the default domain and
     forest, or limit the search to an individual domain controller. Additionally, you can
     specify one or more groups to search. If you don't specify at least one group, all
     groups found in the specified Active Directory Domain location are searched.

  Ｕ Caution

  When you configure a discovery scope, choose only the groups that you must
  discover. This recommendation is because Active Directory group discovery tries to
  discover each member of each group in the discovery scope. Discovery of large
  groups can require extensive use of bandwidth and Active Directory resources.

  ７ Note

  Before you can create collections that are based on extended Active Directory
  attributes, and to ensure accurate discovery results for computers and users, run
  Active Directory system discovery or Active Directory user discovery, depending on
  what you want to discover.

Actions for Active Directory group discovery are recorded in the file adsgdis.log in the
<InstallationPath>\LOGS folder on the site server.

For more information about how to configure this discovery method, see Configure
discovery methods.

<!-- p.1127 -->

Active Directory system discovery
Configurable: Yes

Enabled by default: No

Accounts you can use to run this method:

     Active Directory system discovery account (user defined)

     Computer account of the site server

   Tip

  In addition to the information in this section, see Common features of Active
  Directory group, system, and user discovery.

Use this discovery method to search the specified Active Directory Domain Services
locations for computer resources that can be used to create collections and queries. You
can also install the Configuration Manager client on a discovered device by using client
push installation.

By default, this method discovers basic information about the computer, including the
following attributes:

     Computer name

     OS and version

     Active Directory container name

     IP address

     Active Directory site

     Time stamp of last sign in

To successfully create a DDR for a computer, Active Directory system discovery must be
able to identify the computer account and then successfully resolve the computer name
to an IP address.

In the Active Directory System Discovery Properties dialog box, on the Active
Directory Attributes tab, you can view the full list of default object attributes that it
discovers. You can also configure the method to discover extended attributes.

<!-- p.1128 -->

Actions for Active Directory system discovery are recorded in the file adsysdis.log in the
<InstallationPath>\LOGS folder on the site server.

For more information about how to configure this discovery method, see Configure
discovery methods.

Active Directory user discovery
Configurable: Yes

Enabled by default: No

Accounts you can use to run this method:

     Active Directory user discovery account (user defined)

     Computer account of the site server

   Tip

  In addition to the information in this section, see Common features of Active
  Directory group, system, and user discovery.

Use this discovery method to search Active Directory Domain Services to identify user
accounts and associated attributes. By default, this method discovers basic information
about the user account, including the following attributes:

     User name

     Unique user name, which includes the domain name

     Domain

     Active Directory container names

In the Active Directory User Discovery Properties dialog box, on the Active Directory
Attributes tab, you can view the full default list of object attributes that it discovers. You
can also configure the method to discover extended attributes.

Actions for Active Directory User Discovery are recorded in the file adusrdis.log in the
<InstallationPath>\LOGS folder on the site server.

For more information about how to configure this discovery method, see Configure
discovery methods.

<!-- p.1129 -->

Microsoft Entra user discovery
Use Microsoft Entra user discovery to search your Microsoft Entra subscription for users
with a modern cloud identity. Microsoft Entra user discovery can find the following
attributes:

      objectId

      displayName
      mail

      mailNickname
      onPremisesSecurityIdentifier

      userPrincipalName

      tenantID
      onPremisesDomainName

      onPremisesSamAccountName
      onPremisesDistinguishedName

This method supports full and delta synchronization of user attributes from Microsoft
Entra ID. This information can then be used along-side discovery data you collect from
the other discovery methods.

Actions for Microsoft Entra user discovery are recorded in the
SMS_AZUREAD_DISCOVERY_AGENT.log file on the top-tier site server of the hierarchy.

To configure Microsoft Entra user discovery, see Configure Azure Services for Cloud
Management. For information about how to configure this discovery method, see
Configure Microsoft Entra user Discovery.

Microsoft Entra user group discovery
You can discover user groups and members of those groups from Microsoft Entra ID.
Microsoft Entra user group discovery can find the following attributes:

      objectId

      displayName

      mailNickname
      onPremisesSecurityIdentifier

      tenantID

Actions for Microsoft Entra user group discovery are recorded in the
SMS_AZUREAD_DISCOVERY_AGENT.log file on the top-tier site server of the hierarchy.

<!-- p.1130 -->

For information about how to configure this discovery method, see Configure Microsoft
Entra user group discovery.

Heartbeat discovery
Configurable: Yes

Enabled by default: Yes

Accounts you can use to run this method:

     Computer account of the site server

Heartbeat discovery differs from other Configuration Manager discovery methods. It's
enabled by default and runs on each computer client instead of on a site server to
create a DDR. To help maintain the database record of Configuration Manager clients,
don't disable heartbeat discovery. In addition to maintaining the database record, this
method can force discovery of a computer as a new resource record. It can also
repopulate the database record of a computer that was deleted from the database.

Heartbeat discovery runs on a schedule configured for all clients in the hierarchy. The
default schedule for heartbeat discovery is set to every seven days. If you change the
heartbeat discovery interval, make sure that it runs more frequently than the site
maintenance task Delete Aged Discovery Data. This task deletes inactive client records
from the site database. You can configure the Delete Aged Discovery Data task only for
primary sites.

You can also manually run heartbeat discovery on a specific client. Run the Discovery
Data Collection Cycle on the Action tab of a client's Configuration Manager control
panel.

When heartbeat discovery runs, it creates a DDR that has the client's current
information. The client then copies this small file to a management point so that a
primary site can process it. The file is about 1 KB in size and has the following
information:

     Network location

     NetBIOS name

     Version of the client agent

     Operational status details

<!-- p.1131 -->

Heartbeat discovery is the only discovery method that provides details about the client
installation status. It does so by updating the system resource client attribute to set a
value equal to Yes.

Actions for heartbeat discovery are logged on the client in the InventoryAgent.log file
in the %Windir%\CCM\Logs folder.

For more information about how to configure this discovery method, see Configure
discovery methods.

Network discovery
Configurable: Yes

Enabled by default: No

Accounts you can use to run this method:

     Computer account of the site server

Use this method to discover the topology of your network and to discover devices on
your network that have an IP address. Network discovery searches your network for IP-
enabled resources by querying the following sources:

     Servers that run a Microsoft implementation of DHCP
     Address Resolution Protocol (ARP) caches in network routers
     SNMP-enabled devices
     Active Directory domains

Before you can use network discovery, you must specify the level of discovery to run.
You also configure one or more discovery mechanisms that enable network discovery to
query for network segments or devices. You can also configure settings that help control
discovery actions on the network. Finally, you define one or more schedules for when
network discovery runs.

For this method to successfully discover a resource, network discovery must identify the
IP address and the subnet mask of the resource. The following methods are used to
identify the subnet mask of an object:

     Router ARP cache: Network discovery queries the ARP cache of a router to find
     subnet information. Typically, data in a router ARP cache has a short time-to-live.
     Therefore, when network discovery queries the ARP cache, the ARP cache might no
     longer have information about the requested object.

<!-- p.1132 -->

     DHCP: Network discovery queries each DHCP server that you specify to discover
     the devices for which the DHCP server has provided a lease. Network discovery
     supports only DHCP servers that run the Microsoft implementation of DHCP.

     SNMP device: Network discovery can directly query an SNMP device. For network
     discovery to query a device, the device must have a local SNMP agent installed.
     Also configure network discovery to use the community name that the SNMP
     agent is using.

When discovery identifies an IP-addressable object and can determine the object's
subnet mask, it creates a DDR for that object. Because different types of devices connect
to the network, network discovery discovers resources that don't support the
Configuration Manager client. For example, devices that can be discovered but not
managed include printers and routers.

Network discovery can return several attributes as part of the discovery record that it
creates. These attributes include:

     NetBIOS name

     IP addresses

     Resource domain

     System roles

     SNMP community name

     MAC addresses

Network discovery activity is recorded in the Netdisc.log file in InstallationPath>\Logs
on the site server that runs discovery.

For more information about how to configure this discovery method, see Configure
discovery methods.

  ７ Note

  Complex networks and low-bandwidth connections can cause network discovery to
  run slowly and generate significant network traffic. Run network discovery only
  when the other discovery methods can't find the resources that you have to
  discover. For example, use network discovery to discover workgroup computers.
  Other discovery methods don't discover workgroup computers.

<!-- p.1133 -->

Levels of network discovery
When you configure network discovery, you specify one of three levels of discovery:

                                                                                    ﾉ   Expand table

 Level of discovery      Details

 Topology                This level discovers routers and subnets but doesn't identify a subnet
                         mask for objects.

 Topology and client     In addition to topology, this level discovers potential clients like
                         computers, and resources like printers and routers. This level of discovery
                         tries to identify the subnet mask of objects that it finds.

 Topology, client, and   In addition to topology and potential clients, this level tries to discover
 client operating        the computer operating system name and version. This level uses
 system                  Windows Browser and Windows Networking calls.

With each incremental level, network discovery increases its activity and network
bandwidth usage. Consider the network traffic that can be generated before you enable
all aspects of network discovery.

For example, when you first use network discovery, you might start with only the
topology level to identify your network infrastructure. Then, reconfigure network
discovery to discover objects and their device operating systems. You can also configure
settings that limit network discovery to a specific range of network segments. That way,
you discover objects in network locations that you require and avoid unnecessary
network traffic. This process also allows you to discover objects from edge routers or
from outside your network.

Network discovery options
To enable network discovery to search for IP-addressable devices, configure one or
more of these options.

  ７ Note

  Network discovery runs in the context of the computer account of the site server
  that runs discovery. If the computer account doesn't have permissions to an
  untrusted domain, the domain and DHCP server configurations can fail to discover
  resources.

<!-- p.1134 -->

DHCP
Specify each DHCP server that you want network discovery to query. Network discovery
supports only DHCP servers that run the Microsoft implementation of DHCP.

     Network discovery retrieves information by using remote procedure calls to the
     database on the DHCP server.

     Network discovery can query both 32-bit and 64-bit DHCP servers for a list of
     devices that are registered with each server.

     For network discovery to successfully query a DHCP server, the computer account
     of the server that runs discovery must be a member of the DHCP Users group on
     the DHCP server. For example, this level of access exists when one of the following
     statements is true

       The specified DHCP server is the DHCP server of the server that runs discovery.

       The computer that runs discovery and the DHCP server are in the same domain.

       A two-way trust exists between the computer that runs discovery and the DHCP
       server.

       The site server is a member of the DHCP Users group.

     When network discovery enumerates a DHCP server, it doesn't always discover
     static IP addresses. Network discovery doesn't find IP addresses that are part of an
     excluded range of IP addresses on the DHCP server. It also doesn't discover IP
     addresses that are reserved for manual assignment.

Domains
Specify each domain that you want network discovery to query.

     The computer account of the site server that runs discovery must have permissions
     to read the domain controllers in each specified domain.

     To discover computers from the local domain, you must enable the Computer
     Browser service on at least one computer. This computer must be on the same
     subnet as the site server that runs network discovery.

     Network discovery can discover any computer that you can view from your site
     server when you browse the network.

<!-- p.1135 -->

     Network discovery retrieves the IP address. It then uses an Internet Control
     Message Protocol (ICMP) echo request to ping each device that it finds. The ping
     command helps determine which computers are currently active.

SNMP devices
Specify each SNMP device that you want network discovery to query.

     Network discovery gets the ipNetToMediaTable value from any SNMP device that
     responds to the query. This value returns arrays of IP addresses that are client
     computers or other resources like printers, routers, or other IP-addressable
     devices.

     To query a device, you must specify the IP address or NetBIOS name of the device.

     Configure network discovery to use the community name of the device, or the
     device rejects the SNMP-based query.

Limiting network discovery
When network discovery queries an SNMP device on the edge of your network, it can
identify information about subnets and SNMP devices that are outside your immediate
network. Use the following information to limit network discovery by configuring the
SNMP devices that discovery can communicate with, and by specifying the network
segments to query.

Subnets
Configure the subnets that network discovery queries when it uses the SNMP and DHCP
options. These two options search only the enabled subnets.

For example, a DHCP request can return devices from locations across your whole
network. If you want to discover only devices on a specific subnet, specify and enable
that specific subnet on the Subnets tab in the Network Discovery Properties dialog
box. When you specify and enable subnets, you limit future DHCP and SNMP discovery
tasks to those subnets.

  ７ Note

  Subnet configurations don't limit the objects that the Domains discovery option
  discovers.

<!-- p.1136 -->

SNMP community names
To enable network discovery to successfully query an SNMP device, configure network
discovery with the community name of the device. If network discovery isn't configured
by using the community name of the SNMP device, the device rejects the query.

Maximum hops

When you configure the maximum number of router hops, you limit the number of
network segments and routers that network discovery can query by using SNMP.

The number of hops that you configure limits the number of devices and network
segments that network discovery can query.

For example, a topology-only discovery with 0 (zero) router hops discovers the subnet
on which the originating server resides. It includes any routers on that subnet.

The following diagram shows what a topology-only network discovery query finds when
it runs on Server 1 with 0 router hops specified: subnet D and Router 1.

The following diagram shows what a topology and client network discovery query finds
when it runs on Server 1 with 0 router hops specified: subnet D and Router 1, and all
potential clients on subnet D.

To get a better idea of how more router hops can increase the amount of network
resources that are discovered, consider the following network:

<!-- p.1137 -->

Running a topology-only network discovery from Server 1 with one router hop discovers
the following entities:

     Router 1 and subnet 10.1.10.0 (found with zero hops)

     Subnets 10.1.20.0 and 10.1.30.0, subnet A, and Router 2 (found on the first hop)

  ２ Warning

  Each increase to the number of router hops can significantly increase the number
  of discoverable resources and increase the network bandwidth that network
  discovery uses.

Server discovery
Configurable: No

In addition to the user-configurable discovery methods, Configuration Manager uses a
process named Server Discovery ( SMS_WINNT_SERVER_DISCOVERY_AGENT ). This discovery
method creates resource records for computers that are site systems, like a computer
that is configured as a management point.

Common features of Active Directory group
discovery, system discovery, and user discovery
This section provides information about features that are common to the following
discovery methods:

     Active Directory group discovery

     Active Directory system discovery

<!-- p.1138 -->

     Active Directory user discovery

  ７ Note

  The information in this section doesn't apply to Active Directory forest discovery.

These three discovery methods are similar in configuration and operation. They can
discover computers, users, and information about group memberships of resources that
are stored in Active Directory Domain Services. The discovery process is managed by a
discovery agent. The agent runs on the site server at each site where discovery is
configured to run. You can configure each of these discovery methods to search one or
more Active Directory locations as location instances in the local forest or remote
forests.

When discovery searches an untrusted forest for resources, the discovery agent must be
able to resolve the following to be successful:

     To discover a computer resource by using Active Directory system discovery, the
     discovery agent must be able to resolve the FQDN of the resource. If it can't
     resolve the FQDN, it then tries to resolve the resource by its NetBIOS name.

     To discover a user or group resource by using Active Directory user discovery or
     Active Directory group discovery, the discovery agent must be able to resolve the
     FQDN of the domain controller name that you specify for the Active Directory
     location.

For each location that you specify, you can configure individual search options, like
enabling a recursive search of the location's Active Directory child containers. You can
also configure a unique account to use when it searches that location. This account
provides flexibility in configuring a discovery method at one site to search multiple
Active Directory locations across multiple forests. You don't have to configure a single
account that has permissions to all locations.

When each of these three discovery methods runs at a specific site, the Configuration
Manager site server at that site contacts the nearest domain controller in the specified
Active Directory forest to locate Active Directory resources. The domain and forest can
be in any supported Active Directory mode. The account that you assign to each
location instance must have Read access permission to the specified Active Directory
locations.

Discovery searches the specified locations for objects and then tries to collect
information about those objects. A DDR is created when sufficient information about a

<!-- p.1139 -->

resource can be identified. The required information varies depending on the discovery
method that is being used.

If you configure the same discovery method to run at different Configuration Manager
sites to take advantage of querying local Active Directory servers, you can configure
each site with a unique set of discovery options. Because discovery data is shared with
each site in the hierarchy, avoid overlap between these configurations to efficiently
discover each resource a single time.

For smaller environments, consider running each discovery method at only one site in
your hierarchy. This configuration reduces administrative overhead and the potential for
multiple discovery actions to rediscover the same resources. When you minimize the
number of sites that run discovery, you reduce the overall network bandwidth that
discovery uses. You can also reduce the overall number of DDRs that are created and
must be processed by your site servers.

Many of the discovery method configurations are self-explanatory. Use the following
sections for more information about the discovery options that might require additional
information before you configure them.

The following options are available for use with multiple Active Directory discovery
methods:

     Delta Discovery

     Filter stale computer records by domain sign in

     Filter stale records by computer password

     Search customized Active Directory attributes

Delta discovery
Available for:

     Active Directory group discovery

     Active Directory system discovery

     Active Directory user discovery

Delta discovery isn't an independent discovery method but an option available for the
applicable discovery methods. Delta discovery searches specific Active Directory
attributes for changes that were made since the last full discovery cycle of the applicable

<!-- p.1140 -->

discovery method. The attribute changes are submitted to the Configuration Manager
database to update the discovery record of the resource.

By default, delta discovery runs on a five-minute cycle. This schedule is much more
frequent than the typical schedule for a full discovery cycle. This frequent cycle is
possible because delta discovery uses fewer site server and network resources than a full
discovery cycle. When you use delta discovery, you can reduce the frequency of the full
discovery cycle for that discovery method.

The following are the most common changes that delta discovery detects:

     New computers or users added to Active Directory

     Changes to basic computer and user information

     New computers or users that are added to a group

     Computers or users that are removed from a group

     Changes to system group objects

Although delta discovery can detect new resources and changes to group membership,
it can't detect when a resource has been deleted from Active Directory. DDRs created by
delta discovery are processed similarly to the DDRs that are created by a full discovery
cycle.

You configure delta discovery on the Polling Schedule tab in the properties for each
discovery method.

Filter stale computer records by domain sign in
Available for:

     Active Directory group discovery

     Active Directory system discovery

You can configure discovery to exclude computers with a stale computer record. This
exclusion is based on the last domain sign in of the computer. When this option is
enabled, Active Directory system discovery evaluates each computer that it identifies.
Active Directory group discovery evaluates each computer that is a member of a group
that's discovered.

To use this option:

<!-- p.1141 -->

     Computers must be configured to update the lastLogonTimeStamp attribute in
     Active Directory Domain Services.

     The Active Directory domain functional level must be set to Windows Server 2003
     or later.

When you're configuring the time after the last sign in that you want to use for this
setting, consider the interval for replication between domain controllers.

You configure filtering on the Option tab in the Active Directory System Discovery
Properties and Active Directory Group Discovery Properties dialog boxes. Choose to
Only discover computers that have logged on to a domain in a given period of time.

  ２ Warning

  When you configure this filter and Filter stale records by computer password,
  discovery excludes computers that meet the criteria of either filter.

Filter stale records by computer password
Available for:

     Active Directory group discovery

     Active Directory system discovery

You can configure discovery to exclude computers with a stale computer record. This
exclusion is based on the last computer account password update by the computer.
When this option is enabled, Active Directory system discovery evaluates each computer
that it identifies. Active Directory group discovery evaluates each computer that is a
member of a group that is discovered.

To use this option:

     Computers must be configured to update the pwdLastSet attribute in Active
     Directory Domain Services.

When you're configuring this option, consider the interval for updates to this attribute.
Also consider the replication interval between domain controllers.

You configure filtering on the Option tab in the Active Directory System Discovery
Properties and Active Directory Group Discovery Properties dialog boxes. Choose to

<!-- p.1142 -->

Only discover computers that have updated their computer account password in a
given period of time.

  ２ Warning

  When you configure this filter and Filter stale records by domain logon, discovery
  excludes computers that meet the criteria of either filter.

Search customized Active Directory attributes
Available for:

     Active Directory system discovery

     Active Directory user discovery

Each discovery method supports a unique list of Active Directory attributes that can be
discovered.

You can view and configure the list of customized attributes on the Active Directory
Attributes tab in the Active Directory System Discovery Properties and Active
Directory User Discovery Properties dialog boxes.

Next steps
Select discovery methods to use for Configuration Manager

Configure discovery methods

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1143 -->

Select discovery methods to use for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To successfully and efficiently use discovery for Configuration Manager, you must
consider which methods to use and at which sites to run them.

Because discovery can generate a large volume of network traffic, and the resultant
discovery data records (DDRs) can use significant CPU resources during processing, use
only those discovery methods that you require to meet your goals. You might start by
using only one or two discovery methods, and then later enable additional methods in a
controlled manner to extend the level of discovery in your environment. The information
in this topic can help you make informed decisions.

For information about the different discovery methods, see About discovery methods
for Configuration Manager.

Select methods to discover different things
To discover potential Configuration Manager client computers or user resources, you
must enable the appropriate discovery methods. You can use different combinations of
discovery methods to locate different resources, and to discover additional information
about those resources. The discovery methods that you use determine the type of
resources that are discovered, and which Configuration Manager services and agents are
used in the discovery process. They also determine the type of information about
resources that you can discover.

Discover computers
When you want to discover computers, you can use Active Directory System Discovery
or Network Discovery.

For example, if you want to discover resources that can install the Configuration
Manager client before you use client push installation, you might run Active Directory
System Discovery. Using this method, you not only discover the resource, but also
discover basic information even extended information about it from Active Directory
Domain Services. This information might be useful in building complex queries and
collections to use for the assignment of client settings or content deployment.

<!-- p.1144 -->

Alternatively, you could run Network Discovery, and use its options to discover the
operating system of resources (required to later use client push installation). Network
Discovery provides you with information about your network topology that you are not
able to acquire with other discovery methods. This method does not, however, provide
you any information about your Active Directory environment.

There is also a method called Heartbeat Discovery. It is possible to use only Heartbeat
Discovery to force the discovery of clients that you installed by methods other than
client push installation. However, unlike other discovery methods, Heartbeat Discovery
cannot discover computers that do not have an active Configuration Manager client. It
returns a limited set of information, intended to maintain an existing database record
rather than be the basis of that record. Information submitted by Heartbeat Discovery
might not be sufficient to build complex queries or collections.

If you use Active Directory Group Discovery to discover the membership of a specified
group, you can discover limited system or computer information. This does not replace
a full discovery of computers, but can provide basic information. This information is
insufficient for client push installation.

Discover users
When you want to discover information about users, use Active Directory User
Discovery. Similar to Active Directory System Discovery, this method discovers users
from Active Directory. It includes basic information, in addition to extended Active
Directory information. You can use this information to build complex queries and
collections similar to those for computers.

Discover group information
When you want to discover information about groups and group memberships, use
Active Directory Group Discovery. This discovery method creates resource records for
security groups.

You can use this method to search a specific Active Directory group to identify the
members of that group, in addition to any nested groups within that group. You can
also use this method to search an Active Directory location for groups, and recursively
search each child container of that location in Active Directory Domain Services.

This discovery method can also search the membership of distribution groups. This can
identify the group relationships of both users and computers.

<!-- p.1145 -->

When you discover a group, you can also discover limited information about its
members. This does not replace the Active Directory system or user discovery methods,
though. It is usually insufficient to build complex queries and collections, or serve as the
basis of a client push installation.

Discover infrastructure
There are two methods you can use to discover network infrastructure, Active Directory
Forest Discovery and Network Discovery.

Use Active Directory Forest Discovery to search an Active Directory forest for
information about subnets and Active Directory site configurations. These
configurations can then be automatically entered into Configuration Manager as
boundary locations.

When you want to discover your network topology, use Network Discovery. While other
discovery methods return information related to Active Directory Domain Services, and
can identify the current network location of a client, they do not provide infrastructure
information based on the subnets and router topology of your network.

Discovery data is shared among sites
After Configuration Manager adds discovery data to a database, it is quickly shared
among all sites in the hierarchy. Because there is typically no benefit to discovering the
same information at multiple sites in your hierarchy, consider setting up a single
instance of each discovery method that you use to run at a single site. It's a good idea
to do this instead of running multiple instances of a single method at different sites.

However, for some environments it might be useful to assign the same discovery
method to run at multiple sites, each with a separate configuration and schedule. For
example, when using Network Discovery, you might want to direct each site to discover
its local network, instead of attempting to discover all network locations across a WAN.

If you do configure multiple instances of the same discovery methods to run at different
sites, plan the configuration of each site carefully. You want to avoid having two or more
sites discover the same resources from your network or Active Directory. This can
consume additional network bandwidth and create duplicate DDRs.

The following table identifies at which sites you can set up the different discovery
methods.

<!-- p.1146 -->

                                                                             ﾉ     Expand table

    Discovery method                                 Supported locations

    Active Directory Forest Discovery                Central administration site

                                                     Primary site

    Active Directory Group Discovery                 Primary site

    Active Directory System Discovery                Primary site

    Active Directory User Discovery                  Primary site

    Heartbeat Discovery1                             Primary site

    Network Discovery                                Primary site

                                                     Secondary site

1
    Secondary sites cannot configure Heartbeat Discovery, but can receive the Heartbeat
DDR from a client.

When secondary sites run Network Discovery, or receive Heartbeat Discovery DDRs, they
transfer the DDR by file-based replication to their parent primary site. This is because
only primary sites and central administration sites can process DDRs. For more
information about how DDRs are processed, see About discovery data records.

Considerations for different discovery methods
Because each site server and network environment is different, it's a good idea to limit
your initial configurations for discovery. Then closely monitor each site server for its
ability to process the discovery data that is generated.

When you use an Active Directory discovery method for systems, users, or groups:

        Run discovery at a site that has a fast network connection to your domain
        controllers.

        Consider the Active Directory replication topology to ensure discovery can access
        the latest information.

        Consider the scope of the discovery configuration, and limit discovery to only
        those Active Directory locations and groups that you have to discover.

If you use Network Discovery:

<!-- p.1147 -->

     Use a limited initial configuration to identify your network topography.

     After you identify your network topography, set up Network Discovery to run at
     specific sites that are central to the network areas that you want to more fully
     discover.

Because Heartbeat Discovery does not run at a specific site, you do not have to
consider it in general planning for where to run discovery.

Best practices for discovery
For best results with discovery, we recommend the following:

     Run Active Directory System Discovery and Active Directory User Discovery
     before you run Active Directory Group Discovery.

     When Active Directory Group Discovery identifies a previously undiscovered user
     or computer as a member of a group, it attempts to discover basic details for the
     user or computer. Because Active Directory Group Discovery is not optimized for
     this type of discovery, this process can cause it to run slowly. Additionally, Active
     Directory Group Discovery identifies only the basic details about the users and
     computers it discovers, and does not create a complete user or computer
     discovery record. When you run Active Directory System Discovery and Active
     Directory User Discovery, the additional Active Directory attributes for each object
     type are available. As a result, Active Directory Group Discovery runs more
     efficiently.

     When you set up Active Directory Group Discovery, only specify groups that you
     use with Configuration Manager.

     To help control the use of resources by Active Directory Group Discovery, specify
     only those groups that you use with Configuration Manager. This is because Active
     Directory Group Discovery recursively searches each group it discovers for users,
     computers, and nested groups. The search of each nested group can expand the
     scope of Active Directory Group Discovery, and reduce performance. Additionally,
     when you set up delta discovery for Active Directory Group Discovery, the
     discovery method monitors each group for changes. This further reduces
     performance when the method must search unnecessary groups.

     Set up discovery methods with a longer interval between full discovery, and a
     more frequent period of delta discovery.

<!-- p.1148 -->

     Because delta discovery uses fewer resources than a full discovery cycle, and can
     identify new or modified resources in Active Directory, you can reduce the
     frequency of full discovery cycles to run weekly (or less). Delta discovery for Active
     Directory System Discovery, Active Directory User Discovery and Active Directory
     Group Discovery identifies almost all the changes of Active Directory objects, and
     can maintain accurate discovery data for resources.

     Run Active Directory discovery methods at a primary site that has a network
     location that is closest to your Active Directory domain controller.

     To improve the performance of Active Directory discovery, it's a good idea to run
     discover at a primary site that has a fast network connection to your domain
     controllers. If you run the same Active Directory discovery method at multiple sites,
     set up each discovery method to avoid overlap. Unlike past versions of
     Configuration Manager, discovery data is shared among sites. Therefore, it is not
     necessary to discover the same information at multiple sites. For more information,
     see Discovery data is shared between sites.

     Run Active Directory Forest Discovery at only one site when you plan to
     automatically create boundaries from the discovery data.

     If you run Active Directory Forest Discovery at more than one site in a hierarchy,
     it's a good idea to only enable options to automatically create boundaries at a
     single site. This is because when Active Directory Forest Discovery runs at each site
     and creates boundaries, Configuration Manager cannot merge those boundaries
     into a single boundary object. When you configure Active Directory Forest
     Discovery to automatically create boundaries at multiple sites, the result can be
     duplicated boundary objects in the Configuration Manager console.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1149 -->

Configure discovery methods for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configure discovery methods to find resources to manage from your network, Active
Directory, and Microsoft Entra ID. First enable and then configure each method that you
want to use to search your environment. You can also disable a method by using the
same procedure that you use to enable it. The only exceptions to this process are
Heartbeat Discovery and Server Discovery:

      By default, Heartbeat Discovery is already enabled when you install a
      Configuration Manager primary site. It's configured to run on a basic schedule.
      Keep Heartbeat Discovery enabled. It makes sure that the discovery data records
      (DDRs) for devices are up to date. For more information about Heartbeat
      Discovery, see About Heartbeat Discovery.

      Server Discovery is an automatic discovery method. It finds computers that you
      use as site systems. You can't configure or disable it.

Active Directory Forest Discovery
To finish the configuration of Active Directory Forest Discovery, configure settings in the
following locations of the Configuration Manager console:

      In the Discovery Methods node:

         Enable this discovery method.

         Set a polling schedule.

         Select whether discovery automatically creates boundaries for the Active
         Directory sites and subnets that it discovers.

      In the Active Directory Forests node:

         Add forests that you want to discover.

         Enable discovery of Active Directory sites and subnets in that forest.

         Configure settings that enable Configuration Manager sites to publish their site
         information to the forest.

<!-- p.1150 -->

        Assign an account to use as the Active Directory Forest Account for each forest.

Use the following procedures to enable Active Directory Forest Discovery, and to
configure individual forests for use with Active Directory Forest Discovery.

Configure Active Directory Forest Discovery
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Hierarchy Configuration, and select the Discovery Methods node.

   2. Select the Active Directory Forest Discovery method for the site where you want to
     configure discovery.

   3. On the Home tab of the ribbon, select Properties.

   4. On the General tab of the properties, configure the following settings:

           Enable the discovery method.

           Specify options to create site boundaries for discovered locations.

           Specify a schedule for when discovery runs.

   5. Select OK to save the configuration.

Configure a forest for Active Directory Forest Discovery
   1. In the Administration workspace, expand Hierarchy Configuration, and select the
     Active Directory Forests node. If Active Directory Forest Discovery has previously
     run, you see each discovered forest in the results pane. When this discovery
     method runs, it discovers the local forest and any trusted forests. Manually add
     untrusted forests.

           To configure a previously discovered forest, select the forest in the results
           pane. In the ribbon, select Properties to open the forest properties.

           To configure a new forest that isn't listed, on the Home tab of the ribbon, in
           the Create group, select Add Forest. This action opens the Add Forests
           dialog box.

   2. On the General tab, finish configurations for the forest that you want to discover,
     and specify the Active Directory Forest Account. For more information on this
     account, see Accounts.

<!-- p.1151 -->

        ７ Note

        Active Directory Forest Discovery requires a global account to discover and
        publish to untrusted forests. If you don't use the computer account of the site
        server, you can only select a global account.

   3. If you plan to let sites publish site data to this forest, on the Publishing tab, finish
     configurations for publishing to this forest.

        ７ Note

        If you let sites publish to a forest, extend the Active Directory schema of that
        forest for Configuration Manager. The Active Directory Forest Account must
        have Full Control permissions to the System container in that forest.

   4. Select OK to save the configuration.

Active Directory discovery for computers,
users, or groups
To configure discovery of computers, users, or groups, start with these common steps:

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Hierarchy Configuration, and select the Discovery Methods node.

   2. Select the method for the site where you want to configure discovery.

   3. On the Home tab of the ribbon, select Properties.

   4. On the General tab of the properties, select the checkbox to enable discovery. Or
     you can configure discovery now, and then return to enable discovery later.

Then use the information in the following sections to configure the specific discovery
methods:

     Active Directory Group Discovery

     Active Directory System Discovery

     Active Directory User Discovery

  ７ Note

<!-- p.1152 -->

  The information in this section doesn't apply to Active Directory Forest Discovery.

Although each of these discovery methods is independent of the others, they share
similar options. For more information about these configuration options, see Shared
options for group, system, and user discovery.

  ２ Warning

  The Active Directory polling by each of these discovery methods can generate
  significant network traffic. Consider scheduling each discovery method to run at a
  time when this network traffic doesn't adversely affect business uses of your
  network.

Configure Active Directory Group Discovery
   1. On the General tab of the Active Directory Group Discovery Properties window,
     select Add to configure a discovery scope. Select either Groups or Location. Then
     finish the following configurations in the Add Groups or Add Active Directory
     Location dialog box:

     a. Specify a Name for this discovery scope.

     b. Specify an Active Directory Domain or Location to search:

             If you chose Groups, specify one or more Active Directory groups to
             discover.

             If you chose Location, specify an Active Directory container as a location
             to discover. You can also enable a recursive search of Active Directory child
             containers for this location.

      c. Specify the Active Directory Group Discovery Account that the site uses to
        search this discovery scope. For more information, see Accounts.

     d. Select OK to save the discovery scope configuration.

   2. Repeat the previous steps for each other discovery scope that you want to define.

   3. On the Polling Schedule tab, configure both the full discovery polling schedule
     and delta discovery.

   4. On the Options tab, configure settings to filter out or exclude stale computer
     records from discovery. Also configure the discovery of the membership of

<!-- p.1153 -->

   distribution groups.

     ７ Note

     By default, Active Directory Group Discovery discovers only the membership
     of security groups.

 5. Select OK to save the configuration.

Configure Active Directory System Discovery
 1. On the General tab of the Active Directory System Discovery Properties window,
   select the New icon      to specify a new Active Directory container. In the Active
   Directory Container dialog box, finish the following configurations:

   a. Type or browse to a location for the Path. This value is a valid LDAP path to a
      container or organizational unit (OU). The site queries this path for resources.
      For example, LDAP://CN=Computers,DC=contoso,DC=com

   b. Specify options that change the search behavior:

           Discover objects within Active Directory groups: The site also looks at the
           membership of groups in this path.

           Recursively search Active Directory child containers: If you enable this
           option, the site searches any other containers or OUs within the above
           path. If you disable this option, the site only searches for resources in the
           specific path.

           Select subcontainers to exclude from this recursive search. This option
           helps to reduce the number of discovered objects. Select Add to choose
           the containers under the above path. In the Select New Container dialog
           box, select a child container to exclude. Select OK to close the Select New
           Container dialog box.

               Tip
                 The list of Active Directory containers in the Active Directory
                 System Discovery Properties window includes a column Has
                 Exclusions. When you select containers to exclude, this value is Yes.
                 Starting in version 2203, you can exclude subcontainers in
                 untrusted domains for Active Directory System Discovery and

<!-- p.1154 -->

                 Active Directory User Discovery.

    c. For each location, specify the account to use as the Active Directory Discovery
      Account. For more information, see Accounts.

         Tip

        For each specified location, you can configure a set of discovery options
        and a unique Active Directory Discovery Account.

   d. Select OK to save the Active Directory container configuration.

 2. On the Polling Schedule tab, configure both the full discovery polling schedule
   and delta discovery.

 3. On the Active Directory Attributes tab, configure other Active Directory attributes
   for computers that you want to discover. This tab lists the default object attributes.

      Tip

     For example, your organization uses the Description attribute on the
     computer account in Active Directory. Select Custom, and add Description as
     a custom attribute. After this discovery method runs, this attribute shows on
     the device Properties tab in the Configuration Manager console.

 4. On the Options tab, configure settings to filter out or exclude stale computer
   records from discovery.

 5. Select OK to save the configuration.

Configure Active Directory User Discovery
 1. On the General tab of the Active Directory User Discovery Properties window,
   select the New icon       to specify a new Active Directory container. In the Active
   Directory Container dialog box, finish the following configurations:

   a. Specify one or more locations to search.

   b. For each location, specify options that change the search behavior.

    c. For each location, specify the account to use as the Active Directory Discovery
      Account. For more information, see Accounts.

<!-- p.1155 -->

          ７ Note

          For each specified location, you can configure a unique set of discovery
          options and a unique Active Directory Discovery Account.

     d. Select OK to save the Active Directory container configuration.

   2. On the Polling Schedule tab, configure both the full discovery polling schedule
     and delta discovery.

   3. On the Active Directory Attributes tab, configure other Active Directory attributes
     for computers that you want to discover. This tab lists the default object attributes.

   4. Select OK to save the configuration.

Exclude organizational units (OU) from Active Directory User
Discovery
Starting in version 2103, you can exclude OUs from Active Directory User Discovery. To
exclude an OU:

   1. From the Configuration Manager console, go to Administration > Hierarchy
     Configuration > Discovery Methods.

   2. Select Active Directory User Discovery then select Properties from the ribbon.

   3. On the General tab of the Active Directory User Discovery Properties window,
     select the New icon to specify a new Active Directory container or Edit to change
     an existing one.

   4. In the Active Directory Container dialog box, locate the search option named
     Select sub containers to be excluded from discovery.

   5. Select Add to add an exclusion or Remove to remove an existing exclusion.

   6. Select OK to save the Active Directory container configuration.

   Tip

  Starting in version 2203, you can exclude subcontainers in untrusted domains for
  Active Directory System Discovery and Active Directory User Discovery.

<!-- p.1156 -->

Microsoft Entra user Discovery
Microsoft Entra user Discovery isn't enabled or configured the same as other discovery
methods. Configure it when you onboard the Configuration Manager site to Microsoft
Entra ID.

For more information, see Microsoft Entra user Discovery.

Prerequisites for Microsoft Entra user Discovery
To enable and configure this discovery method, Configure Azure Services for Cloud
Management.

If you use Configuration Manager to create the Azure app, it configures the app with the
necessary permissions.

If you create the app in Azure first, and then import it into Configuration Manager, you
need to manually configure the app. This configuration includes granting the server app
permission to read directory data.

   1. Open the Azure portal     as a user with Global Admin permissions. Go to Microsoft
     Entra ID, and select App registrations. Switch to All applications if necessary.

   2. Select the target application.

   3. In the Manage menu, select API permissions.

      a. On the API permissions panel, select Add a permission.

      b. In the Request API permissions panel, switch to APIs my organization uses.

      c. Search for and select the Microsoft Graph API.

      d. Select the Application permissions group. Expand Directory, and select
        Directory.Read.All.

      e. Select Add permissions.

   4. On the API permissions panel, in the Grant consent section, select Grant admin
     consent.... Select Yes.

Configure Microsoft Entra user Discovery
When configuring the Cloud Management Azure service:

<!-- p.1157 -->

     On the Discovery page of the wizard, select the option to Enable Microsoft Entra
     user Discovery.
     Select Settings.
     In the Microsoft Entra user Discovery Settings dialog box, configure a schedule for
     when discovery occurs. You can also enable delta discovery, which only checks for
     new or changed accounts in Microsoft Entra ID.

  ７ Note

  If the user is a federated or synchronized identity, you must use Configuration
  Manager Active Directory user discovery as well as Microsoft Entra user discovery.
  For more information about hybrid identities, see Define a hybrid identity
  adoption strategy.

Microsoft Entra user Group Discovery
You can discover user groups and members of those groups from Microsoft Entra ID.
When the site finds users in Microsoft Entra groups that it hasn't previously discovered,
it adds them as new user resources in Configuration Manager. A user group resource
record is created when the group is a security group.

Prerequisites for Microsoft Entra user Group Discovery
     Cloud Management Azure service
     Permission to read and search Microsoft Entra groups

Log files
Use the SMS_AZUREAD_DISCOVERY_AGENT.log for troubleshooting. This log is also
shared with Microsoft Entra user discovery. For more information, see Log files.

Enable Microsoft Entra user group discovery
To enable discovery on an existing Cloud Management Azure service:

   1. Go to the Administration workspace, expand Cloud Services, then select the Azure
     Services node.
   2. Select one of your Azure services, then select Properties in the ribbon.
   3. In the Discovery tab, check the box to Enable Microsoft Entra group Discovery,
     then select Settings.

<!-- p.1158 -->

   4. Select Add under the Discovery Scopes tab.

           You can modify the Polling Schedule in the other tab.

   5. Select one or more user groups. You can Search by name.

           You'll be prompted to sign in to Azure when you select Search the first time.

   6. Select OK when you finish selecting groups.
   7. Once discovery finishes running, you can browse your Microsoft Entra user groups
     in the Users node.

To enable discovery when configuring a new Cloud Management Azure service:

     On the Discovery page of the wizard, select the option to Enable Microsoft Entra
     group Discovery.
     Select Settings.
     In the Microsoft Entra group Discovery Settings dialog box, configure your
     discovery scope and a schedule for when discovery occurs.

Heartbeat Discovery
Configuration Manager enables the Heartbeat Discovery method when you install a
primary site. If you want to use the default schedule of every seven days, there's nothing
else to configure. Otherwise, you only have to configure the schedule for how often
clients send the Heartbeat Discovery data record to a management point.

  ７ Note

  If you enable both client push installation and the site maintenance task for Clear
  Install Flag at the same site, set the schedule of Heartbeat Discovery to be less than
  the Client Rediscovery period of the Clear Install Flag site maintenance task. By
  default, this task runs every 21 days. Heartbeat discovery should run more
  frequently than the task, or clients will unnecessarily reinstall. For more information
  about site maintenance tasks, see Maintenance tasks.

Configure the Heartbeat Discovery schedule
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Hierarchy Configuration, and select the Discovery Methods node.

<!-- p.1159 -->

   2. Select the Heartbeat Discovery method for the site where you want to configure
     Heartbeat Discovery.

   3. On the Home tab of the ribbon, select Properties.

   4. Configure the frequency with which clients submit a Heartbeat discovery data
     record. Then select OK to save the configuration.

Network Discovery
Before you configure Network Discovery, understand the following topics:

     Available levels of Network Discovery

     Available Network Discovery options

     Limiting Network Discovery on the network

For more information, see About Network Discovery.

The following sections provide information about common configurations for Network
Discovery. You can configure one or more of these configurations for use during the
same discovery run. If you use multiple configurations, plan for the interactions that can
affect the discovery results.

For example, you discover all Simple Network Management Protocol (SNMP) devices
that use a specific SNMP community name. For the same discovery run, you disable
discovery on a specific subnet. When discovery runs, Network Discovery doesn't
discover the SNMP devices with the specified community name on the subnet that
you've disabled.

Determine your network topology
You can use a topology-only discovery to map your network. This kind of discovery
doesn't discover potential clients. The topology-only Network Discovery relies on SNMP.

When you're mapping your network topology, configure the Maximum hops on the
SNMP tab in the Network Discovery Properties dialog box. Just a few hops can help
control the network bandwidth that's used when discovery runs. As you discover more
of your network, increase the number of hops to gain a better understanding of your
network topology.

After you understand your network topology, configure the properties for Network
Discovery. These properties help to discover potential clients and their operating

<!-- p.1160 -->

systems. Also configure Network Discovery to limit the network segments that it can
search.

For more information, see How to determine your network topology

Network Discovery search options
Configuration Manager supports the following methods to search the network:

     Limit searches by using subnets
     Search a specific domain
     Limit searches by using SNMP community names
     Search a specific DHCP server

Limit searches by using subnets
You can configure Network Discovery to search specific subnets during a discovery run.
By default, Network Discovery searches the subnet of the server that runs discovery. Any
other subnets that you configure and enable apply only to SNMP and DHCP search
options. When Network Discovery searches domains, it isn't limited by configurations
for subnets.

If you specify one or more subnets on the Subnets tab in the Network Discovery
Properties dialog box, it only searches the subnets that you mark as Enabled.

When you disable a subnet, the site excludes it from discovery, and the following
conditions apply:

     SNMP-based queries don't run on the subnet.

     DHCP servers don't reply with a list of resources located on the subnet.

     Domain-based queries can discover resources that are located on the subnet.

Search a specific domain

You can configure Network Discovery to search a specific domain or set of domains
during a discovery run. By default, Network Discovery searches the local domain of the
server that runs discovery.

If you specify one or more domains on the Domains tab in the Network Discovery
Properties dialog box, it only searches the domains that you mark as Enabled.
