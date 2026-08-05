---
title: "OS deployment documentation — pages 1-40"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Tell us about your PDF experience. OS deployment documentation Use Configuration Manager to deploy Windows via different methods and automate tasks. About OS deployment ｅ OVERVIEW Introduction to OS deployment Infrastructure requirements ｐ CONCEPT Prepare for OS deployment OS de"
---

# OS deployment documentation — pages 1-40

<!-- p.1 -->

                                                           Tell us about your PDF experience.

OS deployment documentation
Use Configuration Manager to deploy Windows via different methods and automate tasks.

  About OS deployment

  ｅ OVERVIEW
  Introduction to OS deployment

  Infrastructure requirements

  ｐ CONCEPT
  Prepare for OS deployment

  OS deployment scenarios

  OS deployment methods

  Get started

  ｃ HOW-TO GUIDE
  Manage task sequences

  Create an OS upgrade task sequence

  Create a phased deployment

  Deploy a task sequence

  Debug a task sequence

  Technical reference

  ｉ REFERENCE
  Use the task sequence editor

  About task sequence steps

  How to use task sequence variables

<!-- p.2 -->

Task sequence variable reference

<!-- p.3 -->

Introduction to operating system
deployment in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can use Configuration Manager to deploy operating systems in many ways. Use the
information in this section to understand how to deploy operating systems and
automate tasks.

The operating system deployment process
Configuration Manager provides several methods that you can use to deploy an
operating system. There are several actions that you must take regardless of the
deployment method that you use:

      Identify Windows device drivers that are required to start the boot image or install
      the operating system image that you have to deploy.

      Identify the boot image that you want to use to start the destination computer.

      Use a task sequence to capture an image of the operating system that you'll
      deploy. Alternatively, you can use a default operating system image.

      Distribute the boot image, operating system image, and any related content to a
      distribution point.

      Create a task sequence with the steps to deploy the boot image and the operating
      system image.

      Deploy the task sequence to a collection of computers.

      Monitor the deployment.

Operating system deployment scenarios
There are many operating system deployment scenarios in Configuration Manager that
you can choose from depending on your environment and the purpose for the
operating system installation. For example, you can partition and format an existing
computer with a new version of Windows or upgrade Windows to the latest version. To
help you determine the deployment method that meets your needs, review Scenarios to

<!-- p.4 -->

deploy enterprise operating systems. You can choose from the following operating
system deployment scenarios:

     Upgrade Windows to the latest version

     Refresh an existing computer with a new version of Windows

     Install a new version of Windows on a new computer (bare metal)

     Replace an existing computer and transfer settings

Methods to deploy operating systems
There are several methods that you can use to deploy operating systems to
Configuration Manager client computers.

     PXE initiated deployments: PXE-initiated deployments let client computers request
     a deployment over the network. In this method of deployment, the operating
     system image and a Windows PE boot image are sent to a distribution point that is
     configured to accept PXE boot requests. For more information, see Use PXE to
     deploy Windows over the network with Configuration Manager.

     Make operating systems available in Software Center: You can deploy an
     operating system and make it available in the Software Center. Configuration
     Manager clients can initiate the operating system installation from Software
     Center. For more information, see Replace an existing computer and transfer
     settings.

     Multicast deployments: Multicast deployments conserve network bandwidth by
     concurrently sending data to multiple clients instead of sending a copy of the data
     to each client over a separate connection. In this method of deployment, the
     operating system image is sent to a distribution point. This in turn deploys the
     image when client computers request the deployment. For more information, see
     Use multicast to deploy Windows over the network.

     Bootable media deployments: Bootable media deployments let you deploy the
     operating system when the destination computer starts. When the destination
     computer starts, it retrieves the task sequence, the operating system image, and
     any other required content from the network. Because that content isn't included
     on the media, you can update the content without having to re-create the media.
     For more information, see Create bootable media.

     Stand-alone media deployments: Stand-alone media deployments let you deploy
     operating systems in the following conditions:

<!-- p.5 -->

        In environments where it isn't practical to copy an operating system image or
        other large packages over the network.

        In environments without network connectivity or low bandwidth network
        connectivity.

        For more information, see Create stand-alone media.

     Pre-staged media deployments: Pre-staged media deployments let you deploy an
     operating system to a computer that isn't fully provisioned. The pre-staged media
     is a Windows Imaging Format (WIM) file that can be installed on a bare-metal
     computer by the manufacturer or at an enterprise staging center that isn't
     connected to the Configuration Manager environment.

     Later in the Configuration Manager environment, the computer starts by using the
     boot image provided by the media, and then connects to the site management
     point for available task sequences that complete the download process. This
     method of deployment can reduce network traffic because the boot image and
     operating system image are already on the destination computer. You can specify
     applications, packages, and driver packages to include in the pre-staged media.
     For more information, see Create prestaged media.

Boot images
A boot image in Configuration Manager is a Windows PE (WinPE) image that is used
during an operating system deployment. Boot images are used to start a computer in
WinPE, which is a minimal operating system with limited components and services that
prepare the destination computer for Windows installation. Configuration Manager
provides two boot images: One to support x86 platforms and one to support x64
platforms. These are considered default boot images. Boot images that you create and
add to Configuration Manager are considered custom images. Default boot images can
be automatically replaced when you update Configuration Manager. For more
information about boot images, see Manage boot images.

Operating system images
Operating system images in Configuration Manager are stored in the Windows Imaging
(WIM) file format and represent a compressed collection of reference files and folders
that are required to successfully install and configure an operating system on a
computer. For all operating system deployment scenarios, you must select an operating
system image. You can use the default operating system image or build the operating

<!-- p.6 -->

system image from a reference computer that you configure. For more information, see
Manage operating system images.

Operating system upgrade packages
Operating system upgrade packages are used to upgrade an operating system and are
setup-initiated operating system deployments. You import operating system upgrade
packages to Configuration Manager from a DVD or mounted ISO file. For more
information, see Manage operating system upgrade packages.

Media to deploy operating systems
You can create several kinds of media that can be used to deploy operating systems.
This includes capture media that is used to capture operating system images and stand-
alone, pre-staged, and bootable media that is used to deploy an operating system. By
using media, you can deploy operating systems on computers that do not have a
network connection or that have a low bandwidth connection to your Configuration
Manager site. For more information about how to use media, see Create task sequence
media.

Device drivers
You can install device drivers on destination computers without including them in the
operating system image that is being deployed. Configuration Manager provides a
driver catalog that contains references to all the device drivers that you import into
Configuration Manager. The driver catalog is located in the Software Library workspace
and consists of two nodes: Drivers and Driver Packages. The Drivers node lists all the
drivers that you have imported into the driver catalog. You can use this node to discover
the details about each imported driver, to change what driver package or boot image a
driver belongs to, to enable or disable a driver, and more. For more information, see
Manage drivers.

Save and restore user state
When you deploy operating systems, you can save the user state from the destination
computer, deploy the operating system, and then restore the user state after the
operating systems is deployed. This process is typically used when you install the
operating system on a Configuration Manager client computer.

<!-- p.7 -->

The user state information is captured and restored by using task sequences. When the
user state information is captured, the information can be stored in one of the following
ways:

        You can store the user state data remotely by configuring a state migration point.
        The Capture task sequence sends the data to the state migration point. Then, after
        the operating system is deployed, the Restore task sequence retrieves the data and
        restores the user state on the destination computer.

        You can store the user state data locally to a specific location. In this scenario, the
        Capture task sequence copies the user data to a specific location on the
        destination computer. Then, after the operating system is deployed, the Restore
        task sequence retrieves the user data from that location.

        You can specify hard links that can be used to restore the user data to its original
        location. In this scenario, the user state data remains on the drive when the old
        operating system is removed. Then, after the operating system is deployed, the
        Restore task sequence uses the hard links to restore the user state data to its
        original location.

        For more information Manage user state.

Deploy to unknown computers
You can deploy an operating system to computers that aren't managed by
Configuration Manager. There's no record of these computers in the Configuration
Manager database. These computers are referred to as unknown computers. Unknown
computers include the following:

        A computer where the Configuration Manager client isn't installed

        A computer that isn't imported into Configuration Manager

        A computer that isn't discovered by Configuration Manager

        For more information, see Prepare for unknown computer deployments.

Associate users with a computer
When you deploy an operating system, you can associate users with the destination
computer to support user device affinity actions. When you associate a user with the
destination computer, the administrative user can later perform actions on whichever
computer is associated with that user, such as deploying an application to the computer

<!-- p.8 -->

of a specific user. However, when you deploy an operating system, you can't deploy the
operating system to the computer of a specific user. For more information, see
Associate users with a destination computer.

Use task sequences to automate steps
You can create task sequences to perform various tasks within your Configuration
Manager environment. The actions of the task sequence are defined in the individual
steps of the sequence. When the task sequence is run, the actions of each step are
performed at the command-line level without requiring user intervention. You can use
task sequences for the following:

     Create a task sequence to install an operating system

     Create a task sequence for non-operating system deployments

     Create a task sequence to capture an operating system

     Create a task sequence to capture and restore user state

     Create a custom task sequence

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.9 -->

Infrastructure requirements for OS
deployment in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

OS deployment in Configuration Manager has external dependencies as well as
dependencies within the product. Use this article to help you prepare the infrastructure
for OS deployment.

Dependencies external to Configuration
Manager
This section provides information about external tools, installation kits, and OS versions
that are required to deploy operating systems in Configuration Manager.

Windows ADK
The Windows Assessment and Deployment Kit (ADK) is a set of tools and
documentation that support the configuration and deployment of Windows.
Configuration Manager uses the Windows ADK to automate actions such as installing
Windows, capturing images, and migrating user profiles and data.

For more information, see the following articles:

      Support for the Windows ADK in Configuration Manager

      Download the Windows ADK

        ） Important

        Make sure to download both the Windows ADK and the Windows PE add-on
        for the ADK.

      Windows ADK scenarios for IT Pros

Site systems
The Windows ADK is a prerequisite for the following site systems servers:

<!-- p.10 -->

     The site server of the top-level site in the hierarchy

     The site server of each primary site in the hierarchy

     Every instance of the SMS Provider

  ７ Note

  Manually install the Windows ADK on each site server before you install the
  Configuration Manager site.

Windows ADK features
Install the following features of the Windows ADK:

     User State Migration Tool (USMT)

        ７ Note

        USMT isn't required on the SMS Provider.

     Windows Deployment Tools

     Windows Preinstallation Environment (Windows PE)

        ） Important

        Windows PE is a separate installer. Otherwise there's no functional difference
        from earlier versions of the Windows ADK.

For a list of the versions of the Windows ADK that you can use with different versions of
Configuration Manager, see Support for the Windows ADK.

User State Migration Tool (USMT)
Configuration Manager uses a USMT package that includes the USMT source files to
capture and restore the user state as part of your OS deployment. Configuration
Manager setup at the top-level site automatically creates the USMT package. USMT
captures user state from supported versions of Windows.

For more information, see the following articles:

<!-- p.11 -->

     Manage user state with Configuration Manager

     Common migration scenarios for USMT

Windows PE
Windows PE is used for boot images to start a computer. It's a Windows version with
limited services that's used during the pre-installation and deployment of Windows. For
more information about boot images, see Manage boot images.

Windows Server Update Services (WSUS)
WSUS is required for the software update point, which is required to install software
updates during OS deployment. For more information, see Install a configure a software
update point.

Internet Information Services (IIS) on the site system
servers
IIS is required for the distribution point, state migration point, and management point.
For more information, see Site and site system prerequisites.

Windows Deployment Services (WDS)
You can use WDS for PXE deployments, or you can enable PXE on a distribution point
without WDS. For more information, see PXE provider options.

Dynamic Host Configuration Protocol (DHCP)
DHCP is required for PXE deployments. You must have a functioning DHCP server with
an active host to deploy operating systems by using PXE. For more information about
PXE deployments, see Use PXE to deploy Windows over the network.

Windows device drivers
Windows device drivers can be used when you install the OS on the destination
computer. They're also used when you run Windows PE in a boot image. For more
information, see Manage drivers.

<!-- p.12 -->

Configuration Manager dependencies
This section provides information about Configuration Manager OS deployment
prerequisites.

OS image
OS images in Configuration Manager are stored in the Windows Imaging (WIM) file
format. They represent a compressed collection of reference files and folders. These
images are required to successfully install and configure an OS on a computer. For more
information, see Manage OS images.

Driver catalog
To deploy a device driver, import the device driver, enable it, and make it available on a
distribution point that the Configuration Manager client can access. For more
information about the driver catalog, see Manage drivers.

Management point
Management points transfer information between clients and the Configuration
Manager site. The client uses a management point to run the task sequence to complete
the OS deployment. For more information about task sequences, see Planning
considerations for automating tasks.

Distribution point
Distribution points are used in most deployments to store the data that's used to deploy
an OS, such as the image or driver packages. Task sequences typically retrieve data from
a distribution point to deploy the OS. For more information about how to install
distribution points and manage content, see Manage content and content infrastructure.

PXE-enabled distribution point
To deploy PXE-initiated deployments, configure a distribution point to accept PXE
requests from clients. For more information, see Configure a distribution point.

Multicast-enabled distribution point

<!-- p.13 -->

To optimize your OS deployments by using multicast, configure a distribution point to
support multicast. For more information, see Configure a distribution point.

State migration point
When you capture and restore user state data for side-by-side and refresh deployments,
configure a state migration point to store the user state data on another computer.

For more about how to configure the state migration point, see State migration point.

For more information about how to capture and restore user state, see Manage user
state.

Reporting services point
To use Configuration Manager reports for OS deployments, install and configure a
reporting point. For more information, see Introduction to reporting.

Security permissions for OS deployments
The Operating System Deployment Manager security role is a built-in role that you
can't change. However, you can copy the role, make changes, and then save these
changes as a new custom security role. Here are some of the permissions that apply
directly to OS deployments:

         Boot Image Package: Create, Delete, Modify, Modify Folder, Move Object, Read,
         Set Security Scope

         Device Drivers: Create, Delete, Modify, Modify Folder, Modify Report, Move
         Object, Read, Run Report

         Driver Package: Create, Delete, Modify, Modify Folder, Move Object, Read, Set
         Security Scope

         Operating System Image: Create, Delete, Modify, Modify Folder, Move Object,
         Read, Set Security Scope

         Operating System Upgrade Package: Create, Delete, Modify, Modify Folder, Move
         Object, Read, Set Security Scope

         Task Sequence Package: Create, Create Task Sequence Media, Delete, Modify,
         Modify Folder, Modify Report, Move Object, Read, Run Report, Set Security Scope

For more information, see Create custom security roles.

<!-- p.14 -->

Security scopes for OS deployments
Use security scopes to provide administrative users with access to the securable objects
used in OS deployments, such as OS and boot images, driver packages, and task
sequence packages. For more information, see Security scopes.

PXE provider options
You can use Windows Deployment Services (WDS) on the same server as the distribution
points that you configure to support PXE or multicast. WDS is included in the server OS.
With this configuration, WDS is the service that performs the PXE boot. When the
distribution point is installed and enabled for PXE, Configuration Manager installs a
provider into WDS that uses the WDS PXE boot functions.

You can also enable PXE on a distribution point without WDS. For more information, see
the Enable a PXE responder without Windows Deployment Service option in Install
and configure distribution points.

WDS requirements
     The WDS installation on the server requires that the administrator is a member of
     the local Administrators group.

     The WDS server must be either a member of an Active Directory domain or a
     domain controller for an Active Directory domain. All Windows domain and forest
     configurations support WDS.

     If the provider is installed on a remote server, install WDS on the site server and
     the remote provider.

  ７ Note

  If the server requires a restart, the installation of WDS might fail.

Considerations when you have WDS and DHCP on the
same server
If you plan to co-host the distribution point on a server running DHCP, consider the
following configuration issues:

<!-- p.15 -->

    You need a functioning DHCP server with an active scope. WDS uses PXE, which
    requires a DHCP server.

    A DNS server is required to run WDS.

    The following UDP ports must be open on the WDS server:

        Port 67 (DHCP)

        Port 69 (TFTP)

        Port 4011 (PXE)

          ７ Note

          If DHCP authorization is required on the server, you need DHCP client port
          68 to be open on the server.

    DHCP and WDS both require port number 67. If you co-host WDS and DHCP, you
    can move DHCP or the distribution point that's configured for PXE to a separate
    server. Or, you can use the following procedure to configure the WDS server to
    listen on a different port.

How to configure the WDS server to listen on a different port

  1. Modify the following registry key:

    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WDSServer\Providers\WDSPX

    E

  2. Set the registry value UseDHCPPorts to 0 .

  3. For the new configuration to take effect, run the following command on the server:

    WDSUTIL /Set-Server /UseDHCPPorts:No /DHCPOption60:Yes

 ７ Note

 When you enable a PXE responder on a distribution point without WDS, it can be
 on the same server as the DHCP service. For more information, see Configure at
 least one distribution point to accept PXE requests.

<!-- p.16 -->

Supported operating systems
All Windows operating systems listed as supported clients in Supported operating
systems for clients and devices are supported for OS deployment.

Supported disk configurations
Configuration Manager supports capturing an OS image only from computers that are
configured with simple volumes. The following table lists the hard disk configurations
that Configuration Manager OS deployment supports on reference and destination
computers:

                                                                         ﾉ     Expand table

 Reference computer hard disk                Destination computer hard disk
 configuration                               configuration

 Basic disk                                  Basic disk

 Simple volume on a dynamic disk             Simple volume on a dynamic disk

Configuration Manager doesn't support the following hard disk configurations:

     Spanned volumes

     Striped volumes (RAID 0)

     Mirrored volumes (RAID 1)

     Parity volumes (RAID 5)

If the reference disk has a basic disk, you can't capture and apply the image to a
destination computer with a dynamic disk.

Next steps
     Prepare site system roles for OS deployments
     Prepare for OS deployment

Feedback

<!-- p.17 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.18 -->

Plan for automating tasks in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can create task sequences to automate tasks in your Configuration Manager
environment. These tasks range from capturing an OS on a reference computer to
deploying the OS to one or more destination computers. The actions of the task
sequence are defined in the individual steps of the sequence. When the task sequence
runs, it runs the actions of each step at the command-line level in the Local System
context. This behavior means the task sequence runs fully automated with no user
intervention.

Task sequence steps and actions
Steps are the basic components of a task sequence. They can include commands such
as:

      Configure and capture the OS of a reference computer
      Install Windows, hardware drivers, the Configuration Manager client, and software
      on the destination computer

The actions of the step define the commands of a task sequence step. There are two
types of actions:

      An action that you define by using a command-line string is referred to as a
      custom action
      An action that's predefined by Configuration Manager is referred to as a built-in
      action.

A task sequence can do any combination of custom and built-in actions.

Task sequence steps can also include conditions that control how the step behaves.
These behaviors include stopping the task sequence, or continuing the task sequence if
an error occurs. One type of condition is a task sequence variable. For example, use the
SMSTSLastActionRetCode variable to test the condition of the previous step. Add
conditions to a single step or a group of steps.

The task sequence processes steps sequentially. This sequence includes the action of the
step and any conditions on the step. When Configuration Manager starts to process a

<!-- p.19 -->

task sequence step, it doesn't start the next step until the previous action is complete.

A task sequence is considered complete when:

     All its steps are complete.
     A failed step causes Configuration Manager to stop running the task sequence
     before all its steps are completed.

For example, if the step of a task sequence can't locate a referenced image or package
on a distribution point, the task sequence includes a broken reference. Configuration
Manager stops running the task sequence at that point, unless the failed step has a
condition to continue when an error occurs.

  ） Important

  By default, a task sequence fails after one step or action fails. If you want the task
  sequence to continue even when a step fails, edit the task sequence, switch to the
  Options tab, and then select Continue on error.

For more information about the steps that can be added to a task sequence, see Task
sequence steps.

Task sequence groups
You can group multiple steps within a task sequence. A task sequence group consists of
a name, an optional description, and any optional conditions. The task sequence
evaluates the group conditions as a unit before it continues with the next step. Nest
groups within each other, or include a mixture of steps and subgroups. Groups are
useful for combining multiple steps that share a common condition.

Assign a name to task sequence groups. It doesn't have to be unique. You can also
provide an optional description for the task sequence group.

  ） Important

  By default, a task sequence group fails when any step or embedded group within
  the group fails. If you want the task sequence to continue when a step or
  embedded group fails, set the Continue on error option on the step or group.

The following table shows how the Continue on error option works when you group
steps.

<!-- p.20 -->

In this example, there are two groups of task sequences that include three task
sequence steps each.

                                                                              ﾉ   Expand table

 Task sequence group or step                    Continue on error setting

 Task sequence group 1                          Continue on error selected.

 Task sequence step 1                           Continue on error selected.

 Task sequence step 2                           Not set.

 Task sequence step 3                           Not set.

 Task sequence group 2                          Not set.

 Task sequence step 4                           Not set.

 Task sequence step 5                           Not set.

 Task sequence step 6                           Not set.

     If task sequence step 1 fails, the task sequence continues with task sequence step
     2.

     If task sequence step 2 fails, the task sequence doesn't run task sequence step 3.
     Because task sequence group 1 is configured to Continue on error, the task
     sequence continues to task sequence group 2. It runs task sequence step 4 next.

     If task sequence step 4 fails, no more steps are run. The task sequence fails
     because the Continue on error setting isn't configured for task sequence group 2.

Add child task sequences to a task sequence
Add a new task sequence step that runs another task sequence. This step creates a
parent-child relationship between the task sequences. Using this step allows you to
create more modular task sequences that you can reuse.

For more information, see Run Task Sequence.

  ７ Note

<!-- p.21 -->

  Configuration Manager doesn't enable this optional feature by default. You must
  enable this feature before using it. For more information, see Enable optional
  features from updates.

Task sequence variables
Task sequence variables are a set of name and value pairs. They supply configuration
and OS deployment settings for computer, OS, and user state configuration tasks on a
Configuration Manager client. Task sequence variables provide a mechanism to
configure and customize the steps in a task sequence.

When you run a task sequence, it stores many of the task sequence settings as
environment variables. You can access or change the values of built-in task sequence
variables. You can also create new task sequence variables to customize the way a task
sequence runs on a destination computer.

Use task sequence variables to do the following actions:

     Configure settings for a task sequence action

     Supply command-line arguments for a task sequence step

     Evaluate a condition that determines whether a task sequence step or group runs

     Provide values for custom scripts used in a task sequence

For example, you have a task sequence that includes a Join Domain or Workgroup task
sequence step. Deploy the task sequence to different collections, where the membership
of the collection is determined by domain membership. Specify a per-collection task
sequence variable for each collection's domain name. Then use that task sequence
variable to supply the appropriate domain name in the task sequence.

For more information, see How to use task sequence variables.

Create a task sequence
Create task sequences by using the Create Task Sequence Wizard. The wizard can create
built-in task sequences that do specific tasks or custom task sequences that can do
many different tasks. The wizard lets you create the following types of task sequences:

     Install an existing OS image on a destination computer

     Build and capture an OS image of a reference computer

<!-- p.22 -->

     Upgrade Windows with an OS upgrade package on a destination computer

     Create a custom task sequence that does a customized task or specialized OS
     deployment

For more information, see Create a task sequence to install an OS.

Edit a task sequence
Edit the task sequence by using the Task Sequence Editor. The editor can make the
following changes to the task sequence:

     Add or remove steps from the task sequence

     Change the order of the steps of the task sequence

     Add or remove groups of steps

     Specify whether the task sequence continues when an error occurs

     Add conditions to the steps and groups of a task sequence

  ） Important

  If the task sequence has any unassociated references to an object as a result of the
  edit, the editor requires you fix the reference before it can close. Possible actions
  include:

          Correct the reference
          Delete the unreferenced object from the task sequence
          Temporarily disable the failed task sequence step until the broken reference is
          corrected or removed

For more information about how to edit task sequences, see Use the task sequence
editor.

Deploy a task sequence
Deploy a task sequence to destination computers that are in any Configuration Manager
collection. Use the built-in All Unknown Computers collection to deploy operating
systems to unknown computers. You can't deploy a task sequence to user collections.

<!-- p.23 -->

  ） Important

  Don't deploy task sequences that install operating systems to inappropriate
  collections. Be sure that the collection to which you deploy the task sequence
  includes only those computers where you want to install the OS. To help prevent
  unwanted OS deployments, configure settings for high-risk deployments. For more
  information, see Settings to manage high-risk deployments.

Each destination computer that receives the task sequence runs the task sequence
according to the settings specified in the deployment. The task sequences itself doesn't
contain associated files or programs. Any files that a task sequence references must
already be present on the destination computer or stored on a distribution point that
clients can access.

  ７ Note

  The task sequence installs packages that are referenced by programs, even if the
  program or package is already installed on the destination computer.

  If the task sequence installs an application, the application installs only if the
  requirement rules for the application are met, and the application isn't already
  installed, based on the detection method that's specified for the application.

The Configuration Manager client runs a task sequence deployment when it downloads
client policy. To trigger this action rather than wait until the next polling cycle, see
Initiate policy retrieval for a Configuration Manager client.

When you deploy task sequences to Windows Embedded devices that are enabled with
a write filter, you can specify whether to disable the write filter on the device during the
deployment and then restart the device after the deployment. If the write filter isn't
disabled, the task sequence is deployed to a temporary overlay and it won't be available
when the device restarts.

  ７ Note

  When you deploy a task sequence to a Windows Embedded device, ensure that the
  device is a member of a collection that has a configured maintenance window. This
  allows you to manage when the write filter is disabled and enabled, and when the
  device restarts.

<!-- p.24 -->

  If clients download task sequences outside of a maintenance window, the task
  sequence is downloaded twice. In this scenario, the client downloads the task
  sequence, disables the write filter, restarts the computer, and then downloads the
  task sequence again. This behavior is because the task sequence was originally
  downloaded to the temporary overlay, which is cleared when the device restarts.

For more information about how to deploy task sequences, see the Deploy a task
sequence.

Export and import
Configuration Manager lets you export and import task sequences. When you export a
task sequence, you can include the objects that are referenced by the task sequence.

For more information, see Export and import task sequences.

Run a task sequence
Task sequences always run by using the Local System account. When the task sequence
runs, the Configuration Manager client first checks for any referenced packages before it
starts the steps of the task sequence. If it can't validate or download a referenced
package, the task sequence returns an error for the associated task sequence step.

  ７ Note

  The task sequence step Run Command Line provides the ability to run a command
  as a different account.

If you configure a task sequence deployment to download and run, the Configuration
Manager client downloads all dependent content to its cache. If the client cache size is
too small or the content can't be found, the task sequence fails. The client generates a
status message.

You can also specify that the client downloads the content only when it's required. To do
this action, select Download content locally when needed by running task sequence in
the task sequence deployment. Another option is to Run program from distribution
point. With this option, the client installs the files directly from the distribution point
without downloading them into the cache first.

<!-- p.25 -->

When you configure the task sequence deployment as Available, if the client can't
locate dependent content for the task sequence, it immediately sends an error. For a
Required deployment, the Configuration Manager client waits in this situation. It retries
to download the content until the deadline, in case the content isn't yet replicated to a
content location that the client can access.

When a task sequence completes successfully or fails, Configuration Manager records
this state in the client history.

Once a task sequence starts on a computer, you can't cancel or stop it.

  ） Important

  If a task sequence step requires the computer to restart, the client must be able to
  boot to a formatted disk partition. Otherwise, the task sequence fails regardless of
  any error handling that you specify in the task sequence.

When a dependent object of a task sequence is updated to a newer version, any task
sequence that references the package is automatically updated. It references the newest
version, no matter how many updates you've deployed.

Use maintenance windows
You can specify when the task sequence can run by defining a maintenance window for
the device collection. You configure maintenance windows with a start date, a start and
finish time, and a recurrence pattern. When you set the schedule for the maintenance
window, you can specify that the maintenance window applies only to task sequences.
For more information, see How to use maintenance windows.

  ） Important

  When you configure a maintenance window to run a task sequence, once the task
  sequences starts it continues to run even if the maintenance window closes.

If a device has more than one maintenance window applied, the client may ignore an All
deployments maintenance window. Starting in version 1810, use the following client
setting to control this behavior: Enable installation of software updates in "All
deployments" maintenance window when "Software Update" maintenance window is
available. For more information, see About client settings

<!-- p.26 -->

Task sequences and the network access account

  ） Important

  Some OS deployment scenarios don't require use of the network access account.
  For more information, see Enhanced HTTP.

Although task sequences run only in the context of the Local System account, you might
need to configure the network access account in the following circumstances:

     If the task sequence tries to access Configuration Manager content on distribution
     points. Correctly configure the network access account, or the task sequence will
     fail.

     When you use a boot image to initiate an OS deployment. In this case,
     Configuration Manager uses the Windows PE environment, which isn't a full OS.
     The Windows PE environment uses an automatically generated, random name that
     isn't a member of any domain. If you don't correctly configure the network access
     account, the computer can't access the required content for the task sequence.

  ７ Note

  The network access account is never used as the security context for running
  programs, installing applications, installing updates, or running task sequences. The
  network access account is only used to access the associated resources on the
  network.

For more information about the network access account, see Network access account.

Enhanced HTTP
When you enable Enhanced HTTP, the following scenarios don't require a network
access account to download content from a distribution point:

     Task sequences running from boot media or PXE
     Task sequences running from Software Center

These task sequences can be for OS deployment or custom. It's also supported for
workgroup computers.

For more information, see Enhanced HTTP.

<!-- p.27 -->

  ７ Note

  The following OS deployment scenarios still require the use of a network access
  account:

        The task sequence deployment option, Access content directly from a
        distribution point when needed by the running task sequence
        The Request State Store step option, If computer account fails to connect to
        a state store, use the network access account
        When connecting with an untrusted domain or across Active Directory forests
        The Apply OS Image step option, Access content directly from the
        distribution point
        The task sequence advanced setting to Run another program first
        Multicast

Create media
You can write task sequences and their related files and dependencies to several types
of media. Configuration Manager supports removable media such as a DVD or a USB
flash drive for capture, stand-alone, and bootable media. Prestaged media uses a
Windows image (WIM) file.

When you create media, specify a password to control access. Then a person must enter
the password at the target computer to run the task sequence.

When you run a task sequence from media, the specified processor architecture of the
media isn't recognized. If the specified architecture doesn't match the target computer,
the task sequence still attempts to run. If the architecture of the media doesn't match
the architecture of the target computer, the task sequence fails.

For more information, see Create task sequence media.

Media types
Configuration Manager supports the following types of media:

Capture media

<!-- p.28 -->

This media captures an OS image that you configure and create outside of the
Configuration Manager infrastructure. Capture media can contain custom programs that
can run before a task sequence runs. The custom program can interact with the desktop,
prompt the user for input values, or create variables to be used by the task sequence.

For more information, see Create capture media.

Stand-alone media
Stand-alone media contains the task sequence and all associated objects that are
necessary for the task sequence to run. Stand-alone media task sequences can run when
Configuration Manager has limited or no connectivity to the network. Run stand-alone
media in the following ways:

     If the destination computer isn't booted, the Windows PE image associated with
     the task sequence is used from the stand-alone media, and the task sequence
     begins.

     Manually start the stand-alone media. If a user is signed in to the computer, they
     can initiate the task sequence from the media.

  ） Important

  The steps of a stand-alone media task sequence must be able to run without
  retrieving any data from the network. Otherwise, the task sequence step that tries
  to retrieve the data fails. For example, a task sequence step that requires a
  distribution point to obtain a package fails. If the stand-alone media contains the
  necessary package, the task sequence step succeeds.

For more information, see Create stand-alone media.

Bootable media
Bootable media contains the required files to start a destination computer so that it can
connect to the Configuration Manager infrastructure. It then determines which task
sequences to run based on its collection memberships. This media doesn't include the
task sequence or dependent objects. Instead, the client downloads the content over the
network. This method is useful for new computers or bare-metal deployments, when no
OS is on the destination computer.

For more information, see Create bootable media.

<!-- p.29 -->

Prestaged media
Prestaged media deploys an OS image to a destination computer that isn't provisioned.
The prestaged media is stored as a Windows image (WIM) file. This file can be installed
on a bare-metal computer by the manufacturer or at an enterprise staging center. A
benefit of prestaged media is that these locations don't require a connection to your
Configuration Manager environment.

For more information, see Create prestaged media.

Next steps
     Security and privacy for OS deployment

     Prepare site system roles for OS deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.30 -->

Scenarios to deploy enterprise
operating systems with Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

The following OS deployment scenarios are available in Configuration Manager:

Upgrade Windows to the latest version
This scenario upgrades the OS on computers that run an earlier version of Windows. The
upgrade process keeps the applications, settings, and user data on the computer. There
are no external dependencies, such as the Windows ADK. This process can be faster and
more resilient than traditional OS deployments.

This scenario applies to all supported versions of Windows client and Windows Server.

For more information, see Upgrade Windows to the latest version.

Windows Autopilot for existing devices
Windows Autopilot for existing devices is available with Windows 10, version 1809 or
later. This feature allows you to reimage and provision a device with an earlier version of
Windows for Windows Autopilot user-driven mode using a single Configuration
Manager task sequence.

This scenario applies to Windows 10 version 1809 and later

For more information, see Windows Autopilot for existing devices.

Refresh an existing computer with a new
version
This scenario partitions and formats an existing computer and installs a new OS on the
computer. It's also referred to as wipe and load. You can migrate settings and user data
after the OS is installed.

This scenario applies to all supported versions of Windows client and Windows Server.

<!-- p.31 -->

For more information, see Refresh an existing computer with a new version of Windows.

Install a new version of Windows on a new
computer
This scenario installs an OS on a new computer. It's also referred to as bare metal. It's a
fresh installation of the OS and doesn't include any settings or user data migration.

This scenario applies to all supported versions of Windows client and Windows Server.

For more information, see Install a new version of Windows on a new computer (bare
metal).

Replace an existing computer and transfer
settings
This scenario installs an OS on a new computer, and migrates settings and user data
from an old computer to the new computer.

This scenario applies to all supported versions of Windows client and Windows Server.

For more information, see Replace an existing computer and transfer settings.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.32 -->

Upgrade Windows to the latest version
with Configuration Manager
Article • 12/19/2024

Applies to: Configuration Manager (current branch)

This article provides the steps in Configuration Manager to upgrade the Windows OS on
a computer. You can choose from different deployment methods, such as stand-alone
media or Software Center. The in-place upgrade scenario has the following features:

      Upgrades the OS to Windows 10 or later, or Windows Server 2016 and later

      Keeps the applications, settings, and user data on the computer

      Has no external dependencies, such as the Windows ADK

      Is faster and more resilient than traditional OS deployments

  ７ Note

  The Windows in-place upgrade task sequence supports deployment to internet-
  based clients managed through the cloud management gateway. This ability
  allows remote users to more easily upgrade to Windows without needing to
  connect to the intranet. For more information, see Deploy Windows in-place
  upgrade via CMG.

Starting in version 2103, you can upgrade by using a feature update deployed with the
task sequence. This integration combines the simplicity of Windows servicing with the
flexibility of task sequences. Servicing uses content that you synchronize through the
software update point. This process simplifies the need to manually get, import, and
maintain the Windows image content used with a standard task sequence to upgrade
Windows. The size of the servicing ESD file is generally smaller than the OS upgrade
package and WIM image file. You can also use Windows features such as Dynamic
Update and Delivery Optimization. The user experience with a feature update in a task
sequence is the same as with an OS upgrade package.

Supported versions

Upgrade version

<!-- p.33 -->

Only create OS upgrade packages to upgrade to the following OS versions:

     Windows 11
     Windows 10
     Windows Server 2016
     Windows Server 2019
     Windows Server 2022
        Windows Server 2025

Original version
Devices must run one of the following OS versions to target an OS upgrade task
sequence:

Windows client

     Windows 7
     Windows 8.1
     An earlier version of Windows 10 or Windows 11. For example, you can upgrade
     Windows 10, version 2004 to Windows 10, version 21H1.

For more information, see Windows client upgrade paths.

  ７ Note

  Starting in version 2403 OS deployment is supported for Windows on ARM64
  devices. Starting in version 2103, you can deploy a task sequence with a feature
  update to an ARM64 device.

Windows Server

     Windows Server 2012
     Windows Server 2012 R2
     An earlier version of Windows Server 2016
     An earlier version of Windows Server 2019
     An earlier version of Windows Server 2022
     An earlier version of Windows Server 2025

For more information about Windows Server supported upgrade paths, see Windows
Server 2016 supported upgrade paths and Windows Server Upgrade Center.

<!-- p.34 -->

Plan

Task sequence requirements and limitations
Review the following requirements and limitations for the task sequence to upgrade an
OS to make sure it meets your needs:

     Only add task sequence steps that are related to the core task of upgrading the
     OS. These steps primarily include installing packages, applications, or updates. Also
     use steps that run command lines, PowerShell, or set dynamic variables.

     Review drivers and applications that are installed on computers. Before you deploy
     the upgrade task sequence, make sure the drivers are compatible with the target
     version of Windows.

The following tasks aren't compatible with the in-place upgrade. They require you to use
traditional OS deployments:

     Changing the computer's domain membership, or updating the local
     Administrators group.

     Implementing a fundamental change on the computer, such as:
        Changing disk partitions
        Changing the system architecture from x86 to x64
        Implementing UEFI. For more information on a possible option, see Convert
        from BIOS to UEFI during an in-place upgrade.
        Modifying the base OS language

     You have custom requirements including using a custom base image, using third-
     party disk encryption, or require WinPE offline operations.

Infrastructure requirements
The only infrastructure prerequisite for the upgrade scenario is to have a distribution
point available. Distribute the OS upgrade package or feature update, and any other
content that you include in the task sequence. For more information, see Install or
modify a distribution point.

Starting in version 2103, if you use a feature update with a Windows upgrade task
sequence, you need a software update point to synchronize the Upgrades classification.
For more information, see Install and configure a software update point.

<!-- p.35 -->

Configure

Prepare the OS upgrade package
The Windows upgrade package contains the source files necessary to upgrade the OS
on the destination computer. The upgrade package must be the same edition,
architecture, and language as the clients that you upgrade. For more information, see
Manage OS upgrade packages.

  ７ Note

  In version 2103 or later, if you use a feature update with a Windows upgrade task
  sequence, you don't need the OS upgrade package.

Create a task sequence to upgrade the OS
Use the steps in Create a task sequence to upgrade an OS to automate the upgrade of
the OS.

  ７ Note

  To create a task sequence to upgrade Windows, you typically use the steps in
  Create a task sequence to upgrade an OS. The task sequence includes the
  Upgrade OS step, as well as additional recommended steps and groups to handle
  the end-to-end upgrade process.

  You can create a custom task sequence and add the Upgrade OS step. This step is
  the only one required to upgrade Windows. If you choose this method, to complete
  the upgrade, also add the Restart Computer step after the Upgrade OS step. Make
  sure to use the setting for The currently installed default operating system to
  restart the computer into the installed OS and not Windows PE.

Next steps
First create a task sequence to upgrade an OS.

Then deploy the task sequence with one of the following deployment methods:

     Use Software Center to deploy Windows over the network

<!-- p.36 -->

     Use stand-alone media to deploy Windows without using the network

        ） Important

        When you use stand-alone media, you must include a boot image in the task
        sequence. This configuration makes the task sequence available in the Task
        Sequence Media Wizard.

To monitor the task sequence deployment to upgrade the OS, see Monitor OS
deployments.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.37 -->

Windows Autopilot deployment for existing devices
06/13/2025Applies to: ✅ Windows 11, ✅ Windows 10

Modern desktop deployment with Windows Autopilot helps easily deploy the latest version of Windows to existing devices. Apps used by
the organization can be automatically installed. If Windows user data is managed with OneDrive for work or school, data is synchronized,
so users can resume working right away.

Windows Autopilot for existing devices allows reimaging and provisioning a Windows device for Windows Autopilot user-driven mode
using a single, native Configuration Manager task sequence. The existing device can be on-premises domain-joined. The end result is a
Windows device joined to either Microsoft Entra ID or Active Directory (Microsoft Entra hybrid join).

  ７ Note

  The JSON file for Windows Autopilot for existing devices only supports user-driven Microsoft Entra ID and user-driven hybrid
  Microsoft Entra Windows Autopilot profiles. Self-deploying and pre-provisioning Windows Autopilot profiles aren't supported with
  JSON files due to these scenarios requiring TPM attestation.

  However, during the Windows Autopilot for existing devices deployment, if the following conditions are true:

       Device is already a Windows Autopilot device before the deployment begins
       Device has a Windows Autopilot profile assigned to it

  then the assigned Windows Autopilot profile takes precedence over the JSON file installed by the task sequence. In this scenario, if
  the assigned Windows Autopilot profile is either a self-deploying or pre-provisioning Windows Autopilot profile, then the self-
  deploying and pre-provisioning scenarios are supported.

   Tip

  Using Windows Autopilot for existing devices could be used as a method to convert existing hybrid Microsoft Entra devices into
  Microsoft Entra devices. Using the setting Convert all targeted devices to Autopilot in the Windows Autopilot profile doesn't
  automatically convert existing hybrid Microsoft Entra device in the assigned groups into a Microsoft Entra device. The setting only
  registers the devices in the assigned groups for the Windows Autopilot service.

Requirements
     A currently supported version of Microsoft Configuration Manager current branch.

     Assigned Microsoft Intune licenses.

     Microsoft Entra ID P1 or P2.

     A supported version of Windows imported into Configuration Manager as an OS image.

     Enrollment restrictions aren't configured to block personal devices. For more information, see What are enrollment restrictions?:
     Blocking personal Windows devices.

       ） Important

       Any devices registered using a .json file during a hybrid join scenario are normally enrolled as a Corporate device.

Configure the Enrollment Status Page (optional)
If desired, an enrollment status page (ESP) for Windows Autopilot can be set up using Intune.

   1. Open the Microsoft Intune admin center    .

<!-- p.38 -->

 2. Go to Devices > Device onboarding | Enrollment. Make sure Windows is selected at the top and then under Windows Autopilot,
    select Enrollment Status Page and Set up the Enrollment Status Page.

 3. Go to Microsoft Entra ID > Manage | Mobility (MDM and WIP) > Microsoft Intune and enable Windows automatic enrollment.
    Configure the MDM user scope for some or all users.

Install required modules
 ７ Note

 The PowerShell code snippets in this section were updated in July of 2023 to use the Microsoft Graph PowerShell modules instead of
 the deprecated AzureAD Graph PowerShell modules. The Microsoft Graph PowerShell modules might require approval of additional
 permissions in Microsoft Entra ID when they're first used. It was also updated to force using an updated version of the
 WindowsAutoPilot module. For more information, see AzureAD and Important: Azure AD Graph Retirement and PowerShell
 Module Deprecation     .

 1. On an internet-connected Windows PC or server, open an elevated Windows PowerShell command window.

 2. Enter the following commands to install and import the necessary modules:

      PowerShell

      Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
      Install-Module -Name WindowsAutopilotIntune -MinimumVersion 5.4.0 -Force
      Install-Module -Name Microsoft.Graph.Groups -Force
      Install-Module -Name Microsoft.Graph.Authentication -Force
      Install-Module -Name Microsoft.Graph.Identity.DirectoryManagement -Force

      Import-Module -Name WindowsAutopilotIntune -MinimumVersion 5.4
      Import-Module -Name Microsoft.Graph.Groups
      Import-Module -Name Microsoft.Graph.Authentication
      Import-Module -Name Microsoft.Graph.Identity.DirectoryManagement

 3. Enter the following commands and provide Intune administrative credentials:

    Make sure the specified user account has sufficient administrative rights.

      PowerShell

      Connect-MgGraph -Scopes "Device.ReadWrite.All", "DeviceManagementManagedDevices.ReadWrite.All",
      "DeviceManagementServiceConfig.ReadWrite.All", "Domain.ReadWrite.All", "Group.ReadWrite.All",
      "GroupMember.ReadWrite.All", "User.Read"

    Windows requests the username and password for the account with a standard Microsoft Entra ID form. Type the username and
    password, and then select Sign in.

    The first time Intune Graph APIs are used on a device, it prompts to enable Microsoft Intune PowerShell read and write permissions.
    To enable these permissions, select Consent on behalf or your organization and then Accept.

<!-- p.39 -->

Get Windows Autopilot profiles for existing devices
Get all the Windows Autopilot profiles available in the Intune tenant, and display them in JSON format:

  PowerShell

  Get-AutopilotProfile | ConvertTo-AutopilotConfigurationJSON

See the following sample output:

  PowerShell

  PS C:\> Get-AutopilotProfile | ConvertTo-AutopilotConfigurationJSON
  {
      "CloudAssignedTenantId": "1537de22-988c-4e93-b8a5-83890f34a69b",
      "CloudAssignedForcedEnrollment": 1,
      "Version": 2049,
      "Comment_File": "Profile Autopilot Profile",
      "CloudAssignedAadServerData": "{\"ZeroTouchConfig\":
  {\"CloudAssignedTenantUpn\":\"\",\"ForcedEnrollment\":1,\"CloudAssignedTenantDomain\":\"M365x373186.onmicrosoft.com\"}}",
      "CloudAssignedTenantDomain": "M365x373186.onmicrosoft.com",
      "CloudAssignedDomainJoinMethod": 0,
      "CloudAssignedOobeConfig": 28,
      "ZtdCorrelationId": "7F9E6025-1E13-45F3-BF82-A3E8C5B59EAC"
  }

Each profile is encapsulated within braces ( { } ). The previous example displays a single profile.

JSON file properties
                                                                                                                                     ﾉ   Expand table

 Property                           Type      Required   Description

 Version                            Number    Optional   The version number that identifies the format of the JSON file.

 CloudAssignedTenantId              GUID      Required   The Microsoft Entra tenant ID that should be used. This property is the GUID for the tenant, and
                                                         can be found in properties of the tenant. The value shouldn't include braces.

 CloudAssignedTenantDomain          String    Required   The Microsoft Entra tenant name that should be used. For example: tenant.onmicrosoft.com .

 CloudAssignedOobeConfig            Number    Required   This property is a bitmap that shows which Windows Autopilot settings were configured.

                                                               1: SkipCortanaOptIn
                                                               2: OobeUserNotLocalAdmin
                                                               4: SkipExpressSettings
                                                               8: SkipOemRegistration
                                                               16: SkipEula

 CloudAssignedDomainJoinMethod      Number    Required   This property specifies whether the device should join Microsoft Entra ID or Active Directory
                                                         (Microsoft Entra hybrid join).

                                                               0: Microsoft Entra joined
                                                               1: Microsoft Entra hybrid joined

 CloudAssignedForcedEnrollment      Number    Required   Specifies that the device should require Microsoft Entra join and MDM enrollment.

                                                               0: Not required
                                                               1: required

 ZtdCorrelationId                   GUID      Required   A unique GUID (without braces) provided to Intune as part of the registration process. This ID is
                                                         included in the enrollment message as the OfflineAutopilotEnrollmentCorrelator . This attribute

<!-- p.40 -->

 Property                            Type      Required   Description

                                                          is present only if enrollment happens on a device registered with Zero Touch Provisioning via
                                                          offline registration.

 CloudAssignedAadServerData          Encoded   Required   An embedded JSON string used for branding. It requires enabling Microsoft Entra organization
                                     JSON                 branding. For example:
                                     string
                                                          "CloudAssignedAadServerData": "{\"ZeroTouchConfig\":
                                                          {\"CloudAssignedTenantUpn\":\"\",\"CloudAssignedTenantDomain\":\"tenant.onmicrosoft.com\"}}

 CloudAssignedDeviceName             String    Optional   The name automatically assigned to the computer. This name follows the naming pattern
                                                          convention configured in the Intune Windows Autopilot profile. An explicit name can also be
                                                          specified.

Create the JSON file
Save the Windows Autopilot profile as a JSON file in ASCII or ANSI format. Windows PowerShell defaults to Unicode format. If redirecting
output of the commands to a file, also specify the file format. The following PowerShell example saves the file in ASCII format. The
Windows Autopilot profiles appear in a subfolder under the folder specified by the $targetDirectory variable. By default, the
$targetDirectory variable is C:\AutoPilot , but it can be changed to another location if desired. The subfolder has the name of the

Windows Autopilot profile from Intune. If there are multiple Windows Autopilot profiles, each profile has its own subfolder. In each folder,
there's a JSON file named AutopilotConfigurationFile.json

  PowerShell

  Connect-MgGraph -Scopes "Device.ReadWrite.All", "DeviceManagementManagedDevices.ReadWrite.All",
  "DeviceManagementServiceConfig.ReadWrite.All", "Domain.ReadWrite.All", "Group.ReadWrite.All",
  "GroupMember.ReadWrite.All", "User.Read"
  $AutopilotProfile = Get-AutopilotProfile
  $targetDirectory = "C:\Autopilot"
  $AutopilotProfile | ForEach-Object {
      New-Item -ItemType Directory -Path "$targetDirectory\$($_.displayName)"
      $_ | ConvertTo-AutopilotConfigurationJSON | Set-Content -Encoding Ascii
  "$targetDirectory\$($_.displayName)\AutopilotConfigurationFile.json"
  }

   Tip

  When the PowerShell cmdlet Out-File is used to redirect the JSON output to a file, it uses Unicode encoding by default. This cmdlet
  might also truncate long lines. Use the Set-Content cmdlet with the -Encoding ASCII parameter to set the proper text encoding.

  ） Important

  The file name has to be AutopilotConfigurationFile.json and encoded as ASCII or ANSI.

The profile can also be saved to a text file and edit in Notepad. In Notepad, when choosing Save as, select the save as type: All Files, and
then select ANSI for the Encoding.
