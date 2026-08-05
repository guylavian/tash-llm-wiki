---
title: "Software update management documentation — pages 201-240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0201-0240
family: sccm
documentKind: "doc"
abstract: "5. Select the Props property, select Edit Property, and then View Embedded. 6. Starting at the first query result, open each object until you find the one with AvailableUpdateLanguagesForO365 for the PropertyName property. 7. Select Value2 and choose Edit Property. 8. Add additi"
---

# Software update management documentation — pages 201-240

<!-- p.201 -->

5. Select the Props property, select Edit Property, and then View Embedded.

6. Starting at the first query result, open each object until you find the one with
  AvailableUpdateLanguagesForO365 for the PropertyName property.

7. Select Value2 and choose Edit Property.

<!-- p.202 -->

   8. Add additional languages to the Value2 property and select Save Property.
     For example, 2057 (for en-gb), 2058 (for es-mx), and 3084 (for fr-ca), you would
     type 2057, 2058, 3084 for the example languages.

   9. Select Close, select Close, select Save Property, and choose Save Object (if you
     select Close here the values are discarded). SelectClose, and then Exit to exit the
     Windows Management Instrumentation Tester.

 10. In the Configuration Manager console, go to Software Library > Overview >
     Office 365 Client Management > Office 365 Updates.

 11. When you download Microsoft 365 Apps updates, the updates are downloaded in
     the languages that you select in the wizard and configured in this procedure. To
     verify that the updates download in the correct languages, go to the package
     source for the update and find files with the new language code in the filename.

Updating Microsoft 365 Apps in a task
sequence
When using Install Software Updates task sequence step to Install Microsoft 365 Apps
updates, it is possible that deployed updates will be detected as not applicable. This
might happen if the scheduled Office Automatic Updates task hasn't run at least once
(see the note in Deploy Microsoft 365 Apps updates). For example, this might happen if
Microsoft 365 Apps was installed immediately before running this step.

<!-- p.203 -->

To ensure that the update channel is set so that deployed updates will be properly
detected, use one of the following methods:

Method 1:

   1. On a machine with the same version of Microsoft 365 Apps, open Task Scheduler
     (taskschd.msc) and identify the Microsoft 365 Apps automatic updates task.
     Typically, it is located under Task Scheduler Library >Microsoft>Office.
   2. Right-click on the automatic updates task and select Properties.
   3. Go to the Actions tab and choose Edit. Copy the command and any arguments.
   4. In the Configuration Manager console, edit your task sequence.
   5. Add a new Run Command Line step before the Install Software Updates step in
     the task sequence. If Microsoft 365 Apps is installed as part of the same task
     sequence, make sure this step runs after Office is installed.
   6. Copy in the command and arguments that you gathered from the Office automatic
     updates scheduled task.
   7. Select OK.

Method 2:

   1. On a machine with the same version of Microsoft 365 Apps, open Task Scheduler
     (taskschd.msc) and identify the Microsoft 365 Apps automatic updates task.
     Typically, it is located under Task Scheduler Library >Microsoft>Office.

   2. In the Configuration Manager console, edit your task sequence.

   3. Add a new Run Command Line step before the Install Software Updates step in
     the task sequence. If Microsoft 365 Apps is installed as part of the same task
     sequence, make sure this step runs after Office is installed.

   4. In the command line field, enter the command line that will run the scheduled task.
     See example below making sure the string in quotes matches the path and name
     of the task identified in step 1.

     Example: schtasks /run /tn "\Microsoft\Office\Office Automatic Updates 2.0"

   5. Select OK.

Update channels for Microsoft 365 Apps
When Office 365 ProPlus was renamed to Microsoft 365 Apps for enterprise, the
update channels were also renamed. If you use an automatic deployment rule (ADR) to
deploy updates, you'll need to make changes to your ADRs if they rely on the Title

<!-- p.204 -->

property. That's because the name of update packages in the Microsoft Update Catalog
is changing.

Currently, the title of an update package for Office 365 ProPlus begins with "Office 365
Client Update" as seen in the following example:

  Office 365 Client Update - Semi-annual Channel Version 1908 for x64 based Edition
(Build 11929.20648)

For update packages released on and after June 9, 2020, the title will begin with
"Microsoft 365 Apps Update" as seen in the following example:

  Microsoft 365 Apps Update - Semi-annual Channel Version 1908 for x64 based
Edition (Build 11929.50000)

                                                                             ﾉ   Expand table

 New Channel name                 Previous     CDNBaseUrl
                                  Channel
                                  name

 Semi-Annual Enterprise Channel   Semi-        http://officecdn.microsoft.com/pr/7ffbc6bf-
                                  Annual       bc32-4f92-8982-f9dd17fd3114
                                  Channel

 Semi-Annual Enterprise Channel   Semi-        http://officecdn.microsoft.com/pr/b8f9b850-
 (Preview)                        Annual       328d-4355-9145-c59439a0c4cf
                                  Channel
                                  (Targeted)

 Monthly Enterprise Channel       NA           http://officecdn.microsoft.com/pr/55336b82-
                                               a18d-4dd6-b5f6-9e5095c314a6

 Current Channel                  Monthly      http://officecdn.microsoft.com/pr/492350f6-
                                  Channel      3a01-4f97-b9c0-c7c6ddf67d60

 Current Channel (Preview)        Monthly      http://officecdn.microsoft.com/pr/64256afe-
                                  Channel      f5d9-4f86-8936-8840a6a4f5be
                                  (Targeted)

 Beta Channel                     Insider      http://officecdn.microsoft.com/pr/5440fd1f-
                                               7ecb-4221-8110-145efaa6372f
 Beta Channel needs to be
 updated from the Office CDN
 on the internet instead of
 having Configuration Manager
 manage the update process. For
 more information, see Use

<!-- p.205 -->

 New Channel name                    Previous   CDNBaseUrl
                                     Channel
                                     name

 Configuration Manager to install
 Office Insider builds   .

For more information about how to modify your ADRs, see Automatically deploy
software updates. For more information about the name change, see Name change for
Office 365 ProPlus.

Change the update channel after you enable
Microsoft 365 Apps clients to receive updates
from Configuration Manager
After deploying Microsoft 365 Apps, you can change the update channel with Group
Policy or the Office Deployment Tool (ODT). For example, you can move a device from
Semi-Annual Channel to Semi-Annual Channel (Targeted). When changing the channel,
Office is updated automatically without having to reinstall or download the full version.
For more information, see Change the Microsoft 365 Apps update channel for devices in
your organization.

Next steps
Use the Office 365 Client Management dashboard in Configuration Manager to review
Microsoft 365 Apps client information and deploy Microsoft 365 Apps. For more
information, see Office 365 Client Management dashboard.

Feedback
Was this page helpful?        Yes    No

Provide product feedback

<!-- p.206 -->

Monitor software updates in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager provides many ways to help you to monitor software updates
objects, processes, and compliance information. Use the following sections to monitor
software updates.

Software updates dashboard
You can use the Software Updates Dashboard to view the current compliance status of
devices in your organization and quickly analyze the data to see which devices are at
risk. To view the dashboard, navigate to Monitoring > Overview > Security > Software
Updates Dashboard.

Drill through required updates
You can drill through compliance statistics to see which devices require a specific
Microsoft 365 Apps software update. To view the device list, you need permission to
view updates and the collections the devices belong to. To drill down into the device list:

   1. Go to Software Library > Software Updates > All Software Updates.
   2. Select any update that is required by at least one device.
   3. Look at the Summary tab and find the pie chart under Statistics.
   4. Select the View Required hyperlink next to the pie chart to drill down into the
      device list.
   5. This action takes you to a temporary node under Devices where you can see the
      devices requiring the update. You can also take actions for the node such as
      creating a new collection from the list.

Alerts for software updates
You can configure alerts for software updates to notify administrative users when
compliance levels for software update deployments are below the configured
percentage. You can configure alerts for software update deployments in the following
locations:

<!-- p.207 -->

     ADR setting: You can configure the alerts settings in the Automatic Deployment
     Rule Wizard and in the properties for the ADR.

     Deployment setting: You can configure the alerts settings in the Deploy Software
     Updates Wizard and in deployment properties.

After you configure the alert settings, if the specified conditions occur, Configuration
Manager generates an alert. You can review software update alerts at the following
locations:

   1. Review recent alerts in the Software Updates node in the Software Library
     workspace.

   2. Manage the configured alerts in the Alerts node in the Monitoring workspace.

Software updates synchronization status
After you start the synchronization process, you can monitor the synchronization
process from the Configuration Manager console for all software update points in your
hierarchy. Use the following procedure to monitor the software update synchronization
process.

To monitor the software updates synchronization process
     In the Configuration Manager console, navigate to Monitoring > Overview >
     Software Update Point Synchronization Status.

     The software update points in your Configuration Manager hierarchy are displayed
     in the results pane. From this view, you can monitor the synchronization status for
     all software update points. To see more detailed information about the
     synchronization process, you can review the wsyncmgr.log file, which is located in
     <ConfigMgrInstallationPath>\Logs on each site server.

Software update deployment status
After you deploy the software updates in a software update group or deploy an
individual software update, you can monitor the deployment status. Use the following
procedure to monitor the deployment status for a software update group or software
update.

To monitor deployment status

<!-- p.208 -->

   1. In the Configuration Manager console, navigate to Monitoring > Overview >
     Deployments.

   2. Click the software update group or software update for which you want to monitor
     the deployment status.

   3. On the Home tab, in the Deployment group, click View Status.

   Tip

        Starting in version 2107, you can right-click the status of a deployment and
        select Evaluate Software Update Deployments to send a notification to the
        selected devices to run a software update deployment evaluation cycle.
        Starting in version 2203, you can perform client notification actions, including
        Run Scripts, from the Deployment Status view. Use the right-click menu on
        either a group of clients in a Category or a single client in the Asset details
        pane to display the client notification actions.

Software updates reports
The state messages for software updates provide information about the compliance of
software updates and about the evaluation and enforcement state of software update
deployments. You can run software update reports to display these state messages.
There are more than 30 predefined software update reports available. They're organized
in several categories and can be used to report on specific information about software
updates and deployments. In addition to using the preconfigured reports, you can also
create custom software update reports according to the needs of your enterprise. For
more information, see Operations and maintenance for reporting.

  ７ Note

  Devices running an unsupported operating systems will display as compliant since
  there aren't applicable updates to the operating system any longer.

Recommended software updates reports
The following are some of the reports that are useful in identifying potential issues:

<!-- p.209 -->

Compliance 9 - Overall health and compliance (starting in version
1806)

The report includes the following parts:

     Healthy Clients vs Total Clients: This bar chart compares the "healthy" clients that
     have communicated with the site in the specified time period against the total
     number of clients in the specified collection.
     Compliance Overview: This pie chart shows overall compliance state for the
     specific software update group on active clients in the specified collection.
     Top 5 Non-Compliant by Article ID: This bar chart displays the top five software
     updates in the specified group that are non-compliant on active clients in the
     specified collection.
     The bottom of the report is a table with further details, which lists the software
     updates in the specified group.

Management 2 - Updates required but not deployed
This report displays vendor-specific software updates in a specific updates classification
that have been detected as required on clients but that have not been deployed to a
specific collection.

Troubleshooting 2 - Deployment errors
This report returns the deployment errors at the site and a count of computers that are
experiencing each error.

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

<!-- p.210 -->

status for the package, and detailed status information about the package. Use the
following procedure to view content status.

To monitor content status

   1. In the Configuration Manager console, navigate to Monitoring > Overview >
     Distribution Status > Content Status. The packages are displayed.

   2. Select the package for which to view detailed status information.

   3. On the Home tab, click View Status. Detailed status information for the package is
     displayed.

Distribution point group status
The Distribution Point Group Status node in the Monitoring workspace provides
information about distribution point groups. You can review general information about
the distribution point group, such as distribution point group status and compliance
rate, as well as detailed status information for the distribution point group. Use the
following procedure to view distribution point group status.

To monitor distribution point group status
   1. In the Configuration Manager console, navigate to Monitoring > Overview >
     Distribution Status > Distribution Point Group Status. The distribution point
     groups are displayed.

   2. Select the distribution point group for which to view detailed status information.

   3. On the Home tab, click View Status. Detailed status information for the
     distribution point group is displayed.

Distribution point configuration status
The Distribution Point Configuration Status node in the Monitoring workspace
provides information about the distribution point. You can review which attributes are
enabled for the distribution point, such as the PXE, Multicast, and content validation.
You can also view detailed status information for the distribution point. Use the
following procedure to view distribution point configuration status.

To monitor distribution point configuration status

<!-- p.211 -->

   1. In the Configuration Manager console, navigate to Monitoring > Overview >
     Distribution Status > Distribution Point Configuration Status. The distribution
     points are displayed.

   2. Select the distribution point for which to view distribution point status information.

   3. In the results pane, click the Details tab. Status information for the distribution
     point is displayed.

Next steps
     Log files for Software Updates

     Software Updates management whitepaper

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.212 -->

Manage and monitor phased
deployments
Article • 10/04/2022

This article describes how to manage and monitor phased deployments. Management
tasks include manually beginning the next phase, and suspend or resume a phase.

First, you need to create a phased deployment:

      Application
      Software update
      Task sequence

Move to the next phase
When you select the setting, Manually begin the second phase of deployment, the site
doesn't automatically start the next phase based on success criteria. You need to move
the phased deployment to the next phase.

   1. How to start this action varies based on the type of deployed software:

            Application: Go to the Software Library workspace, expand Application
            Management, and select Applications.

            Software update: Go to the Software Library workspace, and then select one
            of the following nodes:
               Software Updates
                  All Software Updates
                  Software Update Groups
               Windows Servicing, All Windows Updates
               Office 365 Client Management, Office 365 Updates

            Task sequence: Go to the Software Library workspace, expand Operating
            Systems, and select Task Sequences.

   2. Select the software with the phased deployment.

   3. In the details pane, switch to the Phased Deployments tab.

   4. Select the phased deployment, and click Move to next phase in the ribbon.

<!-- p.213 -->

Optionally, use the following Windows PowerShell cmdlet for this task: Move-
CMPhasedDeploymentToNext.

Suspend and resume phases
You can manually suspend or resume a phased deployment. For example, you create a
phased deployment for a task sequence. While monitoring the phase to your pilot
group, you notice a large number of failures. You suspend the phased deployment to
stop further devices from running the task sequence. After resolving the issue, you
resume the phased deployment to continue the rollout.

   1. How to start this action varies based on the type of deployed software:

          Application: Go to the Software Library workspace, expand Application
          Management, and select Applications.

          Software update: Go to the Software Library workspace, and then select one
          of the following nodes:
             Software Updates
                All Software Updates
                Software Update Groups
             Windows Servicing, All Windows Updates
             Office 365 Client Management, Office 365 Updates

          Task sequence: Go to the Software Library workspace, expand Operating
          Systems, and select Task Sequences. Select an existing task sequence, and
          then click Create Phased Deployment in the ribbon.

   2. Select the software with the phased deployment.

   3. In the details pane, switch to the Phased Deployments tab.

   4. Select the phased deployment, and click Suspend or Resume in the ribbon.

<!-- p.214 -->

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365
  Apps for enterprise. For more information, see Name change for Office 365
  ProPlus. You may still see the old name in the Configuration Manager product and
  documentation while the console is being updated.

Optionally, use the following Windows PowerShell cmdlets for this task:

     Suspend-CMPhasedDeployment
     Resume-CMPhasedDeployment

Monitor
Phased deployments have their own dedicated monitoring node, making it easier to
identify phased deployments you have created and navigate to the phased deployment
monitoring view. From the Monitoring workspace, select Phased Deployments, then
double-click one of the phased deployments to see the status.

<!-- p.215 -->

This dashboard shows the following information for each phase in the deployment:

     Total devices or Total resources: How many devices are targeted by this phase.

     Status: The current status of this phase. Each phase can be in one of the following
     states:

        Deployment created: The phased deployment created a deployment of the
        software to the collection for this phase. Clients are actively targeted with this
        software.

        Waiting: The previous phase hasn't yet reached the success criteria for the
        deployment to continue to this phase.

        Suspended: An administrator suspended the deployment.

     Progress: The color-coded deployment states from clients. For example: Success, In
     Progress, Error, Requirements Not Met, and Unknown.

<!-- p.216 -->

Success criteria tile
Use the Select Phase drop-down list to change the display of the Success Criteria tile.
This tile compares the Phase Goal against the current compliance of the deployment.
With the default settings, the phase goal is 95%. This value means that the deployment
needs a 95% compliance to move to the next phase.

In the example, the phase goal is 65%, and the current compliance is 66.7%. The phased
deployment automatically moved to the second phase, because the first phase met the
success criteria.

The phase goal is the same as the Deployment success percentage on the Phase
Settings for the next phase. For the phased deployment to start the next phase, that
second phase defines the criteria for success of the first phase. To view this setting:

   1. Go to the phased deployment object on the software, and open the Phased
     Deployment Properties.

   2. Switch to the Phases tab. Select Phase 2 and click View.

   3. In the phase Properties window, switch to the Phase Settings tab.

   4. View the value for Deployment success percentage in the Criteria for success of the
     previous phase group.

For example, the following properties are for the same phase as the success criteria tile
shown above where the criteria is 65%:

<!-- p.217 -->

PowerShell
Use the following Windows PowerShell cmdlets to manage phased deployments:

Automatically create phased deployments
    New-CMApplicationAutoPhasedDeployment
    New-CMSoftwareUpdateAutoPhasedDeployment
    New-CMTaskSequenceAutoPhasedDeployment

Manually create phased deployments
    New-CMSoftwareUpdatePhase
    New-CMSoftwareUpdateManualPhasedDeployment
    New-CMTaskSequencePhase
    New-CMTaskSequenceManualPhasedDeployment

<!-- p.218 -->

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

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.219 -->

Software updates maintenance
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can schedule and run WSUS cleanup tasks from the Configuration Manager console
from the Software Update Point Component properties. When you first select to run the
WSUS cleanup task, it will run after the next software updates synchronization.

To schedule and run the WSUS cleanup job
Schedule the WSUS cleanup job by running the following steps:

   1. In the Configuration Manager console, navigate to Administration > Overview >
      Site Configuration > Sites.

   2. Select the site at the top of your Configuration Manager hierarchy.

   3. Click Configure Site Components in the Settings group, and then click Software
      Update Point to open Software Update Point Component Properties.

   4. Review the Supersedence behavior. Modify the behavior if needed.

   5. Click the Supersedence Rules tab, select Run WSUS cleanup wizard. In version
      1806, the option is renamed to Run WSUS cleanup after synchronization.

   6. Click OK (Click Close if you're running version 1806).

WSUS cleanup behavior in version 1802 and
earlier
Before Configuration Manager version 1806, the WSUS cleanup option runs the
following item:

<!-- p.220 -->

        The Expired updates option from the WSUS cleanup wizard on the top-level site's
        WSUS server only.

        A cleanup for software update configuration items in the Configuration Manager
        database occurs every seven days and removes unneeded updates from the
        console.
          This cleanup won't remove expired updates from the Configuration Manager
          console if they're currently deployed.

Additional maintenance is still needed on the top-level WSUS database and all other
WSUS databases in the environment. For more information and instructions, see The
complete guide to Microsoft WSUS and Configuration Manager SUP maintenance blog
post.

WSUS cleanup behavior starting in version
1806
Starting version 1806, the WSUS cleanup option occurs after every sync and does the
following cleanup items:

        The Expired updates option for WSUS servers on CAS and primary sites.
          WSUS servers for secondary sites don't run the WSUS cleanup for expired
          updates.

<!-- p.221 -->

         Configuration Manager builds a list of superseded updates from its database. The
         list is based on the supersedence behavior in the Software Update Point
         component properties.
            The update configuration items meeting the supersedence behavior criteria are
            expired in the Configuration Manager console.
            The updates are declined in WSUS for CAS and primary sites but not for
            secondary sites.
         A cleanup for software update configuration items in the Configuration Manager
         database occurs every seven days and removes unneeded updates from the
         console.
            This cleanup won't remove expired updates from the Configuration Manager
            console if they're currently deployed.

  ７ Note

  The "Months to wait before a superseded update is expired" is based on the
  creation date of the superseding update. For example, if you use 2 months for this
  setting, then updates that have been superseded will be declined in WSUS and
  expired in Configuration Manager when the superceding update is 2 months old.

All WSUS maintenance needs to be run manually on secondary site WSUS databases.
The following WSUS Server Cleanup Wizard options aren't run on the CAS and primary
sites:

         Unused updates and update revisions

         Computers not contacting the server

         Unneeded update files

         For more information and instructions, see The complete guide to Microsoft WSUS
         and Configuration Manager SUP maintenance blog post.

WSUS cleanup behavior starting in version 1810
Starting version 1810, you can specify supersedence rules for feature updates separately
from non-feature updates in the Software Update Point component properties. The
WSUS cleanup option occurs after every sync and does the following cleanup items:

         The Expired updates option for WSUS servers on CAS, primary, and secondary
         sites.

<!-- p.222 -->

     Configuration Manager builds a list of superseded updates from its database. The
     list is based on the supersedence behavior in the Software Update Point
     component properties.
        The update configuration items meeting the supersedence behavior criteria are
        expired in the Configuration Manager console.
        The updates are declined in WSUS for CAS, primary, and secondary sites.
     A cleanup for software update configuration items in the Configuration Manager
     database occurs every seven days and removes unneeded updates from the
     console.
        This cleanup won't remove expired updates from the Configuration Manager
        console if they're currently deployed.

  ７ Note

  The "Months to wait before a superseded update is expired" is based on the
  creation date of the superseding update. For example, if you use 2 months for this
  setting, then updates that have been superseded will be declined in WSUS and
  expired in Configuration Manager when the superceding update is 2 months old.

The following WSUS Server Cleanup Wizard options aren't run on the CAS, primary, and
secondary sites:

     Unused updates and update revisions

     Computers not contacting the server

     Unneeded update files

     For more information and instructions, see The complete guide to Microsoft WSUS
     and Configuration Manager SUP maintenance blog post.

WSUS cleanup starting in version 1906
You have additional WSUS maintenance tasks that Configuration Manager can run to
maintain healthy software update points. In addition to declining expired updates in
WSUS, Configuration Manager can add non-clustered indexes to the WSUS databases
and remove obsolete updates from the WSUS databases. The WSUS maintenance
occurs after every synchronization.

Decline expired updates in WSUS according to
supersedence rules

<!-- p.223 -->

Declining updates in WSUS improves performance by removing those updates from the
catalogs sent to clients. Declining updates that Configuration Manager marks as
superseded further minimizes the catalogs and improves performance.

   1. In the Configuration Manager console, navigate to Administration > Overview >
     Site Configuration > Sites.
   2. Select the site at the top of your Configuration Manager hierarchy.
   3. Click Configure Site Components in the Settings group, and then click Software
     Update Point to open Software Update Point Component Properties.
   4. In the WSUS Maintenance tab, select Decline expired updates in WSUS according
     to supersedence rules.

Add non-clustered indexes to the WSUS database to
improve WSUS cleanup performance
The addition of non-clustered indexes improves the WSUS cleanup performance that
Configuration Manager does.

   1. In the Configuration Manager console, navigate to Administration > Overview >
     Site Configuration > Sites.
   2. Select the site at the top of your Configuration Manager hierarchy.
   3. Click Configure Site Components in the Settings group, and then click Software
     Update Point to open Software Update Point Component Properties.
   4. In the WSUS Maintenance tab, select Add non-clustered indexes to the WSUS
     database.
   5. On each SUSDB used by Configuration Manager, indexes are added to the
     following tables:

          tbLocalizedPropertyForRevision
          tbRevisionSupersedesUpdate

SQL Server permissions for creating indexes

When the WSUS database is on a remote SQL Server, you might need to add
permissions in SQL Server to create indexes. The account used to connect to the WSUS
database and create the indexes can vary. If you specify a WSUS Server Connection
Account in the software update point properties, then ensure the connection account
has the SQL Server permissions. If you don't specify a WSUS Server Connection Account,
then the site server's computer account needs the SQL Server permissions.

     Creating an index requires ALTER permission on the table or view. The account
     must be a member of the sysadmin fixed server role or the db_ddladmin and

<!-- p.224 -->

     db_owner fixed database roles. For more information about creating and index and

     permissions, see CREATE INDEX (Transact-SQL).
     The CONNECT SQL server permission must be granted to the account. For more
     information, see GRANT Server Permissions (Transact-SQL).

  ７ Note

       If the WSUS database is on a remote SQL Server using a non-default port,
       then indexes might not be added. You can create a server alias using SQL
       Server Configuration Manager for this scenario. Once the alias is added and
       Configuration Manager can make a connection to the WSUS database,
       indexes will be added.
       If the Software Update Point is remote to the site server and is using a
       Windows Internal Database, then the indexes will not be added.

Remove obsolete updates from the WSUS database
Obsolete updates are unused updates and update revisions in the WSUS database.
Generally speaking, an update is considered obsolete once it's no longer in the
Microsoft Update Catalog     and it isn't needed by other updates as a prerequisite or
dependency.

   1. In the Configuration Manager console, navigate to Administration > Overview >
     Site Configuration > Sites.
   2. Select the site at the top of your Configuration Manager hierarchy.
   3. Click Configure Site Components in the Settings group, and then click Software
     Update Point to open Software Update Point Component Properties.
   4. In the WSUS Maintenance tab, select Remove obsolete updates from the WSUS
     database.

           The obsolete update removal will be allowed to run for a maximum of 30
           minutes before being stopped. It will start up again after the next
           synchronization occurs.

SQL Server permissions for removing obsolete updates
When the WSUS database is on a remote SQL Server, the site server's computer account
needs the following SQL Server permissions:

<!-- p.225 -->

     The db_datareader and db_datawriter fixed database roles. For more information,
     see Database-Level Roles.
     The CONNECT SQL server permission must be granted to the site server's computer
     account. For more information, see GRANT Server Permissions (Transact-SQL).

  ７ Note

  If the Software Update Point is remote to the site server and is using a Windows
  Internal Database, then obsolete updates will not be removed.

WSUS cleanup wizard

Starting in version 1906, the following WSUS Server Cleanup Wizard options aren't run
on the CAS, primary, and secondary sites:

     Computers not contacting the server

     Unneeded update files

     For more information and instructions, see The complete guide to Microsoft WSUS
     and Configuration Manager SUP maintenance blog post.

Known issue
Consider the following scenario:

     You are using Configuration Manager version 1906 or later
     You have remote software update points using a Windows Internal Database
     In the Software Update Point Component Properties, you have any of the
     following selected options under the WSUS Maintenance tab:
         Add non-clustered indexes to the WSUS database
         Remove obsolete updates from the WSUS database

In this scenario, Configuration Manager is unable to perform the above WSUS
Maintenance tasks for the remote Software Updates Points using a Windows Internal
Database. This issue occurs because Windows Internal Database doesn't allow remote
connections. You'll see the following errors in the WSyncMgr.log on the site server:

  text

  Indexing Failed. Could not connect to SUSDB.
  SqlException thrown while connect to SUSDB in Server: <SUP.CONTOSO.COM>.

<!-- p.226 -->

  Error Message: A network-related or instance-specific error occurred while
  establishing a connection to SQL Server. The server was not found or was not
  accessible. Verify that the instance name is correct and that SQL Server is
  configured to allow remote connections. (provider: Named Pipes Provider,
  error: 40 - Could not open a connection to SQL Server)
  ...
  Could not Delete Obselete Updates because ConfigManager could not connect to
  SUSDB: A network-related or instance-specific error occurred while
  establishing a connection to SQL Server. The server was not found or was not
  accessible. Verify that the instance name is correct and that SQL Server is
  configured to allow remote connections. (provider: Named Pipes Provider,
  error: 40 - Could not open a connection to SQL Server) UpdateServer:
  <SUP.CONTOSO.COM>

To work around the issue, you can automate the WSUS maintenance for the remote
software update points using a Windows Internal Database. For more information and
detailed steps, see The complete guide to Microsoft WSUS and Configuration Manager
SUP maintenance      .

Updates cleanup log entries
You can verify this cleanup by reviewing the wsyncmgr.log for the following entries:

     The decline of superseded updates in WSUS is complete when you see this log
     entry: Cleanup processed <number> total updates and declined <number>
     The WSUS cleanup is starting when you see this entry: Calling WSUS Cleanup.
     The WSUS cleanup for expired updates is complete when you see this entry:
      Successfully completed WSUS Cleanup.

     The Configuration Manager expired updates configuration items cleanup is
     starting when you see this entry: Deleting old expired updates...
     The Configuration Manager expired updates configuration items cleanup is
     complete when you see this entry: Deleted <number> expired updates total

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.227 -->

Service a server group
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ） Important

        Starting in Configuration Manager version 2002, server groups have been
        replaced by orchestration groups. For more information, see Orchestration
        groups.
        Pre-release features are features that are in the Current Branch for early
        testing in a production environment. These features are fully supported but
        are still in active development and might receive changes until they move out
        of the pre-release category. You must turn on this feature for it to be
        available. For more information, see Use pre-release features from updates.

Starting in Configuration Manager version 1606, you can configure server group settings
for a collection to define how many, what percentage, or in what order computers in the
collection will install software updates. You can also configure pre-deployment and
post-deployment PowerShell scripts to run custom actions.

When you deploy software updates to a collection that has server group settings
configured, Configuration Manager determines how many computers in the collection
can install the software updates at any given time and makes the same number of
deployment locks available. Only computers that get a deployment lock will start
software update installation. When a deployment lock is available, a computer gets the
deployment lock, installs the software updates, and then releases the deployment lock
when software updates installation successfully completes. Then, the deployment lock
becomes available for other computers. If a computer is unable to release a deployment
lock, you can manually release all server group deployment locks for the collection.

  ） Important

  All of the computers in the collection must be assigned to the same site.

To create a collection for a server group

<!-- p.228 -->

The server group settings are configured in the properties for a device collection. To
service a server group, all members in the collection must be assigned to the same site.
Use the following steps to create a collection and configure the server group settings:

   1. Create a device collection that contains the computers in the server group.

   2. In the Assets and Compliance workspace, click Device Collections, right-click the
     collection that contains the computers in the server group, and then click
     Properties.

   3. On the General tab, select All devices are part of the same server group, and then
     click Settings.

   4. On the Server Group Settings page, specify one of the following settings:

           Allow a percentage of machines to be updated at the same time: Specifies
           that only a certain percentage of clients are updated at any one time. If, for
           example, the collection has 10 clients, and the collection is configured to
           update 30% of clients at the same time, then only 3 clients will install
           software updates at any given time.

           Allow a number of machines to be updated at the same time: Specifies that
           only a certain number of clients are updated at any one time.

           Specify the maintenance sequence: Specifies that the clients in the collection
           will be updated one at a time in the sequence that you configure. A client will
           only install software updates after the client that is ahead of it in the list has
           finished installing its software updates.

   5. Specify whether to use a pre-deployment (node drain) script or post-deployment
     (node resume) script.

        ２ Warning

        Custom scripts are not signed by Microsoft. It is your responsibility to
        maintain the integrity of these scripts.

         Tip

        The following are examples that you can use in testing for pre-deployment
        and post-deployment scripts that write the current time to a text file:

        Pre-deployment

<!-- p.229 -->

        #Start

        $a = Get-Date

        Write-Output "Universal Time: " + $a.ToUniversalTime() |

        Out-File C:\Windows\Temp\start.txt

       Post-deployment

        #End

        $a = Get-Date

        Write-Output "Universal Time: " + $a.ToUniversalTime() |

        Out-File C:\Windows\Temp\end.txt

Deploy software updates to the server group
and monitor status
You deploy software updates to the server group collection by using the typical
deployment process. After you deploy the software updates, you can monitor the
software update deployment in the Configuration Manager console.

   1. Deploy software updates to the server group collection.

   2. Monitor the software update deployment. In addition to the standard monitoring
     views for software updates deployment, the Waiting for lock state is displayed
     when a client is waiting for its turn to install the software updates. You can review
     the UpdatesDeployment.log file for more information.

Clear the deployment locks for computers in a
server group
When a computer fails to release a deployment lock, you can manually release all server
group deployment locks for the collection. Clear locks only when a deployment is stuck
updating computers in the collection and there are computers that are still not
compliant.

   1. In the Assets and Compliance workspace, click Device Collections, and click the
     collection to clear deployment locks.

<!-- p.230 -->

   2. On the Home tab, in the Deployment group, click Clear Server Group
     Deployment Locks. When clients have failed to install the software updates and
     are preventing other clients from installing their software updates, the deployment
     locks can be manually cleared.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.231 -->

Software Update content delivery with
Configuration Manager
  ２ Warning

  Express Updates are no longer valid in Configuration Manager and should not be selected
  in the console. This functionality has been replaced by UUP for Windows 11 / Server 2025.
  In upcoming versions of the product, the Express Update option will be removed
  completely.

Express update delivery
This feature is no longer available and has been replaced by UUP.

Windows Delivery Optimization
Configuration Manager version 1802 added an optional client setting to simplify management
of this process by integrating boundary groups with Delivery Optimization. When this client
setting is enabled, Configuration Manager creates a unique ID for every boundary group. The
site uses the client's location information to automatically configure the client's Delivery
Optimization Group ID with the Configuration Manager boundary ID. When the client roams to
another boundary group, it talks to its management point, and is automatically reconfigured
with a new boundary group ID. With this integration, Delivery Optimization can utilize the
Configuration Manager boundary group information to find a peer from which to download
updates.

  ） Important

        When using Configuration Manager to manage software updates, the Delivery
        Optimization service must be enabled (default) and not bypassed or configured by
        any domain GPO. For more information, see Windows Delivery Optimization
        reference.

     The client setting for Delivery Optimization is not needed for UUP updates and in most
     cases this client setting should not be enabled.

Delta Download client setting

<!-- p.232 -->

Starting in Configuration Manager 2203, the Delta Download option in the software updates
client settings must be configured as follows:

     Allow clients to download delta content when available set to No.
     Port that clients use to receive requests for delta content set to 8005 (default) or a
     custom port number.

Limitations
     Delivery Optimization can't be used for Microsoft 365 Apps client updates if Office COM
     is enabled. Office COM is used by Configuration Manager to manage updates for
     Microsoft 365 Apps clients. You can deregister Office COM to allow the use of Delivery
     Optimization for Microsoft 365 Apps updates. When Office COM is disabled, software
     updates for Microsoft 365 Apps are managed by the default Office Automatic Updates 2.0
     scheduled task. This means that Configuration Manager doesn't dictate or monitor the
     installation process for Microsoft 365 Apps updates. Configuration Manager will continue
     to collect information from hardware inventory to populate Office 365 Client
     Management Dashboard in the console. For information about how to deregister Office
     COM, see Enable Office 365 clients to receive updates from the Office CDN instead of
     Configuration Manager.

     When using a CMG for content storage, the content for third-party updates won't
     download to clients if the Download delta content when available client setting is
     enabled.

     Download of feature updates for Windows may take a long time depending on the
     network and if additional content is determined to be needed for installation. This
     additional download time may also cause the installation to fail because it exceed the
     maximum runtime.

Configuration Manager peer cache
Peer cache is a feature of Configuration Manager that enables clients to share with other
clients content directly from their local Configuration Manager cache. Peer cache has several
limitations and doesn't replace the use of distribution points. It's only ideal for special
circumstances, such as a remote office with just a few employees. The number of peer cache
sources must be kept to a minimum or performance issues can occur in the site and with the
SQL database.

  ７ Note

<!-- p.233 -->

  Clients can only download content from peer cache clients that are in their current
  boundary group.

Windows BranchCache
BranchCache is a bandwidth optimization technology in Windows. Each client has a cache, and
acts as an alternate source for content. Devices on the same network can request this content.
Configuration Manager can use BranchCache to allow peers to source content from each other
versus always having to contact a distribution point. Using BranchCache, files are cached on
each individual client, and other clients can retrieve them as needed. This approach distributes
the cache rather than having a single point of retrieval. This behavior saves a significant
amount of bandwidth, while reducing the time for clients to receive the requested content.

Selecting the right technology
Even though Configuration Manager supports all of the above peer-to-peer technologies, you
should use those that make the most sense for your environment. For most customers,
assuming clients can meet the internet requirements for Delivery Optimization, the Windows
10 or later built-in Delivery Optimization settings will be sufficient. Distribution Points and
content enabled CMG's are always the preferred content delivery method.

Peer cache comparison chart

                                                                                      ﾉ   Expand table

 Functionality      Delivery Optimization            Peer cache                BranchCache

 Supported across   Yes                              Yes                       No
 subnets

 Bandwidth          Yes (Native)                     Yes (via BITS)            Yes (via BITS)
 throttling

 Partial content    Yes, for all supported content   Only for Microsoft 365    Yes, for all supported
 support            types listed in this column's    Apps and Express          content types listed in
                    next row.                        Updates                   this column's next row.

 Supported          Through ConfigMgr:               All ConfigMgr content     All ConfigMgr content
 content types      - Express updates                types, including images   types, except images
                    - All Windows updates            downloaded in Windows
                    (starting version 1910). This    PE
                    doesn't include Microsoft 365
                    Apps updates.

<!-- p.234 -->

 Functionality     Delivery Optimization            Peer cache                   BranchCache

                   Through Microsoft cloud:
                   - Windows and security
                   updates
                   - Drivers
                   - Windows Store apps
                   - Windows Store for Business
                   apps

 Cache size on     Yes                              Yes                          Yes
 disk control

 Discovery of a    Automatic                        Manual (client agent         Automatic
 peer source                                        setting)

 Peer discovery    Via Delivery Optimization        Via management point         Multicast
                   cloud service (requires          (based on client
                   internet access)                 boundary groups)

 Reporting         Update Compliance                ConfigMgr client data        ConfigMgr client data
                                                    sources dashboard            sources dashboard

 WAN usage         Yes (native, can be controlled   Boundary groups              Subnet support only
 control           via group policy settings)

 Management        Partial (client agent setting)   Yes (client agent setting)   Yes (client agent setting)
 through
 ConfigMgr

Frequently asked questions

Does Configuration Manager support express installation files?

No, Configuration Manager no longer support Express Updates.

How much disk space is needed per quality update on the site server
and distribution points?
It depends. For each quality update, both the full-files of the update are stored on servers.
Windows quality updates are cumulative, so the size of these files increases each month. Plan
for a minimum of 5 GB per update per language. The size of UUP updates may be larger than
traditional non-UUP updates.

<!-- p.235 -->

Is there any way to see how much content is downloaded from peers
using Delivery Optimization?

Windows includes two PowerShell cmdlets, Get-DeliveryOptimizationPerfSnap and Get-
DeliveryOptimizationStatus. These cmdlets provide more insight into Delivery Optimization
and cache usage. For more information, see Delivery Optimization for Windows updates

How do clients communicate with Delivery Optimization over the
network?

For more information about the network ports, proxy requirements, and hostnames for
firewalls, see FAQs for Delivery Optimization.

Log files
Use the following log files to monitor delta downloads:

      WUAHandler.log
      DeltaDownload.log

Next steps
      Deploy software updates
      Automatically deploy software updates

 Last updated on 12/08/2025

<!-- p.236 -->

Manage Surface drivers with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager allows you to synchronize drivers for Surface devices and deploy
them like a software update. This functionality allows you to ensure that your Surface
devices are running the latest available drivers. This synchronization was first introduced
in version 1706 as a pre-release feature and it became a feature in 1710.

Prerequisites for synchronizing Surface drivers
      An internet connected top-level software update point.
      All software update points must run Windows Server 2016 with cumulative update
      KB4025339 or later installed.
      In version 2006 and earlier, Configuration Manager doesn't enable this optional
      feature by default. Enable this feature before using it. For more information, see
      Enable optional features from updates.

Enable sync for Surface drivers
To enable synchronization of Surface drivers, do following steps:

   1. Connect the Configuration Manger console to the top-level site server.

   2. Go to Administration > Site Configuration > Sites, then click on your top-level
      site.

   3. In the ribbon, select Settings > Configure Site Components > Software Update
      Point.

   4. Click on the Classifications tab, then click the checkbox for Include Microsoft
      Surface drivers and firmware updates and click Apply.

<!-- p.237 -->

5. In the Software Update Point Component Properties, click the Products tab. For
  more information, see the Products for Surface drivers and Surface Models
  sections.

6. Select the products for each version of Windows 10 for which you would like to
  support Surface drivers. You'll notice that there are two different versions of each
  of the products for drivers:

       Windows 10 version Update and later Servicing Drivers

       Windows 10 version Update and later Upgrade & Servicing Drivers.

<!-- p.238 -->

  7. When you have finished selecting the products, click OK.

  8. Synchronize your software update point to bring the Surface drivers into
     Configuration Manager.

  9. Once the Surface drivers are synchronized, deploy them in the same manner as
     you deploy other updates.

Products for Surface drivers
Most drivers belong to the following product groups:

     Windows 10 and later version drivers
     Windows 10 and later Upgrade & Servicing Drivers
     Windows 10 Anniversary Update and Later Servicing Drivers
     Windows 10 Anniversary Update and Later Upgrade & Servicing Drivers
     Windows 10 Creators Update and Later Servicing Drivers
     Windows 10 Creators Update and Later Upgrade & Servicing Drivers
     Windows 10 Fall Creators Update and Later Servicing Drivers

<!-- p.239 -->

     Windows 10 Fall Creators Update and Later Upgrade & Servicing Drivers
     Windows 10 S and Later Servicing Drivers
     Windows 10 S Version 1709 and Later Servicing Drivers for testing
     Windows 10 S Version 1709 and Later Upgrade & Servicing Drivers for testing
     Windows 10 S Version 1803 and Later Servicing Drivers
     Windows 10 S Version 1803 and Later Upgrade & Servicing Drivers
     Windows 10 S version 1809 and later, Servicing Drivers
     Windows 10 S version 1809 and later, Upgrade & Servicing Drivers
     Windows 10 S version 1903 and later, Servicing Drivers
     Windows 10 S version 1903 and later, Upgrade & Servicing Drivers
     Windows 10 Version 1803 and Later Servicing Drivers
     Windows 10 Version 1803 and Later Upgrade & Servicing Drivers
     Windows 10 version 1809 and later, Servicing Drivers
     Windows 10 Version 1809 and later, Upgrade & Servicing Drivers
     Windows 10 version 1903 and later, Servicing Drivers
     Windows 10 Version 1903 and later, Upgrade & Servicing Drivers

  ７ Note

  Most Surface drivers belong to multiple Windows 10 product groups. You may not
  have to select all the products that are listed here. To help reduce the number of
  products that populate your Update Catalog, we recommend that you select only
  the products that are required by your environment for synchronization.

Surface models
The following table contains the Surface models and versions of Windows 10 on which
Configuration Manager can install drivers. Surface driver updates aren't available in
Configuration Manager the same day they're published to the Microsoft Update catalog.
Configuration Manager maintains its own list of which Surface drivers it will import.
Devices needing Windows 10 S products are noted. Microsoft aims to get the Surface
drivers added to the allow list on the second Tuesday each month to make them
available for synchronization to Configuration Manager. For more information, see
Frequently asked questions.

                                                                         ﾉ   Expand table

<!-- p.240 -->

Surface   Windows     Windows     Windows     Windows     Windows     Windows     Windows
model     10 1709     10 1803     10 1809     10 1903     10 1909     10 2004     10 20H2

Surface   Yes         Yes         Yes         Yes         Yes         Yes         Yes
Pro 3

Surface   Yes         Yes         Yes         Yes         Yes         Yes         Yes
Pro 4

Surface   N/A         Yes         Yes         Yes         Yes         Yes         Yes
Pro 6

Surface   N/A         N/A         N/A         Yes         Yes         Yes         Yes
Pro 7

Surface   N/A         N/A         N/A         N/A         N/A         N/A         Yes
Pro 7+

Surface   N/A         N/A         N/A         Yes         Yes         Yes         Yes
Pro X

Surface   N/A         N/A         N/A         N/A         N/A         Yes         Yes
Pro X
with
SQ2
chip

Surface   Yes         Yes         Yes         Yes         Yes         Yes         Yes
Book

Surface   Yes         Yes         Yes         Yes         Yes         Yes         Yes
Book 2

Surface   N/A         N/A         N/A         Yes         Yes         Yes         Yes
Book 3

Surface   Yes, with   Yes, with   Yes, with   Yes, with   Yes, with   Yes, with   Yes, with
Laptop    the         the         the         the         the         the         the
          product     product     product     product     product     product     product
          "Windows    "Windows    "Windows    "Windows    "Windows    "Windows    "Windows
          10 S        10 S        10 S        10 S        10 S        10 S        10 S
          version     version     version     version     version     version     version
          1709 and    1803 and    1809 and    1903 and    1903 and    1903 and    1903 and
          later       later       later       later       later       later       later
          Servicing   Servicing   Upgrade     Upgrade     Upgrade     Upgrade     Upgrade
          drivers"    drivers"    &           &           &           &           &
          selected    selected    Servicing   Servicing   Servicing   Servicing   Servicing
                                  drivers"    drivers"    drivers"    drivers"    drivers"
                                  selected    selected    selected    selected    selected
