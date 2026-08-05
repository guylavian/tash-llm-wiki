---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 681-720"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0681-0720
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0681-0720
family: sccm
documentKind: "doc"
abstract: "In this step, you prepare the MDT environment prior to creating the reference computer and deploying a captured image of the reference computer to the target computer (WDG-CLI-01). Prepare the MDT environment by: Installing MDT as described in Step 2-1: Install MDT Installing Wi"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 681-720

<!-- p.681 -->

In this step, you prepare the MDT environment prior to creating the reference computer
and deploying a captured image of the reference computer to the target computer
(WDG-CLI-01).

Prepare the MDT environment by:

     Installing MDT as described in Step 2-1: Install MDT

     Installing Windows ADK as described in Step 2-2: Install Windows ADK

Step 2-1: Install MDT
To install MDT, complete the following steps:

   1. Double-click MicrosoftDeploymentToolkit2013_x64.msi (for 64-bit operating
     systems) or MicrosoftDeploymentToolkit2013_x86.msi (for 32-bit operating
     systems), and then select Install.

     The Microsoft Deployment Toolkit 2013 Setup Wizard starts.

   2. Complete the Microsoft Deployment Toolkit 2013 Setup Wizard using the
     following information. Accept the default values unless otherwise specified.

                                                                             ﾉ   Expand table

      On this wizard page                       Do this

      Welcome to the Microsoft Deployment       Select Next.
      Toolkit 2013 Setup Wizard

      End-User License Agreement                Select I accept the terms in the License
                                                Agreement, and then select Next.

      Custom Setup                              Select Next.

      Ready to install Microsoft Deployment     Select Install.
      Toolkit 2013

      Installing Microsoft Deployment Toolkit   The progress for installing MDT is displayed.
      2013

      Completing the Microsoft Deployment       Select Finish.
      Toolkit 2013 Setup Wizard

     The Microsoft Deployment Toolkit 2013 Setup Wizard finishes, and MDT is installed
     on WDG-MDT-01.

<!-- p.682 -->

Step 2-2: Install Windows ADK
To install Windows ADK, perform the following steps:

   1. Mount the Windows ADK distribution files on a physical or virtual CD-ROM drive.

   2. In Windows Explorer, go to the root of the CD-ROM drive, and then double-click
     adksetup.exe.

     The Assessment and Deployment Kit Setup Wizard starts.

   3. Complete the Assessment and Deployment Kit Setup Wizard using the following
     information.

                                                                                ﾉ    Expand table

      On this wizard page               Do this

      Specify Location                  Select Next.

      Join the Customer Experience      Select Yes if you want to participate or No if not. Then,
      Improvement Program (CEIP)        select Next.

      License Agreement                 Select Accept.

      Select the features you want to   Ensure that only the check boxes for the following
      install                           features are selected, and then select Next:

                                        - Deployment Tools
                                        - Windows Preinstallation Environment (Windows PE)
                                        - Windows User State Migration Tool Note: MDT does
                                        not require the other features, but they can be installed,
                                        if desired.

      Installing features               The progress for installing the features is displayed.

      Welcome to the Assessment         Select Close.
      and Deployment Kit

   4. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   5. Close all open windows.

  ７ Note

  After installing Windows ADK, log off, and then log on again to the computer so
  that the PATH environment variable is updated to include the %Program

<!-- p.683 -->

  Files%\Windows Imaging folder.

Step 3: Configure MDT to Create the Reference
Computer
When you have prepared the MDT environment, create the reference computer. The
reference computer is the template for deploying new images to the target computers.
Configure this computer exactly as the target computers will be configured. You will
deploy Windows 8.1 to the reference computer (WDG-REF-01), capture an image of the
reference computer, and then deploy the captured image to the target computer (WDG-
CLI-01).

Configure MDT to create a reference computer by:

     Creating an MDT deployment share as described in Step 3-1: Create an MDT
     Deployment Share

     Adding operating system files to the deployment share as described in Step 3-2:
     Add Operating System Files to the Deployment Share

     Adding device drivers to the deployment share as described in Step 3-3: Add
     Device Drivers to the Deployment Share

     Creating a task sequence for the reference computer as described in Step 3-4:
     Create a Task Sequence for the Reference Computer

     Enabling monitoring of the LTI deployment process as described in Step 3-5:
     Enable LTI Deployment Process Monitoring

     Updating the deployment share as described in Step 3-6: Update the Deployment
     Share

Step 3-1: Create an MDT Deployment Share
Before deployment can begin, create an MDT deployment share in the Deployment
Workbench. This deployment share is the repository for the operating system images,
language packs, applications, device drivers, and other software deployed to the target
computers.

To create a deployment share in the Deployment Workbench

<!-- p.684 -->

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

   3. In the Actions pane, select New Deployment Shares.

     The New Deployment Share Wizard starts.

   4. Complete the New Deployment Share Wizard using the following information.

                                                                              ﾉ   Expand table

      On this wizard       Do this
      page

      Path                 In Deployment share path, type C:\DeploymentShare$, and then
                           select Next.

      Share                Select Next.

      Descriptive Name     Select Next.

      Options              Select Next.

      Summary              Select Next.

      Progress             The progress for creating the deployment share is displayed.

      Confirmation         Select Finish.

     The New Deployment Share Wizard finishes, and the new deployment share—MDT
     Deployment Share (C:\DeploymentShare$)—appears in the details pane.

Step 3-2: Add Operating System Files to the Deployment
Share
MDT acts as a repository for the operating system files deployed to the reference
computer (WDG-REF-01) and target computer (WDG-CLI-01). Add the operating system
in the Operating Systems node in the Deployment Workbench using the Import
Operating System Wizard.

To add the Windows 8.1 operating system files to the deployment share

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

<!-- p.685 -->

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/MDT Deployment Share
     (C:\DeploymentShare$)/Operating Systems.

   3. In the Actions pane, select Import Operating System.

     The Import Operating System Wizard starts.

   4. Complete the Import Operating System Wizard using the following information.

                                                                                ﾉ   Expand table

      On this wizard   Do this
      page

      On this wizard   Do this
      page

      OS Type          Select Full set of source files, and then select Next.

      Source           In Source directory, type source_path (where source_path is the fully
                       qualified path to the Windows 8.1 distribution files), and then select
                       Next.

      Destination      Select Next.

      Summary          Select Next.

      Progress         The progress for importing the operating system is displayed.

      Confirmation     Select Finish.

     The Import Operating System Wizard finishes. Windows 8.1 is added to the list of
     operating systems in the details pane and copied to the
     deployment_share\Operating Systems\operating_system folder (where
     deployment_share is the shared network folder you created earlier in the process
     and operating_system is the name of the operating system you added to the
     deployment share).

Step 3-3: Add Device Drivers to the Deployment Share
After you have added Windows 8.1 to the Deployment Workbench, add any device
drivers required for the reference computer (WDG-REF-01) and the target computer
(WDG-CLI-01). These device drivers will be added to Windows PE and deployed with
Windows 8.1. Add the device drivers in the Out-of-box Drivers node in the Deployment
Workbench by using the New Driver Wizard, which copies the device driver files to the

<!-- p.686 -->

deployment share in Out-of-Box Drivers\device_driver (where device_driver is the name
of the device driver you added to the deployment share).

  ７ Note

  If the device drivers for the reference computer (WDG-REF-01) and the target
  computer (WDG-CLI-01) are included with Windows 8.1, skip this step and proceed
  with the following step.

To add the device drivers for the reference and target computers to the distribution
share

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/MDT Deployment Share
     (C:\DeploymentShare$)/Out-of-Box Drivers.

   3. In the Actions pane, select Import Drivers.

     The Import Driver Wizard starts.

   4. Complete the Import Driver Wizard using the following information.

                                                                                  ﾉ    Expand table

        On this wizard   Do this
        page

        Specify          In Driver source directory, type driver_path (where driver_path is the
        Directory        fully qualified path to the folder containing the device drivers), and then
                         select Next.

        Summary          Select Next.

        Progress         The progress for importing the device drivers is displayed.

        Confirmation     Select Finish.

     The Import Driver Wizard finishes. The device drivers are added to the list of
     operating systems in the details pane and are copied to the
     deployment_share\Out-of-box Drivers folder (where deployment_share is the
     deployment share you created earlier in the process).

<!-- p.687 -->

Step 3-4: Create a Task Sequence for the Reference
Computer
Create MDT task sequences in the Task Sequences node in the Deployment Workbench
using the New Task Sequence Wizard. MDT includes the Standard Client Task Sequence
template, which you can use to deploy the target operating system to the reference
computer (WDG-REF-01).

To create a task sequence for deploying the reference computer

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/MDT Deployment Share
     (C:\DeploymentShare$)/Task Sequences

  3. In the Actions pane, select New Task Sequence.

     The New Task Sequence Wizard starts.

  4. Complete the New Task Sequence Wizard using the following information. Accept
     the default values unless otherwise specified.

                                                                              ﾉ   Expand table

      On this        Do this
      wizard page

      General        1. In Task sequence ID, type WIN8_REFERENCE.
      Settings       2. In Task sequence name, type Deploy Windows 8.1 to Reference
                     Computer.
                     3. In Task sequence comments, type Task sequence for deploying
                     Windows 8.1 to the reference computer (WDG-REF-01).
                     4. Select Next.

      Select         In The following task sequence templates are available. Select the one
      Template       you would like to use as a starting point, select Standard Client Task
                     Sequence, and then select Next.

      Select OS      In The following operating system images are available to be deployed
                     with this task sequence. Select one to use, select Windows 8.1 edition
                     (where edition is the edition of Windows 8.1 added to the Operating
                     Systems node in the Deployment Workbench), and then select Next.

      Specify        Select Do not specify a product key at this time, and then select Next.
      Product Key

<!-- p.688 -->

      On this         Do this
      wizard page

      OS Settings     1. In Full Name, type Woodgrove Bank Employee.

                      2. In Organization, type Woodgrove Bank.

                      3. In Internet Explorer Home Page, type
                      http://www.woodgrovebank.com.

                      4. Select Next.

      Admin           In Administrator Password and Please confirm Administrator Password,
      Password        type P@ssw0rd, and then select Next.

      Summary         Select Next.

      Progress        The progress for creating the task sequence is displayed.

      Confirmation    Select Finish.

     The Import Task Sequence Wizard finishes, and the Deploy Windows 8.1 to
     Reference Computer task sequence is added to the list of task sequences.

Step 3-5: Enable LTI Deployment Process Monitoring
Prior to deploying the reference computer (WDG-REF-01) with the LTI bootable media
you created earlier in the process, enable monitoring of the LTI deployment process. You
monitor the LTI deployment process in the Monitoring node in the deployment share.
You enable monitoring on the Monitoring tab on the deployment share properties
sheet. Later in the process, you will monitor the LTI deployment process.

To enable monitoring of the LTI deployment process

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

   3. In the details pane, select MDT Deployment Share (C:\DeploymentShare$).

   4. In the Actions pane, select Properties

     The MDT Deployment Share (C:\DeploymentShare$) Properties dialog box
     opens.

<!-- p.689 -->

   5. In the MDT Deployment Share (C:\DeploymentShare$) Properties dialog box, on
     the Monitoring tab, select the Enable monitoring for this deployment share
     check box, and then select Apply.

   6. In the MDT Deployment Share (C:\DeploymentShare$) Properties dialog box, on
     the Rules tab, notice that the EventService property has been added to the
     CustomSettings.ini file, and then select OK.

   7. Close all open windows and dialog boxes.

Step 3-6: Update the Deployment Share
After configuring the deployment share, update it. Updating the deployment share
updates all the MDT configuration files and generates a customized version of Windows
PE. You use the customized version of Windows PE to start the reference computer and
initiate LTI deployment.

To update the deployment share in the Deployment Workbench

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

   3. In the details pane, select MDT Deployment Share (C:\DeploymentShare$).

   4. In the Actions pane, select Update Deployment Share.

     The Update Deployment Share Wizard starts.

   5. Complete the Update Deployment Share Wizard using the following information.
     Accept the default values unless otherwise specified.

                                                                            ﾉ   Expand table

      On this wizard page   Do this

      Options               Select Next.

      Summary               Select Next.

      Progress              The progress for updating the deployment share is displayed.

      Confirmation          Select Finish.

<!-- p.690 -->

     The Deployment Workbench starts updating the MDT Deployment Share
     (C:\DeploymentShare$) deployment share. The Deployment Workbench also
     creates the LiteTouchPE_x64.iso and LiteTouchPE_x64.wim files (for 64-bit target
     computers) or LiteTouchPE_x86.iso and LiteTouchPE_x86.wim files (for 32-bit target
     computers) in the deployment_share\Boot folder (where deployment_share is the
     network shared folder used as the deployment share).

Step 4: Deploy Windows 8.1 and Capture an
Image of the Reference Computer
After creating the task sequence to deploy Windows 8.1 to the reference computer,
initiate operating system deployment and image capture by starting the reference
computer with the LTI bootable media.

Deploy Windows 8.1 and capture an image of the reference computer by:

     Creating the LTI bootable media as described in Step 4-1: Create the LTI Bootable
     Media

     Starting the reference computer with the LTI bootable media and monitoring the
     LTI deployment process as described in Step 4-2: Start the Reference Computer
     with the LTI Bootable Media

Step 4-1: Create the LTI Bootable Media
You need to provide a method for starting the computer with the customized version of
Windows PE you created when you updated the deployment share. The Deployment
Workbench creates the LiteTouchPE_x64.iso and LiteTouchPE_x64.wim files (for 64-bit
target computers) or LiteTouchPE_x86.iso and LiteTouchPE_x86.wim files (for 32-bit
target computers) in the deployment_share\Boot folder (where deployment_share is the
network shared folder used as the deployment share). Create the appropriate LTI
bootable media from one of these images.

To create the LTI bootable media

   1. In Windows Explorer, go to C:\DeploymentShare$\Boot.

   2. Based on the type of computer used for the reference computer (WDG-REF-01),
     perform one of the following tasks:

          If the reference computer is a physical computer, create a physical CD or DVD
          of the LiteTouchPE_x64.iso or LiteTouchPE_x86.iso file.

<!-- p.691 -->

           If the reference computer is a VM, start the VM directly from the
           LiteTouchPE_x64.iso or LiteTouchPE_x86.iso file or from a CD or DVD of the
           International Standard Organization (ISO) files.

Step 4-2: Start the Reference Computer with the LTI
Bootable Media
Start the reference computer (WDG-REF-01) with the LTI bootable media you created
earlier in the process. The LTI bootable media starts Windows PE on the reference
computer and initiates deployment. At the end of the MDT deployment process,
Windows 8.1 is deployed on the reference computer.

  ７ Note

  You can use a 32-bit boot image to deploy both 32-bit and 64-bit operating
  systems; however, a 64-bit boot image can only be used to deploy 64-bit operating
  systems.

You could also initiate the process by starting the target computer from Windows
Deployment Services. For more information, see the section, "Preparing Windows
Deployment Services", in the MDT document, Using the Microsoft Deployment Toolkit.

To start the reference computer with the LTI bootable media

   1. Start WDG-REF-01 with the LTI bootable media you created earlier in the process.

     Windows PE starts, and then the Windows Deployment Wizard starts.

   2. Complete the Windows Deployment Wizard using the following information.
     Accept the default values unless otherwise specified.

                                                                          ﾉ    Expand table

      On this wizard page    Do this

      Welcome                Select Run the Deployment Wizard to install a new Operating
                             System.

      Credentials            1. In User Name, type Administrator.
                             2. In Password, type P@ssw0rd.
                             3. In Domain, type MDT2013.
                             4. Select OK.

<!-- p.692 -->

   On this wizard page     Do this

   Task Sequence           Select Deploy Windows 8.1 to Reference Computer, and then
                           select Next.

   Computer Details        In Computer name, type WDG-REF-01, and then select Next.

   Move Data and           Select Next.
   Settings

   User Data (Restore)     Select Next.

   Locale and Time         Select Next.

   Capture Image           Select Capture an image of this reference computer, and then
                           select Next.

   Ready                   1. Select Details to view the information provided in the wizard.
                           2. Select Begin.

  To monitor the reference computer deployment process, complete the following
  steps on WDG-MDT-01

3. On WDG-MDT-01, select Start, and then point to All Programs. Point to Microsoft
  Deployment Toolkit, and then select Deployment Workbench.

4. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/MDT Deployment Share
  (C:\DeploymentShare$)/Monitoring.

5. In the details pane, view the deployment process for WDG-REF-01.

6. In the Actions pane, periodically select Refresh.

  The status of the deployment process is updated in the details pane.

  Continue to monitor the deployment process until the process is complete.

7. In the details pane, select WDG-REF-01.

8. In the Actions pane, select Properties.

  The WDG-REF-01 Properties dialog box is displayed.

9. In the WDG-REF-01 Properties dialog box, on the Identity tab, view the
  monitoring information provided about the deployment process as described in
  the following table.

<!-- p.693 -->

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
                    the target operating system, or does not have the Remote Desktop
                    feature enabled.

VM Connection       This button allows you to establish a remote desktop connection to
                    a VM running in HyperV®. This method assumes that:

<!-- p.694 -->

    Information          Description

                         - The deployment is being performed to a VM running on Hyper-V
                         - vmconnect.exe is located in the %ProgramFiles%\Hyper-V folder
                         Note: This button appears when ZTIGather.wsf detects that Hyper-V
                         integration components are running on the monitored computer.
                         Otherwise, this button will not be visible.

    DaRT Remote          This button allows you to establish a remote control session using
    Control              the remote viewer feature in the Diagnostics and Recovery Toolkit
                         (DaRT).

                         This method assumes that:

                         - DaRT has been deployed to the target computer and is currently
                         running
                         - DartRemoteViewer.exe is located in the
                         %ProgramFiles%\Microsoft DaRT 7\v7 folder Note: This button
                         appears when ZTIGather.wsf detects that DaRT is running on the
                         monitored computer. Otherwise, this button will not be visible.

    Automatically        Check box that controls whether the information in the dialog box is
    refresh this         automatically refreshed. If the check box is:
    information every
    10 seconds           - Selected, the information is refreshed every 10 seconds
                         - Cleared, the information is not automatically refreshed and must
                         be manually refreshed using the Refresh Now button

    Refresh Now          This button immediately refreshes the information displayed in the
                         dialog box.

10. In the WDG-REF-01 Properties dialog box, select OK.

11. Close the Deployment Workbench.

   To complete the reference computer deployment process, perform the following
   steps on WDG-REF-01:

12. On WDG-REF-01, in the Deployment Summary dialog box, select Details.

   If any errors or warnings occur, review the errors or warnings, and record any
   diagnostic information.

13. In the Deployment Summary dialog box, select Finish.

   Windows 8.1 is now installed on the reference computer, and the captured
   Windows Imaging Format (WIM) file of the reference computer
   (WIN7_REFERENCE.wim) is stored in the deployment_share\Captures folder (where

<!-- p.695 -->

     deployment_share is the shared folder used as the deployment share).If errors or
     warnings occur, consult the MDT document Troubleshooting Reference.

Step 5: Configure MDT to Deploy Windows 8.1
to the Target Computer
When you have captured an image of the reference computer (MDT-REF-01), deploy it
to the target computer (MDT-CLI-01). You import the captured image into the
Deployment Workbench using the Import Operating System Wizard. Then, you create a
task sequence to deploy the captured image to the target computer.

Configure MDT to deploy Windows 8.1 to the target computer by:

     Adding the captured image of the reference computer to the Deployment
     Workbench as described in Step 5-1: Add the Captured Image of the Reference
     Computer to the Deployment Workbench

     Creating a task sequence for the target computer as described in Step 5-2: Create
     a Task Sequence for the Target Computer

Step 5-1: Add the Captured Image of the Reference
Computer to the Deployment Workbench
To deploy the captured image of the reference computer to the target computer, add
the captured image to the list of operating systems in the Operating Systems node in
the Deployment Workbench. The Import Operating System Wizard copies the operating
system files to the deployment_share\Operating Systems\operating_system folder (where
deployment_share is the deployment share folder created earlier in the process and
operating_system is the name of the operating system added to the deployment share).

To add the captured image of the reference computer to the Deployment Workbench

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/MDT Deployment Share
     (C:\DeploymentShare$)/Operating Systems.

   3. In the Actions pane, select Import Operating system.

     The Import Operating System Wizard starts.

<!-- p.696 -->

  4. Complete the Import Operating System Wizard using the information in the
     following table.

                                                                               ﾉ   Expand table

      On this wizard    Do this
      page

      OS Type           Select Custom image file, and then select Next.

      Image             In Source file, type
                        C:\DeploymentShare$\Captures\WIN8_REFERENCE.wim, and then
                        select Next.

      Setup             Select Next.

      Destination       Select Next.

      Summary           Select Next.

      Progress          The progress for importing the operating system is displayed.

      Confirmation      Select Finish.

     The Import Operating System Wizard finishes. The captured image of the reference
     computer (WDG-REF-01) operating system is added to the list of operating
     systems in the details pane and is copied to the deployment_share\Operating
     Systems\operating_system folder (where deployment_share is the deployment share
     folder created earlier in the process and operating_system is the name of the
     operating system added to the deployment share).

  5. Close all open windows and dialog boxes.

Step 5-2: Create a Task Sequence for the Target Computer
Create an MDT task sequence for the target computer in the Task Sequences node in the
Deployment Workbench using the New Task Sequence Wizard. This task sequence is
used to deploy the captured image of the reference computer to the target computer.

To create a task sequence for deploying the captured image to the target computer

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/MDT Deployment Share

<!-- p.697 -->

  (C:DeploymentShare$)/Task Sequences.

3. In the Actions pane, select New Task Sequence.

  The New Task Sequence Wizard starts.

4. Complete the New Task Sequence Wizard using the following information. Accept
  the default values unless otherwise specified.

                                                                                ﾉ   Expand table

   On this wizard   Do this
   page

   General          1. In Task sequence ID, type WIN8_TARGET.
   Settings         2. In Task sequence name, type Deploy Captured Image to Target
                    Computer.
                    3. In Task sequence comments, type Task sequence for captured
                    Windows 8.1 image from reference computer (WDG-REF-01) to the
                    target computer (WDG-CLI-01).
                    4. Select Next.

   Select           In The following task sequence templates are available. Select the one
   Template         you would like to use as a starting point, select Standard Client Task
                    Sequence, and then select Next.

   Select OS        In The following operating system images are available to be deployed
                    with this task sequence. Select one to use, select WIN8_RERENCEDrive in
                    "WIN8_REFERENCE\WIN8_REFERENCE.wim", and then select Next.

   Specify          Select Do not specify a product key at this time, and then select Next.
   Product Key

   OS Settings      1. In Full Name, type Woodgrove Bank Employee.
                    2. In Organization, type Woodgrove Bank.
                    3. In Internet Explorer Home Page, type
                    http://www.woodgrovebank.com.
                    4. Select Next.

   Admin            In Administrator Password and Please confirm Administrator Password,
   Password         type P@ssw0rd, and then select Next.

   Summary          Select Next.

   Progress         The progress for creating the task sequence is displayed.

   Confirmation     Select Finish.

  The Import Task Sequence Wizard finishes, and the WIN8_TARGET task sequence is
  added to the list of task sequences.

<!-- p.698 -->

   5. Close all open windows and dialog boxes.

Step 6: Deploy the Captured Image of the
Reference Computer to the Target Computer
When you have captured an image of the reference computer and created and
configured the appropriate task sequence, deploy the captured image. Configure MDT
to provide all the necessary configuration settings for deployment to the target
computer. After initiating the deployment process, the image of the reference computer
running Windows 8.1 is automatically deployed to the target computer and configured
with the settings defined.

Deploy the captured image of the reference computer to the target computer by:

     Starting the target computer with the LTI bootable media and monitor the LTI
     deployment process as described in Step 6-1: Start the Target Computer with the
     LTI Bootable Media

Step 6-1: Start the Target Computer with the LTI Bootable
Media
Start the target computer (WDG-CLI-01) with the LTI bootable media you created earlier
in the process. This CD starts Windows PE on the target computer and initiates
deployment. At the end of the process, Windows 8.1 is deployed on the target
computer.

  ７ Note

  You can also initiate deployment by starting the target computer from Windows
  Deployment Services. For more information, see the MDT document Using the
  Microsoft Deployment Toolkit.

To start the target computer with the LTI bootable media

   1. Start WDG-CLI-01 with the LTI bootable media you created earlier in the process.

     Windows PE starts, and then the Windows Deployment Wizard starts.

   2. Complete the Windows Deployment Wizard using the following information.
     Accept the default values unless otherwise specified.

<!-- p.699 -->

                                                                            ﾉ    Expand table

   On this wizard page     Do this

   Welcome                 Select Run the Deployment Wizard to install a new Operating
                           System.

   Credentials             1. In User Name, type Administrator.
                           2. In Password, type P@ssw0rd.
                           3. In Domain, type MDT2013.
                           4. Select OK.

   Task Sequence           Select Deploy Captured Image to Target Computer, and then
                           select Next.

   Computer Details        In Computer name, type WDG-CLI-01, and then select Next.

   Move Data and           Select Next.
   Settings

   User Data (Restore)     Select Next.

   Locale and Time         Select Next.

   Capture Image           Select Next.

   BitLocker               Select Next.

   Ready                   1. Select Details to view the information provided in the wizard.
                           2. Select Begin.

  The wizard starts, and then the operating system deployment starts.

  To monitor the target computer deployment process, complete the following
  steps on WDG-MDT-01

3. On WDG-MDT-01, select Start, and then point to All Programs. Point to Microsoft
  Deployment Toolkit, and then select Deployment Workbench.

4. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/MDT Deployment Share
  (C:\DeploymentShare$)/Monitoring

5. In the Actions pane, periodically select Refresh.

6. In the details pane, view the deployment process for WDG-CLI-01.

7. In the Actions pane, periodically select Refresh.

<!-- p.700 -->

     The status of the deployment process is updated in the details pane. Continue to
     monitor the deployment process until the process is complete.

   8. Close the Deployment Workbench.

     To complete the target computer deployment process, perform the following
     steps on WDG-CLI-01

   9. On WDG-CLI-01, in the Deployment Summary dialog box, select Details.

     If any errors or warnings occur, review the errors or warnings, and record any
     diagnostic information.

 10. In the Deployment Summary dialog box, select Finish.

     At the end of the MDT deployment process, the Deployment Summary dialog box
     appears. The image of Windows 8.1 captured from the reference computer is now
     installed on the target computer. If any errors or warnings occur, consult the MDT
     document Troubleshooting Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.701 -->

Quick Start Guide for Microsoft System
Center 2012 R2 Configuration Manager
Article • 02/12/2024

Microsoft Deployment Toolkit (MDT) 2013 provides technology for deploying Windows
operating systems, and Microsoft Office. This quick start guide helps you quickly
evaluate MDT 2013 by providing condensed, step-by-step instructions for using it to
install the Windows 8.1 operating system with Microsoft System Center 2012 R2
Configuration Manager. This quick start guide demonstrates how to perform the New
Computer deployment scenario, which covers the deployment of Windows 8.1 to a new
computer. This scenario assumes that there is no user data or profile to preserve.

  ７ Note

  In this document, Windows applies to the Windows 8.1, Windows 8, Windows 7,
  Windows Server® 2012 R2, Windows Server 2012, and Windows Server 2008 R2
  operating systems unless otherwise noted. MDT does not support ARM processor-
  based versions of Windows. Similarly, MDT refers to MDT 2013 unless otherwise
  stated.

After using this guide to evaluate MDT, review the rest of the MDT guidance to learn
more about the technology's advanced features.

Prerequisites
Zero Touch Installation installations using Configuration Manager have the following
prerequisites.

Required Software
To complete this guide, the following software is required:

      Windows Server 2008 R2

      Microsoft SQL Server 2008 R2

      SQL Server 2008 R2 Service Pack 1 (SP1)

      SQL Server 2008 R2 SP1 Cumulative Update 6 (CU6)

<!-- p.702 -->

      Windows 8.1

      System Center 2012 R2 Configuration Manager

      Microsoft .NET Framework version 3.5 with SP1

      Windows PowerShell version 2.0

      Windows Preinstallation Environment (Windows PE), which is included in
      Configuration Manager

      Networking services, including Domain Name System (DNS) and Dynamic Host
      Configuration Protocol (DHCP)

      Active Directory Domain Services (AD DS)

      See the Supported Configurations for Configuration Manager for additional
      software combinations that can be used for installing Configuration Manager.

  ７ Note

  The Task Sequencer used in MDT deployments requires that the Create Global
  Object right be assigned to credentials used to access and run the Deployment
  Workbench and the deployment process. This right is normally available to
  accounts with Administrator-level permissions (unless explicitly removed). Also, the
  Specialized Security - Limited Functionality (SSLF) security profile removes the
  Create Global Object right and should not be applied to computers deployed using
  MDT.

Computer Configuration
To complete this guide, set up the computers listed in the following table. These
computers can be either physical computers or virtual machines (VMs) with the system
resources designated.

                                                                            ﾉ   Expand table

 Computer     Description and system resources

 WDG-MDT-     This computer runs the MDT infrastructure and Configuration Manager. The
 01           computer runs Windows Server 2008 R2 with the following networking services
              installed:

              - AD DS

<!-- p.703 -->

 Computer     Description and system resources

              - DNS Server
              - DHCP Server
              - Windows Deployment Services

              The system resources of the computer are as follows:

              - Quad-core processor running at 2.66 gigahertz (GHz) or faster
              - 4 gigabytes (GB) or more of physical memory
              - A disk partition that has 40 GB or more of available disk space; it will become the
              drive C partition
              - One CD-ROM or DVD-ROM drive that will be assigned the drive letter D
              - A disk partition that has 40 GB or more of available disk space; it will become
              partition E.

 WDG-REF-     This is the reference computer, which runs no current operating system. The system
 01           resources of the computer are as follows:

              - Processor running at 1.4 GHz or faster
              - 1 GB or more of physical memory
              - 16 GB or more of available disk space

 WDG-CLI-     This is the target computer, which runs no current operating system. The system
 01           resources of the computer are as follows:

              - Processor running at 1.4 GHz or faster
              - 1 GB or more of physical memory
              - 16 GB or more of available disk space

The resources listed in the preceding table reflect the system resources recommended
to perform the steps in this guide. For information on the minimum system resource
requirements for:

      Windows Server 2008 R2, see Installing Windows Server 2008 R2

      SQL Server 2008 R2, see Hardware and Software Requirements for Installing SQL
      Server 2008 R2

  ７ Note

  This guide assumes that MDT is being evaluated on 64-bit (x64) physical or virtual
  computers. If evaluating MDT on 32-bit (x86) platforms, download and install the
  x86 editions of MDT and the components that this guide describes.

Step 1: Prepare the Prerequisite Infrastructure

<!-- p.704 -->

For purposes of this guide, all the prerequisite infrastructure services run on the
computer named WDG-MDT-01. Install the prerequisite software, server roles, and
services on this computer before installing MDT.

  ７ Note

  This section assumes that you are creating a new Configuration Manager
  infrastructure for MDT. If you are using an existing Configuration Manager
  infrastructure, review the steps in this section and substitute existing resource
  names for the resources created in this section (such as the computer name and
  shared network folders). After reviewing this section, proceed to Step 2: Prepare
  the MDT Environment.

Prepare the prerequisite infrastructure before installing MDT by:

     Installing Windows Server 2008 R2 as described in Step 1-1: Install Windows Server
     2008 R2

     Creating the required folders and network shares as described in Step 1-2: Create
     the Required Folders and Network Shares

     Obtaining the software required to perform the steps in this guide as described in
     Step 1-3: Obtain the Required Software

     Installing the AD DS server role as described in Step 1-4: Install the AD DS Server
     Role

     Installing the DHCP Server server role as described in Step 1-5: Install the DHCP
     Server Server Role

     Installing the Web Services (IIS) server role as described in Step 1-6: Install the Web
     Services (IIS) Server Role

     Adding the required Windows Server 2008 R2 features as described in Step 1-7:
     Add the Required Windows Server 2008 R2 Features

     Creating the user and service accounts required to perform the steps in this guide
     as described in Step 1-8: Create the Required User and Service Accounts

     Installing SQL Server 2008 R2 for Configuration Manager to use as described in
     Step 1-9: Install SQL Server 2008 R2

     Adding the site server to the Administrators security group as described in Step 1-
     10: Add the Site Server to the Administrators Security Group

<!-- p.705 -->

     Installing Configuration Manager as described in Step 1-11: Install Configuration
     Manager

     Configuring the network access account that Configuration Manager clients use to
     access Configuration Manager distribution points as described in Step 1-12:
     Configure the Network Access Account

     Configuring the Configuration Manager site boundaries and boundary groups as
     described in Step 1-13: Configure the Configuration Manager Site Boundaries and
     Boundary Groups

     Configuring the publishing of site information in AD DS and DNS as described in
     Step 1-14: Configure the Publishing of Site Information in AD DS and DNS

Step 1-1: Install Windows Server 2008 R2
Information for Installing Windows Server 2008 R2. Accept default values unless
otherwise specified.

                                                                              ﾉ   Expand table

 When prompted for          Provide these values

 Where do you want to       Disk 0 Unallocated Space
 install Windows?

 Password                   Any strong password

 Computer name              WDG-MDT-01

 Format for volumes C and   NTFS
 E

 TCP/IP configuration       Configure with a static IP address configuration, with the other
                            TCP/IP configuration options as appropriate for the environment

Step 1-2: Create the Required Folders and Network Shares
The MDT deployment process requires additional folders that are used as the source for
files or to store files created during the MDT deployment process. Some of these folders
need to be shared so that they can be accessed from other computers.

To create the required folders and share

<!-- p.706 -->

1. The MDT Deployment Process Requires several folders. Create the following
  folders and shares with the specified permissions for each share.

                                                                      ﾉ   Expand table

   Create this folder     With this share name     With these share permissions

   E:\Source$             Source$                  Administrators: Co-owner

                                                   Everyone: Read

   E:\Images$             Images$                  Administrators: Co-owner

                                                   Everyone: Read

   E:\Capture$            Capture$                 Administrators: Co-owner

                                                   Everyone: Read

   E:\Packages$           Packages$                Administrators: Co-owner

                                                   Everyone: Read

2. Create the following folders:

        E:\CMDownloads

        E:\Source$\CustomSettings

        E:\Source$\Drivers

        E:\Source$\Windows_8-1

        E:\Source$\MDT_2013

        E:\Source$\SQL2008R2

        E:\Source$\SQL2008R2SP1

        E:\Source$\SQL2008R2CU6

        E:\Source$\ConfigMgr

        E:\Packages$\Drivers

3. Copy the device drivers for the reference computer (WDG-REF-01) and the target
  computer (WDG-CLI-01) to E:\Source$\Drivers.

<!-- p.707 -->

  ７ Note

  The processes in this guide assume that the reference computer and target
  computer have the same devices and do not require different devices drivers.

Step 1-3: Obtain the Required Software
Besides Windows Server 2008 R2, Windows 8.1, and Configuration Manager, certain
software is required to evaluate MDT based on the processes in this guide. The
following table lists the software required to perform deployments using MDT, where to
obtain the software, and where to place the software on WDG-MDT-01.

                                                                               ﾉ   Expand table

 Obtain this software                                             Place in this folder

 MDT 2013                                                         E:\Source$\MDT_2013

 Windows 8.1 distribution files from the product media            E:\Source$\Windows_8-1

 Device drivers required for the reference and target computers   E:\Source$\Drivers
 (WDG-REF-01 and WDG-CLI-01)

 SQL Server 2008 R2 from the product media                        E:\Source$\SQL2008R2

 SQL Server 2008 R2 SP1, available at                             E:\Source$\SQL2008R2SP1
 https://www.microsoft.com/download/details.aspx?id=26113

 SQL Server 2008 R2 SP1 CU6, available at                         E:\Source$\SQL2008R2SP1CU6
 https://support.microsoft.com/kb/2679367

 Configuration Manager from the product media                     E:\Source$\ConfigMgr

Step 1-4: Install the AD DS Server Role
AD DS is required to provide authentication and act as a repository for configuration
values for the Microsoft products and technologies that MDT uses, such as SQL Server
2008 R2 and Configuration Manager.

To install AD DS, run the DCPROMO Wizard to configure the computer as a domain
controller. Install AD DS using the following information, accepting any defaults unless
otherwise specified.

<!-- p.708 -->

                                                                                    ﾉ   Expand table

 When prompted                                               Do this

 For the domain type                                         Create a new domain in a new forest.

 For the fully qualified domain name                         Type
                                                             mdt2013.corp.woodgrovebank.com.

 For the forest functional level                             Select Windows Server 2008 R2.

 To install the DNS Server service as part of the domain     Select Yes.
 controller installation process

Step 1-5: Install the DHCP Server Server Role
The DHCP Server server role is required to provide automatic IP configuration for the
target computers. Install DHCP Server using the following information, accepting any
defaults unless otherwise specified.

  ７ Note

  If you are using a virtualized environment, disable any DHCP configuration that the
  computer-virtualization software provides. Ensure that the DHCP Server service
  running WDG-MDT-01 is the only provider of IP configuration using DHCP.

                                                                                    ﾉ   Expand table

 On this wizard page               Do this

 Authorize DHCP server in          Authorize WDG-MDT-01 to provide client IP configuration.
 Active Directory

 DHCP scopes                       Create an appropriate scope that can be used to automatically
                                   configure TCP/IP for WDG-REF-01 and WDG-CLI-01.

 DHCPv6 stateless mode             Disable DHCPv6 stateless mode for this server.
 configuration

Step 1-6: Install the Web Services (IIS) Server Role
Install the Web Services (IIS) server role with the role services listed in the following
table. These role services are required for SQL Server 2008 R2 and Configuration
Manager. Unless otherwise specified, use the default values.

<!-- p.709 -->

                              ﾉ       Expand table

Role service              Status

Web Server                Installed

Common HTTP Features      Installed

Static Content            Installed

Default Document          Installed

Directory Browsing        Installed

HTTP Errors               Installed

HTTP Redirection          Installed

WebDAV Publishing         Installed

Application Development   Installed

ASP.NET                   Installed

.NET Extensibility        Installed

ASP                       Not installed

CGI                       Not installed

ISAPI Extensions          Installed

ISAPI Filters             Installed

Server Side Includes      Not installed

Health and Diagnostics    Installed

HTTP Logging              Installed

Logging Tools             Installed

Request Monitor           Installed

Tracing                   Installed

Custom Logging            Not installed

ODBC Logging              Not installed

Security                  Installed

Basic Authentication      Not installed

<!-- p.710 -->

Role service                                    Status

Windows Authentication                          Installed

Digest Authentication                           Not installed

Client Certificate Mapping Authentication       Not installed

IIS Client Certificate Mapping Authentication   Not installed

URL Authorization                               Not installed

Request Filtering                               Installed

IP and Domain Restriction                       Not installed

Performance                                     Installed

Static Content Compression                      Installed

Dynamic Content Compression                     Not installed

Management Tools                                Installed

IIS Management Console                          Installed

IIS Management Scripts and Tools                Not installed

Management Service                              Not installed

IIS 6 Management Compatibility                  Installed

IIS 6 Metabase Compatibility                    Installed

IIS 6 WMI Compatibility                         Installed

IIS 6 Scripting Tools                           Not installed

IIS 6 Management Console                        Not installed

FTP Publishing Service                          Not installed

FTP Server                                      Not installed

FTP Management Console                          Not installed

IIS Hostable Web Core                           Not installed

Step 1-7: Add the Required Windows Server 2008 R2
Features

<!-- p.711 -->

In addition to installing the required Windows Server 2008 R2 server roles, add the
following required features in Server Manager in the Features Summary section:

     Background Intelligent Transfer Service

     Remote Differential Compression

Step 1-8: Create the Required User and Service Accounts
Configuration Manager and SQL Server 2008 R2 require user accounts during the
installation process. Use the following information for creating these accounts.

                                                                               ﾉ      Expand table

 Create this account                With these settings

 SQL Server Agent service account   1. In First name, type SQL Agent.
                                    2. In Last name, type Service Account.
                                    3. In User logon name, type SQLAgent.
                                    4. In Password and Confirm password, type P@ssw0rd.
                                    5. Clear the User must change password at next logon check
                                    box.
                                    6. Select the Password never expires check box.
                                    7. Make the account a member of the Domain Admins
                                    security group.
                                    8. In Description, type Service account used to run SQL
                                    Server 2008 R2 Agent service.

 SQL Server Database Engine         1. In First name, type SQL DB Engine.
 service account                    2. In Last name, type Service Account.
                                    3. In User logon name, type SQLDBEngine.
                                    4. In Password and Confirm password, type P@ssw0rd.
                                    5. Clear the User must change password at next logon check
                                    box.
                                    6. Select the Password never expires check box.
                                    7. Make the account a member of the Domain Admins
                                    security group.
                                    8. In Description, type Service account used to run SQL
                                    Server 2008 R2 database engine.

 SQL Server Reporting Services      1. In First name, type SQL Reporting.
 service account                    2. In Last name, type Service Account.
                                    3. In User logon name, type SQLReport.
                                    4. In Password and Confirm password, type P@ssw0rd.
                                    5. Clear the User must change password at next logon check
                                    box.
                                    6. Select the Password never expires check box.
                                    7. Make the account a member of the Domain Admins

<!-- p.712 -->

 Create this account               With these settings

                                   security group.
                                   8. In Description, type Service account used to run SQL
                                   Server 2008 R2 reporting services.

 Configuration Manager Client      1. In First name, type CM 2012.
 Network Access account            2. In Last name, type Client Network Access.
                                   3. In User logon name, type CMNetAccess.
                                   4. In Password and Confirm password, type P@ssw0rd.
                                   5. Clear the User must change password at next logon check
                                   box.
                                   6. Select the Password never expires check box.
                                   7. In Description, type Service account used as the network
                                   access account for Configuration Manager Client.

Step 1-9: Install SQL Server 2008 R2
Before installing Configuration Manager, install SQL Server 2008 R2 with SP1 and CU6
for SP1.

  ７ Note

  To enable all SQL Server 2008 R2 features, install the Web Services (IIS) server role
  before installing SQL Server 2008 R2.

To install SQL Server 2008 R2

   1. Start the SQL Server Installation Center.

   2. In the SQL Server Installation Center, in the navigation pane, select Installation.

   3. In the details pane, select New installation or add features to an existing
     installation.

     SQL Server 2008 R2 Setup Wizard starts.

   4. Install SQL Server 2008 R2 using the following information, accepting the defaults
     unless otherwise specified.

                                                                              ﾉ      Expand table

<!-- p.713 -->

On this wizard page    Do this

Setup Support Rules    Select OK.

Product Key            Select Next.

License Terms          Select the I accept the license terms check box, and then select
                       Next.

Setup Support Files    Select Install.

Setup Support Rules    Ensure that no critical results exist for the rules, and then select
                       Next.

Setup Role             Select SQL Server Feature Installation, and select Next.

Feature Selection      1. Select Database Engine Services check box.
                       2. Select Reporting Services check box.
                       3. Select Full-Text Search check box.
                       4. Select Management Tools - Complete check box.
                       5. Select Next.

Installation Rules     Select Next.

Instance               Select Next.
Configuration

Disk Space             Select Next.
Requirements

Server Configuration   1. For SQL Server Agent, in Account Name, type
                       MDT2013\SQLAgent, and in Password, type P@ssw0rd.
                       2. For SQL Server Database Engine, in Account Name, type
                       MDT2013\SQLDBEngine, in Password, type P@ssw0rd.
                       3. For SQL Server Reporting Services, in Account Name, type
                       MDT2013\SQLReport, in Password, type P@ssw0rd.
                       4. Select Next.

Database Engine        Select Add Current User, and select Next.
Configuration

Reporting Services     Select Next.
Configuration

Error Reporting        Select Next.

Installation           Select Next.
Configuration Rules

Ready to Install       Select Install.

Complete               Select Close.

<!-- p.714 -->

  5. Close the SQL Server Installation Center.

To install SQL Server 2008 R2 SP1
  1. In Windows Explorer, go to E:\Source$\SQL2008R2SP1, and double-click
    SQLServer2008R2SP1-KB2528583-x64-ENU.exe.

    The Extracting Files dialog box displays the file-extraction process. When the
    process is complete, the SQL Server 2008 R2 Service Pack 1 Update Setup Wizard
    starts.

  2. Install SQL Server 2008 R2 SP1 using the following information, accepting the
    defaults unless otherwise specified.

                                                                             ﾉ   Expand table

     On this wizard page    Do this

     SQL Server 2008 R2     Select Next.
     update

     License Terms          Select the I accept the license terms check box, and then select
                            Next.

     Select Features        Select Next.

     Check Files In Use     Select Next.

     Ready to update        Select Update.

     Update Progress        The progress is displayed on the wizard page as the update is
                            performed and completes.

     Complete               Select Close.

To install SQL Server 2008 R2 SP1 CU6
  1. In Windows Explorer, go to E:\Source$\SQL2008R2SP1CU6, and double-click
    446622_intl_x64_zip.exe.

    The Microsoft Self-Extractor dialog box appears.

  2. In the Microsoft Self-Extractor dialog box, select Continue.

  3. In the Microsoft Self-Extractor dialog box, in Select the folder where you want to
    unzip the files to, type E:\Source$\SQL2008R2SP1CU6, and then select OK.

<!-- p.715 -->

    ７ Note

    You can select the ellipsis (...) to browse for the E:\Source$\SQL2008R2SP1CU6
    folder.

  The extraction process is displayed. When the process is complete, the completion
  status is displayed.

4. In the Microsoft Self-Extractor dialog box, select OK.

5. In Windows Explorer, go to E:\Source$\SQL2008R2SP1CU6, and double-click
  SQLServer2008R2-KB2679367-x64.exe.

  The Extracting Files dialog box displays the file-extraction process. When the
  process is complete, the SQL Server 2008 R2 Service Pack 1 CU6 Update Setup
  Wizard starts.

6. Install SQL Server 2008 R2 SP1 CU6 using the following information, accepting the
  defaults unless otherwise specified.

                                                                          ﾉ   Expand table

   On this wizard page      Do this

   SQL Server 2008 R2       Select Next.
   update

   License Terms            Select the I accept the license terms check box, and then select
                            Next.

   Select Features          Select Next.

   Check Files In Use       Select Next.

   Ready to update          Select Update.

   Update Progress          The progress is displayed on the wizard page as the update is
                            performed.

   Complete                 Select Close.

  The Install a SQL Server 2008 R2 Update dialog box appears prompting you to
  restart the computer to complete the setup.

7. In the Install a SQL Server 2008 R2 update dialog box, select OK.

8. Restart the computer.

<!-- p.716 -->

   9. After installing SQL Server 2008 R2 SP1 CU6, the SQL Server build number should
     be 10.51.2811.0.

        Tip

       You can verify the SQL Server build number by viewing the SQL Server
       updates applied in the Programs and Features Control Panel item by selecting
       View installed updates.

Step 1-10: Add the Site Server to the Administrators
Security Group
When all computers are in the same forest, manually add the site server computer
account to the local Administrators group on each computer. Complete this step before
configuring the computer as a site system.

To add the site server to the Administrators security group

   1. Select Start, point to Administrative Tools, and then select Active Directory Users
     and Computers.

   2. In the Active Directory Users and Computers console tree, go to
     mdt2013.corp.woodgrovebank.com/Builtin.

   3. In the preview pane, right-click Administrators, and then select Properties.

   4. In the Administrators Properties dialog box, select the Members tab, and then
     select Add.

   5. In the Select Users, Contacts, Computers, or Groups dialog box, select Object
     Types.

   6. In the Object Types dialog box, in Object types, select Computers, and then select
     OK.

   7. In the Select Users, Contacts, Computers, or Groups dialog box, in Enter the
     object names to select, type WDG-MDT-01. Select Check Names, and then select
     OK.

   8. Close any open windows.

Step 1-11: Install Configuration Manager

<!-- p.717 -->

When the other products and technologies have been installed, install Configuration
Manager. Before doing so, however, extend the Active Directory schema so that
computers can locate the distribution points, service locator points, and other server
roles. Also, you can extend the schema after you have installed Configuration Manager.
For more information about how to extend the Active Directory schema for
Configuration Manager, see the section, "Extend the Active Directory Schema," in the
Configuration Manager Documentation Library, which is installed with Configuration
Manager.

After extending the Active Directory schema, install Configuration Manager. The
configuration of WDG-MDT-01 supports Configuration Manager for this sample. The
configuration of computers in the production network may vary. To find out more about
the prerequisites for installing Configuration Manager, see Supported Configurations for
Configuration Manager.

To install Configuration Manager
   1. Start the System Center 2012 R2 Configuration Manager Setup splash screen.

   2. On the System Center 2012 R2 Configuration Manager Setup splash screen, select
     the Install link.

     The Microsoft System Center 2012 R2 Configuration Manager Setup Wizard starts.

   3. Complete the Microsoft System Center 2012 R2 Configuration Manager Setup
     Wizard using the following information, accepting the defaults unless otherwise
     specified.

                                                                             ﾉ   Expand table

      On this wizard page            Do this

      Before You Begin               Select Next.

      Getting Started                Select Next.

      Product Key                    In Enter your 25-character product key, type product_key
                                     (where product_key is your product key for Configuration
                                     Manager).

      Microsoft Software License     Select the I accept these license terms check box, and
      Terms                          then select Next.

      Prerequisite Licenses          1. In the Microsoft SQL Server 2008 R2 Express section,
                                     select the I accept these License Terms check box.
                                     2. In the Microsoft SQL Server 2008 Native Client

<!-- p.718 -->

   On this wizard page              Do this

                                    section, select the I accept these License Terms check
                                    box.
                                    3. In the Microsoft Silverlight 4 section, select the I
                                    accept these License Terms and automatic updates of
                                    Silverlight check box.
                                    4. Select Next.

   Update Prerequisite              In Download and use the latest updates. Updates will be
   Components                       saved to the following location, type E:\CMDownloads,
                                    and then select Next.

   Server Language Selection        Select Next.

   Client Language Selection        Select Next.

   Site and Installation Settings   1. In Site code, type NYC.
                                    2. In Site name, type New York City Site.
                                    3. Select Next.

   Primary Site Installation        1. Select Install the primary site as a stand-alone site.
                                    2. Select Next.
                                    The Configuration Manager dialog box appears,
                                    confirming that you want to install this site as a stand-
                                    alone site.
                                    3. In the Configuration Manager dialog box, select Yes.

   Database Information             Select Next.

   SMS Provider Settings            Select Next.

   Client Computer                  Select Configure the communication method on each
   Communication Settings           site system role, and then select Next.

   Site System Roles                Select Next.

   Customer Experience              1. Select the appropriate participation in the Customer
   Improvement Program              Experience Improvement program for your organization.
   Configuration                    2. Select Next.

   Settings Summary                 Select Next.

   Prerequisite Check               Select Begin Install.

   Install                          1. Monitor the installation process until it is complete.
                                    2. Select Close.

4. Close all open windows and dialog boxes.

  When the wizard is complete, Configuration Manager is installed.

<!-- p.719 -->

Step 1-12: Configure the Network Access Account
The Configuration Manager client needs an account to provide credentials when
accessing the Configuration Manager distribution points, MDT deployment shares, and
shared folders. This account is called the Network Access account. The CMNetAccess
account was created earlier in the process to use as the Network Access account.

To configure the Network Access account

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select
     Administration.

   3. In the Administration workspace, go to Overview/Site Configuration/Sites.

   4. In the preview pane, select NYC - New York City Site.

   5. On the Ribbon, select Settings, select Configure Site Components, and then select
     Software Distribution.

   6. In the Software Distribution Component Properties dialog box, select the
     Network Access Account tab.

   7. In Network Access Account, select Specify the account that accessed network
     locations, select Set, and then select New Account.

     The Windows User Account dialog box appears.

   8. Complete the Windows User Account dialog box using the following information,
     and then select OK.

                                                                       ﾉ     Expand table

      For this                         Do this

      User name                        Type MDT2013\CMNetAccess.

      Password                         Type P@ssw0rd.

      Confirm password                 Type P@ssw0rd.

   9. In the Software Distribution Component Properties dialog box, select OK.

<!-- p.720 -->

 10. Close any open windows.

Step 1-13: Configure the Configuration Manager Site
Boundaries and Boundary Groups
The Configuration Manager client needs to know the boundaries for the site. Unless the
site boundaries are specified, the client assumes that the computer running
Configuration Manager is in a remote site. Add a site boundary based on the IP subnet
that WDG-MDT-01, WDG-REF-01, and WDG-CLI-01 use. Then add the site boundary to a
site boundary group.

To create a Configuration Manager site boundary

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select
     Administration.

   3. In the Administration workspace, go to Overview/Hierarchy
     Configuration/Boundaries.

   4. On the Ribbon, select Create Boundary.

     The Create Boundary dialog box opens.

   5. Complete the Create Boundary dialog box using the following information, and
     then select OK.

       ７ Note

       For this sample, the site boundary is specified by network address. However,
       you can also specify site boundaries using an AD DS site name or an IP
       address range.

                                                                       ﾉ      Expand table

      For this      Do this

      Description   Type IP Subnet Boundary.

      Type          Select IP subnet.
