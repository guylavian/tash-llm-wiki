---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 161-200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0161-0200
family: sccm
documentKind: "doc"
abstract: "with the task sequence step types in each category. For more information about each of the task sequence step types listed in Table 55, see the corresponding section in the MDT document Toolkit Reference. Table 55. Task Sequence Step Categories and Types ﾉ Expand table Category"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 161-200

<!-- p.161 -->

with the task sequence step types in each category. For more information about
each of the task sequence step types listed in Table 55, see the corresponding
section in the MDT document Toolkit Reference.

Table 55. Task Sequence Step Categories and Types

                                                                  ﾉ   Expand table

 Category         Task sequence step types in this category

 General          - Run Command Line

                  - Run PowerShell Script

                  - Set Task Sequence Variable

                  - Restart computer

                  - Gather

                  - Install Updates Offline

                  - Validate

                  - Install Application

                  - Inject drivers

                  - Execute Orchestrator Runbook

 Disks            - Format and Partition Disk

                  - Enable BitLocker

                  - Create Virtual Hard Disk (VHD)

 Images           - Install Operating System

 Settings         - Apply Network Settings

                  - Capture Network Settings

                  - Recover From Domain

 Roles            - Install Roles and Features

                  - Uninstall Roles and Features

<!-- p.162 -->

     Category          Task sequence step types in this category

                       - Configure DHCP

                       - Configure DNS

                       - Configure ADDS

                       - Authorize DHCP

    Remove. Select to remove the currently highlighted task sequence step or group.

      ） Important

      If you remove a task sequence group, you also remove all the task sequence
      steps in that group.

    Up. Select to configure a task sequence step to be processed earlier in the
    deployment process. The move is reflected in the task sequence hierarchy.

      ７ Note

      If you move the first task sequence step in a task sequence group up, the task
      sequence step will be performed before the entire group and will be removed
      from the group. If another task sequence group immediately precedes the
      group, the task sequence step will become the last step in the preceding
      group.

    Down. Select to configure a task sequence step to be processed earlier in the
    deployment process.

      ７ Note

      If you move the last task sequence step in a task sequence group down, the
      task sequence step will be performed after the entire group and will be
      removed from the group. If another task sequence group immediately follows
      the group, the task sequence step will become the first step in the following
      group.

To modify existing task sequence steps and step sequence

<!-- p.163 -->

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share in which you will configure
     the task sequence).

   3. In the details pane, select task_sequence_name (where task_sequence_name is the
     name of the task sequence you want to configure).

   4. In the Actions pane, select Properties.

     The task_sequence_name Properties dialog box opens (where task_sequence_name
     is the name of the task sequence you want to configure).

   5. On the Task Sequence tab, in the task sequence hierarchy, configure the task
     sequence steps and step sequences based on the requirements of your
     organization, and then select OK.

     The task sequence configuration settings are saved, and the modifications are
     displayed in the details pane of the Deployment Workbench.

     For more information about customizing task sequence steps for installing:

     Applications, see Customize Application Installation in Task Sequences

     Packages, see Customize Package Installation in Task Sequences

Configure the Task Sequence Step Properties

On the Properties tab, you configure the properties for task sequence groups or
individual task sequence steps. The configuration settings for:

     Task sequence groups are the same for all groups

     Task sequence steps are different for each task sequence step type

     Table 56 lists the properties common to task sequence groups and steps. In
     addition to these properties, most task sequence steps have properties that are
     specific to the task sequence type.

Table 56. Properties Common to Task Sequence Groups
and Steps

<!-- p.164 -->

                                                                                ﾉ   Expand table

 Setting       Description

 Type          Contains the task sequence type, which is always set to Group for task sequence
               groups or to the types listed in REF _Ref304894666 \h Table 55

 Name          Contains the name of the task sequence group or step displayed in the task
               sequence hierarchy

 Description   Provides descriptive information about the task sequence group or step

For more information about:

     Configuring specific task sequence step types, see the corresponding section in
     Configuring Task Sequences in the Deployment Workbench

     The properties for each task sequence type, see the section for corresponding task
     sequence steps in the MDT document Toolkit Reference

To modify existing task sequence group and individual step properties

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share in which you will configure
     the task sequence).

  3. In the details pane, select task_sequence_name (where task_sequence_name is the
     name of the task sequence you want to configure).

  4. In the Actions pane, select Properties.

     The task_sequence_name Properties dialog box opens (where task_sequence_name
     is the name of the task sequence you want to configure).

  5. On the Task Sequence tab, in the task sequence hierarchy, select the Properties
     tab.

  6. On the Properties tab, configure the task sequence group or individual step based
     on the requirements of your organization, and then select OK.

Configure the Task Sequence Step Options

<!-- p.165 -->

On the Options tab, you configure settings that control how the task sequence step
runs. These settings allow you to disable the step, specify the return codes for the step
that indicate success, determine whether the step should continue in the event of an
error, and any conditions for running the step.

The configuration settings on the Options tab for:

   1. A task sequence group affect all the steps with the group

   2. An individual task sequence step affect only that step

     For example, if you configure a condition for a task sequence group, that condition
     affects all the task sequence steps within the group.

To modify existing task sequence group and individual step options

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share in which you will configure
     the task sequence).

   3. In the details pane, select task_sequence_name (where task_sequence_name is the
     name of the task sequence you want to configure).

   4. In the Actions pane, select Properties.

     The task_sequence_name Properties dialog box opens (where task_sequence_name
     is the name of the task sequence you want to configure).

   5. On the Task Sequence tab, in the task sequence hierarchy, select the Options tab.

   6. On the Options tab, configure the task sequence group or individual step
     sequences based on the requirements of your organization, and then select OK.

   7. On the Task Sequence tab, configure the settings listed in Table 57 based on the
     requirements of your organization, and then select OK.

     Table 57. Configuration Settings on the Task Sequence
     Tab of Task Sequence Properties

                                                                         ﾉ   Expand table

<!-- p.166 -->

Setting        Description

Disable this   Select to control whether the task sequence step runs during the task
step           sequence. If the check box is:

               - Selected, the task sequence group or step is not run during the task
               sequence

               - Cleared, the task sequence group or step runs during the task sequence

               This check box is cleared by default.

Success        Contains the list of numeric codes that indicate whether the task sequence
codes          step finished successfully.

               Success codes are not available in task sequence step groups.

Continue       Select to control whether the task sequence should continue when the task
on error       sequence group or step encounters an error. If the check box is:

               - Selected, the task sequence continues if the group or step encounters an
               error

               - Cleared, the task sequence will not continue if the group or step encounters
               an error

               This check box is selected by default.

Condition      Contains any conditional criteria for running this step. If no criteria are
list box       specified, the step runs.Add criteria for determining when the group of tasks
               should (or should not) run. Use the Add, Remove, and Edit buttons to modify
               the conditions under which the group of tasks runs.

               The criteria can be based on:

               - An IF statement

               - A task sequence variable

               - The version of the target operating system.

               - A Windows Management Instrumentation (WMI) Query Language (WQL)
               query within a WMI namespace

               Any conditions configured for a group affect all the tasks within a group.

               For more information about conditions in task sequence steps, see Configure
               Task Sequence Step Conditions.

<!-- p.167 -->

Configure the Task Sequence Properties OS Info Tab

The task sequence properties stored on the OS Info tab are mostly configured when you
run the New Task Sequence Wizard. You update the task sequence properties on the OS
Info tab through the task_sequence_name Properties dialog box (where
task_sequence_name is the name of the task sequence in the Deployment Workbench).

To modify existing task sequence properties on the OS Info tab

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share in which you will configure
     the task sequence).

  3. In the details pane, select task_sequence_name (where task_sequence_name is the
     name of the task sequence you want to configure).

  4. In the Actions pane, select Properties.

     The task_sequence_name Properties dialog box opens (where task_sequence_name
     is the name of the task sequence you want to configure).

  5. On the OS Info tab, configure the settings listed in Table 58 based on the
     requirements of your organization, and then select OK.

     Table 58. Configuration Settings on the OS Info Tab of
     Task Sequence Properties

                                                                              ﾉ   Expand table

      Setting           Description

      Operating         Contains the name of the operating system that you provided when
      system            creating the task sequence—for example Windows 8 ENTERPRISE.
      description
                        The information in this text box is automatically generated by the
                        Deployment Workbench and cannot be modified.

      Build             Contains the build number of the operating system.

                        The information in this text box is automatically generated by the
                        Deployment Workbench and cannot be modified.

<!-- p.168 -->

      Setting          Description

      Platform         Contains the processor architecture of the operating system—for
                       example, x86.

                       The information in this text box is automatically generated by the
                       Deployment Workbench and cannot be modified.

      Edit             Select to modify the contents of the Unattended.xml file that the
      Unattend.xml     Deployment Workbench generates for Windows.

                       The Deployment Workbench cannot create catalog files for some
                       Windows images of different architecture types. The following list
                       describes the architecture types running the Deployment Workbench
                       and catalogs that you can create for each architecture:

                       - Deployment Workbench running on x86. Creates catalogs for x86
                       and x64 Windows images

                       - Deployment Workbench running on x64. Creates catalogs only for
                       x64 Windows images

                       The Get Operating System Catalog Wizard may appear if an operating
                       system does not yet have a catalog. You will see a progress bar in the
                       Get Operating System Catalog Wizard, but no user interaction is
                       required. The wizard may take a few minutes to finish.

     The task sequence configuration settings are saved, and the modifications are
     displayed in the details pane of the Deployment Workbench.

Copy Task Sequences in the Deployment Workbench

You can copy and paste task sequences and folders beneath the Task Sequences node in
the Deployment Workbench using the Copy and Paste actions as described in Copy
Items in the Deployment Workbench.

Move Task Sequences in the Deployment Workbench

Move task sequences and folders beneath the Task Sequences node in the Deployment
Workbench by using the Cut and Paste actions as described in Move Items in the
Deployment Workbench.

Rename Task Sequences in the Deployment Workbench

<!-- p.169 -->

Rename task sequences and folders beneath the Task Sequences node in the
Deployment Workbench by using the Rename action as described in Rename Items in
the Deployment Workbench.

Delete Task Sequences from the Deployment Workbench
Delete task sequences and folders beneath the Task Sequences node in the Deployment
Workbench using the Delete Selected Items Wizard as described in Delete Items from
the Deployment Workbench. The Delete Selected Items Wizard allows you to delete
individual task sequences or entire folder structures.

Manage Folders for Task Sequences in the Deployment Workbench
You can manage folders beneath the Task Sequences node in the Deployment
Workbench to create hierarchical groupings of task sequences. For more information on:

   1. Managing folders, see Manage Folders in the Deployment Workbench

   2. Selection profiles, see Manage Selection Profiles

Enable or Disable a Task Sequence in the Deployment Workbench
You can control whether task sequences are available to other wizards and dialog boxes
in the Deployment Workbench using the Enable this task sequence check box on the
General tab of the package Properties dialog box, as described in Configuring Task
Sequences in the Deployment Workbench.

Prevent a Task Sequence from Being Visible in the Deployment
Wizard
You can prevent a task sequence from being visible in the Deployment Wizard using the
Hide this task sequence in the Deployment Wizard check box on the General tab of
the application Properties dialog box, as described in Configuring Task Sequences in the
Deployment Workbench.

Modify the Unattended Setup Answer File Associated with the Task
Sequence

MDT automatically updates the unattended setup answer file (Unattend.xml) for a task
sequence based on the configuration settings you provide in the Deployment
Workbench and in the Deployment Wizard. However, there are instances in which you

<!-- p.170 -->

may need to modify the unattended setup answer file for a task sequence directly, such
as when you modify a configuration parameter that is not exposed in the Deployment
Workbench or in the Deployment Wizard. Directly modify the unattended setup answer
file for a task sequence by selecting Edit Unattend.xml on the OS Info tab of the task
sequence Properties dialog box.

For more information about:

     Modifying the unattended setup answer file in the Deployment Workbench, see
     Configure the Task Sequence Properties OS Info Tab

     Unattend.xml, see the Windows Assessment and Deployment Kit User's Guide in the
     Windows ADK

Performing Common Management Tasks in the
Deployment Workbench
You use the Deployment Workbench to perform many of the common management
tasks. Although some management is unique to each type of item, the following tasks
are common to all items in the Deployment Workbench:

     Managing folders as described in Manage Folders in the Deployment Workbench

     Viewing item properties as described in View Item Properties in the Deployment
     Workbench

     Copying items as described in Copy Items in the Deployment Workbench

     Moving items as described in Move Items in the Deployment Workbench

     Renaming items as described in Rename Items in the Deployment Workbench

     Deleting items as described in Delete Items from the Deployment Workbench

Manage Folders in the Deployment Workbench
You use folders to organize applications, operating systems, device drivers, and other
items in the Deployment Workbench. Folders allow you to create hierarchies for
organizing items as well as subsets of items that you can include in selection profiles.

  ７ Note

<!-- p.171 -->

  Folders are similar in concept to the groups that existed in previous versions of
  MDT, such as device driver groups.

Management tasks for folders include:

     Creating a new folder as described in Create a New Folder in the Deployment
     Workbench

     Modifying an existing folder as described in Modify an Existing Folder in the
     Deployment Workbench

     Copying a folder as described in Copy a Folder in the Deployment Workbench

     Moving a folder as described in Move a Folder in the Deployment Workbench

     Renaming a folder as described in Rename a Folder in the Deployment Workbench

     Deleting a folder as described in Delete a Folder from the Deployment Workbench

     Enabling or disabling a folder as described in Enable or Disable a Folder in the
     Deployment Workbench

Create a New Folder in the Deployment Workbench

Create folders in the Deployment Workbench using the New Folder Wizard. Start the
New Folder Wizard using one of the following methods:

     In the console tree, select a node or a folder. Then, in the Actions pane, select New
     Folder.

     In the console tree, select a node or a folder. Then, from the Action menu, select
     New Folder.

     In the console tree, right-click a node or a folder. Then, select New Folder.

To create a new folder

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/node_or_folder (where
     deployment_share is the name of the deployment share in which you will create the

<!-- p.172 -->

    folder and node_or_folder is the name of the node or folder in which you will create
    the folder).

  3. In the Actions pane, select New Folder.

    The New Folder Wizard starts.

  4. Complete the New Folder Wizard using the information in Table 59.

    Table 59. Information for Completing the New Folder
    Wizard

                                                                              ﾉ    Expand table

     On this wizard   Do this
     page

     General          a. In Folder name, type folder_name (where folder_name is the name of
     Settings         the folder you want to create).

                      b. In Folder comment, type folder_comment (where folder_comment is
                      text that describes the user of the folder in the deployment share).

                      c. Select or clear the Enable this folder check box based on the needs of
                      your organization. If this check box is:

                      - Selected, the folder, subfolders, and content can be included in
                      selection profiles

                      - Cleared, the folder, subfolders, and content cannot be included in
                      selection profiles

                      d. Select Next.

     Summary          Review the information, then select Next.

     Confirmation     You can select Save Output to save the output of the wizard to a file. You
                      can also select View Script to view the Windows PowerShell scripts used
                      to perform the wizard tasks.

                      Select Finish.

    After the New Folder Wizard finishes, the new folder appears in the deployment
    share in the Deployment Workbench.

Modify an Existing Folder in the Deployment Workbench

<!-- p.173 -->

Modify existing folders in the Deployment Workbench using the Properties actions as
described in View Item Properties in the Deployment Workbench. The folder properties
are mostly configured when you run the New Folder Wizard. Update the folder
properties on the General tab through the folder_name Properties dialog box (where
folder_name is the name of the folder in the Deployment Workbench).

To modify an existing folder

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/node_or_folder (where
     deployment_share is the name of the deployment share in which you will modify
     the folder and node_or_folder is the name of the node or folder that contains the
     folder to be modified).

  3. In the details pane, select folder_name (where folder_name is the name of the
     folder you want to modify).

  4. In the Actions pane, select Properties.

     The folder_name Properties dialog box opens (where folder_name is the name of
     the folder to be modified).

  5. On the General tab, configure the settings listed in Table 60 based on the
     requirements of your organization, and then select OK.

     Table 60. Configuration Settings on the General Tab of
     Folder Properties

                                                                                 ﾉ    Expand table

      Setting          Description

      Name             Contains the name of the folder that is displayed in the Deployment
                       Workbench.

      Comments         Provides information about the folder.

      Enable this      Select to enable or disable the folder. If the check box is:
      folder
                       - Selected, you can select the folder in selection profiles

<!-- p.174 -->

       Setting          Description

                        - Cleared, you cannot select the folder in selection profiles

     The folder configuration settings are saved, and the modifications are displayed in
     the details pane of the Deployment Workbench.

Copy a Folder in the Deployment Workbench

You can copy and paste folders in the Deployment Workbench using the Copy and
Paste actions as described in Copy Items in the Deployment Workbench.

Move a Folder in the Deployment Workbench

You can move folders in the Deployment Workbench using the Cut and Paste actions as
described in Move Items in the Deployment Workbench.

Rename a Folder in the Deployment Workbench

You can rename folders in Deployment Workbench using the Rename action as
described in Rename Items in the Deployment Workbench.

Delete a Folder from the Deployment Workbench

You can delete a folder in the Deployment Workbench using the Delete Selected Items
Wizard as described in Delete Items from the Deployment Workbench. The Delete
Selected Items Wizard allows you to delete individual folders or an entire hierarchy of
folders.

Enable or Disable a Folder in the Deployment Workbench

You can control whether folders are available to other wizards and dialog boxes in the
Deployment Workbench using the Enable this folder check box on the General tab of
the folder Properties dialog box. For more information on enabling or disabling folders
in the Deployment Workbench, see Modify an Existing Folder in the Deployment
Workbench.

View Item Properties in the Deployment Workbench

<!-- p.175 -->

You can view the properties of operating systems, device drivers, and other items from
the Deployment Workbench using one of the following methods:

     In the details pane, select an item. Then, in the Actions pane, select Properties.

     In the details pane, select an item. Then, from the Action menu, select Properties.

     In the details pane, right-click an item, and then select Properties.

     In the details pane, double-click an item.

     To set the properties of an item in a deployment share

To set the properties of an item in a deployment share

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/item_type (where
     deployment_share is the name of the deployment share in which you will copy the
     item and item_type is the type of item you will copy, such as an operating system
     or device driver).

   3. In the details pane, select item (where item is the name of the item to be
     renamed).

   4. In the Actions pane, select Properties.

     The item Properties dialog box is displayed (where item is the name of the item
     you selected).

Copy Items in the Deployment Workbench
Use the Deployment Workbench to copy operating systems, device drivers, and other
items within a deployment share or between two deployments shares. When you copy
an item, the Deployment Workbench creates a link to the original item instead of
creating a separate copy of the item. This reduces the size of the deployment share. If
you want to create a duplicate of an item, import the item again in the target folder.

When you copy an item between deployment shares and an item with the same:

     GUID already exists in the target deployment share, the configuration settings for
     the source item will be applied to the target item, including the name (if the items
     do not already have the same name)

<!-- p.176 -->

     Name already exists in the target deployment share, an error is generated, because
     two items of the same type cannot have the same name

     You can copy items by using:

  1. Cut and Paste actions as described in Copy Items Using the Cut and Paste Actions

  2. Drag-and-drop functionality as described in Copy Items Using Drag-and-Drop
     Functionality

Copy Items Using the Cut and Paste Actions

You can copy an item using the Cut and Paste actions in the Deployment Workbench.
Copy the item from the source location using one of the following methods:

     In the details pane, select an item. Then, in the Actions pane, select Copy.

     In the details pane, select an item. Then, from the Action menu, select Copy.

     In the details pane, right-click an item, and then select Copy.

     Paste the item that you have copied using one of the following methods:

     In the details pane, select the target location. Then, in the Actions pane, select
     Paste.

     In the details pane, select the target location. Then, from the Action menu, select
     Paste.

     In the details pane, right-click the target location, and then select Paste.

To copy and paste items in a deployment share

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/item_type (where
     deployment_share is the name of the deployment share in which you will copy the
     item and item_type is the type of item you will copy, such as an operating system
     or device driver).

  3. In the details pane, select item (where item is the name of the item to be copied).

  4. In the Actions pane, select Copy.

<!-- p.177 -->

   5. In the details pane, go to target_folder (where target_folder is the name of the
     folder where you want to copy the item).

   6. In the Actions pane, select Paste.

     The new copy of the item appears in the details pane of the Deployment
     Workbench.

Copy Items Using Drag-and-Drop Functionality

You can copy items by dragging an item from the source location to the target location.

To copy items in the Deployment Workbench using drag-and-drop
functionality

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/item_type (where
     deployment_share is the name of the deployment share to which you will copy the
     item and item_type is the type of item you will copy, such as an operating system
     or device driver).

   3. In the details pane, drag item (where item is the name of the item to be copied) to
     the target location, press CTRL, and then release the mouse button.

     The item is copied to the target location in the details pane of the Deployment
     Workbench.

Move Items in the Deployment Workbench

Use the Deployment Workbench to move operating systems, device drivers, and other
items within a deployment share or between two deployments shares. You can move
items by using:

     Cut and Paste actions as described in Move Items Using the Cut and Paste Actions

     Drag-and-drop functionality as described in Move Items Using Drag-and-Drop
     Functionality

Move Items Using the Cut and Paste Actions

<!-- p.178 -->

You can move an item using the Cut and Paste in the Deployment Workbench. Cut the
item from the source location using one of the following methods:

     In the details pane, select an item. Then, in the Actions pane, select Properties.

     In the details pane, select an item. Then, from the Action menu, select Properties.

     In the details pane, right-click an item, and then select Properties.

     In the details pane, double-click an item.

To set the properties of an item in a deployment share

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/item_type (where
     deployment_share is the name of the deployment share in which you will copy the
     item and item_type is the type of item you will copy, such as an operating system
     or device driver).

  3. In the details pane, select item (where item is the name of the item to be renamed).

  4. In the Actions pane, select Properties.

     The item Properties dialog box is displayed (where item is the name of the item
     you selected).

Move Items Using Drag-and-Drop Functionality

You can move items by dragging them from the source location to the target location.

To move items in the Deployment Workbench using drag-and-drop
functionality

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/item_type (where
     deployment_share is the name of the deployment share to which you will move the
     item and item_type is the type of item you will move, such as an operating system
     or device driver).

<!-- p.179 -->

  3. In the details pane, drag item (where item is the name of the item to be moved) to
     the target location.

     The item is moved to the target location.

Rename Items in the Deployment Workbench
You can rename operating systems, device drivers, and other items in the Deployment
Workbench by using one of the following methods:

     In the details pane, select an item. Then, in the Actions pane, select Rename.

     In the details pane, select an item. Then, from the Action menu, select Rename.

     In the details pane, right-click an item, and then select Rename.

     Because the Copy and Paste actions in the Deployment Workbench create a link to
     the original item rather than a separate copy. So, when you rename an item, the
     Deployment Workbench automatically renames any copies of an item in other
     folders.

To rename an item in a deployment share

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/item_type (where
     deployment_share is the name of the deployment share in which you will rename
     the item and item_type is the type of item you will rename, such as an operating
     system or device driver).

  3. In the details pane, select item (where item is the name of the item to be
     renamed). Then, in the Actions pane, select Rename.

  4. In the details pane, type new_item_name (where new_item_name is the new name
     of the item), and then press ENTER.

     The new name of the item appears in the details pane of the Deployment
     Workbench.

Delete Items from the Deployment Workbench

<!-- p.180 -->

You can delete operating systems, device drivers, and other items from the Deployment
Workbench using the Delete Selected Items Wizard. Start the Delete Selected Items
Wizard using one of the following methods:

     In the details pane, select an item. Then, in the Actions pane, select Delete.

     In the details pane, select an item. Then, from the Action menu, select Delete.

     In the details pane, right-click an item, and then select Delete.

     You can delete individual items or folders that contain one or more items or
     subfolders. You can also delete items that have copies in multiple folders. The
     Delete Selected Items Wizard's Options page includes the check boxes shown in
     Table 61.

Table 61. Information for Completing the Delete Selected
Items Wizard

                                                                                   ﾉ   Expand table

 Check box                            Description

 Completely delete these items,       Select to delete an item, including all copies of an item that
 even if there are copies in other    might exist in other folders. If this check box is:
 folders
                                      - Selected, the selected item and all copies in other folders
                                      are deleted

                                      - Cleared, only the selected item is deleted; all copies in
                                      other folders are unaffected

 Recursively delete the contents of   This check box allows you to delete:
 folders, as well as multiple items
 that have the same source file       - Not only the immediate contents of a folder but also the
                                      content from subfolders

                                      - Multiple items that have the same source file—for
                                      example, if you have an operating system image file that
                                      contains multiple operating system editions, such as Server-
                                      Core or Server-Enterprise

                                      If this check box is:

                                      - Selected and the selected item is a folder, then the folder,
                                      subfolders, and all the contents of all subfolders are deleted

                                      - Selected and the selected item not a folder, then the item

<!-- p.181 -->

Check box                         Description

                                  and all items that have the same source file are deleted

                                  - Cleared, only the selected item is deleted; all subfolders or
                                  other items that have the same source file are unaffected

 ７ Note

 When you delete an item from the Deployment Workbench, the corresponding file
 or folder is also deleted in the deployment_share\item_type\item_subfolder (where
 deployment_share is the name of the deployment share and item_type is the type of
 item you are deleting, such as an operating system or device driver) if no remaining
 items reference the folder.

To delete an item from a deployment share

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
    Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
    Workbench/Deployment Shares/deployment_share/item_type (where
    deployment_share is the name of the deployment share to which you will add the
    operating system and item_type is the type of item you are deleting, such as an
    operating system or device driver).

  3. In the details pane, select item (where item is the name of the item to be deleted,
    such as a folder, an operating system, or a device driver).

  4. In the Actions pane, select Delete.

    The Delete Selected Items Wizard starts.

  5. Complete the Delete Selected Items Wizard using the information in Table 62.

    Table 62. Information for Completing the Delete
    Selected Items Wizard

                                                                              ﾉ    Expand table

<!-- p.182 -->

      On this wizard   Do this
      page

      Options          - Select or clear the Completely delete these items, even if there are
                       copies in other folders check box based on your requirements.

                       By default, this check box is cleared.

      Summary          Select Next.

      Confirmation     You can select Save Output to save the output of the wizard to a file. You
                       can also select View Script to view the Windows PowerShell scripts used
                       to perform the wizard tasks.

                       Select Finish.

     After the Delete Selected Items Wizard finishes, the item and other affected items
     are removed from the Deployment Workbench and from the deployment share.

Performing Advanced Configuration Tasks in the
Deployment Workbench
The Deployment Workbench includes advanced configuration options that extend the
features provided in basic LTI deployments. These configuration options provide more
granular selection of the content you want to include in the deployment, support
deployments in larger organizations, and support deployments from stand-alone media
without the need to connect to a deployment share.

Advanced configuration tasks that you can perform include:

     Managing selection profiles as described in Manage Selection Profiles

     Managing linked deployment shares as described in Manage Linked Deployment
     Shares

     Managing deployment media as described in Manage LTI Deployment Media

     Managing the MDT DB as described in Manage the MDT DB

Manage Selection Profiles
Selection profiles allow you to select one or more folders in the Deployment Workbench
that contain one or more items in the Deployment Workbench, including applications,
device drivers, operating systems, operating system packages, and task sequences.

<!-- p.183 -->

se selection profiles to group items, and then use those groupings of items:

      To include the appropriate device drivers and packages for Windows PE.

      To include the appropriate device drivers for the target operating system in the
      Inject Drivers task sequence step type.

      To identify the operating system packages to deploy in the Install Updates Offline
      task sequence step type.

      As the basis for creating linked deployment shares.

      As the basis for creating MDT deployment media.

Table 63 lists the default selection profiles in the Deployment Workbench.

Table 63. Default Selection Profiles in Deployment
Workbench

                                                                               ﾉ   Expand table

 Selection      Description
 profile

 Everything     Holds all folders from all nodes in the Deployment Workbench, including all
                applications, operating systems, device drivers, operating system packages, and
                task sequences.

 All Drivers    Holds all folders from the Out-of-Box Drivers node in the Deployment
                Workbench, including all device drivers.

 All Drivers    Holds all folders from the Applications and Out-of-Box Drivers nodes in the
 and Packages   Deployment Workbench, including all applications and device drivers.

 All Packages   Holds all folders from the Applications node in the Deployment Workbench,
                including all applications and device drivers.

 Nothing        Includes no folders or items in the Deployment Workbench.

 Sample         A sample selection profile that shows how to select a subset of the items and
                include all folders from the Packages and Task Sequences nodes in the
                Deployment Workbench. This selection profile includes all operating system
                packages and task sequences.

Manage selection profiles by completing the following tasks in the Deployment
Workbench:

<!-- p.184 -->

     Create a new selection profile as described in Create a New Selection Profile in the
     Deployment Workbench.

     Modify an existing selection profile as described in Modify an Existing Selection
     Profile in the Deployment Workbench.

     Copy a selection profile as described in Copy a Selection Profile in the Deployment
     Workbench.

     Move a selection profile as described in Move a Selection Profile in the
     Deployment Workbench.

     Rename a selection profile as described in Rename a Selection Profile in the
     Deployment Workbench.

     Delete a selection profile as described in Delete a Selection Profile from the
     Deployment Workbench.

     Identify the differences between selection provides and groups as described in
     Identify the Relationship Between Selection Profiles and Groups.

Create a New Selection Profile in the Deployment Workbench

Create selection profiles in the Deployment Workbench using the New Selection Profile
Wizard. Start the New Selection Profile Wizard using one of the following methods:

     In the console tree, select the Selection Profiles node. Then, in the Actions pane,
     select New Selection Profile.

     In the console tree, select the Selection Profiles node. Then, from the Action menu,
     select New Selection Profile.

     In the console tree, right-click the Selection Profiles node, and then select New
     Selection Profile.

To create a new selection profile

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Advanced
     Configuration/Selection Profiles (where deployment_share is the name of the
     deployment share to which you will add the application).

<!-- p.185 -->

   3. In the Actions pane, select New Selection Profile.

     The New Selection Profile Wizard starts.

   4. Complete the New Selection Profile Wizard using the information in Table 64.

     Table 64. Information for Completing the New
     Selection Profile Wizard

                                                                                 ﾉ   Expand table

      On this wizard   Do this
      page

      General          - In Selection profile name, type profile_name (where profile_name is the
      Settings         name of the new profile).

                       - In Selection profile comments, type comment (where comment is
                       descriptive text that provides information about the selection profile).

                       - Select Next.

      Folders          In Select the folders that should be included in this selection profile,
                       select folders (where folders is the name of the folders that contain the
                       Deployment Workbench items you want to include in this selection
                       profile), and then select Next.

      Summary          Review in the information in Details, and then select Next.

      Confirmation     You can select Save Output to save the output of the wizard to a file. You
                       can also select View Script to view the Windows PowerShell scripts used
                       to perform the wizard tasks.

                       Select Finish.

     The New Selection Profile Wizard finishes. The selection profile is added to the list
     of selection profiles in the details pane of the Deployment Workbench.

Modify an Existing Selection Profile in the Deployment
Workbench

Modify existing selection profiles in the Deployment Workbench's Selection Profiles
node using the Properties actions as described in View Item Properties in the
Deployment Workbench. The selection profile properties are mostly configured when
you run the New Selection Profile Wizard. However, you can update the selection profile

<!-- p.186 -->

properties on the General tab of the profile_name Properties dialog box (where
profile_name is the name of the selection profile in the Deployment Workbench).

To configure the General tab for package properties

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Advanced
     Configuration/Selection Profiles (where deployment_share is the name of the
     deployment share where you will configure the package).

  3. In the details pane, select profile_name (where profile_name is the name of the
     selection profile you want to configure).

  4. In the Actions pane, select Properties.

     The profile_name Properties dialog box opens (where profile_name is the name of
     the selection profile you want to configure).

  5. On the General tab, configure the settings listed in Table 65 based on the
     requirements of your organization, and then select OK.

     Table 65. Configuration Settings on the General Tab of
     Package Properties

                                                                                 ﾉ   Expand table

      Setting     Description

      Name        Contains the name of the selection displayed in the Deployment Workbench
                  and the Deployment Wizard.

      Comments    Provides information about the selection profile.

      Folders     Hierarchical list of the folders and their selection status.

     The selection profile configuration settings are saved, the modifications are
     displayed in the details pane of the Deployment Workbench, and the
     deployment_share\Control\SelectionProfiles.xml file (where deployment_share is the
     name of the deployment share) is updated with the selection profile configuration
     settings.

<!-- p.187 -->

Copy a Selection Profile in the Deployment Workbench

You can copy and paste selection profiles in the Deployment Workbench using the Copy
and Paste actions as described in Copy Items in the Deployment Workbench.

Move a Selection Profile in the Deployment Workbench

You can move selection profiles in the Deployment Workbench using the Cut and Paste
actions as described in Move Items in the Deployment Workbench.

Rename a Selection Profile in the Deployment Workbench

You can rename selection profiles in the Deployment Workbench using the Rename
action as described in Rename Items in the Deployment Workbench.

Delete a Selection Profile from the Deployment Workbench

You can delete a selection profile in the Deployment Workbench using the Delete
Selected Items Wizard as described in Delete Items from the Deployment Workbench.
The Delete Selected Items Wizard allows you to delete individual selection profiles.

Identify the Relationship Between Selection Profiles and Groups

Use selection profiles to create groups of Deployment Workbench items, such as
operating systems, device drivers, or applications. Use the selection profiles to specify
device drivers, define content to include in a linked deployment share, define the
content to include for media deployments, and other tasks.

The relationship between items and folders in a selection profile is stored in the
following files in the deployment_share\Control folder (where deployment_share is the
location of the deployment share):

     itemGroups.xml. There is a separate file for each type of item, including:

        ApplicationGroups.xml

        DriverGroups.xml

        LinkedDeploymentShareGroups.xml

        MediaGroups.xml

        OperatingSystemGroups.xml

<!-- p.188 -->

   PackageGroups.xml

   SelectionProfileGroups.xml

   TaskSequenceGroups.xml

   For example, consider a selection profile for device drivers called
   WinPEAndFullOS that are stored in a folder created immediately beneath the
   Out-of-Box Drivers node. The following code is an excerpt from the
   DriverGroups.xml file generated when you created the selection profile:

  XML

  <groups>
  ...
  <group_quid="{e5143c1c-24e4-466d-9b56-b0db693c8619}" enable="True">
      <Name>WinPEAndFullOS</Name>
  ...
      <Member>{1eca45a5-d7ef-475a-bb0d-7f7747f16b3a}</Member>

SelectionProfiles.xml. This file contains the definitions for all the selection profiles
defined for the deployment share. The following code is an excerpt from the
SelectionProfile.xml file generated when you created the WinPEAndFullOS
selection profile:

  XML

  <selectionProfile quid="{46a3e6a2-694c-4c2f-afd8-a2986e6e252e}"
  enable="True">
    <Name>Drivers Safe For WinPE</Name>
    <Comments>Include Driver packages safe for WinPE.</Comments>
    <ReadOnly>True</ReadOnly>
    <Definition><SelectionProfile><Include path="Out-of-Box
  Drivers\WinPEAndFullOS" /><Include path="Out-of-Box Drivers\WinPEOnly"
  /></SelectionProfile></Definition>
  </selectionProfile>

By default, if you do not specify a selection profile or group in the
CustomSettings.ini file or in the MDT DB, LTI uses all items. If you specify both
selection profiles and groups in the CustomSettings.ini file or the MDT DB, LTI uses
all the items from both the selection profile and the group.

For example, if you specify a selection profile and use the default group (which
includes all items), the end result is that LTI uses all items, because the default
group includes all items, regardless of what you specify in the selection profile. To

<!-- p.189 -->

     restrict the items to a selection profile, specify a group that contains no items (that
     is, is empty). The reverse is true if you want to use a group.

     Because of the introduction of folders in MDT, groups include all folders and
     subfolders by default. You can override this behavior using the
     SkipGroupSubFoldersproperty. For more information on this property, see the
     corresponding section in the MDT document Toolkit Reference.

     In most instances, you can use selection profiles and groups to perform most
     deployments. However, the following properties are available for more advanced
     scenarios—such as if you want to exclude a parent folder but include a child folder:

     CustomDriverSelectionProfile

     CustomPackageSelectionProfile

     CustomWizardSelectionProfile

     For more information on these properties, see the corresponding sections in the
     MDT document Toolkit Reference.

Manage Linked Deployment Shares

Linked deployment shares in MDT allow you to provide a logical connection between
two deployment shares: a source and a target deployment share. A selection profile
determines the items to be linked. When creating the link between the deployment
shares, you can choose whether to merge or replace content in the target deployment
share.

Using linked deployment shares, you can easily replicate an entire deployment share or
portions of a deployment share to another deployment share. In this way, you can make
changes to one deployment share, and then easily update other deployment shares
based on the selection profiles you chose when creating the linked deployment shares.

Manage linked deployment shares by performing the following tasks in the Deployment
Workbench:

     Create a new linked deployment share as described in Create a New Linked
     Deployment Share in the Deployment Workbench.

     Modify an existing linked deployment share as described in Modify an Existing
     Linked Deployment Share in the Deployment Workbench.

     Copy a linked deployment share as described in Copy a Linked Deployment Share
     in the Deployment Workbench.

<!-- p.190 -->

     Move a linked deployment share as described in Move a Linked Deployment Share
     in the Deployment Workbench.

     Rename a linked deployment share as described in Rename a Linked Deployment
     Share in the Deployment Workbench.

     Delete a linked deployment share as described in Delete a Linked Deployment
     Share from the Deployment Workbench.

     Replicate linked deployment shares as described in Replicate Linked Deployment
     Shares in the Deployment Workbench.

     In addtion to managing linked deployement shares in the Deployment Workbench,
     you can manage linked deployment shares using the MDT Windows PowerShell
     cmdlets. For more information on managing linked deployment shares using the
     MDT Windows PowerShell cmdlets, see the following sections beneath the section,
     "MDT Windows PowerShell Cmdlets", in the MDT document Toolkit Reference:

     Update-MDTLinkedDS

     Get-MDTDeploymentShareStatistics

Create a New Linked Deployment Share in the Deployment
Workbench

Create new linked deployment shares in the Deployment Workbench using the New
Linked Deployment Share Wizard. Start the New Linked Deployment Share Wizard using
one of the following methods:

     In the console tree, select the Linked Deployment Share node. Then, in the Actions
     pane, select New Linked Deployment Share.

     In the console tree, select the Linked Deployment Share node. Then, from the
     Action menu, select New Linked Deployment Share.

     In the console tree, right-click the Linked Deployment Share node, and then select
     New Linked Deployment Share.

To create a new linked deployment share

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

<!-- p.191 -->

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/deployment_share/Advanced Configuration/Linked
  Deployment Share (where deployment_share is the name of the deployment share
  you want to configure).

3. In the Actions pane, select New Linked Deployment Share.

  The New Linked Deployment Share Wizard starts.

4. Complete the New Linked Deployment Share Wizard using the information in Table
  66.

  Table 66. Information for Completing the New Linked
  Deployment Share Wizard

                                                                               ﾉ   Expand table

   On this        Do this
   wizard page

   General        a. In Linked deployment share UNC path, type unc_path (where unc_path
   Settings       is the fully qualified UNC path to the target deployment share).

                  You can alternatively select Browse to find the network shared folder.

                  b. In Comments, type comment (where comment is descriptive text that
                  provides information about the linked deployment share).

                  c. In Selection profile, select profile (where profile is the name of the
                  selection profile that will be used to establish the items to be linked
                  between the source and target deployment shares).

                  d. Under Selection profile, select one of the following options based on
                  your requirements:

                  - Merge the selected content into the target deployment share. Select to
                  configure the wizard to copy the content in the selection profile into an
                  existing target deployment share without deleting or overwriting any
                  folders or items in the target deployment share. Selecting this option also
                  copies the standard folders from the source deployment share, including
                  the Scripts, Tools, USMT, and $OEM$ folders.

                  - Replace the contents of the target deployment share folders with those
                  selected. Select to configure the wizard to copy the content in the
                  selection profile into an existing target deployment share and overwrite
                  any existing folders or items in the target deployment share. Selecting this
                  option also copies the standard folders from the source deployment share,

<!-- p.192 -->

      On this        Do this
      wizard page

                     including the Scripts, Tools, USMT, and $OEM$ folders.

                     By default, the Merge the selected content into the target deployment
                     share option is selected.

                     e. Select Next.

      Summary        Review in the information in Details, and then select Next.

      Confirmation   You can select Save Output to save the output of the wizard to a file. You
                     can also select View Script to view the Windows PowerShell scripts used to
                     perform the wizard tasks.

                     Select Finish.

     The New Linked Deployment Share Wizard finishes, and the linked deployment
     share is added to the list of linked deployments shares in the details pane of the
     Deployment Workbench.

Modify an Existing Linked Deployment Share in the Deployment
Workbench

Modify existing linked deployment share in the Deployment Workbench's Linked
Deployment Shares node using the Properties actions as described in View Item
Properties in the Deployment Workbench. The linked deployment share properties are
configured when you run the New Linked Deployment Share Wizard. However, you can
update the linked deployment share properties on the General tab of the
linked_deployment_share Properties dialog box (where linked_deployment_share is the
name of the linked deployment share in the Deployment Workbench).

To modify an existing linked deployment share

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Advanced Configuration/Linked
     Deployment Share (where deployment_share is the name of the deployment share
     in which you will configure the package).

  3. In the details pane, select linked_deployment_share (where
     linked_deployment_share is the name of the linked deployment share you want to

<!-- p.193 -->

  configure).

4. In the Actions pane, select Properties.

  The linked_deployment_share Properties dialog box opens (where
  linked_deployment_share is the name of the selection profile you want to
  configure).

5. On the General tab, configure the settings listed in Table 67 based on the
  requirements of your organization, and then select OK.

  Table 67. Configuration Settings on the General Tab of
  Linked Deployment Share Properties

                                                                              ﾉ   Expand table

   Setting                      Description

   Link identifier              Contains the identifier of the linked deployment share.

                                The identifier in this text box is automatically generated by
                                the Deployment Workbench and cannot be modified.

   Comments                     Provides information about the linked deployment share.

   Linked deployment share      Contains the fully qualified UNC path to the target
   UNC path                     deployment share.

   Choose a selection profile   Contains the selection profile that identifies the content to be
                                replicated between the source and target deployment shares.

   Merge the selected           Select to configure the wizard to copy the content in the
   content into the target      selection profile into an existing target deployment share
   deployment share             without deleting or overwriting any folders or items in the
                                target deployment share. Selecting this option also copies the
                                standard folders from the source deployment share, including
                                the Scripts, Tools, USMT, and $OEM$ folders.

   Replace the contents of      Select to configure the wizard to copy the content in the
   the target deployment        selection profile into an existing target deployment share and
   share folders with those     overwrite any existing folders or items in the target
   selected                     deployment share. Selecting this option also copies the
                                standard folders from the source deployment share, including
                                the Scripts, Tools, USMT, and $OEM$ folders.

   Copy standard folders        Select to configure the Replicate to Linked Deployment Share
   (Scripts, Tools, USMT,       Wizard to share. If this check box is:

<!-- p.194 -->

Setting                       Description

$OEM$) to this linked         - Selected, the standard folders are copied to the linked
deployment share              deployment share

                              - Cleared, the standard folders are not copied to the linked
                              deployment share

                              This check box is cleared by default.

Automatically update          Select to configure the Replicate to Linked Deployment Share
boot images after             Wizard to automatically update any boot images in the linked
replicating content to this   deployment share after the content is replicated from the
linked deployment share       source deployment share. If this check box is:

                              - Selected, the boot images in the linked deployment share
                              are automatically updated when replication is complete

                              - Cleared, the boot images in the linked deployment share are
                              not automatically updated when replication is complete

                              This check box is cleared by default.

                              By default, the linked deployment share is configured to
                              generate 32-bit and 64-bit boot images. Open the linked
                              deployment share in the Deployment Workbench to change
                              this default behavior as described in Open an Existing
                              Deployment Share in the Deployment Workbench.

Access the linked             Select to configure the Replicate to Linked Deployment Share
deployment share in           Wizard to open the linked deployment share in single-user
single-user mode in order     mode while replicating the content to the linked deployment
to improve replication        share. Single-user mode improves replication performance, If
performance                   this check box is:

                              - Selected, the linked deployment share is opened in single-
                              user mode as replication is performed and replication
                              performance is improved

                              If you select this check box, changes that other users make in
                              the linked deployment share may be overwritten and lost
                              during the replication process.

                              - Cleared, the linked deployment share is not opened in
                              single-user mode as replication is performed and replication
                              performance is unimproved

                              This check box is cleared by default.

<!-- p.195 -->

     The linked deployment share configuration settings are saved. The modifications
     are displayed in the details pane in the Deployment Workbench.

Copy a Linked Deployment Share in the Deployment Workbench

You can copy and paste linked deployment shares in the Deployment Workbench using
the Copy and Paste actions as described in Copy Items in the Deployment Workbench.

Move a Linked Deployment Share in the Deployment Workbench

You can move linked deployment shares in the Deployment Workbench using the Cut
and Paste actions as described in Move Items in the Deployment Workbench.

Rename a Linked Deployment Share in the Deployment
Workbench

You can rename linked deployment shares in the Deployment Workbench using the
Rename action as described in Rename Items in the Deployment Workbench.

Delete a Linked Deployment Share from the Deployment
Workbench

You can delete a linked deployment shares in the Deployment Workbench using the
Delete Selected Items Wizard as described in Delete Items from the Deployment
Workbench. The Delete Selected Items Wizard allows you to delete individual linked
deployment shares.

Replicate Linked Deployment Shares in the Deployment
Workbench

You can replicate the content from the source deployment share to the linked
deployment shares in the Deployment Workbench using the Replicate to Linked
Deployments Share Wizard. Ensure that sufficient storage exists for the linked
deployment share prior to running the Replicate to Linked Deployments Share Wizard,
as the wizard does not verify that sufficient storage exists prior to replicating the
content.

  ７ Note

  By default, the linked deployment share is configured to generate 32-bit and 64-bit
  boot images. Open the linked deployment share in the Deployment Workbench to

<!-- p.196 -->

 change this default behavior as described in Open an Existing Deployment Share
 in the Deployment Workbench.

To replicate content to a linked deployment share

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
    Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
    Workbench/Deployment Shares/deployment_share/Advanced Configuration/Linked
    Deployment Share (where deployment_share is the name of the deployment share
    where you will add the application).

  3. In the details pane, select linked_deployment_share (where
    linked_deployment_share is the name of the linked deployment share you want to
    configure).

  4. In the Actions pane, select Replicate Content.

    The Replicate to Linked Deployment Share Wizard starts. The replication process
    starts automatically and is displayed on the Progress wizard page.

  5. Complete the Replicate to Linked Deployment Share Wizard using the information
    in Table 68.

    Table 68. Information for Completing the Replicate to
    Linked Deployment Share Wizard

                                                                              ﾉ   Expand table

     On this wizard   Do this
     page

     Progress         View the progress of the replication process.

     Confirmation     You can select Save Output to save the output of the wizard to a file. You
                      can also select View Script to view the Windows PowerShell scripts used
                      to perform the wizard tasks.

                      Select Finish.

 ７ Note

<!-- p.197 -->

  If you view the output of the wizard, the replication appears to have occurred twice.
  However, the replication is actually performed in two passes: The first pass copies
  new items into the linked deployment share, and the second pass deletes any items
  that are no longer needed in the linked deployment share.

The Replicate to Linked Deployments Share wizard finishes. The folders and the content
you specified in the selection profile in the linked deployment share are replicated from
the source deployment share to the target deployment share. Depending on the
configuration of the linked deployment share, the folders and content on the target
deployment share are merged or replaced.

Manage LTI Deployment Media

Media in LTI allows you to perform LTI deployments solely from local media, without
connecting to a deployment share. You can store the media on a DVD, USB hard disk, or
other portable device. After you create the media, generate bootable WIM images that
allow the deployment to be performed from portable media devices locally available on
the target computer.

You determine the items to be included on the media in a selection profile you specify
when you create the media. The Deployment Workbench automatically includes
Windows PE in the media WIM image so that Windows PE is started from the media
available to the target computer. When Windows PE starts, the Deployment Wizard is
automatically started, as well.

Manage deployment media by performing the following tasks in the Deployment
Workbench:

     Create new deployment media as described in Create New Deployment Media in
     the Deployment Workbench.

     Modify existing media as described in Modify Existing Media in the Deployment
     Workbench.

     Copy media as described in Copy Media in the Deployment Workbench.

     Move media as described in Move Media in the Deployment Workbench.

     Delete media as described in Delete Media from the Deployment Workbench.

     Generate media images as described in Generate Media Images in the Deployment
     Workbench.

<!-- p.198 -->

     Create bootable devices from deployment media as described in Create Bootable
     Devices from Deployment Media.

     In addtion to managing deployment media in the Deployment Workbench, you
     can manage deployment media using the MDT Windows PowerShell cmdlets. For
     more information on managing deployment media using the MDT Windows
     PowerShell cmdlets, see the following sections beneath the section, "MDT
     Windows PowerShell Cmdlets", in the MDT document Toolkit Reference:

     Update-MDTMedia

     Get-MDTDeploymentShareStatistics

Create New Deployment Media in the Deployment Workbench

Create new deployment media in the Deployment Workbench using the New Media
Wizard. Start the New Media Wizard using one of the following methods:

     In the console tree, select the Media node. Then, in the Actions pane, select New
     Media.

     In the console tree, select the Media node. Then, from the Action menu, select
     New Media.

     In the console tree, right-click the Media node, and then select New Media.

To create new deployment media

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Advanced Configuration/Media
     (where deployment_share is the name of the deployment share to which you will
     add the application).

  3. In the Actions pane, select New Media.

     The New Media Wizard starts.

  4. Complete the New Media Wizard using the information in Table 69.

     Table 69. Information for Completing the New Media
     Wizard

<!-- p.199 -->

                                                                                ﾉ    Expand table

      On this wizard   Do this
      page

      General          - In Media path, type media_path (where media_path is the fully
      Settings         qualified path to an empty local or network shared folder that is the
                       source folder for creating the media).

                       You can alternatively select Browse to find the folder on a local drive or
                       network shared folder.

                       Do not use a subfolder of an existing deployment share as the media
                       path. This will result in the following error when updating the media:
                       "Invalid top level folder"

                       - In Comments, type comment (where comment is descriptive text that
                       provides information about the media).

                       - In Selection profile, select profile (where profile is the name of the
                       selection profile that will be used to establish the items to be stored on
                       the media).

                       - Select Next.

      Summary          Review in the information in Details, and then select Next.

      Confirmation     You can select Save Output to save the output of the wizard to a file. You
                       can also select View Script to view the Windows PowerShell scripts used
                       to perform the wizard tasks.

                       Select Finish.

     The New Media Wizard finishes. The media are added to the list of media in the
     details pane of the Deployment Workbench. The media_path\Content\Deploy
     folder is created (where media_path is the name of the media path you specified in
     the wizard), and some base folders are created. The folders and content you
     specified in the selection profile are copied to the Deploy folder when the Update
     Media Content Wizard runs.

Modify Existing Media in the Deployment Workbench

Modify existing media in the Media node in the Deployment Workbench using the
Properties actions as described in View Item Properties in the Deployment Workbench.
Configure media in the Deployment Workbench by performing the following steps in
the media Properties dialog box:

<!-- p.200 -->

     Configure properties on the General tab as described in Configure the Media
     Properties General Tab.

     Configure properties on the Rules tab as described in Configure the Media
     Properties Rules Tab.

     Configure the settings on the Windows PE x86 Settings tab as described in
     Configure the Media Properties Windows PE x86 Settings Tab.

     Configure the settings on the Windows PE x86 Components tab as described in
     Configure the Media Properties Windows PE x86 Components Tab.

     Configure the settings on the Windows PE x64 Settings tab as described in
     Configure the Media Properties Windows PE x64 Settings Tab.

     Configure the settings on the Windows PE x64 Components tab as described in
     Configure the Media Properties Windows PE x64 Components Tab.

Configure the Media Properties General Tab

The media properties on the General tab are configured when you run the New Media
Wizard. However, you can update the linked deployment share properties on the
General tab of the media Properties dialog box (where media is the name of the media
in the Deployment Workbench).

To modify existing media properties on the General tab

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Advanced Configuration/Media
     (where deployment_share is the name of the deployment share in which you will
     configure the media).

  3. In the details pane, select media (where media is the name of the media you want
     to configure).

  4. In the Actions pane, select Properties.

     The media Properties dialog box opens (where media is the name of the media
     you want to configure).
