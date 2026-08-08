---
title: "Core infrastructure documentation — pages 361-400"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p0361-0400
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p0361-0400
family: sccm
documentKind: "doc"
abstract: "laptops. By combining approaches this way, you can cover all of your device management needs. There are also two tables that compare the management solutions by the following factors: Compare by supported platforms Compare by management functionality Configuration Manager client"
---

# Core infrastructure documentation — pages 361-400

<!-- p.361 -->

laptops. By combining approaches this way, you can cover all of your device
management needs.

There are also two tables that compare the management solutions by the following
factors:

     Compare by supported platforms
     Compare by management functionality

Configuration Manager client
This option requires installation of the Configuration Manager client on devices. It
provides the most features for managing PCs, servers, and other devices in your
environment.

For more information, see Client installation methods.

Security Management for Microsoft Defender for
Endpoint
This options requires utilizing Microsoft Defender for Endpoint on your devices and is
intended to provide security management capability in circumstances where Microsoft
Intune or Microsoft Configuration Manager are not present. This uses the Microsoft
Defender for Endpoint client to communicate directly with Intune and apply security
management policy.

For more information, see Security Management for Microsoft Defender for Endpoint
(MDE).

Co-management with Microsoft Intune
Co-management is one of the primary ways to attach your existing Configuration
Manager deployment to the Microsoft 365 cloud. It enables you to concurrently manage
Windows devices by using both Configuration Manager and Microsoft Intune. Co-
management lets you cloud-attach your existing investment in Configuration Manager
by adding new functionality.

For more information, see What is co-management?.

Microsoft Exchange

<!-- p.362 -->

This option uses the Exchange Server connector to connect multiple Exchange servers to
Configuration Manager. It centralizes management of devices that can connect to
Exchange ActiveSync. You can configure Exchange mobile device management features
from the Configuration Manager console. Example features include remote device wipe
and the settings control for multiple Exchange servers.

For more information, see Manage mobile devices with Configuration Manager and
Exchange.

Compare solutions by supported platforms

                                                                          ﾉ   Expand table

 Platform           Configuration         On-premises     Configuration Manager     Intune
                    Manager client        MDM             with Exchange

 Android                                                  Yes                       Yes

 iOS                                                      Yes                       Yes

 macOS X            Yes                                   Yes                       Yes

 Windows 10/11      Yes                   Yes             Yes                       Yes

 Windows 10                               Yes             Yes                       Yes
 Mobile

 Windows            Yes                                   Yes
 (previous
 versions)

 Windows Server     Yes                                   Yes

 Windows            Yes
 Embedded

For a complete list of supported platforms, see the following articles:

       Supported operating systems for clients and devices for Configuration Manager
       Intune supported configurations

Microsoft recommends using Intune to manage Android, iOS, and Windows 10/11
mobile devices. For more information, see What is Microsoft Intune?.

Compare solutions by management functionality

<!-- p.363 -->

                                                                      ﾉ   Expand table

 Management functionality           Configuration    On-        Configuration
                                    Manager client   premises   Manager with
                                                     MDM        Exchange

 Certificate-based mutual           Yes              Yes
 authentication

 Client installation                Yes

 Support over the internet          Yes

 Discovery                          Yes                         Yes

 Hardware inventory                 Yes              Yes        Yes

 Software inventory                 Yes                         Yes

 Settings                           Yes              Yes        Yes

 Software deployment                Yes              Yes

 Software update management         Yes

 OS deployment                      Yes

 Block from Configuration           Yes              Yes
 Manager

 Quarantine and block from                                      Yes
 Exchange Server (and
 Configuration Manager)

 Remote wipe                                         Yes        Yes

Feedback
Was this page helpful?       Yes    No

Provide product feedback

<!-- p.364 -->

Design a hierarchy of sites for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before installing the first site of a new Configuration Manager hierarchy, it's a good idea
to understand:

      The available topologies for Configuration Manager

      The types of available sites and their relationships with each other

      The scope of management that each type of site provides

      The content management options that can reduce the number of sites you need to
      install

Then plan a topology that efficiently serves your current business needs and can later
expand to manage future growth.

When planning, keep in mind limitations for adding additional sites to a hierarchy or a
stand-alone site:

      Install a new primary site below a central administration site, up to the supported
      number of primary sites for the hierarchy.

      Expand a standalone primary site to install a new central administration site, to
      then install additional primary sites.

      Install new secondary sites below a primary site, up to the supported limit for the
      primary site and overall hierarchy.

      You can't add a previously installed site to an existing hierarchy to merge two
      standalone sites. Configuration Manager only supports installation of new sites to
      an existing hierarchy of sites.

  ７ Note

  When planning a new installation of Configuration Manager, be aware of the
  release notes, which detail current issues in the active versions. The release notes
  apply to all branches of Configuration Manager. When you use the technical

<!-- p.365 -->

  preview branch, find issues specific to that branch in the documentation for each
  version of the technical preview.

Hierarchy topology
Hierarchy topologies range from:

     Simplest: A single standalone primary site

     Most complex: A group of connected primary and secondary sites with a central
     administration site at the top-level site of the hierarchy

The key driver of the type and count of sites that you use in a hierarchy is usually the
number and type of devices you must support.

Standalone primary site
Use a standalone primary site when it can support management of all devices and users.
For more information, see Sizing and scale numbers. This topology is also successful
when your company's geographic locations can be served by a single primary site. To
help manage network traffic, use multiple management points in boundary groups, and
a carefully planned content infrastructure. For more information, see Configure
boundary groups and Fundamental concepts for content management.

This topology provides the following benefits:

     Simplified administrative overhead

     Simplified client site assignment and discovery of available resources and services

     Elimination of possible delays introduced by database replication between sites

     Option to expand a standalone primary site into a larger hierarchy with a central
     administration site. This option enables you to then install new primary sites to
     expand the scale of your deployment.

Central administration site with one or more child
primary sites
Use this topology when you require more than one primary site to support
management of all your devices and users. It's required when you need to use more
than a single primary site.

<!-- p.366 -->

This topology provides the following benefits:

        It supports up to 25 primary sites that enable you to extend the scale of your
        hierarchy.

        You always use the central administration site, unless you reinstall your sites. This
        option is permanent. You can't detach a child primary site to make it a standalone
        primary site.

Determine when to use a central administration
site
Use a central administration site to configure hierarchy-wide settings and to monitor all
sites and objects in the hierarchy. This site type doesn't manage clients directly. It
coordinates site-to-site data replication, which includes the configuration of sites and
clients throughout the hierarchy.

The following information can help you decide when to install a central administration
site:

        The central administration site is the top-level site in a hierarchy.

        When you configure a hierarchy that has more than one primary site, install a
        central administration site.

           If you immediately need two or more primary sites, install the central
           administration site first.

           When you already have a primary site, and want to then install a central
           administration site, expand the stand-alone primary site to install the central
           administration site.

        The central administration site supports only primary sites as child sites.

        The central administration site can't have clients assigned to it.

        The central administration site doesn't support site system roles that directly
        support clients, such as management points and distribution points.

        Manage all clients in the hierarchy and perform all site management tasks from the
        Configuration Manager console that is connected to the central administration site.
        These tasks include installing management points or other site system roles at
        child primary or secondary sites.

<!-- p.367 -->

     When you use a central administration site, it's the only place where you see site
     data from all sites in your hierarchy. This data includes information such as
     inventory data and status messages.

     Configure discovery operations throughout the hierarchy from the central
     administration site. From the central administration site, assign discovery methods
     to run at individual primary sites.

     Manage security throughout the hierarchy by assigning different security roles,
     security scopes, and collections to different administrative users. These
     configurations apply at each site in the hierarchy.

     Configure replication to control communication between sites in the hierarchy.
     Schedule database replication for site data, and managing the bandwidth for the
     transfer of file-based data between sites.

Determine when to use a primary site
Use primary sites to manage clients. Install a primary site as a child site below a central
administration site, or as the first site of a new hierarchy. A primary site that's the first
site of a hierarchy creates a standalone primary site. Both child primary sites and
standalone primary sites support secondary sites.

Consider adding additional primary sites for the following reasons:

     To increase the number of devices, manage with a single hierarchy.

     To meet organizational management requirements. For example, you might install
     a primary site at a remote location to manage the transfer of deployment content
     across a low-bandwidth network.
        Consider instead using options to throttle the network bandwidth when
        transferring data to a distribution point. That content management capability
        can replace the need to install additional sites.

The following information can help you decide when to install a primary site:

     A primary site can be a standalone primary site or a child primary site in a larger
     hierarchy. When a primary site is a member of a hierarchy with a central
     administration site, the sites use database replication to replicate data between the
     sites. Unless you need to support more clients and devices than a single primary
     site supports, consider installing a standalone primary site. After you install a
     standalone primary site, expand it if needed in the future to report to a new central
     administration site to scale up your deployment.

<!-- p.368 -->

     A primary site supports only a central administration site as a parent site.

     A primary site supports only secondary sites as child sites, and supports multiple
     secondary sites.

     Primary sites are responsible for processing all client data from their assigned
     clients.

     Primary sites use database replication to communicate directly to their central
     administration site. This behavior is configured automatically when a new site
     installs.

Determine when to use a secondary site
Use secondary sites to manage the transfer of deployment content and client data
across low-bandwidth networks.

You manage a secondary site from a central administration site or the secondary site's
direct parent primary site. Secondary sites are attached to a primary site. You can't move
them to a different parent site without uninstalling them and then reinstalling them as a
child site below the new primary site.

However, you can route content between two peer secondary sites to help manage the
file-based replication of deployment content. To transfer client data to a primary site,
the secondary site uses file-based replication. A secondary site also uses database
replication to communicate with its parent primary site.

Consider installing a secondary site if any of the following conditions apply:

     You don't require a local point of connectivity for an administrative user.

     You're required to manage the transfer of deployment content to sites lower in the
     hierarchy.

     You're required to manage client information that's sent to sites higher in the
     hierarchy.

If you don't want to install a secondary site, and you have clients in remote locations,
consider the following options:

     Use peer-to-peer technologies such as Windows BranchCache

     Enable distribution points for bandwidth control and scheduling

<!-- p.369 -->

Use these content management options with or without secondary sites. They help
reduce the size of your Configuration Manager infrastructure. For more information
about content management options in Configuration Manager, see Determine when to
use content management options.

The following information can help you decide when to install a secondary site:

     If a local instance of SQL Server isn't available, secondary site servers automatically
     install SQL Server Express during site installation.

     Secondary site installation is initiated from the Configuration Manager console,
     instead of running setup directly on a computer.

     Secondary sites use a subset of the information in the site database. This behavior
     reduces the amount of data that SQL Server replicates between the parent primary
     site and secondary site.

     Secondary sites support the routing of file-based content to other secondary sites
     that have a common parent primary site.

     Secondary site installations automatically install the management point and
     distribution point site system roles on the secondary site server.

Determine when to use content management
options
If you have clients in remote network locations, consider using one or more content
management options instead of a primary or secondary site. The following options often
remove the need to install a site:

     Windows Delivery Optimization

     Configuration Manager peer cache

     Windows BranchCache

     Configure distribution points for bandwidth control

     Manually copy content to distribution points (prestage content)

If any of the following conditions apply, consider deploying a distribution point instead
of installing another site:

     Your network bandwidth is sufficient for client computers at the remote location to
     communicate with a management point at the primary site. Clients communicate

<!-- p.370 -->

     with a management point to download client policy, send inventory, send
     reporting status, and send discovery information.

     Background Intelligent Transfer Service (BITS) doesn't provide sufficient bandwidth
     control for your network requirements.

For more information about content management options in Configuration Manager,
see Fundamental concepts for content management.

Beyond hierarchy topology
Along with your initial hierarchy topology, also consider the following questions:

     Which site system roles provide services or capabilities from different sites in the
     hierarchy?

     How are you managing hierarchy-wide configurations and capabilities in your
     infrastructure?

The following common considerations are covered in separate articles. This information
is important to influence or be influenced by your hierarchy design:

     When you're preparing to Manage computers and devices, consider whether the
     devices are on-premises, in the cloud, or include user-owned devices (BYOD).
     Additionally, consider how you'll manage devices that support multiple
     management options. For example, manage Windows devices with Configuration
     Manager or though integration with Microsoft Intune. For more information, see
     Choose a device management solution.

     Understand how your available network infrastructure might affect the flow of data
     between remote locations. For more information, see Prepare your network
     environment. Also consider the geographic location of your users and devices, and
     whether they access your infrastructure through your on-premises network or the
     internet.

     Plan for a content infrastructure to efficiently distribute the content you deploy to
     devices you manage. This content may be applications, software updates, or
     operating systems. For more information, see Manage content and content
     infrastructure.

     Determine which features and capabilities of Configuration Manager you plan to
     use. Different features require different site system roles or Windows infrastructure.
     In a multiple site hierarchy, decide where you deploy them for the most efficient
     use of your network and server resources.

<!-- p.371 -->

     Consider security for data and devices, including the use of a public key
     infrastructure (PKI). For more information, see PKI certificate requirements.

Next steps
Review the following articles for site-specific configurations:

     Plan for the SMS Provider

     Plan for the site database

     Plan for site system servers and site system roles

     Plan for security

     Managing network bandwidth when deploying content within a site

Consider configurations that span sites and hierarchies

     High availability options for sites and hierarchies

     Extend the Active Directory schema and configure sites to publish site data

     Data transfers between sites

     Fundamentals of role-based administration

     Manage clients on the internet

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.372 -->

Plan for the SMS Provider
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To manage Configuration Manager, you use a Configuration Manager console that
connects to an instance of the SMS Provider. By default, an SMS Provider installs on the
site server when you install a central administration site (CAS) or primary site.

About
The SMS Provider is a Windows Management Instrumentation (WMI) provider that
assigns read and write access to the Configuration Manager database at a site.

      Each CAS and primary site require at least one SMS Provider. You can install more
      providers as needed.

      The SMS Admins security group provides access to the SMS Provider.
      Configuration Manager automatically creates this group on the site server, and on
      each computer where you install an instance of the SMS Provider. For more
      information, see SMS Admins.

      Secondary sites don't support the SMS Provider role.

Configuration Manager administrative users use an SMS Provider to access information
that's stored in the database. To do so, admins can use the Configuration Manager
console, Resource Explorer, tools, and custom scripts. The SMS Provider doesn't interact
with Configuration Manager clients. When a Configuration Manager console connects to
a site, it queries WMI on the site server to locate an instance of the SMS Provider to use.

The SMS Provider helps enforce Configuration Manager security. It returns only the
information that the console user is authorized to view.

The SMS Provider also provides API interoperability access over HTTPS, called the
administration service. This REST API can be used in place of a custom web service to
access information from the site. For more information, see What is the administration
service?.

  ） Important

<!-- p.373 -->

  When each instance of the SMS Provider for a site is offline, Configuration Manager
  consoles can't connect to the site.

For more information about how to manage the SMS Provider, see Manage the SMS
Provider.

Prerequisites
The SMS Provider has the following prerequisites:

     In the same domain as the site server and the site database site systems

     Can't have a site system role from a different site

     Can't already have an SMS Provider from any site

     Run a supported OS version

     At least 650 MB of free disk space to support the Windows ADK components. For
     more information about Windows ADK and the SMS Provider, see OS deployment
     requirements.

     For the administration service REST API:

        Starting in version 2107, the SMS Provider requires .NET version 4.6.2, and
        version 4.8 is recommended. In version 2103 and earlier, this role requires .NET
        4.5 or later. For more information, Site and site system prerequisites.

        In version 2006 and earlier, enable the Windows server role Web Server (IIS).
        Starting in version 2010, this role is no longer required.

            ７ Note

            Every SMS Provider attempts to install the administration service, which
            requires a certificate. This service has a dependency on IIS to bind that
            certificate to HTTPS port 443. If you enable Enhanced HTTP, then the site
            binds that certificate using IIS APIs. If your site uses PKI, you need to
            manually bind a PKI certificate in IIS on the SMS Provider. Unless the server
            already has a PKI-based certificate, the site automatically uses the site's
            self-signed certificate.

Locations

<!-- p.374 -->

When you install a site, you automatically install the first SMS Provider for the site. You
can specify any of the following supported locations for the SMS Provider:

     The site server

     The site database server

     Another server, which meets the installation prerequisites

To view the locations of each SMS Provider for a site:

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and then select the Sites node.

   2. Select a site from the list, and then choose Properties in the ribbon.

   3. On the General tab of the site Properties, view the SMS Provider location field.

Each SMS Provider supports simultaneous connections from multiple requests. The only
limitations on these connections are the number of server connections that are available
to Windows, and the available resources on the server to service the connection
requests.

After you install a site, you can run Configuration Manager setup on the site server
again. Use setup to change the location of an existing SMS Provider, or to install more
SMS Providers at that site. Install only one SMS Provider on a computer. A computer
can't host an SMS Provider from more than one site.

Choosing a location
The following sections describe the advantages and disadvantages of installing an SMS
Provider on each supported location:

Configuration Manager site server
     Advantages:

        The SMS Provider doesn't use the system resources of the site database
        computer.

        This location can provide better performance than an SMS Provider located on a
        computer other than the site server or site database computer.

     Disadvantages:

<!-- p.375 -->

      The SMS Provider uses system and network resources that could be dedicated
      to site server operations.

SQL Server that hosts the site database

    Advantages:

      The SMS Provider doesn't use system resources on the site server.

      This location can provide the best performance of the three locations, if
      sufficient server resources are available.

    Disadvantages:

      The SMS Provider uses system and network resources that could be dedicated
      to site database operations.

      When the site database is hosted on a clustered instance of SQL Server, you
      can't use this location.

Computer other than the site server or site database server

    Advantages:

      SMS Provider doesn't use site server or site database system resources.

      This type of location lets you deploy more SMS Providers to provide high
      availability for connections.

    Disadvantages:

      The SMS Provider performance might be reduced. This behavior is because of
      the more network activity that it requires to coordinate with the site server and
      the site database computer.

      This server must be always accessible to the site database server, and to all
      computers with the Configuration Manager console installed.

      This location can use system resources that would otherwise be dedicated to
      other services.

Authentication

<!-- p.376 -->

You can specify the minimum authentication level for administrators to access
Configuration Manager sites. This feature enforces administrators to sign in to Windows
with the required level before they can access Configuration Manager. It applies to all
components that access the SMS Provider. For example, the Configuration Manager
console, SDK methods, and Windows PowerShell cmdlets.

Configuration Manager supports the following authentication levels:

      Windows authentication: Require authentication with Active Directory domain
      credentials. This setting is the previous behavior, and the current default setting.

      Certificate authentication: Require authentication with a valid certificate that's
      issued by a trusted PKI certificate authority. You don't configure this certificate in
      Configuration Manager. Configuration Manager requires the administrator to be
      signed into Windows using PKI.

      Windows Hello for Business authentication: Require authentication with strong
      two-factor authentication that's tied to a device and uses biometrics or a PIN. For
      more information, see Windows Hello for Business.

         ） Important

         When you select this setting, the SMS Provider and administration service
         require the user's authentication token to contain a multi-factor
         authentication (MFA) claim from Windows Hello for Business. In other words,
         a user of the console, SDK, PowerShell, or administration service has to
         authenticate to Windows with their Windows Hello for Business PIN or
         biometric. Otherwise the site rejects the user's action.

         This behavior is for Windows Hello for Business, not Windows Hello.

For more information on how to configure this setting, see Configure SMS Provider
authentication.

SMS Provider languages
The SMS Provider operates independently of the display language of the server where
you install it.

When an administrative user or Configuration Manager process requests data by using
the SMS Provider, it attempts to return that data in a format that matches the OS
language of the requesting computer.

<!-- p.377 -->

The way it attempts to match the language is indirect. The SMS Provider doesn't
translate information from one language to another. When it returns data for display in
the Configuration Manager console, the display language of the data depends on the
source of the object and type of storage.

When Configuration Manager stores data for an object in the database, the available
languages depend on the following factors:

     Configuration Manager stores objects that it creates by using support for multiple
     languages. It stores the object in the site database by using the languages that you
     configure for the site when you run setup. The Configuration Manager console
     displays these objects in the display language of the requesting computer, when
     that language is available for the object. If the console can't display the object in
     the display language of the requesting computer, it displays the object in the
     default language, which is English.

     Configuration Manager stores objects that an administrative user creates by using
     the language that was used to create the object. These objects display in the
     Configuration Manager console in this same language. The SMS Provider can't
     translate them, and they don't have multiple language options.

Use multiple SMS Providers
After a site completes installation, you can install more SMS Providers for the site. To
install more SMS Providers, run Configuration Manager setup on the site server.

Consider installing more SMS Providers when any of the following are true:

     Many administrative users need to use the Configuration Manager console and
     connect to a site at the same time.

     You use the Configuration Manager SDK, or other products, that might introduce
     frequent calls to the SMS Provider.

     You have a business requirement for high availability of the SMS Provider.

When you install multiple SMS Providers at a site, and a connection request is made, the
site randomly assigns each new connection request to use an installed SMS Provider.
You can't specify the SMS Provider to use with a specific connection session.

  ７ Note

<!-- p.378 -->

  Consider the advantages and disadvantages of each SMS Provider location. For
  more information, see Locations. Balance these considerations with the information
  that you can't control which SMS Provider is used for each new connection.

When you first connect a Configuration Manager console to a site, the connection
queries WMI on the site server. This query identifies an instance of the SMS Provider
that the console uses. This specific instance of the SMS Provider remains in use by the
console until the session ends. If the session ends because the SMS Provider server is
unavailable on the network, when you reconnect the console to the site, it repeats the
initial query. It's possible the site assigns the same SMS Provider instance that's not
available. If this behavior occurs, attempt to reconnect the console until the site returns
an available SMS Provider.

SMS Provider namespace
The Configuration Manager WMI schema defines the structure of the SMS Provider.
Schema namespaces describe the location of Configuration Manager data within the
SMS Provider schema. The following table contains some of the common namespaces
that the SMS Provider uses:

                                                                                   ﾉ   Expand table

 Namespace                       Description

 Root\SMS\site_<site code>       The SMS Provider, which is extensively used by the
                                 Configuration Manager console, Resource Explorer,
                                 Configuration Manager tools, and scripts.

 Root\SMS\SMS_ProviderLocation   The location of the SMS Provider computers for a site.

 Root\CIMv2                      The location inventoried for WMI namespace information
                                 during hardware and software inventory.

 Root\CCM                        Configuration Manager client configuration policies and client
                                 data.

 Root\CIMv2\SMS                  The location of inventory reporting classes that the inventory
                                 client agent collects. Clients compile these settings during
                                 computer policy evaluation. These settings are based on the
                                 client settings configuration for the computer.

OS deployment requirements

<!-- p.379 -->

The computer where you install an instance of the SMS Provider requires a supported
version of the Windows ADK.

For more information about this requirement, see Infrastructure requirements for OS
deployment and Support for the Windows ADK.

When you manage OS deployments, the Windows ADK allows the SMS Provider to
complete various tasks, such as:

     View WIM file details

     Add driver files to existing boot images

     Create boot ISO files

The Windows ADK installation can require up to 650 MB of free disk space on each
computer that installs the SMS Provider. This high disk space requirement is necessary
for Configuration Manager to install the Windows PE boot images.

Administration service
The SMS Provider provides API interoperability access over an HTTPS OData connection,
called the administration service. This REST API can be used in place of a custom web
service to access information from the site.

For more information, see What is the administration service?

Next steps
Manage the SMS Provider

Configure authentication for the SMS Provider

Plan for the site database

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.380 -->

Plan for the site database for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The site database server is a computer that runs a supported version of Microsoft SQL
Server. SQL Server is used to store information for Configuration Manager sites. Each
site in a Configuration Manager hierarchy contains a site database and a server that is
assigned the site database server role.

      For central administration sites and primary sites, you can install SQL Server on the
      site server, or you can install SQL Server on a computer other than the site server.

      For secondary sites, you can use SQL Server Express instead of a full SQL Server
      installation. The database server must, however, be run on the secondary site
      server.

      For SQL Server Always On availability groups, set the database recovery model to
      FULL.

      For non-availability group configurations, set the database recovery model to
      SIMPLE.

Further information on SQL Server Recovery Modes can be found in Recovery Models
(SQL Server).

The following SQL Server configurations can be used to host the site database:

      The default instance of SQL Server

      A named instance on a single computer running SQL Server

      A named instance on a failover cluster instance of SQL Server

      A SQL Server Always On availability group

To host the site database, the SQL Server must meet the requirements detailed in
Support for SQL Server versions for Configuration Manager.

Remote database server location
considerations

<!-- p.381 -->

If you use a remote database server computer, ensure that the intervening network
connection is a high-availability, high-bandwidth network connection. The site server
and some site system roles must constantly communicate with the remote server that is
hosting the site database.

     The amount of bandwidth required for communications to the database server
     depends on a combination of many different site and client configurations.
     Therefore, the actual bandwidth required cannot be adequately predicted.

     Each computer that runs the SMS Provider and that connects to the site database
     increases network bandwidth requirements.

     The computer that runs SQL Server must be located in a domain that has two-way
     trust with the site server and all computers running the SMS Provider.

     You can't use a failover cluster instance of SQL Server for the site database server
     when the site database is co-located with the site server.

Typically, a site system server supports site system roles from only a single Configuration
Manager site. You can, however, use different instances of SQL Server to host a database
from different Configuration Manager sites. To support databases from different sites,
configure each instance of SQL Server to use unique ports for communication.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.382 -->

Plan for site system servers and site
system roles in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Each Configuration Manager site you install includes a site server that's a site system
server. The site can also include additional site system servers on computers that are
remote from the site server. Site system servers (the site server or a remote site system
server) support site system roles.

Site system servers
When you install a site system role on a computer, that computer becomes a site system
server. At each site, you can install one or more additional site system servers. You don't
have to install additional site system servers, and can choose to run all site system roles
directly on the site server computer. Each site system server supports one or more site
system roles. Additional servers can help expand the capabilities and capacity of a site
by sharing the processing load that site system roles place on a server.

When considering the addition of a site system server, ensure the server meets
prerequisites for the intended use. Also add it on a network location that has sufficient
bandwidth to communicate with expected endpoints. These endpoints include the site
server, domain resources, a cloud-based location, site system servers, and clients.

Site system roles
Install site system roles on a server to provide additional capabilities to the site.
Examples include:

      Additional management points so that the site can support more devices, up to
      the site's supported capacity.

      Additional distribution points to expand your content infrastructure, improving the
      performance of content distributions to devices.

      One or more feature-specific site system roles. For example, a software update
      point lets you manage software updates for managed devices. A reporting services
      point lets you run reports to monitor, understand, and share information about
      your environment.

<!-- p.383 -->

Different Configuration Manager sites can support different sets of site system roles. The
supported set of site system roles depends on the type of site. (The types of sites
include a central administration site, primary sites, or secondary sites.) The topology of
your hierarchy can limit the placement of some roles at certain site types. For example,
the service connection point is only supported at the top-tier site of the hierarchy. The
top-tier site might be a central administration site or a standalone primary site. This role
isn't supported at a child primary site or at secondary sites.

After a site installs, you can move the location of some site system roles from their
default location on the site server to another server. For example, the management
point or distribution point roles install by default on a primary or secondary site server.
Also install additional instances of some site system roles to expand the capabilities of
your site, and to meet your business requirements. Some roles are required, while others
are optional.

Configuration Manager site server
This role identifies the server where Configuration Manager setup is run to install a site,
or the server on which you install a secondary site. You can't move or uninstall this role
until the site is uninstalled.

Configuration Manager site system
This role is assigned to any computer on which you either install a site or install a site
system role. You can't move or uninstall this role until you remove the last site system
role from the computer.

Configuration Manager component site system role
This role identifies a site system that runs an instance of the SMS Executive service. It's
required to support other roles, like management points. You can't move or uninstall
this role until you remove the last applicable site system role from the computer.

Configuration Manager site database server
The site assigns this role to site system servers that hold an instance of the site
database. Only move this role to a new server by running setup to modify the site to use
a different instance of SQL Server to host the site database.

SMS Provider

<!-- p.384 -->

The site assigns this role to each computer that hosts an instance of the SMS Provider.
The provider is the interface between a Configuration Manager console and the site
database. By default, this role automatically installs on the site server of a central
administration site and primary sites. Install additional instances at each site to provide
access to additional administrative users or for redundancy.

To install additional providers, run Configuration Manager setup to Manage the SMS
Provider. Then install additional providers on additional computers. Only install one
instance of the SMS Provider on a computer. That computer must be in the same
domain as the site server.

Asset Intelligence synchronization point

  ） Important

  Starting in November 2021, this feature of Configuration Manager is deprecated.
  For more information, see Asset intelligence deprecation.

A site system role that connects to Microsoft to download information for the Asset
Intelligence catalog. This role also uploads uncategorized titles, so that Microsoft can
consider them for future inclusion in the catalog. A hierarchy supports only a single
instance of this role at the top-tier site of your hierarchy. If you expand a standalone
primary site into a larger hierarchy, uninstall this role from the primary site. Then install
it at the central administration site.

For more information, see Asset Intelligence in Configuration Manager.

Certificate registration point

  ２ Warning

  Starting in version 2203, the certificate registration point is no longer supported.
  For more information, see Frequently asked questions about resource access
  deprecation.

A site system role that communicates with a server that runs the Network Device
Enrollment Service (NDES). This role manages device certificate requests that use the
Simple Certificate Enrollment Protocol (SCEP). This role is supported only at primary sites
and the central administration site.

<!-- p.385 -->

Although a single certificate registration point can provide functionality to an entire
hierarchy, you may want to install multiple instances of this role at a site, and at multiple
sites in the same hierarchy. This design helps with load balancing. When multiple
instances exist in a hierarchy, clients are randomly assigned to one of the certificate
registration points.

Each certificate registration point requires access to a separate NDES instance. You can't
configure two or more certificate registration points to use the same NDES instance.
Additionally, don't install the certificate registration point on the same server that runs
NDES.

Cloud management gateway connection point
A site system role for communicating with the cloud management gateway.

Data warehouse service point
Use the data warehouse service point to store and report on long-term historical data in
your Configuration Manager environment. For more information, see Data warehouse.

Distribution point
A site system role that contains source files for clients to download, for example:

     Application content
     Software packages
     Software updates
     OS images
     Boot images

By default, this role installs on the site server when you install a new primary or
secondary site. This role isn't supported at a central administration site. Install multiple
instances of this role at a supported site, and at multiple sites in the same hierarchy. For
more information, see Fundamental concepts for content management, and Manage
content and content infrastructure.

Endpoint Protection point
A site system role that Configuration Manager uses to accept the Endpoint Protection
license terms, and to configure the default membership for Cloud Protection Service. A
hierarchy only supports a single instance of this role, and that must be at the top-tier

<!-- p.386 -->

site. If you expand a standalone primary site into a larger hierarchy, uninstall this role
from the primary site, and then install it at the central administration site. For more
information, see Endpoint Protection in Configuration Manager.

Enrollment point

  ） Important

  With the deprecation of on-premises MDM and the Configuration Manager client
  for macOS, this site system role is also deprecated. For more information, see
  Removed and deprecated features for Configuration Manager.

A site system role that uses PKI certificates for Configuration Manager to enroll mobile
devices and macOS computers. Although this role is supported only at primary sites, you
can install multiple instances of this role at a site, or at multiple sites in the same
hierarchy.

If a user enrolls mobile devices by using Configuration Manager, and the user's Active
Directory account is in a forest that's untrusted by the site server's forest, install an
enrollment point in the user's forest. Then Configuration Manager can authenticate the
user.

Enrollment proxy point

  ） Important

  With the deprecation of on-premises MDM and the Configuration Manager client
  for macOS, this site system role is also deprecated. For more information, see
  Removed and deprecated features for Configuration Manager.

A site system role that manages Configuration Manager enrollment requests from
mobile devices and macOS computers. Although this role is supported only at primary
sites, you can install multiple instances of this role at a site, or at multiple sites in the
same hierarchy.

When you support mobile devices on the internet, install an enrollment proxy point in a
perimeter network, and install one on the intranet.

Exchange Server connector

<!-- p.387 -->

For information about this role, see Manage mobile devices with Configuration Manager
and Exchange.

Fallback status point
A site system role that helps you monitor client installation. It identifies clients that are
unmanaged because they can't communicate with their management point. Although
this role is supported only at primary sites, you can install multiple instances of this role
at a site, and at multiple sites in the same hierarchy.

Management point
A site system role that provides policy and service location information to clients. It also
receives configuration data from clients.

By default, this role installs on the site server when you install a new primary or
secondary site. Primary sites support multiple instances of this role. Secondary sites
support a single management point. Also referred to as a proxy management point, this
role at a secondary site provides a local point of contact for clients to obtain computer
and user policies.

Set up management points to support either HTTP or HTTPs. They can also support
mobile devices that you manage with Configuration Manager on-premises mobile
device management (MDM). To help reduce the processing load placed on the site
database server by management points as they service requests from clients, use
Database replicas for management points.

  ） Important

  Starting in Configuration Manager version 2103, sites that allow HTTP client
  communication are deprecated. Configure the site for HTTPS or Enhanced HTTP.
  For more information, see Enable the site for HTTPS-only or enhanced HTTP.

Reporting services point
A site system role that integrates with SQL Server Reporting Services to create and
manage reports for Configuration Manager. This role is supported at primary sites and
the central administration site, and you can install multiple instances of this role at a
supported site. For more information, see Planning for reporting.

<!-- p.388 -->

Service connection point
A site system role that uploads usage data from your site, and is required to make
updates for Configuration Manager available in the console. A hierarchy only supports a
single instance of this role, and that must be at the top-tier site of your hierarchy. If you
expand a standalone primary site into a larger hierarchy, uninstall this role from the
primary site, and then install it at the central administration site. For more information,
see About the service connection point.

Software update point
A site system role that integrates with Windows Server Update Services (WSUS) to
provide software updates to Configuration Manager clients. This role is supported at all
sites:

         Install this site system at the central administration site to synchronize with WSUS.

         Set up each instance of this role at child primary sites to synchronize with the
         central administration site.

         When data transfer across the network is slow, consider installing a software
         update point in secondary sites.

For more information, see Plan for software updates.

State migration point
When you migrate a computer to a new operating system, this site system role stores
user state data. This role is supported at primary sites and at secondary sites. Install
multiple instances of this role at a site, and at multiple sites in the same hierarchy. For
more information about storing user state when you deploy an OS, see Manage user
state.

Next steps
Some Configuration Manager site system roles require connections to the internet. If
your environment requires internet traffic to use a proxy server, configure these site
system roles to use the proxy. For more information, see Proxy server support.

Feedback

<!-- p.389 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.390 -->

Fundamental concepts for content
management in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager supports a robust system of tools and options to manage
software content. Software deployments such as applications, packages, software
updates, and OS deployments all need content. Configuration Manager stores the
content on both site servers and distribution points. This content requires a large
amount of network bandwidth when it's being transferred between locations. To plan
and use the content management infrastructure effectively, first understand the
available options and configurations. Then consider how to use them to best fit your
networking environment and content deployment needs.

   Tip

  For more information about the content distribution process and to find help in
  diagnosing and resolving general content distribution problems, see
  Understanding and Troubleshooting Content Distribution in Microsoft
  Configuration Manager       .

The following sections are key concepts for content management. When a concept
requires additional or complex information, links are provided to direct you to those
details.

Accounts used for content management
The following accounts can be used with content management:

Network access account
Used by clients to connect to a distribution point and access content. If allowed, the
client first tries anonymous authentication. Then it tries Windows-integrated
authentication with the computer account or network access account. For more
information, see Client to distribution point communication.

This account is also used by pull-distribution points to download content from a source
distribution point in a remote forest.

<!-- p.391 -->

Some scenarios no longer require a network access account. You can enable the site to
use Enhanced HTTP with Microsoft Entra authentication.

For more information, see Network access account.

Package access account
By default, Configuration Manager grants access to content on a distribution point to
the generic access accounts Users and Administrators. However, you can configure
additional permissions to restrict access.

For more information, see Package access account.

Bandwidth throttling and scheduling
Both throttling and scheduling are options that help you control when content is
distributed from a site server to distribution points. These capabilities are similar to, but
not directly related to bandwidth controls for site-to-site file-based replication.

For more information, see Manage network bandwidth.

Binary differential replication
Configuration Manager uses binary differential replication (BDR) to update content that
you previously distributed to other sites or to remote distribution points. To support
BDR's reduction of bandwidth usage, install the Remote Differential Compression
feature on distribution points. For more information, see Distribution point
prerequisites.

BDR minimizes the network bandwidth used to send updates for distributed content. It
resends only the new or changed content instead of sending the entire set of content
source files each time you change those files.

When BDR is used, Configuration Manager identifies the changes that occur to source
files for each set of content that you previously distributed.

     When files in the source content change, the site creates a new incremental version
     of the content. It then replicates only the changed files to destination sites and
     distribution points. A file is considered changed if you renamed or moved it, or if
     you changed the contents of the file. For example, if you replace a single driver file
     for a driver package that you previously distributed to several sites, only the
     changed driver file is replicated.

<!-- p.392 -->

     Configuration Manager supports up to five incremental versions of a content set
     before it resends the entire content set. After the fifth update, the next change to
     the content set causes the site to create a new version of the content set.
     Configuration Manager then distributes the new version of the content set to
     replace the previous set and any of its incremental versions. After the new content
     set is distributed, later incremental changes to the source files are again replicated
     by BDR.

BDR is supported between each parent and child site in a hierarchy. BDR is supported
within a site between the site server and its regular distribution points. However, pull-
distribution points and content-enabled cloud management gateways don't support
BDR to transfer content. Pull-distribution points support file-level deltas, transferring
new files, but not blocks within a file.

Applications always use binary differential replication. BDR is optional for packages and
isn't enabled by default. To use BDR for packages, enable this functionality for each
package. Select the option Enable binary differential replication when you create or
edit a package.

BDR or delta replication
The following lists summarize the differences between binary differential replication
(BDR) and delta replication.

Summary of binary differential replication
     Configuration Manager's term for Windows Remote Differential Compression
     Block-level differences
     Always enabled for apps
     Optional on legacy packages
     If a file already exists on the distribution point, and there's a change, the site uses
     BDR to replicate the block-level change instead of the entire file. This behavior
     only applies when you enable the object to use BDR.

Summary of delta replication

     File-level differences
     On by default, not configurable
     When a package changes, the site checks for changes to the individual files instead
     of the entire package.
        If a file changes, use BDR to do the work

<!-- p.393 -->

           If there's a new file, copy the new file

Peer caching technologies
Configuration Manager supports several options for managing content between peer
devices on the same network:

     BranchCache
     Delivery Optimization
     Configuration Manager peer cache

Use the following table to compare major features of these technologies:

                                                                              ﾉ   Expand table

 Feature             Peer cache                 Delivery Optimization       BranchCache

 Across subnets      Yes                        Yes                         No

 Throttle            Yes (BITS)                 Yes (native)                Yes (BITS)
 bandwidth

 Partial content     Yes                        Yes                         Yes

 Control cache       Yes                        Yes                         Yes
 size on disk

 Peer source         Manual (client setting)    Automatic                   Automatic
 discovery

 Peer discovery      Via management point       DO cloud service            Broadcast
                     using boundary groups

 Reporting           Client data sources        Client data sources         Client data sources
                     dashboard                  dashboard                   dashboard

 WAN usage           Boundary groups            DO GroupID                  Subnet only
 control

 Supported           All ConfigMgr content      Windows updates, drivers,   All ConfigMgr
 content                                        store apps                  content

 Policy control      Client agent settings      Client agent settings       Client agent
                                                (partial)                   settings

Recommendations

<!-- p.394 -->

     Modern management: If you're already using modern tools such as Intune,
     implement Delivery Optimization

     Configuration Manager and co-management: Use a combination of peer cache
     and Delivery Optimization. Use peer cache with on-premises distribution points,
     and use Delivery Optimization for cloud scenarios.

     Existing BranchCache implemented: Use all three technologies in parallel. Use peer
     cache and Delivery Optimization for scenarios that aren't supported by
     BranchCache.

BranchCache
BranchCache is a Windows technology. Clients that support BranchCache, and have
downloaded a deployment that you configure for BranchCache, then serve as a content
source to other BranchCache-enabled clients.

For example, you have a distribution point that runs Windows Server 2012 or later, and
is configured as a BranchCache server. When the first BranchCache-enabled client
requests content from this server, the client downloads that content and caches it.

     That client then makes the content available for additional BranchCache-enabled
     clients on the same subnet that also cache the content.
     Other clients on the same subnet don't have to download content from the
     distribution point.
     The content is distributed across multiple clients for future transfers.

For more information, see Support for Windows BranchCache.

Delivery Optimization
You use Configuration Manager boundary groups to define and regulate content
distribution across your corporate network and to remote offices. Windows Delivery
Optimization is a cloud-based, peer-to-peer technology to share content between
Windows 10 or later devices. Configure Delivery Optimization to use your boundary
groups when sharing content among peers. Client settings apply the boundary group
identifier as the Delivery Optimization group identifier on the client. When the client
communicates with the Delivery Optimization cloud service, it uses this identifier to
locate peers with the content. For more information, see delivery optimization client
settings.

<!-- p.395 -->

Delivery Optimization is the recommended technology to optimize Windows update
delivery of express installation files for Windows quality updates. Internet access to the
Delivery Optimization cloud service is a requirement to utilize its peer-to-peer
functionality. For information about the needed internet endpoints, see Frequently
asked questions for Delivery Optimization. Optimization can be used for all Windows
updates. For more information, see optimize Windows update delivery.

Microsoft Connected Cache
You can install a Microsoft Connected Cache server on your distribution points. By
caching this content on-premises, your clients can benefit from the Delivery
Optimization feature, but you can help to protect WAN links.

  ７ Note

  This feature was previously known as Delivery Optimization In-Network Cache.

This cache server acts as an on-demand transparent cache for content downloaded by
Delivery Optimization. Use client settings to make sure this server is offered only to the
members of the local Configuration Manager boundary group.

This cache is separate from Configuration Manager's distribution point content. If you
choose the same drive as the distribution point role, it stores content separately.

For more information, see Microsoft Connected Cache with Configuration Manager.

Peer cache
Client peer cache helps you manage deployment of content to clients in remote
locations. Peer cache is a built-in Configuration Manager solution that enables clients to
share content with other clients directly from their local cache.

First deploy client settings that enable peer cache to a collection. Then members of that
collection can act as a peer content source for other clients in the same boundary
group.

Client peer cache sources can divide content into parts. These parts minimize the
network transfer to reduce WAN utilization. The management point provides more
detailed tracking of the content parts. It tries to eliminate more than one download of
the same content per boundary group.

For more information, see Peer cache for Configuration Manager clients.

<!-- p.396 -->

Windows PE peer cache
When you deploy a new OS with Configuration Manager, computers that run the task
sequence can use Windows PE peer cache. They download content from a peer cache
source instead of from a distribution point. This behavior helps minimize WAN traffic in
branch office scenarios where there's no local distribution point.

For more information, see Windows PE peer cache.

Windows LEDBAT
Windows Low Extra Delay Background Transport (LEDBAT) is a network congestion
control feature of Windows Server to help manage background network transfers. For
distribution points running on supported versions of Windows Server, enable an option
to help adjust network traffic. Then clients only use network bandwidth when it's
available.

For more information on Windows LEDBAT in general, see the New transport
advancements       blog post.

For more information on how to use Windows LEDBAT with Configuration Manager
distribution points, see the setting to Adjust the download speed to use the unused
network bandwidth (Windows LEDBAT) when you Configure the general settings of a
distribution point.

  ７ Note

  Staring in Configuration Manager version 2203, you can use LEDBAT with your
  software update points. If a site system has both the distribution point and
  software update point roles, you can configure LEDBAT independently on the roles.
  For more information, see the setting Adjust the download speed to use the
  unused network bandwidth (Windows LEDBAT) setting for Installing software
  update points.

Client locations
The following are locations that clients access content from:

     Intranet (on-premises):

        Distribution points can use HTTP or HTTPs.

<!-- p.397 -->

        Only use a content-enabled cloud management gateway for fallback when on-
        premises distribution points aren't available.

     Internet:

        Requires internet-facing distribution points to accept HTTPS.

        Can use a content-enabled cloud management gateway.

     Workgroup:

        Requires distribution points to accept HTTPS.

        Can use a content-enabled cloud management gateway.

Content source priority
When a client needs content, it makes a content location request to the management
point. The management point returns a list of source locations that are valid for the
requested content. This list varies depending upon the specific scenario, technologies in
use, site design, boundary groups, and deployment settings. For example, when a task
sequence runs, the full Configuration Manager client isn't always running, so the
behaviors may differ.

The following list contains all of the possible content source locations that the
Configuration Manager client can use, in the order in which it prioritizes them:

   1. The distribution point on the same computer as the client
   2. A peer source in the same network subnet
   3. A distribution point in the same network subnet
   4. A peer source in the same boundary group
   5. A distribution point in the current boundary group
   6. A distribution point in a neighbor boundary group configured for fallback
   7. A distribution point in the default site boundary group
   8. The Windows Update cloud service
   9. An internet-facing distribution point
 10. A content-enabled cloud management gateway in Azure

Delivery Optimization isn't applicable to this source prioritization. This list is how the
Configuration Manager client finds content. The Windows Update Agent downloads
content for Delivery Optimization. If the Windows Update Agent can't find the content,
then the Configuration Manager client uses this list to search for it.

<!-- p.398 -->

BranchCache applies to this list only when you enable a distribution point for
BranchCache. For example, if a client gets to option #3 in the prioritization list, it first
asks the distribution point for BranchCache metadata. The BranchCache-enabled
distribution point is what provides the client information for BranchCache peer
discovery. The client will download content from a BranchCache peer if it can. If it can't
download the content via BranchCache, it then tries the distribution point itself, before
continuing down the list of content sources. This behavior applies at any point in the
priority list where the client uses a BranchCache-enabled distribution point.

The configuration of boundary group options can modify the sort order of this priority
list.

Content library
The content library is the single-instance store of content in Configuration Manager.
This library reduces the overall size of content that you distribute.

        Learn more about the content library.
        Use the content library cleanup tool to remove content that is no longer
        associated with an application.

Distribution points
Configuration Manager uses distribution points to store files that are required for
software to run on client computers. Clients must have access to at least one
distribution point from which they can download the files for content that you deploy.

The basic (non-specialized) distribution point is commonly referred to as a standard
distribution point. There are two variations on the standard distribution point that
receive special attention:

        Pull-distribution point: A variation of a distribution point where the distribution
        point obtains content from another distribution point (a source distribution point).
        This process is similar to how clients download content from distribution points.
        Pull-distribution points can help you avoid network bandwidth bottlenecks that
        occur when the site server must directly distribute content to each distribution
        point. For more information, see Use a pull-distribution point.

        Content-enabled cloud management gateway: A variation of a distribution point
        that's installed on Microsoft Azure. For more information, see Cloud management
        gateway overview.

<!-- p.399 -->

Standard distribution points support a range of configurations and features:

     Use controls such as schedules or bandwidth throttling to help control this
     transfer.

     Use other options, including prestaged content, and pull-distribution points to
     minimize and control network consumption.

     BranchCache, peer cache, and Delivery Optimization are peer-to-peer
     technologies to reduce the network bandwidth that's used when you deploy
     content.

     There are different configurations for OS deployments, such as PXE and Multicast

     Options for mobile devices

Cloud and pull distribution points support many of these same configurations, but have
limitations that are specific to each distribution point variation.

Distribution point groups
Distribution point groups are logical groupings of distribution points that can simplify
content distribution.

For more information, see Manage distribution point groups.

Distribution point priority
The distribution point priority value is based on how long it took to transfer previous
deployments to that distribution point.

     This value is self-tuning. It's set on each distribution point to help Configuration
     Manager more quickly transfer content to more distribution points.

     When you distribute content to multiple distributions points at the same time, or
     to a distribution point group, the site first sends the content to the server with the
     highest priority. Then it sends that same content to a distribution point with a
     lower priority.

     Distribution point priority doesn't replace the distribution priority for packages.
     Package priority remains the deciding factor of when the site sends different
     content.

<!-- p.400 -->

For example, you have a package that has a high package priority. You distribute it to a
server with a low distribution point priority. This high priority package always transfers
before a package that has a lower priority. The package priority applies even if the site
distributes lower priority packages to servers with higher distribution point priorities.

The high priority of the package ensures that Configuration Manager distributes that
content to distribution points before it sends any packages with a lower priority.

  ７ Note

  Pull-distribution points also use a concept of priority to order the sequence of their
  source distribution points.

        The distribution point priority for content transfers to the server is distinct
        from the priority that pull-distribution points use. Pull-distribution points use
        their priority when they search for content from a source distribution point.
        For more information, see Use a pull-distribution point.

Fallback
Several things have changed with Configuration Manager current branch in the way that
clients find a distribution point that has content, including fallback.

Clients that can't find content from a distribution point that's associated with their
current boundary group fall back to use content source locations associated with
neighbor boundary groups. To be used for fallback, a neighbor boundary group must
have a defined relationship with the client's current boundary group. This relationship
includes a configured time that must pass before a client that can't find content locally
includes content sources from the neighbor boundary group as part of its search.

The concepts of preferred distribution points are no longer used, and settings for Allow
fallback source locations for content are no longer available or enforced.

For more information, see Boundary groups.

Network bandwidth
To help manage the amount of network bandwidth that's used when you distribute
content, you can use the following options:
