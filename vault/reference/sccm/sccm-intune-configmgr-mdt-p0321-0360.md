---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 321-360"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0321-0360
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0321-0360
family: sccm
documentKind: "doc"
abstract: "Configuring applications and operating system packages as described in Managing Software Packages in Configuration Manager which is the same process for UDI and ZTI deployments. Configuring device drivers as described in Managing Device Drivers in Configuration Manager, which is"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 321-360

<!-- p.321 -->

       Configuring applications and operating system packages as described in
       Managing Software Packages in Configuration Manager which is the same
       process for UDI and ZTI deployments.

       Configuring device drivers as described in Managing Device Drivers in
       Configuration Manager, which is the same process for UDI and ZTI
       deployments.

3. Ensure that all packages, including operating system deployment packages, that
  the new UDI task sequence uses are properly distributed to the assigned
  distribution points as described in Managing Distribution Points in Configuration
  Manager, which is the same process for UDI and ZTI deployments.

    ７ Note

    Most production networks have multiple distribution points. When
    performing this step in a production environment, select the appropriate
    distribution points for the network.

4. Customize the MDT configuration files to the needs of your organization as
  described in Configuring MDT Deployments.

    ） Important

    If you are capturing an image of the reference computer, you must at least
    add the DoCapture property to the CustomSettings.ini file for the task
    sequence by specifying DoCapture=YES or DoCapture=SYSPREP .

5. Optionally, enable monitoring of the MDT deployment process as described in
  Monitoring MDT Deployments.

6. Customize the task sequence to the needs of your organization as described in
  Configuring ZTI Task Sequence Steps in Configuration Manager, which is the same
  process for UDI and ZTI deployments.

    ７ Note

    The UDI deployment process is unable to perform Sysprep operations on a
    target computer that is encrypted by using BitLocker Drive Encryption. Do not
    enable BitLocker on the reference computer, and enable BitLocker on the

<!-- p.322 -->

        target computers only after the target operating system is completely
        deployed.

Deploying To and Capturing an Image of the Reference
Computer Using UDI
After the distribution points are updated, advertise the task sequence to the reference
computer and start the reference computer with the bootable Windows PE image
created earlier in the process. The task sequence created earlier will deploy the target
operating system, device drivers, operating system packages, and applications to the
reference computer, and then capture an image of the reference computer.

To deploy to and capture an image of the reference computer

   1. Add the reference computer to the Configuration Manager site database as
     described in Manually Adding Computers to the Site Database in Configuration
     Manager , which is the same process for UDI and ZTI deployments.

   2. Create a collection that contains the reference computer as described in Managing
     Computer Collections in Configuration Manager, which is the same process for UDI
     and ZTI deployments.

   3. Deploy the task sequence to the reference computer as described in Managing
     Task Sequence Deployment in Configuration Manager, which is the same process
     for UDI and ZTI deployments.

   4. Optionally, enable monitoring of the MDT deployment process as described in
     Monitoring MDT Deployments.

   5. Create a task sequence bootable media disk by using the Task Sequence Media
     Wizard as described in Creating Task Sequence Bootable Media in Configuration
     Manager, which is the same process for UDI and ZTI deployments.

   6. Start the reference computer with the task sequence bootable media disk as
     described in Deploying an Operating System Using Task Sequence Bootable Media
     in Configuration Manager which is the same process for UDI and ZTI deployments.

Preparing for UDI Deployment to Target Computers
After the images of the reference computers are captured, deploy them to the target
computers. In preparation for deploying the captured images to the target computers,

<!-- p.323 -->

create one or more task sequences for deploying the captured images, ensure that the
necessary deployment resources exist, and customize the MDT deployment process.

To prepare for UDI deployment to target computers

   1. Prepare network shares for storing migration data and MDT deployment logs as
     described in Preparing the MDT Migration Resources.

   2. Optionally, prepare Windows Deployment Services to start the appropriate
     Windows PE images that will in turn start the UDI deployment process to the
     target computers as described in Preparing Windows Deployment Services for UDI
     Deployments.

   3. Create additional distribution points to help in larger deployments as described in
     Managing Distribution Points in Configuration Manager, which is the same process
     for UDI and ZTI deployments.

   4. Prepare the UDI task sequences, the MDT configuration files, the UDI Wizard
     configuration files, and the MDT DB for each deployment scenario as described in
     the following sections:

           Prepare for the New Computer Deployment Scenario to Target Computers
           Using UDI

           Prepare for the Refresh Computer Deployment Scenario to Target Computers
           Using UDI

           Prepare for the Replace Computer Deployment Scenario to Target Computers
           Using UDI

           Depending on the target computers in your organization, any combination of
           these deployments scenarios might be necessary. For more information
           about MDT deployment scenarios, see Identifying Deployment Scenarios.

Prepare for the New Computer Deployment Scenario to Target
Computers Using UDI

In the New Computer deployment scenario, you deploy a new installation of a Windows
operating system to a new computer. There is no user migration information to save
and restore and no existing file systems to preserve. Use the User-Driven Installation
task sequence template to deploy the captured image of the reference computer to the
target computer.

<!-- p.324 -->

To prepare for the New Computer deployment scenario to target
computers using UDI

  1. Create a new task sequence that will deploy the target operating system to the
    reference computer using Create MDT Task Sequence Wizard in the Configuration
    Manager Console as described in Creating a ZTI Task Sequence Using MDT Task
    Sequence Templates in Configuration Manager, but ensure that you specifically
    follow the configuration settings on the wizard pages listed in Table 138 and select
    the appropriate values on the other wizard pages based on your organization's
    requirements.

       Tip

      Create the task sequence for deploying to the reference computer based on
      the Client Task Sequence task sequence template included in MDT.

    Table 138. Information for Completing the Create MDT
    Task Sequence Wizard for Performing New Computer
    Deployment Scenario Using UDI

                                                                           ﾉ   Expand table

     On this wizard   Do this
     page

     OS Image         Select Create a new OS image, and specify the fully qualified UNC path
                      to the WIM image captured from the reference computer.

     Deployment       Select Perform a "User-Drive Installation".
     Method

  2. Configure the application and operating system packages for deployment to the
    reference computer, including:

         Configuring applications and operating system packages as described in
         Managing Software Packages in Configuration Manager, which is the same
         process for UDI and ZTI deployments.

         Configuring device drivers as described in Managing Device Drivers in
         Configuration Manager, which is the same process for UDI and ZTI
         deployments.

<!-- p.325 -->

 3. Ensure that all packages, including operating system deployment packages, that
   the new UDI task sequence uses are properly distributed to the assigned
   distribution points as described in Managing Distribution Points in Configuration
   Manager, which is the same process for UDI and ZTI deployments.

     ７ Note

     Most production networks have multiple distribution points. When
     performing this step in a production environment, select the appropriate
     distribution points for the network.

 4. Customize the MDT configuration files to the needs of your organization as
   described in Configuring MDT Deployments.

 5. Optionally, customize the MDT DB to the needs of your organization as described
   in Performing Deployments Using the MDT DB (if you are using the MDT DB to
   provide MDT configuration information).

 6. Customize the task sequence to the needs of your organization as described in
   Configuring ZTI Task Sequence Steps in Configuration Manager, which is the same
   process for UDI and ZTI deployments.

 7. Customize the UDI Wizard configuration files to the needs of your organization as
   described in Configuring UDI Wizard Behavior.

 8. Optionally, enable monitoring of the MDT deployment process as described in
   Monitoring MDT Deployments.

 9. Ensure that all packages, including operating system deployment packages, that
   the new UDI task sequence uses are properly distributed to the assigned
   distribution points as described in Managing Distribution Points in Configuration
   Manager, which is the same process for UDI and ZTI deployments.

     ７ Note

     Most production networks have multiple distribution points. When
     performing this step in a production environment, select the appropriate
     distribution points for the network.

10. Update the distribution points so that any changes to the packages are distributed
   properly as described in Managing Distribution Points in Configuration Manager,
   which is the same process for UDI and ZTI deployments.

<!-- p.326 -->

       ７ Note

       Most production networks have multiple distribution points. When
       performing this step in a production environment, select the appropriate
       distribution points for the network.

Prepare for the Refresh Computer Deployment Scenario to Target
Computers Using UDI
In the Refresh Computer deployment scenario, a computer is refreshed, including
computers that must be re-imaged for image standardization or to address a problem.
There is user migration information to save and restore but no existing file systems to
preserve. Use the User Driven Installation Task Sequence template to deploy the
captured image of the reference computer to the target computer.

To prepare for the Refresh Computer deployment scenario to target
computers using UDI

   1. Create a new task sequence that will deploy the target operating system to the
     reference computer using the Create MDT Task Sequence Wizard in the
     Configuration Manager console as described in Creating a UDI Task Sequence
     Using MDT Task Sequence Templates, but ensure that you follow the configuration
     settings on the wizard pages listed in Table 139 and select the appropriate values
     on the other wizard pages for your organization's requirements.

        Tip

       Create the task sequence for deploying to the reference computer based on
       the Client Task Sequence task sequence template included in MDT.

     Table 139. Information for Completing the Create MDT
     Task Sequence Wizard for Performing Refresh
     Computer Deployment Scenario Using UDI

                                                                        ﾉ   Expand table

<!-- p.327 -->

   On this wizard   Do this
   page

   OS Image         Select Create a new OS image, and specify the fully qualified path to
                    the WIM image captured from the reference computer.

   Deployment       Select Perform a "User-Drive Installation".
   Method

2. Configure the appropriate software for deployment to the target computer in the
  Configuration Manager console, including:

       Configuring applications and operating system packages as described in
       Managing Software Packages in Configuration Manager

       Configuring device drivers as described in Managing Device Drivers in
       Configuration Manager

3. Optionally, customize the MDT configuration files or the MDT DB to the needs of
  your organization as described in:

       Configuring MDT Deployments

       Performing Deployments Using the MDT DB

4. Customize the task sequence to the needs of your organization as described in
  Configuring ZTI Task Sequence Steps in Configuration Manager, which is the same
  process for UDI and ZTI deployments.

5. Configure the behavior of the UDI Wizard to the needs of your organization as
  described in Configuring UDI Wizard Behavior.

6. Optionally, enable monitoring of the MDT deployment process as described in
  Monitoring MDT Deployments.

7. Ensure that all packages, including operating system deployment packages, that
  the new UDI task sequence uses are properly distributed to the assigned
  distribution points as described in Managing Distribution Points in Configuration
  Manager, which is the same process for UDI and ZTI deployments.

    ７ Note

    Most production networks have multiple distribution points. When
    performing this step in a production environment, select the appropriate
    distribution points for the network.

<!-- p.328 -->

   8. Update the distribution points so that any changes to the packages are distributed
     properly as described in Managing Distribution Points in Configuration Manager,
     which is the same process for UDI and ZTI deployments.

        ７ Note

        Most production networks have multiple distribution points. When
        performing this step in a production environment, select the appropriate
        distribution points for the network.

Prepare for the Replace Computer Deployment Scenario to Target
Computers Using UDI
In the Replace Computer deployment scenario, one computer replaces another
computer. Create a computer association record that associates the existing target
computer and the new target computer. The existing user state migration data is saved
from the existing target computer. Then, a new installation of Windows is deployed to a
new computer. Finally, the user state data is restored to the new computer. There are no
existing file systems to preserve.

  ） Important

  You must establish a computer association record for each existing target computer
  and each new target computer prior to performing the deployment to the target
  computer.

Use the:

     User Driven Installation Replace Task Sequence template to save the user state
     migration of the existing target computer

        ） Important

        Run this task sequence before running the task sequence based on the User
        Driven Installation Task Sequence template on the new target computer.

     Client Task Sequence template to deploy the captured image of the reference
     computer to the new target computer and restore the user state migration data

        ） Important

<!-- p.329 -->

      Run this task sequence after running the task sequence based on the User
      Driven Installation Replace Task Sequence template on the existing target
      computer.

To prepare for the Replace Computer deployment scenario to target
computers using UDI

  1. Create a computer association between the existing target computer and the new
    target computer as described in "How to Perform a Side-by-Side Operating System
    Deployment," in the section, "How to Deploy Operating Systems in Configuration
    Manager," in Configuration Manager Documentation Library, which is installed
    with Configuration Manager.

  2. Create a new task sequence that will save the user state migration data of the
    existing target computer as described in Creating a UDI Task Sequence Using MDT
    Task Sequence Templates.

       Tip

      Create the task sequence for capturing the user state migration data from the
      target computer based on the User Driven Installation Task Replace Sequence
      template included in MDT.

  3. Create a new task sequence that will deploy the captured image of the reference
    computer to the target computer, and restore the user state migration data saved
    by the User Driven Installation Replace Task Sequence as described in Creating a
    UDI Task Sequence Using MDT Task Sequence Templates, but ensure that you
    specifically follow the configuration settings on the wizard pages listed in Table
    140 and select the appropriate values on the other wizard pages for your
    organization's requirements.

       Tip

      Create the task sequence for deploying to the target computer based on the
      ClientTask Sequence template included in MDT.

    Table 140. Information for Completing the Create MDT
    Task Sequence Wizard for Performing the Replace
    Computer Deployment Scenario using UDI

<!-- p.330 -->

                                                                         ﾉ   Expand table

   On this wizard   Do this
   page

   OS Image         Select Create a new OS image, and specify the fully qualified UNC path
                    to the WIM image captured from the reference computer.

   Deployment       Select Perform a "User-Drive Installation".
   Method

4. Configure the appropriate software for deployment to the target computer in the
  Configuration Manager console, including:

       Configuring applications and operating system packages as described in
       Managing Software Packages in Configuration Manager, which is the same
       process for UDI and ZTI deployments.

       Configuring device drivers as described in Managing Device Drivers in
       Configuration Manager, which is the same process for UDI and ZTI
       deployments.

5. Customize the MDT configuration files or the MDT DB to the needs of your
  organization as described in:

       Configuring MDT Deployments

       Performing Deployments Using the MDT DB

6. Customize the task sequences to the needs of your organization as described in
  Configuring ZTI Task Sequence Steps in Configuration Manager, which is the same
  process for UDI and ZTI deployments.

7. Optionally, enable monitoring of the MDT deployment process as described in
  Monitoring MDT Deployments.

8. Ensure that the distribution points for the packages and operating system images
  that the new ZTI task sequence uses are distributed properly as described in
  Managing Distribution Points in Configuration Manager, which is the same process
  for UDI and ZTI deployments.

    ７ Note

    Most production networks have multiple distribution points. When
    performing this step in a production environment, select the appropriate

<!-- p.331 -->

       distribution points for the network.

   9. Update the distribution points so that any changes to the packages are distributed
     properly as described in Managing Distribution Points in Configuration Manager,
     which is the same process for UDI and ZTI deployments.

       ７ Note

       Most production networks have multiple distribution points. When
       performing this step in a production environment, select the appropriate
       distribution points for the network.

Deploying Captured Images to Target Computers Using
UDI
The deployment of the captured images to the target computers is slightly different for
each MDT deployment scenario using UDI. Deploy the captured image of the reference
computer to target computers for each respective deployment scenario in your
organization.

To deploy the capture image of the reference computer to the
target computers using UDI

   1. Add the target computer to the Configuration Manager site database:

          Manually, as described in Manually Adding Computers to the Site Database
          in Configuration Manager, which is the same process for UDI and ZTI
          deployments.

          Automatically in Configuration Manager as described in the section, "How to
          Manage Unknown Computer Deployments in Configuration Manager," in the
          Configuration Manager Documentation Library, which is installed with
          Configuration Manager.

       ７ Note

       If the target computers already exist in the Configuration Manager Site
       database, then this step is not necessary.

<!-- p.332 -->

2. Create a collection that contains the target computers as described in Managing
  Computer Collections in Configuration Manager, which is the same process for UDI
  and ZTI deployments.

    ７ Note

    Create a collection for each MDT deployment scenario to be performed, and
    ensure that the collection includes the target computers requiring the
    corresponding deployment scenario.

3. Create an advertisement for the target computer task sequences as described in
  Managing Task Sequence Deployment in Configuration Manager, which is the
  same process for UDI and ZTI deployments.

4. Provide a method for starting the target computers by doing any combination of
  the following:

       Create a task sequence bootable media disk using the Task Sequence Media
       Wizard as described in Creating Task Sequence Bootable Media in
       Configuration Manager, which is the same process for UDI and ZTI
       deployments.

       Prepare Windows Deployment Services to start the appropriate Windows PE
       images that will in turn start the UDI deployment process to the target
       computers as described in Preparing Windows Deployment Services for ZTI
       Deployments Using Configuration Manager, which is the same process for
       UDI and ZTI deployments.

5. Deploy the captured reference computer image to the target computers for each
  deployment scenario as described in:

       Deploy Captured Images to Target Computers in the New Computer
       Deployment Scenario Using UDI

       Deploy Captured Images to Target Computers in the Refresh Computer
       Deployment Scenario Using UDI

       Deploy Captured Images to Target Computers in the Replace Computer
       Deployment Scenario Using UDI

       Depending on the target computers in your organization, any combination of
       deployments scenarios might be necessary. For more information about the
       MDT deployment scenarios, see Identifying Deployment Scenarios.

<!-- p.333 -->

Deploy Captured Images to Target Computers in the New
Computer Deployment Scenario Using UDI

Start the target computer with the task sequence bootable media created earlier in the
process or from Windows Deployment Services. Either method starts Windows PE on the
target computer and initiates the UDI deployment process. At the end of the process,
the captured image of the reference computer is deployed on the target computer.

To deploy the capture images to the target computers in the New
Computer Deployment Scenario using UDI

   1. Start the target computer with the task sequence bootable media created earlier in
     the process or from Windows Deployment Services.

     The Task Sequence Wizard starts.

   2. Complete the Task Sequence Wizard, ensuring that you specifically follow the
     configuration settings on the wizard pages listed in Table 141 and select the
     appropriate values on the other wizard pages for your organization's requirements.

       ７ Note

       This wizard will not appear if you configure UDI to perform a PXE boot and
       have configured a mandatory advertisement or if only one task sequence is
       advertised to the target computer.

     Table 141. Information for Completing the Task
     Sequence Wizard in the New Computer Deployment
     Scenario using UDI

                                                                             ﾉ   Expand table

      On this wizard    Do this
      page

      Select a Task     Select the task sequence you created for the target computer
      Sequence          deployment for the New Computer deployment scenario.

     The wizard starts, and the operating system deployment starts. Eventually the task
     sequence starts the UDI Wizard.

<!-- p.334 -->

   3. Optionally, view the MDT deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

     For more information about monitoring MDT deployments, see View MDT
     Deployment Progress.

   4. Complete the UDI Wizard by selecting the appropriate values on the wizard pages
     for your organization's requirements as described in Running the UDI Wizard.

Deploy Captured Images to Target Computers in the Refresh
Computer Deployment Scenario Using UDI

Start this scenario by running the Configuration Manager task sequence deployment
(advertisement) for capturing the user state migration data that you created earlier in
the process. This task sequence runs in the current operating system on the existing
target computer.

To deploy the capture images to the target computers in the Refresh
Computer Deployment Scenario Using UDI

   1. On the target computer, run the Configuration Manager deployment
     (advertisement) for capturing the Refresh Computer deployment scenario that you
     created earlier in the deployment process.

     The task sequence starts. Eventually, the task sequence starts the UDI Wizard.

   2. Complete the UDI Wizard by selecting the appropriate values on the wizard pages
     for your organization's requirements, as described in Running the UDI Wizard.

   3. Optionally, view the MDT deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

     For more information about monitoring MDT deployments, see View MDT
     Deployment Progress.

     The task sequence runs in Windows PE to capture user state migration data. The
     task sequence restarts the computer, starts Windows PE, and then initiates
     installation of the new operating system. The task sequence restarts the computer,
     starts the new operating system, restores the user state migration data, installs any
     packages, installs any applications, and performs any other actions configured in
     the task sequence. Finally, the OSD Results program, OSDResults.exe, runs and
     displays the results of the deployment. The target computer is now deployed.

<!-- p.335 -->

Deploy Captured Images to Target Computers in the Replace
Computer Deployment Scenario Using UDI

The Replace Computer deployment scenario requires two separate steps to complete
the migration. First, run the deployment (advertisement) for the task sequence you
created to capture the user state migration data from the existing target computer (old
computer). Second, run the UDI Wizard to deploy the captured image of the reference
computer to the new target computer (new computer) and restore the user state saved
earlier in the process.

To deploy captured images of the reference computer to target
computers in the Replace Computer deployment scenario using UDI

   1. Save the user state migration data from the existing target computer as described
     in Save the User State Migration Data in the Replace Computer Deployment
     Scenario Using UDI.

   2. Deploy the captured image of the reference computer to the new target computer
     as described in Deploy the Captured Image and User State Migration Data in the
     Replace Computer Deployment Scenario Using UDI.

Save the User State Migration Data in the Replace Computer
Deployment Scenario Using UDI

Start this scenario by running the task sequence deployment (advertisement) for
capturing the user state migration data that you created earlier in the process. This task
sequence runs in the current operating system on the existing target computer.

To save the user state migration data from the existing target
computers in the Replace Computer Deployment Scenario using UDI

   1. Run the task sequence deployment (advertisement) for capturing user state
     migration data that you created earlier in the process Refresh Computer
     deployment scenario.

   2. Optionally, view the MDT deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

     For more information about monitoring MDT deployments, see View MDT
     Deployment Progress.

     The task sequence runs in the current operating system to capture user state
     migration data. At the end of the task sequence, the user state migration data of

<!-- p.336 -->

     the existing target computer is saved to the Configuration Manager state
     migration point.

Deploy the Captured Image and User State Migration Data in the
Replace Computer Deployment Scenario Using UDI

Start the target computer with the ZTI bootable media created earlier in the process or
from Windows Deployment Services. The ZTI bootable media starts Windows PE on the
target computer and initiates the UDI deployment process. At the end of the
deployment process, the captured image of the reference computer is deployed on the
target computer, and the user state migration data is restored from the Configuration
Manager state migration point.

To complete the Windows Deployment Wizard in the Replace
Computer deployment scenario for deploying the captured image
using UDI

   1. Start the reference computer with the ZTI bootable media created earlier in the
     process or from Windows Deployment Services.

     Windows PE starts, and then the Windows Deployment Wizard starts.

   2. Complete the Task Sequence Wizard, ensuring that you follow the configuration
     settings for the wizard pages listed in Table 142 and select values on the other
     wizard pages for your organization's requirements.

       ７ Note

       This wizard will not appear if you configure ZTI to perform a PXE boot and
       have configured a mandatory advertisement or if only one task sequence is
       advertised to the target computer.

     Table 142. Information for Completing the Task
     Sequence Wizard for the Replace Computer
     Deployment Scenario Using UDI

                                                                         ﾉ   Expand table

<!-- p.337 -->

      On this         Do this
      wizard page

      Select a Task   Select the task sequence you created for the target computer deployment
      Sequence        in the Replace Computer deployment scenario to deploy the captured
                      image of the reference computer to the new target computer.

     The task sequence starts. Eventually, the task sequence starts the UDI Wizard.

  3. Complete the UDI Wizard by selecting the appropriate values on the wizard pages
     for your organization's requirements, as described in Running the UDI Wizard.

  4. Optionally, view the MDT deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

     For more information about monitoring MDT deployments, see View MDT
     Deployment Progress.

     The task sequence starts Windows PE and then initiates installation of the new
     operating system. The task sequence restarts the computer, starts the new
     operating system, restores the user state migration data, installs any packages,
     installs any applications, and performs any other actions configured in the task
     sequence. Finally, the OSD Results program, OSDResults.exe, runs and displays the
     results of the deployment. The target computer is now deployed.

Managing UDI Deployments
You manage UDI deployments through the Configuration Manager console and the UDI
Wizard Designer. You use the Deployment Workbench in UDI deployments only to
configure the MDT DB. The wizard used to create UDI task sequences are integrated into
the Configuration Manager console. You can use the UDI Wizard Designer to configure
the behavior of the UDI Wizard.

Manage UDI deployments by:

     Reviewing UDI administration process as described in Overview of UDI
     Administration

     Creating a new task sequence for UDI deployments using the Create MDT Task
     Sequence Wizard as described in Creating a UDI Task Sequence Using MDT Task
     Sequence Templates

     Managing operating systems for UDI deployments in the Configuration Manager
     Console as described in Managing Operating Systems in Configuration Manager

<!-- p.338 -->

which is the same process for UDI and ZTI deployments

Managing device drivers for UDI deployments in the Configuration Manager
Console as describe in Managing Device Drivers in Configuration Manager, which
is the same process for UDI and ZTI deployments

Deploying an operating system using task sequence bootable media as described
in Deploying an Operating System Using Task Sequence Bootable Media in
Configuration Manager, which is the same process for UDI and ZTI deployments

Creating task sequence bootable media for UDI as described in Creating Task
Sequence Bootable Media in Configuration Manager, which is the same process for
UDI and ZTI deployments

Creating boot images for use with UDI using the Create Image Using Microsoft
Deployment Wizard as described in Creating ZTI Boot Images in Configuration
Manager, which is the same process for UDI and ZTI deployments

Managing software packages for UDI in the Configuration Manager console as
described in Managing Software Packages in Configuration Manager, which is the
same process for UDI and ZTI deployments

Managing advertisements for UDI as described in Managing Task Sequence
Deployment in Configuration Manager, which is the same process for UDI and ZTI
deployments

Manually adding computers to the site database for UDI as described in Manually
Adding Computers to the Site Database in Configuration Manager, which is the
same process for UDI and ZTI deployments

Managing computer collections for UDI as described in Managing Computer
Collections in Configuration Manager, which is the same process for UDI and ZTI
deployments

Managing distribution points for UDI as described in Managing Distribution Points
in Configuration Manager, which is the same process for UDI and ZTI deployments

Configuring individual UDI task sequence steps as described in Configuring ZTI
Task Sequence Steps in Configuration Manager, which is the same process for UDI
and ZTI deployments

Configuring the UDI Wizard behavior by customizing the UDI Wizard configuration
file as described in Configuring UDI Wizard Behavior

<!-- p.339 -->

     Creating a custom wizard page to collect additional deployment information as
     described in Creating Custom Wizard Pages Using the Build Your Own Page
     Feature

Overview of UDI Administration
The goal of UDI administration is to configure the user experience in the UDI Wizard
and ultimately control the deployment of Windows operating systems and applications
to target computers. You configure the UDI user experience by using the UDI Wizard
Designer and by customizing the Configuration Manager task sequences used with UDI
in the Configuration Manager Console.

The primary tool for administering UDI is the UDI Wizard designer. The UDI Wizard
Designer is installed as a part of MDT, which is installed on the same computer at the
Configuration Manager Console. Because UDI is built-on the OSD feature in
Configuration Manager, you will also use the Configuration Manager Console to
administer specific aspects of UDI deployments.

Figure 6 illustrates the high-level overview of the UDI administrative process.

Figure 6. Overview of UDI administration process

The UDI administration process, as illustrated in Figure 6, is performed as follows:

<!-- p.340 -->

1. Create a UDI task sequence based on the task sequence templates built-in to MDT.

  As a part of creating the task sequence, the Create MDT Task Sequence wizard
  creates an MDT toolkit package that contains the contents of the
  installation_folder\Templates\Distribution folder (where installation_folder is the
  folder where you installed MDT). The toolkit package is referenced by the Use
  Toolkit Package task sequence step.

  For more information about the built-in UDI tasks sequence templates in MDT, see
  Identify the UDI Task Sequence Templates in MDT.

2. Distribute the MDT toolkit package to Configuration Manager distribution points.

  The UDI Wizard and UDI Wizard configuration file are contained in the package.
  The UDI Wizard (UDIWizard.exe) is in the Tools folder in the package. The UDI
  Wizard configuration file (UDIWizard_Config.xml) is in the Scripts folder in the
  package.

3. Customize the UDI Wizard configuration file and application information file using
  the UDI Wizard Designer.

  The UDI Wizard configuration file (UDIWizard_Config.xml) and application
  information file (UDIWizard_Config.xml.app) are stored in the Scripts folder in the
  MDT toolkit package.

4. Update the distribution points with the modified version of the UDI Wizard
  configuration file and corresponding application information file in the MDT toolkit
  package.

5. The target computers initiate the UDI task sequence which runs the UDI Wizard at
  the appropriate point in the task sequence.

  The UDI Wizard is initiated using the UDI Wizard task sequence step.

6. The UDI Wizard runs and the deployment configuration information is collected
  from the user.

  The UDI Wizard reads the UDI Wizard configuration file to determine the wizard
  pages to display and the sequence of the pages. The user completes the UDI
  Wizard by providing the necessary deployment information. The UDI Wizard
  updates task sequence variables based on the information provided. The updated
  task sequence variables are used by the UDI task sequence to perform the balance
  of the deployment.

<!-- p.341 -->

  7. The remainder of the task sequence steps in the UDI task sequence complete and
     the OSD Results dialog is displayed at the end of the deployment. Any applications
     installed during the task sequences are identified the first time a user logs in using
     AppInstaller.

     AppInstaller enables Configuration Manager to identify any applications installed
     using the Application model during the task sequence. This allows Configuration
     Manager to use features such as the monitoring feature.

Creating a UDI Task Sequence Using MDT Task Sequence
Templates
Use the Create MDT Task Sequence Wizard in the Configuration Manager console to
create task sequences in Configuration Manager that are integrated with MDT. MDT
includes task sequence templates that you can use to deploy the reference and target
computers.

Create UDI task sequences using the MDT task sequence templates by:

     Identifying the UDI task sequence templates that are a part of MDT as described in
     Identify the UDI Task Sequence Templates in MDT

     Identifying the packages and images that the UDI task sequence templates require
     as described in Identify the Packages and Images That the UDI Task Sequence
     Templates Require

     Creating UDI task sequences as described in Create UDI Task Sequences Using the
     Create MDT Task Sequence Wizard

     Configure UDI task sequences to deploy different operating systems as described
     in Configure UDI Task Sequences to Deploy Different Operating Systems

Identify the UDI Task Sequence Templates in MDT

MDT includes task sequence templates that are used to create MDT task sequences in
Configuration Manager. The task sequence templates included in MDT are described in
Identify the Task Sequence Templates in MDT in Configuration Manager.

Of the templates described in Identify the Task Sequence Templates in MDT in
Configuration Manager, the following are used in MDT deployment scenarios using UDI:

     Client Task Sequence. This task sequence template is used for the MDT New
     Computer, Refresh Computer, and Replace Computer deployment scenarios. This

<!-- p.342 -->

     task sequence template is also used to build and capture images of the reference
     computers.

     User Driven Installation Replace Task Sequence. This task sequence template is
     the first step in a two-step process in the MDT Replace Computer deployment
     scenario and is used to capture user state migration data. The second step in the
     two step process is the User Driven Installation Task Sequence task sequence
     template, which is used to:

        Deploy the target applications and operating system

        Restore the user state migration data saved during the User Driven Installation
        Replace task Sequence task sequence template in the first step of the process

     For more information on the MDT deployment scenarios, see Identifying
     Deployment Scenarios.

  ７ Note

  Always use the Create MDT Task Sequence Wizard to create task sequences.
  Although you can manually create the task sequences, doing so is not
  recommended.

Identify the Packages and Images That the UDI Task Sequence
Templates Require
The UDI task sequence templates require the same packages and images as required by
ZTI deployments, as described in Identify the Packages and Images That the MDT Task
Sequence Templates in Configuration Manager Require.

Create UDI Task Sequences Using the Create MDT Task Sequence
Wizard
The Create MDT Task Sequence Wizard substitutes the packages and images selected
for the placeholders in the task sequence templates. After completing the wizard, the
new task sequence references the appropriate packages and images.

  ７ Note

  Always use the Create MDT Task Sequence Wizard to create task sequences based
  on the MDT task sequence templates. Although you can manually import the task

<!-- p.343 -->

  sequence templates, doing so is not recommend.

Create UDI task sequences using the same process for creating ZTI task sequences using
the Create MDT Task Sequence Wizard as described in Create ZTI Task Sequences Using
the Create MDT Task Sequence Wizard in Configuration Manager

Select the appropriate UDI task sequence template based on the deployment scenario
being performed. For more information about the UDI task sequence templates in MDT,
see Identify the UDI Task Sequence Templates in MDT.

Configure UDI Task Sequences to Deploy Different Operating
Systems
The VolumePage page in built-in UDI stage groups allows you to select from any
operating system images that you have configured in the UDI Wizard Designer.
However, the task sequence created by the Create MDT Task Sequence wizard
references only one specific operating system image in the Apply Operating System
Image task sequence step.

When you select the operating system image on the VolumePage page, the UDI Wizard
sets the OSDImageName task sequence variable to the value of the image name that
was selected. The value of the OSDImageName task sequence variable corresponds to
the name of the operating system image in the Operating System Images or Operating
System Installers nodes in the Configuration Manager console.

You can configure a UDI task sequence to support the operating systems you have
added to the VolumePage page by performing the following steps:

  1. Rename the existing Apply Operating System Image task sequence step to reflect
     the name of the operating system image being deployed.

  2. Configure a condition for the existing Apply Operating System Image task
     sequence step that will only run the step when the OSDImageName task sequence
     variable is equal to the name of the operating system image being deployed.

  3. For each operating system that has been added to the VolumePage page, perform
     the following steps:

     a. Add a new Apply Operating System Image task sequence step that reflects the
        name of the operating system image to be deployed.

     b. Configure a condition for the new Apply Operating System Image task
        sequence step that will only run the step when the OSDImageName task

<!-- p.344 -->

        sequence variable is equal to the name of the operating system image to be
        deployed.

     After performing these steps, when the user selected an operating system image
     on the VolumePage page, the corresponding Apply Operating System Image task
     sequence step will be run and deploy the appropriate operating system image.

Configuring UDI Wizard Behavior
The User-Driven Installation Task Sequence and User-Driven Installation Replace Task
Sequence templates include task sequence steps that run the UDI Wizard. When a task
sequence step runs the UDI Wizard, the step also references the UDIWizard_Config.xml
file, which controls the behavior of the UDI Wizard and is stored in the Scripts folder of
the MDT files package. You can customize the UDIWizard_Config.xml file using the UDI
Wizard Designer.

Configure the UDI Wizard behavior by performing the following steps in the UDI Wizard
Designer:

     Review the UDI Wizard Designer concepts as described in Review UDI Wizard
     Designer Concepts.

     Identify the UDI components used in performing UDI deployments and the
     relationship between those components as described in Identify UDI Deployment
     Process Components.

     Review the relationship between the UDI wizard pages, UDI wizard page editors,
     and the UDI Wizard configuration file as described in Review the Relationship
     Among UDI Wizard Pages, Wizard Page Editors, and the UDI Wizard Configuration
     File.

     Review the UI of the UDI Wizard Designer as described in Review the UDI Wizard
     Designer User Interface.

     Create a new UDI Wizard configuration file as described in Create a New UDI
     Wizard Configuration File.

     Open an existing UDI Wizard configuration file as described in Open an Existing
     UDI Wizard Configuration File.

     Save changes in the UDI Wizard Designer to a UDI Wizard configuration file as
     described in Save UDI Wizard Configuration Updates.

<!-- p.345 -->

     Override the location and name of the UDI configuration file used by a task
     sequence as described in Override the Configuration File That the UDI Wizard
     Uses.

     Configure the title and banner image to be displayed in the UDI Wizard as
     described in Configure the UDI Wizard Title and Banner Image.

     Add a wizard page to a stage as described in Add a Wizard Page to a Stage.

     Remove a wizard page from a stage as described in Remove a Wizard Page from a
     Stage.

     Change the sequence of a wizard page within a stage as described in Change the
     Wizard Page Sequence Flow Within a Stage.

     Allow or prevent users from entering information in a control on a wizard page as
     described in Allow or Prevent Users from Entering Information in a Control on a
     Wizard Page.

     Configure the user experience for a wizard page as described in Configure the User
     Experience for a Wizard Page.

     Preview how the wizard pages and wizard page sequence flow the UDI Wizard as
     described in Preview Wizard Pages and the Wizard Page Sequence Flow.

     Add a wizard page to the page library as described in Add a Wizard Page to the
     Page Library.

     Remove a wizard page from the page library as described in Remove a Wizard
     Page from the Page Library.

     Change the sequence of a stage group or a stage within a stage group as
     described in Change the Sequence of a Stage Group or a Stage.

     Prepare for language pack deployment using the UDI Wizard as described in
     Prepare for Language Pack Deployment in UDI.

     Skip (remove) a wizard page from a stage as described in Skip a Wizard Page.

Review UDI Wizard Designer Concepts

The UDI Wizard Designer is a console in MDT that allows you to easily configure the UDI
Wizard configuration file. The UDI Wizard Designer can update an existing UDI Wizard
configuration file or create a new UDI Wizard configuration file.

<!-- p.346 -->

  ７ Note

  If you are unfamiliar with UDI, review the UDI terms and terminology in "UDI
  Concepts". Familiarizing yourself with these terms and terminology will help you be
  more successful in applying this guide to your organization.

At a high-level, the UDI Wizard Designer allows you to configure the:

     Types of wizard pages that are displayed in the UDI Wizard

     Sequence of the wizard pages as they will appear in the UDI Wizard

     Configuration settings for each wizard page

     For more detailed information about the tasks that can be performed in the UDI
     Wizard Designer, see Configuring UDI Wizard Behavior.

Identify UDI Deployment Process Components
The UDI deployment process is based on ZTI deployments in MDT and requires
Configuration Manager. The UDI process runs as any other MDT task sequence, except
that the UDI-specific task sequences run the UDI Wizard at the appropriate steps in the
task sequence.

Table 143 lists the UDI deployment process components and a brief description of how
they work together in a UDI deployment.

Table 143. UDI Deployment Process Components

                                                                               ﾉ   Expand table

 Component        Description

 UDI Wizard       The UDI Wizard is the UI that allows customization of the deployment process
                  based on configuration settings made in the wizard. The configuration
                  settings are used to modify the task sequence variables and unattended
                  installation files used in the operating system and application deployment
                  process.

                  The UDI Wizard is initiated by the appropriate task sequence steps in task
                  sequences created using UDI task sequence templates.

                  The wizard pages that are displayed in the UDI Wizard and the controls that

<!-- p.347 -->

 Component        Description

                  are active for each wizard page is controlled by the UDI Wizard configuration
                  file.

 UDI Wizard       The UDI Wizard Designer is used to customize the UDI Wizard configuration
 Designer         file. You can use the UDI Wizard Designer to:

                  - Determine the wizard pages that are displayed in the UDI Wizard

                  - Determine the sequence of the wizard pages that are displayed in the UDI
                  Wizard

                  - Configure default values for controls on the wizard pages

                  - Enable or disable individual controls on the wizard pages

 UDI Wizard       The UDI Wizard configuration file is read by the UDI Wizard to determine the
 configuration    wizard pages that are displayed, the sequence of the wizard pages, any
 file             default values for controls, and whether controls are enabled or disabled for
                  user interaction.

                  The UDI Wizard configuration file is customized using the UDI Wizard
                  Designer.

                  The default UDI Wizard configuration file is name UDIWizard_Config.xml and
                  is stored in the Scripts folder in the MDT files package.

 UDI task         The UDI task sequences are created using UDI-related MDT task sequence
 sequences        templates. The UDI task sequence templates include the task sequence step to
                  run the UDI Wizard at the appropriate time in the UDI deployment process.

                  For more information about UDI task sequence templates, see Identify the UDI
                  Task Sequence Templates in MDT.

Review the Relationship Among UDI Wizard Pages, Wizard Page
Editors, and the UDI Wizard Configuration File
For each wizard page displayed in the UDI Wizard, there is a corresponding wizard page
editor that can be used to configure that wizard page using the UDI Wizard Designer.
The UDI Wizard configuration file (UDIWizard_Config.xml) is used to store the
configuration settings for each wizard page. Figure 7 illustrates the relationship between
UDI wizard pages, UDI wizard page editors, and the UDI Wizard configuration file.

<!-- p.348 -->

Figure 7. Relationship between UDI wizard pages, UDI wizard page editors, and the
UDI Wizard configuration file

In the UDI Wizard configuration file, there is a separate Page XML element for each
wizard page that is displayed in the UDI Wizard. When you add a wizard page using the
UDI Wizard Designer a corresponding Page XML element is created in the UDI Wizard
configuration file. Similarly, when you remove a wizard page, the corresponding Page
XML element is removed.

Each Page XML element has child XML elements for each configuration setting for the
wizard page. These child XML elements are also configured using the wizard page
editors in the UDI Wizard Designer.

For a complete list of the Page XML elements, see the "UDI Wizard Configuration File
Schema Reference".

  ７ Note

  Do not directly modify the UDI Wizard configuration file. Instead, use the
  appropriate wizard page editors in the UDI Wizard Designer.

Review the UDI Wizard Designer User Interface

<!-- p.349 -->

The UDI Wizard Designer is used to customize the user experience in the UDI Wizard,
including the:

     Wizard pages that are displayed in the UDI Wizard (wizard pages can be added or
     removed)

     Sequence of the wizard pages as they are displayed in the UDI Wizard

     Controls on each wizard page, such as:

        Enabling a control for user interaction

        Disabling a control for user interaction

        Specifying a default value

     Review the UDI Wizard Designer UI by completing the following steps:

   1. Review the UDI Wizard Designer high-level UI elements as described in Review the
     UDI Wizard Designer High-Level User Interface Elements.

   2. Review the Page Library pane UI elements in the UDI Wizard Designer as
     described in Review the Page Library Pane in the UDI Wizard Designer.

   3. Review the Flow tab in the details pane the UDI Wizard Designer as described in
     Review the Flow Tab in the UDI Wizard Designer.

   4. Review the Configure tab in the details pane the UDI Wizard Designer as described
     in Review the Configure Tab in the UDI Wizard Designer.

Review the UDI Wizard Designer High-Level User Interface
Elements

Figure 8 illustrates the UDI Wizard Designer high-level UI elements.

<!-- p.350 -->

Figure 8. UDI Wizard Designer high-level UI elements

Table 144 lists the high-level UI elements illustrated in Figure 8 and provides a brief
description of each element.

Table 144. UDI Wizard Designer High-Level UI Elements

                                                                                ﾉ   Expand table

 UI          Description
 element

 Ribbon      Provides access to task-based actions that can be performed within the UDI Wizard
             Designer. The actions are combined into groups, such as the File Menu group or the
             Flow Designer group.

 Page        Contains the wizard pages that are available for use within the UDI Wizard Designer.
 Library     The number of times that each page is used within the UDI Wizard configuration file

<!-- p.351 -->

 UI         Description
 element

 pane       is displayed on the far right portion of the wizard page entry. For example, the
            Language page is used three times while the Scan Configuration page is used twice.

 Details    Provides access to the configuration details of the UDI Wizard configuration file
 pane       being customized.

Review the Page Library Pane in the UDI Wizard Designer

Figure 9 illustrates the UI elements in the Page Library pane in the UDI Wizard Designer.

<!-- p.352 -->

Figure 9. UI elements in the Page Library pane

Table 145 lists the UI elements illustrated in Figure 9 and provides a brief description of
each element.

Table 145. UI Elements in the Page Library Pane

                                                                           ﾉ   Expand table

<!-- p.353 -->

 UI element      Description

 Page            Each wizard page in the Page Library is an instance of a specific wizard page type.
 instance        As shown in REF _Ref307996589 \h Figure 9, there are two instances of the
                 ConfigScanPage wizard page type with the page name of ConfigScanBareMetal
                 and ConfigScanPage.

                 Configuration settings are made to a wizard page instance in the Page Library and
                 affect all stages to which the wizard page is added.

 Page type       A page type defines a template that can be used to create instances of the wizard
                 page type. The Add New Page dialog box has a list of the wizard page types
                 available in the UDI Wizard Designer.

 Display name    This is the user-friendly name for the instance of the wizard page type. This value
                 does not have to be unique within the Page Library.

 Page name       This is the name of the instance of the wizard page type. This value must be
                 unique within a page library.

 Number of       This element maintains a count of the number of times that a wizard page
 times page is   instance is used in the stages. For example, as shown in REF _Ref307996589 \h
 used            Figure 9, the ComputerPage wizard page instance is used in two different places
                 within the UDI Wizard configuration file.

Review the Flow Tab in the UDI Wizard Designer

Figure 10 illustrates the UI elements in the Flow tab in the details pane. The Flow tab is
used to configure the:

   1. Wizard pages that will be displayed in the UDI Wizard for a specific stage within a
     specific stage group

   2. Sequence of the wizard pages as they are displayed in the UDI Wizard

<!-- p.354 -->

    Figure 10. Flow tab in the UDI Wizard Designer

    Table 146 lists the UI elements on the Flow tab, which is illustrated in Figure 10,
    and provides a brief description of each element.

Table 146. UDI Wizard Designer Flow Tab UI Elements

                                                                              ﾉ   Expand table

UI element   Description

Stage        Collection of one or more sets of wizard page groupings (stages) that are used by
group        the deployment scenarios that UDI supports, including the New Computer, Refresh
             Computer, and Replace Computer MDT deployment scenarios.

             The stage groups are predefined in UDI. Adding or removing stage groups is not
             supported.

Stage        Collection of one or more wizard pages used at a specific time within a stage
             group.

             For the New Computer stage group, MDT includes the following stages:

<!-- p.355 -->

 UI element   Description

              - NEWCOMPUTER. This stage is used for new computer deployments.

              - NEWCOMPUTER.Prestaged. This stage is used for prestaged media deployments
              in Configuration Manager.

              For the Replace Computer stage group, MDT includes the following stages:

              1. REPLACE. This stage is used for the portion of the Replace Computer stage
              group performed in the original operating system running on the target computer.

              2. REPLACE.WinPE. This stage is used for the portion of the Replace Computer
              stage group performed in Windows PE.

              The stages are predefined in UDI. Adding or removing stages is not supported.

 Wizard       The wizard page that is to be displayed in the UDI Wizard for a specific stage within
 page         a specific stage group.

              A wizard page is based on an instance of the wizard page in the Page Library. An
              instance of a wizard page may appear in multiple stages and stage groups.
              Configuration settings for a wizard page affect the wizard page instance, not the
              individual pages that appear in the stages and stage groups.

              Create a unique instance of a wizard page in the Page Library for each set of
              unique configuration settings that you want to manage for a specific type of wizard
              page.

 Wizard       The sequence in which the wizard page is displayed in the UDI Wizard for a specific
 page         stage within a specific stage group.
 sequence

Review the Configure Tab in the UDI Wizard Designer

Figure 11 illustrates the UI elements in the Configure tab in the details pane. You use
the Configure tab to configure the individual controls on the wizard page.

  ７ Note

  Any changes made to the settings on the Configure tab affect the instance of that
  wizard page in the Page Library. The result is any stage groups or stages that
  contain the same instance of that wizard page will also reflect the changes in the
  configuration settings.

<!-- p.356 -->

Figure 11. Configure tab in the UDI Wizard Designer

Table 147 lists the UI elements on the Flow tab, which is illustrated in Figure 11, and
provides a brief description of each element.

Table 147. UDI Wizard Designer Configure Tab UI
Elements

                                                                              ﾉ   Expand table

 UI element     Description

 Page           Expand to show a sample of the wizard page as displayed in the UDI Wizard.
 screenshot

 Section        Logical grouping of one or more user controls.

 Subsection     Logical grouping of one or more user controls within a section. Expand to show
                the user controls contained within the configuration details.

<!-- p.357 -->

If you expand a subsection, you can see the controls within that subsection. Figure 12
illustrates the UI elements for a control beneath a subsection. A subsection may contain
multiple controls.

Figure 12. UI elements for a control on the Configure tab in the UDI Wizard Designer

Table 148 lists the UI elements for a control on the Configure tab, which is illustrated in
Figure 12, and provides a brief description of each element.

  ７ Note

<!-- p.358 -->

  Each control on a wizard page is unique and has different UI elements. The control
  illustrated in Figure 12 is provided as an example for generalized discussion.

Table 148. UI Elements for a Control on the Configure Tab

                                                                                   ﾉ   Expand table

 UI element           Description

 Control lock         Allows you to enable (unlocked) or disable (lock) the control to allow or
                      prevent users from entering information in the control. The status in the
                      button can be one of the following values:

                      - Unlocked. Users are able to interact with the control in the UDI Wizard.

                      - Locked. Users are unable to interact with the control in the UDI Wizard.

                      If you disable a control, you must provide the information collected by the
                      control either as a default value in the control or in the CustomSettings.ini
                      file or in MDT DB.

 Default value        The value that is displayed in the control by default. If the control is
                      enabled, then the user can override the default value.

 Associated task      The task sequence variable name associated with the control. The UDI
 sequence variable    Wizard sets the specified task sequence variable with the value provided in
 name                 the UDI Wizard.

 Friendly name        The name which appears on the Summary wizard page (if included) and
                      shows the configuration setting collected by this control.

 Validators           A list of validation checks performed on the information entered in the
                      control. You can add or remove validation checks to this list.

For more information about configuring specific controls on specific wizard pages, see
the corresponding section for that wizard page in the MDT document Toolkit Reference.

Create a New UDI Wizard Configuration File
The UDI Wizard displays wizard pages based on the configuration options specified in
the UDIWizard_Config.xml file in the Scripts folder of the MDT files package specified in
the task sequence. Create a new UDI Wizard configuration file using the UDI Wizard
Designer.

   Tip

<!-- p.359 -->

  Create a new MDT files package and corresponding package source for each
  unique configuration of the UDIWizard_Config.xml file.

To create a new UDI Wizard configuration file using the UDI Wizard
Designer

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select UDI Wizard Designer.

     The UDI Wizard Designer starts.

   2. In the UDI Wizard Designer console, on the Ribbon, in the File Menu group, select
     New.

   3. Make the appropriate changes in the UDI Wizard Designer console.

   4. In the UDI Wizard Designer console, on the Ribbon, in the File Menugroup, select
     Save As.

     The Save As dialog box opens.

   5. In the Save As dialog box, go to folder_path (where folder_path is the fully
     qualified path to the Scripts folder in the MDT files package source), in File name,
     type file_name (where file_name is the file name for the configuration file), and
     then select Save.

     After creating the new UDI Wizard configuration file, create a new task sequence or
     modify an existing task sequence steps to use the appropriate MDT files package.
     You also need to update the distribution points with the modified MDT files
     package as described in Managing Distribution Points in Configuration Manager,
     which is the same process for UDI and ZTI deployments.

Open an Existing UDI Wizard Configuration File
The UDI Wizard displays pages based on the configuration options specified in the
UDIWizard_Config.xml file in the Scripts folder of the MDT files package specified in the
task sequence. Open an existing UDI Wizard configuration file using the UDI Wizard
Designer.

To open an existing UDI Wizard configuration file using the UDI
Wizard Designer

<!-- p.360 -->

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select UDI Wizard Designer.

     The UDI Wizard Designer starts.

   2. In the UDI Wizard Designer console, on the Ribbon, in the File Menu group, select
     Open.

   3. In the Open dialog box, go to folder_path (where folder_path is the fully qualified
     path to the Scripts folder in the MDT files package source), select file_name (where
     file_name is the file name for the configuration file), and then select Open.

Save UDI Wizard Configuration Updates
After you have updated the UDI Wizard configuration, you need to save the changes to
the UDI wizard configuration file. Save the UDI Wizard configuration file in the Scripts
folder of the MDT files package specified in the task sequence.

To save the UDI Wizard configuration updates using the UDI Wizard
Designer

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select UDI Wizard Designer.

     The UDI Wizard Designer starts.

   2. In the UDI Wizard Designer console, on the Ribbon, in the File Menu group, select
     Open.

   3. In the Open dialog box, go to folder_path (where folder_path is the fully qualified
     path to the Scripts folder in the MDT files package source), select file_name (where
     file_name is the file name for the configuration file), and then select Open.

   4. Make the appropriate changes in the UDI Wizard Designer console.

   5. In the UDI Wizard Designer console, on the Ribbon, in the File Menu group, select
     Save.

     The File Save dialog box opens, notifying you that the file Save operation is
     complete.

   6. In the File Save dialog box, select OK.

Override the Configuration File That the UDI Wizard Uses
