---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 641-680"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0641-0680
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0641-0680
family: sccm
documentKind: "doc"
abstract: "Add the Custom Code as a Task Sequence Step Custom deployment code can be called directly from any point within a task sequence; this gives access to the usual task sequence rules and options. To add the custom deployment code to an existing task sequence 1. Copy the custom depl"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 641-680

<!-- p.641 -->

Add the Custom Code as a Task Sequence Step
Custom deployment code can be called directly from any point within a task sequence;
this gives access to the usual task sequence rules and options.

To add the custom deployment code to an existing task sequence

   1. Copy the custom deployment code to the deployment_share\Scripts folder (where
     deployment_share is the fully qualified path to the deployment share).

   2. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   3. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share to configure).

   4. In the details pane, select task_sequence (where task_sequence is the name of the
     task sequence that runs the custom code).

   5. In the Actions pane, select Properties.

   6. In the task_sequenceProperties dialog box, select the Task Sequence tab.

   7. In the console tree, go to group (where group is the group to add the task
     sequence step).

   8. Select Add, select General, and then select Run Command Line.

   9. In the console tree, select Run Command Line, and then select the Properties tab.

 10. In the Name box, type name (where name is a descriptive name of the custom
     code).

 11. On the Properties tab, in the Command line box, type command_line (where
     command_line is the command to run the custom code—for example, cscript.exe
     %SCRIPTROOT%\CustomCode.vbs).

 12. In the Start in box, type path (where path is the fully qualified path to the working
     folder of the custom code; typically, this is the same path specified in the
     Command line box), and then select OK.

     The newly created task sequence step appears in the list of task sequence steps.

Run Custom Code as a User Exit Script

<!-- p.642 -->

It also is possible to run the custom code as a user exit script from CustomSettings.ini
using the UserExit directive. This provides a mechanism for information to be passed
into the CustomSettings.ini rule validation process and provides a dynamic update of
MDT properties

For more information on user exit scripts and the UserExit directive, see the section,
"User Exit Scripts in the CustomSettings.ini File", in the MDT document Using the
Microsoft Deployment Toolkit.

Installing Device Drivers Using Various
Installation Methods
In this scenario, you use MDT to deploy an operating system to different types of
hardware. As part of the deployment process, identify and install device drivers so that
each hardware type will function correctly. There are two main types of device drivers;
each must be handled differently during the deployment process:

     Device drivers that contain an .inf file that can be used to import the device driver
     into the Deployment Workbench

     Device drivers that are packaged as an application, and that must be installed as an
     application

     Using MDT, you can handle both types of drivers as part of an operating system
     deployment.

     Install device drivers by:

     Determining methods for installing each device driver as described in Determining
     Which Method to Use to Install a Device Driver

     Using the out-of-box drivers method as described in Installing Device Drivers
     Using the Out-of-Box Drivers Method

     Installing them as applications as described in Installing Device Drivers as
     Applications

     This scenario assumes that MDT is running on a deployment server.

Determining Which Method to Use to Install a Device
Driver
Hardware manufacturers release device drivers in one of two forms:

<!-- p.643 -->

     As a package that you can extract and that contains .inf files used to import the
     driver into the Deployment Workbench

     As an application that you must install using traditional application installation
     processes

     Device driver packages that can be extracted to access .inf files can use the MDT
     automatic driver detection and installation process by first importing the driver
     into the Out-of-Box Drivers node in the Deployment Workbench.

     Device driver packages that cannot be extracted to isolate .inf files or those that do
     not work correctly without first being installed using an application installer such
     as an MSI or Setup.exe file can use the MDT Install Application feature and install
     the device driver during the deployment process just as for any normal application.

Installing Device Drivers Using the Out-of-Box Drivers
Method
You can import device driver packages that include an .inf file to the Deployment
Workbench and install them automatically as part of the deployment process. To
implement this type of device driver deployment, first add the device driver to the
Deployment Workbench.

To add the device driver to the Deployment Workbench

   1. Download the device drivers required for the hardware types to be deployed, and
     extract the device driver package to a temporary location.

   2. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   3. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Out-of-Box Drivers (where
     deployment_share is the name of the deployment share to configure).

   4. In the Actions pane, select Import Drivers.

     The Import Device Driver Wizard starts.

   5. On the Specify Directory page, in the Drive source directory section, select Browse
     to go to the folder that contains the new device drivers, and then select Next.

       ７ Note

<!-- p.644 -->

        The New Device Driver Wizard will search all subdirectories of the driver
        source directory; therefore, if there are multiple drivers to install, extract them
        into folders within the same root directory, and then set the driver source
        directory as the root directory that holds all of the driver source folders.

   6. On the Summary page, verify that the settings are correct, and then select Next to
     import the drivers into the Deployment Workbench.

   7. On the Confirmation page, select Finish.

     If the device drivers contain boot-critical drivers such as mass storage or network
     class drivers, the deployment share must next be updated to generate a new
     LiteTouch_x86 and LiteTouch_x64 boot environment that contains the new drivers.

     To add device drivers to the Lite Touch Windows PE images

   8. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   9. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

 10. In the Actions pane, select Update Deployment Share.

     The Update Deployment Share Wizard starts.

 11. On the Options page, select the desired options for updating the deployment
     share, and then select Next.

 12. On the Summary page, verify that the details are correct, and then select Next.

 13. On the Confirmation page, select Finish.

Installing Device Drivers as Applications
Device drivers that are packaged as applications and that you cannot extract to a folder
containing an .inf file, in addition to driver files, should be added to the Deployment
Workbench as an application for installation during the deployment process.

Applications can be specified as a task sequence step or specified in CustomSettings.ini;
however, device driver applications should be installed only when the task sequence is
run on a computer with the devices. To ensure this, run the task sequence step for
deploying the relevant device driver applications as a conditional task sequence step.

<!-- p.645 -->

The conditional criteria can be specified for running the task sequence step using WMI
queries for the device on the target computer.

Add the Device Driver Application to the Deployment Workbench

Each device driver application must first be imported into the Deployment Workbench.

  ７ Note

  Configure whether the application should is visible during deployment on the
  Properties dialog box of any application by selecting or clearing the Hide this
  application in the Deployment Wizard check box. Repeat this process for each
  device driver application used during deployment.

To add the device driver application to the Deployment Workbench

   1. Download the device driver application, and save it to a temporary location.

   2. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   3. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Applications (where
     deployment_share is the name of the deployment share to configure).

   4. In the Actions pane, select New Application.

     The New Application Wizard starts.

   5. On the Application Type page, select Application with source files, and then
     select Next.

   6. On the Details page, type relevant details about the application, and then select
     Next.

   7. On the Source page, in the Source directory section, select Browse to go to, and
     then select the directory that contains the device driver application source files.
     Select OK.

   8. Select Next.

   9. On the Destination page, type a name for the destination directory, and then
     select Next.

<!-- p.646 -->

 10. On the Command Details page, in the Command line section, type the command
     that allows silent installation of the device driver application.

 11. On the Summary page, verify the settings are correct, and then select Next to
     import the device driver application into the Deployment Workbench.

 12. On the Confirmation page, select Finish.

     After the applications are imported into the Deployment Workbench, add them to
     the deployment process using the appropriate logic to ensure that the application
     installs only when running on the correct hardware. There are different methods
     for achieving this:

     Specify the device driver application as part of a deployment task sequence.

     Specify the device driver application in CustomSettings.ini.

     Specify the device driver application in the MDT DB.

     Each approach is discussed in more detail in the following sections.

Specify the Device Driver Application as Part of a Task Sequence
The first method for adding a device driver application to the deployment process is to
use a task sequence to add steps for each device driver application.

There are two main approaches for managing device driver applications in the task
sequence:

     Create a new task sequence group for each hardware model, and then add a query
     to run that group of actions if the computer matches a specific hardware type.

     Create a task sequence group for hardware-specific applications, and then add
     queries for each task sequence action so that each task sequence step is evaluated
     against the hardware type and will run only if a match is found.

     To create a new task sequence group for each type of hardware

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share to configure).

<!-- p.647 -->

 3. In the details pane, select task_sequence (where task_sequence is the deployment
   task sequence that will be required to install the device driver application).

 4. In the Actions pane, select Properties.

 5. In the task_sequenceProperties dialog box, on the Task Sequence tab, in the
   details pane, go to State Restore/Windows Update (Pre-Application Installation).

 6. On the Task Sequence tab, select Add, and then select New Group.

   This creates a new task sequence group in the task sequence. Use this new task
   sequence group to create the steps for installing the hardware-specific device
   driver applications.

 7. In the details pane, select New Group.

 8. On the Properties tab, in the Name box, type group_name (where group_name is
   the name of the group; for example, Hardware Specific Applications - Dell
   Computer Corporation).

 9. On the Options tab, select Add, and then select Query WMI.

10. In the Task Sequence WMI Condition dialog box, type the following details:

         In the WMI namespace box, type root\cimv2.

         In the WQL query box, type a WMI Query Language (WQL) query using the
         Win32_ComputerSystem class to ensure that the application is installed only
         for a specific application type—for example:

         Select * FROM Win32_ComputerSystem WHERE Model LIKE
         %hardware_model% AND Manufacturer LIKE %hardware_manufacturer%

         In this example, hardware_model is the name of the computer model (such as
         Latitude D620) and hardware_manufacturer is the name of the computer
         make (such as Dell Corporation).

         The % symbol is a wildcard character that is included in the names to allow
         administrators to return any computer models or manufactures that contains
         the value specified for hardware_model or hardware_manufacturer.

         For more information about WMI and WQL queries, see the section, "Add
         WMI Queries to Task Sequence Step Conditions", in the MDT document Using
         the Microsoft Deployment Toolkit, and see Querying with WQL.

<!-- p.648 -->

 11. Select OK to submit the query, and then select OK to submit changes to the task
     sequence.

  ７ Note

  This process must be repeated for each hardware type of each device driver
  application to be installed.

After the hardware-specific task sequence groups have been created, device driver
applications can be added to each group.

To add device driver applications to hardware-specific task sequence groups

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences (where
     deployment_share is the name of the deployment share to configure).

   3. In the details pane, select task_sequence (where task_sequence is the deployment
     task sequence that will be required to install the device driver application).

   4. In the Actions pane, select Properties.

   5. In the task_sequenceProperties dialog box, select the Task Sequence tab.

   6. In the details pane, go to State Restore/hardware_specific_group (where
     hardware_specific_group is the name of the hardware-specific group where the task
     sequence step will be added to install the device driver application).

   7. On the Task Sequence tab, select Add, select General, and then select Install
     Application.

     The Install Application task sequence step appears in the details pane.

   8. In the details pane, select Install Application.

   9. On the Properties tab, select Install a single application, and in the Application to
     install list, select hardware_application (where hardware_application is the
     application for installing the hardware-specific application).

  ７ Note

<!-- p.649 -->

  This process must be repeated for each device driver application that needs to be
  used during a deployment.

Specify the Device Driver Application in CustomSettings.ini

When an LTI or ZTI deployment begins, one of the first actions to be completed is the
processing of the BootStrap.ini and CustomSettings.ini control files. Both of these files
contain rules that can be used to dynamically customize the deployment.

Because of the way MDT processes the CustomSettings.ini file, you can use it to add
applications based on specific conditions. This logic will be used to add device driver-
specific applications during deployment based on specific hardware types. Applications
are referenced in CustomSettings.ini by the application's GUID, located in the
Applications.xml file in the deployment share.

To locate an imported application's GUID

   1. In the deployment share of the deployment server, open the Control folder—for
        example, D:\Production Deployment Share\Control.

   2. Locate and open the Applications.xml file.

   3. Locate the required application.

   4. Locate the application GUID by locating the line enclosed in the application <guid>
        tags; for example, <application guid={c303fa6e-3a4d-425e-8102-77db9310e4d0}> .

        As part of the initialization process, both the LTI and ZTI process gather
        information about the computer on which it is running. As part of this process,
        WMI queries are performed and the values from the Win32_ComputerSystem
        class for make and manufacturer are populated as variables %Make% and
        %Model%, respectively.

        These values can be used during processing the CustomSettings.ini file to
        dynamically read sections of the file depending on the make and model detected.
        The following sample shows an example of the CustomSettings.ini file.

        Sample CustomSettings.ini Configured for a Hardware-Specific Application
        Installation

  ini

  [Settings]
  Priority=Make, Default

<!-- p.650 -->

  Properties=MyCustomProperty

  [Default]
  OSInstall=Y

  [Dell Computer Corporation]
  Subsection=Dell-%Model%

  [Dell-Latitude D620]
  MandatoryApplications001={1D7DF331-47B7-472C-87B3-442597EC2F7D}

  [Dell-Latitude D610]
  MandatoryApplications001={c303fa6e-3a4d-425e-8102-77db9310e4d0}

Use the following properties to specify applications in CustomSettings.ini:

     Applications. This property can be used when deployment administrators do not
     want to present an application wizard as part of the deployment process by
     specifying SkipApplications=YES in CustomSettings.ini.

     MandatoryApplications. This property can be used if deployment administrators
     want to present the application wizard during the deployment to allow
     deployment engineers to select additional applications to be installed during the
     deployment.

     If the application wizard is used without the MandatoryApplications property (for
     example, SkipApplications=NO), it will overwrite applications specified by the
     Applications property.

     The previous sample shows how to use the %Make% and %Model% variable
     values to dynamically manipulate how the applications list is built. The values for
     the make and model of each type of hardware can be located using one of the
     following methods:

     The System Information tool. Use the System Summary node in this tool to
     identify the System Manufacturer (make) and System Model (model).

     Windows PowerShell. Use the Get-WMIObject -class Win32_ComputerSystem
     cmdlet to determine the make and model of the computer.

     Windows Management Instrumentation Command Line. Use CSProduct Get
     Name, Vendor to return the name (model) and vendor (make) of the computer.

     To modify CustomSettings.ini to add hardware-specific logic

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

<!-- p.651 -->

 2. In the Deployment Workbench console tree, go to Deployment
   Workbench/Deployment Shares/deployment_share (where deployment_share is the
   name of the deployment share to configure).

 3. In the Actions pane, select Properties.

 4. Select the Rules tab.

 5. Information typed on this tab is stored in the CustomSettings.ini file. Modify the
   CustomSettings.ini file entries to add logic for each hardware model that has a
   device driver-specific application, as described in Specify the Device Driver
   Application as Part of a Task Sequence.

 6. Select OK to submit the changes.

 7. In the details pane, select deployment_share (where deployment_share is the name
   of the deployment share to configure).

 8. In the Actions pane, select Update Deployment Share.

   The Update Deployment Share Wizard starts.

 9. On the Options page, select the desired options for updating the deployment
   share, and then select Next.

10. On the Summary page, verify the details are correct, and then select Next.

11. On the Confirmation page, select Finish.

   By default, all available applications are displayed in the Windows Deployment
   Wizard during an LTI deployment. Because device driver-specific applications are
   applicable only to specific hardware types, you might not want them displayed all
   the time. By specifying the device driver-specific application package in
   CustomSettings.ini, the application can be hidden using the Hide the application
   in the Deployment Wizard option in the application configuration.

   To hide an application in the Deployment Wizard

12. Select Start, and then point to All Programs. Point to Microsoft Deployment
   Toolkit, and then select Deployment Workbench.

13. In the Deployment Workbench console tree, go to Deployment
   Workbench/Deployment Shares/deployment_share/Applications (where
   deployment_share is the name of the deployment share to configure).

<!-- p.652 -->

 14. In the details pane, select device_driver_application (where
     device_driver_application is the application to be hidden from the Deployment
     Wizard).

 15. In the Actions pane, select Properties.

 16. On the General tab, select the Hide the application in the Deployment Wizard
     check box.

 17. Select Apply, and then close the Properties dialog box.

Specify the Device Driver Application in the MDT DB

The MDT DB is a database version of the CustomSettings.ini file and can be queried at
deployment time for information to be used during the deployment. For more
information about using the MDT DB, see "Selecting the Methods for Applying
Configuration Settings".

When querying the MDT DB at deployment time, three methods are available for
identifying the target computer:

     Search for the individual computer (using the MAC address, asset tag, or similar).

     Search for the location of the computer (using the default gateway).

     Search for the make and model of the computer (using WMI manufacturer or
     make and model queries).

     For each database entry you create, you can specify deployment properties,
     applications, whether to use Configuration Manager packages, and administrators.
     By creating make and model entries in the database, you can add the required
     hardware-specific device driver applications.

     To create entries in the MDT DB to allow installation of device driver applications

  ７ Note

  Repeat this process for each hardware make and model that requires a device
  driver application.

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

<!-- p.653 -->

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Advanced
     Configuration/Database/Make and Model (where deployment_share is the name of
     the deployment share to configure).

   3. In the Actions pane, select New.

   4. In the Properties dialog box, on the Identity tab, in the Make box, type
     make_name (where make_name is an easily identified name to associate with the
     manufacturer of the target computer).

   5. In the Model box, type model_name (where model_name is an easily identified
     name to associate with the model of the target computer).

   6. On the Applications tab, add each of the device driver applications required for
     that model of hardware.

Initiating MDT Using Windows Deployment
Services
Windows Server 2008 uses Windows Deployment Services as an updated and
redesigned version of Remote Installation Services, the default deployment tool in
Windows Server 2003 with SP2. Using Windows Deployment Services, you can deploy
Windows operating systems—particularly Windows 7, Windows Server 2008 or later
operating systems—across a network using either a computer's PXE-enabled network
adapter or boot media.

Before deploying Windows Deployment Services, determine which of the following
integration options best suits your environment:

     Option 1. Boot computers in PXE to initiate the LTI process.

     Option 2. Deploy an operating system image from the Windows Deployment
     Services image store.

     Option 3. Use multicasting with MDT and the Windows Server 2008 Windows
     Deployment Services server role.

Option 1: Boot Computers in PXE to Initiate the LTI
Process

<!-- p.654 -->

Help minimize the cost of managing operating system deployments by starting the MDT
deployment process using Windows Deployment Services in conjunction with Dynamic
Host Configuration Protocol. This removes the requirement of creating and delivering
bootable media to each target computer.

Create and Import the Deployment Workbench Windows PE Image
into Windows Deployment Services
When creating a new MDT deployment share or modifying an existing MDT deployment
share, you can create a customized Windows PE boot image. When the deployment
share is updated, the Windows PE boot image is automatically generated and updated
with information about the deployment share, and it will inject any additional drivers or
components specified during the deployment share configuration.

The Windows PE boot image is generated as both an ISO image file, which you can write
to a CD or DVD, and a bootable WIM file. You can import the WIM file to Windows
Deployment Services so that computers that can boot in PXE can download and run the
LTI Windows PE boot image across a network used to initialize an installation.

To create a bootable Windows PE image in the Deployment Workbench

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Properties.

     In the deployment_shareProperties dialog box, select the Windows PE platform
     Settings tab (where platform is the architecture of the Windows PE image to be
     configured).

   4. In the Lite Touch Boot Image Settings area, select the Generate a Lite Touch
     bootable RAM disk ISO image check box.

   5. Select the Windows PE platform Components tab (where platform is the
     architecture of the Windows PE image to be configured).

   6. In the Driver Injection section, select the appropriate driver types to include.

        ７ Note

<!-- p.655 -->

      This step is not necessary if Windows PE already includes the necessary device
      drivers.

 7. In the Driver Injection section, in the Selection profile list, select the appropriate
   driver selection profile.

 8. In the Properties dialog box, select OK.

      ７ Note

      This step is not necessary if Windows PE already includes the necessary device
      drivers.

 9. In the details pane, select deployment_share (where deployment_share is the name
   of the deployment share to configure).

10. In the Actions pane, select Update Deployment Share.

   The Update Deployment Share Wizard starts.

11. On the Options page, select the desired options for updating the deployment
   share, and then select Next.

12. On the Summary page, verify the details are correct, and then select Next.

13. On the Confirmation page, select Finish.

   When this process is complete, the Boot folder in the deployment share will
   contain a number of boot images—for example:

   D:\Production Deployment Share\Boot\LiteTouchPE_x64.iso

   D:\Production Deployment Share\Boot\LiteTouchPE_x64.wim

   D:\Production Deployment Share\Boot\LiteTouchPE_x86.iso

   D:\Production Deployment Share\Boot\LiteTouchPE_x86.wim

   You can write the ISO files that have been generated directly to CD or DVD or use
   them to initialize the LTI process on new hardware. You can import the boot WIM
   files into Windows Deployment Services, as well, so that new computers can
   initialize the LTI deployment process without requiring any physical media.

   To import the Windows PE image into Windows Deployment Services

<!-- p.656 -->

 14. Start the Windows Deployment Services console, and then connect to Windows
     Deployment Services.

 15. In the console tree, right-click Boot Images, and then select Add Boot Image.

 16. Browse to the WIM image to be imported—for example, D:\Production
     Deployment Share\Boot\LiteTouchPE_x86.wim.

 17. The import process automatically reads the metadata from the boot image, but the
     Image Name and Image Description values can also be edited; the Image Name
     affects the boot option information displayed by Windows Boot Manager when
     the client boots in PXE.

 18. When the boot image has been imported, any computer that boots in PXE and
     receives a reply from Windows Deployment Services will be able to download the
     LTI boot image and initiate an LTI installation.

     Installing and configuring Windows Deployment Services is not covered in this
     guide. For additional information about Windows Deployment Services, see the
     Windows Deployment Services Guide.

Use Windows Deployment Services to Automatically Detect the
Deployment Server

An additional option is available when using Windows Deployment Services to host
MDT boot images when the MDT deployment share is hosted on the same server as
Windows Deployment Services.

When a PXE client loads the MDT boot image, the name of the Windows Deployment
Services server hosting the boot image is captured and placed in the MDTProperty
WDSServer. You can then reference this property in the boot image's BootStrap.ini file
and in the deployment share's CustomSettings.ini file by the DeployRoot property.
Doing so results in a client that boots from Windows Deployment Services automatically
using the deployment share hosted on the Windows Deployment Services server. This
eliminates the need to specify a server name in any configuration file.

To set the local Windows Deployment Services server as the deployment server

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Advanced

<!-- p.657 -->

     Configuration/Database (where deployment_share is the name of the deployment
     share to configure).

  3. In the Actions pane, select Properties.

  4. Select the Rules tab.

     Information typed on this tab is stored in the CustomSettings.ini file.

  5. Configure the DeployRoot property to use the %WDSServer% variable—for
     example, DeployRoot=\\%WDSServer%\Deployment$.

  6. Select Edit Bootstrap.ini.

  7. Configure BootStrap.ini to use the %WDSServer% property by adding or changing
     the DeployRoot value to DeployRoot=\\%WDSServer%\Deployment$.

  8. On the File menu, select Save to save the changes to the BootStrap.ini file.

  9. Select OK.

     The deployment share needs to be updated.

 10. In the details pane, select deployment_share (where deployment_share is the name
     of the deployment share to configure).

 11. In the Actions pane, select Update Deployment Share.

     The Update Deployment Share Wizard starts.

 12. On the Options page, select the desired options for updating the deployment
     share, and then select Next.

 13. On the Summary page, verify the details are correct, and then select Next.

 14. On the Confirmation page, select Finish.

 15. Import the updated boot WIM into Windows Deployment Services.

Option 2: Deploy an Operating System Image from the
Windows Deployment Services Store
If you are already using Windows Deployment Services for operating system
deployment, extend the functionality of MDT by configuring it to reference the Windows
Deployment Services operating system images already in use rather than using its own
store and to supplement Windows Deployment Services deployments with driver

<!-- p.658 -->

management, application deployment, update installation, rule processing, and other
MDT functionality. After MDT has reference a Windows Deployment Services operating
system image, you can treat it like any operating system that has been staged to an
MDT deployment share.

To reference a Windows Deployment Services operating system image

  ７ Note

  The following steps require that at least one operating system image has previously
  been imported into the Windows Deployment Services server.

   1. Update MDT to be able to access Windows Deployment Services images by
     copying the following files from the Sources folder of the Windows media to the
     C:\Program Files\Microsoft Deployment Toolkit\bin folder on the Windows
     Deployment Services server:

           Wdsclientapi.dll

           Wdscsl.dll

           Wdsimage.dll

           Wdstptc.dll (this is only applicable if copying from the Windows Server 2008
           source directories)

       ７ Note

       The Windows source directory being used must match the platform of the
       operating system running on the computer where MDT is installed.

   2. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   3. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Operating Systems (where
     deployment_share is the name of the deployment share to configure).

   4. In the Actions pane, select Import Operating System.

     The New OS Wizard starts.

<!-- p.659 -->

   5. On the OS Type page, select Windows Deployment Services images, and then
     select Next.

   6. On the WDS Server page, type the name of the Windows Deployment Services
     server to be referenced—for example, WDSSvr001—and then select Next.

   7. On the Summary page, verify the settings are correct, and then select Next.

   8. On the Confirmation page, select Finish.

     All of the images available on the Windows Deployment Services server will now
     be available to MDT task sequences.

  ７ Note

  Importing images from Windows Deployment Services does not copy the source
  files from the Windows Deployment Services server to the deployment share. MDT
  continues to use the source files from their original location.

Option 3: Use Multicasting with MDT and the Windows
Server 2008 Windows Deployment Services Role
With the release of Windows Server 2008, Windows Deployment Services was enhanced
to support the deployment of images using multicast transmissions. MDT also includes
updates to integrate MDT with Windows Deployment Services multicasting.

In addition, an updated Windows Automated Installation Kit (Windows AIK), version 1.1,
includes Wdsmcast.exe. This allows multicast sessions to be joined manually and allows
the client launching Wdsmcast.exe to copy files from an active multicast session.

The LTIApply.wsf script uses Wdsmcast.exe when it accesses operating system source
files from the deployment share. LTIApply.wsf looks for Wdsmcast.exe on the
deployment share either in the deployment_share\Tools\x86 or the
deployment_share\Tools\x64 folder (where deployment_share is the name of the file
system folder that contains the deployment share), depending on the version of
Windows PE that is running.

When LTIApply.wsf runs it will always attempt to access and download WIM images
from an existing multicast stream, but it will fall back to a standard file copy if a
multicast stream does not exist.

  ７ Note

<!-- p.660 -->

  This process applies only to WIM image files.

The deployment server prerequisites for preparing for MDT multicasting are:

     The deployment server must be running Windows Server 2008 or later

     The Windows Deployment Services role must be installed from the Server
     Management console

     Windows AIK 1.1 for Windows Server 2008 must be installed

     MDT must be installed

     As with any deployment using MDT, at least one operating system WIM image
     must have been imported, either as a full set of source files or as a custom image
     with setup files

  ７ Note

  It is important to use the latest version of Windows AIK for multicasting; the copy
  of Windows PE included in earlier versions of Windows AIK—for example, Windows
  AIK 1.0—does not support downloading from a multicast server.

To configure MDT for multicasting from an existing deployment share

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Properties.

   4. On the General tab, select the Enable multicast for this deployment share
     (requires Windows Server 2008 Windows Deployment Services) check box.

   5. Select OK.

   6. In the Actions pane, select Update Deployment Share.

     The Update Deployment Share Wizard starts.

   7. On the Options page, select the desired options for updating the deployment
     share, and then select Next.

<!-- p.661 -->

 8. On the Summary page, verify the details are correct, and then select Next.

 9. On the Confirmation page, select Finish.

   The deployment share is now configured for Windows Deployment Services
   multicast transmission.

   This process creates an Auto-Cast Windows Deployment Services multicast
   transmission that directly uses the existing MDT deployment share. MDT does not
   create Scheduled-Cast transmissions. Also note that no additional images are
   imported into Windows Deployment Services and that it is not possible to use
   multicast for boot images, because the multicast client cannot be loaded until after
   Windows PE is running.

   To verify that the multicast transmission has been generated in Windows
   Deployment Services

10. Select Start, point to Administrative Tools, and then select Windows Deployment
   Services.

11. In the Windows Deployment Services console tree, right-click Servers, and then
   select Add Server.

12. In the Add Servers(s) dialog box, select Local computer, and then select OK.

13. In the Windows Deployment Services console tree, select Servers, then select
   server_name (where server_name is the name of the computer running Windows
   Deployment Services). Select Multicast Transmissions.

14. In the details pane, a new Auto-Cast transmission for the deployment share will be
   listed—for example, BDD Share Deployment$.

15. Verify that the status of the BDD Share Deployment$ Auto-Cast transmission is set
   to Active.

   After a computer has been deployed, verify that the operating system was
   downloaded from a multicast transmission by examining the BDD.log file in the
   \Windows\Temp\DeploymentLogs folder.

   There will be two entries in the logs folder, both beginning with Multicast transfer;
   check them to verify that the transfer was successful. For more information on
   multicast transmissions with MDT and Windows Deployment Services, see the
   section, "Enable Windows Deployment Services Multicast Deployment for LTI
   Deployments", in the MDT document Using the Microsoft Deployment Toolkit.

<!-- p.662 -->

Performing Staged Deployments Using MDT
(OEM Preload)
In many organizations, computers are loaded with the operating system image before
deployment to the production network. In some instances, loading the operating system
image is performed by a team within the organization that is responsible for building
the computers in a staging environment. In other instances, loading the operating
system image is performed by the computer hardware vendor, also known as an original
equipment manufacturer (OEM).

  ７ Note

  The OEM preload process is supported in MDT only for deployments performed
  using LTI. For Configuration Manager, use the prestaged media feature.

Overview of the OEM Preload Process in MDT
The OEM preload process is divided into three phases:

     Phase 1. Create a media-based image of the reference computer to be applied in
     the staging environment.

     Phase 2. Apply the reference computer image to the target computer in a staging
     environment.

     Phase 3. Complete deployment of the target computer in the production
     environment.

     Phase 1 and Phase 3 are typically performed by the deployment organization.
     Depending on the use of the OEM preload process in the organization, Phase 2
     may be performed by the organization or by the computer hardware vendor that
     supplies the computers. If the organization performs Phase 2, then the staging
     environment is within the organization. If an OEM performs Phase 2, then the
     staging environment is in the OEM's environment.

Overview of MDT Configuration Files in the OEM Preload Process
Separate MDT configuration files (CustomSettings.ini and Bootstrap.ini) are used by the
task sequences run during Phase 1 and Phase 3 of the OEM preload process. However,
both configuration files exist simultaneously in different folder structures.

<!-- p.663 -->

In the first phase, the configuration files are used during the creation of the reference
computer and are stored in the folder specific to the task sequence used in that phase.
The configuration files used in the third and last phase of the OEM preload process are
stored in the folder that is specific to the task sequence used in that phase.

When making modifications to the configuration files, ensure that changes to the
configuration file are made that corresponds to the appropriate task sequence in each
OEM preload process phase.

Overview of MDT Log Files in the OEM Preload Process

Separate MDT log files are generated during Phase 1 and Phase 3 of the OEM preload
process:

     The MDT log files for Phase 1 are stored in the C:\MININT and C:\SMSTSLog
     folders.

     The MDT log files for Phase 3 are stored in the %WINDIR%\System32\CCM\Logs
     folder for x86-based deployments or in the %WINDIR%\SysWow64\CCM\Logs
     folder for x64-based deployments.

     Use the appropriate folder when diagnosing or troubleshooting MDT-related
     deployment problems.

Staged Deployments Using LTI
For LTI deployments, perform the OEM preload process using a Removable media
(Media) deployment share type. Other deployment share types are not supported for
the OEM preload process.

To perform the OEM preload process, create a task sequence based on the Litetouch
OEM Task Sequence task sequence template, in addition to any task sequences that will
be used to deploy the target operating system. Then, create a Removable media (Media)
deployment share that will ultimately create an ISO file of the deployment share
contents, specifically the LiteTouchPE_x86.iso file or LiteTouchPE_x64.iso file (based on
the target computer's processor platform). The deployment share update process also
creates a folder structure that can be used to create Universal Disk Format media.

LTI OEM Preload Process—Phase 1: Create a Media-Based Image
The deployment organization performs the first phase in the OEM preload process. The
final deliverable of this phase is a bootable image (such as an ISO file) or media (such as

<!-- p.664 -->

a DVD) that is sent to the OEM or to the staging environment within the deployment
organization. Most of these steps are performed in the Deployment Workbench.

To create a media-based image for delivery to the OEM or to the staging environment
within the deployment organization

  1. Populate the following nodes for the deployment share in the Deployment
     Workbench:

          Operating Systems

          Applications

          Packages

          Out-of-Box Drivers

          For more information about performing this step, see the section, "Managing
          Deployment Shares in the Deployment Workbench", in the MDT document
          Using the Microsoft Deployment Toolkit.

  2. Create a new task sequence based on the Litetouch OEM Task Sequence task
     sequence template in the Deployment Workbench.

     For more information about performing this step, see the section, "Configuring
     Task Sequences in the Deployment Workbench", in the MDT document Using the
     Microsoft Deployment Toolkit.

  3. Create one or more task sequences that will be used to deploy the target
     operating system on the target computer after deployment in the production
     environment.

     For more information about performing this step, see the section, "Configuring
     Task Sequences in the Deployment Workbench", in the MDT document Using the
     Microsoft Deployment Toolkit.

  4. Create a selection profile that includes the applications, operating systems, drivers,
     packages, and task sequences required for the OEM deployment.

     For more information about performing this step, see the section, "Manage
     Selection Profiles", in the MDT document Using the Microsoft Deployment Toolkit.

  5. Create deployment media.

     For more information on performing this step, see the section, "Manage LTI
     Deployment Media", in the MDT document Using the Microsoft Deployment Toolkit.

<!-- p.665 -->

   6. Update the deployment media created in the Deployment Workbench in the
     previous step.

     When you update the deployment media, the Deployment Workbench creates the
     LiteTouchMedia.iso file. For more information about performing this step, see the
     section, "Manage LTI Deployment Media", in the MDT document Using the
     Microsoft Deployment Toolkit.

   7. Burn a DVD of the LiteTouchMedia.iso file created in the previous step.

        ７ Note

        If delivering the ISO file to the OEM or to the organization's staging
        environment, this step is not necessary.

   8. Deliver the ISO file or the DVD to the OEM or to the organization's staging
     environment.

LTI OEM Preload Process—Phase 2: Apply the Image to the Target
Computer
The second phase of the OEM preload process is performed by the OEM or by the
deployment team in the staging environment of the deployment organization. During
this phase of the process, the .iso file or DVD created in Phase 1 is applied to the target
computers. The deliverable of this phase is the image deployed on the target computers
so that they are ready for deployment in the production environment.

To apply the image to the target computers

   1. Start a target computer with the media created in the Phase 1.

     Windows PE starts, and then the Windows Deployment Wizard starts.

   2. In the Windows Deployment Wizard, select the OEM Preinstallation Task
     Sequence for Staging Environment task sequence.

     The task sequence will start and the contents of the bootable media will be copied
     to the local hard disk of the target computer.

   3. When the Windows Deployment Wizard is complete for the OEM Preinstallation
     Task Sequence for Staging Environment task sequence, the hard disk will be ready
     to initiate the remainder of the deployment process by running the Windows

<!-- p.666 -->

     Deployment Wizard for the other task sequences that are used to deploy the
     operating system.

     The OEM Preinstallation Task Sequence for Staging Environment task sequence is
     responsible for deploying the image to the target computer and initiating the LTI
     process. The Windows Deployment Wizard will start a second time to run the task
     sequences used to deploy the operating system on the target computer.

   4. Clone the contents of the first hard disk to as many target computers in the
     staging environment as required.

   5. The target computers are delivered to the production environment for
     deployment.

LTI OEM Preload Process—Phase 3: Complete Target Computer
Deployment

The third and final phase of the OEM preload process is performed in the deployment
organization's production environment. During this phase of the process, the target
computer is started and the bootable media image, placed on the hard disk in the
staging environment during the previous phase, starts.

To complete deployment of the target computers in the production environment

   1. Start the target computer.

     Windows PE starts, and then the Windows Deployment Wizard starts.

   2. Complete the Windows Deployment Wizard using the specific configuration
     information for each target computer.

     For more information about completing this step, see the section, "Running the
     Deployment Wizard", in the MDT document Using the Microsoft Deployment
     Toolkit.

     When this phase is complete, the target computer will be ready to use in the
     production environment.

Using Windows PowerShell to Perform
Common Tasks
The MDT administration tasks in the Deployment Workbench are performed by
underlying Windows PowerShell cmdlets, which you can use to automate administrative

<!-- p.667 -->

tasks such as those in the following sections.

You can automate MDT administration by performing the following steps:

     Create a new deployment share as described in Creating a New Deployment Share.

     Create a folder in a deployment share as described in Creating a Folder.

     Delete a folder from a deployment share as described in Deleting a Folder.

     Import a device driver into a deployment share as described in Importing a Device
     Driver.

     Deleting a device driver from a deployment share as described in Deleting a Device
     Driver.

     Import an operating system package into a deployment share as described in
     Importing an Operating System Package.

     Deleting an operating system package from a deployment share as described in
     Deleting an Operating System Package.

     Import an operating system into a deployment share as described in Importing an
     Operating System.

     Deleting an operating system from a deployment share as described in Deleting an
     Operating System.

     Create an application in a deployment share as described in Creating an
     Application.

     Delete an application from a deployment share as described in Deleting an
     Application.

     Create a task sequence in a deployment share as described in Creating a Task
     Sequence.

     Delete a task sequence from a deployment share as described in Deleting a Task
     Sequence.

     Create an MDT DB as described in Creating an MDT DB.

     Create a selection profile as described in Creating a Selection Profile.

     Update a deployment share as described in Updating a Deployment Share.

<!-- p.668 -->

     Create a linked deployment share as described in Creating a Linked Deployment
     Share.

     Update a linked deployment share as described in Updating a Linked Deployment
     Share.

     Delete a linked deployment share as described in Deleting a Linked Deployment
     Share.

     Create deployment media as described in Creating Media.

     Generate deployment media as described in Generating Media.

     Delete deployment media as described in Deleting Media.

Creating a New Deployment Share
The following Windows PowerShell commands create a new deployment share at
D:\Production Deployment Share named Production$. The new deployment share will be
displayed in the Deployment Workbench as Production.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider "MDTProvider" -Root "D:\Production
  Deployment Share" -Description "Production" -NetworkPath
  "\\Deployment_Server\Production$" -Verbose | add-MDTPersistentDrive -Verbose

Creating a Folder
The following Windows PowerShell commands create an Adobe folder in the
Deployment Workbench console tree at Deployment Workbench/Deployment
Shares/Production/Applications.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  New-item -path "DS002:\Applications" -enable "True" -Name "Adobe" -Comments
  "This folder contains Adobe software" -ItemType "folder" -Verbose remove-
  psdrive DS001 -Verbose

  ７ Note

<!-- p.669 -->

  Adding "remove-psdrive" to the script ensures that the background process
  finishes before proceeding.

Deleting a Folder
The following Windows PowerShell commands delete the Deployment
Workbench/Deployment Shares/Production/Applications/Adobe folder.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Remove-item -path "DS002:\Applications\Adobe" -Verbose

  ７ Note

  The script will fail if the folder is not empty.

Importing a Device Driver
The following Windows PowerShell commands will import the Dell 2407 WFP monitor
device driver into the Production deployment share.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Import-mdtdriver -path "DS002:\Out-of-Box Drivers\Monitor" -SourcePath
  "D:\Drivers\Dell\2407 WFP" -Verbose

Deleting a Device Driver
The following Windows PowerShell command deletes the Dell 2407 WFP monitor driver
from the Production deployment share.

  PowerShell

  Remove-item -path "DS002:\Out-of-Box Drivers\Dell Inc. Monitor 2407WFP.INF
  1.0" -Verbose

<!-- p.670 -->

Importing an Operating System Package
The following Windows PowerShell commands import all operating system packages
located under D:\Updates\Microsoft\Vista. These operating system packages will be
stored in the Production deployment share, which is in D:\Production Deployment
Share.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Import-mdtpackage -path "DS002:\Packages" -SourcePath
  "D:\Updates\Microsoft\Vista" -Verbose

Deleting an Operating System Package
The following Windows PowerShell command deletes the specified operating system
package from the Production deployment share.

  PowerShell

  Remove-item -path "DS002:\Packages\Package_1_for_KB940105 neutral x86
  6.0.1.0 KB940105" -Verbose

Importing an Operating System
The following Windows PowerShell commands import the Windows Vista operating
system located in D:\Operating Systems\Windows Vista x86. The operating system will
be stored in the Production deployment share, which is in D:\Production Deployment
Share.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Import-mdtoperatingsystem -path "DS002:\Operating Systems" -SourcePath
  "D:\Operating Systems\Windows Vista x86" -DestinationFolder "Windows Vista
  x86" -Verbose

Deleting an Operating System

<!-- p.671 -->

The following Windows PowerShell command deletes the Windows Vista HOMEBASIC
operating system from the Production deployment share.

  PowerShell

  Remove-item -path "DS002:\Operating Systems\Windows Vista HOMEBASIC in
  Windows Vista x86 install.wim" -Verbose

Creating an Application
The following Windows PowerShell commands create the Adobe Reader 9 application
using source files from D:\Software\Adobe\Reader 9. The application will be stored in
the Production deployment share, which is in D:\Production Deployment Share.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Import-MDTApplication -path "DS002:\Applications" -enable "True" -Name
  "Adobe Reader 9" -ShortName "Reader" -Version "9" -Publisher "Adobe" -
  Language "" -CommandLine "setup.exe" -WorkingDirectory ".\Applications\Adobe
  Reader 9" -ApplicationSourcePath "D:\Software\Adobe\Reader 9" -
  DestinationFolder "Adobe Reader 9" -Source ".\Applications\Adobe Reader 9" -
  Verbose

Deleting an Application
The following Windows PowerShell command deletes the Adobe Reader 9 application
from the Production deployment share.

  PowerShell

  Remove-item -path "DS002:\Applications\Adobe Reader 9" -Verbose

Creating a Task Sequence
The following Windows PowerShell commands create the Windows Vista Production
Build task sequence in the Production deployment share, which is located in
D:\Production Deployment Share.

  PowerShell

<!-- p.672 -->

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Import-mdttasksequence -path "DS002:\Task Sequences" -Name "Windows Vista
  Business Production Build" -Template "Client.xml" -Comments "Approved for
  use in the production environment. This task sequence uses the Standard
  Client task sequence template" -ID "Vista_Ref" -Version "1.0" -
  OperatingSystemPath "DS002:\Operating Systems\Windows Vista BUSINESS in
  Windows Vista x86 install.wim" -FullName "Fabrikam User" -OrgName "Fabrikam"
  -HomePage "http://www.Fabrikam.com" -AdminPassword "secure_password" -
  Verbose

Deleting a Task Sequence
The following Windows PowerShell command deletes the Windows Vista Production
Build task sequence from the Production deployment share.

  PowerShell

  Remove-item -path "DS002:\Task Sequences\Windows Vista Business Production
  Build" -force -Verbose

Creating an MDT DB
The following Windows PowerShell commands create a new MDT DB on the
deployment_server server for the Production deployment share. The database
connection will be via TCP/IP.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  New-MDTDatabase -path "DS002:" -SQLServer "DeploymentServer" -Netlib
  "DBMSSOCN" -Database "MDT2010" -SQLShare "DB_Connect" -Force -Verbose

Creating a Selection Profile
The following Windows PowerShell commands create a new Applications selection
profile.

  PowerShell

<!-- p.673 -->

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  New-item -path "DS002:\Selection Profiles" -enable "True" -Name
  "Applications" -Comments "" -Definition "<SelectionProfile><Include
  path="Applications" /></SelectionProfile>" -ReadOnly "False" -Verbose

Updating a Deployment Share
The following Windows PowerShell commands update the Production deployment
share, which is in D:\Production Deployment Share.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Update\-MDTDeploymentShare \-path "DS002:" \-Verbose

Creating a Linked Deployment Share
The following Windows PowerShell commands create a deployment share that is linked
to the Production deployment share and resides under the
\\remote_server_name\Deployment$ share. The Everything selection profile is used to
determine which content is replicated to the linked deployment share. Content from the
Production deployment share will be merged with content that already exists in the
\\remote_server_name\Deployment$ share.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  New-item -path "DS002:\Linked Deployment Shares" -enable "True" -Name
  "LINKED001" -Comments "" -Root "\\RemoteServerName\Deployment$" -
  SelectionProfile "Everything" -Replace "False" -Verbose

Updating a Linked Deployment Share
The following Windows PowerShell commands update the LINKED001 deployment
share.

  PowerShell

<!-- p.674 -->

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Replicate-MDTContent -path "DS002:\Linked Deployment Shares\LINKED001" -
  Verbose

Deleting a Linked Deployment Share
The following Windows PowerShell commands delete the LINKED001 deployment share.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  Remove-item -path "DS002:\Linked Deployment Shares\LINKED001" -Verbose

Creating Media
The following Windows PowerShell commands create a source folder that contains
content used to create bootable media. The Production deployment share will be used
as the source. The Everything selection profile determines what content is placed in the
media content folder. The LiteTouchMedia.iso file will be created when the media is
generated. The media will support both x86 and x64 platforms.

  PowerShell

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  New-item -path "DS002:\Media" -enable "True" -Name "MEDIA001" -Comments
  "some comment here" -Root "D:\Media" -SelectionProfile "Everything" -
  SupportX86 "True" -SupportX64 "True" -GenerateISO "True" -ISOName
  "LiteTouchMedia.iso" -Verbose
  New-PSDrive -Name "MEDIA001" -PSProvider "MDTProvider" -Root
  "D:\Media\Content" -Description "Embedded media deployment share" -Force -
  Verbose

Generating Media
The following Windows PowerShell commands create the LiteTouchMedia.iso file in
D:\Media, which will use content from the MEDIA001 media source folder.

  PowerShell

<!-- p.675 -->

  Add-PSSnapIn Microsoft.BDD.PSSnapIn
  New-PSDrive -Name "DS002" -PSProvider MDTProvider -Root "D:\Production
  Deployment Share"
  Generate-MDTMedia -path "DS002:\Media\MEDIA001" -Verbose

Deleting Media
The following Windows PowerShell command deletes the MEDIA001 media from the
Production deployment share.

  PowerShell

  Remove-item -path "DS002:\Media\MEDIA001" -Verbose

Delaying Domain Join to Avoid Application of
Group Policy Objects
Group Policy is a rich and flexible technology providing the capability to efficiently
manage a large number of Active Directory Domain Services (AD DS) computer and user
objects through a centralized, one-to-many model. Group Policy settings are contained
in a Group Policy object (GPO) and linked to one or more AD DS service containers—
sites, domains, and organizational units (OUs).

Some organizations have Group Policy settings that are restrictive and could cause
problems during operating system deployments. For example, the following Group
Policy settings can interrupt an automated logon process:

     Autologon restrictions

     Administrator account renaming

     Legal banners and captions

     Restrictive security policies (for example, the Specialized Security - Limited
     Functionality [SSLF] policy)

     One option to overcome the issues that a GPO might cause during deployment is
     to join the computer to the domain as late as possible in the deployment process.
     This join can be done using a custom task sequence step that runs the
     ZTIDomainJoin.wsf script.

<!-- p.676 -->

     To join the target computer to the domain, the ZTIDomainJoin.wsf script uses the
     DomainAdmin, DomainAdminDomain, DomainAdminPassword, JoinDomain, and
     MachineObjectOU properties. You can declare these properties using the Windows
     Deployment Wizard, deployment share rules, the MDT DB, and Configuration
     Manager computer and collection rules. The account used must have the rights
     required to create and delete computer objects in the domain.

     Typically, the ZTIConfigure.wsf script updates the Unattend.xml or Unattend.txt file
     with the values that these properties specify. These settings are then parsed by the
     Windows Setup program, and the system attempts to join to the domain early in
     the deployment process. Doing so subjects the target computer to settings
     specified in domain GPOs and can possibly cause the deployment process to fail.

     To intentionally delay joining the target computer to the domain during the
     deployment process, you can remove certain elements from the Unattend.xml file.
     The ZTIConfigure.wsf script will skip over writing properties to the Unattend.xml
     file if the associated property element is missing from the file.

  ７ Note

  This sample work-around is only valid when deploying the Windows 7, Windows
  Server 2008, or Windows Server 2008 R2 operating systems.

Prepare the unattend.xml file so the target computer does not attempt to join the
domain during Windows Setup

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences/task_sequence
     (where deployment_share is the name of the deployment share and task_sequence
     is the name of the task sequence to be configured).

  3. In the Actions pane, select Properties.

  4. On the OS Info tab, select Edit Unattend.xml.

     The Windows System Image Manager (Windows SIM) starts.

  5. In the Answer File pane, go to 4 specialize/Identification/Credentials. Right-click
     Credentials, and then select Delete.

  6. Select Yes.

<!-- p.677 -->

   7. Save the answer file, and then exit Windows SIM.

   8. Select OK on the task sequence Properties dialog box.

     With the Credentials elements missing from the unattend.xml file, the
     ZTIConfigure.wsf script is not able to populate the domain join information in the
     Unattend.xml file, which will prevent Windows Setup from attempting to join the
     domain.

     To add a task sequence step that joins the target computer to the domain

   9. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

 10. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Task Sequences/task_sequence
     (where deployment_share is the name of the deployment share and task_sequence
     is the name of the task sequence to be configured).

 11. In the Actions pane, select Properties.

 12. On the Task Sequence tab, go to and expand the State Restore node.

 13. Verify that the Recover From Domain task sequence step is present. If yes, proceed
     to step 9.

 14. In the task sequence Properties dialog box, select Add, go to Settings, and select
     Recover From Domain.

 15. Add the Recover From Domain task sequence step to the task sequence editor.
     Verify that the step is in the desired location in the task sequence.

 16. Verify that the settings for the Recover From Domain task sequence step are
     configured to meet your needs.

 17. Select OK on the task sequence Properties dialog box to save the task sequence.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.678 -->

Quick Start Guide for Lite Touch
Installation
Article • 02/12/2024

Microsoft Deployment Toolkit (MDT) 2013 provides technology for deploying Windows
operating systems, and Microsoft Office. This guide helps you quickly evaluate MDT
2013 by providing condensed, step-by-step instructions for using it to install the
Windows 8.1 operating system through Lite Touch Installation (LTI) using bootable
media (DVD or USB flash drive). This guide demonstrates how to perform the New
Computer deployment scenario using an MDT 2013 deployment share. The New
Computer deployment scenario covers the deployment of Windows 8.1 to a new
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
To deploy operating systems and applications using MDT, the environment must meet
the following software and computer configuration prerequisites.

Required Software
To complete this guide, the following software is required:

      Windows 8.1

      If you decide to complete this guide on an operating system other than Windows
      8.1, MDT requires the following elements:

         Microsoft .NET Framework version 3.5 with Service Pack 1

<!-- p.679 -->

        Windows PowerShell™ version 2.0

        Windows 8.1 includes these features.

     Windows Assessment and Deployment Kit (Windows ADK) for Windows 8.1

     Networking services, including Domain Name System and Dynamic Host
     Configuration Protocol

  ７ Note

  The Task Sequencer used in MDT deployments requires that the Create Global
  Object right be assigned to credentials used to access and run the Deployment
  Workbench and the deployment process. This right is normally available to
  accounts with Administrator-level permissions (unless explicitly removed). Also, the
  Specialized Security - Limited Functionality (SSLF) security profile removes the
  Create Global Object right and should not be applied to computers being deployed
  using MDT until the MDT process is complete.

Computer Configuration
To complete this guide, set up the computers listed in the following table. These
computers can be either physical computers or virtual machines (VMs) with the system
resources designated.

                                                                                ﾉ   Expand table

 Computer     Description
 name

 WDG-MDT-     This computer runs MDT and Windows 8.1 and is installed in a domain named
 01           mdt2013.corp.woodgrovebank.com with a network basic input/output system
              (NetBIOS) name of MDT2013. The system resources of the computer are:

              - Processor running at 1.4 gigahertz (GHz) or faster.
              - 1 gigabyte (GB) or greater physical memory.
              - One disk partition that has 16 GB or more available disk space that will become
              the drive C partition.
              - One CD-ROM or DVD-ROM drive that will be assigned the drive letter D.

 WDG-REF-     This is the reference computer and runs no current operating system. The system
 01           resources of the computer are:

              - Processor running at 1.4 GHz or faster.

<!-- p.680 -->

 Computer    Description
 name

             - 1 GB or more of physical memory.
             - 16 GB or more of available disk space.

 WDG-CLI-    This is the target computer and runs no current operating system. The system
 01          resources of the computer are:

             - Processor running at 1.4 GHz or faster.
             - 1 GB or more of physical memory.
             - 16 GB or more of available disk space.

  ７ Note

  This guide assumes that you are evaluating MDT on 64-bit (x64) physical or virtual
  computers. If evaluating MDT on 32-bit (x86) platforms, download and install the
  x86 editions of MDT and the components that this guide describes.

Step 1: Obtain the Required Software
This guide assumes that the 64-bit version of Windows 8.1 is installed on a computer
named WDG-MDT-01. If the computer you are using has a different name, substitute the
name of that computer for WDG-MDT-01.

  ７ Note

  This section assumes that you are creating a new infrastructure for MDT.

The following software is required to perform LTI deployments:

     MDT 2013

     Windows ADK for Windows 8.1

     Windows 8.1 distribution files

     Device drivers required for the target computer, WDG-CLI-01

     Device drivers required for the reference computer, WDG-REF-01

Step 2: Prepare the MDT Environment
