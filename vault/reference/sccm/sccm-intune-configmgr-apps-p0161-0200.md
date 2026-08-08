---
title: "App management documentation — pages 161-200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-apps-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-apps-p0161-0200
family: sccm
documentKind: "doc"
abstract: "User and deployment configuration files have settings that control how an application behaves. You can use these files to change application settings without resequencing the application. A typical App-V 5 application might contain the following files: An application package (.a"
---

# App management documentation — pages 161-200

<!-- p.161 -->

User and deployment configuration files have settings that control how an application
behaves. You can use these files to change application settings without resequencing
the application.

A typical App-V 5 application might contain the following files:

     An application package (.appv) file

     A user configuration file

     A deployment configuration file

The user configuration file has settings that apply only to the logged-on user. You can,
for example, edit the configuration files to change the information about the application
shortcut that will be deployed to users. You can also create a Configuration Manager
application with multiple deployment types. Each deployment type can contain a
different user configuration file and use requirement rules to ensure that these are
installed for the relevant users.

The deployment configuration file has settings that apply to the computer, like registry
settings. The file can also have user settings, which are applied to all users.

If you want to deploy App-V 5 virtual applications with Configuration Manager, all three
files must be present in the same folder when you create the App-V 5 deployment type.
If there are multiple files in the folder, Configuration Manager will use the most recent.

For more information, see your About App-V 5.0 dynamic configuration.

App-V local interaction
In some application deployment scenarios, applications are installed locally on client
computers, and other applications are deployed as virtual applications to the same
client computer. By default, the applications that were locally installed cannot see or
communicate directly with virtualized applications. This is the intended behavior of the
application isolation that App-V provides. Local interaction is a feature of the App-V
Client that you can enable for each application to allow locally installed applications that
run on a client computer to see and communicate with virtualized applications.
Configuration Manager and App-V fully support local interaction.

For more information about the App-V local interaction feature, see your App-V
documentation.

App-V 5 Shared Content Store

<!-- p.162 -->

Configuration Manager supports the App-V 5 Shared Content Store feature. For more
information, see Planning for the App-V 5.0 Shared Content Store (SCS).

Monitoring virtual applications

Virtual application reports
You can use the following reports to monitor App-V in your Configuration Manager
environment:

                                                                                       ﾉ   Expand table

 Report name              Description

 App-V Virtual            Shows information about a selected virtual environment that is in a
 Environment Results      specified state for a selected collection (App-V 5 only).

 App-V Virtual            Shows information about a selected virtual environment for a specified
 Environment Results      asset and any deployment types for the selected virtual environment (App-
 For Asset                V 5 only).

 App-V Virtual            Shows compliance information for a selected virtual environment for a
 Environment Status       selected collection. The Retained column in this report shows the assets in
                          which a virtual environment that was previously set up is no longer
                          applicable, but it is retained to persist user settings in applications that run
                          in the virtual environment (App-V 5 only).

 Computers with a         Shows a summary of computers that have the specified App-V shortcut
 specific virtual         that the Application Virtualization Management Sequencer created (App-V
 application              4.6 only).

 Computers with a         Shows a list of computers that have the specified App-V application
 specific virtual         package installed (App-V 4.6 only).
 application package

 Count all instances      Shows a count of all detected App-V application packages (App-V 4.6
 of virtual application   only).
 packages

 Count all instances      Shows a count of all detected App-V applications (App-V 4.6 only).
 of virtual
 applications

Log files

<!-- p.163 -->

Configuration Manager records information about virtual application deployments in
log files. For information about the log files that virtual applications and Configuration
Manager application management use, see Log files.

For Windows 8.1, find logs for the App-V client in
C:\ProgramData\Microsoft\Application Virtualization Client.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.164 -->

Disable and delete application
deployments
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

If you want to stop the deployment of an application, you can either disable it
temporarily or delete it entirely.

  ） Important

  Neither of these actions by themselves cause an instant change on the client. You
  can use client notifications or other automation tools to quickly request that
  clients refresh policy. But that still doesn't guarantee that a client won't run a
  deployment.

  Make sure you carefully plan app deployments. Simulate more complex
  deployments. When you deploy to a query-based collection, use query results
  preview to make sure you understand the scope of the query.

Disable
Starting in version 2103, you can disable application deployments. Other objects already
have similar behaviors:

      Software update deployments: Disable the deployment
      Phased deployments: Suspend the phase
      Package: Disable the program
      Task sequence: Disable the task sequence
      Configuration baseline: Disable the baseline

For device-based deployments, when you disable the deployment or object, use the
client notification action to Download Computer Policy. This action immediately tells
the client to update its policy from the site. If the deployment hasn't already started, the
client receives the updated policy that the object is now disabled.

For user-based deployments, the user needs to sign out of Windows. Policy updates
when they sign in to Windows, or every 24 hours by default.

<!-- p.165 -->

  ７ Note

  You can't disable an available deployment of an application to a user collection. You
  can only disable required deployments to user collections, or both type of
  deployments to device collections. The following table summarizes the supported
  scenarios to disable app deployments:

                                                                       ﾉ   Expand table

   Deployment purpose                Device collection           User collection

   Required                          Yes                         Yes

   Available                         Yes                         No

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select the Applications node.

   2. Select an app that you've deployed. In the details pane, switch to the Deployment
     tab.

   3. Select a deployment. In the ribbon, on the Deployment tab, select Disable.

   4. For a device-based deployment, note the name of the collection in Collection field
     of the deployment.

        Tip

       When you select the deployment, press CTRL + C. This keyboard shortcut
       copies the values of the current columns for the selected deployment.

   5. Switch to the Assets and Compliance workspace, select the Device Collections
     node, and locate the target collection for the deployment. The quickest method is
     to search for the collection name as previously noted. You may need to select the
     option in the ribbon to search All subfolders.

   6. Select the target collection for the deployment. In the ribbon, in the Collection
     group, select Client Notification and choose the Download Computer Policy
     action.

To enable the deployment, repeat this process but select the Enable action on the
application deployment.

<!-- p.166 -->

  ７ Note

  When you select a deployment, you can use the Collection action to change to the
  Assets and Compliance workspace. But the current collection view doesn't support
  client notification actions.

Delete
   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Application Management, and select either the Applications or
     Application Groups node.

   2. Select the application or application group that includes the deployment you want
     to delete.

   3. Switch to the Deployments tab of the details pane, and select the deployment.

   4. In the ribbon, on the Deployment tab in the Deployment group, select Delete.

When you delete an application deployment, any instances of the application that
clients have already installed aren't removed. To remove these applications, deploy the
application to computers to Uninstall. If you delete an application deployment, the
application is no longer visible in Software Center. The same behavior happens when
you remove a resource from the target collection for the deployment.

When you delete a deployment, you remove the policy that deploys an application to a
specific collection. This action doesn't delete the collection, any deployment types, or
the application itself.

Next steps
Revise and supersede applications

Uninstall applications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.167 -->

Troubleshooting tips for application
deployments
Applies to: Configuration Manager (current branch)

Typical problems with application deployments fall into one of the following categories:

     Application download failures

     Application deployment compliance stuck at 0%

If you experience either of these issues, this article provides some steps you can use to
troubleshoot. For more in-depth troubleshooting, see Troubleshooting application deployment
technical reference.

Download failures
Application download failures include the following problems:

     The client is stuck downloading an application

     The client fails to download the application content

     The client gets stuck at 0% while downloading the application

The first thing to check when you experience application download failures is for missing or
misconfigured boundaries and boundary groups. For example, if the client is on the intranet and
not configured for internet-only client management, its network location must be in a configured
boundary. There must also be a boundary group assigned to this boundary for the client to
download content. For more information, see Define site boundaries and boundary groups.

If you can't configure a boundary for a client, or if a specific boundary group can't be a member
of another boundary group:

   1. In the Configuration Manager console, open the properties of the Deployment Type.

   2. Switch to the Content tab.

   3. In the section for using a distribution point from a neighbor boundary group or the default
     site boundary group, change the Deployment options to Download content from

<!-- p.168 -->

      distribution point and run locally. (By default this setting is Do not download content.)

If the client can't download the application content, make sure it's distributed to a distribution
point. To verify this configuration, use the in-console features to monitor content distribution to
the distribution points. For more information, see Monitor content you have distributed.

Compliance stuck at 0%
When the application's deployment compliance is 0%, check the deployment status for the
application in the Monitoring workspace under the Deployments node.

      In Progress: The client could be stuck downloading content.

      Error: For more information on how to troubleshoot this problem, see the following blog
      post: Tips and Tricks: How to Take Action on Assets That Report a Failed Deployment           .

      Unknown: This status usually means that the client hasn't received policy. Manually refresh
      client policy to see if the client receives it. For more information, see Initiate policy retrieval
      for a Configuration Manager client.

If these actions don't resolve the issue, check the client status. There may be a deeper underlying
problem with the client. For more information, see How to monitor clients.

Next steps
      Monitor applications
      Deploy applications
      Management tasks for applications
      Troubleshooting application deployment technical reference

 Last updated on 03/30/2026

<!-- p.169 -->

Monitor applications from the
Configuration Manager console
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Applications in Configuration Manager support state-based monitoring, which enables
you to track the last application deployment state for users and devices. These state
messages display information about individual devices. For example, if an application is
deployed to a collection of users, you can view the compliance state of the deployment
and the deployment purpose in the Configuration Manager console.

Monitor application deployments by using the Monitoring workspace in the
Configuration Manager console or by using reports.

About compliance states
An application deployment state has one of the following compliance states:

      Success: The client successfully deployed the application or it's already deployed. A
      deployment can install or uninstall an application.

      In progress: The client is currently running the application deployment.

      Unknown: Configuration Manager can't determine the state of the application
      deployment. This state isn't applicable for deployments with a purpose of
      Available. The console typically displays this state when the site hasn't yet received
      state messages from the client.

      Requirements not met: The client didn't run the application deployment because it
      wasn't compliant with a dependency or a requirement rule. For example, the OS on
      the device isn't applicable.

      Error: The client failed to deploy the application because of an error.

For each compliance state, you can view additional information, such as the number of
users and devices in this category. The compliance states also include subcategories. For
example, the Error compliance state includes the following subcategories:

      Error evaluating requirements

      Content related errors

<!-- p.170 -->

      Installation errors

When more than one compliance state applies for an application deployment, you can
see the aggregate state that represents the lowest compliance. For example:

      A user signs in to two devices. The application successfully installs on one device
      but fails to install on the other. The aggregate deployment state of the application
      for this user displays as Error.

      You deploy an application to all users that sign in to a computer. Configuration
      Manager displays multiple deployment results for that computer. If one of the
      deployments fails, the aggregate deployment state for the computer displays as
      Error.

Use these subcategories to help you to quickly identify any important issues with an
application deployment. You can also view additional information about the devices that
fall into a particular subcategory of a compliance state.

Application monitoring reports
Application management in Configuration Manager includes many built-in reports to
monitor information about applications and deployments. These reports have the report
category of Software Distribution – Application Monitoring. For more information, see
List of reports.

For more information about how to configure reporting in Configuration Manager, see
Introduction to reporting.

Monitor app state in the console
   1. In the Configuration Manager console, go to the Monitoring workspace, and select
      the Deployments node.

      If your site has numerous deployments, filter the list to just application
      deployments.
      a. At the top of the list next to the Search field, select Add Criteria. Choose
         Feature Type and then select Add.
      b. The search area adds the default criteria, AND Feature Type Content
         Distribution. Select Content Distribution and choose Application instead.
      c. Select Search to refresh the list.

   2. Select a deployment for the app to monitor.

<!-- p.171 -->

                                                                                       

The following two tabs in the details pane are populated for the selected deployment:

     Summary: Displays general status information about an application deployment.
     Deployment Types: Displays status for the application's deployment types.

Review deployment details
From the Deployments node, you can review deployment details for each compliance
state and the resources in that state. To review the deployment details, select View
status on the Home tab of the ribbon. This action opens the Deployment Status pane.
Here you can review the assets in each compliance state. To display Details list. Then
select More Details on the right side of the window.

     The maximum number of items that the Deployment Status pane can display is
     20,000. If you need to see more items, use Configuration Manager reports to
     review application status data.

     The status of deployment types is aggregated in the Deployment Status pane. To
     display more detailed information about the deployment types, use the
     Application Infrastructure Errors report.

     Starting in version 2203, you can perform client notification actions, including Run
     Scripts, from the Deployment Status view. Use the right-click menu on either a
     group of clients in a Category or a single client in the Asset details pane to display
     the client notification actions.

<!-- p.172 -->

                                                                                    

Summarized data
The information on the Summary and Deployment Types tabs is summarized data.
When you select View Status, the console displays current data from the site database.
If these data don't match, select Run Summarization.

To configure the default application deployment summarization interval:

   1. In the Configuration Manager console, go to the Administration workspace,
     expand Site Configuration, and select the Sites node.

   2. Select the site for which you want to configure the summarization interval. Then in
     the Settings group of the ribbon, choose Status Summarizers.

   3. Select Application Deployment Summarizer, and the select Edit.

   4. Configure the summarization intervals:

          Frequency of status updates for a deployment that was modified in the last
          30 days: By default, this value is 60 minutes.
          Frequency of status updates for a deployment that was modified in the last
          31 to 90 days: By default, this value is 24 hours.
          Frequency of status updates for a deployment that was last modified over
          90 days ago: By default this value is 7 days.

       ７ Note

       These values apply to application, task sequence, and package deployments.

<!-- p.173 -->

        The site calculates the period of time based on the deployment start time.

Next steps
Monitor phased deployments

Monitor app usage with software metering

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.174 -->

Manage and monitor phased deployments
This article describes how to manage and monitor phased deployments. Management tasks
include manually beginning the next phase, and suspend or resume a phase.

First, you need to create a phased deployment:

     Application
     Software update
     Task sequence

Move to the next phase
When you select the setting, Manually begin the second phase of deployment, the site doesn't
automatically start the next phase based on success criteria. You need to move the phased
deployment to the next phase.

   1. How to start this action varies based on the type of deployed software:

          Application: Go to the Software Library workspace, expand Application
          Management, and select Applications.

          Software update: Go to the Software Library workspace, and then select one of the
          following nodes:
             Software Updates
                All Software Updates
                Software Update Groups
             Windows Servicing, All Windows Updates
             Office 365 Client Management, Office 365 Updates

          Task sequence: Go to the Software Library workspace, expand Operating Systems,
          and select Task Sequences.

   2. Select the software with the phased deployment.

   3. In the details pane, switch to the Phased Deployments tab.

   4. Select the phased deployment, and click Move to next phase in the ribbon.

<!-- p.175 -->

Optionally, use the following Windows PowerShell cmdlet for this task: Move-
CMPhasedDeploymentToNext.

Suspend and resume phases
You can manually suspend or resume a phased deployment. For example, you create a phased
deployment for a task sequence. While monitoring the phase to your pilot group, you notice a
large number of failures. You suspend the phased deployment to stop further devices from
running the task sequence. After resolving the issue, you resume the phased deployment to
continue the rollout.

   1. How to start this action varies based on the type of deployed software:

           Application: Go to the Software Library workspace, expand Application
           Management, and select Applications.

           Software update: Go to the Software Library workspace, and then select one of the
           following nodes:
              Software Updates
                 All Software Updates
                 Software Update Groups
              Windows Servicing, All Windows Updates
              Office 365 Client Management, Office 365 Updates

           Task sequence: Go to the Software Library workspace, expand Operating Systems,
           and select Task Sequences. Select an existing task sequence, and then click Create
           Phased Deployment in the ribbon.

   2. Select the software with the phased deployment.

   3. In the details pane, switch to the Phased Deployments tab.

   4. Select the phased deployment, and click Suspend or Resume in the ribbon.

<!-- p.176 -->

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365 Apps for
  enterprise. For more information, see Name change for Office 365 ProPlus. You may still
  see the old name in the Configuration Manager product and documentation while the
  console is being updated.

Optionally, use the following Windows PowerShell cmdlets for this task:

     Suspend-CMPhasedDeployment
     Resume-CMPhasedDeployment

Monitor
Phased deployments have their own dedicated monitoring node, making it easier to identify
phased deployments you have created and navigate to the phased deployment monitoring view.
From the Monitoring workspace, select Phased Deployments, then double-click one of the
phased deployments to see the status.

<!-- p.177 -->

This dashboard shows the following information for each phase in the deployment:

     Total devices or Total resources: How many devices are targeted by this phase.

     Status: The current status of this phase. Each phase can be in one of the following states:

       Deployment created: The phased deployment created a deployment of the software to
       the collection for this phase. Clients are actively targeted with this software.

       Waiting: The previous phase hasn't yet reached the success criteria for the deployment
       to continue to this phase.

       Suspended: An administrator suspended the deployment.

     Progress: The color-coded deployment states from clients. For example: Success, In
     Progress, Error, Requirements Not Met, and Unknown.

<!-- p.178 -->

Success criteria tile
Use the Select Phase drop-down list to change the display of the Success Criteria tile. This tile
compares the Phase Goal against the current compliance of the deployment. With the default
settings, the phase goal is 95%. This value means that the deployment needs a 95% compliance
to move to the next phase.

In the example, the phase goal is 65%, and the current compliance is 66.7%. The phased
deployment automatically moved to the second phase, because the first phase met the success
criteria.

The phase goal is the same as the Deployment success percentage on the Phase Settings for the
next phase. For the phased deployment to start the next phase, that second phase defines the
criteria for success of the first phase. To view this setting:

   1. Go to the phased deployment object on the software, and open the Phased Deployment
      Properties.

   2. Switch to the Phases tab. Select Phase 2 and click View.

   3. In the phase Properties window, switch to the Phase Settings tab.

   4. View the value for Deployment success percentage in the Criteria for success of the previous
      phase group.

<!-- p.179 -->

For example, the following properties are for the same phase as the success criteria tile shown
above where the criteria is 65%:

PowerShell
Use the following Windows PowerShell cmdlets to manage phased deployments:

Automatically create phased deployments
     New-CMApplicationAutoPhasedDeployment
     New-CMSoftwareUpdateAutoPhasedDeployment
     New-CMTaskSequenceAutoPhasedDeployment

Manually create phased deployments
     New-CMSoftwareUpdatePhase

<!-- p.180 -->

     New-CMSoftwareUpdateManualPhasedDeployment
     New-CMTaskSequencePhase
     New-CMTaskSequenceManualPhasedDeployment

Get existing phased deployment objects
     Get-CMApplicationPhasedDeployment
     Get-CMSoftwareUpdatePhasedDeployment
     Get-CMTaskSequencePhasedDeployment
     Get-CMPhase

Monitor phased deployment status
     Get-CMPhasedDeploymentStatus

Manage existing phased deployments
     Move-CMPhasedDeploymentToNext
     Resume-CMPhasedDeployment
     Suspend-CMPhasedDeployment

Modify existing phased deployments
     Set-CMApplicationPhasedDeployment
     Set-CMSoftwareUpdatePhase
     Set-CMSoftwareUpdatePhasedDeployment
     Set-CMTaskSequencePhase
     Set-CMTaskSequencePhasedDeployment
     Remove-CMApplicationPhasedDeployment
     Remove-CMSoftwareUpdatePhasedDeployment
     Remove-CMTaskSequencePhasedDeployment

Last updated on 10/04/2022

<!-- p.181 -->

Software metering in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic contains a reference for all of the operations you might perform when using
Configuration Manager software metering.

  ） Important

  Software metering is used to monitor Windows PC desktop apps with a filename
  ending in .exe. Software metering does not monitor modern Windows apps (such
  as those used by Windows 8).

Prerequisites for software metering
Software metering has no external dependencies, only dependencies within the product.

                                                                                 ﾉ   Expand table

 Dependency            More information

 Client settings for   To use software metering, the client setting Enable software metering on
 software              clients must be enabled and deployed to computers. You can deploy
 metering.             software metering settings to all computers in the hierarchy, or you can
                       deploy custom settings to groups of computers. See Configure software
                       metering in this topic.

 The reporting         You must configure a reporting services point before you can view software
 services point.       metering reports. For more information, see Introduction to reporting.

Configure software metering
This procedure configures the default client settings for software metering and applies
to all computers in your hierarchy. If you want these settings to apply to only some
computers, create a custom device client setting and deploy it to a collection that
contains the computers on which you want to use software metering. For more
information about how to create custom device settings, see Configure client settings.

<!-- p.182 -->

   1. In the Configuration Manager console, click Administration > Client Settings >
     Default Client Settings.

   2. On the Home tab, in the Properties group, click Properties.

   3. In the Default Settings dialog box, click Software Metering.

   4. In the Device Settings list, configure the following:

           Enable software metering on clients: Select True to enable software
           metering.

           Schedule data collection: Configure how often software metering data is
           collected from client computers. Use the default value of every 7 days or click
           Schedule to specify a custom schedule.

   5. Click OK to close the Default Settings dialog box.

     Client computers are configured with these settings the next time they download
     client policy. To initiate policy retrieval for a single client, see Manage clients.

Create software metering rules
Use the Create Software Metering Rule wizard to create a new software metering rule
for your Configuration Manager site.

   1. In the Configuration Manager console, click Assets and Compliance > Software
     Metering.

   2. On the Home tab, in the Create group, click Create Software Metering Rule.

   3. On the General page of the Create Software Metering Rule wizard, specify the
     following information:

           Name - The name of the software metering rule. This should be unique and
           descriptive.

             ７ Note

             Software metering rules can share the same name if the file name
             contained in the rules is different.

           File Name - The name of the program file that you want to meter. You can
           click Browse to display the Open dialog box, in which you can select the

<!-- p.183 -->

        program file to use.

          ７ Note

          If you type the executable file name in the File name box, no checks are
          carried out to determine whether this file exists or whether it contains
          the necessary header information. When possible, click Browse and
          select the executable file to be metered.

          Wildcard characters are not permitted in the file name.

          This box is optional if a value for Original file name is specified.

        Original File Name - The name of the executable file that you want to meter.
        This name matches information in the header of the file, not the file name
        itself so that it can be useful in cases where the executable file has been
        renamed but you want to meter it by the original name.

          ７ Note

          Wildcard characters are not permitted in the original file name.

          This box is optional if a value for File Name is specified.

        Version - The version of the executable file you that want to meter. You can
        use the wildcard character ( * ) to represent any string of characters or the
        wildcard character ( ? ) to represent any single character. If you want to meter
        for all versions of an executable file, use the default value ( * ).

        Language - The language of the executable file to meter. The default value is
        the current locale of the operating system you are using. If you select an
        executable file to be metered by clicking the Browse button, this box is
        automatically filled if language information is present in the header of the
        file. To meter all language versions of a file, select Any in the drop-down list.

        Description - An optional description for the software metering rule.

        Apply this software metering rule to the following clients – Select whether
        you want to apply the software metering rule to all clients in the hierarchy or
        to the clients that are assigned to the site specified in the Site list.

4. To continue, click Next.

<!-- p.184 -->

   5. Review and confirm the settings and then complete the wizard to create the
     software metering rule. The new software metering rule is displayed in the
     Software Metering node in the Assets and Compliance workspace.

Configure automatic software metering rules
You can configure software metering in Configuration Manager to automatically
generate disabled software metering rules from recent usage inventory data held in the
site database. You can configure this inventory data so that only for applications that are
used on a specified percentage of computers metering rules are created. You can also
specify the maximum number of automatically generated software metering rules
allowed on the site.

  ７ Note

  By default, software metering rules that are automatically created are disabled.
  Before you can begin to collect usage data from these rules, you must enable them.

   1. In the Configuration Manager console, click Assets and Compliance > Software
     Metering, and then, in the Home tab, in the Settings group, click Software
     Metering Properties.

   2. In the Software Metering Properties dialog box, configure the following:

           Data retention (in days) - Specifies the amount of time that data generated
           by software metering rules are kept in the site database. The default value is
           90 days.

           Enable the option Automatically create disabled metering rules from recent
           usage inventory data.

           Specify the percentage of computers in the hierarchy that must use a
           program before a software metering rule is automatically created - The
           default value is 10 percent.

           Specify the number of software metering rules that must be exceeded in
           the hierarchy before the automatic creation of rules is disabled - The
           default value is 100 rules.

   3. Click OK to close the Software Metering Properties dialog box.

Manage software metering rules

<!-- p.185 -->

In the Assets and Compliance workspace, select Software Metering, select the software
metering rule to manage, and then select a management task.

Use the following table for more information about the management tasks that might
require some information before you select them.

                                                                                      ﾉ   Expand table

 Management       Details
 Task

 Enable           Enables or disables a software metering rule. This setting is downloaded to
                  client computers according to the Client policy polling interval in the Client
 Disable          Policy section of client settings (by default, every 60 minutes).

                  See Configure client settings .

Monitor software metering
Software metering in Configuration Manager includes a number of built-in reports
which allow you to monitor information about software metering operations. These
reports have the report category of Software Metering.

For more information about how to configure reporting in Configuration Manager, see
Introduction to reporting.

Additionally, you can create queries and collections based on the data stored in the
Configuration Manager database by software metering.

For more information about collections in Configuration Manager, see Introduction to
collections.

For more information about queries in Configuration Manager, see Introduction to
queries.

Security and privacy for software metering

Security Issues for Software Metering
An attacker could send invalid software metering information to Configuration Manager,
which will be accepted by the management point even when the software metering
client setting is disabled. This might result in a large number of metering rules that are

<!-- p.186 -->

replicated throughout the hierarchy, causing a denial of service on the network and to
Configuration Manager site servers.

Because an attacker can create invalid software metering data, do not consider software
metering information to be authoritative.

Software metering is enabled by default as a client setting.

Privacy Information for Software Metering
Software metering monitors the usage of applications on client computers. Software
metering is enabled by default. You must configure which applications to meter.
Metering information is stored in the Configuration Manager database. The information
is encrypted during transfer to a management point but it is not stored in encrypted
form in the Configuration Manager database.

This information is retained in the database until it is deleted by the site maintenance
tasks Delete Aged Software Metering Data (every five days) and Delete Aged Software
Metering Summary Data (every 270 days). You can configure the deletion interval.
Metering information is not sent to Microsoft.

Before you configure software metering, consider your privacy requirements.

Example scenario for using software metering
In this section, you'll create an example software metering rule that can help you solve
the following business requirements:

     Determine how many copies of a particular app are in your company

     Discover any unused copies of an app

     Determine which users regularly use a particular app

     Woodgrove Bank has deployed Microsoft Office 2010 as its standard office
     productivity suite. However, to support a legacy application, some computers must
     continue to run Microsoft Office Word 2003. The IT department wants to reduce
     support and licensing costs by removing these copies of Word 2003 if the legacy
     application is no longer used. The help desk also wants to identify which users use
     the legacy application.

     Woodgrove Bank's IT Systems Manager uses software metering in Configuration
     Manager to achieve these business objectives. The Admin performs the following

<!-- p.187 -->

     actions:

     Checks the prerequisites for software metering and confirms that the reporting
     services point is installed and operational.

     Configures the default client settings for software metering:
     The Admin enables software metering and uses the default data collection
     schedule of once every seven days.
     The Admin configures software inventory to inventory files that have the extension
     .exe by configuring the software inventory client setting Inventory these file types.
     The Admin adds a new software metering rule, named woodgrove.exe, to monitor
     the legacy application.

     Waits for seven days, after which the client computers begin to report usage data
     for the woodgrove.exe executable.

     The Admin uses the Configuration Manager report Install base for all metered
     software programs to see which computers have the application woodgrove.exe
     loaded.

     After six months, the Admin runs the report Computers that have a metered
     program installed, but have not run the program since a specified date,
     specifying the software metering rule and a date six months in the past. This report
     identifies 120 computers that have not run the program in the past six months.

     The Admin makes some further checks to confirm that the legacy application is not
     required on the identified computers. The Admin then uninstalls the legacy
     application and the copy of Word 2003 from these computers.
     The Admin runs the report Users that have run a specific metered software
     program to provide the help desk with a list of users who continue to use the
     legacy application.

     The Admin continues to check the software metering reports weekly and takes
     remedial action if necessary.

     As a result of this course of action, IT support and licensing costs are reduced by
     removing the applications that are no longer required. In addition, the help desk
     now has the list that it wanted of the users who run the legacy application.

Feedback
Was this page helpful?

<!-- p.188 -->

                            Yes    No

Provide product feedback

<!-- p.189 -->

Management tasks for Configuration
Manager applications
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the information in this article to help you manage Configuration Manager
applications and deployment types.

For more information on how to create applications and deployment types, see Create
applications.

  ） Important

  Depending on the type of application or deployment type, some management
  options might not be available.

Manage applications
In the Software Library workspace, expand Application Management, and select the
Applications node. Select the application to manage, and then choose a management
task in the ribbon.

Manage access accounts
Use this action to control access to the associated content on distribution points.

When you Add an account:

   1. Specify one of the following account types:

            User: Any account that Windows can authenticate.
            Guest: An unauthenticated user.
            Administrator: An account that Windows recognizes as an administrator.
            Windows User: A specific user account. It can either be from a local machine
            or Active Directory.

   2. Specify one of the following access rights:

<!-- p.190 -->

          No access: Explicitly block the specified account type from accessing the
          content associated with this application.
          Read
          Change
          Full control

By default, the Administrator type has Full control access, and the User type has Read
access.

Create prestaged content file
Prestaged content files help you to manage the delivery of content to remote
distribution points. When scheduling and throttling options don't provide a valid
solution for the remote distribution point, you can prestage the content.

For more information, see Deploy and manage content.

Revision history
View and manage the revisions to this application. For more information, see How to
revise and supersede applications.

Update statistics
Updates the information that's displayed in the Deployments node of the Monitoring
workspace about the deployments of this application. For more information, see
Monitor applications from the Configuration Manager console.

Create deployment type
Add a new deployment type to the selected application. For more information, see
Create deployment types for the application.

Convert to .MSIX
Convert an existing Windows Installer (.msi) application to the MSIX format. For more
information, see Support for MSIX format.

Reinstate

<!-- p.191 -->

If you previously retired an application, use this action to reinstate it. When you reinstate
a retired app, you can then deploy it again.

Retire
When you retire an application, it's no longer available for deployment. Configuration
Manager doesn't delete the application and any deployments. If the app was installed
on clients, Configuration Manager doesn't remove the app. Configuration Manager
deletes any revisions to the app after 60 days in retirement.

Before you delete an application:

   1. Retire the application.
   2. Delete all deployments.
   3. Remove references to the application by other deployments
   4. Delete all of the application's revisions.

For more information, see Revise and supersede applications.

Export
Export the selected applications to a .zip file that you can archive or import to another
site. If you choose to export application content, Configuration Manager creates a folder
with the content.

You can export:

     Application dependencies
     Supersedence relationships and conditions
     Content for the application and its dependencies

To automate this process, use the following Configuration Manager PowerShell cmdlets:

     Export-CMApplication
     Import-CMApplication

For more information, see Import and export applications.

Copy (application)
Duplicate the application to create a new one. This action is useful to test something or
when you need to create a similar application. The site creates a new application, and

<!-- p.192 -->

appends -copy to the name. While the site copies most of the metadata to the new
application, it doesn't copy any deployments.

Delete (application)
Delete the currently selected applications.

You can't delete an application if any of the following conditions are true:

     Other applications are dependent on it
     It has an active deployment
     It has dependent task sequences

Before you delete an application, retire it.

Simulate deployment
Test the results of an application deployment to computers without installing or
uninstalling it. For more information, see Simulate application deployments.

Deploy
Deploy the selected application to a collection of computers. For more information, see
Deploy applications.

Create phased deployment
Phased deployments automate a coordinated, sequenced rollout of software across
multiple collections. For example, deploy software to a pilot collection, and then
automatically continue the rollout based on success criteria. For more information, see
Create phased deployments.

Distribute content
Copy the content for the selected application to distribution points. For more
information, see Distribute content.

Move
Move the selected application to another folder in the Applications node.

<!-- p.193 -->

Set security scopes
Select the security scopes for the selected application. For more information, see
Security scopes.

Categorize
Administrative categories help you organize apps in the Configuration Manager console.
You can add the Administrative categories column to the Applications node.

With this action, you can:

     Quickly add the selected app to an administrative category.

     Clear all categories on the current app.

     Select Manage categories to create, rename, or delete categories.

You can also manage categories on the application properties, General information tab.

   Tip

  To help users find apps by category in Software Center, define user categories for
  your apps. You can add these categories on the application properties, Software
  Center tab.

View relationships
Show a graphical diagram of the relationships of the selected applications to other
applications. Choose one of the following relationship types:

     Dependency: Shows applications that are dependent on the selected application
     and the applications that the selected application depends on. For more
     information, see Deployment type Dependencies.

     Supersedence: Shows applications that the selected application supersedes, and
     applications that the selected application is superseded by. For more information,
     see Supersedence.

     Global Conditions: Shows the global conditions that this application references.
     For more information, see Create global conditions.

<!-- p.194 -->

Properties
Display and edit the metadata for this application.

Manage deployment types
In the Software Library workspace, expand Application Management, and select the
Applications node. Select the application with the deployment type that you want to
manage. In the details pane, switch to the Deployment Types tab. Select the
deployment type that you want to manage, and then choose a management task from
the Deployment Type tab of the ribbon.

Increase priority
Increase the priority of the selected deployment type. The Configuration Manager client
evaluates deployment types in order. If the device meets the deployment type's
requirements, it runs the deployment type. Then the client doesn't evaluate any further
deployment types on the priority list.

Decrease priority
Lower the priority of the selected deployment type.

Copy (deployment type)
Duplicate the deployment type to create a new one. This action is useful to test
something or when you need to create a similar deployment type. The site creates a new
deployment type on the same application, and appends -copy to the name.

Delete (deployment type)
Delete the selected deployment type. You can't delete a deployment type if it's
referenced by a deployment type in another application.

To delete a deployment type:

   1. Remove all dependencies from other deployment types.

   2. Remove previous revisions of all applications that have a deployment type that
     references this deployment type.

<!-- p.195 -->

Update content
Refresh the content for the selected deployment type. When you refresh the content of
a deployment type, the site creates a new revision of the application. This behavior
might cause client devices to update with the new application content.

Next steps
Import and export applications

Revise and supersede applications

Uninstall applications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.196 -->

Link users and devices with user device
affinity in Configuration Manager
Article • 02/22/2023

Applies to: Configuration Manager (current branch)

User device affinity in Configuration Manager associates a user with one or more
devices. This behavior can eliminate the need to know the names of a user's devices to
deploy an application to the user. Instead of deploying the application to each of the
user's devices, you deploy the application to the user. Then, user device affinity
automatically makes sure that the application installs on all devices that are associated
with that user.

Define primary devices that users use every day for their work. When you create an
affinity between a user and a device, you gain more app deployment options. For
example, if a user requires Microsoft Visio, you can install it on the user's primary device
by using a Windows Installer deployment. However, on a device that's not a primary
device, you might deploy Visio as a virtual application. You also can use user device
affinity to predeploy software on a user's device when the user isn't signed in. Then
when the user logs on, the app is already installed and ready to run.

You only manage user device affinity information for computers. Configuration Manager
automatically manages user device affinities for the mobile devices that it enrolls.

Manually set up user device affinity
   1. In the Configuration Manager console, go to the Assets and Compliance
      workspace, and select the Devices node.

   2. Select a device. On the Home tab in the ribbon, in the Device group, choose Edit
      Primary Users.

   3. In the Edit Primary Users dialog box, search for and then select the users to add as
      primary users for the selected device. Choose Add.

        ７ Note

        The Primary Users list shows users who are already primary users of this
        device, and the method by which each user-device relationship was assigned.

<!-- p.197 -->

Set up primary devices for a user
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the Users node.

   2. Select a user. On the Device tab in the ribbon, choose Edit Primary Devices.

   3. In the Edit Primary Devices dialog box, search for and then select the devices to
     add as primary devices for the selected user. Choose Add.

        ７ Note

        The Primary Devices list shows devices that are already set up as primary
        devices for this user, and the method by which each user-device relationship
        was assigned.

Automatically create user device affinities
(Windows PCs only)
Configuration Manager reads data about user logon events from the Windows event
log. To automatically create user device affinities, turn on these two options in the local
security policy on client computers to store logon events in the Windows event log:

     Audit account logon events
     Audit logon events

To configure these settings, use Windows Group Policy.

  ） Important

  If an error causes the Windows event log to generate a high number of entries, it
  might create a new event log. If this behavior occurs, existing logon events might
  not be available to Configuration Manager.

Set up the site to automatically create user device
affinities
   1. In the Configuration Manager console, go to the Administration workspace, and
     select the Client Settings node.

<!-- p.198 -->

   2. To modify the default client settings, select Default Client Settings. On the Home
     tab in the ribbon, in the Properties group, choose Properties. If you modify the
     default client settings, the site deploys them to all computers in the hierarchy. For
     more information, see How to configure client settings.

           To create custom client agent settings, on the Home tab in the ribbon, in the
           Create group, choose Create Custom Client Device Settings.

   3. In the User and Device Affinity group, set the following settings:

           User device affinity threshold (minutes): Set the number of minutes of
           device usage before the site creates a user device affinity.

           User device affinity threshold (days): Set the number of days over which the
           site measures the usage-based affinity threshold.

           Automatically configure user device affinity from usage data: Select True to
           let the site automatically create user device affinities. If you select False, you
           need to manually approve all user device affinity assignments.

As an example, if you set User device affinity threshold (minutes) to 60 minutes and
you set User device affinity threshold (days) to 5 days, the user must use the device for
at least 60 minutes over a period of 5 days to automatically create a user device affinity.

After Configuration Manager creates an automatic user device affinity, it continues to
monitor the user device affinity thresholds. If the user's activity for the device falls below
the thresholds you've set, the site removes the user device affinity. Set User device
affinity threshold (days) to a value of at least seven days. This configuration avoids
situations in which an automatically configured user device affinity might be lost while
the user isn't signed in, for example, during the weekend.

  ７ Note

  Starting in Configuration Manager version 2010, the troubleshooting portal in the
  Microsoft Intune admin center        allows you to search for a user and view their
  associated devices. Tenant attached devices that are assigned user device affinity
  automatically based on usage are returned when searching for a user. For more
  information, see Tenant attach: ConfigMgr client details in the admin center.

Import user device affinities from a file

<!-- p.199 -->

To create many relationships at one time, import a file that has the details for multiple
user device affinities. Make sure the target devices are already discovered by the site
and exist as resources in the Configuration Manager database.

   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select either the Users or Devices node.

   2. On the Home tab in the ribbon, in the Create group, choose Import User Device
     Affinity.

   3. In the Import User Device Affinity Wizard, on the Choose Mapping page, set this
     information:

           File name. Specify a comma-separated values (CSV) file that has a list of users
           and devices between which you want to create an affinity. In this file, each
           user-and-device pair must be on its own row, with values separated by a
           comma. Use this format: <domain>\<username>,<device NetBIOS name>

           This file has column headings for reference purposes. If the .csv file has a
           top-row header, select this option. The site ignores the header row during the
           import.

   4. If the file you import has more than two items in each row, use Column and Assign
     to specify which columns represent users and devices, and which columns to
     ignore during import.

   5. Complete the wizard.

Let users create their own device affinities
Set up a user to create their own user device affinity in Software Center.

Set up the site to allow user-created user device affinity
requests
1 In the Configuration Manager console, go to the Administration workspace, and
select the Client Settings node.

   1. To modify the default client settings, select Default Client Settings. On the Home
     tab in the ribbon, in the Properties group, choose Properties.

     To create custom client agent settings, on the Home tab in the ribbon, in the
     Create group, choose Create Custom Client User Settings.

<!-- p.200 -->

        ７ Note

        If you modify the default client settings, the site deploys them to all
        computers in the hierarchy. For more information, see Configure client
        settings.

   2. In the User and Device Affinity group, enable the setting to Allow user to define
     their primary devices.

Set up a user device affinity in Software Center
Users can use Software Center to set affinity.

   1. In Software Center, go to the Options tab.

   2. In the Work information section, select the option I regularly use this computer
     to do my work.

Manage user device affinity requests from
users
When you disable the client setting to Automatically configure user device affinity
from usage data, you need to manually approve all user device affinity assignments.

Approve or reject a user device affinity request
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace.

   2. Select the user or device collection for which you want to manage affinity requests.

   3. On the Home tab in the ribbon, in the Collection group, choose Manage Affinity
     Requests.

   4. In the Manage User Device Affinity Requests dialog box, select an affinity request,
     and then choose Approve or Reject.

Next steps
You can also use Microsoft Intune to find the primary use of an enrolled device. For
more information, see Find the primary user of an Intune device in the Intune
