---
title: "OS deployment documentation — pages 321-360"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0321-0360
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0321-0360
family: sccm
documentKind: "doc"
abstract: "12. On the Select Driver Package page, select additional driver packages to add to the prestaged media file. 13. On the Distribution Points page, select one or more distribution points from which to get content. Configuration Manager only displays distribution points that have t"
---

# OS deployment documentation — pages 321-360

<!-- p.321 -->

 12. On the Select Driver Package page, select additional driver packages to add to the
     prestaged media file.

 13. On the Distribution Points page, select one or more distribution points from which to get
     content.

     Configuration Manager only displays distribution points that have the content. Distribute
     all of the content associated with the task sequence to at least one distribution point
     before you continue. After you distribute the content, refresh the distribution point list.
     Remove any distribution points that you already selected on this page, go to the previous
     page, and then back to the Distribution Points page. Alternatively, restart the wizard. For
     more information, see Distribute referenced content and Manage content and content
     infrastructure.

 14. On the Customization page, specify the following options:

          Add any variables that the task sequence uses.

          Enable prestart command: Specify any prestart commands that you want to run
          before the task sequence runs. Prestart commands are a script or an executable that
          can interact with the user in Windows PE before the task sequence runs. For more
          information, see Prestart commands for task sequence media.

              Tip

             During media creation, the task sequence writes the package ID and prestart
             command-line, including the value for any task sequence variables, to the
             CreateTSMedia.log file on the computer that runs the Configuration Manager
             console. You can review this log file to verify the value for the task sequence
             variables.

          If the prestart command requires any content, select the option to Include files for
          the prestart command.

 15. Complete the wizard.

Next steps
Create an image for an OEM in factory or a local depot

<!-- p.322 -->

Create bootable media
07/17/2025

Applies to: Configuration Manager (current branch)

Bootable media in Configuration Manager contains the boot image, optional prestart
commands and associated files, and Configuration Manager files. Use bootable media for the
following OS deployment scenarios:

     Install a new version of Windows on a new computer (bare metal)

     Replace an existing computer and transfer settings

Usage
The following process occurs when you boot to bootable media:

   1. The destination computer starts

   2. It connects to the network

   3. It retrieves the following content from the site:

             The specified task sequence

             OS image

             Any other required content

Because the task sequence isn't on the media, you can change the task sequence or content
without having to recreate the media.

The packages on bootable media aren't encrypted. To make sure that the package contents are
secured from unauthorized users, take appropriate security measures. For example, add a
password to the media.

Starting in version 2006, bootable media can download cloud-based content. The device still
needs an intranet connection to the management point. It can get content from a content-
enabled cloud management gateway (CMG). For more information, see Bootable media
support for cloud-based content.

Prerequisites

<!-- p.323 -->

Before you create bootable media by using the Create Task Sequence Media Wizard, be sure
that all of these conditions are met.

Boot image
Consider the following points about the boot image that you use in the task sequence to
deploy the OS:

      The architecture of the boot image must be appropriate for the architecture of the
      destination computer. For example, an x64 destination computer can boot and run an x86
      or x64 boot image. However, an x86 destination computer can boot and run only an x86
      boot image.
      Make sure that the boot image contains the network and storage drivers that are required
      to provision the destination computer.

Create a task sequence to deploy an OS
As part of the bootable media, specify the task sequence to deploy the OS. For more
information, see Create a task sequence to install an OS.

Distribute all content associated with the task sequence
Distribute all content that the task sequence requires to at least one distribution point. This
content includes the boot image and other associated prestart files. The wizard gathers the
content from the distribution point when it creates the bootable media.

Your user account needs at least Read access rights to the content library on that distribution
point. For more information, see Distribute content.

Prepare the removable USB drive
If you're using a removable USB drive, connect it to the computer where you run the Create
Task Sequence Media wizard. The USB drive must be detectable by Windows as a removal
device. The wizard writes directly to the USB drive when it creates the media.

Create an output folder
Before you run the Create Task Sequence Media Wizard to create media for a CD or DVD set,
create a folder for the output files it creates. Media that it creates for a CD or DVD set is written
as an .ISO file directly in the folder.

<!-- p.324 -->

Process

 ７ Note

 For PKI environments, since you specify the root certificate authority (CA) at the primary
 site, make sure to create the bootable media at the primary site. The central
 administration site (CAS) doesn't have the root CA information to properly create the
 bootable media. For more technical information on this issue, see Sending with winhttp
 failed 80072f8f error in Smsts.log during OS deployment by using bootable or
 prestaged media.

 1. In the Configuration Manager console, go to the Software Library workspace, expand
    Operating Systems, and select the Task Sequences node.

 2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence Media.
    This action starts the Create Task Sequence Media Wizard.

 3. On the Select Media Type page, specify the following options:

          Select Bootable media.

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

 5. On the Media Type page, specify whether the media is a Removable USB drive or a
    CD/DVD set. Then configure the following options:

      ） Important

<!-- p.325 -->

Media uses a FAT32 file system. You can't create media on a USB drive whose content
contains a file over 4 GB in size.

   If you select Removable USB drive, select the drive where you want to store the
   content.
      Format removable USB drive (FAT32) and make bootable: By default, let
      Configuration Manager prepare the USB drive. Many newer UEFI devices require
      a bootable FAT32 partition. However, this format also limits the size of files and
      overall capacity of the drive. If the removable drive is already formatted and
      configured, disable this option.

   If you select CD/DVD set, specify the capacity of the media (Media size) and the
   name and path of the output file (Media file). The wizard writes the output files to
   this location. For example: \\servername\folder\outputfile.iso

   If the capacity of the media is too small to store the entire content, it creates
   multiple files. Then you need to store the content on multiple CDs or DVDs. When it
   requires multiple media files, Configuration Manager adds a sequence number to
   the name of each output file that it creates.

     ） Important

     If you select an existing .iso image, the Task Sequence Media Wizard deletes
     that image from the drive or share as soon as you proceed to the next page of
     the wizard. The existing image is deleted, even if you then cancel the wizard.

   Staging folder: The media creation process can require much temporary drive
   space. By default this location is similar to the following path:
   %UserProfile%\AppData\Local\Temp . To give you greater flexibility with where to store

   these temporary files, you can change this value to another drive and path.

   Media label: Add a label to task sequence media. This label helps you better identify
   the media after you create it. The default value is Configuration Manager . This text
   field appears in the following locations:

      If you mount an ISO file, Windows displays this label as the name of the mounted
      drive.

      If you format a USB drive, it uses the first 11 characters of the label as its name.

      Configuration Manager writes a text file called MediaLabel.txt to the root of the
      media. By default, the file includes a single line of text: label=Configuration

<!-- p.326 -->

          Manager . If you customize the label for media, this line uses your custom label

          instead of the default value.

       Include autorun.inf file on media: Configuration Manager doesn't add an
       autorun.inf file by default. Anti-malware products commonly block this file. For more
       information on the AutoRun feature of Windows, see Creating an AutoRun-enabled
       CD-ROM Application. If still necessary for your scenario, select this option to include
       the file.

6. On the Security page, specify the following options:

       Enable unknown computer support: Allow the media to deploy an OS to a
       computer that Configuration Manager doesn't manage. There's no record of these
       computers in the Configuration Manager database. For more information, see
       Prepare for unknown computer deployments.

       Protect media with a password: Enter a strong password to help protect the media
       from unauthorized access. When you specify a password, the user must provide that
       password to use the bootable media.

          ） Important

          As a security best practice, always assign a password to help protect the
          bootable media. Assigning a password to the media:
             Prevents someone without the password from running a task sequence
             when using the media
             Properly encrypts the task sequence environment on the media. The task
             sequence environment includes the task sequence steps and their variables.

          Using a password doesn't encrypt the remaining content of the bootable media
          such as packages. Don't include any sensitive information in task sequence
          packages such as scripts. Store and implement all sensitive information by
          using task sequence variables.

       For HTTP communications, select Create self-signed media certificate. Then specify
       the start and expiration date for the certificate.

          ７ Note

          If you select this option, you can't select any HTTPS management point on the
          Boot image page of this wizard.

<!-- p.327 -->

       For HTTPS communications, select Import PKI certificate. Then specify the
       certificate to import and its password.

       For more information about this client certificate that boot images use, see PKI
       certificate requirements.

       User device affinity: To support user-centric management in Configuration
       Manager, specify how you want the media to associate users with the destination
       computer. For more information about how OS deployment supports user device
       affinity, see Associate users with a destination computer.

          Allow user device affinity with auto-approval: The media automatically
          associates users with the destination computer. This functionality is based on the
          actions of the task sequence that deploys the OS. In this scenario, the task
          sequence creates a relationship between the specified users and destination
          computer when it deploys the OS to the destination computer.

          Allow user device affinity pending administrator approval: The media associates
          users with the destination computer after approval is granted. This functionality is
          based on the scope of the task sequence that deploys the OS. In this scenario,
          the task sequence creates a relationship between the specified users and the
          destination computer. It then waits for approval from an administrative user
          before it deploys the OS.

          Do not allow user device affinity: The media doesn't associate users with the
          destination computer. In this scenario, the task sequence doesn't associate users
          with the destination computer when it deploys the OS.

          ７ Note

          When setting the *SMSTSAssignUsersMode variable during a task sequence, the
          value specified needs to match what is configured on the PXE enabled DP, boot
          media, or pre-staged media being used for imaging.

          If the values don't match, then device affinity isn't set.

          For more information, see Task sequence variables.

7. On the Boot image page, specify the following options:

    ） Important

<!-- p.328 -->

    The architecture of the boot image that you distribute must be appropriate for the
    architecture of the destination computer. For example, an x64 destination computer
    can boot and run an x86 or x64 boot image. However, an x86 destination computer
    can only boot and run an x86 boot image.

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

          When you specify a PKI certificate on the Security page of this wizard, this page
          only displays HTTPS-enabled management points.

8. On the Customization page, specify the following options:

       Add any variables that the task sequence uses.

       Enable prestart command: Specify any prestart commands that you want to run
       before the task sequence runs. Prestart commands are a script or an executable that
       can interact with the user in Windows PE before the task sequence runs. For more
       information, see Prestart commands for task sequence media.

           Tip

          During media creation, the task sequence writes the package ID and prestart
          command-line, including the value for any task sequence variables, to the
          CreateTSMedia.log file on the computer that runs the Configuration Manager

<!-- p.329 -->

              console. You can review this log file to verify the value for the task sequence
              variables.

          If the prestart command requires any content, select the option to Include files for
          the prestart command.

  9. Complete the wizard.

Alternate method
You can create bootable media on a removable USB drive when the drive isn't connected to the
computer running the Configuration Manager console.

  1. Create the task sequence boot media. On the Media type page, select CD/DVD set. The
     wizard writes the output files to the location that you specify. For example:
     \\servername\folder\outputfile.iso .

  2. Prepare the removable USB drive. The drive must be formatted, empty, and bootable.

  3. Mount the ISO from the share location and transfer the files from the ISO to the USB
     drive.

Next steps
Use bootable media to deploy Windows over the network

<!-- p.330 -->

Create capture media
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Capture media in Configuration Manager allows you to capture an OS image from a
reference computer. Capture media contains the boot image that starts the reference
computer and the task sequence that captures the OS image. Use capture media for the
scenario to Create a task sequence to capture an OS.

Prerequisites
Before you create capture media by using the Create Task Sequence Media Wizard, be
sure that all of these conditions are met.

Boot image
Consider the following points about the boot image that you use in the task sequence
to deploy the OS:

      The architecture of the boot image must be appropriate for the architecture of the
      destination computer. For example, an x64 destination computer can boot and run
      an x86 or x64 boot image. However, an x86 destination computer can boot and
      run only an x86 boot image.
      Make sure that the boot image contains the network and storage drivers that are
      required to provision the destination computer.

Distribute all content associated with the task sequence
Distribute all content that the task sequence requires to at least one distribution point.
This content includes the boot image, OS image, and other associated files. The wizard
gathers the content from the distribution point when it creates the capture media.

Your user account needs at least Read access rights to the content library on that
distribution point. For more information, see Distribute content.

Prepare the removable USB drive
If you're using a removable USB drive, connect it to the computer where you run the
Create Task Sequence Media wizard. The USB drive must be detectable by Windows as a

<!-- p.331 -->

removal device. The wizard writes directly to the USB drive when it creates the media.

Create an output folder
Before you run the Create Task Sequence Media Wizard to create media for a CD or DVD
set, create a folder for the output files it creates. Media that it creates for a CD or DVD
set is written as an .ISO file directly in the folder.

Process
   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Operating Systems, and select the Task Sequences node.

   2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence
      Media. This action starts the Create Task Sequence Media Wizard.

   3. On the Select Media Type page, select Capture media.

   4. On the Media Type page, specify whether the media is a Removable USB drive or
      a CD/DVD set. Then configure the following options:

        ） Important

        Media uses a FAT32 file system. You can't create media on a USB drive whose
        content contains a file over 4 GB in size.

            If you select Removable USB drive, select the drive where you want to store
            the content.
               Format removable USB drive (FAT32) and make bootable: By default, let
               Configuration Manager prepare the USB drive. Many newer UEFI devices
               require a bootable FAT32 partition. However, this format also limits the
               size of files and overall capacity of the drive. If you've already formatted
               and configured the removable drive, disable this option.

            If you select CD/DVD set, specify the capacity of the media (Media size) and
            the name and path of the output file (Media file). The wizard writes the
            output files to this location. For example:
            \\servername\folder\outputfile.iso

            If the capacity of the media is too small to store the entire content, it creates
            multiple files. Then you need to store the content on multiple CDs or DVDs.

<!-- p.332 -->

       When it requires multiple media files, Configuration Manager adds a
       sequence number to the name of each output file that it creates.

          ） Important

          If you select an existing .iso image, the Task Sequence Media Wizard
          deletes that image from the drive or share as soon as you proceed to
          the next page of the wizard. The existing image is deleted, even if you
          then cancel the wizard.

       Staging folder: The media creation process can require a lot of temporary
       drive space. By default this location is similar to the following path:
        %UserProfile%\AppData\Local\Temp . Starting in version 1902, to give you

       greater flexibility with where to store these temporary files, change this value
       to another drive and path.

       Media label: Starting in version 1902, add a label to task sequence media.
       This label helps you better identify the media after you create it. The default
       value is Configuration Manager . This text field appears in the following
       locations:

          If you mount an ISO file, Windows displays this label as the name of the
          mounted drive

          If you format a USB drive, it uses the first 11 characters of the label as its
          name

          Configuration Manager writes a text file called MediaLabel.txt to the root
          of the media. By default, the file includes a single line of text:
          label=Configuration Manager . If you customize the label for media, this

          line uses your custom label instead of the default value.

       Include autorun.inf file on media: Starting in version 1906, Configuration
       Manager doesn't add an autorun.inf file by default. This file is commonly
       blocked by antimalware products. For more information on the AutoRun
       feature of Windows, see Creating an AutoRun-enabled CD-ROM Application.
       If still necessary for your scenario, select this option to include the file.

5. On the Boot image page, specify the following options:

    ） Important

<!-- p.333 -->

        The architecture of the boot image that you distribute must be appropriate
        for the architecture of the destination computer. For example, an x64
        destination computer can boot and run an x86 or x64 boot image. However,
        an x86 destination computer can boot and run only an x86 boot image.

           Boot image: Select the boot image to start the destination computer.

           Distribution point: Select the distribution point that has the boot image. The
           wizard retrieves the boot image from the distribution point and writes it to
           the media.

              ７ Note

              Your user account needs at least Read permissions to the content library
              on the distribution point.

   6. Complete the wizard.

Next steps
Create a task sequence to capture an OS

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.334 -->

Use the task sequence editor
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Edit task sequences in the Configuration Manager console by using the Task Sequence
Editor. Use the editor to:

      Open a read-only view of the task sequence

      Add or remove steps from the task sequence

      Change the order of the steps of the task sequence

      Add or remove groups of steps

      Copy and paste steps between task sequences

      Set step options like whether the task sequence continues when an error occurs

      Add conditions to the steps and groups of a task sequence

      Copy and paste conditions between steps in a task sequence

      Search the task sequence to quickly locate steps

Before you can edit a task sequence, you need to create it. For more information, see
Manage and create task sequences.

About the task sequence editor
The task sequence editor includes the following components:

<!-- p.335 -->

1. The name of the task sequence

2. Search. For more information, see Search.

3. Properties for the selected group or step in the sequence

  For more information about the properties and options of a specific step, see
  About task sequence steps.

4. Options for the selected group or step in the sequence

  For more information on general options on all steps, or options of a specific step,
  see About task sequence steps.

  For more information on how to configure conditions, see Conditions.

5. Add a group or steps

6. Remove a group or steps

7. Collapse all groups or expand all groups

8. Move the position of a group or step in the sequence (move up, move down)

9. The task sequence:

       See the order of steps and groups.
       Expand or collapse a group.

<!-- p.336 -->

           When you disable a step or group on its Options, it's greyed out in the
           sequence.
           A step's icon changes to a red error if there's an issue with the step. For
           example, a required value is missing.

 10. OK: Save and close

 11. Cancel: Close without saving changes

 12. Apply: Save changes and keep open

You can resize the task sequence editor using standard Windows controls. To resize the
widths of the two main panes, use the mouse to select the bar between the task
sequence and the step properties, and then drag it left or right.

  ７ Note

  Configuration Manager restricts actions for a task sequence that's greater than 2
  MB in size. For example, the task sequence editor will display an error if you try to
  save changes to a large task sequence. For more information, see Reduce the size
  of task sequence policy.

View a task sequence
   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Task Sequences node.

   2. In the Task Sequence list, select the task sequence that you want to view.

   3. On the Home tab of the ribbon, in the Task Sequence group, select View.

         Tip

        This action is the default. If you double-click a task sequence, you'll View the
        task sequence.

This action opens the task sequence editor in read-only mode. In this mode you can do
the following actions:

     View all groups, steps, properties, and options
     Expand and collapse groups
     Search the task sequence

<!-- p.337 -->

     Resize the editor window

In this read-only mode, you can't make any changes, including copying a step or
condition. This action also doesn't lock the task sequence for editing. For more
information on these locks, see Reclaim lock for editing task sequences.

To make changes to a task sequence, close the task sequence editor that you have open
in read-only mode. Then Edit the task sequence.

  ７ Note

  When you view or edit a task sequence that was created by the Create Task
  Sequence Wizard, the name of the step can be the action or type of the step. For
  example, you might see a step that has the name "Partition disk 0", which is the
  action for a step of type Format and Partition Disk. All task sequence steps are
  documented by their type, not necessarily by the name of the step that the editor
  displays.

Edit a task sequence
Use the following procedure to modify an existing task sequence:

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Task Sequences node.

   2. In the Task Sequence list, select the task sequence that you want to edit.

   3. On the Home tab of the ribbon, in the Task Sequence group, select Edit. Then do
     any of the following actions:

           Add a step: Select Add, select a category, and then select the step to add. For
           example, to add the Run Command Line step: select Add, choose the General
           category, and then select Run Command Line. This action adds the step after
           the currently selected step.

           Add a group: Select Add, and then choose New Group. After you add a
           group, then add steps to it.

           Change the order: Select the step or group that you want to reorder. Then
           use the Move Up or Move Down icons. You can move only one step or group
           at a time. These actions are also available when you right-click a group or
           step.

<!-- p.338 -->

             You can cut, copy, and paste a group or a step. Right-click the item and select
             the action. You can also use standard keyboard shortcuts for each action:
               Cut: CTRL + X
               Copy: CTRL + C
               Paste: CTRL + V

             Remove a step or group: Select the step or group, and choose Remove.

   4. Select OK to save your changes and close the window. Select Cancel to discard
     your changes and close the window. Select Apply to save your changes and keep
     the task sequence editor open.

For a list of the available task sequence steps, see Task sequence steps.

  ） Important

  If the task sequence has any unassociated references to an object as a result of the
  edit, the editor requires you fix the reference before it can close. Possible actions
  include:

        Correct the reference
        Delete the unreferenced object from the task sequence
        Temporarily disable the failed task sequence step until the broken reference is
        corrected or removed

You can open more than one instance of the task sequence editor at the same time. This
behavior lets you compare multiple task sequences, or copy and paste steps between
them. You can Edit one task sequence, and View another, but you can't do both actions
on the same task sequence.

Conditions
Use conditions to control how the task sequence behaves. Add conditions to a single
step or a group of steps. The task sequence evaluates the conditions before it runs the
step on the device. It only runs the step if the conditions evaluate true. If a condition
evaluates false, then the task sequence skips the group or step.

Use the Options tab to manage conditions:

<!-- p.339 -->

The following types of conditions are available:

     If statement: Use an if statement to group conditions. You can evaluate All
     conditions, Any condition, or None.

     Task Sequence Variable. Evaluate the current value of any built-in, action, custom,
     or read-only task sequence variable in the task sequence environment. For more
     information, see Step conditions.

       ７ Note

       You can use an array variable in this condition, but you have to specify the
       specific array member. For example, OSDAdapter0EnableDHCP specifies whether
       the first network adapter enables DHCP. For more information, see Array
       variables.

     Operating System Version: Evaluate the OS version of the device where the task
     sequence runs. This list is the general OS versions used throughout Configuration
     Manager. To evaluate a more detailed OS version, such as a specific version of
     Windows 10, use the Query WMI condition.

     Operating System Language: Evaluate the OS language of the device where the
     task sequence runs. This list includes the 257 languages that Windows supports.

     File Properties: Evaluate the existence, version, or timestamp of any file on the
     device where the task sequence runs.

     Folder Properties: Evaluate the existence or timestamp of any folder on the device
     where the task sequence runs.

     Registry Setting: Evaluate the existence or value of any registry key on the device
     where the task sequence runs.

<!-- p.340 -->

     Query WMI: Specify the namespace and query to evaluate on the device where the
     task sequence runs.

     Installed Software: Specify a Windows Installer (MSI) file to load product
     information to match on the device where the task sequence runs. You can match
     against a specific product or any version of the product.

Cmdlets for conditions
Manage conditions with the following PowerShell cmdlets:

     Get-CMTSStepConditionFile
     Get-CMTSStepConditionFolder
     Get-CMTSStepConditionIfStatement
     Get-CMTSStepConditionOperatingSystem
     Get-CMTSStepConditionQueryWmi
     Get-CMTSStepConditionRegistry
     Get-CMTSStepConditionSoftware
     Get-CMTSStepConditionVariable

Copy and paste conditions
To reuse conditions from one step to another, copy and paste conditions in the task
sequence editor. Select a condition to cut or copy it. If a condition has children, it copies
the entire block. If there's a condition on the clipboard, you can paste it with the
following options:

     Paste before
     Paste after
     Paste under (only applies to nested conditions)

Use standard keyboard shortcuts to copy (CTRL + C) and cut (CTRL + X). The standard
CTRL + V keyboard shortcut does the Paste after action.

There are also new options to move conditions up or down the list.

  ７ Note

  You can copy and paste conditions between steps in a task sequence. It doesn't
  support this action between different task sequences.

<!-- p.341 -->

Reclaim lock for editing
If the Configuration Manager console stops responding, you can be locked out of
making further changes until the lock expires after 30 minutes. This lock is part of the
Configuration Manager SEDO (Serialized Editing of Distributed Objects) system. For
more information, see Configuration Manager SEDO.

You can clear your lock on a task sequence. This action only applies to your user account
that has the lock, and on the same device from which the site granted the lock. When
you attempt to access a locked task sequence, you can now Discard Changes, and
continue editing the object. These changes would be lost anyway when the lock expired.

   Tip

  You can clear your lock on any object in the Configuration Manager console. For
  more information, see Using the Configuration Manager console.

Search
If you have a large task sequence with many groups and steps, it can be difficult to find
specific steps. To more quickly locate steps in the task sequence, search in the task
sequence editor.

<!-- p.342 -->

Enter a search term to start. You can scope your search using the following types:

     Step name
     Step description
     Step type
     Group name
     Group description
     Variable name
     Conditions
     Other content, for example, strings like variable values or command lines

It enables all scopes by default.

You can also filter for all steps with the following attributes:

     Continue on error
     Has conditions

It doesn't enable either filter by default.

<!-- p.343 -->

When you search, the editor window highlights in yellow the steps that match your
search criteria.

Quickly access these search fields and navigate the search results with the following
keyboard shortcuts:

     CTRL + F: enter a search string
     CTRL + O: select the search options to scope the results
     F3 or Enter: step forward through the results
     SHIFT + F3: step backwards through the results

See also
     Manage and create task sequences

     About task sequence steps

     How to use task sequence variables

     Using the Configuration Manager console

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.344 -->

User experiences for OS deployment
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you deploy a task sequence, depending upon the scenario there are different ways
for users to interact with the deployment. This article shows the main user experiences
with OS deployments, and how you can configure them:

      Software Center user notification for a high-impact deployment
      A sample PXE boot experience
      Task sequence wizard from media
      Progress window when the task sequence runs
      Error window when the task sequence fails

Software Center
For a high-impact deployment, you can customize the message that Software Center
displays. When the user opens the OS deployment in Software Center, they see a
message similar to the following window:

For more information on how to customize the message in this window, see Create a
custom notification.

You can also customize the organization name at the top of the window. (The above
example shows the default value, IT Organization ). Change the Organization name
client setting in the Computer Agent group. For more information, see About client
settings.

<!-- p.345 -->

For more information, see Use Software Center to deploy Windows over the network.

PXE
Different hardware models have different experiences for PXE. To boot to the network,
UEFI-based devices typically use the Enter key, and BIOS-based devices use the F12
key.

The following example shows the Hyper-V Gen1 (BIOS) PXE experience:

After the device successfully boots via PXE, it behaves similarly to bootable media. For
more information, see the next section on the Task sequence wizard.

For more information, see Use PXE to deploy Windows over the network.

  ２ Warning

  If you use PXE deployments, and configure device hardware with the network
  adapter as the first boot device, these devices can automatically start an OS
  deployment task sequence without user interaction. Deployment verification
  doesn't manage this configuration. While this configuration may simplify the
  process and reduce user interaction, it puts the device at greater risk for accidental
  reimage.

Task sequence wizard
When you use task sequence media, the task sequence wizard runs to guide the
process.

Welcome to the task sequence wizard

<!-- p.346 -->

     If you password-protect the media, the user has to enter the password on this
     welcome page.

     Select Configure Network Settings to specify a static IP address or other custom
     network settings. Otherwise, the device uses DHCP by default.

     If your network requires a proxy, select Configure Proxy Settings.

Select a task sequence to run
If you deploy more than one task sequence to the device, you see this page to select a
task sequence. Make sure to use a name and description for your task sequence that
users can understand.

<!-- p.347 -->

Edit task sequence variables
If any task sequence variables have empty values, the wizard shows a page to edit the
variable values.

Return to previous page on failure

<!-- p.348 -->

When you run a task sequence, and there's a failure, you can return to a previous page
of the task sequence wizard. In prior versions of Configuration Manager, you had to
restart the task sequence when there was a failure. Use the Previous button in the
following scenarios:

     When a computer starts in Windows PE, the task sequence bootstrap dialog might
     display before the task sequence is available. When you select Next in this
     scenario, the final page of the task sequence displays with a message that there
     are no task sequences available. Now, you can select Previous to search again for
     available task sequences. You can repeat this process until the task sequence is
     available.

     When you run a task sequence, but dependent content packages aren't available
     yet on distribution points, the task sequence fails. If the missing content wasn't
     distributed yet, distribute it now. Or wait for the content to be available on
     distribution points. Then select Previous to have the task sequence search again
     for the content.

Prestart commands
You can customize task sequence media or boot images to run a prestart command. A
prestart command runs before the task sequence starts. The following actions are some
of the more common ones:

     Prompt the user for dynamic values, like the computer name
     Specify network configuration
     Set user device affinity

The prestart command is a command line that you specify with a script or program. The
user experience is unique to that script or program.

For more information, see the following articles:

     Prestart commands for task sequence media
     Manage boot images
     Task sequence media

Task sequence progress
When the task sequence runs, it displays the Installation progress window:

<!-- p.349 -->

     This window is always on top; you can move it, but you can't close or minimize it.

     You can customize the organization name at the top of the window. (The above
     example shows the default value, IT Organization ). Change the Organization
     name client setting in the Computer Agent group. For more information, see
     About client settings.

        Tip

       The task sequence stores this value in the read-only variable
       _SMSTSOrgName.

     You can customize the subheading. (The above example shows the default value,
     Running: <task sequence name> .) On the properties of the task sequence, select the

     option to Use custom text for the progress notification text. It allows a maximum
     of 255 characters.

     Running action: The first line shows the name of the current task sequence step.
     The progress bar below it shows the overall completion of the task sequence.

     The second line only shows for some steps that provide more detailed progress.

     Use the task sequence variable TSDisableProgressUI to control when the task
     sequence displays progress.

     To completely disable the progress window, disable the option to Show Task
     Sequence progress on the User Experience page of the task sequence
     deployment.

The task sequence progress window includes the following information:

     Shows the current step number, total number of steps, and percent completion

<!-- p.350 -->

     Increased the width of the window to give you more space to better show the
     organization name in a single line

By default, the task sequence progress window uses the existing text. If you make no
changes, it continues to work the same as in earlier versions. To show the progress
information, specify the task sequence variable, TSProgressInfoLevel.

The count and percentage completed are intended for general guidance purposes only.
These values are based on the total number of steps in the task sequence. For a more
complex task sequence with steps that run conditionally based on task sequence logic,
the progress may be non-linear.

The count of total steps doesn't include the following items in the task sequence:

     Groups. This item is a container for other steps, not a step itself.

     Instances of the Run task sequence step. This step is a container for other steps.

     Steps that you explicitly disable. A disabled step doesn't run during the task
     sequence.

     It doesn't count enabled steps in a disabled group.

Task sequence error
If the task sequence fails, it displays the Task Sequence Error window.

<!-- p.351 -->

     You customize the header information the same as the task sequence progress
     window.

     It displays the name of the task sequence, an error code, and a general message
     for users. For example: Task sequence: Upgrade to Windows 10 Enterprise has
     failed with the error code (0x80004005). For more information, contact your

     system administrator or helpdesk operator.

     The window automatically closes after a timeout period. By default, this timeout is
     15 minutes. You can customize this value with the task sequence variable
     SMSTSErrorDialogTimeout.

Starting in version 2103, if the task sequence fails because the client doesn't meet the
requirements configured in the Check readiness step, the user can now see more details
about the failed prerequisites. They still see the common "task sequence error" message,
but can then select an option to Inspect. This action shows the checks that failed on the
device.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.352 -->

Task sequence steps
Article • 04/30/2024

Applies to: Configuration Manager (current branch)

The following task sequence steps can be added to a Configuration Manager task
sequence. For more information, see Use the task sequence editor.

Common settings
The following settings are common to all task sequence steps:

Properties for all steps
      Name: The task sequence editor requires that you specify a short name to describe
      this step. When you add a new step, the task sequence editor sets the name to the
      Type by default. The Name length can't exceed 50 characters.

      Description: Optionally, specify more detailed information about this step. The
      Description length can't exceed 256 characters.

The rest of this article describes the other settings on the Properties tab for each task
sequence step.

Options for all steps
      Disable this step: The task sequence skips this step when it runs on a computer.
      The icon for this step is greyed out in the task sequence editor.

      Continue on error: If an error occurs while running the step, the task sequence
      continues. For more information, see Planning considerations for automating tasks.

      Add Condition: The task sequence evaluates these conditional statements to
      determine if it runs the step. For an example of using a task sequence variable as a
      condition, see How to use task sequence variables. For more information about
      conditions, see Task sequence editor - Conditions.

The sections below for specific task sequence steps describe other possible settings on
the Options tab.

Apply Data Image

<!-- p.353 -->

Use this step to copy the data image to the specified destination partition.

This step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Images, and select Apply
Data Image.

Variables for Apply Data Image
Use the following task sequence variables with this step:

     OSDDataImageIndex
     OSDWipeDestinationPartition

Cmdlets for Apply Data Image
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepApplyDataImage
     New-CMTSStepApplyDataImage
     Remove-CMTSStepApplyDataImage
     Set-CMTSStepApplyDataImage

Properties for Apply Data Image
On the Properties tab for this step, configure the settings described in this section.

Image Package

Select Browse to specify the Image Package used by this task sequence. Select the
package you want to install in the Select a Package dialog box. The bottom of the
dialog box displays the associated property information for each existing image
package. Use the drop-down list to select the Image you want to install from the
selected Image Package.

  ７ Note

  This task sequence action treats the image as a data file. This action doesn't do any
  setup to boot the image as an OS.

Destination

<!-- p.354 -->

Configure one of the following options:

     Next available partition: Use the next sequential partition that an Apply Operating
     System or Apply Data Image step in this task sequence has not already targeted.

     Specific disk and partition: Select the Disk number (starting with 0) and the
     Partition number (starting with 1).

     Specific logical drive letter: Specify the Drive Letter that Windows PE assigns to
     the partition. This drive letter can be different from the drive letter assigned by the
     newly deployed OS.

     Logical drive letter stored in a variable: Specify the task sequence variable that
     contains the drive letter assigned to the partition by Windows PE. This variable is
     typically set in the Advanced section of the Partition Properties dialog box for the
     Format and Partition Disk task sequence step.

Delete all content on the partition before applying the image

Specifies that the task sequence deletes all files on the target partition before installing
the image. By not deleting the content of the partition, this action can be used to apply
additional content to a previously targeted partition.

Apply Driver Package
Use this step to download all of the drivers in the driver package and install them on the
Windows OS.

The Apply Driver Package task sequence step makes all device drivers in a driver
package available for use by Windows. Add this step between the Apply Operating
System and Setup Windows and ConfigMgr steps to make the drivers in the package
available to Windows. The Apply Driver Package task sequence step is also useful with
stand-alone media deployment scenarios.

Put similar device drivers into a driver package, and distribute them to the appropriate
distribution points. For example, put all drivers from one manufacturer into a driver
package. Then distribute the package to distribution points where the associated
computers can access them.

The Apply Driver Package step is useful for stand-alone media. This step is also useful
to install a specific set of drivers. These types of drivers include devices that Windows
plug-and-play doesn't detect, such as network printers.

<!-- p.355 -->

This task sequence step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Drivers, and select Apply
Driver Package.

   Tip

  For an overview on drivers in Configuration Manager, see Use task sequences to
  install drivers.

  Use content pre-caching to download an applicable driver package before a user
  installs the task sequence. For more information, see Configure pre-cache content.

Variables for Apply Driver Package
Use the following task sequence variables with this step:

     OSDApplyDriverBootCriticalContentUniqueID
     OSDApplyDriverBootCriticalHardwareComponent
     OSDApplyDriverBootCriticalID
     OSDApplyDriverBootCriticalINFFile
     OSDInstallDriversAdditionalOptions

Cmdlets for Apply Driver Package
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepApplyDriverPackage
     New-CMTSStepApplyDriverPackage
     Remove-CMTSStepApplyDriverPackage
     Set-CMTSStepApplyDriverPackage

Properties for Apply Driver Package
On the Properties tab for this step, configure the settings described in this section.

Driver package
Specify the driver package that contains the needed device drivers. Select Browse to
launch the Select a Package dialog box. Select an existing driver package to apply. The
bottom of the dialog box displays the associated package properties.

<!-- p.356 -->

Install driver package via running DISM with recurse option
Select this option to add the /recurse parameter to the DISM command line when
Windows applies the driver package.

When you enable this option, you can also specify additional DISM command-line
parameters. Use the OSDInstallDriversAdditionalOptions task sequence variable to
include more options. For more information, see Windows DISM Command-Line
Options.

Select the mass storage driver within the package that needs to be
installed before setup on pre-Windows Vista operating systems
Specify any mass storage drivers needed to install a classic OS.

Driver

Select the mass storage driver file to install before setup of a classic OS. The drop-down
list populates from the specified package.

Model

Specify the boot-critical device that is needed for pre-Windows Vista OS deployments.

Do unattended installation of unsigned drivers on version of
Windows where this is allowed

This option allows Windows to install drivers without a digital signature.

Apply Network Settings
Use this step to specify the network or workgroup configuration information for the
destination computer. The task sequence stores these values in the appropriate answer
file. Windows Setup uses this answer file during the Setup Windows and ConfigMgr
action.

This task sequence step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Settings, and select
Apply Network Settings.

<!-- p.357 -->

  ７ Note

  If you include multiple instances of this step in a task sequence, conditions don't
  apply. The settings from the last instance of this step in the task sequence are
  applied to the device. To work around this behavior, include each step in a separate
  group with conditions on the group.

Variables for Apply Network Settings
Use the following task sequence variables with this step:

     OSDAdapter
     OSDAdapterCount
     OSDDNSDomain
     OSDDNSSuffixSearchOrder
     OSDDomainName
     OSDDomainOUName
     OSDEnableTCPIPFiltering
     OSDJoinAccount
     OSDJoinPassword
     OSDWorkgroupName

Cmdlets for Apply Network Settings
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepApplyNetworkSetting
     New-CMTSStepApplyNetworkSetting
     Remove-CMTSStepApplyNetworkSetting
     Set-CMTSStepApplyNetworkSetting
     New-CMTSNetworkAdapterSetting

Properties for Apply Network Settings
On the Properties tab for this step, configure the settings described in this section.

Join a workgroup

Select this option to have the destination computer join the specified workgroup. Enter
the name of the workgroup on the Workgroup line. The value that the Capture

<!-- p.358 -->

Network Settings task sequence step captures can override this value.

Join a domain
Select this option to have the destination computer join the specified domain. Specify or
browse to the domain, such as fabricam.com . Specify or browse to a Lightweight
Directory Access Protocol (LDAP) path for an organizational unit. For example:
LDAP//OU=computers, DC=Fabricam.com, C=com .

  ７ Note

  When a Microsoft Entra joined client runs an OS deployment task sequence, the
  client in the new OS won't automatically join Microsoft Entra ID. Even though it's
  not Microsoft Entra joined, the client is still managed.

Account
Select Set to specify an account with the necessary permissions to join the computer to
the domain. In the Windows User Account dialog box, enter the user name in the
following format: Domain\User . For more information, see Domain joining account.

Adapter settings

Specify network configurations for each network adapter in the computer. Select New to
open the Network Settings dialog box, and then specify the network settings.

     If you also use the Capture Network Settings step, the task sequence applies the
     previously captured settings to the network adapter.
     If the task sequence didn't previously capture network settings, it applies the
     settings you specify in this step.
     The task sequence applies these settings to network adapters in Windows device
     enumeration order.
     The task sequence doesn't immediately apply the settings you specify in this step
     to the computer.

Apply Operating System Image
Use this step to install an OS on the destination computer.

<!-- p.359 -->

After the Apply Operating System action runs, it sets the OSDTargetSystemDrive
variable to the drive letter of the partition containing the OS files.

This task sequence step runs only in Windows PE. It doesn't run in the full OS.

To add this step in the task sequence editor, select Add, select Images, and select Apply
Operating System Image.

   Tip

  Windows 11 and Windows 10 media include multiple editions. When you configure
  a task sequence to use an OS upgrade package or OS image, be sure to select a
  supported edition.

  Use content pre-caching to download an applicable OS upgrade package before a
  user installs the task sequence. For more information, see Configure pre-cache
  content.

  The Setup Windows and ConfigMgr step starts the installation of Windows.

Variables for Apply OS Image
Use the following task sequence variables with this step:

     OSDConfigFileName
     OSDImageIndex
     OsdLayeredDriver
     OSDTargetSystemDrive

Cmdlets for Apply OS Image
Manage this step with the following PowerShell cmdlets:

     Get-CMTSStepApplyOperatingSystem
     New-CMTSStepApplyOperatingSystem
     Remove-CMTSStepApplyOperatingSystem
     Set-CMTSStepApplyOperatingSystem

Behaviors for Apply OS Image
This step performs different actions depending on whether it uses an OS image or an
OS upgrade package.

<!-- p.360 -->

OS image actions
The Apply Operating System Image step performs the following actions when using an
OS image:

   1. Delete all content on the targeted volume, except files in the folder specified by
     the _SMSTSUserStatePath variable.

   2. Extract the contents of the specified .wim file to the specified destination partition.

   3. Prepare the answer file:

      a. Create a new default Windows Setup answer file (sysprep.inf or unattend.xml)
        for the deployed OS.

      b. Merge any values from the user-supplied answer file.

   4. Copy Windows boot loaders into the active partition.

   5. Set the boot.ini or the Boot Configuration Database (BCD) to reference the newly
     installed OS.

OS upgrade package actions
The Apply Operating System Image step performs the following actions when using an
OS upgrade package:

   1. Delete all content on the targeted volume, except files in the folder specified by
     the _SMSTSUserStatePath variable.

   2. Prepare the answer file:

      a. Create a fresh answer file with standard values created by Configuration
        Manager.

      b. Merge any values from the user-supplied answer file.

Properties for Apply OS Image
On the Properties tab for this step, configure the settings described in this section.

Apply operating system from a captured image

Installs an OS image that you captured. Select Browse to open the Select a package
dialog box. Then select the existing image package you want to install. If multiple
