---
title: "Software update management documentation — pages 121-160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0121-0160
family: sccm
documentKind: "doc"
abstract: "to determine what type of software updates are in the software update group. To proceed, select Create. 6. Select Software Update Groups to display the new software update group. 7. Select the software update group, and in the Home tab, in the Update group, select Show Members t"
---

# Software update management documentation — pages 121-160

<!-- p.121 -->

   to determine what type of software updates are in the software update group. To
   proceed, select Create.

 6. Select Software Update Groups to display the new software update group.

 7. Select the software update group, and in the Home tab, in the Update group,
   select Show Members to display a list of the software updates that are included in
   the group.

 ７ Note

 Feature updates can't be added to a software update group. Use the following
 options to manage feature updates:

      Windows servicing
      Phased deployments
      Upgrade OS task sequences.

Add software updates to an existing software
update group
 1. In the Configuration Manager console, select Software Library.

 2. In the Software Library workspace, expand Software Updates, and then select All
   Software Updates.

 3. Select the software updates that you want to add to the new software update
   group.

          On the All Software Updates node, Configuration Manager displays all
          updates except those in the Upgrades classification and Office 365 Client
          product classification.

 4. On the Home tab, in the Update group, select Edit Membership.

 5. Select the software update group into which you want to add the software
   updates.

 6. Select the Software Update Groups node to display the software update group.

 7. Select the software update group, and in the Home tab, in the Update group,
   select Show Members to display a list of the software updates that are included in
   the software update group.

<!-- p.122 -->

Remove software updates from an existing
software update group
   1. In the Configuration Manager console, select Software Library.
   2. In the Software Library workspace, expand Software Updates, and then select
     Software Update Groups.
   3. Select the software update group from which you want to remove updates, then
     select Show members
   4. Right-click on the update to remove and select Edit Membership.

           Select multiple updates by using either the Shift or Ctrl keys.
           From the All Software Updates node, you can also use Edit Membership
           from the ribbon after selecting an update.

   5. Uncheck the box for the software update group from which you'd like to remove
     the update, then select Ok.

Next steps
Deploy software updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.123 -->

Deploy software updates
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The software update deployment phase is the process of deploying software updates.
No matter how you deploy software updates, the site:

      Adds the updates to a software update group
      Distributes the update content to distribution points
      Deploys the update group to clients

After you create the deployment, the site sends an associated software update policy to
targeted clients. The clients download the software update content files from a content
source to their local cache. Clients on the internet always download content from the
Microsoft Update cloud service. The software updates are then available for installation
by the client.

   Tip

  If a distribution point isn't available, clients on the intranet can also download
  software updates from Microsoft Update.

  ７ Note

  Unlike other deployment types, software updates are all downloaded to the client
  cache. This is regardless of the maximum cache size setting on the client. For more
  information about the client cache setting, see Configure the client cache.

If you configure a required software update deployment, the software updates are
automatically installed at the scheduled deadline. Alternatively, the user on the client
computer can schedule or initiate the software update installation prior to the deadline.
After the attempted installation, client computers send state messages back to the site
server to report whether the software update installation was successful. For more
information about software update deployments, see Software update deployment
workflows.

There are three main scenarios for deploying software updates:

      Manual deployment
      Automatic deployment

<!-- p.124 -->

     Phased deployment

Typically, you start by manually deploying software updates to create a baseline for your
clients, and then you manage software updates on clients by using an automatic or
phased deployment.

  ７ Note

  You can't use an automatic deployment rule with a phased deployment.

Manually deploy software updates
Select software updates in the Configuration Manager console and manually start the
deployment process. You typically use this method of deployment to:

     Get clients up-to-date with required software updates before you create automatic
     deployment rules that manage monthly deployments

     Deploy out-of-band software updates

The following list provides the general workflow for manual deployment of software
updates:

   1. Filter for software updates that use specific requirements. For example, provide
     criteria that retrieves all security or critical software updates that are required on
     more than 50 clients.

   2. Create a software update group that contains the software updates.

   3. Download the content for the software updates in the software update group.

   4. Manually deploy the software update group.

For more information and detailed steps, see Manually deploy software updates.

  ７ Note

       Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft
       365 Apps for enterprise. For more information, see Name change for Office
       365 ProPlus. You may still see references to the old name in the Configuration
       Manager console and supporting documentation while the console is being
       updated.

<!-- p.125 -->

        When manually deploying Microsoft 365 Apps client updates, find them in the
        Office 365 Updates node under Office 365 Client Management of the
        Software Library workspace.

Automatically deploy software updates
Configure automatic software updates deployment by using an automatic deployment
rule (ADR). This method of deployment is common for monthly software updates
(typically known as "Patch Tuesday") and for managing definition updates. You define
the criteria for an ADR to automate the deployment process. The following list provides
the general workflow to automatically deploy software updates:

   1. Create an ADR that specifies deployment settings.

   2. The site adds the software updates to a software update group.

   3. The site deploys the software update group to the clients in the target collection.

First, determine your automatic software update deployment strategy. For example,
create the ADR to initially target a collection of test clients. After you verify the test
group successfully installed the software updates, add a new deployment to the rule.
You could also change the targeted collection in the existing deployment to one that
includes a larger set of clients. Consider the following behaviors when deciding upon
the strategy to use:

     You're able to modify the properties of the software update objects that the ADR
     creates.

     The ADR automatically deploys software updates to clients when you add them to
     the target collection.

     When you or the ADR adds new software updates to the software update group,
     the site automatically deploys them to the clients in the target collection.

     Enable or disable deployments at any time for the ADR.

After you create an ADR, add additional deployments to the rule. This action helps you
manage the complexity of deploying different updates to different collections. Each new
deployment has the full range of functionality and deployment monitoring experience.

Each new deployment that you add:

     Uses the same update group and package, which the ADR creates when it first runs

<!-- p.126 -->

     Can target a different collection
     Supports unique deployment properties including:
        Activation time
        Deadline
        User experience
        Separate alerts for each deployment

For more information and detailed steps, see Automatically deploy software updates

Deploy software updates in phases
Create phased deployments for software updates. Phased deployments allow you to
orchestrate a coordinated, sequenced rollout of software based on customizable criteria
and groups.

For more information, see Create phased deployments.

Folder support for software update nodes
Starting in version 2203, you can organize software update groups and packages by
using folders. This change allows for better categorization and management of software
updates.

   1. Open the Configuration Manager console and go to the Software Library
     workspace.
   2. From the ribbon or right-click menu, in the Software Updates Groups or
     Deployment Packages nodes, select from the following options:

           Create Folder
           Delete Folder
           Rename Folder
           Move Folders
           Set Security Scopes

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.127 -->

Manually deploy software updates
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

A manual software update deployment is the process of selecting software updates
from the Configuration Manager console and manually starting the deployment process.
Or add selected software updates to an update group, and then manually deploy the
update group. You typically use manual deployments to get your clients up-to-date with
required software updates. You then use automatic deployment rules (ADR) to manage
ongoing monthly software update deployments. Also use this manual method to deploy
out-of-band software updates. For more information on which deployment method is
right for you, see Deploy software updates.

Step 1: Specify search criteria for software
updates
Depending upon the combinations of products and classifications that your site
synchronizes, there are potentially thousands of software updates displayed in the
Configuration Manager console. The first step in the workflow for manually deploying
software updates is to identify the software updates that you want to deploy. For
example, show all software updates required on more than 50 client devices with a
Security or Critical classification.

  ） Important

  A single software update deployment has a limit of 1000 software updates.

Process to specify search criteria for software updates
   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Software Updates, and click All Software Updates. This node displays all
      synchronized software updates.

        ７ Note

        The All Software Updates node only displays software updates with a Critical
        and Security classification that have been released in the last 30 days.

<!-- p.128 -->

  2. In the search pane, filter to identify the software updates that you need. Use one or
     both of the following options:

          In the search text box, type a search string that filters the software updates.
          For example, type the article or bulletin ID for a specific software update. Or
          enter a string that appears in the title of several software updates.

          Click Add Criteria, and select the criteria to filter software updates. Click Add,
          and then provide the values for the criteria.

  3. Click Search to filter the software updates.

        Tip

       Save frequently used filter criteria. On the ribbon, click the option to Save
       Current Search. Retrieve previous searches by clicking on Saved Searches.

Step 2: Create a software update group that
contains the software updates
Software update groups let you organize software updates in preparation for
deployment. Use the following procedure to manually add software updates to a new
software update group.

Process to manually add software updates to a new
software update group
  1. In the Configuration Manager console, go to the Software Library workspace, and
     select Software Updates. Select the desired software updates.

  2. Click Create Software Update Group in the ribbon.

  3. Specify the name for the software update group and optionally provide a
     description. Use a name and description that provide enough information for you
     to determine what type of updates are in the software update group. Click Create.

  4. Select the Software Update Groups node, and select the new software update
     group. To display the list of updates in the group, click Show Members in the
     ribbon.

<!-- p.129 -->

Step 3: Download the content for the software
update group
Before you deploy the software updates, download the content for the software updates
in the software update group. This step lets you verify that the content is available on
distribution points before you deploy the software updates. It also helps you avoid any
unexpected issues with content distribution. If you skip this step, as part of the
deployment process the site downloads the content and distributes to the distribution
points. Use the following procedure to download the content for software updates in
the software update group.

Process to download content for the software update
group
   1. In the Configuration Manager console, go to the Software Library workspace, and
     select the Software Updates node.

   2. Choose the software update to download by using one of the following methods:

           Select one or more software update groups from the Software Update
           Groups node. Then click Download in the ribbon.

           Select one or more software updates from All Software Updates node. Then
           click Download in the ribbon.

             ７ Note

             In the All Software Updates node, Configuration Manager displays only
             software updates with a Critical and Security classification that have
             been released in the last 30 days.

              Tip

             Click Add Criteria to filter the software updates that are displayed in the
             All Software Updates node. Save search criteria that you often use, and
             then manage saved searches on the Search tab.

   3. On the Deployment Package page of the Download Software Updates Wizard,
     configure the following settings:

<!-- p.130 -->

Select deployment package: Choose this setting to select an existing
deployment package for the software updates that are in the deployment.

  ７ Note

  Software updates that the site has already downloaded to the selected
  deployment package won't be downloaded again.

Create a new deployment package: Select this setting to create a new
deployment package for the software updates in the deployment. Configure
the following settings:

  Name: Specifies the name of the deployment package. The package must
  have a unique name that briefly describes the package content. It's limited
  to 50 characters.

  Description: Specify a description that provides information about the
  deployment package. The optional description is limited to 127 characters.

  Package source: Specifies the location of the software update source files.
  Type a network path for the source location, for example,
   \\server\sharename\path , or click Browse to find the network location.

  Create the shared folder for the deployment package source files before
  you proceed to the next page.

     You can't use the specified location as the source of another software
     deployment package.

     You can change the package source location in the deployment
     package properties after Configuration Manager creates the
     deployment package. If you do, first copy the content from the original
     package source to the new package source location.

     The computer account of the SMS Provider and the user that's running
     the wizard to download the software updates must both have Write
     permissions to the download location. Restrict access to the download
     location. This restriction reduces the risk of attackers tampering with the
     software update source files.

  Enable binary differential replication: Enable this setting to minimize
  network traffic between sites. Binary differential replication (BDR) only
  updates the content that has changed in the package, instead of updating

<!-- p.131 -->

          the entire package contents. For more information, see Binary differential
          replication.

4. On the Distribution Points page, specify the distribution points or distribution
  point groups to host the software update files. For more information about
  distribution points, see Distribution point configurations. This page is available
  only when you create a new software update deployment package.

5. The Distribution Settings page is available only when you create a new software
  update deployment package. Specify the following settings:

       Distribution priority: Use this setting to specify the distribution priority for
       the deployment package. The distribution priority applies when the
       deployment package is sent to distribution points at child sites. Deployment
       packages are sent in priority order: high, medium, or low. Packages with
       identical priorities are sent in the order in which they were created. If there's
       no backlog, the package processes immediately regardless of its priority. By
       default, the site sends packages with Medium priority.

       Enable for on-demand distribution: Use this setting to enable on-demand
       content distribution to distribution points configured for this feature and in
       the client's current boundary group. When you enable this setting, the
       management point creates a trigger for the distribution manager to
       distribute the content to all such distribution points when a client requests
       the content for the package and the content isn't available. For more
       information, see On-demand content distribution.

       Prestaged distribution point settings: Use this setting to specify how you
       want to distribute content to prestaged distribution points. Choose one of
       the following options:

          Automatically download content when packages are assigned to
          distribution points: Use this setting to ignore the prestage settings and
          distribute content to the distribution point.

          Download only content changes to the distribution point: Use this
          setting to prestage the initial content to the distribution point, and then
          distribute content changes to the distribution point.

          Manually copy the content in this package to the distribution point: Use
          this setting to always prestage content on the distribution point. This
          option is the default.

<!-- p.132 -->

         For more information about prestaging content to distribution points, see
         Use Prestaged content.

 6. On the Download Location page, specify the location that Configuration Manager
   uses to download the software update source files. Use one of the following
   options:

         Download software updates from the Internet: Select this setting to
         download the software updates from the location on the internet. This option
         is the default.

         Download software updates from a location on my network: Select this
         setting to download the software updates from a local directory or shared
         folder. This setting is useful when the computer that runs the wizard doesn't
         have internet access. Any computer with internet access can preliminarily
         download the software updates. Then store them in a location on the local
         network that's accessible from the computer that runs the wizard.

 7. On the Language Selection page, select the languages for which the site
   downloads the selected software updates. The site only downloads these updates
   if they're available in the selected languages. Software updates that aren't
   language-specific are always downloaded. By default, the wizard selects the
   languages that you've configured in the software update point properties. At least
   one language must be selected before proceeding to the next page. When you
   select only languages that a software update doesn't support, the download fails
   for the update.

 8. On the Summary page, verify the settings that you selected in the wizard, and then
   click Next to download the software updates.

 9. On the Completion page, verify that the software updates were successfully
   downloaded, and then click Close.

Process to monitor content status
 1. To monitor the content status for the software updates, go to the Monitoring
   workspace in the Configuration Manager console. Expand Distribution Status, and
   then select the Content Status node.

 2. Select the software update package that you previously identified to download the
   software updates in the software update group.

 3. Click View Status in the ribbon.

<!-- p.133 -->

Step 4: Deploy the software update group
After you determine the updates you want to deploy, and add them to a software
update group, manually deploy the software update group.

Process to manually deploy the software updates in a
software update group
  1. In the Configuration Manager console, go to the Software Library workspace,
     expand Software Updates, and select the Software Update Groups node.

  2. Select the software update group that you want to deploy. Click Deploy in the
     ribbon.

  3. On the General page of the Deploy Software Updates Wizard, configure the
     following settings:

          Name: Specify the name for the deployment. The deployment must have a
          unique name that describes its purpose, and differentiates it from other
          deployments in the site. This name field has a limit of 256 characters. By
          default, Configuration Manager automatically provides a name for the
          deployment in the following format: Microsoft Software Updates - YYYY-MM-
          DD <time>

          Description: Specify a description for the deployment. The description is
          optional, but provides an overview of the deployment. Include any other
          relevant information that helps to identify and differentiate it among others
          in the site. The description field has a limit of 256 characters, and has a blank
          value by default.

          Software Update/Software Update Group: Verify that the displayed software
          update group or software update is correct.

          Select Deployment Template: Specify whether to apply a previously saved
          deployment template. Configure a deployment template to save common
          software update deployment properties. Then apply the template when you
          deploy software updates in the future. These templates save time and help to
          ensure consistency across similar deployments.

          Collection: Specify the collection for the deployment. Devices in the
          collection receive the software updates in this deployment.

  4. On the Deployment Settings page, configure the following settings:

<!-- p.134 -->

Type of deployment: Specify the deployment type for the software update
deployment.

  ） Important

  After you create the software update deployment, you can't change the
  type of deployment.

   Select Required to create a mandatory software update deployment. The
   software updates are automatically installed on clients before the
   installation deadline you configure. When you deploy a software update
   group as Required, clients download the content in background and
   honor BITS settings, if configured.

   Select Available to create an optional software update deployment. This
   deployment is available for users to install from Software Center. For
   software update groups deployed as Available, clients download the
   content in the foreground and ignore BITS settings.

  ７ Note

  Starting in Configuration Manager version 2203, you can select the Pre-
  download content for this deployment setting for Available
  deployments. This setting reduces installation wait times for clients since
  installation notifications won't be visible in Software Center until the
  content has fully downloaded.
     If an update is in multiple deployments for a client and the Pre-
     download content for this deployment setting is enabled for a least
     one of the deployments, then the content will pre-download.
     If you edit an existing deployment to use the Pre-download content
     for this deployment setting, the content will only pre-download if the
     software update is not yet available on the client.

Use Wake-on-LAN to wake up clients for required deployments: Specifies
whether to enable Wake On LAN at the deadline. Wake On LAN sends wake-
up packets to computers that require one or more software updates in the
deployment. The site wakes up any computers that are in sleep mode at the
installation deadline time so the installation can initiate. Clients that are in
sleep mode that don't require any software updates in the deployment aren't
started. By default, this setting isn't enabled. It's only available for Required

<!-- p.135 -->

       deployments. Before using this option, configure computers and networks for
       Wake On LAN. For more information, see How to configure Wake On LAN.

       Detail level: Specify the level of detail for the state messages that clients
       report to the site.

5. On the Scheduling page, configure the following settings:

       Schedule evaluation: Specify the time that Configuration Manager evaluates
       the available time and installation deadline times. Choose to use Coordinated
       Universal Time (UTC) or the local time of the computer that runs the
       Configuration Manager console.
          When you select Client local time here, and then select As soon as
          possible for the Software available time, the current time on the
          computer running the Configuration Manager console is used to evaluate
          when updates are available. This behavior is the same with the Installation
          deadline and the time when updates are installed on a client. If the client
          is in a different time zone, these actions occur when the client's time
          reaches the evaluation time.

       Software available time: Select one of the following settings to specify when
       the software updates are available to clients:

          As soon as possible: Makes the software updates in the deployment
          available to clients as soon as possible. When you create the deployment
          with this setting selected, Configuration Manager updates the client policy.
          At the next client policy polling cycle, clients become aware of the
          deployment and the software updates are available for installation.

          Specific time: Makes software updates included in the deployment
          available to clients at a specific date and time. When you create the
          deployment with this setting enabled, Configuration Manager updates the
          client policy. At the next client policy polling cycle, clients become aware
          of the deployment. However, the software updates in the deployment
          aren't available for installation until after the configured date and time.

       Installation deadline: These options are only available for Required
       deployments. Select one of the following settings to specify the installation
       deadline for the software updates in the deployment

          As soon as possible: Select this setting to automatically install the software
          updates in the deployment as soon as possible.

<!-- p.136 -->

          Specific time: Select this setting to automatically install the software
          updates in the deployment at a specific date and time.

             The actual installation deadline time is the displayed deadline time plus
             a random amount of time up to two hours. The randomization reduces
             the potential impact of clients in the collection installing updates in the
             deployment at the same time.

             To disable the installation randomization delay for required software
             updates, configure the client setting to Disable deadline randomization
             in the Computer Agent group. For more information, see Computer
             Agent client settings.

       Delay enforcement of this deployment according to user preferences, up to
       the grace period defined in client settings: Enable this setting to give users
       more time to install required software updates beyond the deadline.

          This behavior is typically required when a computer is turned off for long
          time, and needs to install many software updates or applications. For
          example, when a user returns from vacation, they have to wait for a long
          time as the client installs overdue deployments.

          Configure this grace period with the property Grace period for
          enforcement after deployment deadline (hours) in client settings. For
          more information, see the Computer agent section. The enforcement
          grace period applies to all deployments with this option enabled and
          targeted to devices to which you also deployed the client setting.

          After the deadline, the client installs the software updates in the first non-
          business window, which the user configured, up to this grace period.
          However, the user can still open Software Center and install the software
          updates at any time. Once the grace period expires, enforcement reverts
          to normal behavior for overdue deployments.

6. On the User Experience page, configure the following settings:

       User notifications: Specify whether to display notification in Software Center
       at the configured Software available time. This setting also controls whether
       to notify users on the client computers. For Available deployments, you can't
       select the option to Hide in Software Center and all notifications.

       Deadline behavior: This setting is only configurable for Required
       deployments. Specify the behaviors when the software update deployment
       reaches the deadline outside of any defined maintenance windows. The

<!-- p.137 -->

options include whether to install the software updates, and whether to
perform a system restart after installation. For more information about
maintenance windows, see How to use maintenance windows.

  ７ Note

  This applies only when the maintenance window is configured for the
  client device. If no maintenance window is defined on the device, the
  update of the installation and restart will always happen after the
  deadline.

Device restart behavior: This setting is only configurable for Required
deployments. Specify whether to suppress a system restart on servers and
workstations if a restart is required to complete update installation.

  ２ Warning

  Suppressing system restarts can be useful in server environments, or
  when you don't want the target computers to restart by default.
  However, doing so can leave computers in an insecure state. Allowing a
  forced restart helps to ensure immediate completion of the software
  update installation.

Write filter handling for Windows Embedded devices: This setting controls
the installation behavior on Windows Embedded devices that are enabled
with a write filter. Choose the option to commit changes at the installation
deadline or during a maintenance window. When you select this option, a
restart is required and the changes persist on the device. Otherwise, the
update is installed, applied to the temporary overlay, and committed later.
  When you deploy a software update to a Windows Embedded device,
  make sure the device is a member of a collection that has a configured
  maintenance window.

Software updates deployment re-evaluation behavior upon restart: Select
this setting to configure software updates deployments to have clients run a
software updates compliance scan immediately after a client installs software
updates and restarts. This setting enables the client to check for additional
updates that become applicable after the client restarts, then installs them
during the same maintenance window.

<!-- p.138 -->

7. On the Alerts page, configure how Configuration Manager generates alerts for this
  deployment. Review recent software updates alerts from Configuration Manager in
  the Software Updates node of the Software Library workspace. If you're also using
  System Center Operations Manager, configure its alerts as well. Only configure
  alerts for Required deployments.

8. On the Download Settings page, configure the following settings:

    ７ Note

    Clients request the content location from a management point for the
    software updates in a deployment. The download behavior depends upon
    how you've configured the distribution point, the deployment package, and
    the settings on this page.

       Specify if clients should download and install the updates when they use a
       distribution point from a neighbor or the default site boundary groups.

       Specify if clients should download and install the updates from a distribution
       point in the site default boundary group, when the content for the software
       updates isn't available from a distribution point in the current or neighbor
       boundary groups.

       Allow clients to share content with other clients on the same subnet:
       Specify whether to enable the use of BranchCache for content downloads. For
       more information, see BranchCache. Starting in version 1802, BranchCache is
       always enabled on clients. This setting is removed, as clients use BranchCache
       if the distribution point supports it.

       If software updates are not available on distribution point in current,
       neighbor or site boundary groups, download content from Microsoft
       Updates: Select this setting to have intranet-connected clients download
       software updates from Microsoft Update if updates aren't available on
       distribution points. Internet-based clients always go to Microsoft Update for
       software updates content.

       Specify whether to allow clients to download after an installation deadline
       when they use metered internet connections. Internet providers sometimes
       charge by the amount of data that you send and receive when you're on a
       metered connection.

9. On the Deployment Package page, select one of the following options:

<!-- p.139 -->

７ Note

If you already performed Step 3: Download the content for the software
update group, then the wizard doesn't display the Deployment Package,
Distribution Points, and Language Selection pages. Skip to the Summary
page of the wizard.

Software updates that have been previously downloaded to the content
library on the site server aren't downloaded again. This behavior is true even
when you create a new deployment package for the software updates. If all
software updates have already been downloaded, the wizard skips to the
Summary page.

   Select a deployment package: Add these updates to an existing deployment
   package.

   Create a new deployment package: Add these updates to a new deployment
   package. Configure the following additional settings:

     Name: Specify the name of the deployment package. Use a unique name
     that describes the package content. It's limited to 50 characters.

     Description: Specify a description that provides information about the
     deployment package. The optional description is limited to 127 characters.

     Package source: Specify the location of the software update source files.
     Type a network path for the source location, for example,
      \\server\sharename\path , or click Browse to find the network location.
     Create the shared folder for the deployment package source files before
     you continue to the next page.

         You can't use the specified location as the source of another software
         deployment package.

         You can change the package source location in the deployment
         package properties after Configuration Manager creates the
         deployment package. If you do, first copy the content from the original
         package source to the new package source location.

         The computer account of the SMS Provider and the user that's running
         the wizard to download the software updates must both have Write
         permissions to the download location. Restrict access to the download

<!-- p.140 -->

               location. This restriction reduces the risk of attackers tampering with the
               software update source files.

            Sending priority: Specify the sending priority for the deployment package.
            Configuration Manager uses this priority when it sends the package to
            distribution points. Deployment packages are sent in priority order: high,
            medium, or low. Packages with identical priorities are sent in the order in
            which they were created. If there's no backlog, the package processes
            immediately regardless of its priority.

            Enable binary differential replication: Enable this setting to minimize
            network traffic between sites. Binary differential replication (BDR) only
            updates the content that has changed in the package, instead of updating
            the entire package contents. For more information, see Binary differential
            replication.

         No deployment package: Starting in version 1806, deploy software updates
         to devices without first downloading and distributing content to distribution
         points. This setting is beneficial when dealing with extremely large update
         content. Also use it when you always want clients to get content from the
         Microsoft Update cloud service. Clients in this scenario can also download
         content from peers that already have the necessary content. The
         Configuration Manager client continues to manage the content download,
         thus can utilize the Configuration Manager peer cache feature, or other
         technologies such as Delivery Optimization. This feature supports any update
         type supported by Configuration Manager software updates management,
         including Windows and Office updates.

10. On the Distribution Points page, specify the distribution points or distribution
   point groups to host the software update files. For more information about
   distribution points, see Distribution point configurations.

      ７ Note

      If you already performed Step 3: Download the content for the software
      update group, then the wizard doesn't display the Deployment Package,
      Distribution Points, and Language Selection pages. Skip to the Summary
      page of the wizard.

11. On the Download Location page, specify whether to download the software
   update files from the internet or from your local network. Configure the following
   settings:

<!-- p.141 -->

        Download software updates from the internet: Select this setting to
        download the software updates from a specified location on the internet. This
        setting is enabled by default.

        Download software updates from a location on the local network: Select
        this setting to download the software updates from a local directory or
        shared folder. This setting is useful when the computer that runs the wizard
        doesn't have internet access. Any computer with internet access can
        preliminarily download the software updates. Then store them in a location
        on the local network that's accessible from the computer that runs the
        wizard.

12. On the Language Selection page, select the languages for which the site
   downloads the selected software updates. The site only downloads these updates
   if they're available in the selected languages. Software updates that aren't
   language-specific are always downloaded. By default, the wizard selects the
   languages that you've configured in the software update point properties. At least
   one language must be selected before proceeding to the next page. When you
   select only languages that a software update doesn't support, the download fails
   for the update.

     ７ Note

     If you already performed Step 3: Download the content for the software
     update group, then the wizard doesn't display the Deployment Package,
     Distribution Points, and Language Selection pages. Skip to the Summary
     page of the wizard.

13. On the Summary page, review the settings. To save the settings to a deployment
   template, click Save As Template. Enter a name and select the settings you want to
   include in the template, then click Save. To change a configured setting, click the
   associated wizard page and change the setting.

        The template name can consist of alphanumeric ASCII characters as well as \
        (backslash) or ' (single quotation mark).

14. Click Next to deploy the software update.

   After you complete the wizard, Configuration Manager downloads the software
   updates to the content library on the site server. It then distributes the content to
   the configured distribution points, and deploys the software update group to

<!-- p.142 -->

     clients in the target collection. For more information about the deployment
     process, see Software update deployment process.

Next steps
Monitor software updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.143 -->

Automatically deploy software updates
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use an automatic deployment rule (ADR) rather than adding new updates to an existing
software update group. Typically, you use ADRs to deploy monthly software updates
(also known as "Patch Tuesday" updates) and for managing Endpoint Protection
definition updates. If you need help determining which deployment method is right for
you, see Deploy software updates.

Create an automatic deployment rule (ADR)
Automatically approve and deploy software updates by using an ADR. The rule can add
software updates to a new software update group each time the rule runs, or add
software updates to an existing group. When a rule runs and adds software updates to
an existing group, the rule removes all updates from the group. It then adds to the
group the updates that meet the criteria you define.

  ２ Warning

  Before you create an ADR for the first time, verify that the site has completed
  software updates synchronization. This step is important when you run
  Configuration Manager with a non-English language. Software update
  classifications are displayed in English before the first synchronization, and then
  displayed in the localized languages after software update synchronization
  completes. Rules that you create before you sync software updates might not work
  properly after synchronization because the text string might not match.

Process to create an ADR
   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Software Updates, and select the Automatic Deployment Rules node.

   2. In the ribbon, click Create Automatic Deployment Rule.

   3. On the General page of the Create Automatic Deployment Rule Wizard, configure
      the following settings:

<!-- p.144 -->

Name: Specify the name for the ADR. The name must be unique, help to
describe the purpose of the rule, and identify it from others in the
Configuration Manager site.

Description: Specify a description for the ADR. The description should
provide an overview of the deployment rule and other relevant information
that helps to differentiate the rule from others. The description field is
optional, has a limit of 256 characters, and has a blank value by default.

Template: Select a deployment template to specify whether to apply
previously saved ADR configurations. Configure a deployment template
containing multiple common update deployment properties that you can use
when creating additional ADRs. These templates save time and help to ensure
consistency across similar deployments. Select from one of the following
built-in software update deployment templates:

   The Patch Tuesday template provides common settings to use when you
   deploy software updates on a monthly cycle.

   The Office 365 Client Updates template provides common settings to use
   when you deploy updates for Microsoft 365 Apps clients.

     ７ Note

     Starting on April 21, 2020, Office 365 ProPlus is being renamed to
     Microsoft 365 Apps for enterprise. If your ADRs rely on the "Title"
     property, you'll need to edit it starting June 9, 2020. Microsoft 365
     Apps Update - Semi-annual Channel Version 1908 for x64 based

     Edition (Build 11929.50000) is an example of the new title. For more

     information on modifying your ADRs for the title change, see Update
     channels for Microsoft 365 Apps. For more information about the
     name change, see Name change for Office 365 ProPlus.

   The SCEP and Windows Defender Antivirus Updates template provides
   common settings to use when you deploy Endpoint Protection definition
   updates.

Collection: Specifies the target collection to be used for the deployment.
Members of the collection receive the software updates that are defined in
the deployment.

<!-- p.145 -->

       Decide whether to add software updates to a new or existing software
       update group. In most cases, choose to create a new software update group
       when the ADR runs. If the rule runs on a more aggressive schedule, you
       might choose to use an existing group. For example, if you run the rule daily
       for definition updates, then you could add the software updates to an
       existing software update group.

       Enable the deployment after this rule is run: Specify whether to enable the
       software update deployment after the ADR runs. Consider the following
       options for this setting:

          When you enable the deployment, the updates that meet the rule's
          defined criteria are added to a software update group. The software
          update content is downloaded as necessary. The content is copied to the
          specified distribution points, and the updates are deployed to the clients
          in the target collection.

          When you don't enable the deployment, the updates that meet the rule's
          defined criteria are added to a software update group. The software
          update deployment content is downloaded, as necessary, and distributed
          to the specified distribution points. The site creates a disabled deployment
          on the software update group to prevent the updates from being
          deployed to clients. This option provides time to prepare to deploy the
          updates, verify the updates that meet the criteria are adequate, and then
          enable the deployment.

4. On the Deployment Settings page, configure the following settings:

       Type of deployment: Starting in version 2107, you can specify the
       deployment type for the software update deployment. Prior to version 2107,
       all deployments created by an automatic deployment rule are required.

          Select Required to create a mandatory software update deployment. The
          software updates are automatically installed on clients before the
          installation deadline you configure.

          Select Available to create an optional software update deployment. This
          deployment is available for users to install from Software Center.

         ７ Note

         Starting in Configuration Manager version 2203, you can select the Pre-
         download content for this deployment setting for Available

<!-- p.146 -->

  deployments. This setting reduces installation wait times for clients since
  installation notifications won't be visible in Software Center until the
  content has fully downloaded.
     If an update is in multiple deployments for a client and the Pre-
     download content for this deployment setting is enabled for a least
     one of the deployments, then the content will pre-download.
     If you edit an existing deployment to use the Pre-download content
     for this deployment setting, the content will only pre-download if the
     software update is not yet available on the client.

Use Wake on LAN to wake up clients for required deployments: Specifies
whether to enable Wake On LAN at the deadline. Wake On LAN sends wake-
up packets to computers that require one or more software updates in the
deployment. The site wakes up any computers that are in sleep mode at the
installation deadline time so the installation can initiate. Clients that are in
sleep mode that don't require any software updates in the deployment aren't
started. By default, this setting isn't enabled. Before using this option,
configure computers and networks for Wake On LAN. For more information,
see How to configure Wake On LAN.

Detail level: Specify the level of detail for the update enforcement state
messages that are reported by clients.

  ） Important
     When you deploy definition updates, set the detail level to Error only
     to have the client report a state message only when a definition
     update fails. Otherwise, the client reports a large number of state
     messages that might impact site server performance.
     The Error only detail level does not send the enforcement status
     messages required for tracking pending reboots.

License terms setting: Specify whether to automatically deploy software
updates with associated license terms. Some software updates include license
terms. When you automatically deploy software updates, the license terms
aren't displayed, and there isn't an option to accept the license terms. Choose
to automatically deploy all software updates regardless of an associated
license term, or only deploy updates that don't have associated license terms.

<!-- p.147 -->

          To review the license terms for a software update, select the software
          update in the All Software Updates node of the Software Library
          workspace. In the ribbon, click Review License.

          To find software updates with associated license terms, add the License
          Terms column to the results pane in the All Software Updates node. Click
          the heading for the column to sort by the software updates with license
          terms.

5. On the Software Updates page, configure the criteria for the software updates that
  the ADR retrieves and adds to the software update group.

       The limit for software updates in the ADR is 1000 software updates.

       If needed, filter on the content size for software updates in automatic
       deployment rules. For more information, see Configuration Manager and
       simplified Windows servicing on down level operating systems         .

       Starting in version 2111, the following options were added in the Date
       Released or Revised search criteria:
          Older than 30 days
          Older than 60 days
          Older than 90 days
          Older than 6 months
          Older than 1 year

       You can use Deployed as an update filter for your automatic deployment
       rules. This filter helps identify new updates that may need to be deployed to
       your pilot or test collections. The software update filter can also help avoid
       redeploying older updates.
          When using Deployed as a filter, be mindful that you may have already
          deployed the update to another collection, such as a pilot or test
          collection.

       A property filter for Architecture is now available. Use this filter to exclude
       architectures like Itanium and ARM64 that are less common. Remember that
       there are 32-bit (x86) applications and components running on 64-bit (x64)
       systems. Unless you're certain that you don't need x86, enable it as well when
       you choose x64.

6. On the Evaluation Schedule page, specify whether to enable the ADR to run on a
  schedule. When enabled, click Customize to set the recurring schedule.

<!-- p.148 -->

       The start time configuration for the schedule is based on the local time of the
       computer that runs the Configuration Manager console.

       The ADR evaluation can run as often as three times per day.

       Never set the evaluation schedule with a frequency that exceeds the software
       updates synchronization schedule. This page displays the software update
       point sync schedule to help you determine evaluation schedule frequency.

       To manually run the ADR, select the rule in the Automatic Deployment Rule
       node of the console, and then click Run Now in the ribbon.

       ADRs can be scheduled to evaluate offset from a base day. For example, if
       Patch Tuesday actually falls on Wednesday for you, set the evaluation
       schedule for the second Tuesday of the month offset by one day.
          When scheduling evaluation with an offset during the last week of the
          month, if you choose an offset that continues into the next month, the site
          schedules evaluation for the last day of the month.

7. On the Deployment Schedule page, configure the following settings:

       Schedule evaluation: Specify the time that Configuration Manager evaluates
       the available time and installation deadline times. Choose to use Coordinated
       Universal Time (UTC) or the local time of the computer that runs the
       Configuration Manager console.

<!-- p.149 -->

  When you select Client local time here, and then select As soon as
  possible for the Software available time, the current time on the
  computer running the Configuration Manager console is used to evaluate
  when updates are available. This behavior is the same with the Installation
  deadline and the time when updates are installed on a client. If the client
  is in a different time zone, these actions occur when the client's time
  reaches the evaluation time.

Software available time: Select one of the following settings to specify when
the software updates are available to clients:

  As soon as possible: Makes the software updates in the deployment
  available to clients as soon as possible. When you create the deployment
  with this setting selected, Configuration Manager updates the client policy.
  At the next client policy polling cycle, clients become aware of the
  deployment and the software updates are available for installation.

  Specific time: Makes software updates included in the deployment
  available to clients at a specific date and time. When you create the
  deployment with this setting enabled, Configuration Manager updates the
  client policy. At the next client policy polling cycle, clients become aware
  of the deployment. However, the software updates in the deployment
  aren't available for installation until after the configured date and time.

  ７ Note

  Starting in version 2203, the Software available time and Installation
  deadline for deployments created by an ADR are now calculated based
  on the time the ADR evaluation is scheduled and starts. Previously, these
  times were calculated based on when the ADR evaluation completed.
  This change makes the Software available time and Installation
  deadline consistent and predictable for deployments.

Installation deadline: These options are only available for Required
deployments. Select one of the following settings to specify the installation
deadline for the software updates in the deployment:

  As soon as possible: Select this setting to automatically install the software
  updates in the deployment as soon as possible.

  Specific time: Select this setting to automatically install the software
  updates in the deployment at a specific date and time. Configuration

<!-- p.150 -->

          Manager determines the deadline to install software updates by adding
          the configured Specific time interval to the Software available time.

             The actual installation deadline time is the displayed deadline time plus
             a random amount of time up to two hours. The randomization reduces
             the potential impact of clients in the collection installing updates in the
             deployment at the same time.

             The Disable deadline randomization in the Computer Agent group
             doesn't override the randomization behavior. For more information, see
             Computer Agent client settings.

          ７ Note

          Starting in version 2203, the Software available time and Installation
          deadline for deployments created by an ADR are now calculated based
          on the time the ADR evaluation is scheduled and starts. Previously, these
          times were calculated based on when the ADR evaluation completed.
          This change makes the Software available time and Installation
          deadline consistent and predictable for deployments.

       Delay enforcement of this deployment according to user preferences, up to
       the grace period defined in client settings: Enable this setting to give users
       more time to install required software updates beyond the deadline.

          This behavior is typically required when a computer is turned off for long
          time, and needs to install many software updates or applications. For
          example, when a user returns from vacation, they have to wait for a long
          time as the client installs overdue deployments.

          Configure this grace period with the property Grace period for
          enforcement after deployment deadline (hours) in client settings. For
          more information, see the Computer agent section. The enforcement
          grace period applies to all deployments with this option enabled and
          targeted to devices to which you also deployed the client setting.

          After the deadline, the client installs the software updates in the first non-
          business window, which the user configured, up to this grace period.
          However, the user can still open Software Center and install the software
          updates at any time. Once the grace period expires, enforcement reverts
          to normal behavior for overdue deployments.

8. On the User Experience page, configure the following settings:

<!-- p.151 -->

User notifications: Specify whether to display notification in Software Center
at the configured Software available time. This setting also controls whether
to notify users on the clients.

Deadline behavior: This setting is only configurable for Required
deployments. Specify the behaviors when the software update deployment
reaches the deadline outside of any defined maintenance windows. The
options include whether to install the software updates, and whether to
perform a system restart after installation. For more information about
maintenance windows, see How to use maintenance windows.

  ７ Note

  This applies only when the maintenance window is configured for the
  client device. If no maintenance window is defined on the device, the
  update of the installation and restart will always happen after the
  deadline.

Device restart behavior: This setting is only configurable for Required
deployments. Specify whether to suppress a system restart on servers and
workstations if a restart is required to complete update installation.

  ２ Warning

  Suppressing system restarts can be useful in server environments, or
  when you don't want the target computers to restart by default.
  However, doing so can leave computers in an insecure state. Allowing a
  forced restart helps to ensure immediate completion of the software
  update installation.

Write filter handling for Windows Embedded devices: This setting controls
the installation behavior on Windows Embedded devices that are enabled
with a write filter. Choose the option to commit changes at the installation
deadline or during a maintenance window. When you select this option, a
restart is required and the changes persist on the device. Otherwise, the
update is installed, applied to the temporary overlay, and committed later.
   When you deploy a software update to a Windows Embedded device,
   make sure the device is a member of a collection that has a configured
   maintenance window.

<!-- p.152 -->

        Software updates deployment re-evaluation behavior upon restart: Select
        this setting to configure software updates deployments to have clients run a
        software updates compliance scan immediately after a client installs software
        updates and restarts. This setting enables the client to check for additional
        updates that become applicable after the client restarts, then installs them
        during the same maintenance window.

 9. On the Alerts page, configure how Configuration Manager generates alerts for this
   deployment. Review recent software updates alerts from Configuration Manager in
   the Software Updates node of the Software Library workspace. If you're also using
   System Center Operations Manager, configure its alerts as well.

10. On the Download Settings page, configure the following settings:

        Specify if clients should download and install the updates when they use a
        distribution point from a neighbor or the default site boundary groups.

        Specify if clients should download and install the updates from a distribution
        point in the site default boundary group, when the content for the software
        updates isn't available from a distribution point in the current or neighbor
        boundary groups.

        Allow clients to share content with other clients on the same subnet:
        Specify whether to enable the use of BranchCache for content downloads. For
        more information, see BranchCache. BranchCache is always enabled on
        clients. This setting is removed, as clients use BranchCache if the distribution
        point supports it.

        If software updates are not available on distribution point in current,
        neighbor or site boundary groups, download content from Microsoft
        Updates: Select this setting to have intranet-connected clients download
        software updates from Microsoft Update if updates aren't available on
        distribution points. Internet-based clients always go to Microsoft Update for
        software updates content.

        Specify whether to allow clients to download after an installation deadline
        when they use metered internet connections. Internet providers sometimes
        charge by the amount of data that you send and receive when you're on a
        metered connection.

     ７ Note

<!-- p.153 -->

     Clients request the content location from a management point for the
     software updates in a deployment. The download behavior depends upon
     how you've configured the distribution point, deployment package, and the
     settings on this page.

11. On the Deployment Package page, select one of the following options:

        Select a deployment package: Add these updates to an existing deployment
        package.

        Create a new deployment package: Add these updates to a new deployment
        package. Configure the following additional settings:

           Name: Specify the name of the deployment package. Use a unique name
           that describes the package content. It's limited to 50 characters.

           Description: Specify a description that provides information about the
           deployment package. The optional description is limited to 127 characters.

           Package source: Specifies the location of the software update source files.
           Type a network path for the source location, for example,
           \\server\sharename\path , or click Browse to find the network location.

           Create the shared folder for the deployment package source files before
           you proceed to the next page.

              You can't use the specified location as the source of another software
              deployment package.

              You can change the package source location in the deployment
              package properties after Configuration Manager creates the
              deployment package. If you do, first copy the content from the original
              package source to the new package source location.

              The computer account of the SMS Provider and the user that's running
              the wizard to download the software updates must both have Write
              permissions to the download location. Restrict access to the download
              location. This restriction reduces the risk of attackers tampering with the
              software update source files.

           Sending priority: Specify the sending priority for the deployment package.
           Configuration Manager uses this priority when it sends the package to
           distribution points. Deployment packages are sent in priority order: high,
           medium, or low. Packages with identical priorities are sent in the order in

<!-- p.154 -->

            which they were created. If there's no backlog, the package processes
            immediately regardless of its priority.

            Enable binary differential replication: Enable this setting to use binary
            differential replication for the deployment package. For more information,
            see Binary differential replication.

         No deployment package: Deploy software updates to devices without first
         downloading and distributing content to distribution points. This setting is
         beneficial when dealing with extremely large update content. Also use it
         when you always want clients to get content from the Microsoft Update
         cloud service. Clients in this scenario can also download content from peers
         that already have the necessary content. The Configuration Manager client
         continues to manage the content download, thus can utilize the
         Configuration Manager peer cache feature, or other technologies such as
         Delivery Optimization. This feature supports any update type supported by
         Configuration Manager software updates management, including Windows
         and Microsoft 365 Apps updates.

           ７ Note

           Once you select this option and apply the settings, it can no longer be
           changed. The other options are greyed out.

12. On the Distribution Points page, specify the distribution points or distribution
   point groups to host the software update files. For more information about
   distribution points, see Distribution point configurations. This page is available
   only when you create a new software update deployment package.

13. On the Download Location page, specify whether to download the software
   update files from the internet or from your local network. Configure the following
   settings:

         Download software updates from the internet: Select this setting to
         download the software updates from a specified location on the internet. This
         setting is enabled by default.

         Download software updates from a location on the local network: Select
         this setting to download the software updates from a local directory or
         shared folder. This setting is useful when the computer that runs the wizard
         doesn't have internet access. Any computer with internet access can
         preliminarily download the software updates. Then store them in a location

<!-- p.155 -->

              on the local network that's accessible from the computer that runs the
              wizard. Another scenario could be when downloading content that is
              published through System Center Updates Publisher or a third-party patching
              solution. The WSUS content share on the top-level software update point can
              be entered as the network location to download from, such as
              \\server\WsusContent .

 14. On the Language Selection page, select the languages for which the site
     downloads the selected software updates. The site only downloads these updates
     if they're available in the selected languages. Software updates that aren't
     language-specific are always downloaded. By default, the wizard selects the
     languages that you've configured in the software update point properties. At least
     one language must be selected before proceeding to the next page. When you
     select only languages that a software update doesn't support, the download fails
     for the update.

 15. On the Summary page, review the settings. To save the settings to a deployment
     template, click Save As Template. Enter a name and select the settings you want to
     include in the template, then click Save. To change a configured setting, click the
     associated wizard page and change the setting.

              The template name can consist of alphanumeric ASCII characters as well as \
              (backslash) or ' (single quotation mark).

 16. Click Next to create the ADR.

After you complete the wizard, the ADR runs. It adds the software updates that meet the
specified criteria to a software update group. Then the ADR downloads the updates to
the content library on the site server and distributes them to the configured distribution
points. The ADR then deploys the software update group to clients in the target
collection.

Add a new deployment to an existing ADR
After you create an ADR, add additional deployments to the rule. This action helps you
manage the complexity of deploying different updates to different collections. Each new
deployment has the full range of functionality and deployment monitoring experience.

Process to add a new deployment to an existing ADR
   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Software Updates, select the Automatic Deployment Rules node, and

<!-- p.156 -->

     then select the desired rule.

   2. In the ribbon, click Add Deployment.

   3. On the Collection page of the Add Deployment Wizard, configure the available
     settings similarly as the General page of the Create Automatic Deployment Rule
     Wizard. For more information, see the previous section on the Process to create an
     ADR. The rest of the Add Deployment Wizard includes the following pages, which
     also match detailed descriptions above:

           Deployment Settings
           Deployment Schedule
           User Experience
           Alerts
           Download Settings

Deployments can also be added programmatically using Windows PowerShell cmdlets.
For a complete description of using this method, see New-
CMSoftwareUpdateDeployment .

For more information about the deployment process, see Software update deployment
process.

Process to create a folder for automatic
deployment rules
(Starting in version 2207)

   1. In the Configuration Manager console, go to the Software Library workspace, and
     then go to Automatic Deployment Rules.

   2. From the ribbon or right-click menu, and in the Automatic Deployment Rules
     select from the following options:

           Create Folder
           Delete Folder
           Rename Folder
           Move Folders
           Set Security Scopes

Folder creations can also be added programmatically using Windows PowerShell
cmdlets. For a complete description of using this method, see

<!-- p.157 -->

     New-CMFolder
     Set-CMFolder
     Get-CMFolder
     Remove-CMfolder

Known issues

Error code 0x87D20417
Scenario: When running Configuration Manager version 2010, you may notice that an
automatic deployment rule fails and returns Last Error Code of 0x87D20417. In the
PatchDownloader.log, you see Failed to create temp file with GetTempFileName() at
temp location C:\Windows\TEMP\, error 80 and 0-byte files in the %temp% directory.

Workaround: Remove all the files from the temp directory specified in the
PatchDownloader.log and rerun the ADR.

Resolution: Install KB 4600089   , Update Rollup for Microsoft Endpoint Configuration
Manager current branch, version 2010.

Script to apply deployment package settings for
automatic deployment rule
If you create an ADR with the No deployment package option, you're' unable to go
back and add one later. To help you resolve this issue, we've uploaded the following
script into Community hub:

   Tip

  Open this script directly in Community hub. For more information, see Direct links
  to Community hub items.

  PowerShell

  <# Apply-ADRDeploymentPackageSettings #>

  #=============================================
  # START SCRIPT
  #=============================================
  param
  (
  [parameter(Mandatory = $true)]

<!-- p.158 -->

  [ValidateNotNullOrEmpty()]
  [ValidateLength(1,256)]
  [string]$sourceADRName,

  [parameter(Mandatory = $true)]
  [ValidateNotNullOrEmpty()]
  [ValidateLength(1,256)]
  [string]$targetADRName
  )

  Try {
         # Source ADR that already has the needed deployment package. You may
  need to create one if it doesn’t exist.
         $sourceADR = Get-CMSoftwareUpdateAutoDeploymentRule -Name
  $sourceADRName

          # Target ADR that will be updated to use the source ADR’s deployment
  package. Typically, this is the ADR that used the “No deployment package”
  option.
          $targetADR = Get-CMSoftwareUpdateAutoDeploymentRule -Name
  $targetADRName

           # Apply the deployment package settings
           $targetADR.ContentTemplate = $sourceADR.ContentTemplate

           # Update the wmi object
           $targetADR.Put()
  }
  Catch{
         $exceptionDetails = "Exception: " + $_.Exception.Message + "HResult:
  " + $_.Exception.HResult
         Write-Error "Failed to apply ADR deployment package settings:
  $exceptionDetails"
  }
  #=============================================
  # END SCRIPT
  #=============================================

Next steps
Monitor software updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.159 -->

Create phased deployments with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Phased deployments automate a coordinated, sequenced rollout of software across
multiple collections. For example, deploy software to a pilot collection, and then
automatically continue the rollout based on success criteria. Create phased deployments
with the default of two phases, or manually configure multiple phases.

Create phased deployments for the following objects:

      Task sequence
         The phased deployment of task sequences doesn't support PXE or media
         installation
      Application
      Software update
         You can't use an automatic deployment rule (ADR) with a phased deployment

Prerequisites

Security scope
Deployments created by phased deployments aren't viewable to any administrative user
that doesn't have the All security scope. For more information, see Security scopes.

Distribute content
Before creating a phased deployment, distribute the associated content to a distribution
point.

      Application: Select the target application in the console and use the Distribute
      Content action in the ribbon. For more information, see Deploy and manage
      content.

      Task sequence: You have to create referenced objects like the OS upgrade package
      before creating the task sequence. Distribute these objects before creating a
      deployment. Use the Distribute Content action on each object, or the task
      sequence. To view status of all referenced content, select the task sequence, and

<!-- p.160 -->

     switch to the References tab in the details pane. For more information, see the
     specific object type in Prepare for OS deployment.

     Software update: create the deployment package and distribute it. Use the
     Download Software Updates Wizard. For more information, see Download
     software updates.

Phase settings
These settings are unique to phased deployments. Configure these settings when
creating or editing the phases to control the scheduling and behavior of the phased
deployment process.

Optionally, use the following Windows PowerShell cmdlets to manually configure phases
for software update and task sequence phased deployments:

     New-CMSoftwareUpdatePhase
     New-CMTaskSequencePhase

Criteria for success of the first phase
     Deployment success percentage: Specify the percent of devices that need to
     successfully complete the deployment for the first phase to succeed. By default,
     this value is 95%. In other words, the site considers the first phase successful when
     the compliance state for 95% of the devices is Success for this deployment. The
     site then continues to the second phase, and creates a deployment of the software
     to the next collection.

     Number of devices successfully deployed: Specify the number of devices that
     need to successfully complete the deployment for the first phase to succeed. This
     option is useful when the size of the collection is variable, and you have a specific
     number of devices to show success before moving to the next phase.

Conditions for beginning second phase of deployment
after success of the first phase
     Automatically begin this phase after a deferral period (in days): Choose the
     number of days to wait before beginning the second phase after the success of the
     first. By default, this value is one day.

     Manually begin the second phase of deployment: The site doesn't automatically
     begin the second phase after the first phase succeeds. This option requires that
