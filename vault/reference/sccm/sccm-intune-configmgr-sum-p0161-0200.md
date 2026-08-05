---
title: "Software update management documentation — pages 161-200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-sum-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-sum-p0161-0200
family: sccm
documentKind: "doc"
abstract: "you manually start the second phase. For more information, see Move to the next phase. ７ Note This option isn't available for phased deployments of applications. Gradually make this software available over this period of time (in days) Configure this setting for the rollout in e"
---

# Software update management documentation — pages 161-200

<!-- p.161 -->

     you manually start the second phase. For more information, see Move to the next
     phase.

        ７ Note

        This option isn't available for phased deployments of applications.

Gradually make this software available over this period of
time (in days)
Configure this setting for the rollout in each phase to happen gradually. This behavior
helps mitigate the risk of deployment issues, and decreases the load on the network
that is caused by the distribution of content to clients. The site gradually makes the
software available depending on the configuration for each phase. Every client in a
phase has a deadline relative to the time the software is made available. The time
window between the available time and deadline is the same for all clients in a phase.
The default value of this setting is zero, so by default the deployment isn't throttled.
Don't set the value higher than 30.

<!-- p.162 -->

Configure the deadline behavior relative to when the
software is made available
   Installation is required as soon as possible: Set the deadline for installation on the
   device as soon as the device is targeted.

   Installation is required after this period of time: Set a deadline for installation a
   certain number of days after device is targeted. By default, this value is seven days.

Automatically create a default two-phase
deployment
 1. Start the Create Phased Deployment wizard in the Configuration Manager console.
   This action varies based on the type of software you're deploying:

        Application: Go to the Software Library, expand Application Management,
        and select Applications. Select an existing application, and then choose
        Create Phased Deployment in the ribbon.

        Software update: Go to the Software Library, expand Software Updates, and
        select All Software Updates. Select one or more updates, and then choose
        Create Phased Deployment in the ribbon.

        This action is available for software updates from the following nodes:
           Software Updates
              All Software Updates
              Software Update Groups
           Windows Servicing, All Windows Updates
           Office 365 Client Management, Office 365 Updates

        Task sequence: Go to the Software Library workspace, expand Operating
        Systems, and select Task Sequences. Select an existing task sequence, and
        then choose Create Phased Deployment in the ribbon.

 2. On the General page, give the phased deployment a Name, Description (optional),
   and select Automatically create a default two phase deployment.

 3. Select Browse and choose a target collection for both the First Collection and
   Second Collection fields. For a task sequence and software updates, select from
   device collections. For an application, select from user or device collections. Select
   Next.

<!-- p.163 -->

          ） Important

          The Create Phased Deployment wizard doesn't notify you if a deployment is
          potentially high-risk. For more information, see Settings to manage high-risk
          deployments and the note when you Deploy a task sequence.

   4. On the Settings page, choose one option for each of the scheduling settings. For
     more information, see Phase settings. Select Next when complete.

   5. On the Phases page, see the two phases that the wizard creates for the specified
     collections. Select Next. These instructions cover the procedure to automatically
     create a default two-phase deployment. The wizard lets you add, remove, reorder,
     edit, or view phases for a phased deployment. For more information on these
     additional actions, see Create a phased deployment with manually configured
     phases.

   6. Confirm your selections on the Summary tab, and then select Next to complete
     the wizard.

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365
  Apps for enterprise. For more information, see Name change for Office 365
  ProPlus. You may still see the old name in the Configuration Manager product and
  documentation while the console is being updated.

Optionally, use the following Windows PowerShell cmdlets for this task:

     New-CMApplicationAutoPhasedDeployment
     New-CMSoftwareUpdateAutoPhasedDeployment
     New-CMTaskSequenceAutoPhasedDeployment

Create a phased deployment with manually
configured phases
Create a phased deployment with manually configured phases for a task sequence. Add
up to 10 additional phases from the Phases tab of the Create Phased Deployment
wizard.

  ７ Note

<!-- p.164 -->

You can't currently manually create phases for an application. The wizard
automatically creates two phases for application deployments.

1. Start the Create Phased Deployment wizard for either a task sequence or software
  updates.

2. On the General page of the Create Phased Deployment wizard, give the phased
  deployment a Name, Description (optional), and select Manually configure all
  phases.

3. From the Phases page of the Create Phased Deployment wizard, the following
  actions are available:

        Filter the list of deployment phases. Enter a string of characters for a case-
        insensitive match of the Order, Name, or Collection columns.

        Add a new phase:

        a. On the General page of the Add Phase Wizard, specify a Name for the
            phase, and then browse to the target Phase Collection. The additional
            settings on this page are the same as when normally deploying a task
            sequence or software updates.

        b. On the Phase Settings page of the Add Phase Wizard, configure the
            scheduling settings, and select Next when complete. For more
            information, see Settings.

              ７ Note

              You can't edit the phase settings, Deployment success percentage or
              Number of devices successfully deployed, on the first phase. These
              settings only apply to phases that have a previous phase.

         c. The settings on the User Experience and Distribution Points pages of the
            Add Phase Wizard are the same as when normally deploying a task
            sequence or software updates.

        d. Review the settings on the Summary page, and then complete the Add
            Phase Wizard.

        Edit: This action opens the selected phase's Properties window, which has
        tabs the same as the pages of the Add Phase Wizard.

<!-- p.165 -->

          Remove: This action deletes the selected phase.

             ２ Warning

             There is no confirmation, and no way to undo this action.

          Move Up or Move Down: The wizard orders the phases by how you add
          them. The most recently added phase is last in the list. To change the order,
          select a phase, and then use these buttons to move the phase's location in
          the list.

             ） Important

             Review the phase settings after changing the order. Make sure the
             following settings are still consistent with your requirements for this
             phased deployment:
                Criteria for success of the previous phase
                Conditions for beginning this phase of deployment after success of
                the previous phase

   4. Select Next. Review the settings on the Summary page, and then complete the
     Create Phased Deployment wizard.

Optionally, use the following Windows PowerShell cmdlets for this task:

     New-CMSoftwareUpdateManualPhasedDeployment
     New-CMTaskSequenceManualPhasedDeployment

After you create a phased deployment, open its properties to make changes:

     Add additional phases to an existing phased deployment.

     If a phase isn't active, you can Edit, Remove, or Move it up or down. You can't
     move it before an active phase.

     When a phase is active, it's read-only. You can't edit it, remove it, or move its
     location in the list. The only option is to View the properties of the phase.

     An application phased deployment is always read-only.

Next steps

<!-- p.166 -->

Manage and monitor phased deployments:

     Application
     Software update
     Task sequence

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.167 -->

About orchestration groups in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Create an orchestration group to better control the deployment of software updates to
devices. Many server administrators need to carefully manage updates for specific
workloads, and automate behaviors in between.

                                                                                      

An orchestration group gives you the flexibility to update devices based on a
percentage, a specific number, or an explicit order. You can also run a PowerShell script
before and after the devices run the update deployment.

Members of an orchestration group can be any Configuration Manager client, not just
servers. The orchestration group rules apply to the devices for all software update
deployments to any collection that contains an orchestration group member. Other
deployment behaviors still apply. For example, maintenance windows and deployment
schedules.

  ７ Note

<!-- p.168 -->

 Starting in Configuration Manager version 2111, Orchestration groups is no longer
 a pre-release feature. For more information, see Pre-release features.

 The Orchestration Groups feature is the evolution of the Server Groups feature. An
 orchestration group is an object in Configuration Manager.

Orchestration group usage example
    As the software updates administrator, you manage all updates for your
    organization.
    You have one large collection for all servers and one large collection for all clients.
    You deploy all updates to these collections.
    The SQL Server administrators want to control all the software installed on the SQL
    Servers. They want to patch five servers in a specific order. Their current process is
    to manually stop specific services before installing updates, and then restart the
    services afterwards.
    You create an orchestration group and add all five SQL Servers. You also add pre-
    and post-scripts, using the PowerShell scripts provided by the SQL Server
    administrators.
    During the next update cycle, you create and deploy the software updates as
    normal to the large collection of servers. The SQL Server administrators run the
    deployment, and the orchestration group automates the order and services.

Prerequisites

Site server and permission prerequisites
    To see all of the orchestration groups and updates for those groups, your account
    needs to be a Full Administrator.
       Role-based administration for orchestration groups currently isn't available.
    Enable the Orchestration Groups feature. For more information, see Enable
    optional features.
       When you enable Orchestration Groups, the site disables the Server Groups
       feature. This behavior avoids any conflicts between the two features.

Client prerequisites
    Upgrade the target devices to the latest version of the Configuration Manager
    client.

<!-- p.169 -->

     Members of an orchestration group should be assigned to the same site.
     Devices can't be in more than one orchestration group.
        Devices already in an orchestration group won't be available to select when
        adding new members.

Permissions for approving scripts
(Introduced in version 2111)

Approving scripts for orchestration groups requires one of the following security roles:

     Full Administrator
     Operations Administrator

Limitations
     You can have up to 1000 orchestration group members.
     Orchestration groups don't work in interoperability mode. For more information,
     see Interoperability between different versions of Configuration Manager.
     If updates are initiated by users from Software Center, orchestration will be
     bypassed.
     Starting in Configuration Manager version 2103, updates in the Definition
     classification don't require orchestration and will always bypass orchestration
     group rules.
     Scripts that have parameters aren't supported

Server groups are automatically updated to
orchestration groups
The Orchestration Groups feature is the evolution of the Server Groups feature. When
you install Configuration Manager version 2002 or later and you have Server Groups
enabled, your server groups are automatically moved to orchestration groups.

Next steps
     Create orchestration groups
     Monitor orchestration groups

<!-- p.170 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.171 -->

Create and use orchestration groups in
Configuration Manager
Article • 03/28/2023

Applies to: Configuration Manager (current branch)

An orchestration group gives you the flexibility to update devices based on a
percentage, a specific number, or an explicit order. You can also run a PowerShell script
before and after the devices run the update deployment.

Members of an orchestration group can be any Configuration Manager client, not just
servers. The orchestration group rules apply to the devices for all software update
deployments to any collection that contains an orchestration group member. Other
deployment behaviors still apply. For example, maintenance windows and deployment
schedules.

                                                                                         

Create an orchestration group
   1. Verify the prerequisites, permissions, and limitations for orchestration groups.

   2. In the Configuration Manager console, go to the Assets and Compliance
      workspace, and select the Orchestration Group node.

<!-- p.172 -->

3. In the ribbon, select Create Orchestration Group to open the Create Orchestration
  Group Wizard.

4. On the General page, give your orchestration group a Name and optionally a
  Description. Specify your values for the following items:

       Orchestration Group timeout (in minutes): Time limit for all group members
       to complete update installation.
       Orchestration Group member timeout (in minutes): Time limit for a single
       device in the group to complete the update installation.

5. On the Member Selection page, first specify the Site code. Then select Add to add
  device resources as members of this orchestration group. Search for devices by
  name, and then Add them. You can also filter your search to a single collection by
  using Search in Collection. Select OK when you finish adding devices to the
  selected resources list.

       When selecting resources for the group, only valid clients are shown. Checks
       are made for verifying the site code, that the client is installed, and that
       resources aren't duplicated.

6. On the Rule Selection page, select one of the following options:

       Allow a percentage of the machines to be updated at the same time, then
       select or enter a number for this percentage. Use this setting to allow for
       future flexibility of the size of the orchestration group. For example, your
       orchestration group contains 50 devices, and you set this value to 10. During
       a software update deployment, Configuration Manager allows five devices to
       simultaneously run the deployment. If you later increase the size of the
       orchestration group to 100 devices, then 10 devices update at once.

       Allow a number of the machines to be updated at the same time, then
       select or enter a number for this specific count. Use this setting to always
       limit to a specific number of devices, whatever the overall size of the
       orchestration group.

       Specify the maintenance sequence, then sort the selected resources in the
       proper order. Use this setting to explicitly define the order in which devices
       run the software update deployment.

7. Choose a Pre-installation script and Post-installation script for your orchestration
  group, if needed, on the Script Picker page.

<!-- p.173 -->

       Pre-Script: A PowerShell script to run on each device before the deployment
       runs.
       Post-Script page, enter a PowerShell script to run on each device after the
       deployment runs and a restart, if required, occurs. The behavior is otherwise
       the same as the PreScript.

  The scripts should return a value of 0 for success. Any non-zero value is
  considered a script failure. Scripts with parameters can't be used and the maximum
  script length is 50,000 bytes which is 25,000 characters (as we use Unicode
  encoding). Choose from the following options when adding or modifying a script
  on the Script Picker page:

       Add: Allows you to choose a script to add. Type or paste a PowerShell script
       into the pane or use one fo the following options:
          Open: Open a specific .ps1 file
          Browse: Choose a script that's already approved from the Scripts list.
          Scripts with parameters will be hidden from the list.
          Clear: Clears the current script in the script pane
       Edit: Edit the currently selected script
       Delete: Removes the current script
       Script timeout (in seconds): The allowed time in seconds for the script to run
       before it times out

8. Complete the wizard.

２ Warning

    Starting in version 2111, pre and post-scripts require approval to take effect.
    Editing a script after it's approved will reset the approval state to Waiting for
    approval. Scripts that don't have approval will not run on clients.
    In version 2103 and later, scripts that have parameters aren't supported and
    the maximum script length is 50,000 bytes which is 25,000 characters (as we
    use Unicode encoding).
    For Configuration Manager 2010 and earlier, add scripts to your orchestration
    groups on the Pre-Script and Post-Script pages.
       Ensure pre-scripts and post-scripts are tested before using them for
       orchestration groups. The pre-scripts and post-scripts don't timeout and
       will run until the orchestration group member timeout has been reached.

<!-- p.174 -->

           Scripts that have parameters aren't supported and the maximum script
           length is 5,000 characters.

Approvals for orchestration group scripts
(Introduced in version 2111)

Starting in version 2111, pre and post-scripts for orchestration groups require approval
to take effect. If you select a script from a file, author, or modify your own script,
approval for the script is required from another admin. When selecting an approved
script from the Scripts library, no additional approval is needed. By default, users can't
approve a script they've authored. These roles give an additional level of security against
running a script without oversight. For ease of testing, you're able to disable script
approval for the environment by changing the hierarchy setting.

To assist you with script approval, the following two tabs were added to the details pane
for Orchestration Groups in version 2111:

     Summary: Contains information about the selected orchestration group, including
     the Approval State of scripts.
     Scripts: Lists information about pre and post-scripts, including the timeout,
     approver, and approval state for each script.

Approval states for pre and post-scripts
The approval state for each of the scripts is displayed in the Scripts tab. Editing a script
after it's approved will reset the approval state. The Approval State for each script is
defined below:

     Approved: The script is approved. Approval is granted from either of the following
     ways:
        Selecting a script from the list of approved PowerShell scripts
        Manual approval of the script by selecting Approve from the ribbon or the
        right-click menu.
     Waiting for approval: The script is pending approval. Scripts that are written or
     edited directly in the code editor, or imported from a .ps1 file will start in this
     approval state.
     Declined: The script was denied during the approval process.

  ２ Warning

<!-- p.175 -->

  Editing a script after it's approved will reset the approval state to Waiting for
  approval. This also means that the previously approved version of the script will not
  run if you start orchestration on the group while that script is in the Waiting for
  approval state. Scripts that don't have approval will not run on clients.

   Tip

  One way to update a script without any interruption is to create a new script in the
  Scripts library and get approval. Then choose the approved script from the library
  when you edit an orchestration group's pre or post-script. The already approved
  new script will replace the existing script immediately.

Permissions for approving scripts
Approving scripts for orchestration groups requires one of the following security roles:

     Full Administrator
     Operations Administrator

Approve or deny a script for an orchestration group
   1. From the Configuration Manager console, go to the Assets and Compliance
     workspace > Overview > Orchestration Groups.
   2. Select an orchestration group and then select the Scripts tab for the group.
   3. Select one of the scripts and choose Approve/Deny from either the ribbon or the
     right-click menu.
   4. Review the script from the Script Details page in the Approve or Deny Script
     wizard. Select Next when you're finished reviewing the script.
   5. On the Script Approval page in the wizard, select Approve or Deny. If needed,
     enter in a comment to be displayed in the Scripts detail pane.
   6. Complete the wizard to finish the approval process.

Edit or delete an orchestration group
To delete the orchestration group, select it then select Delete in the ribbon or from the
right-click menu. To edit an orchestration group, select it then select Properties in the
ribbon or from the right-click menu. Change the settings from the following tabs:

     General:
        Name: The name of your orchestration group

<!-- p.176 -->

  Description: Orchestration group description (optional)
  Orchestration Group timeout (in minutes): Time limit for all group members to
  complete update installation.
  Orchestration Group member timeout (in minutes): Time limit for a single
  device in the group to complete the update installation.

Member Selection:
  Site Code: Site code for the orchestration group.
  Members: Select Add to select more devices for the orchestration group.
  Choose Remove to remove the selected device.

Rules Selection:
  Allow a percentage of the machines to be updated at the same time, then
  select or enter a number for this percentage. Use this setting to allow for future
  flexibility of the size of the orchestration group. For example, your orchestration
  group contains 50 devices, and you set this value to 10. During a software
  update deployment, Configuration Manager allows five devices to
  simultaneously run the deployment. If you later increase the size of the
  orchestration group to 100 devices, then 10 devices update at once.
  Allow a number of the machines to be updated at the same time, then select
  or enter a number for this specific count. Use this setting to always limit to a
  specific number of devices, whatever the overall size of the orchestration group.
  Specify the maintenance sequence: Sort the selected resources to the proper
  order. Use this setting to explicitly define the order in which devices run the
  software update deployment.

Choose a Pre-installation script and Post-installation script for your orchestration
group as needed. The script should return a value of 0 for success. Any non-zero
value is considered a script failure. Scripts with parameters can't be used and the
maximum script length is 50,000 bytes which is 25,000 characters (as we use
Unicode encoding) .

  For Configuration Manager version 2103 and later, choose a Pre-installation
  script and Post-installation script on the Script Picker page. Choose from the
  following options when adding or modifying a script:
     Add: Allows you to choose a script to add. Type or paste a PowerShell script
     into the pane or use one fo the following options:
        Open: Open a specific .ps1 file
        Browse: Choose a script that's already approved from the Scripts list.
        Scripts with parameters will be hidden from the list.
        Clear: Clears the current script in the script pane
     Edit: Edit the currently selected script

<!-- p.177 -->

          Delete: Removes the current script
          Script timeout (in seconds): The allowed time in seconds for the script to run
          before it times out

       For Configuration Manager version 2010 and earlier, add scripts to your
       orchestration groups on the Pre-Script and Post-Script tabs.

  ２ Warning

       Starting in version 2111, pre and post-scripts require approval to take effect.
       Editing a script after it's approved will reset the approval state to Waiting for
       approval. Scripts that don't have approval will not run on clients.
       In version 2103 and later, scripts that have parameters aren't supported and
       the maximum script length is 50,000 bytes which is 25,000 characters (as we
       use Unicode encoding) .
       For Configuration Manager 2010 and earlier, add scripts to your orchestration
       groups on the Pre-Script and Post-Script tabs.
          Ensure pre-scripts and post-scripts are tested before using them for
          orchestration groups. The pre-scripts and post-scripts don't timeout and
          will run until the orchestration group member timeout has been reached.
          Scripts that have parameters aren't supported and the maximum script
          length is 5,000 characters.

Display orchestration groups and members
From the Assets and Compliance workspace, select the Orchestration Group node. To
view members, select an orchestration group and select Show Members in the ribbon.
For more information about the available columns for the nodes, see Monitor
orchestration groups and members.

Start orchestration
  1. Deploy software updates to a collection that contains the members of the
     orchestration group.

  2. Orchestration starts when any client in the group tries to install any software
     update at deadline or during a maintenance window. It starts for the entire group,
     and makes sure that the devices update by following the orchestration group rules.

<!-- p.178 -->

   3. You can manually start orchestration by selecting it from the Orchestration Group
     node, then choosing Start Orchestration from the ribbon or right-click menu.

   4. If needed, select Ignore all applicable windows for the members to start the
     installation immediately and bypass maintenance windows.

           This option was introduced in Configuration Manager version 2103

   5. If an orchestration group is in a Failed state:
      a. Determine why the orchestration failed and resolve any issues.
     b. Reset the orchestration state for group members.
      c. From the Orchestration Group node, choose the Start Orchestration button to
        restart orchestration.

   Tip

        Orchestration groups only apply to software update deployments. They don't
        apply to other deployments.
        You can right-click on an Orchestration Group member and select Reset
        Orchestration Group Member. This allows you to rerun orchestration.

Reset orchestration state for a group member
If you want to rerun orchestration on a group member, you can clear its state such as
Complete or Failed. To clear the state, right-click on the Orchestration Group member
and select Reset Orchestration Group Member. You can also select Reset Orchestration
Group Member from the ribbon. Before resetting the state, you should check the client
to see why it failed and correct any issues found.

Automate with Windows PowerShell
You can use the following PowerShell cmdlets to automate some of these tasks:

     Get-CMOrchestrationGroup: Use this cmdlet to get an orchestration group object
     by name or ID. You can use this object to start, remove, or configure the
     orchestration group.

     Invoke-CMOrchestrationGroup: Use this cmdlet to start orchestration.

     New-CMOrchestrationGroup: Use this cmdlet to create a new orchestration group.

<!-- p.179 -->

     Remove-CMOrchestrationGroup: Use this cmdlet to remove an orchestration
     group.

     Set-CMOrchestrationGroup: Use this cmdlet to configure an orchestration group.

Next steps
     Orchestration groups prerequisites
     Monitor orchestration groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.180 -->

Monitor orchestration groups in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you create, edit, or start an orchestration group, you may need to monitor the
group or its members. Using monitoring information along with the log files, can help
you troubleshoot orchestration groups and group members.

Monitor orchestration groups
From the Assets and Compliance workspace, select the Orchestration Group node. Add
any of the following columns to get information about the groups:

      Orchestration Name: The name of your orchestration group.

      Site Code: Site code for the group.

      Orchestration Type: is one of the following types:
         Number
         Percentage
         Sequence

      Orchestration Value: How many members or the percentage of members that can
      get a lock simultaneously. Orchestration Value is only populated when
      Orchestration Type is either Number or Percentage.

      Orchestration State: In progress during orchestration. Idle when not in progress.

      Orchestration Start Time: Date and time that the orchestration started.

      Current Sequence Number: Indicates for which member of the group
      orchestration is active. This number corresponds with the Sequence Number for
      the member.

      Orchestration Timeout (in minutes): Value of The Orchestration Group timeout
      (in minutes) set on the General page when creating the group, or the General tab
      when editing the group.

      Orchestration Group Member Timeout (in minutes): Value of Orchestration
      Group member timeout (in minutes) set on the General page when creating the

<!-- p.181 -->

     group, or the General tab when editing the group.

     Orchestration Group ID: ID of the group, The ID is used in logs and the database.

     Orchestration Group Unique ID: Unique ID of the group, The Unique ID is used in
     logs and the database.

     Last Modified Time: The time the orchestration group was last modified (starting
     in version 2203).

     Last Modified By: The user that last modified the orchestration group (starting in
     version 2203).

Orchestration groups details tabs
(Introduced in version 2107)

Starting in Configuration Manager version 2107, the following two tabs were added to
the details pane for Orchestration Groups to assist you with monitoring the script
approval:

     Summary: Contains information about the selected orchestration group, including
     the Approval State of scripts.
     Scripts: Lists information about pre and post-scripts, including the timeout,
     approver, and approval state for each script.

Monitor orchestration group members
In the Orchestration Group node, select an orchestration group. In the ribbon, select
Show Members. You can see the members of the group, and their orchestration status.
Add any of the following columns to get information about the members:

     Name: Device name of the orchestration group member
     Current State: Gives you the state of the member device.
        In progress during orchestration.
        Waiting: Indicates the client is waiting on the lock for its turn to install updates.
        Idle when orchestration is complete or not running.
     State Code: You can right-click on the Orchestration Group member and select
     Reset Orchestration Group Member. This reset allows you to rerun orchestration.
     States include:
        Idle
        Waiting, the device is waiting its turn

<!-- p.182 -->

          In progress, installing an update
          Failed
          Reboot pending
      Lock Acquired Time: Locks are requested by the client based on its policy. Once
      the client acquires a lock, orchestration is triggered on it.
      -Last State Reported Time: Time the member last reported a state.
      Sequence Number: The client's location in the queue for installing updates.
      Site Code: The site code for the member.
      Client Activity: Tells you if the client is active or inactive.
      Primary User(s): Which users are primary for the device.
      Client Type: What type of device the client is.
      Currently Logged on User: Which user is currently logged on to the device.
      OG ID: ID of the orchestration group the member belongs to.
      OG Unique ID: Unique ID of the orchestration group the member belongs to.
      Resource ID: Resource ID of the device.

Alerts for orchestration groups
(Introduced in version 2203)

Starting in version 2203, if an orchestration group fails, an alert is generated. In the
Configuration Manager console, go to the Monitoring workspace, expand Alerts, and
then select Active Alerts or All Alerts. For more information about alerts, see Configure
alerts.

Log files
Use the following log files on the site server to help monitor and troubleshoot:

Site server
      Policypv.log: shows that the site targets the orchestration group to the clients.
      SMS_OrchestrationGroup.log: shows the behaviors of the orchestration group.

Client
      MaintenanceCoordinator.log: Shows the lock acquisition, update installation, pre
      and post-scripts, and lock release process.
      UpdateDeployment.log: Shows the update installation process.
      PolicyAgent.log: Checks if the client is in an orchestration group.

<!-- p.183 -->

Next steps
     Orchestration groups prerequisites
     Create, edit, and use orchestration groups

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.184 -->

Office 365 Client Management
dashboard
Article • 04/05/2024

Applies to: Configuration Manager (current branch)

  ７ Note

  Starting on April 21, 2020, Office 365 ProPlus is being renamed to Microsoft 365
  Apps for enterprise. For more information, see Name change for Office 365
  ProPlus. You may still see references to the old name in the Configuration Manager
  console and supporting documentation while the console is being updated.

  ７ Note

  Starting on April 1, 2025, office 365 client management dashboard add-in support
  statement will be removed from dashboard

Beginning in Configuration Manager version 1802, you can review Microsoft 365 Apps
client information from the Office 365 Client Management dashboard. The Office 365
client management dashboard displays a list of relevant devices when graph sections
are selected.

Prerequisites

Enable hardware inventory
The data that is displayed in the Office 365 Client Management dashboard comes from
hardware inventory. Enable hardware inventory and select the Office 365
Configurations hardware inventory class for data to display in the dashboard.

   1. Enable hardware inventory, if it isn't yet enabled. For details, see Configure
      hardware inventory.
   2. In the Configuration Manager console, navigate to Administration > Client
      Settings > Default Client Settings.
   3. On the Home tab, in the Properties group, click Properties.
   4. In the Default Client Settings dialog box, click Hardware Inventory.
   5. In the Device Settings list, click Set Classes.

<!-- p.185 -->

   6. In the Hardware Inventory Classes dialog box, select Office 365 Configurations.
   7. Click OK to save your changes and close the Hardware Inventory Classes dialog
     box.

The Office 365 Client Management dashboard starts displaying data as hardware
inventory is reported.

Connectivity for the top-level site server
(Introduced in version 1906 as a prerequisite)

Your top-level site server needs access to the following endpoint to download the
Microsoft Apps 365 readiness file:

     Starting March 2, 2021:
      https://omex.cdn.office.net/mirrored/sccmreadiness/SOT_SCCM_AddinReadiness.CA
     B

         Location prior to March 2, 2021:
         https://contentstorage.osi.office.net/sccmreadinessppe/sot_sccm_addinreadin
         ess.cab

  ７ Note

         The location of this file is changing March 2, 2021 . For more information, see
         Download location change for Microsoft 365 Apps readiness file          .
         Internet connectivity isn't required for the client devices for any of these
         scenarios.

Enable data collection for Microsoft 365 Apps
(Introduced in version 1910 as a prerequisite)

Starting in version 1910, you'll need to enable data collection for Microsoft 365 Apps to
populate information in the Office 365 Pilot and Health Dashboard. The data is stored
in the Configuration Manager site database and not sent to Microsoft.

This data is different from the diagnostic data, which is described in Diagnostic data sent
from Microsoft 365 Apps to Microsoft.

You can enable data collection either by using Group Policy or by editing the registry.

<!-- p.186 -->

Enable data collection from Group Policy
   1. Download the latest Administrative Template files from the Microsoft Download
      Center   .
   2. Enable the Turn on telemetry data collection policy setting under User
      Configuration\Policies\Administrative Templates\Microsoft Office

      2016\Telemetry Dashboard .

            Alternatively, apply the policy setting with the Office cloud policy service.
            The policy setting is also used by the Office Telemetry Dashboard, which you
            don't need to deploy for this data collection.

Enable data collection from the registry

The command below is an example of how to enable the data collection from the
registry:

  Windows Command Prompt

  reg add HKCU\Software\Policies\Microsoft\office\16.0\OSM /v EnableLogging /t
  REG_DWORD /d 1

Viewing the Office 365 Client Management
dashboard
To view the Office 365 Client Management dashboard in the Configuration Manager
console, go to Software Library > Overview > Office 365 Client Management. At the
top of the dashboard, use the Collection drop-down setting to filter the dashboard data
by members of a specific collection. Beginning in Configuration Manager version 1802,
the dashboard displays a list of relevant devices when graph sections are selected.

The Office 365 Client Management dashboard provides charts for the following
information:

      Number of Microsoft 365 Apps clients
      Microsoft 365 Apps client versions
      Microsoft 365 Apps client languages
      Microsoft 365 Apps client channels For more information, see Overview of update
      channels for Microsoft 365 Apps.

<!-- p.187 -->

Integration for Microsoft 365 Apps readiness
Starting in Configuration Manager version 1902, you can use the dashboard to identify
devices with high confidence that are ready to upgrade to Microsoft 365 Apps. This
integration provides insights into potential compatibility issues with add-ins and macros
in your environment. Then use Configuration Manager to deploy Microsoft 365 Apps to
ready devices.

The Office 365 client management dashboard includes a tile, Office 365 Apps Upgrade
Readiness. This tile is a bar chart of devices in the following states:

     Not assessed
     Ready to upgrade
     Needs review

Select a state to drill-through to a device list. This readiness report shows more detail
about devices. It includes columns for the compatibility state of both add-ins and
macros.

Prerequisites for Microsoft 365 Apps readiness
integration
     Enable hardware inventory in client settings. For more information, see the
     Prerequisites section.

     The device needs connectivity to the Office content delivery network (CDN) to
     download an add-in readiness file. For more information, see Content delivery
     networks. If the device can't download this file, the add-ins state is Needs review.

          ７ Note

          No data is sent to Microsoft for this feature.

Detailed macro readiness
By default, the scanning agent looks at the most recently used (MRU) files list on each
device. It counts the files in this list that support macros. These files include the
following types:

     Macro-enabled Office file formats, such as Excel macro-enabled workbooks (.xlsm)
     or Word macro-enabled document (.docm)

<!-- p.188 -->

     Older Office formats that don't indicate whether there's macro content. For
     example, an Excel 97-2003 workbook (.xls).

Microsoft 365 Apps readiness dashboard
(Introduced in version 1906)

To help you determine which devices are ready to upgrade to Microsoft 365 Apps,
there's a readiness dashboard starting in version 1906. It includes the Office 365 Apps
Upgrade Readiness tile that released in Configuration Manager current branch version
1902. The following new tiles on this dashboard help you evaluate add-in and macro
readiness:

     Deployment
     Device readiness
     Add-in readiness
     Add-in support statements
     Top add-ins by count of version
     Number of devices that have macros
     Macro readiness
     Macro advisories

The following video is a session from Ignite 2019, which includes more information:
https://medius.studios.ms/Embed/Video-nc/IG19-BRK3090

Best practices for compatibility assessment and Microsoft Office 365 upgrades using
Office Readiness in Configuration Manager

Using the Microsoft 365 Apps upgrade readiness
dashboard
After verifying you have the prerequisites, use the following instructions to use the
dashboard:

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Office 365 Client Management.
   2. Select the Microsoft 365 Apps Upgrade Readiness node.
   3. Change the Collection and Target Office Architecture to change the information
     relayed in the dashboard.

<!-- p.189 -->







<!-- p.190 -->

Device Readiness information
Once the add-in and macro inventory on each device is evaluated, the devices are then
grouped according to the information. Devices whose status are listed as Ready to
upgrade aren't likely to have any compatibility issues.

Selecting the Ready to upgrade category on the graph shows more details about the
devices in the limiting collection. You can review the device list, make selections
according to your business requirements, and create a new device collection from your
selection. Use your new collection to deploy Microsoft 365 Apps with Configuration
Manager.

Devices that might be at risk for compatibility issues are marked as Needs review. These
devices may need action to be taken before upgrading them to Microsoft 365 Apps. For
example, you might update critical add-ins to a more recent version.

Add-in information

  ７ Note

  Starting on April 1, 2025, office 365 client management dashboard add-in support
  statement will be removed from dashboard

On each device, an inventory of all installed add-ins is collected. The inventory is then
compared with the information Microsoft has about the add-in performance on
Microsoft 365 Apps. If an add-in is found which is likely to cause issues after upgrading,
then all devices with the add-in are flagged for review.

Macro information
Configuration Manager looks at the most recently used files on each device. It counts
the files in this list that support macros, including the following types:

     Macro-enabled Office file formats.
     Older Office formats, which don't indicate if there's macro content.

This report can be used to identify which devices have recently used files that may
contain macros.

Office 365 Pilot and Health dashboard

<!-- p.191 -->

(Introduced in version 1910)

Starting in version 1910, the Office 365 Pilot and Health Dashboard helps you plan,
pilot, and perform your Microsoft 365 Apps deployment. The dashboard provides health
insights for devices with Microsoft 365 Apps to help identify possible issues that may
affect your deployment plans. The Office 365 Pilot and Health Dashboard provides a
recommendation for pilot devices based on add-in inventory. The following tiles are in
the dashboard:

     Generate pilot
     Recommended pilot devices
     Deploy pilot
     Devices sending health data
     Devices not meeting health goals
     Add-ins not meeting health goals
     Macros not meeting health goals

Using the Office 365 Pilot and Health dashboard
After verifying you have the prerequisites, use the following instructions to use the
dashboard:

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Office 365 Client Management.
   2. Select the Office 365 Pilot and Health node.

<!-- p.192 -->

Generate pilot
Generate a pilot recommendation from a limiting collection at the click of a button. As
soon as the action is launched, a background task starts calculating your pilot collection.
Your limiting collection must contain at least one device with an Office version that isn't
Office 365 Apps.

  ７ Note

  The All Desktop and Server Clients (Office Pilot) collection is managed by
  Configuration Manager. Manual changes aren't supported. If you delete or edit this
  collection, the pilot deployment won't work.

Recommended pilot devices
Recommended pilot devices are a minimal set of devices representing all installed add-
ins across the limiting collection you used when generating the pilot. Drill down to get a
list of these devices. Then use the details to exclude any devices from the pilot if
needed. If all of your add-ins are already on Microsoft 365 Apps devices, then devices
with those add-ins won't be included in the calculation. This also means it's possible that
you won't get any results in your pilot collection since all of your add-ins have been
seen on devices where Microsoft 365 Apps is installed.

Deploy pilot
Once you accept your pilot devices, deploy Microsoft 365 Apps to the pilot collection
using the phased deployment wizard. Admins can define the pilot and limiting collection
in the wizard to manage deployments.

Health data
Once Microsoft 365 Apps is installed, enable health data on your pilot devices. The
health data gives you insight into which add-ins and macros don't meet health goals.
The Devices ready to deploy chart identifies non-pilot devices that are ready for
deployment by using the health insights. Get a count of devices that are sending health
data from the Devices sending health data chart.

Devices not meeting health goals
This tile summarizes devices that have issues with add-ins, macros, or both.

<!-- p.193 -->

Add-ins not meeting health goals
     Load failures: The add-in failed to start.
     Crashes: The add-in failed while it was running.
     Error: The add-in reported an error.
     Multiple issues: The add-in has more than one of the above issues.

Macros not meeting health goals
     Load failures: The document failed to load.
     Runtime errors: An error happened while the macro was running. These errors can
     be dependent on the inputs so may not always occur.
     Compile errors: The macro didn't compile correctly so it won't attempt to run.
     Multiple issues: The macro has more than one of the above issues.

Known issues
There is a known issue with the Deploy Pilot tile. At this time it can't be used to deploy
to a pilot. The workaround is the existing workflow for deploying an application using
the Phased Deployment Wizard.

Next steps
Manage Microsoft 365 Apps updates with Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.194 -->

Manage Microsoft 365 Apps with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

  ７ Note

  On April 21, 2020, Office 365 ProPlus was renamed to Microsoft 365 Apps for
  enterprise. For more information, see Name change for Office 365 ProPlus. You
  may still see references to the old name in the Configuration Manager console and
  supporting documentation while the console is being updated.

Configuration Manager lets you manage Microsoft 365 Apps in the following ways:

      Deploy Microsoft 365 Apps: You can start the Microsoft 365 Apps Installer from the
      Office 365 Client Management dashboard to make the initial Microsoft 365 Apps
      installation experience easier. The wizard lets you configure Microsoft 365 Apps
      installation settings, download files from Office Content Delivery Networks (CDNs),
      and create and deploy a script application with the content.

      Deploy Microsoft 365 Apps updates: You can manage Microsoft 365 Apps client
      updates by using the software update management workflow. When Microsoft
      publishes a new Microsoft 365 Apps update to the Office Content Delivery
      Network (CDN), Microsoft also publishes an update package to Windows Server
      Update Services (WSUS). After Configuration Manager synchronizes the Microsoft
      365 Apps updates from the WSUS catalog to the site server, the update is available
      to deploy to clients.
         Starting in Configuration Manager version 2002, you can import Microsoft 365
         Apps updates into disconnected environments. For more information, see
         Synchronize Microsoft 365 Apps updates from a disconnected software update
         point.

      Add languages for Microsoft 365 Apps update downloads: You can add support for
      Configuration Manager to download updates for any languages supported by
      Microsoft 365 Apps. Meaning Configuration Manager doesn't have to support the
      language as long as Microsoft 365 Apps does.

      Change the update channel: You can use group policy to distribute a registry key
      value change to Microsoft 365 Apps clients to change the update channel.

<!-- p.195 -->

To review Microsoft 365 Apps client information and start some of these Microsoft 365
Apps management actions, use the Office 365 Client Management dashboard.

Deploy Microsoft 365 Apps
Start the Microsoft 365 Apps Installer from the Office 365 Client Management
dashboard for the initial Microsoft 365 Apps installation. The wizard lets you configure
Microsoft 365 Apps installation settings, download files from the Office Content Delivery
Networks (CDNs), and create and deploy a script application for the files. Until Microsoft
365 Apps is installed on clients and the Microsoft 365 Apps automatic updates task runs,
Microsoft 365 Apps updates aren't applicable. For testing purposes, you can run the
update task manually.

For previous Configuration Manager versions, you must take the following steps to
install Microsoft 365 Apps for the first time on clients:

     Download Office Deployment Tool (ODT)
     Download the Microsoft 365 Apps installation source files, including all of the
     language packs that you need.
     Generate the Configuration.xml that specifies the correct Microsoft 365 Apps
     version and channel.
     Create and deploy either a legacy package or a script application for clients to
     install Microsoft 365 Apps.

Requirements
     The computer that runs the installer must have Internet access.
     The user that runs the installer must have Read and Write access to the content
     location share provided in the wizard.
     If you receive a 404 download error, copy the following files to the user %temp%
     folder:
        releasehistory.xml
        o365client_32bit.xml

Limitations
     Content-enabled cloud management gateways don't support content for
     Microsoft 365 Apps updates.
     In certain circumstances when using Office Customization Tool for Click-to-Run,
     you may encounter the following exception: Could not load type
     'System.Runtime.InteropServices.Architecture' from assembly 'mscorlib

<!-- p.196 -->

     Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089' . To work

     around the issue, update .NET Framework to version 4.7.1 or later for the machine
     running the Configuration Manager console.

Deploy Microsoft 365 Apps using Configuration Manager
The Office Customization Tool is integrated with the installer in the Configuration
Manager console. When creating a deployment for Microsoft 365 Apps, you can
dynamically configure the latest manageability settings.

   1. In the Configuration Manager console, navigate to Software Library > Overview >
     Office 365 Client Management.
   2. Select Office 365 Installer in the upper-right pane. The installation wizard opens.
   3. On the Application Settings page, provide a name and description for the app,
     enter the download location for the files, and then choose Next. The location must
     be specified as \\server\share.
   4. On the Office Settings page, select Go to the Office Customization Tool. This will
     open the Office Customization Tool for Click-to-Run     .
   5. Configure the desired settings for your Microsoft 365 Apps installation. Select
     Submit in the upper right of the page when you complete the configuration.
   6. On the Deployment page, determine if you would like to deploy now or at a later
     time. If you choose to deploy later, you can find the application in Software
     Library > Application Management > Applications.
   7. Confirm the settings on the Summary page.
   8. Select Next then Close once the wizard completes.

After you create and deploy Microsoft 365 Apps using the installer, Configuration
Manager may not manage the Microsoft 365 Apps updates by default. To enable
Microsoft 365 Apps clients to receive updates from Configuration Manager, see Deploy
Microsoft 365 Apps updates with Configuration Manager.

After you deploy Microsoft 365 Apps, you can create automatic deployment rules to
maintain the apps. To create an automatic deployment rule for Microsoft 365 Apps,
select Create an ADR from the Office 365 Client Management dashboard. Select Office
365 Client when you choose the product. For more information, see Automatically
deploy software updates.

Drill through required Microsoft 365 Apps
updates
(Introduced in version 1906)

<!-- p.197 -->

You can drill through compliance statistics to see which devices require a specific
Microsoft 365 Apps software update. To view the device list, you need permission to
view updates and the collections the devices belong to. To drill down into the device list:

   1. Go to Software Library > Office 365 Client Management > Office 365 Updates.
   2. Select any update that is required by at least one device.
   3. Look at the Summary tab and find the pie chart under Statistics.
   4. Select the View Required hyperlink next to the pie chart to drill down into the
     device list.
   5. This action takes you to a temporary node under Devices where you can see the
     devices requiring the update. You can also take actions for the node such as
     creating a new collection from the list.

Deploy Microsoft 365 Apps updates
Use the following steps to deploy Microsoft 365 Apps updates with Configuration
Manager:

   1. Verify the requirements for using Configuration Manager to manage Microsoft 365
     Apps client updates in the Requirements for using Configuration Manager to
     manage Microsoft 365 Apps client updates section of the article.

   2. Configure software update points to synchronize the Microsoft 365 Apps client
     updates. Set Updates for the classification and select Microsoft 365 Apps/Office
     2019/Office LTSC for the product. Synchronize software updates after you
     configure the software update points to use the Updates classification.

   3. Enable Microsoft 365 Apps clients to receive updates from Configuration Manager.
     Use Configuration Manager client settings or group policy to enable the client.

     Method 1: You can use the Configuration Manager client setting to manage the
     Microsoft 365 Apps client agent. After you configure this setting and deploy
     Microsoft 365 Apps updates, the Configuration Manager client agent
     communicates with the Microsoft 365 Apps client agent to download the updates
     from a distribution point and install them. Configuration Manager takes inventory
     of Microsoft 365 Apps client settings.

      a. In the Configuration Manager console, select Administration > Overview >
        Client Settings.

     b. Open the appropriate device settings to enable the client agent. For more
        information about default and custom client settings, see How to configure
        client settings.

<!-- p.198 -->

      c. Select Software Updates and choose Yes for the Enable management of the
        Office 365 Client Agent setting.

     Method 2: Enable Microsoft 365 Apps clients to receive updates from
     Configuration Manager by using the Office Deployment Tool or Group Policy.

   4. Deploy the Microsoft 365 Apps updates to clients.

If Microsoft 365 Apps was installed recently, and depending on how it was installed, it is
possible that the update channel has not been set yet. In that case, deployed updates
will be detected as not applicable. There is a scheduled Automatic Updates task created
when Microsoft 365 Apps installs. In this situation, this task needs to run at least once in
order for the update channel to be set and updates detected as applicable.

If Microsoft 365 Apps was installed recently and deployed updates are not detected, for
testing purposes, you can start the Office Automatic Updates task manually and then
start the Software Updates Deployment Evaluation Cycle on the client. For instructions
on how to do this in a task sequence, see Updating Microsoft 365 Apps in a task
sequence.

Restart behavior and client notifications for
Microsoft 365 Apps updates
The client receives pop-up and in-app notifications, and a countdown dialog, prior to
installing the update. If any Microsoft 365 Apps are running during a client update
enforcement, the Microsoft 365 Apps will not be forced to close. Instead, the update
install will return as requiring a system restart. For more information about notifications
from Microsoft 365 Apps, see End-user update notifications for Microsoft 365 Apps.

  ７ Note

  Starting in version 2111, you can configure the end-user notification experience for
  Microsoft 365 Apps updates. The Enable update notifications from Microsoft 365
  Apps option was added to the Software Updates group of client settings. For more
  information about this setting and the user notification experience, see About
  client settings in Configuration Manager.

Add languages for Microsoft 365 Apps update
downloads

<!-- p.199 -->

You can add support for Configuration Manager to download updates for any languages
that are supported by Microsoft 365 Apps.

Download updates for additional languages in version
1902, or later
Starting in Configuration Manager version 1902, the update workflow separates the 38
languages for Windows Update from the numerous additional languages for Office 365
Client Update.

To select the necessary languages, use the Language Selection page in the following
locations:

     Create Automatic Deployment Rule Wizard
     Deploy Software Updates Wizard
     Download Software Updates Wizard
     Automatic Deployment Rule Properties

In the Language Selection page, select Office 365 Client Update, then select Edit. Add
the needed languages for Microsoft 365 Apps, then choose OK.

<!-- p.200 -->

To add support to download updates for additional
languages in version 1902 and later
When new languages are added to Microsoft 365 Apps they don't appear in the content
download languages, you can add them if needed. Use the following procedure on the
software update point at the central administration site or stand-alone primary site:

   1. From a command prompt, type wbemtest as an administrative user to open the
     Windows Management Instrumentation Tester.

   2. Select Connect, and then type root\sms\site_<siteCode>.

   3. Choose Query, and then run the following query: select * from SMS_SCI_Component
     where componentname ="SMS_WSUS_CONFIGURATION_MANAGER"

   4. In the results pane, double-click the object with the site code for the central
     administration site or stand-alone primary site.
