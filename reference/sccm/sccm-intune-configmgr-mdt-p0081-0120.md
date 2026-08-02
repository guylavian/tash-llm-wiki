---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 81-120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0081-0120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0081-0120
family: sccm
documentKind: "doc"
abstract: "2. In the Deployment Workbench console tree, go to Deployment Workbench/Deployment Shares. 3. In the Actions pane, select New Deployment Share. The New Deployment Share Wizard starts. 4. Complete the New Deployment Share Wizard using the information in Table 20. Table 20. Inform"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 81-120

<!-- p.81 -->

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares.

3. In the Actions pane, select New Deployment Share.

  The New Deployment Share Wizard starts.

4. Complete the New Deployment Share Wizard using the information in Table 20.

  Table 20. Information for Completing the New
  Deployment Share Wizard

                                                                              ﾉ   Expand table

   On this wizard   Do this
   page

   Path             In Deployment share path, type path (where path is the fully qualified
                    path to an existing folder on a local drive or a network shared folder
                    created earlier in the deployment process), and then select Next.

                    Alternatively, select Browse to find the existing folder on a local drive or
                    network shared folder.

   Share            This page is displayed only if you entered a path to a folder on a local
                    drive on the Path wizard page.

                    - In Share name, type share_name (where share_name is the share name
                    for the folder on a local drive specified on the Path wizard page).

                    - Note the fully qualified to UNC path to the share being created listed
                    immediately below the Share name box, and then select Next.

                    The wizard grants the local group Everyone Full Control access at the
                    share level. Based on your security requirements, you may want to
                    restrict the security of the share.

   Descriptive      In Deployment share description, type description (where description is
   Name             a descriptive name that for the deployment share specified on previous
                    wizard pages), and then select Next.

   Allow Image      Select or clear the Ask if an image should be captured check box based
   Capture          on requirements, and then select Next.

                    This check box configures the Deployment Wizard to allow the user to
                    optionally capture an image of the target computer, which is usually the
                    reference computer. If the check box is:

<!-- p.82 -->

 On this wizard   Do this
 page

                  - Selected, the path for storing the image and the image name can be
                  configured in the Deployment Wizard

                  - Cleared, an image is not capture or the image-capture information
                  must be set in the MDT configuration file or database

                  By default, this check box is selected.

 Allow Admin      Select or clear the Ask user to set the local Administrator Password
 Password         check box based on requirements, and then select Next.

                  This check box configures the Deployment Wizard to allow the user to
                  provide the password for the local Administrator account during the
                  deployment process. If the check box is:

                  - Selected, the password can be configured in the Deployment Wizard

                  - Cleared, the password must be set in the MDT configuration file or
                  database

                  By default, this check box is cleared.

 Allow Product    Select or clear the Ask user for a product key check box based on your
 Key              requirements, and then select Next.

                  This check box configures the Deployment Wizard to allow the user to
                  provide a product key for the target operating system during the
                  deployment process. If the check box is:

                  - Selected, the product key can be configured in the Deployment Wizard

                  - Cleared, the product key must be set in the MDT configuration file or
                  database

                  By default, this check box is cleared.

 Summary          Review the information in the Details box, and then select Next.

 Confirmation     Select Save Output to save the output of the wizard to a file, or select
                  View Script to view the Windows PowerShell scripts used to perform the
                  wizard tasks.

                  Select Close.

Upon completion, the new deployment share is created in the target folder you
selected in the wizard and appears in the Deployment Workbench.

<!-- p.83 -->

Open an Existing Deployment Share in the Deployment Workbench
The Deployment Workbench can open an existing deployment share using the Open
Deployment Share Wizard. Start the Open Deployment Share Wizard by:

     Right-clicking the Deployment Shares node, and then selectingOpen Deployment
     Share

     Selecting the Deployment Shares node, and then, from the Action menu,
     selectingOpen Deployment Share

     Selecting the Deployment Shares node, and then, in the Actions pane, selecting
     Open Deployment Share

To open an existing deployment share not already listed in the
Deployment Workbench

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

  3. In the Actions pane, select Open Deployment Share.

     The Open Deployment Share Wizard starts.

  4. Complete the Open Deployment Share Wizard using the information in Table 21.

     Table 21. Information for Completing the Open
     Deployment Share Wizard

                                                                               ﾉ   Expand table

      On this wizard   Do this
      page

      Path             a. In Deployment share path, type share_path (where share_path is the
                       fully qualified path to the existing deployment share).

                       You can alternatively select Browse to find the local or network shared
                       folder.

                       b. Select the **Upgrade the content of the deployment share (if
                       required)**check box. If the check box is:

<!-- p.84 -->

      On this wizard   Do this
      page

                       - Selected, the Open Deployment Share Wizard upgrades the
                       deployment share

                       - Cleared, the Open Deployment Share Wizard will not upgrade the
                       deployment share

                       c. Select Next.

      Summary          Review the information in the Details box, and then select Next.

      Confirmation     You can select Save Output to save the output of the wizard to a file. You
                       can also select View Script to view the Windows PowerShell scripts used
                       to perform the wizard tasks.

                       Select Finish.

Upgrade an Existing Deployment Share in the Deployment
Workbench
MDT can upgrade an existing deployment share by:

     Opening an existing deployment share that is not already listed in the Deployment
     Workbench as described in Upgrade Deployment Shares Not Already Listed in the
     Deployment Workbench

     Upgrading an existing deployment share that is listed in the Deployment
     Workbench as described in Upgrade Deployment Shares Already Listed in the
     Deployment Workbench

Upgrade Deployment Shares Not Already Listed in the
Deployment Workbench

Upgrade deployment shares not listed in the Deployment Workbench using the Open
Deployment Share Wizard. Start the wizard by:

     Right-clicking the deployment share, and then selecting Open Deployment Share

     Selecting the deployment share, and then, from the Actions menu, selecting Open
     Deployment Share

     Selecting the deployment share, and then, in the Actions pane, selecting Open
     Deployment Share

<!-- p.85 -->

  To upgrade deployment shares that are not already listed in the Deployment
  Workbench, perform the following steps:

1. Select Start, and then point to All Programs. Point to Microsoft Deployment
  Toolkit, and then select Deployment Workbench.

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares.

3. In the Actions pane, select Open Deployment Share.

  The Open Deployment Share Wizard starts.

4. Complete the Open Deployment Share Wizard using the information in Table 22.

  Table 22. Information for Completing the Open
  Deployment Share Wizard

                                                                             ﾉ   Expand table

   On this wizard   Do this
   page

   Path             - In Deployment share path, type share_path (where share_path is the
                    fully qualified path to the existing deployment share).

                    Alternatively, select Browse to find the local or network shared folder.

                    - Select the Upgrade the content of the deployment share (if required)
                    check box, and then select Next.

   Summary          Review the information in the Details box, and then select Next.

   Confirmation     Select Save Output to save the output of the wizard to a file, or select
                    View Script to view the Windows PowerShell scripts used to perform the
                    wizard tasks.

                    Select Finish.

  After the wizard finishes, the existing deployment share is upgraded (if required),
  and the Upgrade the content of the deployment share (if required) check box is
  selected. The deployment share is added to the details pane in the Deployment
  Workbench.

  In addition to upgrading existing deployment shares, any existing installations of
  previous versions of MDT must be upgraded to MDT. For more information on

<!-- p.86 -->

     upgrading any previous installations to MDT, see Upgrading to MDT.

Upgrade Deployment Shares Already Listed in the Deployment
Workbench

Upgrade existing deployment shares already listed in the Deployment Workbench using
the Upgrade Deployment Share Wizard. Start the wizard by:

     Right-clicking the deployment share, and then selecting Upgrade Deployment
     Share

     Selecting the deployment share, and then, from the Actions menu, selecting
     Upgrade Deployment Share

     Selecting the deployment share, and then, in the Actions pane, selecting Upgrade
     Deployment Share

     To upgrade existing deployment shares already listed in the Deployment
     Workbench, perform the following steps:

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

  3. In the Actions pane, select Upgrade Deployment Share.

     The Upgrade Deployment Share Wizard starts.

  4. Complete the Upgrade Deployment Share Wizard using the information in Table
     23.

     Table 23. Information for Completing the Upgrade
     Deployment Share Wizard

                                                                               ﾉ   Expand table

      On this wizard   Do this
      page

      Summary          Review the information in the Details box, and then select Next.

      Confirmation     Select Save Output to save the output of the wizard to a file, or select
                       View Script to view the Windows PowerShell scripts used to perform the

<!-- p.87 -->

      On this wizard   Do this
      page

                       wizard tasks.

                       Select Finish.

     After the wizard finishes, the existing deployment share is upgraded and now can
     be accessed in the Deployment Workbench.

Configure a Deployment Share in the Deployment Workbench
You can view the properties of deployment shares beneath the Deployment Shares node
in the Deployment Workbench by using the Properties actions as described in View
Item Properties in the Deployment Workbench.

Configure an application in the Deployment Workbench by performing the following
tasks in the Application Properties dialog box:

     Configure the settings on the General tab as described in Configure the
     Deployment Share Properties General Tab.

     Configure the settings on the Rules tab as described in Configure the Deployment
     Share Properties Rules Tab.

     Configure the settings on the Windows PE x86 Settings tab as described in
     Configure the Deployment Share Properties Windows PE x86 Settings Tab.

     Configure the settings on the Windows PE x86 Components tab as described in
     Configure the Deployment Share Properties Windows PE x86 Components Tab.

     Configure the settings on the Windows PE x64 Settings tab as described in
     Configure the Deployment Share Properties Windows PE x64 Settings Tab.

     Configure the settings on the Windows PE x64 Components tab as described in
     Configure the Deployment Share Properties Windows PE x64 Components Tab.

Configure the Deployment Share Properties General Tab

The deployment share properties stored on the General tab are mostly configured when
you run the New Deployment Share Wizard. You can update the deployment share
properties on the General tab through the deployment_share Properties dialog box
(where deployment_share is the name of the deployment share in the Deployment
Workbench).

<!-- p.88 -->

To configure the General tab

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
    Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
    Workbench/Deployment Shares.

  3. In the details pane, select deployment_share (where deployment_share is the name
    of the deployment share).

  4. In the Actions pane, select Properties.

    The deployment_share Properties* dialog box opens (where deployment_share is
    the name of the deployment share you want to configure).

  5. On the General tab, configure the settings listed in Table 24 based on the
    requirements of your organization, and then select OK.

    Table 24. Configuration Settings on the General Tab of
    Deployment Share Properties

                                                                               ﾉ    Expand table

     Setting           Description

     Description       Contains the name of the deployment share displayed in the
                       Deployment Workbench. The default value is MDT Deployment Share.

     Comments          Provides information about the deployment share.

     Network (UNC)     Text box that contains fully qualified UNC path to the deployment share.
     path              This value is used only to enable multicast and is required if you want to
                       do so by selecting the Enable multicast for this deployment share
                       check box.

                       If the deployment share was created from an existing network shared
                       folder, this value is displayed in the details pane of the Deployment
                       Workbench.

     Local path        Contains the fully qualified path to the local folder in which the
                       deployment share was created. This value is used only to enable
                       multicast and is required if you want to do so by selecting the Enable
                       multicast for this deployment share check box. If you created the
                       deployment share from:

                       - A local path, then this text box contains the local path used in the

<!-- p.89 -->

      Setting            Description

                         creation process

                         - An existing network shared folder, then this text box is empty

                         If you created the deployment share from a local path, the local path
                         rather than the UNC path is displayed in the details pane of the
                         Deployment Workbench.

      Platforms          Select to configure the Update Deployment Share Wizard to create
      supported: x86     WIM files and bootable media for 32-bit target computers.

      Platforms          Select to configure the Update Deployment Share Wizard to create
      supported: x64     WIM files and bootable media for 64-bit target computers.

      Enable multicast   Select to configure Windows Deployment Services to enable multicast
      for this           deployment of images generated in this deployment share. If you select
      deployment         this check box, you must provide values for the Network (UNC) path
      share              and Local path boxes. For more information about enabling multicast-
                         based deployments, see Enable Windows Deployment Services
                         Multicast Deployment for LTI Deployments.

                         The multicast features of MDT are available using Windows Deployment
                         Services in Windows Server.

     The deployment share configuration settings are saved, and the deployment share
     appears in the details pane of the Deployment Workbench.

Configure the Deployment Share Properties Rules Tab

The deployment share properties stored on the Rules tab are mostly configured when
you run the New Deployment Share Wizard. These settings reside in CustomSettings.ini,
which is in the deployment share's Control folder. For more information about the
settings that you can configure on this tab, see the MDT document Toolkit Reference.

To configure the Rules tab

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

   3. In the details pane, select deployment_share (where deployment_share is the name
     of the deployment share).

<!-- p.90 -->

  4. In the Actions pane, select Properties.

     The deployment_share Properties dialog box opens (where deployment_share is
     the name of the deployment share you want to configure).

  5. On the Rules tab, configure the settings listed in Table 25 based on the
     requirements of your organization, and then select OK.

     Table 25. Configuration Settings on the Rules Tab of
     Deployment Share Properties

                                                                                 ﾉ    Expand table

      Setting              Description

      CustomSettings.ini   Contains the current configuration of the CustomSetting.ini file for the
                           deployment share.

      Edit Bootstrap.ini   Select to modify the contents of the Bootstrap.ini file that the
                           Deployment Workbench generates.

     The deployment share configuration settings are saved, and the deployment share
     appears in the details pane of the Deployment Workbench.

Configure the Deployment Share Properties Windows PE x86
Settings Tab

The deployment share properties stored on the Windows PE x86 Settings tab are
mostly configured when you run the New Deployment Share Wizard.

To configure the Windows PE x86 Settings tab

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

  3. In the details pane, select deployment_share (where deployment_share is the name
     of the deployment share).

  4. In the Actions pane, select Properties.

<!-- p.91 -->

  The *deployment_shareProperties dialog box opens (where deployment_share is the
  name of the deployment share you want to configure).

5. On the Windows PE x86 Settings tab, configure the settings listed in REF
  _Ref304458789 \h Table 26 based on the requirements of your organization, and
  then select OK.

  Table 26. Configuration Settings on the Windows PE
  x86 Settings Tab of Deployment Share Properties

                                                                           ﾉ   Expand table

   Setting           Description

   Generate a Lite   Select to configure the Update Deployment Share Wizard to create a
   Touch Windows     Windows PE WIM file that includes the LTI deployment scripts. If the
   PE WIM file       check box is:

                     - Selected, the Update Deployment Share Wizard creates the
                     LiteTouchPE_x86.wim file with the image description specified in the
                     Image description text box

                     - Cleared, the Update Deployment Share Wizard will not create the
                     WIM file

   Image             Contains the image description for the Windows PE WIM file that the
   description       Update Deployment Share Wizard creates. The default value is Lite
                     Touch Windows PE (x86).

   Generate a Lite   Select to configure the Update Deployment Share Wizard to create a
   Touch bootable    bootable Windows PE ISO file that includes the LTI deployment scripts.
   ISO image         If the check box is:

                     - Selected, the Update Deployment Share Wizard creates the ISO file
                     with the name specified in the ISO file name text box

                     - Cleared, the Update Deployment Share Wizard will not create the ISO
                     file

   ISO file name     Contains the file name for the Windows PE ISO file that the Update
                     Deployment Share Wizard creates. The default value for this text box is
                     LiteTouchPE_x86.iso.

                     This text box is enabled only if you select Generate a Lite Touch
                     bootable ISO image.

   Generate a        Select to configure the Update Deployment Share Wizard to create a
   generic Windows   Windows PE WIM file that does not include the LTI deployment scripts.

<!-- p.92 -->

Setting              Description

PE WIM file          If the check box is:

                     - Selected, the Update Deployment Share Wizard creates the
                     GenericPE_x86.wim file with the image description specified in the
                     Image description text box

                     - Cleared, the Update Deployment Share Wizard will not create the
                     WIM file

Image                Contains the image description for the generic Windows PE WIM file
description          that the Update Deployment Share Wizard creates. The default value
                     for this text box is Generic Windows PE (x86).

                     This text box is enabled only if you select Generate a generic
                     Windows PE WIM file.

Generate a           Select to configure the Update Deployment Share Wizard to create a
generic bootable     bootable Windows PE ISO file that does not include the LTI
ISO image            deployment scripts. If the check box is:

                     - Selected, the Update Deployment Share Wizard creates the
                     Generic_x86.iso file with the image description specified in the ISO file
                     name text box

                     - Cleared, the Update Deployment Share Wizard will not create the ISO
                     file

                     This box is enabled only if you select Generate a generic Windows PE
                     WIM file.

ISO file name        Contains the file name for the generic Windows PE ISO file that the
                     Update Deployment Share Wizard creates. The default value for this
                     text box is Generic_x86.iso.

                     This text box is enabled only if you select Generate a generic bootable
                     ISO image.

Custom               Contains the fully qualified path to the BMP file that is to be used as
background           the custom background bitmap. The default value for this text box is
bitmap file          %INSTALLDIR%\Samples\Background.bmp.

Extra directories    Contains the fully qualified path to a folder structure to be included in
to add               the Windows PE images. The default value for the text box is empty.

Scratch space size   Configures the size of the scratch space in megabytes; you can select a
                     value of 32, 64, 128, 256, or 512 MB. The default value is 32.

<!-- p.93 -->

    The deployment share configuration settings are saved, and the deployment share
    appears in the details pane of the Deployment Workbench.

Configure the Deployment Share Properties Windows PE x86
Components Tab

The deployment share properties stored on the Windows PE x86 Components tab are
mostly configured when you run the New Deployment Share Wizard.

To configure the Windows PE x86 Components tab

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
    Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
    Workbench/Deployment Shares.

  3. In the details pane, select deployment_share (where deployment_share is the name
    of the deployment share).

  4. In the Actions pane, select Properties.

    The deployment_share Properties** dialog box opens (where deployment_share is
    the name of the deployment share you want to configure).

  5. On the Windows PE x86 Components tab, configure the settings listed in Table 29
    based on the requirements of your organization, and then select OK.

    Table 27. Configuration Settings on the Windows PE
    x86 Components Tab of Deployment Share Properties

                                                                                   ﾉ   Expand table

      Setting               Description

      Selection profile     Use to select the device drivers and packages to be included in the
                            Windows PE images based on the selection profile you choose. The
                            default value is All Drivers and Packages. For more information
                            about selection profiles, see Manage Selection Profiles.

      Include all drivers   Select to configure the Update Deployment Share Wizard to include
      from the selected     all the device drivers in the selection profile specified in the Selection
      driver group          profile box.

<!-- p.94 -->

Setting               Description

Include only          Select to configure the Update Deployment Share Wizard to include
drivers of the        only the device drivers in the chosen selection profile that are
following types       specified in the following check boxes:

                      - Include all network drivers in the selected group

                      - Include all video drivers in the selected group

                      - Include all mass storage drivers in the selected group

                      - Include all system-class drivers in the selected group

Include all network   Select to configure the Update Deployment Share Wizard to include
drivers in the        all network drivers in the chosen selection profile. If the check box is:
selected group
                      - Selected, the Update Deployment Share Wizard includes all
                      network drivers in the selection profile specified in the Selection
                      profile box in the Windows PE images

                      - Cleared, the Update Deployment Share Wizard will not include all
                      network drivers in the selection profile specified in the Selection
                      profile box in the Windows PE images

                      This check box is enabled only if you select Include only drivers of
                      the following types.

Include all video     Select to configure the Update Deployment Share Wizard to include
drivers in the        all video drivers in the chosen selection profile. If the check box is:
selected group
                      - Selected, the Update Deployment Share Wizard includes all video
                      drivers in the selection profile specified in the Selection profile box
                      in the Windows PE images

                      - Cleared, the Update Deployment Share Wizard will not include all
                      video drivers in the selection profile specified in the Selection profile
                      list box in the Windows PE images

                      This check box is enabled only if you select Include only drivers of
                      the following types.

Include all mass      Select to configure the Update Deployment Share Wizard to include
storage drivers in    all mass storage drivers in chosen the selection profile. If the check
the selected group    box is:

                      - Selected, the Update Deployment Share Wizard includes all mass
                      storage drivers in the selection profile specified in the Selection
                      profile box in the Windows PE images

<!-- p.95 -->

Setting                Description

                       - Cleared, the Update Deployment Share Wizard will not include all
                       mass storage drivers in the selection profile specified in the Selection
                       profile box in the Windows PE images

                       This check box is enabled only if you select Include only drivers of
                       the following types.

Include all system-    Select to configure the Update Deployment Share Wizard to include
class drivers in the   all system-class drivers in the chosen selection profile. If the check
selected group         box is:

                       - Selected, the Update Deployment Share Wizard includes all system-
                       class drivers in the selection profile specified in the Selection profile
                       box in the Windows PE images

                       - Cleared, the Update Deployment Share Wizard will not include all
                       system-class drivers in the selection profile specified in the Selection
                       profile box in the Windows PE images

                       This check box is enabled only if you select Include only drivers of
                       the following types.

ADO                    Select to add optional ADO components to the Windows PE images.
                       These components are necessary for accessing Microsoft SQL
                       Server® databases, such as the MDT DB. If the check box is:

                       - Selected, the ADO components are added to the Windows PE
                       images

                       - Cleared, the ADO components are not added to the Windows PE
                       images

Optional Fonts         Select to configure the Update Deployment Share Wizard to include
                       the following fonts:

                       - Chinese (ZH-CN)

                       - Chinese (ZH-HK)

                       - Chinese (ZH-TW)

                       - Japanese (JA-JP)

                       - Korean (KO-KR)

                       Add these fonts when performing an LTI deployment of Windows
                       Server images and the Setup files are Japanese, Korean, or Chinese. If
                       the check box for a corresponding font is:

<!-- p.96 -->

      Setting             Description

                          - Selected, the Update Deployment Share Wizard includes the font in
                          the Windows PE images

                          - Cleared, the Update Deployment Share Wizard will not include the
                          font in the Windows PE images

                          Adding fonts to Windows PE boot images increases the size of the
                          images. Add fonts only if necessary.

     The deployment share configuration settings are saved, and the deployment share
     appears in the details pane of the Deployment Workbench.

Configure the Deployment Share Properties Windows PE x64
Settings Tab

The deployment share properties stored on the Windows PE x64 Settings tab are mostly
configured when you run the New Deployment Share Wizard.

To configure the Windows PE x64 Settings tab

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares.

  3. In the details pane, select deployment_share (where deployment_share is the name
     of the deployment share).

  4. In the Actions pane, select Properties.

     The deployment_share Properties dialog box opens (where deployment_share is
     the name of the deployment share you want to configure).

  5. On the Windows PE x64 Settings tab, configure the settings listed in Table 28
     based on the requirements of your organization, and then select OK.

     Table 28. Configuration Settings on the Windows PE
     x64 Settings Tab of Deployment Share Properties

                                                                            ﾉ   Expand table

<!-- p.97 -->

Setting           Description

Generate a Lite   Select to configure the Update Deployment Share Wizard to create a
Touch Windows     Windows PE WIM file that includes the LTI deployment scripts. If the
PE WIM file       check box is:

                  - Selected, the Update Deployment Share Wizard creates the
                  LiteTouchPE_x86.wim file with the image description specified in the
                  Image description box

                  - Cleared, the Update Deployment Share Wizard will not create the
                  WIM file

Image             Contains the image description for the Windows PE WIM file that the
description       Update Deployment Share Wizard creates. The default value is Lite
                  Touch Windows PE (x64).

Generate a Lite   Select to configure the Update Deployment Share Wizard to create a
Touch bootable    bootable Windows PE ISO file that includes the LTI deployment scripts.
ISO image         If the check box is:

                  - Selected, the Update Deployment Share Wizard creates the ISO file
                  with the name specified in the ISO file name box

                  - Cleared, the Update Deployment Share Wizard will not create the ISO
                  file

ISO file name     Contains the file name for the Windows PE ISO file that the Update
                  Deployment Share Wizard creates. The default value for this text box is
                  LiteTouchPE_x64.iso.

                  This box is enabled only if you select Generate a Lite Touch bootable
                  ISO image.

Generate a        Select to configure the Update Deployment Share Wizard to create a
generic Windows   Windows PE WIM file that does not include the LTI deployment scripts.
PE WIM file       If the check box is:

                  - Selected, the Update Deployment Share Wizard creates the
                  GenericPE_x64.wim file with the image description specified in the
                  Image description box

                  - Cleared, the Update Deployment Share Wizard will not create the
                  WIM file

Image             Contains the image description for the generic Windows PE WIM file
description       that the Update Deployment Share Wizard creates. The default value
                  for this text box is Generic Windows PE (x64).

<!-- p.98 -->

      Setting            Description

                         This box is enabled only if you select Generate a generic bootable ISO
                         Windows PE WIM file.

      Generate a         Select to configure the Update Deployment Share Wizard to create a
      generic bootable   bootable Windows PE ISO file that does not include the LTI
      ISO image          deployments scripts. If the check box is:

                         - Selected, the Update Deployment Share Wizard creates the
                         Generic_x64.iso file with the image description specified in the ISO file
                         name box

                         - Cleared, the Update Deployment Share Wizard will not create the ISO
                         file

                         This box is enabled only if you select Generate a generic Windows PE
                         WIM file.

      ISO file name      Contains the file name for the generic Windows PE ISO file that the
                         Update Deployment Share Wizard creates. The default value for this
                         text box is Generic_x64.iso.

                         This text box is enabled only if the Generate a generic bootable ISO
                         image check box is selected.

      Custom             Contains the fully qualified path to the BMP file that is to be used as
      background         the custom background bitmap. The default value for this text box is
      bitmap file        %INSTALLDIR%\Samples\Background.bmp.

      Custom             Contains the fully qualified path to a folder structure to be included in
      background         the Windows PE images. The default value for the text box is empty.
      bitmap file

      Custom             Configures the size of the scratch space in megabytes; you can select a
      background         value of 32, 64, 128, 256, or 512 MB. The default value is 32.
      bitmap file

    The deployment share configuration settings are saved, and the deployment share
    appears in the details pane of the Deployment Workbench.

Configure the Deployment Share Properties Windows PE x64
Components Tab

The deployment share properties stored on the Windows PE x64 Components tab are
mostly configured when you run the New Deployment Share Wizard.

To configure the Windows PE x64 Components tab

<!-- p.99 -->

1. Select Start, and then point to All Programs. Point to Microsoft Deployment
  Toolkit, and then select Deployment Workbench.

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares.

3. In the details pane, select deployment_share (where deployment_share is the name
  of the deployment share).

4. In the Actions pane, select Properties.

  The deployment_share Properties dialog box opens (where deployment_share is
  the name of the deployment share you want to configure).

5. On the Windows PE x86 Components tab, configure the settings listed in Table 29
  based on the requirements of your organization, and then select OK.

  Table 29. Configuration Settings on the Windows PE
  x64 Components Tab of Deployment Share Properties

                                                                                 ﾉ   Expand table

   Setting                Description

   Selection profile      Selects the device drivers and packages to be included in the
                          Windows PE images based on the selection profile you choose. The
                          default value is All Drivers and Packages. For more information
                          about selection profiles, see Manage Selection Profiles.

   Include all drivers    Select to configure the Update Deployment Share Wizard to include
   from the selected      all the device drivers in the selection profile specified in the Selection
   driver group           profile box.

   Include only drivers   Select to configure the Update Deployment Share Wizard to include
   of the following       only the device drivers in the chosen selection profile that are
   types                  specified in the following check boxes:

                          - Include all network drivers in the selected group

                          - Include all video drivers in the selected group

                          - Include all mass storage drivers in the selected group

                          - Include all system-class drivers in the selected group

   Include all network    Select to configure the Update Deployment Share Wizard to include
   drivers in the         all network drivers in the chosen selection profile. If the check box is:

<!-- p.100 -->

Setting                Description

selected group
                       - Selected, the Update Deployment Share Wizard includes all
                       network drivers in the selection profile specified in the Selection
                       profile box in the Windows PE images

                       - Cleared, the Update Deployment Share Wizard will not include all
                       network drivers in the selection profile specified in the Selection
                       profile box in the Windows PE images

                       This check box is enabled only if you select Include only drivers of
                       the following types.

Include all video      Select to configure the Update Deployment Share Wizard to include
drivers in the         all video drivers in the chosen selection profile. If the check box is:
selected group
                       - Selected, the Update Deployment Share Wizard includes all video
                       drivers in the selection profile specified in the Selection profile box
                       in the Windows PE images

                       - Cleared, the Update Deployment Share Wizard will not include all
                       video drivers in the selection profile specified in the Selection profile
                       box in the Windows PE images

                       This check box is enabled only if you select include only drivers of
                       the following types.

Include all mass       Select to configure the Update Deployment Share Wizard to include
storage drivers in     all mass storage drivers in the chosen selection profile. If the check
the selected group     box is:

                       - Selected, the Update Deployment Share Wizard includes all mass
                       storage drivers in the selection profile specified in the Selection
                       profile box in the Windows PE images

                       - Cleared, the Update Deployment Share Wizard will not include all
                       mass storage drivers in the selection profile specified in the Selection
                       profile box in the Windows PE images

                       This check box is enabled only if you select include only drivers of
                       the following types.

Include all system-    Select to configure the Update Deployment Share Wizard to include
class drivers in the   all system-class drivers in chosen the selection profile. If the check
selected group         box is:

                       - Selected, the Update Deployment Share Wizard includes all system-
                       class drivers in the selection profile specified in the Selection profile
                       box in the Windows PE images

<!-- p.101 -->

 Setting            Description

                    - Cleared, the Update Deployment Share Wizard will not include all
                    system-class drivers in the selection profile specified in the Selection
                    profile box in the Windows PE images

                    This check box is enabled only if you select Include only drivers of
                    the following types.

 ADO                Select to add the optional ADO components to the Windows PE
                    images. These components are necessary for accessing SQL Server
                    databases, such as the MDT DB. If this check box is:

                    - Selected, the ADO components are added to the Windows PE
                    images

                    - Cleared, the ADO components are not added to the Windows PE
                    images

 Optional Fonts     Use to configure the Update Deployment Share Wizard to include
                    the following fonts:

                    - Chinese (ZH-CN)

                    - Chinese (ZH-HK)

                    - Chinese (ZH-TW)

                    - Japanese (JA-JP)

                    - Korean (KO-KR)

                    Add these fonts when performing an LTI deployment of Windows
                    Server images when the Setup files are Japanese, Korean, or Chinese.
                    If the check box for a corresponding font is:

                    - Selected, the Update Deployment Share Wizard includes the font in
                    the Windows PE images

                    - Cleared, the Update Deployment Share Wizard will not include the
                    font in the Windows PE images

                    Adding fonts to Windows PE boot images increases the size of the
                    images. Add fonts only if necessary.

The deployment share configuration settings are saved, and the deployment share
appears in the details pane of the Deployment Workbench.

<!-- p.102 -->

Copy a Deployment Share
Deployment shares are local or network shared folders. You can make a copy of a
deployment share using any file-copy process, such as in Windows Explorer. When
copying a deployment share to another computer, ensure that you share the folder with
the appropriate permissions.

After you copy the deployment share, open it in the Deployment Workbench. For more
information about opening deployment shares, see Open an Existing Deployment Share
in the Deployment Workbench.

Close a Deployment Share in the Deployment Workbench

  ７ Note

  Closing a deployment share does not remove the local or network shared folder or
  delete the contents of the local or network shared folder: It only removes the
  deployment share from the list of deployment shares in the Deployment Shares
  node in the Deployment Workbench.

Close existing deployment shares in the Deployment Workbench using the Close
Deployment Share action. Start the Close Deployment Share action by performing one
of the following tasks:

     Right-click the deployment share, and then select Close Deployment Share.

     Select the deployment share, and then, from the Action menu, select Close
     Deployment Share.

     Select the deployment share, and then, in the Actions pane, select Close
     Deployment Share.

Update a Deployment Share in the Deployment Workbench
Updating a deployment share creates the Windows PE boot images (WIM and ISO files)
necessary to start LTI deployment.

To update a deployment share in the Deployment Workbench

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

<!-- p.103 -->

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares.

3. In the details pane, select deployment_share, and then in the Actions pane, select
  Update Deployment Share (where deployment_share is the name of the
  deployment share you want to update).

  The Update Deployment Share Wizard starts.

4. Complete the Update Deployment Share Wizard using the information in Table 30.
  Accept the default values unless otherwise specified.

  Table 30. Information for Completing the Update
  Deployment Share Wizard

                                                                            ﾉ   Expand table

   On this        Do this
   wizard page

   Options        a. Select one of the following options based on your requirements:

                  - Optimize the boot image updating process. This option configures the
                  Update Deployment Share Wizard to update existing versions of the image
                  files. Select this option when you want to reduce the amount of time
                  required to update the boot images. Typically, this process takes less time
                  than the Completely regenerate the boot images option.

                  You can optionally select the Compress the boot image contents to
                  recover space used by removed or modified content check box to reduce
                  the size of the boot images. Over time, the process of adding and
                  removing content (such as drivers, components, and packages) can
                  increase the size of the Windows PE image. Selecting this option reduces
                  the image size to the minimum for the current content. However, it may
                  also increase the time required to generate the images.

                  - Completely regenerate the boot images. This option configures the
                  Update Deployment Share Wizard to create a new version of all the image
                  files. Select this option when you want to force the creation of new images.
                  This process can take longer than the Optimize the boot image updating
                  process option.

                  By default, the Optimize the boot image updating process option is
                  selected and the Compress the boot image contents to recover space
                  used by removed or modified content check box is cleared.

<!-- p.104 -->

      On this         Do this
      wizard page

                      b. Select Next.

      Summary         Review the information in the Details box, and then select Next.

      Confirmation    You can select Save Output to save the output of the wizard to a file. You
                      can also select View Script to view the Windows PowerShell scripts used to
                      perform the wizard tasks.

                      Select Close.

     The Deployment Workbench starts updating the deployment share and creates the
     LiteTouchPE_x86.iso and LiteTouchPE_x86.wim files (for 32-bit target computers) or
     LiteTouchPE_x64.iso and LiteTouchPE_x64.wim files (for 64-bit target computers) in
     the deployment_share\Boot folder (where deployment_share is the network shared
     folder used as the deployment share) based on the configuration settings on the
     Windows PE x86 Settings and Windows PE x64 Settings tabs.

  ７ Note

  Optionally, create a bootable device, such as a UFD or USB hard disk, from the ISO
  file so that you can start the target computer from the device as described in
  Create Bootable Devices from MDT Boot Images.

Create Bootable Devices from MDT Boot Images

Starting destination computers using a bootable device (such as a UFD or a USB hard
disk) is often quicker and easier than starting computers using Windows Deployment
Services or CDs.

  ７ Note

  The target computer must support booting from the device to use this method of
  starting target computers.

To create a bootable UFD

   1. On a computer running Windows 7 or later operating system, insert the UFD or
     USB hard disk.

<!-- p.105 -->

2. Run Diskpart.exe, and type the command list disk to determine the disk number
  associated with the device.

3. Input the following commands, where N is the disk number identified in the
  previous step:

       select disk N

       clean

       create partition primary

       select partition 1

       active

       format fs=fat32

       assign

       exit

4. Copy the contents of LiteTouchPE_x86.iso (for 32-bit target computers) or
  LiteTouchPE_x64.iso (for 64-bit target computers) to the device by performing one
  of the following tasks:

       Burn the ISO file to a CD, and then copy its contents to the device using the
       command:

          Windows Command Prompt

          xcopy <d>:\*.* <e>:\*.* /s /e /f

       Where d is the driver letter of the CD and e is the drive letter of the device.

       Alternatively, mount the ISO file using a virtual CD program, and then copy its
       contents to the device using the command:

          Windows Command Prompt

          xcopy <d>:\*.* <e>:\*.* /s /e /f

       where d is the driver letter of the CD and e is the drive letter of the device.

<!-- p.106 -->

Configuring Operating Systems in the Deployment
Workbench
MDT uses the Deployment Workbench to manage the operating systems that you can
deploy to the reference and target computers in your organization. Configure the
operating systems in the Deployment Workbench by:

     Importing an operating system as described in Import an Operating System into
     the Deployment Workbench

     Viewing an operating system's properties as described in View Operating System
     Properties in the Deployment Workbench

     Copying an operating system as described in Copy an Operating System in the
     Deployment Workbench

     Moving an operating system as described in Move an Operating System in the
     Deployment Workbench

     Renaming an operating system as described in Rename an Operating System in the
     Deployment Workbench

     Deleting an operating system as described in Delete an Operating System from the
     Deployment Workbench

     Managing folders for operating systems as described in Manage Folders for
     Operating Systems in the Deployment Workbench

     In addtion to configuring operating systems in the Deployment Workbench, you
     can configure operating systems using the MDT Windows PowerShell cmdlets. For
     more information on configuring operating systems using the MDT Windows
     PowerShell cmdlets, see the following sections beneath the section, "MDT
     Windows PowerShell Cmdlets", in the MDT document Toolkit Reference:

     Get-MDTOperatingSystemCatalog

     Import-MDTOperatingSystem

Import an Operating System into the Deployment Workbench

You can import operating systems into the Deployment Workbench using the options
listed in Table 31. You manage this import in the Import Operating System Wizard in the
Deployment Workbench.

<!-- p.107 -->

Table 31. Options for Importing Operating Systems into
the Deployment Workbench

                                                                            ﾉ   Expand table

 Option                      Select this option to import an operating system from

 Full set of source files    Windows distribution media, such as a DVD, CD, or equivalent
                             media source.

 Custom image file           A WIM image that was previously captured for deployment,
                             typically from a reference computer.

 Windows Deployment          Images that exist on computers running Windows Deployment
 Services images             Services.

  ７ Note

  Always import operating systems from operating system sources that have the
  most recent updates. Doing so helps reduces the management effort and network
  traffic when applying the updates after the target operating system has been
  deployed.

Start the Import Operating System Wizard using one of the following methods:

      In the Deployment Workbench console tree, select the Operating System node or a
      folder beneath the Operating System node. Then, in the Actions pane, select
      Import Operating System.

      In the Deployment Workbench console tree, select the Operating System node or a
      folder beneath the Operating System node. Then, from the Action menu, select
      Import Operating System.

      In the Deployment Workbench console tree, select the Operating System node or a
      folder beneath the Operating System node. Then, select Import Operating System.

      You can also import operating systems into the Deployment Workbench from:

      Windows distribution media as described in Import an Operating System from
      Windows Distribution Media

      WIM images previously captured from reference computers as described in Import
      a Previously Captured Image of a Reference Computer

<!-- p.108 -->

     Existing WIM images in Windows Deployment Services as described in Import an
     Operating System from an Existing Windows Deployment Services Image

Import an Operating System from Windows Distribution Media

MDT allows you to import operating systems into the Deployment Workbench from
Windows distribution media, which includes product DVDs, CDs, or folders containing
the distribution files. Import the operating system using the Import Operating System
Wizard in the Deployment Workbench.

To import an operating system from Windows distribution media

   1. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Operating Systems (where
     deployment_share is the name of the deployment share to which the operating
     system will be added).

   2. In the Actions pane, select Import Operating System.

     The Import Operating System Wizard starts.

   3. Complete the Import Operating System Wizard using the information in Table 32.

                                                                                 ﾉ   Expand table

      On this wizard   Do this
      page

      OS Type          Select Full set of source files, and then select Next.

      Source           In Source directory, type source_folder (where source_folder is the fully
                       qualified path to the folder containing the operating system source files),
                       and then select Next.

                       Alternatively, select Browse to find the source folder.

      Destination      In Destination directory name, type destination_folder (where
                       destination_folder is the name of the folder in the deployment share that
                       will contain the operating system source files), and then select Next.

      Summary          Select Next.

      Confirmation     Select Save Output to save the output of the wizard to a file, or select
                       View Script to view the Windows PowerShell scripts used to perform the
                       wizard tasks.

<!-- p.109 -->

      On this wizard    Do this
      page

                        Select Finish.

     The Import Operating System Wizard finishes. The operating system is added to
     the list of operating systems in the details pane of the Deployment Workbench.

Import a Previously Captured Image of a Reference Computer

MDT allows you to import previously captured images of reference computers or other
custom images into the Deployment Workbench. Import the operating system using the
Import Operating System Wizard in the Deployment Workbench.

To import an operating system from a previously captured image of a
reference computer

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Operating Systems (where
     deployment_share is the name of the deployment share to which the operating
     system will be added).

  3. In the Actions pane, select Import Operating System.

     The Import Operating System Wizard starts.

  4. Complete the Import Operating System Wizard using the information in Table 33.

                                                                                    ﾉ   Expand table

      On this          Do this
      wizard page

      OS Type          Select Custom image file, and then select Next.

      Source           In Source file, type source_file (where source_file is the fully qualified path
                       to the WIM image file containing the operating system source files), and
                       then select Next.

                       Alternatively, select Browse to find the source WIM image.

<!-- p.110 -->

      On this         Do this
      wizard page

      Setup           Select one of the following options based on your requirements, and then
                      select Next:

                      - Setup files are not needed. Select this option when no Setup files are
                      needed for an image.

                      - Copy Windows 7, Windows Server 2008 R2, or later setup files from
                      the specified path. Select this option to copy the Setup files from a folder
                      containing the Windows setup files when those files are not available in
                      another operating system in the Deployment Workbench. In Setup source
                      directory, type or select Browse to find the folder containing the Setup
                      files.

                      The default option is Setup and Sysprep files are not needed.

      Destination     In Destination directory name, type destination_folder (where
                      destination_folder is the name of the folder in the deployment share that
                      will contain the operating system source files), and then select Next.

      Summary         Select Next.

      Confirmation    Select Save Output to save the output of the wizard to a file, or select
                      View Script to view the Windows PowerShell scripts used to perform the
                      wizard tasks.

                      Select Finish.

     The Import Operating System Wizard finishes. The operating system is added to
     the list of operating systems in the details pane of the Deployment Workbench.

     If you attempt to import a custom image that does not have an Edition ID, the
     wizard fails with an error similar to the following:

  Console

  Setup failed applying image F:\Deploy\Operating
  Systems\W2K8R2RTM\W2K8R2RTM.wim, rc = 31
  ZTI ERROR - Non-zero return code by LTIApply, rc = 31.

To resolve this issue, add an Edition ID to the image by running the following command
(where edition_id is the appropriate SKU ID as defined in the original factory image or in
the Windows ADK, wim_file is the name of the WIM file, new_image_name is the new
image name, and new_image_description is the new description for the image):

  Windows Command Prompt

<!-- p.111 -->

  imagex /flags <edition_id> /info <wim_file> 1 <new_image_name>
  <new_image_description>

Import an Operating System from an Existing Windows
Deployment Services Image

MDT allows you to import existing WIM images in Windows Deployment Services into
the Deployment Workbench. Import the operating system using the Import Operating
System Wizard in the Deployment Workbench.

To import an operating system from an existing image in Windows
Deployment Services

  1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

  2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Operating Systems (where
     deployment_share is the name of the deployment share to which the operating
     system will be added).

  3. In the Actions pane, select Import Operating System.

     The Import Operating System Wizard starts.

  4. Complete the Import Operating System Wizard using the information in Table 34.

     Table 34. Information for Completing the Import
     Operating System Wizard

                                                                           ﾉ   Expand table

      On this wizard   Do this
      page

      OS Type          Select Custom image file, and then select Next.

      WDS Server       In Server name, type server_name (where server_name is the name of
                       the Windows Deployment Services server that contains the existing WIM
                       images), and then select Next.

      Summary          Select Next.

<!-- p.112 -->

      On this wizard    Do this
      page

      Confirmation      Select Save Output to save the output of the wizard to a file, or select
                        View Script to view the Windows PowerShell scripts used to perform the
                        wizard tasks.

                        Select Finish.

     The Import Operating System Wizard finishes. The operating system is added to
     the list of operating systems in the details pane but is not is copied to the
     deployment share. The Deployment Workbench leaves the operating system image
     on the Windows Deployment Services server, but the image is now available to LTI.

View Operating System Properties in the Deployment Workbench

You view operating system properties beneath the Operating System node in the
Deployment Workbench using the Properties actions as described in View Item
Properties in the Deployment Workbench.

Table 35 lists the configuration settings on the General tab of the operating system
Properties dialog box and provides a description of each setting.

  ７ Note

  The configuration settings on the General tab are populated when you import the
  operating system, and only the Operating system name can be modified. No other
  settings can be modified.

                                                                               ﾉ   Expand table

 Setting               Description

 Operating system      Contains the name of the operating system—for example, Windows 8
 name                  ENTERPRISE in Windows 8 x64 install.wim.

 Description           Contains the description of the operating system—for example, Windows 8
                       ENTERPRISE.

 OS type               Contains the type of operating system—for example, Windows Image-
                       based Setup.

 Platform              Contains the processor architecture of the operating system—for example,
                       x64.

<!-- p.113 -->

 Setting            Description

 Languages(s)       Contains the languages included in the operating system—for example,
                    en-US.

 Includes Setup     Contains True or False, which indicates whether the operating system
                    includes the files necessary to perform setup.

 Path               Contains the path to the operating system relative to the root of the
                    deployment share.

 Image file         Contains the path and file name of the operating system relative to the
                    root of the deployment share.

 Image index        Contains a numeric value that indicates the image index for the image—for
                    example, 1.

 Image name         Includes the image name—for example, Windows 8 ENTERPRISE.

 Image size (MB)    Contains the size of the image in megabytes—for example, 7921 indicates
                    7,921 MB, or 7.921 GB.

 HAL                Contains the HAL type for the image—for example, acpiapic.

Copy an Operating System in the Deployment Workbench
Copy and paste operating systems and folders beneath the Operating System node in
the Deployment Workbench using the Copy and Paste actions as described in Copy
Items in the Deployment Workbench.

Move an Operating System in the Deployment Workbench

Move operating systems and folders beneath the Operating System node in the
Deployment Workbench using the Cut and Paste actions as described in Move Items in
the Deployment Workbench.

Rename an Operating System in the Deployment Workbench
Rename operating systems and folders beneath the Operating System node in the
Deployment Workbench using the Rename action as described in Rename Items in the
Deployment Workbench.

Delete an Operating System from the Deployment Workbench

<!-- p.114 -->

Delete operating systems and folders beneath the Operating System node in the
Deployment Workbench using the Delete Selected Items Wizard as described in Delete
Items from the Deployment Workbench. The Delete Selected Items Wizard allows
deletion of individual operating system files or entire folder structures.

Manage Folders for Operating Systems in the Deployment
Workbench
You can manage folders beneath the Operating Systems node in the Deployment
Workbench to create hierarchical groupings of operating systems. For more information
on:

      Managing folders, see Manage Folders in the Deployment Workbench

      Selection profiles, see Manage Selection Profiles

Configuring Applications in the Deployment Workbench
MDT uses the Deployment Workbench to manage the applications deployed to the
reference and target computers in your organization. Configure the applications in the
Deployment Workbench by:

      Creating a new application as described in Create a New Application in the
      Deployment Workbench

      Viewing and configuring an application as described in View and Configure an
      Application in the Deployment Workbench

      Copying an application as described in Copy an Application in the Deployment
      Workbench

      Moving an application as described in Move an Application in the Deployment
      Workbench

      Renaming an application as described in Rename an Application in the
      Deployment Workbench

      Deleting an application as described in Delete an Application from the Deployment
      Workbench

      Managing folders for applications as described in Manage Folders for Applications
      in the Deployment Workbench

<!-- p.115 -->

     Enabling or disabling an application as described in Enable or Disable an
     Application in the Deployment Workbench

     Preventing an application from being visible as described in Prevent an Application
     from Being Visible in the Deployment Wizard

     Configuring the computer to restart as described in Configure the Computer to
     Restart After Application Installation

     Customizing application installation as described in Customize Application
     Installation in Task Sequences

     In addtion to managing applications in the Deployment Workbench, you can
     manage applications using the MDT Windows PowerShell cmdlets. For more
     information on managing applications using the MDT Windows PowerShell
     cmdlets, see the following sections beneath the section, "MDT Windows
     PowerShell Cmdlets", in the MDT document Toolkit Reference:

     Get-MDTDeploymentShareStatistics

     Import-MDTApplication

Create a New Application in the Deployment Workbench
You can create new applications in the Deployment Workbench using one of the options
listed in Table 36. You import operating systems into the Deployment Workbench using
the New Application Wizard.

Table 36. Options for Creating a New Application

                                                                                 ﾉ   Expand table

 Option                Select this option to create an application when

 Application with      The application source files are not available to the destination computer
 source files          when installing the operating system build or when they must be
                       customized. When you select this option, the application files are copied to
                       the deployment share, and the deployment process installs the application
                       from the deployment share.

 Application without   The application source files are available during installation of the
 source files or       operating system build or to run a command that requires no application
 elsewhere on the      source files. When you select this option, no application source files are
 network               copied to the deployment share. Instead, the deployment process installs
                       the application from another location on the network.

<!-- p.116 -->

 Option               Select this option to create an application when

 Application bundle   A list of applications that you must install in a particular order. This list is
                      specified as dependencies for the application bundle, but the bundle itself
                      does not install anything.

Start the New Application Wizard using one of the following methods:

     In the Deployment Workbench console tree, select the Applications node or a
     folder beneath the Applications node. Then, in the Actions pane, select New
     Application.

     In the Deployment Workbench console tree, select the Applications node or a
     folder beneath the Applications node. Then, from the Action menu, select New
     Application.

     In the Deployment Workbench console tree, select the Applications node or a
     folder beneath the Applications node. Then, select New Application.

     You can create a new application in the Deployment Workbench for:

     Applications to be deployed from the deployment share as described in Create a
     New Application That Is Deployed from the Deployment Share

     Applications to be deployed from another network shared folder as described in
     Create a New Application That Is Deployed from Another Network Shared Folder

     Deploying application dependencies as described in Create a New Application for
     Deploying Application Dependencies

Create a New Application That Is Deployed from the Deployment
Share

MDT allows you to use the New Application Wizard in the Deployment Workbench to
create new applications that are deployed from the deployment share. The New
Application Wizard copies source files for this type of applications to the deployment
share.

To create a new application that is deployed from the deployment
share

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

<!-- p.117 -->

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/deployment_share/Applications (where
  deployment_share is the name of the deployment share to which the application
  will be added).

3. In the Actions pane, select New Application.

  The New Application Wizard starts.

4. Complete the New Application Wizard using the information in Table 37.

  Table 37. Information for Completing the New
  Application Wizard

                                                                               ﾉ   Expand table

   On this wizard   Do this
   page

   Application      Select Application with source files, and then select Next.
   Type

   Details          - In Publisher, type publisher_name (where publisher_name is the name
                    of the application's publisher).

                    - In Application Name, type application_name (where application_name
                    is the descriptive name of the application).

                    - In Version, type version (where version is the version of the application).

                    - In Language, type language (where language is the language of the
                    application).

                    - Select Next.

   Source           a. In Source directory, type source_folder (where source_folder is the fully
                    qualified path to the folder containing the application source files).

                    Alternatively, select Browse to find the source folder.

                    b. Select or clear the Move the files to the deployment share instead of
                    copying them check box based on your requirements, and then select
                    Next.

                    This check box determines whether the wizard copies or moves the
                    application source files to the deployment share. If the check box is:

<!-- p.118 -->

       On this wizard   Do this
       page

                        - Selected, the wizard moves the source files to the deployment share

                        - Cleared, the wizard copies the source files to the deployment share

                        By default, this check box is cleared.

       Destination      In Specify the name of the directory that should be created, type
                        destination_folder (where destination_folder is the name of the folder in
                        the deployment share that will contain the application source files), and
                        then select Next.

       Command          - In Command line, type command_line (where command_line is the
       Details          command line to be run to start the installation of the application,
                        including any command-line parameters).

                        - In Working directory, type working_directory (where working_directory
                        is the fully qualified or relative path for the folder designated as the
                        working directory for the application).

                        - Select Next.

       Summary          Select Next.

       Confirmation     Select Save Output to save the output of the wizard to a file, or select
                        View Script to view the Windows PowerShell scripts used to perform the
                        wizard tasks.

                        Select Finish.

     The New Application Wizard finishes. The application is added to the list of
     operating systems in the details pane in the Deployment Workbench.

Create a New Application That Is Deployed from Another Network
Shared Folder

MDT allows for the creation of new applications that you deploy from a network shared
folder other than the deployment share. Create a new application using the New
Application Wizard in the Deployment Workbench. The New Application Wizard does
not copy the source files for this type of application.

To create a new application that is deployed from a network shared
folder other than the deployment share

<!-- p.119 -->

1. Select Start, and then point to All Programs. Point to Microsoft Deployment
  Toolkit, and then select Deployment Workbench.

2. In the Deployment Workbench console tree, go to Deployment
  Workbench/Deployment Shares/deployment_share/Applications (where
  deployment_share is the name of the deployment share to which the application
  will be added).

3. In the Actions pane, select New Application.

  The New Application Wizard starts.

4. Complete the New Application Wizard using the information in Table 38.

                                                                              ﾉ   Expand table

   On this wizard   Do this
   page

   Application      Select Application without source files or elsewhere on the network,
   Type             and then select Next.

   Details          - In Publisher, type publisher_name (where publisher_name is the name
                    of the application's publisher).

                    - In Application Name, type application_name (where application_name
                    is the descriptive name of the application).

                    - In Version, type version (where version is the version of the application).

                    - In Language, type language (where language is the language of the
                    application).

                    - Select Next.

   Command          - In Command line, type command_line (where command_line is the
   Details          command line to be run to start the installation of the application,
                    including any command-line parameters).

                    - In Working directory, type working_directory (where working_directory
                    is the fully qualified or relative path for the folder designated as the
                    working directory for the application).

                    - Select Next.

   Summary          Select Next.

   Confirmation     Select Save Output to save the output of the wizard to a file, or select
                    View Script to view the Windows PowerShell scripts used to perform the

<!-- p.120 -->

       On this wizard   Do this
       page

                        wizard tasks.

                        Select Finish.

     The New Application Wizard finishes. The application is added to the list of
     operating systems in the details pane of the Deployment Workbench.

Create a New Application for Deploying Application Dependencies

MDT allows for the creation of new applications used to deploy only the dependencies
for an application instead of installing the application itself. Create a new application
using the New Application Wizard in the Deployment Workbench. The New Application
Wizard does not copy source files to the deployment share.

To create a new application for deploying application dependencies

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share/Applications (where
     deployment_share is the name of the deployment share to which the application
     will be added).

   3. In the Actions pane, select New Application.

     The New Application Wizard starts.

   4. Complete the New Application Wizard by using the information in Table 39.

     Table 39. Information for Completing the New
     Application Wizard

                                                                           ﾉ   Expand table

       On this wizard   Do this
       page

       Application      Select Application bundle, and then select Next.
       Type
