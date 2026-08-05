---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1681-1720"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1681-1720
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1681-1720
family: sccm
documentKind: "doc"
abstract: "Table 55 provides information about the DesignerConfig element. Table 55. DesignerConfig Element Information ﾉ Expand table Attribute Value Number of occurrences One: This element is required. Parent elements None Contents DesignerMappings, TaskLibrary, ValidatorLibrary Element"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1681-1720

<!-- p.1681 -->

Table 55 provides information about the DesignerConfig element.

Table 55. DesignerConfig Element Information

                                                                              ﾉ     Expand table

 Attribute                        Value

 Number of occurrences            One: This element is required.

 Parent elements                  None

 Contents                         DesignerMappings, TaskLibrary, ValidatorLibrary

Element Attributes

This element has no attributes.

Remarks

None.

Example

  C++

  <DesignerConfig>
     + <TaskLibrary>
     + <ValidatorLibrary>
     + <DesignerMappings>
  </DesignerConfig>

DesignerMappings

This element groups a set of Page elements.

Element Information

Table 56 provides information about the DesignerMappings element.

Table 56. DesignerMappings Element Information

<!-- p.1682 -->

                                                                                ﾉ   Expand table

 Attribute         Value

 Number of         Zero or one within the DesignerConfig element (This element is optional if
 occurrences       there are no custom wizard page in the DLL that corresponds to this UDI
                   Wizard Designer configuration file.)

 Parent elements   DesignerConfig

 Contents          Page

Element Attributes

This element has no attributes.

Remarks

None.

Example

  C++

  <DesignerConfig>
     + <TaskLibrary>
     + <ValidatorLibrary>
     - <DesignerMappings>
          <Page DLL="SharedPages.dll"
              Description="Used to display text that describes the current
  stagegroup"
              Type="Microsoft.SharedPages.WelcomePage"
              DisplayName="Welcome"
              Image="Welcome_188.png"

  DesignerType="Microsoft.Enterprise.UDIDesigner.CoreModules.Views.WelcomePage
  View"

  DesignerAssembly="Microsoft.Enterprise.UDIDesigner.CoreModules.dll"/>
          <Page DLL="OSDRefreshWizard.dll"
             Description="Captures or restores user state data"
             Type="Microsoft.OSDRefresh.UserStatePage"
             DisplayName="User Data"
             Image="UserState_188.png"

  DesignerType="Microsoft.Enterprise.UDIDesigner.CoreModules.Views.UserStatePa
  geView"

  DesignerAssembly="Microsoft.Enterprise.UDIDesigner.CoreModules.dll"/>

<!-- p.1683 -->

          <Page DLL="OSDRefreshWizard.dll"
             Description="Allows selecting the image to install, target drive,
  and whether to format"
             Type="Microsoft.OSDRefresh.VolumePage"
             DisplayName="Volume"
             Image="Volume_188.png"

  DesignerType="Microsoft.Enterprise.UDIDesigner.CoreModules.Views.VolumePageV
  iew"

  DesignerAssembly="Microsoft.Enterprise.UDIDesigner.CoreModules.dll"/>
       </DesignerMappings>
  </DesignerConfig>

Page
This element specifies a wizard page editor to be loaded in the UDI Wizard Designer,
which is in turn used to edit the configuration settings for a wizard page.

Element Information

Table 57 provides information about the Page element.

Table 57. Page Element Information

                                                                           ﾉ    Expand table

 Attribute              Value

 Number of              One or more for each wizard page defined in the DesignerMappings
 occurrences            element

 Parent elements        DesignerMappings

 Contents               Any well-formed XML content

Element Attributes

Table 58 lists the attributes of the Page element and a description for each.

Table 58. Attributes and Corresponding Values for the
Page Element

<!-- p.1684 -->

                                                                                     ﾉ   Expand table

 Attribute          Description

 Description        Specifies text that provides information about the parameter, which is
                    displayed in the UDI Wizard Designer

 DesignerAssembly   Specifies the name of the .dll file associated with the wizard page editor (The
                    .dll file must exist in the installation_folder\Bin folder (where
                    installation_folder is the folder in which you installed MDT.)

 DesignerType       Specifies the name of the wizard page editor within the .dll file specified in
                    the DesignerAssembly attribute (This is the Microsoft .NET type for the
                    wizard page editor, with the fully qualified Microsoft .NET namespace.)

 DisplayName        Specifies the user-friendly name of the page editor, which is displayed in the
                    UDI Wizard Designer

 DLL                Specifies the name of the .dll file associated with the wizard page (The .dll
                    file must exist in the
                    installation_folder\Templates\Distribution\Tools\platform folder (where
                    installation_folder is the folder in which you installed MDT and platform is
                    x86 for the 32-bit version or x64 is for the 64-bit version.) Note: Ensure that
                    the DLL processor architecture matches the MDT processor architecture
                    installed. For example, if you installed a 32-bit version of MDT, then ensure
                    you use a 32-bit DLL for the wizard page.

 Image              Specifies the name of an image of the page that is in Portable Network
                    Graphics (PNG) format (The .png file must exist in the
                    installation_folder\Bin\Images folder (where installation_folder is the folder in
                    which you installed MDT.)

 Type               Specifies the wizard page editor and must match the named used when the
                    custom page was registered

Remarks

The UDI Wizard Designer uses the Page element like a template to create the initial XML
for a new wizard. The UDI Wizard Designer performs schema validation to ensure that
the Page and child elements have a valid format. This element provides a mapping
between the UDI Wizard page type and the information that the UDI Wizard Designer
needs to edit and create pages of this type using a custom page editor.

Example

None.

<!-- p.1685 -->

Param
This element specifies a parameter that is passed to the parent Task or Validator element
and corresponds to a Setter element in the UDI Wizard configuration file.

  ７ Note

  The attributes for this element are different if the parent is the Task or Validator
  element.

Element Information

Table 59 provides information about the Param element.

Table 59. Param Element Information

                                                                                    ﾉ   Expand table

 Attribute                       Value

 Number of occurrences           One or more for each TaskItem or Validator parent element

 Parent elements                 TaskItem, Validator

 Contents                        Any well-formed XML content

Element Attributes

Table 60 lists the attributes of the Param element and provides a description of each.

Table 60. Attributes and Corresponding Values for the
Param Element

                                                                                    ﾉ   Expand table

 Attribute         Description

 Description       Specifies text that provides information about the parameter, which is displayed
                   in the UDI Wizard Designer Note: This attribute is valid only for the Validator
                   element.

 DisplayName       Specifies the user-friendly name of the validator parameter, which is displayed for
                   the appropriate UDI Wizard page in the UDI Wizard Designer (This name is

<!-- p.1686 -->

 Attribute         Description

                   usually more descriptive than the Name attribute.) Note: This attribute is valid
                   only for the Validator element.

 Name              Specifies the name of the parameter that is passed to the task or validator,
                   depending on the parent element (This attribute will become the Property
                   attribute in a Setter element in the UDI Wizard configuration file.) Note: This
                   parameter is used for both TaskItem and Validator parent elements.

Remarks

None.

Example

None.

Task
This element specifies a task within the task library.

Element Information

Table 61 provides information about the Task element.

Table 61. Task Element Information

                                                                                     ﾉ   Expand table

 Attribute              Value

 Number of              One or more within the TaskLibrary element (This element is not optional if
 occurrences            the TaskLibrary element is specified.)

 Parent elements        TaskLibrary

 Contents               TaskItem

Element Attributes

Table 62 lists the attributes of the Task element and provides a description of each.

<!-- p.1687 -->

Table 62. Attributes and Corresponding Values for the
Task Element

                                                                                      ﾉ   Expand table

 Attribute     Description

 Description   Specifies text that provides information about the task, which is displayed in the
               UDI Wizard Designer

 DLL           Specifies the name of the .dll file associated with the task (The .dll file must exist in
               the installation_folder\Templates\Distribution\Tools\platform folder (where
               installation_folder is the folder in which you installed MDT and platform is x86 for
               the 32-bit version or x64 for the 64-bit version.)

 Name          Specifies the name of the task, which is displayed in the appropriate UDI Wizard
               page and in the UDI Wizard Designer

 Type          Specifies the task type, which is registered with the factory registry and used to call
               a specific task within a .dll file

Remarks

None.

Example

None.

TaskItem
This element specifies a group of parameters that are passed to the task.

Element Information

Table 63 provides information about the TaskItem element.

Table 63. TaskItem Element Information

                                                                                      ﾉ   Expand table

<!-- p.1688 -->

 Attribute                                  Value

 Number of occurrences                      One or more for each Task element

 Parent elements                            Task

 Contents                                   Param

Element Attributes

Table 64 lists the attributes of the TaskItem element and provides a description of each.

Table 64. Attribute and Corresponding Values for the
TaskItem Element

                                                                                      ﾉ    Expand table

 Attribute   Description

 Type        Specifies the of element type that will be created in the UDI Wizard configuration file.
             An XML element will be created that corresponds to the value of this attribute. For
             example, if the value for this attribute is File, then a File element will be created in the
             UDI Wizard configuration file.

             Currently, the only values supported are:

             - File, which requires two Param child elements (one Param child element with the
             Name attribute set to Source and another Param child element with the Name
             attribute set to Dest)
             - Setter, which requires one Param child element

Remarks

None.

Example

None.

TaskLibrary

This element groups a set of Task elements.

<!-- p.1689 -->

Element Information

Table 65 provides information about the TaskLibrary element.

Table 65. TaskLibrary Element Information

                                                                                ﾉ   Expand table

 Attribute         Value

 Number of         Zero or one within the DesignerConfig element (This element is optional if
 occurrences       there are no custom tasks in the DLL that correspond to this UDI Wizard
                   Designer configuration file.)

 Parent elements   DesignerConfig

 Contents          Task

Element Attributes

This element has no attributes.

Remarks

None.

Example

  C++

  <DesignerConfig>
     - <TaskLibrary>
          +<Task DLL="" Description="Executes a process with the given command
  line." Type="Microsoft.Wizard.ShellExecuteTask" Name="Shell Execute Task">
          +<Task DLL="OSDRefreshWizard.dll" Description="Discovers supported
  applications for install." Type="Microsoft.OSDRefresh.AppDiscoveryTask"
  Name="Application Discovery">
          +<Task DLL="SharedPages.dll" Description="Check to ensure a wired
  network connection is available."
  Type="Microsoft.SharedPages.WiredNetworkTask" Name="Wired Network Check">
          +<Task DLL="OSDRefreshWizard.dll" Description="Check to ensure power
  source is AC (not battery)." Type="Microsoft.OSDRefresh.ACPowerTask"
  Name="AC Power Check">
          +<Task DLL="" Description="Check to ensure power source is AC (not
  battery)." Type="Microsoft.Wizard.CopyFilesTask" Name="Copy Files Task">
       </TaskLibrary>
     + <ValidatorLibrary>

<!-- p.1690 -->

     + <DesignerMappings>
  </DesignerConfig>

Validator
This element specifies a validator within the validator library.

Element Information

Table 66 provides information about the Validator element.

Table 66. Validator Element Information

                                                                                     ﾉ    Expand table

 Attribute                  Value

 Number of                  Zero or more within the ValidatorLibrary element (This element is
 occurrences                optional.)

 Parent elements            ValidatorLibrary

 Contents                   Param

Element Attributes

Table 67 lists the attributes of the Validator element and provides a description of each.

Table 67. Attributes and Corresponding Values for the
Validator Element

                                                                                     ﾉ    Expand table

 Attribute         Description

 Description       Specifies text that provides information about the validator, which is displayed in
                   the UDI Wizard Designer

 DisplayName       Specifies the user-friendly name of the validator displayed in the UDI Wizard
                   Designer (This name is usually more descriptive than the Name attribute.)

 DLL               Specifies the name of the .dll file associated with the validator (The .dll file must
                   exist in the installation_folder\Templates\Distribution\Tools\platform folder (where

<!-- p.1691 -->

 Attribute         Description

                   installation_folder is the folder in which you installed MDT and platform is x86 for
                   the 32-bit version or x64 for the 64-bit version.)

 Name              Specifies the name of the validator, which is displayed in the appropriate UDI
                   Wizard page and in the UDI Wizard Designer

 Type              Specifies the validator type, which is registered with the registry factor and used
                   to call a specific validator within a .dll file

Remarks

None.

Example

None.

ValidatorLibrary
This element groups a set of Validator elements.

Element Information

Table 68 provides information about the ValidatorLibrary element.

Table 68. ValidatorLibrary Element Information

                                                                                     ﾉ    Expand table

 Attribute           Value

 Number of           Zero or one within the DesignerConfig element (This element is optional if
 occurrences         there are no custom validators in the DLL that correspond to this UDI Wizard
                     Designer configuration file.)

 Parent elements     DesignerConfig

 Contents            Validator

Element Attributes

This element has no attributes.

<!-- p.1692 -->

Remarks

None.

Example

<DesignerConfig> + <TaskLibrary> - <ValidatorLibrary> +<Validator DLL=""
Description="Requires text in a field" Type="Microsoft.Wizard.Validation.NonEmpty"
Name="NonEmpty"> +<Validator DLL="" Description="Doesn't allow certain characters
to be in a field" Type="Microsoft.Wizard.Validation.InvalidChars" Name="InvalidChars">
+<Validator DLL="" Description="Must follow a pre-defined pattern"
Type="Microsoft.Wizard.Validation.RegEx" Name="NamedPattern"> +<Validator DLL=""
Description="Require the contents match a regular expression"
Type="Microsoft.Wizard.Validation.RegEx" Name="RegEx"> </ValidatorLibrary> +
<DesignerMappings></DesignerConfig>

UDI Wizard Designer Reference

Controls
The controls used to create custom wizard page editors for use in the UDI Wizard
Designer are WPF UserControl instances. Table 69 lists the controls that you can use to
create custom wizard page editors.

Table 69. Controls That Can Be Used to Create Custom
Wizard Page Editors

                                                                                     ﾉ   Expand table

 Control               Description

 CollectionTControl    This control is used to edit data stored in the Data element within a Page
                       element.

 FieldElementControl   This control is used to edit a field, which is typically linked to a TextBox
                       control on the .xaml page.

 SetterControl         This control is used to modify the value of a setter element in the UDI
                       Wizard configuration file.

CollectionTControl

<!-- p.1693 -->

This control provides many capabilities for editing data. The best way to learn how to
use this control is to look at the sample, which shows how to edit data under a page's
Data element. In particular, the sample shows how to add, remove, and edit items in this
control.

FieldElementControl

Use this control to edit a field, which is typically linked to a TextBox control on the .xaml
page.

Example

The following excerpt from an .xaml file illustrates the use of the FieldElementControl to
configure the default value for a field on a wizard page using a child TextBox control:

  XAML

  <Controls:FieldElementControl
  Width="450"
  Margin="0,5"
  FieldData="{Binding DataContext.Location, ElementName=ControlRoot}"
  HeaderText="Location Combo Box"
  InstructionText="Here you can configure the behavior of the location combo
  box."
  HideValidationTab="True">

  <TextBox Text="{Binding FieldData.DefaultValue,
   UpdateSourceTrigger=PropertyChanged,
   Mode=TwoWay}"/>
  </Controls:FieldElementControl>

Properties

FieldData

This string property contains information for connecting the FieldElementControl to the
underlying XML for the field. The connection is made to a property of the page editor
interface. The following excerpt from an .xaml file illustrates the use of the FieldData
property:

  C++

  FieldData="{Binding DataContext.Location, ElementName=ControlRoot}"

<!-- p.1694 -->

In this excerpt, the page editor interface is called ControlRoot and is specified in the
ElementName parameter. The binding is performed to the DataContext.Location
property of the ControlRoot page editor interface. DataContext is a view model that
points to the Page element within the UDI Wizard configuration file. Location is a
property of the view that returns a list of the possible locations and is defined by a Data
element within the UDI Wizard configuration file. Each location is defined by a DataItem
element within the UDI Wizard configuration file.

HeaderText

This string property allows you to specify a header for the FieldElementControl control.
The header acts as a title for the control and is formatted as bold, orange text displayed
immediately above the control.

InstructionText

This string property allows you to specify informational text for the FieldElementControl
control. Typically, the text is used to provide a brief description of the field and explain
how configuring the field affects the corresponding wizard page.

HideEnableButton

This Boolean property allows you to control the visibility of the button that changes
state between Unlocked and Locked (enabled or disabled). If set to:

     True, the button is not visible

     False, the button is visible (This is the default value.)

HideDefaultTab

This Boolean property allows you to control the visibility of the section that contains the
control used to set the default value. Although the property refers to a tab, there is no
tab on the FieldElementControl but rather a section that can be hidden. If set to:

     True, the section is not visible

     False, the section is visible (This is the default value.)

HideBorder

<!-- p.1695 -->

This Boolean property allows you to control the visibility of the border around the field
control. If set to:

      True, the border is not visible

      False, the border is visible (This is the default value.)

HideImage

This Boolean property allows you to control the visibility of the image that the
FieldImageSource property configures. If set to:

      True, the image is not visible

      False, the image is visible (This is the default value.)

HideValidationTab

This Boolean property allows you to control the visibility of the section where the list of
validators is managed. Although the property refers to a tab, there is no tab on the
FieldElementControl but rather a section that can be hidden. If set to:

      True, the section is not visible

      False, the section is visible (This is the default value.)

HideSummaryTab

This Boolean property allows you to control the visibility of the section in which you
configure the field summary caption. The caption and corresponding value from the
field are displayed on a SummaryPage wizard page type in a stage flow. Although the
property refers to a tab, there is no tab on the FieldElementControl but rather a section
that can be hidden. If set to:

      True, the section is not visible

      False, the section is visible (This is the default value.)

HideTaskSequenceTab

This Boolean property allows you to control the visibility of the section in which you
configure the task sequence variable that corresponds to the field. Although the
property refers to a tab, there is no tab on the FieldElementControl but rather a section
that can be hidden. If set to:

<!-- p.1696 -->

        True, the section is not visible

        False, the section is visible (This is the default value.)

SetterControl

Use this control to modify the value of a Setter element in the UDI Wizard configuration
file. This control contains a child control used to modify the value of the setter element.

Example

The following excerpt from an .xaml file illustrates the use of the SetterControl to
modify a Setter element named KeyLocationSetter using a child TextBox control.

  XAML

  <Controls:SetterControl Margin="5"
          Width="450"
          HeaderText="Title text"
          SetterData="{Binding KeyLocationSetter}"
          InstructionText="What this means..."
          HorizontalAlignment="Left">

         <TextBox
                     Margin="0,3"
                     Text="{Binding SetterData.SetterValue, Mode=TwoWay,
  UpdateSourceTrigger=PropertyChanged}"
      />

  </Controls:SetterControl>

Properties

SetterData

You need to bind this to a property of your view or view model that connects to the
setter. Doing so is similar to how you would bind to a field, as described for the
FieldElementControl.

HeaderText

This property allows you to set the text that will appear in the header of the control.
Think of this property as a title for the control; by default, it appears as bold, orange
text.

<!-- p.1697 -->

InstructionText

Set this property to the text you want to appear below the header—typically instruction
text that tells the user of your custom editor when and why they would want to modify
the behavior of the field.

Interfaces
Table 70 lists the interfaces that you can use to create custom wizard page editors.

Table 70. Interfaces That Can Be Used to Create Custom
Wizard Page Editors

                                                                                ﾉ   Expand table

 Interface            Description

 IDataService         Use this interface to connect fields to the Data elements in the UDI Wizard
                      configuration file.

 IMessageBoxService   This interface provides access to methods that you can use to display
                      message boxes.

IDataService
This interface contains several properties and methods, but there is only one property
that you are like to need. That property is the only one documented here.

You can use dependency injection to obtain a pointer to this interface using code like
this in your class:

  C#

  [Dependency]
  public IDataService DataService { get; set; }

Properties

Table 71 lists the properties for the IDataService interface.

Table 71. Properties for the IDataService Interface

<!-- p.1698 -->

                                                                                ﾉ   Expand table

 Interface      Description

 CurrentPage    This property provides access to the XML elements, attributes, and values beneath
                the context of the current page being edited in the UDI Wizard configuration file

CurrentPage

  C#

  XElement CurrentPage { get; set; }

This property provides access to the XML for the current page. You should never set this
property, but you are free to modify the XML for your page. The sample page editor
shows examples of modifying the XML. You use this property primarily when you have
custom data. For fields and properties (setters), you can use prebuilt controls that take
care of all the details.

IMessageBoxService
This interface provides access to methods that you can use to display message boxes.
You may be wondering why you need an interface to display a message box. The reality
is that you do not: Microsoft uses this interface with in code, because it aids in writing
automated tests for designer pages.

However, using these methods does provide one useful benefit: The dialog boxes always
have the "owner" set to the UDI Wizard, which ensures that the dialog box is grouped
correctly with the main window.

You can use dependency injection to obtain a pointer to this interface using code like
this in your class:

  C#

  [Dependency]
  public IMessageBoxService MessageBoxes { get; set; }

Methods

Table 72 lists the methods for the IMessageBoxService interface.

<!-- p.1699 -->

Table 72. Methods for the IMessageBoxService Interface

                                                                               ﾉ   Expand table

 Method               Description

 ShowMessageBox       This overloaded method is used to display a message box with the
                      following members:

                      - ShowMessageBox(String message, String caption, MessageBoxImage
                      icon)
                      - ShowMessageBox(string message, string caption, MessageBoxButton
                      button, MessageBoxImage icon)
                      - ShowMessageBox(Exception exception)

 ShowDialogWindow     Use this method to create a new dialog box.

 ShowWizardWindow     Use this method to display a custom editor inside a dialog box that
                      includes Next and Back buttons for navigation.

ShowMessageBox

This method displays a message box that is a child of the custom wizard page editor.
This member is overloaded: Table 73 contains a list of the members and a brief
description of each. For complete information about each member (including syntax,
usage, and examples), see the section that corresponds to each member.

Table 73. Overloaded Members for the ShowMessagBox
Method

                                                                               ﾉ   Expand table

 Member                                                Description

 ShowMessageBox(String message, String caption,        Displays a message box with an icon and
 MessageBoxImage icon)                                 an OK button

 ShowMessageBox(string message, string caption,        Displays a message box with an icon and
 MessageBoxButton button, MessageBoxImage icon)        different possible combinations of
                                                       buttons

 ShowMessageBox(Exception exception)                   Displays a message box that provides
                                                       information about an exception and has
                                                       an OK button

<!-- p.1700 -->

ShowMessageBox(String message, String caption, MessageBoxImage
icon)

  C#

  void ShowMessageBox(String message, String caption, MessageBoxImage icon);

This method displays a message box with an OK button. See Table 74.

Table 74. Parameters for the ShowMessageBox(String
message, String caption, MessageBoxImage icon) Method

                                                                               ﾉ   Expand table

 Parameter     Description

 message       The message to display in the content area of the message box

 caption       The text to show in the title bar of the dialog box

 icon          The type of icon to show in the message box

ShowMessageBox(string message, string caption, MessageBoxButton
button, MessageBoxImage icon)

  C#

  MessageBoxResult ShowMessageBox(string message, string caption,
  MessageBoxButton button, MessageBoxImage icon);

This method displays a message box with the set of buttons you want shown and
reports which button you selected. See Table 75.

Table 75. Parameters for the ShowMessageBox(string
message, string caption, MessageBoxButton button,
MessageBoxImage icon) Method

                                                                               ﾉ   Expand table

 Parameter     Description

 message       The message to display in the content area of the message box

<!-- p.1701 -->

 Parameter      Description

 caption        The text to show in the title bar of the dialog box

 button         Which buttons to show

 icon           The type of icon to show in the message box

ShowMessageBox(Exception exception)

  C#

  void ShowMessageBox(Exception exception);

This method displays a message box that reports information about an exception. This
message box has a single OK button. See Table 76.

Table 76. Parameters for the ShowMessageBox(Exception
exception) Method

                                                                             ﾉ   Expand table

 Parameter   Description

 exception   The exception that you want to report (The dialog box uses exception.Message as
             the contents.)

ShowDialogWindow

  C#

  void ShowDialogWindow(Type viewType, DialogInteraction dialogPayload);

This method creates a new dialog box, the contents of which is the text you supply in
the viewType parameter. The UDI Designer creates a new instance of this type and
wraps it in a dialog box that has OK and Cancel buttons.

You pass data to your control using the dialogPayload parameter. The SampleEditor
solution in the SDK directory has an example of how to use this functionality.

ShowWizardWindow

<!-- p.1702 -->

  C#

  void ShowWizardWindow(Type viewType, DialogInteraction dialogPayload);

This method allows you to display a custom editor inside a dialog box that includes
Next and Back buttons for navigation. Microsoft has not provided a sample for how to
use this method.

UDI Wizard Configuration File Schema Reference
This file is consumed by the UDI Wizard and configured by the UDI Wizard Designer.
This file is used to configure the:

        Wizard pages displayed in the UDI Wizard

        The sequence of the wizard pages in the UDI Wizard

        Settings for the fields on each wizard page

        Available StageGroups in the UDI Wizard Designer

        Available Stages within each deployment wizard in the UDI Wizard Designer

        77 lists the elements in the UDI Wizard Configuration File and their descriptions.
        The Wizard element is the root node for this reference.

Table 77. Elements in the UDI Wizard Configuration File
and Their Descriptions

                                                                                    ﾉ   Expand table

 Element         Description
 name

 Data            Groups the individual DataItem elements within a Page element and is named by
                 the Name attribute.

 DataItem        Groups the individual Setter elements within a Page element. You can create
                 hierarchical data by including one or more Data elements within a DataItem
                 element. Each DataItem element represents an individual item. For example, a list
                 of available drives might have a DataItem for the display name and another
                 DataItem element for the corresponding drive letter.

 Default         Specifies a default value for the field specified in the parent Field or RadioGroup
                 element. The default is set to the value bracketed by this element.

<!-- p.1703 -->

Element       Description
name

DLL           Specifies a DLL that is to be loaded and referenced by the UDI Wizard and the UDI
              Wizard Designer.

DLLs          Groups the individual DLL elements.

Error         Specifies a possible error code that can a task can return. The value of the error
              code is returned by the task's HRESULT and is trapped by this element to provide
              more specific error information.

ExitCode      Specifies a possible exit code for a task. The exit codes are return codes that the
              task expects. Create an ExitCode element for each possible exit code. Otherwise,
              you can specify an asterisk (*) in the Value attribute to handle return codes not
              listed in other ExitCode elements.

ExitCodes     Groups a set of ExitCode and Error elements for a Task element or an Error
              element.

Field         Specifies an instance of a control in a Page element that is used to provide
              customization with XML. Not all controls allow customization with XML—only
              controls that use the Field element.

Fields        Groups the individual Field elements within a Page element.

File          Specifies the source and destination for a file copy operation using the
              Microsoft.Wizard.CopyFilesTask task type. You can include a separate File
              element to copy more than one file in a single task.

Page          Specifies an instance of a page and includes all the configuration settings for the
              page.

PageRef       Specifies a reference to an instance of a page within a Stage within a StageGroup.

Pages         Groups the individual Page elements.

RadioGroup    Specifies a group of radio buttons within a Field element.

StageGroup    Specifies a group of one or more stages.

StageGroups   Groups a set of stage groups within a UDI Wizard configuration file.

Setter        Specifies a property setting of a value for a property that is named in the Property
              property.

Stage         Specifies a stage within a StageGroup and contains one or more PageRef
              elements.

Style         Groups the individual setter elements that configure the UDI Wizard look and feel,
              including the title shown at the top of the wizard and the banner image shown on
              the UDI Wizard.

<!-- p.1704 -->

 Element       Description
 name

 Task          Specifies a task that is to be run on the page specified in the parent Page element.

 Tasks         Groups a set of tasks for a Page element.

 Validator     Specifies a validator for the field control that is specified in the parent Field
               element.

 Wizard        Specifies the root for all other elements.

Data
This element groups the individual DataItem elements within a Page element and is
named by the Name attribute.

Element Information

Table 78 provides information about the Data element.

Table 78. Data Element Information

                                                                                     ﾉ   Expand table

 Attribute                   Value

 Number of occurrences       Zero or more within each Page element (This element is optional.)

 Parent elements             Page, DataItem

 Contents                    DataItem, Setter

Element Attributes

Table 79 lists the attributes of the Data element and provides a description of each.

Table 79. Attributes and Corresponding Values for the
Data Element

                                                                                     ﾉ   Expand table

<!-- p.1705 -->

 Attribute           Description

 Name                Specifies the name of the Data element

Remarks

The Name attribute allows code to retrieve a specific set of data.

Example

None.

DataItem

This element groups the individual Setter elements within a Page element. You can
create hierarchical data by including one or more Data elements within a DataItem
element. Each DataItem element represents an individual item. For example, a list of
available drives might have a DataItem for the display name and another DataItem
element for the corresponding drive letter.

Element Information

Table 80 provides information about the DataItem element.

Table 80. DataItem Element Information

                                                                              ﾉ   Expand table

 Attribute                Value

 Number of occurrences    Zero or more within each Data element (This element is optional.)

 Parent elements          Data

 Contents                 Data, Setter

Element Attributes

This element has no attributes.

Remarks

<!-- p.1706 -->

None.

Example

None.

Default

This element specifies a default value for the field specified in the parent Field or
RadioGroup element. The default is set to the value that this element brackets.

Element Information

Table 81 provides information about the Default element.

Table 81. Default Element Information

                                                                              ﾉ   Expand table

 Attribute              Value

 Number of              Zero or more within a Field or RadioGroup element (This element is
 occurrences            optional.)

 Parent elements        Field, RadioGroup

 Contents               Can be any well-formed XML content but is typically standard text

Element Attributes

This element has no attributes.

Remarks

None.

Example

In the following example, the default for the TimeZone field is set to "Pacific Standard
Time":

  XML

<!-- p.1707 -->

  <Field Name="TimeZone" Enabled="true" VarName="OSDTimeZone" Summary="Time
  Zone:">
    <Default>Pacific Standard Time</Default>

DLL
This element specifies a DLL for the UDI Wizard and UDI Wizard Designer to load and
reference.

Element Information

Table 82 provides information about the DLL element.

Table 82. DLL Element Information

                                                                               ﾉ   Expand table

 Attribute                              Value

 Number of occurrences                  One or more within the DLLs element

 Parent element                         DLLs

 Contents                               No content allowed for this element

Element Attributes

Table 83 lists the attributes of the DLL element and provides a description of each.

Table 83. Attributes and Corresponding Values for the
DLL Element

                                                                               ﾉ   Expand table

 Attribute   Description

 Name        Specifies the name of the DLL for the UDI Wizard and UDI Wizard Designer to
             reference

Remarks

<!-- p.1708 -->

None.

Example

  XML

  <DLLs>
    <DLL Name="OSDRefreshWizard.dll" />
    <DLL Name="SharedPages.dll" />
  </DLLs>

DLLs
This element groups the individual DLL elements.

Element Information

Table 84 provides information about the DLLs element.

Table 84. DLLs Element Information

                                                                 ﾉ   Expand table

 Attribute                                              Value

 Number of occurrences                                  One

 Parent elements                                        Wizard

 Contents                                               DLL

Element Attributes

This element has no attributes.

Remarks

None.

Example

  XML

<!-- p.1709 -->

  <DLLs>
     <DLL Name="OSDRefreshWizard.dll" />
     <DLL Name="SharedPages.dll" />
  </DLLs>

Error
This element specifies a possible error code that a task can return. The value of the error
code is returned and trapped by the task's HRESULT to provide more specific error
information.

Element Information

Table 85 provides information about the Error element.

Table 85. Error Element Information

                                                                                     ﾉ   Expand table

 Attribute                  Value

 Number of occurrences      Zero or more within each ExitCode element (This element is optional.)

 Parent elements            ExitCodes

 Contents                   Any well-formed XML content

Element Attributes

Table 86 lists the attributes of the Error element and provides a description of each.

Table 86. Error Element Information

                                                                                     ﾉ   Expand table

 Attribute   Description

 State       Specifies the return state of a task that encountered an error. Typically, the value for
             this attribute is set to Error. This value is displayed in the State column on the wizard
             page in the UDI Wizard.

 Text        Specifies the descriptive text about the error condition that the task encountered.

<!-- p.1710 -->

 Attribute   Description

 Type        Specifies whether this element represents an error, warning, or success. The value
             specified inType must be unique within an ExitCodes element. The following are valid
             values for this element:

             - **0.**The element represent a success.
             - 1. The element represents a warning.
             - -1. The element represents an error.

 Value       Specifies the value of the code that the task returned as a numeric value. Specifying
             the value of an asterisk (*) indicates the default element for return codes that are not
             listed in other Error elements.

Remarks

None.

Example

None.

ExitCode

This element specifies a possible exit code for a task. The exit codes are return codes
that the task expects. Create an ExitCode element for each possible exit code.
Otherwise, you can specify an asterisk (*) in the Value attribute to handle return codes
not listed in other ExitCode elements.

Element Information

Table 87 provides information about the ExitCode element.

Table 87. ExitCode Element Information

                                                                                    ﾉ   Expand table

 Attribute                  Value

 Number of occurrences      Zero or more within each ExitCodes element (This element is optional.)

 Parent elements            ExitCodes

 Contents                   At least one ExitCode element and zero or more Error elements

<!-- p.1711 -->

Element Attributes

Table 88 lists the attributes of the ExitCode element and provides a description of each.

Table 88. Attributes and Corresponding Values for the
ExitCode Element

                                                                                      ﾉ   Expand table

 Attribute   Description

 State       Specifies the return state of a task. The value of this attribute is displayed in the State
             column on the corresponding wizard page in the UDI Wizard. You can use any values
             for this attribute that are meaningful for your task. The following are typical values
             used for this attribute:

             - Success
             - Warning
             - Error

 Text        Specifies the descriptive text about the exist code of the task.

 Type        Specifies whether this element represents an error, warning, or success. The value
             specified in type must be unique within an ExitCodes element. The following are valid
             values for this element:

             - 0. The element represents a success.
             - 1. The element represents a warning.
             - -1. The element represents an error.

 Value       Specifies the value of the code that the task returned as a numeric value. Specifying
             the value of an asterisk (*) indicates the default element for return codes that are not
             listed in other ExitCode elements.

Remarks

None.

Example

None.

ExitCodes

This element groups a set of ExitCode and Error elements for a Task or an Error element.

<!-- p.1712 -->

Element Information

Table 89 provides information about the ExitCodes element.

Table 89. ExitCodes Element Information

                                                                       ﾉ   Expand table

 Attribute                              Value

 Number of occurrences                  One within each Task element

 Parent elements                        Task

 Contents                               Error, ExitCode

Element Attributes

This element has no attributes.

Remarks

None.

Example

None.

Field

This element specifies an instance of a control in a Page element used to provide
customization with XML. Not all controls allow customization with XML—only controls
that use the Field element.

Element Information

Table 90 provides information about the Field element.

Table 90. Field Element Information

                                                                       ﾉ   Expand table

<!-- p.1713 -->

 Attribute                   Value

 Number of occurrences       Zero or more within each Field element (This element is optional.)

 Parent elements             Fields

 Contents                    Default, Validator

Element Attributes

Table 91 lists the attributes of the Field element and provides a description of each.

Table 91. Attributes and Corresponding Values for the
Field Element

                                                                                   ﾉ   Expand table

 Attribute   Description

 Enabled     Specifies whether the field is enabled for user input (The attribute can be set to True
             or False.)

 Name        Specifies the name of the field

 Summary     Specifies the descriptive text displayed on the Summary wizard page for the value
             that this field sets

 VarName     Specifies the task sequence variable name read or configured using the field in the
             parent Field element

Remarks

This element can contain zero or more Default elements and zero or more Validator
elements.

Example

None.

Fields
This element groups the individual Field elements within a Page element.

<!-- p.1714 -->

Element Information

Table 92 provides information about the Fields element.

Table 92. Fields Element Information

                                                                              ﾉ   Expand table

 Attribute                Value

 Number of occurrences    Zero or more within each Page element (This element is optional.)

 Parent elements          Page

 Contents                 Field, RadioGroup

Element Attributes

This element has no attributes.

Remarks

None.

Example

None.

File

This element specifies the source and destination for a file copy operation using the
Microsoft.Wizard.CopyFilesTask task type. You can include a separate File element to
copy more than one file in a single task.

Element Information

Table 93 provides information about the File element.

Table 93. File Element Information

                                                                              ﾉ   Expand table

<!-- p.1715 -->

 Attribute                 Value

 Number of                 One or more for each task that has a task type of
 occurrences               Microsoft.Wizard.CopyFilesTask

 Parent elements           Task

 Contents                  None

Element Attributes

Table 94 lists the attributes of the File element and provides a description of each.

Table 94. Attributes and Corresponding Values for the File
Element

                                                                                   ﾉ   Expand table

 Attribute   Description

 Dest        Specifies the fully qualified or relative path to the destination folder for the file
             specified in the Source attribute. Environment variables are allowed as a part of the
             path.

 Source      Specifies the fully qualified or relative path to the source file that the
             Microsoft.Wizard.CopyFilesTask task type copies. This attribute supports wildcard
             characters so that multiple files can be copied using a single File element.
             Environment variables are allowed as part of the path.

Remarks

None.

Example

None.

Page

This element specifies an instance of a page and includes all the configuration settings
for the page.

Element Information

<!-- p.1716 -->

Table 95 provides information about the Page element.

Table 95. Page Element Information

                                                                                     ﾉ   Expand table

 Attribute                               Value

 Number of occurrences                   One or more within each Pages element

 Parent elements                         Pages

 Contents                                Data, Fields, Setter, Tasks

Element Attributes

Table 96 lists the attributes of the Page element and provides a description of each.

Table 96. Attributes and Corresponding Values for the
Page Element

                                                                                     ﾉ   Expand table

 Attribute         Description

 DisplayName       Specifies the user-friendly name of the wizard page displayed in the UDI Wizard
                   Designer. This name is usually more descriptive than the Name attribute.

 Name              Specifies the name of the wizard page displayed in the UDI Wizard Designer.

 Type              Specifies the type of wizard page that directly relates to a specific wizard page
                   within a DLL.

Remarks

None.

Example

None.

PageRef

<!-- p.1717 -->

This element specifies a reference to an instance of a page within a Stage within a
StageGroup.

Element Information

Table 97 provides information about the PageRef element.

Table 97. PageRef Element Information

                                                                                   ﾉ   Expand table

 Attribute                                Value

 Number of occurrences                    One or more within a Stage element

 Parent elements                          Stage

 Contents                                 None

Element Attributes

Table 98 lists the attribute of the PageRef element and provides a description of it.

Table 98. Attributes and Corresponding Values for the
PageRef Element

                                                                                   ﾉ   Expand table

 Attribute   Description

 Page        Specifies the instance of a page within a Stage within a StageGroup. Set this value to
             the Name attribute of a Page element.

Remarks

None.

Example

None.

<!-- p.1718 -->

Pages
This element groups the individual Page elements.

Element Information

Table 99 provides information about the Pages element.

Table 99. Pages Element Information

                                                                    ﾉ   Expand table

 Attribute                                                 Value

 Number of occurrences                                     One

 Parent elements                                           Wizard

 Contents                                                  Page

Element Attributes

This element has no attributes.

Remarks

None.

Example

  C#

  <Pages>
     + <Page Name="WelcomePage" DisplayName="Welcome"
  Type="Microsoft.SharedPages.WelcomePage">
     + <Page Name="ConfigScanPage" DisplayName="Deployment Readiness"
  Type="Microsoft.OSDRefresh.ConfigScanPage">
     + <Page Name="ConfigScanBareMetal" DisplayName="Deployment Readiness"
  Type="Microsoft.OSDRefresh.ConfigScanPage">
     + <Page Name="RebootPage" DisplayName="Reboot"
  Type="Microsoft.OSDRefresh.RebootPage">
     + <Page Name="WelcomePageReplace" DisplayName="Welcome"
  Type="Microsoft.SharedPages.WelcomePage">
     + <Page Name="VolumePage" DisplayName="Volume"
  Type="Microsoft.OSDRefresh.VolumePage">
     + <Page Name="UserRestorePage" DisplayName="Select Target"

<!-- p.1719 -->

  Type="Microsoft.OSDRefresh.UserStatePage">
     + <Page Name="ComputerPage" DisplayName="New Computer Details"
  Type="Microsoft.OSDRefresh.ComputerPage">
     + <Page Name="AdminAccounts" DisplayName="Administrator Password"
  Type="Microsoft.SharedPages.AdminAccountsPage">
     + <Page Name="UDAPage" DisplayName="User Device Affinity"
  Type="Microsoft.OSDRefresh.UDAPage">
     + <Page Name="LanguagePage" DisplayName="Language"
  Type="Microsoft.OSDRefresh.LanguagePage">
     + <Page Name="ApplicationPage" DisplayName="Install Programs"
  Type="Microsoft.OSDRefresh.ApplicationPage">
       <Page Name="SummaryPage" DisplayName="Summary"
  Type="Microsoft.Shared.SummaryPage" />
     + <Page Name="UserCapturePageOldPC" DisplayName="Select Target"
  Type="Microsoft.OSDRefresh.UserStatePage">
     + <Page Name="ProgressPage" DisplayName="Capture Data"
  Type="Microsoft.OSDRefresh.ProgressPage">
     + <Page Name="RebootAfterCapture" DisplayName="Reboot"
  Type="Microsoft.OSDRefresh.RebootPage">
  </Pages>

RadioGroup
This element specifies a group of radio buttons with in a Field element.

Element Information

Table 100 provides information about the RadioGroup element.

Table 100. RadioGroup Element Information

                                                                              ﾉ   Expand table

 Attribute                Value

 Number of occurrences    Zero or more within a Fields element (This element is optional.)

 Parent elements          Fields

 Contents                 Default

Element Attributes

Table 101 lists the attributes of the RadioGroup element and provides a description of
each.

<!-- p.1720 -->

Table 101. Attributes and Corresponding Values for the
RadioGroup Element

                                                                                   ﾉ   Expand table

 Attribute   Description

 Locked      Specifies whether the group of radio buttons is enabled for user input. The attribute
             can be set to:

             - True. Specifies that the radio buttons are disabled and users cannot select a radio
             button in the group.
             - False. Specifies that the radio buttons are enabled and users can select a radio
             button in the group.

 Name        Specifies the name of the radio option group.

Remarks

None.

Example

None.

StageGroup
This element specifies a deployment stage group.

Element Information

Table 102 provides information about the StageGroup element.

Table 102. StageGroup Element Information

                                                                                   ﾉ   Expand table

 Attribute                            Value

 Number of occurrences                One or more within a StageGroups element

 Parent elements                      StageGroups
