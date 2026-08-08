---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 801-840"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0801-0840
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0801-0840
family: sccm
documentKind: "doc"
abstract: "4. On the Ribbon, on the Home tab, in the Create group, select Import Driver. The Import New Driver Wizard starts. 5. Complete the Import New Driver Wizard using the information in Table 21. Accept the default values unless otherwise specified. Table 21. Information for Completi"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 801-840

<!-- p.801 -->

4. On the Ribbon, on the Home tab, in the Create group, select Import Driver.

  The Import New Driver Wizard starts.

5. Complete the Import New Driver Wizard using the information in Table 21. Accept
  the default values unless otherwise specified.

  Table 21. Information for Completing the Import New
  Driver Wizard

                                                                           ﾉ   Expand table

   On this wizard page     Do this

   Locate Driver           In Source folder, type \\WDG-MDT-01\Source$\Drivers, and
                           then select Next.

   Locate Driver: Driver   Select Next.
   Details

   Locate Driver: Add       a. Select New Package.
   Driver to Package        b. Complete the New Driver Package dialog box by performing
                              the following steps:

                                i. In Name, type device_driver_name Package (where
                                   device_driver_name is a descriptive name for the device
                                   drivers).
                               ii. In Comment, type Device drivers that are necessary for
                                   the reference and target computers.
                            c. In Driver package source, type \\WDG-MDT-
                               01\Packages$\Drivers, and then select OK.
                            d. Select Next.

   Locate Driver: Add      1. In the list of images, select the Windows PE Custom check
   Driver to Boot Images   box.
                           2. Select the Update distribution points when finished check
                           box, and then select Next.

   Summary                 Review the information in the Details box that you provided
                           while completing the previous wizard pages, and then select
                           Next.

   Progress                The progress for importing the device drivers is displayed.

   Confirmation            Select Close.

  To select the distribution points for the driver package

<!-- p.802 -->

 6. Select Start, point to All Programs, and then point to Microsoft System Center
   2012. Point to Configuration Manager, and then select Configuration Manager
   Console.

 7. In the Configuration Manager console, in the navigation pane, select Software
   Library.

 8. In the Software Library workspace, go to Overview/Operating Systems/Driver
   Packages.

 9. In the preview pane, select device_driver_name Package (where
   device_driver_name is a descriptive name for the device drivers).

10. On the Ribbon, on the Home tab, in the Deployment group, select Distribute
   Content.

   The Distribute Content Wizard starts.

11. Complete the Distribute Content Wizard using the information in Table 22. Accept
   the default values unless otherwise specified.

   Table 22. Information for Completing the Distribute
   Content Wizard

                                                                                ﾉ   Expand table

    On this wizard   Do this
    page

    General          Select Next.

    General:         Select Next.
    Content

    General:         1. Select Add, and then select Distribution Point.
    Content          The Add Distribution Points dialog box appears.
    Destination      2. In the Add Distribution Points dialog box, select \\WDG-MDT-
                     01.mdt2013.corp.woodgrovebank.com, and then select OK.
                     \\WDGMDT01.mdt2013.corp.woodgrovebank.com appears in the
                     Content destination list.
                     3. Select Next.

    Summary          Review the information in the Details box that you provided while
                     completing the previous wizard pages, and then select Next.

    Progress         The progress for distributing the software is displayed.

<!-- p.803 -->

      On this wizard     Do this
      page

      Completion         Select Close.

 12. Close all open windows and dialog boxes.

Step 3-4: Enable MDT Deployment Process Monitoring
Prior to deploying the reference computer (WDG-REF-01) with the task sequence
bootable media, enable MDT monitoring of the ZTI deployment process. You enable
monitoring on the Monitoring tab on the deployment share Properties dialog box.
Later in the process, you will monitor the ZTI deployment process using the Deployment
Workbench or the Get-MDTMonitorData cmdlet.

To enable MDT monitoring of the ZTI deployment process

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

  3. In the Actions pane, select New Deployment Shares.

     The New Deployment Share Wizard starts.

  4. Complete the New Deployment Share Wizard using the information in Table 23.

     Table 23. Information for Completing the New
     Deployment Share Wizard

                                                                          ﾉ   Expand table

      On this wizard       Do this
      page

      Path                 In Deployment share path, type C:\DeploymentShare$, and then
                           select Next.

      Share                Select Next.

      Descriptive Name     Select Next.

      Options              Select Next.

<!-- p.804 -->

      On this wizard       Do this
      page

      Summary              Select Next.

      Progress             The progress for creating the deployment share is displayed.

      Confirmation         Select Finish.

     The New Deployment Share Wizard finishes, and the new deployment share—MDT
     Deployment Share (C:\DeploymentShare$)—appears in the details pane.

   5. In the details pane, select MDT Deployment Share (C:\DeploymentShare$).

   6. In the Actions pane, select Properties.

     The MDT Deployment Share (C:\DeploymentShare$) Properties dialog box
     opens.

   7. In the MDT Deployment Share (C:\DeploymentShare$) Properties dialog box, on
     the Monitoring tab, select the Enable monitoring for this deployment share
     check box, and then select Apply.

   8. In the MDT Deployment Share (C:\DeploymentShare$) Properties dialog box, on
     the Rules tab, notice that the EventService property has been added to the
     CustomSettings.ini file, and then select OK.

     The EventService property is as follows:

        ini

        EventService=http://WDG-MDT-01:9800

   9. Close all open windows and dialog boxes.

Step 3-5: Customize the MDT Configuration Files for the
Reference Computer
When the MDT task sequence has been created, customize the MDT configuration files
that provide the configuration settings for deploying Windows 8.1 to the target
computer. Specifically, customize the CustomSettings.ini file.

When the CustomSettings.ini file customization is finished, save the updated files to the
source folder for the MDT Reference Computer Custom Settings package created earlier
in the process (E:\Packages$\CustomSettings_Reference). Then, add the DoCapture and

<!-- p.805 -->

EventService properties and corresponding values to the CustomSettings.ini file so that
the MDT deployment process captures an image of the reference computer (WDG-REF-
01) after deploying Windows 8.1.

To customize the MDT configuration files for the reference computer

   1. In Windows Explorer, go to E:\Packages$\CustomSettings_Reference, and then
     double-click CustomSettings.ini.

   2. Open Microsoft Notepad, and then add the following lines to the end of the
     CustomSettings.ini file, as shown in Listing 1:

       ini

        DoCapture=YES
        EventService=http://WDG-MDT-01:9800

       ７ Note

       Ensure that you remove any additional settings other than those shown in
       Listing 1.

     Listing 1. CustomSettings.ini File After Adding the DoCapture Property

       ini

        [Settings]
        Priority=Default
        Properties=MyCustomProperty

        [Default]
        OSInstall=Y
        SkipCapture=YES
        SkipAdminPassword=NO
        SkipProductKey=YES
        DoCapture=YES
        EventService=http://WDG-MDT-01:9800

   3. Save the file, and then exit Notepad.

Step 3-6: Update the Distribution Points for the Custom
Settings Files Package

<!-- p.806 -->

When the source folder has been updated for the MDT Reference Computer Custom
Settings package in Configuration Manager, update the distribution points for the MDT
Reference Computer Custom Settings Files package. Updating the distribution points
copies the updated version of the CustomSettings.ini file to the deployment shares
specified in the package.

To update the distribution points for the Custom Settings package

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Application
     Management/Packages.

   4. In the preview pane, select MDT Reference Computer Custom Settings.

   5. On the Ribbon, on the Home tab, in the Deployment group, select Update
     Distribution Points.

     The Configuration Manager dialog box opens, notifying you that you are going to
     update the package on all distribution points.

   6. In the Configuration Manager dialog box, select OK.

   7. Close all open windows and dialog boxes.

     Configuration Manager starts updating the distribution points with the latest
     versions of the CustomSettings.ini file. This process could take several minutes.
     Check the status of the package until the Last Update value of the package status
     has been updated to a recent date and time.

Step 3-7: Customize the Task Sequence for the Reference
Computer
For most deployments, the Windows 8.1 Reference Deployment task sequence created
earlier in the process performs all the necessary steps without modification. In this
sample, modify the task sequence to set the password for the local Administrator
account to a known value. By default, the task sequence sets the password for the local
Administrator account to a random value. Further customization of the task sequence
may be required depending on the environment.

<!-- p.807 -->

To customize the Windows 8.1 Reference Deployment task sequence

  1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

  2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

  3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences.

  4. In the preview pane, select Windows 8.1 Reference Deployment.

  5. On the Ribbon, on the Home tab, in the Task Sequence group, select Edit.

     The Windows 8.1 Reference Deployment Task Sequence Editor dialog box opens.

  6. In the Windows 8.1 Reference Deployment Task Sequence Editor dialog box, go
     to PostInstall/Apply Windows Settings.

  7. On the Properties tab, select Enable the account and specify the local
     administrator password.

  8. On the Properties tab, in Password and Confirm Password, type P@ssw0rd, and
     then select Apply.

  9. Make any additional modifications to the task sequence that the environment
     requires, and then select OK.

 10. Close all open windows and dialog boxes.

Step 4: Deploy Windows 8.1 and Capture an
Image of the Reference Computer
When you have created the task sequence to deploy Windows 8.1 to the reference
computer and captured an image of the reference computer, start the task sequence.
Create the operating system capture by using the Task Sequence Media Wizard in the
Configuration Manager console.

Deploy Windows 8.1 and capture an image of the reference computer by:

     Adding the reference computer to the Configuration Manager site database as
     described in Step 4-1: Add the Reference Computer to the Configuration Manager
     Site Database

<!-- p.808 -->

     Creating a collection that contains the reference computer you just added as
     described in Step 4-2: Create a Collection That Contains the Reference Computer

     Deploy the reference computer task sequence as described in Step 4-3: Deploy the
     Reference Computer Task Sequence

     Using the Task Sequence Media Wizard to create a task sequence bootable media
     disk as described in Step 4-4: Create the Task Sequence Bootable Media

     Starting the reference computer with the task sequence bootable media disk as
     described in Step 4-5: Start the Reference Computer with the Task Sequence
     Bootable Media

Step 4-1: Add the Reference Computer to the
Configuration Manager Site Database
To deploy an operating system without stand-alone media to a new computer that
Configuration Manager does not currently manage, add the new computer to the
Configuration Manager site database prior to initiating the operating system
deployment process. Configuration Manager can automatically discover computers on
the network that have a Windows operating system installed; however, if the computer
has no operating system installed, use the Import Computer Information Wizard to
import the new computer information.

To add the reference computer to the Configuration Manager site database

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Assets and
     Compliance.

   3. In the Assets and Compliance workspace, go to Overview/Devices.

   4. On the Ribbon, on the Home tab, in the Create group, select Import Computer
     Information.

     The Import Computer Information Wizard starts.

   5. Complete the Import Computer Information Wizard using the information in 24.
     Accept the default values unless otherwise specified.

<!-- p.809 -->

     Table 24. Information for Completing Import
     Computer Information Wizard

                                                                              ﾉ   Expand table

      On this wizard page     Do this

      Select Source           Select Import single computer, and then select Next.

      Select Source: Single   1. In Computer Name, type WDG-REF-01.
      Computer                2. In MAC address, type mac_address (where mac_address is the
                              media access control [MAC] address of the primary network
                              adapter for the reference computer, WDG-REF-01).
                              3. Select Next.

      Select Source: Data     Select Next.
      Preview

      Select Source:          Select Next.
      Choose Target
      Collection

      Summary                 Review the information in the Details box that you provided while
                              completing the previous wizard pages, and then select Next.

      Progress                The progress for importing the computer is displayed.

      Confirmation            Select Close.

     For more information on adding a new computer to the Configuration Manager
     site database, see the section, "To import computer information for a single
     computer," in the section, "How to Deploy Operating Systems in Configuration
     Manager," in the Configuration Manager Documentation Library, which is installed
     with Configuration Manager.

Step 4-2: Create a Collection That Contains the Reference
Computer
In the Configuration Manager console, create a collection that includes the reference
computer (WDG-REF-01). This computer collection is used later when advertising the
task sequence created earlier in the process.

To create a collection that includes the reference computer

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager

<!-- p.810 -->

  Console.

2. In the Configuration Manager console, in the navigation pane, select Assets and
  Compliance.

3. In the Assets and Compliance workspace, go to Overview/Device Collections.

4. On the Ribbon, on the Home tab, in the Create group, select Create, and then
  select Create Device Collection.

  The Create Device Collection Wizard starts.

5. Complete the Create Device Collection Wizard using the information in Table 25.
  Accept the default values unless otherwise specified.

  Table 25. Information for Completing the Create
  Device Collection Wizard

                                                                            ﾉ   Expand table

   On this wizard   Do this
   page

   General          a. In Name, type Microsoft Deployment - Reference Computer.
                    b. In Comment, type Computer that is to be the reference computer for
                       the target computers to be deployed.
                     c. In Limited Collection, select Browse.

                       The Select Collection dialog box appears. Complete the dialog box by
                       performing the following steps:

                         i. In Name, select All Systems.
                        ii. Select OK.
                    d. Select Next.

   Membership       a. Select Add Rule, and then select Direct Rule.
   Rules
                       The Create Direct Membership Rule Wizard starts.
                    b. Complete the Create Direct Membership Rule Wizard by performing
                       the following steps:

                         i. On the Welcome page, select Next.
                        ii. On the Search for Resources page, in Resource class, select
                            System Resource; in Attribute name, select Name; in Value, type
                            WDG-REF-01; and then select Next.
                       iii. On the Select Resources page, select WDG-REF-01, and then select
                            Next.

<!-- p.811 -->

      On this wizard   Do this
      page

                          iv. On the Summary page, select Next.
                           v. On the Progress page, view the progress for creating the new
                              membership rule.
                          vi. On the Completion page, select Close.
                        c. Select Next.

      Summary          Review the information in the Details box that you provided while
                       completing the previous wizard pages, and then select Next.

      Progress         The progress for creating the device collection is displayed.

      Completion       Select Close.

     For more information, see the section, "How to Create Collections in Configuration
     Manager," in the Configuration Manager Documentation Library, which is installed
     with Configuration Manager.

Step 4-3: Deploy the Reference Computer Task Sequence
In the Configuration Manager console, deploy the task sequence created earlier in the
process to the device collection that includes the reference computer created earlier in
the process.

To deploy the task sequence

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences.

   4. In the preview pane, select Windows 8.1 Reference Deployment.

   5. On the Ribbon, on the Home tab, in the Deployment group, select Deploy.

     The Deploy Software Wizard starts.

   6. Complete the Deploy Software Wizard using the information in Table 26. Accept
     the default values unless otherwise specified.

<!-- p.812 -->

     Table ARABIC 26. Information for Completing the
     Deploy Software Wizard

                                                                           ﾉ   Expand table

      On this wizard page     Do this

      General                 1. In Collection, select Browse.
                              2. In the Browse Collection dialog box, select Microsoft
                              Deployment - Reference Computer, and then select OK.
                              3. In Comment, type Deploy Windows 8.1 to the reference
                              computer and then capture an image of the reference
                              computer.
                              4. Select Next.

      Deployment Settings     1. In Purpose, select Available.
                              2. Select the Make available to boot media and PXE check box.
                              3. Select Next.

      Deployment Settings:    Select Next.
      Schedule

      Deployment Settings:    Select Next.
      User Experience

      Deployment Settings:    Select Next.
      Alerts

      Deployment Settings:    Select Next.
      Distribution Points

      Summary                 Review the information in the Details box that you provided
                              while completing the previous wizard pages, and then select
                              Next.

      Progress                The progress for deploying the task sequence is displayed.

      Completion              Select Close.

     For more information, see the section, "How to Deploy a Task Sequence," in the
     Configuration Manager Documentation Library, which is installed with
     Configuration Manager.

Step 4-4: Create the Task Sequence Bootable Media
To initiate the MDT process, provide a method for starting the computer with Windows
PE and the necessary software by creating the task sequence bootable media disk. Use

<!-- p.813 -->

the Task Sequence Media Wizard in the Configuration Manager console to create
bootable media for storage on a USB flash drive, CD, or DVD.

To create a task sequence bootable media disk

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences.

   4. On the Ribbon, on the Home tab, in the Create group, select Create Task
     Sequence Media.

     The Create Task Sequence Media Wizard starts.

   5. Complete the Create Task Sequence Media Wizard using the information in Table
     27. Accept the default values unless otherwise specified.

     Table 27. Information for Completing the Create Task
     Sequence Media Wizard

                                                                             ﾉ   Expand table

      On this wizard page   Do this

      Select Media Type     1. Select Bootable media.
                            2. Clear the Allow unattended operating system deployment
                            check box.
                            3. Select Next.

      Select Media Type:    Select Site-based media, and then select Next.
      Media Management

      Select Media Type:    In Media file, type \\WDG-MDT-
      Media Type            01\Capture$\CM2012_TS_Boot_Media.iso, and then select Next.

      Select Media Type:    In Password and Confirm password, type P@ssw0rd, and then
      Security              select Next.

      Select Media Type:    1. In Boot image, select Browse.
      Boot Image            2. In the Select a Boot Image dialog box, select Windows PE
                            Custom, and then select OK.

<!-- p.814 -->

      On this wizard page     Do this

                              3. In Distribution point, select \\WDG-MDT-
                              01.mdt2013.corp.woodgrovebank.com, and then select OK.
                              4. In Management point, select \\WDG-MDT-
                              01.mdt2013.corp.woodgrovebank.com, and then select OK.
                              5. Select Next.

      Select Media Type:      Select Next.
      Customization

      Summary                 Review the information in the Details box that you provided while
                              completing the previous wizard pages, and then select Next.

      Progress                The progress for creating the task sequence media is displayed.

      Completion              Select Close.

     The wizard creates the CM2012_TS_Boot_Media.iso file in the WDG-MDT-
     01Capture$ shared folder.

   6. If WDG-REF-01 is a physical computer, create a CD or DVD of the International
     Organization for Standardization (ISO) file. If WDG-REF-01 is a VM, start the VM
     directly from the ISO file.

     For more information on creating the task sequence bootable media disk, see the
     section, "How to Create Bootable Media," in the Configuration Manager
     Documentation Library, which is installed with Configuration Manager.

Step 4-5: Start the Reference Computer with the Task
Sequence Bootable Media
Start the reference computer (WDG-REF-01) with the task sequence bootable media disk
created earlier in the process. This medium starts Windows PE on the reference
computer and initiates the MDT process. At the end of the MDT process, Windows 8.1 is
deployed on the reference computer and an image of the reference computer is saved
to \WDG-MDT-01\Capture$\WDG-REF-01.wim.

  ７ Note

  You can also initiate the MDT process by starting the target computer from
  Windows Deployment Services.

To start the reference computer with the task sequence bootable media

<!-- p.815 -->

1. Start WDG-REF-01 with the task sequence bootable media created earlier in the
  process.

  Windows PE starts, and then the Task Sequence Wizard starts.

2. Complete the Task Sequence Wizard using the information in Table 28. Accept the
  default values unless otherwise specified.

  Table 28. Information for Completing the Task
  Sequence Wizard

                                                                          ﾉ   Expand table

   On this wizard page            Do this

   Welcome to the Task            In Password, type P@ssw0rd, and then select Next.
   Sequence Wizard

   Select a Task Sequence         In the list box, select Windows 8.1 Reference Deployment,
                                  and then select Next.

  To monitor the reference computer deployment process using the Deployment
  Workbench

3. On WDG-MDT-01, select Start, and then point to All Programs. Point to Microsoft
  Deployment Toolkit, and then select Deployment Workbench.

4. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/MDT Deployment Share
  (C:\DeploymentShare$)/Monitoring.

5. In the details pane, view the deployment process for WDG-REF-01.

6. In the Actions pane, periodically select Refresh.

  The status of the deployment process is updated in the details pane. Continue to
  monitor the deployment process until the process is complete.

7. In the details pane, select WDG-REF-01.

8. In the Actions pane, select Properties.

  The WDG-REF-01 Properties dialog box is displayed.

9. In the WDG-REF-01 Properties dialog box, on the Identity tab, view the
  monitoring information provided about the deployment process as described in

<!-- p.816 -->

Table 29.

Table 29. Monitoring Information About the
Deployment Process

                                                                        ﾉ    Expand table

 Information         Description

 ID                  Unique identifier for the computer being deployed.

 Computer Name       The name of the computer being deployed.

 Deployment status   The current status of the computer being deployed; the status can
                     be one of the following:

                     - Running. The task sequence is healthy and running.
                     - Failed. The task sequence failed, and the deployment process was
                     unsuccessful.
                     - Completed. The task sequence has finished.
                     - Unresponsive. The task sequence has not updated its status in the
                     past four hours and is assumed to be nonresponsive.

 Step                The current task sequence step being run.

 Progress            The overall progress of the task sequence. The progress bar
                     indicates how many task sequence steps have been run out of the
                     total number of task sequence steps.

 Start               The time the deployment process started.

 End                 The time the deployment process ended.

 Elapsed             The length of time the deployment process has been running or
                     took to run if the deployment process has finished.

 Errors              The number of errors encountered during the deployment process.

 Warnings            The number of warnings encountered during the deployment
                     process.

 Remote Desktop      This button allows you to establish a remote desktop connection
                     with the computer being deployed using the Windows Remote
                     Desktop feature. This method assumes that:

                     - The target operating system is running and has remote desktop
                     support enabled
                     - mstsc.exe is in the path Note: This button is always visible but may
                     not be able to establish a remote desktop session if the monitored
                     computer is running Windows PE, has not completed installation of

<!-- p.817 -->

    Information         Description

                        the target operating system, or does not have the Remote Desktop
                        feature enabled.

    VM Connection       This button allows you to establish a remote desktop connection to
                        a VM running in HyperV®. This method assumes that:

                        - The deployment is being performed to a VM running on Hyper-V
                        - vmconnect.exe is located in the %ProgramFiles%\Hyper-V folder
                        Note: This button appears when ZTIGather.wsf detects that Hyper-V
                        integration components are running on the monitored computer.
                        Otherwise, this button will not be visible.

    DaRT Remote         This button allows you to establish a remote control session using
    Control             the remote viewer feature in the Diagnostics and Recovery Toolkit
                        (DaRT).

                        This method assumes that:

                        - DaRT has been deployed to the target computer and is currently
                        running
                        - DartRemoteViewer.exe is located in the
                        %ProgramFiles%\Microsoft DaRT 7\v7 folder Note: This button
                        appears when ZTIGather.wsf detects that DaRT is running on the
                        monitored computer. Otherwise, this button will not be visible.

    Automatically       Check box that controls whether the information in the dialog box is
    refresh this        automatically refreshed. If the check box is:
    information every
    10 seconds          - Selected, the information is refreshed every 10 seconds
                        - Cleared, the information is not automatically refreshed and must
                        be manually refreshed using the Refresh Now button

    Refresh Now         This button immediately refreshes the information displayed in the
                        dialog box.

10. In the WDG-REF-01 Properties dialog box, select OK.

11. Close the Deployment Workbench.

   To monitor the reference computer deployment process using the Get-
   MDTMonitorData cmdlet

12. On WDG-MDT-01, select Start, point to Administrative Tools, and then select
   Windows PowerShell Modules.

   The Windows PowerShell Modules command prompt opens.

<!-- p.818 -->

13. Create a Windows PowerShell drive that uses the MDT PowerShell provider by
   running the New-PSDrive cmdlet, as shown in the following example:

     PowerShell

     New-PSDrive -Name DS001 -PSProvider mdtprovider -Root
     d:\DeploymentShare$

14. View the MDT monitoring process by running the Get-MDTMonitorData cmdlet,
   as shown in the following example:

     PowerShell

     Get-MDTMonitorData -Path DS001:

   This command returns the monitoring data collected by the MDT monitoring
   service running on the same computer that hosts the deployment share, as shown
   in the following example output:

     PowerShell

     Name               : WDG-REF-01
     PercentComplete    : 96
     Settings           :
     Warnings           : 0
     Errors             : 0
     DeploymentStatus   : 1
     StartTime          : 6/7/2012 6:45:39 PM
     EndTime            :
     ID                 : 1
     UniqueID           : 94a0830e-f2bb-421c-b1e0-6f86f9eb9fa1
     CurrentStep        : 130
     TotalSteps         : 134
     StepName           : Gather
     LastTime           : 6/7/2012 8:46:32 PM
     DartIP             :
     DartPort           :
     DartTicket         :
     VMHost             : XYL-DC-02
     VMName             : WDG-REF-01
     ComputerIdentities : {}

15. Close the Windows PowerShell console.

   If any problems occur during the deployment, consult the MDT document
   Troubleshooting Reference. When completed, a captured image of the reference
   computer should exist in \\WDG-MDT-01\Capture$\WDG-REF-01.wim.

<!-- p.819 -->

Step 5: Create and Configure a Task Sequence
to Deploy the Target Computer
After the task sequence to deploy the reference computer (WDG-REF-01) finishes, a
captured image of the reference computer is stored in \\WDG-MDT-01\Capture$\WDG-
REF-01.wim. Now, create a task sequence that will deploy the captured image of the
reference computer to the target computer (WDG-CLI-01). When this step is complete,
you can deploy the captured image of the reference computer to the target computer.

Create and configure a task sequence to deploy the target computer by:

     Importing the .wim file captured in the previous step into Configuration Manager
     using the Add Operating System Image Wizard as described in Step 5-1: Import
     the Captured .wim File into Configuration Manager

     Using the Create MDT Task Sequence Wizard to create an MDT task sequence
     template to deploy the captured image of the reference computer to the target
     computer as described in Step 5-2: Create an MDT Task Sequence to Deploy the
     Captured Image

     Selecting the distribution points for the new packages and images that the Create
     MDT Task Sequence Wizard creates as described in Step 5-3: Select the Distribution
     Points for the New Packages and Images

     Customizing the MDT configuration files for the target computer—specifically, the
     CustomSettings.ini file—as described in Step 5-4: Customize the MDT
     Configuration Files

     Updating the Configuration Manager distribution points for the Custom Settings
     package as described in Step 5-5: Update the Distribution Points for the Custom
     Settings Package

     Customizing the task sequence for the target computer as described in Step 5-6:
     Customize the Task Sequence for the Target Computer

     Configuring unattended installation of Office Professional Plus 2010 as described
     in Step 5-7: Configure an Unattended Installation of Office Professional Plus 2010

     Creating a Configuration Manager application to deploy Office Professional Plus
     2010 as described in Step 5-8: Create an Office Professional Plus 2010 Application

     Distributing the Office Professional Plus 2010 application to the distributions
     points as described in Step 5-9: Distribute the Office Professional Plus 2010
     Application

<!-- p.820 -->

     Making the Office Professional Plus 2010 application available to all users as
     described in Step 5-10: Make the Office Professional Plus 2010 Application
     Available to All Users

     Customizing the UDI Wizard configuration file as described in Step 5-11:
     Customize the UDI Wizard Configuration File for the Target Computer

     Creating a new custom wizard page to collect additional deployment information
     as described in Step 5-13: Create a New Custom Wizard Page

     Adding controls to the new custom wizard page as described in Step 5-14: Add
     Controls to New Custom Wizard Page

     Updating the MDT files package that contains the updated UDI Wizard
     configuration file as described in Step 5-15: Update the Distribution Points for the
     MDT Files Package

Step 5-1: Import the Captured .wim File into
Configuration Manager
After the image of the reference computer (WDG-REF-01) is captured in to the .wim file,
import the captured .wim file into Configuration Manager. Import the captured .wim file
into the Operating System Images node using the Add Operating System Image Wizard.

The captured WIM file contains two images, one for each partition on the reference
computer. Identify which of the images has the captured Windows 8.1 operating system
using the image description containing Windows 8.1. You use the image index when you
create the task sequence for deploying the captured image to the target computer.

To import the captured .wim file into Configuration Manager

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Operating
     System Images.

   4. On the Ribbon, in the Create group, select Add Operating System Image.

     The Add Operating System Image Wizard starts.

<!-- p.821 -->

 5. Complete the Add Operating System Image Wizard using the information in Table
   30. Accept the default values unless otherwise specified.

   Table 30. Information for Completing the Add
   Operating System Image Wizard

                                                                            ﾉ   Expand table

    On this wizard   Do this
    page

    Data Source      In Path, type \\WDG-MDT-01\Capture$\WDG-REF-01.wim, and then
                     select Next.

    General          1. In Name, type Windows 8.1 Reference Image.
                     2. In Version, type 1.00.
                     3. In Comments, type Windows 8.1 captured image of reference
                     computer (WDG-REF-01) used to deploy to target computers, and then
                     select Next.

    Summary          Review the information in the Details box that you provided while
                     completing the previous wizard pages, and then select Next.

    Progress         The progress for importing the operating system image is displayed.

    Completion       Select Close.

 6. In the preview pane, select Windows 8.1 Reference Image.

 7. In the preview pane, select the Details tab.

   The list of operating system partitions captured in the .wim file is displayed. The
   image index that contains Windows 8.1 is the image index you will specify later
   during the Create MDT Task Sequence Wizard.

 8. Record the image index that contains Windows 8.1.

      Tip

     For the purposes of this example, image index 2 should have the Windows 8.1
     operating system.

Step 5-2: Create an MDT Task Sequence to Deploy the
Captured Image

<!-- p.822 -->

After the image is captured, create a task sequence to deploy the captured image of the
reference computer (WDG-REF-01) to the target computer (WDG-CLI-01). Most of the
packages needed for this task sequence were created earlier in the process. However,
you must create a new MDT Custom Settings package that has the proper configuration
settings for the target computer and creates an operating system image of the captured
image of the reference computer.

To create a task sequence template to deploy the captured image to the target
computer

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

   5. Complete the Create MDT Task Sequence Wizard using the information in Table 31.
     Accept the default values unless otherwise specified.

     Table 31. Information for Completing the Create MDT
     Task Sequence Wizard

                                                                            ﾉ   Expand table

      On this wizard   Do this
      page

      Choose           Select Client Task Sequence, and then select Next.
      Template

      Choose           1. In Task sequence name, type UDI - Windows 8.1 Target Deployment.
      Template:        2. In Task sequence comments, type Task sequence for deploying
      General          captured reference computer image to the target computer (WDG-CLI-
                       01) using UDI, and then select Next.

      Choose           1. In Use name, type Woodgrove Bank Employee.
      Template:        2. In Organization name, type Woodgrove Bank.

<!-- p.823 -->

On this wizard   Do this
page

Details          3. Select Next.

Choose           Select Next.
Template:
Capture
Settings

Boot Image       1. In Specify an existing boot image package, select Browse.
                 2. In Select a Package dialog box, select Windows PE Custom, and then
                 select OK.
                 3. Select Next.

MDT Package      1. In Specify an existing Microsoft Deployment Toolkit Files package,
                 select Browse.
                 2. In the Select a Package dialog box, select MDT Files, and then select
                 OK.
                 3. Select Next.

OS Image         1. Select Specify an existing OS image.
                 2. In Specify an existing OS image, select Browse.
                 3. In the Select a Package dialog box, select Windows 8.1 Reference
                 Image, and then select OK.
                 4. Select Next.

OS Image: OS     1. In The selected operating system image (WIM) file contains multiple
Image Index      images. Specify which image you would like to deploy, select
                 image_index (where image_index is the image index of the image that
                 contains Windows 8.1, which was identified in the Step 5-1: Import the
                 Captured .wim File into Configuration Manager; for the purposes of this
                 guide, select 2).
                 2. Select Next.

Deployment       Select Perform a "User-Driven Installation", and then select Next.
Method

Client Package   1. In Specify an existing ConfigMgr client package, select Browse.
                 2. In the Select a Package dialog box, select Microsoft Configuration
                 Manager Client Upgrade, and then select OK.
                 3. Select Next.

USMT Package     1. In Specify an existing USMT package, select Browse.
                 2. In the Select a Package dialog box, select USMT, and then select OK.
                 3. Select Next.

Settings         1. Select Create a new settings package.
Package          2. In Package source folder to be created, type \\WDG-MDT-
                 01\Packages$\UDICustomSettings_Target, and then select Next.

<!-- p.824 -->

      On this wizard   Do this
      page

      Settings         1. In Name, type UDI Target Computer Custom Settings.
      Package:         2. In Version, type 1.00.
      Settings         3. In Comments, type Configuration settings for MDT deployment
      Details          process using UDI (such as CustomSettings.ini) for the target computer,
                       and then select Next.

      Sysprep          Select Next.
      Package

      Summary          Review the information in the Details box that you provided while
                       completing the previous wizard pages, and then select Next.

      Progress         The progress for creating the task sequence is displayed.

      Confirmation     Select Finish.

     The list of task sequences is displayed. The task sequence that you just created
     (UDI - Windows 8.1 Target Deployment) is listed in the list of task sequences.

Step 5-3: Select the Distribution Points for the New
Packages and Images
Running the Create MDT Task Sequence Wizard to create the task sequence for the
target generates a new software-distribution package and a new image. When the
package and image are created, select the distribution points from which the package
and image will be copied and available to target computers.

  ７ Note

  In this sample, there is only one distribution point (WDG-MDT-01). However, most
  production networks will have multiple distribution points. When performing this
  step in a production environment, select the appropriate distribution points for the
  network.

Select the distribution points for the software-distribution package (for the new target
computer custom settings package called MDT 2013 Target Computer Custom Settings)
and the operating system image package (for the new captured .wim file of the
reference computer called Windows 8.1 Reference Image).

To select the distribution points for the software-distribution package

<!-- p.825 -->

1. Select Start, point to All Programs, and then point to Microsoft System Center
  2012. Point to Configuration Manager, and then select Configuration Manager
  Console.

2. In the Configuration Manager console, in the navigation pane, select Software
  Library.

3. In the Software Library workspace, go to Overview/Operating Systems/Task
  Sequences.

4. In the preview pane, select UDI - Windows 8.1 Target Deployment.

  On the Ribbon, on the Home tab, in the Deployment group, select Distribute
  Content.

  The Distribute Content Wizard starts.

5. Complete the Distribute Content Wizard using the information in Table 32. Accept
  default values unless otherwise specified.

  Table 32. Information for Completing the Distribute
  Content Wizard

                                                                               ﾉ   Expand table

   On this wizard   Do this
   page

   General          Select Next.

   Content          Select Next.

   General:         1. Select Add, and then select Distribution Point.
   Content          The Add Distribution Points dialog box appears.
   Destination      2. In the Add Distribution Points dialog box, select
                    \\WDGMDT01.mdt2013.corp.woodgrovebank.com, and then select OK.
                    \\WDGMDT01.mdt2013.corp.woodgrovebank.com appears in the
                    Content destination list.
                    3. Select Next.

   Summary          Review the information in the Details box that you provided while
                    completing the previous wizard pages, and then select Next.

   Progress         The progress for distributing the software is displayed.

   Completion       Select Close.

<!-- p.826 -->

Step 5-4: Customize the MDT Configuration Files
When the task sequence for the target computer has been created, customize the MDT
configuration files that provide the configuration settings for deploying Windows 8.1 to
the target computer—specifically, CustomSettings.ini.

When the CustomSettings.ini file has been customized, save the updated files to the
source folder for the MDT Custom Settings package created earlier in the process
(E:\Packages$\CustomSettings_Target).

To customize the MDT configuration files for the target computer

   1. In Windows Explorer, go to E:\Packages$\CustomSettings_Target folder, and then
     double-click CustomSettings.ini.

   2. Open Notepad, and then add the following line to the CustomSettings.ini file that
     the environment requires, as shown in Listing 2:

     This setting configures monitoring of the target computer deployment.

       ７ Note

       Make any other changes that your environment requires.

     Listing 2. Default CustomSettings.ini File

       ini

       [Settings]
       Priority=Default
       Properties=MyCustomProperty

       [Default]
       OSInstall=Y
       SkipCapture=YES
       SkipAdminPassword=NO
       SkipProductKey=YES
       EventService=http://WDG-MDT-01:9800

   3. Save the file, and then close Notepad.

Step 5-5: Update the Distribution Points for the Custom
Settings Package

<!-- p.827 -->

When the source folder has been updated for the MDT Target Computer Custom
Settings package in Configuration Manager, update the distribution points for the MDT
Target Computer Custom Settings package. Updating the distribution points copies the
updated version of the CustomSettings.ini file to the deployment shares specified in the
package.

To update the distribution points for the Custom Settings package

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Application
     Management/Packages.

   4. In the preview pane, select MDT Target Computer Custom Settings.

   5. On the Ribbon, on the Home tab, in the Deployment group, select Update
     Distribution Points.

     The Configuration Manager dialog box opens, notifying you that you are going to
     update the package on all distribution points.

   6. In the Configuration Manager dialog box, select OK.

   7. Close all open windows and dialog boxes.

Step 5-6: Customize the Task Sequence for the Target
Computer
For most deployments, the Windows 8.1 Target Deployment task sequence created
earlier in the process performs all the necessary steps without modification. In this
sample, modify the task sequence template to set the password for the local
Administrator account to a known value. (By default, the task sequence sets the
password for the local Administrator account to a random value.) The task sequence
may require further customization depending on the environment.

To customize the Windows 8.1 Target Deployment task sequence

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager

<!-- p.828 -->

     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences.

   4. In the preview pane, select UDI - Windows 8.1 Target Deployment.

   5. On the Ribbon, on the Home tab, in the Task Sequence group, select Edit.

     The Windows 8.1 Reference Deployment Task Sequence Editor dialog box opens.

   6. In the Windows 8.1 Reference Deployment Task Sequence Editor dialog box, go
     to PostInstall/Apply Windows Settings.

   7. On the Properties tab, select Enable the account and specify the local
     administrator password.

   8. On the Properties tab, in Password and Confirm Password, type P@ssw0rd, and
     then select Apply.

   9. Make any additional modifications to the task sequence that the environment
     requires, and then select OK.

 10. Close all open windows and dialog boxes.

Step 5-7: Configure an Unattended Installation of Office
Professional Plus 2010
Configuration Manager distributes the files and folders used to deploy Office
Professional Plus 2010 but does not provide the method for performing an unattended
installation after distribution. Instead, the unattended installation must be configured
using methods provided in Office Professional Plus 2010. You can configure unattended
(silent) installation of Office Professional Plus 2010 using one of the following methods:

     Create an Office Customization Tool (OCT) Setup customization file (.msp file).

     Modify the Config.xml file.

     For more information about each of these methods, see Customize Setup before
     installing Office 2010.

<!-- p.829 -->

   For the purposes of this guide, the unattended installation of Office Professional
   Plus 2010 will be done by creating an OCT Setup customization file (.msp file). You
   will save the OCT Setup customization file in the Updates folder, which is
   automatically scanned by the Office Professional Plus 2010 Setup Wizard.

   To configure an unattended installation of Office Professional Plus 2010

 1. At a command prompt, type the following command, and then press ENTER.

     Windows Command Prompt

      e:

 2. At a command prompt, type the following command, and then press ENTER.

     Windows Command Prompt

      cd \Source$\OfficeProPlus2010\

 3. At a command prompt, type the following command, and then press ENTER.

     Windows Command Prompt

      setup /admin

   The OCT starts, and the Select Product dialog box opens.

 4. In the OCT, in the Select Product dialog box, select OK.

   The OCT loads the appropriate information, and then displays the settings that can
   be customized in the .msp file.

 5. In the OCT, in the navigation pane, go to Setup/Install location and organization
   name.

 6. In the preview pane, in Organization name, type Woodgrove Bank.

 7. In the OCT, in the navigation pane, go to Setup/Licensing and user interface.

 8. In the preview pane, select the I accept the terms in the License Agreement check
   box.

 9. In the preview pane, in Display level, select None.

10. From the File menu, select Save As.

<!-- p.830 -->

     The Save As dialog box opens.

 11. In the Save As dialog box, type
     E:\Source$\OfficeProPlus2010\Updates\OPP2010_Unattend, and then select Save.

     The OPP2010_Unattend.msp file is saved.

 12. Close all open windows and dialog boxes.

Step 5-8: Create an Office Professional Plus 2010
Application
One of the advantages to performing MDT deployments using UDI is the ability for the
user to select the applications to install at deployment time. You can add any number of
applications to Configuration Manager, and then select the applications when running
the UDI Wizard, as described in Step 6-4: Start the Target Computer with the Task
Sequence Bootable Media.

You can configure the applications that appear in the UDI Wizard using the UDI Wizard
Designer, as described in Step 5-11: Customize the UDI Wizard Configuration File for the
Target Computer.

To create an Office Professional Plus 2010 application

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Application
     Management/Applications.

   4. On the Ribbon, on the Home tab, in the Create group, select Create Application.

     The Create Application Wizard starts.

   5. Complete the Create Application Wizard using the information in Table 33. Accept
     default values unless otherwise specified.

     Table 3. Information for Completing the Create
     Application Wizard

<!-- p.831 -->

                                                                          ﾉ   Expand table

On this       Do this
wizard page

General       Select Manually specify the application information, and then select Next.

General:      1. In Name, type Microsoft Office Professional Plus 2010 - x86.
General       2. In Administrator comments, type 32-bit version of Microsoft Office
              Professional Plus 2010.
              3. Select the Allow this application to be installed from Install Application task
              sequence action instead of deploying it manually check box.
              4. Select Next.

General:      1. In Localized description, type 32-bit version of Microsoft Office Professional
Application   Plus 2010 for use by Woodgrove Bank Employees.
Catalog       2. In Keywords, type Office Professional Plus 2010.
              3. Select Next.

General:      a. Select Add.
Deployment
Type s           The Create Deployment Type Wizard Starts.
              b. In the Create Deployment Type Wizard, on the General page, select
                 Manually specify the deployment type information and then select Next.
              c. On the General: General Information page, perform the following steps, and
                 then select Next:

                  i. In Name, type Microsoft Office Professional Plus 2010 - x32 (Windows
                      Installer).
                  ii. In Administrator comments, type Deploy Microsoft Office Professional
                      Plus 2010 using native Windows Installer.
              d. On the General: Content page, perform the following steps, and then select
                 Next:

                  i. In Content location, type \\WDGMDT01\Source$\OfficeProPlus2010.
                   ii. In Installation program, type setup.exe.
                  iii. In Uninstall program, type setup.exe /uninstall PROPLUS.
              e. On the General: Detection Method page, perform the following steps, and
                 then select Next:

                  i. Select Add Clause,

                      The Detection Rule dialog box appears.
                  ii. In the Detection Rule dialog box, in Setting Type, select Windows
                      Installer.
                 iii. In Product code, select Browse

                    The Open dialog box appears.
                 iv. In the Open dialog box, in File name, type
                     \\WDGMDT01\Source$\OfficeProPlus2010\ProPlus.WW\ProPlusWW.msi,

<!-- p.832 -->

       On this       Do this
       wizard page

                           and then select Open.

                            The product code for Office Professional Plus 2010 appears in the
                            Product code box.
                         v. In the Detection Rule dialog box, select OK.
                      f. On the General: User Experience page, perform the following steps, and
                         then select Next:

                          i. In Installation behavior, select Install for system.
                         ii. In Logon requirement, select Whether or not a user is logged on.
                        iii. In Installation program visibility, select Normal.
                        iv. In Estimated installation time, type 120.
                     g. On the Requirements page, select Next.
                     h. On the Dependencies page, select Next.
                      i. On the Summary page, select Next.
                      j. On the Completion page, select Close.

                         The Create Application Wizard starts.
                      k. Select Next.

       Summary       Review the information in the Details box that you provided while completing
                     the previous wizard pages, and then select Next.

       Progress      The progress for creating the application is displayed.

       Completion    Select Close.

     The Office Professional Plus 2010 - x86 application appears in the preview pane.

Step 5-9: Distribute the Office Professional Plus 2010
Application
After you have created the Office Professional Plus 2010 application, you need to
distribute the application to the distribution points. Doing so allows installation of the
application from the distribution points. For the purposes of this guide, there is only one
distribution point (WDG-MDT-01). In typical Configuration Manager deployments, there
are usually multiple distribution points.

To distribute the Office Professional Plus 2010 application

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

<!-- p.833 -->

2. In the Configuration Manager console, in the navigation pane, select Software
  Library.

3. In the Software Library workspace, go to Overview/Application
  Management/Applications.

4. In the preview pane, select Microsoft Office Professional Plus 2012 - x86.

5. On the Ribbon, on the Home tab, in the Deployment group, select Distribute
  Content.

  The Distribute Content Wizard starts.

6. Complete the Distribute Content Wizard using the information in Table 34. Accept
  the default values unless otherwise specified.

  Table 34. Information for Completing the Distribute
  Content Wizard

                                                                             ﾉ     Expand table

   On this wizard    Do this
   page

   General           Select Next.

   General:          Select Next.
   Content

   General:          1. Select Add, and then select Distribution Point.
   Content           The Add Distribution Points dialog box appears.
   Destination       2. In the Add Distribution Points dialog box, select
                     \\WDGMDT01.mdt2013.corp.woodgrovebank.com, and then select OK.
                     \\WDGMDT01.mdt2013.corp.woodgrovebank.com appears in the
                     Content destination list.
                     3. Select Next.

   Summary           Review the information in the Details box that you provided while
                     completing the previous wizard pages, and then select Next.

   Progress          The progress for distributing the application is displayed.

   Completion        Select Close.

7. Close all open windows and dialog boxes.

<!-- p.834 -->

Step 5-10: Make the Office Professional Plus 2010
Application Available to All Users
After you have created the Office Professional Plus 2010 application, you need to
distribute the application to the distribution points. Doing so allows installation of the
application from the distribution points. For the purposes of this guide, there is only one
distribution point (WDG-MDT-01). In typical Configuration Manager deployments, there
are usually multiple distribution points.

To make the Office Professional Plus 2010 application available to all users

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Application
     Management/Applications.

   4. In the preview pane, select Microsoft Office Professional Plus 2010 - x86.

   5. On the Ribbon, on the Home tab, in the Deployment group, select Deploy.

     The Deploy Software Wizard starts.

   6. Complete the Deploy Software Wizard using the information in Table 35. Accept
     the default values unless otherwise specified.

     Table 35. Information for Completing the Deploy
     Software Wizard

                                                                                 ﾉ    Expand table

       On this wizard    Do this
       page

       General           1. In Collection, select Browse.
                         The Select Collection dialog box appears.
                         2. In the Select Collection dialog box, select All Users, and then select
                         OK.
                         3. In Comments, type Make Microsoft Office Professional Plus 2010
                         available for deployment to all users.
                         4. Select Next.

<!-- p.835 -->

      On this wizard         Do this
      page

      Content                Select Next.

      Deployment             Select Next.
      Settings

      Scheduling             Select Next.

      Alerts                 Select Next.

      Summary                Review the information in the Details box that you provided while
                             completing the previous wizard pages, and then select Next.

      Progress               The progress for deploying the application is displayed.

      Completion             Select Close.

   7. Close all open windows and dialog boxes.

Step 5-11: Customize the UDI Wizard Configuration File
for the Target Computer
The User-Driven Installation task sequence template includes a task sequence step that
runs the UDI Wizard. When a task sequence step runs the UDI Wizard, the step also
references an XML file that determines the configuration of the UDI Wizard. The
UDIWizard_Config.xml file in the Scripts folder controls the behavior of the UDI Wizard.
Customize the UDIWizard_Config.xml file using the UDI Wizard Designer.

The UDI Wizard Designer includes predefined stage groups for the UDI Wizard listed in
Table 36. You can add or remove the wizard pages that appear in the UDI Wizard and
the sequence of each wizard page for each stage group.

Table 36. Predefined Stage Groups for Each Supported
MDT Deployment Scenario

                                                                                    ﾉ   Expand table

 Stage         Description
 group

 New           Use this stage group as the basis for your deployment when a new installation of a
 Computer      Windows operating system is deployed to a new computer and no user state is
               migrated.

<!-- p.836 -->

 Stage        Description
 group

 Refresh      Use this stage group as the basis for your deployment when a computer is
              refreshed, including computers that must be re-imaged for image standardization
              or to address a problem.

 Replace      Use this stage group as the basis for your deployment when one computer replaces
              another computer. The existing user state migration data is saved from the original
              computer. Then, a new installation of Windows is deployed to a new computer.
              Finally, the user state data is restored to the new computer.

To customize the UDI Wizard configuration file for the reference computer

  1. Select Start, point to All Programs, point to Microsoft Deployment Toolkit, and
     then select UDI Wizard Designer.

     The UDI Wizard Designer starts.

  2. On the Ribbon, on the Home tab, in the File Menu group, select Open.

  3. In the Open dialog box, in File name, type \\WDG-MDT-
     01\Packages$\MDT_Files\Scripts\UDIWizard_Config.xml, and then select Open.

         ７ Note

         This opens the copy of the UDIWizard_Config.xml file that resides in the MDT
         Package folder you created when you ran the Create Microsoft Deployment
         Task Sequence Wizard earlier in the process.

  4. In the Page Library, select Install Programs.

  5. On the Ribbon, on the Home tab, in the Edit Settings group, select Configuration
     Manager.

     The Site Settings dialog box appears.

  6. In the Site Settings dialog box, perform the following steps, and then select OK:

     a. In Site Server Name, type WDG-MDT-01.

     b. In Site Code, type NYC.

     c. Select Validate Site.

     d. In Application Collection, type All Users.

<!-- p.837 -->

       ７ Note

       The Configuration Manager collection you type here must match the
       Configuration Manager collection to which you deployed your applications.
       In this guide, you selected the All Users collection in Step 5-10: Make the
       Office Professional Plus 2010 Application Available to All Users.

7. In the preview pane, on the Flow tab, expand StageGroup: New Computer.

  The list of wizard pages used in the StageGroup: New Computer flow is displayed.

    ７ Note

    Make note of the sequence of the wizard pages in the StageGroup: New
    Computer flow in the UDI Wizard Designer. You will see the same sequence of
    wizard pages when you run the UDI Wizard in Step 6-4: Start the Target
    Computer with the Task Sequence Bootable Media.

8. Configure the StageGroup: New Computer flow using the information for each
  page listed in Table 37. Accept the default values unless otherwise specified.

  Table 37. Information for Configuring UDI Wizard
  Designer Pages

                                                                         ﾉ   Expand table

   Wizard       Select the Configure tab and do the following
   page

   BitLocker     a. Under BitLocker Mode, expand BitLocker Mode. In BitLocker Checkbox,
                    clear the Initially check this check box check box.
                 b. Under BitLocker Mode, select Unlocked for each of the following
                    configuration options:

                         BitLocker Checkbox
                         BitLocker Mode Radio Buttons
                         PIN Text Box

                The status for each configuration option changes to Locked, which prevents
                users from changing these options in the UDI Wizard.

<!-- p.838 -->

Wizard     Select the Configure tab and do the following
page

Volume     a. Under Image Combo Box, expand Image Combo Behavior, under Image
              Combo Box Values, right-click Windows 8.1 RTM (x86), and then select
              Select an Operating System Image.

              The Select an Operating System Image dialog box appears.
           b. Complete the Select an Operating System Image dialog box by
              performing the following steps, and then select OK:

               i. In Select an Operating System Image/Installer to add, select
                  image_index (where image_index is the image index of the image that
                  contains Windows 8.1, which was identified in Step 5-1: Import the
                  Captured .wim File into Configuration Manager; for the purposes of
                  this guide, select 2).
                ii. In Display Name, type Windows 8.1 Reference Image - x64.
            c. Under Image Combo Box, expand Image Combo Behavior; under Image
               Combo Box Values, right-click Windows 8.1 RTM (x86), and then select
               Remove Item.

              The Delete Item Confirmation dialog box appears.
           d. In the Delete Item Confirmation dialog box, select Yes.
           e. Under User Data and Settings, expand User Data Combo Behavior, and
              then select the Format: Clean all the data on the target volume during
              install check box.
           f. Under User Data Combo Behavior, select Unlocked for each of the
              following configuration options:

                    Format Drive
                    Windows Directory

           The status for each configuration option changes to Locked, which prevents
           users from changing these options in the UDI Wizard.

New        1. Under Network Details, expand Network Details; in Domain or
Computer   Workgroup Radio Buttons, select Domain.
Details    2. Under Domain or Workgroup Radio Buttons, select Unlocked.
           The status changes to Locked, which prevents users from changing this
           option in the UDI Wizard.
           3. Under Network Details, expand Domains and OUs, and then select Add
           Domain.
           The Create or Edit Domain Information dialog box appears.
           4. In the Create or Edit Domain Information dialog box, in Domain Name
           type mdt2013.corp.woodgrovebank.com.
           5. In the Create or Edit Domain Information dialog box, in Friendly Name,
           type Woodgrove Bank Active Directory Domain, and then select OK.

<!-- p.839 -->

     Wizard       Select the Configure tab and do the following
     page

     Install       a. Under Software and Groups, right-click any blank area, and then select
     Programs         Add Software Group.

                     The Add/Edit a Software Group dialog box appears.
                   b. In the Add/Edit a Software Group dialog box, in Name, type Woodgrove
                      Bank Applications, and then select OK.
                   c. Under Software and Groups, select Woodgrove Bank Applications.
                   d. On the Ribbon, on the Home tab, in the General Software Item Settings
                      group, select Add, and then select Add Software to Group.

                     The Add Software to Group Wizard starts.
                   e. Complete the Add Software to Group Wizard by performing the following
                      steps:

                       i. On the What type of software item do you want to add page, select I
                          want to add an Application, and then select Next.
                      ii. On the Search Configuration Manager for the Software Item to Add
                          page, in Display Name, type Microsoft Office Professional Plus 2010 -
                           x86.
                      iii. On the Search Configuration Manager for the Software Item to Add
                           page, select Select.

                          The Search Applications dialog box appears.
                      iv. In the Search Applications dialog box, select Search, select Microsoft
                         Office Professional Plus 2010 - X86, and then select OK.
                      v. On the Search Configuration Manager for the Software Item to Add
                         page, select Finish.

                       Microsoft Office Professional Plus 2010 - x86 appears underneath the
                       Woodgrove Bank Applications software group.
                    f. Under Software and Groups, select General Software.
                   g. On the Ribbon, on the Home tab, in the General Software Item Settings
                      group, select Add, and then select Remove Item.

                       The Delete the Selected Item dialog box appears.
                   h. In the Delete the Selected Item dialog box, select Yes.
                    i. Under Software and Groups, select the check box for Woodgrove Bank
                       Applications.

                     The group and Microsoft Office Professional Plus 2010 - x86 are selected.

 9. On the Ribbon, on the Home tab, select Save.

   The File Save dialog box appears.

10. In the File Save dialog box, select OK.

<!-- p.840 -->

 11. Leave the UDI Wizard Designer open for the next step.

Step 5-13: Create a New Custom Wizard Page
You can create custom wizard pages that allow you to collect deployment information in
addition to the information collected on other UDI Wizard pages. You create custom
wizard pages based on the Build Your Own Page wizard page type. After you create the
custom wizard page, you can add controls to it and configure the task sequence
variables the controls set.

For this guide, Woodgrove Bank wants to allow users to enter their name and the
department in which they work. Woodgrove Bank is departmentalized by geographic
location. This information will be used to configure the registered user name and
organization in Windows. In this step, you add a new custom wizard page to the New
Computer stage group.

To create a new custom wizard page

   1. On the Ribbon, on the Home tab, in the Page Library group, select Add Page.The
     Add New Page dialog box appears.

   2. In the Add New Page dialog box, in the Page Type column, select Build Your Own
     Page.

   3. In Display Name, type User Information.

   4. In Page Name, type UserInformationPage, and then select OK.

     The User Information page appears in the Page Library.

   5. In the details pane, select the Flow tab.

   6. On the Flow tab, expand the New Computer stage group.

     The list of wizard pages in the New Computer stage group is displayed.

   7. In the Page Library, drag the User Information page to a point immediately before
     the BitLocker page in the New Computer stage group on the Flow tab.

   8. On the Ribbon, on the Home tab, select Save.

     The File Save dialog box appears.

   9. In the File Save dialog box, select OK.

 10. Leave the UDI Wizard Designer open for the next step.
