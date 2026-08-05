---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1441-1480"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1441-1480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1441-1480
family: sccm
documentKind: "doc"
abstract: "When you have completed reviewing these tables, select Start Windows to log on to Windows 7 for the first time. ７ Note Configuration Manager applications are not displayed on the Applications Installed tab. The Configuration Manager applications are detected after the user logs"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1441-1480

<!-- p.1441 -->

     When you have completed reviewing these tables, select Start Windows to log on
     to Windows 7 for the first time.

        ７ Note

        Configuration Manager applications are not displayed on the Applications
        Installed tab. The Configuration Manager applications are detected after the
        user logs on to the target computer the first time.

   5. The Windows logon screen is displayed, and the logon process continues normally.

     AppInstall.exe is run the first time a user logs on to the target computer. For more
     information on this process, see User-Centric App Installer Reference.

User-Centric App Installer Reference
The User-Centric App Installer feature in UDI is used to report any applications installed
during the UDI deployment process to the Application Catalog feature in Configuration
Manager. The User-Centric App Installer feature provides the link between the
applications selected on the ApplicatonPage wizard page in the UDI Wizard and any
optional Configuration Manager applications advertised to the users.

For more information on the Application Catalog feature in Configuration Manager, see
Application Management in Configuration Manager.

The following is the high-level process for how the App Install feature works in UDI:

   1. Configuration Manager applications are created in Configuration Manager.

     For more information about creating and managing Configuration Manager
     applications, see the following resources:

           How to Create Applications in Configuration Manager

           Operations and Maintenance for Application Management in Configuration
           Manager

   2. The Configuration Manager user collections are created, and users are added to
     the collection.

     For more information about creating and managing user collections and adding
     users to collections, see the following resources:

           Collections in Configuration Manager

<!-- p.1442 -->

       How to Create Collections in Configuration Manager

3. The Configuration Manager applications are deployed to the user collections.

  For more information about how to deploy the applications to user collections, see
  How to Deploy Applications in Configuration Manager.

4. The Configuration Manager applications are made available on the
  ApplicatonPage wizard page using the UDI Wizard Designer.

  For more information about how to make Configuration Manager applications
  available on the ApplicatonPage wizard page, see the section, "Step 5-11:
  Customize the UDI Wizard Configuration File for the Target Computer", in the MDT
  document Quick Start Guide for User-Driven Installation.

5. UDA is configured using one of the following methods:

       In the Configuration Manger console (For more information about
       configuring UDA in the Configuration Manager console, see How to Manage
       User Device Affinity in Configuration Manager.)

       On the UDAPage wizard page in the UDI Wizard. For more information about
       the UDAPage wizard page, see UDAPage.

       After UDA is configured, the specified user account will be the primary user
       for the target computer.

    ７ Note

    UDA can only be configured by UDI in the New Computer deployment
    scenario. It cannot be configured in the Refresh Computer or Replace
    Computer deployment scenarios.

6. The task sequence is run, and the user selects the Configuration Manager
  applications on the ApplicatonPage wizard page in the UDI Wizard.

  The UDI Wizard is run in the UDI Wizard task sequence step in the Preinstall group
  of the task sequence. When the user selects Configuration Manager applications
  on the ApplicatonPage wizard page, the wizard page creates a separate task
  sequence variable for each application selected.

  For more information on selecting the Configuration Manager applications on the
  ApplicatonPage wizard page in the UDI Wizard, see the section, "Step 6-4: Start

<!-- p.1443 -->

   the Target Computer with the Task Sequence Bootable Media", in the MDT
   document Quick Start Guide for User-Driven Installation.

 7. The task sequence installs the Configuration Manager applications that were
   selected in the previous step.

   The Configuration Manager applications are installed using the following task
   sequence steps in the Install Applications group in the task sequence:

         Convert list to two digits

         Install Application

 8. The task sequence performs the following tasks in the OSD Results and Branding
   group prior to starting the target operating system for the first time:

         Copies the information used for OSDResults.exe to the %WINDIR%\UDI
         folder on the target computer in the Cache OSD Results task sequence step

         Records the task sequence variables created in step 6 for the Configuration
         Manager applications in the registry on the target computer in the Branding
         to Reg and Branding to Reg x64 task sequence steps

         The tasks sequence variables are saved in the following location in the
         registry:

         HKEY_LOCAL_MACHINE\Software\Microsoft\MPSD\OSD

         Configures the target operating system to automatically run OSDResults.exe
         when the computer starts prior to the Windows logon screen in the Run OSD
         Results task sequence step

         Configures the target operating system to automatically run AppInstall.exe
         when a user logs on to the computer for the first time in the Run OSD
         Results task sequence step

         Configures a task on the target operating system to remove the
         %WINDIR%\UDI folder one month from the date of the deployment

 9. The target computer is started, and OSDResults.exe is run.

   For more information about OSDResults.exe, see OSDResults Reference.

10. A user logs on to the target computer, and AppInstall.exe starts automatically.

11. AppInstall checks whether the currently logged-on user is a primary user who was
   configured in UDA.

<!-- p.1444 -->

    A primary user is a user who uses the device on a regular basis and is considered
    the owner, or one of the owners, of the device.

    If the currently logged-on user is:

            Not a primary user, then AppInstall.exe stops

            A primary user, then AppInstall.exe reads the registry entries saved in step 8
            to determine which applications were installed

 12. AppIntaller connects to Configuration Manager and reads the Application Catalog
    using the following steps:

     a. AppInstall will wait 5 minutes after it starts to allow the Configuration Manager
          policies to be available.

    b. After 5 minutes, AppInstall attempts to connect to the Application Catalog.

     c. If AppInstall is unable to connect, then it will wait for a period of time before
          attempting to connect again.

    d. AppInstall attempts to connect up to five times before exiting.

          You can configure the connection time-out delay and the number of retries for
          AppInstall using the AppInstall.exe.config file, which resides in the
          Tools\OSDResults folder in the MDT files Configuration Manager package. Table
          11 lists the configuration settings in the AppInstall.exe.config file.

Table 11. Configuration Settings in the
AppInstall.exe.config File
                                                                                     ﾉ    Expand table

Setting             Description

timeoutMinutes      This setting allows you to specify the length of time for AppInstall to wait for a
                    response from the Configuration Manager Application Catalog before timing
                    out. The value is specified in minutes. The default value for this setting is 5.

delayTimer          This setting allows you to specify the length of time for AppInstall to wait prior
                    to attempting the connection to the Configuration Manager Application
                    Catalog. The value is specified in minutes. The default value for this setting is 5.

  1. AppInstall compares the list of applications discovered in the registry with the list
    of applications available from the Configuration Manger Application Catalog for

<!-- p.1445 -->

     the user currently logged on.

     If the application discovered in the registry:

          Is available in the Application Catalog, then AppInstall.exe maps the
          applications and identifies the applications as existing both in the registry
          and in the Application Catalog. These applications will be used in the
          following step.

          Is not available in the Application Catalog, then AppInstall.exe does not
          create a mapping. These applications will not be used in the following step.

   2. AppInstall uses Configuration Manager APIs to initiate the installation of the
     mapped applications.

     The applications used in this step were mapped in the previous step. That is to say,
     they were both listed in the registry and found in the Application Catalog.

   3. As a part of the installation process, Configuration Manager detects whether the
     application is already installed.

     Because the application has already been installed, Configuration Manager records
     that the application has been successfully deployed to that user, and the
     application will be listed in Software Center for that user. Configuration Manager
     begins management and monitoring of the application for that user.

   4. After 1 month, the task created on the target computer in step 8 runs and removes
     the %WINDIR%\UDI folder.

     The folder is retained for 1 month so that the primary users have an opportunity to
     be log on and run AppInstall.exe.

UDI Stage Reference
The MDT deployment scenarios use one or more UDI stage. Each UDI stage used in the
MDT deployment scenarios is discussed in a subsequent section in the context of the
MDT deployment scenario. In some MDT deployment scenarios, only one stage is used.
In other MDT deployment scenarios, multiple stages are used within the scenario. For
more information on the MDT deployment scenarios, see the section, "Identifying
Deployment Scenarios", in the MDT document Using the Microsoft Deployment Toolkit.

Table 12 lists the MDT deployment scenarios and provides a brief description of each,
how each scenario is selected, and which UDI stages are used in each deployment
scenario. MDT automatically determines which MDT deployment scenario to use based

<!-- p.1446 -->

on the MDT task sequence template you use to create your task sequence and on how
the task sequence is initiated.

Each UDI stage used in the MDT deployment scenarios is discussed in a subsequent
section in the context of the MDT deployment scenario. In some MDT deployment
scenarios, only one stage is used. In other MDT deployment scenarios, multiple stages
are used within the scenario. For more information on the MDT deployment scenarios,
see the section, "Identifying Deployment Scenarios", in the MDT document Using the
Microsoft Deployment Toolkit.

Table 12. MDT Deployment Scenarios and UDI
Stages
                                                                                ﾉ   Expand table

 Scenario     Description

 New          MDT for UDI automatically selects this scenario when you:
 Computer
              - Create the advertised task sequence using the User-Driven Installation Task
              Sequence task sequence template

              - Start the task sequence in Windows PE using PXE boot, task sequence boot media,
              or prestaged media for the NEWCOMPUTER.Prestaged stage

              This scenario can be used with traditional deployments or with prestaged media
              deployments as supported in Configuration Manager. Run the UDI Wizard with the
              following UDI stages to support each type of deployment:

              - NEWCOMPUTER stage. The UDI Wizard is run with this stage in the User-Driven
              Installation Task Sequence task sequence when the operating system image is
              stored on distribution points. For more information, see NEWCOMPUTER Stage.

              - NEWCOMPUTER.Prestage stage. The UDI Wizard is run with this stage in the
              User-Driven Installation Task Sequence task sequence when the operating system
              image is stored on a local disk on the target computer (prestaged). For more
              information, see NEWCOMPUTER.Prestaged Stage.

 Refresh      MDT for UDI automatically selects this scenario when you:
 Computer
              - Create the advertised task sequence using the User-Driven Installation Task
              Sequence task sequence template

              - Start the task sequence in the existing Windows operating system on the target
              computer (not in Windows PE)

<!-- p.1447 -->

Scenario   Description

           - The UDI Wizard is run with the REFRESH stage to support this deployment
           scenario. For more information, see REFRESH Stage.

Replace    This scenario includes an existing computer and a replacement computer. A
Computer   separate task sequence is created and run on each computer as described in the
           following process:

           - On the existing computer. MDT for UDI automatically selects this portion of the
           scenario when you:

           - Create the advertised task sequence using the User-Driven Installation Replace
           Task Sequence task sequence template

           Start the task sequence in the existing Windows operating system on the target
           computer (not in Windows PE)

           The UDI Wizard is run with the following UDI stages to support this deployment
           scenario:

           - REPLACE stage. This stage is run in the existing Windows operating system and
           captures configuration information from within Windows.

           - REPLACE.WinPE stage. This stage is run in Windows PE and completes the
           capturing of configuration information from the existing computer—for example,
           running USMT and capturing the user state migration data.

           The user state is captured to a network shared folder or to a local USB drive.

           For more information on the REPLACE and REPLACE.WinPE stages, see REPLACE
           and REPLACE.WinPE Stages.

           - On the replacement computer. This portion of the scenario is identical to the New
           Computer scenario, except that the user state captured in the previous step is
           restored. MDT for UDI automatically selects this portion of the scenario when you:

           - Create the advertised task sequence using the User-Driven Installation Task
           Sequence task sequence template

           - Start the task sequence in Windows PE using PXE boot, task sequence boot media,
           or prestaged media for the NEWCOMPUTER.Prestaged stage.

           This portion of the scenario can be used with traditional deployments or with
           prestaged media deployments as supported in Configuration Manager. As a part of
           this portion of the scenario, the user state migration data is restored. The UDI
           Wizard is run with the following UDI stages to support each type of deployment:

           - NEWCOMPUTER stage. The UDI Wizard is run with this stage in the User-Driven
           Installation Task Sequence task sequence when the operating system image is

<!-- p.1448 -->

 Scenario    Description

             stored on distribution points. For more information, see NEWCOMPUTER Stage.

             - NEWCOMPUTER.Prestage stage. The UDI Wizard is run with this stage in the
             User-Driven Installation Task Sequence task sequence when the operating system
             image is stored on a local disk on the target computer (prestaged). For more
             information, see NEWCOMPUTER.Prestaged Stage.

NEWCOMPUTER Stage
Figure 1 illustrates the use of the NEWCOMPUTER stage in a task sequence created
using the User-Driven Installation Task Sequence task sequence template. The primary
difference between the task sequences calling the NEWCOMPUTER stage and the
NEWCOMPUTER.Prestaged stage is that the task sequence calling the
NEWCOMPUTER.Prestaged stage does not run the Apply Operating System Image task
sequence step, because the operating system image is already located on the target
computer.

<!-- p.1449 -->

Figure SEQ Figure \* ARABIC 1. Process flow for the NEWCOMPUTER stage

NEWCOMPUTER.Prestaged Stage

Figure 2 illustrates the high-level process flow for the NEWCOMPUTER.Prestaged stage
in a task sequence created using the User-Driven Installation Task Sequence task

<!-- p.1450 -->

sequence template. The primary difference between the task sequences calling the
NEWCOMPUTER stage and the NEWCOMPUTER.Prestaged stage is that the task
sequence calling the NEWCOMPUTER.Prestaged stage does not run the Apply
Operating System Image task sequence step, because the operating system image is
already located on the target computer.

Figure 2. Process flow for the NEWCOMPUTER.Prestaged stage

REFRESH Stage

<!-- p.1451 -->

Figure 3 illustrates the high-level process flow for the REFRESH stage in a task sequence
created using the User-Driven Installation Task Sequence task sequence template.

Figure SEQ Figure \* ARABIC 3. Process flow for the REFRESH stage

<!-- p.1452 -->

REPLACE and REPLACE.WinPE Stages
Figure 4 illustrates the high-level process flow for the REPLACE and REPLACE.WinPE
stages in a task sequence created using the User-Driven Installation Replace Task
Sequence task sequence template.

Figure 4. Process flow for the REPLACE and REPLACE.WinPE stages

UDI Task Reference
UDI tasks are software that is run on a wizard page that perform specific functions. In
some instances, these tasks are used to verify that the target computer is ready for

<!-- p.1453 -->

deployment. Other tasks can be used to perform deployment steps, such as copying
configuration or result files.

  ７ Note

  The Next button on the wizard page where the tasks are run will be disabled if any
  of the tasks finish with warning or error completion status.

This reference includes:

     An overview of UDI tasks, as described in UDI Task Overview

     A description of the configuration settings for UDI tasks, as described in UDI Task
     Configuration Settings

     A description of the built-in UDI validators that are provided with MDT, as
     described in Built-in UDI Tasks

UDI Task Overview
UDI tasks allow you to run software on the target computer that helps with the
deployment process. UDI includes several built-in tasks that help you perform common
tasks, such as ensuring that the target computer is not running on a battery and is
connected to a wired network connection.

In addition to the built-in UDI tasks, you can create custom UDI tasks using the UDI
software development kit (SDK). For more information about creating custom UDI tasks
using the UDI SDK, see User-Driven Installation Developers Guide.

UDI Task Configuration Settings
You manage tasks using the UDI Wizard Designer. You can add tasks, remove tasks, and
edit the configuration of a task in the UDI Wizard Designer. The configuration settings
for a task are stored in the UDI Wizard configuration file and are read by the UDI Wizard
when the wizard page that contains the task is displayed.

UTI tasks have some configuration settings that are common to all UDI tasks, as listed in
Table 13. For the configuration settings that are specific to each UDI task, see the
corresponding section in Built-in UDI Tasks.

<!-- p.1454 -->

Table 13. Configuration Settings Common to All
UDI Tasks
                                                                                         ﾉ   Expand table

 Task              Description

 Bitmap            This parameter specifies the graphic used to indicate the task type.
 Filename

 Display           This specifies the name of the task, which is displayed on the wizard page when
 Name              the task is run.

 Exit Code         This specifies a list of possible return codes for the task. An item exists in the list
 Values            for each possible return code.

 Error Code        This specifies a list of possible unexpected exceptions that may be encountered
 Values            (thrown) by the task. An item exists in the list for each possible exception.

Built-in UDI Tasks
Table 14 lists the built-in UDI tasks. Each built-in UDI task is discussed in a subsequent
section.

Table 14. Built-in UDI Tasks
                                                                                         ﾉ   Expand table

 Task                         Description

 AC Power Check               This UDI task is used to identify whether the target computer is
                              connected to AC power, not solely on battery.

 Application Discovery        This UDI task is used to discover applications that are installed on the
                              target computer.

 CheckSMSFolderOnUSB          This UDI task is used to determine whether the _SMSTaskSequence
                              folder is located on a USB drive on the target computer.

 Copy Files Task              This UDI task is used to copy files while the UDI Wizard is running on
                              the target computer.

 Shell Execute Task           This UDI task is used to run software that can be initiated from a
                              command line.

<!-- p.1455 -->

 Task                     Description

 Wired Network Check      This UDI task is used to identify whether the target computer is
                          connected to a wired network, not connected using a wireless network
                          connection.

AC Power Check
Use this UDI task to identify whether the target computer is connected to AC power.
This task uses only those parameters common to all UDI tasks. For more information
about these parameters, see UDI Task Configuration Settings.

Table 15 lists the error and exit codes that the AC Power Check task generates.

Table 15. Error and Exit Codes for the AC Power
Check Task
                                                                               ﾉ   Expand table

 Exit or error    Value   Status
 code

 Exit             0       Success, which indicates that the target computer is plugged into AC
                          power

 Exit             \*      Error, which indicates that the target computer is not plugged into AC
                          power

Application Discovery

Use this UDI task to discover applications that are installed on the target computer.

Table 16 lists the parameters that the Application Discovery task uses.

Table 16. Parameters Used by the Application
Discovery Task
                                                                               ﾉ   Expand table

<!-- p.1456 -->

 Task        Description

 Readcfg     This parameter specifies the fully qualified or relative path to the location of the .app
             file that has a list of applications for the task to discover. The .app file contains the list
             of available software items from which the user can select.

             The Application Discovery task reads the .app file and determines whether any of
             these software items is installed. If a software item is installed, the item is added to the
             file specified in the Writecfg parameter.

             Ensure that this parameter uses the same location and file name as the
             ApplicationPage wizard page.

 Writecfg    This parameter specifies the fully qualified or relative path to the location of the .xml
             file that contains a list of the applications discovered by the task.

 Log         This parameter specifies the fully qualified or relative path to the location of the log
             file generated by this task. The file name of the log file is AppDiscovery.log.

In addition to the parameters in Table 16, this task uses the parameters common to all
UDI tasks. For more information about these common parameters, see UDI Task
Configuration Settings.

Table 17 lists the error and exit codes that the Application Discovery task generates.

Table 17. Error and Exit Codes for the
Application Discovery Task
                                                                                        ﾉ    Expand table

 Exit or error   Value        Status and description
 code

 Exit            0            Success, which indicates that the task successfully scanned for
                              applications

 Exit            \*           Warning, which indicates that the application discovery engine could
                              not be run for some unknown reason

 Exit            1            Warning, which indicates that the application discovery engine
                              encountered one or more warnings

 Exit            16777216     Warning, which indicates that critical problems were encountered
                              while initializing the application discovery engine

 Exit            33554432     Warning, which indicates that critical problems were encountered
                              while processing the application master list

<!-- p.1457 -->

CheckSMSFolderOnUSB
Use this UDI task to identify whether the _SMSTaskSequence folder is located on a USB
drive on the target computer. By default, the Configuration Manager task sequencer
places the _SMSTaskSequence folder on the drive with the most available free disk
space. This can cause problems later in the deployment process if the USB drive is
removed.

This task checks to see whether the folder is located on a USB drive and prevents the
deployment from proceeding if it is. This task uses only those parameters common to all
UDI tasks. For more information about these parameters, see UDI Task Configuration
Settings.

If the _SMSTaskSequence folder is located on a USB drive, this task fails and prevents the
deployment from continuing. To resolve this issue and perform the deployment,
complete the following steps:

   1. Disconnect the USB drive from the target computer before starting the task
        sequence.

   2. Start the task sequence.

   3. Wait until the UDI Wizard starts.

   4. Connect the USB drive.

   5. Complete the UDI Wizard.

        Table 18 lists the error and exit codes that the CheckSMSFolderOnUSB task
        generates.

Table 18. Error and Exit Codes for the
CheckSMSFolderOnUSB Task
                                                                                 ﾉ   Expand table

 Exit or        Value   Status
 error code

 Exit           0       Success, which indicates that the _SMSTaskSequence folder is not located
                        on a USB drive and the deployment can continue.

 Exit           \*      Error, which indicates that the _SMSTaskSequence folder is located on a
                        USB drive and the deployment cannot continue.

<!-- p.1458 -->

Copy Files Task
Use this UDI task to copy files while the UDI Wizard is running on the target computer.

Table 19 lists the parameters that the Copy Files task uses.

Table 19. Parameters Used by the Copy Files
Task
                                                                                     ﾉ   Expand table

 Task          Description

 Source        This parameter specifies the fully qualified or relative path to the source file, which
               can contain wildcards to copy multiple files using a single task.

 Destination   This parameter specifies the fully qualified or relative path to the destination file
               without a file name.

In addition to the parameters in Table 19, this task uses parameters common to all UDI
tasks. For more information about these parameters, see UDI Task Configuration
Settings.

Table 20 lists the error and exit codes that the Copy Files task generates.

Table 20. Error and Exit Codes for the Copy
Files Task
                                                                                     ﾉ   Expand table

 Exit or error code      Value     Status and description

 Exit                    0         Success, which indicates that the copy process succeed

 Exit                    \*        Error, which indicates that the copy process failed

 Error                   -1        Error, which indicates that the copy process failed

Shell Execute Task

Use this UDI task to run software that can be initiated from a command line.

Table 21 lists the parameters that the Shell Execute task uses.

<!-- p.1459 -->

Table 21. Parameters Used by the Shell Execute
Task
                                                                                    ﾉ   Expand table

 Task            Description

 Filename        This parameter specifies the fully qualified or relative path to the command for the
                 task to run.

 Parameters      This parameter specifies the command-line parameters that are to be provided
                 when running the command.

In addition to the parameters in Table 21, this task uses parameters common to all UDI
tasks. For more information about these parameters, see UDI Task Configuration
Settings.

You can also run custom Visual Basic scripts designed to run in cscript.exe using the
Shell Execute task. To run Visual Basic scripts, perform the following steps:

   1. Type the following text in the Filename parameter:

          Windows Command Prompt

          %windir%\system32\cscript.exe

   2. Type name of the Visual Basic script file (.vbs file) in the Parameters parameter,
        including any command-line parameters for the script.

        For example, to run a Visual Basic script named SelfTest.vbs with a parameter value
        of Debug, type the following (where script_path is the fully qualified path to the
        SelfTest.vbs file):

          Windows Command Prompt

          <script_path>\SelfTest.vbs Debug

        Table 22 lists the common error and exit codes that the Shell Execute task
        generates.

  ７ Note

<!-- p.1460 -->

  Each specific task based on the Shell Execute task has a unique set of error and exit
  codes. Please check the return codes for the software you are running using this
  task.

Table 22. Common Error and Exit Codes for the
Shell Execute Task
                                                                                      ﾉ   Expand table

 Exit or error code        Value     Status and description

 Exit                      0         Success, which indicates that the task finished successfully

 Exit                      \*        Error, which indicates that the task failed

Wired Network Check

Use this UDI task to determine whether the target computer is connected to a wired
network, not using a wireless network connection. This task only uses parameters
common to all UDI tasks. For more information about these parameters, see UDI Task
Configuration Settings.

Table 23 lists the common error and exit codes that the Wired Network Check task
generates.

Table 23. Error and Exit Codes for the Wired
Network Check Task
                                                                                      ﾉ   Expand table

 Exit or error        Value     Status and description
 code

 Exit                 0         Success, which indicates that the target computer is connected to a
                                wired network

 Exit                 \*        Error, which indicates that the target computer is not connected to a
                                wired network

UDI Validator Reference

<!-- p.1461 -->

UDI validators are used to validate values entered in text fields on wizard pages. When a
UDI validator detects an invalid entry, a message is displayed for the first error
encountered at the bottom of the wizard page. The next validation error message, if any,
is displayed after you resolve the first validation error. This process continues until all
validation errors are resolved. The Next button is disabled until all validation errors on
the wizard page are resolved.

This reference includes:

     An overview of UDI validators, as described in UDI Validator Overview

     A description of the built-in UDI validators provided with MDT, as described in
     Built-in UDI Validators

UDI Validator Overview
UDI validators are used to help ensure that users provide the correct information in the
text fields on wizard pages in the UDI Wizard. UDI includes several built-in validators
that help you perform typical validations of fields used for entering text, such as
preventing users from entering invalid characters or ensuring that the field is not empty.

In addition to the built-in UDI validators, you can create custom UDI validators using the
UDI SDK. For more information about creating custom UDI validators using the UDI SDK,
see the MDT document User-Driven Installation Developers Guide.

Built-in UDI Validators
Table 24 lists the built-in UDI validators. Each built-in validator is discussed in a
subsequent section. When a validator detects an invalid entry in a text box, a message is
displayed on the wizard page, and the Next button is disabled until all invalid entries are
resolved.

Table 24. Built-in UDI Validators
                                                                                   ﾉ   Expand table

 Validator       Description

 InvalidChars    This validator identifies any invalid characters that have been entered from a list
                 that you configure.

 NamedPattern    This validator helps ensure that the text follows a predefined pattern.

<!-- p.1462 -->

 Validator       Description

 NonEmpty        This validator is used to require text in a field.

 RegEx           This validator allows you ensure that the text matches a regular expression that
                 you specify as a part of the validator.

InvalidChars
This validator prevents users from entering specific characters. The Message box allows
you to enter a message that is displayed if the text field contains any of the invalid
characters. The Invalid Characters box allows you to enter the characters that are
considered invalid. The characters are entered without spaces between them.

NamedPattern
This validator helps ensure that the text follows a predefined pattern. The Message box
allows you to enter a message that is displayed if the text field does not match the
named pattern. The Named Pattern box allows you to enter the name of the predefined
pattern and must be Username, ComputerName, or Workgroup. The names are case
insensitive.

NonEmpty

Use this validator to require text in a field. The Message box allows you to enter a
message that is displayed if the text field is empty.

RegEx
This validator allows you ensure that the text matches a regular expression that you
specify as a part of the validator. The Message box allows you to enter a message that is
displayed if the text field does not match the regular expression. The Regular
Expression box allows you to enter the regular expression used for the validation. For
more information about how to build regular expressions for this validator, see TR1
Regular Expressions.

UDI Wizard Page Reference
You add a UDI wizard page to stages from the Page Library in the UDI Wizard Designer.
UDI wizard pages are displayed in the UDI Wizard.

<!-- p.1463 -->

This reference includes:

     An overview of UDI wizard pages, as described in UDI Wizard Page Overview

     A description of the built-in UDI wizard pages that are provided with MDT, as
     described in Built-in UDI Wizard Pages

UDI Wizard Page Overview
Wizard pages are displayed in the UDI Wizard and collect the information required to
complete the deployment process. You create wizard pages using C++ in Visual Studio.
The custom wizard pages are implemented as DLLs that the UDI Wizard reads.

Each built-in UDI wizard page has a corresponding UDI wizard page editor, which you
use to configure the wizard page in the UDI Wizard Designer.

In addition to the built-in UDI wizard pages, you can create custom UDI wizard pages
using the UDI SDK. For more information about creating custom UDI wizard pages using
the UDI SDK, see the MDT document User-Driven Installation Developers Guide.

Each wizard page can reference the following types of variables:

     Task sequence variables

     Memory variables

     Environment variables

     You can reference task sequence and environment variables by bracketing the
     variable using percent signs (%), such as %OSDImageIndex%. You can reference
     memory variables by bracketing the variable using dollar signs ($), such as
     $VolumeArchitecture$.

  ７ Note

  If a task sequence variable and an environment variable both have the same name,
  then the task sequence variable takes precedence over the environment variable.

Table 25 lists the memory variables that are set when the UDI Wizard starts, the
description of the variables, and whether the UDI Wizard reads or writes the variables
during startup.

<!-- p.1464 -->

Table 25. Memory Variables Set by the UDI
Wizard at Startup and Their Descriptions
                                                                                       ﾉ   Expand table

 Variable                                                                                  Read   Write

 LogPath                                                                                   No     Yes

 Specifies the fully qualified path to the log files for the UDI Wizard. You can set
 this variable to one of the following values:

 - The value in the _SMSTSLogPath task sequence variable

 - The value of the %TEMP% environment variable if the _SMSTSLogPath task
 sequence variable is not set

 WizardConfigFilename                                                                      No     Yes

 Specifies the name of the UDI Wizard configuration file currently in use. The
 ApplicationPage wizard page reads the value of this variable to find the
 corresponding .app file, which contains the list of applications. For example, if the
 UDI Wizard configuration file is named config.xml, then the wizard page will look
 for the corresponding .app file (config.xml.app).

Built-in UDI Wizard Pages
Table 26 lists the built-in UDI wizard pages. Each built-in UDI wizard page is discussed in
a subsequent section.

Table 26. Built-in Wizard Pages and Their
Descriptions
                                                                                       ﾉ   Expand table

 Wizard page        Description

 AdminAccounts      Use this wizard page to set the password for the local administrator account
                    and add other users to the local Administrators group on the target computer.

 ApplicationPage    Use this wizard page to configure the list of applications that can be installed
                    during the setup process. These applications can include applications or
                    packages and programs from Configuration Manager.

<!-- p.1465 -->

Wizard page      Description

BitLockerPage    Use this wizard page to configure BitLocker settings for the target computer.

ComputerPage     Use this wizard page to configure the computer name of the target computer,
                 the domain or workgroup to join, and the credential to be used when joining a
                 domain.

ConfigScanPage   Use this wizard page to run UDI tasks that scan the configuration of the target
                 computer to determine whether the target computer is ready for the
                 deployment of the operating system image. This readiness includes having
                 sufficient system resources and ensuring that any prerequisite software is
                 installed and configured properly.

LanguagePage     Use this wizard page to determine which language pack should be installed,
                 the default language for the target operating system, the keyboard locale, and
                 the time zone in which the computer will be physically located.

ProgressPage     Use this wizard page to run UDI tasks that capture the user state migration
                 data from the target computer.

RebootPage       Use this wizard page to notify the user that the target computer is going to be
                 restarted. You can configure the notification message using the UDI Wizard
                 Designer.

SummaryPage      Use this wizard page to notify the user about the configuration options that
                 were selected while running the UDI Wizard. The configuration information
                 displayed on this wizard page is automatically collected from other wizard
                 pages. Some fields on other wizard pages allow you to configure the caption
                 (label) displayed on this wizard page using the UDI Wizard Designer.

UDAPage          Use this wizard page to configure the UDA between the target computer and a
                 specified user. Defining affinity between a computer and a user allows
                 automatic installation of software that is deployed to a user. The UDA feature is
                 only available in Configuration Manager and in the UDI New Computer
                 scenario.

UserStatePage    Use this wizard page to configure the settings for capturing or restoring user
                 state migration data. This wizard page allows the user to select the location to
                 capture user state migration to or restore user state migration data from.

VolumePage       Use this wizard page to configure the settings for the disk volume on target
                 computer where the operating system will be deployed. These settings include
                 selecting the target operating system, selecting the target drive, selecting any
                 Windows installation, and determining whether the target drive should be
                 formatted as a part of the deployment process.

WelcomePage      Use this wizard page to provide information to the user about UDI Wizard and
                 the deployment process. You can configure the notification message using the
                 UDI Wizard Designer.

<!-- p.1466 -->

AdminAccounts
Use this wizard page to set the password for the local administrator account and to add
other user to the local Administrators group on the target computer.

Task Sequence Variables

Table 27 lists the AdminAccounts task sequence variables with the description and
determines whether the variable is read by the wizard page, written by the wizard page,
or can be configured in the UDI Wizard configuration file.

Table 27. AdminAccounts Task Sequence
Variables
                                                                                 ﾉ    Expand table

 Variable                                                                  Read      Write   Config

 OSDAddAdmin                                                               Yes       Yes     Yes

 Specifies a list of additional user names to be added to the local
 Administrators group on the target computer.

 OSDLocalAdminPassword                                                     Yes       Yes     Yes

 Specifies the passwords for the local built-in Administrator account on
 the target computer.

ApplicationPage

Use this wizard page to configure the list of application software that can be installed
during the setup process. These applications can include applications or packages and
programs from Configuration Manager.

  ７ Note

  If applications appear to be disabled, the application may require administrator
  approval but has not yet been approved. If the Require administrator approval if
  users request this application check box is selected for the application, verify that
  the application has been approved. For more information, see How to Deploy
  Applications in Configuration Manager.

<!-- p.1467 -->

Task Sequence Variables

Table 28 lists the ApplicationPage task sequence variables with the description and
whether the variable is read by the wizard page, written by the wizard page, or can be
configured in the UDI Wizard configuration file.

Table 28. ApplicationPage Task Sequence
Variables
                                                                                 ﾉ    Expand table

 Variable                                                                  Read      Write   Config

 ApplicationBaseVariable                                                   No        Yes     Yes

 Specifies the name used as the base for the task sequence variable
 names created for each Configuration Manager application selected on
 the ApplicationPage wizard page. This variable is configured using the
 Edit Software Settings button in the Edit Settings group on the Ribbon
 in the UDI Wizard Designer.

 A separate task sequence variable is created for each application
 selected on this page. The default value for this variable is
 APPLICATIONS. So, for example, the default names of the task sequence
 variables created for each application selected on this page will be
 APPLICATIONS001, APPLICATIONS002, APPLICATIONS003, and so forth.

 OSDApplicationList                                                        Yes       No      No

 Specifies the list of application identifiers that should be initially
 selected. The variable contains a list of numeric values separated by
 semicolons (;).

 The application identifiers are found in the Id attribute of the
 Application element in the UDI Wizard application configuration file
 (UDIWizard_Config.xml.app). There is a separate Application element for
 each application displayed in this wizard page.

 OSDArchitecture                                                           Yes       No      No

 Specifies the processor architecture of the target computer. The
 ApplicationPage wizard page uses this variable to filter the available
 applications when the VolumeArchitecture memory variable has not
 been set. However, if the VolumeArchitecture memory variable has been
 set, it always takes precedence over this task sequence variable for
 filtering the available applications.

<!-- p.1468 -->

 Variable                                                                        Read         Write   Config

 The value for this variable can be:

 - x86, which indicates a 32-bit processor architecture

 - amd64, which indicates a 64-bit processor architecture

 OSDBaseVariableName                                                             No           Yes     Yes

 Specifies the name used as the base for the task sequence variable
 names created for each Configuration Manager package and program
 selected on the ApplicationPage wizard page. This variable is configured
 using the Edit Software Settings button in the Page Behavior group on
 the Ribbon in the UDI Wizard Designer.

 A separate task sequence variable is created for each application
 selected on this page. The default value for this variable is PACKAGES.
 So, for example, the default names of the task sequence variables
 created for each application selected on this page will be PACKAGES001,
 PACKAGES002, PACKAGES003, and so forth.

Memory Variables
Table 29 lists the ApplicationPage memory variables with the description and whether
the variable is read or written by the wizard page.

Table 29. ApplicationPage Memory Variables
                                                                                          ﾉ    Expand table

 Variable                                                                                      Read    Write

 VolumeArchitecture                                                                            Yes     No

 Specifies the processor architecture of the target operating system image to be
 deployed (whether the image contains a 32-bit or 64-bit operating system). When
 this page is displayed, it checks to see if this variable has changed. If the variable
 has changed since the last time the wizard page was displayed, the wizard page
 filters the programs available for selection based on architecture of the target
 operating system. For example, if a 32-bit operating system is to be deployed,
 then the wizard page removes (filters) any 64-bit applications from the list of
 available applications on the wizard page.

 WizardConfigFilename                                                                          Yes     No

 Specifies the name of the UDI Wizard configuration file currently in use. If the

<!-- p.1469 -->

 Variable                                                                                 Read    Write

 value of the Link.Uri setter property is empty, the ApplicationPage wizard page
 reads the value of this variable to find the corresponding .app file, which contains
 the list of applications. For example, if the UDI Wizard configuration file is named
 config.xml, then the wizard page will look for the corresponding .app file
 (config.xml.app). This variable is set when the UDI Wizard starts.

 The Link.Uri setter property is set on the Software Settings dialog box, which can
 be opened using the Edit Software Settings button in the Page Behavior group
 on the Ribbon in the UDI Wizard Designer.

BitLockerPage
This wizard page is used to configure BitLocker settings for the target computer.

Task Sequence Variables

Table 30 lists the BitLockerPage task sequence variables with a description and whether
the variable is read by the wizard page, written by the wizard page, or can be configured
in the UDI Wizard configuration file.

Table 30. BitLockerPage Task Sequence
Variables
                                                                                     ﾉ    Expand table

 Variable                                                                      Read      Write   Config

 BDEInstallSuppress                                                            Yes       Yes     Yes

 Specifies whether BitLocker installation should be suppressed. If the
 variable is set to:

 - YES, then the Enable BitLocker check box is selected and the
 installation is performed

 - NO, then the Enable BitLocker check box is cleared and the installation
 is not performed

 BDEKeyLocation                                                                No        Yes     No

 Specifies the fully qualified path to the location where the BitLocker
 encryption keys are stored, which can be a local or UNC path. This
 variable is set to the value of the KeyLocation setter value in the UDI

<!-- p.1470 -->

Variable                                                                      Read   Write   Config

Wizard configuration file for the BitLockerPage. This variable is only
considered valid when the OSDBitLockerMode is set to TPMKEY or KEY.

BDEPin                                                                        Yes    Yes     Yes

Specifies the BitLocker PIN value if the Enable BitLocker using TPM and
Pin option is selected.

OSDBitLockerCreateRecoveryPassword                                            No     Yes     No

Specifies whether a BitLocker recovery password should be stored in AD
DS. If the variable is set to:

- AD, then the In Active Directory option is selected and the recovery
keys will be stored in AD DS (recommended)

- NONE, then the Do not create a recovery key option is selected and
the recovery keys will not be stored in AD DS (not recommended)

OSDBitLockerMode                                                              No     Yes     No

Specifies the mode to be used when enabling BitLocker on the target
computer. Valid values include:

- TPM. This value indicates that the Enable BitLocker using TPM only
option is selected and that only TPM will be used when enabling
BitLocker on the target computer.

- TPMPIN. This value indicates that the Enable BitLocker using TPM and
Pin option is selected and that TPM and a user-specified PIN will be
used when enabling BitLocker on the target computer.

- TPMKEY. This value indicates that the Enable BitLocker using TPM and
Startup Key option is selected and that TPM and a startup key will be
used when enabling BitLocker on the target computer.

- KEY. This value indicates that the Enable BitLocker using only an
External Startup Key option is selected and that only an external startup
key will be used when enabling BitLocker on the target computer.

OSDBitLockerStartupKeyDrive                                                   No     Yes     No

Specifies the drive letter where the BitLocker external startup key will be
stored on the target computer. This variable is only considered valid
when OSDBitLockerMode is set to TPMKEY or KEY.

OSDBitLockerWaitForEncryption                                                 Yes    Yes     Yes

Specifies whether the task sequence should wait until BitLocker

<!-- p.1471 -->

 Variable                                                                    Read      Write   Config

 encryption finishes. If the variable is set to:

 - YES, then the Wait for BitLocker Encryption to complete on all drives
 before continuing check box is selected and the task sequence will wait
 until the installation is complete

 - NO, then the Wait for BitLocker Encryption to complete on all drives
 before continuing check box is cleared and the task sequence will not
 wait until the installation is complete

Configuration Variables

Table 31 lists the BitLockerPage configuration variables with a description and whether
the variable is read by the wizard page, written by the wizard page, or can be configured
in the UDI Wizard configuration file.

Table 31. BitLockerPage Configuration Variables
                                                                                   ﾉ    Expand table

 Variable                                                                    Read      Write   Config

 KeyLocation                                                                 Yes       No      Yes

 Specifies the fully qualified path to the location where the BitLocker
 encryption keys are stored, which can be a local or UNC path. This
 configuration value is used to set the value of the BDEKeyLocation task
 sequence variable for the BitLockerPage. This variable is only considered
 valid when OSDBitLockerMode is set to TPMKEY or KEY.

ComputerPage

Use this wizard page to configure the computer name of the target computer, the
domain or workgroup to join, and the credentials to be used when joining a domain.
When you configure this page to join the target computer to a domain, this wizard page
will validate the credentials you provide for joining the domain in AD DS by default.
Then, this wizard page attempts to modify a computer object in AD DS to verify that the
user credentials provided on this page have permissions to create or modify the
computer object. You can disable either of these behaviors. If you disable the validation
of the credentials, then the verification of permissions for creating or modifying
computer objects is also disabled. Both of these validations occur when the Next button

<!-- p.1472 -->

is selected. If either of the validations encounters an error, an error message will be
displayed and this page will continue to be displayed.

The following is the order of precedence for determining the default computer name:

   1. If the UserExistingComputerName value in the UDI Wizard configuration file is set
     to TRUE, then the existing computer name is used (if present).

   2. If the OSDComputerName task sequence variable is set, then the computer name
     in that variable is used.

   3. If a default value is specified for the computer name in the UDI Wizard
     configuration file, then that value is used.

Task Sequence Variables

Table 32 lists the ComputerPage task sequence variables with a description and whether
the variable is read by the wizard page, written by the wizard page, or can be configured
in the UDI Wizard configuration file.

Table 32. ComputerPage Task Sequence
Variables
                                                                                   ﾉ    Expand table

 Variable                                                                    Read      Write   Config

 OSDComputerName                                                             Yes       Yes     Yes

 Specifies the name of the target computer. The value of this variable is
 set in the Computer name box.

 OSDDomainName                                                               Yes       Yes     Yes

 Specifies the name of the domain to which the target computer is to be
 joined. The value of this variable is set in the Domain box.

 OSDDomainOUName                                                             Yes       Yes     Yes

 Specifies the name of the OU within the domain to which the target
 computer object is to be placed. The value of this variable is set in the
 Organizational Unit box.

 OSDJoinAccount                                                              Yes       Yes     Yes

<!-- p.1473 -->

 Variable                                                                        Read   Write   Config

 Specifies the user account used to join the target computer to the
 domain. The value for this variable is set in the User name box.

 OSDJoinPassword                                                                 Yes    Yes     Yes

 Specifies the password for the user account used to join the target
 computer to the domain. The value for this variable is set in the
 Password and Confirm password boxes.

 OSDNetworkJoinType                                                              No     Yes     No

 Specifies if the target computer is to be joined to a workgroup or a
 domain. If the value is set to:

 - 0, then the Domain option is selected and the target computer will be
 joined to a domain

 - 1, then the Workgroup option is selected and the target computer will
 be joined to a workgroup

 SMSTSAssignUsersMode                                                            No     Yes     No

 Specifies the mode for configuring user affinity in Configuration
 Manager. Use this variable to configure the behavior of creating affinity
 between the target computer and user accounts in the SMSTSUdaUsers
 task sequence variable. If this variable is not specified prior to displaying
 this page, the value of this variable is set to Pending.

 Possible values for this variable include:

 - Auto. The affinity processing is automatically approved by
 Configuration Manager.

 - Pending. The affinity processing rules will require approval by a
 Configuration Manager administrator.

 - Disabled. No affinity processing will occur.

Configuration Variables

Table 33 lists the ComputerPage configuration variables with a description and whether
the variable is read by the wizard page, written by the wizard page, or can be configured
in the UDI Wizard configuration file.

<!-- p.1474 -->

Table 33. ComputerPage Configuration
Variables
                                                                                  ﾉ    Expand table

Variable                                                                    Read      Write   Config

ADComputerObjectCheck                                                       Yes       No      Yes

Specifies whether the ComputerPage wizard page will validate that the
credentials provided have the appropriate permissions to modify a
computer object in AD DS prior to continuing to the next wizard page.

Note:

This configuration setting is ignored if ADCredentialCheck is set to
FALSE.

If the value is set to:

- TRUE, then the Active Directory Computer Object Check check box is
selected in the wizard page editor in the Domain Join Credentials
section in the UDI Wizard Designer, and permissions to modify a
computer object for the credentials are validated

- FALSE, then the Active Directory Computer Object Check check box is
cleared in the wizard page editor in the Domain Join Credentials section
in the UDI Wizard Designer, and permissions to modify a computer
object for the credentials are not validated

ADCredentialCheck                                                           Yes       No      Yes

Specifies whether the ComputerPage wizard page will validate the
credentials provided for joining a domain prior to continuing to the next
wizard page. If the value is set to:

- TRUE, then the Active Directory Credential Check check box is
selected in the wizard page editor in the Domain Join Credentials
section in the UDI Wizard Designer, and credentials are validated

If this configuration setting is set to TRUE, then the credentials are
validated even if the credential fields are disabled (locked).

- FALSE, then the Active Directory Credential Check check box is cleared
in the wizard page editor in the Domain Join Credentials section in the
UDI Wizard Designer, and credentials are not validated

If this configuration setting is set to FALSE, then the

<!-- p.1475 -->

 Variable                                                                   Read   Write   Config

 ADComputerObjectCheck configuration setting is ignored and the
 validation that the provided credentials can modify a computer object in
 AD DS is not performed.

 UseExistingComputerName                                                    Yes    No      Yes

 Specifies whether the ComputerPage wizard page will use the existing
 computer name on the target computer as the default for the computer
 name.

 Note:

 This check box is only relevant for the Refresh Computer deployment
 scenario.

 If the value is set to:

 - TRUE, then the Use Existing Computer Name check box is selected in
 the wizard page editor in the Computer Name section in the UDI Wizard
 Designer, and the existing computer name will be used as the default
 computer name for the target computer after the new operating system
 is deployed

 - FALSE, then the Use Existing Computer Name check box is cleared in
 the wizard page editor in the Computer Name section in the UDI Wizard
 Designer, and the existing computer name will not be used as the
 default computer name for the target computer after the new operating
 system is deployed

ConfigScanPage
Use this wizard page to run UDI tasks that scan the configuration of the target computer
to determine whether the target computer is ready for the deployment of the operating
system image. This readiness includes having sufficient system resources and any
prerequisite software being installed and configured properly. In addition, other UDI
tasks are run that collect configuration information about the target computer, such as
identifying:

      Whether the computer is connected to power (as opposed to running on a battery)

      Whether the computer is connected to a wired network connection (as opposed to
      using a wireless network connection)

      Any installed applications

<!-- p.1476 -->

     Any installed printers

LanguagePage
Use this wizard page to determine which language packs should be installed, the default
language for the target operating system, the keyboard locale, and the time zone in
which the computer will be located.

Task Sequence Variables

Table 34 lists the LanguagePage task sequence variables with a description and whether
the variable is read by the wizard page, written by the wizard page, or can be configured
in the UDI Wizard configuration file.

Table 34. LanguagePage Task Sequence
Variables
                                                                                   ﾉ    Expand table

 Variable                                                                    Read      Write   Config

 InputLocale                                                                 Yes       Yes     Yes

 Specifies the input locale of the target operating system. You set the
 value of this variable in the Time and currency format box. If not
 specified, the input locale configured in the image is used.

 KeyboardLocale                                                              Yes       Yes     Yes

 Specifies the keyboard locale of the target operating system. Set the
 value of this variable in the Keyboard layout box. If not specified, the
 keyboard locale configured in the image is used.

 OSDTimeZone                                                                 Yes       Yes     Yes

 Specifies the time zone where the target computer will be physically
 located. Set the value of this variable in the Time zone box. If not
 specified, the time zone configured in the image is used.

 UILanguage                                                                  Yes       Yes     Yes

 Specifies the default language to be used for the target operating
 system. Set the value of this variable in the Language to install box. If
 not specified, the language configured in the image is used.

<!-- p.1477 -->

ProgressPage
Use this wizard page to run UDI tasks that capture the user state migration data from
the target computer. These tasks include:

     Copying the application discovery file to the location selected on the
     UserStatePage wizard page

     Copying the printer configuration file to the location selected on the
     UserStatePage wizard page

     Copying the list of installed products to the location selected on the UserStatePage
     wizard page

     Running the USMT and saving the user state migration data to the location
     selected on the UserStatePage wizard page

RebootPage

Use this wizard page to notify the user that the target computer is going to be restarted.
You can configure the notification message using the UDI Wizard Designer.

SummaryPage

Use this wizard page to notify the user about the configuration options that were
selected while running the UDI Wizard. The configuration information displayed on this
wizard page is automatically collected from other wizard pages. Some fields on other
wizard pages allow you to configure the caption (label) displayed on this wizard page
using the UDI Wizard Designer.

UDAPage
Use this wizard page to configure the UDA between the target computer and a specified
user. Assigning a user as the primary user of a computer allows automatic installation of
software that is deployed to that user. The UDA feature is only available in Configuration
Manager and only in the New Computer deployment scenario.

Task Sequence Variables

Table 35 lists the UDAPage task sequence variables with a description and whether the
variable is read by the wizard page, written by the wizard page, or can be configured in
the UDI Wizard configuration file.

<!-- p.1478 -->

Table 35. UDAPage Task Sequence Variables
                                                                                   ﾉ    Expand table

 Variable                                                                    Read      Write   Config

 SMSTSAssignUsersMode                                                        No        Yes     No

 Specifies the mode for configuring user affinity in Configuration
 Manager. Use this variable to configure the behavior of creating affinity
 between the target computer and user accounts in the SMSTSUdaUsers
 task sequence variable. To set this variable, select the Use User Device
 Affinity check box.

 If the variable is set to:

 - Auto, then the affinity processing is automatically approved by
 Configuration Manager

 - Pending, then the affinity processing rules will require approval by a
 Configuration Manager administrator (This is the value used when the
 Use User Device Affinity check box is selected.)

 - Disabled, then no affinity processing will occur

 SMSTSUdaUsers                                                               Yes       Yes     Yes

 Specifies the users to be associated with the target computer. The User
 Device Affinity Account sets this variable. This variable can have one or
 many users specified and is in the format Domain\User1, Domain\User2 .

UserStatePage
Use this wizard page to configure the settings for capturing or restoring user state
migration data. This wizard page is used for both user state migration data capture and
restore.

The UserStatePage can capture or restore user state migration data from a disk locally
attached to the target computer, a USB drive attached to the target computer, or a
network shared folder. In addition, you can select to not restore any user data. The code
logic behind the wizard page enables, disables, or automatically selects each of the
following options based on the deployment scenario and whether the disk is being
formatted:

      No Data to Restore. This option indicates that there is no user state migration data
      to restore and sets the OSDUserStateMode task sequence variable and

<!-- p.1479 -->

     UserStateMode variable to NoData.

     Local. This option indicates that the user state migration data should be stored on
     a disk locally attached to the target computer and sets the OSDUserStateMode
     task sequence variable and UserStateMode variable to Local.

     USB. This option indicates that the user state migration data should be stored on a
     USB disk locally attached to the target computer and sets the OSDUserStateMode
     task sequence variable and UserStateMode variable to USB.

     Network. This option indicates that the user state migration data should be stored
     on a network shared folder and sets the OSDUserStateMode task sequence
     variable and UserStateMode variable to Network.

NEWCOMPUTER Stage Behavior

The NEWCOMPUTER stage is used for computers on which no user state migration data
exists. The New Computer deployment scenario can be used as the second part of the
Replace Computer deployment scenario. If the user selects to:

     Format the disk on the target computer, then the UserStatePage assumes that no
     user state migration data is located on the local hard disk, so the Local option is
     disabled and all other options are enabled

     Not format the disk on the target computer, then the UserStatePage assumes that
     there is user state migration data to be restored, and all options are disabled other
     than the Local option (Using the Local option provides a faster method for
     restoring the user state migration data than the USB or network shared folder
     methods.)

     Table 36 lists the behavior of the options on the wizard page for the
     NEWCOMPUTER stage. The Format column indicates whether the target hard disk
     is to be formatted as a part of the deployment. The other columns indicate the
     configuration of the options when the UserStatePage is loaded.

Table 36. Behavior of Options for the
NEWCOMPUTER Stage
                                                                         ﾉ   Expand table

<!-- p.1480 -->

 Format            NoData            Local              USB               Network

 Yes               Enabled           Disabled           Enabled           Enabled

 No                Disabled          Selected           Disabled          Disabled

NewComputer.Prestaged Stage Behavior

The NEWCOMPUTER.Prestaged stage is based on the prestaged media feature in
Configuration Manager. Because the local hard disk is new, there is no user state
migration data to be restored from the local hard disk, so the Local option is disabled.
All other options are valid for this deployment scenario and are enabled. No default
option is selected.

Table 37 lists the behavior of the options on the wizard page for the
NewComputer.Prestaged stage. The Format column indicates whether the target hard
disk is to be formatted as a part of the deployment. The other columns indicate the
configuration of the options when the UserStatePage is loaded.

Table 37. Behavior of Options for the
NewComputer.Prestaged Stage
                                                                           ﾉ   Expand table

 Format            NoData            Local              USB               Network

 N/A               Enabled           Disabled           Enabled           Enabled

REFRESH Stage Behavior

The REFRESH stage is initiated in a full Windows operating system, instead of Windows
PE. If the user selects to:

       Format the disk on the target computer, then the UserStatePage assumes that no
       user state migration data is to be restored, and all options are disabled other than
       the NoData option

       Not format the disk on the target computer, then the UserStatePage assumes that
       there is user state migration data to be restored, and all options are disabled other
       than the Local option (Using the Local option provides a faster method for
       restoring the user state migration data than the USB or network shared folder
       methods.)
