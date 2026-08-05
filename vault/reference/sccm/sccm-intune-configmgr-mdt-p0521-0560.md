---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 521-560"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0521-0560
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0521-0560
family: sccm
documentKind: "doc"
abstract: "Woodgrove Bank does not need to modify any views, as the LocationSettings view already returns all columns from the Settings table. However, Woodgrove Bank ran the sp_refreshview stored procedure to refresh the ComputerSettings, LocationSettings, MakeModelSettings, or RoleSettin"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 521-560

<!-- p.521 -->

        Woodgrove Bank does not need to modify any views, as the LocationSettings view
        already returns all columns from the Settings table. However, Woodgrove Bank ran
        the sp_refreshview stored procedure to refresh the ComputerSettings,
        LocationSettings, MakeModelSettings, or RoleSettings views, which reference the
        Settings table. This allows all the views to return the computer name of the
        antivirus server, if required.

Reference the New Column in the CustomSettings.ini File
After you have added the column to the table and modified the appropriate views,
configure the CustomSettings.ini file to reference the new column. To reference the new
column in the CustomSettings.ini file, perform the following steps:

   1. Add a reference to the query section on the Priority line in the CustomSettings.ini
        file, if required.

        This reference initiates the query defined in the query section that you will create
        in a later step. This step may not be necessary if CustomSettings.ini already has an
        existing query for the view or table referenced in the query.

   2. Add the new column name to the Properties line in the CustomSettings.ini file.

        This reference informs MDT to resolve the value for AVServer and create a task
        sequence variable of the same name. The task sequence variable can then be
        referenced in a task sequence step.

   3. Create a query section that was referenced in step 1, which queries the appropriate
        table or view.

        Example: How Woodgrove Bank Referenced the New Column in the
        CustomSettings.ini File

        Woodgrove Bank queries the LocationSettings view to return the antivirus server
        for a particular location. The LSettings query already exists in the
        CustomSettings.ini file after running the Configure DB Wizard. As shown in Listing
        16, all Woodgrove Bank needs to do is add AVServer to the Priority line so that
        MDT creates a task sequence variable of the same name.

        Listing 16. CustomSettings.ini File to Retrieve Antivirus Server for Woodgrove
        Bank

  ini

<!-- p.522 -->

  [Settings]
  Priority=LSettings, Default
  Properties=AVServer

  [Default]
  OSInstall=YES

  [LSettings]
  SQLServer=NYC-SQL-01
  Instance=SQLExpress
  Database=MDTDB
  Netlib=DBNMPNTW
  SQLShare=SQL$
  Table=LocationSettings
  Parameters=DefaultGateway

Reference the New Column in a Task Sequence Step
Now that the CustomSettings.ini file is modified to return the configuration settings
from the new column, you are ready to reference the new column in a task sequence
step. You reference the new column as a task sequence variable in the task sequence
step. The variable will have the same name as the column. For example, if you create a
column named Zip_Code, the task sequence variable will be named Zip_Code.

Example: How Woodgrove Bank Referenced the New Column in a Task Sequence Step

Woodgrove Bank creates a custom task sequence step to run the antivirus setup
program. As a part of the antivirus setup program, the antivirus server name can be
provided by using the -server parameter and referencing the new column name as a
task sequence variable (%AVSERVER%). The command line used to run the antivirus
setup program is:

avsetup.exe -server %AVSERVER%

Monitoring MDT Deployments
You can monitor MDT deployments using the monitoring feature supported by the MDT
scripts and the Deployment Workbench. The MDT deployment monitoring feature
allows you to view the MDT deployment process for LTI, ZTI, and UDI deployments. You
can view the deployment process in the Deployment Workbench or by using the Get-
MDTMonitorData cmdlet.

Monitor MDT deployments using the MDT monitoring features by performing the
following steps:

<!-- p.523 -->

   1. Enable monitoring of MDT deployments as described in Enable MDT Deployment
     Monitoring.

   2. View MDT deployment process as described in View MDT Deployment Progress.

Enable MDT Deployment Monitoring
Before you can monitor MDT deployments, you must enable MDT deployment
monitoring. The process for enabling MDT deployment monitoring is different for LTI
deployments and Configuration Manager-based deployments (including ZTI and UDI
deployments).

Enable MDT deployment monitoring by:

     Enabling MDT monitoring for LTI deployments as described in Enabling LTI
     Deployment Monitoring

     Enabling MDT monitoring for ZTI or UDI deployments as described in Enabling ZTI
     or UDI Deployment Monitoring

Enabling LTI Deployment Monitoring

Prior to deploying computers using LTI, enable monitoring of the LTI deployment
process. You enable monitoring on the Monitoring tab in the deployment share
properties dialog box.

To enable monitoring of the LTI deployment process

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

   3. In the details pane, select deployment_share (where deployment_share is the name
     of the deployment share where you want to enable monitoring).

   4. In the Actions pane, select Properties.

     The deployment_share Properties dialog box opens (where deployment_share is
     the name of the deployment share for which you want to enable monitoring).

   5. In the deployment_share Properties dialog box (where deployment_share is the
     name of the deployment share for which you want to enable monitoring), on the

<!-- p.524 -->

     Monitoring tab, select the Enable monitoring for this deployment share check
     box, and then select Apply.

   6. In the deployment_share Properties dialog box (where deployment_share is the
     name of the deployment share for which you want to enable monitoring), on the
     Rules tab, notice that the EventService property has been added to the
     CustomSettings.ini file, and then select OK.

   7. Close all open windows and dialog boxes.

Enabling ZTI or UDI Deployment Monitoring

Prior to deploying computers using ZTI or UDI, enable monitoring of theses deployment
process in the Deployment Workbench. You enable monitoring on the Monitoring tab in
the deployment share Properties dialog box just as you do for LTI deployments.

Then, copy the EventService property line on the Rules tab in the deployment share
Properties dialog box to the CustomSettings.ini file in the MDT files package in
Configuration Manager. Update the MDT files package on all distribution points.

To enable monitoring of the ZTI or UDI deployment processes

   1. Enable MDT monitoring for a deployment share using the Deployment Workbench
     as described in Enabling LTI Deployment Monitoring.

   2. Copy the EventService property line on the Rules tab in the deployment share
     Properties dialog box to the CustomSettings.ini file in the MDT files package in
     Configuration Manager.

     The following is an example of the EventService property line:

     EventService=https://WDG-MDT-01:9800

     For more information on customizing the MDT configuration files to include the
     EventService property line, see "Step 3-4: Customize the MDT Configuration Files
     for the Reference Computer" inQuick Start Guide for Microsoft System Center 2012
     R2 Configuration Manager for Configuration Manager environments.

   3. Update the MDT files package for distribution points so that the customized
     CustomSettings.ini file is available.

     For more information on updating the MDT files package for distribution points,
     see "Step 3-5: Update the Distribution Points for the Custom Settings Files

<!-- p.525 -->

     Package" in Quick Start Guide for Microsoft System Center 2012 R2 Configuration
     Manager for Configuration Manager environments.

View MDT Deployment Progress
You can view the MDT deployment progress using the Deployment Workbench or the
Get-MDTMonitorData cmdlet.

  ７ Note

  To view the MDT deployment progress, monitoring must be enabled as described
  in Enable MDT Deployment Monitoring.

To view the MDT deployment process, complete either of the following tasks:

   1. View the MDT deployment progress using the Deployment Workbench as
     described in Viewing the MDT Deployment Progress in the Deployment
     Workbench.

   2. View the MDT deployment progress using the Get-MDTMonitorData cmdlet as
     described in Viewing the MDT Deployment Progress Using the Get-
     MDTMonitorData Cmdlet.

Viewing the MDT Deployment Progress in the Deployment
Workbench
You view the MDT deployment process in the Monitoring node in the deployment
share. The progress of the LTI deployment process is displayed as a percentage of
completion.

  ７ Note

  The percentage of completion displayed in the Monitoring node is based on the
  percentage completion of the steps in the task sequence, not in overall time. For
  example, if a task sequence has completed 20 steps in task sequence that has a
  total of 50 steps, then the process will show 40% complete.

To view the LTI deployment process

<!-- p.526 -->

1. Select Start, and then point to All Programs. Point to Microsoft Deployment
  Toolkit, and then select Deployment Workbench.

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/deployment_share/Monitoring (where
  deployment_share is the name of the deployment share that you want to monitor)

3. In the details pane, view the deployment process for each computer being
  deployed.

4. In the Actions pane, periodically select Refresh.

  The status of the deployment process is updated in the details pane. Continue to
  monitor the deployment process till the process completes.

5. In the details pane, select target_computer (where target_computer is the name of
  the computer being monitored).

6. In the Actions pane, select Properties.

  The target_computer Properties dialog box is displayed (where target_computer is
  the name of the computer being monitored).

7. In the target_computer Properties dialog box (where target_computer is the name
  of the computer being monitored), on the Identity tab, view the monitoring
  information provided about the deployment process as described in Table 197.

  Table 197. Monitoring Information About the
  Deployment Process

                                                                             ﾉ   Expand table

   Information            Description

   ID                     Unique identifier for the computer being deployed.

   Computer Name          The name of the computer being deployed.

   Deployment status      The current status of the computer being deployed; can be one of
                          the following:

                          - Running. Indicates that the task sequence is healthy and running.

                          - Failed. Indicates that the task sequence failed and the
                          deployment process was unsuccessful.

<!-- p.527 -->

Information      Description

                 - Completed. Indicates that the task sequence has finished.

                 - Unresponsive. The task sequence has not updated its status in
                 the past four hours and is assumed to be nonresponsive.

Step             The current task sequence step being run.

Progress         The overall progress of the task sequence. The progress bar
                 indicates how many task sequence steps have been run out of the
                 total number of task sequence steps.

Start            Time the deployment process started.

End              Time the deployment process ended.

Elapsed          The length of time the deployment process has been running or
                 took to run if the deployment process has finished.

Error            The number of errors encountered during the deployment process.

Warnings         The number of warnings encountered during the deployment
                 process.

Remote Desktop   This button allows you to establish a remote desktop connection
                 with the computer being deployed using the Windows Remote
                 Desktop feature. This method assumes that:

                 - The target operating system is running and has remote desktop
                 support enabled

                 - mstsc.exe is in the path

                 This button is always visible but may not be able to establish a
                 remote desktop session if the monitored computer is running
                 Windows PE, has not completed installation of the target operating
                 system, or does not have the Remote Desktop feature enabled.

VM Connection    This button allows you to establish a remote desktop connection to
                 virtual machine running in Hyper-V. This method assumes that:

                 - The deployment is being performed to a VM running on Hyper-V

                 - vmconnect.exe is located in the %ProgramFiles%\Hyper-V folder

                 This button appears when ZTIGather.wsf detects that Hyper-V
                 integration components are running on the monitored computer.
                 Otherwise, this button will not be visible.

<!-- p.528 -->

      Information            Description

      DaRT Remote            This button allows you to establish a remote control session using
      Control                the remote viewer feature in the Diagnostics and Recovery Toolkit
                             (DaRT).

                             This method assumes that:

                             - DaRT has been deployed to the target computer and is currently
                             running

                             - DartRemoteViewer.exe is located in the
                             %ProgramFiles%\Microsoft DaRT 7\v7 folder

                             This button appears when ZTIGather.wsf detects that DaRT is
                             running on the monitored computer. Otherwise, this button will not
                             be visible.

      Automatically          Check box that controls whether the information in the dialog box
      refresh this           is automatically refreshed. If the check box is:
      information every 10
      seconds                a. Selected, the information is refreshed every 10 seconds

                             b. Cleared, the information is not automatically refreshed and must
                             be manually refreshed using the Refresh Now button

      Refresh Now            This button immediately refreshes the information displayed in the
                             dialog box.

  8. In the target_computer Properties dialog box (where target_computer is the name
     of the computer being monitored), select OK.

  9. Close the Deployment Workbench

Viewing the MDT Deployment Progress Using the Get-
MDTMonitorData Cmdlet

You can view the MDT deployment process using the Get-MDTMonitorData cmdlet.
This cmdlet is included in the MDT PowerShell microsoft.bdd.pssnapin snap-in, which is
included with MDT. To use this cmdlet, monitoring must be enabled as described in
Enable MDT Deployment Monitoring.

To view MDT deployment progress using the Get-MDTMonitorData
cmdlet

  1. Open a Windows PowerShell console.

<!-- p.529 -->

2. Add the MDT PowerShell snap-in by running the Add-PSSnapIn cmdlet as shown
  in the following example:

  Add-PSSnapIn Microsoft.BDD.PSSnapIn

3. Create a PowerShell drive that uses the MDT PowerShell provider by running the
  New-PSDrive cmdlet as shown in the following example:

  New-PSDrive -Name DS001 -PSProvider mdtprovider -Root d:\DeploymentShare$

4. View the MDT monitoring process by running the following command:

  Get-MDTMonitorData -Path DS001:

  This command returns the monitoring data collected by the MDT monitoring
  service running on the same computer that hosts the deployment share, as shown
  in the following example output:

  Name : WDG-REF-01

  PercentComplete : 100

  Settings :

  Warnings : 0

  Errors : 0

  DeploymentStatus : 3

  StartTime : 5/23/2012 6:45:39 PM

  EndTime : 5/23/2012 8:46:32 PM

  ID : 1

  UniqueID : 94a0830e-f2bb-421c-b1e0-6f86f9eb9fa1

  CurrentStep : 88

  TotalSteps : 88

  StepName :

  LastTime : 5/23/2012 8:46:32 PM

  DartIP :

<!-- p.530 -->

     DartPort :

     DartTicket :

     VMHost : XYL-DC-02

     VMName : WDG-REF-01

     ComputerIdentities : {}

     For more information about the monitoring data that the cmdlet returns, see Table
     197 in Viewing the MDT Deployment Progress in the Deployment Workbench.

   5. Close the Windows PowerShell console.

Supporting Windows RE and DaRT
MDT integrates with Windows RE and DaRT to provide enhanced support and
troubleshooting features. MDT support for Windows RE and DaRT is as follows:

     LTI supports Windows RE and DaRT in LTI boot images and on the recovery
     partition on the target computer as described in Supporting Windows RE and
     DaRT in LTI.

     ZTI and UDI support DaRT in boot images as described in Supporting DaRT in ZTI
     and UDI Boot Images.

Supporting Windows RE and DaRT in LTI
MDT supports the ability to deploy Windows RE partitions to computers. In addition, if
your organization is licensed for the Microsoft Desktop Optimization Package (MDOP),
you can include DaRT in the Windows RE partitions.

  ７ Note

  MDT does not support Windows RE in Windows 7 when using the Windows ADK.

Provide support for Windows RE and DaRT by performing the
following steps:

   1. Enable Windows RE support on target computers by installing the MDT-enabled
     boot image to the target computer as described in Enable Windows RE Support in

<!-- p.531 -->

     LTI.

   2. Enable DaRT support on target computers by installing DaRT along with Windows
     RE as described in Enable DaRT Support in LTI.

   3. Customize the DaRT configuration when DaRT is integrated with LTI as described in
     Customize DaRT When Integrated with LTI.

Enable Windows RE Support in LTI
Windows RE helps users troubleshoot and recover from startup-related problems on
their computers. When a deployment share is updated, Deployment Workbench
automatically generates .iso and .wim files that contain Windows RE support.

  ７ Note

  You must import the entire Windows 7 installation files to a deployment share to
  support Windows RE. Otherwise, Windows 7 is installed without Windows RE
  support.

While running the LTI task sequence, the Add Windows Recovery (WinRE) task
sequence step is responsible for:

     Installing the appropriate .wim image to the active partition

     Modifying the BCD file so that a user can choose to start Windows RE by pressing
     F8 as Windows is starting.

     The Add Windows Recovery (WinRE) task sequence step runs when the
     PrepareWinRE property is set to a value of YES. For more information about the
     PrepareWinRE property, see the "PrepareWinRE" property in the MDT document
     Toolkit Reference.

Enable DaRT Support in LTI
DaRT is included as a part of the Microsoft Desktop Optimization Package, which is
provided as a part of Microsoft Software Assurance. You can include DaRT in the
Windows RE partitions.

The following is a summary of the DaRT features:

     Includes 14 administrative, system, and network tools.

<!-- p.532 -->

     Provides many options for recovery, even when Windows Safe mode or normal
     startup will not function

     Provides an easy-to-use, offline boot environment that helps IT teams quickly
     restart computers

     Helps recover deleted files and reset lost or forgotten local passwords, even the
     administrator's

     Enable DaRT support in LTI for:

     DaRT version 7 (used with Windows 7) as described in Enable DaRT 7 Support in LTI

     DaRT version 8 (used with Windows 8) as described in Enable DaRT 8 Support in LTI

Enable DaRT 7 Support in LTI

DaRT version 7 is for use with Windows 7. For information on how to enable DaRT
version 8 for use with Windows 8, see Enable DaRT 8 Support in LTI.

To enable DaRT 7 support in LTI

   1. Perform an administrative installation of DaRT on the computer running the
     Deployment Workbench.

     By default, if you do a traditional installation of DaRT, the processor architecture of
     DaRT is the same as the processor architecture of the operating system where you
     installed DaRT. For example, if you install DaRT on a 64-bit operating system, you
     will have a 64-bit version of DaRT.

     Performing an administrative installation allows you to install both 32-bit and 64-
     bit versions of DaRT. With an administrative installation the folder structures for
     both processor architectures are created, but none of the shortcuts are created.

     Perform an administrative installation of DaRT by running the following command
     from a command prompt:

     msiexec.exe /a MSDart70.msi

   2. Copy the 32-bit version of Tools.cab file from the DaRT administrative installation
     to the Tools\x86 folder in a deployment share.

   3. Copy the 64-bit version of Tools.cab file from the DaRT administrative installation
     to the Tools\x64 folder in a deployment share.

<!-- p.533 -->

  4. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  5. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares

  6. In the details pane, select deployment_share (where deployment_share is the name
     of the deployment share for which you want to enable DaRT support).

  7. In the Actions pane, select Properties.

     The deployment_share Properties dialog box appears (where deployment_share is
     the name of the deployment share for which you want to enable DaRT support).

  8. In the deployment_share Properties dialog box, on the Windows PE tab, select
     platform (where deployment_share is the name of the deployment share for which
     you want to enable DaRT support and platform is the processor architecture
     platform for which you want to enable DaRT support), select the Microsoft
     Diagnostics and Recovery Toolkit (DaRT) check box, and then select OK.

  9. Update the deployment share.

     As a part of updating the deployment share, the DaRT files are integrated with the
     Lite Touch Windows PE .wim files, which automatically include Windows RE. When
     the .wim files are installed on the target computer, DaRT support will automatically
     be included.

       ７ Note

       For more information about updating a deployment share see Update a
       Deployment Share in the Deployment Workbench.

 10. Close all open windows and dialog boxes.

Enable DaRT 8 Support in LTI

DaRT version 8 is for use with Windows 8. For information on how to enable DaRT 7 for
use with Windows 7, see Enable DaRT 7 Support in LTI.

To enable DaRT 8 support in LTI

  1. Perform an administrative installation of DaRT on the computer running the
     Deployment Workbench.

<!-- p.534 -->

  By default, if you perform a traditional installation of DaRT, the processor
  architecture of DaRT is the same as the processor architecture of the operating
  system on which you installed DaRT. For example, if you install DaRT on a 64-bit
  operating system, you will have a 64-bit version of DaRT.

  Performing an administrative installation allows you to install both 32-bit and 64-
  bit versions of DaRT. With an administrative installation, the folder structures for
  both processor architectures are created, but none of the shortcuts are created.

  Perform an administrative installation of DaRT by running the following command
  from a command prompt:

  msiexec.exe /a MSDart80.msi

2. If the computer on which you installed MDT is running Windows 8, you can
  proceed to step 5.

  MDT automatically performs the following two steps if you install DaRT 8 on the
  computer running Windows 8 and MDT.

3. Copy the Toolsx86.cab file from the DaRT administrative installation to the
  Tools\x86 folder in a deployment share.

     Tip

    By default, the administrative installation of DaRT installs the Toolsx86.cab file
    in C:\Program Files\Microsoft DaRT 8\v8.

4. Copy the Toolsx64.cab file from the DaRT administrative installation to the
  Tools\x64 folder in a deployment share.

     Tip

    By default, the administrative installation of DaRT installs the Toolsx64.cab file
    in C:\Program Files\Microsoft DaRT 8\v8.

5. Select Start, and then point to All Programs. Point to Microsoft Deployment
  Toolkit, and then select Deployment Workbench.

6. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares.

<!-- p.535 -->

   7. In the details pane, select deployment_share (where deployment_share is the name
     of the deployment share for which you want to enable DaRT support).

   8. In the Actions pane, select Properties.

     The deployment_share Properties dialog box appears (where deployment_share is
     the name of the deployment share for which you want to enable DaRT support).

   9. In the deployment_share Properties dialog box, on the Windows PE tab, select
     platform (where deployment_share is the name of the deployment share for which
     you want to enable DaRT support and platform is the processor architecture
     platform for which you want to enable DaRT support). Select the Microsoft
     Diagnostics and Recovery Toolkit 8 (DaRT 8) check box, and then select OK.

 10. Update the deployment share.

     As a part of updating the deployment share, the DaRT files are integrated with the
     Lite Touch Windows PE .wim files, which automatically include Windows RE. When
     the .wim files are installed on the target computer, DaRT support will automatically
     be included.

       ７ Note

       For more information about updating a deployment share see Update a
       Deployment Share in the Deployment Workbench.

 11. Close all open windows and dialog boxes.

Customize DaRT When Integrated with LTI

You can customize DaRT, and then save the customizations in LTI so that the deployed
partitions that include DaRT are configured consistently. You can do this by creating a
new DaRT recovery image that includes the configuration settings you desire, then
copying the DartConfig.dat file from the newly configured DaRT recovery image to an
LTI deployment share.

To customize DaRT when integrated with LTI

   1. Install DaRT on the computer where you installed MDT.

   2. Create a new DaRT recovery image using the DaRT Recovery Image Wizard.

<!-- p.536 -->

     While running the DaRT Recovery Image Wizard, make the configuration settings
     that you wish to have applied to your environment. Select to save the DaRT
     recovery image as an .iso file.

     For more information about how to create a new DaRT recovery image for:

           DaRT 7, see How to create & test Diagnostics & Recovery Toolkit (DaRT 7)
           Recovery Image-Part I.

           DaRT 8, see the section, "Create the DaRT 8 Recovery Image," in the Microsoft
           Diagnostics and Recovery Toolset Administrator's Guide, which is included with
           DaRT 8.

   3. Extract the DartConfig.dat file from the .iso file created in the previous step.

   4. Copy the DartConfig.dat file extracted in the previous step into the
     installation_folder\Templates folder (where installation_folder is the folder where
     you installed MDT) on the computer where you installed MDT.

   5. Update the deployment share in the Deployment Workbench to create a LTI boot
     image that includes the customized DartConfig.dat file.

     For more information about updating a deployment share, see Update a
     Deployment Share in the Deployment Workbench.

Supporting DaRT in ZTI and UDI Boot Images
MDT supports DaRT version 7 (for Windows 7) and DaRT version 8 (for Windows 8) in
ZTI and UDI boot images. This support makes DaRT features available when the ZTI or
UDI boot images are running on the target computers.

After a ZTI or UDI boot image is enabled for DaRT, the Use Toolkit Package task
sequence step will recognize that the DaRT remote control files are present and will
automatically start the DaRT remote control agent. The DaRT remote control agent
provides remote control of the target computer during the deployment process, which
helps troubleshoot deployment problems.

Enable DaRT support in ZTI and UDI boot images for:

     DaRT version 7 (used with Windows 7) as described in Enable DaRT 7 Support in
     ZTI and UDI Boot Images.

     DaRT version 8 (used with Windows 8) as described in Enable DaRT 8 Support in
     ZTI and UDI Boot Images.

<!-- p.537 -->

Enable DaRT 7 Support in ZTI and UDI Boot Images
DaRT version 7 is for use with Windows 7. For information on how to enable DaRT
version 8 for use with Windows 8, see Enable DaRT 8 Support in ZTI and UDI Boot
Images.

To enable DaRT 7 support in ZTI and UDI Boot Images

  1. Perform an administrative installation of DaRT on the computer running the
     Deployment Workbench.

     By default, if you do a traditional installation of DaRT, the processor architecture of
     DaRT is the same as the processor architecture of the operating system where you
     installed DaRT. For example, if you install DaRT on a 64-bit operating system, you
     will have a 64-bit version of DaRT.

     Performing an administrative installation allows you to install both 32-bit and 64-
     bit versions of DaRT. With an administrative installation the folder structures for
     both processor architectures are created, but none of the shortcuts are created.

     Perform an administrative installation of DaRT by running the following command
     from a command prompt:

     msiexec.exe /a MSDart70.msi

  2. Copy the 32-bit version of Tools.cab file from the DaRT administrative installation
     to the installation_folder\Templates\Distribution\Tools\x86 folder (where
     installation_folder is the folder where you installed MDT).

  3. Copy the 64-bit version of Tools.cab file from the DaRT administrative installation
     to the installation_folder\Templates\Distribution\Tools\x64 folder (where
     installation_folder is the folder where you installed MDT).

  4. Run the Create Boot Image using MDT wizard to generate the boot image.

     While running the Create Boot Image using MDT wizard, on the General Settings:
     Components wizard page, select the Microsoft Diagnostics and Recovery Toolkit
     (DaRT) check box.

     For information about how to run the Create Boot Image using MDT wizard for
     Configuration Manager, see Creating ZTI Boot Images in Configuration Manager

  5. Close all open windows and dialog boxes.

<!-- p.538 -->

Enable DaRT 8 Support in ZTI and UDI Boot Images
DaRT version 8 is for use with Windows 8. For information on how to enable DaRT 7 for
use with Windows 7, see Enable DaRT 7 Support in ZTI and UDI Boot Images.

You enable DaRT support based on the operating system running on the computer on
which you installed MDT. DaRT 8 can only be installed on Windows 8. If you install MDT
on a computer running:

     Windows 8, then install DaRT on the same computer, and MDT will automatically
     copy the necessary files to support DaRT 8 as described in Enable DaRT 8 Support
     in ZTI and UDI Boot Images for Windows 8 Operating Systems.

     Operating systems prior to Windows 8, then perform an administrative installation
     on a computer running Windows 8, and then copy the Toolsx86.cab and
     Toolsx64.cab files to the computer running MDT as described in Enable DaRT 8
     Support in ZTI and UDI Boot Images for Operating Systems Prior to Windows 8.

Enable DaRT 8 Support in ZTI and UDI Boot Images for Windows 8
Operating Systems

Enabling DaRT 8 support in ZTI and UDI boot images for Windows 8 Operating Systems
requires the installation of DaRT 8 on the computer on which you installed MDT. After
DaRT 8 is installed, the Deployment Workbench in MDT automatically copies the
necessary DaRT 8 files to the appropriate locations.

To enable DaRT 8 support in ZTI and UDI boot images for Windows 8
operating systems

   1. Install DaRT on the computer running MDT.

     Install DaRT by running the following command from a command prompt:

     msiexec.exe /i MSDart80.msi

   2. Start the Deployment Workbench.

     When the Deployment Workbench starts, MDT copies the necessary DaRT files to
     the MDT installation. The Deployment workbench copies the:

           Toolsx86.cab file from the DaRT installation to the
           installation_folder\Templates\Distribution\Tools\x86 folder (where
           installation_folder is the folder where you installed MDT).

<!-- p.539 -->

            Toolsx64.cab file from the DaRT installation to the
            installation_folder\Templates\Distribution\Tools\x64 folder (where
            installation_folder is the folder where you installed MDT).

   3. Run the Create Boot Image Using the MDT Wizard to generate the boot image.

       While running the Create Boot Image Using MDT Wizard, on the General Settings:
       Components wizard page, select the Microsoft Diagnostics and Recovery Toolkit
       8 (DaRT 8) check box.

       For information about how to run the Create Boot Image Using MDT Wizard for
       Configuration Manager, see Creating ZTI Boot Images in Configuration Manager

   4. Close all open windows and dialog boxes.

Enable DaRT 8 Support in ZTI and UDI Boot Images for Operating
Systems Prior to Windows 8

Enabling DaRT 8 support in ZTI and UDI boot images for operating systems prior to
Windows 8 requires an administrative installation of DaRT 8 on a computer running an
operating system prior to Windows 8. After DaRT 8 is installed, you will need to
manually copy the DaRT 8 files to the appropriate locations on the computer running
MDT.

To enable DaRT 8 support in ZTI and UDI boot images for operating
systems prior to Windows 8

   1. Perform an administrative installation of DaRT on the computer running the
       Deployment Workbench.

       By default, if you perform a traditional installation of DaRT, the processor
       architecture of DaRT is the same as the processor architecture of the operating
       system on which you installed DaRT. For example, if you install DaRT on a 64-bit
       operating system, you will have a 64-bit version of DaRT.

       Performing an administrative installation allows you to install both 32-bit and 64-
       bit versions of DaRT. With an administrative installation the folder structures for
       both processor architectures are created, but none of the shortcuts are created.

       Perform an administrative installation of DaRT by running the following command
       from a command prompt:

       msiexec.exe /a MSDart80.msi

<!-- p.540 -->

   2. Copy the Toolsx86.cab file from the DaRT administrative installation to the
     installation_folder\Templates\Distribution\Tools\x86 folder (where
     installation_folder is the folder where you installed MDT).

        Tip

       By default the administrative installation of DaRT installs the Toolsx86.cab file
       in C:\Program Files\Microsoft DaRT 8\v8.

   3. Copy the Toolsx64.cab file from the DaRT administrative installation to the
     installation_folder\Templates\Distribution\Tools\x64 folder (where
     installation_folder is the folder where you installed MDT).

        Tip

       By default the administrative installation of DaRT installs the Toolsx64.cab file
       in C:\Program Files\Microsoft DaRT 8\v8.

   4. Run the Create Boot Image using MDT wizard to generate the boot image.

     While running the Create Boot Image using MDT wizard, on the General Settings:
     Components wizard page, select the Microsoft Diagnostics and Recovery Toolkit
     8 (DaRT 8) check box.

     For information about how to run the Create Boot Image using MDT wizard for
     Configuration Manager, see Creating ZTI Boot Images in Configuration Manager

   5. Close all open windows and dialog boxes.

Preparing the MDT Migration Resources
During deployment to the target computers, deployment scripts connect to the
deployment shares and shared folders. Create accounts for the scripts to use when
accessing these resources.

Prepare the MDT migration resources by:

     Creating additional shared folders as described in Creating Additional Shared
     Folders

     Configuring shared folder permissions as described in Configuring Shared Folder
     Permissions

<!-- p.541 -->

        Configuring access to other resources as described in Configuring Access to Other
        Resources

Creating Additional Shared Folders
Before starting the deployment, create additional shared folders in which to store the
user state migration data and the deployment logs. Table 198 lists the shared folders
that must be created and describes the purpose of each.

Table 198. Shared Folders and Their Descriptions

                                                                                  ﾉ   Expand table

 Shared          Description
 folder

 MigData         Stores the user state migration data during the LTI deployment process.

 Logs            Stores the deployment logs during the LTI or ZTI deployment process. This folder is
                 optional for either deployment.

  ７ Note

  The files in Table 198 are recommended shared folder names. Use any name for
  these shared folders. However, the remainder of the deployment process refers to
  these shared folders by these names.

Configuring Shared Folder Permissions
After creating additional shared folders listed in Table 198, configure the appropriate
shared folder permissions. Ensure that unauthorized users are unable to access user
state migration information and the deployment logs. Only the target computer
creating the user state migration information and the deployment logs should have
access to these folders.

To configure the shared folder permissions for the folders listed in
Table 198

   1. In Windows Explorer, right-click shared_folder (where shared_folder is one of the
        shared folders listed in Table 198), and then select Properties.

<!-- p.542 -->

 2. On the Security tab, select Advanced.

 3. On the Permissions tab, clear the Allow inheritable permissions from the parent
   to propagate to this object and all child objects check box.

 4. In the Security dialog box, select Remove.

 5. On the Permissions tab, select Add.

 6. In the Enter the object name to select box, type Authenticated Users, and then
   select OK.

 7. In the Permission Entry for shared_folder dialog box (where shared_folder is one of
   the shared folders listed in Table 198), in the Apply onto list, select This folder
   only.

 8. In the Permission Entry for shared_folder dialog box (where shared_folder is one of
   the shared folders listed in Table 198), in the Permissions list, select Allow for the
   Create Folders/Append Data permission, and then select OK.

 9. On the Permissions tab, select Add.

10. In the Enter the object name to select box, type CREATOR OWNER, and then
   select OK.

   This action allows domain computers and domain users to access the subfolders
   they create.

11. In the Permission Entry for shared_folder dialog box (where shared_folder is one of
   the shared folders listed in Table 198), in the Apply onto list, select Subfolders and
   files only.

12. In the Permission Entry for shared_folder dialog box (where shared_folder is one of
   the shared folders listed in Table 198), in the Permissions list, select Allow for the
   Full Control permission, and then select OK.

13. Repeat steps 10-13 for each group that will receive Administrator privileges.

   The permissions set in these steps work for both LTI and ZTI deployments. In some
   instances, you may want to further restrict the user accounts that can access the
   shared folder. You can restrict user accounts for:

   LTI deployments by substituting Authenticated Users in the steps above with each
   account you want to have access

<!-- p.543 -->

     ZTI deployments by substituting Authenticated Users in the steps above with a
     network access account in Configuration Manager

Configuring Access to Other Resources
In addition to the shared folders just created, the MDT scripts might require access to
other resources. The resources include application or database servers (such as
Microsoft SQL Server or Microsoft Exchange Server).

Access is granted to the credentials specified in the:

     UserID, UserPassword, and UserDomain properties for LTI deployments

     Deployment Wizard for LTI deployments

     Network access account used by the Configuration Manager client for ZTI
     deployments

     Grant access to the following resources:

     MDT deployment share for LTI deployments. Configure access to the deployment
     share created in the Deployment Workbench.

     Any resources accessed using the ZTIConnect.wsf script for LTI or ZTI
     deployments. Configure access to resources that are referenced using the
     ZTIConnect.wsf script.

        ７ Note

        For further guidance on using the ZTIConnect.wsf script, see the MDT
        document Microsoft Deployment Toolkit Samples Guide.

     Any resources on application or database servers for LTI or ZTI deployments.
     Configure access to applications or databases that are accessed through the
     SQLServer, SQLShare, and Database properties.

        ７ Note

        Other connections to the same servers, such as Named Pipes and RPC, use the
        same credentials listed above. Use the ZTIConnect.wsf script to establish these
        connections.

<!-- p.544 -->

Preparing Windows Deployment Services
You can use Windows Deployment Services in conjunction with MDT to automatically
initiate boot images on target computers. These boot images can be Windows PE
images or custom images that can deploy operating systems directly to the target
computers.

Prepare Windows Deployment Services for use with MDT by:

     Preparing Windows Deployment Services for use in LTI deployments as described
     in Preparing Windows Deployment Services for LTI Deployments

     Preparing Windows Deployment Services for use in ZTI deployments using
     Configuration Manager as described in Preparing Windows Deployment Services
     for ZTI Deployments Using Configuration Manager

     Preparing Windows Deployment Services for use in UDI deployments as described
     in Preparing Windows Deployment Services for UDI Deployments

Preparing Windows Deployment Services for LTI
Deployments
You can use Windows Deployment Services in LTI deployments in the following ways:

     Start Windows PE on the target computers. The beginning of the New Computer
     deployment scenario and the second half of the Replace Computer deployment
     scenario both start the target computer in Windows PE. For these scenarios, you
     can automate starting Windows PE using Windows Deployment Services.

     Install images created in the Deployment Workbench on the target computers.
     You can create custom WIM images in the Deployment Workbench that you can
     deploy directly to target computers using Windows Deployment Services.

     For more information about setting up and configuring Windows Deployment
     Services, see:

     Windows Deployment Services

     The Windows Deployment Services Help file, included in Windows Deployment
     Services

     Prepare Windows Deployment Services for LTI deployments by:

<!-- p.545 -->

     Adding boot images created in the Deployment Workbench for LTI deployments to
     Windows Deployment Services as described in Add LTI Boot Images to Windows
     Deployment Services

     Pre-staging target computers in Windows Deployment Services for LTI
     deployments as described in Pre-stage Target Computers for Windows
     Deployment Services for LTI Deployments

     Enabling Windows Deployment Services multicast deployment of images in
     Windows Deployment Services for LTI deployments as described in Enable
     Windows Deployment Services Multicast Deployment for LTI Deployments

Add LTI Boot Images to Windows Deployment Services

You can add the LTI boot image WIM files in the Boot folder of a deployment share to
Windows Deployment Services. Doing so allows Windows Deployment Services to
automatically initiate LTI deployment by starting LTI boot images.

  ７ Note

  Add the LTI boot images only to Windows Deployment Services. You do not need
  to add operating system images from the Deployment Workbench.

You can add LTI boot images to Windows Deployment Services using the Windows
Deployment Services management console or the WDSUTIL.exe tool.

For more information about adding an LTI boot image to Windows Deployment
Services, see:

     "Add an Image," in Windows Deployment Services Help, which is included in
     Windows Deployment Services

     Windows Deployment Services Getting Started Guide

Pre-stage Target Computers for Windows Deployment Services for
LTI Deployments

You can pre-stage PXE client computers in AD DS domains. When target computers are
pre-staged, the computer accounts exist in AD DS domains (also called known
computers). Target computers that are not pre-staged do not have computer accounts in
AD DS domains (also called unknown computers).

<!-- p.546 -->

  ７ Note

  Responding to unknown computers is the preferred method for LTI deployments,
  because it is the simplest method. If you pre-stage the target computers, LTI is
  unable to use the pre-staged computer account. Only Windows Deployment
  Services can use the pre-staged computer accounts.

You can configure Windows Deployment Services to respond to computers that are
known or unknown. Depending on the Windows Deployment Services configuration,
you may need to pre-stage the target computers. Doing so authorizes Windows
Deployment Services to deploy operating system images to the target computer.

  ７ Note

  If Windows Deployment Services is configured to respond to any computer (known
  or unknown), pre-staging the target computers is not necessary. LTI will not use a
  pre-staged computer account when joining the domain. Instead, LTI uses the
  computer name and credentials configured in the task sequence or through the
  rules process.

To pre-stage the target computers for Windows Deployment Services

  1. Select Start, point to Administrative Tools, and then select Active Directory Users
     and Computers.

  2. In the console tree, right-click organizational_unit (where organizational_unit is
     the name of the OU that will contain the target computer), point to New, and then
     select Computer.

  3. In the New Object - Computer dialog box, in the Computer name box, type
     computer_name (where computer_name is the name of the target computer), and
     then select Next.

  4. In the Managed dialog box, select the This is a managed computer check box. In
     the Computer's unique ID (GUID/UUID) box, type guid_uuid (where guid_uuid is
     the GUID/UUID of the computer), and then select Next.

  5. In the Host server dialog box, select one of the following options, and then select
     Next:

<!-- p.547 -->

           Any available remote installation server. This option specifies that this
           computer can be serviced by any Windows Deployment Services server.

           The following remote installation server. This option designates a specific
           server to service the computer. Specify the FQDN of the server running
           Windows Deployment Services.

   6. In the New Object - Computer dialog box, review the information displayed, and
     then select Finish.

   7. Close all open windows.

Enable Windows Deployment Services Multicast Deployment for
LTI Deployments

Multicast deployment of LTI operating systems using Windows Deployment Services
allows multiple computers to receive a single copy of an image, which reduces the
amount of network traffic required when multiple computers need to receive the same
image. By default, multicasting support is disabled in MDT.

For LTI deployments, the Deployment Workbench creates a multicast namespace for the
deployment share. The images are transferred to the target computers using multicast
from the deployment share, not from a Windows Deployment Services share.

  ７ Note

  MDT supports only the multicast transfer of images stored in the LTI$ distribution
  share. Images stored in Windows Deployment Services cannot be deployed using
  multicast transfer.

The multicast types available for use in LTI deployments include:

     Auto-Cast. In this option, as soon as an applicable client computer requests an
     installation image, a multicast transmission of the selected image begins. Then, as
     other client computers request the same image, they are joined to the
     transmission that has already started.

     Scheduled-Cast. This option sets the start criteria for the transmission based on
     the number of client computers requesting an image or a specific day and time.

     MDT supports multicast-based deployments when MDT and the deployment share
     are installed on:

<!-- p.548 -->

     The computer running Windows Deployment Services. In this scenario, MDT is
     installed on a computer running Windows Server with the Windows Deployment
     Services role as described in Enable Multicast Deployments with MDT Installed on
     the Same Computer as Windows Deployment Services.

     A computer other than the computer Windows Deployment Services is running
     on. In this scenario, MDT and the deployment share are installed on a separate
     computer from the one running Windows Server with the Windows Deployment
     Services role as described in Enable Multicast Deployments with MDT Installed on
     a Different Computer from Windows Deployment Services.

       ７ Note

       If MDT is installed on a separate computer, you must install the Remote Server
       Administration Tools feature so that the WDSUTIL command-line utility is
       available.

  ７ Note

  You cannot use these scenarios to allow multicast for boot images, as the multicast
  client is not loaded until after Windows PE is running. LTI only uses multicast to
  transfer operating system WIM files.

Enable Multicast Deployments with MDT Installed on the Same
Computer as Windows Deployment Services

In this scenario, MDT is installed on a computer running Windows Server with the
Windows Deployment Services server role. In this scenario, MDT can automatically
configure Windows Deployment Services to support multicast deployments.

To enable multicast deployments with MDT installed on the same
computer as Windows Deployment Services

   1. Install Windows Server on the computer that is to be the deployment server.

   2. Install the Windows Deployment Services server role on the computer that is to be
     the deployment server.

   3. Install Windows ADK for Windows 8.1 on the computer that is to be the
     deployment server.

<!-- p.549 -->

  4. Install MDT on the computer that is to be the deployment server.

  5. Start the Deployment Workbench.

  6. In the Deployment Workbench console tree, select Deployment Shares.

  7. In the details pane, right-click deployment_share (where deployment_share is the
     name of an existing deployment share for which multicast deployments will be
     enabled), and then select Properties.

  8. In the deployment_share Properties dialog box (where deployment_share is the
     name of an existing deployment share), on the General tab, select the Enable
     multicast for this deployment share check box, and then select OK.

       ７ Note

       The Network (UNC) path and Local Path text boxes on the General tab must
       contain valid paths for multicasting to function properly.

  9. In the Actions pane, select Update Deployment Share.

     When completed, the Deployment Workbench creates an Auto-Cast Windows
     Deployment Services multicast transmission from the deployment share.

Enable Multicast Deployments with MDT Installed on a Different
Computer from Windows Deployment Services

In this scenario, Windows Deployment Services and Windows Server are all installed on
the computer acting as the deployment server, but MDT is installed on another
computer. In this configuration, remotely run the WDSUTIL command on the computer
running Windows Deployment Services and Windows Server.

To enable multicast deployments with MDT Installed on a different
computer than Windows Deployment Services

  1. Install Windows Server on the computer hosting the deployment share.

  2. Install the Windows Deployment Services server role on the computer hosting the
     deployment share.

  3. Install Windows ADK for Windows 8.1 on a computer other than the computer
     hosting the deployment share.

  4. Install MDT on the same computer as in step 3.

<!-- p.550 -->

   5. On the computer hosting the deployment share, in a Command Prompt window,
     type the following command, and then press ENTER (where remote_server is the
     name of the computer running Windows Server with the Windows Deployment
     Services server role and deploy_share_path is the fully qualified path to the root of
     the deployment share).

      wdsutil.exe /new-namespace /friendlyname:"BDD Share Deploy$"
     /server:remote_server /namespace:"Deploy$" /contentprovider:WDS

     /configstring:"deploy_share_path" /namespacetype:AutoCast

     When completed, the WDSUTIL tool creates an Auto-Cast Windows Deployment
     Services multicast transmission from the deployment share.

Preparing Windows Deployment Services for ZTI
Deployments Using Configuration Manager
For ZTI deployments using Configuration Manager, configure a Configuration Manager
PXE service point on the computer on which Windows Deployment Services is installed.
Doing so allows Configuration Manager to directly service PXE boot requests received
by Windows Deployment Services as a PXE service point, which in turn allows target
computers to boot images that Configuration Manager manages using PXE. The PXE
service point is a feature of the distribution point site system role, which means that you
will configure the computer running Windows Deployment Services as a distribution
point site system role.

For more information about preparing Windows Deployment Services for ZTI
deployments using Configuration Manager, see:

     "How to Deploy Operating Systems by Using PXE in Configuration Manager" in the
     Configuration Manager Documentation Library, included with Configuration
     Manager

     "Configuring Distribution Points to Accept PXE Requests" in the Configuration
     Manager Documentation Library, included with Configuration Manager

  ７ Note

  In addition to the methods described here, you can use traditional Windows
  Deployment Services methods for responding to PXE boot requests. For more
  information, see the Windows Deployment Services Help file included with
  Windows Deployment Services.

<!-- p.551 -->

Preparing Windows Deployment Services for UDI
Deployments
Prepare Windows Deployment Services for UDI deployments using the same process for
ZTI deployments as described in Preparing Windows Deployment Services for ZTI
Deployments Using Configuration Manager.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.552 -->

Microsoft Deployment Toolkit Samples
Guide
Article • 02/12/2024

This guide is part of Microsoft Deployment Toolkit (MDT) and guides a specialist team
through deploying Windows operating systems and Microsoft Office. Specifically, this
guide is designed to provide sample configuration settings for specific deployment
scenarios.

  ７ Note

  In this article, Windows applies to the Windows 8.1, Windows 8, Windows 7,
  Windows Server 2012 R2, Windows Server 2012, and Windows Server 2008 R2
  operating systems unless otherwise noted. MDT does not support ARM processor-
  based versions of Windows. Similarly, MDT refers to the current version of MDT
  unless otherwise stated.

To use this guide

Review the list of scenario topics in the Table of Contents.

   1. Select the scenario that most closely represents your organization's deployment
      goals.

   2. Review the sample configuration settings for the selected scenario.

   3. Use the sample configuration settings as the foundation for the configuration
      settings in your environment.

   4. Customize the sample configuration settings for your environment.

      In many instances, more than one scenario might be necessary to complete the
      configuration settings for the environment.

      Because this guide contains only sample configuration settings, reviewing the
      guides listed in the following table can further assist in customizing the
      configuration settings for the environment.

                                                                           ﾉ   Expand table

<!-- p.553 -->

      Guide                         This guide offers assistance to help

      Quick Start Guide for         Use System Center 2012 R2 Configuration Manager to install
      Microsoft System Center       the Windows 8.1 operating system in a New Computer
      2012 R2 Configuration         deployment scenario.
      Manager

      Quick Start Guide for Lite    Install the Windows 8.1 operating system through Lite Touch
      Touch Installation            Installation (LTI) using bootable media in a New Computer
                                    deployment scenario.

      Quick Start Guide for User-   Install the Windows 8.1 operating system with User-Driven
      Driven Installation           Installation and System Center 2012 R2 Configuration
                                    Manager in a New Computer deployment scenario.

      Using the Microsoft           Further customize the configuration files used in Zero Touch
      Deployment Toolkit            Installation (ZTI) and LTI deployments. This guide also
                                    provides generic configuration guidance and a technical
                                    reference for configuration settings.

Deploying Windows 8 Applications Using MDT
MDT can deploy Windows 8 application packages, which have an .appx file extension.
These application packages are new to Windows 8. For more information on these
applications, see Windows Store App development.

Deploy Windows 8 applications using MDT by performing the following steps:

     Deploy Windows 8 applications using LTI as described in Deploying Windows 8
     Applications Using LTI.

     Deploy Windows 8 applications using User-Driven Installation (UDI) as described in
     Deploying Windows 8 Applications Using UDI.

Deploying Windows 8 Applications Using LTI
You can deploy Windows 8 applications using LTI like any other application that initiates
the installation process from a command line. You can add Windows 8 applications to
LTI deployments in the Applications node in the Deployment Workbench.

To deploy a Windows 8 application using LTI

   1. Create a network shared folder in which to store the application.

   2. Copy the Windows 8 application into the network shared folder that you created in
     the previous step.

<!-- p.554 -->

     Ensure that you copy the Windows 8 application .appx file and any other required
     files, such as a .cer file that contains the application certificate.

  3. Create an LTI application item for the Windows 8 application in the Applications
     node in the Deployment Workbench using the New Application Wizard.

     While completing the New Application Wizard, on the Command Details wizard
     page, in Command line, type app_file_name (where app_file_name is the name of
     the Windows 8 application).

     For more information about how to complete the New Application Wizard in the
     Deployment Workbench, see the following sections in the MDT document, Using
     the Microsoft Deployment Toolkit:

            "Create a New Application That Is Deployed from the Deployment Share"

            "Create a New Application That Is Deployed from Another Network Shared
            Folder"

  4. Select the LTI application item created in the previous step in an LTI task sequence.

Deploying Windows 8 Applications Using UDI
You can deploy Windows 8 applications using UDI like any other application that
initiates the installation process from a command line. You can add Windows 8
applications to UDI deployments on the ApplicationPage wizard page in the UDI Wizard
Designer.

  ７ Note

  Deployment of Windows 8 and Windows 8 applications using UDI requires System
  Center 2012 R2 Configuration Manager.

To deploy a Windows 8 application using UDI

  1. Create a network shared folder in which to store the application.

     This folder will be the source folder for the Configuration Manager application that
     you will create later in the process.

  2. Copy the Windows 8 application into the network shared folder that you created in
     the previous step.

<!-- p.555 -->

  Ensure that you copy the Windows 8 application .appx file and any other required
  files, such as a .cer file that contains the application certificate.

3. Add the Windows 8 application as a Configuration Manager application

4. Create a Configuration Manager application item for the Windows 8 application
  using the Create Application Wizard in the Configuration Manager console.

  While completing the Create Application Wizard, create a deployment type to
  deploy the Windows 8 application using the Create Deployment Type Wizard. In
  the Create Deployment Type Wizard, on the Content page, in Installation
  program, type app_file_name (where app_file_name is the name of the Windows 8
  application).

  For more information about how to complete the Create Application Wizard in the
  Configuration Manager console, see the following sections in the Documentation
  Library for System Center 2012 Configuration Manager, which is included with
  Configuration Manager:

        How to Create Applications in Configuration Manager

        How to Create Deployment Types in Configuration Manager

        How to Manage Applications and Deployment Types in Configuration
        Manager

5. Ensure that the user device affinity (UDA) feature in Configuration Manager is
  configured properly to support affinity between users and devices for
  Configuration Manager application deployment.

  For more information about how to configure UDA to support Configuration
  Manager application deployment, see How to Manage User Device Affinity in
  Configuration Manager.

6. Deploy the application created in step 4 to the targeted users.

  For more information about how to deploy an application to user, see How to
  Deploy Applications in Configuration Manager.

7. Configure the ApplicationPage wizard page to include the Configuration Manager
  application created in step 4 using the UDI Wizard Designer.

  For more information about how to configure the ApplicationPage wizard page
  using the UDI Wizard Designer, see the section, "Step 5-11: Customize the UDI

<!-- p.556 -->

     Wizard Configuration File for the Target Computer", in the MDT document Quick
     start Guide for User-Driven Installation.

  8. Select the UDI application item created in the previous step in a UDI task
     sequence.

       ７ Note

       The Windows 8 application is not installed by the task sequence but rather will
       be installed the first time the user logs on to the targeted computer (as
       defined by the UDA setting configured in step 5) using the User-Centric App
       Installer feature (AppInstall.exe) in UDI.

     For more information on the User-Centric App Installer feature in UDI, see the
     section, "User-Centric App Installer Reference", in the MDT document Toolkit
     Reference.

Managing MDT Using Windows PowerShell
You can manage MDT deployment shares using the Deployment Workbench and
Windows PowerShell. MDT includes a Windows PowerShell™ snap-in—
Microsoft.BDD.SnapIn—that must be loaded prior to using the MDT-specific features in
Windows PowerShell. The MDT Windows PowerShell snap-in includes:

     A Windows PowerShell provider—MDTProvider—that provides access to the
     contents of a deployment share

     Cmdlets that provide the ability to administer MDT deployment shares

     Manage MDT deployment shares using Windows PowerShell by performing the
     following steps:

     Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

     Create a deployment share using Windows PowerShell as described in Creating a
     Deployment Share Using Windows PowerShell.

     View deployment share properties using Windows PowerShell as described in
     Viewing Deployment Share Properties Using Windows PowerShell.

     View the list of deployment shares using Windows PowerShell as described in
     Viewing the List of Deployment Shares Using Windows PowerShell.

<!-- p.557 -->

     Update a deployment share, which generates new Windows Preinstallation
     Environment (Windows PE) boot images, as described in Updating a Deployment
     Share Using Windows PowerShell.

     Update a linked deployment share, which replicates content from a deployment
     share to the linked deployment share, as described in Updating a Linked
     Deployment Share Using Windows PowerShell.

     Update deployment media, which replicates content from a deployment share to
     the deployment media, and then generates new bootable images as described in
     Updating Deployment Media Using Windows PowerShell.

     Manage items in a deployment share (such as operating systems, operating system
     packages, applications, and device drivers) as described in Managing Items in a
     Deployment Share Using Windows PowerShell.

     Automate the population of items in a deployment share (such as operating
     systems, operating system packages, applications, and device drivers) as described
     in Automating Population of a Deployment Share.

     Manage the folders in a deployment share using Windows PowerShell as described
     in Managing Deployment Share Folders Using Windows PowerShell.

Loading the MDT Windows PowerShell Snap-In
The MDT cmdlets are provided in a Windows PowerShell snap-in Microsoft.BDD.SnapIn
that must be loaded prior to using the MDT cmdlets. Load the MDT Windows
PowerShell snap-in using the Add-PSSnapIn cmdlet as described in Load the MDT
Windows PowerShell Snap-In Using the Add-PSSnapIn Cmdlet.

Load the MDT Windows PowerShell Snap-In Using the Add-
PSSnapIn Cmdlet
You can load the MDT Windows PowerShell snap-in Microsoft.BDD.PSSnapIn from any
Windows PowerShell environment using the Add-PSSnapIn cmdlet, as show in the
following example:

  PowerShell

  Add-PSSnapin -Name Microsoft.BDD.PSSnapIn

Creating a Deployment Share Using Windows PowerShell

<!-- p.558 -->

You can create deployment shares using the MDT Windows PowerShell cmdlets. The
root folder for the deployment share is created and shared using standard Windows
PowerShell cmdlets and calls to Windows Management Instrumentation (WMI) class
commands. The deployment share is populated using the MDTProvider Windows
PowerShell provider and the NewPSDrive        cmdlet. The MDTProvider Windows
PowerShell drive is persisted using the Add-MDTPersistentDrive cmdlet.

To prepare a deployment share using the MDT Windows PowerShell cmdlets

  1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

  2. Create the folder that will be the root of the new deployment share using the
     New-Item cmdlet, as shown in the following example and described in Using the
     New-Item Cmdlet:

       PowerShell

       New-Item "C:\MDTDeploymentShare$" -Type directory

     The cmdlet displays the successful creation of the folder.

  3. Share the folder created in the previous step using the WMI win32_share class as
     sown in the following example:

       PowerShell

       ([wmiclass]"win32_share").Create("C:\MDTDeploymentShare$",
       "MDTDeploymentShare$",0)

     The call to the win32_share class returns the results of the call. If the value of
     ReturnValue is zero (0), then the call was successful.

  4. Specify the new shared folder as a deployment share using the NewPSDrive
     cmdlet, as shown in the following example:

       PowerShell

       New-PSDrive -Name "DS002" -PSProvider "MDTProvider" -Root
       "C:\MDTDeploymentShare$" -Description "MDT Deployment Share Created
       with Cmdlets" -NetworkPath "\\WDG-MDT-01\MDTDeploymentShare$" -Verbose

     The cmdlet automatically starts creating the deployment share and copying the
     template information into the new deployment share. Upon completion of the

<!-- p.559 -->

   copy process, the cmdlet displays the information for the new deployment share.

     ７ Note

     The value provided in the Name parameter (DS002) must be unique and
     cannot be the same as an existing deployment share Windows PowerShell
     drive.

 5. Verify that the appropriate deployment share folders have been created using the
   dir command, as show in the following example:

     PowerShell

     Get-ChildItem ds002:

   The list of default folders in the root of the deployment share is displayed.

 6. Add the new deployment share to the list of persisted MDT deployment shares
   using the Add-MDTPersistentDrive cmdlet, as shown in the following example:

     PowerShell

     $NewDS=Get-PSDrive "DS002"
     Add-MDTPersistentDrive -Name "DS002" -InputObject $NewDS Verbose

   In this example, the $NewDS variable is used to pass the Windows PowerShell drive
   object for the new deployment share to the cmdlet.

   Alternatively, you could have combined the NewPSDrive        and Add-
   MDTPersistentDrive cmdlets, as shown in the following example:

     PowerShell

     New-PSDrive -Name "DS002" -PSProvider "MDTProvider" -Root
     "C:\MDTDeploymentShare$" -Description "MDT Deployment Share Created
     with Cmdlets" -NetworkPath "\\WDG-MDT-01\MDTDeploymentShare$" -Verbose
     | Add-MDTPersistentDrive -Verbose

   In the previous example, the Windows PowerShell pipeline provides both the
   Name and InputObject parameters.

Viewing Deployment Share Properties Using Windows
PowerShell

<!-- p.560 -->

You can view the properties of MDT deployment shares using the Get-ItemProperty
cmdlet and the MDTProvider Windows PowerShell provider. These same properties can
also be seen in the Deployment Workbench.

To view deployment share properties using the MDT Windows PowerShell cmdlets

  1. Load the MDT Windows PowerShell snap-in as described in Loading the MDT
     Windows PowerShell Snap-In.

  2. Ensure the MDT deployments share Windows PowerShell drives are restored using
     the Restore-MDTPersistentDrive cmdlet, as shown in the following example:

       PowerShell

        Restore-MDTPersistentDrive -Verbose

       ７ Note

       If the MDT deployments that share Windows PowerShell drives are already
       restored, you will receive a warning message indicating that the cmdlet is
       unable to restore the drive.

  3. Verify that the MDT deployments that share Windows PowerShell drives are
     restored properly using the Get-PSDrive cmdlet, as follows:

       PowerShell

        Get-PSDrive -PSProvider Microsoft.BDD.PSSnapIn\MDTProvider

     The list of Windows PowerShell drives that are provided using the MDTProvider are
     listed.

  4. View the properties of the deployment share using the Get-ItemProperty cmdlet,
     as shown in the following example:

       PowerShell

        Get-ItemProperty "DS002:"

     In this example, DS002: is the name of a Windows PowerShell drive returned in
     step 3. The cmdlet returns the properties for the deployment share.
