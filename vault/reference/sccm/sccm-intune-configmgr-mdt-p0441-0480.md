---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 441-480"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0441-0480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0441-0480
family: sccm
documentKind: "doc"
abstract: "An Orchestrator runbook is the sequence of activities that orchestrate actions on computers and networks. You can initiate Orchestrator runbooks in MDT using the Execute Runbook task sequence step type. ７ Note The Execute Runbook task sequence step is not included any MDT task s"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 441-480

<!-- p.441 -->

    An Orchestrator runbook is the sequence of activities that orchestrate actions on
    computers and networks. You can initiate Orchestrator runbooks in MDT using the
    Execute Runbook task sequence step type.

 ７ Note

 The Execute Runbook task sequence step is not included any MDT task sequence
 templates. You must add the Execute Runbook task sequence step to any task
 sequences you create.

To configure the Execute Runbook task sequence step type to run
Orchestrator runbooks

  1. Edit task_sequence_name (where task_sequence_name is the name of the task
    sequence to which you want to add the task sequence step) for:

           LTI as described in Configure the Task Sequence Properties Task Sequence
           Tab

           ZTI using Configuration Manager as described in Configuring ZTI Task
           Sequence Steps in Configuration Manager

  2. Add a new task sequence step based on the Execute Runbook task sequence type
    for:

    a. LTI on the Task Sequence tab (In the task sequence hierarchy, select Add, select
       General, and then select Execute Runbook.)

    b. ZTI in the task sequence hierarchy (Select Add, point to MDT, and then select
       Execute Runbook.)

  3. On the Properties tab, configure the settings listed in Table 171 based on the
    requirements of your organization, and then select OK.

    Table 171. Configuration Settings on the Properties
    Tab of the Execute Runbook Task Sequence Step Type

                                                                        ﾉ   Expand table

     Setting          Description

     Name             Type a name for the task.

<!-- p.442 -->

Setting        Description

Description    Type a description of the task—for example, runbook_name (where
               runbook_name is the name of the Orchestrator runbook that this task
               sequence step will run).

Orchestrator   Type the URL for the Orchestrator web service, which includes the server
Server         name. The Orchestrator web service can use either Hypertext Transfer
               Protocol (HTTP) or HTTP over Secure Sockets Layer (HTTPS). The
               Orchestrator web service defaults to port 81.

               The Orchestrator web service supports multiple runbook servers. By
               default, a runbook can run on any runbook server. A runbook can be
               configured to specify which runbook servers should be used to run the
               runbook.

               The Orchestrator web service supports the ability to run a runbook on a
               specific runbook server. This feature is not supported in MDT.

               Specify the URL in any of the following formats:

               - servername. When using this format, the URL defaults to:

               https://<servername>:81/Orchestrator2012/Orchestrator.svc

               - servername:port. When using this format, the URL defaults to:

               https://<servername:port>/Orchestrator2012/Orchestrator.svc.

               - https://servername:port. When using this format, the URL defaults to:

               https://<servername:port>/Orchestrator2012/Orchestrator.svc.

               - https://servername:port. When using this format, the URL defaults to:

               https://<servername:port>/Orchestrator2012/Orchestrator.svc.

               - https://servername:port/Orchestrator2012/Orchestrator.svc. When
               using this format, MDT assumes that you are providing the fully qualified
               URL, because the value ends with .svc.

               - https://servername:port/Orchestrator2012/Orchestrator.svc. When
               using this format, MDT assumes that you are providing the fully qualified
               URL, because the value ends with .svc.

Runbook        Select Browse, and then select the name of the Orchestrator runbook that
               this task sequence should run.

               To successfully browse for Orchestrator runbooks, install the ADO.NET

<!-- p.443 -->

Setting         Description

                Data Services Update for .NET Framework 3.5 SP1 for Windows 7 and
                Windows Server 2008 R2.

Automatically   Select this option to automatically provide the Orchestrator runbook
provide         input parameter values( which assumes that the runbook parameter
runbook         values are task sequence variables). For example, if a runbook has an
parameter       input parameter named OSDComputerName, then the
values          OSDComputerName task sequence variable value is passed to the
                runbook.

                This option works only for input parameters that are valid task sequence
                variable names and do not contain spaces or other special characters.
                Although spaces and other special characters are supported as
                Orchestrator parameter names, they are not valid task sequence variable
                names. If you need to pass values to parameters with spaces or other
                special characters, use the Specify explicit runbook parameters option.

                The other option is Specify explicit runbook parameters.

                The values provided for the runbook input parameters to the Orchestrator
                web service are formatted as XML. Passing values that contain data that is
                or resembles XML-formatted data may cause errors.

Specify         Select this option to explicitly provide the Orchestrator runbook input
explicit        parameters.
runbook
parameters      You must configure the following settings for each input parameter that
                the Orchestrator runbook requires:

                - Name. This is the name of the input runbook parameter.

                If you change the parameters for an existing Orchestrator runbook, you
                need to browse (reselect) for the runbook again, because MDT only
                retrieves the parameter list when initially adding the Orchestrator
                runbook.

                - Value. This can be a constant or a variable, such as a task sequence
                variable or an environment variable. For example, you can specify a value
                of %OSDComputerName%, which will pass the value of the
                OSDComputerName task sequence variable to the runbook input
                parameter.

Wait for the    This check box controls whether the task sequence step will wait for the
runbook to      runbook to finish before proceeding to the next task sequence step.If this
finish before   check box is:
continuing
                - Selected, then the task sequence step will wait for the runbook to finish
                before proceeding on to the next task sequence step.

<!-- p.444 -->

      Setting        Description

                     When this check box is selected, the task sequence step will poll the
                     Orchestrator web service for the runbook to finish. The amount of time
                     between polls starts at 1 second, then increases to 2, 4, 8, 16, 32, and 64
                     seconds between each poll. Once the amount of time reaches 64 seconds,
                     the task sequence step continues to poll every 64 seconds.

                     - Cleared, then the task sequence step will not wait for the runbook to
                     finish before proceeding to the next task sequence step.

                     This check box must be selected if the runbook returns output
                     parameters.

     If the Orchestrator runbook returns parameters, the values of the return
     parameters are set to corresponding task sequence variable names. If an
     Orchestrator runbook return parameter name contains spaces, the
     ZTIExecuteRunbook.wsf script will strip the spaces from the parameter name
     when creating the corresponding task sequence variable name.

  ７ Note

  If a runbook return parameter name contains other special characters, the return
  parameter may be ignored or generate errors.

For example, if a runbook return parameter has a name of OSD Computer Name, then
the corresponding task sequence variable name OSDComputerName and the value in
the return parameter will be saved in the OSDComputerName task sequence variable.

  ７ Note

  The Wait for the runbook to finish before continuing check box must be selected
  if the runbook returns output parameters.

Running Windows PowerShell Scripts During Deployment
MDT supports running Windows PowerShell scripts as a part of the deployment process.
You can develop Windows PowerShell scripts to help automate the deployment process
and then run those scripts within an MDT task sequence.

Run the Windows PowerShell scripts using a task sequence step created using the Run
PowerShell Script task sequence step type. You can add a task sequence step based on

<!-- p.445 -->

the Run PowerShell Script task sequence step type for task sequences in LTI, ZTI, or UDI.

  ７ Note

  For Configuration Manager task sequences, run the Use Toolkit Package task
  sequence step prior to running the Run PowerShell Script task sequence step.

To run a Windows PowerShell script in a task sequence

   1. Create the Windows PowerShell script.

     For more information about creating Windows PowerShell scripts for use in MDT
     task sequences, see Create Windows PowerShell Scripts for Use in MDT.

   2. Place the Windows PowerShell script in the Scripts subfolder in the:

           Deployment share for LTI

           MDT files package for ZTI and UDI

   3. Add a new task sequence step to your task sequence based on the Run
     PowerShell Script task sequence step type.

   4. In the newly create task sequence step, in the PowerShell script text box,
     script_name (where script_name is the fully qualified path to the Windows
     PowerShell script).

     If you specify:

           Just the script name, then the assumption is that the script exists in the
           Scripts subfolder

           A fully qualified path and script name, then ensure that the task sequence has
           access to the folder in which the script is stored (For example, if the script is
           stored on a network shared folder, ensure that there is an existing connection
           to that server prior to running the script.)

Applying Group Policy Object Packs
Deploying operating systems and applications so that they are compliant with security
and regulatory standards is an essential part of any deployment effort. MDT allows you
to apply security and compliance configuration templates to the operating system and
applications after they are deployed using Group Policy object (GPO) packs.

<!-- p.446 -->

GPO packs are created by exporting a GPO backup in the Microsoft Security Compliance
Manager. These GPO packs are applied by the Apply Local GPO Package task sequence
step for task sequences created using the MDT task sequence templates. The Apply
Local GPO Package task sequence step runs the ZTIApplyGPOPack.wsf script, which is
responsible for applying the GPO packs to the target computer.

  ７ Note

  GPO packs are only used to configure security and compliance configuration
  settings for Windows operating systems, not the applications running on the
  operating system. For example, the Internet Explorer or Microsoft Office security
  and compliance configuration settings in Security Compliance Manager cannot be
  used as GPO packs.

The following MDT task sequence templates include theApply Local GPO Package task
sequence step:

     Standard Client Task Sequence in LTI in ZTI

     Standard Server Task Sequence in LTI and ZTI

     Deploy to VHD Client Task Sequence in LTI

     Deploy to VHD Server Task Sequence in LTI

  ７ Note

  Applying GPO packs affects system behavior and features because of the increased
  security requirements that GPO packs could configure. The result is that you may
  lose certain functionality after a GPO pack is applied.

If the security configuration settings that the Security Compliance Manager GPO packs
provide are too stringent, perform one of the following tasks:

     Modify the existing GPO templates to be less restrictive.

     Provide a custom GPO template that you have created that is less restrictive.

     Disable the Apply Local GPO Package task sequence step in your task sequence.

     For example, the GPO pack for Windows 7 can enforce Server Message Block
     (SMB) configuration settings that could prevent Windows 7 from communicating
     with other devices running Common Internet File System (CIFS) or SAMBA.

<!-- p.447 -->

     Apply GPO packs templates by performing the following steps:

   1. Identify or create the GPO packs required by your organization as described in
     Identify or Create the GPO Packs.

   2. Place the GPO packs in the appropriate MDT folders as described in Place the GPO
     Packs in the Appropriate MDT Folders.

   3. Configure MDT to deploy the GPO packs as described in Configure MDT to Deploy
     the GPO Packs.

Identify or Create the GPO Packs

You can use GPO packs that are:

     Generated from the Security Compliance Manager. The Security Compliance
     Manager can export a GPO backup that you can use as a GPO pack. You can copy
     these GPO packs to the MDT files folder and apply them during the deployment
     process.

     Customized by you. You can create your own customized GPO packs based on
     your organization's requirements. You can use the security and compliance
     configuration settings in Security Compliance Manager as a beginning, and then
     customize those settings for your organization. Then, you can export the security
     and compliance configurations settings as a GPO backup and subsequently a GPO
     pack.

Place the GPO Packs in the Appropriate MDT Folders

After you have identified or created the GPO packs that your organization requires,
place the GPO packs in subfolder in the Templates\GPOPacksfolder in the:

     Deployment share for LTI

     MDT files package for ZTI and UDI

Configure MDT to Deploy the GPO Packs

The Apply Local GPO Package task sequence step can be configured using the
properties listed in Table 172. These properties can be configured using the
CustomSettings.ini file or the MDT DB.

<!-- p.448 -->

Table 172. Properties Used to Configure the Apply Local
GPO Package Task Sequence Step

                                                                                 ﾉ   Expand table

 Property       Description

 ApplyGPOPack   This property is used to determine whether the Apply Local GPO Package task
                sequence step is performed. If the value is set to:

                - YES, then the task sequence step is performed

                - NO, then the task sequence step is not performed

                The default value is YES.

                The ApplyGPOPack property can be set in the CustomSettings.ini file or in the
                MDT DB. For more information on configuring the ApplyGPOPack property, see
                the ApplyGPOPack property in the MDT document Toolkit Reference.

 GPOPackPath    This property is used to override the default path to the root folder for all the
                GPO packs. The path specified in this property is relative to the
                Templates\GPOPacks folder.The default path to the root folder for all the GPO
                packs is the Templates\GPOPacks folder.

                For more information on configuring the GPOPackPath property, see the
                GPOPackPath property in the MDT document Toolkit Reference.

  ７ Note

  The appropriate GPO pack is selected based on the operating system being
  deployed. If no matching GPO pack can be found, then no GPO pack will be
  applied.

Enabling Participation in CEIP and WER
MDT includes a new task sequence step that automates the configuration of
participation in Windows Customer Experience Improvement Program                   (CEIP) and
Windows Error Reporting (WER). The Opt In to CEIP and WER task sequence step is
used to automate this participation.

  ７ Note

<!-- p.449 -->

  Although you can use MDT task sequences to enable CEIP and WER for Windows
  operating systems (only when the corresponding task sequence step is enabled),
  this is separate from the CEIP information gathered when you opt in to the MDT
  CEIP program. For more information, see the Microsoft Privacy Statement       .

The Opt In to CEIP and WER task sequence step is included in the following MDT task
sequence templates but is disabled by default:

     Standard Client Task Sequence in LTI and ZTI

     Standard Server Task Sequence in LTI and ZTI

     Deploy to VHD Client Task Sequence in LTI

     Deploy to VHD Server Task Sequence in LTI

     User Driven Installation Task Sequence in UDI

     The Opt In to CEIP and WER task sequence step runs the ZTIOptIn.wsf script as
     shown in the following example:

  Windows Command Prompt

  cscript.exe %SCRIPTROOT%\ZTIOptIn.wsf /CEIP:YES /WER:YES

The ZTIOptIn.wsf script has the following named parameters:

     CEIP. This parameter determines the participation in CEIP and can be one of the
     following:

        YES. This value specifies to enable participation.

        NO. This value specifies to not enable participation.

       ７ Note

       Any value other than YES is treated as NO, including not providing the
       parameter.

     WER. This parameter determines the participation in WER and can be one of the
     following:

        YES. This value specifies to enable participation.

        NO. This value specifies to not enable participation.

<!-- p.450 -->

  ７ Note

  Any value other than YES is treated as NO, including not providing the parameter.

Configuring Roles and Features Task Sequence Steps
MDT automates the installation and uninstallation of Windows roles and features using
the Install Roles and Features and Uninstall Roles and Features task sequence step
types. These task sequence types allow organizations to deploy the target computers
with the Windows roles and features that comply with configuration standards defined
by organizational or regulatory authorities.

Configure the roles and features task sequence steps for LTI and ZTI by:

     Installing the appropriate Windows roles and features as described in Configure
     Install Roles and Features Task Sequence Steps

     Uninstalling the appropriate Windows roles and features as described in Configure
     Uninstall Roles and Features Task Sequence Steps

Configure Install Roles and Features Task Sequence Steps

MDT automates the deployment of Windows roles and features using the Install Roles
and Features task sequence step type. This task sequence step must be run in the target
operating system, not in Windows PE.

  ７ Note

  For ZTI task sequences that are not created using the MDT task sequence
  templates, ensure that you run the Use Toolkit Package and Gather task sequence
  step prior to running the Install Roles and Features task sequence step. The Install
  Roles and Features task sequence step depends on the Use Toolkit Package and
  Gather task sequence steps.

To configure the Install Roles and Features task sequence step type to
install Windows roles and features

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

<!-- p.451 -->

       LTI as described in Configure the Task Sequence Properties Task Sequence
       Tab

       ZTI using Configuration Manager as described in Configuring ZTI Task
       Sequence Steps in Configuration Manager

2. Add a new task sequence step based on the Install Roles and Features task
  sequence type for:

       LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
       point to Roles, and then select Install Roles and Features.)

       ZTI in the task sequence hierarchy (Select Add, point to MDT, and then select
       Install Roles and Features.)

3. On the Properties tab, configure the settings listed in Table 173 based on the
  requirements of your organization, and then select OK.

  Table 173. Configuration Settings on the Properties
  Tab of the Install Roles and Features Task Sequence
  Step Type

                                                                           ﾉ   Expand table

   Setting                           Description

   Name                              Type a name for the task.

   Description                       Type a description of the task.

   Select the operating system for   Select the target operating system to be deployed from
   which roles are to be installed   the following list:

                                     - Windows 7

                                     - Windows 8

                                     - Windows 8.1

                                     - Windows Server 2008 R2

                                     - Windows Server 2008 R2 Core

                                     - Windows Server 2012

                                     - Windows Server 2012 Core

<!-- p.452 -->

      Setting                         Description

                                      - Windows Server 2012 R2

                                      - Windows Server 2012 R2 Core

      Select the roles and features   Select the check box next to the roles or features to be
      that should be installed        installed.

                                      You can select Select All to select all the roles and
                                      features, or you can select Select None to clear all the
                                      roles and features.

     For information on how to uninstall Windows roles and features, see Configure
     Uninstall Roles and Features Task Sequence Steps.

Configure Uninstall Roles and Features Task Sequence Steps

MDT automates the removal (uninstallation) of operating system roles and features in
Windows using the Uninstall Roles and Features task sequence step. This task sequence
step must be run in the target operating system, not in Windows PE.

For ZTI task sequences that are not created using the MDT task sequence templates,
ensure that you run the Use Toolkit Package and Gather task sequence steps prior to
running the Install Roles and Features task sequence step. The Install Roles and
Features task sequence step depends on the Use Toolkit Package and Gather task
sequence steps.

  ７ Note

  Before uninstalling roles or features, remove all dependent roles or features.

To configure the Uninstall Roles and Features task sequence step type
to install Windows roles and features

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

           LTI as described in Configure the Task Sequence Properties Task Sequence
           Tab

           ZTI using Configuration Manager as described in Configuring ZTI Task
           Sequence Steps in Configuration Manager

<!-- p.453 -->

2. Add a new task sequence step based on the Uninstall Roles and Features task
  sequence type for:

       LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
       point to Roles, and then select Uninstall Roles and Features.)

       ZTI in the task sequence hierarchy (Select Add, point to MDT, and then select
       Uninstall Roles and Features.)

3. On the Properties tab, configure the settings listed in Table 174 based on the
  requirements of your organization, and then select OK.

  Table 174. Configuration Settings on the Properties
  Tab of the Uninstall Roles and Features Task Sequence
  Step Type

                                                                              ﾉ   Expand table

   Setting                              Description

   Name                                 Type a name for the task.

   Description                          Type a description of the task.

   Select the operating system for      Select the target operating system to be deployed
   which roles are to be uninstalled    from the following list:

                                        - Windows 7

                                        - Windows 8

                                        - Windows 8.1

                                        - Windows Server 2008 R2

                                        - Windows Server 2008 R2 Core

                                        - Windows Server 2012

                                        - Windows Server 2012 Core

                                        - Windows Server 2012 R2

                                        - Windows Server 2012 R2 Core

   Select the roles and features that   Select the check box next to the roles or features to be
   should be uninstalled                uninstalled.

<!-- p.454 -->

      Setting                             Description

                                          You can select Select All to select all the roles and
                                          features or select Select None to clear all the roles and
                                          features.

     For information on how to install Windows roles and features, see Configure Install
     Roles and Features Task Sequence Steps.

Configuring Server Role Task Sequence Steps
MDT automates the deployment of server roles in Windows Server. Configure task
sequence steps in MDT to deploy the server roles that are supported in MDT.

  ７ Note

  For ZTI task sequences that are not created using the MDT task sequence
  templates, ensure that you run the Use Toolkit Package and Gather task sequence
  steps prior to running any of the server role task sequence steps. The server role
  task sequence steps are dependent on the Use Toolkit Package and Gather task
  sequence steps.

Configure the Windows Server server role task sequence steps for MDT deployments by:

     Configuring the AD DS server role task sequence step as described in Configure
     AD DS Server Role Task Sequence Step Settings

     Configuring the DNS Server server role task sequence step as described in
     Configure DNS Server Role Settings

     Configuring the DHCP Server server role task sequence step as described in
     Configure DHCP Server Role Task Sequence Step Settings

     Configuring the Authorize DHCP task sequence step as described in Configure
     Authorize DHCP Task Sequence Step Settings

Configure AD DS Server Role Task Sequence Step Settings
AD DS stores directory data and manages communications between users and domains,
including logon processes, authentication, and directory searches. An AD DS domain
controller is a server that runs AD DS.

<!-- p.455 -->

  ７ Note

  For ZTI task sequences in Configuration Manager that are not created using the
  MDT task sequence templates, ensure that you run the Use Toolkit Package and
  Gather task sequence steps prior to running any of the server role task sequence
  steps. The server role task sequence steps are dependent on the Use Toolkit
  Package and Gather task sequence steps.

Configure the AD DS Server Role task sequence step by:

     Deploying a new domain controller in a new forest as described in Deploy a
     Domain Controller in a New Forest

     Deploying a new domain controller as a replica in an existing domain as described
     in Deploy a New Domain Controller as a Replica in an Existing Domain

     Deploying a new domain controller in a new domain tree in an existing forest as
     described in Deploy a New Domain Controller in a New Domain Tree in an Existing
     Forest

     Deploying a new domain controller in a new domain in an existing forest as
     described in Deploy a New Domain Controller in a New Domain in an Existing
     Forest

     Deploying a new read-only domain controller (RODC) in an existing domain as
     described in Deploy an RODC in an Existing Domain

     Configuring AD DS advanced properties for domain controllers as described in
     Configure AD DS Advanced Properties

Deploy a Domain Controller in a New Forest

Using this option, deploy a domain controller that contains a new forest environment.
Use this option when deploying a new forest environment.

To deploy a domain controller with a new forest

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

           LTI as described in Configure the Task Sequence Properties Task Sequence
           Tab

<!-- p.456 -->

           ZTI using Configuration Manager as described in Configuring ZTI Task
           Sequence Steps in Configuration Manager

  2. Add a new task sequence step based on the Configure ADDS task sequence type
    for:

           LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
           select Roles, and then select Configure ADDS.)

           ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
           Configure ADDS.)

  3. On the Properties tab, type the relevant information in the following boxes:

           Name. Type a name for the task.

           Description. Type a description of the task—for example, Server_Name
           Site_Name (where Server_Name is the name of the server and Site_Name is
           the name of the domain).

  4. In the Create box, select New Forest.

  5. In the New forest domain DNS name box, type a name for the new domain—for
    example, woodgrove.com.

    You must include the extension of the domain—for example, .com, .net, .int.

  6. In the NetBIOS name box, type a name for the NetBIOS.

    This name is usually the domain name without .com or any other type of extension.
    For example, the forest domain name woodgrove.com might have the NetBIOS
    name WOODGROVE.

  7. In the Recovery (safe mode) password box, type a password to use for safe mode
    recovery.

    You use this password to recover from a failed AD DS service. Make note of this
    password in case AD DS must be recovered.

  8. In the Advanced Properties section, complete the task configuration as described
    in Configure AD DS Advanced Properties, and then select OK.

    For more information about DCPROMO command-line options, see Dcpromo.

Deploy a New Domain Controller as a Replica in an Existing
Domain

<!-- p.457 -->

Using this option, deploy an existing domain controller as a new domain controller by
replicating it into an existing environment. Use this option when deploying a new
domain controller into an existing environment if replication will obtain the existing
domain information from AD DS.

To deploy a domain controller as a new domain controller replica

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

            LTI as described in Configure the Task Sequence Properties Task Sequence
            Tab

            ZTI using Configuration Manager as described in Configuring ZTI Task
            Sequence Steps in Configuration Manager

   2. Add a new task sequence step based on the Configure ADDS task sequence type
     for:

            LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
            select Roles, and then select Configure ADDS.)

            ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
            Configure ADDS.)

   3. On the Properties tab, type the relevant information in the following boxes:

            Name. Type a name for the task.

            Description. Type a description of the task—for example, Server_Name
            Site_Name (where Server_Name is the name of the server, and Site_Name is
            the name of the domain).

   4. In the Create box, select New domain controller replica.

   5. In the Existing domain DNS name box, type the FQDN of an existing domain
     controller.

   6. In the Replication source domain controller box, type the name of a domain
     controller the new server will replicate within the existing environment. The
     directory services database replicates this domain controller.

   7. In the Account box, type the name of an account that has permissions to add a
     domain controller to the existing network (typically, a domain Administrator
     account), and then select Set.

<!-- p.458 -->

   8. In the Recovery (safe mode) password box, type a password to use for safe mode
     recovery.

     This password is used to recover from a failed AD DS service. Make note of this
     password in case AD DS must be recovered.

   9. In the Advanced Properties section, complete the task configuration as described
     in Configure AD DS Advanced Properties, and then select OK.

     For more information about DCPROMO command-line options, see Dcpromo.

Deploy a New Domain Controller in a New Domain Tree in an
Existing Forest

Using this option, deploy a domain controller that contains a new tree into an existing
forest environment. Use this option when deploying a child domain into an existing
forest environment.

To deploy a domain controller with a new domain tree in an existing
forest

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

            LTI as described in Configure the Task Sequence Properties Task Sequence
            Tab

            ZTI using Configuration Manager as described in Configuring ZTI Task
            Sequence Steps in Configuration Manager

   2. Add a new task sequence step based on the Configure ADDS task sequence type
     for:

            LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
            select Roles, and then select Configure ADDS.)

            ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
            Configure ADDS.)

   3. On the Properties tab, type the relevant information in the following boxes:

            Name: Type a name for the task.

            Description. Type a description of the task—for example, Server_Name
            Site_Name (where Server_Name is the name of the server and Site_Name is

<!-- p.459 -->

          the name of the domain).

   4. In the Create box, select New domain in existing forest.

   5. In the Existing forest (parent) domain DNS name box, type the name of an
     existing domain in the network.

   6. In the NetBIOS name box, type the NetBIOS name of an existing domain in the
     network, usually the domain name without .com or any other type of extension—
     for example, the domain woodgrove.com might have the NetBIOS name
     WOODGROVE.

   7. In the New domain tree (child) DNS name box, type a name for the child domain
     being created—for example, child.woodgrove.com (where child is the name of the
     child domain).

   8. In the Replication source domain controller box, type the name of the domain
     controller to which the new child domain will replicate.

   9. In the Account box, type the name of an account with permissions to add a
     domain controller to the existing network (typically, a domain Administrator
     account), and then select Set.

 10. In the Recovery (safe mode) password box, type a password to use for safe mode
     recovery.

     You use this password to recover from a failed AD DS service. Make note of this
     password in case AD DS must be recovered.

 11. In the Advanced Properties section, complete the task configuration as described
     in Configure AD DS Advanced Properties, and then select OK.

     For more information about DCPROMO command-line options, see Dcpromo.

Deploy a New Domain Controller in a New Domain in an Existing
Forest

Using this option, deploy a domain controller that contains a new domain into an
existing forest environment. Use this option when deploying a new child domain into an
existing forest environment.

To deploy a domain controller with a new domain in an existing forest

<!-- p.460 -->

1. Edit task_sequence_name (where task_sequence_name is the name of the task
  sequence to which you want to add the task sequence step) for:

         LTI as described in Configure the Task Sequence Properties Task Sequence
         Tab

         ZTI using Configuration Manager as described in Configuring ZTI Task
         Sequence Steps in Configuration Manager

2. Add a new task sequence step based on the Configure ADDS task sequence type
  for:

         LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
         select Roles, and then select Configure ADDS.)

         ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
         Configure ADDS.)

3. On the Properties tab, type the relevant information in the following boxes:

         Name. Type a name for the task.

         Description. Type a description of the task—for example, Server_Name
         Site_Name (where Server_Name is the name of the server and Site_Name is
         the name of the domain).

4. In the Create box, select New domain in existing forest.

5. In the Existing forest (parent) domain DNS name box, type the name of an
  existing domain in the network.

6. In the NetBIOS name box, type the NetBIOS name of an existing domain in the
  network, usually the domain name without .com or any other type of extension—
  for example, the domain woodgrove.com might have the NetBIOS name
  WOODGROVE.

7. In the New domain (child) DNS name box, type a name for the child domain
  being created—for example, child.woodgrove.com (where child is the name of the
  child domain).

8. In the Replication source domain controller box, type the name of the domain
  controller to which the new child domain will be replicated.

9. In the Account box, type the name of an account with permissions to add a
  domain controller to the existing network (typically, a domain Administrator
  account), and then select Set.

<!-- p.461 -->

 10. In the Recovery (safe mode) password box, type a password to use for safe mode
     recovery.

     You use this password to recover from a failed AD DS service. Make note of this
     password in case AD DS must be recovered.

 11. In the Advanced Properties section, complete the task configuration as described
     in Configure AD DS Advanced Properties, and then select OK.

     For more information about DCPROMO command-line options, see Dcpromo.

Deploy an RODC in an Existing Domain

Using this option, deploy a domain controller that contains a read-only replica of the
existing domain into an existing forest environment. Use this option to deploy a domain
controller that contains an un-editable replica of a domain structure into an existing
forest environment.

To deploy an RODC in an existing domain

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

            LTI as described in Configure the Task Sequence Properties Task Sequence
            Tab

            ZTI using Configuration Manager as described in Configuring ZTI Task
            Sequence Steps in Configuration Manager

   2. Add a new task sequence step based on the Configure ADDS task sequence type
     for:

            LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
            select Roles, and then select Configure ADDS.)

            ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
            Configure ADDS.)

   3. On the Properties tab, type the relevant information in the following boxes:

            Name. Type a name for the task.

            Description. Type a description of the task; for example, Server_Name
            Site_Name (where Server_Name is the name of the server and Site_Name is
            the name of the domain).

<!-- p.462 -->

  4. In the Create box, select New read-only domain controller (RODC) replica.

  5. In the Existing domain DNS name box, type the name of an existing DNS server.

  6. In the Replication source domain controller box, type the name of the domain
     controller to be replicated within the existing environment. The directory services
     database replicates this domain controller.

  7. In the Account box, type the name of an account with permissions to add a
     domain controller to the existing network (typically, a domain Administrator
     account), and then select Set.

  8. In the Recovery (safe mode) password box, type a password to use for safe mode
     recovery.

     You use this password to recover from a failed AD DS service. Make note of this
     password in case AD DS must be recovered.

  9. In the Advanced Properties section, complete the task configuration as described
     in Configure AD DS Advanced Properties, and then select OK.

     For more information about DCPROMO command-line options, go to Dcpromo.

Configure AD DS Advanced Properties

To configure AD DS advanced properties, perform the following steps:

  1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

          LTI as described in Configure the Task Sequence Properties Task Sequence
          Tab

          ZTI using Configuration Manager as described in Configuring ZTI Task
          Sequence Steps in Configuration Manager

  2. Modify the Configure ADDS task sequence step you created for:

          LTI on the Task Sequence tab (In the task sequence hierarchy, select
          task_sequence_step [where task_sequence_step is the Configure ADDS task
          sequence step].)

          ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
          task_sequence_step [where task_sequence_step is the Configure ADDS task
          sequence step].)

<!-- p.463 -->

3. On the Properties tab, select Advanced.

4. In the AD DS Advanced Properties dialog box, in the Options, Functional Levels,
  and Folders sections, select the following options as required for your environment
  and AD DS scenario:

  Options section:

       Install DNS if not already present. Select this option when creating a new
       forest or new domain.

       Make this domain controller a global catalog (GC) server. This is the default
       option and should be selected for new domains or forests and domains
       without a GC server.

       Wait for critical replication only. Select this option to populate only the
       directory services database using replication.

       Functional levels section:

       Forest Functional Level. Windows Server 2003, Windows Server 2008 (2 =
       Windows Server 2003; 3 = Windows Server 2008; 4 = Windows Server 2008
       R2)

       Domain Functional Level. Windows Server 2003, Windows Server 2008 (2 =
       Windows Server 2003; 3 = Windows Server 2008; 4 = Windows Server 2008
       R2)

       Folders section:

       Database. Contains the fully qualified path on the target computer to the
       location for the NTDS database. The default value is %SYSTEMROOT%NTDS.
       You can also configure this value using the DatabasePath property in the
       CustomSettings.ini file or the MDT DB.

       Log Files. Contains the fully qualified path on the target computer to the
       location for the log files. The default value is %SYSTEMROOT%NTDS. You can
       also configure this value using the LogPath property in the
       CustomSettings.ini file or the MDT DB.

       SYSVOL. Contains the fully qualified path on the target computer to the
       location for the SYSVOL folder. The default value is %SYSTEMROOT%SYSVOL.
       You can also configure this value using the SysVolPath property in the
       CustomSettings.ini file or the MDT DB.

<!-- p.464 -->

        ７ Note

        If you configure values in the CustomSettings.ini or the MDT DB, use the
        %DESTINATIONLOGICALDRIVE% task sequence variable instead of the
        %SYSTEMROOT% variable. For LTI deployments, the variables are evaluated
        while running Windows PE, so the %SYSTEMROOT% variable will return the
        SystemRoot folder for Windows PE, not the target operating system. The
        %SYSTEMROOT% variable for Windows PE typically is set to X:\WINDOWS.

   5. In the Site name box, type the name of the site in which to install the domain
     controller.

     The default name for a new forest or site is default_first_site; however, this value
     does not appear in the Site name box by default—you must type it. Then, select
     OK to complete the configuration of the AD DS Advanced Properties dialog box,
     and then select OK in the Task Name Properties dialog box to complete
     configuration of the task.

Configure DNS Server Role Settings

Using this option, configure and deploy the DNS server role to a new computer or a
DNS server operating on an existing computer. By assigning the DNS server role, you
can configure standard DNS primary, secondary, and stub zones as well as AD DS-
integrated primary and stub zones. There is also an option to manage aging, updates,
types, and multiple zones—all in an automated process. This is not a migration process
from an existing DNS server; rather, it is a new installation of DNS zones of all types.

  ７ Note

  For ZTI task sequences using Configuration Manager that are not created using the
  MDT task sequence templates, ensure that you run the Use Toolkit Package and
  Gather task sequence steps prior to running any of the server role task sequence
  steps. The server role task sequence steps are dependent on the Use Toolkit
  Package and Gather task sequence steps.

To configure and deploy the DNS server role

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

<!-- p.465 -->

          LTI as described in Configure the Task Sequence Properties Task Sequence
          Tab

          ZTI using Configuration Manager as described in Configuring ZTI Task
          Sequence Steps in Configuration Manager

 2. Add a new task sequence step based on the Configure DNS task sequence type
   for:

          LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
          select Roles, and then select Configure DNS.)

          ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
          Configure DNS.)

 3. On the Properties tab, in Name, type name (where name is the name by which the
   task is identified in the task sequence).

 4. In Description, type description (where description is the description of the task
   and its role in the task sequence).

 5. In the Zones section, select the yellowAdd button.

 6. In the DNS Zone Properties dialog box, in DNS zone name, type a name for the
   zone (for example, woodgrove.com).

 7. In Type, select Change.

 8. In the Change Zone Type dialog box, select one of the following zone types:

          Primary zone

          Secondary zone

          Stub zone

 9. In the Change Zone Type dialog box, select the Store the zone in Active Directory
   check box if DNS will be installed on a domain controller, and then select OK.

10. In theDNS Zone Properties dialog box, in Dynamic updates, select one of the
   following:

          None

          Nonsecure and Secure

<!-- p.466 -->

 11. Select the Scavenge stale resource records check box to enable this feature, and
     then select OK.

 12. On the Properties tab of the Configure DNS step, select Server Properties.

 13. In the Server Properties dialog box, in Server Options, select the appropriate
     server options to enable.

 14. In the Server Properties dialog box, in Name checking, select the appropriate
     name-checking options to enforce, and then select OK.

 15. In the task_sequence Properties dialog box (where task_sequence is the name of
     the task sequence being edited), select OK.

 16. Close the Deployment Workbench.

Configure DHCP Server Role Task Sequence Step Settings
Using this option, configure and deploy the DHCP server role using MDT. You can
configure all the standard DHCP scope options similar to using the standard DHCP
console in Windows Server. To implement the DHCP server role, configure the Authorize
DHCP task sequence in conjunction with the Configure DHCP Server task sequence.

  ７ Note

  For ZTI task sequences using Configuration Manager that are not created using the
  MDT task sequence templates, ensure that you run the Use Toolkit Package and
  Gather task sequence steps prior to running any of the server role task sequence
  steps. The server role task sequence steps are dependent on the Use Toolkit
  Package and Gather task sequence steps.

Configure the Configure DHCP Server task sequence step settings by:

     Configuring the deployment of the DHCP server role as described in Configure
     Deployment of the DHCP Server Role

     Configuring the DHCP scopes for the DHCP server role as described in Configure
     DHCP Scopes for the DHCP Server Role

     Configuring the DHCP server options for the DHCP server role as described in
     Configure the DHCP Server Options for the DHCP Server Role

Configure Deployment of the DHCP Server Role

<!-- p.467 -->

Install and configure the DHCP Server role on the target computer by modifying the
Configure DHCP Server task sequence step type.

To configure and deploy the DHCP server role

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

           LTI as described in Configure the Task Sequence Properties Task Sequence
           Tab

           ZTI using Configuration Manager as described in Configuring ZTI Task
           Sequence Steps in Configuration Manager

   2. Add a new task sequence step based on the Configure DHCP Server task
     sequence type for:

           LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
           select Roles, and then select Configure DHCP.)

           ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
           Configure DHCP.)

   3. On the Properties tab, type the relevant information in the following boxes:

           Name. The name by which the task will be identified in the task sequence list.

           Description. A description of the task (for example, DHCP scope information,
           scope names).

           Scope details. Details about the IP address the DHCP scopes configured.

           Server options. The options passed to DHCP clients (for example, default
           gateway, DNS server, and WINS server addresses).

   4. Select OK.

Configure DHCP Scopes for the DHCP Server Role

Using this option, configure the DHCP scopes that contain the rules and active scopes
used on the DHCP server. For more information about DHCP scope configuration
options and for guidance on using each configuration option, see Chapter 6 - Dynamic
Host Configuration Protocol    in TCP/IP Fundamentals for Microsoft Windows.

<!-- p.468 -->

To configure and deploy DHCP scopes

  1. Edit task_sequence_name (where task_sequence_name is the name of the task
    sequence to which you want to add the task sequence step) for:

         LTI as described in Configure the Task Sequence Properties Task Sequence
         Tab

         ZTI using Configuration Manager as described in Configuring ZTI Task
         Sequence Steps in Configuration Manager

  2. Modify the task sequence step you created based on the Configure DHCP task
    sequence type for:

         LTI on the Task Sequence tab (In the task sequence hierarchy, select
         task_sequence_step [where task_sequence_step is the name of the task
         sequence step].)

         ZTI in the task sequence hierarchy (Select task_sequence_step [where
         task_sequence_step is the name of the task sequence step].)

  3. On the Properties tab, select the yellow Add scope button.

  4. In the Scope Properties dialog box, configure the following options as required for
    the environment:

         Scope name. The name used to refer to the scope.

         Start IP address. The beginning address of the scope (for example,
         192.168.0.150).

         End IP address. The ending address of the scope (for example,
         192.168.0.250).

         Subnet mask. The mask used for the IP address scope (for example,
         255.255.255.0).

         Scope IP address. The address of the scope itself (for example, 192.168.0.1).

         Lease duration for DHCP clients. The maximum time a client can keep the IP
         address that the DHCP server assigns.

         Description. A description of the scope (for administrative reference).

  5. On the Advanced tab, in the Exclude IP Address Range section, type the following
    information to exclude addresses for the scope created on the General tab:

<!-- p.469 -->

           Start IP address. The beginning address for exclusion from a scope (for
           example, 192.168.0.251).

           End IP address. The ending address for exclusion from a scope (for example,
           192.168.0.255).

   6. On the Options tab, configure the following options for the scope created on the
     General tab:

           003 Router. The default gateway given to DHCP clients.

           006 DNS Servers. The DNS server address given to DHCP clients.

           015 DNS Domain Name. The DNS domain name given to clients (for
           example, woodgove.com).

           044 WINS/NBNS Servers. The WINS server IP address (for example,
           192.168.0.2).

           046 WINS/NBT Node Type. The WINS node type.

           060 PXE Client. The address used for PXE client Bootstrap code.

   7. Select OK.

Configure the DHCP Server Options for the DHCP Server Role

Using this option, configure the DHCP server options given to DHCP clients, including
router or default gateway designation, DNS server IP information, and WINS server
information.

To configure and deploy DHCP server options

   1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

           LTI as described in Configure the Task Sequence Properties Task Sequence
           Tab

           ZTI using Configuration Manager as described in Configuring ZTI Task
           Sequence Steps in Configuration Manager

   2. Modify the task sequence step you created based on the Configure DHCP task
     sequence type for:

<!-- p.470 -->

       LTI on the Task Sequence tab (In the task sequence hierarchy, select
       task_sequence_step [where task_sequence_step is the name of the task
       sequence step].)

       ZTI in the task sequence hierarchy (Select task_sequence_step [where
       task_sequence_step is the name of the task sequence step].)

3. On the Properties tab, in the Server Options section, select Configure, and then
  configure the following options as required for your environment.

4. Select 003 Router, and then perform the following steps:

  a. In the Server Name box, type the IP address and resolve the name.

  b. Select Add to type an IP address.

   c. Select an IP address, and then select Remove to remove the highlighted IP
     address.

5. Select 006 DNS Servers, and then perform the following tasks:

  a. In the Server Name box, type the IP address and resolve the name.

  b. Select Add to type an IP address.

   c. Select an IP address, and then select Remove to remove the highlighted IP
     address.

6. Select 015 DNS Domain Name, and then, in the String Value box, type the domain
  name (for example, woodgrove.com).

7. Select 044 WINS/NBNS Servers, and then perform the following tasks:

  a. In the Server Name box, type the IP address and resolve the name.

  b. Select Add to type an IP address.

   c. Select an IP address, and then select Remove to remove the highlighted IP
     address.

8. Select 046 WINS/NBT Node Type, and then type one of the following codes: 44,
  46, or 47.

  For more information about how to determine the correct option for the
  environment, see Managing DHCP Options.

<!-- p.471 -->

  9. Select 060 PXE Client; then, in the String Value box, type the PXE client string
     (typically, PXEClient).

Configure Authorize DHCP Task Sequence Step Settings

Authorizing the DHCP service within AD DS is imperative to successfully deploying and
using DHCP services within a Windows-based network.

  ７ Note

  The ZTI task sequence templates that are provided with MDT do not include an
  Authorize DHCP task sequence step type. You must manually add this step type if
  you want to automatically authorize the DHCP server as a part of the ZTI
  deployment.

To authorize the DHCP server role in AD DS

  1. Edit task_sequence_name (where task_sequence_name is the name of the task
     sequence to which you want to add the task sequence step) for:

            LTI as described in Configure the Task Sequence Properties Task Sequence
            Tab

            ZTI using Configuration Manager as described in Configuring ZTI Task
            Sequence Steps in Configuration Manager

  2. Add a new task sequence step based on the Authorize DHCP task sequence type
     for:

            LTI on the Task Sequence tab (In the task sequence hierarchy, select Add,
            select Roles, and then select Authorize DHCP.)

            ZTI in the task sequence hierarchy (Select Add, select MDT, and then select
            Authorize DHCP.)

  3. On the Properties tab, type the relevant information in the following boxes:

            Name. The name by which the task appears in the task sequence list.

            Description. A description of the task.

  4. In the Account box, type the name of an account with permissions to authorize the
     DHCP service in AD DS. Select Set, and then type the following information in the

<!-- p.472 -->

     relevant boxes:

           Username. The account that can authorize DHCP, in the format domain\user

           Password. The password for the account

           Confirm Password. Retype the password

   5. Select OK, then select OK again.

Copying Content to the Target Computer
To copy content to target computers, perform any combination of the following steps:

     Copy content to the target computer using a task sequence step as described in
     Copy Content to Target Computers Using Task Sequence Steps.

     Copy content to the target computer using $OEM$ folders as described Copy
     Content to Target Computers Using $OEM$ Folders.

Copy Content to Target Computers Using Task Sequence Steps
Create a task sequence based on the Run Command Line task sequence step type that
runs the xcopy.exe command or a similar command to copy the content to the target
computer. Ensure that the Run Command Line task sequence step type occurs prior to
any task sequence steps or scripts that depend on the files being copied to the target
computers. For more information about modifying task sequence steps, see Configure
the Task Sequence Steps and Step Sequence.

Copy Content to Target Computers Using $OEM$ Folders
MDT supports using legacy $OEM$ folders to organize and copy supplemental files to
the target computers. Data WIM files are preferred over $OEM$ folders.

  ７ Note

  In an instance where multiple $OEM$ folders have been defined, the first driver that
  LTIApply.wsf finds is deployed to the target computer.

For more information about using data WIM files or $OEM$ folders see the Windows
Assessment and Deployment Kit User's Guide in the Windows ADK.

<!-- p.473 -->

MDT looks in the following locations within the deployment share, in the order specified,
to find an $OEM$ folder:

     Control\task_sequence (where task_sequence is the name or ID of the task
     sequence that MDT is installing). Create $OEM$ folders in this location to create a
     custom folder for each build.

     Operating Systems\Name (where Name is the name of the operating system MDT
     is installing). Create $OEM$ folders in this location to create a custom folder for
     each operating system.

     Platform (where Platform is either x86 or x64). Create $OEM$ folders in this
     location to create a custom folder for each platform.

     $OEM$, which is at the root of the deployment share and is the default $OEM$
     folder if a folder is not found in the previous locations.

     An $OEM$ folder contains supplemental files. The following list describes each
     folder that you can create within an $OEM$ folder to organize these files:

     $$. Windows Setup copies the contents of this folder to %SystemRoot% on each
     destination computer. It replicates all the folders, subfolders, and files that this
     folder contains in the %SystemRoot% folder of each destination computer. For
     Windows Setup to copy a file to %SystemRoot%\System32 on each destination
     computer, for example, put the file in $OEM$\$$\System32.

     $1. Windows Setup copies the contents of this folder to %SystemDrive% on each
     destination computer. It replicates all the folders, subfolders, and files that this
     folder contains in the %SystemDrive% folder on each destination computer. This is
     typically drive C on most computers.

     Drive. Drive is a drive letter (C, D, E, and so on). Windows Setup copies the
     contents of this folder to the root of the corresponding drive on each destination
     computer. It replicates all the folders, subfolders, and files that this folder contains
     in the corresponding drive during the setup process. For example, Windows Setup
     copies any files put in $OEM$\D to the root of drive D on each destination
     computer.

     Microsoft recommends that these folders not be used. The folders rely on a very
     specific disk configuration on the destination computer. Use $1 to represent
     %SystemDrive%, instead. In most installations, $OEM$\$1 and $OEM$\C write to
     the same location: the root of drive C.

Creating Custom Scripts for MDT

<!-- p.474 -->

Scripts provide automation of the image-build and overall deployment process. They
scan the configuration files, query the configuration database, evaluate environment
variables to determine the rules to be used when deploying the images to the target
computers, and perform many other intricate deployment tasks. MDT uses both
Microsoft Visual Basic® Scripting Edition (VBScript [.vbs]) and Windows Script file (.wsf)
scripts. Typically, there is no need to modify one of the delivered scripts. If a
modification is necessary, instead of modifying one of the delivered scripts, copy the
script to a new file, update it, and thoroughly test the effect of any change.

The scripts create log files as the scripts automate the deployment process. The log files
record the status of the deployment process and can be used to assist in
troubleshooting this process:

     Develop new scripts for use in MDT deployments as described in Develop Custom
     Scripts.

     Create new scripts for use in MDT deployments from a template as described in
     Create New Scripts from a Template.

     Create Windows PowerShell scripts for use in MDT deployments as described in
     Create Windows PowerShell Scripts for Use in MDT.

Develop Custom Scripts

You can develop new scripts for use in MDT deployments. These scripts should be in the
form of .vbs or .wsf files. For examples of scripts that the Deployment Workbench uses,
open the installation path of the deployment share, and then open the Scripts folder.

  ７ Note

  Microsoft does not support customized and custom scripts.

Before describing how to create a script, it is best to review how the scripts included
with MDT are constructed. The standard MDT script is a .wsf file, which allows references
to be made to functions that are contained in other scripts. MDT scripts leverage this
functionality by referencing the ZTIUtility.vbs script and the ZTIDataAccess.vbs script.
The ZTIUtility.vbs script is used to initialize the MDT environment and setup classes. The
ZTIDataAccess.vbs script includes the common routines for database access, including
connecting to and querying databases, and provides a web service interface.

The scripts define several standard objects that need not be declared in the script:

     oFSO. File System Object

<!-- p.475 -->

       oShell. WScript Shell object

       oEnv. Process Environment object

       oNetwork. WScript Network object

       The following classes are defined that perform several standard tasks:

       Environment. Configures environment variables gathered through WMI and MDT
       rule processing, allowing for direct reference from the script, and is defined in
       ZTIUtility.vbs as described in Environment Class.

       Logging. Provides the logging functionality that all MDT scripts use, creating a
       single log file for each script and a consolidated log file of all scripts and is defined
       in ZTIUtility.vbs as described in Logging Class.

       Utility. Provides general utility functionality and is defined in ZTIUtility.vbs as
       described in Utility Class.

       Database. Provide access to databases and is defined in ZTIDataAccess.vbs as
       described in Database Class. The Database class:

          Is used by ZTIGather.wsf when processing database rules from the
          CustomSettings.ini or BootStrap.ini files

          Can be used to access databases in scripts instead of configuring the
          CustomSettings.ini or BootStrap.ini files; you can specify the parameters for
          accessing the database in the scripts

       WebService. Provides access to web services and is defined in ZTIDataAccess.vbs
       as described in WebService Class. The WebService class:

          Is used by ZTIGather.wsf when processing web service rules from the
          CustomSettings.ini or BootStrap.ini files

          Can be used to access web services in scripts instead of configuring the
          CustomSettings.ini or BootStrap.ini files; you can specify the parameters for
          accessing the web services in the scripts

Environment Class

Reference this class in scripts through the oEnvironment object. For example, change
the computer name to Example using the command:

  VB

<!-- p.476 -->

  oEnvironment.Item("ComputerName") = "Example"

Or, to determine whether this is a 32-bit or 64-bit architecture, query the architecture
using the command:

  VB

  oEnvironment.Item("Architecture")

Logging Class

Reference this class in scripts through the oLogging object. When creating an
informational log entry, use the command:

  VB

  oLogging.CreateEntry "Informational message", LogTypeInfo

When creating an error log entry, use the command:

  VB

  oLogging.CreateEntry "An error occurred",LogTypeError

Utility Class

Reference this class in scripts through the oUtility object. To determine the name of the
current script, use the command:

  VB

  oUtility.ScriptName

To find the location of a file, use the command:

  VB

  iRetVal = oUtility.FindFile("CustomSettings.ini", sIniFile)

Database Class

<!-- p.477 -->

Reference this class in scripts through the Database class. You can create an instance of
the object class and connect to a database using following script excerpt:

  VB

  <script language="VBScript" src="ZTIUtility.vbs"/>         <script
  language="VBScript" src="ZTIDataAccess.vbs"/>
  <script language="VBScript">

       Dim oDatabase
       Dim oRecordset

       Set oDatabase = new Database
       oDatabase.SQLServer = "NYC-MDT-01"
       oDatabase.Instance = "SQLExpress"
       oDatabase.Database = "MDTDB"
       oDatabase.Port = ""
       oDatabase.Netlib = "DBNMPNTW"
       oDatabase.Table = "ComputerSettings"
       oDatabase.Parameters = "UUID, AssetTag, SerialNumber, MacAddress"
       oDatabase.ParameterCondition = "OR"
       oDatabase.SQLShare = "DeploymentShare$"

       oDatabase.Connect

       Set oRecordset = oDatabase.Query
       WScript.Echo "Records retrieved: " & oRecordset.RecordCount

WebService Class

Reference this class in scripts through the WebService class. You can create an instance
of the object class and connect to a database using following script excerpt:

  VB

  <script language="VBScript" src="ZTIUtility.vbs"/>         <script
  language="VBScript" src="ZTIDataAccess.vbs"/>
  <script language="VBScript">

       Dim oWebService
       Dim oXML

     oEnvironment.Item("USZip") = "98029"
     oEnvironment.Item("USZip") = "98029"
     Set oWebService = new WebService
     oWebService.WebService =
  "https://www.webservicex.net/uszip.asmx/GetInfoByZIP"
     oWebService.Parameters = "USZip"

       Set oXML = oWebService.Query

<!-- p.478 -->

       WScript.Echo "Web service response:"
       WScript.Echo oXML.XML

Create New Scripts from a Template
You can also create scripts for use in the imaging process. You call these scripts by
adding them to the Task Sequence Editor and ultimately by adding them to the TS.xml
file. Listing 13 shows a template for creating custom scripts.

Listing 13. Custom Script Template

  VB

  <job id="Z-Sample">
  <script language="VBScript" src="ZTIUtility.vbs"/>
  <script language="VBScript">

  '
  //**************************************************************************
  *
  ' // ***** Script Header *****
  ' //
  ' // Solution: Solution Accelerator for Microsoft Deployment
  ' // File: Z-Sample.wsf
  ' //
  ' // Purpose: Template
  ' //
  ' // Usage: cscript Z-Sample.wsf [/debug:true]
  ' //
  ' // Customer Build Version: 1.0.0
  ' // Customer Script Version: 1.0.0
  ' // Customer History:
  ' //
  ' // ***** End Header *****
  '
  //**************************************************************************
  *

  '//-------------------------------------------------------------------------
  ---
  '//
  '// Global constant and variable declarations
  '//
  '//-------------------------------------------------------------------------
  ---

  Option Explicit

  Dim iRetVal

  '//-------------------------------------------------------------------------

<!-- p.479 -->

  ---
  '// End declarations
  '//-------------------------------------------------------------------------
  ---

  '//-------------------------------------------------------------------------
  ---
  '// Main routine
  '//-------------------------------------------------------------------------
  ---

  On Error Resume Next
  iRetVal = ZTIProcess
  ProcessResults iRetVal
  On Error Goto 0

  '//-------------------------------------------------------------------------
  --
  '//
  '// Function: ZTIProcess()
  '//
  '// Input: None
  '//
  '// Return: Success - 0
  '// Failure - non-zero
  '//
  '// Purpose: Perform main ZTI processing
  '//
  '//-------------------------------------------------------------------------
  --
  Function ZTIProcess()

        iRetVal = Success

        ZTIProcess = iRetval

        '!!!!!!!!!!!      INSERT YOUR CODE HERE        !!!!!!!!!!!!

  End Function

  </script>
  </job>

At a high level, complete the following steps to add a custom script:

   1. Create the script based on the template.

   2. Place the script in the Scripts folder of the:

           Deployment share for LTI deployments

           Package source for the Microsoft Deployment Toolkit Files package

<!-- p.480 -->

  3. Create a task sequence step based on the Run Command Line task sequence step
     type in your task sequence.

  4. Configure the task sequence step created in the previous step to run your script.

     Follow these guidelines when creating a script:

     Always declare variables.

     Only create objects where required, because MDT includes most objects that are
     needed.

     Verify that ZTIUtility.vbs and ZTIDataAccess.vbs do not already provide the
     functionality required before writing a function.

Create Windows PowerShell Scripts for Use in MDT

MDT allows you to create Windows PowerShell scripts, and then run those scripts as a
part of a MDT task sequence using the Run PowerShell Script task sequence step type.
The Windows PowerShell scripts that you create can perform any typical automation
supported by the target operating system.

Create Windows PowerShell scripts for use in MDT by:

  1. Including the prerequisites in your Windows PowerShell script for running in MDT
     as described in Include Prerequisites for Running Windows PowerShell Scripts in
     MDT

  2. Using task sequence variables within your Windows PowerShell script as described
     in Use Task Sequence Variables Within Windows PowerShell Scripts

  3. Updating the MDT logs with output from your Windows PowerShell scripts as
     described in Update MDT Logs Using Windows PowerShell Scripts

  4. Interpreting Windows PowerShell return codes generated by your script as
     described in Interpret Windows PowerShell Script Return Codes

Include Prerequisites for Running Windows PowerShell Scripts in
MDT

When a Run PowerShell Script task sequence step runs a Windows PowerShell script,
the step automatically loads the Microsoft.BDD.TaskSequenceModule module prior to
running the script. The Microsoft.BDD.TaskSequenceModule module is responsible for
creating the TSENV: and TSENVLIST: Windows PowerShell drives.
