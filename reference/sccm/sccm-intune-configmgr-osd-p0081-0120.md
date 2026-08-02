---
title: "OS deployment documentation — pages 81-120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0081-0120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0081-0120
family: sccm
documentKind: "doc"
abstract: "After you make changes to a boot image, update the boot image on the distribution points that already have it. This process makes the most current version of the boot image available to clients. For more information, see Manage content you've distributed. Modify the properties o"
---

# OS deployment documentation — pages 81-120

<!-- p.81 -->

     After you make changes to a boot image, update the boot image on the
     distribution points that already have it. This process makes the most current
     version of the boot image available to clients. For more information, see Manage
     content you've distributed.

Modify the properties of a boot image
   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Boot Images node.

   2. Select the boot image that you want to modify.

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. Set any of the following settings to change the behavior of the boot image:

Images

On the Images tab, if you change the properties of the boot image by using an external
tool, select Reload.

Drivers
On the Drivers tab, add the Windows device drivers that WinPE requires to boot.
Consider the following points when you add device drivers:

     Make sure that the drivers that you add to the boot image match the architecture
     of the boot image.

     To only display drivers for the architecture of the boot image, select Hide drivers
     that do not match the architecture of the boot image. The architecture of the
     driver is based on the architecture reported in the INF from the manufacturer.

     WinPE already comes with many drivers built-in. Add only network and storage
     drivers that aren't included in WinPE.

     Add only network and storage drivers to the boot image, unless there are
     requirements for other drivers in WinPE.

     To only display storage and network drivers, select Hide drivers that are not in a
     storage or network class (for boot images). This option also hides other drivers
     that aren't typically needed for boot images, such as video or modem drivers.

<!-- p.82 -->

     To hide drivers that don't have a valid digital signature, select Hide drivers that are
     not digitally signed.

  ７ Note

  Import device drivers into the drivers catalog before you add them to a boot
  image. For information about how to import device drivers, see Manage drivers.

Customization
On the Customization tab, select any of the following settings:

     Select the Enable Prestart Commands option to specify a command to run before
     the task sequence runs. When you enable this option, also specify the command
     line to run and any support files required by the command.

       ２ Warning

       Add cmd /c to the start of the command line. If you don't specify cmd /c , the
       command won't close after it runs. The deployment continues to wait for the
       command to finish and won't start any other configured commands or
       actions.

        Tip

       During task sequence media creation, the wizard writes the package ID and
       prestart command line to the CreateTSMedia.log file. This information
       includes the value for any task sequence variables. This log is on the computer
       that runs the Configuration Manager console. Review this log file to verify the
       values for the task sequence variables.

     Set the Windows PE Background settings to specify whether you want to use the
     default WinPE background or a custom background.

     Configure the Windows PE scratch space (MB), which is temporary storage (RAM
     drive) used by WinPE. For example, when an application is run within WinPE and
     needs to write temporary files, WinPE redirects the files to the scratch space in
     memory to simulate the presence of a hard disk. By default, this amount is 512 MB
     for devices with more than 1 GB of RAM, otherwise the default is 32 MB.

<!-- p.83 -->

     Select Enable command support (testing only) to open a command prompt by
     using the F8 key while the boot image is deployed. This option is useful for
     troubleshooting while you're testing your deployment. Using this setting in a
     production deployment isn't advised because of security concerns.

     Set default keyboard layout in WinPE: Configure the default keyboard layout for a
     boot image. If you select a language other than en-us, Configuration Manager still
     includes en-us in the available input locales. On the device, the initial keyboard
     layout is the selected locale, but the user can switch the device to en-us if needed.

   Tip

  Use the Set-CMBootImage PowerShell cmdlet to configure these settings from a
  script.

Optional Components
On the Optional Components tab, specify the components that are added to Windows
PE for use with Configuration Manager. For more information about available optional
components, see WinPE: Add packages (Optional Components Reference).

The following components are required by Configuration Manager and always added to
boot images:

     Scripting (WinPE-Scripting)
     Startup (WinPE-SecureStartup)
     Network (WinPE-WDS-Tools)
     Scripting (WinPE-WMI)

The Components list shows additional items that are added to this boot image. To add
more components, select the gold asterisk. To remove a component, select it from the
list, and then select the red X.

The following components are commonly used by customers:

     Microsoft .NET (WinPE-NetFX): This component is a prerequisite for PowerShell. It's
     one of the larger optional components.
     Windows PowerShell (WinPE-PowerShell): This component requires .NET, and adds
     limited PowerShell support. If you run custom PowerShell scripts during the WinPE
     phase of your task sequence, add this component. There are other components
     that may be required for other PowerShell cmdlets.

<!-- p.84 -->

     HTML (WinPE-HTA): If you run custom HTML applications during the WinPE phase
     of your task sequence, add this component.

For more information about adding languages, see Configure multiple languages.

Data Source
On the Data Source tab, update any of the following settings:

     To change the source file of the boot image, set Image path and Image index.

     To create a schedule for when the site updates the boot image, select Update
     distribution points on a schedule.

     If you don't want the content of this package to age out of the client cache to
     make room for other content, select Persist content in client cache.

     To specify that the site only distributes changed files when it updates the boot
     image package on the distribution point, select Enable binary differential
     replication (BDR). This setting minimizes the network traffic between sites. BDR is
     especially useful when the boot image package is large and the changes are
     relatively small.

     If you use the boot image in a PXE-enabled deployment, select Deploy this boot
     image from the PXE-enabled distribution point. For more information, see Use
     PXE to deploy Windows over the network.

Data Access
On the Data Access tab, you can configure package share settings. If needed in your
environment, set the option to Copy the content in this package to a package share on
distribution points. You then have the additional option to Use a custom name for the
package share and specify the custom Share name. Additional disk space is required on
distribution points when you enable this option. It applies to all distribution points that
receive this boot image.

Distribution Settings
On the Distribution Settings tab, select any of the following settings:

     In the Distribution priority list, specify the priority level. Configuration Manager
     uses this priority list when the site distributes multiple packages to the same
     distribution point.

<!-- p.85 -->

     If you want to enable on-demand content distribution to preferred distribution
     points, select Enable for on-demand distribution. When you enable this setting, if
     a client requests the content for the package and the content isn't available on any
     distribution points, then the management point distributes the content. For more
     information, see On-demand content distribution.

     To specify how you want the site to distribute the boot image to distribution points
     that are enabled for prestaged content, set the Prestaged distribution point
     settings. For more information about prestaged content, see Prestage content.

Content Locations
On the Content Locations tab, select the distribution point or distribution point group,
and use the following actions:

     Validate: Check the integrity of the boot image package on the selected
     distribution point or distribution point group.

     Redistribute: Distribute the boot image to the selected distribution point or
     distribution point group again.

     Remove: Delete the boot image from the selected distribution point or distribution
     point group.

Security
On the Security tab, view the administrative users that have permissions to this object.

Configure a boot image for PXE
Before you can use a boot image for a PXE-based deployment, configure the boot
image to deploy from a PXE-enabled distribution point.

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Boot Images node.

   2. Select the boot image that you want to modify.

   3. On the Home tab of the ribbon, in the Properties group, select Properties.

   4. On the Data Source tab, select Deploy this boot image from the PXE-enabled
     distribution point. For more information, see Use PXE to deploy Windows over the
     network.

<!-- p.86 -->

Configure multiple languages

   Tip

  You can configure the default keyboard layout on the properties of a boot image.
  For more information, see Customization.

Boot images are language neutral. This functionality allows you to use one boot image
to display the task sequence text in multiple languages while in WinPE. Include the
appropriate language support from the boot image Optional Components tab. Then set
the appropriate task sequence variable to indicate which language to display. The
language of the deployed OS is independent from the language in WinPE. The language
that WinPE displays to the user is determined as follows:

     When a user runs the task sequence from an existing OS, Configuration Manager
     automatically uses the language configured for the user. When the task sequence
     automatically runs as the result of a mandatory deployment deadline,
     Configuration Manager uses the language of the OS.

     For OS deployments that use PXE or media, set the language ID value in the
     SMSTSLanguageFolder variable as part of a prestart command. When the
     computer boots to WinPE, messages are displayed in the language that you
     specified in the variable. If there's an error accessing the language resource file in
     the specified folder, or you don't set the variable, WinPE displays messages in the
     default language.

       ７ Note

       When you protect media with a password, the text that prompts the user for
       the password is always displayed in the WinPE language.

Use the following procedure to set the WinPE language for PXE or media-initiated OS
deployments.

Set the Windows PE language for a PXE or media-
initiated OS deployment
   1. Before you update the boot image, verify that the appropriate task sequence
     resource file (tsres.dll) is in the corresponding language folder on the site server.

<!-- p.87 -->

     For example, the English resource file is in the following location:
      <ConfigMgrInstallationFolder>\OSD\bin\x64\00000409\tsres.dll

   2. As part of your prestart command, set the SMSTSLanguageFolder environment
     variable to the appropriate language ID. The language ID must be specified by
     using decimal and not hexadecimal format. For example, to set the language ID to
     English, specify the decimal value 1033, not the hexadecimal value 00000409 of the
     folder name.

Next steps
Customize boot images

Manage OS images

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.88 -->

Customize boot images with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Each version of Configuration Manager supports a specific version of the Windows
Assessment and Deployment Kit (Windows ADK). You can service, or customize, boot
images from the Configuration Manager console when they're based on a Windows PE
(WinPE) version from the WinPE add-on of a supported version of the Windows ADK.
For more information on how to customize boot images in the Configuration Manager
console, see Manage boot images.

For boot images with other versions of WinPE, customize them by using another
method. For example, use the Deployment Image Servicing and Management (DISM)
command-line tool. Then import the boot images into Configuration Manager to use
with OS deployments.

For example, you install the Windows ADK and WinPE add-on for Windows 11 on the
site server. For x64 boot images based on WinPE version 11 from the WinPE add-on for
Windows 11, you can customize them from the Configuration Manager console.
However, while x86 boot images based on WinPE version 10 are supported, you need to
manually customize them from a different computer. Use the version of DISM that's
installed with the Windows ADK for Windows 10. Then, you can add the boot image to
the Configuration Manager console.

  ） Important

  The 32-bit versions of Windows PE (WinPE) in the WinPE add-ons for Windows 11
  and Windows Server 2022 aren't supported. The last supported version of 32-bit
  WinPE is available in the WinPE add-on for Windows 10, version 2004. For more
  information, see Download and install the Windows ADK.

The following steps summarize the process to customize an x86 boot image that uses
WinPE version 10:

      Install the Windows ADK and WinPE add-on for Windows 10, version 2004
      Use the DISM command-line tool to:
         Mount the x86 boot image
         Add optional components

<!-- p.89 -->

       Add drivers
       Commit the changes to the boot image
     Import the customized boot image to Configuration Manager

Required components
The procedures in this article demonstrate how to add the WinPE optional components
that Configuration Manager requires:

     WinPE-WMI: Adds Windows Management Instrumentation (WMI) support.

     WinPE-Scripting: Adds Windows Script Host (WSH) support.

     WinPE-WDS-Tools: Installs Windows Deployment Services (WDS) tools.

There are other WinPE packages available to add. For more information, see WinPE
optional components reference.

Customize the image with DISM
  1. On a computer that doesn't have a version of the Windows ADK and doesn't have
     any Configuration Manager components installed, install the Windows ADK
     ( adksetup.exe ) and WinPE add-on ( adkwinpesetup.exe ). For more information, see
     Other ADK downloads.

        Tip

       You only need to install the Deployment Tools component for this process.

  2. Copy the boot image ( winpe.wim ) from the WinPE installation folder, which by
     default is C:\Program Files (x86)\Windows Kits\10\Assessment and Deployment
     Kit\Windows Preinstallation Environment\x86\en-us . Create a working directory

     on the computer where you'll customize the boot image, and copy the default
     image file to it. This procedure uses C:\WinPE as the folder name. For example:

       PowerShell

       $workingDir = New-Item -Path "C:\" -Name "WinPE" -ItemType "directory"
       $peDir = "C:\Program Files (x86)\Windows Kits\10\Assessment and
       Deployment Kit\Windows Preinstallation Environment\x86\en-us"
       Copy-Item "$($peDir)\winpe.wim" -Destination $workingDir

<!-- p.90 -->

3. Create a new folder to use as the mount point for the boot image. This procedure
  uses C:\WinPEMount as the folder name.

    PowerShell

    New-Item -Path "C:\" -Name "WinPEMount" -ItemType "directory"

4. Use DISM to mount the boot image to a local Windows PE folder. For example,
  type the following command line:

    ） Important

    Make sure you're using the version of DISM from the installed Windows ADK.
    Windows may default to the OS version, which may not technically support
    the version of WinPE that you're servicing. For more information, see DISM
    supported platforms.

    PowerShell

    Set-Location "C:\Program Files (x86)\Windows Kits\10\Assessment and
    Deployment Kit\Deployment Tools\amd64\DISM\"

    .\dism.exe /mount-wim /wimfile:C:\WinPE\winpe.wim /index:1
    /mountdir:C:\WinPEMount

     Tip

    For more information on DISM commands, see the DISM Reference.

5. After you mount the boot image, use DISM to add optional components to the
  boot image. By default, the optional components are located in C:\Program Files
  (x86)\Windows Kits\10\Assessment and Deployment Kit\Windows Preinstallation

  Environment\x86\WinPE_OCs .

    ７ Note

    This procedure uses the default location and en-us locale for the optional
    components. The path you use might be different depending on the version
    and installation options you choose for the Windows ADK, and the locale of
    the boot image.

<!-- p.91 -->

  Type the following commands to install the optional components that
  Configuration Manager requires:

    PowerShell

    $ocpath = "C:\Program Files (x86)\Windows Kits\10\Assessment and
    Deployment Kit\Windows Preinstallation Environment\x86\WinPE_OCs"

    .\dism.exe /image:C:\WinPEMount /add-package
    /packagepath:"$($ocpath)\winpe-wmi.cab"

    .\dism.exe /image:C:\WinPEMount /add-package
    /packagepath:"$($ocpath)\winpe-scripting.cab"

    .\dism.exe /image:C:\WinPEMount /add-package
    /packagepath:"$($ocpath)\winpe-wds-tools.cab"

    .\dism.exe /image:C:\WinPEMount /add-package
    /packagepath:"$($ocpath)\en-us\winpe-wmi_en-us.cab"

    .\dism.exe /image:C:\WinPEMount /add-package
    /packagepath:"$($ocpath)\en-us\winpe-scripting_en-us.cab"

    .\dism.exe /image:C:\WinPEMount /add-package
    /packagepath:"$($ocpath)\en-us\winpe-wds-tools_en-us.cab"

     Tip

    For more information about the different packages that you can add to the
    boot image, see WinPE optional components reference.

6. If needed, use DISM to add specific drivers to the boot image. For example, type
  the following command to add a driver to the boot image:

    PowerShell

    .\dism.exe /image:C:\WinPEMount /add-driver
    /driver:C:\Drivers\driver.inf

7. When you're done making changes, type the following command to unmount the
  boot image file and commit the changes:

    PowerShell

    .\dism.exe /unmount-wim /mountdir:C:\WinPEMount /commit

<!-- p.92 -->

       ） Important

       Whether or not you will use this customized image, make sure to unmount it
       when you're done. To not save your changes but still unmount the image, use
       the /discard parameter instead of the /commit option.

  8. Copy the customized boot image to your site's centralized package source
     location.

Import the boot image
Add the updated boot image to Configuration Manager to make it available to use in
your task sequences. Use the following steps to import the updated boot image:

  1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and select the Boot Images node.

  2. On the Home tab of the ribbon, in the Create group, select Add Boot Image. This
     action starts the Add Boot Image Wizard.

  3. On the Data Source page, specify the following options:

          Specify the Path to the updated boot image file. The specified path must be a
          valid network path in the UNC format. For example:
           \\server\share\WinPE10x86\winpe.wim

          Choose the specific boot image from the Boot Image list. If the WIM file
          contains multiple images, each image is listed.

  4. On the General page, specify the following options:

          Name: Specify a unique name for the boot image.

          Version: Specify a version number for the boot image. This value doesn't
          have to be the OS version, it's a string that you maintain for the boot image
          version.

          Comment: Specify an optional description of how the boot image is used to
          better identify it in the console.

  5. Complete the wizard.

<!-- p.93 -->

Enable command shell for testing
You can enable a command shell in the boot image to open a command prompt by
using the F8 key while the boot image is deployed. This option is useful for
troubleshooting while you're testing your deployment. Using this setting in a production
deployment isn't advised because of security concerns.

Use the following steps to enable the command shell on a custom boot image:

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Boot Images node.

   2. Find the new boot image in the list and identify the package ID for the image. You
     can find the package ID in the Image ID column for the boot image.

   3. From a command prompt, type wbemtest to open the Windows Management
     Instrumentation Tester.

   4. For the Namespace, type \\<smsprovider>\root\sms\site_<sitecode> , and then
     select Connect.

   5. Select Open Instance. Type sms_bootimagepackage.packageID="<packageID>" , and
     then select OK.

   6. Select Refresh Object, and then in the Properties pane select EnableLabShell.

   7. Select Edit Property, change the value to TRUE, and select Save Property.

   8. Select Save Object, and then exit the Windows Management Instrumentation
     Tester.

  ７ Note

  When you boot to WinPE from a customized boot image that includes tools that
  you added, you can open a command prompt from WinPE and type the file name
  of the tool to run it. The location of these tools are automatically added to the path
  variable.

Distribute content
Before you can use the boot image in a task sequence, distribute the boot image to
distribution points. Use the following steps to distribute the boot image:

<!-- p.94 -->

   1. In the Configuration Manager console, go to the Software Library workspace,
     expand Operating Systems, and then select the Boot Images node.

   2. Select the new custom boot image.

   3. On the Home tab of the ribbon, in the Deployment group, select Update
     Distribution Points.

Next steps
Manage boot images

Support for the Windows ADK in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.95 -->

Manage OS images with Configuration
Manager
07/31/2025

Applies to: Configuration Manager (current branch)

OS images in Configuration Manager are stored in the Windows image (WIM) file format.
These images are a compressed collection of reference files and folders use to install and
configure a new OS on a computer. Many OS deployment scenarios require an OS image.

OS image types
You can use a default OS image, or build the OS image from a reference computer that you
configure. When you build the reference computer, you add OS files, drivers, support files,
software updates, tools, and applications to the OS. Then you capture it to create the image
file.

Default image
The Windows installation files include the default OS image. This image is a basic OS image
that contains a standard set of drivers. When you use the default OS image, use task sequence
steps to install apps and make other configurations after the OS installs on a device. Locate the
default OS image in the Windows source files: \Sources\install.wim .

Default image advantages

        The image size is smaller than a captured image.

        Installing apps and configurations with task sequence steps is more dynamic. For
        example, change the configurations and apps that install in the task sequence, without
        having to reimage the device.

Default image disadvantages

        OS installation can take more time. The application installation and other configurations
        occur after the OS installation completes.

Captured image from a reference computer

<!-- p.96 -->

To create a customized OS image, build a reference computer with the desired OS then install
applications and configure settings. To create the WIM file, capture the OS image from the
reference computer. Manually build the reference computer, or use a task sequence to
automate some or all of the build steps. For more information, see Customize OS images.

Captured image advantages

     The installation can be faster than using the default image. For example, applications can
     be preinstalled with the captured OS image. Then you don't need to install those same
     applications later by using task sequence steps.

Captured image disadvantages
     The image size is potentially larger than the default image.

     Need to create a new image when you require updates for applications and tools.

Add an OS image
Before you can use an OS image, add it to your Configuration Manager site.

   1. In the Configuration Manager console, go to the Software Library workspace, expand
     Operating Systems, and then select the Operating System Images node.

   2. On the Home tab of the ribbon, in the Create group, select Add Operating System
     Image. This action starts the Add Operating System Image Wizard.

   3. On the Data Source page, specify the following information:

          Network Path to the OS image file. For example, \\server\share\path\image.wim .

          Accept Eula, by checking the box

          Extract a specific image index from the specified WIM file and then select an
          image index from the list. Starting in version 1902, this option automatically imports
          a single index rather than all image indexes in the file. Using this option results in a
          smaller image file, and faster offline servicing. It also supports the process to
          Optimize image servicing, for a smaller image file after applying software updates.

             ７ Note

             Configuration Manager doesn't modify the source image file. It creates a new
             image file in the same source directory.

<!-- p.97 -->

             This extraction process can fail for extremely large image files, for example over
             60 GB. The DISM error is Not enough storage is available to process this
             command. The command line that Configuration Manager uses is in the

             smsprov.log and dism.log. Manually run the same command and then import
             the image.

           Starting in version 1906, if you want to pre-cache content on a client, specify the
           Architecture and Language of the image. For more information, see Configure pre-
           cache content.

   4. On the General page, specify the following information. This information is useful for
     identification purposes when you have more than one OS image.

           Name: A unique name for the image. By default, the name comes from the WIM file
           name.

           Version: An optional version identifier. This property doesn't need to be the OS
           version of the image. It's often your organization's version for the package.

           Comment: An optional brief description.

   5. Complete the wizard.

For the PowerShell cmdlet equivalent of this console wizard, see New-
CMOperatingSystemImage.

Next, distribute the OS image to distribution points.

Distribute content to distribution points
Distribute OS images to distribution points the same as other content. Before you deploy the
task sequence, distribute the OS image to at least one distribution point. For more information,
see Distribute content.

Apply software updates to an image

  ） Important

  Due to changes in how Windows 11 updates are delivered through UUP patches, Offline
  Servicing of Windows 11 images and update packages using Configuration Manager is no
  longer supported. The recommended method to keep Windows 11 deployments up-to-

<!-- p.98 -->

  date is to acquire the latest patched Windows 11 ISO from Microsoft 365 admin center            .
  Once the updated Windows 11 ISO is obtained:

        Import the install.wim image from the ISO into the site for Operating System
        Images packages used in bare metal/refresh task sequences.
        Import the whole contents of the ISO into the site for Operating System Upgrade
        Packages used in-place upgrade task sequences.

  ７ Note

  This section applies to both Operating System Images and Operating System Upgrade
  Packages. It uses the general term "image" to refer to the Windows image file (WIM). Both
  of these objects have a WIM, which contains Windows installation files. Software updates
  are applicable to these files in both objects. The behavior of this process is the same
  between both objects.

Each month there are new software updates applicable to the image. Before you can apply
software updates to it, you need the following prerequisites:

     A software updates infrastructure
     Successfully synchronized software updates
     Downloaded the software updates to the content library on the site server

For more information, see Deploy software updates.

Apply applicable software updates to an image on a specified schedule. This process is
sometimes called offline servicing. On this schedule, Configuration Manager applies the
selected software updates to the image. It can then also redistribute the updated image to
distribution points.

  ） Important

  While you can select any software update that's applicable to the image based on version,
  DISM can only apply certain types of updates to the image. The OfflineServicingMgr.log
  file shows the following entry: Not applying this update binary, it is not supported .

The site database stores information about the image, including the software updates that
were applied at the time of the import. Software updates that you apply to the image since it
was initially added are also stored in the site database. When you start the wizard to apply
software updates, it retrieves the list of applicable software updates that the site hasn't yet

<!-- p.99 -->

applied to the image. Configuration Manager copies the software updates that you select from
the content library on the site server. It then applies the software updates to the image.

Servicing process
   1. In the Configuration Manager console, go to the Software Library workspace, expand
     Operating Systems, and then select either Operating System Images or Operating
     System Upgrade Packages.

   2. Select the object to which to apply software updates.

   3. On the ribbon, select Schedule Updates to start the wizard.

   4. On the Choose Updates page, select the software updates to apply to the image. It might
     take some time for the list of updates to appear in the wizard. Use the Filter to search for
     strings in the metadata. Use the System architecture drop-down list to filter on X86, X64,
     or All. You can select one, many, or all updates in the list. When you're finished selecting
     updates, select Next.

   5. On the Set Schedule page, specify the following settings, and then select Next.

      a. Schedule: Specify the schedule for when the site applies the software updates to the
        image.

     b. Continue on error: Select this option to continue to apply software updates to the
        image even when there's an error.

      c. Update distribution points with the image: Select this option to update the image on
        distribution points after the site applies the software updates.

   6. Complete the Schedule Updates Wizard.

  ７ Note

  To minimize the payload size, the servicing of OS upgrade packages and OS images
  removes the older version.

Servicing operations
In the Configuration Manager console, in either the OS Images or OS Upgrade Packages node,
add the following columns to the view:

     Scheduled Updates Date: This property shows the next defined schedule.

<!-- p.100 -->

     Scheduled Updates Status: This property shows the status. For example, Successful or In
     Process.

Select a specific image object, and then switch to the Update Status tab in the details pane.
This tab shows the list of updates in the image.

Select a specific image object, and select Properties in the ribbon. The Installed Updates tab
shows the list of updates in the image. The Servicing tab is a read-only view of the current
servicing schedule and the updates that you've scheduled to apply.

When the status is In Process, you can select Cancel Scheduled Updates on the ribbon. This
action cancels the active servicing process.

To troubleshoot this process, view the OfflineServicingMgr.log and dism.log files on the site
server. For more information, see Log files.

Specify the drive for offline OS image servicing
You can specify the drive that Configuration Manager uses during offline servicing of OS
images. This process can consume a large amount of disk space with temporary files. This
option gives you flexibility to select the drive to use.

   1. In the Configuration Manager console, go to the Administration workspace, expand Site
     Configuration, and select the Sites node. In the ribbon, select Configure Site
     Components and then choose Operating System Deployment.

   2. On the Offline Servicing tab, specify the option for A local drive to be used by offline
     servicing of images.

By default, this setting is Automatic. With this value, Configuration Manager selects the drive
on which it's installed.

If you select a drive that doesn't exist on the site server, Configuration Manager behaves the
same as if you select Automatic.

During offline servicing, Configuration Manager stores temporary files in the folder,
<drive>:\ConfigMgr_OfflineImageServicing . It also mounts the OS image in this folder.

Optimized image servicing
When you apply software updates to an OS image, you can optimize the output by removing
any superseded updates. The optimization to offline servicing only applies to images with a
single index.

<!-- p.101 -->

When you schedule the site to apply software updates to an OS image, it uses the Windows
Deployment Image Servicing and Management (DISM) command-line tool. During the
servicing process, this change introduces the following two additional steps:

     It runs DISM against the mounted offline image with the parameters /Cleanup-Image
     /StartComponentCleanup /ResetBase . If this command fails, the current servicing process

     fails. It doesn't commit any changes to the image.

     After Configuration Manager commits changes to the image and unmounts it from the
     file system, it exports the image to another file. This step uses the DISM parameter
     /Export-Image . It removes unneeded files from the image, which reduces the size.

Microsoft recommends that you regularly apply updates to your offline images. You don't have
to use this option every time you service an image. When you do this process each month, this
option provides you the greatest advantage by using it over time. For more information, see
Recommendations for Install Software Updates step.

While this option helps reduce the overall size of the serviced image, it does take longer to
complete the process. Use the wizard to schedule servicing during convenient times. It also
requires additional storage on the site server. You can customize the site to use an alternate
location. For more information, see Specify the drive for offline OS image servicing.

Process to optimize image servicing

   1. Start the servicing process.

   2. On the Set Schedule page, select the option to Remove superseded updates after the
     image is updated. This option isn't automatically enabled. If the image has more than
     one index, you can't use this option.

   3. To schedule image servicing, complete the wizard.

Validate and monitor the process using the OfflineServicing.log.

Prepare the OS image for multicast deployments
Use multicast deployments to allow more than one computer to simultaneously download an
OS image. The image is multicast to clients by the distribution point, rather than each client
downloading a copy of the image from the distribution point over a separate connection.
When you choose the OS deployment method to Use multicast to deploy Windows over the
network, configure the OS image to support multicast. Then distribute the image to a
multicast-enabled distribution point.

<!-- p.102 -->

1. In the Configuration Manager console, go to the Software Library workspace, expand
  Operating Systems, and then select the Operating System Images node.

2. Select the OS image that you want to distribute to a multicast-enabled distribution point.

3. On the Home tab of the ribbon, in the Properties group, select Properties.

4. Switch to the Distribution Settings tab, and configure the following options:

       Allow this package to be transferred via multicast (WinPE only): Select this option
       for Configuration Manager to simultaneously deploy OS images using multicast.

       Encrypt multicast packages: Specify whether the site encrypts the image before it's
       sent to the distribution point. If the image contains sensitive information, use this
       option. If the image isn't encrypted, its contents are visible in clear text on the
       network. Then an unauthorized user could intercept and view the image contents.

       Transfer this package only via multicast: Specify whether you want the distribution
       point to deploy the image only during a multicast session.

       If you select Transfer this package only via multicast, you must also specify the task
       sequence deployment option to Download content locally when needed by the
       running task sequence. For more information, see Deploy a task sequence.

5. Select OK to save the settings and close the image properties.

<!-- p.103 -->

Customize operating system images with
Configuration Manager
07/31/2025

Applies to: Configuration Manager (current branch)

Operating system images in Configuration Manager are WIM files. A WIM file represents a
compressed collection of reference files and folders that are required to successfully install and
configure an operating system on a computer. A custom operating system image is built and
captured from a reference computer. The reference computer is configured with all the
required operating system files, support files, software updates, tools, and other software apps.
The extent to which you manually configure the reference computer is up to you. You can:

     Completely automate the configuration of the reference computer by using a build and
     capture task sequence.
     Manually configure certain aspects of the reference computer and then automate the rest
     by using task sequences.
     Manually configure the reference computer without using task sequences.

Use the following sections to customize an operating system.

Prepare for the reference computer
There are several things to think about before you use capture an operating system image
from a reference computer.

Decide between an automated or manual configuration
The following outlines advantages and disadvantage for an automated and manual
configuration of the reference computer.

Automated configuration

Advantages of automated configuration

     The configuration can be completely unattended, which eliminates the requirement for an
     administrator or user to be present.

     You can reuse the task sequence to repeat the configuration of additional reference
     computers with a high level of confidence.

<!-- p.104 -->

     You can modify the task sequence to accommodate differences in reference computers
     without having to recreate the entire task sequence.

Disadvantages of automated configuration

     The initial action to build a task sequence can take a long time to create and test.

     If the reference computer requirements change significantly, it can take a long time to
     rebuild and retest the task sequence.

Manual configuration

Advantages of manual configuration

     You don't have to create a task sequence or take the time to test and troubleshoot the
     task sequence.

     You can install directly from CDs without putting all the software packages (including
     Windows itself) into a Configuration Manager package.

Disadvantages of manual configuration

     The accuracy of the reference computer configuration depends on the administrator or
     user who configures the computer.

     You must still verify and test that the reference computer is configured correctly.

     You can't reuse the configuration method.

     Requires a person to be actively involved throughout the process.

Considerations for the reference computer
The following lists the basic items to consider when you configure a reference computer.

     Operating system to deploy

     The reference computer must be installed with the operating system that you intend to
     deploy to your destination computers. For more information about the operating systems
     that you can deploy, see Infrastructure requirements for operating system deployment.

     Appropriate service pack

<!-- p.105 -->

The reference computer must be installed with the operating system that you intend to
deploy to your destination computers.

Appropriate software updates

Install all software applications that you want included in the operating system image that
you capture from the reference computer. You can also install software applications when
you deploy the captured operating system image to your destination computers.

Workgroup membership

The reference computer must be configured as a member of a workgroup.

Sysprep

The System Preparation (Sysprep) tool is a technology that you can use with other
deployment tools to install Windows operating systems onto new hardware. Sysprep
prepares a computer for disk imaging or delivery to a customer. Sysprep configures the
computer to create a new computer security identifier (SID) when the computer is
restarted. In addition, Sysprep cleans up user and computer-specific settings and data
that must not be copied to a destination computer.

You can manually Sysprep the reference computer by running the following command:

Sysprep /quiet /generalize /reboot

The /generalize option instructs Sysprep to remove system-specific data from the
Windows installation. System-specific information includes event logs, unique security IDs
(SIDs), and other unique information. After the unique system information is removed, the
computer restarts.

You can automate Sysprep by using the Prepare Windows for Capture task sequence step
or capture media.

  ） Important

  The Prepare Windows for Capture task sequence step attempts to reset the local
  administrator password on the reference computer to a blank value before Sysprep
  runs. If the Local Security policy Password must meet complexity requirements is
  enabled, this task sequence step fails to reset the administrator password. In this
  scenario, disable this policy before you run the task sequence.

For more information about Sysprep, see Sysprep (System Preparation) overview.

<!-- p.106 -->

     Appropriate tools and scripts required to mitigate installation
     scenarios

     Appropriate tools and scripts required to mitigate installation scenarios

     Appropriate desktop customization, such as wall paper, branding,
     and default user profile

     You can configure the reference computer with the desktop customization properties that
     you want to include when you capture the operating system image from the reference
     computer. Desktop properties include wallpaper, organizational branding, and a standard
     default user profile.

Manually build a reference computer
Use the following procedure to manually build a reference computer.

  ７ Note

  When you manually build the reference computer, you can capture the operating system
  image by using capture media. For more information, see Create capture media.

To manually build the reference computer
  1. Identify the computer to use as the reference computer.

  2. Configure the reference computer with the appropriate operating system and any other
     software that is required to create the operating system image that you want to deploy.

       ２ Warning

       At a minimum, install the appropriate operating system and service pack, support
       drivers, and required software updates.

  3. Configure the reference computer to be a member of a workgroup.

  4. Reset the local Administrator password on the reference computer so that the password
     value is blank.

  5. Run Sysprep by using the command: sysprep /quiet /generalize /reboot. The /generalize
     option instructs Sysprep to remove system-specific data from the Windows installation.

<!-- p.107 -->

     System-specific information includes event logs, unique security IDs (SIDs), and other
     unique information. After the unique system information is removed, the computer
     restarts.

     After the reference computer is ready, use a task sequence to capture the operating
     system image from the reference computer. For detailed steps, see Capture an operating
     system image from an existing reference computer.

Use a task sequence to build a reference computer
You can automate the process to create a reference computer by using a task sequence to
deploy the operating system, drivers, applications, and so on. Use the following steps to build
the reference computer and then to capture the operating system image from the reference
computer.

     Use a task sequence to build and capture the operating system image from the reference
     computer. For detailed steps, see Use a task sequence to build and capture a reference
     computer.

<!-- p.108 -->

Manage OS upgrade packages with
Configuration Manager
07/31/2025

Applies to: Configuration Manager (current branch)

An OS upgrade package in Configuration Manager contains the Windows setup source files to
upgrade an existing OS on a computer. This article describes how to add, distribute, and
service an OS upgrade package.

  ７ Note

  OS upgrade packages can also be used for new installations of Windows. However it's
  dependent on drivers being compatible with this method. When new installations of
  Windows are performed from an OS upgrade package, drivers are installed while still in
  Windows PE versus simply being injected while in Windows PE. Some drivers aren't
  compatible with being installed while in Windows PE. If drivers aren't compatible with
  being installed while in Windows PE, then use an OS image, such as install.wim, instead.

Add an OS upgrade package
Before you can use an OS upgrade package, first add it to your Configuration Manager site.

   1. In the Configuration Manager console, go to the Software Library workspace, expand
     Operating Systems, and then select the Operating System Upgrade Packages node.

   2. On the Home tab of the ribbon, in the Create group, select Add Operating System
     Upgrade Package. This action starts the Add Operating System Upgrade Wizard.

   3. On the Data Source page, specify the following settings:

             The network Path to the installation source files of the OS upgrade package. For
             example, \\server\share\path .

               ７ Note

               The installation source files contain setup.exe and other files and folders to
               install the OS.

<!-- p.109 -->

             ） Important

             Limit access to these installation source files to prevent unwanted tampering.

          Starting in version 2107, review and agree to the license terms for this OS media on
          behalf of your organization.

          Extract a specific image index from install.wim file of selected upgrade package
          and then select an image index from the list. This option automatically imports a
          single index rather than all image indexes in the file. Using this option results in a
          smaller image file, and faster offline servicing. It also supports the process to
          Optimize image servicing, for a smaller image file after applying software updates.

             ） Important

             Configuration Manager overwrites the existing install.wim in the OS upgrade
             package. It extracts the image index to a temporary location, and then moves it
             into the original source directory. Before you import an OS upgrade package
             and enable this option, make sure to backup the original source files.

          If you want to pre-cache content on a client, specify the Architecture and Language
          of the image. For more information, see Configure pre-cache content.

   4. On the General page, specify the following information. This information is useful for
     identification purposes when you have more than one OS upgrade package.

          Name: A unique name for the OS upgrade package.

          Version: An optional version identifier. This property doesn't need to be the OS
          version of the upgrade package. It's often your organization's version for the
          package.

          Comment: An optional brief description.

   5. Complete the wizard.

Next, distribute the OS upgrade package to distribution points.

Distribute content to a distribution point
Distribute OS upgrade packages to distribution points the same as other content. Before you
deploy the task sequence, distribute the OS upgrade package to at least one distribution point.

<!-- p.110 -->

For more information, see Distribute content.

Apply software updates to an image

  ） Important

  Due to changes in how Windows 11 updates are delivered through UUP patches, Offline
  Servicing of Windows 11 images and update packages using Configuration Manager is no
  longer supported. The recommended method to keep Windows 11 deployments up-to-
  date is to acquire the latest patched Windows 11 ISO from Microsoft 365 admin center       .
  Once the updated Windows 11 ISO is obtained:

        Import the install.wim image from the ISO into the site for Operating System
        Images packages used in bare metal/refresh task sequences.
        Import the whole contents of the ISO into the site for Operating System Upgrade
        Packages used in-place upgrade task sequences.

  ７ Note

  This section applies to both Operating System Images and Operating System Upgrade
  Packages. It uses the general term "image" to refer to the Windows image file (WIM). Both
  of these objects have a WIM, which contains Windows installation files. Software updates
  are applicable to these files in both objects. The behavior of this process is the same
  between both objects.

Each month there are new software updates applicable to the image. Before you can apply
software updates to it, you need the following prerequisites:

     A software updates infrastructure
     Successfully synchronized software updates
     Downloaded the software updates to the content library on the site server

For more information, see Deploy software updates.

Apply applicable software updates to an image on a specified schedule. This process is
sometimes called offline servicing. On this schedule, Configuration Manager applies the
selected software updates to the image. It can then also redistribute the updated image to
distribution points.

  ） Important

<!-- p.111 -->

  While you can select any software update that's applicable to the image based on version,
  DISM can only apply certain types of updates to the image. The OfflineServicingMgr.log
  file shows the following entry: Not applying this update binary, it is not supported .

The site database stores information about the image, including the software updates that
were applied at the time of the import. Software updates that you apply to the image since it
was initially added are also stored in the site database. When you start the wizard to apply
software updates, it retrieves the list of applicable software updates that the site hasn't yet
applied to the image. Configuration Manager copies the software updates that you select from
the content library on the site server. It then applies the software updates to the image.

Servicing process
   1. In the Configuration Manager console, go to the Software Library workspace, expand
     Operating Systems, and then select either Operating System Images or Operating
     System Upgrade Packages.

   2. Select the object to which to apply software updates.

   3. On the ribbon, select Schedule Updates to start the wizard.

   4. On the Choose Updates page, select the software updates to apply to the image. It might
     take some time for the list of updates to appear in the wizard. Use the Filter to search for
     strings in the metadata. Use the System architecture drop-down list to filter on X86, X64,
     or All. You can select one, many, or all updates in the list. When you're finished selecting
     updates, select Next.

   5. On the Set Schedule page, specify the following settings, and then select Next.

      a. Schedule: Specify the schedule for when the site applies the software updates to the
        image.

      b. Continue on error: Select this option to continue to apply software updates to the
        image even when there's an error.

      c. Update distribution points with the image: Select this option to update the image on
        distribution points after the site applies the software updates.

   6. Complete the Schedule Updates Wizard.

  ７ Note

<!-- p.112 -->

  To minimize the payload size, the servicing of OS upgrade packages and OS images
  removes the older version.

Servicing operations
In the Configuration Manager console, in either the OS Images or OS Upgrade Packages node,
add the following columns to the view:

     Scheduled Updates Date: This property shows the next defined schedule.
     Scheduled Updates Status: This property shows the status. For example, Successful or In
     Process.

Select a specific image object, and then switch to the Update Status tab in the details pane.
This tab shows the list of updates in the image.

Select a specific image object, and select Properties in the ribbon. The Installed Updates tab
shows the list of updates in the image. The Servicing tab is a read-only view of the current
servicing schedule and the updates that you've scheduled to apply.

When the status is In Process, you can select Cancel Scheduled Updates on the ribbon. This
action cancels the active servicing process.

To troubleshoot this process, view the OfflineServicingMgr.log and dism.log files on the site
server. For more information, see Log files.

Specify the drive for offline OS image servicing
You can specify the drive that Configuration Manager uses during offline servicing of OS
images. This process can consume a large amount of disk space with temporary files. This
option gives you flexibility to select the drive to use.

   1. In the Configuration Manager console, go to the Administration workspace, expand Site
     Configuration, and select the Sites node. In the ribbon, select Configure Site
     Components and then choose Operating System Deployment.

   2. On the Offline Servicing tab, specify the option for A local drive to be used by offline
     servicing of images.

By default, this setting is Automatic. With this value, Configuration Manager selects the drive
on which it's installed.

If you select a drive that doesn't exist on the site server, Configuration Manager behaves the
same as if you select Automatic.

<!-- p.113 -->

During offline servicing, Configuration Manager stores temporary files in the folder,
<drive>:\ConfigMgr_OfflineImageServicing . It also mounts the OS image in this folder.

Optimized image servicing
When you apply software updates to an OS image, you can optimize the output by removing
any superseded updates. The optimization to offline servicing only applies to images with a
single index.

When you schedule the site to apply software updates to an OS image, it uses the Windows
Deployment Image Servicing and Management (DISM) command-line tool. During the
servicing process, this change introduces the following two additional steps:

     It runs DISM against the mounted offline image with the parameters /Cleanup-Image
     /StartComponentCleanup /ResetBase . If this command fails, the current servicing process

     fails. It doesn't commit any changes to the image.

     After Configuration Manager commits changes to the image and unmounts it from the
     file system, it exports the image to another file. This step uses the DISM parameter
      /Export-Image . It removes unneeded files from the image, which reduces the size.

Microsoft recommends that you regularly apply updates to your offline images. You don't have
to use this option every time you service an image. When you do this process each month, this
option provides you the greatest advantage by using it over time. For more information, see
Recommendations for Install Software Updates step.

While this option helps reduce the overall size of the serviced image, it does take longer to
complete the process. Use the wizard to schedule servicing during convenient times. It also
requires additional storage on the site server. You can customize the site to use an alternate
location. For more information, see Specify the drive for offline OS image servicing.

Process to optimize image servicing
   1. Start the servicing process.

   2. On the Set Schedule page, select the option to Remove superseded updates after the
     image is updated. This option isn't automatically enabled. If the image has more than
     one index, you can't use this option.

   3. To schedule image servicing, complete the wizard.

Validate and monitor the process using the OfflineServicing.log.

<!-- p.114 -->

Next steps
Create a task sequence to upgrade an OS

<!-- p.115 -->

Manage drivers in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager provides a driver catalog that you can use to manage the
Windows device drivers in your Configuration Manager environment. Use the driver
catalog to import device drivers into Configuration Manager, to group them in
packages, and to distribute those packages to distribution points. Device drivers can be
used when you install the full OS on the destination computer and when you use
Windows PE in a boot image. Windows device drivers consist of a setup information
(INF) file and any additional files that are required to support the device. When you
deploy an OS, Configuration Manager obtains the hardware and platform information
for the device from its INF file.

Driver categories
When you import device drivers, you can assign the device drivers to a category. Device
driver categories help group similarly used device drivers together in the driver catalog.
For example, set all network adapter device drivers to a specific category. Then, when
you create a task sequence that includes the Auto Apply Drivers step, specify a category
of device drivers. Configuration Manager then scans the hardware and selects the
applicable drivers from that category to stage on the system for Windows Setup to use.

Driver packages
Group similar device drivers in packages to help streamline OS deployments. For
example, create a driver package for each computer manufacturer on your network. You
can create a driver package when importing drivers into the driver catalog directly in the
Driver Packages node. After you create a driver package, distribute it to distribution
points. Then Configuration Manager client computers can install the drivers as required.

Consider the following points:

      When you create a driver package, the source location of the package must point
      to an empty network share that's not used by another driver package. The SMS
      Provider must have Full control permissions to that location.

<!-- p.116 -->

     When you add device drivers to a driver package, Configuration Manager copies it
     to the package source location. You can add to a driver package only device
     drivers that you've imported and that are enabled in the driver catalog.

     You can copy a subset of the device drivers from an existing driver package. First,
     create a new driver package. Then add the subset of device drivers to the new
     package, and then distribute the new package to a distribution point.

     When you use task sequences to install drivers, create driver packages that contain
     less than 500 device drivers.

Create a driver package

  ） Important

  To create a driver package, you must have an empty network folder that's not used
  by another driver package. In most cases, create a new folder before you start this
  procedure.

   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Operating Systems, and then select the Driver Packages node.

   2. On the Home tab of the ribbon, in the Create group, select Create Driver Package.

   3. Specify a descriptive Name for the driver package.

   4. Enter an optional Comment for the driver package. Use this description to provide
     information about the contents or the purpose of the driver package.

   5. In the Path box, specify an empty source folder for the driver package. Each driver
     package must use a unique folder. This path is required as a network location.

       ） Important

       The site server account must have Full control permissions to the specified
       source folder.

The new driver package doesn't contain any drivers. The next step adds drivers to the
package.

If the Driver Packages node contains several packages, you can add folders to the node
to separate the packages into logical groups.

<!-- p.117 -->

Additional actions for driver packages
You can do additional actions to manage driver packages when you select one or more
driver packages from the Driver Packages node.

Create prestage content file

Creates files that you can use to manually import content and its associated metadata.
Use prestaged content when you have low network bandwidth between the site server
and the distribution points where the driver package is stored.

Delete (driver package)

Removes the driver package from the Driver Packages node.

Distribute content

Distributes the driver package to distribution points, distribution point groups, and
distribution point groups that are associated with collections.

Export (driver package)

Start the Export Driver Package Wizard to save associated drivers and content to a file.
Use this process to move driver packages between hierarchies.

Import driver package
Start the Import Driver Package Wizard to create a driver package from a previously
exported package.

   Tip

  Starting in version 2010, when you import an object in the Configuration Manager
  console, it now imports to the current folder. Previously, Configuration Manager
  always put imported objects in the root node.

Manage access accounts

Adds, modifies, or removes access accounts for the driver package.

<!-- p.118 -->

For more information about package access accounts, see Accounts used in
Configuration Manager.

Move (driver package)

Moves the driver package to another folder in the Driver Packages node.

Properties (driver package)

Opens the Properties window. Review and change the content and properties of the
driver. For example, change the name and description of the driver, enable or disable it,
and specify on which platforms it can run.

Driver packages have metadata fields for Manufacturer and Model. Use these fields to
tag driver packages with information to assist in general housekeeping, or to identify
old and duplicate drivers that you can delete. On the General tab, select an existing
value, or enter a string to create a new entry.

In the Driver Packages node, these fields display in the list as the Driver Manufacturer
and Driver Model columns. They can also be used as search criteria.

Starting in version 1906, use these attributes to pre-cache content on a client. For more
information, see Configure pre-cache content.

Show members

View all the drivers in the selected driver package.

Update distribution points

Updates the driver package on all the distribution points where the site stores it. This
action copies only the content that has changed after the last time it was distributed.

Device drivers
You can install drivers on destination computers without including them in the OS image
that is deployed. Configuration Manager provides a driver catalog that contains
references to all the drivers that you import into Configuration Manager. The driver
catalog is located in the Software Library workspace and consists of two nodes: Drivers
and Driver Packages. The Drivers node lists all the drivers that you've imported into the
driver catalog.

<!-- p.119 -->

Import device drivers into the driver catalog
Before you can use a driver when you deploy an OS, import it into the driver catalog. To
better manage them, import only the drivers that you plan to install as part of your OS
deployments. Store multiple versions of drivers in the catalog to provide an easy way to
upgrade existing drivers when hardware device requirements change on your network.

As part of the import process for the device driver, Configuration Manager reads the
following properties about the driver:

     Provider
     Class
     Version
     Signature
     Supported hardware
     Supported platform information

By default, the driver is named after the first hardware device that it supports. You can
rename the device driver later. The supported platforms list is based on the information
in the INF file of the driver. Because the accuracy of this information can vary, manually
verify that the driver is supported after you import it into the catalog.

After you import device drivers into the catalog, add them to driver packages or boot
image packages.

  ） Important

  You can't import device drivers directly into a subfolder of the Drivers node. To
  import a device driver into a subfolder, first import the device driver into the
  Drivers node, and then move the driver to the subfolder.

Process to import Windows device drivers into the driver catalog
   1. In the Configuration Manager console, go to the Software Library workspace.
     Expand Operating Systems, and select the Drivers node.

   2. On the Home tab of the ribbon, in the Create group, select Import Driver to start
     the Import New Driver Wizard.

   3. On the Locate Driver page, specify the following options:

             Import all drivers in the following network path (UNC): To import all the
             device drivers in a specific folder, specify its network path. For example:

<!-- p.120 -->

        \\servername\share\folder .

          ７ Note

          If there are a lot of subfolders and a lot of driver INF files, this process
          can take time.

       Import a specific driver: To import a specific driver from a folder, specify the
       network path to the Windows device driver INF file.

       Specify the option for duplicate drivers: Select how you want Configuration
       Manager to manage driver categories when you import a duplicate device
       driver
          Import the driver and append a new category to the existing categories
          Import the driver and keep the existing categories
          Import the driver and overwrite the existing categories
          Do not import the driver

    ） Important

    When you import drivers, the site server must have Read permission to the
    folder, or the import fails.

4. On the Driver Details page, specify the following options:

       Hide drivers that are not in a storage or network class (for boot images):
       Use this setting to only display storage and network drivers. This option hides
       other drivers that aren't typically needed for boot images, such as a video
       driver or modem driver.

       Hide drivers that are not digitally signed: Microsoft recommends only using
       drivers that are digitally signed

       In the list of drivers, select the drivers that you want to import into the driver
       catalog.

       Enable these drivers and allow computers to install them: Select this setting
       to let computers install the device drivers. This option is enabled by default.

          ） Important
