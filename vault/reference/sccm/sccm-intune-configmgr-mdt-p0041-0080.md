---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 41-80"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0041-0080
family: sccm
documentKind: "doc"
abstract: "Windows Internet Explorer® components.) It is possible for deployment to finish but still trigger several errors or warnings if the errors are nonfatal. It is useful to inspect these errors and warnings—for example, by opening corresponding logs files and running verification te"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 41-80

<!-- p.41 -->

Windows Internet Explorer® components.) It is possible for deployment to finish
but still trigger several errors or warnings if the errors are nonfatal. It is useful to
inspect these errors and warnings—for example, by opening corresponding logs
files and running verification tests—and determine whether they are unexpected.

Some device drivers can stall the deployment process. If this happens, isolate the
device driver and remove it from the target computer, or contact the vendor for an
updated version of the device driver.

The error "Cannot Find Driver Path" can appear if you choose to optimize a
Windows PE image and select drivers that are not available from the distribution
point. To work around this problem, select theCompletely Regenerate The Boot
Images option.

The USMT fails if you enter a path surrounded by quotation marks that also ends
in a backslash (\). To prevent problems, simply leave off the final backslash when
specifying a folder. For example, the following paths will cause an error:

   "D:\"

   "D:\folder\"

   However, these paths will not cause an error:

   D:

   D:\

   D:\folder\

   D:\folder

   "D:\folder"

   "D:\"

   "D:"

Configure the Internet Explorer home page using CustomSettings.ini, in the MDT
DB, or by using the Windows Internet Explorer Administration Kit (IEAK).
Configuring the Internet Explorer home page works only in Windows unattended
installation.

During LTI deployments to new computers, some pages (such as the User Locale
and Keyboard Locale pages) do not display text correctly if required fonts are not

<!-- p.42 -->

installed in Windows PE. In the Refresh Computer scenario, the same symptoms
appear if required fonts are not installed in the operating system being replaced.

Some keyboard layouts might require language packs or input method editors that
MDT does not automatically include in the Windows PE startup image. MDT does
not verify that the keyboard layout is valid. For more information, see Custom
Input Method Editor (IME) requirements.

A maximum of two WINS server addresses can be added when configuring static IP
configuration settings for a network adapter. If more than two WINS server
addresses are added using MDT, only the first two WINS server addresses are used.

Hash value errors may occur in Configuration Manager during download on
demand or when creating a media deployment DVD. This can occur if the
packages on the distribution points are inconsistent with the information in the
Configuration Manager database.

To correct hash value errors for Configuration Manager

   1. Select Start, point to All Programs, and then point to Microsoft System
     Center 2012. Point to Configuration Manager, and then select Configuration
     Manager Console.

   2. In the Configuration Manager console, in the Navigation pane, select
     Software Library.

   3. In the Software Library workspace, go to Overview/Application
     Management/Packages.

   4. In the preview pane, select package_name (where package_name is the name
     of the package that is inconsistent).

   5. On the Ribbon, on the Home tab, in the Properties group, select Properties.

     The package_nameProperties dialog box opens (where package_name is the
     name of the package).

   6. In the package_nameProperties dialog box (where package_name is the
     name of the package), on the Content Locations tab, in Distribution points
     or distribution point groups box, select distribution_point (where
     distribution_point is the name of the distribution point or distribution point
     group), then select Redistribute.

   7. In the Configuration Manager dialog box, select OK.

<!-- p.43 -->

   8. Repeat steps f through g for each distribution point or distribution point
     group.

   9. In the package_nameProperties dialog box, select OK.

 10. Repeat steps d through i for each package that is inconsistent.

In LTI deployments, you set several kinds of information in the Create Task
Sequence Wizard. The UI does not provide an option to edit this information at a
later time. However, you can edit the information directly in the Unattend.xml file.
The information includes:

  Organization name

  Full name

  Internet Explorer home page

  Local Administrator password

No user state configuration settings can be or need to be specified using the
CustomSettings.ini file for Configuration Manager scenarios. The network location
is determined automatically by the Request State Store task.

In Configuration Manager deployments, you can install multiple application
packages on a computer by specifying them in the CustomSettings.ini file
according to the following parameters:

  Specify a base variable named PACKAGES in the task sequence in the Install
  Software task.

  Each PACKAGES variable name should have a suffix starting with 001.

  The PACKAGESxxx value should have the format PACKAGEID:ProgramName
  (use a colon between items).

  The ProgramName value is case-sensitive.

  The following is an example of specifying packages in CustomSettings.ini:

     ini

     PACKAGES001=DEP0002B:Install Office 2007
     PACKAGES002=DEP00011:Install Office Communicator

<!-- p.44 -->

In LTI New Computer deployments, applications marked as hidden in the
Deployment Workbench are not installed when you do not skip the Application
page in the Deployment Wizard and specify the application globally unique
identifier (GUID) in CustomSettings.ini. Specify hidden applications using the
MandatoryApplications property instead of the Applications property.

Close the Configuration Manager console before running the integration option
from MDT. Otherwise, some files may not be properly updated.

During the Scanstate and Loadstate processes, multiple copies of log files may be
created. You can use a new USMT template for excluding the log files or log
directories while running Scanstate and Loadstate.

New Computer and Replace Computer deployment scenarios format Disk 0 by
default. Using MDT on computers with original equipment manufacturer (OEM)
partitions or multiple fixed or external hard disks may require additional
configuration and scripting in addition to thorough testing.

The Task Sequencer will not accept XML files that contain Unicode content (from
an XML file encoded as UTF-8). Attempting to do use XML files results in a task
sequence failure. The Task Sequencer does not properly deal with encoded UTF-7
data: It does not cause a failure, but it does cause the data to be translated
unexpectedly.

After uninstalling MDT using the Control Panel Add or Remove Programs item, the
Distribution share directory (if created) must be removed manually. MDT does not
remove files or folders that it did not initially install.

When using MDT extensions (add-in wizards) with Configuration Manager, MDT
must be installed on every server running Configuration Manager used to
administer operating system deployments.

The Priority property in CustomSettings.ini has no maximum line length. However,
if the property name is longer than 55 characters when the Configure Database
Wizard runs, the wizard will truncate the Priority property, and you will need to
manually edit the property. As a workaround, run the Configure Database Wizard
before performing any other customization, or clear the check boxes for queries in
the wizard that are not needed.

MDT supports deployment from a UFD. See the Windows ADK for information
about preparing the device, then copy (using thexcopy command) all files and
folders from the \Media\content folder to the UFD.

<!-- p.45 -->

     Dialing properties that are not configured, even if present in the answer file,
     include the country/region code, area code, long-distance access, and dialing rules.
     To work around this issue, configure dialing rules by creating and testing a .reg file
     in a lab environment, and then import that .reg file as a custom task during the
     task sequence.

Review Known Issues, Limitations, and Recommendations That
Relate to Windows

The following is a list of known issues, limitations, and recommendations that relate to
Windows:

     Deployment will fail on computers configured for a language other than English
     when the Windows Media® Player Network Sharing Service is run. As a
     workaround, stop the Windows Media Player Network Sharing Service until after
     deployment is complete.

     You can use AD DS to back up BitLocker and TPM data. Recovery information
     includes the recovery password for each encrypted value, the TPM owner
     password, and the information necessary to associate recovery information with
     computers and volumes. Another option is to save a package containing the keys
     used to encrypt data in addition to the recovery password required to access those
     keys. For more information, see BitLocker FAQ for AD DS in the Microsoft
     Download Center.

     When enabling BitLocker, key files are generated as hidden, read-only system files.
     To see them, set the Windows Explorer option to show hidden and system files.

     BitLockerduring LTI deployment requires at least two partitions. The first partition
     is the primary partition and can be any size; it stores operating system files and
     user data. In BitLocker terminology, this is called the boot partition. For Windows 7,
     it should be at least 300 MB. This partition stores startup files required during the
     first phase of startup and is called the system partition. A BitLocker partition is
     created for all Windows 7 deployments, regardless of whether you are deploying
     BitLocker.

     If a user with a limited account maps a drive (such as drive Z) to the MDT
     distribution point (\\server\distribution$, where server is the name of the computer
     hosting the distribution point), runs LiteTouch.vbs, and then provides Administrator
     credentials in the User Credentials dialog box, MDT displays the error, "Cannot
     find script file 'Z:\Scripts\LiteTouch.wsf' because the account that the user provided
     in the User Credentials dialog box cannot access the mapped drive created by the

<!-- p.46 -->

   limited user account." To resolve this issue, use an account with Administrator
   credentials to map the drive to the distribution point.

   BitLockerdeployment can fail with the error, "Unable to merge BDEPartition, return
   code=87," when the user does not specify a locale. Restarting the computer does
   not allow the operating system to start. To avoid this error, specify a user language,
   or edit the CustomSettings.ini file to specify the UILanguage property. For
   example, you could add UILanguage = en-us to the CustomSettings.ini file.

   If activating BitLocker during installation fails in Refresh Computer scenario, verify
   that MDT is able to shrink the partition as required by following these steps:

      1. At a command prompt, type diskpart shrink querymax, and note the value
         displayed.

      2. If the value is less than 2,000 MB, then manually defragment the disk. MDT
         performs an automatic defragmentation, however, so this might not resolve
         the problem.

      3. If defragmenting the disk does not resolve the issue, back up the computer's
         hard disk, create a new partition, and repeat these steps until typing diskpart
         shrink querymax returns a value greater than 2,000 MB. There might be files
         in specific areas of the partition that cannot be relocated or removed.

   The BDERequired flag is no longer used. By default, all sample templates that
   enable BitLocker and encounter an error will stop. You can edit the task sequence
   to enable deployment to continue if an error occurs.

   When deploying an image that is using a different language, Setup will prompt for
   the keyboard layout, language, and time and currency settings during the
   Windows PE phase. As a workaround, import Setup files with the custom image.

   MDT supports Windows language pack selection during deployment for all
   scenarios if the language packs are configured in the Deployment Workbench.
   Selecting multiple language packs is possible when deploying Enterprise or
   Ultimate editions of the operating systems. When other editions of Windows are
   deployed, only one language pack can be selected because of Windows licensing
   restrictions.

Review Known Issues, Limitations, and Recommendations That
Relate to Disks and Partitioning

<!-- p.47 -->

The following is a list of known issues, limitations, and recommendations that relate to
disk and partitioning:

     LTI does not support the deployment of the target operating system to logical
     drives or dynamic disks.

     Deployments to existing disk partitions created by newer operating system
     versions are not supported in Refresh Computer deployment scenarios.

     However, you can deploy different processor architecture versions to the existing
     partitions created by the same operating system version. For example, you can
     deploy a 64-bit version of Windows on a computer that is currently running a 32-
     bit version of Windows or vice versa.

     In the Format and Partition Disk task sequence step types, always configure the
     logical partitions that will reside on an extended partition immediately after the
     extended partition. If you do not specify the logical partitions immediately after
     the extended partition, creating the logical partition sizes using a percentage
     produces unexpected results.

     For example, the following partition creation order is incorrect, because the logical
     partitions (partition 4 and partition 5) are not immediately after the extended
     partition (partition 2):

        Console

        Partition 1: Primary
        Partition 2: Extended
        Partition 3: Primary
        Partition 4: Logical
        Partition 5: Logical
        Partition 6: Primary

     Instead, create the partitions in the following order:

        Console

        Partition 1: Primary
        Partition 2: Extended
        Partition 3: Logical
        Partition 4: Logical
        Partition 5: Primary
        Partition 6: Primary

<!-- p.48 -->

     Windows always hides the system volume during deployment, so a drive letter is
     not assigned to the system volume. For example, if the target computer has one
     drive with two partitions, Partition_1 and Partition_2, and you deploy Windows to
     Partition_2, Windows will be properly deployed to Partition_ 2. However, a drive
     letter will not be assigned to Partition_1.

     After starting Windows PE, the drive letters assigned to each storage device may
     change. For example, if the destination computer has a CD-ROM assigned to drive
     D and a hard disk drive assigned to drive E, the hard disk drive will be on drive D
     and the CD-ROM will be on drive E when Windows PE starts. If a DVD deployment
     fails, check that the drives have not been reassigned on the target computer. To
     simplify deployment, save user data to a network location instead of to a local
     drive.

     Avoid editing the Unattend.xml files to format or alter the partitions. MDT might
     store state and user data on the partition before calling Setup.exe (in LTI
     scenarios), and instructions added to Unattend.xml would cause Setup to destroy
     that data, resulting in a deployment failure.

     While configuring the Format and Partition Disk task, always specify the extended
     and logical partitions together, and do not add a primary partition in-between,
     which gives undesirable results when a logical partition size is configured using a
     percentage. In other words, do not add a primary partition between an extended
     and logical partition.

Review Known Issues, Limitations, and Recommendations That
Relate to BitLocker
The following is a list of known issues, limitations, and recommendations that relate to
BitLocker:

     Windows Server may crash if the operating system image used to perform the
     deployment does not have the optional BitLocker component. This situation can
     occur in the following scenarios:

        Performing the MDT Refresh Computer deployment scenario (in LTI, ZTI, or UDI),
        where BitLocker is enabled on the existing operating system. In this situation,
        BitLocker is suspended in the existing operating system by MDT, but without
        the optional component in the new operating system image, Windows is unable
        to boot from the disk on which BitLocker is suspended.

        Performing the MDT New Computer deployment scenario (in LTI, ZTI, or UDI) on
        a Trusted Platform Module-enabled server on which BitLocker has been

<!-- p.49 -->

        enabled. In this situation, BitLocker will be enabled offline using BitLocker pre-
        provisioning, but without the BitLocker optional component in the new
        operating system image, the new operating system is unable to boot from the
        disk on which BitLocker has been pre-provisioned.

        The workaround for any of these situations is to deploy a custom operating
        system image that includes the BitLocker component in the image.

     If you want to use an alphanumeric PIN for BitLocker during deployment, you must
     enable the Allow enhanced PINs for Startup group policy setting. TheAllow
     enhanced PINs for Startup group policy setting is located in Computer
     Configuration/Policies/Administrative Templates/Windows Components/BitLocker
     Drive Encryption/Operating System Drives.

     If a BitLocker recovery prompt appears after restarting the target computer
     (because the BitLocker key required to unlock the volume could not be obtained),
     work around the problem by using one of the following approaches:

        Remove the media (such as the deployment DVD) while Windows PE is still
        running. Doing so prevents the operating system from seeing the DVD when it
        starts.

        Change the boot order of the computer so that the DVD drive follows the hard
        disk.

        Deploy the computer with no startup media; for example, use a Pre-Boot
        Execution Environment (PXE) deployment.

Review Known Issues, Limitations, and Recommendations for LTI
Deployments
The following is a list of known issues, limitations, and recommendations that relate to
LTI deployments:

     The network credentials specified for accessing network resources (the USMT store
     location, computer backup location, and so on) are not validated if a user is logged
     on to the computer using a domain account and if the computer already has a
     connection established to another share on the same server.

Review Known Issues, Limitations, and Recommendations for ZTI
Deployments Using Configuration Manager

<!-- p.50 -->

The following is a list of known issues, limitations, and recommendations that relate to
ZTI deployments using Configuration Manager:

     When deploying a non-English-language target operating system, the installation
     method prompts for user language, because the template for the unattend.xml file
     contains settings for United States English (en-us). To work around this problem,
     perform one of the following tasks:

        Modify the unattend.xml template file to reflect the language of the target
        operating system.

        Configure the KeyboardLocale, UserLocale, and UILanguage properties in the
        CustomSettings.ini file or the MDT DB to reflect the language of the target
        operating system.

     When deploying computers using Configuration Manager and backing up the
     computer data locally, computers with two partitions may not be able to retain the
     backup. To prevent backups from being removed, save to a network location
     instead of to a local drive.

     In a Configuration Manager task sequence, the Format and Partition task might
     not run successfully on a computer if it has only one unformatted partition. To
     work around this issue, either remove the partition or format it.

     While installing the server roles, Configuration Manager might display a prompt
     for DLLs needed to complete the role installation. If this happens, specify a valid
     location for the required files. To avoid this step, add a step earlier in the task
     sequence that copies the required DLLs to the Windows Setup files folder defined
     in the registry. This folder location is defined in the SourcePath registry value,
     located in
     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Setup.

Review Known Issues, Limitations, and Recommendations for UDI
Deployments

The following is a list of known issues, limitations, and recommendations that relate to
UDI deployments:

     Applications are disabled and cannot be automatically installed. This issue arises
     when the application requires administrator approval but has not yet been
     approved. If the Require administrator approval if users request this
     applicationcheck box is selected for the application, verify that the application has
     been approved.

<!-- p.51 -->

     For more information on how to require administrator approval and grant
     approval, see How to Deploy Applications in Configuration Manager.

     When performing the MDT Refresh Computer deployment scenario with a USB
     hard disk attached, task sequence errors may occur, because the Configuration
     Manager task sequencer placed the _SMSTaskSequence folder on the USB drive. By
     default, the Configuration Manager task sequencer places the _SMSTaskSequence
     folder on the drive with the most available free disk space, which can cause
     problems later in the deployment process if the USB drive is removed.

     If the _SMSTaskSequence folder is located on a USB drive, the
     CheckSMSFolderOnUSB UDI task will detect this condition and prevent the
     deploment from continuing. To resolve this issue and perform the deployment,
     complete the following steps:

        1. Disconnect the USB drive from the target computer before starting the task
          sequence.

        2. Start the task sequence.

        3. Wait until the UDI Wizard starts.

        4. Connect the USB drive.

        5. Complete the UDI Wizard.

Review Known Issues, Limitations, and Recommendations for
Running Task Sequences on Target Computers

The following is a list of known issues, limitations, and recommendations for running
task sequences on target computers in MDT:

     For LTI deployments, ensure that User Account Control (UAC) is disabled for the
     built-in local Administrator account on the target computers until the task
     sequence finishes. Running task sequences on computers with UAC enabled for the
     local Administrator account causes task sequences to fail.

       ７ Note

       UAC should be disabled only for the built-in local Administrator account and
       enabled for all other accounts. By default, the built-in local Administrator
       account is excluded from UAC because of the User Account Control: Admin

<!-- p.52 -->

       Approval Mode for the built-in Administrator account (disabled) policy
       setting.

     For more information about UAC Group Policy settings, see UAC Group Policy
     Settings and Registry Key Settings .

Review Known Issues, Limitations, and Recommendations for
Saving and Restoring User Information
The following is a list of known issues, limitations, and recommendations for saving and
restoring user information in MDT:

     For LTI deployments, do not add any of the following USMT command-line
     parameters to the ScanStateArgs or LoadStateArgs properties, as they cause the
     saving and restoration of user state information to fail:

        /hardlink

        /nocompress

        /encrypt

        /key

        /keyfile

        /vsc

        /l

        /I

     User state migration data may not be restored properly depending on the disk
     configuration of the target computer when deploying Windows.

     This issue can occur when the target computer has two physical hard disks, Disk_0
     and Disk_1. Disk_0 contains the C volume, which is encrypted using BitLocker. The
     MDT deployment process is configured to deploy a new operating system to
     Disk_1. The problems in the deployment process occur as follows:

        Early the deployment process, the minint and smstasksequence folders are
        copied to the existing C volume, which is encrypted.

        Disk_1 is partitioned and formatted properly in preparation for deploying the
        target operating system.

<!-- p.53 -->

        The target operating system is installed on the new partition and disk volume
        on Disk_1.

        During the State Restore Phase, the original C volume is not assigned a drive
        letter, so the task sequence steps in the State Restore Phase cannot access the
        minint and smstasksequence folders on the BitLocker-encrypted drive. The
        restoration of the user state migration data fails.

        The result is that the target operating system is installed, but the restoration of
        the user state migration data fails.

Overview of UDI
Typically, when deploying operating systems using the OSD feature in Configuration
Manager and ZTI in MDT you must provide all the information necessary to deploy the
operating system. Prior to performing the deployment, the information is configured in
configuration files or in databases (such as the CustomSettings.ini file or the MDT DB).
During the ZTI deployment process, ZTI converts the appropriate configuration settings
to task sequence variables, which are consumed by the MDT task sequences for UDI. All
of the configuration settings must be provided before you can initiate the deployment.

UDI provides a wizard driven interface that allows users to provide configuration
information immediately prior to the deployment being performed. You can configure
the user experience in the wizard, which lets you control the amount information the
user completing the wizard must provide. This division of user roles allows IT pros to
provide precise control over deployments while reducing the load on them by allowing
other users to perform the deployments. The interface allows you to create generic OSD
task sequences, and then provide computer specific information at the time of
deployment, which provides greater flexibility in the deployment process.

  ７ Note

  If you are unfamiliar with UDI, review the UDI terms and terminology in "UDI
  Concepts" in the Microsoft Deployment Toolkit Reference. Familiarizing yourself with
  these terms and terminology will help you be more successful in applying the
  remainder of this guide to your organization.

Installing or Upgrading to MDT
To prepare for performing deployments using MDT, perform the following tasks:

<!-- p.54 -->

   1. Review the known issues, limitations, and recommendations for preparing disks on
       target computers in MDT as described in Reviewing Known Issues, Limitations, and
       Recommendations for Installing or Upgrading to MDT.

   2. Prepare the prerequisite infrastructure required for the LTI, ZTI, and UDI
       deployments methods as described in Preparing the Prerequisite Infrastructure for
       All MDT Deployment Methods.

   3. Perform any combination of the following steps to ensure that MDT is installed
       correctly:

            Install a new instance of MDT on each computer where you want to manage
            MDT deployment shares as described in Installing a New Instance of MDT.

            Upgrade an existing instance of MDT 2012 Update 1 as described in
            Upgrading to MDT.

   4. Determine whether any updates are available for the components in the
       Deployment Workbench using the Check Updates Wizard as described in
       Upgrading to MDT.

  ７ Note

  Windows PowerShell™ version 2.0 or later must be installed on any computer on
  which MDT is installed for management of LTI or ZTI deployments.

Reviewing Known Issues, Limitations, and
Recommendations for Installing or Upgrading to MDT
The following is a list of known issues, limitations, and recommendations for installing
MDT:

       Ensure that the disk volume that contains the temporary folder that the
       Deployment Workbench uses has at least 20 GB of available disk space.

       The Deployment Workbench creates large images and requires temporary storage
       during the image-creation process. The Deployment Workbench determines the
       temporary folder to use by performing the following steps:

          1. Use the temporary folder specified in the Temp_Dir registry subkey, which is
            located at HKEY_LOCAL_MACHINE\Software\Microsoft\Deployment 4.
            Create the Temp_Dir registry subkey as a REG_SZ type that contains the fully
            qualified path to the folder to be used as the temporary folder.

<!-- p.55 -->

        2. If the TEMP_DIR registry subkey does not exist, then the Deployment
           Workbench uses the folder specified in the %TEMP% environment variable.

           Ensure that the disk volume specified in the TEMP_DIR registry subkey or in
           the %TEMP% environment variable has sufficient available disk space.

Preparing the Prerequisite Infrastructure for All MDT
Deployment Methods
MDT requires installation of the following software for LTI, ZTI, and UDI:

     Microsoft .NET Framework version 3.5 with SP1

     Windows PowerShell version 2.0

     For specifics about how to prepare your environment specifically for LTI, ZTI, or
     UDI, see the following sections:

     Preparing the LTI Deployment Environment

     Preparing the ZTI Deployment Environment for Configuration Manager

     Preparing the UDI Deployment Environment

Installing a New Instance of MDT
With all the prerequisite software installed, perform the following steps to install MDT
(MicrosoftDeploymentToolkit_platform.msi, where platform is either x86 or x64):

   1. Double-click MicrosoftDeploymentToolkit2012_x64.msi (for 64-bit operating
     systems) or MicrosoftDeploymentToolkit2012_x86.msi (for 32-bit operating
     systems).

     The Microsoft Deployment Toolkit 2013 Setup Wizard starts.

   2. Complete the Microsoft Deployment Toolkit 2013 Setup Wizard using the
     information in Table 8.

Table 8. Information for Completing the Microsoft Deployment
Toolkit 2013 Setup Wizard

                                                                             ﾉ   Expand table

<!-- p.56 -->

 On this wizard page             Do the following

 Welcome to the Microsoft        Select Next.
 Deployment Toolkit 2013 Setup
 Wizard

 End-User License Agreement      - Review the license agreement.

                                 - Select the I accept the terms in the License Agreement
                                 check box, and then select Next.

 Custom Setup                    - Select the desired features.

                                 - Select the desired destination folder for installing MDT
                                 (which defaults to C:\Program Files\Microsoft Deployment
                                 Toolkit), and then select Next.

 Ready to install Microsoft      Select Install.
 Deployment Toolkit 2013

 Installing Microsoft            The progress for installing the Microsoft Deployment Toolkit
 Deployment Toolkit 2013         2013 is displayed.

 Completed the Microsoft         Select Finish.
 Deployment Toolkit 2013 Setup
 Wizard

Upon completion, MDT is installed in the target folder you selected in the wizard.

Upgrading to MDT
MDT automatically uninstalls previous versions before installing, including the following
versions:

     MDT 2012 Update 1

     In addition to upgrading the MDT installation, upgrade any existing deployment
     shares. For more information on this process, see Upgrade an Existing Deployment
     Share in the Deployment Workbench.

Performing LTI Deployments
You perform LTI deployments using only MDT and supporting components. You can
perform LTI deployments over a network or from removable media. This flexibility makes
LTI deployments appropriate for a wide range of organizations.

Perform LTI deployments by:

<!-- p.57 -->

     Preparing the deployment environment as described in Preparing the LTI
     Deployment Environment

     Preparing for deployment to the reference computer as described in Preparing for
     LTI Deployment to the Reference Computer

     Deploying to and capture a reference computer image as described in Deploying
     To and Capturing an Image of the Reference Computer in LTI

     Preparing for deployment to target computers as described in Preparing for LTI
     Deployment to Target Computers

     Deploying captured images to target computers as described in Deploying
     Captured Images to Target Computers in LTI

Preparing the LTI Deployment Environment
After preparing the prerequisite infrastructure for MDT, prepare the LTI deployment
environment.

To prepare the LTI deployment environment

   1. Install the prerequisite LTI infrastructure as described in Prepare the Prerequisite
     LTI Infrastructure.

   2. Install a new instance of MDT on the deployment server, or upgrade an existing
     instance of MDT as described in Install or Upgrade to MDT for LTI Deployments.

   3. Install the components required by MDT and the LTI deployment process as
     described in Install Components That MDT and LTI Require.

   4. Obtain the software that the LTI deployment process requires as described in
     Obtain the Software That the LTI Deployment Process Requires.

Prepare the Prerequisite LTI Infrastructure
LTI deployments require that a properly configured infrastructure exist prior to installing
MDT and performing deployments. Ensure that your new or existing infrastructure is
specifically optimized for the operating system deployments.

  ７ Note

<!-- p.58 -->

  Windows PowerShell version 2.0 or later must be installed on any computer on
  which MDT is installed for management of LTI deployments.

For more information about configuring your environment to support LTI deployments,
see the following sections in the MDT document Quick Start Guide for Lite Touch
Installation:

      "Prerequisites"

      "Step 1: Obtain the Required Software"

Install or Upgrade to MDT for LTI Deployments

To perform LTI deployments, you must have at least one instance of MDT running in
your environment. If your existing environment has:

      No computers currently running MDT or a previous version of MDT, then install
      one or more new instances of MDT as described in Installing a New Instance of
      MDT

      One or more computers running a previous version of MDT, then upgrade those
      instances to MDT as described in Upgrading to MDT.

Install Components That MDT and LTI Require
The Deployment Workbench is the administration console for LTI. Most of the LTI
management tasks are performed in the Deployment Workbench. MDT also includes a
Windows PowerShell provider that allows for the automation of LTI management tasks
through the Windows PowerShell command shell using MDT cmdlets.

  ７ Note

  MDT supports Windows ADK for Windows 8.1, Windows PE 5.0, and System Center
  2012 R2 Configuration Manager.

Table 10 lists the top-level nodes in the Deployment Workbench and the types of tasks
performed in each node.

Table 10. Deployment Workbench Nodes

                                                                      ﾉ   Expand table

<!-- p.59 -->

 Node            Description

 Information     Provides access to documentation, displays breaking news about MDT, and lists
 Center          the components required to use the Deployment Workbench.

 Deployment      Lists the deployment shares that this instance of the Deployment Workbench
 Shares          manages. Each deployment share includes operating systems, applications,
                 operating system packages, task sequences, and out-of-box drivers populated in
                 the deployment share.

The Deployment Workbench automates the download and installation of components
used in LTI.

  ７ Note

  If the MDT computer has internet connectivity, the Deployment Workbench can
  automatically download the components.

To download and install Deployment Workbench components

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Information Center/Components.

   3. In the Components pane, in the Available for Download section, select
     component_name (where component_name is the name of the component you
     want to download).

   4. In the details pane, select Download.

     After downloading the component from the internet, the component is listed in
     the Downloaded section in the details pane.

   5. In the details pane, in the Download section, select the downloaded component,
     and then select Install.

        ７ Note

        If there is no Install button, the component cannot be installed or the
        installation is not necessary.

<!-- p.60 -->

     The installation process for the respective component is initiated. Complete the
     installation process for the component using the instructions provided for the
     component.

     After the component is installed, the component appears in the Installed section
     of the details pane. If the component cannot be installed or you did not choose to
     install it, the component remains in the Downloaded section.

     MDT uses the Windows ADK for Windows 8.1 which includes USMT.

Obtain the Software That the LTI Deployment Process Requires

Collect the software that LTI will deploy. LTI will import or add this software to
deployment shares. The software that can be deployed includes:

     Operating system source files or image files for each operating system to be
     deployed to the reference and target computers

     Operating system packages for the operating systems, such as security updates,
     feature packs, or language packs

     Device drivers for the reference and target computers that are not included as a
     part of the operating system

     Applications that are to be installed as a part of the operating system image or
     during the deployment of the reference image

     The Task Sequencer used in MDT deployments requires that the Create Global
     Object right be assigned to credentials used to access and run the Deployment
     Workbench and the deployment process. This right is typically available to
     accounts with Administrator-level permissions (unless explicitly removed). Also, the
     Specialized Security - Limited Functionality (SSLF) security profile, which is part of
     the Windows security baselines, removes the Create Global Object right and
     should not be applied to computers being deployed using MDT.

     In addition, LTI requires that the:

     Local Administrator account on the target computer be enabled

     Local Administrator account be granted the Create Global Objects right

     Local Administrator account not have UAC enabled

     Ability to have an account automatically log on to the target computer be enabled
     and not blocked using Group Policy or a local security policy

<!-- p.61 -->

     Logon banner for the target computers not be enabled using Group Policy or a
     local security policy

Preparing for LTI Deployment to the Reference Computer
For many of the LTI deployment scenarios, best practice is to create a reference
computer as described in Choosing Thick, Thin, or Hybrid Images, and then capture an
image of that computer. Later in the LTI deployment process, you will deploy the
captured image of your reference computer to the appropriate target computers.

  ７ Note

  In some LTI deployment scenarios, you may want to deploy Windows operating
  systems without creating a reference image—for example, when you want to
  deploy thin images. If you are deploying thin images and you do not want to create
  a reference image, skip the steps that relate to the reference computer. For more
  information about determining which image type to use, see Choosing Thick, Thin,
  or Hybrid Images.

Create a reference computer for each image you want to create for deployment to the
target computers. For more information about determining the number of images
required in your organization and subsequently the number of reference computers
required, see Estimate Storage Requirements for MDT Deployment Shares.

For more information about the use of reference computers in MDT-based
deployments, see Using Reference Computers in MDT Deployments.

To prepare for deployment to the reference computer

   1. Create a new deployment share, or upgrade an existing deployment share.For
     more information about:

           Creating a new deployment share, see Create a New Deployment Share in the
           Deployment Workbench

           Upgrading an existing deployment share, see Upgrade an Existing
           Deployment Share in the Deployment Workbench

   2. Configure the deployment share to contain the appropriate software for
     deployment to the reference computer, including the following:

<!-- p.62 -->

       Configuring operating systems as described in Configuring Operating
       Systems in the Deployment Workbench

       Configuring applications as described in View and Configure an Application
       in the Deployment Workbench

       Configuring operating system packages as described in Configuring Packages
       in the Deployment Workbench

       Configuring device drivers as described in Configuring Device Drivers in the
       Deployment Workbench

3. Create a new task sequence that will deploy the target operating system to the
  reference computer as described in:

       Configuring Task Sequences in the Deployment Workbench

       Configuring LTI Task Sequence Steps in the Deployment Workbench

       The LTI deployment process is unable to perform Sysprep operations on a
       target computer that is encrypted using BitLocker. Ensure that you do not
       enable BitLocker on the reference computer. Enable BitLocker on the target
       computers only after the target operating system is completely deployed.

     Tip

    Create the task sequence for deploying to the reference computer based on
    the Standard Client Task Sequence template, included in MDT.

4. Customize the MDT configuration files to the needs of your organization as
  described in Configuring MDT Deployments.

5. Configure any Windows PE options for the deployment share as described in:

       Configure the Deployment Share Properties Windows PE x86 Settings Tab

       Configure the Deployment Share Properties Windows PE x86 Components
       Tab

       Configure the Deployment Share Properties Windows PE x64 Settings Tab

       Configure the Deployment Share Properties Windows PE x64 Components
       Tab

<!-- p.63 -->

   6. Update the deployment share to create the Windows PE images used to start LTI
     deployment as described in Update a Deployment Share in the Deployment
     Workbench.

Deploying To and Capturing an Image of the Reference
Computer in LTI
After you have configured the deployment share, updated the deployment share, and
created the Windows PE images that include the LTI scripts, start the reference computer
with the Windows PE image, and complete the Deployment Wizard. The task sequence
you created earlier in the process will deploy the target operating system, device drivers,
operating system packages, and applications to the reference computer, and then
capture an image of the reference computer.

To deploy to and capture an image of the reference computer

   1. Create the LTI bootable media used to start the reference computer as described in
     Create the LTI Bootable Media.

   2. Complete the Deployment Wizard to deploy and capture an image of the
     reference computer as described in Complete the Deployment Wizard.

   3. Add the captured reference computer image to the Operating Systems node in the
     Deployment Workbench as described in Add the Captured Image of the Reference
     Computer to the Deployment Workbench.

Create the LTI Bootable Media

You must provide a method for starting the computer with the customized version of
Windows PE you created when you updated the deployment share. The Deployment
Workbench creates the LiteTouchPE_x86.iso and LiteTouchPE_x86.wim files (for 32-bit
target computers) or the LiteTouchPE_x64.iso and LiteTouchPE_x64.wim files (for 64-bit
target computers) in the deployment_share\Boot folder (where deployment_share is the
network shared folder used as the deployment share). Create the appropriate LTI
bootable media from one of these images.

To create the LTI bootable media

   1. In Windows Explorer, go to deployment_share\Boot (where deployment_share is the
     network shared folder used as the deployment share).

<!-- p.64 -->

        Tip

       To determine the location of the deployment share, view the properties of the
       share in the Deployment Workbench.

   2. Based on the type of computer used for the reference computer, perform one of
     the following tasks:

            If the reference computer is a physical computer, create a UFD, CD, or DVD of
            the ISO file.

            If the reference computer is a VM, start the VM directly from the ISO file or
            from a CD or DVD of the ISO file.

Complete the Deployment Wizard

Start the reference computer with the LTI bootable media you created earlier in the
process. The LTI bootable media starts Windows PE on the reference computer and
initiates the deployment process. At the end of the process, the target operating system
is deployed on the reference computer, and an image of the reference computer is
captured.

  ７ Note

  You could also initiate the process by starting the target computer from Windows
  Deployment Services. For more information, see Preparing Windows Deployment
  Services for LTI Deployments.

To complete the Deployment Wizard

   1. Start the reference computer with the LTI bootable media you created earlier in the
     process.

     Windows PE starts, and then the Deployment Wizard starts.

   2. Complete the Deployment Wizard as described in Running the Deployment
     Wizard, ensuring that you specifically follow the configuration settings on the
     wizard pages listed in Table 11 and selecting the values on the other wizard pages
     appropriate to your organization.

<!-- p.65 -->

     Table 11. Information for Completing the Deployment
     Wizard

                                                                              ﾉ   Expand table

      On this wizard       Do this
      page

      Select a task        Select the task sequence you created for the reference computer
      sequence to          deployment.
      execute on this
      computer

      Join the computer    Join a workgroup.
      to a domain or
      workgroup            Joining the reference computer to a domain causes problems when
                           deploying the captured image of the reference computer to target
                           computers. The most common symptom of trouble is that the
                           deployment process halts, because the LTI process is not able to
                           automatically log on.

      Specify whether to   Select Capture an image of this reference computer, and provide
      capture an image     the fully qualified Universal Naming Convention (UNC) path for the
                           name of the captured Windows Imaging Format (WIM) image,
                           including the WIM file name.

     The wizard starts, and the operating system deployment starts. At the end of the
     deployment process, the Deployment Summary dialog box appears.

   3. In the Deployment Summary dialog box, select Details.

     If any errors or warnings occur, review them, and record any diagnostic
     information. For more information about the errors or warnings, see the MDT
     document Troubleshooting Reference.

   4. In the Deployment Summary dialog box, select Finish.

     The reference computer is now deployed, and the captured WIM file of the
     reference computer is stored in the location you specified on the Specify whether
     to capture an image wizard page.

Add the Captured Image of the Reference Computer to the
Deployment Workbench
To deploy the captured image of the reference computer to the target computer, add
the captured image to the list of operating systems in the Operating Systems node in

<!-- p.66 -->

the Deployment Workbench. The Import Operating System Wizard copies the operating
system files to the deployment_share\Operating Systems\operating_system folder (where
deployment_share is the deployment share folder created earlier in the process and
operating_system is the name of the operating system added to the deployment share).

Add the captured image of the reference computer by completing the operating system
import process as described in Import a Previously Captured Image of a Reference
Computer, ensuring that you specifically follow the configuration settings on the wizard
pages listed in Table 12 and selecting the values on the other wizard pages that are
appropriate to your organization.

Table 12. Information for Completing the Importing a
Previously Captured Image of a Reference Computer

                                                                                  ﾉ   Expand table

 On this wizard   Do this
 page

 Image            In Source File, specify the fully qualified path to the WIM file of the captured
                  image of the reference computer.

The Import Operating System Wizard finishes. The captured image of the reference
computer is added to the list of operating systems in the information pane and is
copied to the deployment share.

Preparing for LTI Deployment to Target Computers
With the images of the reference computer captured, deploy the images to the target
computers. In preparation, create one or more task sequences for deploying the
captured images, ensure that the necessary deployment resources exist, and customize
the deployment process.

To prepare for deployment to the target computers

   1. Prepare network shares for storing migration data and MDT deployment logs as
     described in Preparing the MDT Migration Resources.

   2. Create additional deployment shares to help in larger deployments as described in
     Create a New Deployment Share in the Deployment Workbench.

<!-- p.67 -->

   3. Optionally, prepare Windows Deployment Services to start the appropriate
     Windows PE images that will in turn start LTI deployment to the target computers
     as described in Preparing Windows Deployment Services for LTI Deployments (if
     you are using Windows Deployment Services to start the process).

   4. Prepare the MDT task sequences, the MDT configuration files, and the MDT DB for
     each deployment scenario as described in:

          Prepare for the New Computer Deployment Scenario to Target Computers
          Using LTI

          Prepare for a Refresh Computer Deployment Scenario to Target Computers
          Using LTI

          Prepare for a Replace Computer Deployment Scenario to Target Computers
          Using LTI

          Depending on the target computers in your organization, any combination of
          the deployments scenarios might be necessary. For more information about
          the MDT deployment scenarios, see Identifying Deployment Scenarios.

Prepare for the New Computer Deployment Scenario to Target
Computers Using LTI

In the New Computer deployment scenario, a new installation of a Windows operating
system is deployed to a new computer. There is no user migration information to save
and restore and no existing file systems to preserve. Use the Standard Client Task
Sequence or Standard Server Task Sequence templates to deploy the captured image of
the reference computer to the target computer.

To prepare for the New Computer deployment scenario

   1. Create a new task sequence that will deploy the captured image of the reference
     computer to the target computer as described in the following list, ensuring that
     you specifically follow the configuration settings on the wizard pages listed in
     Table 13 and select the values on the other wizard pages appropriate to your
     organization:

          Configuring Task Sequences in the Deployment Workbench

          Configuring LTI Task Sequence Steps in the Deployment Workbench

        Tip

<!-- p.68 -->

    Create the task sequence for deploying to the target computer based on the
    Standard Client Task Sequence or Standard Server Task Sequence templates
    included in MDT.

  Table 13. Information for Completing the New Task
  Sequence Wizard for Performing New Computer
  Deployment Scenario

                                                                        ﾉ   Expand table

   On this wizard page     Do this

   Select OS               Select the captured image of the reference computer.

2. Customize the MDT configuration files to the needs of your organization as
  described in Configuring MDT Deployments.

3. Optionally, customize the MDT DB to the needs of your organization as described
  in Performing Deployments Using the MDT DB (if you are using the MDT DB to
  provide MDT configuration information).

4. Verify the Windows PE options for each deployment share as described in:

       Configure the Deployment Share Properties Windows PE x86 Settings Tab

       Configure the Deployment Share Properties Windows PE x86 Components
       Tab

       Configure the Deployment Share Properties Windows PE x64 Settings Tab

       Configure the Deployment Share Properties Windows PE x64 Components
       Tab

5. Update each deployment share, linked deployment share, and media to create the
  Windows PE images used to start LTI deployment as described in:

       Update a Deployment Share in the Deployment Workbench

       Replicate Linked Deployment Shares in the Deployment Workbench

       Generate Media Images in the Deployment Workbench

<!-- p.69 -->

Prepare for a Refresh Computer Deployment Scenario to Target
Computers Using LTI

In the Refresh Computer deployment scenario, a computer is refreshed—that is, re-
imaged for image standardization or to address a problem. You must save and restore
the user migration information, because the existing file systems on the target computer
are not preserved. Use the Standard Client Task Sequence or Standard Server Task
Sequence templates to deploy the captured image of the reference computer to the
target computer.

To prepare for the Refresh Computer deployment scenario

   1. Create a new task sequence that will deploy the captured image of the reference
     computer to the target computer as described in the following list, ensuring that
     you specifically follow the configuration settings on the wizard pages listed in
     Table 14 and select the values on the other wizard pages that are appropriate to
     your organization:

          Configuring Task Sequences in the Deployment Workbench

          Configuring LTI Task Sequence Steps in the Deployment Workbench

        Tip

       Create the task sequence for deploying images to the target computer based
       on the Standard Client Task Sequence or Standard Server Task Sequence
       templates included in MDT.

     Table 14. Information for Completing the New Task
     Sequence Wizard for Performing a Refresh Computer
     Deployment Scenario

                                                                           ﾉ   Expand table

      On this wizard page      Do this

      Select OS                Select the captured image of the reference computer.

   2. Customize the MDT configuration files to the needs of your organization as
     described in Configuring MDT Deployments.

<!-- p.70 -->

   3. Optionally, customize the MDT DB to the needs of your organization as described
     in Performing Deployments Using the MDT DB (if you are using the MDT DB to
     provide MDT configuration information).

   4. Verify the Windows PE options for each deployment share as described in:

          Configure the Deployment Share Properties Windows PE x86 Settings Tab

          Configure the Deployment Share Properties Windows PE x86 Components
          Tab

          Configure the Deployment Share Properties Windows PE x64 Settings Tab

          Configure the Deployment Share Properties Windows PE x64 Components
          Tab

   5. Update each deployment share, linked deployment share, and media to create the
     Windows PE images used to start LTI deployment as described in:

          Update a Deployment Share in the Deployment Workbench

          Replicate Linked Deployment Shares in the Deployment Workbench

          Generate Media Images in the Deployment Workbench

Prepare for a Replace Computer Deployment Scenario to Target
Computers Using LTI

In the Replace Computer deployment scenario, one computer replaces another
computer. The existing user state migration data is saved from the original computer to
a network shared folder or removable media. Then, a new installation of Windows is
deployed to a new computer. Finally, the user state data is restored to the new
computer, because the file systems on the new computer are formatted as part of the
new installation of Windows. Use the:

     Standard Client Replace Task Sequence template to save the user state migration
     data of the existing target computer

       ） Important

       Run this task sequence on the existing target computer before running the
       task sequence based on the Standard Client Task Sequence template on the
       new target computer.

<!-- p.71 -->

    Standard Client Task Sequence template to deploy the captured image of the
    reference computer to the new target computer and restore the user state
    migration data

      ） Important

      Run this task sequence on the new target computer after running the task
      sequence based on the Standard Client Replace Task Sequence template on
      the existing target computer.

To prepare for the Replace Computer deployment scenario

  1. Create a new task sequence that will save the user state migration data of the
    existing target computer as described in:

         Configuring Task Sequences in the Deployment Workbench

         Configuring LTI Task Sequence Steps in the Deployment Workbench

       Tip

      Create the task sequence for capturing the user state of the existing target
      computer based on the Standard Client Task Replace Sequence template
      included in MDT.

  2. Create a new task sequence that will deploy the captured image of the reference
    computer to the new target computer and restore the user state migration data
    saved by the task sequence in the previous step as described in the following list,
    ensuring that you specifically follow the configuration settings on the wizard pages
    listed in Table 15 and select the values on the other wizard pages that are
    appropriate to your organization:

         Configuring Task Sequences in the Deployment Workbench

         Configuring LTI Task Sequence Steps in the Deployment Workbench

       Tip

      Create the task sequence for deploying to the new target computer based on
      the Standard Client Task Sequence template, included in MDT.

<!-- p.72 -->

     Table 15. Information for Completing the New Task
     Sequence Wizard for Performing the Refresh
     Computer Deployment Scenario

                                                                           ﾉ   Expand table

      On this wizard page     Do this

      Select OS               Select the captured image of the reference computer.

   3. Customize the MDT configuration files to the needs of your organization as
     described in Configuring MDT Deployments.

   4. Optionally, customize the MDT DB to the needs of your organization as described
     in Performing Deployments Using the MDT DB (if you are using the MDT DB to
     provide MDT configuration information).

   5. Verify the Windows PE options for each deployment share as described in:

          Configure the Deployment Share Properties Windows PE x86 Settings Tab

          Configure the Deployment Share Properties Windows PE x86 Components
          Tab

          Configure the Deployment Share Properties Windows PE x64 Settings Tab

          Configure the Deployment Share Properties Windows PE x64 Components
          Tab

   6. Update each deployment share, linked deployment share, and media to create the
     Windows PE images used to start LTI deployment as described in:

          Update a Deployment Share in the Deployment Workbench

          Replicate Linked Deployment Shares in the Deployment Workbench

          Generate Media Images in the Deployment Workbench

Deploying Captured Images to Target Computers in LTI
The deployment of the captured images to the target computers is slightly different for
LTI. Deploy the captured image of the reference computer to target computers for each
of the deployment scenarios in your organization as described in:

<!-- p.73 -->

     Deploy Captured Images to Target Computers in the New Computer Deployment
     Scenario Using LTI

     Deploy Captured Images to Target Computers in a Refresh Computer Deployment
     Scenario Using LTI

     Deploy Captured Images to Target Computers in a Replace Computer Deployment
     Scenario Using LTI

     Depending on the target computers in your organization, any combination of the
     deployment scenarios might be necessary. For more information about the MDT
     deployment scenarios, see Identifying Deployment Scenarios.

Deploy Captured Images to Target Computers in the New
Computer Deployment Scenario Using LTI
Start the target computer with the LTI bootable media you created earlier in the process
or from Windows Deployment Services. The LTI bootable media starts Windows PE on
the target computer and initiates deployment. At the end of the process, the captured
image of the reference computer is deployed on the target computers.

To complete the Deployment Wizard

   1. Start the reference computer with the LTI bootable media you created earlier in the
     process or from Windows Deployment Services.

     Windows PE starts, and then the Deployment Wizard starts.

   2. Complete the Deployment Wizard as described in Running the Deployment
     Wizard, ensuring that you specifically follow the configuration settings on the
     wizard pages listed in Table 16 and select the values on the other wizard pages
     appropriate to your organization.

     Table 16. Information for Completing the Deployment
     Wizard for the New Computer Deployment Scenario
     Using LTI

                                                                        ﾉ   Expand table

<!-- p.74 -->

      On this wizard page          Do this

      Select a task sequence to    Select the task sequence you created for the target
      execute on this computer     computer deployment for the New Computer deployment
                                   scenario.

     The wizard starts, and the operating system deployment starts. At the end of the
     process, the Deployment Summary dialog box appears.

   3. In the Deployment Summary dialog box, select Details.

     If any errors or warnings occur, review them, and record any diagnostic
     information. For more information about the errors or warnings, see the MDT
     document Troubleshooting Reference.

   4. In the Deployment Summary dialog box, select Finish.

     The target computers are now deployed.

Deploy Captured Images to Target Computers in a Refresh
Computer Deployment Scenario Using LTI

Start the Deployment Wizard on the existing operating system on the target computer
to start the Standard Client task sequence or Standard Server task sequence created
earlier in the process. The Deployment Wizard saves the user state migration data of the
existing target computer to the location you specify. Later in the task sequence, the user
state migration data is restored to the target computer.

To complete the Deployment Wizard

   1. Start the Deployment Wizard by connecting to the appropriate deployment share
     (for example, \\server_name\Distribution$\Scripts) and typing cscript litetouch.vbs.

     The Deployment Wizard starts.

   2. Complete the Deployment Wizard as described in Running the Deployment
     Wizard, ensuring that you specifically follow the configuration settings on the
     wizard pages listed in Table 17 and select the values on the other wizard pages
     appropriate to your organization.

     Table 17. Information for Completing the Deployment
     Wizard for the Refresh Computer Deployment
     Scenario Using LTI

<!-- p.75 -->

                                                                               ﾉ   Expand table

       On this wizard page          Do this

       Select a task sequence to    Select the task sequence you created for the target
       execute on this computer     computer deployment for the Refresh Computer
                                    deployment scenario.

       Choose a migration type.     Select Refresh this computer.

       Specify where to save your   Select one of the following options based on the
       data and settings.           requirements of your organization:

                                    - Automatically determine the location

                                    - Specify a location

     The wizard starts, and the operating system deployment starts. At the end of the
     process, the Deployment Summary dialog box appears.

   3. In the Deployment Summary dialog box, select Details.

     If any errors or warnings occur, review them, and record any diagnostic
     information. For more information about the errors or warnings, see the MDT
     document Troubleshooting Reference.

   4. In the Deployment Summary dialog box, select Finish.

     The target computer is now deployed.

Deploy Captured Images to Target Computers in a Replace
Computer Deployment Scenario Using LTI
The Replace Computer deployment scenario requires that you run the Deployment
Wizard twice. Run the wizard the first time to capture the user state migration data from
the existing target computer (old computer). Then, run it again to deploy the captured
image of the reference computer to the new target computer (new computer) and
restore the user state saved earlier in the process.

Ensure that the user state migration data is stored in a consistent and secure location so
that the data can be readily restore later in the LTI process.

To deploy captured images of the reference computer

<!-- p.76 -->

   1. Save the user state migration data from the existing target computer as described
     in Save the User State Migration Data from the Existing Target Computer Using LTI.

   2. Deploy the captured image of the reference computer to the new target computer
     as described in Deploy the Captured Image of the Reference Computer to the New
     Target Computer Using LTI.

Save the User State Migration Data from the Existing Target
Computer Using LTI

Start the Deployment Wizard on the existing operating system on the target computer
to start the Standard Client Replace Task Sequence template created earlier in the
process. The Deployment Wizard saves the user state migration data of the existing
target computer to the location you specify.

To complete the Deployment Wizard

   1. Start the Deployment Wizard by connecting to the appropriate deployment share
     (for example, \\server_name\Distribution$\Scripts) and typing cscript litetouch.vbs.

     The Deployment Wizard starts.

   2. Complete the Deployment Wizard as described in Running the Deployment
     Wizard, ensuring that you specifically follow the configuration settings on the
     wizard pages listed in Table 18 and select the values on the other wizard pages
     that are appropriate to your organization.

     Table 18. Information for Completing the Deployment
     Wizard for the Replace Computer Deployment
     Scenario for Saving User State Migration Data Using
     LTI

                                                                             ﾉ   Expand table

      On this wizard      Do this
      page

      Select a task       Select the task sequence you created for the target computer in the
      sequence to         Replace Computer deployment scenario to save the user state
      execute on this     migration data.
      computer

<!-- p.77 -->

      On this wizard      Do this
      page

      Specify where to    In the Location box, type the fully qualified path to the location in
      save your data      which you want to store the user state migration data. This location
      and settings.       must be accessible to the new target computer.

      Specify where to    Select Specify a location, and then type the fully qualified path to the
      save a complete     location in which you want to store the backup.
      computer backup
                          This backup is for use in restoring user state migration data that
                          might have been missed, not as a rollback method for the target
                          computer. If you want to have rollback capability for the target
                          computer, perform a full backup using your organization's backup
                          software.

     The wizard starts, and the operating system deployment starts. At the end of the
     process, the Deployment Summary dialog box appears.

   3. In the Deployment Summary dialog box, select Details.

     If any errors or warnings occur, review them, and record any diagnostic
     information. For more information about the errors or warnings, see the MDT
     document Troubleshooting Reference.

   4. In the Deployment Summary dialog box, select Finish.

     The user state migration data of the existing target computer is saved.

Deploy the Captured Image of the Reference Computer to the
New Target Computer Using LTI

Start the target computer with the LTI bootable media you created earlier in the process
or from Windows Deployment Services. The LTI bootable media starts Windows PE on
the target computer and initiates LTI deployment. At the end of the process, the
captured image of the reference computer is deployed to the target computer.

To deploy the captured image of the reference computer

   1. Start the reference computer with the LTI bootable media you created earlier in the
     process or from Windows Deployment Services.

     Windows PE starts, and then the Deployment Wizard starts.

   2. Complete the Deployment Wizard as described in Running the Deployment
     Wizard, ensuring that you specifically follow the configuration settings on the

<!-- p.78 -->

     wizard pages listed in Table 19 and select the values on the other wizard pages
     that are appropriate to your organization.

     Table 19. Information for Completing the Deployment
     Wizard for the Replace Computer Deployment
     Scenario for Deploying the Captured Image

                                                                              ﾉ   Expand table

      On this wizard page           Do this

      Select a task sequence to     Select the task sequence you created for the target
      execute on this computer      computer for the Replace Computer deployment scenario.

      Specify whether to restore    Select the Specify a location option and type the location
      user data                     of the saved user state migration data in the Location box.

     The wizard starts, and the operating system deployment starts. At the end of the
     process, the Deployment Summary dialog box appears.

   3. In the Deployment Summary dialog box, select Details.

     If any errors or warnings occur, review them, and record any diagnostic
     information. For more information about the errors or warnings, see the MDT
     document Troubleshooting Reference.

   4. In the Deployment Summary dialog box, select Finish.

Managing LTI Deployments in the Deployment
Workbench
Deployment shares are the repository for all the deployment files used in LTI
deployment. You can store a deployment share on a local drive, in a network shared
folder, or in a stand-alone distributed file system (DFS); it does not have to reside on any
specific computer. Deployment shares contain operating systems, applications,
operating system packages, and device drivers.

Manage LTI deployments in the Deployment Workbench by:

     Managing shares as described in Managing Deployment Shares in the Deployment
     Workbench

<!-- p.79 -->

     Configuring the operating systems as described in Configuring Operating Systems
     in the Deployment Workbench

     Configuring the applications to be deployed as described in Configuring
     Applications in the Deployment Workbench

     Configuring packages as described in Configuring Packages in the Deployment
     Workbench

     Configuring device drivers as described in Configuring Device Drivers in the
     Deployment Workbench

     Configuring task sequences as described in Configuring Task Sequences in the
     Deployment Workbench

     Performing common administrative tasks as described in Performing Common
     Management Tasks in the Deployment Workbench

     Performing advanced configuration tasks as described in Performing Advanced
     Configuration Tasks in the Deployment Workbench

     Performing common administrative tasks as described in Configuring LTI Task
     Sequence Steps in the Deployment Workbench

     In addtion to managing LTI deployments in the Deployment Workbench, you can
     manage LTI deployments using the MDT Windows PowerShell cmdlets. For more
     information on managing LTI deployments using the MDT Windows PowerShell
     cmdlets, see:

     The section, "MDT Windows PowerShell Cmdlets", in the MDT document, Toolkit
     Reference

     The section, "Managing MDT Using Windows PowerShell", in the MDT document,
     Microsoft Deployment Toolkit Samples Guide

Managing Deployment Shares in the Deployment
Workbench
MDT uses the Deployment Workbench to manage the deployment shares in your
organization. You configure the deployment shares by:

     Creating a new deployment share as described in Create a New Deployment Share
     in the Deployment Workbench

<!-- p.80 -->

     Opening an existing deployment share as described in Open an Existing
     Deployment Share in the Deployment Workbench

     Upgrading an existing deployment share to MDT as described in Upgrade an
     Existing Deployment Share in the Deployment Workbench

     Configuring a deployment share as described in Configure a Deployment Share in
     the Deployment Workbench

     Copying a deployment share as described in Copy a Deployment Share

     Closing a deployment share as described in Close a Deployment Share in the
     Deployment Workbench

     Updating a deployment share as described in Update a Deployment Share in the
     Deployment Workbench

     Creating bootable devices to start LTI from the MDT boot images as described in
     Create Bootable Devices from MDT Boot Images

     In addtion to managing deployment shares in the Deployment Workbench, you
     can manage deployment shares using the MDT Windows PowerShell cmdlets. For
     more information on managing deployment shares using the MDT Windows
     PowerShell cmdlets, see the following sections beneath the section, "MDT
     Windows PowerShell Cmdlets", in the MDT document Toolkit Reference:

     Add-MDTPersistentDrive

     Get-MDTDeploymentShareStatistics

     Get-MDTPersistentDrive

     Remove-MDTPersistentDrive

     Restore-MDTPersistentDrive

     Update-MDTDeploymentShare

Create a New Deployment Share in the Deployment Workbench

To create a new deployment share, perform the following steps:

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.
