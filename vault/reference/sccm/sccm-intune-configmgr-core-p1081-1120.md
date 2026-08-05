---
title: "Core infrastructure documentation — pages 1081-1120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1081-1120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1081-1120
family: sccm
documentKind: "doc"
abstract: "1. In the Configuration Manager console, go to the Software Library workspace. 2. Select the content types that you want to redistribute. 3. On the Home tab of the ribbon, in the Properties group, select Properties. 4. Switch to the Content Locations tab. Select the distribution"
---

# Core infrastructure documentation — pages 1081-1120

<!-- p.1081 -->

  1. In the Configuration Manager console, go to the Software Library workspace.

  2. Select the content types that you want to redistribute.

  3. On the Home tab of the ribbon, in the Properties group, select Properties.

  4. Switch to the Content Locations tab. Select the distribution point or distribution
     point group to which you want to redistribute the content, and select Redistribute.

Process to redistribute content from distribution point properties
  1. In the Configuration Manager console, go to the Administration workspace.

  2. In the Administration workspace, select the Distribution Points node. Then select
     the distribution point to which you want to redistribute content.

  3. On the Home tab of the ribbon, in the Properties group, select Properties.

  4. Switch to the Content tab. Select the content to redistribute, and select
     Redistribute.

Process to redistribute content from distribution point group
properties
  1. In the Configuration Manager console, go to the Administration workspace.

  2. In the Administration workspace, select the Distribution Point Groups node. Then
     select the distribution point group to which you want to redistribute content.

  3. On the Home tab of the ribbon, in the Properties group, select Properties.

  4. Switch to the Content tab. Select the content to redistribute, and select
     Redistribute.

       ） Important

       The site redistributes the content in the package to all of the distribution
       points in the group.

Use the SDK to force replication of content

You can use the RetryContentReplication WMI method from the Configuration
Manager SDK to force distribution manager to copy content from the source location to

<!-- p.1082 -->

the content library.

Only use this method to force replication when you need to redistribute content after
there were issues with normal replication of content. You can typically confirm this state
in the Monitoring node of the console.

For more information about this SDK option, see RetryContentReplication method in
class SMS_CM_UpdatePackages.

Distribution point content migration
Content migration support is now available for migrating content from one DP to
another DP using PowerShell cmdlets. You can also monitor the DP migration status
using these PowerShell cmdlets.

There are multiple scenarios where the content of one distribution point needs to be
migrated to another distribution point.

   1. Cloud distribution points (CDP) hosted on Azure classic services are getting
     deprecated by mid of 2024. You need to migrate CDP content to another
     distribution point.
   2. Migration of cloud migration gateway v1 (CMGv1) hosted with *.cloudapp.net
     domain is also getting deprecated, hence you may need to migrate CMGv1
     content to another distribution point.
   3. You may need to migrate local distribution point content to other local distribution
     point or CMG.

Prerequisites
   1. The user's security role permission should have "Copy to Distribution Point"
     enabled under Distribution Point.
   2. If you want to deprecate the source distribution point, make sure that the source,
     and destination distribution points have the same boundary group.
   3. The destination distribution point should be installed already and able to receive
     the content.

  ７ Note

  You can't currently configure this behavior from the Configuration Manager
  console.
  For more information on configuring this behavior with PowerShell, see the cmdlet
  details in the following section.

<!-- p.1083 -->

  Distribution failure status is not shown in admin console when source distribution
  point is locked during migration and sending new content to source distribution
  point.
  Get and Stop DP migration cmdlets works only on the site server where the DP
  migration is initiated.

Start-CMDistributionPointMigration
Use this cmdlet to initiate distribution point content migration. You can pass the desired
parameters such as SourceDistributionPointName and
DestinationDistributionPointName per your distribution point migration scenario. You
can also pass the LockSourceDistributionPoint parameter to lock the source distribution
point. This parameter is used to deprecate the source distribution point scenarios (for
example: CDP Migration). If the source DP is locked during migration, you won't be able
to distribute the new content to the source dp, but the endpoints will be able to
download the content that is already available in the source DP. For deprecation
scenarios, you can delete the source distribution point after the distribution content
migration is completed.

Syntax

  PowerShell

  Start-CMDistributionPointMigration -SourceDistributionPointName <FQDN for
  source distribution point> -DestinationDistributionPointName <FQDN for
  destination distribution point>

Examples

  PowerShell

  Start-CMDistributionPointMigration -SourceDistributionPointName <FQDN for
  source distribution point> -DestinationDistributionPointName <FQDN for
  destination distribution point> -LockSourceDistributionPoint
  Start-CMDistributionPointMigration -SourceDistributionPointName <FQDN for
  source distribution point> -DestinationDistributionPointName <FQDN for
  destination distribution point>

Parameters

<!-- p.1084 -->

     SourceDistributionPointName: Use the parameter to specify the source
     distribution point from where content will be migrated.

     DestinationDistributionPointName: Use the parameter to specify the destination
     distribution point where you want the content to be copied.

     LockSourceDistributionPoint: Use when you need to initiate distribution point
     migration with source distribution point locked.

Get-CMDistributionPointMigrationStatus
Use this cmdlet to monitor the distribution point migration status.

Syntax

  PowerShell

  Get-CMDistributionPointMigrationStatus -SourceDistributionPointName <FQDN
  for source distribution point> -DestinationDistributionPointName <FQDN for
  destination distribution point>

Get-CMDistributionPointMigrationContentStatus
Use this cmdlet to monitor the distribution point content migration status.

Syntax

  PowerShell

  Get-CMDistributionPointMigrationContentStatus -SourceDistributionPointName
  <FQDN for source distribution point> -DestinationDistributionPointName <FQDN
  for destination distribution point>

Stop-CMDistributionPointMigration
Use this cmdlet to stop the distribution point migration. In case you have mistakenly
locked the source distribution point, you can use this cmdlet to unlock the source
distribution point. Unlocking the source distribution point will stop the distribution point
migration. To restart the migration, use the Start-CMDistributionPointMigration cmdlet.

Syntax

<!-- p.1085 -->

  PowerShell

  Stop-CMDistributionPointMigration -SourceDistributionPointName <FQDN for
  source distribution point> -DestinationDistributionPointName <FQDN for
  destination distribution point>

Examples

  PowerShell

  Stop-CMDistributionPointMigration -SourceDistributionPointName <FQDN for
  source distribution point> -DestinationDistributionPointName <FQDN for
  destination distribution point> -LockSourceDistributionPoint
  Stop-CMDistributionPointMigration -SourceDistributionPointName <FQDN for
  source distribution point> -DestinationDistributionPointName <FQDN for
  destination distribution point>

  ７ Note

  You can't currently configure this behavior from the Configuration Manager
  console.
  For more information on configuring this behavior with PowerShell, see the cmdlet
  details in the following section.
  Distribution failure status is not shown in admin console when source distribution
  point is locked during migration and sending new content to source distribution
  point.
  Get and Stop DP migration cmdlets works only on the site server where the DP
  migration is initiated.

Remove content
When you no longer require content on your distribution points, you can remove it.

When the content is associated with another package that was distributed to the same
distribution point, you can't remove the content.

Process to remove content from distribution points using object
properties

   1. In the Configuration Manager console, select the Software Library workspace.

   2. Select the content type that you want to remove its content.

<!-- p.1086 -->

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. Switch to the Content Locations tab. Select the distribution point or distribution
     point group from which you want to remove the content, select Remove, and then
     select OK.

Process to remove content using distribution point properties

   1. In the Configuration Manager console, select the Administration workspace.

   2. In the Administration workspace, select the Distribution Points node, and then
     select the distribution point from which you want to delete the content.

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. Switch to the Content tab. Choose the content to remove, select Remove, and
     then select OK.

Process to remove content using distribution point group
properties
   1. In the Configuration Manager console, select the Administration workspace.

   2. In the Administration workspace, select the Distribution Point Groups node. Then
     select the distribution point group from which you want to remove content.

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. Switch to the Content tab. Choose the content to remove, select Remove, and
     then select OK.

Validate content
The content validation process verifies the integrity of content files on distribution
points. You enable content validation on a schedule, or you can manually start content
validation from the properties of distribution points and packages.

When the content validation process starts, Configuration Manager verifies the content
files on distribution points. If the file hash is unexpected for the files on the distribution
point, Configuration Manager creates a status message that you can review in the
Monitoring workspace.

For more information about configuring the content validation schedule, see
Distribution point configurations.

<!-- p.1087 -->

Process to validate all content on a distribution point
   1. In the Configuration Manager console, select the Administration workspace.

   2. Select the Distribution Points node, and then select the distribution point from
     which you want to validate content.

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. Switch to the Content tab. Select the package that you want to validate. Select
     Validate, and then select OK. The content validation process starts for the package
     on the distribution point.

   5. To view the results of the content validation process, go to the Monitoring
     workspace. Expand Distribution Status, and select the Content Status node. This
     node displays the content for each type. For more information about monitoring
     content status, see Monitor content you've distributed.

Process to validate content for a specific object

   1. In the Configuration Manager console, select the Software Library workspace.

   2. Select the content type that you want to validate.

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. Switch to the Content Locations tab. Select the distribution point or distribution
     point group on which to validate the content. Select Validate, and then select OK.
     The content validation process starts for the content on the selected distribution
     point or distribution point group.

   5. To view the results of the content validation process, go to the Monitoring
     workspace. Expand Distribution Status, and select the Content Status node. It
     displays the content for each type. For more information about monitoring the
     content status, see Monitor content you've distributed.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1088 -->

Monitor content you distribute with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the Configuration Manager console to monitor distributed content, including:

      The status for all package types for the associated distribution points.
      The content validation status for the content in a package.
      The status of content assigned to a specific distribution point group.
      The state of content assigned to a distribution point.
      The status of optional features for each distribution point (content validation, PXE,
      and multicast).

Configuration Manager only monitors the content on a distribution point that's in the
content library. It doesn't monitor content stored on the distribution point in package or
custom shares.

   Tip

  The Power BI sample reports for Configuration Manager includes a report called
  Content Status. This report can also help with monitoring content.

Content status monitoring
The Content Status node in the Monitoring workspace provides information about
content packages. In the Configuration Manager console, review information like:

      Package name, type, and ID
      How many distribution points a package has been sent to
      Compliance rate
      When the package was created
      Source version

You also find detailed status information for any package, including:

      Distribution status
      The number of failures
      Pending distributions

<!-- p.1089 -->

     The number of installations

You can also manage distributions that remain in progress to a distribution point, or that
failed to successfully distribute content to a distribution point:

     The option to either cancel or redistribute content is available when you view the
     deployment status message of a distribution job to a distribution point in the
     Asset Details pane. This pane can be found in either the In Progress tab or the
     Error tab of the Content Status node.

     Additionally, the job details display the percentage of the job that has completed
     when you view the details of a job on the In Progress tab. The job details also
     display the number of retries that remain for a job. When you view the details of a
     job on the Error tab, it shows how long before the next retry occurs.

When you cancel a deployment that's not yet complete, the distribution job to transfer
that content stops:

     The status of the deployment then updates to indicate that the distribution failed,
     and that it was canceled by a user action.
     This new status appears in the Error tab.

  ７ Note

  When a deployment is near completion, it's possible the action to cancel that
  distribution won't process before the distribution to the distribution point
  completes. When this occurs, the action to cancel the deployment is ignored, and
  the status for the deployment displays as successful.

  Although you can select the option to cancel a distribution to a distribution point
  that is located on a site server, this has no effect. This behavior is because the site
  server and the distribution point on a site server share the same single instance
  content store. There's no actual distribution job to cancel.

When you redistribute content that previously failed to transfer to a distribution point,
Configuration Manager immediately begins redeploying that content to the distribution
point. Configuration Manager updates the status of the deployment to reflect the
ongoing state of that redeployment.

Tasks to monitor content

<!-- p.1090 -->

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Distribution Status, and then select the Content Status node. This node displays
     the packages.

   2. Select the package you want to manage.

   3. On the Home tab of the ribbon, in the Content group, select View Status. The
     console displays detailed status information for the package.

   Tip

  Starting in version 2203, select View Content Distribution to monitor content
  distribution path and status in a graphical format. The graph shows distribution
  point type, distribution state, and associated status messages. This visualization
  allows you to more easily understand the status of your content package
  distribution. For more information, see Visualize content distribution status.

Continue to one of the following sections for other actions:

Cancel a distribution that remains in progress
   1. Switch to the In Progress tab.

   2. In the Asset Details pane, right-click the entry for the distribution that you want to
     cancel, and select Cancel.

   3. Select Yes to confirm the action and cancel the distribution job to that distribution
     point.

Redistribute content that failed to distribute

   1. Switch to the Error tab.

   2. In the Asset Details pane, right-click the entry for the distribution that you want to
     redistribute, and select Redistribute.

   3. Select Yes to confirm the action and start the redistribution process to that
     distribution point.

Distribution point group status

<!-- p.1091 -->

The Distribution Point Group Status node in the Monitoring workspace provides
information about distribution point groups. You can review information like:

     The distribution point group name, description, and status
     How many distribution points are members of the distribution point group
     How many packages have been assigned to the group
     The compliance rate

You also view the following detailed status information:

     Errors for the distribution point group
     How many distributions are in progress
     How many have been successfully distributed

Monitor distribution point group status
   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Distribution Status, and then select the Distribution Point Group Status node. It
     displays the distribution point groups.

   2. Select the distribution point group for which you want detailed status information.

   3. On the Home tab of the ribbon, select View Status. It displays detailed status
     information for the distribution point group.

Distribution point configuration status
The Distribution Point Configuration Status node in the Monitoring workspace
provides information about the distribution point. You can review what attributes are
enabled for the distribution point, such as the PXE, multicast, content validation. Also
review the distribution status for the distribution point.

  ２ Warning

  Distribution point configuration status is relative to the last 24 hours. If the
  distribution point has an error and recovers, the error status might be displayed for
  up to 24 hours after the distribution point recovers.

Monitor distribution point configuration status

<!-- p.1092 -->

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Distribution Status, and then select the Distribution Point Configuration Status
     node.

   2. Select a distribution point.

   3. In the results pane, switch to the Details tab. It displays status information for the
     distribution point.

Client data sources dashboard
Use the Client data sources dashboard to better understand from where clients get
content in your environment. The dashboard starts displaying data after clients
download content and report that information back to the site. This process can take up
to 24 hours.

The client data sources dashboard includes a selection of filters to view information
about where clients get content:

                                                                                        

  ７ Note

<!-- p.1093 -->

  Configuration Manager doesn't enable this optional feature by default. Before you
  can use it, enable the Client Peer Cache feature. For more information, see Enable
  optional features from updates.

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Distribution Status, and select the Client Data Sources node.

   2. Report Period: Select a time period to apply to the dashboard.

   3. Then select the single boundary group for which you want to view information.

     You can also select more filters for the dashboard:

           All boundary groups
           Internet clients
           Clients not associated with a boundary group

        ７ Note

        If there's no data available for the selected client group, the chart displays:
        "This data is not yet available."

You can hover your mouse over tiles to see more details about the different content or
policy sources.

Also use the report, Client Data Sources - Summarization, to view a summary of the
client data sources for each boundary group.

Dashboard tiles
The dashboard includes the following tiles:

Data source usage

This tile summarizes the types of sources in your environment and how many clients use
them.

This summary tile replaces the following four tiles in prior versions:

     Distribution points
     Clients that used a distribution point
     Peer cache sources
     Clients that used a peer

<!-- p.1094 -->

Client content sources
Displays the sources from which clients got content:

     Distribution point
     Cloud distribution point, which includes content-enabled cloud management
     gateways
     BranchCache
     Peer Cache
     Delivery Optimization Note 1
     Microsoft Update: Devices report this source when the Configuration Manager
     client downloads software updates from Microsoft cloud services. These services
     include Microsoft Update and Microsoft 365 Apps for enterprise.

  ７ Note

  To include Delivery Optimization on this dashboard, do the following actions:

       Configure the client setting, Enable installation of Express Updates on clients
       in the Software Updates group

       Deploy Windows express updates

<!-- p.1095 -->

  For more information, see Manage Express installation files for Windows updates.

Content downloads using fallback source
This information helps you understand how often clients download content from an
alternate source.

Top distributed content

The most distributed packages by source type

Next steps
Visualize content distribution status

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1096 -->

Visualize content distribution status
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Starting in version 2203, you can monitor content distribution path and status in a
graphical format. The graph shows distribution point type, distribution state, and
associated status messages. This visualization allows you to more easily understand the
status of your content package distribution. It helps you answer questions like:

      Has the site successfully distributed the content?
      Is the content distribution in progress?
      Which distribution points have already processed the content?

<!-- p.1097 -->

This example shows a graph for the content distribution status of the Configuration
Manager client package in an example hierarchy. It lets you easily see the following
information:

     The solid blue line from the site server to each distribution point indicates that the
     rate limit is Unlimited. For more information, see Rate limits.
     The green check mark on DP01 and DP02 indicates that the content was
     successfully distributed to these site systems.
     The red X on DP03 and both cloud distribution points indicates that there's an
     error in distributing the content to these site systems.

View content distribution
   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Distribution Status and select the Content Status node.

   2. If this node doesn't show anything, first distribute content.

   3. Select a distributed content item. For example, the Configuration Manager client
     package.

   4. In the ribbon, select View Content Distribution. This action displays the
     distribution graph for the selected content.

           Hover over the status icon to quickly view more information. Select the path
           or the status icon to view status messages for the content.

           Hover over the title of the site system to quickly view more information.
           Select it to drill through to the Distribution Points node.

Navigation tips
Use the following tips to navigate the relationship viewer:

     Select the plus ( + ) or minus ( - ) icons next to the server name to expand or
     collapse members of a node.

     The style and color of the line between the servers determines the type of
     distribution. If you hover over a specific line, a tooltip shows the type.

     The maximum number of child nodes displayed depends upon the level of the
     graph:
        First level: five nodes

<!-- p.1098 -->

        Second level: three nodes
        Third level: two nodes
        Fourth level: one node

     If there are more objects than the graph can display at that level, you'll see the
     More icon.

     When the size of the tree is larger than the window, use the green arrows to view
     more.

     When a node of the tree is larger than the available space, select More to change
     the view to just that node.

     To navigate to a prior view, select the Back arrow. Select the Home icon to return
     to the main page.

     Use the Search box to locate a server in the current tree view.

     Use the Navigator to zoom and pan around the tree. You can also print the current
     view.

   Tip

  Hold the Ctrl key and scroll the mouse wheel to zoom the graph.

For more information on how to navigate the graph with a keyboard, see Accessibility
features for the collection relationship diagram.

Next steps
Deploy and manage content for Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1099 -->

Microsoft Connected Cache with
Configuration Manager
Applies to: Configuration Manager (current branch)

You can install a Microsoft Connected Cache server on your distribution points. By caching this
content on-premises, your clients can benefit from the Delivery Optimization feature that can
help to protect WAN links.

This cache server acts as an on-demand transparent cache for content downloaded by Delivery
Optimization. Use client settings to make sure this server is offered only to the members of the
local Configuration Manager boundary group.

This cache is separate from Configuration Manager's distribution point content. If you choose the
same drive as the distribution point role, it stores content separately.

Supported scenarios
Connected Cache supports the following scenarios:

     Co-managed clients with workloads shifted to Intune that receive Win32 app assignments
     from Microsoft Intune. For more information, see Support for Intune Win32 apps.

     Cloud-only devices, such as Intune-enrolled devices without the Configuration Manager
     client. For more information, see Support for cloud-managed devices.

Supported content types
When clients download cloud-managed content, they use Delivery Optimization from the cache
server installed on your distribution point. Cloud-managed content includes the following types:

     For co-management workloads moved to Intune:

        Windows Update client policies: Windows feature and quality updates assigned from
        Intune

        Office Click-to-Run apps: Microsoft 365 Apps and updates

        Client apps: Microsoft Store apps (UWP) and updates

<!-- p.1100 -->

        Endpoint Protection: Windows Defender definition updates

     Intune Win32 apps

     For a complete list visit: Types of download content supported by Delivery Optimization and
     Microsoft Connected Cache

  ２ Warning

  Connected Cache only provides content for co-managed devices with workloads shifted to
  Intune. It doesn't support content related any deployments that originate from
  Configuration Manager, like software updates with an integrated software update point.

How it works
When you configure clients to use the Connected Cache server, they no longer request Microsoft
cloud-managed content from the internet. Clients request this content from the cache server
installed on the distribution point. The on-premises server caches this content using the IIS
feature for Application Request Routing (ARR). Then the cache server can quickly respond to any
future requests for the same content. If the Connected Cache server is unavailable, clients
download the content from the internet. Clients also use Delivery Optimization to download
portions of the content from peers in their network.

<!-- p.1101 -->

1. Client checks for updates and gets the address for the content delivery network (CDN).

2. Configuration Manager configures Delivery Optimization (DO) settings on the client,
  including the cache server name.

3. Client A requests content from the Connected Cache server.

4. If the cache doesn't include the content, then the Connected Cache server gets it from the
  CDN.

5. If the cache server fails to respond, the client downloads the content from the CDN. To
  delay this behavior, set the
  DelayCacheServerFallbackForeground/DelayCacheServerFallbackBackground setting(s) to
  avoid the immediate fallback.

6. Clients will also use DO to get pieces of the content from peers, such as client B and client
  C.

<!-- p.1102 -->

Prerequisites and limitations

  ７ Note

  Additional prerequisites apply to the scenario for co-managed clients and Intune Win32
  apps. For more information, see Support for Intune Win32 apps.

Supported clients
Connected Cache and Delivery Optimization only support clients running a supported version of
Windows 10 or later.

Licensing
You need one of the following license subscriptions for each device that gets content from a
Connected Cache-enabled distribution point:

     Windows Enterprise E3 or E5, included in Microsoft 365 F3, E3, or E5

     Windows Education A3 or A5, included in Microsoft 365 A3 or A5

     Windows Virtual Desktop Access (VDA) E3 or E5

Distribution point
Connected Cache with Configuration Manager requires an on-premises distribution point, with
the following configurations:

     Running a currently supported version of Windows Server.

     Microsoft .NET Framework version 4.8 or later. For more information, see .NET Framework
     system requirements.

     The default web site enabled on port 80.

     Don't preinstall the IIS Application Request Routing (ARR) feature. Connected Cache installs
     ARR and configures its settings. Microsoft can't guarantee that the Connected Cache's ARR
     configuration won't conflict with other applications on the server that also use this feature.

     The Connected Cache application can use a proxy server for internet access. For more
     information, see Configure the proxy for a site system server.

<!-- p.1103 -->

   It's not supported to use a distribution point that has other site roles, for example, a
   management point. Enable Connected Cache on a site system server that only has the
   distribution point role.

Network access requirements
   The distribution point requires internet access to the Microsoft cloud. The specific URLs can
   vary depending upon the specific cloud-enabled content. Make sure to also allow the
   endpoints for delivery optimization. For more information, see Internet access requirements.

   For co-managed clients and Intune Win32 apps, allow the distribution point to access the
   endpoints for that scenario. For more information, see Network requirements for PowerShell
   scripts and Win32 apps.

   Clients technically only need access to the distribution point with the Connected Cache.
   Although it's best to also give clients access to the internet endpoints for the content, in
   case they need to fall back to the original source.

Enable Connected Cache
 1. In the Configuration Manager console, go to the Administration workspace, and select the
   Distribution Points node.

 2. Select an on-premises distribution point, and then in the ribbon select Properties.

 3. In the properties of the distribution point role, on the General tab, configure the following
   settings:

    a. Enable the option to Enable this distribution point to be used as Microsoft Connected
      Cache server

      Review the list of required license subscriptions, and then confirm your licenses.

   b. Local drive to be used: Select the disk to use for the cache. Automatic is the default
      value, which uses the disk with the most free space.Note 1

        ７ Note

        You can change this drive later. Any cached content is lost, unless you copy it to the
        new drive.

<!-- p.1104 -->

      c. Disk space: Select the amount of disk space to reserve in GB or a percentage of the total
        disk space. By default, this value is 100 GB.

       ７ Note

       The default cache size should be sufficient for most customers. You can adjust the
       cache size later.

       If the cache size on disk exceeds the allocated space, ARR clears space by removing
       content based on its built-in heuristics.

     d. Retain cache when disabling the Connected Cache server: If you remove the cache
        server, and you enable this option, the server keeps the cache's content on the disk.

   4. In client settings, in the Delivery Optimization group, configure the setting to Enable
     devices managed by Configuration Manager to use Microsoft Connected Cache servers
     for content download.

Note 1: About drive selection
If you select Automatic, when Configuration Manager installs the Connected Cache component,
it honors the NO_SMS_ON_DRIVE.SMS file. For example, the distribution point has the file
C:\NO_SMS_ON_DRIVE.SMS . Even if the C: drive has the most free space, Configuration Manager

configures Connected Cache to use another drive for its cache.

If you select a specific drive that already has the NO_SMS_ON_DRIVE.SMS file, Configuration
Manager ignores the file. Configuring Connected Cache to use that drive is an explicit intent. For
example, the distribution point has the file F:\NO_SMS_ON_DRIVE.SMS . When you explicitly
configure the distribution point properties to use the F: drive, Configuration Manager configures
Connected Cache to use the F: drive for its cache.

To change the drive after you install Connected Cache:

     Manually configure the distribution point properties to use a specific drive letter.

     If set to automatic, first create the NO_SMS_ON_DRIVE.SMS file. Then make some change
     to the distribution point properties to trigger a configuration change.

Automation
Automation via Windows PowerShell

<!-- p.1105 -->

Starting in version 2010, use the following parameters of the Set-CMDistributionPoint cmdlet to
configure the Connected Cache:

     EnableDoinc
     DiskSpaceUnit
     DiskSpaceDoinc
     LocalDriveDoinc
     RetainDoincCache
     AgreeDoincLicense

For more information, see the 2010 release notes.

Automation via the Configuration Manager SDK

You can use the Configuration Manager SDK to automate the configuration of Microsoft
Connected Cache settings on a distribution point. As is the case for all site roles, use the
SMS_SCI_SysResUse WMI class. For more information, see Programming the site roles.

When you update the SMS_SCI_SysResUse instance for the distribution point, set the following
properties:

     AgreeDOINCLicense: Set to 1 to accept the license terms.
     Flags: Enable |= 4 , disable &= ~4
     DiskSpaceDOINC: Set to Percentage or GB
     RetainDOINCCache: Set to 0 or 1
     LocalDriveDOINC: Set to Automatic , or a specific drive letter, such as C: or D:

Verify
On supported versions of Windows 10 or later, verify this behavior with the Get-
DeliveryOptimizationStatus Windows PowerShell cmdlet. In the cmdlet output, review the
BytesFromCacheServer value. For more information, see Monitor Delivery Optimization.

If the cache server returns any HTTP failure, the Delivery Optimization client falls back to the
original cloud source.

For more detailed information, see Troubleshoot Microsoft Connected Cache with Configuration
Manager.

Connected Cache version history

<!-- p.1106 -->

The following table lists key Connected Cache KB updates, the ConfigMgr versions each hotfix
applies to, and the corresponding DoincInstall.exe version.

                                                                                         ﾉ   Expand table

 KB                                     Applies to (ConfigMgr versions)     DoincInstall.exe version

 KB33247081                             2409, 2503, 2509, 2603              1.5.6.44280

 Configuration Manager version 2603     -                                   1.5.6.43080

 KB14978429                             2103-2207                           1.5.5.14088

 KB12819689                             2111                                1.5.5.9002

 KB5001600                              1910-2010                           1.5.4.1512

Support for Intune Win32 apps
When you enable Connected Cache on your Configuration Manager distribution points, they can
serve Microsoft Intune Win32 apps to co-managed clients. Starting June 16, 2026, Intune is
rolling out HTTPS for Win32 app content downloads          by region. During the rollout, some
tenants might still use HTTP until HTTPS is available in their region.

To support this change, you need:

      The latest Connected Cache version: either KB33247081 for versions 2409, 2503, 2509, and
      2603, or Configuration Manager version 2603.
      On a Configuration Manager distribution point with Microsoft Connected Cache (MCC)
      enabled, if the IIS HTTPS binding is configured to use a self-signed certificate, replace it with
      a certificate issued by a trusted certification authority (CA). For examples, see the
      instructions to request the certificate from internal PKI and bind it to the IIS website.
      Ensure that all client devices that download content from MCC trust the issuing CA.

   Tip

  You can cache other cloud-managed content without PKI certificates configured. This
  includes Windows updates, Microsoft 365 apps, and Microsoft Edge. Only Intune Win32
  apps require the HTTPS PKI certificate configuration.

Prerequisites

<!-- p.1107 -->

Client

       Update the client to the latest version

       Co-Managed with workloads shifted to Intune

       Devices must be on the intranet and in a boundary group where a Connected Cache
       enabled Distribution Point is added as a reference

       For Delivery Optimization peer-to-peer: the client device needs to have at least 4 GB of
       memory.

          Tip

         Use the following group policy setting: Computer Configuration > Administrative
         Templates > Windows Components > Delivery Optimization > Minimum RAM
         capacity (inclusive) required to enable use of Peer Caching (in GB).

Site

For Microsoft Connected Cache:

       Enable Connected Cache on a distribution point.

       The client and the Connected Cache-enabled distribution point need to be in the same
       boundary group. If a client isn't in a boundary group with a Connected Cache-enabled
       distribution point, it won't download content from a Connected Cache-enabled distribution
       point in a neighbor or site default boundary group.

       Enable the following client setting in the Delivery Optimization group:

       Enable devices managed by Configuration Manger to use Microsoft Connected Cache
       servers for content download

For Delivery Optimization peer-to-peer:

       Enable the following client settings in the Delivery Optimization group:
         Use Configuration Manager Boundary Groups for Delivery Optimization Group ID:
       Enable Allow peer downloads in this boundary group option for the Boundary Group that
       contains the client and the distribution point. For more information, see Boundary Group
       options.

<!-- p.1108 -->

  ） Important

  You do not need to set the options that enable Delivery Optimization peer-to-peer in order
  to use Microsoft Connected Cache.

Intune

     For apps managed in Intune, this feature only supports the Intune Win32 app type.
        Create and assign (deploy) a new app in Intune for this purpose. (Apps created before
        Intune version 1811 don't work.) For more information, see Win32 app management in
        Microsoft Intune.

     Enable co-management, and switch the Client apps workload to Pilot Intune or Intune. For
     more information, see the following articles:

     Workloads - Client apps

        How to enable co-management

        Switch workloads to Intune

        If in pilot, add the client to the pilot collection for Client Apps.

Support for cloud-managed devices
When you install a Microsoft Connected Cache on a Configuration Manager distribution point,
cloud-managed devices can use the on-premises cache. For example, a device that's managed by
Intune, but connects to the on-premises network. As long as the device can communicate with
the server, the cache is available to deliver content to these devices.

To configure the device to use the Microsoft Connected Cache, configure the DOCacheHost
policy. Set it to the FQDN or IP address of the Configuration Manager distribution point. For
more information on this policy, see Policy CSP - DeliveryOptimization.

To use Intune to configure this policy, use the DO Cache Host setting in Intune Delivery
Optimization profiles created after April 24, 2025. If your Intune profile was created before April
24, 2025, use the setting named Cache server host names. For more information, see Delivery
Optimization Windows devices in Intune.

When you enable this policy for cloud-managed devices, either type of device can request the
server to cache content, and either can download the content. If multiple devices request the

<!-- p.1109 -->

same content, no matter their management authority, they download supported and available
content from the Microsoft Connected Cache.

Next steps
Optimize Windows updates with Delivery Optimization

Troubleshoot Microsoft Connected Cache with Configuration Manager

Last updated on 06/22/2026

<!-- p.1110 -->

Troubleshoot Microsoft Connected Cache
with Configuration Manager
This article provides technical details about Microsoft Connected Cache with Configuration
Manager. Use it to help troubleshoot issues that you might have in your environment. For more
information on how it works and how to use it, see Microsoft Connected Cache with
Configuration Manager.

Verify
When you correctly install the Delivery Optimization cache server, and correctly configure clients,
they download from the cache server installed on your distribution point rather than the internet.

Verify this behavior on a client or on the server.

Verify on a client
Use the following workflow to verify the Microsoft Connected Cache configuration:

   1. Open a 64-bit PowerShell window as an administrator.

   2. Ensure the host is targeted by policy. If policy isn't set by Configuration Manager or Intune,
     set DOCacheHost to the distribution point FQDN or IP:

       PowerShell

       $parentKeyPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization"
       if (!(Test-Path $parentKeyPath)) {
           New-Item -Path $parentKeyPath -ItemType RegistryKey -Force -ErrorAction Stop
       | Out-Null
       }
       Set-ItemProperty -Path $parentKeyPath -Name "DOCacheHost" -Value "[DP IP Address
       or FQDN]" -ErrorAction Stop

   3. Verify HTTP delivery by running the following command, and replace the name or IP
     address of your server for <DoincServer> :

       PowerShell

       Invoke-WebRequest -URI "http://<DoincServer>/mscomtest/wuidt.gif" -Headers

<!-- p.1111 -->

    @{"Host"="b1.download.windowsupdate.com"}

  The output looks similar to the following example:

    PowerShell

    PS C:\WINDOWS\system32> Invoke-WebRequest -URI
    "http://SERVER01.CONTOSO.COM/mscomtest/wuidt.gif" -Headers
    @{"Host"="b1.download.windowsupdate.com"}

    StatusCode        : 200
    StatusDescription : OK
    Content           : {71, 73, 70, 56...}
    RawContent        : HTTP/1.1 200 OK
                        X-HW:
    1567797125.dop019.se2.t,1567797125.cds058.se2.s,1567797125.dop114.at2.r,156779712
    5.cds079.at2
                        .p,1567797125.cds058.se2.p
                        X-CCC: cdP+dRBgUCoZO1mezA9zhg2VwQ7P1JWTh9k+GhfQmu8=_SLwv...
    Headers           : {[X-HW,
    1567797125.dop019.se2.t,1567797125.cds058.se2.s,1567797125.dop114.at2.r,156779712
    5.cds079.a
                        t2.p,1567797125.cds058.se2.p], [X-CCC,

    cdP+dRBgUCoZO1mezA9zhg2VwQ7P1JWTh9k+GhfQmu8=_SLwvtSBQdT3uPQ5ikBe1ABMbdYIIncem+h5d
    tcLI6GY=],
                        [X-CID, 100], [Accept-Ranges, bytes]...}
    RawContentLength : 969710

  The following attributes indicate success:

        StatusCode : 200

        StatusDescription : OK

4. Verify MSIX download via HTTPS channel by requesting Microsoft Teams content from
  Connected Cache:

    PowerShell

    Add-AppxPackage "https://installer.teams.static.microsoft/production-windows-
    x64/25177.2002.3761.5185/MSTeams-x64.msix"

  Expected result: Download completes without error.

5. Verify that bytes were served by cache:

    PowerShell

<!-- p.1112 -->

       Get-DeliveryOptimizationStatus | Select-Object DownloadMode,
       TotalBytesDownloaded, BytesFromCacheServer

     Expected result: BytesFromCacheServer is greater than 0 .

   6. (Optional) In environments using DOINC/CDN byte reporting, interpret results as follows:

           CDN bytes equals DOINC bytes: 100% of bytes came from cache.

           DOINC bytes is 0 : 100% of bytes came from CDN.

           CDN bytes greater than DOINC bytes: Partial bytes came from cache.

  ７ Note

  You may observe an issue where Intune content isn't cached until the third request from the
  cache server. This can occur when the Intune CDN returns a VARY header that instructs
  content not to be cached.

Verify on the server
On the distribution point server, check the registry values at HKLM\SOFTWARE\Microsoft\Delivery
Optimization In-Network Cache . Verify that PrimaryDrivesInput value reflects the actual cache

location, like PrimaryDrivesInput\DOINC-E77D08D0-5FEA-4315-8C95-10D359D59294 . Note that
PrimaryDrivesInput can reference multiple drives (for example, C,D,E ).

Also, check the DoincSetup.log to confirm successful installation:

   1. On the distribution point server, navigate to \SMS_DP$\Ms.Dsp.Do.Inc.Setup\DoincSetup.log
     located at one of the logical drives.
   2. Open the file and scroll to the end.
   3. Verify that it contains entries similar to the following:

 Output

 Requesting content from the Delivery Optimization In-Network Cache (DOINC) instance...
 (Attempt #1)
      Started download of test content from http://localhost/mscomtest/cedtest/r20.gif
      Completed download of test content from
 http://localhost/mscomtest/cedtest/r20.gif
      Download response
           StatusCode:        OK
           ContentLength:     43
      Successful download of test content from
 http://localhost/mscomtest/cedtest/r20.gif

<!-- p.1113 -->

       Verifying downloaded content is present in primary disk cache: E:\DOINC-E77D08D0-
 5FEA-4315-8C95-10D359D59294\download.windowsupdate.com\mscomtest\cedtest\r20.gif.full
 (
 Found
 )
 Completed VerifyCacheNodeSetup.ps1
 Delivery Optimization In-Network Cache (DOINC) Install succeeded

Log files
     Application Request Routing (ARR) setup log: %temp%\arr_setup.log

     Connected Cache server setup log: \SMS_DP$\Ms.Dsp.Do.Inc.Setup\DoincSetup.log on the
     distribution point and DistMgr.log on the site server

     Internet Information Services (IIS) operational logs: By default,
     %SystemDrive%\inetpub\logs\LogFiles

     Connected Cache server operational log: C:\Doinc\Product\Install\Logs

         Tip

        Among other uses, this log can help you identify connectivity issues with the Microsoft
        cloud.

Setup error codes
When Configuration Manager installs the Connected Cache component on the distribution point,
the following table lists the possible error codes that might occur:

                                                                                            ﾉ   Expand table

 Error code      Error description

 0x00000000      Success

 0x00000BC2      Success, reboot required

 0x00000643      Generic install failure

 0x00D00001      Connected Cache setup can only be run if Internet Information Services (IIS) has been
                 installed

 0x00D00002      Connected Cache setup can only be run if a 'Default Web Site' exists on the server

<!-- p.1114 -->

Error code   Error description

0x00D00003   You can't install Connected Cache if Application Request Routing (ARR) is already installed

0x00D00004   Connected Cache setup can only be run if Application Request Routing (ARR) was installed
             by the Install.ps1 script

0x00D00005   Connected Cache setup requires a PowerShell session running as Administrator

0x00D00006   Connected Cache setup can only be run from a 64-bit PowerShell environment

0x00D00007   Connected Cache setup can only be run on a Windows Server

0x00D00008   Failure: The number of cache drives specified must match the number of cache drive size
             percentages specified

0x00D00009   Failure: A valid cache node ID must be supplied

0x00D0000A   Failure: A valid cache drive set must be supplied

0x00D0000C   Failure: A valid cache drive size percent set or cache drive size in GB must be supplied

0x00D0000D   Failure: A valid cache drive size percent set and cache drive size in GB cannot both be
             supplied

0x00D0000E   Failure: The number of cache drives specified must match the number of cache drive sizes in
             GB specified

0x00D0000F   Failure: Could not back up the applicationhost.config file from $AppHostConfig to
             $AppHostConfigDestinationName

0x00D00010   Failure: Could not back up the Default Web Site web.config file from $WebsiteConfigFilePath
             to $WebConfigDestinationName

0x00D00011   Failure: An exception occurred in Setup.ps1, method SetupFarmAndRewriteRules

0x00D00012   Failure: An exception occurred in Setup.ps1, method SetupFarmAndRewriteRules (v15 or v20)

0x00D00014   Failure: An exception occurred in SetupAllowableServerVariables.ps1

0x00D00015   Failure: An exception occurred in SetupFirewallRules.ps1

0x00D00017   Failure: An exception occurred in SetupARROutboundRules.ps1

0x00D00018   Failure: An exception occurred in SetupARRDiskCache.ps1

0x00D00019   Failure: An exception occurred in SetupARRProperties.ps1

0x00D0001A   Failure: An exception occurred in SetupARRHealthProbes.ps1

0x00D0001B   Failure: An exception occurred in VerifyIISSitesStarted.ps1

0x00D0001D   Failure: An exception occurred in VerifyCacheNodeSetup.ps1

<!-- p.1115 -->

 Error code    Error description

 0x00D0001E    You can't install Connected Cache if the Default Web Site isn't on port 80

 0x00D0001F    Failure: The cache drive allocation in percentage can't exceed 100, or another Install.ps1
               instance is already running

 0x00D00020    Failure: The cache drive allocation in GB can't exceed the drive's free space

 0x00D00021    Failure: The cache drive allocation in percentage must be greater than 0

 0x00D00022    Failure: The cache drive allocation in GB must be greater than 0

 0x00D00023    Failure: Connected Cache dependency installation failed

 0x00D00024    Failure: An exception occurred in RegisterScheduledTask_Maintenance

 0x00D00025    Failure: An exception occurred setting up the rewrite rules for HTTPS farm: $FarmName

 0x00D00026    Failure: An exception occurred setting up the rewrite rules for HTTP farm: $FarmName

 0x00D00027    You can't install Connected Cache because dependent software "Application Request Routing
               (ARR)" failed to install. See the log file located at %temp%\arr_setup.log

 0x00D00029    Connected Cache can't be installed because IIS is still running (iisreset /stop failed to stop IIS)

IIS configurations
The Connected Cache server installation makes several modifications to the IIS configuration on
the distribution point.

Application request routing
The Connected Cache server installs and configures IIS Application Request Routing                   . To avoid
potential conflicts, the distribution point can't already have this component installed.

Allowed server variables
After you install the Connected Cache server, the default website has the following local server
variables:

     HTTP_HOST
     QUERY_STRING
     X-CCC
     X-CID
     X-DOINC-OUTBOUND

<!-- p.1116 -->

Rewrite rules
The Connected Cache server adds the following rewrite rules:

Inbound rewrite rules

Connected Cache creates inbound rules using this naming pattern:

      Doinc_ForwardToFarm_<origin>_E77D08D0-5FEA-4315-8C95-10D359D59294

      Doinc_ForwardToFarm_v15_<origin>_E77D08D0-5FEA-4315-8C95-10D359D59294

      Doinc_ForwardToFarm_v20_<origin>_E77D08D0-5FEA-4315-8C95-10D359D59294

Depending on origin and transport mapping, additional protocol-specific variants can exist with
suffixes such as _HTTP , _HTTPS , or _HTTP_HTTPS .

In KB33247081: Connected Cache update for Microsoft Configuration Manager versions 2409,
2503, 2509 and 2603, inbound rewrite rules are created for these origins:

      assets.xbox.com

      assets1.xboxlive.com

      assets2.xboxlive.com

      au.b1.download.windowsupdate.com

      au.download.windowsupdate.com

      b.c2r.ts.cdn.office.net

      b1.download.windowsupdate.com

      betaswda01-mscdn.download.manage-beta.microsoft.com

      betaswda01.download.manage-beta.microsoft.com

      betaswdb01-mscdn.download.manage-beta.microsoft.com

      betaswdb01.download.manage-beta.microsoft.com

      bg.tscdn.m365.static.microsoft

      ctldl.windowsupdate.com

      d1.xboxlive.com

      d2.xboxlive.com

      dl.delivery.mp.microsoft.com

      dlassets.xboxlive.com

      dlassets2.xboxlive.com

      download.windowsupdate.com

      emdl.ws.microsoft.com

      f.c2r.ts.cdn.office.net

      fg.tscdn.m365.static.microsoft

<!-- p.1117 -->

installer.teams.static.microsoft

officecdn.microsoft.com

officecdn.microsoft.com.edgesuite.net

onedfswd-mscdn.download.manage-dogfood.microsoft.com

onedfswd.blob.core.windows.net

onedfswd.download.manage-dogfood.microsoft.com

sb.dl.delivery.mp.microsoft.com

sb.teams.static.microsoft

sb.tlu.dl.delivery.mp.microsoft.com

sf.dl.delivery.mp.microsoft.com

sf.teams.static.microsoft

sf.tlu.dl.delivery.mp.microsoft.com

shswda01-mscdn.download.manage-selfhost.microsoft.com

shswda01.download.manage-selfhost.microsoft.com

statics.teams.cdn.office.net

swda01-mscdn.manage.microsoft.com

swda01.manage.microsoft.com

swda02-mscdn.manage.microsoft.com

swda02.manage.microsoft.com

swdb01-mscdn.manage.microsoft.com

swdb01.manage.microsoft.com

swdb02-mscdn.manage.microsoft.com

swdb02.manage.microsoft.com

swdc01-mscdn.manage.microsoft.com

swdc01.manage.microsoft.com

swdc02-mscdn.manage.microsoft.com

swdc02.manage.microsoft.com

swdd01-mscdn.manage.microsoft.com

swdd01.manage.microsoft.com

swdd02-mscdn.manage.microsoft.com

swdd02.manage.microsoft.com

swdin01-mscdn.manage.microsoft.com

swdin01.manage.microsoft.com

swdin02-mscdn.manage.microsoft.com

swdin02.manage.microsoft.com

swdsw01-mscdn.manage.microsoft.com

swdsw01.manage.microsoft.com

<!-- p.1118 -->

     swdsw02-mscdn.manage.microsoft.com

     swdsw02.manage.microsoft.com

     tlu.dl.delivery.mp.microsoft.com

     xvcb1.xboxlive.com

     xvcb2.xboxlive.com

     xvcf1.xboxlive.com

     xvcf2.xboxlive.com

Outbound rewrite rules

     Doinc_Outbound_SetHeader_X_CID_E77D08D0-5FEA-4315-8C95-10D359D59294

     Doinc_Outbound_SetHeader_X_CCC_E77D08D0-5FEA-4315-8C95-10D359D59294

IIS custom headers
If requests with X-Forwarded-For headers are blocked on a proxy server, either allow the header
on the proxy server or change the custom header name in IIS for each server farm.

To change the custom header name for each server farm:

   1. Open IIS Manager.
   2. Select Server Farms.
   3. Select a server farm and the proxy icon.
   4. Under Custom Headers, change the value X-Forwarded-For to X-Forwarded-For-<custom-
     name> .

Manage server resources
Disk space required for each Connected Cache server might vary, based on your organization's
update requirements. Disk space of 100 GB should be enough to cache the following content:

     A feature update
     Two to three months of quality and Microsoft 365 Apps updates
     Microsoft Intune apps and Windows inbox apps

The Connected Cache server shouldn't consume much system memory or processor time. After
you install the Connected Cache server, if you notice significant process or memory resource
consumption, analyze the IIS and ARR log files.

If the IIS and ARR log files take up too much space on the server, there are several methods you
can use to manage the log files. For more information, see Managing IIS log file storage.

<!-- p.1119 -->

See also
Microsoft Connected Cache with Configuration Manager

Last updated on 06/30/2026

<!-- p.1120 -->

Run discovery for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You use one or more discovery methods in Configuration Manager to find device and
user resources that you can manage. You can also use discovery to identify network
infrastructure in your environment. There are several different methods you can use to
discover different things, and each method has its own configurations and limitations.

Overview of discovery
Discovery is the process by which Configuration Manager learns about the things you
can manage. The following are the available discovery methods:

      Active Directory Forest Discovery

      Active Directory Group Discovery

      Active Directory System Discovery

      Active Directory User Discovery

      Microsoft Entra user Discovery

      Microsoft Entra user Group Discovery

      Heartbeat Discovery

      Network Discovery

      Server Discovery

   Tip

  You can learn about the individual discovery methods in About discovery methods
  for Configuration Manager.

  For assistance in selecting which methods to use, and at which sites in your
  hierarchy, see Select discovery methods to use for Configuration Manager.
