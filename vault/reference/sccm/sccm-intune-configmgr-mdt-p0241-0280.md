---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 241-280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0241-0280
family: sccm
documentKind: "doc"
abstract: "Option Select this option to Keyboard Layout Select the keyboard layout for Windows PE prior to completing the LTI deployment process. Configure with Static IP Configure the IP configuration settings for Windows PE when Address DHCP configuration is not available. Select this bu"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 241-280

<!-- p.241 -->

   Option                     Select this option to

   Keyboard Layout            Select the keyboard layout for Windows PE prior to completing
                              the LTI deployment process.

   Configure with Static IP   Configure the IP configuration settings for Windows PE when
   Address                    DHCP configuration is not available. Select this button to open
                              the Configure Static IP Network Settingsdialog box.

                              The IP configuration settings configured in the Configure
                              Static IP Network Settings dialog box override any IP
                              configuration settings specified in the CustomSettings.ini file or
                              in the MDT DB.

  The Specify credentials for connecting to network shares wizard page in the
  Deployment Wizard is displayed.

5. Complete the Specify credentials for connecting to network shares page, and
  then select OK.

  Complete the Specify credentials for connecting to network shares page, and
  then select OK.

  This wizard appears when the conditions in Table 89 are met.

  Table 89. Specify Credentials for Connecting to
  Network Shares Page Conditions

                                                                             ﾉ   Expand table

   Property                                     Condition

   UserID_isDirty                               Equal to TRUE

   UserID                                       Equal to ""

   DeploymentType                               Not equal to REPLACE

   DeploymentMethod                             Not equal to MEDIA

  You use these credentials to access network shared folders used during the
  deployment process. These shared folders include folders used to store user state
  migration data or image backups of the target computer.

  Table 90. Credentials Options

<!-- p.242 -->

                                                                          ﾉ   Expand table

   Option     Type

   User       user_name (where user_name is the user name of the account that has the
   Name       appropriate permissions for the network shared folders that the deployment
              scripts use).

   Password   password (where password is the password for the user account specified in
              the User Name box).

   Domain     domain (where domain is the name of the domain in which the user account,
              specified in the User Name box, is located).

  The Task Sequence page is displayed.

6. On the Task Sequence page, beneath Select a task sequence to execute on this
  computer, select task_sequence (where task_sequence is the name of the task
  sequence to run).

    ７ Note

    If a task sequence based on the Litetouch OEM task sequence template
    appears in the list, ensure that the deployment is being performed from a
    removable media (MEDIA) deployment share. Although task sequences based
    on the Litetouch OEM task sequence template can be selected from other
    deployment shares, the task sequence will not finish successfully.

7. On the Computer Details page, in the Computer name box, type computer_name
  (where computer_name is the computer name to assign to the target computer),
  select one of the options listed in Table 92 based on your environment's
  requirements and then select Next.

  This wizard appears when the conditions in Table 91 are met.

  Table 91. Configure the Computer Details Page
  Conditions

                                                                          ﾉ   Expand table

   Property                      Condition

   SkipComputerName              Not equal to YES

<!-- p.243 -->

   Property                      Condition

   SkipDomainMembership          Not equal to YES

   DeploymentType                Not equal to StateRestore or REPLACE or CUSTOM

   DeploymentType                Not equal to REPLACE

  Table 92. Specify Computer Membership
  Configuration

                                                                           ﾉ   Expand table

   For this      Perform this task to
   option

   Join a        Join an existing AD DS domain:
   domain
                 - In the Domain to join box, type domain (where domain is the name of the
                 domain to be joined).

                 - In the Organizational Unit box, type organizational_unit (where
                 organizational_unit is the name of the organizational unit [OU] in the AD DS
                 domain in which the computer account will be created).

                 - In the User Name box, type user_name (where user_name is the name of a
                 user account that has sufficient permissions to create the computer account
                 in the domain).

                 - In the Password box, type password (where password is the password for
                 the user account specified in the User Name box).

                 - In the Domain box, type domain (where domain is the name of the
                 domain in the user account specified in the User Name box is located).

   Join a        Join a Windows workgroup:
   workgroup
                 - In the Workgroup box, type workgroup (where workgroup is the name of
                 the workgroup to join).

  The User Data page is displayed.

8. On the User Data page, select one of the options listed in Table 94 based on your
  environment's requirements, and then select Next.

  This wizard appears when the conditions in Table 93 are met.

<!-- p.244 -->

  Table 93. User Data Page Conditions

                                                                              ﾉ   Expand table

   Property                 Condition

   SkipUserData             Not equal to YES

   DeploymentType           Not equal to REFRESH or REPLACE or StateRestore

   ImageFlags               Does not contain SERVER

   IsServerOS               Not equal to TRUE

  Table 94. User Data Page Options

                                                                              ﾉ   Expand table

   Option                   Select this option to

   Automatically            - Allow the MDT scripts and process rules to automatically
   determine the location   determine the best location based on local available disk space
                            on the target computer.

                            - Optionally, select the Allow data and settings to be stored
                            locally when possible check box to give preference to storing the
                            data locally.

   Specify a location       Save the user state migration data to a specific location.

                            In the Location box, type location (where location is the fully
                            qualified path to the locations for storing the user state migration
                            data).

                            Alternatively, select Browse to go to the location.

   Do not save data and     Discard any existing user state migration data or deploy a new
   settings                 computer with no existing data.

  The Move Data and Settings page is displayed.

9. On the Move Data and Settings page, select one of the options listed in Table 96
  based on your environment's requirements, and then select Next.

  This wizard appears when the conditions in Table 95 are met.

  Table 95. Move Data and Settings Page Conditions

<!-- p.245 -->

                                                                            ﾉ   Expand table

Property                 Condition

SkipUserData             Not equal to YES

DeploymentType           Equal to NEWCOMPUTER

ImageFlags               Does not contain SERVER

IsServerOS               Not equal to TRUE

FindTaskSequenceStep     Task sequence includes Offline User State Capture and
                         ZTIUserState.wsf

Table 96. Move Data and Settings Page Options

                                                                            ﾉ   Expand table

Option         Select this option to

Do not         Install the new operating system without capturing any user data or settings
move user      from any existing operating systems. This option sets the
data and       USMTOfflineMigration property to "FALSE".
settings
               Optionally, select the Keep existing partitionscheck box to give preference
               to storing the data locally. If the check box is:

               - Selected, then the new operating system is installed on the existing
               partitions. This option sets the DoNotFormatAndPartition property to "YES".

               - Cleared, then the target computer is partitioned and formatted and the
               target operating system is installed on the new partition structure. This
               option does not set the DoNotFormatAndPartition property.

               The Keep existing partitionscheck box is disabled for the MDT New
               Computer deployment scenario because no existing partitions exist.

Move user      Capture the user data and settings from an existing operating system and
data and       restore them into the new operating system. This option sets the:
settings
               - DoNotFormatAndPartition property to "YES".

               - USMTOfflineMigration property to "TRUE".

               Optionally, if the target computer has multiple operating systems installed,
               the Select the partition that contains the operating system and data group
               of options is displayed. There is an option for each partition that contains an

<!-- p.246 -->

    Option           Select this option to

                     operating system. Select the partition that contains the user state migration
                     data that you want to capture.

   The User Data (Restore) page is displayed.

10. On the User Data (Restore) page, select one of the options listed in Table 98 based
   on your environment's requirements, and then select Next.

   This wizard appears when the conditions in Table 97 are met.

   Table 97. User Data (Restore) Page Conditions

                                                                                  ﾉ   Expand table

    Property              Condition

    SkipUserData          Not equal to YES

    DeploymentType        Equal to NEWCOMPUTER or StateRestore and not equal to CUSTOM

    ImageFlags            Does not contain SERVER

    IsServerOS            Not equal to TRUE

   Table 98. User Data (Restore) Options

                                                                                  ﾉ   Expand table

    Option                Select this option if

    Do not restore        The migration type is New Computer and there is no user state
    user data and         migration data to restore.
    settings

    Specify a location    The migration type is Replace Computer.In the Location box, type
                          location (where location is the fully qualified path to the location in
                          which the user state migration back files are stored).

11. On the Computer Backup page, select one of the options listed in Table 100 based
   on requirements, and then select Next.

   This wizard appears when the conditions in Table 99 are met.

   Table 99. Computer Backup Page Conditions

<!-- p.247 -->

                                                                           ﾉ   Expand table

 Property                 Condition

 SkipComputerBackup       Not equal to YES

 DeploymentType           Not equal to NEWCOMPUTER and not equal to CUSTOM and not
                          equal to STATERESTORE and equal to REFRESH or equal to
                          REPLACE

Table 100. Computer Backup Options

                                                                           ﾉ   Expand table

 Option                    Select this option to

 Automatically             - Allow the MDT scripts and process rules to automatically
 determine the location    determine the best location based on local available disk space
                           on the target computer.

                           - Optionally, select the Allow data and settings to be stored
                           locally when possible check box to give preference to storing the
                           data locally.

 Specify a location        Save the computer image backup to a specific location.

                           In the Location box, type location (where location is the fully
                           qualified path to the locations for storing the computer backup).

 Do not back up the        Discard any existing data on the target computer or deploy a
 existing computer         new computer with no existing data.

The Deployment Wizard uses the ImageX utility to perform the backup. ImageX is
not intended to be used as a part of the overall backup and disaster recovery
process. Instead, it is designed to create a backup of the target computer to assist
in recovering user state migration information that might not have been captured
correctly.

  ７ Note

  MDT uses the ImageX utility during migration because it works on all
  platforms that MDT supports. Use tools such as Windows Backup for
  enhanced disaster recovery protection after migration is complete.

<!-- p.248 -->

12. On the Product Key page, in the Product key box, type product_key (where
   product_key is the product key to be assigned to the target computer), and then
   select Next (see Table 102).

   This wizard appears when the conditions in Table 101 are met.

   Table 101. Product Key Page Conditions

                                                                                ﾉ   Expand table

    Property           Condition

    SkipProductKey     Not equal to YES.

    DeploymentType     Not equal to REPLACE and not equal to CUSTOM and not equal to
                       StateRestore.

   Table 102. Product Key Options

                                                                                ﾉ   Expand table

    Option                          Select this option to

    No product key is required      Assign product keys to target computers using a KMS
                                    key.

    Activate the machine with a     Assign a MAK to the target computer and activate the
    Multiple Activation Key (MAK)   computer over the Internet.

                                    In the Multiple activation key box, type mak (where mak
                                    is the MAK to be assigned to the target computer).

    Use a specific product key      Assign a specific license key for installation or retail
                                    activation.

                                    In the Product_key box, type product_key (where
                                    product_key is the product key to be assigned to the
                                    target computer).

13. On the Language Packs page, in the Select the language packs to install box,
   select the check box next to language_pack (where language_pack is the language
   pack to be installed), and then select Next.

      Tip

<!-- p.249 -->

     You can select multiple language packs by selecting multiple check boxes that
     correspond to the language packs.

   This wizard appears when the conditions in Table 103 are met.

   Table 103. Language Packs Page Conditions

                                                                               ﾉ    Expand table

    Property              Condition

    SkipPackageDisplay    Not equal to YES

    DeploymentType        Not equal to REPLACE or CUSTOM

    ImageBuild            The first character in the property is equal to 6 (which indicates the
                          Windows 7, Windows 8, or Windows 8.1 build), and there are active
                          packages to display to the user.

   For Ultimate, Enterprise, and all editions of Windows Server you can select more
   than one language. For all other Windows editions, select only one language.

14. On the Locale and Time page, select the appropriate values for each option listed
   in Table 105 based on your requirements, and then select Next.

   This wizard appears when the conditions in Table 104 are met.

   Table 104. Locale and Time Page Conditions

                                                                               ﾉ    Expand table

    Property              Condition

    SkipLocaleSelection   Not equal to YES.

    DeploymentType        Not equal to REPLACE or CUSTOM.

    ImageBuild            The first character in the property is equal to 6 (which indicates the
                          Windows 7, Windows 8, or Windows 8.1 build).

   Table 105. Locale and Time Options

                                                                               ﾉ    Expand table

<!-- p.250 -->

    In this box                       Select

    Language to install               The default language for the target operating system.

    Time and currency format          The default locale for the target operating system.
    (Locale)

    Keyboard layout                   Keyboard layout to be used with the target operating
                                      system.

    Time zone                         The time zone in which the target computer is located.

15. On the Roles and Features page, select the appropriate values for each option
   listed in Table 107 based on your requirements, and then select Next.

   This wizard appears when the conditions in Table 106 are met.

   Table 106. Roles and Features Page Conditions

                                                                              ﾉ   Expand table

    Property                   Condition

    SkipRoles                  Not equal to YES.

    FindTaskSequenceStep       Task sequence includes BDD_InstallRoles and ZTIOSRole.wsf

    OSVersion                  Not equal to WinPE.

    ImageBuild                 Not Null.

   Table 107. Roles and Features Options

                                                                              ﾉ   Expand table

    In this box                    Select

    The following roles and role   The check boxes that correspond to the desired Windows
    services are available         roles, role services, or features.

    Select All                     Select this button to select all the check boxes associated
                                   with the Windows roles, role services, or features.

    Select None                    Select this button to deselect all the check boxes
                                   associated with the Windows roles, role services, or
                                   features.

<!-- p.251 -->

16. On the Applications page, select the check box next to application_name (where
   application_name is the name of the application you want to deploy, and then
   select Next.

      Tip

     You can select multiple applications by selecting multiple check boxes that
     correspond to the applications.

   This wizard appears when the conditions in Table 108 are met.

   Table 108. Applications Page Conditions

                                                                           ﾉ    Expand table

    Property                                                 Condition

    SkipApplications                                         Not equal to YES

    DeploymentType                                           Not equal to REPLACE

    IsThereAtLeastOneApplicationPresent                      Greater than one

17. On the Administrator Password page, in the Administrator Password and Confirm
   Administrator Password boxes, type password (where password is the password
   for the local built-in Administrator account on the target computer), and then
   select Next.

   This wizard page appears when the conditions in Table 109 are met.

   Table 109. Administrator Password Page Conditions

                                                                           ﾉ    Expand table

    Property                              Condition

    SkipAdminPassword                     Not equal to YES

    DeploymentType                        Not equal to REPLACE or CUSTOM

    TaskSequenceTemplate                  Not equal LTIOEM.XML

18. On the Local Administrators page, in the Administrator Accountsbox, type
   admin_accounts (where admin_accounts are the accounts that you want to add to

<!-- p.252 -->

   the local built-in Administrator account on the target computer), and then select
   Next.

   This wizard page appears when the conditions in Table 109 and Table 110 are met.

   Table 110. Local Administrators Page Conditions

                                                                       ﾉ   Expand table

    Property                  Condition

    SkipAdminAccounts         Not equal to YES

    DeploymentType            Not equal to REPLACE and not equal to CUSTOM

    JoinDomain                Not equal to ""

     ７ Note

     Unlike other Deployment Wizard pages, the Administrator Accounts page is
     skipped by default, because the default value for the SkipAdminAccount
     property is YES. For more information, see the SkipAdminAccounts property
     in the MDT document Toolkit Reference.

19. On the Capture Image page, select one of the options listed in Table 112 based on
   requirements, and then select Next.

   This wizard appears when the conditions in Table 111 are met.

   Table 111. Capture Image Page Conditions

                                                                       ﾉ   Expand table

    Property                Condition

    SkipCapture             Not equal to YES

    DeploymentType          Not equal to REFRESH or not equal to REPLACE

    JoinDomain              Equal to ""

   Table 112. Capture Image Options

<!-- p.253 -->

                                                                                 ﾉ   Expand table

    Option                 Select this option to

    Capture an image       Run Sysprep, and then capture an image of the target computer.
    of this reference      Then, store the image in the location specified.
    computer
                           In the Location box, type location (where location is the fully
                           qualified path to the location for storing the image of the target
                           computer).In the File name box, type file_name (where file_name is
                           the name of the image file).

    Sysprep this           Copy the required Sysprep files to the target computer, initiate
    computer               Sysprep, but do not capture an image of the target computer.

    Prepare to capture     Copy the required Sysprep files to the target computer, but do not
    the machine            initiate Sysprep.

    Do not capture an      Deploy the target operating system to the target computer without
    image of this          capturing a Sysprep image of the computer.
    computer

20. On the BitLocker page, select one of the options listed in Table 114 based on your
   environment's requirements, and then select Next.

   This wizard appears when the conditions in Table 113 are met.

   Table 113. BitLocker Page Conditions

                                                                                 ﾉ   Expand table

    Property             Condition

    SkipBitLocker        Not equal to YES.

    DeploymentType       Equal to REPLACE or CUSTOM.

    DoCapture            Not equal to YES or not equal to PREPARE.

    ImageBuild           The first character in the property is equal to 6 (which indicates an
                         operating system that is Windows Vista or later).

    ImageFlags           Equal to ENTERPRISE or ULTIMATE.

   Table 114. BitLocker Configuration Options

                                                                                 ﾉ   Expand table

<!-- p.254 -->

    Option               Select this option to

    Do not enable        Deploy the new operating system without activating BitLocker.
    BitLocker for this
    computer

    Enable BitLocker     Activate BitLocker and use TPM version 1.2 or later. Then, select one of
                         the following options for using TPM:

                         - To use TPM only, select Enable BitLocker using TPM only.

                         - To use TPM with a PIN, select Enable BitLocker using TPM and a PIN;
                         in the Pin box, type pin (where pin is the BitLocker PIN for the target
                         computer).

                         The value provided can be numeric only or alphanumeric depending
                         on the value of the BDEAllowAlphaNumericPin property.

                         - To use TPM with a startup key, select Enable BitLocker using TPM
                         and a startup key; in the box, select the drive on which the startup key
                         resides.

                         - To use only an External Startup Key, select Enable BitLocker using
                         only an External Startup Key; in the box, select the drive on which the
                         external startup key resides.

                         - To store the recovery key in AD DS, under Choose where to store the
                         Recovery Key, select In Active Directory.

                         - To not create a recovery key, under Choose where to store the
                         Recovery Key, select Do not create a recovery key.

                         - To configure the deployment process to wait until encryption is
                         complete on all drives before continuing, select the Wait for BitLocker
                         Encryption to complete on all drives before continuing check box.

     ７ Note

     The default setting for BitLocker is disabled.

21. Review the information on the Ready to begin page, and then select Begin.

     ７ Note

     To expand the details of this deployment, select Details.

<!-- p.255 -->

     The Deployment Wizard closes, and deployment of the new operating system
     begins.

Performing ZTI Deployments Using
Configuration Manager
You perform ZTI deployments using Configuration Manager and MDT within an AD DS
domain, within a Windows workgroup, or from removable media. Perform ZTI
deployments by:

     Preparing the ZTI deployment environment as described in Preparing the ZTI
     Deployment Environment for Configuration Manager

     Preparing for ZTI deployment to the reference computer as described in Preparing
     for ZTI Deployment to the Reference Computer Using Configuration Manager

     Deploying to and capturing an image of the reference computer in ZTI as
     described in Deploying To and Capturing an Image of the Reference Computer
     Using Configuration Manager

     Preparing for ZTI deployment to the target computers as described in Preparing
     for ZTI Deployment to Target Computers Using Configuration Manager

     Deploying captured images to the target computer in ZTI as described in
     Deploying Captured Images to Target Computers Using Configuration Manager

Preparing the ZTI Deployment Environment for
Configuration Manager
After you have prepared the prerequisite infrastructure for MDT, you are ready to
prepare the MDT deployment environment for ZTI.

To prepare the MDT deployment environment for ZTI deployments

   1. Preparing the prerequisite infrastructure as described in Prepare the Prerequisite
     ZTI Infrastructure for Use with Configuration Manager.

   2. Install a new instance of MDT on the deployment server, or upgrade an existing
     instance of MDT to MDT as described in Install or Upgrade to MDT for the ZTI
     Deployment Process Using Configuration Manager.

<!-- p.256 -->

   3. Obtain the software that ZTI requires as described in Obtain the Software That the
     ZTI Deployment Process Using Configuration Manager Requires.

   4. Enable Configuration Manager console integration with MDT as described in
     Enable Configuration Manager Console Integration for Configuration Manager.

Prepare the Prerequisite ZTI Infrastructure for Use with
Configuration Manager
ZTI deployments using Configuration Manager require that a properly configured
Configuration Manager infrastructure exist prior to installing MDT and performing
deployments. Ensure that your new or existing Configuration Manager infrastructure is
specifically optimized for the Operating System Deployment feature.

  ７ Note

  Windows PowerShell version 2.0 or later must be installed on any computer on
  which MDT is installed for management of ZTI deployments.

For more information about:

     Hardware and software requirements for Configuration Manager, see Supported
     Configurations for Configuration Manager

     Configuring a Configuration Manager infrastructure to support ZTI deployments,
     see the section, "Step 1: Prepare the Prerequisite Infrastructure", in the MDT
     document Quick Start Guide for Microsoft System Center 2012 R2 Configuration
     Manager.

Install or Upgrade to MDT for the ZTI Deployment Process Using
Configuration Manager

The first step in performing ZTI deployments is to have at least one instance of MDT
running in your environment. Install MDT on each computer that has the Configuration
Manager console installed and that you will use to create or edit task sequences that
MDT generates. If your existing environment has:

     No computers currently running MDT or a previous version of MDT, install one or
     more new instances of MDT as described in Installing a New Instance of MDT.

     One or more computers running a previous version of MDT, upgrade those
     instances to MDT as described in Upgrading to MDT. After the upgrade process is

<!-- p.257 -->

     complete:

        Run the Configure ConfigMgr Integration Wizard. This wizard must be run
        after the upgrade to register the new components and install the ZTI new task
        sequence templates.

        Run the Remove PXE Filter Wizard. If you had previously installed and
        configured the PXE filter to support the unknown computer capability in
        previous versions of MDT. This support is now provided in Configuration
        Manager and has been removed in MDT.

        Ensure you create a new Microsoft Deployment Toolkit Files package for any
        new ZTI task sequences you create. The existing Microsoft Deployment Toolkit
        Files package can be used for any ZTI task sequences created prior to the
        upgrade, but a new Microsoft Deployment Toolkit Files package must be
        created for new ZTI task sequences.

        Ensure any ZTI task sequences created prior to the upgrade use the Microsoft
        Deployment Toolkit Files package that existed prior to the upgrade. You can
        modify these ZTI task sequences, but you cannot use any of the new MDT task
        sequence actions or steps. To use the new MDT task sequence actions or steps,
        create a new ZTI task sequence.

           ７ Note

           If you upgraded from a previous version of Configuration Manager, you
           can use ZTI task sequences for MDT that were created in the previous
           version of Configuration Manager as long as they were created using the
           same version of MDT.

Obtain the Software That the ZTI Deployment Process Using
Configuration Manager Requires

Collect the software needed during the ZTI deployment process for Configuration
Manager. This software will be imported or added to deployment shares unless it
already exists in the deployment share.

  ７ Note

  MDT supports the Windows ADK for Windows 8.1, Windows PE 5.0, and System
  Center 2012 R2 Configuration Manager.

<!-- p.258 -->

Required software includes:

        Operating system source files for each operating system to be deployed to the
        reference and target computers

        Operating system packages for the operating systems, such as security updates,
        feature packs, and language packs

        Device drivers for the reference and target computers that are not included as part
        of the operating system

        Applications that are to be installed as a part of the operating system image or
        during the deployment of the reference image

        USMT source files used to create a software package that is deployed to the target
        computers to capture user state migration data

Enable Configuration Manager Console Integration for
Configuration Manager

Before you can use the Configuration Manager integration features of MDT, run the
Configure ConfigMgr Integration Wizard. This wizard copies the appropriate
Configuration Manager integration files to the Configuration Manager_root (where
Configuration Manager_root is the folder in which the Configuration Manager console is
installed).

The wizard also adds WMI classes for the new MDT custom actions. You add these
classes by compiling a Managed Object Format (.mof) file that contains the new class
definitions.

To run the Configure ConfigMgr Integration Wizard

   1.     ７ Note

          The Configuration Manager console should be closed when performing this
          procedure.

        Select Start, and then point to All Programs. Point to Microsoft Deployment
        Toolkit, and then select Configure ConfigMgr Integration.

        The Configure ConfigMgr Integration Wizard starts.

<!-- p.259 -->

   2. Complete the Configure ConfigMgr Integration Wizard using the information in
     Table 115. Accept the default values unless otherwise specified.

     Table 115. Information for Completing the Configure
     ConfigMgr Integration Wizard

                                                                                ﾉ   Expand table

      On this wizard    Do this
      page

      Options           - Verify that the Install the MDT extensions for Configuration Manager
                        option is selected.

                        - Verify that the Install the MDT console extensions for System Center
                        2012 R2 Configuration Manager check box is selected.

                        - Verify that the Add the MDT task sequence actions to a System Center
                        2012 R2 Configuration Manager server check box is selected.

                        - In Site Server Name, type ConfigMgr_server_name (where
                        ConfigMgr_server_name is the name of the Configuration Manager server
                        on which to install MDT integration).

                        - In Site Code, type ConfigMgr_site_code (where ConfigMgr_site_code is
                        the Configuration Manager site code that installs MDT integration), and
                        then select Next.

                        The Site Server Name and Site Code fields will be automatically
                        populated with the most recent connection details if the Configuration
                        Manager console has been opened once.

      Confirmation      Review the completion status of the wizard, and then select Finish.

     When the wizard finishes, the Configuration Manager console is configured for
     MDT integration.

Preparing for ZTI Deployment to the Reference Computer
Using Configuration Manager
Regardless of the ZTI deployment scenario you are performing, always start by creating
a reference computer, and then capturing an image of that computer. Later in the ZTI
deployment process, you will deploy the captured image of your reference computer to
the appropriate target computers.

<!-- p.260 -->

Create a reference computer for each image that you want to create for deployment to
the target computers. For more information about determining the number of images
required in your organization (and subsequently the number of reference computers
required), see Estimate Storage Requirements for Configuration Manager Distribution
Points. For more information about the use of reference computers in MDT
deployments, see Using Reference Computers in MDT Deployments.

To prepare for deployment to the reference computer using
Configuration Manager

  1. Create a new task sequence that will deploy the target operating system to the
     reference computer using the Create MDT Task Sequence Wizard in the
     Configuration Manager console as described in Creating a ZTI Task Sequence
     Using MDT Task Sequence Templates in Configuration Manager.

        Tip

       Create the task sequence for deploying to the reference computer based on
       the Client Task Sequence or Server Task Sequence template included in MDT.

  2. Configure Configuration Manager to contain the appropriate software for
     deployment to the reference computer, including the following:

          Configuring applications and operating system packages as described in
          Managing Software Packages in Configuration Manager

          Configuring device drivers as described in Managing Device Drivers in
          Configuration Manager

  3. Ensure that the distribution points for the packages and operating system images
     that the new ZTI task sequence uses are distributed properly as described in
     Managing Distribution Points in Configuration Manager.

       ７ Note

       Most production networks have multiple distribution points. When
       performing this step in a production environment, select the appropriate
       distribution points for the network.

  4. Customize the MDT configuration files to the needs of your organization as
     described in Configuring MDT Deployments.

<!-- p.261 -->

        ） Important

        If you are capturing an image of the reference computer, you must at least
        add the DoCapture property to the Customsettings.ini file for the task
        sequence by specifying DoCapture=YES or DoCapture=SYSPREP .

   5. Optionally, enable monitoring of the MDT deployment process as described in
     Monitoring MDT Deployments.

   6. Customize the task sequence to the needs of your organization as described in
     Configuring ZTI Task Sequence Steps in Configuration Manager.

        ７ Note

        The ZTI deployment process is unable to perform Sysprep operations on a
        target computer that is encrypted by using BitLocker Drive Encryption. Do not
        enable BitLocker on the reference computer, and enable BitLocker on the
        target computers only after the target operating system is completely
        deployed.

   7. Update the distribution points so that any changes to the packages are distributed
     properly as described in Managing Distribution Points in Configuration Manager.

        ７ Note

        Most production networks have multiple distribution points. When
        performing this step in a production environment, select the appropriate
        distribution points for the network.

Deploying To and Capturing an Image of the Reference
Computer Using Configuration Manager
After the distribution points are updated, advertise the task sequence to the reference
computer and start the reference computer with the bootable Windows PE image
created earlier in the process. The task sequence created earlier will deploy the target
operating system, device drivers, operating system packages, and applications to the
reference computer, and then capture an image of the reference computer.

To deploy to and capture an image of the reference computer

<!-- p.262 -->

  1. Add the reference computer to the Configuration Manager site database as
     described in Manually Adding Computers to the Site Database in Configuration
     Manager.

  2. Create a collection that contains the reference computer as described in Managing
     Computer Collections in Configuration Manager.

  3. Deploy the task sequence to the reference computer as described in Managing
     Task Sequence Deployment in Configuration Manager.

  4. Create a task sequence bootable media disk by using the Task Sequence Media
     Wizard as described in Creating Task Sequence Bootable Media in Configuration
     Manager.

  5. Start the reference computer with the task sequence bootable media disk as
     described in Deploying an Operating System Using Task Sequence Bootable Media
     in Configuration Manager.

  6. Optionally, monitor the deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

Preparing for ZTI Deployment to Target Computers Using
Configuration Manager
After the images of the reference computers are captured, deploy them to the target
computers. In preparation for deploying the captured images to the target computers,
create one or more task sequences for deploying the captured images, ensure that the
necessary deployment resources exist, and customize the MDT deployment process.

To prepare for ZTI deployment to target computers

  1. Prepare network shares for storing migration data and MDT deployment logs as
     described in Preparing the MDT Migration Resources.

  2. Optionally, prepare Windows Deployment Services to start the appropriate
     Windows PE images that will in turn start the ZTI deployment process to the target
     computers as described in Preparing Windows Deployment Services for ZTI
     Deployments Using Configuration Manager.

  3. Create additional distribution points to help in larger deployments as described in
     Managing Distribution Points in Configuration Manager.

<!-- p.263 -->

   4. Prepare the ZTI task sequences, the MDT configuration files, and the MDT DB for
     each deployment scenario as described in the following:

            Prepare for the ZTI New Computer Deployment Scenario to Target
            Computers Using Configuration Manager

            Prepare for the ZTI Refresh Computer Deployment Scenario to Target
            Computers Using Configuration Manager

            Prepare for the ZTI Replace Computer Deployment Scenario to Target
            Computers Using Configuration Manager

     Depending on the target computers in your organization, any combination of
     these deployments scenarios might be necessary. For more information about
     MDT deployment scenarios, see Identifying Deployment Scenarios.

Prepare for the ZTI New Computer Deployment Scenario to Target
Computers Using Configuration Manager

In the New Computer deployment scenario, you deploy a new installation of a Windows
operating system to a new computer. There is no user migration information to save
and restore and no existing file systems to preserve. Use the Client Task Sequence
template to deploy the captured image of the reference computer to the target
computer.

To prepare for the New Computer deployment scenario to target
computers

   1. Create a new task sequence that will deploy the target operating system to the
     reference computer using the Create MDT Task Sequence Wizard in the
     Configuration Manager console as described in Creating a ZTI Task Sequence
     Using MDT Task Sequence Templates in Configuration Manager, but ensure that
     you specifically follow the configuration settings on the wizard pages listed in
     Table 116 and select the appropriate values on the other wizard pages based on
     your organization's requirements.

        Tip

       Create the task sequence for deploying to the reference computer based on
       the Client Task Sequence or Server Task Sequence template included in MDT.

<!-- p.264 -->

  Table 116. Information for Completing the Create MDT
  Task Sequence Wizard for Performing New Computer
  Deployment Scenario Using ZTI

                                                                         ﾉ   Expand table

   On this wizard   Do this
   page

   OS Image         Select Create a new OS image, and specify the fully qualified UNC path
                    to the WIM image captured from the reference computer.

   Deployment       Select Perform a "Zero Touch Installation" OS deployment, with no
   Method           user interaction.

2. Configure Configuration Manager to contain the appropriate software for
  deployment to the target computer, including:

       Configuring applications and operating system packages as described in
       Managing Software Packages in Configuration Manager

       Configuring device drivers as described in Managing Device Drivers in
       Configuration Manager

3. Customize the MDT configuration files to the needs of your organization as
  described in Configuring MDT Deployments.

4. Optionally, customize the MDT DB to the needs of your organization as described
  in Performing Deployments Using the MDT DB (if you are using the MDT DB to
  provide MDT configuration information).

5. Optionally, enable monitoring of the MDT deployment process as described in
  Monitoring MDT Deployments.

6. Customize the task sequence to the needs of your organization as described in
  Configuring ZTI Task Sequence Steps in Configuration Manager.

7. Ensure that the distribution points for the packages and operating system images
  that the new ZTI task sequence uses are distributed properly as described in
  Managing Distribution Points in Configuration Manager.

    ７ Note

    Most production networks have multiple distribution points. When
    performing this step in a production environment, select the appropriate

<!-- p.265 -->

       distribution points for the network.

   8. Update the distribution points so that any changes to the packages are distributed
     properly as described in Managing Distribution Points in Configuration Manager.

       ７ Note

       Most production networks have multiple distribution points. When
       performing this step in a production environment, select the appropriate
       distribution points for the network.

Prepare for the ZTI Refresh Computer Deployment Scenario to
Target Computers Using Configuration Manager
In the Refresh Computer deployment scenario, a computer is refreshed, including
computers that must be re-imaged for image standardization or to address a problem.
There is user migration information to save and restore but no existing file systems to
preserve. Use the Client Task Sequence template to deploy the captured image of the
reference computer to the target computer.

To prepare for the Refresh Computer deployment scenario to target
computers

   1. Create a new task sequence that will deploy the target operating system to the
     reference computer using the Create MDT Task Sequence Wizard in the
     Configuration Manager console as described in Creating a ZTI Task Sequence
     Using MDT Task Sequence Templates in Configuration Manager, but ensure that
     you follow the configuration settings on the wizard pages listed in Table 117 and
     select the appropriate values on the other wizard pages for your organization's
     requirements.

        Tip

       Create the task sequence for deploying to the reference computer based on
       the Client Task Sequence or Server Task Sequence template included in MDT.

     Table 117. Information for Completing the Create MDT
     Task Sequence Wizard for Performing New Computer

<!-- p.266 -->

  Deployment Scenario Using ZTI

                                                                         ﾉ   Expand table

   On this wizard   Do this
   page

   OS Image         Select Create a new OS image, and specify the fully qualified UNC path
                    to the WIM image captured from the reference computer.

   Deployment       Select Perform a "Zero Touch Installation" OS deployment, with no
   Method           user interaction.

2. Configure the appropriate software for deployment to the target computer in the
  Configuration Manager Console, including:

       Configuring applications and operating system packages as described in
       Managing Software Packages in Configuration Manager

       Configuring device drivers as described in Managing Device Drivers in
       Configuration Manager

3. Optionally, customize the MDT configuration files or the MDT DB to the needs of
  your organization as described in:

       Configuring MDT Deployments

       Performing Deployments Using the MDT DB

4. Optionally, enable monitoring of the MDT deployment process as described in
  Monitoring MDT Deployments.

5. Customize the task sequence to the needs of your organization as described in
  Configuring ZTI Task Sequence Steps in Configuration Manager.

6. Ensure that the distribution points for the packages and operating system images
  that the new ZTI task sequence uses are distributed properly as described in
  Managing Distribution Points in Configuration Manager.

    ７ Note

    Most production networks have multiple distribution points. When
    performing this step in a production environment, select the appropriate
    distribution points for the network.

<!-- p.267 -->

   7. Update the distribution points so that any changes to the packages are distributed
     properly as described in Managing Distribution Points in Configuration Manager.

        ７ Note

        Most production networks have multiple distribution points. When
        performing this step in a production environment, select the appropriate
        distribution points for the network.

Prepare for the ZTI Replace Computer Deployment Scenario to
Target Computers Using Configuration Manager

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

     Client Replace Task Sequence template to save the user state migration of the
     existing target computer

        ） Important

        Run this task sequence before running the task sequence based on the Client
        Task Sequence template on the new target computer.

     Client Task Sequence template to deploy the captured image of the reference
     computer to the new target computer and restore the user state migration data

        ） Important

<!-- p.268 -->

      Run this task sequence after running the task sequence based on the Client
      Replace Task Sequence template on the existing target computer.

To prepare for the Replace Computer deployment scenario to target
computers

  1. Create a computer association between the existing target computer and the new
    target computer as described in the subsection, "How to Perform a Side-by-Side
    Operating System Deployment," in the section, "How to Deploy Operating Systems
    in Configuration Manager," in the Configuration Manager Documentation Library,
    which is installed with Configuration Manager.

  2. Create a new task sequence that will save the user state migration data of the
    existing target computer as described in Creating a ZTI Task Sequence Using MDT
    Task Sequence Templates in Configuration Manager.

       Tip

      Create the task sequence for capturing the user state migration data from the
      target computer based on the Client Task Replace Sequence template
      included in MDT.

  3. Create a new task sequence that will deploy the captured image of the reference
    computer to the target computer, and restore the user state migration data saved
    by the Client Replace Task Sequence as described in Creating a ZTI Task Sequence
    Using MDT Task Sequence Templates in Configuration Manager, but ensure that
    you specifically follow the configuration settings on the wizard pages listed in
    Table 118 and select the appropriate values on the other wizard pages for your
    organization's requirements.

       Tip

      Create the task sequence for deploying to the target computer based on the
      Client Task Sequence template included in MDT.

    Table 118. Information for Completing the Create MDT
    Task Sequence Wizard for Performing the ZTI Replace
    Computer Deployment Scenario

<!-- p.269 -->

                                                                         ﾉ   Expand table

   On this wizard   Do this
   page

   OS Image         Select Create a new OS image, and specify the fully qualified UNC path
                    to the WIM image captured from the reference computer.

   Deployment       Select Perform a "Zero Touch Installation" OS deployment, with no
   Method           user interaction.

4. Configure the appropriate software for deployment to the target computer in the
  Configuration Manager Console, including:

       Configuring applications and operating system packages as described in
       Managing Software Packages in Configuration Manager

       Configuring device drivers as described in Managing Device Drivers in
       Configuration Manager

5. Customize the MDT configuration files or the MDT DB to the needs of your
  organization as described in:

       Configuring MDT Deployments

       Performing Deployments Using the MDT DB

6. Optionally, enable monitoring of the MDT deployment process as described in
  Monitoring MDT Deployments.

7. Customize the task sequences to the needs of your organization as described in
  Configuring ZTI Task Sequence Steps in Configuration Manager.

8. Ensure that the distribution points for the packages and operating system images
  that the new ZTI task sequence uses are distributed properly as described in
  Managing Distribution Points in Configuration Manager.

    ７ Note

    Most production networks have multiple distribution points. When
    performing this step in a production environment, select the appropriate
    distribution points for the network.

9. Update the distribution points so that any changes to the packages are distributed
  properly as described in Managing Distribution Points in Configuration Manager.

<!-- p.270 -->

       ７ Note

       Most production networks have multiple distribution points. When
       performing this step in a production environment, select the appropriate
       distribution points for the network.

Deploying Captured Images to Target Computers Using
Configuration Manager
The deployment of the captured images to the target computers is slightly different for
each MDT deployment scenario using ZTI. Deploy the captured image of the reference
computer to target computers for each respective deployment scenario in your
organization.

To deploy the capture image of the reference computer to the
target computers

   1. Add the target computer to the Configuration Manager site database:

          Manually, as described in Manually Adding Computers to the Site Database
          in Configuration Manager

          Automatically as described in the section, "How to Manage Unknown
          Computer Deployments in Configuration Manager," in the Configuration
          Manager Documentation Library, which is installed with Configuration
          Manager

   2. Create a collection that contains the target computers as described in Managing
     Computer Collections in Configuration Manager.

       ７ Note

       Create a collection for each MDT deployment scenario to be performed, and
       ensure that the collection includes the target computers requiring the
       corresponding deployment scenario.

   3. Deploy the task sequence to the target computers as described in Managing Task
     Sequence Deployment in Configuration Manager.

   4. Provide a method for starting the target computers by doing any combination of
     the following:

<!-- p.271 -->

          Create a task sequence bootable media disk using the Task Sequence Media
          Wizard as described in Creating Task Sequence Bootable Media in
          Configuration Manager.

          Prepare Windows Deployment Services to start the appropriate Windows PE
          images that will in turn start the ZTI deployment process to the target
          computers as described in Preparing Windows Deployment Services for ZTI
          Deployments Using Configuration Manager.

   5. Deploy the captured reference computer image to the target computers for each
     deployment scenario as described in:

          Deploy Captured Images to Target Computers in the ZTI New Computer
          Deployment Scenario Using Configuration Manager

          Deploy Captured Images to Target Computers in the ZTI Refresh Computer
          Deployment Scenario Using Configuration Manager

          Deploy Captured Images to Target Computers in the Replace Computer
          Deployment Scenario Using Configuration Manager

          Depending on the target computers in your organization, any combination of
          deployments scenarios might be necessary. For more information about the
          MDT deployment scenarios, see Identifying Deployment Scenarios.

Deploy Captured Images to Target Computers in the ZTI New
Computer Deployment Scenario Using Configuration Manager

Start the target computer with the task sequence bootable media created earlier in the
process or from Windows Deployment Services. Either method starts Windows PE on the
target computer and initiates the ZTI deployment process. At the end of the process, the
captured image of the reference computer is deployed on the target computer.

To deploy the capture images to the target computers in the ZTI New
Computer Deployment Scenario using Configuration Manager

   1. Start the target computer with the task sequence bootable media created earlier in
     the process or from Windows Deployment Services.

     The Task Sequence Wizard starts.

   2. Complete the Task Sequence Wizard, ensuring that you specifically follow the
     configuration settings on the wizard pages listed in Table 119 and select the
     appropriate values on the other wizard pages for your organization's requirements.

<!-- p.272 -->

        ７ Note

        This wizard will not appear if you configure ZTI to perform a PXE boot and
        have configured a mandatory advertisement or if only one task sequence is
        advertised to the target computer.

     Table 119. Information for Completing the Task
     Sequence Wizard in the ZTI New Computer
     Deployment Scenario Using Configuration Manager

                                                                              ﾉ   Expand table

      On this wizard     Do this
      page

      Select a Task      Select the task sequence you created for the target computer
      Sequence           deployment for the New Computer deployment scenario.

     The wizard starts, and the operating system deployment starts.

   3. Optionally, view the MDT deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

     For more information about monitoring MDT deployments, see View MDT
     Deployment Progress.

Deploy Captured Images to Target Computers in the ZTI Refresh
Computer Deployment Scenario Using Configuration Manager
Start ZTI by running the Configuration Manager task sequence deployment for
capturing the user state migration data that you created earlier in the process. This task
sequence runs in the current operating system on the existing target computer.

To deploy the capture images to the target computers in the Refresh
Computer Deployment Scenario Using ZTI

   1. Run the Configuration Manager advertisement for capturing the Refresh Computer
     deployment scenario that you created earlier in the deployment process.

   2. Optionally, view the MDT deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

<!-- p.273 -->

     For more information about monitoring MDT deployments, see View MDT
     Deployment Progress.

     The task sequence runs in the current operating system to capture user state
     migration data. The task sequence restarts the computer, starts Windows PE, and
     then initiates installation of the new operating system. Finally, the task sequence
     restarts the computer, starts the new operating system, restores the user state
     migration data, installs any packages, installs any applications, and performs any
     other actions configured in the task sequence. The target computer is now
     deployed.

Deploy Captured Images to Target Computers in the Replace
Computer Deployment Scenario Using Configuration Manager
The Replace Computer deployment scenario requires two separate steps to complete
the migration. First, run the advertisement for the task sequence you created to capture
the user state migration data from the existing target computer (old computer). Second,
run the Task Sequence Wizard to deploy the captured image of the reference computer
to the new target computer (new computer) and restore the user state saved earlier in
the process.

To deploy captured images of the reference computer to target
computers

   1. Save the user state migration data from the existing target computer as described
     in Save the User State Migration Data from the Existing Target Computer Using
     Configuration Manager.

   2. Deploy the captured image of the reference computer to the new target computer
     as described in Deploy the Captured Image to the New Target Computer with the
     User State Migration Data from the Existing Computer Using Configuration
     Manager.

Save the User State Migration Data from the Existing Target
Computer Using Configuration Manager

Start the ZTI deployment process by running the Configuration Manager advertisement
for capturing the user state migration data that you created earlier in the process. This
task sequence runs in the current operating system on the existing target computer.

<!-- p.274 -->

To deploy the capture images to the target computers in the Replace
Computer Deployment Scenario Using Configuration Manager

   1. Run the Configuration Manager advertisement for capturing the Refresh Computer
     deployment scenario that you created earlier in the process.

   2. Optionally, view the MDT deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

     For more information about monitoring MDT deployments, see View MDT
     Deployment Progress.

     The task sequence runs in the current operating system to capture user state
     migration data. At the end of the task sequence, the user state migration data of
     the existing target computer is saved to the Configuration Manager state
     migration point.

Deploy the Captured Image to the New Target Computer with the
User State Migration Data from the Existing Computer Using
Configuration Manager

Start the target computer with the ZTI bootable media created earlier in the process or
from Windows Deployment Services. The ZTI bootable media starts Windows PE on the
target computer and initiates the ZTI. At the end of the deployment process, the
captured image of the reference computer is deployed on the target computer, and the
user state migration data is restored from the Configuration Manager state migration
point.

deployment scenario for deploying the captured image

   1. Start the reference computer with the ZTI bootable media created earlier in the
     process or from Windows Deployment Services.

     Windows PE starts, and then the Windows Deployment Wizard starts.

   2. Complete the Task Sequence Wizard, ensuring that you follow the configuration
     settings for the wizard pages listed in Table 120 and select values on the other
     wizard pages for your organization's requirements.

         ７ Note

         This wizard will not appear if you configure ZTI to perform a PXE boot and
         have configured a mandatory advertisement or if only one task sequence is

<!-- p.275 -->

       advertised to the target computer.

     Table 120. Information for Completing the Task
     Sequence Wizard for the Replace Computer
     Deployment Scenario for Deploying the Captured
     Image Using Configuration Manager

                                                                             ﾉ   Expand table

      On this         Do this
      wizard page

      Select a Task   Select the task sequence you created for the target computer deployment
      Sequence        in the Replace Computer deployment scenario to deploy the captured
                      image of the reference computer to the new target computer.

     The wizard starts, and the operating system deployment starts.

   3. Optionally, view the MDT deployment process using the Monitoring node in the
     Deployment Workbench or using the Get-MDTMonitorData cmdlet.

     For more information about monitoring MDT deployments, see View MDT
     Deployment Progress.

     The new target computer is deployed with the user state from the existing target
     computer automatically restored to the new target computer.

Managing ZTI Deployments in the
Configuration Manager Console
You manage ZTI deployments using Configuration Manager through the Configuration
Manager console. You use the Deployment Workbench in ZTI deployments only to
configure the MDT DB. The wizards used to configure ZTI are integrated into the
Configuration Manager console.

Manage ZTI deployments in the Configuration Manager console by:

     Creating a new task sequence for ZTI deployments using the Create MDT Task
     Sequence Wizard as described in Creating a ZTI Task Sequence Using MDT Task
     Sequence Templates in Configuration Manager

<!-- p.276 -->

     Managing operating systems for ZTI deployments in the Configuration Manager
     console as described in Managing Operating Systems in Configuration Manager

     Managing device drivers for ZTI deployments in the Configuration Manager
     console as describe in Managing Device Drivers in Configuration Manager

     Deploying an operating system using task sequence bootable media as described
     in Deploying an Operating System Using Task Sequence Bootable Media in
     Configuration Manager

     Creating task sequence bootable media for ZTI as described in Creating Task
     Sequence Bootable Media in Configuration Manager

     Creating boot images for use with ZTI using the Create Image Using Microsoft
     Deployment Wizard as described in Creating ZTI Boot Images in Configuration
     Manager

     Managing software packages for ZTI in the Configuration Manager console as
     described in Managing Software Packages in Configuration Manager

     Deploying task sequences to reference or target computers for ZTI as described in
     Managing Task Sequence Deployment in Configuration Manager

     Manually adding computers to the site database for ZTI as described in Manually
     Adding Computers to the Site Database in Configuration Manager

     Managing computer collections for ZTI as described in Managing Computer
     Collections in Configuration Manager

     Managing distribution points for ZTI as described in Managing Distribution Points
     in Configuration Manager

     Configuring individual ZTI task sequence steps as described in Configuring ZTI Task
     Sequence Steps in Configuration Manager

     Configuring ZTI task sequence steps that perform server role-related actions as
     described in Configuring ZTI Server Role Task Sequence Steps in Configuration
     Manager

Creating a ZTI Task Sequence Using MDT Task Sequence
Templates in Configuration Manager
Use the Create MDT Task Sequence Wizard in the Configuration Manager console to
create task sequences in Configuration Manager that are integrated with MDT. MDT

<!-- p.277 -->

includes task sequence templates that you can use to deploy the reference and target
computers.

Create ZTI task sequences using the MDT task sequence templates by:

     Identifying the ZTI task sequence templates that are a part of MDT as described in
     Identify the Task Sequence Templates in MDT in Configuration Manager

     Identifying the packages and images that the MDT task sequence templates
     require as described in Identify the Packages and Images That the MDT Task
     Sequence Templates in Configuration Manager Require

     Creating ZTI task sequences as described in Create ZTI Task Sequences Using the
     Create MDT Task Sequence Wizard in Configuration Manager

Identify the Task Sequence Templates in MDT in Configuration
Manager

Table 121 lists the task sequences templates included in MDT for Configuration
Manager, the file name for each template, and a description of the template. The
template files are located in the install_folder\SCCM folder (where install_folder is the
folder in which MDT was installed).

Table 121. Task Sequence Templates Included in MDT for
Configuration Manager

                                                                            ﾉ   Expand table

 Template               File name                Select this template to

 Client Task Sequence   SCCM_Client.xml          Deploy client operating systems to target
                                                 computers for all scenarios except the MDT
                                                 Replace Computer deployment scenario.

 Client Replace Task    SCCM_ClientReplace.xml   Captures user state migration data from
 Sequence                                        target computers for the MDT Replace
                                                 Computer deployment scenario.

 Microsoft              SCCM_Custom.xml          Create a task sequence that can be
 Deployment Custom                               customizable to meet the needs of your
 Task Sequence                                   organization.

 Standard Server Task   SCCM_Server.xml          Deploy server operating systems to target
 Sequence                                        computers for all scenarios.

<!-- p.278 -->

 Template               File name                 Select this template to

 User Driven            SCCM_UDI.xml              Deploy operating systems to target
 Installation Task                                computers using UDI.
 Sequence

 User Driven            SCCM_UDIReplace.xml       Captures user state migration data from
 Installation Replace                             target computers for the MDT Replace
 Task Sequence                                    Computer deployment scenario using UDI.

  ７ Note

  Always use the Create MDT Task Sequence Wizard to import the task sequence
  templates. Although you can manually import the task sequence templates, doing
  so is not recommended.

Identify the Packages and Images That the MDT Task Sequence
Templates in Configuration Manager Require
Table 122 lists the packages and images that the task sequence templates in MDT
require. These packages and images must exist (or be created) for the task sequences to
run correctly in Configuration Manager.

Table 122. Packages and Images Required by the Task
Sequence Templates Included in MDT for Configuration
Manager

                                                                              ﾉ   Expand table

 This package or        Contains the
 image

 Boot image package     Boot image used to initiate the ZTI deployment process and in the
                        middle of the process when performing the Refresh Computer
                        deployment scenario.

 Microsoft              Script and tools necessary for the MDT task sequence templates for
 Deployment Files       Configuration Manager.
 package

 OS image package       Image of the target operating system to be deployed to the target
                        computer.

<!-- p.279 -->

 This package or      Contains the
 image

 OS install package   All the files required to install the operating system (using Windows
                      Setup.exe).

 Client package       Configuration Manager client installation files.

 USMT package         USMT files used to capture and restore user state.

 Custom Settings      Contains unattended files and customsettings.ini.
 package

  ７ Note

  You can use the generic boot images (WIM files) that the Deployment Workbench
  generates in ZTI deployments. However, you cannot use the LTI LiteTouch boot
  images (WIM files) that the Deployment Workbench generates in ZTI deployments
  using Configuration Manager.

The Create MDT Task Sequence Wizard can automatically create these packages and
images or can use existing packages and images. The task sequence templates contain
placeholders for each package and image listed in Table 122. The Create MDT Task
Sequence Wizard substitutes the packages and images selected for the placeholders in
the task sequence templates. After completing the wizard, the new created task
sequence references the appropriate packages and images.

In addition to the packages and images that the task sequence templates require,
consider creating and including the following elements in the task sequences to provide
similar functionality in the Deployment Workbench:

     Software distribution packages. This package includes any software that will be
     installed as part of the operating system deployment (similar to the Applications
     node in the Deployment Workbench). These packages are created as packages and
     programs in Configuration Manager. For more information on how to create these
     packages, see the following sections in the Configuration Manager Documentation
     Library, which is included with Configuration Manager:

        "Content Management in Configuration Manager"

        "Application Management in Configuration Manager"

     Windows package file (software update) packages. These packages include any
     Windows package files that contain software updates (such as language packs,

<!-- p.280 -->

     security updates, and service packs) that will be installed as part of the operating
     system deployment (similar to the OS Packages node in the Deployment
     Workbench). You can use these software update packages:

        Without modification by using the Software Updates feature in Configuration
        Manager. For more information on using these packages in the Software
        Updates feature, see the section, "Software Updates in Configuration Manager,"
        in the Configuration Manager Documentation Library, which is included with
        Configuration Manager.

        As installed directly by ZTI using the Install Updates Offline task sequence step
        type. For more information about configuring a task sequence step based on
        this type, see Configuring ZTI Task Sequence Steps in Configuration Manager.

        Custom software distribution packages in Configuration Manager. For more
        information on how to create these packages, see the section, "Technical
        Reference for Content Management in Configuration Manager," in the
        Configuration Manager Documentation Library, which is included with
        Configuration Manager.

     Device driver package. Configuration Manager uses driver packages to control the
     distribution of drivers to distribution points. You can specify device driver
     categories in an Auto Apply Drivers task sequence step type to limit which drivers
     are installed, or you can install all device drivers using an Apply driver package
     task sequence step type. For more information about how to include device drivers
     in the operating system image, see the section, "How to Install Device Drivers to
     Computers by Using Task Sequences," in the Configuration Manager
     Documentation Library, which is included with Configuration Manager.

Create ZTI Task Sequences Using the Create MDT Task Sequence
Wizard in Configuration Manager
The Create MDT Task Sequence Wizard in Configuration Manager substitutes the
packages and images selected for the placeholders in the task sequence templates.
After completing the wizard, the new task sequence references the appropriate
packages and images.

  ７ Note
