---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 281-320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0281-0320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0281-0320
family: sccm
documentKind: "doc"
abstract: "Always use the Create MDT Task Sequence Wizard to create task sequences based on the MDT task sequence templates. Although you can manually import the task sequence templates, doing so is not recommend. To create a ZTI task sequence using the Create MDT Task Sequence Wizard in C"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 281-320

<!-- p.281 -->

 Always use the Create MDT Task Sequence Wizard to create task sequences based
 on the MDT task sequence templates. Although you can manually import the task
 sequence templates, doing so is not recommend.

To create a ZTI task sequence using the Create MDT Task Sequence
Wizard in Configuration Manager

  1. Select Start, point to All Programs, and then point to Microsoft System Center
    2012. Point to Configuration Manager, and then select Configuration Manager
    Console.

  2. In the Configuration Manager console, in the navigation pane, select Software
    Library.

  3. In the Software Library workspace, go to Overview/Operating Systems/Task
    Sequences.

  4. On the Ribbon, on the Home tab, in the Task Sequences group, select Create MDT
    Task Sequence.

    The Create MDT Task Sequence Wizard starts.

  5. Complete the Create MDT Task Sequence Wizard using the information in Table
    123. Accept the default values unless otherwise specified.

    Table 123. Information for Completing the Create MDT
    Task Sequence Wizard

                                                                             ﾉ   Expand table

     On this wizard   Do this
     page

     Choose           - In The following SCCM task sequence templates are available, select
     Template         task_sequence_template (where task_sequence_template is the task
                      sequence template to be selected from Table 121).

                      - Select Next.

     Choose           - In Task sequence name, type task_sequence_name (where
     Template:        task_sequence_name is the name of the task sequence displayed in the
     General          Configuration Manager console).

                      - In Task sequence comments, type comment (where comment is
                      descriptive text that describes the purpose of the task sequence).

<!-- p.282 -->

On this wizard   Do this
page

                 - Select Next.

Choose           a. Select Join a workgroup.
Template:
Details          b. The other option is Join a domain. If you select this option, in
                 Workgroup, type workgroup_name (where workgroup_name is the name
                 of the workgroup to join).

                 c. Select Join a domain.

                 The other option is Join a workgroup. If you select this option, perform
                 the following steps:

                 - In Domain, type domain_name (where domain_name is the name of
                 the workgroup to join).

                 - Select Set.

                 The Windows User Account dialog box appears.

                 - In the Windows User Account dialog box, in User name, type
                 domain_name\user_name (where user_name is the name of the user
                 account used to join the computer to the domain and domain_name is
                 the name of the domain in which the user account resides. This account
                 must be a member of the Domain Admins group in the domain or have
                 sufficient delegated permissions).

                 - In Password and Confirm password, type password (where password is
                 the password for the user account), and then select OK.

                 d. In User name, type user_name (where user_name is the name of the
                 registered user that appears in the Windows operating system
                 properties).

                 e. In Organization name, type organization_name (where
                 organization_name is the name of the registered organization that
                 appears in the Windows operating system properties).

                 f. In Product key, type product_key (where product_key is the product
                 key for operating system).

                 g. Select Next.

Choose           a. Select This task sequence will never be used to capture and image.
Template:
                 The other option is This task sequence may be used to capture and

<!-- p.283 -->

On this wizard   Do this
page

Capture          image.
Settings
                 b. Select This task sequence may be used to capture and image.

                 The other option is This task sequence will never be used to capture
                 and image. If you select this option, perform the following steps:

                 - In Capture destination, type unc_path (where unc_path is the fully
                 qualified UNC path for the location of the WIM file, including the name
                 of the WIM file).

                 - Select Set.

                 The Windows User Account dialog box appears.

                 - In the Windows User Account dialog box, in User name, type
                 domain_name\user_name (where user_name is the name of the user
                 account that has Write permission to the folder specified in Capture
                 destination and domain_name is the name of the domain in which the
                 user account resides).

                 - In Password and Confirm password, type password (where password is
                 the password for the user account), and then select OK.

                 c. Select Next.

Boot Image       a. Select Specify an existing boot image.

                 The other option is Create a new boot image package. If you select this
                 option, perform the following steps:

                 - Select Browse.

                 The Select a Package dialog box appears.

                 - In Select a Package dialog box, select package_name (where
                 package_name is the name of the existing boot image), and then select
                 OK.

                 b. Select Create a new boot image package.The other option is Create a
                 new boot image package. If you select this option, in Package source to
                 be created, type unc_path (where unc_path is the fully qualified UNC
                 path for the location of the folder in which the package source will be
                 stored).

                 The Configuration Manager service account must have permission to
                 modify the contents of this UNC path to update the boot images. Ensure

<!-- p.284 -->

On this wizard   Do this
page

                 that the Configuration Manager service account has the appropriate
                 permission on this network shared folder.

                 You can also select Browse to locate the UNC path.

                 c. Select Next.

Boot Image:      This wizard page appears only if you select Create a new boot image
General          package on the Boot Image wizard page.
Settings
                 a. In Name, type package_name (where package_name is the name to
                 be given to the boot image package).

                 b. In Version, type version_number (where version_number is the version
                 number to be assigned to the boot image package).

                 c. In Comments, type comment_text (where comment_text is descriptive
                 information about the boot image package).

                 d. Select Next.

Boot Image:      This wizard page appears only if you select Create a new boot image
Components       package on the Boot Image wizard page.

                 a. In Platform, select platform (where platform is the platform
                 architecture for the boot image—x86 or X64).

                 b. Select or clear the ADO check box if you want to add ADO
                 components to the boot image, which is needed to access SQL Server
                 databases such as the MDT DB. By default, this check box is selected. If
                 the check box is:

                 - Selected, the ADO components are added to the boot image

                 - Cleared, the ADO components are not added to the boot image

                 Scripting, Hypertext Markup Language Application (HTA), XML, and WMI
                 support are always added to the boot image.

                 c. Select or clear the font check box (where font is the name of the font
                 to be added, which can be Chinese [ZH-CN], Chinese [ZH-HK], Chinese
                 [ZH-TW], Japanese [JA-JP], or Korean [KO-KR]) to add support for the
                 optional fonts.

                 d. Select Next.

<!-- p.285 -->

On this wizard   Do this
page

Boot Image:      a. Select or clear the Add prestart command files to enable the
Customization    Deployment Wizard for this boot media check box. If this check box is:

                 - Selected, the prestart command files are added to the boot image. In
                 Command line, type the prestart command script to run, which defaults
                 to ZTIMediaHook.wsf. In Folder for prestart command files, type
                 unc_path (where unc_path is the fully qualified UNC path to a writable
                 folder).

                 Alternatively, select Browse to find the folder in which the prestart
                 command files reside.

                 - Cleared, the prestart command files are not added to the boot image.

                 b. Select or clear the Add extra files to the new boot image check box.
                 If this check box is:

                 - Selected, the extra files are added to the boot image. In Path, type
                 path (where path is the fully qualified or relative local or UNC path to a
                 writable folder).

                 Alternatively, select Browse to find the folder in which the extra files
                 reside.

                 - Cleared, the extra files are not added to the boot image.

                 c. In Use a custom background bitmap file (UNC Path), type unc_path
                 (where unc_path is the fully qualified UNC path to the bitmap file that
                 you want to use as the background).

                 Alternatively, select Browse to find the bitmap file.

                 d. Select or clear the Enable command support (F8) check box. If this
                 check box is:

                 e. Select Next.

Boot Image:      a. Select Specify an existing Microsoft Deployment Toolkit files
Customization    package.

                 The other option is Create a new Microsoft Deployment Toolkit files
                 package. If you select this option, perform the following steps:

                 - Select Browse.

                 The Select a Package dialog box appears.

<!-- p.286 -->

On this wizard   Do this
page

                 - In the Select a Package dialog box, select package_name (where
                 package_name is the name of the existing package), and then select OK.

                 b. Select Create a new Microsoft Deployment Toolkit files package.

                 The other option is Specify an existing Microsoft Deployment Toolkit
                 files package. If you select this option, in Package source to be created,
                 type unc_path (where unc_path is the fully qualified UNC path for the
                 location of the folder in which the package source will be stored).

                 You can also select Browse to locate the UNC path.

                 c. Select Next.

MDT Package:     This wizard page appears only if you select Create a new Microsoft
MDT Details      Deployment Toolkit files package on the MDT Package wizard page.

                 a. In Name, type package_name (where package_name is the name to
                 be given to the Microsoft Deployment Toolkit files package).

                 b. In Version, type version_number (where version_number is the version
                 number to be assigned to the Microsoft Deployment Toolkit files
                 package).

                 c. In Language, type language (where language is the language of the
                 Microsoft Deployment Toolkit files package).

                 d. In Manufacturer, type manufacturer (where manufacturer is the
                 manufacturer of the Microsoft Deployment Toolkit files package).

                 e. In Comments, type comment_text (where comment_text is descriptive
                 information about the Microsoft Deployment Toolkit files package).

                 f. Select Next.

OS Image         On this wizard page, you can select (or create) OS image packages or OS
                 install packages. OS image packages are created from WIM files either
                 from distribution media or from custom WIM files you have created. OS
                 install packages contain all the necessary files to install the operating
                 system, such as the contents of a Windows DVD.

                 The ZTI task sequence templates always configure the Apply Operating
                 System Image task sequence step to deploy the image index equal to 1.
                 If you want to deploy an image with a different index, change the
                 configuration of the Apply Operating System Image task sequence
                 step.

<!-- p.287 -->

On this wizard   Do this
page

                 Also, if you select a SKU that is different from the default SKU, remove
                 the following section from Unattend.xml in the Settings package:

                 <MetaData> <Key>/image/index</Key> <Value>1</Value> </MetaTag>

                 a. Select Specify an existing OS image.

                 The other options are Create a new OS image, Specify an existing OS
                 installation package, or Create a new OS install package. If you select
                 this option, perform the following steps:

                 - Select Browse.

                 The Select a Package dialog box appears.

                 - In Select a Package dialog box, select package_name (where
                 package_name is the name of the existing package), and then select OK.

                 b. Select Create a new OS image. Select Create a new OS image.

                 The other options are Specify an existing OS image,Specify an existing
                 OS installation package, or Create a new OS install package. If you
                 select this option, perform the following steps:

                 - In OS image file (WIM) location, type unc_path (where unc_path is the
                 fully qualified UNC path for the location of the folder in which the WIM
                 file is located, including the name of the WIM file).

                 You can also select Browse to locate the WIM file.

                 - In Package source folder to be created, type unc_path (where
                 unc_path is the fully qualified UNC path for the location of the folder in
                 which the package source will be stored). In Package source folder to
                 be created, type unc_path (where unc_path is the fully qualified UNC
                 path for the location of the folder in which the package source will be
                 stored).

                 You can also select Browse to locate the UNC path.

                 c. Select Specify an existing OS installation package.

                 The other options are Specify an existing OS image, Create a new OS
                 image, or Create a new OS install package. If you select this option,
                 perform the following steps:

                 - Select Browse.

<!-- p.288 -->

On this wizard   Do this
page

                 The Select a Package dialog box appears.

                 - In the Select a Package dialog box, select package_name (where
                 package_name is the name of the existing package), and then select OK.

                 d. Select Create a new OS install package.

                 e. The other options are Specify an existing OS image, Create a new OS
                 image, or Specify an existing OS installation package. The other
                 options are Specify an existing OS image, Create a new OS image, or
                 Specify an existing OS installation package.

                 The OS installation folder contents are copied from the specified UNC
                 location to the package source folder, which are then used to create the
                 package.

                 If you select this option, perform the following steps:

                 - In OS installation folder location, type unc_path (where unc_path is
                 the fully qualified UNC path for the location of the folder in which the
                 package source will be stored).

                 You can also select Browse to locate the UNC path.

                 - In Package source folder to be created, type unc_path (where
                 unc_path is the fully qualified UNC path for the location of the folder in
                 which the package source will be stored).

                 You can also select Browse to locate the UNC path.

                 f. Select Next.

OS Image:        This wizard page appears only if you select Create a new OS image on
Image Details    the OS Image wizard page.

                 a. In Name, type package_name (where package_name is the name to
                 be given to the package).

                 b. In Version, type version_number (where version_number is the version
                 number to be assigned to the package).

                 c. In Comments, type comment_text (where comment_text is descriptive
                 information about the package).

                 d. Select Next.

<!-- p.289 -->

On this wizard   Do this
page

OS Image:        This wizard page appears only if you select Create a new OS install
Install Source   package on the OS Image wizard page.

                 a. In Name, type package_name (where package_name is the name to
                 be given to the package).

                 b. In Version, type version_number (where version_number is the version
                 number to be assigned to the package).

                 c. In Comments, type comment_text (where comment_text is descriptive
                 information about the package).

                 d. Select Next.

OS Image: OS     a. In The selected operating system image (WIM) file contains multiple
Image Index      images. Specify which image you would like to deploy, select
                 image_index (where image_index is the image index of the image that
                 contains the operating system you want to deploy).

                 b. Select Next.

Client Package   a. Select Specify an existing ConfigMgr client package.

                 The other option is Create a new ConfigMgr client package. If you
                 select this option, perform the following steps:

                 - Select Browse.

                 The Select a Package dialog box appears.

                 - In the Select a Package dialog box, select package_name (where
                 package_name is the name of the existing package), and then select OK.

                 b. Select Create a new ConfigMgr client package. Select Create a new
                 ConfigMgr client package.

                 The other option is Specify an existing ConfigMgr client package.

                 c. Select Next.

USMT Package     You cannot specify the location for storing the user state migration data
                 in the CustomSettings.ini file for ZTI using Configuration Manager. The
                 Request state store task automatically determines the state migration
                 point to use for storing user state migration data. For more information,
                 see the section, "How to Capture and Restore User State," in the section,
                 "How to Manage the User State in Configuration Manager," in the
                 Configuration Manager Documentation Library, which is installed with

<!-- p.290 -->

On this wizard   Do this
page

                 Configuration Manager.

                 a. Select Specify an existing USMT package.

                 The other option is Create a new USMT package. If you select this
                 option, perform the following steps: The other option is Create a new
                 USMT package. If you select this option, perform the following steps:

                 - Select Browse.

                 The Select a Package dialog box appears.

                 - In the Select a Package dialog box, select package_name (where
                 package_name is the name of the existing package), and then select OK.

                 b. Select Create a new USMT package.

                 The other option is Specify an existing USMT package. If you select this
                 option, perform the following steps:

                 - In Path to USMT executables and related, type path (where path is the
                 fully qualified path for the location of the folder in which the USMT
                 source files are located).

                 You can also select Browse to locate the path.

                 - In Package source to be created, type unc_path (where unc_path is the
                 fully qualified UNC path for the location of the folder in which the
                 package source will be stored).

                 You can also select Browse to locate the UNC path.

                 c. Select Next.

                 USMT can only back up and restore locally cached user profiles, not
                 network copies. For more information on using roaming profiles, see the
                 Folder Redirection, Offline Files, and Roaming User Profiles overview.

USMT Package:    This wizard page appears only if you select Create a new USMT package
USMT Details     on the USMT Package wizard page.

                 a. In Name, type package_name (where package_name is the name to
                 be given to the package).

                 b. In Version, type version_number (where version_number is the version
                 number to be assigned to the package).

<!-- p.291 -->

On this wizard     Do this
page

                   c. In Language, type language (where language is the language of the
                   package).

                   d. In Manufacturer, type manufacturer_name (where
                   manufacturer_name is the name of the software manufacturer in the
                   package).

                   e. In Comments, type comment_text (where comment_text is descriptive
                   information about the package).

                   f. Select Next.

Settings           a. Select Specify an existing settings package.
Package
                   The other option is Create a new settings package. If you select this
                   option, perform the following steps:

                   - Select Browse.

                   The Select a Package dialog box appears.

                   - In the Select a Package dialog box, select package_name (where
                   package_name is the name of the existing package), and then select OK.

                   b. Select Create a new settings package.

                   The other option is Specify an existing settings package. If you select
                   this option, in Package source to be created, type unc_path (where
                   unc_path is the fully qualified UNC path for the location of the folder in
                   which the package source will be stored).

                   You can also select Browse to locate the UNC path.

                   c. Select Next.

Settings           This wizard page appears only if you select Create a new settings
Package:           package on the Settings Package wizard page. This wizard page
Settings Details   appears only if you select Create a new settings package on the
                   Settings Package wizard page.

                   a. In Name, type package_name (where package_name is the name to
                   be given to the package).

                   b. In Version, type version_number (where version_number is the version
                   number to be assigned to the package).

                   c. In Language, type language (where language is the language of the

<!-- p.292 -->

       On this wizard   Do this
       page

                        package).

                        d. In Manufacturer, type manufacturer_name (where
                        manufacturer_name is the name of the manufacturer for the software in
                        the package).

                        e. In Comments, type comment_text (where comment_text is descriptive
                        information about the package).

                        f. Select Next.

       Sysprep          a. Select No Sysprep package is required.
       Package

       Summary          Select Next.

      The Summary wizard page displays a status bar that shows the progress of the
      tasks defined in the wizard. The Create MDT Task Sequence Wizard closes when
      the task sequence is created.

Managing Operating Systems in Configuration Manager
Manage operating systems in the Operating Systems node in the Software Library
workspace. The operating systems are contained and managed in the following nodes
beneath the Operating Systems node:

      Operating System Installers. This node contains operating systems that are used
      to deploy reference computers and are based on the install.wim file from the
      original operating system media.

      Operating System Images. This node contains captured operating system images
      from reference computers and that are deployed to your target computers.

      For more information about managing operating systems in the Configuration
      Manager console, see the section, "Configuring Configuration Manager for
      Operating System Deployments," in the Configuration Manager Documentation
      Library, which is installed with Configuration Manager.

Managing Device Drivers in Configuration Manager
Manage device drivers in the Configuration Manager console in Configuration Manager
by:

<!-- p.293 -->

     Importing the device drivers into Configuration Manager as described in Import
     Drivers into Configuration Manager

     Creating a new driver package that contains the device drivers as described in
     Create a New Configuration Manager Driver Package

     Adding device drivers and device driver packages to operating systems and boot
     images as described in Add Device Drivers to Operating System and Boot Images
     in Configuration Manager

     Deploying specific device drivers to target computers for ZTI deployments as
     described in Deploy Specific Device Drivers to Target Computers in Configuration
     Manager

Import Drivers into Configuration Manager
To import drivers into Configuration Manager, use the Import New Driver Wizard. For
information about this wizard, see the section, "How to Import Windows Device Drivers
into the Driver Catalog," in the Configuration Manager Documentation Library, which is
installed with Configuration Manager.

Create a New Configuration Manager Driver Package
A driver package contains the content associated with one or more device drivers. You
must add device drivers to a driver package and copy them to a distribution point
before Configuration Manager clients can install them. For information about creating a
new driver package, see the section, "How to Create a New Driver Package," in the
Configuration Manger Documentation Library, which is installed with Configuration
Manager.

Add Device Drivers to Operating System and Boot Images in
Configuration Manager

When you have added device drivers to the driver catalog, you can add them to existing
operating systems and boot images. The driver catalog helps manage the cost and
complexity of deploying an operating system in an environment that contains different
types of computers and devices. Storing device drivers in the driver catalog and not with
each individual operating system image greatly reduces the number of operating system
images you need.

For information about managing the driver catalog, see the section, "How to Manage
the Driver Catalog in Configuration Manager," in the Configuration Manager

<!-- p.294 -->

Documentation Library, which is installed with Configuration Manager.

To add device drivers to operating systems and boot images in
Configuration Manager

     Add device drivers from the driver catalog to existing operating systems as
     described in Add Device Drivers to an Operating System in Configuration Manager.

     Add device drivers from the driver catalog to existing boot images as described in
     Add Device Drivers to a Boot Image in Configuration Manager.

Add Device Drivers to an Operating System in Configuration
Manager

Add new device drivers to an existing operating system image using the Task Sequence
Editor. To allow Configuration Manager to search in the driver catalog for the new
device drivers, add an Auto Apply Drivers task sequence step to an existing task
sequence.

For information about adding device drivers to an operating system, see the section,
"How to Install Device Drivers to Computers by Using Task Sequences," in the
Configuration Manager Documentation Library, which is installed with Configuration
Manager.

Add Device Drivers to a Boot Image in Configuration Manager

You can add Windows device drivers that you have imported into the driver catalog to
one or more boot images. Only mass storage device drivers and network adapter device
drivers should be added to boot images, because other types of drivers are not needed
and will increase the size of the boot image. Only add valid device drivers that are
intended for use with Windows 8.1, because the version of Windows PE is based on
Windows 8.1.

For information about adding device drivers to boot images, see the section, "How to
Add and Remove Device Drivers That Are Associated with Driver Packages and Boot
Images," in the Configuration Manager Documentation Library, which is installed with
Configuration Manager.

Deploy Specific Device Drivers to Target Computers in
Configuration Manager

<!-- p.295 -->

By default, ZTI using Configuration Manager deploys all device drivers to the target
computers. Then, the target operating system uses Plug-and-Play IDs to identify the
device drivers needed for the devices on the target computers.

To change this default behavior, configure the ZTI deployment process to install specific
drivers to target computers as described in Control Device Driver Deployments Using
Configuration Manager for ZTI. For more information about strategies for device driver
management, see Select the Device Driver Management Strategy.

Deploying an Operating System Using Task Sequence
Bootable Media in Configuration Manager
To initiate ZTI deployment using Configuration Manager from bootable media, start the
target computer with the bootable media. The boot process starts Windows PE, and
then starts ZTI. You can start the target computer from a UFD, CD, or DVD.

  ７ Note

  The ZTI deployment process using Configuration Manager can also be initiated by
  starting the target computer from Windows Deployment Services. However, for
  reference computers it may be easier to start the ZTI deployment process from
  bootable media.

For more information about how to deploy an operating system using task sequence
bootable media, see the section "How to Deploy Operating Systems by Using Media in
Configuration Manager" in the Configuration Manager Documentation Library, which is
installed with Configuration Manager.

Creating Task Sequence Bootable Media in Configuration
Manager
To initiate the ZTI deployment process using Configuration Manager from bootable
media, provide a method for starting the computer with Windows PE and the necessary
software by creating the task sequence bootable media disk. Use the Task Sequence
Media Wizard in Configuration Manager console to create bootable media for storage
on a UFD, CD, or DVD.

  ７ Note

<!-- p.296 -->

  The ZTI deployment process using Configuration Manager can also be initiated by
  starting the target computer from Windows Deployment Services. However, for
  reference computers it may be easier to start the ZTI deployment process from
  bootable media.

For more information about how to create task sequence bootable media, see the
section, "How to Create Bootable Media ," in the Configuration Manager Documentation
Library, which is installed with Configuration Manager.

Creating ZTI Boot Images in Configuration Manager
Some situations call for you to create a new boot image for the ZTI process without
running the Create MDT Task Sequence Wizard. You can create new boot images for ZTI
using the Create Boot Image using MDT Wizard in the Boot Images node in the
Configuration Manager console.

To create a ZTI boot image in Configuration Manager

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Boot
     Images.

   4. On the Ribbon, on the Home tab, in the Task Sequences group, select Create Boot
     Image using MDT.

     The Create Boot Image Using MDT Wizard starts.

   5. Complete the Create Boot Image Using MDT Wizard using the information in Table
     124. Accept the default values unless otherwise specified.

     Table 124. Information for Completing the Create Boot
     Image using MDT Wizard

                                                                       ﾉ   Expand table

<!-- p.297 -->

On this wizard      Do this
page

Package Source      a. In Package source folder to be created (UNC) path, type unc_path
                    (where unc_path is the fully qualified UNC path to the folder you want
                    to use as the source for the boot image package).

                    The Configuration Manager service account must have permission to
                    modify the contents of this UNC path to update the boot images.
                    Ensure that the Configuration Manager service account has the
                    appropriate permission on this network shared folder.

                    Alternatively, select Browse to find the network shared folder.

                    b. Select Next.

General Settings    a. In Name, type package_name (where package_name is descriptive
                    name displayed in the Configuration Manager Console).

                    b. In Version, type package_version (where package_version is version
                    number that you want to assign to the package).

                    c. In Comments, type package_comments (where package_comments is
                    text that describes the purpose of the boot image).

                    d. Select Next.

General Settings:   a. In Platform, select platform (where platform is the platform
Options             architecture for the boot image—x86 or x64).

                    b. In Scratch Space, select scratch_space (where scratch_space is the
                    amount of writeable space available on the Windows PE system volume
                    when booted in ramdisk mode and is specified in MB).

                    c. Select Next.

General Settings:   a. In Platform, select platform (where platform is the platform
Components          architecture for the boot image—x86 or x64).

                    b. Select or clear the component check box (where component is the
                    name of the component to be selected). If the check box is:

                    - Selected, the component is added to the boot image

                    - Cleared, the component is not added to the boot image

                    Scripting, HTA, XML, and WMI support are always added to the boot
                    image.

<!-- p.298 -->

On this wizard   Do this
page

                 c. Select Next.

Customization    a. Select or clear the Add prestart command files to enable the
                 Deployment Wizard for this boot media check box. If this check box is:

                 - Selected, the prestart command files are added to the boot image. In
                 Command line, type the prestart command script to run, which
                 defaults to ZTIMediaHook.wsf. In Folder for prestart command files,
                 type unc_path (where unc_path is the fully qualified UNC path to a
                 writable folder).

                 Alternatively, select Browse to find the folder in which the prestart
                 command files reside.

                 - Cleared, the prestart command files are not added to the boot image.

                 b. Select or clear the Add extra files to the new boot image check box.
                 If this check box is:

                 - Selected, the extra files are added to the boot image. In Path, type
                 path (where path is the fully qualified or relative local or UNC path to a
                 writable folder).

                 Alternatively, select Browse to find the folder in which the extra files
                 reside.

                 - Cleared, the extra files are not added to the boot image.

                 c. In Use a custom background bitmap file (UNC Path), type unc_path
                 (where unc_path is the fully qualified UNC path to the bitmap file that
                 you want to use as the background).

                 Alternatively, select Browse to find the bitmap file.

                 d. Select or clear the Enable command support (F8) check box.

                 e. Select Next.

Summary          Review the information in Details, and then select Next.

Confirmation     You can select Save Output to save the output of the wizard to a file.
                 You can also select View Script to view the Windows PowerShell scripts
                 used to perform the wizard tasks.

                 Select Close.

<!-- p.299 -->

     After the Create Boot Image using MDT Wizard finishes, the new boot image
     appears in the preview pane in the Configuration Manager console.

Managing Software Packages in Configuration Manager
Manage software packages in the Configuration Manager console in Configuration
Manager by:

     Adding language packs as described in Add Language Packs in Configuration
     Manager

     Adding software updates as described in Add Software Updates in Configuration
     Manager

Add Language Packs in Configuration Manager
Language packs are .cab files that you can add to Configuration Manager packages
either offline or online. Before adding language packs, however, create a Configuration
Manager package that contains one or more language packs.

The number of language packs that you add to a Configuration Manager package is
based on the type of deployment being performed. When deploying language packs
using:

     ZTI, put one or more language packs in each Configuration Manager package. This
     allows you to bundle the necessary language packs for your organization and
     include them in one Configuration Manager package.

     If you bundle two or more language packs in a Configuration Manager package
     and deploy that package, all language packs will be deployed. If you want to
     deploy different combination of language packs, then consider bundling one
     language pack in a Configuration Manager package and create a separate,
     conditional task sequence step to deploy each different language pack.

     UDI, put only one language pack in each Configuration Manager package. This
     one-to-one relationship allows the user to select individual language packs as
     desired in the UDI Wizard.

To create a Configuration Manager package that contains one or more
language packs

   1. Create a folder that will contain the package source for the language pack (.cab
     file).

<!-- p.300 -->

     ７ Note

     Create this folder where previously created packages are stored or where
     space is available.

2. Create a subfolder beneath the folder you created in step 1 for the language pack
  (.cab file).

3. Add the language pack (.cab file) downloaded from Microsoft into the subfolder
  created in step 2.

     ７ Note

     Language packs already in .cab format are available for download from the
     Microsoft Volume Licensing website.

4. Repeat steps 2 and 3 for each language pack that you want to be a part of the
  package.

5. Run the New Package Wizard in the Configuration Manager console, ensuring the
  following options are selected during the wizard:

         On the Data Source wizard page, select This package contains source files,
         and then select Set to set the source directory to the folder you created in
         step 1.

         On the Data Source wizard page, select the Enable binary differential
         replication check box.

         For more information about how to create a Configuration Manager package,
         see the section, "How to Create a Package and Program by using the Create
         Package and Program Wizard ," in the Configuration Manager
         Documentation Library, which is installed with Configuration Manager.

  To add language packs offline to Windows

７ Note

When used with MDT, the term offline means that the computer is booted into
Windows PE, and thus the image can be modified offline—not in the currently
booted operating system.

<!-- p.301 -->

 1. Select Start, point to All Programs, and then point to Microsoft System Center
   2012. Point to Configuration Manager, and then select Configuration Manager
   Console.

 2. In the Configuration Manager console, in the navigation pane, select Software
   Library.

 3. In the Software Library workspace, go to Overview/Operating Systems/Task
   Sequences.

 4. In the preview pane, select task_sequence (where task_sequence is the name of the
   task sequence for which you want to add the language pack).

 5. On the Ribbon, on the Home tab, in the Task Sequences group, select Edit.

   The task_sequence_name Task Sequence Editor dialog box opens (where
   task_sequence_name is the name of the task sequence to which you want to add
   language packs offline).

 6. In the task_sequence_name ask Sequence Editor dialog box, under the Postinstall
   phase, go to the Setup Windows and ConfigMgr task.

 7. Select the task immediately above this task so that the new added task will be
   positioned immediately before the Setup Windows and ConfigMgr task.

 8. On the menu bar, select Add, select MDT, and then select Install Language Packs
   Offline.

   The Install Language Packs Offline task sequence step is added to the task
   sequence.

 9. On the Properties tab of the newly added task sequence step, type the relevant
   information in the Name and Description boxes.

10. On the Properties tab of the newly added task sequence step, select Browse.

   The Select a Package dialog box appears.

11. In the Select a Package dialog box, select language_package (where
   language_package is the name of the package that contains the language pack you
   want to install), and then select OK.

12. In the task_sequence_name Task Sequence Editor dialog box, select OK.

   To add language packs online to Windows

<!-- p.302 -->

７ Note

When used in MDT, the term online means that the computer is booted into an
operating system but run as an Administrator user so that final configurations can
be made to the running operating system.

1. Select Start, point to All Programs, and then point to Microsoft System Center
  2012. Point to Configuration Manager, and then select Configuration Manager
  Console.

2. In the Configuration Manager console, in the navigation pane, select Software
  Library.

3. In the Software Library workspace, go to Overview/Operating Systems/Task
  Sequences.

4. In the preview pane, select task_sequence (where task_sequence is the name of the
  task sequence for which you want to add the language pack).

5. On the Ribbon, on the Home tab, in the Task Sequences group, select Edit.

  The task_sequence_name Task Sequence Editor dialog box opens (where
  task_sequence_name is the name of the task sequence to which you want to add
  language packs offline).

6. In the task_sequence_name Task Sequence Editor dialog box, under the State
  Restore group, select the Gatherstep (so that the newly added task will be
  positioned immediately after the Gathertask sequence step in the State Restore
  group).

7. On the menu bar, select Add, select MDT, and then select Install Language Packs
  Online.

  The Install Language Packs Online task sequence step is added to the task
  sequence.

8. On the Properties tab of the newly added task sequence step, type the relevant
  information in the Name andDescription boxes.

9. On the Properties tab of the newly added task sequence step, select Browse.

  The Select a Package dialog box appears.

<!-- p.303 -->

 10. In the Select a Package dialog box, select language_package (where
     language_package is the name of the package that contains the language pack you
     want to install), and then select OK.

 11. In the task_sequence_name Task Sequence Editor dialog box, select OK.

Add Software Updates in Configuration Manager

Use Configuration Manager to add updates—online or offline—during the task
sequence. Manage software updates in Configuration Manager using a server
configured as a software update point. For detailed information on software updates
using Configuration Manager, see the section "Configuring Software Updates in
Configuration Manager," in the Configuration Manager Documentation Library, which is
installed with Configuration Manager.

Use deployment packages to deploy software updates. For more information about
configuration and deployment of software update packages, see the section "Download
Software Updates," in the Configuration Manager Documentation Library, which is
installed with Configuration Manager.

To install operating system updates online, add the updates to a Deployment
Management item. Create a Deployment Management item using the Deploy Package
Wizard. For more information on deploying packages and deployment management,
see the following sections in the Configuration Manager Documentation Library, which
is installed with Configuration Manager:

     "Manage Software Update Settings".

     "Deploy Software Updates".

To add offline updates to Windows

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences

   4. In the preview pane, select task_sequence (where task_sequence is the name of the
     task sequence for which you want to add the language pack).

<!-- p.304 -->

 5. On the Ribbon, on the Home tab, in the Task Sequences group, select Edit.

   The task_sequence_name Task Sequence Editor dialog box opens (where
   task_sequence_name is the name of the task sequence to which you want to add
   language packs offline).

 6. In the task_sequence_name Task Sequence Editor dialog box, under the Postinstall
   phase, go to the Setup Windows and ConfigMgr task.

 7. Select the task immediately above this task so that the new added task will be
   positioned just above the Setup Windows and ConfigMgr task.

     ７ Note

     Only updates in CAB files are supported using the Install Updates Offline task
     sequence type. Other formats of update files are ignore, such as MSI, MSP, or
     executable (.exe) files.

 8. On the menu bar, select Add, select MDT, and then select Install Updates Offline.

   The Install Updates Offline task sequence step is added to the task sequence.

 9. On the Properties tab of the newly added task sequence step, type the relevant
   information in the Name and Description boxes.

10. On the Properties tab of the newly added task sequence step, select Browse. The
   Select a Package dialog box appears.

11. In the Select a Package dialog box, select update_package (where update_package
   is the name of the package that contains the updates you want to install), and then
   select OK.

12. In the task_sequence_name Task Sequence Editor dialog box, select OK.

   To add online updates to Windows

７ Note

The task sequence templates in MDT include the Install Software Updates task
sequence step to perform online updates. This step is only necessary when creating
custom task sequences.

<!-- p.305 -->

 1. Select Start, point to All Programs, and then point to Microsoft System Center
   2012. Point to Configuration Manager, and then select Configuration Manager
   Console.

 2. In the Configuration Manager console, in the navigation pane, select Software
   Library.

 3. In the Software Library workspace, go to Overview/Operating Systems/Task
   Sequences.

 4. In the preview pane, select task_sequence (where task_sequence is the name of the
   task sequence for which you want to add the language pack).

 5. On the Ribbon, on the Home tab, in the Task Sequences group, select Edit.

   The task_sequence_name Task Sequence Editor dialog box opens (where
   task_sequence_name is the name of the task sequence to which you want to add
   language packs offline).

 6. In the task_sequence_name Task Sequence Editor dialog box, under the State
   Restore phase, go to the Restart Computer task.

 7. Select the task immediately above this task so that the new added task will be
   positioned just above the Restart Computer task.

 8. In the Task Sequence Editor dialog box, select Add, select General, and then select
   Install Software Updates.

 9. On the menu bar, select Add, select General, and then select Install Software
   Updates.

   The Install Software Updates task sequence step is added to the task sequence.

10. On the Properties tab of the newly added task sequence step, type the relevant
   information in the Name and Description boxes.

11. On the Properties tab of the newly added task sequence step, select one of the
   following options:

        Mandatory Software Updates. This option installs only the software updates
        that are categorized as being mandatory. This option is selected by default.

        All Software Updates. This option installs all software updates, including
        mandatory and optional software updates.

12. In the task_sequence_name Task Sequence Editor dialog box, select OK.

<!-- p.306 -->

  ７ Note

  The Software Update Point role and Windows Server Update Services (WSUS) must
  be properly configured to work with this task sequence step type.

Managing Task Sequence Deployment in Configuration
Manager
In ZTI deployments using Configuration Manager, you must deploy the task sequences
to the target computers using the Deploy Software Wizard. The task sequence is
deployed to a collection that includes the reference computer or target computers. For
more information about deploying task sequences, see the section "How to Deploy a
Task Sequence," in the section, "How to Manage Task Sequences in Configuration
Manager," in the Configuration Manager Documentation Library, which is installed with
Configuration Manager.

Manually Adding Computers to the Site Database in
Configuration Manager
In ZTI deployments using Configuration Manager, computers must exist in the
Configuration Manager site database before you can advertise a task sequence to the
computer. Configuration Manager includes a feature for automatically adding target
computers to the site database. However, for reference computers, it is easier to
manually add the reference computer to the site database.

For more information about manually adding computers to the site database, see the
section, "How to Add a Computer to the Configuration Manager Database," in the
section, "How to Deploy Operating Systems in Configuration Manager," in the
Configuration Manager Documentation Library, which is installed with Configuration
Manager.

Managing Computer Collections in Configuration
Manager
In ZTI deployments using Configuration Manager, the task sequences must be
advertised to a collection of target computers. In Configuration Manager, collections are
a grouping of one or more computers. For more information about managing computer
collections, see the following sections in the Configuration Manager Documentation
Library, which is installed with Configuration Manager:

<!-- p.307 -->

     "Introduction to Collections in Configuration Manager"

     "Planning for Collections in Configuration Manager"

     "Operations and Maintenance for Collections in Configuration Manager"

     "Security and Privacy for Collections in Configuration Manager"

Managing Distribution Points in Configuration Manager
In ZTI deployments using Configuration Manager, distribution points are the repository
for the files being deployed to the reference and target computers. Your organization
may have more than one distribution point. Configure distribution points for the
operating system images and software packages that MDT uses, ensuring that each
reference and target computer has a persistent, high-speed connection to a distribution
point.

If you make any changes to the operating system images and software packages that
MDT uses, update the distribution points where these images and packages are stored.

For more information about managing distribution points, see the section, "Operations
and Maintenance for Content Management in Configuration Manager," in the
Configuration Manager Documentation Library, which is installed with Configuration
Manager.

Configuring ZTI Task Sequence Steps in Configuration
Manager
After you create a ZTI task sequence using the Create MDT Task Sequence Wizard in
Configuration Manager, you can customize it using the Configuration Manager console.
The Configuration Manager console allows you to:

     Add new task sequence steps

     Modify existing task sequence steps

     Delete existing task sequence steps

     You perform these tasks using the standard methods available in the Configuration
     Manager console. For more information about:

     Configuring ZTI task sequence steps using the Configuration Manager console in
     Configuration Manager, see the section, "How to Edit an Existing Task Sequence,"
     in the section, "How to Manage Task Sequences in Configuration Manager," in the

<!-- p.308 -->

     Configuration Manager Documentation Library, which is installed with
     Configuration Manager.

     Task sequences, see the section, "Planning a Task Sequences Strategy in
     Configuration Manager," in the Configuration Manager Documentation Library,
     which is installed with Configuration Manager.

Configuring ZTI Server Role Task Sequence Steps in
Configuration Manager
ZTI can help automate the deployment of server roles in Windows Server. Configure ZTI
task sequence steps in Configuration Manager to deploy the supported server roles,
which include:

     AD DS

     DNS Server

     DHCP Server

     The process for configuring the server role task sequence steps is similar for ZTI
     and LTI. For more information about configuring server role task sequence steps
     for ZTI in Configuration Manager, see Configuring Server Role Task Sequence
     Steps.

Performing UDI Deployments
You perform UDI deployments in MDT using Configuration Manager within an AD DS
domain, within a Windows workgroup, or from removable media.

  ７ Note

  If you are unfamiliar with UDI, review the UDI terms and terminology in the section,
  "UDI Concepts", in the MDT document Microsoft Deployment Toolkit Reference.
  Familiarizing yourself with these terms and terminology will help you be more
  successful in applying the remainder of this guide to your organization.

Perform UDI deployments by:

     Reviewing the overview information for UDI deployments as described in Overview
     of UDI Deployments

<!-- p.309 -->

     Preparing the UDI deployment environment as described in Preparing the UDI
     Deployment Environment

     Preparing for UDI deployment to the reference computer as described in Preparing
     for UDI Deployment to the Reference Computer

     Deploying to and capturing an image of the reference computer in UDI as
     described in Deploying To and Capturing an Image of the Reference Computer
     Using UDI

     Preparing for UDI deployment to the target computers as described in Preparing
     for UDI Deployment to Target Computers

     Deploying captured images to the target computer using UDI as described in
     Deploying Captured Images to Target Computers Using UDI

Overview of UDI Deployments
UDI allows the interactive deployment of Windows operating systems and applications
using Configuration Manager. Typically, when deploying operating systems using the
OSD feature in Configuration Manager and ZTI in MDT, you must provide all the
information necessary to deploy the operating system. Prior to performing the
deployment, the information is configured in configuration files or in databases (such as
the CustomSettings.ini file or the MDT DB). During the ZTI deployment process, ZTI
converts the appropriate configuration settings to task sequence variables, which the
MDT task sequences consume for UDI. All of the configuration settings must be
provided before you can initiate the deployment.

UDI provides a wizard-driven interface that runs on the target computer, which allows
you to provide configuration information immediately prior to operating system and
application deployment. This allows you to create generic OSD task sequences, and then
have other users provide computer specific information at the time of deployment,
which provides greater flexibility in the deployment process.

  ７ Note

  If you are unfamiliar with UDI, review the UDI terms and terminology in the section,
  "UDI Concepts", in the MDT document Microsoft Deployment Toolkit Reference.
  Familiarizing yourself with these terms and terminology will help you be more
  successful in applying the remainder of this guide to your organization.

Review the overview information about UDI deployments in the subsequent sections:

<!-- p.310 -->

     Overview of UDI in MDT Deployment Scenarios

     Overview of Built-in UDI Components

     Table 135 lists additional content resources for UDI administration and
     development.

Table 135. Additional Content Resources for UDI
Administration and Development

                                                                                 ﾉ   Expand table

 Resource                               Description

 Overview of UDI Administration         This content provides an overview of UDI administration.

 Configuring UDI Wizard Behavior        This content describes how to configure the behavior of
                                        the UDI Wizard using the UDI Wizard Designer.

 Review the UDI Wizard Designer User    This content provides an overview of the UI for the UDI
 Interface                              Wizard designer.

 "UDI Reference" section in Microsoft   This content provides reference material for UDI,
 Deployment Toolkit Reference           including information on:

                                        - OSDResults

                                        - AppInstaller

                                        - Built-in UDI stage groups and stages

                                        - UDI tasks

                                        - UDI validators

                                        - UDI wizard pages

 User-Driven Installation Developers    This content provides guidance on how to customized
 Guide                                  and extend UDI to meet the needs of your organization.

 "UDI Concepts" section in Microsoft    This content provides definitions of UDI terms and
 Deployment Toolkit Reference           terminology and conceptual information about UDI.

Overview of UDI in MDT Deployment Scenarios
UDI supports the New Computer, Refresh Computer, and Replace Computer MDT
deployment scenarios, which were described in Identifying Deployment Scenarios. UDI

<!-- p.311 -->

supports these deployments scenarios using the Configuration Manager task sequence
templates provided with MDT. Table 136 lists the MDT deployment scenarios and the
corresponding UDI task sequence templates used to perform the deployment scenario.

Table 136. MDT Deployment Scenarios and UDI Task
Sequence Templates Used to Perform the Scenarios

                                                                              ﾉ   Expand table

 Deployment        UDI tasks sequences used
 scenario

 New Computer      Run task sequence created using User Driven Installation Task Sequence task
                   sequence template.

 Refresh           Run task sequence created using User Driven Installation Task Sequence task
 Computer          sequence template.

 Replace           - Run task sequence created using User Driven Installation Replace Task
 Computer          Sequence task sequence template on existing computer.

                   - Run the task sequence created using the User Driven Installation Task
                   Sequence task sequence template on the new computer.

The UDI Wizard is run by the UDI Wizard task sequence step in these task sequences at
the appropriate place in the task sequence. To identify how UDI performs each of the
MDT deployment scenarios, see the subsequent sections:

     UDI in the New Computer Deployment Scenario

     UDI in the Refresh Computer Deployment Scenario

     UDI in the Replace Computer Deployment Scenario

     For more details about how UDI operates in each of these MDT deployment
     scenarios, see the corresponding sections in "UDI Stage Reference" in Microsoft
     Deployment Toolkit Reference.

UDI in the New Computer Deployment Scenario

For the New Computer Deployment Wizard, the operating system images can be in the
following locations:

     On a distribution point. This method uses the traditional OSD deployment
     methodology in Configuration Manager.

<!-- p.312 -->

On a local disk on the target computer. This method leverages the prestaged
media feature in Configuration Manager.

Task sequences created using the User Driven Installation Task Sequence task
sequence template automatically detect which method to use and perform the
deployment accordingly. The New Computer deployment scenario always begins
with the target computer running Windows PE, which is how the tasks sequence
knows the difference between the New Computer deployment scenario and the
Refresh Computer deployments scenario. Figure 2 illustrates how UDI is used in the
New Computer deployment scenario using the traditional OSD deployment
methodology in Configuration Manager with the operating system image located
on a distribution point.

Figure 2. Process flow for UDI performing the New Computer deployment
scenario for images stored on distribution points

Figure 3 illustrates how UDI is used in the New Computer deployment scenario
using the prestaged media feature in Configuration Manager with the operating
system image located on a local disk on the target computer.

<!-- p.313 -->

     Figure 3. Process flow for UDI performing the New Computer deployment
     scenario for prestaged media

UDI in the Refresh Computer Deployment Scenario

Task sequences used to perform the Refresh Computer scenario use the same task
sequence template as the New Computer scenario, the User Driven Installation Task
Sequence task sequence template. The Refresh Computer deployment scenario always
begins with the target computer running the existing Windows operating system, which
is how the tasks sequence knows the difference between the Refresh Computer
deployment scenario and the New Computer deployments scenario. Figure 4 illustrates
how UDI is used in the Refresh Computer deployment scenario.

<!-- p.314 -->

Figure 4. Process flow for UDI performing the Refresh Computer deployment scenario

UDI in the Replace Computer Deployment Scenario

The Replace Computer scenario requires the following task sequences.

     A task sequence created using the User Driven Installation Replace Task Sequence
     task sequence template. This task sequence is run first on the existing computer
     and is used to capture user state migration data to a network shared folder or to a
     USB disk that is attached to the existing computer.

     A task sequence created using the User Driven Installation Task Sequence task
     sequence template. This task sequence is run second on the replacement
     computer and is used to install the operating system, install the applications, and
     to restore user state migration data saved by the task sequence run on the existing
     computer.

<!-- p.315 -->

Figure 5 illustrates how UDI is used in the Replace Computer deployment scenario.

Figure 5. Process flow for UDI performing the Replace Computer deployment
scenario

<!-- p.316 -->

Overview of Built-in UDI Components
UDI comes with built-in Configuration Manager task sequences, stage groups, stages,
tasks, validators, and wizard pages that can perform most common deployment
scenarios without the assistance of a developer. These built-in components can be
configured using the UDI Wizard Designer:

For more information about the built-in UDI components, see the following sections in
the Microsoft Deployment Toolkit Reference:

     "UDI Stage Reference"

     "UDI Wizard Page Reference"

     "UDI Task Reference"

     "UDI Validator Reference"

     In addition to these built-in components, you can create custom wizard pages,
     wizard page editors, tasks, and validators using the UDI software development kit
     (SDK). The UDI SDK is installed with MDT and contains example solutions for
     Microsoft Visual Studio 2010. For more information about extending UDI using the
     UDI SDK, see the MDT document User-Driven Installation Developers Guide.

Preparing the UDI Deployment Environment
After you have prepared the prerequisite infrastructure for MDT, you are ready to
prepare the MDT deployment environment for UDI.

To prepare the MDT deployment environment for UDI
deployments

   1. Preparing the prerequisite infrastructure as described in Prepare the Prerequisite
     Infrastructure for UDI Deployments.

   2. Install a new instance of MDT on the deployment server, or upgrade an existing
     instance of MDT to MDT as described in Install or Upgrade to MDT for UDI
     Deployments.

   3. Obtain the software that UDI requires as described in Obtain the Software That the
     UDI Deployment Process Requires.

   4. Enable Configuration Manager console integration with MDT as described in
     Enable Configuration Manager Console Integration for UDI.

<!-- p.317 -->

Prepare the Prerequisite Infrastructure for UDI Deployments
UDI deployments require that a properly configured Configuration Manager
infrastructure exist prior to installing MDT and performing deployments. Ensure that
your new or existing Configuration Manager infrastructure is specifically optimized for
the Operating System Deployment feature.

  ７ Note

  Windows PowerShell version 2.0 or later must be installed on any computer on
  which MDT is installed for management of UDI deployments.

For more information about:

     Hardware and software requirements for Configuration Manager, see Supported
     Configurations for Configuration Manager.

     Configuring a Configuration Manager infrastructure to support UDI deployments,
     see the section, "Step 1: Prepare the Prerequisite Infrastructure", in the MDT
     document Quick Start Guide for User-Driven Installation.

Install or Upgrade to MDT for UDI Deployments

The first step in performing UDI deployments is to have at least one instance of MDT
running in your environment. Install MDT on each computer that has the Configuration
Manager console installed and that you will use to create or edit task sequences that
MDT generates. If your existing environment has:

     No computers currently running MDT or a previous version of MDT, install one or
     more new instances of MDT as described in Installing a New Instance of MDT.

     One or more computers running a previous version of MDT, upgrade those
     instances to MDT as described in Upgrading to MDT. After the upgrade process is
     complete:

        Run the Configure ConfigMgr Integration Wizard. This wizard must be run
        after the upgrade to register the new components and install the UDI new task
        sequence templates.

        Ensure you create a new Microsoft Deployment Toolkit Files package for any
        new UDI task sequences you create. The existing Microsoft Deployment Toolkit
        Files package can be used for any UDI task sequences created prior to the

<!-- p.318 -->

         upgrade, but a new Microsoft Deployment Toolkit Files package must be
         created for new UDI task sequences.

         Ensure any UDI task sequences created prior to the upgrade use the Microsoft
         Deployment Toolkit Files package that existed prior to the upgrade. You can
         modify these UDI task sequences, but you cannot use any of the new MDT task
         sequence actions or steps. To use the new MDT task sequence actions or steps,
         create a new UDI task sequence.

Obtain the Software That the UDI Deployment Process Requires

Collect the software needed during the UDI deployment process. This software will be
imported or added to deployment shares unless it already exists in the deployment
share.

  ７ Note

  UDI requires Configuration Manager.

Required software includes:

     Operating system source files for each operating system to be deployed to the
     reference and target computers

     Operating system packages for the operating systems, such as security updates,
     feature packs, and language packs

     Device drivers for the reference and target computers that are not included as part
     of the operating system

     Applications that are to be installed as a part of the operating system image or
     during the deployment of the reference image

     USMT source files used to create a software package that is deployed to the target
     computers to capture user state migration data

Enable Configuration Manager Console Integration for UDI

Before you can use the Configuration Manager integration features of MDT, run the
Configure ConfigMgr Integration Wizard. This wizard copies the appropriate
Configuration Manager integration files to the Configuration Manager _root (where

<!-- p.319 -->

Configuration Manager _root is the folder in which the Configuration Manager console is
installed).

The wizard also adds WMI classes for the new MDT custom actions. You add these
classes by compiling a .mof file that contains the new class definitions.

To run the Configure ConfigMgr Integration Wizard

  ７ Note

  The Configuration Manager console should be closed when performing this
  procedure.

      Select Start, and then point to All Programs. Point to Microsoft Deployment
      Toolkit, and then select Configure ConfigMgr Integration.

      The Configure ConfigMgr Integration Wizard starts.

      Complete the Configure ConfigMgr Integration Wizard using the information in
      Table 137. Accept the default values unless otherwise specified.

      Table 137. Information for Completing the Configure
      ConfigMgr Integration Wizard

                                                                               ﾉ   Expand table

       On this wizard   Do this
       page

       Options          1. Verify that the Install the MDT console extensions for System Center
                        2012 R2 Configuration Manager check box is selected.

                        2. Verify that the Add the MDT task sequence actions to a System
                        Center 2012 R2 Configuration Manager server check box is selected.

                        3. In Site server name, type ConfigMgr_server_name (where
                        ConfigMgr_server_name is the name of the Configuration Manager server
                        on which to install MDT integration).

                        4. In Site code, type ConfigMgr_site_code (where ConfigMgr_site_code is
                        the Configuration Manager site code that installs MDT integration).

                        5. Select Next.

                        The Site Server Name and Site Code fields will be automatically

<!-- p.320 -->

      On this wizard   Do this
      page

                       populated with the most recent connection details if the Configuration
                       Manager console has been opened once.

      Confirmation     Select Finish.

     The Configure ConfigMgr Integration Wizard finishes, and MDT is integrated with
     Configuration Manager.

Preparing for UDI Deployment to the Reference
Computer
Regardless of the MDT deployment scenario you are performing using UDI, always start
by creating a reference computer, and then capturing an image of that computer. Later
in the MDT deployment process, you will deploy the captured image of your reference
computer to the appropriate target computers. In addition, you can use existing
operating system images in WIM format.

Create a reference computer for each image that you want to create for deployment to
the target computers. For more information about determining the number of images
required in your organization (and subsequently the number of reference computers
required), see Estimate Storage Requirements for Configuration Manager Distribution
Points. For more information about the use of reference computers in MDT
deployments, see Using Reference Computers in MDT Deployments.

To prepare for deployment to the reference computer

   1. Create a new task sequence that will deploy the target operating system to the
     reference computer using the Create MDT Task Sequence Wizard in the
     Configuration Manager console as described in Creating a UDI Task Sequence
     Using MDT Task Sequence Templates.

        Tip

       Create the task sequence for deploying to the reference computer based on
       the User-Driven Installation task sequence template included in MDT.

   2. Configure Configuration Manager to contain the appropriate software for
     deployment to the reference computer, including the following:
