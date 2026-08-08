---
title: "OS deployment documentation — pages 161-200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-osd-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-osd-p0161-0200
family: sccm
documentKind: "doc"
abstract: "Create a task sequence for non-OS deployments Article • 10/04/2022 Applies to: Configuration Manager (current branch) Task sequences in Configuration Manager are used to automate different kinds of tasks within your environment. These tasks are primarily designed and tested for"
---

# OS deployment documentation — pages 161-200

<!-- p.161 -->

Create a task sequence for non-OS
deployments
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Task sequences in Configuration Manager are used to automate different kinds of tasks
within your environment. These tasks are primarily designed and tested for deploying
operating systems. Configuration Manager has many other features that should be the
primary technology that you use for the following scenarios:

      Application installation

        ７ Note

        Starting in version 2002, install complex applications using task sequences via
        the application model. Add a deployment type to an app that's a task
        sequence, either to install or uninstall the app. For more information, see
        Create Windows applications.

      Starting in version 2010, use the task sequence deployment type of an application
      to deploy a task sequence to a user-based collection.

      Software updates installation

      Setting configuration

Also consider other Microsoft System Center automation technologies, such as
Orchestrator and Service Management Automation.

The power of task sequences lies in their flexibility and how you use them. They can
configure client settings, distribute software, update drivers, edit user states, and do
other tasks independent of OS deployment. You can create a custom task sequence to
add any number of tasks. The use of custom task sequences for non-OS deployment is
supported in Configuration Manager. However, if a task sequence results in unwanted or
inconsistent results, look at ways to simplify the operation:

      Use simpler steps
      Divide the actions across multiple task sequences
      Take a phased approach to creating and testing the task sequence

<!-- p.162 -->

Supported steps
The following steps are supported for use in a non-OS deployment custom task
sequence:

     Check Readiness

     Connect To Network Folder

     Download Package Content

     Install Application

     Install Package

     Install Software Updates

     Restart Computer

     Run Command Line

     Run PowerShell Script

     Run Task Sequence

     Set Dynamic Variables

     Set Task Sequence Variable

Next steps
Create a custom task sequence

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.163 -->

Deploy Windows To Go with
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This topic provides the steps to provision Windows To Go in Configuration Manager.
Windows To Go is an enterprise feature of Windows 8 that enables the creation of a
Windows To Go workspace that can be booted from a USB-connected external drive on
computers that meet the Windows 7 or Windows 8 certification requirements,
regardless of the operating system running on the computer. Windows To Go
workspaces can use the same image enterprises use for their desktops and laptops and
can be managed the same way.

For more information about Windows To Go, see Windows To Go feature overview.

Provision Windows To Go
Windows To Go is an operating system stored on a USB-connected external drive. You
can provision the Windows To Go drive much like you provision other operating system
deployments. However, because Windows To Go is designed to be a user-centric and
highly mobile solution, you must take a slightly different approach to provisioning these
drives.

At a high level, Windows To Go is a two-phased deployment that allows you to
configure the Windows To Go device and prestage content for the operating system
deployment. You can achieve this with minimal impact to the user and limit downtime
for the user's computer. After you prestage the computer, you must complete the
provisioning process to ensure the computer is ready for the user. The provisioning
process is similar to the current operating system deployment process. The following
lists the general workflow to prestage content and provision Windows To Go:

   1. Prerequisites to provision Windows To Go

   2. Create prestaged media

   3. Create a Windows To Go Creator package

   4. Update the task sequence to enable BitLocker for Windows To Go

   5. Deploy the Windows To Go Creator package and task sequence

<!-- p.164 -->

  6. User runs the Windows To Go Creator

  7. Configuration Manager configures and stages the Windows To Go drive

  8. User logs in to Windows 8

Prerequisites to provision Windows To Go
Before you provision Windows To Go, you must complete the following in Configuration
Manager:

     Distribute a boot image to a distribution point

     Before you create prestaged media, you must distribute the boot image to a
     distribution point.

       ７ Note

       Boot images are used to install the operating system on the destination
       computers in your Configuration Manager environment. They contain a
       version of Windows PE that installs the operating system, as well as any
       additional device drivers that are required. Configuration Manager provides
       two boot images: One to support x86 platforms and one to support x64
       platforms. You can also create your own boot images. For more information,
       see Manage boot images.

     Distribute the Windows 8 operating system image to a distribution point

     Before you create prestaged media, you must distribute the Windows 8 operating
     system image to a distribution point.

       ７ Note

       Operating system images are .WIM format files and represent a compressed
       collection of reference files and folders that are required to successfully install
       and configure an operating system on a computer. For more information, see
       Manage operating system images.

     Create a Task Sequence to Deploy Windows 8

     You must create a task sequence for a Windows 8 deployment that you will
     reference when you create prestaged media. For more information, see Manage

<!-- p.165 -->

     task sequences to automate tasks.

Create prestaged media
Prestaged media contains the boot image used to start the destination computer and
the operating system image that is applied to the destination computer. The computer
that you provision with prestaged media can be started by using the boot image. The
computer can then run an existing operating system deployment task sequence to
install a complete operating system deployment. The task sequence that deploys the
operating system is not included in the media.

You can add content, such as applications and device drivers, in addition to the
operating system image and boot image during the prestage phase. This reduces the
time it takes to deploy an operating system and reduces network traffic because the
content is already on the drive.

Use the following procedure to create the prestaged media.

To create prestaged media

   1. In the Configuration Manager console, click Software Library.

   2. In the Software Library workspace, expand Operating Systems, and then click Task
     Sequences.

   3. On the Home tab, in the Create group, click Create Task Sequence Media to start
     the Create Task Sequence Media Wizard.

   4. On the Select Media Type page, specify the following information, and then click
     Next.

           Select Prestaged media.

           Select Allow unattended operating system deployment to boot to the
           Windows To Go deployment with no user interaction.

             ） Important

             When you use this option with the SMSTSPreferredAdvertID custom
             variable (set later in this procedure), no user interaction is required and
             the computer will automatically boot to the Windows To Go deployment
             when it detects a Windows To Go drive. The user is still prompted for a
             password if the media is configured for password protection. If you use

<!-- p.166 -->

          the Allow unattended operating system deployment setting without
          configuring the SMSTSPreferredAdvertID variable, an error will occur
          when you deploy the task sequence.

5. On the Media Management page, specify the following information, and then click
  Next.

       Select Dynamic media if you want to allow a management point to redirect
       the media to another management point, based on the client location in the
       site boundaries.

       Select Site-based media if you want the media to contact only the specified
       management point.

6. On the Media Properties page, specify the following information, and then click
  Next.

       Created by: Specify who created the media.

       Version: Specify the version number of the media.

       Comment: Specify a unique description of what the media is used for.

       Media file: Specify the name and path of the output files. The wizard writes
       the output files to this location. For example:
       \\servername\folder\outputfile.wim

7. On the Security page, specify the following information, and then click Next.

       Select Enable unknown computer support to allow the media to deploy an
       operating system to a computer that is not managed by Configuration
       Manager. There is no record of these computers in the Configuration
       Manager database. Unknown computers include the following:

          A computer where the Configuration Manager client is not installed

          A computer that is not imported into Configuration Manager

          A computer that is not discovered by Configuration Manager

       Select Protect the media with a password and enter a strong password to
       help protect the media from unauthorized access. When you specify a
       password, the user must provide that password to use the prestaged media.

          ） Important

<!-- p.167 -->

  As a security best practice, always assign a password to help protect the
  prestaged media.

  ７ Note

  When you protect the prestaged media with a password, the user is
  prompted for the password even when the media is configured with the
  Allow unattended operating system deployment setting.

For HTTP communications, select Create self-signed media certificate, and
then specify the start and expiration date for the certificate.

For HTTPS communications, select Import PKI certificate, and then specify
the certificate to import and its password.

For more information about this client certificate that is used for boot images,
see PKI certificate requirements.

User Device Affinity: To support user-centric management in Configuration
Manager, specify how you want the media to associate users with the
destination computer. For more information about how operating system
deployment supports user device affinity, see Associate users with a
destination computer.

   Specify Allow user device affinity with auto-approval if you want the
   media to automatically associate users with the destination computer. This
   functionality is based on the actions of the task sequence that deploys the
   operating system. In this scenario, the task sequence creates a relationship
   between the specified users and destination computer when it deploys the
   operating system to the destination computer.

   Specify Allow user device affinity pending administrator approval if you
   want the media to associate users with the destination computer after
   approval is granted. This functionality is based on the scope of the task
   sequence that deploys the operating system. In this scenario, the task
   sequence creates a relationship between the specified users and the
   destination computer, but waits for approval from an administrative user
   before the operating system is deployed.

   Specify Do not allow user device affinity if you do not want the media to
   associate users with the destination computer. In this scenario, the task

<!-- p.168 -->

           sequence does not associate users with the destination computer when it
           deploys the operating system.

 8. On the Task Sequence page, specify the Windows 8 task sequence that you
   created in the previous section.

 9. On the Boot image page, specify the following information, and then click Next.

     ） Important

     The architecture of the boot image that is distributed must be appropriate for
     the architecture of the destination computer. For example, an x64 destination
     computer can boot and run an x86 or x64 boot image. However, an x86
     destination computer can boot and run only an x86 boot image. For Windows
     8 certified computers in EFI mode, you must use an x64 boot image.

        Boot image: Specify the boot image to start the destination computer.

        Distribution point: Specify the distribution point that hosts the boot image.
        The wizard retrieves the boot image from the distribution point and writes it
        to the media.

           ７ Note

           The administrative user must have Read access rights to the boot image
           content on the distribution point. For more information, see Package
           access account.

        If you selected Site-based media on the Media Management page of this
        wizard, in the Management point box, specify a management point from a
        primary site.

        If you selected Dynamic media on the Media Management page of the
        wizard, in the Associated management points box, specify the primary site
        management points to use and a priority order for the initial
        communications.

10. On the Images page, specify the following information, and then click Next.

        Image package: Specify the package that contains the Windows 8 operating
        system image.

<!-- p.169 -->

         Image index: Specify the image to deploy if the package contains multiple
         operating system images.

         Distribution point: Specify the distribution point that hosts the operating
         system image package. The wizard retrieves the operating system image from
         the distribution point and writes it to the media.

           ７ Note

           The administrative user must have Read access rights to the operating
           system image content on the distribution point. For more information,
           see Package access account.

11. On the Select Application page, select application content to include in the media
   file, and then click Next.

12. On the Select Package page, select additional package content to include in the
   media file, and then click Next.

13. On the Select Driver Package page, select driver package content to include in the
   media file, and then click Next.

14. On the Distribution Points page, select one or more distribution points that
   contain the content required by the task sequence, and then click Next.

15. On the Customization page, specify the following information, and then click Next.

         Variables: Specify the variables that the task sequence uses to deploy the
         operating system. For Windows To Go, use the SMSTSPreferredAdvertID
         variable to automatically select the Windows To Go deployment by using the
         following format:

         SMSTSPreferredAdvertID = {DeploymentID}, where DeploymentID is the
         deployment ID associated with the task sequence that you will use to
         complete the provisioning process for the Windows To Go drive.

            Tip

           When you use this variable with a task sequence that is set to run
           unattended (set earlier in this procedure), no user interaction is required
           and the computer automatically boots to the Windows To Go
           deployment when it detects a Windows To Go drive. The user is still

<!-- p.170 -->

           prompted for a password if the media is configured for password
           protection.

        Prestart commands: Specify any prestart commands that you want to run
        before the task sequence runs. Prestart commands can be a script or
        executable that can interact with the user in Windows PE before the task
        sequence runs to install the operating system. Configure the following for the
        Windows To Go deployment:

           OSDBitLockerPIN: BitLocker for Windows To Go requires a passphrase. Set
           the OSDBitLockerPIN variable as part of a prestart command to set the
           BitLocker passphrase for the Windows To Go drive.

             ２ Warning

             After BitLocker is enabled for the passphrase, the user must enter the
             passphrase each time the computer boots to the Windows To Go
             drive.

           SMSTSUDAUsers: Specifies the primary user of the destination computer.
           Use this variable to collect the user name, which can then be used to
           associate the user and device. For more information, see Associate users
           with a destination computer.

              Tip

             To retrieve the username, you can create an input box as part of the
             prestart command, have the user enter their username, and then set
             the variable with the value. For example, you can add the following
             lines to the prestart command script file:

              UserID = inputbox("Enter Username" ,"Enter your

             username:","",400,0)

              env("SMSTSUDAUsers") = UserID

           For more information about how to create a script file to use as your
           prestart command, see Prestart commands for task sequence media.

16. Complete the wizard.

<!-- p.171 -->

       ７ Note

       It can take an extended period of time for the wizard to complete the
       prestaged media file.

Create a Windows To Go Creator package
As part of the Windows To Go deployment, you must create a package to deploy the
prestage media file. The package must include the tool that configures the Windows To
Go drive and extracts the prestaged media to the drive. Use the following procedure to
create the Windows To Go Creator package.

To create the Windows To Go Creator package

   1. On the server to host the Windows To Go Creator package files, create a source
     folder for the package source files.

       ７ Note

       The computer account of the site server must have Read access rights to the
       source folder.

   2. Copy the prestaged media file that you created in the Create prestaged media
     section to the package source folder.

   3. Copy the Windows To Go Creator tool (WTGCreator.exe) to the package source
     folder. The creator tool is available on any primary site server at the following
     location: <ConfigMgrInstallationFolder>\OSD\Tools\WTG\Creator.

   4. Create a package and program by using the Create Package and Program Wizard.

   5. In the Configuration Manager console, click Software Library.

   6. In the Software Library workspace, expand Application Management, and then
     click Packages.

   7. On the Home tab, in the Create group, click Create Package.

   8. On the Package page, specify the name and description of the package. For
     example, enter Windows To Go for the package name and specify Package to

<!-- p.172 -->

   configure a Windows To Go drive using Configuration Manager for the package
   description.

 9. Select This package contains source files, specify the path to the package source
   folder that you created in step 1, and then click Next.

10. On the Program Type page, select Standard program, and then click Next.

11. On the Standard Program page, specify the following:

        Name: Specify the name of the program. For example, type Creator for the
        program name.

        Command Line: Type WTGCreator.exe /wim:PrestageName.wim, where
        PrestageName is the name of prestaged file that you created and copied to
        the package source folder for the Windows To Go Creator package.

        Optionally, you can add the following options:
           enableBootRedirect: command-line option to change the Windows To Go
           startup options to allow boot redirection. When you use this option, the
           computer will boot from USB without having to change the boot order in
           the computer firmware or have the user select from a list of boot options
           during startup. If a Windows To Go drive is detected, the computer boots
           to that drive.

        Run: Specify Normal to run the program based on the system and program
        defaults.

        Program can run: Specify whether the program can run only when a user is
        logged on.

        Run mode: Specify whether the program will run with the logged on users
        permissions or with administrative permissions. The Windows To Go Creator
        requires elevated permissions to run.

        Select Allow users to view and interact with the program installation, and
        then click Next.

12. On the Requirements page, specify the following:

        Platform requirements: Select the applicable Windows 8 platforms to allow
        provisioning.

        Estimated disk space: Specify the size of the package source folder for the
        Windows To Go Creator.

<!-- p.173 -->

           Maximum allowed run time (minutes): Specifies the maximum time that the
           program is expected to run on the client computer. By default, this value is
           set to 120 minutes.

             ） Important

             If you are using maintenance windows for the collection on which this
             program is run, a conflict might occur if the Maximum allowed run time
             is longer than the scheduled maintenance window. If the maximum run
             time is set to Unknown, it will start during the maintenance window, but
             will continue to run until it completes or fails after the maintenance
             window is closed. If you set the maximum run time to a specific period
             (not set to Unknown) that exceeds the length of any available
             maintenance window, then that program will not be run.

             ７ Note

             If the value is set to Unknown, Configuration Manager sets the
             maximum allowed run time to 12 hours (720 minutes).

             ７ Note

             If the maximum run time (whether set by the user or as the default
             value) is exceeded, Configuration Manager stops the program if run with
             administrative rights is selected and Allow users to view and interact
             with the program installation is not selected on the Standard Program
             page.

           Click Next and complete the wizard.

Update the task sequence to enable BitLocker for
Windows To Go
Windows To Go enables BitLocker on an external bootable drive without the use of TPM.
Therefore, you must use a separate tool to configure BitLocker on the Windows To Go
drive. To enable BitLocker, you must add an action to the task sequence after the Setup
Windows and ConfigMgr step.

  ７ Note

<!-- p.174 -->

  BitLocker for Windows To Go requires a passphrase. In the Create prestaged media
  step, you set the passphrase as part of a prestart command by using the
  OSDBitLockerPIN variable.

Use the following procedure to update the Windows 8 task sequence to enable
BitLocker for Windows To Go.

To update the Windows 8 task sequence to enable BitLocker
  1. In the Configuration Manager console, click Software Library.

  2. In the Software Library workspace, expand Application Management, and then
     click Packages.

  3. On the Home tab, in the Create group, click Create Package.

  4. On the Package page, specify the name and description of the package. For
     example, type BitLocker for Windows To Go for the package name and specify
     Package to update BitLocker for Windows To Go for the package description.

  5. Select This package contains source files, specify the location for the BitLocker
     tool for Windows To Go, and then click Next. The BitLocker tool is available on any
     Configuration Manager primary site server at the following location:
     <ConfigMgrInstallationFolder>\OSD\Tools\WTG\BitLocker\

  6. On the Program Type page, select Do not create a program.

  7. Click Next and complete the wizard.

  8. In the Configuration Manager console, click Software Library.

  9. In the Software Library workspace, expand Operating Systems, and then click Task
     Sequences.

 10. Select the Windows 8 task sequence that you reference in the prestaged media.

 11. On the Home tab, in the Task Sequence group, click Edit.

 12. Click the Setup Windows and ConfigMgr step, click Add, click General, and then
     click Run Command Line. The Run Command Line step is added after the Setup
     Windows and ConfigMgr step.

 13. On the Properties tab for the Run Command Line step, add the following:

<!-- p.175 -->

a. Name: Specify a name for the command line, such as Enable BitLocker for
  Windows To Go.

b. Command Line: i386\osdbitlocker_wtg.exe /Enable /pwd:< None|AD>

  Parameters:

       /pwd:<None|AD> - Specify the BitLocker password recovery mode. This
       parameter is required you use the /Enable parameter is in the command-
       line.

       Select AD to configure BitLocker Drive Encryption to back up recovery
       information for BitLocker-protected drives to Active Directory Domain
       Services (AD DS). Backing up recovery passwords for a BitLocker-protected
       drive allows administrative users to recover the drive if it is locked. This
       ensures that encrypted data belonging to the enterprise can always be
       accessed by authorized users. When you specify None, the user is
       responsible for keeping a copy of the recovery password or recovery key. If
       the user loses that information or neglects to decrypt the drive before
       leaving the organization, administrative users cannot easily access to the
       drive.

       /wait:<TRUE|FALSE> - Specify whether the task sequence waits for
       encryption to complete before it completes.

c. Select Package, and then specify the package that you created at the start of
  this procedure.

d. On the Options tab, add the following conditions:

       Condition = Task Sequence Variable

       Variable = _SMSTSWTG

       Condition = Equals

       Value = True

  ７ Note

  The Enable BitLocker step, which is likely after the new command-line step, is
  not used to enable BitLocker for Windows To Go. However, you can keep this
  step in the task sequence to use for Windows 8 deployments that do not use
  a Windows To Go drive.

<!-- p.176 -->

Deploy the Windows To Go Creator package and task
sequence
Windows To Go is a hybrid deployment process. Therefore, you must deploy the
Windows To Go Creator package and the Windows 8 task sequence. Use the following
procedures to complete the deployment process.

To deploy the Windows To Go Creator package
  1. In the Configuration Manager console, click Software Library.

  2. In the Software Library workspace, expand Application Management, and then
     click Packages.

  3. Select the Windows To Go package that you created in the Create a Windows To
     Go Creator package step.

  4. On the Home tab, in the Deployment group, click Deploy.

  5. On the General page, specify the following settings:

     a. Software: Verify that the Windows To Go package is selected.

     b. Collection: Click Browse to select the collection to which you want to deploy
       the Windows To Go package.

     c. Use default distribution point groups associated to this collection: Select this
       option if you want to store the package content on the collections default
       distribution point group. If you have not associated the selected collection with
       a distribution point group, this option will be unavailable.

  6. On the Content page, click Add and then select the distribution points or
     distribution point groups to which you want to deploy the content associated with
     this package and program.

  7. On the Deployment Settings page, select Available for the deployment type, and
     then click Next.

  8. On the Scheduling, configure when this package and program will be deployed or
     made available to client devices.

     The options on this page will differ depending on whether the deployment action
     is set to Available or Required.

  9. On the Scheduling, configure the following settings, and then click Next.

<!-- p.177 -->

    a. Schedule when this deployment will become available: Specify the date and
      time when the package and program is available to run on the destination
      computer. When you select UTC, this setting ensures that the package and
      program is available for multiple destination computers at the same time rather
      than at different times, according to the local time on the destination
      computers.

   b. Schedule when this deployment will expire: Specify the date and time when
      the package and program expires on the destination computer. When you
      select UTC, this setting ensures that the task sequence expires on multiple
      destination computers at the same time rather than at different times, according
      to the local time on the destination computers.

10. On the User Experience page of the Wizard, specify the following information:

         Software installation: Allows the software to be installed outside of any
         configured maintenance windows.

         System restart (if required to complete the installation): Allows a device to
         restart outside of configured maintenance windows when required by the
         software installation.

         Embedded Devices: When you deploy packages and programs to Windows
         Embedded devices that are write filter enabled, you can specify to install the
         packages and programs on the temporary overlay and commit changes later,
         or commit the changes at the installation deadline or during a maintenance
         window. When you commit changes at the installation deadline or during a
         maintenance window, a restart is required and the changes persist on the
         device.

11. On the Distribution Points page, specify the following information:

         Deployment options: Specify Download content from distribution point
         and run locally.

         Allow clients to share content with other clients on the same subnet: Select
         this option to reduce load on the network by allowing clients to download
         content from other clients on the network that have already downloaded and
         cached the content. This option utilizes Windows BranchCache and can be
         used on computers running Windows Vista SP2 and later.

         All clients to use a fallback source location for content: Specify whether to
         allow clients to fall back and use a non-preferred distribution point as the

<!-- p.178 -->

         source location for content when the content is not available on a preferred
         distribution point.

 12. Complete the wizard.

To deploy the Windows 8 task sequence
  1. In the Configuration Manager console, click Software Library.

  2. In the Software Library workspace, expand Operating Systems, and then click Task
    Sequences.

  3. Select the Windows 8 task sequence that you created in the Prerequisites to
    provision Windows To Go step.

  4. On the Home tab, in the Deployment group, click Deploy.

  5. On the General page, specify the following settings:

     a. Task sequence: Verify that the Windows 8 task sequence is selected.

    b. Collection: Click Browse to select the collection that includes all devices for
       which a user might provision Windows To Go.

         ） Important

         If the prestaged media that you created in the Create prestaged media
         section uses the SMSTSPreferredAdvertID variable, you can deploy the task
         sequence to the All Systems collection and specify the Windows PE only
         (hidden) setting on the Content page. Because the task sequence is
         hidden, it will only be available to media.

     c. Use default distribution point groups associated to this collection: Select this
       option if you want to store the package content on the collections default
       distribution point group. If you have not associated the selected collection with
       a distribution point group, this option will be unavailable.

  6. On the Deployment Settings page, configured the following settings, and then
    click Next.

         Purpose: Select Available. When you deploy the task sequence to a user, the
         user sees the published task sequence in the Application Catalog and can
         request it on demand. If you deploy the task sequence to a device, the user
         will see the task sequence in Software Center and can install it on demand.

<!-- p.179 -->

       Make available to the following: Specify whether the task sequence is
       available to Configuration Manager clients, media, or PXE.

          ） Important

          Use the Only media and PXE (hidden) setting for automated task
          sequence deployments. Select Allow unattended operating system
          deployment and set the SMSTSPreferredAdvertID variable as part of the
          prestaged media to have the computer automatically boot to the
          Windows To Go deployment with no user interaction when it detects a
          Windows To Go drive. For more information about these prestaged
          media settings, see the Create prestaged media section.

7. On the Scheduling page, configure the following settings, and then click Next.

  a. Schedule when this deployment will become available: Specify the date and
     time when the task sequence is available to run on the destination computer.
     When you select UTC, this setting ensures that the task sequence is available for
     multiple destination computers at the same time rather than at different times,
     according to the local time on the destination computers.

  b. Schedule when this deployment will expire: Specify the date and time when
     the task sequence expires on the destination computer. When you select UTC,
     this setting ensures that the task sequence expires on multiple destination
     computers at the same time rather than at different times, according to the
     local time on the destination computers.

8. On the User Experience page, specify the following information:

       Show Task Sequence progress: Specify whether the Configuration Manager
       client displays the progress of the task sequence.

       Software installation: Specify whether the user is allowed to install software
       outside a configured maintenance windows after the scheduled time.

       System restart (if required to complete the installation): Allows a device to
       restart outside of configured maintenance windows when required by the
       software installation.

       Embedded Devices: When you deploy packages and programs to Windows
       Embedded devices that are write filter enabled, you can specify to install the
       packages and programs on the temporary overlay and commit changes later,
       or commit the changes at the installation deadline or during a maintenance

<!-- p.180 -->

           window. When you commit changes at the installation deadline or during a
           maintenance window, a restart is required and the changes persist on the
           device.

           Internet-based clients: Specify whether the task sequence is allowed to run
           on an Internet-based client. Operations that install software, such as an
           operating system, are not supported with this setting. Use this option only for
           generic script-based task sequences that perform operations in the standard
           operating system.

   9. On the Alerts page, specify the alert settings that you want for this task sequence
     deployment, and then click Next.

 10. On the Distribution Points page, specify the following information, and then click
     Next.

           Deployment options: Select Download content locally when needed by
           running task sequence.

           When no local distribution point is available, use a remote distribution
           point: Specify whether clients can use distribution points that are on slow and
           unreliable networks to download the content that is required by the task
           sequence.

           Allow clients to use a fallback source location for content:
              Prior to version 1610, you can select the Allow fallback source location for
              content check box to allow clients outside these boundary groups to fall
              back and use the distribution point as a source location for content when
              no other distribution points are available.
              Beginning with version 1610, you no longer can configure Allow fallback
              source location for content. Instead, you configure relationships between
              boundary groups that determine when a client can begin to search
              additional boundary groups for a valid content source location.

 11. Complete the wizard.

User runs the Windows To Go Creator
After you deploy the Windows To Go package and Windows 8 task sequence, the
Windows To Go Creator is available to the user. The user can go to the software catalog,
or Software Center if the Windows To Go Creator was deployed to devices, and run the
Windows To Go Creator program. Once the creator package is downloaded, a flashing
icon is displayed on the task bar. When the user clicks the icon, a dialog box is displayed

<!-- p.181 -->

for the user to select the Windows To Go drive to provision (unless the /drive command-
line option is used). If the drive does not meet the requirements for Windows To Go or if
the drive does not have enough free disk space to install the image, the creator program
displays an error message. The user can verify the drive and image that will be applied
from the confirmation page. As the creator configures and prestages content to the
Windows To Go drive, it displays a progress dialog box. After the prestaging is complete,
the creator displays a prompt to restart the computer to boot to the Windows To Go
drive.

  ７ Note

  If you did not enable boot redirection as part of the command line for the creator
  program in the Create a Windows To Go Creator package section, the user might
  be required to manually boot to the Windows To Go drive on every system restart.

Configuration Manager configures and stages the
Windows To Go drive
After the computer restarts to the Windows To Go drive, the drive will boot into
Windows PE and connect to the management point to get the policy to complete the
operating system deployment. Configuration Manager configures and stages the drive.
After Configuration Manager stages the drive, the user can restart the computer to
finalize the provisioning process (such as to join a domain or install apps). This process
is the same for any prestaged media.

User logs in to Windows 8
After Configuration Manager completes the provisioning process and the Windows 8
lock screen is displayed, the user can login to the operating system.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.182 -->

Create a task sequence to install an OS
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use task sequences in Configuration Manager to automatically install an OS image on a
destination computer. You create a task sequence that references a boot image used to
start the destination computer, the OS image that you want to install on the destination
computer, and any other additional content, such as other applications or software
updates, that you want to install. Then you deploy the task sequence to a collection that
contains the destination computer.

Create a task sequence to install an OS
There are multiple scenarios to deploy an OS to computers in your environment. In most
cases, create a task sequence and select Install an existing image package in the Create
Task Sequence Wizard. This option creates a task sequence that installs the OS, migrates
user settings, applies software updates, and installs applications.

Prerequisites
Before you create a task sequence to install an OS, the following requirements must be
in place:

Required
      A boot image

      An OS image

Required (if used)
      Synchronize software updates

      Add applications

Process to create a task sequence that installs an OS
   1. In the Configuration Manager console, go to the Software Library workspace,
      expand Operating Systems, and select the Task Sequences node.

<!-- p.183 -->

2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence.
  This action starts the Create Task Sequence Wizard.

3. On the Create a New Task Sequence page, select Install an existing Image
  package, and then select Next.

4. On the Task Sequence Information page, specify the following settings:

       Task sequence name: Specify a name that identifies the task sequence.

       Description: Specify a description of what the task sequence does.

       Boot image: Specify the boot image that the task sequence uses to install the
       OS on the destination computer. The boot image contains a version of
       Windows PE, plus any additional required device drivers. For more
       information, see Manage boot images.

          ） Important

          The architecture of the boot image must be compatible with the
          hardware architecture of the destination computer.

5. On the Install Windows page, specify the following settings:

       Image package: Specify the package that contains the OS image to install.
       For more information, see Manage OS images.

       Image: If the OS image package has multiple images, specify the index of the
       OS image to install.

       Partition and format the target computer installing the operating system:
       Specify whether you want the task sequence to partition and format the
       destination computer before it installs the OS.

       Product key: Specify the Windows product key, if necessary. You can specify
       encoded volume license keys and standard product keys. If you use a non-
       encoded product key, each group of five characters must be separated by a
       dash ( - ). For example: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX

       Server licensing mode: Specify that the server license is Per seat, Per server,
       or that no license is specified. If the server license is Per server, also specify
       the maximum number of server connections.

       Specify how to handle the administrator account for the new OS:

<!-- p.184 -->

          Randomly generate the local administrator account password and
          disable the account on all supported platform (recommended): Windows
          disables the local administrator account after the task sequence deploys
          the OS image.

          Enable the account and specify the local administrator password:
          Windows uses the same password for the local administrator account on
          all computers where the task sequence deploys the OS image.

6. On the Configure Network page, specify the following settings:

       Join a workgroup: Add the destination computer to a workgroup.

       Join a domain: Add the destination computer to a domain. In Domain,
       specify the name of the domain.

          ） Important

          You can browse to locate domains in the local forest, but you must
          specify the domain name for a remote forest.

       You can also specify an organizational unit (OU) in the Domain OU field. This
       setting is optional, and specifies the LDAP X.500-distinguished name of the
       OU. If it doesn't already exist, Windows creates the computer account in this
       OU.

       Account: The user name and password for the account that has permissions
       to join the specified domain. For example: domain\user or %variable%.

          ） Important

          If you plan to migrate either the domain settings or the workgroup
          settings, enter the appropriate domain credentials.

7. On the Install Configuration Manager page, specify the Configuration Manager
  client package to install on the destination computer. You can also include any
  installation properties.

8. On the State Migration page, specify the following information:

       Capture user settings: The task sequence captures the user state. For more
       information about how to capture and restore the user state, see Manage
       user state.

<!-- p.185 -->

           Capture network settings: The task sequence captures network settings from
           the destination computer. It captures the membership of the domain or
           workgroup, also the network adapter settings.

           Capture Microsoft Windows settings: The task sequence captures Windows
           settings from the destination computer before it installs the OS image. It
           captures the computer name, registered user and organization name, and the
           time zone settings.

   9. On the Include Updates page, specify whether to install required software updates,
     all software updates, or no software updates. If you specify to install software
     updates, Configuration Manager installs only those software updates that are
     targeted to the collections that the destination computer is a member of.

 10. On the Install Applications page, specify the applications to install on the
     destination computer. If you specify multiple applications, you can also specify that
     the task sequence continues if the installation of a specific application fails.

 11. Complete the wizard.

You can now deploy the task sequence to a collection of computers. For more
information, see Deploy a task sequence.

Pre-cache content
Starting in version 1906, you can enable this type of task sequence to pre-cache content.
The pre-cache feature for available deployments of task sequences lets clients download
relevant content before a user installs the task sequence.

For more information, see Configure pre-cache content.

Example task sequence
Use the following table as a guide as you create a task sequence that deploys an OS
using an existing image. The table helps you decide the general sequence for your task
sequence steps and how to organize and structure those task sequence steps into
logical groups. The task sequence that you create may vary from this sample and can
contain more or less task sequence steps and groups.

  ７ Note

  Use the Create Task Sequence Wizard to create this task sequence.

<!-- p.186 -->

 When you use the Create Task Sequence Wizard to create this new task sequence,
 some of the step names are different than what they would be if you manually
 added these task sequence steps to an existing task sequence.

                                                                                   ﾉ   Expand table

Task sequence        Description
group or step

Capture File and     Create a task sequence group. A task sequence group keeps similar task
Settings - (New      sequence steps together for better organization and error control.
task sequence
group)               This group contains the steps needed to capture files and settings from the
                     operating system of a reference computer.

Capture Windows      Use this task sequence step to identify the Microsoft Windows settings to
Settings             capture from the reference computer. You can capture the computer name,
                     user and organizational information, and the time zone settings.

Capture Network      Use this task sequence step to capture network settings from the reference
Settings             computer. You can capture the domain or workgroup membership of the
                     reference computer and the network adapter setting information.

Capture User Files   Create a task sequence group within a task sequence group. This subgroup
and Settings -       contains the steps needed to capture user state data. Similar to the initial
(New task            group that you added, this subgroup keeps similar task sequence steps
sequence             together for better organization and error control.
subgroup)

Request User         Use this task sequence step to request access to a state migration point
State Storage        where the user state data is stored. You can configure this task sequence step
                     to capture or restore the user state information.

Capture User Files   Use this task sequence step to use the User State Migration Tool (USMT) to
and Settings         capture the user state and settings from the reference computer that will
                     receive the task sequence associated with this task step. You can capture the
                     standard options or configure which options to capture.

Release User State   Use this task sequence step to notify the state migration point that the
Storage              capture or restore action is complete.

Install Operating    Create another task sequence subgroup. This subgroup contains the steps
System - (New        needed to install and configure the Windows PE environment.
task sequence
group)

Restart in           Use this task sequence step to specify the restart options for the destination
Windows PE           computer that receives this task sequence. This step will display a message to
                     the user indicating that the computer will be restarted so that the installation

<!-- p.187 -->

Task sequence      Description
group or step

                   can continue.

                   This step uses the read-only _SMSTSInWinPE task sequence variable. If the
                   associated value equals false the task sequence step continues.

Partition Disk 0   This task sequence step specifies the actions necessary to format the hard
                   drive on the destination computer. The default disk number is 0.

                   This step uses the read-only _SMSTSClientCache task sequence variable. This
                   step runs if the Configuration Manager client cache doesn't exist.

Apply Operating    Use this task sequence step to install the operating system image onto the
System             destination computer. This step first deletes all files on the volume, except
                   for any Configuration Manager-specific control files. It then applies all
                   volume images contained in the WIM file to the corresponding sequential
                   disk volume on the target computer. You can specify a sysprep answer file
                   and also configure which disk partition is used for the installation.

Apply Windows      Use this task sequence step to configure the Windows settings configuration
Settings           information for the destination computer. The windows settings you can
                   apply are user and organizational information, product or license key
                   information, time zone, and the local administrator password.

Apply Network      Use this task sequence step to specify the network or workgroup
Settings           configuration information for the destination computer. You can also specify
                   if the computer uses a DHCP server or you can statically assign the IP address
                   information.

Apply Device       Use this task sequence step to install drivers as part of the operating system
Drivers            deployment. You can allow Windows Setup to search all existing driver
                   categories by selecting Consider drivers from all categories or limit which
                   driver categories Windows Setup searches by selecting Limit driver matching
                   to only consider drivers in selected categories.

                   This step uses the read-only _SMSTSMediaType task sequence variable. This
                   task sequence step runs only if the value of the variable doesn't equal
                   FullMedia.

Apply Driver       Use this task sequence step to make all device drivers in a driver package
Package            available for use by Windows setup.

Setup Operating    Create another task sequence subgroup. This subgroup contains the steps
System - (New      needed to set up the installed operating system.
task sequence
group)

Setup Windows      Use this task sequence step to install the Configuration Manager client
and ConfigMgr      software. Configuration Manager installs and registers the Configuration

<!-- p.188 -->

 Task sequence        Description
 group or step

                      Manager client GUID. You can assign the necessary installation parameters in
                      the Installation properties window.

 Install Updates      Use this task sequence step to specify how software updates are installed on
                      the destination computer. The destination computer isn't evaluated for
                      applicable software updates until this task sequence step runs. At that point,
                      the destination computer is evaluated for software updates similar to any
                      other Configuration Manager-managed client.

                      This step uses the read-only _SMSTSMediaType task sequence variable. This
                      task sequence step runs only if the value of the variable doesn't equal
                      FullMedia.

 Restore User Files   Create another task sequence subgroup. This subgroup contains the steps
 and Settings -       needed to restore the user files and settings.
 (New task
 sequence
 subgroup)

 Request User         Use this task sequence step to request access to a state migration point
 State Storage        where the user state data is stored.

 Restore User Files   Use this task sequence step to run the User State Migration Tool (USMT) to
 and Settings         restore user state and settings to a destination computer.

 Release User State   Use this task sequence step to notify the state migration point that the user
 Storage              state data is no longer needed.

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.189 -->

Create a task sequence to upgrade an
OS in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use task sequences in Configuration Manager to automatically upgrade an OS on a
destination computer. This upgrade can be from Windows 7 or later to Windows 10 or
later, or from Windows Server 2012 or later to Windows Server 2016 or later. Create a
task sequence that references an OS upgrade package or feature update and any other
content to install, such as applications or software updates. The task sequence to
upgrade an OS is part of the Upgrade Windows to the latest version scenario.

Starting in version 2103, you can upgrade by using a feature update deployed with the
task sequence. This integration combines the simplicity of Windows servicing with the
flexibility of task sequences. Servicing uses content that you synchronize through the
software update point. This process simplifies the need to manually get, import, and
maintain the Windows image content used with a standard task sequence to upgrade
Windows. The size of the servicing ESD file is generally smaller than the OS upgrade
package and WIM image file.

Prerequisites
Before you create the task sequence, make sure the following requirements are in place:

Required
      An OS upgrade package is available in the Configuration Manager console.

      Starting in version 2103, you can also use a feature update. In this case, the OS
      upgrade package isn't required. For more information, see Requirements for a
      feature update in a task sequence.

      When upgrading to Windows Server 2016 or later, select the Ignore any
      dismissable compatibility messages setting in the Upgrade Operating System task
      sequence step. Otherwise the upgrade fails.

Required (if used)
      Synchronize software updates in the Configuration Manager console.

<!-- p.190 -->

   Add applications to the Configuration Manager console.

Requirements for a feature update in a task sequence
   Synchronize the software update point to include the Upgrades classification. For
   more information, see Configure classifications and products.

   For a deployment package that contains the feature update, distribute it to a
   distribution point that the client can access. For more information, see Download
   software updates.

     ７ Note

     If the feature update isn't already downloaded, you can manage the
     deployment package when you deploy the task sequence.

     When you deploy the task sequence, you can also select the option of No
     deployment package for the feature update. When clients run the task
     sequence, they download the feature update from peers or the Microsoft
     cloud.

     The option to Pre-download content for this task sequence doesn't apply to
     feature updates.

   Review the configuration of the following client settings in the Software Updates
   group, which are applicable to this scenario:

      Specify thread priority for feature updates: In most instances, set this value to
      Normal.

      Enable Dynamic Update for feature updates: Use this setting to use dynamic
      update to install language packs, features on demand, drivers, and cumulative
      updates during Windows Setup. Clients download these other updates from the
      internet.

      Allow clients to download delta content when available: If you use Windows
      Delivery Optimization, the content that the client downloads may be much
      smaller.

Known issues with feature updates in a task sequence

<!-- p.191 -->

Windows 11 Feature Upgrades are not visible to be selected from the Wizard. This
happens if the License Terms of the desired Feature Upgrade have not been accepted
yet. To do so navigate to the Feature Upgrade and select "Review Licence" from the
context menu. Review and Accept the licensing terms to make this Upgrade
"deployable".

Create a new task sequence

Applies to version 2103

If you need to create a new task sequence, you need an OS upgrade package to
complete the Create Task Sequence Wizard.

  ７ Note

  To create a task sequence to upgrade Windows, you typically use the steps in the
  Process section. The task sequence includes the Upgrade OS step, as well as
  additional recommended steps and groups to handle the end-to-end upgrade
  process.

  You can create a custom task sequence and add the Upgrade OS step. If you
  choose this method, also add the Restart Computer step after the Upgrade OS
  step. Make sure to use the setting for The currently installed default operating
  system to restart the computer into the installed OS and not Windows PE.

If you have an existing in-place upgrade task sequence, edit or copy it. Then change the
Upgrade OS task sequence step to install the feature update.

Starting in version 2107, you can create a new task sequence with just a feature update.

Export, import, and migrate task sequences

If you export a task sequence with the Upgrade OS step that uses a feature update, the
exported task sequence doesn't include the feature update content. When you import
the task sequence, readd the Upgrade OS step with the feature update.

This behavior is similar if you migrate a task sequence with a feature update between
hierarchies.

Create prestaged content file

<!-- p.192 -->

You can't currently use the action to Create prestaged content file for a task sequence
with a feature update.

Create standalone media

Standalone media isn't supported for a task sequence with a feature update. When you
try to create standalone media, it fails with entries similar to the following in
CreateTSMedia.log:

  log

  Unable to retrieve policy for Task Sequence XYZ004BD from site XYZ.
  Failed to initialize.... Verify the user is authorized to create Task
  Sequence media and has local admin permissions.
  MediaGenerator::~MediaGenerator()
  Failed to create media generator (0x80070490)
  CreateTsMedia failed with error 0x80070490, details=''
  Media temp directory 'C:\Users\jqpublic\AppData\Local\Temp\_tsmedia_1053544'
  is fully cleared
  Media creation process that was started from Admin Console completed.
  CreateMedia.exe finished with error code 80070490

Process
To upgrade the OS on clients, create a task sequence and select Upgrade an operating
system from upgrade package in the Create Task Sequence Wizard. The wizard adds the
task sequence steps to upgrade the OS, apply software updates, and install applications.

   1. In the Configuration Manager console, go to the Software Library workspace,
        expand Operating Systems, and then select Task Sequences.

   2. On the Home tab of the ribbon, in the Create group, select Create Task Sequence.

   3. On the Create a New Task Sequence page of the Create Task Sequence Wizard,
        select Upgrade an operating system from an upgrade package, and then select
        Next.

   4. On the Task Sequence Information page, specify the following settings:

             Task sequence name: Specify a name that identifies the task sequence.

             Description: Optionally specify a description.

   5. On the Upgrade the Windows Operating System page, specify the following
        settings:

<!-- p.193 -->

        Upgrade package: Specify the upgrade package that contains the OS
        upgrade source files. Verify that you've selected the correct upgrade package
        by looking at the information in the Properties pane. For more information,
        see Manage OS upgrade packages.

        Edition index: If there are multiple OS edition indexes available in the
        package, select the edition index you want. By default, the wizard selects the
        first index.

        Product key: Specify the Windows product key for the OS to install. Specify
        encoded volume license keys or standard product keys. If you use a standard
        product key, separate each group of five characters by a dash ( - ). For
        example: XXXXX-XXXXX-XXXXX-XXXXX-XXXXX . When the upgrade is for a volume
        license edition, the product key may not be required.

          ７ Note

          This product key can be a multiple activation key (MAK), or a generic
          volume licensing key (GVLK). A GVLK is also referred to as a key
          management service (KMS) client setup key. For more information, see
          Plan for volume activation. For a list of KMS client setup keys, see KMS
          client setup keys in the Windows Server activation guide.

        Ignore any dismissable compatibility messages: Select this setting if you're
        upgrading to Windows Server 2016 or later. If you don't select this setting,
        the task sequence fails to complete because Windows Setup is waiting for the
        user to select Confirm on a Windows app compatibility dialog.

6. On the Include Updates page, specify whether to install required, all, or no
  software updates. Then select Next. If you specify to install software updates,
  Configuration Manager installs only those updates targeted to the collections of
  which the destination computer is a member.

7. On the Install Applications page, specify the applications to install on the
  destination computer, and then select Next. If you select more than one
  application, also specify whether the task sequence should continue if the
  installation of a specific application fails.

8. Complete the wizard.

） Important

<!-- p.194 -->

  When the task sequence runs on a device, the Configuration Manager client creates
  several scripts to control the task sequence behavior in various scenarios. When the
  task sequence completes, the client doesn't remove these scripts until the
  computer restarts. These script files don't contain sensitive information.

Customize
The default task sequence template for in-place upgrade includes other groups with
recommended actions to add before and after the upgrade process. These actions are
common among many customers who are successfully upgrading devices to Windows
10 or later. For more information, see In-place upgrade recommendations.

Next steps
Deploy the task sequence, Deploy the task sequence over the internet, or Create a
phased deployment.

The pre-cache feature for available deployments of task sequences lets clients download
relevant OS upgrade package content before a user installs the task sequence. For more
information, see Configure pre-cache content.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.195 -->

Task sequence steps to manage BIOS to
UEFI conversion
Article • 10/04/2022

Windows includes many security features that require UEFI-enabled devices. You might
have newer Windows devices that support UEFI, but are using legacy BIOS. Previously,
converting a device to UEFI required you to go to each device, repartition the hard disk,
and reconfigure the firmware.

With Configuration Manager you can automate the following actions:

      Prepare a hard drive for BIOS to UEFI conversion
      Convert from BIOS to UEFI as part of the in-place upgrade process
      Collect UEFI information as part of hardware inventory

Hardware inventory collects UEFI information
The hardware inventory class (SMS_Firmware) and property (UEFI) are available to help
you determine whether a computer starts in UEFI mode. When a computer is started in
UEFI mode, the UEFI property is set to TRUE. Hardware inventory enables this class by
default. For more information about hardware inventory, see How to configure hardware
inventory.

Create a custom task sequence to prepare the
hard drive
You can customize an OS deployment task sequence with the TSUEFIDrive variable. The
Restart Computer step prepares a FAT32 partition on the hard drive for transition to
UEFI. The following procedure provides an example of how you can create task
sequence steps to do this action.

Prepare the FAT32 partition for the conversion to UEFI
In an existing task sequence to install an OS, add a new group with steps to do the BIOS
to UEFI conversion.

   1. Create a new task sequence group after the steps to capture files and settings, and
      before the steps to install the OS. For example, create a group after the Capture
      Files and Settings group named BIOS-to-UEFI.

<!-- p.196 -->

2. On the Options tab of the new group, add a new task sequence variable as a
  condition. Set _SMSTSBootUEFI not equal true. With this condition, the task
  sequence only runs these steps on BIOS devices.

3. Under the new group, add the Restart Computer task sequence step. In Specify
  what to run after restart, select The boot image assigned to this task sequence is
  selected. This action restarts the computer in Windows PE.

4. On the Options tab, add a task sequence variable as a condition. Set
  _SMSTSInWinPE equals false. With this condition, the task sequence doesn't run
  this step if the computer is already in Windows PE.

<!-- p.197 -->

5. Add a step to start an OEM tool to convert the firmware from BIOS to UEFI. This
  step is typically Run Command Line, with the command to run the OEM tool.

6. Add the Format and Partition Disk task sequence step. In this step, configure the
  following options:

  a. Create the FAT32 partition to convert to UEFI before the OS is installed. For Disk
     type, choose GPT.

<!-- p.198 -->

b. Go to the properties for the FAT32 partition. In the Variable field, enter
  TSUEFIDrive . When the task sequence detects this variable, it prepares the

  partition for the UEFI transition before it restarts the computer.

<!-- p.199 -->

      c. Create an NTFS partition that the task sequence uses to save its state and to
        store log files.

   7. Add another Restart Computer task sequence step. In Specify what to run after
     restart, select The boot image assigned to this task sequence is selected to start
     the computer in Windows PE.

        Tip

       By default, the EFI partition size is 500 MB. In some environments, the boot
       image is too large to store on this partition. To work around this issue,
       increase the size of the EFI partition. For example, set it to 1 GB.

Convert from BIOS to UEFI during in-place
upgrade
Windows includes a simple conversion tool, MBR2GPT. It automates the process to
repartition the hard disk for UEFI-enabled hardware. You can integrate the conversion

<!-- p.200 -->

tool into the in-place upgrade process. Combine this tool with your upgrade task
sequence and the OEM tool that converts the firmware from BIOS to UEFI.

Requirements
     A supported version of Windows 10 or later
     Computers that support UEFI
     OEM tool that converts the computer's firmware from BIOS to UEFI

Process to convert from BIOS to UEFI during an in-place
upgrade task sequence
   1. Create a task sequence to upgrade an OS

   2. Edit the task sequence. In the Post-Processing group, make the following changes:
     a. Add the Run Command Line step. Specify the command line for the MBR2GPT
        tool. When run in the full OS, configure it to covert the disk from MBR to GPT
        without modifying or deleting data. In Command line, enter the following
        command: MBR2GPT.exe /convert /disk:0 /AllowFullOS

        Tip

       You can also choose to run the MBR2GPT.EXE tool when in Windows PE
       instead of in the full OS. Add a step to restart the computer to Windows PE
       before the step to run the MBR2GPT.EXE tool. Then remove the /AllowFullOS
       option from the command line.

     For more information about the tool and available options, see MBR2GPT.EXE.

     a. Add a step to run the OEM tool that converts the firmware from BIOS to UEFI.
        This step is typically Run Command Line, with a command line to run the OEM
        tool.

     b. Add the Restart Computer step, and select The currently installed default
        operating system.

   3. Deploy the task sequence.

Feedback
