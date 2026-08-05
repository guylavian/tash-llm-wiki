---
title: "OS deployment documentation — pages 121-160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0121-0160
family: sccm
documentKind: "doc"
abstract: "If a device driver is causing a problem or you want to suspend the installation of a device driver, disable it during import. You can also disable drivers after you import them. To assign the device drivers to an administrative category for filtering purposes, such as \"Desktops\""
---

# OS deployment documentation — pages 121-160

<!-- p.121 -->

         If a device driver is causing a problem or you want to suspend the
         installation of a device driver, disable it during import. You can also
         disable drivers after you import them.

       To assign the device drivers to an administrative category for filtering
       purposes, such as "Desktops" or "Notebooks", select Categories. Then choose
       an existing category, or create a new category. Use categories to control
       which device drivers are applied by the Auto Apply Drivers task sequence
       step.

5. On the Add Driver to Packages page, choose whether to add the drivers to a
  package.

       Select the driver packages that are used to distribute the device drivers.

       If necessary, select New Package to create a new driver package. When you
       create a new driver package, provide a network share that's not in use by
       other driver packages.

       If the package has already been distributed to distribution points, select Yes
       in the dialog box to update the boot images on distribution points. You can't
       use device drivers until they're distributed to distribution points. If you select
       No, run the Update Distribution Point action before using the boot image. If
       the driver package has never been distributed, you must use the Distribute
       Content action in the Driver Packages node.

6. On the Add Driver to Boot Images page, choose whether to add the device drivers
  to existing boot images.

    ７ Note

    Add only storage and network drivers to the boot images.

       Select Yes in the dialog box to update the boot images on distribution points.
       You can't use device drivers until they're distributed to distribution points. If
       you select No, run the Update Distribution Point action before using the
       boot image. If the driver package has never been distributed, you must use
       the Distribute Content action in the Driver Packages node.

       Configuration Manager warns you if the architecture for one or more drivers
       doesn't match the architecture of the boot images that you selected. If they
       don't match, select OK. Go back to the Driver Details page, and clear the

<!-- p.122 -->

           drivers that don't match the architecture of the selected boot image. For
           example, if you select an x64 and x86 boot image, all drivers must support
           both architectures. If you select an x64 boot image, all drivers must support
           the x64 architecture.

             ７ Note
                The architecture is based on the architecture reported in the INF from
                the manufacturer.
                If a driver reports it supports both architectures, then you can import
                it into either boot image.

           Configuration Manager warns you if you add device drivers that aren't
           network or storage drivers to a boot image. In most cases, they aren't
           necessary for the boot image. Select Yes to add the drivers to the boot
           image, or No to go back and modify your driver selection.

           Configuration Manager warns you if one or more of the selected drivers
           aren't properly digitally signed. Select Yes to continue, and select No to go
           back and make changes to your driver selection.

   7. Complete the wizard.

Manage device drivers in a driver package
Use the following procedures to modify driver packages and boot images. To add or
remove a driver, first locate it in the Drivers node. Then edit the packages or boot
images with which the selected driver is associated.

   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Operating Systems, and then select the Drivers node.

   2. Select the device drivers that you want to add to a driver package.

   3. On the Home tab of the ribbon, in the Driver group, select Edit, and then choose
     Driver Packages.

   4. To add a device driver, select the check box of the driver packages to which you
     want to add the device drivers. To remove a device driver, clear the check box of
     the driver packages from which you want to remove the device driver.

     If you're adding device drivers that are associated with driver packages, you can
     optionally create a new package. Select New Package, which opens the New

<!-- p.123 -->

     Driver Package dialog box.

   5. If the package has already been distributed to distribution points, select Yes in the
     dialog box to update the boot images on distribution points. You can't use device
     drivers until they're distributed to distribution points. If you select No, run the
     Update Distribution Point action before using the boot image. If the driver
     package has never been distributed, you must use the Distribute Content action in
     the Driver Packages node. Before the drivers are available, you must update the
     driver package on distribution points.

     Select OK when finished.

Manage device drivers in a boot image
You can add to boot images Windows device drivers that have been imported into the
catalog. Use the following guidelines when you add device drivers to a boot image:

     Add only storage and network drivers to boot images. Other types of drivers aren't
     usually required in Windows PE. Drivers that aren't required unnecessarily increase
     the size of the boot image.

     Add only device drivers to a boot image for the version of Windows PE. For
     example, if you're using the Windows ADK for Windows 11, only add Windows 11
     drivers.

     Make sure that you use the correct device driver for the architecture of the boot
     image. Don't add an x86 device driver to an x64 boot image.

Process to modify the device drivers associated with a boot image

   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Operating Systems, and then select the Drivers node.

   2. Select the device drivers that you want to add to the driver package.

   3. On the Home tab of the ribbon, in the Driver group, select Edit, and then choose
     Boot images.

   4. To add a device driver, select the check box of the boot image to which you want
     to add the device drivers. To remove a device driver, clear the check box of the
     boot image from which you want to remove the device driver.

   5. If you don't want to update the distribution points where the boot image is stored,
     clear the Update distribution points when finished check box. By default, the

<!-- p.124 -->

     distribution points are updated when the boot image is updated.

           Select Yes in the dialog box to update the boot images on distribution points.
           You can't use device drivers until they're distributed to distribution points. If
           you select No, run the Update Distribution Point action before using the
           boot image. If the driver package has never been distributed, you must use
           the Distribute Content action in the Driver Packages node.

           Configuration Manager warns you if the architecture for one or more drivers
           doesn't match the architecture of the boot images that you selected. If they
           don't match, select OK. Go back to the Driver Details page and clear the
           drivers that don't match the architecture of the selected boot image. For
           example, if you select an x64 and x86 boot image, all drivers must support
           both architectures. If you select an x64 boot image, all drivers must support
           the x64 architecture.

             ７ Note
                The architecture is based on the architecture reported in the INF from
                the manufacturer.
                If a driver reports it supports both architectures then you can import
                it into either boot image.

           Configuration Manager warns you if you add device drivers that aren't
           network or storage drivers to a boot image. In most cases, they aren't
           necessary for the boot image. Select Yes to add the drivers to the boot image
           or No to go back and modify your driver selection.

           Configuration Manager warns you if one or more of the selected drivers
           aren't properly digitally signed. Select Yes to continue or select No to go back
           and make changes to your driver selection.

Additional actions for device drivers
You can do additional actions to manage drivers when you select them in the Drivers
node.

Categorize
Clears, manages, or sets an administrative category for the selected drivers.

<!-- p.125 -->

Delete (driver)
Removes the driver from the Drivers node and also removes the driver from the
associated distribution points.

Disable
Prohibits the driver from being installed. This action temporarily disables the driver. The
task sequence can't install a disabled driver when you deploy an OS.

  ７ Note

  This action only prevents drivers from installing using the Auto Apply Driver task
  sequence step.

Enable

Lets Configuration Manager client computers and task sequences install the device
driver when you deploy the OS.

Move (driver)
Moves the device driver to another folder in the Drivers node.

Properties (driver)
Opens the Properties dialog box. Review and change the properties of the driver. For
example, change its name and description, enable or disable it, and specify which
platforms it can run on.

Use task sequences to install drivers
Use task sequences to automate how the OS is deployed. Each step in the task sequence
can do a specific action, such as installing a driver. You can use the following two task
sequence steps to install device drivers when you deploy an OS:

     Auto Apply Drivers: This step lets you automatically match and install device
     drivers as part of an operating system deployment. You can configure the task
     sequence step to install only the best matched driver for each detected hardware
     device. Alternatively, specify that the step installs all compatible drivers for each

<!-- p.126 -->

     detected hardware device, and then let Windows Setup choose the best driver. You
     can also specify a driver category to limit the drivers that are available for this step.

     Apply Driver Package: This step lets you make all device drivers in a specific driver
     package available for Windows Setup. In the specified driver packages, Windows
     Setup searches for the device drivers that are required. When you create stand-
     alone media, you must use this step to install device drivers.

When you use these task sequence steps, you can also specify how the drivers are
installed on the computer where you deploy the OS. For more information, see Manage
task sequences to automate tasks.

Driver reports
You can use several reports in the Driver Management reports category to determine
general information about the device drivers in the driver catalog. For more information
about reports, see Introduction to reporting.

Next steps
Manage task sequences to automate tasks

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.127 -->

Manage user state in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can use Configuration Manager task sequences to capture and restore the user
state data in OS deployment scenarios where you want to keep the user state of the
current OS. For example:

      Deployments where you want to capture the user state from one computer to
      restore it on another computer.

      Update deployments where you want to capture and restore the user state on the
      same computer.

Configuration Manager uses the User State Migration Tool (USMT) 10.0 to manage the
migration of user state data from a source computer to a destination computer after the
operating system installation completes. For more information about common
migration scenarios for the USMT 10.0, see Common Migration Scenarios.

Capture user state data
When you capture user state, you can store the user state data on the destination
computer or on a state migration point. To store the user state on a state migration
point, first configure a site system server to host the role. To store the user state on the
destination computer, configure the task sequence to store the data locally using links.

  ７ Note

  The links that Windows uses to store the user state locally are referred to as hard-
  links. A hard-link migration store is a USMT 10.0 feature. It scans the computer for
  user files and settings and then creates a directory of hard-links to those files.
  USMT then uses the hard-links to restore the user data after the task sequence
  deploys the new OS.

  ） Important

<!-- p.128 -->

  You can't use a state migration point and use hard-links to store the user state data
  at the same time.

When USMT captures the user state, it can store the information in one of the following
ways:

        Store the data remotely on a state migration point. The Capture User State task
        sequence step sends the data to the server. After the task sequence deploys the
        OS, the Restore User State step downloads the data from the server and restores
        the user state on the destination computer.

        Store the data locally to a specific location. In this scenario, the Capture User State
        step copies the user data to a specific location on the destination computer. After
        the task sequence deploys the OS, the Restore User State step gets the user data
        from that local location.

        Use hard-links. In this scenario, the user state data remains on the drive when the
        task sequence removes the old OS. After the task sequence deploys the OS, the
        Restore User State step uses the hard-links to restore the user state data to its
        original location.

Store user state data on a state migration point
To store the user state data on a state migration point, use the following steps:

   1. Configure a state migration point to store the user state data.

   2. Create a computer association between the source computer and the destination
        computer. Create this association before you capture the user state on the source
        computer.

   3. Create a task sequence to capture and restore user state. Specifically, add the
        following task sequence steps to capture user data from a computer, store the user
        date on a state migration point, and restore the user data to a computer:

             Request State Store: Requests access to a state migration point when
             capturing state from a computer or restoring state to a computer.

             Capture User State: Runs USMT to capture and store the user state data on
             the state migration point.

             Restore User State: Runs USMT to restore the data from a state migration
             point to the destination computer.

<!-- p.129 -->

           Release State Store: Notifies the state migration point that the capture or
           restore action is complete.

Store user data locally
To store the user state data locally, create a task sequence to capture and restore user
state. Specifically, add the following task sequence steps to capture user data from a
computer and restore it:

     Capture User State: Run USMT to capture and store the user state to a local folder,
     with or without hard-links.

     Restore User State: Run USMT to restore the data from the local store to the
     destination computer.

        ７ Note

        The user state data that the hard-links reference remains on the computer
        after the task sequence removes the old OS.

The state migration point
The state migration point stores user state data. The task sequence captures it from one
computer and then restores it on another computer. When you capture user settings for
an OS deployment on the same computer, you can store the data on the same
computer by using hard-links or you can use a state migration point. For some
deployments, when you create the state store, Configuration Manager automatically
creates an association between the state store and the destination computer.

For more information about the state migration point and the steps to configure it, see
State migration point.

Computer associations
You use a computer association when you install an OS on new hardware and restore
user data settings from another computer. The association defines the relationship
between the source and destination computers. The source computer is an existing
computer that Configuration Manager manages. It has the original user state. The
destination computer is a new computer with a new OS. You restore the user state to
the destination computer.

<!-- p.130 -->

  ７ Note

  It's not supported to create a computer association between computers located in
  a Configuration Manager parent site with computers located in a child site.
  Computer associations are site specific and don't replicate.

Create a computer association
   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, and select the User State Migration node.

   2. On the Home tab, in the Create group, select Create Computer Association.

   3. On the Computer Association tab:

      a. For the Source computer, select Search. Locate and select the existing
        computer that has the user state.

     b. Repeat this process for the Destination computer. You may need to Import
        computer information to predefine the device record.

   4. Switch to the User Accounts tab to specify the user accounts to migrate to the
     destination computer. Select one of the following migration behaviors:

           Capture and restore all user accounts: Use this option to create multiple
           associations to the same source computer.

           Capture all user accounts and restore specified accounts: This option
           captures all user accounts from the source computer and only restores the
           accounts that you specify to the destination computer. You can also use this
           setting to create multiple associations to the same source computer.

           Capture and restore specified user accounts: This option captures and
           restores only the accounts that you specify. When you select this option, you
           can't create multiple associations to the same source computer. This value is
           the default option.

     Select the new button (gold asterisk) to add user accounts from Active Directory.

When a deployment fails
If the OS deployment fails, use the USMT 10.0 LoadState tool to manually get the user
state data that the task sequence captured. Use this process for data stored on a state

<!-- p.131 -->

migration point or saved locally on the computer. For more information on command-
line options, see LoadState Syntax.

Next steps
State migration point

Create a task sequence to capture and restore user state

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.132 -->

Prepare for unknown computer
deployments in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the information in this topic to deploy operating systems to unknown computers in
your Configuration Manager environment. An unknown computer is a computer that
isn't managed by Configuration Manager. This means that there's no record of these
computers in the Configuration Manager database. Unknown computers include the
following:

      A computer where the Configuration Manager client isn't installed

      A computer that isn't imported into Configuration Manager

      A computer that isn't been discovered by Configuration Manager

      You can deploy operating systems to unknown computers with the following
      deployment methods:

      Use PXE to deploy Windows over the network

      Use bootable media to deploy an operating system

      Use prestaged media to deploy an operating system

Unknown computer deployment workflow
The following is the basic workflow to deploy an operating system to an unknown
computer:

      Select an unknown computer object to use in the deployment. You can deploy the
      operating system to one of the unknown computer objects in the All Unknown
      Computers collection or you can add the objects in the All Unknown Computer
      collection to another collection. Configuration Manager provides two unknown
      computer objects in the All Unknown Computers collection. One object is for x86
      computers and the other object is for x64 computers.

        ７ Note

<!-- p.133 -->

       The x86 Unknown Computer object is for computers that are only x86
       capable. The x64 Unknown Computer object is for computers that are x86
       and x64 capable. In other words, these objects describe the architecture of the
       destination computer. They do not describe the operating system that you
       want to deploy to the destination computer.

     Configure a PXE-enabled distribution point or create media to support unknown
     computer deployments.

     Deploy the task sequence to install the operating system.

Unknown Computer Installation Process
When a computer is first started from PXE or from media, Configuration Manager checks
to see if a record for that computer exists in the Configuration Manager database. If
there's a record, Configuration Manager then checks to see if there are any task
sequences deployed to the record. If there isn't a record, Configuration Manager checks
to see if there are any task sequences deployed to an unknown computer object. In
either case, Configuration Manager then performs one of the following actions:

     If there's an available task sequence, Configuration Manager prompts the user to
     run the task sequence.

     If there's a required task sequence, Configuration Manager automatically runs the
     task sequence.

     If a task sequence isn't deployed for the record, Configuration Manager generates
     an error that there's no deployed task sequence for the destination computer.

     When an unknown computer is started, Configuration Manager recognizes the
     computer as an unprovisioned computer rather than an unknown computer. This
     means that the computer can now receive the task sequences that were deployed
     to the unknown computer object. The deployed task sequence then installs an
     operating system image that must include the Configuration Manager client.

     After the Configuration Manager client is installed, a record for the computer is
     created and the computer is listed in the appropriate Configuration Manager
     collection. If the computer fails to install the operating system image or the
     Configuration Manager client, an "Unknown" record for the computer is created
     and the computer appears in the All Systems collection.

  ７ Note

<!-- p.134 -->

  During the installation of the operating system image, the task sequence can
  retrieve collection variables but not computer variables from this computer.

Enabling Unknown Computer Support
Use the following to enable unknown computer support when you deploy an operating
system by using PXE, bootable media, and prestaged media.

     PXE

     Select the Enable unknown computer support check box on the PXE tab for a
     distribution point that is enabled for PXE. For more information, see Configuring
     distribution points to accept PXE requests.

     Bootable media

     Select the Enable unknown computer support check box on the Security page of
     the Create Task Sequence Media Wizard. For more information, see Configuring
     distribution points to accept PXE requests and Use PXE to deploy Windows over
     the network with Configuration Manager.

     Prestaged media

     Select the Enable unknown computer support check box on the Security page of
     the Create Task Sequence Media Wizard. For more information, see Create
     prestaged media with Configuration Manager.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.135 -->

Associate users with a destination
computer in Configuration Manager
07/17/2025

Applies to: Configuration Manager (current branch)

When you use Configuration Manager to deploy operating systems, you can associate users
with the destination computer. This option works whether a single user or multiple users are
the primary users of the destination computer.

User device affinity supports user-centric management for when you deploy applications.
When you associate a user with the destination computer on which to install an OS, you can
later deploy applications to that user, and the applications automatically install on the
destination computer. While you can configure support for user device affinity during OS
deployment, you can't use user device affinity to deploy the OS.

For more information about user device affinity, see Link users and devices with user device
affinity.

There are several methods by which you can integrate user device affinity into your OS
deployments. You can integrate user device affinity into PXE deployments, bootable media
deployments, and pre-staged media deployments.

  ７ Note

  When integrating user device affinity in OS deployments, the value of the
  SMSTSAssignUsersMode variable needs to match the value configured in the boot
  method (PXE, bootable media, pre-staged media).

  If the values don't match, then device affinity isn't set.

Create a task sequence that includes the
SMSTSAssignUsersMode variable
Add the SMSTSAssignUsersMode variable to the beginning of your task sequence by using
the Set Task Sequence Variable step. This variable specifies how the task sequence handles the
user information.

For more information, see Task sequence variables.

<!-- p.136 -->

Create a prestart command that gathers the user information
The prestart command can be a VBScript with an input box. It can also be an HTML application
(HTA) that validates the user data that they enter.

This prestart command must set the SMSTSUDAUsers variable that's used when the task
sequence runs. This variable can be set on a computer, a collection, or a task sequence variable.

For more information, see Task sequence variables.

Configure how distribution points and media associate the
user with the destination computer
The distribution point or media supports associating users with the destination computer
where the OS is deployed. Use one of the following methods:

     Configure a distribution point to accept PXE boot requests
     Create bootable media
     Create pre-staged media

Configuring user device affinity support doesn't have a built-in method to validate the user
identity. This behavior is important when a technician is provisioning the computer and enters
the information on behalf of the user. In addition to setting how task sequence handles the
user information, configuring these options on the distribution point and media provides the
ability to restrict the deployments that are started from a PXE boot or from a specific type of
media.

<!-- p.137 -->

Prepare Windows PE peer cache to
reduce WAN traffic in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

When you deploy a new operating system in Configuration Manager, computers that
run the task sequence can use Windows PE Peer Cache to obtain content from a local
peer (a peer cache source) instead of downloading content from a distribution point.
This helps minimize wide area network (WAN) traffic in branch office scenarios where
there is no local distribution point.

Windows PE Peer Cache is similar to Windows BranchCache, but functions in the
Windows Preinstallation Environment (Windows PE). The following terms are used to
describe the clients that use Windows PE Peer Cache:

      A peer cache client is a computer that is configured to use Windows PE Peer
      Cache.

      A peer cache source is a client that is configured for peer cache and that makes
      content available to other peer cache clients that request that content.

Use the following sections to manage Peer Cache.

Objects stored on a Peer Cache source
A task sequence configured to use Windows PE Peer Cache can get the following
content objects while running in Windows PE:

      Operating system image

      Driver package

      Packages and Programs (When the client continues to run the task sequence in the
      full operating system, the client gets this content from a peer cache source if the
      task sequence was originally configured for peer cache when running in Windows
      PE.)

      Additional boot images

<!-- p.138 -->

     The following content objects never transfer using peer cache. Instead, they
     transfer from a distribution point or by Windows BranchCache if you have
     configured Windows BranchCache in your environment:

     Applications

     Software updates

How does Windows PE Peer Cache work?
Consider a scenario with a branch office that does not have a distribution point but does
have several clients enabled to use Windows PE Peer Cache. You deploy the task
sequence configured to use peer cache to several clients that are configured to be part
of the peer cache source. The first client to run the task sequence broadcasts a request
for a peer with the content. It doesn't find one so it gets the content from a distribution
point across the WAN. The client installs the new image and then stores the content in
its Configuration Manager client cache so it can function as a peer cache source to other
clients. When the next client runs the task sequence, it broadcasts a request on the
subnet for a peer cache source, and that first client responds and makes its cached
content available.

Determine what clients will be part of the
Windows PE Peer Cache source
To help you determine what computers to select as a Windows PE Peer Cache source,
there are several things that you should consider:

     The Windows PE Peer Cache source should be a desktop computer that is always
     powered on and available to peer cache clients.

     The Windows PE Peer Cache has a client cache size sufficient to store the images.

Requirements for a client to use a Windows PE
Peer Cache source
For clients to use a Windows PE Peer Cache source, they must meet the following
requirements:

     The Configuration Manager client must be able to communicate across the
     following ports on your network:

<!-- p.139 -->

        Port for the initial network broadcast to find a peer cache source. By default, this
        is UDP port 8004.

        Port for content downloading from a peer cache source (HTTP and HTTPS). By
        default, this is TCP port 8003.

        For more information, see Ports used for connections.

           Tip

          Clients will use HTTPS to download content when it is available. However,
          the same port number is used for either HTTP or HTTPS.

     Configure the client cache on clients to ensure they have enough space to hold
     and store the images you deploy. Windows PE Peer Cache does not affect the
     configuration or behavior of the client cache.

     The deployment options for the task sequence deployment must be configured as
     Download content locally when needed by task sequence.

Configure Windows PE Peer Cache
You can use the following methods to provision a client with peer cache content so it
can serve as a peer cache source:

     A peer cache client that cannot find a peer cache source with the content will
     download it from a distribution point. If the client receives client settings that
     enable peer cache and the task sequence is configured to preserve the cached
     content, the client becomes a peer cache source.

     A peer cache client can get content from another peer cache client (a peer cache
     source). Because the client is configured for peer cache, when it runs a task
     sequence that is configured to preserve the cached content, the client becomes a
     peer cache source.

     A client runs a task sequence that includes the optional step, Download Package
     Content, which is used to prestage the relevant content that is included in the
     Windows PE Peer Cache task sequence. When you use this method:

        The client does not need to install the image that is being deployed.

        In addition to the Download Package Content option, the task sequence must
        also use the Configuration Manager client cache option. You use this option to

<!-- p.140 -->

      store the content in the clients cache so the client can act as a peer cache
      source for other peer cache clients.

   The following procedures will help you configure Windows PE Peer Cache on
   clients and configure task sequences that support peer cache.

To configure the Windows PE Peer Cache source
computers
 1. In the Configuration Manager console, navigate to Administration > Client
   Settings, and then create a new Custom Client Device Settings or edit an existing
   settings object. You can also configure this for the Default Client Settings object.

      Tip

     Use a custom settings object to manage which clients receive this
     configuration. For example, you might want to avoid configuring this on the
     laptops of users who are frequently on the move. A highly mobile system can
     be a poor source to provide content to other peer cache clients.

     Also remember that when you configure this setting as part of the Default
     Client Settings, the configuration applies to all clients in your environment.

 2. Under Client Cache Settings, set Enable Configuration Manager client in full OS
   to share content to Yes.

        By default, only HTTP is enabled. If you want to enable clients to download
        content over HTTPS, set Enable HTTPS for client peer communication to Yes.

        By default, the port for broadcasts is set to 8004 and the port for content
        downloads is set to 8003. You can change both.

 3. Save and deploy the Client Settings to the clients that you select to be a peer
   cache source.

   After a device is configured with this settings object, the device is configured to act
   as a peer cache source. These settings should be deployed to potential peer cache
   clients to configure the required ports and protocols.

Configure a task sequence for Windows PE Peer Cache

<!-- p.141 -->

When you configure the task sequence, use the following task sequence variables as
Collection Variables on the collection to which the task sequence is deployed:

     SMSTSPeerDownload

     Value: TRUE

     This enables the client to use Windows PE Peer Cache.

     SMSTSPeerRequestPort

     Value: <Port number>

     When you do not use the default port configured in the Client Settings (8004), you
     must configure this variable with a custom value of the network port to use for the
     initial broadcast.

     SMSTSPreserveContent

     Value: TRUE

     This flags the content in the task sequence to be retained in the Configuration
     Manager client cache after the deployment. This is different than using
     SMSTSPersisContent which only preserves the content for the duration of the task
     sequence and uses the task sequence cache, not the Configuration Manager client
     cache.

     For more information, see Task sequence variables.

Validate the success of using Windows PE peer cache
After you use Windows PE peer cache to deploy and install a task sequence, you can
confirm that peer cache was successfully used in the process by viewing the smsts.log
on the client that ran the task sequence.

In the log, locate an entry similar to the following where <SourceServerName> identifies
the computer from which the client obtained the content. This computer should be a
peer cache source, and not a distribution point server. Other details will vary based on
your local environment and configurations.

     <![LOG[Downloaded file from http://
     <SourceServerName>:8003/SCCM_BranchCache$/SS10000C/sccm?/install.wim to
     C:\_SMSTaskSequence\Packages\SS10000C\install.wim ]LOG]!>
     <time="14:24:33.329+420" date="06-26-2015"

<!-- p.142 -->

     component="ApplyOperatingSystem" context="" type="1" thread="1256"
     file="downloadcontent.cpp:1626">

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.143 -->

OS deployment methods with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

There are different methods that you can use to deploy an OS in your Configuration
Manager environment:

      Use PXE to deploy Windows over the network

      Use Software Center to deploy Windows over the network

      Use bootable media to deploy Windows over the network

      Use standalone media to deploy Windows without using the network

      Use multicast to deploy Windows over the network

      Create an image for an OEM in factory or a local depot

      Create a task sequence for non-OS deployments

      Deploy Windows to Go

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.144 -->

Use PXE to deploy Windows over the
network with Configuration Manager
09/02/2025

Applies to: Configuration Manager (current branch)

Preboot execution environment (PXE)-initiated OS deployments in Configuration Manager let
clients request and deploy operating systems over the network. For this deployment method,
you send the OS image and the boot images to a PXE-enabled distribution point.

  ７ Note

  When you create an OS deployment that targets only x64 BIOS computers, both the x64
  boot image and x86 boot image must be available on the distribution point.

You can use PXE-initiated OS deployments in the following scenarios:

     Refresh an existing computer with a new version of Windows

     Install a new version of Windows on a new computer (bare metal)

Complete the steps in one of the OS deployment scenarios, and then use the sections in this
article to prepare for PXE-initiated deployments.

  ２ Warning

  If you use PXE deployments, and configure device hardware with the network adapter as
  the first boot device, these devices can automatically start an OS deployment task
  sequence without user interaction. Deployment verification doesn't manage this
  configuration. While this configuration may simplify the process and reduce user
  interaction, it puts the device at greater risk for accidental reimage.

Starting in version 2006, PXE-based task sequences can download cloud-based content. The
PXE-enabled distribution point still requires the boot image, and the device needs an intranet
connection to the management point. It can then get additional content from a content-
enabled cloud management gateway (CMG). For more information, see Bootable media
support for cloud-based content.

Configure distribution points for PXE

<!-- p.145 -->

To deploy operating systems to Configuration Manager clients that make PXE boot requests,
configure one or more distribution points to accept PXE requests. Then the distribution point
responds to PXE boot requests, and determines the appropriate deployment action. For more
information, see Install or modify a distribution point.

  ７ Note

  When you configure a single PXE-enabled distribution point to support multiple subnets,
  it's not supported to use DHCP options. To allow the network to forward client PXE
  requests to PXE-enabled distribution points, configure IP helpers on the routers.

When you enable a PXE responder on a distribution point without Windows Deployment
Service, it can be on the same server as the DHCP service. When the PXE responder and DHCP
are on the same server, add the following settings to support this configuration:

     Set the DWord value DoNotListenOnDhcpPort to 1 in the following registry key:
      HKLM\Software\Microsoft\SMS\DP .

     Set DHCP option 60 to PXEClient .
     Restart the SCCMPXE and DHCP services on the server.

  ） Important

  An on-premises distribution point is required in the following scenarios:

     1. Responding to PXE boot requests.
     2. When using multicast.

Prepare a PXE-enabled boot image
To use PXE to deploy an OS, distribute both x86 and x64 PXE-enabled boot images to one or
more PXE-enabled distribution points.

     To enable PXE on a boot image, select Deploy this boot image from the PXE-enabled
     distribution point from the Data Source tab in the boot image properties.

     When you change the properties for the boot image, update and redistribute the boot
     image to distribution points. For more information, see Distribute content.

Manage duplicate hardware identifiers

<!-- p.146 -->

Configuration Manager may recognize multiple computers as the same device if they have
duplicate SMBIOS attributes or you use a shared network adapter. Mitigate these issues by
managing duplicate hardware identifiers in hierarchy settings. For more information, see
Manage duplicate hardware identifiers.

Create an exclusion list for PXE deployments

  ７ Note

  In some circumstances, the process to Manage duplicate hardware identifiers may be
  easier.

  The behaviors of each can cause different results in some scenarios. The exclusion list
  never boots a client with the listed MAC address, no matter what.

  The duplicate ID list doesn't use the MAC address to find the task sequence policy for a
  client. If it matches the SMBIOS ID, or if there's a task sequence policy for unknown
  machines, the client still boots.

When you deploy operating systems with PXE, you can create an exclusion list on each
distribution point. Add the MAC addresses to the exclusion list of the computers you want the
distribution point to ignore. Listed computers don't receive the deployment task sequences
that Configuration Manager uses for PXE deployment.

   1. Create a text file on the PXE-enabled distribution point. For example, name the file
     pxeExceptions.txt.

   2. Use a plain text editor, such as Notepad, to edit the file. Add the MAC addresses of the
     computers that the PXE-enabled distribution point should ignore. Separate the MAC
     address values by colons, and enter each address on a separate line. For example:
     01:23:45:67:89:ab

   3. Save the text file on the PXE-enabled distribution point. You can save it to any location on
     the server.

   4. Edit the registry on the PXE-enabled distribution point. Browse to the following registry
     path: HKLM\Software\Microsoft\SMS\DP . Create a MACIgnoreListFile string value. Add the
     full path to the text file on the PXE-enabled distribution point.

       ２ Warning

<!-- p.147 -->

       If you use the Registry Editor incorrectly, you might cause serious problems that may
       require you to reinstall Windows. Microsoft can't guarantee that you can solve
       problems that result from using the Registry Editor incorrectly. Use the Registry
       Editor at your own risk.

   5. After you make this registry change, restart the WDS service or PXE responder service.
     You don't need to restart the server.

RamDisk TFTP block size and window size
You can customize the RamDisk TFTP block and window sizes for PXE-enabled distribution
points. If you've customized your network, a large block or window size could cause the boot
image download to fail with a time-out error. The RamDisk TFTP block and window size
customizations allow you to optimize TFTP traffic when using PXE to meet your specific
network requirements. To determine what configuration is most efficient, test the customized
settings in your environment. For more information, see Customize the RamDisk TFTP block
size and window size on PXE-enabled distribution points.

Configure deployment settings
To use a PXE-initiated OS deployment, configure the deployment to make the OS available for
PXE boot requests. Configure available operating systems on the Deployment Settings tab in
the deployment properties. For the Make available to the following setting, select one of the
following options:

     Configuration Manager clients, media, and PXE

     Only media and PXE

     Only media and PXE (hidden)

Option 82 during PXE DHCP handshake
Configuration Manager supports option 82 during the PXE DHCP handshake with the PXE
responder without WDS. If you require option 82, make sure to use the PXE responder without
WDS. Configuration Manager doesn't support option 82 with WDS.

Deploy the task sequence

<!-- p.148 -->

Deploy the OS to a target collection. For more information, see Deploy a task sequence. When
you deploy operating systems by using PXE, you can configure whether the deployment is
required or available.

       Required deployment: Required deployments use PXE without any user intervention. The
       user can't bypass the PXE boot. However, if the user cancels the PXE boot before the
       distribution point responds, the OS isn't deployed.

       Available deployment: Available deployments require that the user is present at the
       destination computer. A user must press the F12 key to continue the PXE boot process. If
       a user isn't present to press F12, the computer boots into the current OS, or from the next
       available boot device.

You can redeploy a required PXE deployment by clearing the status of the last PXE deployment
assigned to a Configuration Manager collection or a computer. For more information on the
Clear Required PXE Deployments action, see Manage clients or Manage collections. This
action resets the status of that deployment and reinstalls the most recent required
deployments.

  ） Important

  The PXE protocol isn't secure. Make sure that the PXE server and the PXE client are located
  on a physically secure network, such as in a data center, to prevent unauthorized access to
  your site.

How the boot image is selected for PXE
When a client boots with PXE, Configuration Manager provides the client with a boot image to
use. Configuration Manager uses a boot image with an exact architecture match. If a boot
image with the exact architecture isn't available, Configuration Manager uses a boot image
with a compatible architecture.

The following list provides details about how a boot image is selected for clients booting with
PXE:

   1. Configuration Manager looks in the site database for the system record that matches the
       MAC address or SMBIOS of the client that's trying to boot.

         ７ Note

         If a computer that's assigned to a site boots to PXE for a different site, the policies
         aren't visible for the computer. For example, if a client is already assigned to site A,

<!-- p.149 -->

       the management point and distribution point for site B aren't able to access the
       policies from site A. The client doesn't successfully PXE boot.

  2. Configuration Manager looks for task sequences that are deployed to the system record
     found in step 1.

  3. In the list of task sequences found in step 2, Configuration Manager looks for a boot
     image that matches the architecture of the client that's trying to boot. If a boot image is
     found with the same architecture, that boot image is used.

     If it finds more than one boot image, it uses the highest or most recent task sequence
     deployment ID. In the case of a multi-site hierarchy, the higher letter site would take
     precedence in that string comparison. For example, if they're both matched otherwise, a
     year-old deployment from site ZZZ is selected over yesterday's deployment from site
     AAA.

  4. If a boot image isn't found with the same architecture, Configuration Manager looks for a
     boot image that's compatible with the architecture of the client. It looks in the list of task
     sequences found in step 2. For example, a 64-bit BIOS/MBR client is compatible with 64-
     bit boot images. UEFI clients are only compatible with matching architecture. A 64-bit
     UEFI client is compatible with only 64-bit boot images and Arm64 bit UEFI client is
     compatible with only Arm64 boot images.

  ） Important

  Starting with the ADK for Windows 11, version 22H2 the 32-bit versions of Windows PE
  are no longer included in the Windows PE add-ons. The last supported version of 32-bit
  Windows PE is available in the Windows PE add-on for Windows 10, version 2004.

Next steps
User experiences for OS deployment

<!-- p.150 -->

Use Software Center to deploy Windows
over the network with Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can make a task sequence that installs an OS available in Software Center. A user
can run a task sequence from Software Center for the following OS deployment
scenarios:

      Refresh an existing computer with a new version of Windows

      Upgrade Windows to the latest version

      Create a task sequence for non-OS deployments

Complete the steps in one of those OS deployment scenarios. Then use the following
sections to prepare for deployments that are available in Software Center.

Deploy the task sequence
Deploy the task sequence to a target collection. For more information, see Deploy a task
sequence.

On the Deployment Settings page of the deployment, for the Make available to the
following setting, select one of the following options:

      Only Configuration Manager Clients

      Configuration Manager clients, media and PXE

Also configure whether the deployment is required or available:

      Required deployment: Required deployments make the task sequence available in
      Software Center. It automatically starts at the configured deadline.

      Available deployment: The task sequence is available in Software Center, and a
      user can install it on demand.

After you create the deployment, clients in the target collection will show the task
sequence in Software Center.

<!-- p.151 -->

  ７ Note

  If multiple users are signed in on the device, task sequence deployments might not
  appear in Software Center until other users are signed out.

Next steps
User experiences for OS deployment

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.152 -->

Use bootable media to deploy Windows
over the network with Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Bootable media only includes the boot image and a pointer to the task sequence. It
downloads the OS image and other referenced content from the network. Since the
bootable media doesn't contain much content, you can update the task sequence and
most content without having to replace the media.

Deploy operating systems over the network with boot media in the following scenarios:

      Refresh an existing computer with a new version of Windows

      Install a new version of Windows on a new computer (bare metal)

      Replace an existing computer and transfer settings

Complete the steps in one of the OS deployment scenarios and then use the following
sections to use bootable media to deploy the OS.

Configure deployment settings
When you use bootable media to start the OS deployment process, configure the task
sequence deployment to make the OS available to the media. Set this option on the
Deployment Settings page of the deployment. For the Make available to the following
setting, select one of the following options:

      Configuration Manager clients, media, and PXE

      Only media and PXE

      Only media and PXE (hidden)

For more information, see Deploy a task sequence.

Create the bootable media

<!-- p.153 -->

When you create bootable media, specify whether it's a USB flash drive or CD/DVD set.
The computer that starts the media must support the option that you choose as a
bootable drive. For more information, see Create bootable media.

Install the OS from bootable media
To install the OS, insert the bootable media, and then power on the computer.

Support for cloud-based content
Starting in version 2006, bootable media can download cloud-based content. For
example, you send a USB key to a user at a remote office to reimage their device. Or an
office that has a local PXE server, but you want devices to prioritize cloud services as
much as possible. Instead of further taxing the WAN to download large OS deployment
content, boot media and PXE deployments can now get content from cloud-based
sources.

For more information, see Bootable media support for cloud-based content.

Next steps
User experiences for OS deployment

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.154 -->

Use standalone media to deploy
Windows without using the network
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Standalone media in Configuration Manager contains everything required to deploy an
OS on a computer. The media includes the boot image, OS image, task sequence policy,
applications, drivers, and more. Standalone media deployments let you deploy
operating systems in the following conditions:

      In environments where it isn't practical to copy an OS image or other large
      packages over the network.

      In environments without network connectivity or low-bandwidth network
      connectivity.

Use standalone media in the following OS deployment scenarios:

      Refresh an existing computer with a new version of Windows

      Install a new version of Windows on a new computer (bare metal)

      Upgrade Windows to the latest version

Complete the steps in one of these OS deployment scenarios. Then use the following
sections to prepare for and create the standalone media.

Unsupported task sequence actions
When you use standalone media, Configuration Manager doesn't support the following
actions in the task sequence:

      The Auto Apply Drivers step. Automatic application of device drivers from the
      driver catalog isn't supported. To make a specific set of drivers available to
      Windows Setup, use the Apply Driver Package step.

      Installing software updates.

      Installing software before deploying the OS.

      Associating users with the destination computer for user device affinity.

<!-- p.155 -->

     Dynamic package installs with the Install Package step.

     Dynamic application installs with the Install Application step.

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

Configure deployment settings
When you use standalone media to start the OS deployment process, configure the
deployment to make the OS available to media. On the Deployment Settings page of
the deployment, for the Make available to the following setting, select one of the
following options:

<!-- p.156 -->

     Configuration Manager clients, media, and PXE

     Only media and PXE

     Only media and PXE (hidden)

Create the standalone media
You can specify whether the standalone media is a USB flash drive or CD/DVD set. The
computer that will start the media must support the option that you choose as a
bootable drive. For more information, see Create standalone media.

Install the OS from standalone media
To install the OS, insert the standalone media to the computer, and then power it on.

Next steps
User experiences for OS deployment

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.157 -->

Use multicast to deploy Windows over
the network with Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Multicast is a network optimization method that you can use when multiple clients are
likely to download the same OS image at the same time. When you use multicast,
multiple computers simultaneously download the OS image as it's multicast by the
distribution point. This behavior is instead of each client downloading a copy of the
image over a separate connection from the distribution point.

Deploy operating systems over the network by using multicast in the following OS
deployment scenarios:

      Refresh an existing computer with a new version of Windows

      Install a new version of Windows on a new computer (bare metal)

Complete the steps in one of these OS deployment scenarios. Then use the following
sections to support multicast.

Configure distribution points for multicast
To use multicast, configure at least one distribution point to support multicast. For more
information, see Install and configure distribution points.

For a list of ports required to support multicast, see Ports.

Prepare an OS image for multicast
You need to configure the OS image to support multicast. For more information, see
Prepare the OS image for multicast deployments.

Deploy the task sequence
Deploy the OS to a target collection. For more information, see Deploy a task sequence.

<!-- p.158 -->

Next steps
User experiences for OS deployment

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.159 -->

Create an image for an OEM in factory
or a local depot with Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Prestaged media deployments in Configuration Manager let you deploy an OS to a
computer that isn't fully provisioned. The prestaged media is a Windows image (WIM)
file. The manufacturer (OEM) can install it on a bare-metal computer, or you can use it in
a staging center that's separate from your production environment.

This method of deployment can reduce network traffic because the boot image and OS
image are already on the destination computer. You can specify applications, packages,
and driver packages to also include in the prestaged media. After it installs the OS on
the computer, the task sequence first checks the prestaged cache for applications,
packages, or driver packages. If it can't find the necessary content, or there is a newer
revision available online, the task sequence downloads the content from a distribution
point.

Use prestaged media in the following OS deployment scenarios:

      Install a new version of Windows on a new computer (bare metal)

      Replace an existing computer and transfer settings

Complete the steps in one of these OS deployment scenarios. Then use the following
sections to prepare for and create the prestaged media.

Configure deployment settings
On the Deployment Settings page of the deployment, for the Make available to the
following setting, select one of the following options:

      Configuration Manager clients, media, and PXE

      Only media and PXE

      Only media and PXE (hidden)

<!-- p.160 -->

Create the prestaged media
Create the prestaged media file to send to the OEM or your local depot. For more
information, see Create prestaged media with Configuration Manager.

Send the prestaged media file
Send the media to the OEM or your local depot to prestage on the computers. They
apply the image file to a formatted hard disk on the computer.

Deliver the computer
When you deliver the computer to a user, and turn it on for the first time:

   1. The computer starts with the prestaged boot image.

   2. It checks a hash on the prestaged media to make sure it's valid.

   3. The computer connects to the management point for available task sequences to
     complete the process.

Next steps
User experiences for OS deployment

Feedback
Was this page helpful?      Yes    No

Provide product feedback
