---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 361-400"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0361-0400
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0361-0400
family: sccm
documentKind: "doc"
abstract: "The UDI Wizard defaults to using the UDIWizard_Config.xml file in the Scripts folder in the MDT Files package for configuration. You can override the default configuration file that the wizard uses by modifying the UDI Wizardtask sequence step to use the /definition parameter. T"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 361-400

<!-- p.361 -->

The UDI Wizard defaults to using the UDIWizard_Config.xml file in the Scripts folder in
the MDT Files package for configuration. You can override the default configuration file
that the wizard uses by modifying the UDI Wizardtask sequence step to use the
/definition parameter.

To override the configuration file that the UDI Wizard uses

   1. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   2. In the Software Library, go to Overview/Operating Systems/Task Sequences.

   3. In the preview pane, select task_sequence (where task_sequence is the name of the
     task sequence you want to edit).

   4. On the Ribbon, on the Home tab, in the Task Sequence group, select Edit.

     The task_sequence task_sequence_name TaskTask Sequence Editor* dialog box
     opens (where task_sequence is the name of the task sequence you want to edit).

   5. In the task_sequence Task Sequence Editor dialog box (where task_sequence is the
     name of the task sequence you want to edit), in the task sequence hierarchy, go to
     the State Capture phase.

   6. Beneath the State Capture phase, select the UDI Wizard task sequence step.

   7. On the Properties tab for the UDI Wizard task sequence step in Command line,
     modify the text as follows (where path is the path to the configuration file, which is
     relative to the Scripts folder and file_name is the name of the configuration file):

       Windows Command Prompt

        cscript.exe "%DeployRoot%\Scripts\UDIWizard.wsf" /definition:
        <path\file_name>.xml.

       ７ Note

       The above text appears on one line. The line wrap seen here is the result of
       document formatting constraints.

   8. Repeat steps 3 and 4, substituting State Capture with Preinstall/New Computer
     Only.

   9. Repeat steps 3 and 4 for any custom task sequence steps that run UDIWizard.wsf.

<!-- p.362 -->

 10. Select OK.

Configure the UDI Wizard Title and Banner Image
The UDI Wizard displays a title and a banner at the top of the wizard pages. You can
configure the UDI Wizard title and banner image for your organization in the UDI
Wizard Designer.

To configure the UDI Wizard title and banner image using the UDI
Wizard Designer

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select UDI Wizard Designer.

     The UDI Wizard Designer starts.

   2. In the UDI Wizard Designer console, on the Ribbon, in the File Menu group, select
     Open.

   3. In the Open dialog box, go to folder_path (where folder_path is the fully qualified
     path to the Scripts folder in the MDT files package source), select file_name (where
     file_name is the file name for the configuration file), and then select Open.

   4. On the Ribbon, on the Home tab, in the File Menu group, select Wizard Config.

     The Edit Wizard Settings dialog box appears.

   5. Complete the Edit Wizard Settings dialog box by performing the following steps:

     a. In Wizard Title, type wizard_title (where wizard_title is the title that you want
        displayed at the top of the UDI Wizard).

     b. In Banner Image, type image_name (where image_name is the name of the file
        that contains the image that you want displayed at the top of the UDI Wizard).

          ７ Note

          Your custom image file needs to be placed in the Tools\x64, Tools\x86, and
          Tools\OSDResults folders in the MDT files package source.

      c. Select OK.

   6. Make other appropriate changes in the UDI Wizard Designer console.

<!-- p.363 -->

   7. In the UDI Wizard Designer console, on the Ribbon, in the File Menu group, select
     Save.

     The File Save dialog box opens, notifying you that the file Save operation is
     complete.

   8. In the File Save dialog box, select OK.

   9. Close all open windows and dialog boxes.

Add a Wizard Page to a Stage
The UDI Wizard displays a sequence of wizard pages that are used to collect the
necessary information to complete the operating system and application deployment.
You can configure the wizard pages and the sequence of wizard pages displayed in the
UDI Wizard using the UDI Wizard Designer.

The list of available wizard pages is displayed in the Page Library pane. You can add
pages from the Page Library pane by dragging the wizard page from the Page Library
pane to the stage in the details pane.

To add a wizard page to a UDI stage using the UDI Wizard Designer

   1. In the UDI Wizard Designer console, in the details pane, expand stage (where
     stage is the stage you want to customize).

   2. In the Page Library pane, select wizard_page, and then drag wizard_page to the
     details pane (where wizard_page is the wizard page you want to add).

     The wizard page appears in the details pane in location where you dragged it in
     the stage.

         Tip

        Remember to save the UDI Wizard configuration file after making any
        changes.

Remove a Wizard Page from a Stage
The UDI Wizard displays a sequence of wizard pages that are used to collect the
necessary information to complete the operating system and application deployment.
You can configure the wizard pages and the sequence of wizard pages displayed in the

<!-- p.364 -->

UDI Wizard using the UDI Wizard Designer. As a part of this process, you can remove
wizard pages within a stage. Removing a wizard page from a stage does not remove a
wizard page from the Page Library pane.

  ７ Note

  If you remove a wizard page, you must provide the values for the task sequence
  variables that the wizard page configured. For more information, see the
  corresponding wizard page in the MDT document Toolkit Reference.

To remove a wizard page from a stage using the UDI Wizard Designer

   1. In the UDI Wizard Designer console, in the details pane, expand stage (where
     stage is the stage you want to customize).

   2. In the details pane, select wizard_page (where wizard_page is the wizard page you
     want to remove).

   3. On the Ribbon, on the Home tab, in the Flow Designer group, select Remove
     Item.

     The Delete Item Confirmation dialog box appears.

   4. In the Delete Item Confirmation dialog box, select Yes.

     In the details pane, the wizard page is removed from the stage.

        Tip

       Remember to save the UDI Wizard configuration file after making any
       changes.

Change the Wizard Page Sequence Flow Within a Stage
The UDI Wizard displays a sequence of wizard pages used to collect the necessary
information to complete the operating system and application deployment. You can
configure the wizard pages and the sequence of wizard pages displayed in the UDI
Wizard using the UDI Wizard Designer. As a part of this process, you can the sequence
of wizard pages within a stage.

<!-- p.365 -->

To change the wizard page sequence flow within a stage using the UDI
Wizard Designer

   1. In the UDI Wizard Designer console, in the details pane, expand stage (where
     stage is the stage you want to customize).

   2. In the details pane, select wizard_page, and then drag wizard_page to the location
     in the stage flow where you want the page to appear (where wizard_page is the
     wizard page you want to move within the stage).

     The wizard page appears in the details pane in the location to which you dragged
     it.

   Tip

  Remember to save the UDI Wizard configuration file after making any changes.

Allow or Prevent Users from Entering Information in a Control on a
Wizard Page
Each wizard page displayed by UDI Wizard either displays information about the UDI
deployment process or collects information to be used in the UDI deployment process.
Then wizard pages that collect information have one or more controls used to collect
the information.

By default, all controls are enabled on all wizard pages. Using the UDI Wizard Designer,
you can disable individual controls on each wizard page to prevent users from entering
information using those controls. The UDI Wizard designer has button that displays the
following status:

   1. Unlocked. This status indicates that the control is enabled and users can enter
     information using it.

   2. Locked. This status indicates that the control is disabled and users are unable to
     enter information using it.

  ７ Note

  If you disable (lock) a control, you must provide the information the control
  collected by configuring MDT properties in CustomSettings.ini or in the MDT DB.
  Otherwise, the UDI Wizard will not collect the necessary information, and the UDI
  deployment will fail.

<!-- p.366 -->

To allow or prevent users from entering formation in a control on a
wizard page using the UDI Wizard Designer

   1. In the UDI Wizard Designer console, in the details pane, expand stage (where
     stage is the stage you want to customize).

   2. In the details pane, select wizard_page (where wizard_page is the wizard page you
     want to remove).

   3. In the details pane, on the Configure tab, expand section, go to control(where
     section is the section where the control is located and control is the control you
     want to allow or prevent users from entering information), and then select the
     corresponding button with one of the following status indicators:

           Unlocked. Selecting the button changes the status to Locked and prevents
           users from entering information in the control.

           Locked. Selecting the button changes the status to Unlocked and allows
           users to enter information in the control.

   Tip

  Remember to save the UDI Wizard configuration file after making any changes.

Configure the User Experience for a Wizard Page

Each wizard page collects unique information that helps configure the UDI deployment
process. You can configure the user experience for each wizard page.

To configure the user experience for a specific wizard page using the
UDI Wizard Designer

   1. In the UDI Wizard Designer console, in the details pane, expand stage (where
     stage is the stage that contains the wizard page you want to customize).

   2. In the details pane, on the Flow tab, select wizard_page (where wizard_page is the
     name of the wizard page you want to customize).

   3. In the details pane, select the Configure tab.

   4. In the details pane, configure the user experience based on the type of wizard
     page being configured.

<!-- p.367 -->

     For more information about configuring the user experience for each type of
     wizard page included in MDT, see the corresponding section for the wizard page in
     the User-Driven Installation Developers Guide.

   Tip

  Remember to save the UDI Wizard configuration file after making any changes.

Preview Wizard Pages and the Wizard Page Sequence Flow
After you have the appropriate wizard pages in the correct sequence for a stage, you
can preview how the pages will appear in the UDI Wizard using the Preview feature in
the UDI Wizard Designer. The Preview feature allows you to visualize the user experience
and to make any changes to the user experience prior to performing actual
deployments.

To preview the wizard pages and wizard page sequence flow for a
stage using the UDI Wizard Designer

   1. In the UDI Wizard Designer console, in the details pane, expand stage (where
     stage is the stage you want to customize).

   2. On the Ribbon, on the Home tab, in the Preview Wizard group, select Preview.

     The UDI Wizard opens and allows you to navigate through (preview) the wizard
     pages. For each wizard page, you can see the controls displayed and whether the
     controls are enabled.

   3. After reviewing the wizard pages, close the UDI Wizard.

     You can also preview the wizard pages and the wizard page sequence flow for a
     stage by selecting the Preview hyperlink on the stage within a stage.

Add a Wizard Page to the Page Library
The Page Library in the UDI Wizard Designer contains a list of the wizard pages that you
can add to stages. Each wizard page in the Page Library maintains a count of the
number of instances in which the wizard page is used in the current version of the UDI
Wizard configuration file.

You can add a wizard page to the Page Library so that it can be added to stages.

<!-- p.368 -->

To add a wizard page to the Page Library using the UDI Wizard
Designer

   1. In the UDI Wizard Designer console, on the Ribbon, on the Home tab, in the Page
     Library group, select Add Page.

     The Add New Page dialog box appears.

   2. Complete the Add New Page dialog box by performing the following steps:

      a. In Select the page that you want to add, select page_type (where page_type is
        the page type that you want to add to the stage).

      b. In Page Name, type unique_name (where unique_name is a unique name for
        the wizard page).

              Tip

             An error message appears directly above Display Name if the Page Name
             is not unique.

      c. Select OK.

        The wizard page appears in the list of wizard pages in the Page Library.

   Tip

  Remember to save the UDI Wizard configuration file after making any changes.

You can also add a wizard page by right-clicking anywhere in the stage in the details
pane, and then selecting Add Page.

Remove a Wizard Page from the Page Library
The Page Library in the UDI Wizard Designer contains a list of the wizard pages that you
can add to stages. Each wizard page in the Page Library maintains a count of the
number of instances in which the wizard page is used in the current version of the UDI
Wizard configuration file.

You can remove a wizard page from the Page Library so that it can no longer be added
to stages.

  ７ Note

<!-- p.369 -->

  You cannot remove wizard pages from the Page Library that are currently in use in
  any stage. Verify that the wizard page is not used in any stages by viewing the in
  use count in the Page Library.

To remove a wizard page from the Page Library using the UDI Wizard
Designer

   1. In the UDI Wizard Designer console, in Page Library, select wizard_page (where
     wizard_page is the name of the wizard page you want to remove from the page
     library).

   2. On the Ribbon, on the Home tab, in the Page Library group, select Remove Page.

   3. If the wizard page is:

           In use in any stage, the Page In Use dialog box is displayed, notifying you
           that the wizard page is currently in use and cannot be removed. In the Page
           In Use dialog box, select OK.

           Not in use by any stage, the Delete Item Confirmation dialog box is
           displayed, confirming that you want to remove the wizard page. In the Delete
           Item Confirmation dialog box, select Yes.

           The wizard page is deleted from the Page Library.

   Tip

  Remember to save the UDI Wizard configuration file after making any changes.

Change the Sequence of a Stage Group or a Stage
The details pane contains a list of the stage groups and stages that the UDI Wizard
configuration file (UDIWizard_Config.xml) supports. Each stage group listed in the
details pane is used in one or more of the following MDT deployment scenarios:

     New Computer

     Refresh Computer

     Replace Computer

     You can change the sequence of a stage group or the stages within in the details
     pane.

<!-- p.370 -->

To change the sequence of a stage group using the UDI Wizard
Designer

  1. In the UDI Wizard Designer console, in the details pane, select stage_group (where
    stage_group is the name of the stage group for which you want to change the
    sequence).

  2. On the Ribbon, on the Home tab, in the Flow Designer group, select one of the
    following:

         Move Up to make the stage group appear earlier in the list of scenarios

         Move Down to make the stage group appear later in the list of scenarios

         The stage group moves up or down in the list of stage group based on the
         option you select.

    You can also change the sequence of a stage group by right-clicking the stage
    group, and then selecting Move Up or Move Down based on the desired result.

  Tip

 Remember to save the UDI Wizard configuration file after making any changes.

To change the sequence of a stage within a stage group using the UDI
Wizard Designer

  1. In the UDI Wizard Designer console, in the details pane, expand stage_group, and
    then select stage (where stage_group is the name of the stage group that contains
    the stage and stage is the name of the stage for which you want to change the
    sequence).

  2. On the Ribbon, on the Home tab, in the Flow Designer group, select one of the
    following:

         Move Up to make the stage appear earlier in the list of stages within the
         stage group

         Move Down to make the stage appear later in the list of stages within the
         stage group

         The stage moves up or down in the list of stages within the stage group
         based on the option you select.

<!-- p.371 -->

     You can also change the sequence of a stage by right-clicking the stage, and then
     selecting Move Up or Move Down based on the desired result.

   Tip

  Remember to save the UDI Wizard configuration file after making any changes.

Prepare for Language Pack Deployment in UDI

One the UDI Wizard page types available in the Page Library in the UDI Wizard Designer
is the LanguagePage wizard page type. The LanguagePage wizard page type allows you
to select the:

     Default language

     Time and currency format (locale)

     Keyboard layout

     Time zone

     Specifically, the LanguagePage wizard page allows you select the default language
     of the target operating system. However, additional steps must be performed to
     support the selection and subsequent deployment of the language pack for the
     target operating system.

To support the deployment of multiple languages as the default
language for target computers

   1. Add a language pack that you want to support in UDI using the Install Language
     Packs Offline task sequence as described in Add Language Packs in Configuration
     Manager

   2. For the Install Language Packs Offline task sequence step created in step 1,
     configure the task sequence step to run on the condition that the UILanguage task
     sequence variable is equal to the language pack added in step 1

         Tip

        You configure conditions on the Options tab of the task sequence step. Add a
        Task Sequence Variable condition.

<!-- p.372 -->

     For example, if you add a Japanese language pack, then the condition for the
     corresponding Install Language Packs Offline task sequence step will be for the
     UILanguage task sequence variable to be equal to JA-JP.

     For more information on the LanguagePage wizard page type in the UDI Wizard
     Designer, see the corresponding section in the User-Driven Installation Developers
     Guide.

Skip a Wizard Page
In some instances, you may want to further control and simplify the UDI Wizard
experience by skipping (removing) wizard pages. Skipping a wizard page allows you to
provide configuration values usually provided by the user for the wizard page. Also,
skipping a wizard page is simpler and less confusing than disabling (locking) all the
controls on a wizard page.

To skip a wizard page

   1. Identify the variables that are written by the wizard page in a specific stage.

     To identify the variables written by a specific wizard page, see the corresponding
     section for the wizard page in "UDI Wizard Page Reference".

   2. Configure the variables identified in the previous step in the CustomSettings.ini or
     the MDT DB.

   3. Remove the wizard page from the stage within a stage by using the Remove Item
     action on the Ribbon in the Flow Designer group.

Creating Custom Wizard Pages Using the Build Your Own
Page Feature
There may be instances in which you want to collect additional deployment information
to be used in UDI. You must collect this additional information in the UDI Wizard using a
custom wizard page. You can create custom wizard pages using the:

     Build Your Own Page feature. This feature allows you to create a custom wizard
     page for collecting deployment information without requiring you to write code or
     have developer skills. Use this feature if you need to collect basic information
     without advanced user interaction. For example, you cannot add any code or
     customize UI fonts using this feature.

<!-- p.373 -->

     UDI SDK and Visual Studio. Use this SDK if you want to create an advanced, fully
     customized wizard page in Visual Studio for collecting deployment information.
     Although the UDI SDK allows you to create customized wizard pages, such as
     adding custom code or changing fonts, this method requires developer skills.

     For more information on using the UDI SDK to create custom wizard pages, see
     "Creating Custom UDI Wizard Pages" in the User-Driven Installation Developers
     Guide.

     Create custom wizard pages using the Build Your Own Page Feature in UDI by
     performing the following tasks:

     Create a new custom wizard page in a stage group as described in Create a New
     Custom Wizard Page.

     Add a control to a custom wizard page as described in Add a Control to a Custom
     Wizard Page.

     Position a control on a custom wizard page as described in Position a Control on a
     Custom Wizard Page.

     Change the size of a control on a custom wizard page as described in Change the
     Size of a Control on a Custom Wizard Page.

     Remove a control from a custom wizard page as described in Remove a Control
     from a Custom Wizard Page.

     Edit the properties of a control on a custom wizard page as described in Edit
     Custom Wizard Page Control Properties.

     Show or hide the gridlines on a custom wizard page as described in Show or Hide
     Custom Wizard Page Gridlines.

     Verify and test the custom wizard page after you create it as described in Verify
     and Test a Custom Wizard Page.

Create a New Custom Wizard Page
UDI custom wizard pages created using the Build Your Own Page feature allow you to
collect deployment information in addition to the information collected on other UDI
Wizard pages. You create custom wizard pages based on the Build Your Own Page
wizard page type. After you create the custom wizard page, you can add controls to the
wizard page and configure the task sequence variables that the controls set.

<!-- p.374 -->

To create a new custom wizard page

   1. Select Start, point to All Programs, point to Microsoft Deployment Toolkit, and
     then select UDI Wizard Designer.

     The UDI Wizard Designer starts.

   2. Open the .xml file

   3. On the Ribbon, on the Home tab, in the Page Library group, select Add Page.

     The Add New Page dialog box appears.

   4. In the Add New Page dialog box, in the Page Type column, select Build Your Own
     Page.

   5. In Display Name, type display_name (where display_name is the user-friendly
     name of the wizard page and appears in the wizard navigation progress pane).

   6. In Page Name, type page_name (where page_name is name of the wizard page
     and must be unique in the Page Library), and then select OK.

     The new custom wizard page appears in the Page Library.

   7. In the details pane, select the Flow tab.

   8. On the Flow tab, expand stage_group (where stage_group is the name of the stage
     group to which you want to add the new custom wizard page).

     The list of wizard pages in the stage group is displayed.

   9. In the Page Library, select display_name. Drag the page to the appropriate place in
     stage_group on the Flow tab (where display_name is the user-friendly name of the
     wizard page and stage_group is the name of the stage group to which you want to
     add the new custom wizard page).

Add a Control to a Custom Wizard Page
After a new UDI custom wizard page is added to a stage group, you must add the
appropriate controls to the new custom wizard page. You add these controls from the
Build Your Own Page toolbox, which is displayed when you view the custom wizard page
on the Configure tab in the UDI Wizard Designer.

Table 149 lists the types of controls to your custom wizard page, which is illustrated in
Figure 13.

<!-- p.375 -->

Table 149. Types of Controls in the UDI Build Your Own
Page Toolbox

                                                                                 ﾉ   Expand table

Control    Description
type

Checkbox   This control allows you select or clear a configuration option and behaves as a
           traditional UI check box. This control has a corresponding label that you can use to
           describe the purpose of the check box. The state of this control is True when the
           check box is selected and False when the check box is cleared. The state of the
           check box is stored in the task sequence variable configured for this control. For
           more information on this control, see "Checkbox Control" in the MDT document,
           Toolkit Reference.

Combobox   This control allows you to select an item from a list of items and behaves as a
           traditional UI drop-down list. This control allows you to add or remove items from
           the list and provide a corresponding value that will be set in the task sequence
           variable configured for this control. For more information on this control, see
           "Combobox Control" in the MDT document, Toolkit Reference.

Line       This control allows you to add a horizontal line to divide one portion of the custom
           wizard page from another. This control does not collect any configuration values
           but rather is used to visually enhance the UI. For more information on this control,
           see "Line Control" in the MDT document, Toolkit Reference.

Label      This control allows you to add descriptive, read-only text to the wizard page. This
           control does not collect any configuration values but rather is used to visually
           enhance the UI. For more information on this control, see "Label Control" in the
           MDT document, Toolkit Reference.

Radio      This control allows you to select one configuration option from a group of two or
           more options. As with traditional radio buttons, two or more of these controls can
           be grouped together, and then the user can select one of the options in the radio
           button group. A unique value is assigned to each option. The value assigned to the
           selected option control is saved in the task sequence variable configured for this
           control. For more information on this control, see "Radio Control" in the MDT
           document, Toolkit Reference.

Bitmap     This control allows you to add a bitmap graphic (.bmp file) to the custom wizard
           page. This control does not collect any configuration values but rather is used to
           visually enhance the UI. The path to the .bmp file is relative to the location of the
           UDI Wizard (OSDSetupWizard.exe). For more information on this control, see
           "Bitmap Control" in the MDT document, Toolkit Reference.

Textbox    This control allows you to enter text on the custom wizard page. The text typed into
           this control is saved in the task sequence variable configured for this control. For

<!-- p.376 -->

 Control       Description
 type

               more information on this control, see "Textbox Control" in the MDT document,
               Toolkit Reference.

You can add any combination of these controls to your custom wizard page based on
the information you want to collect. In addition, you can use the Show Gridlines check
box to show or hide gridlines that can be used to assist in visually designing the custom
wizard page.

Figure 13 provides an example of a custom wizard page and the Build Your Own Page
toolbox.

Figure 13. Example custom wizard page

To add a control to a custom wizard page

   1. In the UDI Wizard Designer, in the Page Library, select custom_wizard_page (where
     custom_wizard_page is the name of the custom wizard page to which you want to
     add the control).

     If you have not already added a custom wizard page based on the Build Your Own
     Page wizard page type to the Page Library, add a custom wizard page. For more
     information on how to add a custom wizard page based on the Build Your Own
     Page wizard page type to the Page Library, see Create a New Custom Wizard Page.

<!-- p.377 -->

   2. In the details pane, select the Configure tab.

     The custom wizard page is displayed in the details pane.

   3. In the Build Your Own Page toolbox, select toolbox_control (where toolbox_control
     is the type of control you want to add to the custom wizard page), and drag it to
     the custom wizard page.

     The control is added to the custom wizard page.

Position a Control on a Custom Wizard Page
After a control has been added to a custom wizard page, you can position the control
by performing one of the following tasks:

     Position a control on a custom wizard page using drag and drop as described in
     Position a Control on a Custom Wizard Page Using Drag and Drop.

     Position a control on a custom wizard page using control properties as described
     in Position a Control on a Custom Wizard Page Using Control Properties.

Position a Control on a Custom Wizard Page Using Drag and Drop

You can position a control on a custom wizard page using drag and drop for one of the
following situations:

   1. Initially placing the control from the Build Your Own Page to the custom wizard
     page

   2. Moving the control to an approximate location on the custom wizard page

     To position a control more precisely, position the control using the X and Y
     properties on the Layout properties of the control. For more information on
     positioning a control on a custom wizard page using control properties, see
     Position a Control on a Custom Wizard Page Using Control Properties.

To position a control on a custom wizard page using drag and drop

   1. In the UDI Wizard Designer, in the Page Library, select custom_wizard_page (where
     custom_wizard_page is the name of the custom wizard page to which you want to
     position the control).

     If you have not already added a custom wizard page based on the Build Your Own
     Page wizard page type to the Page Library, add a custom wizard page. For more

<!-- p.378 -->

     information about how to add a custom wizard page based on the Build Your Own
     Page wizard page type to the Page Library, see Create a New Custom Wizard Page.

   2. In the details pane, select the Configure tab.

     The custom wizard page is displayed in the details pane.

   3. In the details pane, select toolbox_control (where toolbox_control is the control you
     want to position on the custom wizard page), and then drag it to the desired
     location on the custom wizard page.

         Tip

        You can use the x and y coordinate locations displayed at the top of the
        custom wizard page to help you position the control.

Position a Control on a Custom Wizard Page Using Control
Properties

Position a control on a custom wizard page when you want to control the placement of
the control so that all your controls are aligned precisely. You position the control using
the X and Y properties on the Layout properties of the control.

To position a control approximately, such as when you are doing your initial layout, do
so using drag and drop. For more information on positioning a control on a custom
wizard page using drag and drop, see Position a Control on a Custom Wizard Page
Using Drag and Drop.

To position a control on a custom wizard page using control
properties

   1. In the UDI Wizard Designer, in the Page Library, select custom_wizard_page (where
     custom_wizard_page is the name of the custom wizard page to which you want to
     position the control).

     If you have not already added a custom wizard page based on the Build Your Own
     Page wizard page type to the Page Library, then add a custom wizard page. For
     more information about how to add a custom wizard page based on the Build
     Your Own Page wizard page type to the Page Library, see Create a New Custom
     Wizard Page.

   2. In the details pane, select the Configure tab.

<!-- p.379 -->

     The custom wizard page is displayed in the details pane.

   3. In the details pane, select toolbox_control (where toolbox_control is the control you
     wish to position on the custom wizard page), and then select the Layout tab.

   4. On the Layout tab, configure the values for the properties listed in Table 150 based
     on the coordinates at which you want the control to be located.

     Table 150. Control Position Layout Properties

                                                                                   ﾉ   Expand table

      Property      Description

      X             This property controls the horizontal position of the control.

      Y             This property controls the vertical position of the control.

     After the properties are configured, the control is positioned at the coordinates
     specified by these properties.

Change the Size of a Control on a Custom Wizard Page
Change the size of a control on a custom wizard page so that the contents of the
control are properly displayed. You change the size of the control using the Width and
Height properties on the Layout properties of the control.

To change the size of a control on a custom wizard page

   1. In the UDI Wizard Designer, in the Page Library, select custom_wizard_page (where
     custom_wizard_page is the name of the custom wizard page to which you want to
     position the control).

   2. In the details pane, select the Configure tab.

     The custom wizard page is displayed in the details pane.

   3. In the details pane, select toolbox_control (where toolbox_control is the control you
     wish to change in size on the custom wizard page), and then select the Layout tab.

   4. On the Layout tab, configure the values for the properties listed in Table 151 based
     on the size you want the control to be.

<!-- p.380 -->

     Table 151. Control Size Layout Properties

                                                                                  ﾉ    Expand table

      Property   Description

      Width      This property controls the width of the control.

                 If the text or graphic displayed in the control is wider than the width of the
                 control, the text or graphic is clipped and not displayed.

      Height     This property controls the height of the control.

                 If the text or graphic displayed in the control is higher than the height of the
                 control, the text or graphic is clipped and not displayed.

     After the properties are configured, the size of the control reflects the values in
     these properties.

Remove a Control from a Custom Wizard Page
Remove a control from a custom wizard page when the control is no longer needed on
the custom wizard page. Once you remove a control from a custom wizard page, all
Layout and Settings properties associated with the control are also removed. Once the
control has been removed and the UDI Wizard configuration file has been saved, the
removal cannot be undone.

   Tip

  If you want to undo removal of a control, close the UDI Wizard without saving
  changes.

To remove a control from a custom wizard page

  1. In the UDI Wizard Designer, in the Page Library, select custom_wizard_page (where
     custom_wizard_page is the name of the custom wizard page from which you want
     to remove the control).

  2. In the details pane, select the Configure tab.

     The custom wizard page is displayed in the details pane.

<!-- p.381 -->

   3. In the details pane, select toolbox_control (where toolbox_control is the control you
     want to remove from the custom wizard page), and then select the red X in the
     upper right corner of the control.

     The control is removed from the custom wizard page.

Edit Custom Wizard Page Control Properties

Each control that you place on your custom wizard page has properties. These
properties are used to configure the appearance of the control and how the UDI Wizard
processes the information the control collects.

The following types of properties are available for Build Your Own Page toolbox
controls:

     Layout properties. Use these properties to configure the UI characteristics of the
     control. Every control has Layout properties, such as the Y, X, Width, and Height
     properties.

     For more information about the Layout properties for a specific control, see the
     corresponding section for each control in "UDI Build Your Own Page Toolbox
     Control Reference" in the MDT document, Toolkit Reference.

     Settings properties. Use these properties to configure the data that is initially
     shown in a control (default value) and where the information collected from the
     user is saved. Only controls that collect information have Settings properties, such
     as the Task sequence variable name and Friendly display name visible in
     summary page properties.

     For more information about the Settings properties for a specific control, see the
     corresponding section for each control in "UDI Build Your Own Page Toolbox
     Control Reference" in the MDT document, Toolkit Reference.

     To edit custom wizard page control properties

        1. In the UDI Wizard Designer, in the Page Library, select custom_wizard_page
            (where custom_wizard_page is the name of the custom wizard page on which
            you want to position the control).

        2. In the details pane, select the Configure tab.

            The custom wizard page is displayed in the details pane.

<!-- p.382 -->

        3. In the details pane, select toolbox_control (where toolbox_control is the
           control you want to position on the custom wizard page).

        4. Select the Layout tab to configure the Layout properties.

           For more information about the Layout properties for a specific control, see
           the corresponding sections for each control in "UDI Build Your Own Page
           Toolbox Control Reference" in the MDT document, Toolkit Reference.

        5. Select the Settings tab to configure the Settings properties.

           For more information about the Settings properties for a specific control, see
           the corresponding sections for each control in "UDI Build Your Own Page
           Toolbox Control Reference" in the MDT document, Toolkit Reference.

Show or Hide Custom Wizard Page Gridlines
You can show or hide gridlines on your custom wizard pages. The gridlines help you
place controls so that they are aligned properly to each other.

To show or hide custom wizard page gridlines

   1. In the UDI Wizard Designer, in the Page Library, select custom_wizard_page (where
     custom_wizard_page is the name of the custom wizard page on which you want to
     position the control).

   2. In the details pane, select the Configure tab.

     The custom wizard page is displayed in the details pane.

   3. In the details pane, select or clear the Show Gridlines check box.

     The Show Gridlines check box determines whether the gridlines are displayed on
     the custom wizard page. If theShow Gridlines check box is:

           Selected, then the gridlines are displayed

           Cleared, then the gridlines are not displayed

Verify and Test a Custom Wizard Page
After you create your custom wizard page and configure the appropriate controls, verify
that your custom wizard page behaves as expected. You can verify and test your custom
wizard page using the preview feature in the UDI Wizard Designer.

<!-- p.383 -->

The preview feature allows you to visualize the user experience and make any changes
to the user experience prior to performing actual deployments. You can interact with
your custom wizard page as though you were the user running the UDI Wizard.

For more information on how to preview wizard pages and the wizard page sequence
flow, see Preview Wizard Pages and the Wizard Page Sequence Flow.

Running the UDI Wizard
The UDI Wizard is automatically initiated when you run a UDI-based task sequence.
Initiate the UDI-based task sequence automatically by using Windows Deployment
Services or manually by using a deployed (advertised) task sequence in the
Configuration Manager Client. Each MDT deployment scenario (New Computer, Refresh
Computer, or Replace Computer) uses a different process. Initiate the deployment from
Windows Deployment Services or using task sequence bootable media. The deployment
process prompts for any configuration settings not already specified.

The UDI Wizard displays wizard pages based on the MDT deployment scenario you
selected and the configuration options you saved in UDI Wizard configuration file
(UDIWizard_Config.xml) in the Scripts folder of the MDT files package. The controls that
are enabled and their default values are also controlled by the configuration options you
saved in the UDI Wizard configuration file.

To run the UDI Wizard
   1. Initiate the task sequence created using a UDI-based task sequence template and
     one of the following methods:

          Task sequence bootable media disk using the Task Sequence Media Wizard as
          described in Creating Task Sequence Bootable Media in Configuration
          Manager.

          Windows Deployment Services to start the appropriate Windows PE images
          that will in turn start the UDI deployment process to the target computers as
          described in Preparing Windows Deployment Services for UDI Deployments.

          Windows PE starts, and then the Task Sequence Wizard starts.

   2. Complete the Task Sequence Wizard by selecting the appropriate UDI-based task
     sequence.

     At the appropriate task sequence step, the UDI Wizard starts.

<!-- p.384 -->

  3. Complete the UDI Wizard based on the wizard pages selected and the sequence of
    the wizard pages.

       Tip

      Ensure that you preview the user experience of the wizard pages in the UDI
      Wizard using the Preview feature in the UDI Wizard Designer prior to
      performing deployments in your production environment.

    After you complete the UDI Wizard, the deployment of the new operating system
    begins. When the deployment process is complete, the OSD Results page is
    displayed just prior to the first user logging on to the target computer. For more
    information about how to configure the OSD Results page, see the section,
    "OSDResults.exe.config File Element Values", in the MDT document Toolkit
    Reference.

Configuring MDT Deployments
Configure MDT deployments by:

    Customizing the CustomSettings.ini and Bootstrap.ini files as described in
    Customizing MDT Configuration Files

    Customizing the MDT properties as described in Configuring the Appropriate MDT
    Properties

    Applying the MDT properties to groups of computers as described in Applying
    MDT Properties to Groups of Computers

    Applying the MDT properties to individual computers as described in Applying
    MDT Properties to Individual Computers

    Configuring the MDT processing rules as described in Configuring MDT Processing
    Rules

    Preparing disks on the target computers as described in Preparing Disks on Target
    Computers

    Saving and restoring the user state migration data using USMT as described in
    Saving and Restoring User State Information

    Joining target computers to AD DS domains as described in Joining Target
    Computers to AD DS Domains

<!-- p.385 -->

     Deploying software updates to the target computers as described in Deploying
     Software Updates to Target Computers

     Managing device drivers in MDT deployments as described in Managing Device
     Drivers

     Running Microsoft System Center 2012 Orchestrator runbooks from MDT as
     described in Running Orchestrator Runbooks

     Running Windows PowerShell scripts in a task sequence as described in Running
     Windows PowerShell Scripts During Deployment

     Applying security and compliance configuration settings using Group Policy Object
     Packs as described in Applying Group Policy Object Packs

     Enabling participation in Windows Customer Experience Improvement
     Program    (CEIP) and Windows Error Reporting (WER) as described in Enabling
     Participation in CEIP and WER

     Configuring the task sequence steps that configure Windows roles and features on
     the target computer as described in Configuring Roles and Features Task Sequence
     Steps

     Configuring server roles for Windows Server operating systems in MDT
     deployments as described in Configuring Server Role Task Sequence Steps

     Copying content to the target computers for MDT deployments as described in
     Copying Content to the Target Computer

     Creating custom scripts that integrate with the MDT deployment processes as
     described in Creating Custom Scripts for MDT

Customizing MDT Configuration Files
MDT is flexible and highly customizable with the MDT configuration files. The following
sections contain configuration samples that demonstrate how to customize the
deployment process.

Customize the MDT configuration files by:

     Identifying the syntax of the CustomSettings.ini file as described in Identify the
     CustomSettings.ini File Syntax

     Identifying the sections of the CustomSettings.ini file as described in Sections in
     the CustomSettings.ini File

<!-- p.386 -->

        Configuring the properties in the CustomSettings.ini file as described in Properties
        in the CustomSettings.ini File

        Configuring subsections in the CustomSettings.ini file as described in Subsections
        in the CustomSettings.ini File

        Configuring the CustomSettings.ini file to run user exit scripts using the UserExit
        directive as described in User Exit Scripts in the CustomSettings.ini File

        Configuring the basic configuration settings for the CustomSettings.ini file for LTI
        deployments as described in Basic CustomSettings.ini File for LTI Deployments

        Configuring the basic configuration settings for the CustomSettings.ini file for ZTI
        deployments in Configuration Manager as described in Basic CustomSettings.ini
        File for ZTI Deployments Using Configuration Manger

        Identifying the syntax of the BootStrap.ini file as described in Identify the
        BootStrap.ini File Syntax

Identify the CustomSettings.ini File Syntax
The syntax of the CustomSettings.ini file is similar to many .ini files. A CustomSettings.ini
file includes:

        Sections

        Properties

        Settings

        Listing 1 shows a CustomSettings.ini file customized for ZTI for Configuration
        Manager. For more information about the CustomSettings.ini file in Listing 1, see
        Basic CustomSettings.ini File for ZTI Deployments Using Configuration Manger,
        later in this guide.

        Listing 1. CustomSettings.ini File Customized for ZTI Deployment for
        Configuration Manager

  ini

  [Settings]
  Priority=Default, MACAddress
  Properties=CustomProperty

  [Default]
  OSInstall=Y

<!-- p.387 -->

  ScanStateArgs=/v:5 /o /c
  LoadStateArgs=/v:5 /c /lac
  UserDataLocation=NONE

  [00:0F:20:35:DE:AC]
  CustomProperty=TRUE

  [00:03:FF:FE:FF:FF]
  CustomProperty=FALSE

Sections in the CustomSettings.ini File
Sections are identified by brackets ( [] ) that surround the section name (for example,
[Settings] ). In Listing 1, the sections include [Settings] , [Default] ,
[00:0F:20:35:DE:AC] , and [00:03:FF:FE:FF:FF] .

The sections in the CustomSettings.ini file include the:

     Required sections as described in Required Sections

     Optional sections as described in Optional Sections

Required Sections

Only the [Settings] section is required. All other sections are optional. The MDT scripts
require the [Settings] section in CustomSettings.ini to locate the reserved properties
(Priority and Properties).

Optional Sections

You use the optional sections in the CustomSettings.ini file to assign a group of
configuration settings to:

     A group of computers. In Listing 1, the configuration settings in the
      [Default] section are applied to more than one computer. For more information,

     see Applying MDT Properties to Groups of Computers, later in this guide.

     An individual computer. In Listing 1, the configuration settings in the
      [00:0F:20:35:DE:AC] and [00:03:FF:FE:FF:FF] sections are applied to the

     corresponding computer (in this case, identified by the media access control [MAC]
     address of the target computer). For more information, see Applying MDT
     Properties to Individual Computers, later in this guide.

<!-- p.388 -->

Properties in the CustomSettings.ini File
Properties are variables to which values must be assigned. Properties are followed by an
equal sign (=). The scripts scan the CustomSettings.ini file to locate the properties.

The types of properties that you can use in deploying target computers include
properties that are:

     Automatically declared in ZTIGather.wsf. These predefined properties are
     declared in the ZTIGather.wsf code and are documented in the MDT document
     Toolkit Reference. In addition, the ZTIGather.wsf file automatically sets the values
     for these properties. These properties are not configured in CustomSettings.ini and
     should be treated as read only.

     Declared in the ZTIGather.xml file. These predefined properties are listed in the
     ZTIGather.xml file and are documented in the MDT document Toolkit Reference.
     The ZTIGather.wsf file retrieves these properties by scanning the ZTIGather.xml file.
     Divide the properties in this file into properties that:

        ZTIGather.wsf automatically assigns values to. ZTIGather.wsf automatically sets
        the values for these properties, which must be treated as read only.

        Must be assigned values in CustomSettings.ini. Ensure that the value for any
        property to be used is set in CustomSettings.ini and is considered modifiable.

     Declared in the Properties property. These are custom properties that can be
     declared, and they are in addition to the properties automatically declared in
     ZTIGather.wsf and in ZTIGather.xml.

     The way you use properties for ZTI and LTI are identical. However, some properties
     are unique to ZTI or LTI deployment. Like ZTI deployments, LTI deployments also
     have unique properties. Most of the LTI-specific properties relate to the
     Deployment Wizard (such as SkipAdministratorPassword, SkipCapture, or
     SkipUserData). Although these properties use the same syntax as other properties,
     the reserved properties perform specific functions in the deployment processing
     rules.

  ７ Note

  Property values must be specified in upper case so that the deployment scripts can
  properly identify them—for example, YES, TRUE, or FALSE. This is true for property
  values specified in the CustomSettings.ini file, BootStrap.ini file, and MDT DB.

<!-- p.389 -->

Configure the CustomSettings.ini file by:

     Configuring the Priority reserved property as described in Priority Reserved
     Property

     Configuring the Properties reserved property as described in Properties Reserved
     Property

     Configuring the values for properties as described in Values in the
     CustomSettings.ini File

Priority Reserved Property

The Priority reserved property determines the sequence and section in which you can
find configuration values. Each section is searched in the order specified. When a
property value is found, the remaining sections are not used for that property. In Listing
1, the [Default] section is parsed first, and then the section that corresponds to the
MAC address of the target computer (in this case, [00:0F:20:35:DE:AC] or
[00:03:FF:FE:FF:FF] ).

Table 152 lists the types of sections that you can reference in the Priority property.

Table 152. Section Types for the Priority Property

                                                                                   ﾉ   Expand table

 Type         You can base sections on

 MDT          Any property known MDT. For example, specifying the HostName property causes
 properties   MDT to scan for a section with the target computer host name. Other properties,
              like MACAddress, can result in multiple section names being checked (because a
              computer can have multiple MAC addresses).

 Literal      A literal name that you specify in the Priority property. For example, if MySection is
 section      included in the Priority property, MDT would search for properties not previously
 name         found in the [MySection] section.

 Indirect     A literal name that references a section, which in turn references other sections. For
 reference    example, if the DefaultGateway property is included in the Priority property, MDT
              would search for the [DefaultGateway] section. If the [DefaultGateway] section
              references other sections (based on the IP address of the default gateway), this is an
              example of an indirect reference. For an example of indirect reference using the
              DefaultGateway property, see "Example: Computer Groupings Selected by
              Woodgrove Bank" in Select the Method for Grouping Computers.

<!-- p.390 -->

Properties Reserved Property

The Properties reserved property (shown in Listing 1) defines any custom, user-defined
properties to be used in the deployment. These user-defined properties are located by
ZTIGather.wsf script in the CustomSettings.ini file (or configuration database). These
properties are in addition to the predefined properties in MDT.

In Listing 1, CustomProperty is a user-defined property, and ScanStateArgs is a
predefined property. For a list of the predefined properties in MDT, see the section,
"Properties", in the MDT document Toolkit Reference.

You can also define custom properties to which you can assign multiple values by
adding numerical suffixes, such as ListProperty001, ListProperty002, and so on. You
create these types of custom properties by adding " (*) " to the end of the property
name. For example, ListProperty(*) defines the custom property as a list of property
values instead of a single-valued property. Consider the following excerpt from a
CustomSettings.ini file in which ListProperty(*) is defined:

  ini

  [Settings]
  Priority=Default
  Property=CustomProperty, ListProperty(*)

  [Default]
  CustomProperty=TRUE
  ListProperty001=New York City
  ListProperty002=Chicago

Values in the CustomSettings.ini File

Values are the configuration settings assigned to the properties. Values are preceded by
an equal sign (=). The scripts scan the CustomSettings.ini file to locate the values. In
Listing 1, the value assigned to the LoadStateArgs property is:

  ini

  /v:5 /c /lac

  ７ Note

  the CustomSettings.ini file is different from traditional INI files in that you do not
  place quotation marks around values, even if the value contains spaces.

<!-- p.391 -->

Subsections in the CustomSettings.ini File
You can create subsections in the Customsettings.ini file based on the value of a
property using the Subsection directive. The value of the Subsection directive can be
used to dynamically reference subsections that can be used to group configuration
settings.

Listing 2 illustrates an excerpt of a CustomSettings.ini file that uses the Subsection
directive to dynamically reference subsections based on the computer model, which is
specified in the Model property.

Listing 2. Using the Subsection Directive to Dynamically Reference Subsections in the
CustomSettings.ini File

  ini

  [Settings]
  Priority=Make, Default

  [Default]

  [Contoso Computer Corporation]
  Subsection=Contoso-%Model%

  [Contoso-MDT 6600]
  Packages001=XXX00009:Program9
  Packages002=XXX0000A:Program10

  [Contoso-MDT 2431]
  Packages001=XXX00003:Program2
  Packages002=XXX00003:Program4

In Listing 2, the Priority line contains the Make property, which is used to references
subsections based on the value of the Make property. The "Contoso Computer
Corporation" subsection is referenced when the value of the Make property is equal to
"Contoso Computer Corporation".

The "Contoso Computer Corporation" subsection contains a Subsection line that
references other subsections based on the value of the Model property. In this example,
the "Contoso-MDT 6600" and "Contoso-MDT 2431" sections will be processed by MDT
depending on the value of the Model property.

User Exit Scripts in the CustomSettings.ini File

<!-- p.392 -->

A user exit script is effectively a function library that can be called during the processing
of the CustomSettings.ini file using the UserExit directive. A user exit script contains one
or more functions that can be called during the process of the CustomSettings.ini file.

A user exit script is called by specifying the UserExit directive and assigning the property
name of the script to be called—for example, UserExit=TrimAssetTag.vbs. A function
within the user exit script is called by specifying the name of a function enclosed in the
# characters. For example, if the user exit script contains a function called
TrimAssetTag(), it would be called by specifying #TrimAssetTag()#.

Parameters can be passed to the function in the user exit script in the usual way by
specifying the parameter while calling the function. For example, to pass the variable
%ASSETTAG% to the function TrimAssetTag(), the function would be called by
specifying #TrimAssetTag("%ASSETTAG%")#.

The value returned by the function can be assigned to a variable by assigning the
function to that variable. For example, to take the asset tag of a computer and trim it
using the function TrimAssetTag(), and to then reassign the trimmed asset tag to the
variable AssetTag, the CustomSettings.ini file would read
AssetTag=#TrimAssetTag("%ASSETTAG%")#.

An example of how this could be used is to determine the task sequence to be run
based on a rule that sets the TaskSequenceID property. Listing 3 is an example user exit
script that determines the task sequence to be run based on the amount of available
RAM. This script also uses the ZTIUtility logging class.

Listing 3. Example User Exit Script

  VB

  Function UserExit(sType, sWhen, sDetail, bSkip)
    UserExit = Success
  End Function

  Function SetTaskSequence(vMemory)

       oLogging.CreateEntry "UserExit - Determining Task " & _
         "Sequence to run based on available RAM", LogTypeInfo

       If vMemory <= 2048 Then
         SetTaskSequence = "Win7_X86"
         oLogging.CreateEntry "UserExit - Available RAM: " & _
           vMemory & ". Selecting Win7_X86 TS.", LogTypeInfo
       Else
         SetTaskSequence = "Win8_X86"
         oLogging.CreateEntry "UserExit - Available RAM: " & _
           vMemory & ". Selecting Win8_X86 TS.", LogTypeInfo
       End If

<!-- p.393 -->

  End Function

The user exit script should be placed in the Scripts folder on the deployment share (for
example, D:\Production Deployment Share\Scripts).

To create the user exit script

   1. Create and test the custom script to be used.

   2. Locate the MDT Scripts folder (for example, D:\Production Deployment
     Share\Scripts).

   3. Copy the custom script to the Scripts folder.

     With the user exit script added to the deployment share (in this case, Z-
     RAMTest.wsf), it must then be referenced in the CustomSettings.ini file for the
     deployment share so it is called during deployment.

To call the user exit script from CustomSettings.ini

   1. Select Start, and then point to All Programs. Point to Microsoft Deployment
     Toolkit, and then select Deployment Workbench.

   2. In the Deployment Workbench console tree, go to Deployment
     Workbench/Deployment Shares/deployment_share (where deployment_share is the
     name of the deployment share to configure).

   3. In the Actions pane, select Properties.

   4. Select the Rules tab to display the CustomSettings.ini file.

   5. Add sections to UserExit.vbs to call the required functionality using the principles
     described in the previous section. An example CustomSetting.ini file is shown in
     Listing 4.

   6. Select OK to submit the changes.

   7. In the details pane, select deployment_share (where deployment_share is the name
     of the deployment share to configure).

   8. In the Actions pane, select Update Deployment Share.

     The Update Deployment Share Wizard starts.

<!-- p.394 -->

   9. On the Options page, select Optimize the boot image updating process, and then
        select Next.

 10. On the Summary page, verify the details are correct, and then select Next.

 11. On the Confirmation page, select Finish.

        Another common use for the user exit script is to dynamically set the computer
        name from known MDT properties such as SerialNumber, Model, or Product.

        Listing 4. Example CustomSettings.ini for Calling the User Exit Script

  ini

  [Settings]
  Priority=Default

  [Default]
  OSInstall=Y
  TaskSequenceID=#SetTaskSequence("%MEMORY%")#
  UserExit=Z-RAMTest.vbs

  UserDataLocation=NONE
  SkipCapture=YES
  SkipAdminPassword=NO
  SkipProductKey=YES

Basic CustomSettings.ini File for LTI Deployments
For LTI deployments, the Deployment Workbench uses a template version of the
CustomSettings.ini file (stored in installation_folder\Templates, where installation_folder
is the folder in which MDT is installed) as a basis for a customized version of
CustomSettings.ini. The template version of the CustomSettings.ini file is illustrated in
Listing 5. The template version in Listing 5 does not contain sufficient settings to
successfully deploy Windows to a target computer. However, the file will be further
customized using the Deployment Workbench.

Listing 5. Unmodified CustomSettings.ini File in the Templates Folder

  ini

  [Settings]
  Priority=Default
  Properties=MyCustomProperty

  [Default]

<!-- p.395 -->

  OSInstall=Y
  ScanStateArgs=/v:5 /o /c
  LoadStateArgs=/v:5 /c /lac

The New Deployment Share Wizard in the Deployment Workbench modifies this
template of the CustomSettings.ini file based on the responses provided. Listing 6 shows
the customized version of the CustomSettings.ini file after completing the New
Deployment Share Wizard.

Listing 6. Customized CustomSettings.ini File Modified by the Deployment
Workbench

  ini

  [Settings]
  Priority=Default
  Properties=MyCustomProperty

  [Default]
  OSInstall=Y
  ScanStateArgs=/v:5 /o /c
  LoadStateArgs=/v:5 /c /lac
  UserDataLocation=NONE
  SkipCapture=NO
  SkipAdminPassword=YES
  SkipProductKey=YES

The CustomSettings.ini file in Listing 6 contains the property values for all the target
computers to be migrated using this version of the file. This version of the file contains
no values unique to a specific target computer. For LTI, the target computer-specific
configuration values are manually provided during the installation process.

Table 153 explains the properties and corresponding values used in Listing 6.

Table 153. Explanation of CustomSettings.ini Properties in
Listing 6

                                                                                 ﾉ   Expand table

 Line in CustomSettings.ini   Purpose

 [Settings]                   Indicates the start of the [Settings] section.

 Priority=Default             Establishes the sequence in which the process parses subsections
                              to locate values for the variables. In this example, the [Default]
                              section is the only subsection that is parsed for variables.

<!-- p.396 -->

 Line in CustomSettings.ini    Purpose

 Properties=MyCustomProperty   Indicates any additional properties to locate. The properties listed
                               here are in addition to the properties listed in ZTIGather.xml.
                               ZTIGather.wsf parses ZTIGather.xml to obtain a list of the
                               properties.

 [Default]                     Indicates the start of the [Default] section.

 OSInstall=Y                   Indicates that the computer is supposed to perform an operating
                               system deployment.

 ScanStateArgs=/v:5 /o /c      Parameters passed to the Scanstate.exe tool in the USMT. These
                               parameters are passed to Scanstate.exe during state capture.

 LoadStateArgs=/v:5 /c /lac    Parameters passed to the Loadstate.exe tool in the USMT. These
                               parameters are passed to Loadstate.exe during state restore.

 UserDataLocation=NONE         Indicates where the user state migration data should be saved.
                               The value NONE indicates that the user state migration data should
                               not be saved. Indicates where the user state migration data
                               should be saved. The value NONE indicates that the user state
                               migration data should not be saved.

 SkipCapture=YES               Indicates whether the Specify whether to prompt for image
                               capture page in the Deployment Wizard is displayed. If the
                               property is set to YES, the wizard page is skipped and not
                               displayed. Indicates whether the Specify whether to prompt for
                               image capture page in the Deployment Wizard is displayed. If the
                               property is set to YES, the wizard page is skipped and not
                               displayed.

 SkipAdminPassword=YES         Indicates whether the Allow user to set Administrator Password
                               page in the Deployment Wizard is displayed. If the property is set
                               to YES, the wizard page is skipped and not displayed.

 SkipProductKey=YES            Indicates whether the Allow user to specify a product key page
                               in the Deployment Wizard is displayed. If the property is set to
                               YES, the wizard page is skipped and not displayed.

For more information on the individual properties, see the corresponding reference
section in the MDT document Toolkit Reference.

Basic CustomSettings.ini File for ZTI Deployments Using
Configuration Manger

For ZTI deployments using Configuration Manager, the Deployment Workbench uses a
template version of the CustomSettings.ini file (stored in installation_folder\Templates,

<!-- p.397 -->

where installation_folder is the folder in which MDT is installed) as a basis for a
customized version of CustomSettings.ini. The template version of the
CustomSettings.ini file is illustrated in Listing 7. The template version in Listing 7 does
not contain sufficient settings to successfully deploy Windows to a target computer.
However, the file will be further customized using the Deployment Workbench.

Listing 7. Unmodified CustomSettings.ini File in the Templates Folder

  ini

  [Settings]
  Priority=Default
  Properties=MyCustomProperty

  [Default]
  OSInstall=Y
  ScanStateArgs=/v:5 /o /c
  LoadStateArgs=/v:5 /c /lac

The New Deployment Share Wizard in the Deployment Workbench modifies this
template version of the CustomSettings.ini file based on the responses provided. Listing
8 shows the customized version of the CustomSettings.ini file after completing the New
Deployment Share Wizard.

Listing 8. Customized CustomSettings.ini File Modified by the Deployment
Workbench

  ini

  [Settings]
  Priority=Default
  Properties=MyCustomProperty

  [Default]
  OSInstall=Y
  ScanStateArgs=/v:5 /o /c
  LoadStateArgs=/v:5 /c /lac
  UserDataLocation=NONE

The CustomSettings.ini file shown in Listing 8 contains the property values for all of the
target computers to be deployed using this version of the file. This version of the file
contains no values that are unique to a specific target computer.

For ZTI using Configuration Manager, the Create MDT Task Sequence Wizard copies an
unmodified version of the CustomSettings.ini template with no modifications to the file.
Modify the version of the template in the package source folder that you specified in

<!-- p.398 -->

Package source to be created on the MDT Package wizard page in the Create MDT Task
Sequence Wizard as described in Create ZTI Task Sequences Using the Create MDT Task
Sequence Wizard in Configuration Manager.

Modify this version of the CustomSettings.ini file to include the target computer-specific
configuration values. After modifying the file, update the distribution points for the
Microsoft Deployment Files package so that the changes are available to the task
sequences. Listing 9 shows a modified version of the CustomSettings.ini file, which
includes target computer-specific settings.

Listing 9. Customized CustomSettings.ini File with Target Computer Settings

  ini

  [Settings]
  Priority=Default, MACAddress
  Properties=MyCustomProperty

  [Default]
  OSInstall=Y
  ScanStateArgs=/v:5 /o /c
  LoadStateArgs=/v:5 /c /lac
  UserDataLocation=NONE

  [00:0F:20:35:DE:AC]
  MyCustomProperty=TRUE

  [00:03:FF:FE:FF:FF]
  MyCustomProperty=FALSE

Table 154 explains the properties and corresponding values used in Listing 9.

Table 154. Explanation of CustomSettings.ini Properties in
Listing 9

                                                                               ﾉ   Expand table

 Line in CustomSettings.ini   Purpose

 [Settings] [Settings]        Indicates the start of the [Settings] section.

 Priority=Default,            Establishes the sequence in which the process parses subsections
 MACAddress                   to locate values for the variables. In this example, the [Default]
                              section is parsed first, and then the section that corresponds to
                              the MAC address of the target computer ( MACAddress ) is parsed.
                              The sections for the target computers ( [00:0F:20:35:DE:AC] and
                              [00:03:FF:FE:FF:FF] ) contain computer-specific settings.

<!-- p.399 -->

 Line in CustomSettings.ini    Purpose

                               Establishes the sequence in which the process parses subsections
                               to locate values for the variables. In this example, the [Default]
                               section is parsed first, and then the section that corresponds to
                               the MAC address of the target computer ( MACAddress ) is parsed.
                               The sections for the target computers ( [00:0F:20:35:DE:AC] and
                               [00:03:FF:FE:FF:FF] ) contain computer-specific settings.

 Properties=MyCustomProperty   Indicates any additional properties to locate. The properties listed
                               here are in addition to the properties listed in ZTIGather.xml.
                               ZTIGather.wsf parses ZTIGather.xml to obtain a list of the
                               properties.

 [Default]                     Indicates the start of the [Default] section.

 OSInstall=Y                   Indicates whether the target computer is authorized to have the
                               operating system installed.

 ScanStateArgs=/v:5 /o /c      Parameters passed to the Scanstate.exe tool in the USMT. These
                               parameters are passed to Scanstate.exe during the State Capture
                               Phase.

 LoadStateArgs=/v:5 /c /lac    Parameters passed to the Loadstate.exe tool in the USMT. These
                               parameters are passed to Loadstate.exe during state restore.

 UserDataLocation=NONE         Indicates where the user state migration data should be saved.
                               The value NONE indicates that the user state migration data should
                               not be saved.

 [00:0F:20:35:DE:AC]           Section that contains all the properties and settings specific to the
                               target computer with the matching MAC address. In this sample,
                               the target computer has a MAC address of [00:0F:20:35:DE:AC] .

 [00:03:FF:FE:FF:FF]           Section that contains all the properties and settings specific to the
                               target computer with the matching MAC address. In this sample,
                               the target computer has a MAC address of [00:03:FF:FE:FF:FF] .

For more information on the individual properties, see the corresponding reference
section in the MDT document Toolkit Reference.

Identify the BootStrap.ini File Syntax
In LTI deployments, use the BootStrap.ini file to specify property settings before
accessing the CustomSettings.ini file. Use the BootStrap.ini file to provide distribution
point information, logon credentials, and Windows PE keyboard locale settings. The
properties configured in BootStrap.ini help the MDT scripts locate the appropriate MDT
distribution share.

<!-- p.400 -->

The syntax of the BootStrap.ini file is identical to the CustomSettings.ini file. The
BootStrap.ini file contains a subset of the properties used in CustomSettings.ini as
follows:

        DeployRoot

           ７ Note

           Ensure that the DeployRoot property is specified in the BootStrap.ini file, as
           the LTI deployment process will not be able to locate the CustomSettings.ini
           file in the deployment share. If not configured correctly, errors and warnings
           are displayed when running the Deployment Wizard.

        SkipBDDWelcome

        UserDomain

        UserID

        UserPassword

        KeyboardLocale

        For more information about each of these properties, see the corresponding
        section in the MDT document Toolkit Reference.

        The Deployment Workbench creates the BootStrap.ini file when you create a
        deployment share. After the initial creation, make all further customizations
        manually.

        Listing 10 shows the BootStrap.ini file that the Deployment Workbench creates
        automatically for a deployment share. You may need to customize the
        BootStrap.ini file in Listing 10.

        Listing 10. BootStrap.ini File As Created by the Deployment Workbench for
        Deployment Shares

  ini

  [Settings]
  Priority=Default

  [Default]
  DeployRoot=\\NYC-MDT-01\Distribution$
