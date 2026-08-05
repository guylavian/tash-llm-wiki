---
title: "OS deployment documentation — pages 201-240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0201-0240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0201-0240
family: sccm
documentKind: "doc"
abstract: "Was this page helpful?  Yes  No Provide product feedback Create a task sequence to capture an OS Article • 10/04/2022 Applies to: Configuration Manager (current branch) When you use a task sequence to deploy an OS to a computer in Configuration Manager, the computer installs t"
---

# OS deployment documentation — pages 201-240

<!-- p.201 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.202 -->

Create a task sequence to capture an OS
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you use a task sequence to deploy an OS to a computer in Configuration
Manager, the computer installs the OS image that you specify in the task sequence. You
can customize the OS image so it includes specific applications and software updates.
First use a build and capture task sequence to build a reference computer. Then capture
the OS image from that reference computer. If you already have a reference computer
available to capture, create a custom task sequence to capture the OS.

  ７ Note

  To avoid potential hardware driver issues when deploying custom reference images
  to different model devices, it is recommended to create custom reference images
  using virtual machines (VMs). This minimizes the amount of potentially conflicting
  drivers that are included as part of the custom reference image. Additionally it is
  recommended not to add any drivers to the custom reference image via either the
  Auto Apply Drivers task or the Apply Driver Package task.

About the build and capture task sequence
The build and capture task sequence:

      Partitions and formats the reference computer
      Installs the OS
      Installs the Configuration Manager client
      Installs applications
      Applies software updates
      Captures the OS from the reference computer

The packages associated with the task sequence, such as applications, must be available
on distribution points before you deploy the build and capture task sequence.

Requirements
Before you create a task sequence to install an OS, make sure the following components
are in place:

<!-- p.203 -->

Required
     Boot image

     OS image

Required (if used)
     Driver packages that contain the necessary Windows drivers to support hardware
     on the reference computer. For more information about the task sequence steps to
     manage drivers, see Use task sequences to install device drivers.

     Software updates

     Applications

Create a build and capture task sequence
Use the following procedure to use a task sequence to build a reference computer and
capture the OS.

  1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Task Sequences node.

  2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence
     to start the Create Task Sequence Wizard.

  3. On the Create a New Task Sequence page, select Build and capture a reference
     operating system image.

  4. On the Task Sequence Information page, specify the following settings:

          Task sequence name: Specify a name that identifies the task sequence.

          Description: Specify an optional description for the task sequence. For
          example, describe the OS that the task sequence creates.

          Boot image: Specify the boot image to use with this task sequence.

            ） Important

            The architecture of the boot image must be compatible with the
            hardware architecture of the destination computer.

<!-- p.204 -->

5. On the Install Windows page, specify the following settings:

       Image package: Specify the OS image package, which contains the required
       files to install the OS.

       Image index: Specify the index of the OS to install in the image. If the OS
       image contains multiple versions, select the version that you want to install.

       Product key: If necessary, specify the product key for the Windows OS to
       install. You can specify encoded volume license keys and standard product
       keys. If you use a non-encoded product key, separate each group of five
       characters with a dash ( - ). For example: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX

       Server licensing mode: If necessary, specify that the server license is Per seat,
       Per server, or that no license is specified. If the server license is Per server,
       also specify the maximum number of server connections.

       Specify how to configure the administrator account for the deployed OS:

          Randomly generate the local administrator password and disable the
          account on all supported platforms: Create a random password for the
          local administrator account. Disable the account when the Windows is set
          up.

          Enable the account and specify the local administrator password: Use the
          same password for the local administrator account on all computers where
          you deploy this OS.

6. On the Configure Network page, specify the following settings:

       Join a workgroup: Specify whether to add the destination computer to a
       workgroup when the OS is deployed.

       Join a domain: Specify whether to add the destination computer to a domain
       when the OS is deployed. In Domain, specify the name of the domain.

          ） Important

          You can browse to locate domains in the local forest. Specify the domain
          name for a remote forest.

       You can also specify an organizational unit (OU). This setting is optional, and
       specifies the LDAP X.500 distinguished name of the OU in which to create the
       computer account, if it doesn't already exist.

<!-- p.205 -->

         Account: Specify the user name and password for the account that has
         permissions to join the specified domain. For example: domain\user or
         %variable% .

           ） Important

           If you plan to migrate either the domain settings or the workgroup
           settings during the deployment, make sure you enter the appropriate
           domain credentials here.

 7. On the Install Configuration Manager page, specify the Configuration Manager
   client package. This package contains the source files to install the Configuration
   Manager client. Also specify any additional properties needed to install the client.

   For more information, see About client installation properties.

 8. On the Include Updates page, specify whether to install required software updates,
   all software updates, or no software updates. If you specify to install software
   updates, Configuration Manager installs only those software updates that are
   targeted to the collections that the destination computer is a member of.

 9. On the Install Applications page, specify the applications to install on the
   destination computer. If you specify multiple applications, you can also specify that
   the task sequence continues if the installation of a specific application fails.

     ７ Note

     The System Preparation page appears next in the wizard, but it's no longer
     used. Select Next to continue.

10. On the Images Properties page, specify the following settings for the OS image:

         Created by: Specify the name of the user to note as the creator of the OS
         image.

         Version: Specify your version number that's associated with the OS image.
         This attribute doesn't need to be the OS version, as the site stores that value
         separately.

         Description: Specify your description of the OS image.

11. On the Capture Image page, specify the following settings:

<!-- p.206 -->

            Path: Specify a shared network folder where Configuration Manager should
            store the output image file (.wim). This file contains the OS image that's
            based on the settings you specify in this wizard. If you specify a folder that
            contains an existing .WIM file, it's overwritten.

            Account: Specify the Windows account that has permissions to the network
            share where the image is stored.

 12. Complete the wizard.

To add additional steps to the task sequence, select it, and choose Edit. For more
information about how to edit a task sequence, see Use the task sequence editor.

Deploy the task sequence to a reference computer in one of the following ways:

     If the reference computer is already a Configuration Manager client, deploy the
     build and capture task sequence to a collection that contains the reference
     computer. For more information, see Deploy a task sequence.

     If the reference computer isn't a Configuration Manager client, or if you want to
     manually run the task sequence on the reference computer, use the Create Task
     Sequence Media Wizard to create bootable media. For more information, see
     Create bootable media.

After you capture the image, you can deploy it to other computers. For more
information about how to deploy the captured OS image, see Create a task sequence to
install an OS.

Capture from an existing reference computer
When you already have a reference computer ready to capture, create a task sequence
that only captures the OS from the reference computer. Use the Capture Operating
System Image task sequence step to capture one or more images from a reference
computer and store them in an image file (.wim) on the specified network share. Start
the reference computer in Windows PE with a boot image. The task sequence captures
each hard drive on the reference computer as a separate image within the .wim file. If
the referenced computer has multiple drives, the resulting .wim file contains a separate
image for each volume. It only captures volumes that are formatted as NTFS or FAT32. It
skips volumes with other formats or USB volumes.

Use the following procedure to capture an OS image from an existing reference
computer:

<!-- p.207 -->

 1. In the Configuration Manager console, go to the Software Library workspace,
   expand Operating Systems, and then select the Task Sequences node.

 2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence.
   This action starts the Create Task Sequence Wizard.

 3. On the Create a New Task Sequence page, select Create a new custom task
   sequence.

 4. On the Task Sequence Information page, specify a name for the task sequence.
   Optionally add a description for the task sequence.

 5. Specify a boot image for the task sequence. Configuration Manager uses this boot
   image to start the reference computer with Windows PE. For more information, see
   Manage boot images.

 6. Complete the wizard.

 7. In the Task Sequences node, select the new task sequence. Then on the Home tab
   of the ribbon, in the Task Sequence group, select Edit. This action opens the task
   sequence editor.

 8. If the Configuration Manager client is installed on the reference computer:

   Go to the Add menu, select Images, and then choose Prepare ConfigMgr Client for
   Capture. This step generalizes the Configuration Manager client on the reference
   computer.

     ７ Note

     The task sequence doesn't support uninstalling the Configuration Manager
     client.

 9. Go to the Add menu, select Images, and choose Prepare Windows for Capture.
   This step runs Sysprep, and then restarts the computer to the Windows PE boot
   image specified for the task sequence. For this action to complete successfully,
   don't join the reference computer to a domain.

10. Go to the Add menu, select Images, and choose Capture Operating System Image.
   This step only runs from Windows PE to capture the hard drives on the reference
   computer. Configure the following settings:

        Name and Description: Optionally, you can change the name of the task
        sequence step and provide a description.

<!-- p.208 -->

           Destination: Specify a shared network folder where the output .WIM file is
           stored. This file contains the OS image based on the settings that you specify
           by using this wizard. If you specify a folder that contains an existing .WIM file,
           it's overwritten.

           Description, Version, and Created by: Optionally, provide details about the
           image to capture.

           Capture operating system image account: Specify the Windows account that
           has permissions to the network share you specified. Select Set to specify the
           name of that Windows account.

Select OK to save your changes and close the task sequence editor.

Deploy the task sequence to a reference computer in one of the following ways:

     If the reference computer is already a Configuration Manager client, deploy the
     capture task sequence to a collection that contains the reference computer. For
     more information, see Deploy a task sequence.

     If the reference computer isn't a Configuration Manager client, or if you want to
     manually run the task sequence on the reference computer, use the Create Task
     Sequence Media Wizard to create capture media. For more information, see
     Create capture media.

After you capture the image, you can deploy it to other computers. For more
information about how to deploy the captured OS image, see Create a task sequence to
install an OS.

Example task sequence
Use the following table as a guide as you create a task sequence that builds and
captures an OS image. The table helps you decide the general sequence for your task
sequence steps, and how to organize and structure those steps into logical groups. The
task sequence that you create may vary from this sample. It can contain more or less
steps and groups.

  ７ Note

  Always use the Create Task Sequence Wizard to create this type of task sequence.

  The wizard adds steps to the task sequence with slightly different names that what
  you'd see if you manually add the same steps.

<!-- p.209 -->

Group: Build the Reference Machine
This group contains the actions necessary to build a reference computer.

                                                                                 ﾉ   Expand table

 Task sequence step   Description

 Restart in Windows   Restart the destination computer to the boot image assigned to the task
 PE                   sequence. This step displays a message to the user that the computer will
                      be restarted so that the installation can continue.

                      This step uses the read-only _SMSTSInWinPE task sequence variable. If the
                      associated value equals false , then the task sequence step continues.

 Partition Disk 0 -   Partition and format the hard drive on the destination computer in BIOS
 BIOS                 mode. The default disk number is 0 .

                      This step uses several read-only task sequence variables. For example, it
                      only runs if the Configuration Manager client cache doesn't exist, and
                      doesn't run if the computer is configured for UEFI.

 Partition Disk 0 -   Partition and format the hard drive on the destination computer in UEFI
 UEFI                 mode. The default disk number is 0 .

                      This step uses several read-only task sequence variables. For example, it
                      only runs if the Configuration Manager client cache doesn't exist, and only
                      runs if the computer is configured for UEFI.

 Apply Operating      Install the specified OS image on the destination computer. This step first
 System               deletes all files on the volume, other than Configuration Manager-specific
                      control files. It then applies all volume images contained in the WIM file to
                      the corresponding sequential disk volume on the target computer.

 Apply Windows        Configure the Windows settings for the destination computer.
 Settings

 Apply Network        Specify the network or workgroup configuration information for the
 Settings             destination computer.

 Apply Device         Match and install drivers as part of this OS deployment. For more
 Drivers              information, see Auto Apply Drivers.

                      This step uses the read-only _SMSTSMediaType task sequence variable. If the
                      associated value doesn't equal FullMedia , this step doesn't run.

 Setup Windows        Install the Configuration Manager client software. Configuration Manager
 and Configuration    installs and registers the Configuration Manager client GUID. Include any
 Manager              necessary Installation properties.

<!-- p.210 -->

 Task sequence step      Description

 Install Updates         Specify how software updates are installed on the destination computer.
                         The destination computer isn't evaluated for applicable software updates
                         until this step runs. At that point, the evaluation is similar to any other
                         Configuration Manager-managed client. For more information, see Install
                         Software Updates.

                         This step uses the read-only _SMSTSMediaType task sequence variable. If the
                         associated value doesn't equal FullMedia , this step doesn't run.

 Install Applications    Specifies any applications to install on the reference computer.

Group: Capture the Reference Machine
This group contains the necessary steps to prepare and capture a reference computer.

                                                                                   ﾉ   Expand table

 Task sequence step           Description

 Prepare Configuration        Generalize the Configuration Manager client on the reference
 Manager Client               computer.

 Prepare OS                   Runs Sysprep to generalize Windows. It then restarts the computer
                              into the Windows PE boot image specified for the task sequence.

 Capture the Reference        Captures the image to the specified network share and .WIM file.
 Machine

  ） Important

  After you capture an image from a reference computer, don't capture another OS
  image from the reference computer. Registry entries are created during the initial
  configuration. Create a new reference computer each time that you capture the OS
  image. If you plan to use the same reference computer to create future OS images,
  first uninstall and reinstall the Configuration Manager client.

Next steps
Methods to deploy enterprise operating systems

<!-- p.211 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.212 -->

Create a task sequence to capture and
restore user state in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use Configuration Manager task sequences to capture and restore the user state data in
OS deployment scenarios. In these scenarios, you want to retain the user state of the
current OS. Depending on the type of task sequence you create, the capture and restore
steps might be automatically added as part of the task sequence. In other scenarios, you
might need to manually add the capture and restore steps to the task sequence. This
article provides the steps that you must add to an existing task sequence to capture and
restore user state data.

Task sequence steps
To capture and restore the user state, add the following steps to the task sequence:

      Request State Store: If you store the user state on the state migration point, you
      need this step.

      Capture User State: This step captures the user state data. It then stores the data
      on either the state migration point or the local disk using hardlinks.

      Restore User State: This step restores the user state data on the destination
      computer. It can retrieve the data from a state migration point or if hardlinked on
      the local disk.

      Release State Store: If you store the user state on the state migration point, you
      need this step. This step removes the data from the state migration point.

Use the following procedures to add the task sequence steps needed to capture and
restore the user state. For more information about creating a task sequence, see
Manage task sequences to automate tasks.

Capture the user state
To add task sequence steps to capture the user state, use the following steps:

<!-- p.213 -->

   1. In the Task Sequence list, select a task sequence, and then click Edit.

   2. If you're using a state migration point to store the user state, add the Request
     State Store step to the task sequence. In the Task Sequence Editor, click Add. Point
     to User State, and then click Request State Store. Configure the properties and
     options for this step, and then click Apply. For more information about the
     available settings, see Request State Store.

   3. Add the Capture User State step to the task sequence. In the Task Sequence
     Editor, click Add. Point to User State, and then click Capture User State. Configure
     the properties and options for this step, and then click Apply. For more
     information about the available settings, see Capture User State.

       ） Important

       When you add this step to your task sequence, also set the
       OSDStateStorePath task sequence variable to specify where to store the user
       state data. If you store the user state locally, don't specify a root folder as that
       can cause the task sequence to fail. When you store the user data locally
       always use a folder or subfolder. For more information about this variable, see
       Task sequence variables.

   4. If you're using a state migration point, add the Release State Store step to the task
     sequence. In the Task Sequence Editor, click Add. Point to User State, and then
     click Release State Store. Configure the properties and options for this step, and
     then click Apply. For more information about the available settings, see Release
     State Store.

       ） Important

       The task sequence action that runs before the Release State Store step must
       be successful before the Release State Store step starts.

Deploy this task sequence to capture the user state on a destination computer. For
information about how to deploy task sequences, see Deploy a task sequence.

Restore the user state
To add task sequence steps to restore the user state, use the following steps:

   1. In the Task Sequence list, select a task sequence, and then click Edit.

<!-- p.214 -->

   2. Add the Restore User State step to the task sequence. In the Task Sequence
     Editor, click Add. Point to User State, and then click Restore User State. This step
     establishes a connection to the state migration point if necessary. Configure the
     properties and options for this step, and then click Apply. For more information
     about the available settings, see Restore User State.

       ） Important

       When you use the Capture User State step with the option to Capture all user
       profiles with standard options, you must select the Restore local computer
       user profiles setting in the Restore User State step. Otherwise the task
       sequence will fail.

       ７ Note

       If you store the user state by using local hardlinks and the restore isn't
       successful, you can manually delete the hardlinks that were created to store
       the data. The task sequence can run the USMTUtils tool to automate this
       action with a Run Command Line step. If you use USMTUtils to delete the
       hardlink, add a Restart Computer step after you run USMTUtils.

   3. If you're using a state migration point to store the user state, add the Release
     State Store step to the task sequence. In the Task Sequence Editor, click Add. Point
     to User State, and then click Release State Store. Configure the properties and
     options for this step, and then click Apply. For more information about the
     available settings, see Release State Store.

       ） Important

       The task sequence action that runs before the Release State Store step must
       be successful before the Release State Store step starts.

Deploy this task sequence to restore the user state on a destination computer. For
information about deploying task sequences, see Deploy a task sequence.

Next steps
Monitor the task sequence deployment

<!-- p.215 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.216 -->

Create a custom task sequence with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you create a custom task sequence in Configuration Manager, it contains no task
sequence steps. After you create the task sequence, edit it, and add the task sequence
steps you need.

Create a custom task sequence
Use the following procedure to create a custom task sequence:

   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Operating Systems, and then select the Task Sequences node.

   2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence.
      This action starts the Create Task Sequence Wizard.

   3. On the Create a New Task Sequence page, select Create a new custom task
      sequence.

   4. On the Task Sequence Information page, specify:

            A name for the task sequence
            A description of the task sequence
            An optional boot image for the task sequence to use

After you complete the Create Task Sequence Wizard, Configuration Manager adds the
custom task sequence to the Task Sequences node. You can now edit this task sequence
to add task sequence steps to it.

See also
For a list of available task sequence steps, see Task sequence steps.

For more information about how to edit a task sequence, see Use the task sequence
editor.

Most often you'll use task sequences to automate tasks for OS deployment, but you can
create a custom task sequence to automate different kinds of tasks. For more

<!-- p.217 -->

information, see Create a task sequence for non-OS deployments.

Starting in version 2002, install complex applications using task sequences via the
application model. Add a deployment type to an app that's a task sequence, either to
install or uninstall the app. For more information, see Create Windows applications.

Next steps
Deploy the task sequence

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.218 -->

Manage task sequences
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you create a task sequence, there are additional settings that you can configure.
Task sequences are located in the Configuration Manager console. In the Software
Library workspace, expand Operating Systems, and select Task Sequences. The Task
Sequences node, including subfolders that you create, is replicated throughout the
Configuration Manager hierarchy. For planning information, see Planning considerations
for automating tasks.

Edit
Modify a task sequence by adding or removing steps, adding or removing groups, or by
changing the order of the steps. For more information, see Use the task sequence
editor.

Properties
The task sequence editor configures the steps of the task sequence. There are additional
settings available on the Properties of the task sequence, which control other aspects of
how the task sequence runs and behaves.

In the Configuration Manager console, go to the Software Library workspace, expand
Operating Systems, and select Task Sequences. Select the task sequence to configure,
and then in the ribbon select Properties.

The following sections provide more details about each tab of the task sequence
properties.

General tab: Software Center properties
On the General tab, the following settings for Software Center are available:

Restart required
Lets the user know whether a restart is required during the installation.

<!-- p.219 -->

Download size (MB)
Specifies how many megabytes are displayed in Software Center for the task sequence.

Estimated run time (minutes)

Specifies the estimated run time in minutes that's displayed in Software Center for the
task sequence.

Advanced tab
On the Advanced tab, the following settings are available:

Run another program first

Select this option to run a program in another package before the task sequence runs.
By default, this option isn't enabled. You don't need to separately deploy the program
that you specify to run first.

  ） Important

  This setting applies only to task sequences that run in the full OS. If you start the
  task sequence by using PXE or boot media, Configuration Manager ignores this
  setting.

  It also doesn't apply to task sequences that run on clients that communicate via a
  cloud management gateway (CMG). This option uses the UNC network path of the
  package, which isn't accessible via CMG.

     Package: Browse for the package that contains the program to run before this task
     sequence.

     Program: Select the program to run before this task sequence.

        ７ Note

        If the selected program fails to run on a client, the task sequence doesn't run.
        If the selected program runs successfully, it doesn't run again, even if the task
        sequence is rerun on the same client.

<!-- p.220 -->

Suppress task sequence notifications
Select this option to hide the New Software is available toast notification. You still see
the New software icon from Software Center in the notification area. By default, this
option is disabled.

Disable this task sequence on computers where it is deployed

If you select this option, Configuration Manager temporarily disables all deployments
that contain this task sequence. It also removes the task sequence from the list of
deployments available to run. The task sequence doesn't run until you enable it. By
default, this option is disabled.

Maximum allowed run time

Specifies the maximum time in minutes that you expect the task sequence to run on the
destination computer. Use a whole number equal to or greater than zero. By default, this
value is 120 minutes.

  ） Important

  If you're using maintenance windows for the collection to which you deploy this
  task sequence, a conflict might occur if the Maximum allowed run time is longer
  than the scheduled maintenance window. If you set the maximum run time to 0,
  the task sequence starts during the maintenance window. It continues to run until it
  completes or fails after the maintenance window is closed. As a result, task
  sequences with a maximum run time set to 0 might run past the end of their
  maintenance windows. If you set the maximum run time to a specific period (non-
  zero) that exceeds the length of any available maintenance window, then that task
  sequence doesn't run. For more information, see How to use maintenance
  windows.

If you set the value as 0, Configuration Manager evaluates the maximum allowed run
time as 12 hours (720 minutes) for monitoring progress. However, the task sequence
starts as long as the countdown duration doesn't exceed the maintenance window
value.

  ７ Note

  When it reaches the maximum run time, if you don't allow users to interact with a
  required deployment, then Configuration Manager stops the task sequence. If the

<!-- p.221 -->

  task sequence itself isn't stopped, Configuration Manager stops monitoring the
  task sequence after it reaches the maximum allowed run time.

Use a boot image

Use the selected boot image when the task sequence is run. Select Browse to select a
different boot image. Clear this option to disable the use of the selected boot image
when the task sequence runs.

This task sequence can run on any platform

If you select this option, Configuration Manager doesn't check the platform type of the
destination computer when the task sequence runs. This option is selected by default.

This task sequence can only run on the specified client platforms

This option specifies the processors, OS versions, and service packs on which this task
sequence can run. When you select this option, select at least one platform from the list.
By default, no platforms are selected. Configuration Manager uses this information
when is evaluates which destination computers in a collection receive the deployed task
sequence.

  ７ Note

  When you run a task sequence from boot media or PXE, Configuration Manager
  ignores this option. The task sequence runs as though the option This program can
  run on any platform is selected.

User Notification tab for high-impact settings
Configure a task sequence as high-impact and customize the messages that users
receive when they run the task sequence. For more information, see High-impact task
sequence settings.

Any task sequence that meets certain conditions is automatically defined as high-
impact. For more general information, see Manage high-risk deployments.

More Options tab

<!-- p.222 -->

  ７ Note

  In version 2111 and earlier, this tab is named Performance.

To improve the overall speed of the task sequence, run it with the high-performance
power plan. It configures Windows to use its built-in high-performance power plan,
which delivers maximum performance at the expense of higher power consumption. For
more information, see Task sequence performance.

Custom icons for task sequences
Starting in version 2203, add custom icons for task sequences. These icons appear in
Software Center when you deploy the task sequence. Instead of a default icon, a custom
icon can improve the user experience to better identify the software.

On the More Options tab of task sequence properties, in the section for the icon, select
Browse. Select an icon from the default shell library, or browse to another file in a local
or network path.

     It supports the following file types:
        Programs ( .exe )
        Libraries ( .dll )
        Icons ( .ico )
        Images ( .png , .jpeg , .jpg )
     The file doesn't need to be on clients that you target with the deployment.
     Configuration Manager includes the image with the deployment policy.
     The maximum file size for an image is 256 KB.
     Icons can have pixel dimensions of up to 512 x 512.

When clients receive the deployment policy, they'll display the icon in Software Center.

  ７ Note

  To take full advantage of new Configuration Manager features, after you update the
  site, also update clients to the latest version. While new functionality appears in the
  Configuration Manager console when you update the site and console, the
  complete scenario isn't functional until the client version is also the latest.

Additional actions

<!-- p.223 -->

You can manage task sequences by using additional actions when you select a task
sequence.

Edit action
For more information, see Use the task sequence editor.

Enable
Enables the task sequence so that clients can run it. You don't need to redeploy a task
sequence after it's enabled.

Disable
Disables the task sequence so that it can't run on computers. You can deploy a disabled
task sequence, but computers don't run the task sequence until you enable it.

Export
For more information, see Export and import task sequences.

Copy
Makes a copy of the selected task sequence. This action is useful to create a new task
sequence that's based on an existing task sequence.

When you make a copy of a task sequence in a folder, the copy is listed in that folder
until you refresh the task sequence node. After the refresh, the copy appears in the root
folder.

Refresh
Refreshes the details for the selected task sequence.

Delete
Deletes the selected task sequence.

Create Phased Deployment

<!-- p.224 -->

For more information, see Create phased deployments.

Deploy
For more information, see Deploy a task sequence.

Distribute Content
Starts the Distribute Content Wizard to send the referenced content to distribution
points.

Create Prestaged Content File
Starts the Create Prestaged Content File Wizard to prestage the task sequence content.
For information about how to create a prestaged content file, see Prestage content.

Move
Moves the selected task sequence to another folder in the Task Sequences node.

Set Security Scopes
Select the security scopes for the selected task sequence. For more information, see
Security scopes.

Properties action
For more information, see Properties.

View
The View action on task sequences is the default. This action lets you see the steps of
the task sequence without locking it for editing. For more information, see Use the task
sequence editor.

Next steps
     Distribute referenced content

     Reduce the size of task sequence policy

<!-- p.225 -->

     Deploy a task sequence

     How to use task sequence variables

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.226 -->

High-impact task sequence settings
Applies to: Configuration Manager (current branch)

Configure a task sequence as high-impact and customize the messages that users receive
when they run the task sequence. Any task sequence that meets certain conditions is
automatically defined as high-impact. For more information, see Manage high-risk
deployments.

  ２ Warning

  If you use PXE deployments, and configure device hardware with the network adapter as
  the first boot device, these devices can automatically start an OS deployment task
  sequence without user interaction. Deployment verification doesn't manage this
  configuration. While this configuration may simplify the process and reduce user
  interaction, it puts the device at greater risk for accidental reimage.

Set a task sequence as high-impact
Use the following procedure to set a task sequence as high-impact.

   1. In the Configuration Manager console, go to the Software Library workspace, expand
     Operating Systems, and select Task Sequences.

   2. Select the task sequence to configure, and select Properties.

   3. On the User Notification tab, select This is a high-impact task sequence.

Create a custom notification

  ７ Note

  The client only displays high-impact notifications for required OS deployment task
  sequences. It doesn't display them for non-OS deployment or stand-alone task sequences.

Use the following procedure to create a custom notification for high-impact deployments.

   1. In the Configuration Manager console, go to the Software Library workspace, expand
     Operating Systems, and select Task Sequences.

   2. Select the task sequence to configure, and select Properties.

<!-- p.227 -->

   3. On the User Notification tab, select Use custom text.

       ７ Note

       You can only set user notification text when you select the option, This is a high-
       impact task sequence.

   4. Configure the following settings:

       ７ Note

       Each text box has a maximum limit of 255 characters.

          User notification headline text: Specifies the blue text that displays on the Software
          Center user notification. For example, in the default user notification, this section
          contains "Confirm you want to upgrade the operating system on this computer."

          User notification message text: There are three text boxes that provide the body of
          the custom notification. All text boxes require that you add text.

             First text box: Specifies the main body of text, typically containing instructions for
             the user. For example, in the default user notification, this section contains
             "Upgrading the operating system takes time and your computer might restart
             several times."

             Second text box: Specifies the bold text under the main body of text. For
             example, in the default user notification, this section contains "This in-place
             upgrade installs the new operating system and automatically migrates your apps,
             data, and settings."

             Third text box: Specifies the last line of text under the bold text. For example, in
             the default user notification, this section contains "Click Install to begin.
             Otherwise, click Cancel."

Example
You configure the following custom notification in task sequence properties:

<!-- p.228 -->

The following notification message displays when the end user opens the installation from
Software Center:

  ７ Note

<!-- p.229 -->

  If you set up a non-OS deployment task sequence as high-impact, it displays under the
  Operating Systems node in Software Center as well as all OSD task sequence
  deployments. Normally, non-OSD task sequence deployments are displayed under the
  Applications node.

Next steps
Task sequence performance

Last updated on 02/02/2026

<!-- p.230 -->

Task sequence performance
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

To improve the overall speed of the task sequence, run it with the high-performance
power plan. It configures Windows to use its built-in high-performance power plan,
which delivers maximum performance at the expense of higher power consumption.
This option is on by default for new task sequences.

When the task sequence starts, in most scenarios it records the currently enabled power
plan. It then switches the active power plan to the Windows default High Performance
plan. If the task sequence restarts the computer, it repeats this process. At the end of
the task sequence, it resets the power plan to the stored value. This functionality works
in both Windows and Windows PE, but has no effect on virtual machines.

      If the task sequence starts in Windows PE, the task sequence doesn't record the
      currently enabled power plan for later reuse.

      An OS deployment task sequence that reimages the computer (wipe and load)
      doesn't preserve the power plan setting of the old OS. At the end of the task
      sequence, it restores the default Balanced power plan.

You can use this option on devices with modern standby. It also supports other devices
that don't have that default power plan. When you use this task sequence option, it
creates a temporary power plan that's similar to the default for High Performance. This
power plan modifies the timeout values to 0 for standby, monitor, disk, and hibernate
when plugged in. These configurations prevent these devices from falling asleep during
an OS deployment task sequence. After the task sequence completes, it reverts to the
original power plan, and deletes the temporary plan.

  ） Important

  To take advantage of this Configuration Manager feature, after you update the site,
  update clients to the latest version. Also update boot images to include the latest
  client components. While new functionality appears in the Configuration Manager
  console when you update the site and console, the complete scenario isn't
  functional until the client version is also the latest.

Configure the task sequence

<!-- p.231 -->

   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Operating Systems, and select the Task Sequences node.

   2. Select the task sequence to configure, and then in the ribbon select Properties.

   3. Switch to the More Options tab.

         Tip

        In version 2111 and earlier, this tab is named Performance.

   4. Enable the option to Run as high performance power plan.

  ２ Warning

  Be cautious with this setting on low performance hardware. Running intense system
  operations for an extended period of time can strain low-end hardware. Check with
  your hardware manufacturer for specific guidance.

Known issues
Usually, when you change settings in task sequence properties, it updates all existing
deployments. When you change this performance setting in the task sequence
properties, it doesn't affect any existing deployments of the task sequence. To enable or
disable this setting for high performance, create a new task sequence deployment.

Next steps
Distribute referenced content

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.232 -->

Distribute referenced content
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before clients run a task sequence that references content, distribute that content to
distribution points. At any time, you can select the task sequence and distribute its
content to build a new list of reference packages for distribution. If you make changes
to the task sequence with updated content, redistribute the content before it's available
to clients.

Distribute content
Use the following procedure to distribute the content that is referenced by a task
sequence:

   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Operating Systems, and then select the Task Sequences node.

   2. In the Task Sequence list, select the task sequence that you want to distribute.

   3. On the Home tab of the ribbon, in the Deployment group, select Distribute
      Content. This action starts the Distribute Content Wizard.

   4. On the General page, verify that the correct task sequence is selected for
      distribution.

   5. On the Content page, verify the content to distribute, such as the boot image
      referenced by the task sequence.

   6. On the Content Destination page, specify the collections, distribution point, or
      distribution point group where you want to distribute the task sequence contents.

        ） Important

        If the task sequence that you selected references content that's already
        distributed to a specific distribution point, the wizard doesn't list that
        distribution point.

   7. Complete the wizard.

<!-- p.233 -->

Prestage content
You can also prestage the content referenced in the task sequence. Configuration
Manager creates a compressed, prestaged content file that contains the files, associated
dependencies, and associated metadata for the content that you select. Then you
manually import the content at a site server, secondary site, or distribution point. For
more information about how to prestage content files, see Prestage content.

Next steps
Reduce the size of task sequence policy

Deploy a task sequence

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.234 -->

Reduce the size of task sequence policy
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When the size of the task sequence policy exceeds 32 MB, the client fails to process the
large policy. The client then fails to run the task sequence deployment. The size of the
task sequence as stored in the site database is smaller, but can still cause problems if
too large. When the client processes the entire task sequence policy, the expanded size
can cause problems over 32 MB.

To check for the 32-MB task sequence policy size on clients, use management insights.

Configuration Manager restricts the following actions for a task sequence in the site
database that's greater than 2 MB in size:

      Save changes in the task sequence editor
      Save changes with PowerShell cmdlets
      Import a new task sequence
      Any other change using supported SDK methods

For example, if you try to save changes to a large task sequence, the task sequence
editor will display an error.

   Tip

  The behavior in version 2010 and later checks for the 2 MB size limit on the task
  sequence as stored in the site database. When the client processes the entire task
  sequence policy, the expanded size can cause problems over 32 MB. The
  management insights check for the 32 MB task sequence policy size.

When you view the list of task sequences in the Configuration Manager console, add the
Size (KB) column. Use this column to identify large task sequences that can cause
problems.

Actions to reduce task sequence size
To help reduce the size of task sequences and task sequence deployment policies, take
the following actions:

<!-- p.235 -->

     Separate functional segments into child task sequences, and use the Run Task
     Sequence step. Keep each task sequence less than 2 MB in the database. Each task
     sequence has a separate 32-MB limit on its policy size.

        ７ Note

        Reducing the total number of steps and groups in a task sequence has
        minimal impact on the policy size. Each step is generally a couple of KB in
        policy. Moving groups of steps to a child task sequence is more impactful.

     Reduce the number of software updates in deployments to the same collection as
     the task sequence.

     Instead of entering a script in the Run PowerShell Script step, reference it via a
     package.

     There's an 8-KB limit on the size of the task sequence environment when it runs.
     Review the usage of custom task sequence variables, which can also contribute to
     the policy size.

     As a last resort, split a complex, dynamic task sequence into separate task
     sequences with distinct deployments to different collections.

Next steps
Export and import task sequences

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.236 -->

Export and import task sequences
Article • 04/13/2023

Applies to: Configuration Manager (current branch)

Export and import task sequences with or without their related objects. Use this process
to move task sequences between hierarchies. For example, you create a task sequence
in a development lab and export it. You then import that task sequence into the
production environment to deploy.

This referenced content includes the following objects:

      OS images
      Boot images
      Packages like the client install package
      Driver packages
      Applications with dependencies
      Other task sequences referenced with the Run task sequence step

Consider the following points when you export and import task sequences:

      Configuration Manager doesn't export passwords in the task sequence. If you
      export and import a task sequence that contains passwords, edit the imported task
      sequence to reenter any passwords. Review the following steps that may include a
      password:
         Join Domain or Workgroup
         Connect To Network Folder
         Run Command Line

      When you export a task sequence with the Set Dynamic Variables step,
      Configuration Manager doesn't export values for variables that you configure with
      the Secret value setting. Reenter the values for these variables after you import the
      task sequence.

      When you have multiple primary sites, import task sequences at the central
      administration site.

Export
   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Operating Systems, and then select the Task Sequences node.

<!-- p.237 -->

   2. In the Task Sequence list, select the task sequences that you want to export. If you
      select more than one task sequence, they're all stored in one export file.

   3. On the Home tab of the ribbon, in the Task Sequence group, select Export. This
      action starts the Export Task Sequence Wizard.

   4. On the General page, specify the following settings:

            File: Specify the location and name of the export file. If you enter the file
            name directly, be sure to include the .zip extension to the file name. If you
            browse for the export file, the wizard automatically adds this file name
            extension.

            If you don't want to export task sequence dependencies, deselect the option
            to Export all task sequence dependencies. By default, the wizard scans for all
            the related objects and exports them with the task sequence. These
            dependencies include any for applications and child task sequences.

            If you don't want to copy the content from the package source to the export
            location, deselect the option to Export all content for the selected task
            sequences and dependencies. If you select this option, the Import Task
            Sequence Wizard uses the import path as the new package source location.

            Administrator comments: Add a description of the task sequences to export.

   5. Complete the wizard.

The wizard creates the following output files:

      If you don't export content: a .zip file.

      If you export content: a .zip file and a folder named export_files, where export is the
      name of the .zip file that contains the exported content.

If you include content when you export a task sequence, make sure that you copy the
.zip file and the export_files folder, or the import fails.

  ７ Note

  If you have a multi-site hierarchy, the export of task sequences should be done
  from the central administration site because the primary site may not have the
  required permissions to all the artifacts.

<!-- p.238 -->

Import
   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Task Sequences node.

   2. On the Home tab of the ribbon, in the Create group, select Import Task Sequence.
     This action starts the Import Task Sequence Wizard.

   3. On the General page of the ribbon, specify the exported .zip file.

   4. On the File Content page, select the action that you require for each object that
     you import. This page shows all the objects that Configuration Manager found to
     import.

          If the object has never been imported, select Create New.

          If the object has been previously imported, select one of the following
          actions:

               Ignore Duplicate (default): This action doesn't import the object. Instead,
               the wizard links the existing object to the task sequence.

               Overwrite: This action overwrites the existing object with the imported
               object. For applications, you can add a revision to update the existing
               application or create a new application.

   5. Complete the wizard.

After you import the task sequence, edit the task sequence to specify any passwords
that were in the original task sequence. For security reasons, passwords aren't exported.

   Tip

  When you import an object in the Configuration Manager console, it imports to the
  current folder. In earlier versions of Configuration Manager, it always put imported
  objects in the root node.

Next steps
Deploy a task sequence

<!-- p.239 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.240 -->

Deploy a task sequence
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After you create a task sequence, and distribute the referenced content, deploy it to a
device collection. This action allows the task sequence to run on a device. A deployed
task sequence can run automatically, or when installed by a user of the device.

  ２ Warning

  You can manage the behavior for high-risk task sequence deployments. A high-risk
  deployment is a deployment that is automatically installed and has the potential to
  cause unwanted results. For example, a task sequence that has a purpose of
  Required that deploys an OS is considered a high-risk deployment. For more
  information, see Settings to manage high-risk deployments.

Process
Use the following procedure to deploy a task sequence to the computers in a collection.

  ７ Note

  The status messages for the task sequence deployment are displayed in the
  message window on a primary site, but they aren't displayed on a central
  administration site.

   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Operating Systems, and then select the Task Sequences node.

   2. In the Task Sequence list, select the task sequence that you want to deploy.

   3. On the Home tab of the ribbon, in the Deployment group, select Deploy.

        ７ Note

        If Deploy isn't available, the task sequence has a reference that's not valid.
        Correct the reference and then try to deploy the task sequence again.
