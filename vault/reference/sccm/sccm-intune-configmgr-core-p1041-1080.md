---
title: "Core infrastructure documentation — pages 1041-1080"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1041-1080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1041-1080
family: sccm
documentKind: "doc"
abstract: "Management point On the General tab, set up the site to publish information about its management points to Active Directory Domain Services. Configuration Manager clients use management points to locate services, and to find site information such as boundary group membership and"
---

# Core infrastructure documentation — pages 1041-1080

<!-- p.1041 -->

Management point
On the General tab, set up the site to publish information about its management points
to Active Directory Domain Services.

Configuration Manager clients use management points to locate services, and to find
site information such as boundary group membership and PKI certificate selection
options. Clients also use management points to find other management points in the
site, and distribution points from which to download software. Management points also
help clients to complete site assignment, and to download client policy and upload
client information.

The most secure method for clients to find management points is to publish them in
Active Directory Domain Services. This service location method requires the following to
be true:

     The schema is extended for Configuration Manager.
     There's a System Management container, with appropriate security permissions
     for the site server to publish to this container.
     The Configuration Manager site is set up to publish to Active Directory Domain
     Services.
     Clients belong to the same Active Directory forest as the site server's forest.

When clients on the intranet can't use Active Directory Domain Services to find
management points, use DNS publishing. This article also describes the option to
Publish selected intranet management points in DNS.

For general information about service location, see Understand how clients find site
resources and services.

Automate management point site component with PowerShell
To programmatically view and configure the Management point site component, use
the following PowerShell cmdlets:

     Get-CMManagementPointComponent
     Set-CMManagementPointComponent

Status reporting
These settings directly set up the level of detail that's included in status reports from
sites and clients.

<!-- p.1042 -->

Automate status reporting site component with PowerShell
To programmatically view and configure the Status reporting site component, use the
following PowerShell cmdlets:

      Get-CMStatusReportingComponent
      Set-CMStatusReportingComponent

Email notification
Specify account and email server details to enable Configuration Manager to send email
notifications for alerts.

For more information, see Configure alerts.

Automate email notification site component with PowerShell
To programmatically view and configure the Email notification site component, use the
following PowerShell cmdlets:

      Get-CMEmailNotificationComponent
      Set-CMEmailNotificationComponent

Collection membership evaluation
Use this component to set how often collection membership is incrementally evaluated.
Incremental evaluation updates a collection membership with only new or changed
resources.

For more information, see Best practices for collections.

Automate collection membership evaluation site component with
PowerShell

To programmatically view and configure the Collection membership evaluation site
component, use the following PowerShell cmdlets:

      Get-CMCollectionMembershipEvaluationComponent
      Set-CMCollectionMembershipEvaluationComponent

Configuration Manager Service Manager

<!-- p.1043 -->

You can use the Service Manager to control Configuration Manager services, and to view
the status of any Configuration Manager service or working thread. These services and
threads are referred to collectively as Configuration Manager components.

     Components can run on any site system.

     Manage components the same way that you manage services in Windows. The
     following actions apply to Configuration Manager components:
        Start
        Stop
        Pause
        Resume
        Query

A Configuration Manager service runs when there's something for it to do. For example,
when a configuration file is written to a component's inbox.

Use Service Manager
   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     System Status, and select the Component Status node.

   2. In the Component group of the ribbon, select Start, and then choose
     Configuration Manager Service Manager.

   3. When the Configuration Manager Service Manager opens, connect to the site that
     you want to manage.

     If you don't see the site that you want to manage, go to the Site menu, and select
     Connect. Then enter the name of the site server of the correct site.

   4. Expand the site and navigate to Components or Servers, depending on the
     location of the components that you want to manage.

   5. In the right pane, select one or more components. Then on the Component menu,
     select Query to update the status of your selection.

   6. After it updates the status of the component, use one of the four action-based
     options on the Component menu. Use these actions to modify the component's
     operation. After you request an action, query the component again to display the
     new status of the component.

   7. Close the Configuration Manager Service Manager when you're finished modifying
     the operational status of components.

<!-- p.1044 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1045 -->

Publish site data for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you extend the Active Directory schema for Configuration Manager, you can
publish Configuration Manager sites to Active Directory Domain Services (AD DS). This
lets Active Directory computers securely retrieve site information from a trusted source.
Although publishing site information to AD DS is not required for basic Configuration
Manager functionality, it can reduce administrative overhead to do so.

      When a site is configured to publish to AD DS, Configuration Manager clients can
      automatically find management points through Active Directory publishing. They
      use an LDAP query to a global catalog server.

      When a site does not publish to AD DS, clients must have an alternative
      mechanism to locate their default management point.

For information about how clients find a management point, see Understand how
clients find site resources and services for Configuration Manager.

Configure sites to publish to AD DS
The following are the high-level steps:

      You must extend the Active Directory schema for Configuration Manager in each
      forest where you will publish site data. Also ensure the System Management
      container is present.

      You must grant the computer account of each primary site that will publish data
      full control to the System Management container, and all of its child objects.

To enable a Configuration Manager site to publish site
information to Active Directory forest
   1. In the Configuration Manager console, click Administration.

   2. In the Administration workspace, expand Site Configuration, and click Sites. Select
      the site that you want to have publish its site data. Then on the Home tab, in the
      Properties group, click Properties.

<!-- p.1046 -->

  3. On the Publishing tab of the site's properties, select the forests to which this site
    will publish site data.

  4. Click OK to save the configuration.

To set up Active Directory forests for publishing
  1. In the Configuration Manager console, click Administration.

  2. In the Administration workspace, expand Hierarchy Configuration, and click
    Active Directory Forests. If Active Directory Forest Discovery has previously run,
    you see each discovered forest in the results pane. The local forest and any trusted
    forests are discovered when Active Directory Forest Discovery runs. Only untrusted
    forests must be manually added.

          To set up a previously discovered forest, select the forest in the results pane.
          Then on the Home tab, in the Properties group, click Properties to open the
          forest properties. Continue with step 3.

          To set up a new forest that is not listed, on the Home tab, in the Create
          group, click Add Forest to open the Add Forests dialog box. Continue with
          step 3.

  3. On the General tab, complete configurations for the forest that you want to
    discover, and specify the Active Directory Forest Account.

       ７ Note

       Active Directory Forest Discovery requires a global account to discover and
       publish to untrusted forests. If you do not use the computer account of the
       site server, you can only select a global account.

  4. If you plan to allow sites to publish site data to this forest, on the Publishing tab,
    complete configurations for publishing to this forest.

       ７ Note

       If you enable sites to publish to a forest, you must extend the Active Directory
       schema of that forest for Configuration Manager. The Active Directory Forest
       Account must have Full Control permissions to the System container in that
       forest.

<!-- p.1047 -->

   5. When you complete the configuration of this forest for use with Active Directory
     Forest Discovery, click OK to save the configuration.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1048 -->

Manage content and content
infrastructure for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you are ready to set up and then manage your content management
infrastructure for Configuration Manager, use the information in the following topics:

      Install and configure distribution points for Configuration Manager. Before you can
      deploy content, you must install and set up distribution points. Then you can set
      up distribution point groups to help simplify management of content across your
      infrastructure. The information in this topic can help you complete these tasks, and
      details the deep and varied settings supported by individual distribution points.

      Deploy and manage content for Configuration Manager. Content deployment
      transfers files and software to distribution point servers throughout your network.
      In addition to a simple transfer, you can prestage content, which is a method that
      can help you avoid excessive use of network bandwidth. The information in this
      topic can help you with the basic tasks of sending that content or using pre-staged
      content effectively.

      Monitor content you have distributed with Configuration Manager. As you deploy
      content, you can monitor its status across your infrastructure. You can also
      redistribute content that fails to reach distribution points, or cancel distributions
      that remain in progress. The information in this topic helps you understand how to
      monitor your content, including how to fix some problems when the transfer of
      content fails.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1049 -->

Install and configure distribution points in
Configuration Manager
07/17/2025

Applies to: Configuration Manager (current branch)

Install Configuration Manager distribution points to host the content files that you deploy to
devices and users. Create distribution point groups to simplify how you manage distribution
points, and how you distribute content to distribution points.

You install a new distribution point by using the installation wizard. For more information, see
Install a distribution point. To manage the properties of an existing distribution point, edit the
properties of the distribution point. For more information, see Configure a distribution point.

Configure most of the distribution point settings with either method. A few settings are
available only when you're either installing or editing, but not both:

     Settings that are available only when you're installing a distribution point:

        Allow Configuration Manager to install IIS on the distribution point computer

        Configure drive space settings for the distribution point

     Settings that are available only when you're editing the properties of a distribution point:

        Manage distribution point group relationships

        View Content deployed to the distribution point

        Configure Rate limits for data transfers to distribution points

        Configure Schedules for data transfers to distribution points

Install a distribution point
Before you can make content available to clients, choose a site system server as a distribution
point. Assign each distribution point to at least one boundary group. Add the distribution point
role to a new server, or add it to an existing server.

Prerequisites
When you install a new distribution point, you use an installation wizard that walks you
through the available settings. Before you start, consider the following prerequisites:

<!-- p.1050 -->

     You must have the following security permissions to create and configure a distribution
     point:

        Read for the Distribution Point object

        Copy to Distribution Point for the Distribution Point object

        Modify for the Site object

        Manage Certificates for Operating System Deployment for the Site object

     Install Internet Information Services (IIS) on the Windows server that hosts the distribution
     point. Or, when you install the site system role, Configuration Manager can install and
     configure IIS for you.

   Tip

  To prevent Configuration Manager from installing on a specific drive, create an empty file
  named NO_SMS_ON_DRIVE.SMS and copy it to the root folder of the drive before you
  install the distribution point.

Procedure to install a distribution point
Use this procedure to add a new distribution point. To change the configuration of an existing
distribution point, see the Configure a distribution point section.

Start with the general procedure to Install site system roles. Select the Distribution point role
on the System Role Selection page of the Create Site System Server wizard. This action adds
the following pages to the wizard:

     Distribution point
     Communication
     Drive Settings
     Pull Distribution Point
     PXE Settings
     Multicast
     Content Validation
     Boundary Groups

  ） Important

  The following settings are available only when you're installing a distribution point:

<!-- p.1051 -->

        Allow Configuration Manager to install IIS on the distribution point computer

        Configure drive space settings for the distribution point

For more information on the pages of the wizard specific to the distribution point role, see the
Configure a distribution point section. For example, if you want to install the distribution point
as a pull-distribution point, choose the option to Enable this distribution point to pull content
from other distribution points. Then make the other configurations that pull-distribution
points require.

After you finish the Create Site System Server wizard, the site adds the distribution point role to
the site system server.

  ７ Note

  You can use PowerShell to automate the installation of a distribution point. For more
  information, see Add-CMDistributionPoint.

To help you troubleshoot, review the following log files on the site server:

     distmgr.log
     SMSdpmon.log

For more information, see Log file reference.

Manage distribution point groups
Distribution point groups provide a logical grouping of distribution points for content
distribution. Use these groups to manage and monitor content from a central location for
distribution points that span multiple sites. Keep the following point in mind:

     Add one or more distribution points from any site in the hierarchy to a distribution point
     group.

     Add a distribution point to more than one distribution point group.

     When you distribute content to a distribution point group, Configuration Manager
     distributes the content to all distribution points that are members of the group.

     If you add a distribution point to the group after an initial content distribution,
     Configuration Manager automatically distributes the content to the new distribution
     point member.

<!-- p.1052 -->

     Associate a collection with a distribution point group. When you distribute content to that
     collection, Configuration Manager determines which groups are associated with the
     collection. It then distributes the content to all distribution points that are members of
     those groups.

          ７ Note

          After you distribute content to a collection, if you then associate the collection with a
          new distribution point group, you must redistribute the content to the collection
          before the content is distributed to the new distribution point group.

The next sections list the procedures for the following actions to manage distribution point
groups:

     Create and configure a new distribution point group
     Modify an existing distribution point group
     Add selected distribution points to existing distribution point groups

Procedure to create and configure a new distribution point
group
   1. In the Configuration Manager console, go to the Administration workspace, and select
     the Distribution Point Groups node.

   2. In the ribbon, select Create Group.

   3. In the Create New Distribution Point Group window, enter the Name, and optionally a
     Description for the group.

   4. On the Members tab, select Add.

   5. In the Add Distribution Points window, select one or more distribution points to add as
     members of the group. Then choose OK.

   6. If necessary, switch to the Collections tab of the Create New Distribution Point Group
     window, and select Add.

   7. In the Select Collections window, select the collections to associate with the distribution
     point group, and then choose OK.

   8. In the Create New Distribution Point Group window, choose OK to create the group.

  ７ Note

<!-- p.1053 -->

  You can use PowerShell to automate this process. For more information, see New-
  CMDistributionPointGroup.

Create a new group from an existing distribution point

  1. In the Configuration Manager console, go to the Administration workspace, and select
     the Distribution Points node. Select one or more distribution points to add to a new
     distribution point group.

  2. In the ribbon, select Add Selected Items, and then select Add Selected Items to New
     Distribution Point Group.

This process automatically populates the Members tab of the Create New Distribution Point
Group window with the selected servers.

Procedure to modify an existing distribution point group
  1. In the Configuration Manager console, go to the Administration workspace, and select
     the Distribution Point Groups node.

  2. Select an existing distribution point group to modify. In the ribbon, select Properties.

  3. To associate new collections with this group, switch to the Collections tab, and choose
     Add. Select the collections, and then choose OK.

  4. To add new distribution points to this group, switch to the Members tab, and choose
     Add. Select the distribution points, and then choose OK.

  5. Choose OK to save changes to the distribution point group.

  ７ Note

  You can use PowerShell to automate this process. For more information, see Set-
  CMDistributionPointGroup.

Procedure to add selected distribution points to existing
distribution point groups
  1. In the Configuration Manager console, go to the Administration workspace, and select
     the Distribution Points node. Select one or more distribution points to add to an existing
     group.

<!-- p.1054 -->

   2. In the ribbon, select Add Selected Items, and then select Add Selected Items to Existing
     Distribution Point Groups.

   3. In the Available distribution point groups, select the groups to which the selected
     distribution points are added as members. Then choose OK.

  ７ Note

  You can use PowerShell to automate this process. For more information, see Add-
  CMDistributionPointToGroup.

Reassign a distribution point
Many customers have large Configuration Manager infrastructures, and are reducing primary
or secondary sites to simplify their environment. They still need to keep distribution points at
branch office locations to serve content to managed clients. These distribution points often
contain multiple terabytes or more of content. This content is costly for time and network
bandwidth to distribute to these remote servers.

This feature lets you reassign a distribution point to another primary site without redistributing
the content. The distribution point's current site can be either a primary or secondary site. This
action updates the site system assignment while persisting all of the content on the server. If
you need to reassign multiple distribution points, first do this action on a single distribution
point. Then continue with other servers one at a time.

  ） Important

  The target server can only host the distribution point role. If the site system server hosts
  another Configuration Manager server role, such as the state migration point, you can't
  reassign the distribution point. You can't reassign a cloud management gateway.

Before reassigning a distribution point, add the computer account of the destination site server
to the local Administrator group on the target distribution point server.

Follow these steps to reassign a distribution point:

   1. In the Configuration Manager console, connect to the central administration site.

   2. Go to the Administration workspace, and select the Distribution Points node.

   3. Right-click the target distribution point, and select Reassign Distribution Point.

<!-- p.1055 -->

   4. Select the target site server and site code to which you want to reassign this distribution
     point.

Monitor the reassignment similarly as when you add a new role. The simplest method is to
refresh the console view after several minutes. Add the site code column to the view. This value
changes when Configuration Manager reassigns the server. If you try to do another action on
the target server before you refresh the console view, an "object not found" error occurs.
Ensure the process is complete and refresh the console view before starting any other actions
on the server.

After reassigning a distribution point, refresh the server's certificate. The new site server needs
to re-encrypt this certificate using its public key and store it in the site database. For more
information, see the Create a self-signed certificate or import a public key infrastructure (PKI)
client certificate for the distribution point setting on the General tab of the distribution point
properties.

     For PKI certificates, you don't need to create a new certificate. Import the same .PFX and
     enter the password.

     For self-signed certificates, adjust the expiration date or time to update it.

     If you don't refresh the certificate, the distribution point still serves content, but the
     following functions fail:

        Content validation messages (the distmgr.log shows that it can't decrypt the
        certificate)

        PXE support for clients

Tips
     Do this action from the central administration site. This practice helps with replication to
     the primary sites.

     Don't distribute content to the target server and then attempt to reassign it. Distribute
     content tasks that are in progress may fail during the reassignment process, but it retries
     per normal.

     If the server is also a Configuration Manager client, make sure to also reassign the client
     to the new primary site. This step is especially critical for pull-distribution points, which
     use client components to download content.

     This process removes the distribution point from the old site's default boundary group.
     You need to manually add it to the new site's default boundary group, if necessary. All

<!-- p.1056 -->

     other boundary group assignments remain the same.

  ７ Note

  You can use PowerShell to automate this process. For more information, see the
  ReassignSiteCode parameter of the Set-CMDistributionPoint cmdlet.

Maintenance mode
You can set a distribution point in maintenance mode. Enable maintenance mode when you're
installing software updates, or making hardware changes to the server.

While the distribution point is in maintenance mode, it has the following behaviors:

     The site doesn't distribute any content to it.

     Management points don't return the location of this distribution point to clients.

     When you update the site, a distribution point in maintenance mode still updates.

     The distribution point properties are read-only. For example, you can't change the
     certificate or add boundary groups.

     Any scheduled task, like content validation, still runs on the same schedule.

Be careful about enabling maintenance mode on more than one distribution point. This action
may cause a performance impact to your other distribution points. Depending upon your
boundary group configurations, clients may have increased download times or be unable to
download content.

Maintenance mode shouldn't be a long-term state for any distribution point. For any actions
with a long duration, consider first removing the distribution point role.

  ７ Note

  While a distribution point is in maintenance mode, don't do the following actions:

        Remove role
        Reassign distribution point

Enable maintenance mode

<!-- p.1057 -->

To put a distribution point in maintenance mode, your user account requires the Modify
permission on the Site class. For example, the Infrastructure Administrator and Full
Administrator built-in roles have this permission.

   1. In the Configuration Manager console, go to the Administration workspace.

   2. Select the Distribution Points node.

   3. Select the target distribution point, and choose Enable maintenance mode from the
     ribbon.

To view the current state of the distribution points, add the "Maintenance mode" column to the
Distribution Points node in the console.

For more information on automating this process with the Configuration Manager SDK, see
SetDPMaintenanceMode method in class SMS_DistributionPointInfo.

Configure a distribution point
Individual distribution points support different kinds of configurations. However, not all
distribution point types support all configurations. For example, cloud management gateways
don't support PXE- or multicast-enabled deployments. For more information about specific
limitations, see the following articles:

     Supported configurations for cloud management gateway

     Use a pull-distribution point

The following sections describe the distribution point configurations when you're installing a
new one or editing an existing one:

     General settings
     Communication
     Drive Settings
     Firewall Settings
     Pull Distribution Point
     PXE Settings
     Multicast
     Content Validation
     Boundary Groups

Procedure to change a distribution point

<!-- p.1058 -->

   1. In the Configuration Manager console, go to the Administration workspace, and select
     the Distribution Points node.

   2. Select the distribution point to configure. In the ribbon, choose Properties.

   3. Use the information in the following sections when you're editing the properties of the
     distribution point.

   4. After you make the changes that you want, select OK to save your settings and close the
     distribution point properties.

  ７ Note

  You can use PowerShell to automate this process. For more information, see Set-
  CMDistributionPoint.

General
The following settings are on the Distribution point page of the Create Site System Server
wizard, and the General tab of the distribution point properties window:

     Description: An optional description for this distribution point role.

     Install and configure IIS if required by Configuration Manager: If IIS isn't already
     installed on the server, Configuration Manager installs and configures it. Configuration
     Manager requires IIS on all distribution points. If you don't choose this setting, and IIS
     isn't installed on the server, first install IIS before Configuration Manager can successfully
     install the distribution point.

       ７ Note

       This option is only on the Distribution point page of the Create Site System Server
       wizard. It's available only when you're installing a new distribution point.

     Enable and configure BranchCache for this distribution point: Choose this setting to let
     Configuration Manager configure Windows BranchCache on the distribution point server.
     For more information, see BranchCache.

     Adjust the download speed to use the unused network bandwidth (Windows LEDBAT):
     Enable distribution points to use network congestion control. For more information, see
     Windows LEDBAT. Minimum requirements for LEDBAT support:
        Windows Server, version 1709 or later

<!-- p.1059 -->

        Windows Server 2016 with the following updates:
           Cumulative update KB4132216, released June 21, 2018, or a later cumulative update.
           Servicing stack update KB4284833, released May 18, 2018, or a later servicing stack
           update.
        Windows Server 2019

     Enable this distribution point for prestaged content: This setting enables you to add
     content to the server before you distribute software. Because the content files are already
     in the content library, they don't transfer over the network when you distribute the
     software. For more information, see Prestaged content.

     Enable this distribution point to be used as Microsoft Connected Cache server: Use this
     option to install a Microsoft Connected Cache server on your distribution point. By
     caching this content on-premises, your clients can benefit from the Delivery Optimization
     feature, but you can help to protect WAN links. For more information, including
     description of the other settings, see Microsoft Connected Cache with Configuration
     Manager.

Communication
The following settings are on the Communication page of the Create Site System Server wizard
and the distribution point properties window:

     Configure how client devices communicate with the distribution point: There are
     advantages and disadvantages to using HTTP or HTTPS. For more information, see
     Security guidance for content management.

     Allow clients to connect anonymously: This setting specifies whether the distribution
     point allows anonymous connections from Configuration Manager clients to the content
     library.

     Create a self-signed certificate or import a PKI client certificate: Configuration Manager
     uses this certificate for the following purposes:

        It authenticates the distribution point to a management point before the distribution
        point sends status messages.

        When you Enable PXE support for clients on the PXE Settings page, the distribution
        point sends it to computers that PXE boot. These computers then use it to connect to a
        management point during the OS deployment process.

        When you configure all your management points in the site for HTTP, select the option
        to Create self-signed certificate. When you configure the management points for

<!-- p.1060 -->

        HTTPS, use the option to Import certificate from PKI. In other words, don't use self-
        signed certificates on distribution points when management points use certificates.
        Issues may occur otherwise. For example, distribution points won't send state
        messages.

        To import the certificate, browse to a valid Public Key Cryptography Standard (PKCS
        #12) file. This PFX or CER file has the PKI certificate with the following requirements for
        Configuration Manager:

        The intended use includes client authentication

        Enable the private key to be exported

            Tip

           There are no specific requirements for the certificate subject or subject alternative
           name (SAN). If necessary, use the same certificate for multiple distribution points.

        For more information about the certificate requirements, see PKI certificate
        requirements.

        For an example deployment of this certificate, see Deploying the client certificate for
        distribution points.

Drive settings

  ７ Note

  These options are available only when you're installing a new distribution point.

Specify the drive settings for the distribution point. Configure up to two disk drives for the
content library and two disk drives for the package share. Configuration Manager can use
other drives when the first two reach the configured drive space reserve. The Drive Settings
page configures the priority for the disk drives and the amount of free disk space that remains
on each disk drive.

     Drive space reserve (MB): This value determines the amount of free space on a drive
     before Configuration Manager chooses a different drive and continues the copy process
     to that drive. Content files can span multiple drives.

     Content locations: Specify the locations for the content library and package share on this
     distribution point. By default, all content locations are set to Automatic. Configuration

<!-- p.1061 -->

      Manager copies content to the primary content location until the amount of free space
      reaches the value specified for Drive space reserve (MB). When you select Automatic,
      Configuration Manager sets the primary content locations to the disk drive with the most
      disk space at installation. It sets the secondary locations to the disk drive with the second-
      most free disk space. When the primary and secondary locations reach the drive space
      reserve, Configuration Manager selects another available drive with the most free disk
      space to continue the copy process.

   Tip

  To prevent Configuration Manager from installing on a specific drive, create an empty file
  named NO_SMS_ON_DRIVE.SMS and copy it to the root folder of the drive before you
  install the distribution point.

For more information, see The content library.

Firewall Settings
The distribution point must have the following inbound rules configured in the Windows
firewall:

      Windows Management Instrumentation (DCOM-In)
      Windows Management Instrumentation (WMI-In)

Without these rules, clients will receive error 0x801901F4 in DataTransferService.log when
attempting to download content.

Pull distribution point
When you Enable this distribution point to pull content from other distribution points, it
becomes a pull-distribution point. You change the behavior of how the distribution point gets
the content that you distribute to it. For more information, see Use a pull-distribution point.

For each pull-distribution point that you configure, specify one or more source distribution
points from which it gets the content:

      Choose Add, and then select one or more of the available distribution points to be
      sources.

      Use the arrow buttons to adjust the priority. When the pull-distribution point attempts to
      transfer content, the priority is the order in which it contacts the source distribution
      points. It first contacts distribution points with the lowest value.

<!-- p.1062 -->

PXE
Specify whether to enable PXE on the distribution point. Use PXE to start OS deployments on
clients. For more information on how to use PXE in Configuration Manager, see Use PXE to
deploy Windows over the network.

When you enable PXE, Configuration Manager installs Windows Deployment Services (WDS) on
the server, if necessary. WDS is the service that supports PXE boot to install operating systems.
After you finish the wizard to create the distribution point, Configuration Manager installs a
provider in WDS that uses the PXE boot functions.

You can enable PXE on a distribution point without WDS.

Select the option to Enable PXE support for clients, and then configure the following settings:

  ７ Note

  Select Yes in the Review Required Ports for PXE dialog box to confirm that you want to
  enable PXE. Configuration Manager automatically configures the default ports on
  Windows firewall. If you use a different firewall, manually configure the ports.

  If you install WDS and DHCP on the same server, configure WDS to listen on a different
  port. By default, DHCP listens on the same port. For more information, see Considerations
  when you have WDS and DHCP on the same server.

     Allow this distribution point to respond to incoming PXE requests: Specify whether to
     enable WDS to respond to PXE service requests. Use this setting to enable and disable the
     service without removing the PXE functionality from the distribution point.

     Enable unknown computer support: Specify whether to enable support for computers
     that Configuration Manager doesn't manage. For more information, see Prepare for
     unknown computer deployments.

     Enable a PXE responder without Windows Deployment Service: This option enables a
     PXE responder on the distribution point, which doesn't require WDS. This PXE responder
     supports IPv6 networks. If you enable this option on a distribution point that's already
     PXE-enabled, Configuration Manager suspends the WDS service. If you disable this
     option, but still Enable PXE support for clients, then the distribution point enables WDS
     again.

        ７ Note

<!-- p.1063 -->

  When you enable a PXE responder on a distribution point without Windows
  Deployment Service, it can be on the same server as the DHCP service.

Enable Preferred Management Point(s) for PXE requests: This option allows PXE clients
to communicate to an initial lookup MP and receive the list of MP(s) to be used for
further communication. The lookup MP then returns an MP from the site.

Require a password when computers use PXE: To provide more security for your PXE
deployments, specify a strong password.

User device affinity: Specify how you want the distribution point to associate users with
the destination computer for PXE deployments. Choose one of the following options:

  Allow user device affinity with auto-approval: Choose this setting to automatically
  associate users with the destination computer without waiting for approval.

  Allow user device affinity pending administrator approval: Choose this setting to wait
  for approval from an administrative user before users are associated with the
  destination computer.

  Do not allow user device affinity: Choose this setting to specify that users aren't
  associated with the destination computer. This setting is the default.

  For more information about user device affinity, see Link users and devices with user
  device affinity.

     ７ Note

     When setting user device affinity during a task sequence, the value configured
     here needs to match the value specified for the SMSTSAssignUsersMode variable.

     If the values don't match, then device affinity isn't set.

     For more information, see Task sequence variables.

Network interfaces: Specify that the distribution point responds to PXE requests from all
network interfaces or from specific network interfaces. If the distribution point responds
to specific network interfaces, then provide the MAC address for each network interface.

  ７ Note

  When changing the network interface, restart the WDS service to make sure it
  properly saves the configuration. When using the PXE responder service, restart the

<!-- p.1064 -->

       ConfigMgr PXE Responder Service (SccmPxe).

     Specify the PXE server response delay (seconds): When you use multiple PXE servers,
     specify how long this PXE-enabled distribution point should wait before it responds to
     computer requests. By default, the Configuration Manager PXE-enabled distribution point
     responds immediately.

Multicast
Specify whether to enable multicast on the distribution point. Multicast deployments conserve
network bandwidth by simultaneously sending data to multiple Configuration Manager clients.
Without multicast, the server sends a copy of the data to each client over a separate
connection. For more information about using multicast for OS deployment, see Use multicast
to deploy Windows over the network.

When you enable multicast, Configuration Manager installs Windows Deployment Services
(WDS) on the server, if necessary.

Select the option to Enable multicast to simultaneously send data to multiple clients, and
then configure the following settings:

     Multicast Connection Account: Specify the account to use when you configure
     Configuration Manager database connections for multicast. For more information, see the
     Multicast connection account.

     Multicast address settings: Specify the IP addresses for sending data to the destination
     computers. By default, it obtains the IP address from a DHCP server that's enabled to
     distribute multicast addresses. Depending on the network environment, you can specify a
     range of IP addresses from 239.0.0.0 through 239.255.255.255.

       ） Important

       The IP addresses that you configure must be accessible by the destination computers
       that request the OS image. Verify that routers and firewalls allow for multicast traffic
       between the destination computer and the distribution point.

     UDP port range for multicast: Specify the range of UDP ports that are used to send data
     to the destination computers.

       ） Important

<!-- p.1065 -->

       The UDP ports must be accessible by the destination computers that request the OS
       image. Verify that routers and firewalls allow for multicast traffic between the
       destination computer and the site server.

     Maximum clients: Specify the maximum number of destination computers that can
     download the OS image from this distribution point.

     Enable scheduled multicast: Specify how Configuration Manager controls when to start
     deploying operating systems to destination computers. Configure the following options:

        Session start delay (minutes): Specify the number of minutes that Configuration
        Manager waits before it responds to the first deployment request.

        Minimum session size (clients): Specify how many requests must be received before
        Configuration Manager starts to deploy the operating system.

  ） Important

  To enable and configure multicast on the Multicast tab of the distribution point
  properties, the distribution point must use Windows Deployment Service.

       If you Enable PXE support for clients and Enable multicast to simultaneously send
       data to multiple clients, then you can't Enable a PXE responder without Windows
       Deployment Service.

       If you Enable PXE support for clients and Enable a PXE responder without Windows
       Deployment Service, then you can't Enable multicast to simultaneously send data
       to multiple clients.

Group relationships

  ７ Note

  These options are available only when you're editing the properties of a previously
  installed distribution point.

Manage the distribution point groups in which this distribution point is a member.

To add this distribution point as a member to an existing a distribution point group, choose
Add. In the Add to Distribution Point Groups window, select an existing group, and then

<!-- p.1066 -->

choose OK.

To remove this distribution point from a distribution point group, select the group in the list,
and then choose Remove. Removing the distribution point from a distribution point group
doesn't remove any content from the distribution point.

Content

  ７ Note

  These options are available only when you're editing the properties of a previously
  installed distribution point.

Manage the content that you distributed to the distribution point. Select from the list of
deployment packages, and then select one of the following actions:

     Validate: Start the process to validate the integrity of the content files for the software. To
     view the results of the content validation process, in the Monitoring workspace, expand
     Distribution Status, and then choose the Content Status node. For more information, see
     Validate content.

     Redistribute: Copies all of the content files for the selected software to the distribution
     point, and overwrites the existing files. You typically use this action to repair content files.
     For more information, see Redistribute content.

     Remove: Removes the content files for the software from the distribution point. For more
     information, see Remove content.

Content validation
Set a schedule to validate the integrity of content files on the distribution point. When you
enable content validation on a schedule, Configuration Manager starts the process at the
scheduled time. It verifies all content on the distribution point based on the local
SMS_PackagesInContLib SCCMDP class. You can also configure the content validation priority.
By default, the priority is set to Lowest. Increasing the priority might increase the processor and
disk utilization on the server during the validation process, but it should complete faster.

To view the results of the content validation process, in the Monitoring workspace, expand
Distribution Status, and then choose the Content Status node. It shows the content for each
software type, for example, application, software update package, and boot image.

<!-- p.1067 -->

  ２ Warning

  Although you specify the content validation schedule by using the local time for the
  computer, the Configuration Manager console shows the schedule in UTC.

For more information, see Validate content.

Boundary groups
Manage the boundary groups to which you assign this distribution point. Add the distribution
point to at least one boundary group. During content deployment, clients must be in a
boundary group associated with a distribution point to use that distribution point as a source
location for content.

Configure boundary group relationships that define when and to which boundary groups a
client can fall back to find content. For more information, see Boundary groups.

Choose Add and select an existing boundary group from the list.

To create a new boundary group for this distribution point, choose Create. For more
information on how to create and configure a boundary group, see Procedures for boundary
groups.

When you're editing the properties of a previously installed distribution point, manage the
option to Enable for on-demand distribution. This option allows Configuration Manager to
automatically distribute content to this server when a client requests it. For more information,
see On-demand content distribution.

Schedule

  ７ Note

  These options are available only when you're editing the properties of a previously
  installed distribution point.

  This tab is available only when you edit the properties for a distribution point that's
  remote from the site server.

Configure a schedule that restricts when Configuration Manager can transfer data to the
distribution point. Restrict data by priority or close the connection for selected time periods.

<!-- p.1068 -->

To restrict data, select the time period in the grid, and then choose one of the following
settings for Availability:

     Open for all priorities: Configuration Manager sends data to the distribution point with
     no restrictions. This setting is the default for all time periods.

     Allow medium and high priority: Configuration Manager sends only medium-priority and
     high-priority data to the distribution point.

     Allow high priority only: Configuration Manager sends only high-priority data to the
     distribution point.

     Closed: Configuration Manager doesn't send any data to the distribution point.

Configure the Distribution priority of software on the Distribution Settings tab of the
software's properties.

  ） Important

  The schedule is based on the time zone from the sending site, not the distribution point.

Rate limits

  ７ Note

  These options are available only when you're editing the properties of a previously
  installed distribution point.

  This tab is available only when you edit the properties for a distribution point that's
  remote from the site server.

Configure rate limits to control the network bandwidth that Configuration Manager uses to
transfer content to the distribution point. Choose from the following options:

     Unlimited when sending to this destination: Configuration Manager sends content to
     the distribution point with no rate limit restrictions. This setting is the default.

     Pulse mode: This option specifies the size of the data blocks that the site server sends to
     the distribution point. You can also specify a time delay between sending each data block.
     Use this option when you must send data across a very low-bandwidth network
     connection to the distribution point. For example, you have constraints to send 1 KB of
     data every five seconds, whatever the speed of the link or its usage at a given time.

<!-- p.1069 -->

Limited to specified maximum transfer rates by hour: Specify this setting to have a site
send data to a distribution point by using only the percentage of time that you configure.
When you use this option, Configuration Manager doesn't identify the network's available
bandwidth. Instead it divides the time that it can send data. The server sends data for a
short period of time, which is followed by periods of time when data isn't sent. For
example, if you set Limit available bandwidth to 50%, Configuration Manager transmits
data for a time period followed by an equal period of time when no data is sent. The
actual size amount of data, or size of the data block, isn't managed. It only manages the
amount of time during which it sends data.

<!-- p.1070 -->

Deploy and manage content for
Configuration Manager
Article • 12/05/2022

Applies to: Configuration Manager (current branch)

After you install distribution points for Configuration Manager, you can begin to deploy
content to them. Typically, content transfers to distribution points across the network,
but other options to get content to the distribution points exists. After content transfers
to a distribution point, you can update, redistribute, remove, and validate that content
on distribution points.

There are many types of content. All of the actions in this article apply to the following
objects in the Software Library workspace in the Configuration Manager console:

      Applications: Expand the Application Management node, select Applications, and
      then select the specific applications.

      Packages: Expand the Application Management node, select Packages, and then
      select the specific packages.

      Software update deployment packages: Expand the Software Updates node,
      select Deployment Packages, and then select the specific deployment packages.

      Driver packages: Expand the Operating Systems node, select Driver Packages, and
      then select the specific driver packages.

      OS images: Expand the Operating Systems node, select Operating System
      Images, and then select the specific OS images.

      OS upgrade packages: Expand the Operating Systems node, select Operating
      System Upgrade Packages, and then select the specific OS upgrade packages.

      Boot Images: Expand the Operating Systems node, select Boot Images, and then
      select the specific boot images.

      Task Sequences: Expand the Operating Systems node, select Task Sequences, and
      then select the specific task sequence. Although task sequences don't contain
      content, they have associated content references.

Distribute content

<!-- p.1071 -->

Typically, you distribute content to distribution points so that it's available to clients. The
exception to this behavior is when you use on-demand content distribution for a
specific deployment. When you distribute content, Configuration Manager stores
content files in a package, and then distributes the package to the distribution point.
The content for the package is pulled from the site server's content library.

When you create a package that contains source files, the site on which you create it
becomes the site owner for the content source. Configuration Manager copies the
source files from the source file path that you specify for the object to the content
library on the site server that owns it. Then Configuration Manager replicates the
information to additional sites. For more information, see The content library.

Use the following procedure to distribute content to distribution points.

   1. In the Configuration Manager console, go to the Software Library workspace.

   2. Select one of the content types that you want to distribute.

   3. On the Home tab of the ribbon, in the Deployment group, select Distribute
     Content.

   4. On the General page of the Distribute Content Wizard, verify that the content
     listed is the content that you want to distribute. Then choose whether you want
     Configuration Manager to detect content dependencies that are associated with
     the selected content and add the dependencies to the distribution.

        ７ Note

        For applications, you can also configure the Detect associated content
        dependencies and add them to this distribution setting. Configuration
        Manager automatically configures this setting for task sequences.

   5. On the Content tab, if displayed, verify that the content listed is the content that
     you want to distribute.

        ７ Note

        The Content page displays only when you select the Detect associated
        content dependencies and add them to this distribution setting on the
        General page of the wizard.

<!-- p.1072 -->

   6. On the Content Destination page, select Add, choose one of the following
     options:

           Collections: Choose User Collections or Device Collections, and then select
           the collection associated with one or more distribution point groups.

              ７ Note

              It only displays the collections that are associated with a distribution
              point group. For more information, see Manage distribution point
              groups.

           Distribution Point: Choose an existing distribution point, and then select OK.
           It doesn't display distribution points that have previously received the
           content.

           Distribution Point Group: Choose an existing distribution point group, and
           then select OK. It doesn't display distribution point groups that have
           previously received the content.

     When you finish adding content destinations, select Next.

   7. On the Summary page, review the settings for the distribution before you
     continue. To distribute the content to the selected destinations, select Next.

   8. The Progress page displays the progress of the distribution.

   9. The Confirmation page displays whether the content was successfully assigned to
     the servers. To further monitor the content distribution, see Monitor content
     you've distributed with Configuration Manager.

Use prestaged content
Prestaged content is a compressed file that contains the content files and associated
metadata for a content type. You can then manually import this content to another site
server, a secondary site, or a distribution point.

     When you import the prestaged content file on a site server, it adds the content
     files to its content library. It then registers the content in the site server database.

     When you import the prestaged content file on a distribution point, the content
     files are added to the content library on the distribution point. It then sends a

<!-- p.1073 -->

     status message to the site server, which informs the site that the content is
     available on the distribution point.

Limitations and considerations for prestaged content
     When the distribution point is located on the site server, don't enable the
     distribution point for prestaged content. Instead use the procedure in How to
     prestage content on a distribution point on a site server.

     When the distribution point is configured as a pull-distribution point, don't enable
     the distribution point for prestaged content. The prestage content configuration
     for a distribution point overrides the pull-distribution point configuration. A pull-
     distribution point that you configure for prestaged content doesn't pull content
     from its source distribution point and doesn't receive content from the site server.

     Before you can prestage content to the distribution point, create the content
     library on the server. Distribute content over the network at least once to prepare
     the content library. Then you can prestage content.

     When you prestage content for an object with a long package source path, the
     Extract Content command-line tool might fail. A long package source path is more
     than 140 characters.

For more information about when to prestage content files, see Manage network
bandwidth for content management.

Step 1: Create a prestaged content file
  1. In the Configuration Manager console, go to the Software Library workspace.

  2. Select one of the content types that you want to prestage.

  3. On the Home tab of the ribbon, select Create Prestage Content File.

  4. On the General page of the Create Prestaged Content File Wizard, select Browse.
     Choose the location for the prestaged content file, specify a name for the file, and
     then select Save. You use this prestaged content file on primary site servers,
     secondary site servers, or distribution points to import the content and metadata.

  5. For applications, select Export all dependencies to have Configuration Manager
     detect and add the dependencies associated with the application to the prestaged
     content file. By default, this setting is selected.

<!-- p.1074 -->

   6. In Administrator comments, enter optional comments about the prestaged
     content file.

   7. On the Content page, verify that the content listed is the content that you want to
     add to the prestaged content file.

   8. On the Content Locations page, specify the distribution points from which to
     retrieve the content for the prestaged content file. You can select more than one
     distribution point to retrieve the content. The distribution points are listed in the
     Content locations section. The Content column displays how many of the selected
     packages or applications are available on each distribution point.

     Configuration Manager starts with the first distribution point in the list to retrieve
     the selected content. It then moves down the list to retrieve the remaining content
     required for the prestaged content file. To change the priority order of the
     distribution points, select Move Up or Move Down.

     When the distribution points in the list don't contain all of the selected content,
     add distribution points to the list that contain the content. Otherwise, exit the
     wizard, distribute the content to at least one distribution point, and then restart
     the wizard.

   9. On the Summary page, confirm the details. You can go back to previous pages and
     make changes. Select Next to create the prestaged content file.

 10. The Progress page displays the content that it's adding to the prestaged content
     file.

 11. On the Completion page, verify that it successfully created the prestaged content
     file, and then select Close.

Step 2: Assign the content to distribution points
After you prestage the content file, assign the content to distribution points.

  ７ Note

  When you use a prestaged content file to recover the content library on a site
  server, and don't have to prestage the content files on a distribution point, you can
  skip this procedure.

Use the following procedure to assign the content in the prestaged content file to
distribution points.

<!-- p.1075 -->

） Important

Verify that the distribution points that you want to prestage are configured as
prestaged distribution points, or that the content is distributed to the distribution
points over the network.

1. In the Configuration Manager console, go to the Software Library workspace.

2. Select the same content type that you selected when you created the prestaged
   content file.

3. On the Home tab, in the Deployment group, select Distribute Content.

4. On the General page of the Distribute Content Wizard, verify that the content
   listed is the content that you prestaged. Choose whether you want Configuration
   Manager to detect content dependencies that are associated with the selected
   content and add the dependencies to the distribution.

     ７ Note

     For applications, you can also configure the Detect associated content
     dependencies and add them to this distribution setting. Configuration
     Manager automatically configures this setting for task sequences.

5. On the Content page, if displayed, verify that the content listed is the content that
   you want to distribute.

     ７ Note

     The Content page displays only when the Detect associated content
     dependencies and add them to this distribution setting is selected on the
     General page of the wizard.

6. On the Content Destination page, select Add, and choose one of the following
   options that includes the distribution points to be prestaged:

        Collections: Choose User Collections or Device Collections, then select the
        collection associated with one or more distribution point groups.

           ７ Note

<!-- p.1076 -->

             It only displays the collections that are associated with a distribution
             point group. For more information, see Manage distribution point
             groups.

           Distribution Point: Select an existing distribution point, and then select OK. It
           doesn't display distribution points that already have the content.

           Distribution Point Group: Select an existing distribution point group, and
           then select OK. It doesn't display distribution point groups that already have
           the content.

     When you finish adding content destinations, select Next.

   7. On the Summary page, review the settings for the distribution before you
     continue. To distribute the content to the selected destinations, select Next.

   8. The Progress page displays the progress of the distribution.

   9. The Confirmation page displays whether the content was successfully assigned to
     the distribution points. To monitor the content distribution, see Monitor content
     you've distributed.

Step 3: Extract the content from the prestaged content
file
After you create the prestaged content file and assign the content to distribution points,
extract the content files to the content library on the target server.

First, manually copy the prestaged content file to the target server. Use a portable drive
like a USB drive, or media like a DVD. Have it available at the location of the server that
requires the content.

Next, you use the Extract Content command-line tool to export the content files from
the prestaged content file.

     When you run the tool, it creates a temporary file as it creates the content files.
     Then it copies the file to the destination folder, and deletes the temporary file. The
     server needs sufficient disk space for this temporary file.

     The tool creates the temporary file in the specified destination folder for the
     content files.

     The user that runs the tool must have Administrator rights on the server where
     you extract the content.

<!-- p.1077 -->

To extract the content files from the prestaged content file
  1. Copy the prestaged content file to the server where you want to extract the
    content.

  2. Copy ExtractContent.exe from the \bin\x64 subfolder of the Configuration
    Manager site installation. Copy it to the same folder on the target server as the
    prestaged content file.

  3. On the target server, open the command prompt. Navigate to the folder location
    of the prestaged content file and Extract Content tool.

      ７ Note

      You can extract one or more prestaged content files on a site server,
      secondary site server, or distribution point.

  4. Use the following commands to import the content:

         Single file: extractcontent.exe /P:<PrestagedFileLocation>\
         <PrestagedFileName> /S

         All prestaged files in the specified folder: extractcontent.exe /P:
         <PrestagedFileLocation> /S

    For example, if D:\PrestagedFiles\ is the prestaged file location, and
    MyPrestagedFile.pkgx is the prestaged file name:

    extractcontent /P:D:\PrestagedFiles\MyPrestagedFile.pkgx /S

    The /S parameter extracts only content files that are newer than what's currently
    in the content library.

    When you extract the prestaged content file on a site server, the content files are
    added to its content library. The site then registers the content in the site server
    database. When you export the prestaged content file on a distribution point, it
    adds the content files to the content library on the distribution point. The
    distribution point sends a status message to the parent primary site server, which
    then registers the content in the site database.

 ） Important

<!-- p.1078 -->

  When you update content on the site to a new version, make sure to also update
  content for prestaged content files. For example:

     1. You create a prestaged content file for version 1 of a package.
     2. You update the source files for the package with version 2.
     3. You extract the version 1 prestaged content file on a distribution point.

  In this example, Configuration Manager doesn't automatically distribute package
  version 2 to the distribution point. Create a new prestaged content file that
  contains the new file version. Then extract the content, update the distribution
  point to distribute the files that have changed, or redistribute all files in the
  package.

How to prestaged content on a distribution point on a
site server
When a distribution point is installed on a site server, use the following procedure to
successfully prestage content. This process is different because the content files are
already in the content library.

When the distribution point isn't enabled for prestaged content or when the distribution
point isn't located on a site server, see the Use Prestaged content section.

   1. Verify that the distribution point isn't enabled for prestaged content.

      a. In the Configuration Manager console, go to the Administration workspace.

      b. In the Administration workspace, select the Distribution Points node. Then
        select the distribution point that's on the site server.

      c. On the Home tab of the ribbon, in the Properties group, select Properties.

      d. On the General tab, verify that the option to Enable this distribution point for
        prestaged content isn't selected.

   2. Create a prestaged content file.

   3. Assign the content to the distribution point.

   4. On the site server, extract the content from the prestaged content file.

        ７ Note

<!-- p.1079 -->

        When the distribution point is on a secondary site, wait for at least 10
        minutes. Then in the Configuration Manager console, assign the content to
        the distribution point on the secondary site.

Manage distributed content
You have the following options for managing content:

     Update content
     Update content on schedule
     Redistribute content
     Remove content
     Validate content

Update content
When you update the source file location for a deployment by adding new files or
replace existing files with a newer version, update the content files on distribution
points. Use the Update Distribution Points or Update Content actions.

     The site copies the content files from the original package source location to the
     content library on the site that owns the package content source.
     It increments the package version.
     Each instance of the content library on site servers and on distribution points
     updates with only the changed files.

  ２ Warning

  The package version for applications is always 1. When you update the content for
  an application deployment type, Configuration Manager creates a new content ID
  for the deployment type, and the package references the new content ID.

Process to update content on distribution points
   1. In the Configuration Manager console, go to the Software Library workspace.

   2. Select the content type that you want to update.

   3. For most object types: On the Home tab of the ribbon, in the Deployment group,
     select Update Distribution Points. Then select OK to confirm that you want to

<!-- p.1080 -->

     update the content.

     To update content for applications: Select the Deployment Types tab in the details
     pane. Choose the deployment type. On the Deployment Type tab of the ribbon,
     select Update Content. Then select OK to confirm that you want to refresh the
     content.

     When you update content for boot images: The Update Distribution Points action
     opens the Manage Distribution Point Wizard. For more information, see Update
     distribution points with the boot image.

Update content on schedule
You can create a schedule for when the site updates the content for the object. Use this
option for an object whose content changes frequently.

   1. In the Configuration Manager console, go to the Software Library workspace.

   2. Select the content type that you want to update.

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. Switch to the Data source tab. Select the option to Update distribution points on
     a schedule.

   5. Select Schedule and specify a custom schedule. You can also set a recurrence
     pattern.

If the source content hasn't changed, then this action doesn't do anything. To
redistribute all content, use the distribute or redistribute actions.

Redistribute content
You can redistribute a package to copy all of the content files in the package to
distribution points or distribution point groups. This action overwrites the existing files.

Use this operation to repair content files in the package or resend the content when the
initial distribution fails. You can redistribute a package from:

     Package properties
     Distribution point properties
     Distribution point group properties

Process to redistribute content from package properties
