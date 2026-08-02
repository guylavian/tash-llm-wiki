---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 721-760"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0721-0760
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0721-0760
family: sccm
documentKind: "doc"
abstract: "For this Do this Network Type network_address (where network_address is the network address of the subnet where the computers are installed). Subnet Type subnet_mask (where subnet_mask is the subnet mask of the subnet mask where the computers are installed). To add the Configura"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 721-760

<!-- p.721 -->

     For this      Do this

     Network       Type network_address (where network_address is the network address of the
                   subnet where the computers are installed).

     Subnet        Type subnet_mask (where subnet_mask is the subnet mask of the subnet
     mask          where the computers are installed).

To add the Configuration Manager site boundary to a site
boundary group

  1. In the Configuration Manager console, in the navigation pane, select
    Administration.

  2. In the Administration workspace, go to Overview/Hierarchy
    Configuration/Boundary Groups.

  3. On the Ribbon, select Create Boundary Group.

    The Create Boundary Group dialog box opens.

  4. Complete the General tab of the Create Boundary Group dialog box using the
    following information.

                                                                                ﾉ   Expand table

     For this      Do this

     Name          Type New York City Boundary Group.

     Description   Type This is the boundary group for the site boundaries at the New York
                   City site.

     Boundaries    1. Select Add.
                   The Add Boundaries dialog box appears.
                   2. In the Add Boundaries dialog box, select site_boundary (where
                   site_boundary is the site boundary you created earlier in the process), and
                   then select OK.
                   The site boundary appears in the list of boundaries.

  5. Complete the References tab of the Create Boundary Group dialog box using the
    following information, and then select OK.

                                                                                ﾉ   Expand table

<!-- p.722 -->

        For this         Do this

        Site             Select the Use this boundary group for site assignment check box.
        assignment

        Content          1. Select Add.
        location         The Add Site Systems dialog box appears.
                         2. In the Add Site Systems dialog box, select \\WDG-MDT-
                         01.mdt2013.corp.woodgrovebank.com, and then select OK.
                         The site system server appears in the list of site system servers.

   6. Close any open windows.

Step 1-14: Configure the Publishing of Site Information in
AD DS and DNS
The Configuration Manager client needs to locate the various Configuration Manager
server roles. Modify the site properties to publish the site information in AD DS and in
DNS.

To configure the publishing of site information in AD DS and in DNS

   1. Select Start, point to All Programs, and then point to Microsoft System Center
       2012. Point to Configuration Manager, and then select Configuration Manager
       Console.

   2. In the Configuration Manager console, in the navigation pane, select
       Administration.

   3. In the Administration workspace, go to Overview/Site Configuration/Sites.

   4. In the preview pane, select NYC - New York City Site.

   5. On the Ribbon, select Properties.

   6. In the New York City Site Properties dialog box, on the Publishing tab, verify that
       the mdt2013.corp.woodgrovebank.com Active Directory forest is listed, and then
       select Cancel.

   7. Close any open windows.

Step 2: Prepare the MDT Environment
The first step in the deployment process is to prepare the MDT environment. When this
step is complete, you can create the reference computer and deploy a captured image

<!-- p.723 -->

of it to the target computer (WDG-CLI-01) using Configuration Manager integration
with MDT.

Prepare the MDT environment by:

     Installing MDT as described in Step 2-1: Install MDT

     Enabling Configuration Manager console integration by running the Configure
     ConfigMgr Integration script as described in Step 2-2: Enable Configuration
     Manager Console Integration

Step 2-1: Install MDT
To install MDT, complete the following steps:

   1. In Windows Explorer, go to E:\Source$\MDT_2013.

   2. Double-click MicrosoftDeploymentToolkit2013_x64.msi (for 64-bit operating
     systems) or MicrosoftDeploymentToolkit2013_x86.msi (for 32-bit operating
     systems), and then select Install.

     The Microsoft Deployment Toolkit 2013 Setup Wizard starts.

   3. Complete the Microsoft Deployment Toolkit 2013 Setup Wizard using the
     information in the following table. Accept the default values unless otherwise
     specified.

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

<!-- p.724 -->

     The Microsoft Deployment Toolkit 2013 Setup Wizard finishes, and MDT is installed
     on WDG-MDT-01.

Step 2-2: Enable Configuration Manager Console
Integration
Before you can use the Configuration Manager integration features of MDT, run the
Configure ConfigMgr Integration script. This script copies the appropriate integration
files to the folder in which Configuration Manager is installed. The script also adds
Windows Management Instrumentation (WMI) classes for the new MDT custom actions.
The classes are added by compiling a new Managed Object Format (.mof) file that
contains the new class definitions.

To enable Configuration Manager console integration

  ７ Note

  Ensure that the Configuration Manager console is closed while performing these
  steps.

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Configure ConfigMgr Integration.

     The Configure ConfigMgr Integration Wizard starts.

   2. Complete the Configure ConfigMgr Integration Wizard using the information in
     the following table. Accept the default values unless otherwise specified.

                                                                              ﾉ   Expand table

      On this wizard   Do this
      page

      Options          1. Verify that the Install the MDT console extensions for System Center
                       2012 R2 Configuration Manager check box is selected.
                       2. Verify that the Add the MDT task sequence actions to a System
                       Center 2012 R2 Configuration Manager server check box is selected.
                       3. In Site server name, verify that the value is WDG-MDT-
                       01.mdt2013.corp.woodgrovebank.com.
                       4. In Site code, verify that the value is NYC.
                       5. Select Next.

      Confirmation     Select Finish.

<!-- p.725 -->

     The Configure ConfigMgr Integration Wizard finishes, and MDT is integrated with
     Configuration Manager.

Step 3: Create and Configure a Task Sequence
to Create a Reference Computer
When you have prepared the MDT environment, create the reference computer. The
reference computer is the template for deploying new images to the target computers.
Configure this computer (WDG-REF-01) exactly as you will configure the target
computers. You will then capture an image of the reference computer and deploy the
image to the target computers.

Create the reference computer, WDG-REF-01, by:

     Creating an MDT task sequence to deploy Windows 8.1 to the reference computer
     as described in Step 3-1: Create an MDT Task Sequence for Deploying the
     Reference Computer

     Selecting the distribution points for the new packages and images that the Create
     MDT Task Sequence Wizard creates as described in Step 3-2: Select the Distribution
     Points for the New Packages and Images

     Adding the necessary device drivers to a new drive package and to the appropriate
     boot images as described in Step 3-3: Add the Necessary Device Drivers

     Enable monitoring of the MDT deployment process as described in Step 3-4:
     Enable MDT Deployment Process Monitoring

     Configuring the MDT configuration files for the reference computer—specifically,
     the CustomSettings.ini file—as described in Step 3-5: Customize the MDT
     Configuration Files for the Reference Computer

     Updating the Configuration Manager distribution points for the Custom Settings
     Files package as described in Step 3-6: Update the Distribution Points for the
     Custom Settings Files Package

     Customizing the task sequence for the reference computer as described in Step 3-
     7: Customize the Task Sequence for the Reference Computer

Step 3-1: Create an MDT Task Sequence for Deploying the
Reference Computer

<!-- p.726 -->

Use the Create MDT Task Sequence Wizard in the Configuration Manager console to
create task sequences in Configuration Manager that are integrated with MDT. MDT
includes the Standard Client Task Sequence template, which you can use to deploy the
reference computer.

The Create MDT Task Sequence Wizard substitutes the packages and images selected
for the placeholders in the task sequence templates. After completing the wizard, the
new task sequence references the appropriate packages and images.

  ７ Note

  Always use the Create MDT Task Sequence Wizard to create task sequences based
  on the MDT task sequence templates. Although you can manually import the task
  sequence templates, Microsoft does not recommend this process.

To create a task sequence for deploying the reference computer
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

   5. Complete the Create MDT Task Sequence Wizard using the information in the
     following table. Accept the default values unless otherwise specified.

                                                                               ﾉ   Expand table

      On this wizard      Do this
      page

      Choose Template     Select Client Task Sequence, and then select Next.

      Choose Template:    1. In Task sequence name, type Windows 8.1 Reference Deployment.
      General             2. In Task sequence comments, type Task sequence for deploying

<!-- p.727 -->

On this wizard     Do this
page

                   Windows 8.1 to the reference computer (WDG-REF-01), and then
                   select Next.

Choose Template:   1. Select Join a workgroup.
Details            2. In Workgroup, type WORKGROUP.
                   3. In User name, type Woodgrove Bank Employee.
                   4. In Organization name, type Woodgrove Bank.
                   5. In Product key, type product_key (where product_key is the product
                   key for Windows 8.1).
                   6. Select Next.

Choose Template:   a. Select This task sequence may be used to capture and image.
Capture Settings   b. In Capture destination, type \\WDG-MDT-01\Capture$\WDG-
                      REF-01.wim.
                   c. In Capture account, select Set.
                   d. Complete the Windows User Account dialog box by performing
                      the following steps:

                       i. In User name, type MDT2013\Administrator.
                       ii. In Password and Confirm password, type P@ssw0rd.
                   e. Select OK.
                   f. Select Next.

Boot Image         1. Select Create a new boot image package.
                   2. In Package source folder to be created, type \\WDG-MDT-
                   01\Packages$\WINPE_Custom, and then select Next.

Boot Image:        1. In Name, type Windows PE Custom.
General Settings   2. In Version, type 1.00.
                   3. In Comments, type Customized version of Windows PE to be
                   used in deployment of reference and target computers, and then
                   select Next.

Boot Image:        Under Platform, select x64, and then select Next.
Options

Boot Image:        Select Next.
Components

Boot Image:        Select Next.
Customization

MDT Package        1. Select Create a new Microsoft Deployment Toolkit Files package.
                   2. In Package source folder to be created, type \\WDG-MDT-
                   01\Packages$\MDT_Files, and then select Next.

MDT Package:       1. In Name, type MDT Files.
MDT Details        2. In Version, type 1.00.

<!-- p.728 -->

 On this wizard      Do this
 page

                     3. In Comments, type Provides access to MDT files during
                     Configuration Manager deployment process, and then select Next.

 OS Image            1. Select Create a new OS install package.
                     2. In OS installation folder location, type \\WDG-MDT-
                     01\Source$\Windows_7.
                     3. In Package source folder to be created, type \\WDG-MDT-
                     01\Packages$\Windows_7, and then select Next.

 OS Image: Image     1. In Name, type Windows 8.1.
 Details             2. In Version, type 1.00.
                     3. In Comments, type Windows 8.1 package used to deploy to
                     reference computers, and then select Next.

 Deployment          Select Next.
 Method

 Client Package      Select Create a new ConfigMgr client package, and then select Next.

 USMT Package        1. Select Create a new USMT package.
                     2. In Package source folder to be created, type \\WDG-MDT-
                     01\Packages$\USMT, and then select Next.

 USMT Package:       1. In Name, type USMT.
 USMT Details        2. In Version, type 1.00.
                     3. In Comments, type USMT files used to capture and restore user
                     state migration information, and then select Next.

 Settings Package    1. Select Create a new settings package.
                     2. In Package source folder to be created, type \\WDG-MDT-
                     01\Packages$\CustomSettings_Reference, and then select Next.

 Settings Package:   1. In Name, type MDT Reference Computer Custom Settings.
 Settings Details    2. In Version, type 1.00.
                     3. In Comments, type Configuration settings for MDT deployment
                     process (such as CustomSettings.ini) for the reference computer,
                     and then select Next.

 Sysprep Package     Select Next.

 Summary             1. Review the information in the Details box that you provided while
                     completing the previous wizard pages.
                     2. Select Next.

 Progress            The progress for creating the task sequence is displayed.

 Confirmation        Select Finish.

The new task sequence appears in the preview pane.

<!-- p.729 -->

Step 3-2: Select the Distribution Points for the New
Packages and Images
The Create MDT Task Sequence Wizard creates a number of packages and images. After
these packages and images are created, select the distribution points from which the
packages and images will be copied and available to target computers.

  ７ Note

  In this sample, there is only one distribution point (WDG-MDT-01). However, most
  production networks have multiple distribution points. When performing this step
  in a production environment, select the appropriate distribution points for the
  network.

To select the distribution points for software distribution packages
   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Task
     Sequences.

   4. In the preview pane, select Windows 8.1 Reference Deployment.

   5. On the Ribbon, on the Home tab, in the Deployment group, select Distribute
     Content.

     The Distribute Content Wizard starts.

   6. Complete the Distribute Content Wizard using the information in the following
     table. Accept default values unless otherwise specified.

                                                                        ﾉ   Expand table

      On this wizard     Do this
      page

      General            Select Next.

<!-- p.730 -->

      On this wizard      Do this
      page

      General: Content    Select Next.

      General: Content    1. Select Add, and then select Distribution Point.
      Destination         The Add Distribution Points dialog box appears.
                          2. In the Add Distribution Points dialog box, select WDG-MDT-
                          01.mdt2013.corp.woodgrovebank.com, and then select OK.
                          WDG-MDT-01.corp.woodgrovebank.com appears in the Content
                          destination list.
                          3. Select Next.

      Summary             1. Review the information in the Details box that you provided while
                          completing the previous wizard pages.
                          2. Select Next.

      Progress            The progress for distributing the software is displayed.

      Completion          Select Close.

   7. Close all open windows and dialog boxes.

Step 3-3: Add the Necessary Device Drivers
When the MDT task sequence has been created, add any device drivers required for the
reference computer (WDG-REF-01) to the Windows PE boot image and to the Windows
8.1 image. Add the device drivers in the Drivers node in the Configuration Manager
console. Create a package that contains the device drivers, and inject the drivers into the
custom Windows PE image created earlier in the process.

After creating the package that contains the device drivers, select the distribution point
to which the package will be deployed.

To add the necessary device drivers
   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Operating Systems/Drivers.

   4. On the Ribbon, on the Home tab, in the Create group, select Import Driver.

<!-- p.731 -->

    The Import New Driver Wizard starts.

  5. Complete the Import New Driver Wizard using the information in the following
    table. Accept the default values unless otherwise specified.

                                                                             ﾉ   Expand table

     On this wizard page      Do this

     Locate Driver            In Source folder, type \\WDG-MDT-01\Source$\Drivers, and
                              then select Next.

     Locate Driver: Driver    Select Next.
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

     Locate Driver: Add       1. In the list of images, select the Windows PE Custom check
     Driver to Boot Images    box.
                              2. Select the Update distribution points when finished check
                              box, and then select Next.

     Summary                  1. Review the information in the Details box that you provided
                              while completing the previous wizard pages.
                              2. Select Next.

     Progress                 The progress for importing the device drivers is displayed.

     Confirmation             Select Close.

To select the distribution points for the driver package

  1. Select Start, point to All Programs, and then point to Microsoft System Center
    2012. Point to Configuration Manager, and then select Configuration Manager
    Console.

<!-- p.732 -->

 2. In the Configuration Manager console, in the navigation pane, select Software
   Library.

 3. In the Software Library workspace, go to Overview/Operating Systems/Driver
   Packages.

 4. In the preview pane, select device_driver_name Package (where
   device_driver_name is a descriptive name for the device drivers).

 5. On the Ribbon, on the Home tab, in the Deployment group, select Distribute
   Content.

   The Distribute Content Wizard starts.

 6. Complete the Distribute Content Wizard using the following information. Accept
   the default values unless otherwise specified.

                                                                                 ﾉ   Expand table

    On this wizard    Do this
    page

    General           Select Next.

    General:          Select Next.
    Content

    General:          1. Select Add, and then select Distribution Point.
    Content           The Add Distribution Points dialog box appears.
    Destination       2. In the Add Distribution Points dialog box, select \\WDG-MDT-
                      01.mdt2013.corp.woodgrovebank.com, and then select OK.
                      \\WDGMDT01.mdt2013.corp.woodgrovebank.com appears in the
                      Content destination list.
                      3. Select Next.

    Summary           1. Review the information in the Details box that you provided while
                      completing the previous wizard pages.
                      2. Select Next.

    Progress          The progress for distributing the software is displayed.

    Completion        Select Close.

 7. Close all open windows and dialog boxes.

Step 3-4: Enable MDT Deployment Process Monitoring

<!-- p.733 -->

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

  4. Complete the New Deployment Share Wizard using the following information

                                                                            ﾉ   Expand table

      On this wizard     Do this
      page

      On this wizard     Do this
      page

      Path               In Deployment share path, type C:\DeploymentShare$, and then
                         select Next.

      Share              Select Next.

      Descriptive Name   Select Next.

      Options            Select Next.

      Summary            Select Next.

      Progress           The progress for creating the deployment share is displayed.

      Confirmation       Select Finish.

     The New Deployment Share Wizard finishes, and the new deployment share—MDT
     Deployment Share (C:\DeploymentShare$)—appears in the details pane.

  5. In the details pane, select MDT Deployment Share (C:\DeploymentShare$).

  6. In the Actions pane, select Properties.

<!-- p.734 -->

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
EventService properties and corresponding values to the CustomSettings.ini file so that
the MDT deployment process captures an image of the reference computer (WDG-REF-
01) after deploying Windows 8.1.

To customize the MDT configuration files for the reference
computer
   1. In Windows Explorer, go to E:\Packages$\CustomSettings_Reference, and then
     double-click CustomSettings.ini.

   2. Open Microsoft Notepad, and then add the following lines to the end of the
     CustomSettings.ini file:

        ini

<!-- p.735 -->

        DoCapture=YES
        EventService=http://WDG-MDT-01:9800

     Example of CustomSettings.ini file after adding the DoCapture property:

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

   3. In Notepad, save the file, and then exit Notepad.

Step 3-6: Update the Distribution Points for the Custom
Settings Files Package
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

<!-- p.736 -->

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

<!-- p.737 -->

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

<!-- p.738 -->

Configuration Manager site database prior to initiating the operating system
deployment process. Configuration Manager can automatically discover computers on
the network that have a Windows operating system installed; however, if the computer
has no operating system installed, use the Import Computer Information Wizard to
import the new computer information.

To add the reference computer to the Configuration Manager site
database

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Assets and
     Compliance.

   3. In the Assets and Compliance workspace, go to Overview/Devices.

   4. On the Ribbon, on the Home tab, in the Create group, select Import Computer
     Information.

     The Import Computer Information Wizard starts.

   5. Complete the Import Computer Information Wizard using the following
     information. Accept the default values unless otherwise specified.

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

      Summary                 1. Review the information in the Details box that you provided
                              while completing the previous wizard pages.

<!-- p.739 -->

      On this wizard page    Do this

                             2. Select Next.

      Progress               The progress for importing the computer is displayed.

      Confirmation           Select Close.

     For more information on adding a new computer to the Configuration Manager
     site database, see the section, "To import computer information for a single
     computer," in the section "How to Deploy Operating Systems in Configuration
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
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Assets and
     Compliance.

   3. In the Assets and Compliance workspace, go to Overview/Device Collections.

   4. On the Ribbon, on the Home tab, in the Create group, select Create, and then
     select Create Device Collection.

     The Create Device Collection Wizard starts.

   5. Complete the Create Device Collection Wizard using the following information.
     Accept the default values unless otherwise specified.

                                                                             ﾉ   Expand table

<!-- p.740 -->

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

    Membership        a. Select Add Rule, and then select Direct Rule.
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
                        iv. On the Summary page, select Next.
                         v. On the Progress page, view the progress for creating the new
                             membership rule.
                         vi. On the Completion page, select Close.
                      c. Select Next.

    Summary          1. Review the information in the Details box that you provided while
                     completing the previous wizard pages.
                     2. Select Next.

    Progress         The progress for creating the device collection is displayed.

    Completion       Select Close.

   For more information, see the section, "How to Create Collections in Configuration
   Manager," in the Configuration manager Documentation Library, which is installed
   with Configuration Manager.

Step 4-3: Deploy the Reference Computer Task Sequence

<!-- p.741 -->

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

   6. Complete the Deploy Software Wizard using the following information. Accept the
     default values unless otherwise specified.

                                                                            ﾉ   Expand table

      On this wizard page       Do this

      General                   1. In Collection, select Browse.
                                2. In the Browse Collection dialog box, select Microsoft
                                Deployment - Reference Computer, and then select OK.
                                3. In Comment, type Deploy Windows 8.1 to the reference
                                computer and then capture an image of the reference
                                computer.
                                4. Select Next.

      Deployment Settings       1. In Purpose, select Available.
                                2. Select the Make available to boot media and PXE check box.
                                3. Select Next.

      Deployment Settings:      Select Next.
      Schedule

      Deployment Settings:      Select Next.
      User Experience

<!-- p.742 -->

      On this wizard page      Do this

      Deployment Settings:     Select Next.
      Alerts

      Deployment Settings:     Select Next.
      Distribution Points

      Summary                  1. Review the information in the Details box that you provided
                               while completing the previous wizard pages.
                               2. Select Next.

      Progress                 The progress for deploying the task sequence is displayed.

      Completion               Select Close.

     For more information, see the section, "How to Deploy a Task Sequence," in the
     Configuration manager Documentation Library, which is installed with
     Configuration Manager.

Step 4-4: Create the Task Sequence Bootable Media
To initiate the MDT process, provide a method for starting the computer with Windows
PE and the necessary software by creating the task sequence bootable media disk. Use
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

<!-- p.743 -->

5. Complete the Create Task Sequence Media Wizard using the following information.
  Accept the default values unless otherwise specified.

                                                                             ﾉ   Expand table

   On this wizard page      Do this

   Select Media Type        1. Select Bootable media.
                            2. Clear the Allow unattended operating system deployment
                            check box.
                            3. Select Next.

   Select Media Type:       Select Site-based media, and then select Next.
   Media Management

   Select Media Type:       In Media file, type \\WDG-MDT-
   Media Type               01\Capture$\CM2012_TS_Boot_Media.iso, and then select Next.

   Select Media Type:       In Password and Confirm password, type P@ssw0rd, and then
   Security                 select Next.

   Select Media Type:       1. In Boot image, select Browse.
   Boot Image               2. In the Select a Boot Image dialog box, select Windows PE
                            Custom, and then select OK.
                            3. In Distribution point, select \\WDG-MDT-
                            01.mdt2013.corp.woodgrovebank.com, and then select OK.
                            4. In Management point, select \\WDG-MDT-
                            01.mdt2013.corp.woodgrovebank.com, and then select OK.
                            5. Select Next.

   Select Media Type:       Select Next.
   Customization

   Summary                  1. Review the information in the Details box that you provided
                            while completing the previous wizard pages.
                            2. Select Next.

   Progress                 The progress for creating the task sequence media is displayed.

   Completion               Select Close.

  The wizard creates the CM2012_TS_Boot_Media.iso file in the WDG-MDT-
  01Capture$ shared folder.

6. If WDG-REF-01 is a physical computer, create a CD or DVD of the International
  Organization for Standardization (ISO) file. If WDG-REF-01 is a VM, start the VM
  directly from the ISO file.

<!-- p.744 -->

     For more information on creating the task sequence bootable media disk, see the
     section, "How to Create Bootable Media," in the Configuration manager
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

To start the reference computer with the task sequence bootable
media
   1. Start WDG-REF-01 with the task sequence bootable media created earlier in the
     process.

     Windows PE starts, and then the Task Sequence Wizard starts.

   2. Complete the Task Sequence Wizard using the following information. Accept the
     default values unless otherwise specified.

                                                                           ﾉ   Expand table

      On this wizard page          Do this

      Welcome to the Task          In Password, type P@ssw0rd, and then select Next.
      Sequence Wizard

      Select a Task Sequence       In the list box, select Windows 8.1 Reference Deployment,
                                   and then select Next.

To monitor the reference computer deployment process using the
Deployment Workbench, complete the following steps on WDG-

<!-- p.745 -->

MDT-01
 1. On WDG-MDT-01, select Start, and then point to All Programs. Point to Microsoft
   Deployment Toolkit, and then select Deployment Workbench.

 2. In the Deployment Workbench console tree, go to Deployment
   Workbench/Deployment Shares/MDT Deployment Share
   (C:\DeploymentShare$)/Monitoring.

 3. In the details pane, view the deployment process for WDG-REF-01.

 4. In the Actions pane, periodically select Refresh.

   The status of the deployment process is updated in the details pane. Continue to
   monitor the deployment process until the process is complete.

 5. In the details pane, select WDG-REF-01.

 6. In the Actions pane, select Properties.

   The WDG-REF-01 Properties dialog box is displayed.

 7. In the WDG-REF-01 Properties dialog box, on the Identity tab, view the
   monitoring information provided about the deployment process as follows:

                                                                            ﾉ   Expand table

    Information           Description

    ID                    Unique identifier for the computer being deployed.

    Computer Name         The name of the computer being deployed.

    Deployment status     The current status of the computer being deployed; the status can
                          be one of the following:

                          - Running. The task sequence is healthy and running.
                          - Failed. The task sequence failed, and the deployment process was
                          unsuccessful.
                          - Completed. The task sequence has finished.
                          - Unresponsive. The task sequence has not updated its status in the
                          past four hours and is assumed to be nonresponsive.

    Step                  The current task sequence step being run.

    Progress              The overall progress of the task sequence. The progress bar
                          indicates how many task sequence steps have been run out of the
                          total number of task sequence steps.

<!-- p.746 -->

Information      Description

Start            The time the deployment process started.

End              The time the deployment process ended.

Elapsed          The length of time the deployment process has been running or
                 took to run if the deployment process has finished.

Errors           The number of errors encountered during the deployment process.

Warnings         The number of warnings encountered during the deployment
                 process.

Remote Desktop   This button allows you to establish a remote desktop connection
                 with the computer being deployed using the Windows Remote
                 Desktop feature. This method assumes that:

                 - The target operating system is running and has remote desktop
                 support enabled
                 - mstsc.exe is in the path Note: This button is always visible but may
                 not be able to establish a remote desktop session if the monitored
                 computer is running Windows PE, has not completed installation of
                 the target operating system, or does not have the Remote Desktop
                 feature enabled.

VM Connection    This button allows you to establish a remote desktop connection to
                 a VM running in HyperV®. This method assumes that:

                 - The deployment is being performed to a VM running on Hyper-V
                 - vmconnect.exe is located in the %ProgramFiles%\Hyper-V folder
                 Note: This button appears when ZTIGather.wsf detects that Hyper-V
                 integration components are running on the monitored computer.
                 Otherwise, this button will not be visible.

DaRT Remote      This button allows you to establish a remote control session using
Control          the remote viewer feature in the Diagnostics and Recovery Toolkit
                 (DaRT).

                 This method assumes that:

                 - DaRT has been deployed to the target computer and is currently
                 running
                 - DartRemoteViewer.exe is located in the
                 %ProgramFiles%\Microsoft DaRT 7\v7 folder Note: This button
                 appears when ZTIGather.wsf detects that DaRT is running on the
                 monitored computer. Otherwise, this button will not be visible.

Automatically    Check box that controls whether the information in the dialog box is
refresh this     automatically refreshed. If the check box is:

<!-- p.747 -->

     Information         Description

     information every   - Selected, the information is refreshed every 10 seconds
     10 seconds          - Cleared, the information is not automatically refreshed and must
                         be manually refreshed using the Refresh Now button

     Refresh Now         This button immediately refreshes the information displayed in the
                         dialog box.

  8. In the WDG-REF-01 Properties dialog box, select OK.

  9. Close the Deployment Workbench.

To monitor the reference computer deployment process using the
Get-MDTMonitorData cmdlet, complete the following steps on
WDG-MDT-01
  1. On WDG-MDT-01, select Start, the select Administrative Tools, and then select
    Windows PowerShell Modules.

    The Windows PowerShell Modules command prompt opens.

  2. Create a PowerShell drive that uses the MDT PowerShell provider by running the
    New-PSDrive cmdlet as shown in the following example:

      PowerShell

      New-PSDrive -Name DS001 -PSProvider mdtprovider -Root
      d:\DeploymentShare$

  3. View the MDT monitoring process by running the Get-MDTMonitorData cmdlet as
    shown in the following example:

      PowerShell

      Get-MDTMonitorData -Path DS001:

    This command returns the monitoring data collected by the MDT monitoring
    service running on the same computer that hosts the deployment share, as shown
    in the following example output:

      PowerShell

      Name                 : WDG-REF-01
      PercentComplete      : 96
      Settings             :

<!-- p.748 -->

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

  4. Close the Windows PowerShell console.

     If any problems occur during the deployment, consult the MDT document
     Troubleshooting Reference. When completed, a captured image of the reference
     computer should exist in \\WDG-MDT-01\Capture$\WDG-REF-01.wim.

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

<!-- p.749 -->

     Points for the New Packages and Images

     Customizing the MDT configuration files for the target computer—specifically, the
     CustomSettings.ini file—as described in Step 5-4: Customize the MDT
     Configuration Files

     Updating the Configuration Manager distribution points for the Custom Settings
     package as described in Step 5-5: Update the Distribution Points for the Custom
     Settings Package

     Customizing the task sequence for the target computer as described in Step 5-6:
     Customize the Task Sequence for the Target Computer

Step 5-1: Import the Captured .wim File into
Configuration Manager
After the image of the reference computer (WDG-REF-01) is captured in to the .wim file,
import the captured .wim file into Configuration Manager. Import the captured .wim file
into the Operating System Images node using the Add Operating System Image Wizard.

The captured .wim contains two images, one for each partition on the reference
computer. Identify which of the images has the captured Windows 8.1 operating system
by checking the image description containing Windows 8.1. You will use the image index
when you create the task sequence for deploying the captured image to the target
computer.

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

   5. Complete the Add Operating System Image Wizard using the following
     information. Accept the default values unless otherwise specified.

<!-- p.750 -->

                                                                             ﾉ   Expand table

    On this wizard   Do this
    page

    On this wizard   Do this
    page

    Data Source      In Path, type \\WDG-MDT-01\Capture$\WDG-REF-01.wim, and then
                     select Next.

    General          1. In Name, type Windows 8.1 Reference Image.

                     1. In Version, type 1.00.

                     1. In Comments, type Windows 8.1 captured image of reference
                     computer (WDG-REF-01) used to deploy to target computers, and then
                     select Next.

    Summary          1. Review the information in the Details box that you provided while
                     completing the previous wizard pages.
                     2. Select Next.

    Progress         The progress for importing the operating system image is displayed.

    Completion       Select Close.

 6. In the preview pane, select Windows 8.1 Reference Image.

 7. In the preview pane, select the Details tab.

   The list of operating system partitions captured in the .wim is displayed. The image
   index that contains Windows 8.1 is the image index you will specify later during the
   Create MDT Task Sequence Wizard.

 8. Record the image index that contains Windows 8.1.

      Tip

     For the purposes of this example, image index 2 should have the Windows 8.1
     operating system.

Step 5-2: Create an MDT Task Sequence to Deploy the
Captured Image

<!-- p.751 -->

After the image is captured, create a task sequence to deploy the captured image of the
reference computer (WDG-REF-01) to the target computer (WDG-CLI-01). Most of the
packages needed for this task sequence were created earlier in the process. However,
you must create a new MDT Custom Settings package that has the proper configuration
settings for the target computer and creates an operating system image of the captured
image of the reference computer.

To create a task sequence template to deploy the captured image
to the target computer

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

   5. Complete the Create MDT Task Sequence Wizard using the following information.
     Accept the default values unless otherwise specified.

                                                                            ﾉ   Expand table

      On this wizard   Do this
      page

      Choose           Select Client Task Sequence, and then select Next.
      Template

      Choose           1. In Task sequence name, type Windows 8.1 Target Deployment.
      Template:        2. In Task sequence comments, type Task sequence for deploying
      General          captured reference computer image to the target computer (WDG-CLI-
                       01), and then select Next.

      Choose           a. Select Join a domain.
      Template:        b. In Domain, type mdt2013.corp.woodgrovebank.com.
      Details          c. In Account, select Set, and then complete the Windows User Account
                          dialog box by performing the following steps:

<!-- p.752 -->

On this wizard   Do this
page

                       i. In User name, type MDT2013\Administrator.
                      ii. In Password and Confirm password, type P@ssw0rd.
                     iii. Select OK.
                 d. In User name, type Woodgrove Bank Employee.
                 e. In Organization name, type Woodgrove Bank.
                 f. In Product key, type product_key (where product_key is the product
                    key for Windows 8.1).
                 g. Select Next.

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
                 contains Windows 8.1, which was identified in the section Step 5-1:
                 Import the Captured .wim File into Configuration Manager; for the
                 purposes of this guide, select 2).
                 2. Select Next.

Deployment       Select Next.
Method

Client Package   1. In Specify an existing ConfigMgr client package, select Browse.
                 2. In the Select a Package dialog box, select Microsoft Configuration
                 Manager Client Upgrade, and then select OK.
                 3. Select Next.

<!-- p.753 -->

      On this wizard   Do this
      page

      USMT Package     1. In Specify an existing USMT package, select Browse.
                       2. In the Select a Package dialog box, select USMT, and then select OK.
                       3. Select Next.

      Settings         1. Select Create a new settings package.
      Package          2. In Package source folder to be created, type \\WDG-MDT-
                       01\Packages$\CustomSettings_Target, and then select Next.

      Settings         1. In Name, type MDT Target Computer Custom Settings.
      Package:         2. In Version, type 1.00.
      Settings         3. In Comments, type Configuration settings for MDT deployment
      Details          process (such as CustomSettings.ini) for the target computer, and then
                       select Next.

      Sysprep          Select Next.
      Package

      Summary          1. Review the information in the Details box that you provided while
                       completing the previous wizard pages.
                       2. Select Next.

      Progress         The progress for creating the task sequence is displayed.

      Confirmation     Select Finish.

     The list of task sequences is displayed. The task sequence that you just created
     (Windows 8.1 Target Deployment) is listed in the list of task sequences.

Step 5-3: Select the Distribution Points for the New
Packages and Images
The Create MDT Task Sequence Wizard creates a number of packages and images. After
these packages and images are created, select the distribution points from which the
packages and images will be copied and available to target computers.

  ７ Note

  In this sample, there is only one distribution point (WDG-MDT-01). However, most
  production networks have multiple distribution points. When performing this step
  in a production environment, select the appropriate distribution points for the
  network.

<!-- p.754 -->

To select the distribution points for software distribution packages
  1. Select Start, point to All Programs, and then point to Microsoft System Center
    2012. Point to Configuration Manager, and then select Configuration Manager
    Console.

  2. In the Configuration Manager console, in the navigation pane, select Software
    Library.

  3. In the Software Library workspace, go to Overview/Operating Systems/Task
    Sequences.

  4. In the preview pane, select Windows 8.1 Target Deployment.

  5. On the Ribbon, on the Home tab, in the Deployment group, select Distribute
    Content.

    The Distribute Content Wizard starts.

  6. Complete the Distribute Content Wizard using the following information. Accept
    default values unless otherwise specified.

                                                                                  ﾉ   Expand table

     On this wizard    Do this
     page

     General           Select Next.

     Content           Select Next.

     General:          Select Next.
     Content

     General:          1. Select Add, and then select Distribution Point.
     Content           The Add Distribution Points dialog box appears.
     Destination       2. In the Add Distribution Points dialog box, select
                       \\WDGMDT01.mdt2013.corp.woodgrovebank.com, and then select OK.
                       \\WDGMDT01.mdt2013.corp.woodgrovebank.com appears in the
                       Content destination list.
                       3. Select Next.

     Summary           1. Review the information in the Details box that you provided while
                       completing the previous wizard pages.
                       2. Select Next.

     Progress          The progress for distributing the software is displayed.

     Completion        Select Close.

<!-- p.755 -->

   7. Close all open windows and dialog boxes.

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

   2. Open Notepad, and then add the following lines to the CustomSettings.ini file:

       ini

       EventService=http://WDG-MDT-01:9800

     This setting will configure monitoring of the target computer deployment.

       ７ Note

       Make any other changes that are required by your environment.

     Example of the edited CustomSettings.ini File:

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

<!-- p.756 -->

   3. Save the file, and then close Notepad.

Step 5-5: Update the Distribution Points for the Custom
Settings Package
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

<!-- p.757 -->

password for the local Administrator account to a random value.) The task sequence
may require further customization depending on the environment.

To customize the Windows 8.1 Target Deployment task sequence

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

Step 6: Deploy the Captured Image of the
Reference Computer to the Target Computer
When you have captured the image of the reference computer and created and
configured the task sequence, deploy the captured image. Configure MDT to provide all
the necessary configuration settings to deploy to the target computer. After initiating
the deployment process, the image of the reference computer running Windows 8.1 is

<!-- p.758 -->

automatically deployed to the target computer and configured with the settings
defined.

Deploy the captured image by:

     Adding the target computer to the Configuration Manager site database as
     described in Step 6-1: Add the Target Computer to the Configuration Manager Site
     Database

     Creating a computer collection that includes the target computer as described in
     Step 6-2: Create a Computer Collection That Includes the Target Computer

     Deploying the task sequence created earlier in the process as described in Step 6-
     3: Deploy the Target Computer Task Sequence

     Starting the target computer with the task sequence bootable media as described
     in Step 6-4: Start the Target Computer with the Task Sequence Bootable Media

Step 6-1: Add the Target Computer to the Configuration
Manager Site Database
To deploy an operating system without stand-alone media to a new computer that
Configuration Manager does not currently manage, add the new computer to the
Configuration Manager site database prior to initiating the operating system
deployment process. Configuration Manager can automatically discover computers on
the network that have a Windows operating system installed; however, if the computer
has no operating system installed, use the Import Computer Information Wizard to
import the new computer information.

To add the target computer to the Configuration Manager site
database
   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Assets and
     Compliance.

   3. In the Assets and Compliance workspace, go to Overview/Devices.

   4. On the Ribbon, on the Home tab, in the Create group, select Import Computer
     Information.

<!-- p.759 -->

     The Import Computer Information Wizard starts.

   5. Complete the Import Computer Information Wizard using the following
     information. Accept the default values unless otherwise specified.

                                                                             ﾉ   Expand table

      On this wizard page     Do this

      Select Source           Select Import single computer, and then select Next.

      Select Source: Single   1. In Computer Name, type WDG-CLI-01.
      Computer                2. In MAC address, type mac_address (where mac_address is the
                              MAC address of the primary network adapter for the target
                              computer, WDG-CLI-01).
                              3. Select Next.

      Select Source: Data     Select Next.
      Preview

      Select Source: Choose   Select Next.
      Target Collection

      Summary                 1. Review the information in the Details box that you provided
                              while completing the previous wizard pages.
                              2. Select Next.

      Progress                The progress for importing the computer is displayed.

      Confirmation            Select Close.

     For more information on adding a new computer to the Configuration Manager
     site database, see the section, "To import computer information for a single
     computer," in the section, "How to Deploy Operating Systems in Configuration
     Manager," in the Configuration manager Documentation Library, which is installed
     with Configuration Manager.

Step 6-2: Create a Computer Collection That Includes the
Target Computer
In the Configuration Manager console, create a collection that includes the target
computer (WDG-CLI-01). You use this computer collection later when advertising the
task sequence created earlier in the process.

To create a computer collection that includes the target computer

<!-- p.760 -->

1. Select Start, point to All Programs, and then point to Microsoft System Center
  2012. Point to Configuration Manager, and then select Configuration Manager
  Console.

2. In the Configuration Manager console, in the navigation pane, select Assets and
  Compliance.

3. In the Assets and Compliance workspace, go to Overview/Device Collections.

4. On the Ribbon, on the Home tab, in the Create group, select Create Device
  Collection.

  The Create Device Collection Wizard starts.

5. Complete the Create Device Collection Wizard using the following information.
  Accept the default values unless otherwise specified.

                                                                              ﾉ   Expand table

   On this        Do this
   wizard page

   On this        Do this
   wizard page

   General         a. In Name, type Microsoft Deployment - Batch 01.
                   b. In Comment, type Computers that are to be included in the first batch
                      of computers deployed.
                   c. In Limited Collection, select Browse.

                     The Select Collection dialog box appears. Complete the dialog box by
                     performing the following steps:

                        i. In the Select Collection dialog box, in Name, select All Systems.
                       ii. Select OK.
                   d. Select Next.

   Membership      a. Select Add Rule, and then select Direct Rule.
   Rules
                      The Create Direct Membership Rule Wizard starts.
                   b. Complete the Create Direct Membership Rule Wizard by performing
                      the following steps:

                       i. On the Welcome page, select Next.
                      ii. On the Search for Resources page, in Resource class, select System
                          Resource; in Attribute name, select Name; in Value, type WDG-CLI-
                          01; and then select Next.
