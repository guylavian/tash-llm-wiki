---
title: "Core infrastructure documentation — pages 1161-1200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1161-1200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1161-1200
family: sccm
documentKind: "doc"
abstract: "When you disable a domain, the site excludes it from discovery, and the following conditions apply: Network Discovery doesn't query domain controllers in that domain. SNMP-based queries can still run on subnets in the domain. DHCP servers can still reply with a list of resources"
---

# Core infrastructure documentation — pages 1161-1200

<!-- p.1161 -->

When you disable a domain, the site excludes it from discovery, and the following
conditions apply:

     Network Discovery doesn't query domain controllers in that domain.

     SNMP-based queries can still run on subnets in the domain.

     DHCP servers can still reply with a list of resources located in the domain.

Limit searches by using SNMP community names
You configure Network Discovery to search a specific SNMP community or set of
communities during a discovery run. By default, the method configures the public
community name.

Network Discovery uses community names to gain access to routers that are SNMP
devices. A router can supply Network Discovery with information about other routers
and subnets that are linked to the first router.

  ７ Note

  SNMP community names resemble passwords. Network Discovery can get
  information only from an SNMP device for which you've specified a community
  name. Each SNMP device can have its own community name, but often the same
  community name is shared among several devices. Additionally, most SNMP
  devices have a default community name of public. But some organizations delete
  the public community name from their devices as a security precaution.

If you include more than one SNMP community on the SNMP tab in the Network
Discovery Properties dialog box, it searches them in the order in which they're shown.
Make sure that the most frequently used names are at the top of the list. This
configuration helps to minimize network traffic that the site generates when it tries to
contact a device by using different names.

  ７ Note

  Along with using the SNMP community name, you can specify the IP address or
  resolvable name of a specific SNMP device. You do this action on the SNMP
  Devices tab in the Network Discovery Properties dialog box.

Search a specific DHCP server

<!-- p.1162 -->

You can configure Network Discovery to use a specific DHCP server or multiple servers
to discover DHCP clients during a discovery run.

Network Discovery searches each DHCP server that you specify on the DHCP tab in the
Network Discovery Properties dialog box. If the server that's running discovery leases
its IP address from a DHCP server, you can configure discovery to search that DHCP
server. Enable this behavior with the option to Include the DHCP server that the site
server is configured to use.

  ７ Note

  To successfully configure a DHCP server in Network Discovery, your environment
  must support IPv4. You can't configure Network Discovery to use a DHCP server in
  a native IPv6 environment.

How to configure Network Discovery
Use the following procedures to first discover only your network topology, and then to
configure Network Discovery to discover potential clients by using one or more of the
available Network Discovery options.

How to determine your network topology

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Hierarchy Configuration, and select the Discovery Methods node.

   2. Select the Network Discovery method for the site where you want to discover
     network resources.

   3. On the Home tab of the ribbon, select Properties.

           On the General tab, select the option to Enable network discovery. Then
           select Topology from the Type of discovery options.

           On the Subnets tab, select the Search local subnets option.

              Tip

             If you know the specific subnets that constitute your network, deselect
             the Search local subnets checkbox. Then select the New icon      , and
             add the specific subnets that you want to search. For large networks,

<!-- p.1163 -->

              search only one or two subnets at a time to minimize the use of network
              bandwidth.

            On the Domains tab, select the option to Search local domain.

            On the SNMP tab, select an option from the Maximum hops drop-down list.
            This option specifies how many router hops Network Discovery can take in
            mapping your topology.

               Tip

              When you first map your network topology, configure just a few router
              hops to minimize the use of network bandwidth.

  4. On the Schedule tab, select the New icon     , and set a schedule for running
    discovery. The Duration is the period of time that Network Discovery has to
    complete the search for resources. On smaller subnets, an hour may be enough,
    but searching across an enterprise network with multiple router hops will take
    longer. If Network Discovery runs out of time, a message is logged in Netdisc.log.

      ７ Note

      You can't assign a different discovery configuration to separate Network
      Discovery schedules. Each time Network Discovery runs, it uses the current
      discovery configuration.

  5. Select OK to accept the configurations. Network Discovery runs at the scheduled
    time.

How to configure Network Discovery
  1. In the Configuration Manager console, go to the Administration workspace,
    expand Hierarchy Configuration, and select the Discovery Methods node.

  2. Select the Network Discovery method for the site where you want to discover
    network resources.

  3. On the Home tab of the ribbon, select Properties.

  4. On the General tab, select the option to Enable network discovery.

<!-- p.1164 -->

       Select from the Type of discovery options the type of discovery that you
       want to run.

       Enable the Slow network option for Configuration Manager to make
       automatic adjustments for low-bandwidth networks.

5. To configure discovery to search subnets, switch to the Subnets tab. Then
  configure one or more of the following options:

       To run discovery on subnets that are local to the computer that runs
       discovery, enable the option to Search local subnets.

       To search a specific subnet, make sure that the subnet is listed in Subnets to
       search and has a Search value of Enabled:

        a. If the subnet isn't listed, select the New icon     . In the New Subnet
             Assignment dialog box, enter the Subnet and Mask information, and then
             select OK. By default, a new subnet is enabled for search.

        b. To change the Search value for a listed subnet, select it in the list. Then
             select the Toggle icon to switch the value between Disabled and Enabled.

6. To configure discovery to search domains, switch to the Domains tab. Then
  configure one or more of the following options:

       To run discovery on the domain of the computer that runs discovery, enable
       the option to Search local domain.

       To search a specific domain, make sure that the domain is listed in Domains
       and has a Search value of Enabled:

        a. If the domain isn't listed, select the New icon     . In the Domain
             Properties dialog box, enter the Domain information, and then select OK.
             By default, a new domain is enabled for search.

        b. To change the Search value for a listed domain, select it in the list. Then
             select the Toggle icon to switch the value between Disabled and Enabled.

7. To configure discovery to search specific SNMP community names for SNMP
  devices, switch to the SNMP tab. Then configure one or more of the following
  options:

       To add an SNMP community name to the list of SNMP Community names,
       select the New icon       . In the New SNMP Community Name dialog box,
       specify the Name of the SNMP community, and then select OK.

<!-- p.1165 -->

       To remove an SNMP community name, select the community name, and then

       select the Delete icon     .

       To adjust the search order of SNMP community names, select a community

       name from the list. Then select the Move Item Up icon       or the Move Item
       Down icon       . When discovery runs, community names are searched in a
       top-to-bottom order.

       To configure the maximum number of router hops for use by SNMP searches,
       select the number of hops from the Maximum hops drop-down list.

8. To configure an SNMP device, switch to the SNMP Devices tab. If the device isn't
  listed, select the New icon   . In the New SNMP Device dialog box, specify the IP
  address or device name of the SNMP device, and then select OK.

    ７ Note

    If you specify a device name, Configuration Manager must be able to resolve
    the NetBIOS name to an IP address.

9. To configure discovery to query specific DHCP servers, switch to the DHCP tab.
  Then configure one or more of the following options:

       To query the DHCP server on the computer that is running discovery, enable
       the option to Always use the site server's DHCP server.

          ７ Note

          To use this option, the server must lease its IP address from a DHCP
          server and can't use a static IP address.

       To query a specific DHCP server, select the New icon    . In the New DHCP
       Server dialog box, specify the IP address or server name of the DHCP server,
       and then select OK.

          ７ Note

          If you specify a server name, Configuration Manager must be able to
          resolve the NetBIOS name to an IP address.

<!-- p.1166 -->

 10. To configure when discovery runs, switch to the Schedule tab. Then select the New
     icon     to set a schedule for running Network Discovery. You can configure
     multiple recurring schedules, and multiple schedules that have no recurrence.

        ７ Note

        If the Schedule tab shows more than one schedule at the same time, Network
        Discovery runs for all schedules as it's configured at the time indicated in the
        schedule. This behavior is also true for recurring schedules.

 11. Select OK to save your configurations.

How to verify that Network Discovery has finished
The time that Network Discovery requires to finish can vary depending on one or more
of the following factors:

     The size of your network

     The topology of your network

     The maximum number of hops that are configured to find routers in the network

     The type of discovery that is being run

Network Discovery doesn't create messages to alert you when it's finished. Use the
following procedure to verify when discovery has finished:

   1. In the Configuration Manager console, go to the Monitoring workspace. Expand
     System Status, and then select the Status Message Queries node.

   2. Select the All Status Messages query.

   3. On the Home tab of the ribbon, in the Status Message Queries group, select Show
     Messages.

   4. In the All Status Messages window, select a value from the Select date and time
     drop-down list that includes how long ago the discovery started. Then select OK to
     open the Configuration Manager Status Message Viewer.

         Tip

        You can also use the Specify date and time option to select a given date and
        time that you ran discovery. This option is useful when you ran Network

<!-- p.1167 -->

        Discovery on a given date and want to retrieve messages from only that date.

   5. To validate that Network Discovery has finished, search for a status message that
     has the following details:

           Message ID: 502

           Component: SMS_NETWORK_DISCOVERY

           Description: This component stopped

     If this status message isn't present, Network Discovery hasn't finished.

   6. To validate when Network Discovery started, search for a status message that has
     the following details:

           Message ID: 500

           Component: SMS_NETWORK_DISCOVERY

           Description: This component started

     This information verifies that Network Discovery started. If this information isn't
     present, reschedule Network Discovery.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1168 -->

Overview of boundaries and boundary
groups
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Boundaries in Configuration Manager define network locations on your intranet. These
locations include devices that you want to manage. Boundary groups are logical groups
of boundaries that you configure. A hierarchy can include any number of boundary
groups. Each boundary group can contain any combination of the following boundary
types:

      IP subnet
      Active Directory site name
      IPv6 prefix
      IP address range
      VPN (starting in version 2006)

Clients on the intranet evaluate their current network location and then use that
information to identify boundary groups to which they belong.

Clients use boundary groups to:

      Find an assigned site: Boundary groups enable clients to find a primary site for
      client assignment. This behavior is also known as automatic site assignment.

      Find certain site system roles they can use: Associate a boundary group with
      certain site system roles. Then the site provides clients with that list of site systems
      in the boundary group. Clients use these site systems for actions such as finding
      content or a nearby management point.

Clients that are on the internet or configured as internet-only clients don't use boundary
information. These clients can't use automatic site assignment. They can download
content from an internet-based distribution point from their assigned site or a content-
enabled cloud management gateway.

During OS deployment, while a device is running Windows PE, the site can convert
Active Directory site boundary information to IP subnet information. This behavior is
only during this process, and specifically for these devices. In other words, if your site
only has Active Directory site boundaries, Windows PE clients during an OS deployment
will still be in a boundary.

<!-- p.1169 -->

Overlapping boundaries
Configuration Manager supports overlapping boundary and boundary group
configurations for content and service location requests. Overlapping occurs when a
client's location maps to multiple boundary groups. This behavior happens for one of
two reasons:

     You add the same boundary to multiple boundary groups.

     You add separate boundaries that include the client's location to different
     boundary groups.

When overlapping occurs, Configuration Manager creates a list of all site systems
referenced by all boundary groups that include a client's location. Configuration
Manager sends this list to a client in response to a content or service location request.
Configuration Manager doesn't apply any precedence or deterministic ordering to this
list based on overlapping boundaries and boundary groups. Instead, the client chooses
at random from this list.

For client content requests, Configuration Manager includes only distribution points that
have the requested content in the list of site systems returned. For other service location
requests, Configuration Manager includes only site systems that host the type of role
requested which may be one of the following roles:

     State migration point

     Software update point

     Management point

This behavior enables the client to select the nearest server to communicate with for
each request type.

Recommendations

Use a mix of the fewest boundaries that meet your needs
Use whichever boundary type or types you choose that work for your environment. To
simplify your management tasks, use boundary types that let you use the fewest
number of boundaries you can.

<!-- p.1170 -->

Avoid overlapping boundaries for automatic site
assignment
Although each boundary group supports both site assignment and site system
reference, create a separate set of boundary groups to use only for site assignment.
Make sure that each boundary in a boundary group isn't a member of another boundary
group with a different site assignment.

     A single boundary can be included in multiple boundary groups.

     Each boundary group can be associated with a different primary site for site
     assignment.

     For a boundary that's a member of two different boundary groups with different
     site assignments, clients randomly select a site to join. This behavior might not be
     for the site you want the client to join. This configuration is called overlapping
     boundaries.

     Overlapping boundaries aren't a problem for content location. It can be a useful
     configuration that provides clients more resources or content locations they can
     use.

For more information on boundary groups and site assignment, see Site assignment.

Next steps
     Define network locations as boundaries

     About boundary groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1171 -->

Define network locations as boundaries
for Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager boundaries are locations on your network that contain devices
that you want to manage. You can create different types of boundaries, for example, an
Active Directory site or network IP address. When the Configuration Manager client
identifies a similar network location, that device is a part of the boundary.

Configuration Manager supports the following boundary types:

      IP subnet
      Active Directory site
      IPv6 prefix
      IP address range
      VPN (starting in version 2006)

You can manually create individual boundaries or use Active Directory forest discovery.
This discovery method automatically finds and creates boundaries for IP subnets and
Active Directory sites. When Active Directory forest discovery identifies a supernet for an
Active Directory site, Configuration Manager converts the supernet into an IP address
range boundary.

If a device isn't in the boundary you expect, it may because you haven't defined its
network location as a boundary. When the network location of a device is in doubt, use
the following Windows commands on the device to confirm:

      IP address: ipconfig
      Active Directory site: nltest /dsgetsite
      VPN: ipconfig /all

Boundary types

IP subnet
The IP subnet boundary type requires a Subnet ID. For example, 169.254.0.0 . If you
provide the Network (default gateway) and Subnet mask values, Configuration Manager

<!-- p.1172 -->

automatically calculates the Subnet ID. When you save the boundary, Configuration
Manager only saves the Subnet ID value.

  ７ Note

  Configuration Manager doesn't support the direct entry of a supernet as a
  boundary. Instead, use the IP address range boundary type.

Active Directory site
For the Active Directory site boundary type, you specify the site name. You can type the
name or browse the local forest of the site server.

When you specify an Active Directory site for a boundary, the boundary includes each IP
subnet that's a member of that Active Directory site. If the configuration of the Active
Directory site changes in Active Directory, the network locations included in this
boundary also change.

Active Directory site boundaries don't work for pure Microsoft Entra devices, also called
cloud domain-joined devices. If they roam on-premises, and you only create Active
Directory site type boundaries, these devices won't be in a boundary.

   Tip

  Use the following Windows command to see a device's current Active Directory
  site: nltest /dsgetsite .

  To determine if a client is cloud domain-joined, use the following Windows
  command: dsregcmd /status . For more information, see dsregcmd command -
  device state.

IPv6 prefix
For the IPv6 prefix boundary type, you specify a Prefix. For example,
2001:1111:2222:3333 .

IP address range
For the IP address range boundary type, specify the Starting IP address and Ending IP
address for the range. The range can include part of an IP subnet or multiple IP subnets.

<!-- p.1173 -->

Use an IP address range boundary type to support a supernet.

You can also use this type to define a boundary for a single IP address. Set both the
starting and ending IP addresses as the same value. This configuration may be useful for
unique devices or test environments.

VPN
Starting in version 2006, to simplify managing remote clients, create a boundary type for
VPNs. When a client sends a location request, it includes additional information about
its network configuration. Based upon this information, the server determines whether
the client is on a VPN. For Configuration Manager to associate the client in the
boundary, connect the device to the VPN.

You can configure a VPN boundary in several ways:

     Auto detect VPN: Configuration Manager detects any VPN solution that uses the
     point-to-point tunneling protocol (PPTP). If it doesn't detect your VPN, use one of
     the other options. The boundary value in the console list will be Auto:On .

     Connection name: Specify the name of the VPN connection on the device. It's the
     name of the network adapter in Windows for the VPN connection. Configuration
     Manager matches the first 250 characters of the string, but doesn't support
     wildcard characters or partial strings. The boundary value in the console list will be
     Name:<name> , where <name> is the connection name that you specify.

     For example, you run the ipconfig command on the device, and one of the
     sections starts with: PPP adapter ContosoVPN: . Use the string ContosoVPN as the
     Connection name. It displays in the list as Name:CONTOSOVPN .

     Connection description: Specify the description of the VPN connection.
     Configuration Manager matches the first 243 characters of the string, but doesn't
     support wildcard characters or partial strings. The boundary value in the console
     list will be Description:<description> , where <description> is the connection
     description that you specify.

     For example, you run the ipconfig /all command on the device, and one of the
     connections includes the following line: Description . . . . . . . . . . . :
     ContosoMainVPN . Use the string ContosoMainVPN as the Connection description. It

     displays in the list as Description:CONTOSOMAINVPN .

  ） Important

<!-- p.1174 -->

  To take full advantage of this feature, after you update the site, also update clients
  to the latest version. New functionality appears in the Configuration Manager
  console when you update the site and console. The complete scenario isn't
  functional until the client version is also the latest.

  To use this VPN boundary during an OS deployment, make sure to also update the
  boot image to include the latest client binaries.

Starting in version 2111, you can now match the start of a connection name or
description instead of the whole string. Some third-party VPN drivers dynamically create
the connection, which starts with a consistent string but also has a unique connection
identifier. For example, Virtual network adapter #19 . When you use the Connection
name or Connection description options, also use the new Starts with option.

Create a boundary
   1. In the Configuration Manager console, go to the Administration workspace,
     expand Hierarchy Configuration, and select the Boundaries node.

   2. On the Home tab of the ribbon, in the Create group, select Create Boundary.

   3. On the General tab of the Create Boundary window, specify the following
     information:

           Description: Identify the boundary by a friendly name or reference.

             ７ Note

             Configuration Manager automatically names the boundary based on its
             type and scope. You can't modify the name.

           Type: Select the type of boundary to create. Then specify the additional
           information that the type requires. For more information, see Boundary types.

   4. Switch to the Boundary Groups tab. If you already have boundary groups in the
     site, you can immediately add this new boundary to one or more groups.

   5. Select OK to save the new boundary.

Configure a boundary

<!-- p.1175 -->

 Tip

When you create a boundary, Configuration Manager automatically names it based
on the type and scope of the boundary. You can't modify this name. To help
identify the boundary in the Configuration Manager console, specify a description.

1. In the Configuration Manager console, go to the Administration workspace,
  expand Hierarchy Configuration, and select the Boundaries node.

2. Select the boundary you want to modify. On the Home tab of the ribbon, in the
  Properties group, select Properties.

3. In the Properties window for the boundary, on the General tab, you can configure
  the following settings:

        Edit the Description
        Change the Type for the boundary
        Change the scope of a boundary by editing its network locations. For
        example, for an Active Directory site boundary you can specify a new Active
        Directory site name.

4. To view the site systems that are associated with this boundary, switch to the Site
  Systems tab. You can't change this configuration from the properties of a
  boundary.

      Tip

     For a server to be listed as a site system for a boundary, associate it as a site
     system server for at least one boundary group that includes this boundary.
     Make this configuration on the References tab of a boundary group. For more
     information, see Configure site assignment and select site system servers.

5. To modify the boundary group membership for this boundary, select the Boundary
  Groups tab:

        To add this boundary to one or more boundary groups, select Add. Select
        one or more boundary groups, and then select OK.

        To remove this boundary from a boundary group, choose the boundary
        group, and then select Remove.

6. Select OK to close the boundary properties and save the configuration.

<!-- p.1176 -->

Next steps
Each boundary is available for use by every site in your hierarchy. After you create a
boundary, add the boundary to one or more boundary groups.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1177 -->

About boundary groups in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use boundary groups in Configuration Manager to logically organize related network
locations called boundaries. Use boundaries and boundary groups to make it easier to
manage your infrastructure. Assign boundaries to boundary groups before using the
boundary group.

By default, Configuration Manager creates a default site boundary group at each site.

To configure boundary groups, associate boundaries and site system roles to the
boundary group. This configuration helps associate clients to site system servers that are
located near the clients on the network.

To increase the availability of servers to a wider range of network locations, assign the
same boundary and the same server to more than one boundary group.

Clients use a boundary group for:

      Automatic site assignment

      To find a site system server that can provide a service, including:

         Distribution points for content location.

         Software update points

         State migration points

           ７ Note

           The state migration point doesn't use fallback relationships. For more
           information, see Fallback.

         Management points

         Preferred management points

           ７ Note

<!-- p.1178 -->

           If you use preferred management points, enable this option for the
           hierarchy, not from within the boundary group configuration. For more
           information, see Enable use of preferred management points.

        Cloud management gateway (CMG) for policy and content

Boundary groups and relationships
For each boundary group in your hierarchy, you can assign:

     One or more boundaries. A client's current boundary group is a network location
     that's defined as a boundary assigned to a specific boundary group. A client can
     have more than one current boundary group.

     One or more site system roles. Clients can always use roles associated with their
     current boundary group. Depending on other configurations, they can use roles in
     other boundary groups.

For each boundary group you create, you can configure a one-way link to another
boundary group. The link is called a relationship. The boundary groups you link to are
called neighbor boundary groups. A boundary group can have more than one
relationship, each with a specific neighbor boundary group.

When a client fails to find an available site system in its current boundary group, the
configuration of each relationship determines when it begins to search a neighbor
boundary group. This search of other groups is called fallback.

For more information, see the following articles:

     Example of using boundary groups
     Create a boundary group
     Configure a boundary group
     Show boundary groups for devices

Fallback
To prevent problems when clients can't find an available site system in their current
boundary group, define the relationship between boundary groups for fallback
behavior. Fallback lets a client expand its search to other boundary groups to find an
available site system.

<!-- p.1179 -->

Relationships are configured on a boundary group properties Relationships tab. When
you configure a relationship, you define a link to a neighbor boundary group. For each
type of supported site system role, configure independent settings for fallback to the
neighbor boundary group. For more information, see Configure fallback behavior.

For example, when you configure a relationship to a specific boundary group, set
fallback for distribution points to occur after 20 minutes. The default is 120 minutes For
a more detailed example, see Example of using boundary groups.

If a client fails to find an available site system role in its current boundary group, the
client uses the fallback time in minutes. This fallback time determines when the client
begins to search for an available site system associated with the neighbor boundary
group.

When a client can't find an available site system, it begins to search locations from
neighbor boundary groups. This behavior increases the pool of available site systems.
The configuration of boundary groups and their relationships defines the client's use of
this pool of available site systems.

     A boundary group can have more than one relationship. With this configuration,
     you can configure fallback for each type of site system to different neighbors to
     occur after different periods of time.

     Clients only fall back to a boundary group that's a direct neighbor of their current
     boundary group.

     When a client is a member of more than one boundary group, it defines its current
     boundary group as a union of all its boundary groups. The client falls back to
     neighbors of any of those original boundary groups.

  ７ Note

  The state migration point role doesn't use fallback relationships. If you add both
  the state migration point and distribution point roles to the same site system
  server, don't configure fallback on its boundary group. If you need to use boundary
  group fallback for the distribution point, add the state migration point role on a
  different site system server.

The default site boundary group
You can create your own boundary groups, and each site has a default site boundary
group that Configuration Manager creates. This group is named Default-Site-Boundary-

<!-- p.1180 -->

Group<sitecode>. For example, the group for site ABC would be named Default-Site-
Boundary-Group<ABC>.

For each boundary group you create, Configuration Manager automatically creates an
implied link to each default site boundary group in the hierarchy.

     The implied link is a default fallback option from a current boundary group to the
     site's default boundary group. The default fallback time is 120 minutes.

     For clients not in a boundary associated with any boundary group: to identify valid
     site system roles, use the default site boundary group from their assigned site.

To manage fallback to the default site boundary group:

     Open the properties of the site default boundary group, and change the values on
     the Default Behavior tab. Changes you make here apply to all implied links to this
     boundary group. When you configure an explicit link to this default site boundary
     group from another boundary group, you override these default settings.

     Open the properties of a custom boundary group. Change the values for the
     explicit link to a default site boundary group. When you set a new time in minutes
     for fallback or block fallback, that change affects only the link you're configuring.
     Configuration of the explicit link overrides the settings on the Default Behavior tab
     of a default site boundary group.

Site assignment
You can configure each boundary group with an assigned site for clients.

     A newly installed client that uses automatic site assignment joins the assigned site
     of a boundary group that contains the client's current network location.

     After assigning to a site, a client doesn't change its site assignment when it
     changes its network location. For example, a client roams to a new network
     location. This location is a boundary in a boundary group with a different site
     assignment. The client's assigned site doesn't change.

     When Active Directory System Discovery discovers a new resource, the site
     evaluates network information for the resource against the boundaries in
     boundary groups. This process associates the new resource with an assigned site
     for use by the client push installation method.

     When a boundary is a member of more than one boundary groups that have
     different assigned sites, clients randomly select one of the sites.

<!-- p.1181 -->

     Changes to a boundary groups assigned site only apply to new site assignment
     actions. Clients that previously assigned to a site don't reevaluate their site
     assignment based on changes to the configuration of a boundary group (or to
     their own network location).

For more information about client site assignment, see Using automatic site assignment
for computers.

For more information on how to configure site assignment, see the following
procedures:

     Configure site assignment and select site system servers
     Configure a fallback site for automatic site assignment

Default site boundary group behavior supports
cloud source selection
(Added in version 2207)

You can add options via PowerShell to include and prefer cloud management gateway
(CMG) management points for the default site boundary group. When a site is set up,
there's a default site boundary group created for each site and all the clients are by
default mapped to it until they're assigned to some custom boundary group.

Currently on the admin console, you can add references to default site boundary group,
but the added references don't have any effect when the client requests for
management point list. Starting with technical preview version 2206, you can use
PowerShell cmdlets to include and prefer cloud-based sources for clients in the default
site boundary group. This action is currently only for the management point role.

  ７ Note

  You can't currently configure this behavior from the Configuration Manager
  console. For more information on configuring this behavior with PowerShell, see
  the cmdlet details in the following section.

Set-CMDefaultBoundaryGroup
Use this cmdlet to modify the properties of a default site boundary group. You can set
the options to include and prefer the cloud-based sources for the clients in default site
boundary group.

<!-- p.1182 -->

Syntax

 PowerShell

 Set-CMDefaultBoundaryGroup [-IncludeCloudBasedSources <Boolean>] [-
 PreferCloudBasedSources <Boolean>]

Examples

 PowerShell

 Set-CMDefaultBoundaryGroup -IncludeCloudBasedSources $true -
 PreferCloudBasedSources $true

 Set-CMDefaultBoundaryGroup -IncludeCloudBasedSources $true

 Set-CMDefaultBoundaryGroup -IncludeCloudBasedSources $true -
 PreferCloudBasedSources $false

Parameters
    IncludeCloudBasedSources: Used to specify whether admin wants to include the
    cloud-based sources in the management point list for the clients in default site
    boundary group.

    PreferCloudBasedSources: Used to specify whether admin wants to prefer the
    cloud-based sources in the management point list for the clients in default site
    boundary group. On selecting this option, cloud-based servers will be given
    preference by the clients.

 ７ Note

 You can only set this option to true if the parameter IncludeCloudBasedSources is
 set to true or was already set to true by admin.

Next steps
    Boundary group options

    Procedures for boundary groups

<!-- p.1183 -->

  ７ Note

  Some sections that were previously in this article have moved:

        Show boundary groups for devices
        Distribution points
        Boundary group options
        Software update points
        Management points
        Preferred management points
        Overlapping boundaries
        Example of using boundary groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1184 -->

Boundary group options
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To give you more control over policy and content distribution in your environment,
boundary groups include several options to configure behaviors. These settings
primarily apply to downloading content from peer sources. There's also a setting for
clients to prefer policy and content from cloud-based sources.

For more information on how to configure these settings, see Configure a boundary
group.

If a device is in more than one boundary group, the following behaviors apply for these
settings:

      Allow peer downloads in this boundary group: If it's disabled in any one
      boundary group, the client won't use delivery optimization.
         During peer downloads, only use peers within the same subnet: If it's enabled
         in any one boundary group, this setting takes effect.
         Prefer distribution points over peers within the same subnet: If it's enabled in
         any one boundary group, this setting takes effect.
      Prefer cloud based sources over on-premises sources: If it's enabled in any one
      boundary group, this setting takes effect.

Allow peer downloads in this boundary group
This setting is enabled by default. The management point provides clients a list of
content locations that includes peer sources. This setting also affects applying Group IDs
for Delivery Optimization.

There are two common scenarios in which you should consider disabling this option:

      If you have a boundary group that includes boundaries from geographically
      dispersed locations such as a VPN. Two clients may be in the same boundary
      group because they're connected through VPN, but in vastly different locations
      that are inappropriate for peer sharing of content.

      If you use a single, large boundary group for site assignment that doesn't
      reference any distribution points.

  ） Important

<!-- p.1185 -->

  If a device is in more than one boundary group, make sure to enable this setting on
  all boundary groups for the device. Otherwise the client won't use delivery
  optimization. For example, it doesn't set the DOGroupID registry key.

During peer downloads, only use peers within
the same subnet
This setting is dependent upon the preceding option. If you enable this option, the
management point only includes in the content location list peer sources that are in the
same subnet as the client.

Common scenarios for enabling this option:

      Your boundary group design for content distribution includes one large boundary
      group that overlaps other smaller boundary groups. With this new setting, the list
      of content sources that the management point provides to clients only includes
      peer sources from the same subnet.

      You have a single large boundary group for all remote office locations. Enable this
      option and clients only share content within the subnet at the remote office
      location, instead of risking sharing content between locations.

Depending on the configuration of your network, you can exclude certain subnets for
matching. For example, you want to include a boundary but exclude a specific VPN
subnet. By default, Configuration Manager excludes the default Teredo subnet
( 2001:0000:% ).

  ７ Note

  When you expand a stand-alone primary site to add a central administration site
  (CAS), the subnet exclusion list reverts to the default. To work around this issue,
  after site expansion, run the PowerShell script to customize the subnet exclusion list
  on the CAS.

Import your subnet exclusion list as a comma-separated subnet string. Use the percent
sign ( % ) as a wildcard character. On the top-level site server, set or read the
SubnetExclusionList embedded property for the SMS_HIERARCHY_MANAGER
component in the SMS_SCI_Component class. For more information, see
SMS_SCI_Component server WMI class.

<!-- p.1186 -->

Sample PowerShell script to update the subnet exclusion
list
The following script is a sample way of changing this value. Append your subnets to the
PropertyValue variable after 2001:0000:%,172.16.16.0 . It's a comma-separated string.
Run this script on the top-level site server in your hierarchy.

  PowerShell

  $PropertyValue = "2001:0000:%,172.16.16.0"
  $PropertyName = "SubnetExclusionList"

  $providerMachine = Get-WmiObject -Class "SMS_ProviderLocation" -Namespace
  "root\sms"

  if ($providerMachine -is [system.array])
  {
      $providerMachine=$providerMachine[0]
  }

  $SiteCode = $providerMachine.SiteCode

  $component = Get-WmiObject -Query 'select comp.* from sms_sci_component comp
  join SMS_SCI_SiteDefinition sdef on sdef.SiteCode=comp.SiteCode where
  sdef.ParentSiteCode="" and comp.componentname="SMS_HIERARCHY_MANAGER"' -
  ComputerName $providerMachine.Machine -Namespace root\sms\site_$SiteCode
  $properties = $component.props

  Write-host "Updating property for site " $SiteCode

  foreach ($property in $properties)
  {
    if ($property.propertyname -like $PropertyName)
    {
      Write-host "Current value for SubnetExclusionList is " $property.value1
      $property.value1 = $PropertyValue
      Write-host "Updating value for SubnetExclusionList to " $property.value1
      break
    }
  }

  $component.props = $properties
  $component.put()

  ７ Note

<!-- p.1187 -->

  By default, Configuration Manager includes the Teredo subnet in this list. When you
  change the list, always read the existing value first. Append additional subnets to
  the list, and then set the new value.

Prefer distribution points over peers within the
same subnet
By default, the management point prioritizes peer cache sources at the top of the list of
content locations. This setting reverses that priority for clients that are in the same
subnet as the peer cache source.

   Tip

  This behavior applies to the Configuration Manager client. It doesn't apply when
  the task sequence downloads content. When the task sequence runs, it prefers peer
  cache sources over distribution points.

Prefer cloud based sources over on-premises
sources
If you have a branch office with a faster internet link, you can prioritize cloud-based
sources, which include the following locations:

     Cloud management gateway (CMG). Clients will prefer the CMG for both policy
     and content.
        Starting in version 2203, this setting also applies for software update scanning.
        To reduce the performance impact of this change, existing clients don't
        automatically switch to a cloud-based software update point. For more
        information, see Boundary groups and software update points.
     Microsoft Update
        You can only use Microsoft Update as a source when you enable the following
        option in the software update deployment download settings: If software
        updates are not available on distribution point in current, neighbor or site
        boundary groups, download content from Microsoft Updates.

Next steps
     Boundary groups and distribution points

<!-- p.1188 -->

     Procedures for boundary groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1189 -->

Boundary groups and distribution
points
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When a client requests the location of a distribution point, Configuration Manager
sends the client a list of site systems. These site systems are of the appropriate type
associated with each boundary group that includes the client's current network location.

      During software distribution, clients request a location for deployment content on
      a valid content source. This location may be a distribution point, or a peer cache
      source.

      During OS deployment, clients request a location to send or receive their state
      migration information.
          Clients get content based on boundary group behaviors. For more information,
          see Task sequence support for boundary groups.

During content deployment, if a client requests content that isn't available from a source
in its current boundary group, the client continues to request that content. The client
tries different content sources in its current boundary group until it reaches the fallback
period for a neighbor or the default site boundary group. If the client still hasn't found
content, it then expands its search for content sources to include the neighbor boundary
groups.

If you configure the content to distribute on-demand, and it isn't available on a
distribution point when a client requests it, the site begins to transfer the content to that
distribution point. It's possible the client finds that server as a content source before
falling back to use a neighbor boundary group.

Client installation
The Configuration Manager client installer, ccmsetup, can get installation content from a
local source or via a management point. Its initial behavior depends upon the
command-line parameters you use to install the client:

      If you don't use either /mp or /source parameters, ccmsetup tries to get a list of
      management points from Active Directory or DNS.

<!-- p.1190 -->

     If you only specify /source , it forces the installation from the specified path. It
     doesn't discover management points. If it can't find ccmsetup.cab at the specified
     path, ccmsetup fails.

     If you specify both /mp and /source , it checks the specified management points,
     and any it discovers. If it can't locate a valid management point, it falls back to the
     specified source path.

For more information on these ccmsetup parameters, see Client installation parameters
and properties.

When ccmsetup contacts the management point to locate the necessary content, the
management point returns distribution points based on boundary group configuration.
If you define relationships on the boundary group, the management point returns
distribution points in the following order:

   1. Current boundary group

   2. Neighbor boundary groups

   3. The site default boundary group

  ７ Note

  The client setup process doesn't use the fallback time. To locate content as quickly
  as possible, it immediately falls back to the next boundary group.

  In previous versions of Configuration Manager, during this process the
  management point only returned distribution points in the client's current
  boundary group. If no content was available, the setup process fell back to
  download content from the management point. There was no option to fall back to
  distribution points in other boundary groups that might have the necessary
  content.

Task sequence support
When a device runs a task sequence and needs to acquire content, it uses boundary
group behaviors similar to the Configuration Manager client.

Configure this behavior using the following settings on the Distribution Points page of
the task sequence deployment:

<!-- p.1191 -->

     When no local distribution point is available, use a remote distribution point: For
     this deployment, the task sequence can fall back to distribution points in a
     neighbor boundary group.

     Allow clients to use distribution points from the default site boundary group: For
     this deployment, the task sequence can fall back to distribution points in the
     default site boundary group.

To use this new behavior, make sure to update clients to the latest version.

Location priority
The task sequence tries to acquire content in the following order:

   1. Peer cache sources

   2. Distribution points in the current boundary group

   3. Distribution points in a neighbor boundary group

        ） Important

        Due to the real-time nature of task sequence processing, it doesn't wait for
        the failover time on a neighbor boundary group. It uses the failover times for
        prioritizing the neighbor boundary groups. For example, if the task sequence
        fails to acquire content from a distribution point in its current boundary
        group, it immediately tries a distribution point in a neighbor boundary group
        with the shortest failover time. If that process fails, it then fails over to a
        distribution point in a neighbor boundary group with a larger failover time.

        For content like applications and software updates, which are downloaded by
        the client and not the task sequence engine, the client behaves as normal. In
        other words, if you install applications or software updates from a task
        sequence, when the client tries to download the content it will wait for
        boundary group failover.

   4. Distribution points in the site default boundary group

The task sequence log file smsts.log shows the priority of the location sources that it
uses based on the deployment properties.

Next steps

<!-- p.1192 -->

     Boundary groups and software update points

     Procedures for boundary groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1193 -->

Boundary groups and software update
points
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Clients use boundary groups to find a new software update point. To control which
servers a client can find, add individual software update points to different boundary
groups.

If you add all existing software update points to the default site boundary group, the
client selects a software update point from the pool of available servers. This behavior is
similar to earlier versions of Configuration Manager current branch. For controlled
selection and fallback behavior, add individual software update points to different
boundary groups.

If you install a new site, software update points aren't added to the default site
boundary group. Assign software update points to a boundary group so that clients can
find and use them.

Fallback
Configure software update point fallback like other site system roles, but with the
following caveats.

New clients use boundary groups to select software
update points
When you install new clients, they select a software update point from those servers
associated with the boundary groups you configure. This behavior replaces the previous
behavior where clients select a software update point randomly from a list of the servers
that share the client's forest.

Clients continue to use a last known-good software
update point until they fall back to find a new one
Clients that already have a software update point continue to use it until it can't be
reached. This behavior includes continued use of a software update point that isn't
associated with the client's current boundary group.

<!-- p.1194 -->

This behavior is intentional. The client continues to use an existing software update
point, even when it isn't in the client's current boundary group. When the software
update point changes, the client synchronizes data with the new server, which causes
significant network usage. If all clients switch to a new server at the same time, the delay
in transition helps to avoid saturating your network.

A client always tries to reach its last known-good
software update point for 120 minutes before starting
fallback
After 120 minutes, if the client hasn't established contact, it then begins fallback. When
fallback starts, the client receives a list of all software update points in its current
boundary group. Other software update points in neighbor and site default boundary
groups are available based on fallback configurations.

Fallback configurations
You can configure Fallback times (in minutes) for software update points to be less than
120 minutes. However, the client still tries to reach its original software update point for
120 minutes. Then it expands its search to other servers. Boundary group fallback times
start when the client first fails to reach its original server. When the client expands its
search, the site provides any boundary groups configured for less than 120 minutes.

To block fallback for a software update point to a neighbor boundary group, configure
the setting to Never fallback.

After failing to reach its original server for two hours, the client then uses a shorter cycle
to establish a connection to a new software update point. This behavior enables the
client to rapidly search through the expanding list of potential software update points.

Example
You configure software update points in boundary group A to fall back after 10 minutes.
You configure the same setting for boundary group B to 130 minutes. A client in
boundary group Z fails to reach its last known-good software update point.

     For the next 120 minutes, the client tries to reach only its original server in
     boundary group Z. After 10 minutes, Configuration Manager adds the software
     update points from boundary group A to the pool of available servers. However,
     the client doesn't try to contact them or any other server until the initial 120-
     minute period elapses.

<!-- p.1195 -->

     After trying to contact the original software update point for 120 minutes, the
     client expands its search. It adds servers to the available pool of software update
     points that are in it's current and any neighbor boundary groups configured for
     120 minutes or less. This pool includes the servers in boundary group A, which
     were previously added to the pool of available servers.

     After 10 more minutes, the client expands the search to include software update
     points from boundary group B. This period is 130 minutes of total time after the
     client first failed to reach its last known-good software update point.

Manually switch to a new software update
point
Along with fallback, use client notification to manually force a device to switch to a new
software update point.

When you switch to a new server, the devices use fallback to find that new server.
Clients switch to the new software update point during their next software updates scan
cycle.

Review your boundary group configurations. Before you start this change, make sure
that your software update points are in the correct boundary groups.

For more information, see Manually switch clients to a new software update point.

Intranet clients can use a CMG software update
point
Intranet clients can access a software update point via a cloud management gateway
(CMG). Assign the CMG to a boundary group, and enable the software update point to
Allow Configuration Manager cloud management gateway traffic.

This behavior is useful in the following scenarios:

     When an internet machine connects to the VPN, it will continue to scan against the
     CMG software update point over the internet.

     If the only software update point for the boundary group is the CMG software
     update point, then all intranet and internet devices will scan against it.

Prefer cloud-based software update points

<!-- p.1196 -->

(Introduced in version 2203)

Starting in version 2203, clients prefer to scan against a cloud management gateway
(CMG) software update point (SUP) over an on-premises SUP when the boundary group
uses the Prefer cloud based source over on-premises source option. To reduce the
performance impact of this change, clients don't automatically switch their SUP to a
cloud-based SUP. The client will stay assigned to their current SUP unless their current
SUP fails or the client is manually switched to a new SUP. You won't need to manually
switch the SUP for any new clients added to the environment after the boundary group
option is set.

Use the following high-level guidance to set your clients to prefer a cloud-based
software update point:

   1. Ensure your cloud management gateway is configured and functional
   2. Verify that your software update points are functional and synchronized.
   3. Enable the Allow Configuration Manager cloud management gateway traffic
     option for any SUP you want to use with CMG.
   4. Configure the boundary group for this behavior by enabling the Prefer cloud
     based sources over on-premises sources option and adding the CGM SUP server
     to the Site system servers list.
   5. To manually switch clients to a new SUP, use the Switch to next Software Update
     Point client notification action for a device or for a collection.

           Clients in the boundary group don't automatically switch to a new SUP*9
           unless scanning against their current SUP fails four times over the course of
           two hours.
           You won't need to manually switch the SUP for any new clients added to the
           environment after the boundary group option is set.

   6. To verify that clients prefer the CMG SUP, start a software update scan cycle on
     some of the clients that you switched.

           To limit potential performance issues caused by a large number of clients
           scanning against a new SUP simultaneously, we recommend that if you're
           immediately calling a scan cycle on a large number of clients that you start
           with no more than 100 clients every 10-15 minutes. Increase or decrease the
           number of clients and the frequency once you gauge the performance impact
           in your environment.

Next steps

<!-- p.1197 -->

     Boundary groups and management points

     Procedures for boundary groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1198 -->

Boundary groups and management
points
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configure fallback relationships for management points between boundary groups. This
behavior provides greater control for the management points that clients use. On the
Relationships tab of the boundary group properties, there's a column for management
point. When you add a new fallback boundary group, the fallback time for the
management point is currently always zero (0). This behavior is the same for the Default
Behavior on the site default boundary group.

Previously, a common problem occurred when you had a protected management point
in a secure network. Clients on the main network received policy that included this
protected management point, even though they couldn't communicate with it across a
firewall. To address this problem now, use the Never fallback option to make sure that
clients only fall back to management points with which they can communicate.

  ７ Note

  If you enable distribution points in the site default boundary group to fallback, and
  a management point is collocated on a distribution point, the site also adds that
  management point to the site default boundary group.

If a client is in a boundary group with no assigned management point, the site gives the
client the entire list of management points. This behavior makes sure that a client always
receives a list of management points.

   Tip

  If you enable the option to Prefer cloud-based sources over on-premises sources
  then clients will prefer a cloud management gateway (CMG) for both policy and
  content.

Management point boundary group fallback doesn't change the behavior during client
installation (ccmsetup.exe). If the command line doesn't specify the initial management
point using the /MP parameter, the new client receives the full list of available
management points. For its initial bootstrap process, the client uses the first

<!-- p.1199 -->

management point it can access. Once the client registers with the site, it receives the
management point list properly sorted with this new behavior.

For more information on the client's behavior to acquire content during installation, see
Client installation.

During client upgrade, if you don't specify the /MP command-line parameter, the client
queries sources such as Active Directory and WMI for any available management point.
Client upgrade doesn't honor the boundary group configuration.

For clients to use this capability, enable the following setting: Clients prefer to use
management points specified in boundary groups in Hierarchy Settings.

  ７ Note

  OS deployment processes aren't aware of boundary groups for management
  points.

Troubleshoot
New entries appear in the LocationServices.log. The Locality attribute identifies one of
the following states:

      0: Unknown

      1: The specified management point is only in the site default boundary group for
      fallback.

      2: The specified management point is in a remote or neighbor boundary group.
      When the management point is in both a neighbor and the site default boundary
      groups, the locality is 2.

      3: The specified management point is in the local or current boundary group.
      When the management point is in the current boundary group and either a
      neighbor or the site default boundary group, the locality is 3. If you don't enable
      the preferred management points setting in Hierarchy Settings, the locality is
      always 3 no matter which boundary group the management point is in.

Clients use local management points first (locality 3), remote second (locality 2), then
fallback (locality 1).

When a client receives five errors in 10 minutes and fails to communicate with a
management point in its current boundary group, it tries to contact a management

<!-- p.1200 -->

point in a neighbor or the site default boundary group. If the management point in the
current boundary group later comes back online, the client returns to the local
management point on the next refresh cycle. The refresh cycle is 24 hours, or when the
Configuration Manager agent service restarts.

Preferred management points

  ７ Note

  When you enable Clients prefer to use management points specified in boundary
  groups, Configuration Manager uses the boundary group functionality for the
  assigned management point.

Preferred management points enable a client to identify a management point that's
associated with its current network location (boundary).

     A client tries to use a preferred management point from its assigned site before
     using one not configured as preferred from its assigned site.

     To use this option, enable Clients prefer to use management points specified in
     boundary groups in Hierarchy Settings. Then configure boundary groups at
     individual primary sites. Include the management points that should be associated
     with that boundary group's associated boundaries. For more information, see
     Enable use of preferred management points.

     When you configure preferred management points, and a client organizes its list of
     management points, the client places the preferred management points at the top
     of its list. This list includes all management points from the client's assigned site.

  ７ Note

  Client roaming means it changes its network locations. For example, when a laptop
  travels to a remote office location. When a client roams, it might use a
  management point from the local site before attempting to use a server from its
  assigned site. This list of servers from its assigned site includes the preferred
  management points. For more information, see Understand how clients find site
  resources and services.

Next steps
