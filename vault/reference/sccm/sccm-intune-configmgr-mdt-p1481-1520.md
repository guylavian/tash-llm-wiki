---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1481-1520"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1481-1520
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1481-1520
family: sccm
documentKind: "doc"
abstract: "Table 38 lists the behavior of the options on the wizard page for the REFRESH stage. The Format column indicates whether the target hard disk is to be formatted as a part of the deployment. The other columns indicate the configuration of the options when the UserStatePage is loa"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1481-1520

<!-- p.1481 -->

       Table 38 lists the behavior of the options on the wizard page for the REFRESH
       stage. The Format column indicates whether the target hard disk is to be
       formatted as a part of the deployment. The other columns indicate the
       configuration of the options when the UserStatePage is loaded.

Table 38. Behavior of Options for the REFRESH
Stage
                                                                          ﾉ   Expand table

 Format           NoData            Local              USB                Network

 Yes              Selected          Disabled           Disabled           Disabled

 No               Disabled          Selected           Disabled           Disabled

REPLACE.WinPE Stage Behavior

The REPLACE.WinPE stage captures the user state migration data from the existing (old)
computer, and then restores the user state migration data later using one of the New
Computer deployment scenarios. Because two different computers are involved in the
deployment, the user state migration data must be saved to a USB drive or to a network
shared folder. Saving user state migration data to a local disk is unavailable.

Table 39 lists the behavior of the options on the wizard page for the REPLACE.WinPE
stage. The Format column indicates whether the target hard disk is to be formatted as a
part of the deployment. The other columns indicate the configuration of the options
when the UserStatePage is loaded.

Table 39. Behavior of Options for the
REPLACE.WinPE Stage
                                                                          ﾉ   Expand table

 Format           NoData             Local              USB               Network

 N/A              Disabled           Disabled           Enabled           Enabled

Task Sequence Variables

<!-- p.1482 -->

Table 40 lists the UserStatePage task sequence variables with a description and whether
the variable is read by the wizard page, written by the wizard page, or can be configured
in the UDI Wizard configuration file.

Table 40. UserStatePage Task Sequence
Variables
                                                                                     ﾉ    Expand table

 Variable                                                                      Read      Write   Config

 _SMSTsInWinPE                                                                 Yes       No      No

 Specifies whether the UDI Wizard is running in Windows PE. If the
 variable is set to:

 - TRUE, then the UDI Wizard is running in Windows PE

 - FALSE, then the UDI Wizard is not running in Windows PE, but rather in
 a full Windows operating system

 OSDDataSourceDirectory                                                        No        Yes     No

 Specifies the directory in which the user state migration data is stored.

 OSDDataSourceDrive                                                            Yes       Yes     No

 Specifies the USB drive used for capturing and restoring user state
 migration data, which you select from the USB Target Drive box. If the
 variable is set prior to showing the wizard page, the value of the variable
 is used as the default value.

 OSDDiskPart                                                                   Yes       No      Yes

 Specifies whether the drive selected for the installation of the target
 operating system should be formatted and partitioned. You set this
 variable on the VolumePage wizard page, and the code on this wizard
 page uses it to determine which options are selected and enabled by
 default. For more information, see UserStatePage.

 OSDHardLinks                                                                  No        Yes     No

 Specifies whether the user state migration data is to be captured to or
 restored from a local drive. If the variable is set to:

 - TRUE, then the Local option was selected, and user state migration
 data will be captured or restored from a local drive that is attached to

<!-- p.1483 -->

Variable                                                                        Read   Write   Config

the target computer

- FALSE, then the Local option was not selected, and no user state
migration data will be captured or restored from a local drive that is
attached to the target computer

OSDRestoreData                                                                  No     Yes     No

Specifies whether there is data to be restored. If the variable is set to:

- TRUE, then the Local, USB Target Drive, or Network option was
selected, and user state migration data will be captured or restored from
the target computer

- FALSE, then the No Data to Restore option was selected, and no user
state migration data will be captured or restored from the target
computer

OSDUserStateKey                                                                 Yes    Yes     Yes

Specifies the user name used to secure the user state migration data.
The user name is provided when the user state migration data is
captured. The same user name and password must be provided when
the user state migration data is restored. You set the value of this
variable in the User name box.

OSDUserStateKeyPassword                                                         Yes    Yes     Yes

Specifies the password for the user name used to secure the user state
migration data. Set the value of this variable in the Password and
Confirm password boxes.

OSDUserStateMode                                                                No     Yes     No

Specifies the mode (method) for capturing or restoring the user state
migration data. The value of this variable is set by the options selected. If
the variable is set to:

- NoData, then the No Data to Restore option was selected, and no user
state migration data will be captured or restored

- Local, then the Local option was selected, and the user state migration
data will be captured or restored from a local hard disk on the target
computer

- Network, then the Network option was selected, and the user state
migration data will be captured to or restored from a network shared
folder

<!-- p.1484 -->

 Variable                                                                     Read        Write   Config

 - When used in capture mode, this option creates a folder based on a
 hash of the user name and password so that the identity of the user
 state migration data is protected. The exact same user name and
 password must be used when restoring the user state migration data so
 that the wizard page can accurately locate the folder.

 - USB, then the USB Target Drive option was selected, and the user state
 migration data will be captured to or restored from a USB drive that is
 physically attached to the target computer

 - The wizard page behavior for USB drives is also affected by the Format,
 FormatPrompt, and MinimumDriveSize variables.

 SMSConnectNetworkFolderPath                                                  Yes         Yes     Yes

 Specifies the network shared folder used for capturing and restoring
 user state migration data, which is selected from the Network box. The
 Network box displays a user-friendly name for the network shared
 folder that is configured in the Network Shares box in the Network
 Combo Box section on the wizard page editor in the UDI Wizard
 Designer. If the variable is set prior to showing the wizard page, the
 value of the variable is used as the default value.

Memory Variables

Table 41 lists the UserStatePage memory variables with a description and whether the
variable is read or written by the wizard page.

Table 41. UserStatePage Memory Variables
                                                                                      ﾉ    Expand table

 Variable                                                                                  Read    Write

 DriveLetter                                                                               No      Yes

 Specifies the drive letter for the USB drive selected in the USB Target Drive box on
 the wizard page. The value of this variable will be the drive letter, including the
 colon (:) suffix, such as M:.

 TargetDrive                                                                               No      Yes

 Specifies the caption displayed in the USB Target Drive box on the wizard page
 for the USB drive selected on the target computer. The value of this variable will

<!-- p.1485 -->

 Variable                                                                                Read    Write

 be similar to the following example:

 M: VendorA Ultra TD v1.0 USB Device (74.5 GB)

 UserStateMode                                                                           No      Yes

 Specifies the option selected with the options on the wizard page and is set to the
 same value as the OSDUserStateMode variable. Valid values for this variable
 include:

 - NoData, which indicates that the No Data to Restore option was selected

 - Local, which indicates that the Local option was selected

 - USB, which indicates that the USB Target Drive option was selected

 - Network, which indicates that the Network option was selected

Configuration Variables

Table 42 lists the UserStatePage configuration variables with a description and whether
the variable is read by the wizard page, written by the wizard page, or can be configured
in the UDI Wizard configuration file.

Table 42. UserStatePage Configuration
Variables
                                                                                    ﾉ    Expand table

 Variable                                                                     Read      Write   Config

 DataSourceText                                                               Yes       No      Yes

 Specifies an informational message that instructs the user performing
 the user state capture or restore about how to use the wizard page. You
 set the value of this variable in the Instruction Text box in the Message
 section on the wizard paged editor in the UDI Wizard Designer.

 Format                                                                       Yes       No      Yes

 Specifies whether the USB drive selected for capturing user state on the
 target computer should be partitioned and formatted prior to capturing
 user state migration data. Set the value of this variable by selecting the
 Format the USB drive before capture check box in the USB Combo Box

<!-- p.1486 -->

Variable                                                                       Read   Write   Config

section on the wizard paged editor in the UDI Wizard Designer.

If the variable is set to:

- TRUE, then the drive is formatted prior to capturing user state
migration data

- FALSE, then the drive is not formatted prior to capturing user state
migration data

FormatPrompt                                                                   Yes    No      Yes

Specifies whether the user must confirm that the USB drive used for
capturing user state migration data is to be formatted prior to
performing the capture. Set the value of this variable by selecting the
Prompt the user before formatting the target drive check box in the
USB Combo Box section on the wizard paged editor in the UDI Wizard
Designer.

Note:

This variable is only valid if the OSDUserStateMode task sequence
variable is set to USB.

MinimumDriveSize                                                               Yes    No      Yes

Specifies the minimum available free disk space in gigabytes required for
a drive to be available for storing user state migration data. The value of
this variable acts as a filter, and you set it in the Minimum Drive Size
text box in the USB Combo Box section on the wizard paged editor in
the UDI Wizard Designer.

NetworkDrive                                                                   Yes    No      Yes

Specifies the drive letter that this wizard page uses to map to the
network shared folder in the SMSConnectNetworkFolderPath task
sequence variable. The network shared folder mapping is used for
capturing or restoring the user state migration data. Set the value of this
variable in the Mapped Drive Letter box in the Network Combo Box
section on the wizard paged editor in the UDI Wizard Designer. The
drive letter specified must include the colon (:) after the drive letter and
must not be in use on the target computer. For example, if the target
computer has drives C: and D:, then C: and D: could not be used for this
variable.

Note:

<!-- p.1487 -->

 Variable                                                                      Read      Write   Config

 This variable is only valid if the OSDUserStateMode task sequence
 variable is set to Network.

 State                                                                         Yes       No      Yes

 Specifies whether the wizard page is being used for capturing or
 restoring the user state migration data. Set the value of this variable in
 the Capture or Restore box in the Capture/Restore Location section on
 the wizard paged editor in the UDI Wizard Designer. If the variable is set
 to:

 - Capture, then the wizard page is used to capture user state migration
 data

 - Restore, then the wizard page is used to restore user state migration
 data

VolumePage
Use this wizard page to configure the settings for the disk volume on the target
computer on which the operating system will be deployed. These settings include
selecting the target operating system, selecting the target drive, selecting any Windows
installation, and determining whether the target drive should be formatted as a part of
the deployment process.

Task Sequence Variables

Table 43 lists the VolumePage task sequence variables with a description and whether
the variable is read by the wizard page, written by the wizard page, or can be configured
in the UDI Wizard configuration file.

Table 43. VolumePage Task Sequence Variables
                                                                                     ﾉ    Expand table

 Variable                                                                      Read      Write   Config

 OSDDiskPart                                                                   Yes       Yes     Yes

 Specifies whether the drive selected for deploying the target operating
 system on the target computer should be partitioned and formatted
 prior to capturing user state migration data. The value of this variable is
 set by the one of the following check boxes on the wizard page:

<!-- p.1488 -->

Variable                                                                    Read   Write   Config

- Clean the selected volume. This check box appears when the UDI
Wizard is running in a full Windows operating system. You can configure
the text message using the FormatFullOS setter property for the wizard
page in the UDI Wizard configuration file.

- Partition and format disk 0. This check box appears when the UDI
Wizard is running in Windows PE. You can configure the text message
using the FormatWinPE setter property for the wizard page in the UDI
Wizard configuration file.

The code logic behind the UserStatePage wizard page uses this variable
to determine which options are selected and enabled by default.

If the variable is set to:

- TRUE, then the drive is partitioned and formatted prior to deploying
the target operating system

- FALSE, then the drive is not partitioned and formatted prior to
deploying the target operating system

OSDImageIndex                                                               Yes    Yes     Yes

Specifies a numeric index of the operating system image in the .wim file,
which is selected in the Image Selection combo box. You configure the
list of possible operating system images in the Image Selection box in
the Image Combo Box Values list in the Image Combo Box section on
the VolumePage wizard page editor. The image index is configured as a
part of each image in the Image Combo Box Values list.

OSDImageName                                                                No     Yes     No

Specifies the name of the operating system image in the .wim file, which
is selected in the Image Selection box. The list of possible operating
system images in the Image Selection combo box is configured in the
Image Combo Box Values list in the Image Combo Box section on the
VolumePage wizard page editor. The image name is configured as a part
of each image in the Image Combo Box Values list.

OSDTargetDrive                                                              No     Yes     No

Specifies the drive letter for the volume selected in the Volume box on
the wizard page. The value of this variable will be the drive letter,
including the colon (:) suffix, such as C:.

OSDWinPEWindir                                                              No     Yes     No

<!-- p.1489 -->

 Variable                                                                     Read     Write   Config

 Specifies the location of an existing installation of Windows on the
 target computer. Set the value of this variable in the Windows Directory
 box on the wizard page.

Memory Variables

Table 44 lists the VolumePage memory variables with a description and whether the
variable is read or written by the wizard page.

Table 44. VolumePage Memory Variables
                                                                                   ﾉ    Expand table

 Variable                                                                               Read    Write

 VolumeArchitecture                                                                     No      Yes

 Specifies the processor architecture of the operating system to be deployed,
 which is selected in the Image Selection box. The VolumeArchitecture wizard
 page consumes this variable to filter the architecture of applications displayed on
 that page. For example, if a 32-bit operating system is to be deployed, then the
 VolumeArchitecture wizard page removes (filters) any 64-bit applications from
 the list of available applications.

 If the variable is set to:

 - x86, then a 32-bit operating system was selected

 - amd64, then 64-bit operating system was selected

WelcomePage
Use this wizard page to provide information to the user about the UDI Wizard and the
deployment process. You can configure the notification message using the UDI Wizard
Designer.

UDI Build Your Own Page Toolbox Control
Reference

<!-- p.1490 -->

The Build Your Own Page feature in UDI allows you to create custom wizard pages that
you can use to collect additional deployment information for use in UDI. You can create
custom wizard pages using the:

     Build Your Own Page feature. This feature allows you to create a custom wizard
     page for collecting deployment information without requiring you to write code or
     have developer skills. Use this feature if you need to collect basic information
     without advanced user interaction. For example, you cannot add any code or
     customize UI fonts using this feature.

     UDI SDK and Visual Studio. Use this SDK if you want to create an advanced, fully
     customized wizard page in Visual Studio for collecting deployment information.
     Although the UDI SDK allows you to create customized wizard pages, such as
     adding custom code or changing fonts, this method requires developer skills.

     For more information on using the UDI SDK to create custom wizard pages, see
     "Creating Custom UDI Wizard Pages" in the User-Drive Installation Developers
     Guide.

     The Build Your Own Page feature includes a toolbox of controls that you can add
     to your custom wizard page from the Build Your Own Page toolbox, which is
     displayed when you view the custom wizard page on the Configure tab in the UDI
     Wizard Designer.

     Table 45 lists the types of controls to your custom wizard page, which is illustrated
     in Figure 5. Each of these controls is discussed in further detail in a subordinate
     section.

Table 45. Types of Controls in the UDI Build
Your Own Page Toolbox
                                                                                 ﾉ   Expand table

 Control type     Description

 Checkbox         This control allows you select or clear a configuration option and behaves as a
 control          traditional UI check box.

 Combobox         This control allows you to select an item from a list of items and behaves as a
 control          traditional UI drop-down list.

 Line control     This control allows you to add a horizontal line to divide one portion of the
                  custom wizard page from another.

<!-- p.1491 -->

 Control type      Description

 Label control     This control allows you to add descriptive, read-only text to the wizard page.

 Radio control     This control allows you to select one configuration option from a group of two
                   or more options.

 Bitmap control    This control allows you to add a bitmap graphic (.bmp file) to the custom
                   wizard page.

 Textbox control   This control allows you to enter text on the custom wizard page.

You can add any combination of these controls to your custom wizard page based on
the information you want to collect. In addition, you can use the Show Gridlines check
box to show or hide gridlines that can be used to assist in visually designing the custom
wizard page.

Figure 5 provides an example of a custom wizard page and the Build Your Own Page
toolbox.

Figure SEQ Figure \* ARABIC 5. Example custom wizard page

Checkbox Control
This control allows you select or clear a configuration option and behaves as a
traditional UI check box. This control has a corresponding label that you can use to
describe the purpose of the check box. The state of this control is True when the check

<!-- p.1492 -->

box is selected and False when the check box is cleared. The state of the check box is
stored in the task sequence variable configured for this control.

Layout Properties

Layout properties are used to configure the UI characteristics of the control and are
configured on the Layout tab in the UDI Wizard Designer. Table 46 lists the layout
properties for the Checkbox control and provides a brief description of each property

Table 46. Checkbox Control Layout Properties
                                                                                     ﾉ   Expand table

 Property   Description

 X          Use this property to configure the horizontal position of the control.

 Y          Use this property to configure the vertical position of the control.

 Label      Use this property to configure the descriptive text associated with the check box.

 Width      Use this property to configure the width of the control.

            Note If the text entered in the Label property is longer than the width of the control,
            the text is clipped and not displayed.

 Height     Use this property to configure the height of the control.

            Note If the text entered in the Label property is taller than the height of the control,
            the text is clipped.

Settings Properties

Settings properties are used to configure the data initially shown in a control (the
default value) and where the information collected from the user is saved. Table 47 lists
the settings properties for the Checkbox control and provides a brief description of each
property.

Table 47. Checkbox Control Settings Properties
                                                                                     ﾉ   Expand table

<!-- p.1493 -->

 Property              Description

 Default value         Use this property to configure the default value for the control. For a check
                       box, the default value is False.

 Task sequence         Use this property to configure the task sequence variable where the
 variable name         information collected from the user is stored. If the task sequence variable:

                       - Does not already exist, the task sequence variable is created and set to the
                       value the user provides

                       - Already exists, the existing value of the task sequence variable is
                       overwritten with the value the user provides

 Friendly display      Use this property to configure the descriptive name that appears on the
 name visible in the   Summary wizard page. This name is used to describe the value that was
 summary page          saved in the Task sequence variable name property for this control.

 Unlocked              Use this property to configure whether the user is able to interact with the
                       control. By default, the control is enabled. This button displays the following
                       status:

                       - Unlocked. The control is enabled, and users can enter information using it.

                       - Locked. The control is disabled, and users are unable to enter information
                       using it.

                       Note If you disable (lock) a control, you must provide the information the
                       control collected by configuring MDT properties in CustomSettings.ini or in
                       the MDT DB. Otherwise, the UDI Wizard will not collect the necessary
                       information, and the UDI deployment will fail.

Combobox Control
This control allows you to select an item from a list of items and behaves as a traditional
UI drop-down list. This control allows you to add or remove items from the list and
provide a corresponding value that will be set in the task sequence variable configured
for this control.

Layout Properties

Layout properties are used to configure the UI characteristics of the control and are
configured on the Layout tab in the UDI Wizard Designer. Table 48 lists the layout
properties for the Combobox control and provides a brief description of each property.

<!-- p.1494 -->

Table 48. Combobox Control Layout Properties
                                                                                     ﾉ   Expand table

 Property   Description

 X          Use this property to configure the horizontal position of the control.

 Y          Use this property to configure the vertical position of the control.

 Width      Use this property to configure the width of the control.

            Note If the text entered in the control is longer than the width of the control, the text
            is not displayed.

 Height     Use this property to configure the height of the control.

            Note If the text entered in the control is taller than the height of the control, the text
            is clipped.

 Data       Use this property to configure the list of data items displayed in the control. Each
 Items      data item has the following properties:

            - Value. The value stored in the task sequence variable when the data item is selected

            - DisplayValue. The value displayed to the user in the control

            You can:

            - Add data items to the list using the blue plus sign button immediately to the right
            of the list of data items

            - Remove data items from the list using the red X button immediately to the right of
            the list of data items

            Note You cannot change the sequence of the data item in the list after an item is
            added to the list. Ensure that you enter the data items in the order you wish them to
            appear in the control.

Settings Properties

Settings properties are used to configure the data that is initially shown in a control (the
default value) and where the information collected from the user is saved. Table 49 lists
the settings properties for the Combobox control and provides a brief description of
each property.

<!-- p.1495 -->

Table 49. Combobox Control Settings
Properties
                                                                                    ﾉ   Expand table

 Property              Description

 Task sequence         Use this property to configure the task sequence variable where the
 variable name         information collected from the user is stored. If the task sequence variable:

                       - Does not already exist, the task sequence variable is created and set to the
                       value the user provides

                       - Already exists, the existing value of the task sequence variable is
                       overwritten with the value the user provides

 Friendly display      Use this property to configure the descriptive name that appears on the
 name visible in the   Summary wizard page. This name is used to describe the value that was
 summary page          saved in the Task sequence variable name property for this control.

 Unlocked              Use this property to configure whether the user is able to interact with the
                       control. By default, the control is enabled. This button displays the following
                       status:

                       - Unlocked. The control is enabled, and users can enter information using it.

                       - Locked. The control is disabled, and users are unable to enter information
                       using it.

                       Note If you disable (lock) a control, you must provide the information the
                       control collected by configuring MDT properties in CustomSettings.ini or in
                       the MDT DB. Otherwise, the UDI Wizard will not collect the necessary
                       information, and the UDI deployment will fail.

Line Control
This control allows you to add a horizontal line to divide one portion of the custom
wizard page from another. This control does not collect any configuration values but
rather is used to visually enhance the UI.

Layout Properties

Layout properties are used to configure the UI characteristics of the control and are
configured on the Layout tab in the UDI Wizard Designer. Table 50 lists the layout
properties for the Line control and provides a brief description of each property.

<!-- p.1496 -->

Table 50. Line Control Layout Properties
                                                                                     ﾉ   Expand table

 Property    Description

 X           Use this property to configure the horizontal position of the control.

 Y           Use this property to configure the vertical position of the control.

 Width       Use this property to configure the width of the control.

 Height      Use this property to configure the height of the control.

             Note Increasing this property does not increase the height or width of the line.

Settings Properties

The Line control has no settings properties.

Label Control
This control allows you to add descriptive, read-only text to the wizard page. This
control does not collect any configuration values but rather is used to visually enhance
the UI.

Layout Properties
Layout properties are used to configure the UI characteristics of the control and are
configured on the Layout tab in the UDI Wizard Designer. Table 51 lists the layout
properties for the Label control and provides a brief description of each property.

Table 51. Label Control Layout Properties
                                                                                     ﾉ   Expand table

 Property   Description

 X          Use this property to configure the horizontal position of the control.

 Y          Use this property to configure the vertical position of the control.

 Label      Use this property to configure the descriptive text associated with this control.

<!-- p.1497 -->

 Property   Description

 Width      Use this property to configure the width of the control.

            Note If the text entered in the Label property is longer than the width of the control,
            the text is clipped and not displayed.

 Height     Use this property to configure the height of the control.

            Note If the text entered in the Label property is taller than the height of the control,
            the text is clipped.

Settings Properties
The Label control has no settings properties.

Radio Control
This control allows you to select one option from a group of two or more options. As
with traditional radio buttons, you can group two or more of these controls; then, the
user can select one of the options in the group.

A unique value is assigned to each radio button. The value assigned to the selected
radio button control is saved in the task sequence variable configured for this control.

Layout Properties
Layout properties are used to configure the UI characteristics of the control and are
configured on the Layout tab in the UDI Wizard Designer. Table 52 lists the layout
properties for the Radio control and provides a brief description of each property.

Table 52. Radio Control Layout Properties
                                                                                      ﾉ   Expand table

 Property      Description

 X             Use this property to configure the horizontal position of the control.

 Y             Use this property to configure the vertical position of the control.

 Label         Use this property to configure the descriptive text associated with the radio button.

<!-- p.1498 -->

 Property        Description

 Width           Use this property to configure the width of the control.

                 Note If the text entered in the Label property is longer than the width of the
                 control, the text is clipped and not displayed.

 Height          Use this property to configure the height of the control.

                 Note If the text entered in the Label property is taller than the height of the
                 control, the text is clipped.

 RadioGroup      Use this property to group two or more radio buttons. When radio buttons belong
                 to the same group, only one of the radio buttons within a group can be selected.

                 If you need multiple groups of radio buttons, configure this property for each
                 respective group of radio buttons.

 Value           Use this property to configure the value stored in the task sequence variable when
                 the radio button is selected.

Settings Properties
Settings properties are used to configure the data initially shown in a control (the
default value) and where the information collected from the user is saved. Table 53 lists
the settings properties for the Radio control and provides a brief description of each
property.

Table 53. Radio Control Settings Properties
                                                                                     ﾉ   Expand table

 Property               Description

 Default value          Use this property to configure the default value for the control. By default,
                        the value is set to the control ID.

 Task sequence          Use this property to configure the task sequence variable where the
 variable name          information collected from the user is stored. If the task sequence variable:

                        - Does not already exist, the task sequence variable is created and set to the
                        value the user provides

                        - Already exists, the existing value of the task sequence variable is
                        overwritten with the value the user provides

<!-- p.1499 -->

 Property              Description

 Friendly display      Use this property to configure the descriptive name that appears on the
 name visible in the   Summary wizard page. This name is used to describe the value that was
 summary page          saved in the Task sequence variable name property for this control.

 Unlocked              Use this property to configure whether the user is able to interact with the
                       control. By default, the control is enabled. This button displays the following
                       status:

                       - Unlocked. The control is enabled, and users can enter information using it.

                       - Locked. The control is disabled, and users are unable to enter information
                       using it.

                       Note If you disable (lock) a control, you must provide the information the
                       control collected by configuring MDT properties in CustomSettings.ini or in
                       the MDT DB. Otherwise, the UDI Wizard will not collect the necessary
                       information, and the UDI deployment will fail.

Bitmap Control
This control allows you to add a bitmap graphic (.bmp file) to the custom wizard page.
This control does not collect any configuration values but rather is used to visually
enhance the UI.

Layout Properties
Layout properties are used to configure the UI characteristics of the control and are
configured on the Layout tab in the UDI Wizard Designer. Table 54 lists the layout
properties for the Bitmap control and provides a brief description of each property.

Table 54. Bitmap Control Layout Properties
                                                                                     ﾉ   Expand table

 Property   Description

 X          Use this property to configure the horizontal position of the control.

 Y          Use this property to configure the vertical position of the control.

 Width      Use this property to configure the width of the control.

<!-- p.1500 -->

 Property   Description

            Note If the graphic selected in the Source property is longer than the width of the
            control, the graphic is clipped.

 Height     Use this property to configure the height of the control.

            Note If the graphic selected in the Source property is taller than the height of the
            control, the graphic is clipped.

 Source     Use this property to configure the fully qualified path to the .bmp file, including the
            file name. The path to the .bmp file is relative to the location of the UDI Wizard
            (OSDSetupWizard.exe), which is on one of the following folders (where
            mdt_tookit_package is the location of the MDT toolkit package in Configuration
            Manager):

            - mdt_tookit_package\Tools\x86

            - mdt_tookit_package\Tools\x64

            To view the graphic when previewing the custom wizard page, the .bmp file must also
            be located in the following folders (where mdt_install_folder is the folder where you
            installed MDT):

            - mdt_install_folder\Template\Distribution\Tools\x86

            - mdt_install_folder \Template\Distribution\Tools\x64

Settings Properties
The Bitmap control has no settings properties.

Textbox Control
This control allows you to enter text on the custom wizard page. The text typed into this
control is saved in the task sequence variable configured for this control.

Layout Properties
Layout properties are used to configure the UI characteristics of the control and are
configured on the Layout tab in the UDI Wizard Designer. Table 55 lists the layout
properties for the Textbox control and provides a brief description of each property.

Table 55. Textbox Control Layout Properties

<!-- p.1501 -->

                                                                                      ﾉ   Expand table

 Property   Description

 X          Use this property to configure the horizontal position of the control.

 Y          Use this property to configure the vertical position of the control.

 Width      Use this property to configure the width of the control.

            Note If the text entered in the control is longer than the width of the control, the text
            is clipped and not displayed.

 Height     Use this property to configure the height of the control.

            Note If the text entered in the control is taller than the height of the control, the text is
            clipped.

Settings Properties
Settings properties are used to configure the data that is initially shown in a control (the
default value) and where the information collected from the user is saved. Table 56 lists
the settings properties for the Textbox control and provides a brief description of each
property

Table 56. Textbox Control Settings Properties
                                                                                      ﾉ   Expand table

 Property              Description

 Default value         Use this property to configure the default value for the control.

 Task sequence         Use this property to configure the task sequence variable where the
 variable name         information collected from the user is stored. If the task sequence variable:

                       - Does not already exist, the task sequence variable is created and set to
                       the value the user provides

                       - Already exists, the existing value of the task sequence variable is
                       overwritten with the value the user provides

 Friendly display      Use this property to configure the descriptive name that appears on the
 name visible in the   Summary wizard page. This name is used to describe the value that was
 summary page          saved in the Task sequence variable name property for this control.

<!-- p.1502 -->

 Property             Description

 List of validators   This property contains a list of validators used to verify that the content
 assigned to this     entered in the text box.
 control
                      You can:

                      - Add validators to the list using the blue plus sign button immediately to
                      the right of the list of validators

                      - Edit validators in the list using the pencil button immediately to the right
                      of the list of validators

                      - Remove validators from the list using the red X button immediately to the
                      right of the list of validators

 Unlocked             Use this property to configure whether the user is able to interact with the
                      control. By default, the control is enabled. This button displays the
                      following status:

                      - Unlocked. The control is enabled, and users can enter information using
                      it.

                      - Locked. The control is disabled, and users are unable to enter information
                      using it.

                      Note:

                      Note If you disable (lock) a control, you must provide the information the
                      control collected by configuring MDT properties in CustomSettings.ini or in
                      the MDT DB. Otherwise, the UDI Wizard will not collect the necessary
                      information, and the UDI deployment will fail.

UDI Task Sequence Variables
The task sequence variables in this section are used only in User-Driven Installation (UDI)
deployments. In addition to these task sequence variables, the following ZTI task
sequence variables are also used by UDI and are documented in their respective
sections earlier in this guide:

      KeyboardLocale

      OSDComputerName

      UILanguage

      UserLocale

<!-- p.1503 -->

OSDAddAdmin
This task sequence variable specifies a list of domain-based accounts or local accounts
to be added to the Administrators local built-in group on the target computer.

                                                                                  ﾉ    Expand table

 Value                            Description

 domain\account_name1;            The format of the accounts to be made members of the
 computer\account_name2           Administrators group on the target computer in the format of
                                  domain\account and separated by semicolons, where domain
                                  can be the name of an Active Directory domain or the target
                                  computer name.

                                                                                  ﾉ    Expand table

 Example

 OSDAddAdmin=domain\user01;Win7-01\LocalUser01

OSDApplicationList
This task sequence variable specifies which applications should be selected by default
on the Install Software page of the Operating System Deployment (OSD) Setup Wizard.

                                                                                  ﾉ    Expand table

 Value             Description

 app_id1;app_id2   A semicolon-delimited list of application to be selected by default on the Install
                   Software page of the Operating System Deployment (OSD) Setup Wizard; each
                   application is represented by an application ID and separated by a semicolon.
                   The application ID is derived from the Id attribute of each application in the
                   UDIWizard_Config.xml file. In the following excerpt from a
                   UDIWizard_Config.xml file, the 2007 Microsoft Office system with SP2
                   application has an Id attribute of 1:

                   <Application DisplayName="Office 2007 SP2" State="Disabled" Id="1">

                                                                                  ﾉ    Expand table

 Example

 OSDApplicationList=2;3

<!-- p.1504 -->

OSDArchitecture
This task sequence variable specifies the processor architecture of the target operating
system to be deployed.

                                                                              ﾉ   Expand table

 Value       Description

 x86         The target operating system is a 32-bit operating system.

 amd64       The target operating system is a 64-bit operating system.

                                                                              ﾉ   Expand table

 Example

 OSDArchitecture=amd64

OSDBitlockerStatus
This task sequence variable specifies if BitLocker is enabled on the target computer by
the BitLocker preflight check.

                                                                              ﾉ   Expand table

 Value          Description

 PROTECTED      The target computer has BitLocker enabled.

 Does not       If the target computer does not have BitLocker enabled, then the task sequence
 exist          variable does not exist.

                                                                              ﾉ   Expand table

 Example

 None

OSDDiskPart
This task sequence variable specifies whether the target disk partition should be
formatted.

<!-- p.1505 -->

                                                                                ﾉ   Expand table

 Value         Description

 TRUE          The target disk partition will be formatted.

 FALSE         The target disk partition will not be formatted.

                                                                                ﾉ   Expand table

 Example

 OSDDiskPart=TRUE

OSDDomainName
This task sequence variable specifies the name of the domain to which the target
computer will be joined if the computer is configured to be a domain member.

                                                                                ﾉ   Expand table

 Value          Description

 domain_name    The name of the domain to which the target computer will be joined. If you have
                configured the Computer wizard page in the Operating System Deployment
                (OSD) Setup Wizard to be Silent, the value in this task sequence variable must
                match the values specified in the UDI Wizard Designer. Otherwise, the wizard
                page will be displayed.

                Note:

                This task sequence variable is only necessary when you are creating a new
                computer account in the OU. If the computer account already exists, this variable
                is not needed.

                                                                                ﾉ   Expand table

 Example

 OSDDomainName=domain01

OSDDomainOUName
This task sequence variable specifies the name of the OU in the domain to which the
target computer account will be created when the computer joins a domain.

<!-- p.1506 -->

                                                                                    ﾉ   Expand table

 Value        Description

 ou_name      The name of the OU in the domain in which the computer account will be created

              Note:

              This task sequence variable is only necessary when you are creating a new computer
              account in the OU. If the computer account already exists, this variable is not needed.

                                                                                    ﾉ   Expand table

 Example

 OSDDomainOUName=NewDeployOU

OSDImageIndex
This task sequence variable specifies the index number of the target operating system in
a WIM file.

                                                                                    ﾉ   Expand table

 Value             Description

 index_number      The index number of the target, which is starts with an index number of 1 for the
                   first operating system in the WIM file

                                                                                    ﾉ   Expand table

 Example

 OSDImageIndex=1

OSDImageName
This task sequence variable specifies the name of the operating system image in the
.wim file selected in the Image Selection box on the VolumePage wizard page. The list
of possible operating system images in the Image Selection box is configured in the
Image Combo Box Values list in the Image Combo Box section on the VolumePage
wizard page editor. The image name is configured as a part of each image in the Image
Combo Box Values list.

<!-- p.1507 -->

  ７ Note

  Note This tasks sequence variable is set by the VolumePage wizard and should not
  be configured in the CustomSettings.ini file or in the MDT DB. However, this tasks
  sequence variable can be used to set conditions for task sequence steps, as
  described in the section, "Configure UDI Task Sequences to Deploy Different
  Operating Systems", in the MDT document Using the Microsoft Deployment Toolkit.

                                                                                ﾉ   Expand table

 Value          Description

 image_name     The name of the operating system image in the .wim file selected in the Image
                Selection box on the VolumePage wizard page

                                                                                ﾉ   Expand table

 Example

 None

OSDJoinAccount
This task sequence variable specifies the domain-based account used to join the target
computer to the domain specified in the OSDDomainName task sequence variable. This
task sequence variable is necessary if the target computer will be joined to a domain.

                                                                                ﾉ   Expand table

 Value           Description

 account_name    The name of the account used to join the target computer to the domain in the
                 format of domain\account

                                                                                ﾉ   Expand table

 Example

 OSDJoinAccount=domain\admin01

OSDJoinPassword

<!-- p.1508 -->

This task sequence variable specifies the password for the domain-based account used
to join the target computer to the domain specified in the OSDJoinAccount task
sequence variable. This task sequence variable is necessary if the target computer will be
joined to a domain.

                                                                               ﾉ   Expand table

 Value           Description

 password        The password of the account used to join the domain

                                                                               ﾉ   Expand table

 Example

 OSDJoinPassword=P@ssw0rd10

OSDLocalAdminPassword
This task sequence variable specifies the password for the Administrator local built-in
account on the target computer.

                                                                               ﾉ   Expand table

 Value       Description

 password    The password of the Administrator local built-in account on the target computer

                                                                               ﾉ   Expand table

 Example

 OSDLocalAdminPassword=P@ssw0rd10

OSDNetworkJoinType
This task sequence variable specifies whether the target computer joins a domain or a
workgroup.

                                                                               ﾉ   Expand table

<!-- p.1509 -->

 Value   Description

 0       The target computer will join a domain.

         If you select this option and configure the corresponding Operating System Deployment
         (OSD) Setup Wizard page to be Silent, you must also provide values for the
         OSDJoinAccount, OSDJoinPassword, OSDDomainName, and OSDDomainOUName task
         sequence variables accordingly. In addition, you must select Domain in Default Selection
         in the Workspace pane on the Computer Page in the UDI Wizard Designer.

 1       The target computer will join a workgroup.

         If you select this option and configure the corresponding Operating System Deployment
         (OSD) Setup Wizard page to be Silent, you must also provide a value for the
         OSDWorkgroupName task sequence variable. In addition, you must select Workgroup in
         Default Selection in the Workspace pane on the Computer Page in the UDI Wizard
         Designer.

                                                                                  ﾉ   Expand table

 Example

 OSDNetworkJoinType=0

OSDSetupWizCancelled
This task sequence variable specifies if the user canceled the Operating System
Deployment (OSD) Setup Wizard.

                                                                                  ﾉ   Expand table

 Value            Description

 TRUE             The user canceled the Operating System Deployment (OSD) Setup Wizard.

 Does not exist   If the wizard is not canceled, then the task sequence variable does not exist.

                                                                                  ﾉ   Expand table

 Example

 None

OSDTargetDrive

<!-- p.1510 -->

This task sequence variable specifies the disk volume where the target operating system
will be deployed.

                                                                               ﾉ    Expand table

 Value                         Description

 disk_volume                   The disk volume designation

                                                                               ﾉ    Expand table

 Example

 OSDTargetDrive=C:

OSDWinPEWinDir
This task sequence variable specifies the folder in which the Windows operating system
is currently installed on the target computer.

                                                                               ﾉ    Expand table

 Value               Description

 windows_directory   The directory in which the Windows operating system is currently installed

                                                                               ﾉ    Expand table

 Example

 OSDWinPEWinDir=C:\Windows

OSDWorkgroupName
This task sequence variable specifies the name of the workgroup to which the target
computer will be joined if the computer is configured to be a workgroup member.

                                                                               ﾉ    Expand table

 Value               Description

 workgroup_name      The name of the workgroup to which the target computer will be joined

<!-- p.1511 -->

                                                                              ﾉ   Expand table

 Example

 OSDWorkgroupName=WORKGROUP01

OSDResults.exe.config File Element Values
The OSD Results program, OSDResults.exe, is run at the end of a UDI deployment and
displays the results of the deployment process. The behavior of the OSD Results
program can be customized by modifying the OSDResults.exe.config file element values.
The OSDResults.exe.config file is stored in Tools\OSDResults in the MDT Package in the
User Drive Installation Task Sequence.

backgroundOpacity
This XML element configures the opaqueness of the background wallpaper image
specified as a decimal-formatted percentage in the backgroundWallpaper element.

                                                                              ﾉ   Expand table

 Value             Description

 opacity_percent   The percentage of opaqueness of the backgroundWallpaper element specified
                   in a decimal formatted percentage—for example, a value of 0.8 designates 80%
                   opaqueness.

                                                                              ﾉ   Expand table

 Example

 <add key="backgroundOpacity" value="0.8"/>

backgroundWallpaper
This XML element provides the file name and relative path to the image that is displayed
as the background in the OSD Results dialog box. The path is relative to the
Tools\OSDResults folder in the MDT Package.

                                                                              ﾉ   Expand table

<!-- p.1512 -->

 Value             Description

 path\\file_name   Includes the relative path and file name of the background image; the path is
                   delimited with double forward slashes (//).

                                                                                  ﾉ   Expand table

 Example

 <add key="backgroundWallpaper" value="images\\Wallpaper.jpg"/>

completedText
This XML element provides the text that is displayed in the OSD Results dialog box
when the deployment is complete.

                                                                                  ﾉ   Expand table

 Value   Description

 text    The text to be displayed in the OSD Results dialog box in quotation marks when
         deployment is complete

                                                                                  ﾉ   Expand table

 Example

 <add key="completedText" value="Deployment Complete"/>

headerImagePath
This XML element provides the file name and relative path to the image that is displayed
in the header of the OSD Results dialog box. The path is relative to the
Tools\OSDResults folder in the MDT Package.

                                                                                  ﾉ   Expand table

 Value             Description

 path\\file_name   Includes the relative path and file name of the header image; the path is
                   delimited with double backslashes (\\).

<!-- p.1513 -->

                                                                                    ﾉ   Expand table

 Example

 <add key="headerImagePath" value="images\\Windows7_h_rgb.png"/>

timeoutMinutes
This XML element configures how many minutes the OSD Result dialog box is displayed
before the dialog box is automatically closed and the computer is restarted.

                                                                                    ﾉ   Expand table

 Value              Description

 Non-numeric        The dialog box remains opens until Start Windows is selected.
 value

 Negative value     The dialog box remains opens until Start Windows is selected.

 0                  The dialog box remains opens until Start Windows is selected.

 Include            The dialog box remains opens until Start Windows is selected.
 decimal point

 1 - 10080          The number of minutes the dialog box will be displayed, with a minimum value
                    of 1 minute and a maximum value of 10080 minutes (1 week).

                                                                                    ﾉ   Expand table

 Example

 <add key="timeoutMinutes" value="30"/>

welcomeText
This XML element provides the welcome text that is displayed in the OSD Results dialog
box.

                                                                                    ﾉ   Expand table

 Value            Description

 welcome_text     The welcome text to be displayed in the OSD Results dialog box in quotation
                  marks

<!-- p.1514 -->

                                                                            ﾉ   Expand table

 Example

 <add key="welcomeText" value="Congratulations, Windows 7 has been successfully deployed to
 your computer."/>

Related articles
     Task Sequence Steps.
     Properties.
     Scripts.
     Support Files.
     Utilities.
     MDT Windows PowerShell Cmdlets.
     Tables and Views in the MDT DB.
     Windows 7 Feature Dependency Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1515 -->

Troubleshooting Reference for the
Microsoft Deployment Toolkit

Microsoft Deployment Toolkit (MDT) is now retired

 ） Important

 Microsoft Deployment Toolkit (MDT) is now retired. MDT integration with Configuration
 Manager and MDT Standalone are no longer supported. To prevent task sequence
 corruption and modification failures, remove all MDT task sequence steps, and then
 remove MDT integration. Consider moving to modern provisioning solutions such as
 Windows Autopilot to obtain cloud‑driven, zero‑touch provisioning for Windows devices.
 Learn more about Autopilot. For customers who have on-premises infrastructure and
 existing Configuration Manager environments, OSD remains a fully supported option.

 For full details about this retirement, see the Removed and Deprecated Features page.

 ７ Note

 In this document, Windows applies to the Windows 8.1, Windows 8, Windows 7, Windows
 Server 2012 R2, Windows Server 2012, and Windows Server 2008 R2 operating systems
 unless otherwise noted. MDT does not support ARM processor–based versions of
 Windows. Similarly, MDT refers to MDT 2013 unless otherwise stated.

 ７ Note

 The Microsoft Diagnostics and Recovery Toolset (DaRT) contains powerful tools for
 recovering and troubleshooting client computers that do not start or have become
 unstable. You can use DaRT to determine the cause of a crash, restore lost files, and so on.
 You can also use DaRT as a troubleshooting tool when developing and deploying a
 Windows operating system. For example, if a built image fails to start correctly, you can
 start the client computer containing the image by using ERD Commander—a diagnostic
 environment. Then, you can explore the client computer's hard disk, view the event log,
 remove updates, change operating system settings, and so on. DaRT is part of the

<!-- p.1516 -->

  Microsoft Desktop Optimization Pack for Software Assurance. For more information, see
  Diagnostics and Recovery Toolset 10.

Understanding Logs
Before effective troubleshooting of MDT can begin, you must have a clear understanding of the
many .log files used during an operating system deployment. When you know which log files
to research for what failure condition and at what time, issues that were once mysterious and
difficult to understand may become clear and understandable.

The MDT log file format is designed to be read by CMTrace. Use this tool whenever possible to
read the log files, because it makes finding errors much easier.

The rest of this section details the log files created during deployment as well as during
Windows Setup. This section also provides examples of when to use the files for
troubleshooting.

MDT Logs
Each MDT script automatically creates log files when running. The names of these log files
match the name of the script—for example, ZTIGather.wsf creates a log file named
ZTIGather.log. Each script also updates a common master log file (BDD.log) that aggregates the
contents of the log files that MDT scripts create. MDT log files reside in
C:\MININT\SMSOSD\OSDLOGS during the deployment process. Depending on the type of
deployment being conducted, the log files are moved at the completion of the deployment to
either %WINDIR%\SMSOSD or %WINDIR%\TEMP\SMSOSD. For Lite Touch Installation (LTI)
deployments, the logs start in C:\MININT\SMSOSD\OSDLogs. They end up in
%WINDIR%\TEMP\DeploymentLogs when the task sequence processing is complete.

MDT creates the following log files:

     BDD.log. This is the aggregated MDT log file that is copied to a network location at the
     end of the deployment if you specify the SLShare property in the Customsettings.ini file.

     LiteTouch.log. This file is created during LTI deployments. It resides in
     %WINDIR%\TEMP\DeploymentLogs unless you specify the /debug:true option.

     Scriptname*.log. This file is created by each MDT script. Scriptname represents the name
     of the script in question.

<!-- p.1517 -->

       SMSTS.log. This file is created by the Task Sequencer and describes all Task Sequencer
       transactions. Depending on the deployment scenario, it may reside in %TEMP%,
       %WINDIR%\System32\ccm\logs, or C:\_SMSTaskSequence, or C:\SMSTSLog.

       Wizard.log. The deployment wizards create and update this file.

       WPEinit.log. This file is created during the Windows PE initialization process and is useful
       for troubleshooting errors encountered while starting Windows PE.

       DeploymentWorkbench_id.log. This log file is created in the %temp% folder when you
       specify a /debug when starting the Deployment Workbench.

Configuration Manager Operating System Deployment Logs
For information about which operating system deployment log files created by Microsoft
System Center 2012 R2 Configuration Manager, see Technical Reference for Log Files in
Configuration Manager.

When running the Windows User State Migration Tool (USMT), MDT automatically adds the
logging options to save the USMT log files to the MDT log file locations. The log files and when
they are created are as follows:

       USMTEstimate.log. Created when estimating the USMT requirements

       USMTCapture.log. Created by the USMT when capturing data

       USMTRestore.log. Created by the USMT when restoring data

       The ZeroTouchInstallation.vbs script automatically scans the USMT progress log files for
       errors and warnings. The script generates event ID 41010 to Microsoft System Center
       Operations Manager with the following summary (where usmt_type is ESTIMATE,
       SCANSTATE, or LOADSTATE; error_count is the total number of errors found; and
       warning_count is the total number of warnings found):

 vbs

 ZTI USMT <usmt_type> reported <error_count> errors and <warning_count> warnings

If the error count is greater than 0, this event is an Error type. If the warning count is greater
than 0 with no errors, then the event is a Warning type. Otherwise, the event is an
Informational type.

<!-- p.1518 -->

Identifying Error Codes
Table 1 lists the error codes that the MDT scripts create and provides a description of each
error code. These error codes are recorded in the BDD.log file.

Table 1. Error Codes and Their Description

                                                                                     ﾉ   Expand table

 Error     Description
 code

 5201      A connection to the deployment share could not be made. The deployment will not proceed.

 5203      A connection to the deployment share could not be made. The deployment will not proceed.

 5205      A connection to the deployment share could not be made. The deployment will not proceed.

 5206      The Deployment Wizard was canceled or did not complete successfully. The deployment will
           not proceed.

 5207      A connection to the deployment share could not be made. The deployment will not proceed.

 5208      DeploymentType is not set. Must set some value for SkipWizard.

 5208      Unable to find the SMS Task Sequencer. The deployment will not proceed.

 5400      Create object: Set class_instance = New class_name

 5490      Create MSXML2.DOMDocument.

 5495      Create MSXML2.DOMDocument.ParseErr.ErrCode.

 5496      LoadControlFile.FindFile: ConfigFile

 5601      Verify OS guid: %OSGUID% exists.

 5602      Open XML with OSGUID: %OSGUID%.

 5610      Verify file.

 5630      Verify file: ImagePath.

 5640      Verify file: ImagePath.

 5641      FindFile: ImageX.exe.

 5643      Find BootSect.exe.

 5650      Verify directory: SourcePath.

<!-- p.1519 -->

Error   Description
code

5651    Verify directory: SourcePath\Platform.

5652    FindFile: bootsect.exe.

6001    Verify drive.

6002    Verify drive.

6010    Test for TSGUID.

6020    Robocopy returned value: Value.

6021    Robocopy returned value: Value.

6101    Check for file: DeployCab.

6102    Expand Sysprep files from DEPLOY.CAB.

6111    Run Sysprep.exe.

6121    Run Sysprep.

6191    Test for CloneTag in registry to verify Sysprep completed.

6192    Test for SystemSetupInProgress in registry to verify Sysprep completed.

6401    Authorized DHCP server.

6501    Computer backup not possible, no network path (BackupShare, BackupDir) specified.

6502    ERROR - Unable to locate IMAGEX, unable to perform backup.

6601    GetObject(... root/wmi:BCDStore).

6602    BCD.OpenStore (BCDStore).

6701    Configured protectors.

6702    Moved boot files.

6703    Create BDE partition.

6704    Defragment drive.

6705    Shrink drive.

6706    Testing for more than 1 partition.

6707    Create boot files.

6708    Encrypt the disk.

<!-- p.1520 -->

Error   Description
code

6709    Connect to MicrosoftVolumeEncryption WMI provider.

6710    Encrypting the disk.

6711    ProtectKeyWithTPM.

6712    ProtectKeyWithTPMAndPIN.

6713    ProtectKeyWithTPMAndStartupKey.

6714    Save external key to file.

6715    Protect with external key.

6716    Save external key to file.

6717    Protect key with numerical password.

6718    GetKeyProtectorNumberialP@ssword.

6718    Save password to file.

6719    Open PasswordFile.

6720    Encrypt the drive.

6721    Open DiskPartFile.

6722    Create partition.

6723    Get existing BDE drive.

6724    Open DiskPartFile.

6727    Attempt to open DiskPartFile.

6729    Create text file DiskPartFile.

6730    Execute cmd /c DISKPART.EXE /s DiskPartFile >> LogPath\ZTIMarkActive_diskpart.log 2>&1

6731    Find bcdboot.exe.

6732    Connect to Microsoft TPM provider.

6733    Get a TPM instance in the provider class.

6734    Get TPM instance.

6735    Check to see if TPM is enabled.

6736    Check to see if TPM is activated.
