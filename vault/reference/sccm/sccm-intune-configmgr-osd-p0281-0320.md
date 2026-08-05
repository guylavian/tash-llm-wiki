---
title: "OS deployment documentation — pages 281-320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0281-0320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0281-0320
family: sccm
documentKind: "doc"
abstract: "any other relevant information that helps to identify and differentiate the plan among others in the Configuration Manager site. The description field is optional, and has a limit of 256 characters. 4. On the Servicing Plan page, specify the Target Collection. Members of the col"
---

# OS deployment documentation — pages 281-320

<!-- p.281 -->

       any other relevant information that helps to identify and differentiate the
       plan among others in the Configuration Manager site. The description field is
       optional, and has a limit of 256 characters.

4. On the Servicing Plan page, specify the Target Collection. Members of the
  collection receive the Windows upgrades that the servicing plan defines.

    ） Important

    When you deploy a high-risk deployment, such as servicing plan, the Select
    Collection window displays only the custom collections that meet the
    deployment verification settings. Configure these settings in the site
    properties.

    High-risk deployments are always limited to custom collections, collections
    that you create, and the built-in Unknown Computers collection. When you
    create a high-risk deployment, you can't select a built-in collection such as All
    Systems. Uncheck Hide collections with a member count greater than the
    site's minimum size configuration to see all custom collections that contain
    fewer clients than the configured maximum size. For more information, see
    Settings to manage high-risk deployments.

    The deployment verification settings are based on the current membership of
    the collection. After you deploy the servicing plan, the collection membership
    isn't reevaluated for the high-risk deployment settings.

5. On the Deployment Ring page, configure the following settings:

       Select one of the following options to specify the Windows readiness state to
       which this servicing plan should apply:

          Semi-Annual Channel (Targeted): In this servicing model, feature updates
          are available as soon as Microsoft releases them.

          Semi-Annual Channel: This servicing channel is typically used for broad
          deployment. Windows 10 clients in the semi-annual channel receive the
          same build of Windows 10 as those devices in the targeted channel, just at
          a later time.

          For more information about servicing channels and what options are best
          for you, see Servicing channels.

<!-- p.282 -->

       How many days after Microsoft has published a new upgrade would you
       like to wait before deploying in your environment: If the current date is after
       the release date plus the number of days that you configure for this setting,
       Configuration Manager evaluates whether to include an upgrade in the
       deployment.

6. On the Upgrades page, configure the search criteria to filter the upgrades to add
  the service plan. It only adds upgrades that meet the specified criteria to the
  associated deployment. The following property filters are available:

       Architecture

       Language

       Product Category

       Required

          ） Important

          Set the Required field with a value of >=1 . Using this criteria makes sure
          that only applicable updates are added to the servicing plan.

       Superseded

       Title

  To view the upgrades that meet the specified criteria, select Preview.

7. On the Deployment Schedule page, configure the following settings:

       Schedule evaluation: Specify how Configuration Manager evaluates the
       available time and installation deadline times. It can either use UTC or the
       local time of the computer that runs the Configuration Manager console.

          ７ Note

          When you select local time, it uses the current time on the computer
          running the Configuration Manager console. If you then select As soon
          as possible for the Software available time or Installation deadline, it
          uses the current local time to evaluate when the upgrade is available or
          when a client installs it. If the client is in a different time zone, these
          actions will occur when the client's time reaches the evaluation time.

<!-- p.283 -->

Software available time: Select one of the following settings to specify when
the upgrade is available to clients:

   As soon as possible: Make the upgrade available to clients right away.
   When you create the deployment with this setting, Configuration Manager
   updates the client policy. At the next client policy polling cycle, clients
   become aware of the deployment, and can install the upgrade. This setting
   is the default and most common for the available time.

   Specific time: Make the upgrade available to clients at a specific time
   period after the servicing plan creates the deployment. When it creates the
   deployment with this setting, Configuration Manager updates the client
   policy. At the next client policy polling cycle, clients become aware of the
   deployment. The upgrade isn't available to install until after this specified
   date and time. Use this setting if you want to create the deployment
   several days before clients see it.

Installation deadline: Select one of the following settings to specify when to
require clients to install the upgrade:

   As soon as possible: Automatically install the upgrade right away. As soon
   as clients get this deployment, the start the upgrade.

   Specific time: Automatically install the upgrade at a specific time period
   after the servicing plan creates the deployment. Configuration Manager
   determines the deadline to install the upgrade by adding the configured
   Specific time interval to the Software available time. This setting is the
   default and most common for the installation deadline. By default it's
   seven days. In other words, by default clients receive the upgrade
   deployment at the next policy refresh, and have one week before it's
   required.

     ７ Note

     The actual installation deadline time is the displayed deadline interval
     plus a random amount of time up to 2 hours. This randomization
     reduces the potential impact of all clients in the collection installing
     the upgrade at the same time.

   Delay enforcement of this deployment according to user preferences, up
   to the grace period defined on the client: Select this option to honor the

<!-- p.284 -->

          Grace period for enforcement after deployment deadline (hours) client
          setting.

8. On the User Experience page, configure the following settings:

       User notifications: Specify whether to display notification of the upgrade in
       Software Center on the client at the available time. By default, it's set to Hide
       in Software Center and all notifications.

       Deadline behavior: Specify the behavior after the deadline and outside of
       any maintenance window. By default, the upgrade doesn't install and the
       system won't restart outside of a window. For more information about
       maintenance windows, see How to use maintenance windows.

       Device restart behavior: Specify whether to suppress the restart after
       Windows installs the upgrade. By default, the device restarts after the
       upgrade.

       Write filter handling for Windows Embedded devices: When you deploy an
       upgrade to Windows Embedded devices that use a write filter, configure
       when and how it commits the changes. When you deploy an upgrade to a
       Windows Embedded device, make sure that the device is a member of a
       collection that has a configured maintenance window.

       Software updates deployment re-evaluation behavior upon restart: To force
       another update deployment evaluation cycle after restart, select the option: If
       any update in this deployment requires a system restart, run updates
       deployment evaluation cycle after restart.

9. On the Deployment Package page, first select one of the following options:

       Select a deployment package: Select Browse to choose an existing
       deployment package for this upgrade content.

       No deployment package: Clients download content from peers or the
       Microsoft cloud.

       Create a new deployment package and configure the following additional
       settings:

        a. Name: Specify the name of the deployment package. This name must be
          unique and describes the package content. It's limited to 50 characters.

        b. Description: Optionally specify a description that provides additional
          information about the deployment package. The description is limited to

<!-- p.285 -->

           127 characters.

         c. Package source: Specify the location of the source files. Type a network
           path for the source location. For example: \\server\sharename\path . You
           can also select Browse to find a network location.

              Before you continue to the next page of the wizard, create the shared
              folder for the deployment package source files.

              The location that you specify can't be used by another software
              deployment package.

              The SMS Provider computer account and the user that's running the
              wizard to download the software updates must both have Write NTFS
              permissions on the download location. To reduce the risk of attackers
              tampering with the source files, restrict access to the download
              location.

              After Configuration Manager creates the deployment package, you can
              change the package source location in the deployment package
              properties. Before you change it, copy the content from the original
              package source to the new location.

         d. Sending priority: Specify the sending priority for the deployment package.
           Configuration Manager uses the sending priority when it sends the
           package to distribution points. It sends packages in priority order: high,
           medium, or low. If packages have identical priorities, the site sends them in
           the order in which you created them. If there's no backlog, the package
           processes immediately.

         e. Enable binary differential replication. For more information, see Binary
           differential replication.

10. If you created a new deployment package, you'll see the Distribution Points page
   next. Specify the distribution points or distribution point groups that host the
   upgrade content. For more information about distribution points, see Configure a
   distribution point.

11. If you selected an existing deployment package, you'll see the Download Location
   page next. Select one of the following options:

        Download software updates from the internet: The site server downloads
        the upgrade content from the internet. This setting is the default.

<!-- p.286 -->

           Download software updates from a location on the local network:
           Download the upgrade content from a local directory or shared folder. This
           setting is useful when the computer that runs the wizard doesn't have
           internet access. Any computer with internet access can preliminarily
           download the upgrade content.

 12. If you selected an existing deployment package, you'll also see the Language
     Selection page. The site downloads the upgrade content for the languages that
     you select, only if they're available. By default, the wizard selects the languages
     that you configured in the software update point properties.

 13. On the Summary page, review the settings. Select Next to create the servicing plan
     and complete the wizard.

After you complete the wizard, the site runs the servicing plan for the first time.

Modify a servicing plan
After you create a basic servicing plan from the Windows servicing dashboard, or you
need to change the settings for an existing servicing plan, go to properties for the
servicing plan.

  ７ Note

  You can configure settings in the properties for the servicing plan that aren't
  available in the wizard. The wizard uses default settings for the following areas:
  download settings, deployment settings, and alerts.

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Windows Servicing, and select the Servicing Plans node. Then select the
     servicing plan that you want to modify.

   2. On the Home tab of the ribbon, select Properties.

The following settings are available in the servicing plan properties that weren't
configured in the wizard:

Deployment Settings
     Use Wake-on-LAN to wake up clients for required deployments: Enable Wake On
     LAN at the deployment deadline. The site will send wake-up packets to computers
     for the deployment. By default, this setting isn't enabled.

<!-- p.287 -->

       ２ Warning

       Before you can use this option, configure computers and networks for Wake
       On LAN.

     Detail level: Specify the level of detail for the state messages that clients send to
     the site.

Download Settings
     Specify whether the client downloads and installs the upgrade when it's connected
     to a slow network or is using a fallback content location.

     Specify whether to have the client download and install the upgrade from a
     fallback distribution point when the content isn't available on a preferred
     distribution point.

     Specify whether to have clients download the content from Microsoft Update, if it's
     not available on distribution points.

       ） Important

       Don't use this setting for Windows servicing updates. Configuration Manager
       fails to download the Windows servicing updates from Microsoft Update.

     Specify whether to allow clients to download after an installation deadline when
     they use metered internet connections.

Alerts
Configure how Configuration Manager and System Center Operations Manager
generate alerts for this deployment.

You can review recent alerts from the Software Updates node in the Software Library
workspace.

Analyze SetupDiag errors
With the release of Windows 10, version 2004, the SetupDiag diagnostic tool is included
with Windows Setup. If there's an issue with the upgrade, SetupDiag automatically runs

<!-- p.288 -->

to determine the cause of the failure.

Starting in version 2010, Configuration Manager gathers and summarizes SetupDiag
results from feature update deployments with Windows servicing.

The Windows Servicing dashboard in the Software Library workspace of the
Configuration Manager console includes a tile for Collection Errors. Each bar shows the
number of devices that failed with the specified error code. For more information, see
Windows upgrade error codes.

Each bar shows the number of devices that failed with the specified error code. For more
information, see Windows upgrade error codes.

Next steps
For more information, see Fundamentals of Configuration Manager as a service and
Windows as a service.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.289 -->

Monitor operating system deployments
in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The Configuration Manager console provides the following ways to help you monitor
operating system deployment objects.

Alerts for operating system deployments
You can configure an alert in the task sequence deployment settings to notify
administrative users when compliance levels for the deployment are below the
configured percentage.

After you configure the alert settings, if the specified conditions occur, Configuration
Manager generates an alert. You can review task sequence deployment alerts at the
following locations:

   1. Review recent alerts in the Operating Systems node in the Software Library
      workspace.

   2. Manage the configured alerts in the Alerts node in the Monitoring workspace.

Task sequence deployment status
After you deploy a task sequence, you can monitor the deployment status. Use the
following procedure to monitor the deployment status for a task sequence.

To monitor deployment status

   1. In the Configuration Manager console, click Monitoring.

   2. In the Monitoring workspace, click Deployments.

   3. Click the task sequence for which you want to monitor the deployment status.

   4. On the Home tab, in the Deployment group, click View Status.

   Tip

<!-- p.290 -->

        When an upgrade is initiated, status message 52200 is generated. This
        contains the user that did the upgrade.
        Starting in version 2203, you can perform client notification actions, including
        Run Scripts, from the Deployment Status view.Use the right-click menu on
        either a group of clients in a Category or a single client in the Asset details
        pane to display the client notification actions.

Operating system deployment reports
There are many predefined operating system deployment reports available. They are
organized in several categories and can be used to report on specific information about
state migration and task sequence deployments. In addition to using the preconfigured
reports, you can also create custom software update reports according to the needs of
your enterprise. For more information, see Operations and maintenance for reporting.

Monitor content
You can monitor content in the Configuration Manager console to review the status for
all package types in relation to the associated distribution points. This can include the
content validation status for the content in the package, the status of content assigned
to a specific distribution point group, the state of content assigned to a distribution
point, and the status of optional features for each distribution point (content validation,
PXE, and multicast).

Content status monitoring
The Content Status node in the Monitoring workspace provides information about
content packages. You can review general information about the package, distribution
status for the package, and detailed status information about the package. Use the
following procedure to view content status.

To monitor content status
   1. In the Configuration Manager console, click Monitoring.

   2. In the Monitoring workspace, expand Distribution Status, and then click Content
     Status. The packages are displayed.

   3. Select the package for which to view detailed status information.

<!-- p.291 -->

   4. On the Home tab, click View Status. Detailed status information for the package is
     displayed.

Distribution point group status
The Distribution Point Group Status node in the Monitoring workspace provides
information about distribution point groups. You can review general information about
the distribution point group, such as distribution point group status and compliance
rate, as well as detailed status information for the distribution point group. Use the
following procedure to view distribution point group status.

To monitor distribution point group status

   1. In the Configuration Manager console, click Monitoring.

   2. In the monitoring workspace, expand Distribution Status, and then click
     Distribution Point Group Status. The distribution point groups are displayed.

   3. Select the distribution point group for which to view detailed status information.

   4. On the Home tab, click View Status. Detailed status information for the
     distribution point group is displayed.

Distribution point configuration status
The Distribution Point Configuration Status node in the Monitoring workspace
provides information about the distribution point. You can review which attributes are
enabled for the distribution point, such as the PXE, Multicast, and content validation.
You can also view detailed status information for the distribution point. Use the
following procedure to view distribution point configuration status.

To monitor distribution point configuration status
   1. In the Configuration Manager console, click Monitoring.

   2. In the monitoring workspace, expand Distribution Status, and then click
     Distribution Point Configuration Status. The distribution points are displayed.

   3. Select the distribution point for which to view distribution point status information.

   4. In the results pane, click the Details tab. Status information for the distribution
     point is displayed.

<!-- p.292 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.293 -->

Debug a task sequence
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The task sequence debugger is a troubleshooting tool. You deploy a task sequence in
debug mode to a small collection. It lets you step through the task sequence in a
controlled manner to aid troubleshooting and investigation. The debugger currently
runs on the same device as the task sequence engine, it's not a remote debugger.

   Tip

  This feature was first introduced in version 1906 as a pre-release feature. Beginning
  with version 2203, it's no longer a pre-release feature.

  Configuration Manager doesn't enable this optional feature by default. Before
  using it, you need to enable this feature. For more information, see Enable optional
  features from updates.

Prerequisites
      Update the Configuration Manager client on the target device

      Sign in to the target device as a user in the local Administrators group. The
      debugger only runs for administrators.

      Update the boot image associated with the task sequence to make sure it has the
      latest client version

Start the tool
   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Operating Systems, and select Task Sequences.

   2. Select a task sequence. In the Deployment group of the ribbon, select Debug.

         Tip

        Alternatively, set the variable TSDebugMode to TRUE on a collection or
        computer object to which the task sequence is deployed. Any device that has

<!-- p.294 -->

       this variable set will put any task sequence deployed to it into debug mode.

   3. Create a debug deployment. The deployment settings are the same as a normal
     task sequence deployment. For more information, see Deploy a task sequence.

       ７ Note

       You can only select a small collection for a debug deployment. It only displays
       device collections with 10 or less members.

Use the task sequence variable TSDebugOnError to automatically start the debugger
when the task sequence returns an error. For more information, see Task sequence
variables - TSDebugOnError.

Use the tool
When the task sequence runs on the device, the Task Sequence Debugger window
opens similar to the following screenshot:

<!-- p.295 -->

The debugger includes the following controls:

     Step: From the current position, run only the next step in the task sequence.

       ７ Note

       When the task sequence is in debug mode, if a step returns a fatal error, the
       task sequence doesn't fail as normal. This behavior gives you the option to
       retry a step after you make an external change.

     Run: From the current position, run the task sequence normally to the end, the
     next break point, or if a step fails. Before you use this action, make sure to set any
     break points with the Set Break action.

     Set Current: Select a step in the debugger and then select Set Current. This action
     moves the current pointer to that step. This action allows you to skip steps or
     move backwards.

       ２ Warning

       The debugger doesn't consider the type of step when you change the current
       position in the sequence. Some steps may set task sequence variables that are
       required for condition evaluation by later steps. If run out of order, some
       steps may fail or cause significant damage to a device. Use this option at your
       own risk.

     Set Break: Select a step in the debugger and then select Set Break. This action
     adds a break point in the debugger. When you Run the task sequence, it stops at a
     break.

        Before you use the Run action, set break points.

        If you create a break point in the debugger, and then the task sequence restarts
        the computer, the debugger keeps your break points after restart.

     Clear All Breaks: Remove all break points.

     Log File: Opens the current task sequence log file, smsts.log, with CMTrace. You
     can see log entries when the task sequence engine is "Waiting for the debugger."

     Cmd Prompt: In Windows PE, opens a command prompt.

     Cancel: Close the debugger, and fail the task sequence.

<!-- p.296 -->

     Quit: Detach and close the debugger, but the task sequence continues to run
     normally.

The Task Sequence Variables window shows the current values for all variables in the
task sequence environment. For more information, see Task sequence variables. If you
use the Set Task Sequence Variable step with the option to Do not display this value,
the debugger doesn't display the variable value. You can't edit the variable values in the
debugger.

  ７ Note

  Some task sequence variables are for internal use only, and not listed in the
  reference documentation.

The task sequence debugger continues to run after a Restart Computer step. The
debugger keeps your break points after restart. Even though the task sequence may not
require it, since the debugger requires user interaction, you need to sign in to Windows
to continue. If you don't sign in after one hour to continue debugging, the task
sequence fails.

It also steps into a child task sequence with the Run Task Sequence step. The debugger
window shows the steps of the child task sequence along with the main task sequence.

Known issues
If you target both a normal deployment and debug deployment to the same device
through multiple deployments, the task sequence debugger may not launch.

See also
     About task sequence steps
     Task sequence variables
     How to use task sequence variables
     Deploy a task sequence

Feedback
Was this page helpful?    Yes    No

<!-- p.297 -->

Provide product feedback

<!-- p.298 -->

Configure pre-cache content for task
sequences
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The pre-cache feature for available deployments of task sequences lets clients download
relevant content before a user installs the task sequence. The client can pre-cache
content for task sequences that upgrade an OS or install an OS image.

For example, you only want a single in-place upgrade task sequence for all users, and
have many architectures and languages. In previous versions, the content starts to
download when the user installs an available task sequence deployment from Software
Center. This delay adds more time before the installation is ready to start. All content
referenced in the task sequence is downloaded. This content includes the OS upgrade
package for all languages and architectures. If each upgrade package is roughly 3 GB in
size, the total content is very large.

Pre-cache content gives you the option for the client to only download the applicable
content and all other referenced content as soon as it receives the deployment. When
the user selects Install in Software Center, the content is ready. The installation starts
quickly because the content is on the local hard drive.

Use pre-caching to reduce bandwidth consumption of the following content types:

      OS upgrade packages
      OS images
      Driver packages
      Packages

  ７ Note

  Starting in version 2103, if you use a feature update with the Upgrade OS task
  sequence step, the option to Pre-download content for this task sequence doesn't
  apply to feature updates.

Configure pre-caching
There are three steps to configure the pre-cache feature:

<!-- p.299 -->

   1. Create and configure the packages
   2. Create a task sequence with conditional steps
   3. Deploy the task sequence and enable pre-caching

1. Create and configure the packages
The client evaluates attributes of the packages to determine which content it downloads
during pre-caching.

OS upgrade package
Create OS upgrade packages for specific architectures and languages. Specify the
Architecture and Language on the Data Source tab of its properties.

OS image
Create OS images for specific architectures and languages. Specify the Architecture and
Language on the Data Source tab of its properties.

Driver package

Create driver packages for specific hardware models. Specify the Model on the General
tab of its properties.

To determine which driver package it downloads during pre-caching, the client evaluates
the model against the Name property of the Win32_ComputerSystemProduct WMI
class.

   Tip

  The actual query uses a LIKE statement with wildcards: select * from
  win32_computersystemproduct where name like "%yourstring%" . For example, if you

  specify Surface as the model, the query matches all models that include that string.

Package

Create packages for specific architectures and languages. Specify the Architecture and
Language on the General tab of its properties.

<!-- p.300 -->

2. Create a task sequence
Create a task sequence with conditional steps for the different languages and
architectures, or different hardware models for driver packages.

                                                                       ﾉ   Expand table

 Content                                     Step

 OS upgrade package                          Upgrade OS

 OS image                                    Apply OS Image

 Driver package                              Apply Driver Package

 Package                                     Install Package

For example, the following Upgrade OS step uses the English version:

<!-- p.301 -->

   Tip

  The following WMI query is recommended for the English (United States) OS and
  64-bit architecture:

    WMI

    SELECT * FROM Win32_OperatingSystem WHERE OSArchitecture LIKE '%64%'
    AND OSLanguage='1033'

  First add the language by selecting the Operating System Language condition.
  Then edit the WMI query to include the architecture clause.

3. Deploy the task sequence
Deploy the task sequence. For the pre-cache feature, configure the following settings:

     On the General tab, select Pre-download content for this task sequence.

<!-- p.302 -->

    ７ Note

    Starting in version 2103, if you use a feature update with the Upgrade OS task
    sequence step, this option doesn't apply to feature updates.

  On the Deployment settings tab, configure the task sequence as Available.

  On the Scheduling tab, choose the currently selected time for the setting,
  Schedule when this deployment will be available. The client starts pre-caching
  content at the deployment's available time. When a targeted client receives this
  policy, the available time is in the past, so pre-cache download starts right away. If
  the client receives this policy but the available time is in the future, the client
  doesn't start pre-caching content until the available time occurs.

  On the Distribution Points tab, configure the Deployment options settings. If the
  content isn't pre-cached before a user starts the installation, the client uses these
  settings.

    ） Important

    For a task sequence that installs an OS image, don't use the deployment
    option to Download content locally when needed by the running task
    sequence. When the task sequence wipes the disk before it applies the OS
    image, it removes the client cache. Since the content is gone, the task
    sequence fails. These deployment options are dynamic based on other
    options you select for the deployment. For more information, see Deploy a
    task sequence.

User experience
  When the client receives the deployment policy, it starts to pre-cache the content
  after the deployment's available time. This content includes all referenced
  packages, but only the OS upgrade package that matches the architecture and
  language attributes on the package.

  When the client makes the deployment available to users, a notification displays to
  inform users about the new deployment. Now the task sequence is visible in
  Software Center. The user can go to Software Center and select Install to start the
  installation.

<!-- p.303 -->

     If the client hasn't fully pre-cached the content when the user installs the task
     sequence, then the client uses the settings that you specify for the Deployment
     options on the Distribution Points tab of the deployment.

See also
     Create a task sequence to upgrade an OS

     Scenario to upgrade Windows to the latest version

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.304 -->

Create task sequence media
Article • 12/15/2023

Applies to: Configuration Manager (current branch)

You can use media to capture an OS image from a reference computer or to deploy an
OS to a destination computer in your Configuration Manager environment. The media
that you create can be a CD, DVD set, or a USB flash drive.

Media is used mostly to deploy an OS on computers that don't have a network
connection or that have a low-bandwidth connection to the site. However, you can also
use media to start an OS deployment outside of an existing Windows OS. This method is
useful when there's no OS, the OS isn't working, or you want to repartition the disk.

Deployment media includes bootable media, standalone media, and prestaged media.
The content of the media varies, depending on what type of media that you use. For
example, standalone media contains the task sequence that deploys the OS. Other types
of media retrieve task sequences from the management point.

  ） Important

  As a security best practice, always assign a password to help protect the task
  sequence media. Assigning a password to the media not only prevents someone
  without the password from running a task sequence when using the media, but it
  also properly encrypts the task sequence environment on the media. The task
  sequence environment includes the task sequence steps and their variables.

  Using a password doesn't encrypt the remaining content of the task sequence
  media such as packages. Don't include any sensitive information in task sequence
  packages such as scripts. Store and implement all sensitive information by using
  task sequence variables.

  ） Important

  To create task sequence media, you must be an administrator on the computer
  where you run the Configuration Manager console. If you're not an administrator,
  you're prompted for administrator credentials when you start the Create Task
  Sequence Media wizard.

<!-- p.305 -->

Capture media
Capture media allows you to capture an OS image from a reference computer. Capture
media contains the boot image that starts the reference computer and the task
sequence that captures the OS image.

Bootable media
Bootable media contains the following components:

     The boot image
     Optional prestart commands and their required files
     Configuration Manager binaries

When the destination computer starts, it connects to the network and retrieves the task
sequence, the OS image, and any other required content from the network. Because the
task sequence isn't on the media, you can change the task sequence or content without
having to recreate the media.

Starting in version 2006, bootable media can download cloud-based content. The device
still needs an intranet connection to the management point. It can get content from a
content-enabled cloud management gateway (CMG). For more information, see
Bootable media support for cloud-based content.

Prestaged media
Prestaged media allows you to apply bootable media and an OS image to a hard disk
before the provisioning process. The prestaged media is a Windows Image (WIM) file.
The manufacturer can install it to the bare-metal computer during their build process.
Or you can use it in a staging center that's not connected to the production
Configuration Manager environment.

Prestaged media contains the boot image used to start the destination computer and
the OS image that's applied to the destination computer. You can also specify
applications, packages, and driver packages to include as part of the prestaged media.
The task sequence that deploys the OS isn't included in the media. When you deploy a
task sequence that uses prestaged media, the client checks the local task sequence
cache for valid content first. If the content can't be found or has been revised, the client
downloads the content from a distribution point or peer.

You apply prestaged media to the hard drive of a new computer before you send the
computer to the user. When the computer starts for the first time after you've applied

<!-- p.306 -->

the prestaged media, the computer starts in Windows PE. It connects to a management
point to locate the task sequence that completes the OS deployment process.

Standalone media
Standalone media contains everything that's required to deploy the OS. This content
includes the task sequence and any other required content. Because everything is on the
media, the required disk space is larger than for other types of media.

Considerations when using HTTPS
When you configure your management points and distribution points to use HTTPS,
create boot media and prestaged media at a primary site, not the central administration
site. Also, consider the following point to help you determine whether to configure the
media as dynamic or site-based:

     To configure the media as dynamic media, all primary sites must have the root
     certificate authority (CA) of the site from which you created the media. You can
     import the root CA to all primary sites in your hierarchy.

     When primary sites in your Configuration Manager hierarchy use different root
     CAs, you must use site-based media at each site.

Next steps
     Create capture media

     Create bootable media

     Create prestaged media

     Create standalone media

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.307 -->

Create stand-alone media
Article • 12/14/2023

Applies to: Configuration Manager (current branch)

Stand-alone media in Configuration Manager contains everything required to deploy
the OS on a computer without a network connection.

Use stand-alone media with the following OS deployment scenarios:

      Refresh an existing computer with a new version of Windows

      Install a new version of Windows on a new computer (bare metal)

      Upgrade Windows to the latest version

Usage
Stand-alone media includes the task sequence that automates the steps to install the
OS, and all other required content. This content includes the boot image, OS image, and
device drivers. Because the stand-alone media stores everything to deploy the OS, it
requires more disk space than required for other types of media.

When you create stand-alone media on a CAS, the client retrieves its assigned site code
from Active Directory. Stand-alone media created at child sites automatically assigns to
the client the site code for that site.

Prerequisites
Before you create stand-alone media by using the Create Task Sequence Media Wizard,
be sure that all of these conditions are met.

Create a task sequence to deploy an OS
As part of the stand-alone media, specify the task sequence to deploy an OS. For more
information, see Create a task sequence to install an OS.

Unsupported actions for stand-alone media

The following actions aren't supported for stand-alone media:

<!-- p.308 -->

     The Auto Apply Drivers step in the task sequence. Stand-alone media doesn't
     support automatic application of device drivers from the driver catalog. Use the
     Apply Driver Package step to make a specified set of drivers available to Windows
     Setup.

     The Download Package Content step in the task sequence. The management point
     information isn't available on stand-alone media, so the step fails trying to
     enumerate content locations.

     Installing software updates.

     Installing software before deploying the OS.

     Custom task sequences for non-OS deployments.

     Associating users with the destination computer to support user device affinity.

     Dynamic package installs via the Install Packages step.

     Dynamic application installs via the Install Application step.

     The Use pre-production client package when available setting in the Setup
     Windows and ConfigMgr task sequence step. For more information about this
     setting, see Setup Windows and ConfigMgr.

Known issue with Install Package step and media created at the
central administration site
An error might occur if your task sequence includes the Install Package step and you
create the stand-alone media at a central administration site (CAS). The CAS doesn't
have the necessary client configuration policies. These policies are required to enable
the software distribution agent when the task sequence runs. The following error might
appear in the CreateTsMedia.log file: WMI method
SMS_TaskSequencePackage.GetClientConfigPolicies failed (0x80041001)

For stand-alone media that includes an Install Package step, create the stand-alone
media at a primary site that has the software distribution agent enabled.

Alternatively, use a custom Run PowerShell Script step. Add it after the Setup Windows
and ConfigMgr step and before the first Install Package step. The Run PowerShell
Script step runs the following commands to enable the software distribution agent
before the first Install Package step:

  PowerShell

<!-- p.309 -->

  $namespace = "root\ccm\policy\machine\requestedconfig"
  $class = "CCM_SoftwareDistributionClientConfig"
  $classArgs = @{
      ComponentName = 'Enable SWDist'
      Enabled = 'true'
      LockSettings='TRUE'
      PolicySource='local'
      PolicyVersion='1.0'
      SiteSettingsKey='1'
  }
  Set-WmiInstance -Namespace $namespace -Class $class -Arguments $classArgs -
  PutType CreateOnly

Distribute all content associated with the task sequence
Distribute all content that the task sequence requires to at least one distribution point.
This content includes the boot image, OS image, and other associated files. The wizard
gathers the content from the distribution point when it creates the media.

Your user account needs at least Read access rights to the content library on that
distribution point. For more information, see Distribute content.

Prepare the removable USB drive
If you're using a removable USB drive, connect it to the computer where you run the
Create Task Sequence Media wizard. The USB drive must be detectable by Windows as a
removal device. The wizard writes directly to the USB drive when it creates the media.

Stand-alone media uses a FAT32 file system. You can't create stand-alone media on a
removable USB drive whose content contains a file over 4 GB in size. This doesn't
include WIM files since Configuration Manager will split WIM files over 4 GB so that they
are under 4 GB and compatible with FAT32 files systems.

Create an output folder
Before you run the Create Task Sequence Media Wizard to create media for a CD or DVD
set, create a folder for the output files it creates. Media that it creates for a CD or DVD
set is written as an .ISO file directly in the folder.

Process

<!-- p.310 -->

1. In the Configuration Manager console, go to the Software Library workspace,
  expand Operating Systems, and select the Task Sequences node.

2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence
  Media. This action starts the Create Task Sequence Media Wizard.

3. On the Select Media Type page, specify the following options:

       Select Stand-alone media.

       Optionally, if you want to only allow the OS to be deployed without requiring
       user input, select Allow unattended operating system deployment.

          ） Important

          When you select this option, the user isn't prompted for network
          configuration information or for optional task sequences. If you
          configure the media for password protection, the user is still prompted
          for a password.

4. On the Media Type page, specify whether the media is a Removable USB drive or
  a CD/DVD set. Then configure the following options:

    ） Important

    Media uses a FAT32 file system. You can't create media on a USB drive whose
    content contains a file over 4 GB in size. This doesn't include WIM files since
    Configuration Manager will split WIM files over 4 GB so that they are under 4
    GB and compatible with FAT32 files systems.

       If you select Removable USB drive, select the drive where you want to store
       the content.
          Format removable USB drive (FAT32) and make bootable: By default, let
          Configuration Manager prepare the USB drive. Many newer UEFI devices
          require a bootable FAT32 partition. However, this format also limits the
          size of files and overall capacity of the drive. If you've already formatted
          and configured the removable drive, disable this option.

          ） Important

          It is important when creating stand-alone media on a removable USB
          drive that the removable USB drive is created directly via the

<!-- p.311 -->

  Configuration Manager console using the Removable USB drive option.
  Creating an ISO via the CD/DVD set option and then copying the
  contents of the mounted ISO to a removable USB drive formatted FAT32
  may not work since WIM files over 4 GB may not be split when using the
  CD/DVD set option. FAT32 does not support files over 4 GB. Stand-alone
  media on removable USB drives need to be formatted FAT32 so that
  they are bootable on UEFI devices. UEFI devices will only boot from
  FAT32 volumes.

If you select CD/DVD set, specify the capacity of the media (Media size) and
the name and path of the output file (Media file). The wizard writes the
output files to this location. For example:
\\servername\folder\outputfile.iso

If the capacity of the media is too small to store the entire content, it creates
multiple files. Then you need to store the content on multiple CDs or DVDs.
When it requires multiple media files, Configuration Manager adds a
sequence number to the name of each output file that it creates.

If you deploy an application along with the OS, and the application can't fit
on a single media, Configuration Manager stores the application across
multiple media. When the stand-alone media is run, Configuration Manager
prompts the user for the next media where the application is stored.

  ） Important

  If you select an existing .iso image, the Task Sequence Media Wizard
  deletes that image from the drive or share as soon as you proceed to
  the next page of the wizard. The existing image is deleted, even if you
  then cancel the wizard.

Staging folder: The media creation process can require a lot of temporary
drive space. By default this location is similar to the following path:
%UserProfile%\AppData\Local\Temp . To give you greater flexibility with where

to store these temporary files, change this value to another drive and path.

Media label: Add a label to task sequence media. This label helps you better
identify the media after you create it. The default value is Configuration
Manager . This text field appears in the following locations:

<!-- p.312 -->

          If you mount an ISO file, Windows displays this label as the name of the
          mounted drive

          If you format a USB drive, it uses the first 11 characters of the label as its
          name

          Configuration Manager writes a text file called MediaLabel.txt to the root
          of the media. By default, the file includes a single line of text:
           label=Configuration Manager . If you customize the label for media, this

          line uses your custom label instead of the default value.

       Include autorun.inf file on media: Configuration Manager doesn't add an
       autorun.inf file by default. This file is commonly blocked by antimalware
       products. For more information on the AutoRun feature of Windows, see
       Creating an AutoRun-enabled CD-ROM Application. If still necessary for your
       scenario, select this option to include the file.

5. On the Security page, specify the following options:

       Protect media with a password: Enter a strong password to help protect the
       media from unauthorized access. When you specify a password, the user
       must provide that password to use the media.

          ） Important

          As a security best practice, always assign a password to help protect the
          stand-alone media. Assigning a password to the media not only
          prevents someone without the password from running a task sequence
          when using the media, but it also properly encrypts the task sequence
          environment on the media. The task sequence environment includes the
          task sequence steps and their variables.

          Using a password doesn't encrypt the remaining content of the stand-
          alone media such as packages. Don't include any sensitive information in
          task sequence packages such as scripts. Store and implement all
          sensitive information by using task sequence variables.

       Select date range for this stand-alone media to be valid: Set optional start
       and expiration dates on the media. This setting is disabled by default. The
       dates are compared to the system time on the computer before the stand-
       alone media runs. When the system time is earlier than the start time or later

<!-- p.313 -->

         than the expiration time, the stand-alone media doesn't start. These options
         are also available by using the New-CMStandaloneMedia PowerShell cmdlet.

 6. On the Stand-Alone CD/DVD page, select the task sequence that deploys the OS.
   You can only select those task sequences that are associated with a boot image.
   Verify the list of content referenced by the task sequence.

         Detect associated application dependencies and add them to this media:
         Also add content to the media for application dependencies.

            Tip

           If you don't see expected application dependencies, deselect and then
           reselect this option to refresh the list.

 7. On the Select Application page, specify additional application content to include
   as part of the media file.

 8. On the Select Package page, specify additional package content to include as part
   of the media file.

 9. On the Select Driver Package page, specify additional driver package content to
   include as part of the media file.

10. On the Distribution Points page, specify the distribution points that contain the
   required content.

   Configuration Manager only displays distribution points that have the content.
   Distribute all of the content associated with the task sequence to at least one
   distribution point before you continue. After you distribute the content, refresh the
   distribution point list. Remove any distribution points that you already selected on
   this page, go to the previous page, and then back to the Distribution Points page.
   Alternatively, restart the wizard. For more information, see Distribute referenced
   content and Manage content and content infrastructure.

11. On the Customization page, specify the following options:

         Add any variables that the task sequence uses.

         Enable prestart command: Specify any prestart commands that you want to
         run before the task sequence runs. Prestart commands are a script or an
         executable that can interact with the user in Windows PE before the task
         sequence runs. For more information, see Prestart commands for task
         sequence media.

<!-- p.314 -->

               Tip

              During media creation, the task sequence writes the package ID and
              prestart command-line, including the value for any task sequence
              variables, to the CreateTSMedia.log file on the computer that runs the
              Configuration Manager console. You can review this log file to verify the
              value for the task sequence variables.

           If the prestart command requires any content, select the option to Include
           files for the prestart command.

 12. Complete the wizard.

The stand-alone media files (.ISO) are created in the destination folder. If you selected
CD/DVD set, copy the output files to a set of CDs or DVDs.

Next steps
Use stand-alone media to deploy Windows without using the network

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.315 -->

Create prestaged media
07/17/2025

Applies to: Configuration Manager (current branch)

Prestaged media in Configuration Manager is a Windows Image (WIM) file. It can be installed
on a bare-metal computer by the manufacturer or at your staging center that's not connected
to the production Configuration Manager environment. Prestaged media contains the boot
image used to start the destination computer and the OS image that's applied to the
destination computer. You can also specify applications, packages, and driver packages to
include as part of the prestaged media. The task sequence that deploys the OS isn't included in
the media. Prestaged media is applied to the hard drive of a new computer before the
computer is sent to the end user.

Use prestaged media for the following OS deployment scenarios:

     Create an image for an OEM in factory or a local depot

     Install a new version of Windows on a new computer (bare metal)

     Deploy Windows to Go

Usage
When the computer starts for the first time after you've applied the prestaged media, the
computer starts in Windows PE. It connects to a management point to locate the task
sequence that completes the OS deployment process. When you deploy a task sequence that
uses prestaged media, the client checks the local task sequence cache for valid content first. If
the content can't be found or has been revised, the client downloads the content from a
distribution point or peer.

Prerequisites
Before you create prestaged media by using the Create Task Sequence Media Wizard, be sure
that all of the conditions are met.

Boot image
Consider the following points about the boot image that you use in the task sequence to
deploy the OS:

<!-- p.316 -->

     The architecture of the boot image must be appropriate for the architecture of the
     destination computer. For example, an x64 destination computer can boot and run an x86
     or x64 boot image. However, an x86 destination computer can boot and run only an x86
     boot image.
     Make sure that the boot image contains the network and storage drivers that are required
     to provision the destination computer.

Create a task sequence to deploy an OS
As part of the prestaged media, specify the task sequence to deploy the OS. For more
information, see Create a task sequence to install an OS.

Distribute all content associated with the task sequence
Distribute all content that the task sequence requires to at least one distribution point. This
content includes the boot image, OS image, and other associated files. The wizard gathers the
content from the distribution point when it creates the prestaged media.

Your user account needs at least Read access rights to the content library on that distribution
point. For more information, see Distribute content.

Hard drive on the destination computer
The hard drive of the destination computer must be formatted before the prestaged media is
applied to it. If the hard drive isn't formatted when the media is applied, the task sequence that
deploys the OS fails when it attempts to start the destination computer.

  ７ Note

  The Create Task Sequence Media Wizard sets the following task sequence variable
  condition on the media: _SMSTSMediaType = OEMMedia. You can use this same
  condition in your task sequence.

Process

  ７ Note

  For PKI environments, since the Root CA is specified at the Primary site, make sure the
  prestaged media is created at the Primary site. The CAS site does not have the Root CA

<!-- p.317 -->

information to properly create the prestaged media.

1. In the Configuration Manager console, go to the Software Library workspace, expand
  Operating Systems, and select the Task Sequences node.

2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence Media.
  This action starts the Create Task Sequence Media Wizard.

3. On the Select Media Type page, specify the following options:

        Select Prestaged media.

        Optionally, if you want to only allow the OS to be deployed without requiring user
        input, select Allow unattended operating system deployment.

          ） Important

          When you select this option, the user isn't prompted for network configuration
          information or for optional task sequences. If you configure the media for
          password protection, the user is still prompted for a password.

4. On the Media Management page, specify one of the following options:

        Dynamic media: Allow a management point to redirect the media to another
        management point, based on the client location in the site boundaries.

        Site-based media: The media only contacts the specified management point.

5. On the Media Properties page, specify the following information:

        Created by: Specify who created the media.

        Version: Specify the version number of the media.

        Comment: Specify a unique description of what the media is used for.

        Media file: Specify the name and path of the output files. The wizard writes the
        output files to this location. For example: \\servername\folder\outputfile.wim

        Staging folder: The media creation process can require a lot of temporary drive
        space. By default this location is similar to the following path:
        %UserProfile%\AppData\Local\Temp . To give you greater flexibility with where to store

        these temporary files, change this value to another drive and path.

6. On the Security page, specify the following options:

<!-- p.318 -->

Enable unknown computer support: Allow the media to deploy an OS to a
computer that's not managed by Configuration Manager. There's no record of these
computers in the Configuration Manager database. For more information, see
Prepare for unknown computer deployments.

Protect media with a password: Enter a strong password to help protect the media
from unauthorized access. When you specify a password, the user must provide that
password to use the prestaged media.

  ） Important

  As a security best practice, always assign a password to help protect the
  prestaged media. Assigning a password to the media not only prevents
  someone without the password from running a task sequence when using the
  media, but it also properly encrypts the task sequence environment on the
  media. The task sequence environment includes the task sequence steps and
  their variables.

  Using a password doesn't encrypt the remaining content of the prestaged
  media such as packages. Don't include any sensitive information in task
  sequence packages such as scripts. Store and implement all sensitive
  information by using task sequence variables.

For HTTP communications, select Create self-signed media certificate. Then specify
the start and expiration date for the certificate.

  ７ Note

  If you select this option HTTPS management points will not be available for
  selection on the Boot image page of this wizard.

For HTTPS communications, select Import PKI certificate. Then specify the
certificate to import and its password.

For more information about this client certificate that boot images use, see PKI
certificate requirements.

User device affinity: To support user-centric management in Configuration
Manager, specify how you want the media to associate users with the destination
computer. For more information about how OS deployment supports user device
affinity, see Associate users with a destination computer.

<!-- p.319 -->

          Allow user device affinity with auto-approval: The media automatically
          associates users with the destination computer. This functionality is based on the
          actions of the task sequence that deploys the OS. In this scenario, the task
          sequence creates a relationship between the specified users and destination
          computer when it deploys the OS to the destination computer.

          Allow user device affinity pending administrator approval: The media associates
          users with the destination computer after approval is granted. This functionality is
          based on the scope of the task sequence that deploys the OS. In this scenario,
          the task sequence creates a relationship between the specified users and the
          destination computer, but waits for approval from an administrative user before
          the OS is deployed.

          Do not allow user device affinity: The media doesn't associate users with the
          destination computer. In this scenario, the task sequence doesn't associate users
          with the destination computer when it deploys the OS.

          ７ Note

          When setting user device affinity during a task sequence, the value configured
          here needs to match the value specified for the SMSTSAssignUsersMode
          variable.

          If the values don't match, then device affinity isn't set.

          For more information, see Task sequence variables.

7. On the Task Sequence page, select the task sequence that runs on the destination
  computer. Verify the list of content referenced by the task sequence.

       Detect associated application dependencies and add them to this media: Also add
       content to the media for application dependencies.

           Tip

          If you don't see expected application dependencies, deselect and then reselect
          this option to refresh the list.

8. On the Boot image page, specify the following options:

    ） Important

<!-- p.320 -->

      The architecture of the boot image that you distribute must be appropriate for the
      architecture of the destination computer. For example, an x64 destination computer
      can boot and run an x86 or x64 boot image. However, an x86 destination computer
      can boot and run only an x86 boot image.

           Boot image: Select the boot image to start the destination computer.

           Distribution point: Select the distribution point that has the boot image. The wizard
           retrieves the boot image from the distribution point and writes it to the media.

             ７ Note

             Your user account needs at least Read permissions to the content library on the
             distribution point.

           Management point: Only for site-based media, select a management point from a
           primary site.

           Associated management points: Only for dynamic media, select the primary site
           management points to use, and a priority order for the initial communication.

             ７ Note

             HTTPS enabled management points will only be displayed when a PKI
             certificate is specified in the Security page of this wizard.

 9. On the Images page, specify the following options:

           Image package: Specify the OS image to use. For more information, see Manage OS
           images.

           Image index: If the package contains multiple OS images, specify the index of the
           image to deploy.

           Distribution point: Specify the distribution point that has the OS image package.
           The wizard gets the OS image from the distribution point and writes it to the media.

10. On the Select Application page, select additional applications to add to the prestaged
   media file.

11. On the Select Package page, select additional packages to add to the prestaged media
   file.
