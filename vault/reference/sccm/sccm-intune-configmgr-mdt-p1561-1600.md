---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1561-1600"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1561-1600
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1561-1600
family: sccm
documentKind: "doc"
abstract: "Postinstall (Figure 22) State Restore (Figure 23 and Figure 24) Capture (Figure 25) Figure 17. Flow chart for the Initialization Phase Figure 18. Flow chart for the Validation Phase Figure 19. Flow chart for the State Capture Phase Figure 20. Flow chart for the Preinstall Phase"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1561-1600

<!-- p.1561 -->

Postinstall (Figure 22)

State Restore (Figure 23 and Figure 24)

Capture (Figure 25)

Figure 17. Flow chart for the Initialization Phase

<!-- p.1562 -->

Figure 18. Flow chart for the Validation Phase

Figure 19. Flow chart for the State Capture Phase

<!-- p.1563 -->

Figure 20. Flow chart for the Preinstall Phase

<!-- p.1564 -->

Figure 21. Flow chart for the Install Phase

<!-- p.1565 -->

Figure 22. Flow chart for the Postinstall Phase

<!-- p.1566 -->

Figure 23. Flow chart for the State Restore Phase (1 of 2)

<!-- p.1567 -->

Figure 24. Flow chart for the State Restore Phase (2 of 2)

<!-- p.1568 -->

Figure 25. Flow chart for the Capture Phase

<!-- p.1569 -->

Microsoft Support
Microsoft provides Premier and Professional level support for Microsoft Deployment Toolkit.

     Professional level support

     Premier level support

  ７ Note

<!-- p.1570 -->

 When contacting support, be clear that the issue is with MDT and the specific version.

Last updated on 03/30/2025

<!-- p.1571 -->

User Driven Installation - Developers
Guide
Article • 10/04/2022

User Driven Installation (UDI) helps simplify the deployment of Windows® client
operating systems, such as Windows 8.1, to computers using the operating system
deployment (OSD) feature in Microsoft® System Center 2012 R2 Configuration
Manager. UDI is part of the Microsoft Deployment Toolkit (MDT).

Introduction
Typically, when deploying operating systems using the OSD feature, you must provide
all the necessary information for deploying the operating system. The information is
configured in configuration files or in databases (such as the CustomSettings.ini file or
the MDT database [MDT DB]). You must provide all configuration settings before you
can initiate the deployment.

UDI provides a wizard-driven interface that allows you to provide configuration
information immediately prior to performing the deployment. This behavior allows you
to create generic OSD task sequences, and then provide computer-specific information
at the time of deployment, which provides greater flexibility in the deployment process.

Target Audience
This guide is written for the developers who create custom wizard pages for the UDI
Wizard and custom wizard page editors for the UDI Wizard Designer. This guide
assumes that you are familiar with the development of Windows applications using:

      C++, which is used to create custom wizard pages

      Microsoft .NET Framework, which is used to create custom wizard page editors

      Windows Presentation Foundation (WPF), which is used to create custom wizard
      page editors

      Languages that WPF supports, such as C#, C++, or Microsoft Visual Basic® .NET,
      which are used to create custom wizard page editors

About This Guide

<!-- p.1572 -->

This guide provides the necessary reference information to help you customize UTI for
your organization. This guide does not discuss administrative or operational topics, such
as installing MDT (which includes UDI), configuring UDI to deploy operating systems and
applications, or performing deployments using the UDI Wizard. For more information on
those topics, see the UDI topics in Using the Microsoft Deployment Toolkit, which is
included with MDT.

UDI Development Overview
UDI development allows you extend the features that UDI provides. Typically, UDI
development is required when you want to collect additional information that the UDI
deployment process consumes. This additional information is usually saved as task
sequence variables that task sequence steps in a UDI task sequence in Configuration
Manager read.

UDI Architecture
The high-level goal of UDI development is to create custom wizard pages that can be
displayed in the UDI Wizard. By creating custom wizard pages, you can extend the
existing features of UDI to meet the business and technical requirements of your
organization. A custom wizard page collects information in addition to or in place of the
wizard pages that UDI provides.

Figure 1 illustrates the relationship between the UDI Wizard Designer and the UDI
Wizard.

<!-- p.1573 -->

Figure 1. Relationship between the UDI Wizard and UDI Wizard Designer

Figure 1. Relationship between the UDI Wizard and UDI Wizard Designer

At a conceptual level, UDI development includes the creation of:

     Custom wizard pages. Wizard pages are displayed in the UDI Wizard and collect
     the information required to complete the deployment process. You create wizard
     pages using C++ in Microsoft Visual Studio®. The custom wizard pages are
     implemented as DLLs that the UDI Wizard reads. The UDI software development kit
     (SDK) includes an example of how to create custom wizard pages.

     Custom wizard page editors. You use wizard page editors to configure the
     behavior of your custom wizard page. The custom wizard page editors are
     implemented as DLLs that the UDI Wizard Designer reads. You create wizard page
     editors using:

        WPF version 4.0

        Microsoft Prism   version 4.0

        Microsoft Unity Application Block   (Unity) version 2.1

<!-- p.1574 -->

         MDT includes all the assemblies necessary to create a custom wizard page
         editor for use in the UDI Wizard Designer. The UDI SDK includes an example of
         how to create custom wizard page editors.

     In addition, the UDI Wizard Designer consumes supporting wizard page editor
     configuration files. You create the wizard page editor configuration files as a part
     of the process for creating your custom wizard pages and custom wizard page
     editors. The UDI Wizard Designer creates the necessary XML information in the
     UDI Wizard configuration file and corresponding .app file.

Preparing the UDI Development Environment
Before you begin creating your own custom wizard pages and wizard page editors,
perform the following steps to prepare the UDI development environment:

   1. Prepare the UDI development environment prerequisites as described in Prepare
     the UDI Development Environment Prerequisites.

   2. Configure the UDI development environment as described in Configure the UDI
     Development Environment.

   3. Verify that the UDI development environment is configured correctly as described
     in Verify the UDI Development Environment.

Prepare the UDI Development Environment Prerequisites

To prepare the UDI development environment prerequisites, perform the following
steps:

   1. Prepare the UDI development environment hardware perquisites as described in
     Prepare the UDI Development Environment Hardware Prerequisites.

   2. Prepare the UDI Development environment software perquisites as described in
     Prepare the UDI Development Environment Software Prerequisites.

Prepare the UDI Development Environment Hardware
Prerequisites

The UDI development environment hardware prerequisites are the same hardware
requirements for the edition of Microsoft Visual Studio you are using. For more
information about these requirements, see the system requirements for each edition in
the Visual Studio Documentation.

<!-- p.1575 -->

Prepare the UDI Development Environment Software Prerequisites

The UDI development environment has the following software prerequisites:

     Any Windows operating system that Visual Studio 2010 supports (Windows 7 or
     Windows Server® 2008 R2 is recommended.)

     You will need a Windows operating system that supports the processor
     architecture for which you want to develop. You can perform 32-bit and 64-bit UDI
     development using a 64-bit operating system. You only do 32-bit UDI
     development on 32-bit operating systems. For this reason, you should use a 64-bit
     operating system.

       ７ Note

       IntelItanium versions (IA-64) of Windows operating system are not supported
       for UDI development environments.

     For more information about the operating systems that Visual Studio 2010
     supports, see the system requirements for each edition in the Visual Studio
     Documentation.

     Microsoft .NET Framework version 4.0 (required by Visual Studio 2010)

     C++ language (the language used in extending UDI Wizard pages)

     Other languages that WPF supports, such as C#, Visual Basic .NET, or
     C++/Common Language Infrastructure, which are used to extend UDI Wizard
     Designer wizard page editors

       ７ Note

       The sample source code for the UDI Wizard Designer wizard page editors is
       written in C#. Install the C# language if you want to use the sample source
       code.

Configure the UDI Development Environment
After then UDI development environment prerequisites are met, perform the following
steps to configure the UDI development environment:

  1. Install Visual Studio 2010.

<!-- p.1576 -->

  Ensure that you install the C++ language and any other language that WPF
  supports.

     ７ Note

     The sample source code for the UDI Wizard Designer editor pages is written
     in C#. Install the C# language if you want to use the sample source code.

  For more information about installing Visual Studio 2010, see Installing Visual
  Studio.

2. Install MDT.

  For more information about how to install MDT, see the section, "Installing or
  Upgrading to MDT", in the MDT document Using the Microsoft Deployment Toolkit.

3. In Windows Explorer, create local_folder (where local_folder is any folder located on
  a local drive on the development computer).

4. Copy the installation_folder\SDK folder to local_folder (where installation_folder is
  the folder in which you installed MDT and local_folder is any folder located on a
  local drive on the development computer).

  You copy the SDK folder to another location because MDT is installed in the
  Program Files folder, which cannot be written to without elevated permissions.
  Copying the SDK folder to another location allows you to modify the files in the
  SDK folder without requiring elevated permissions.

5. Copy the installation_folder\Templates\Distribution\Tools folder to local_folder
  (where installation_folder is the folder in which you installed MDT and local_folder
  is the folder you created earlier in the process).

6. Rename the local_folder\Tools folder to local_folder\OSDSetupWizard(where
  local_folder is the folder you created earlier in the process).

  When completed, the folder structure beneath local_folder should look like the
  folder structure illustrated in Figure 2 (where local_folder is the folder you created
  earlier in the process and is shown as UDIDevelopment in the figure).

<!-- p.1577 -->

                                                                Figure 2. Folder
     structure for UDI development

     Figure 2. Folder structure for UDI development

Verify the UDI Development Environment
When the UDI development environment is configured, verify that the UDI development
environment is configured correctly by ensuring that the sample projects build correctly
in Visual Studio 2010.

Verify that the UDI development environment is configured correctly by determining
whether:

<!-- p.1578 -->

     The SamplePage project builds correctly as described in Verify That the
     SamplePage Project Builds Correctly

     The SampleEditor project builds correctly as described in Verify That the
     SampleEditor Project Builds Correctly

Verify That the SamplePage Project Builds Correctly

The SamplePage project provides an example of how to create a custom wizard page for
the UDI Wizard. For more information about the SamplePage project, see Review the
SamplePage Visual Studio Solution.

To verify that the SamplePage project builds correctly

  1. Start Visual Studio 2010.

  2. Open the SamplePage project.

     The SamplePage project resides in the local_folder\SDK\UDI\SamplePage folder
     (where local_folder is the folder you created earlier in the process).

  3. In Visual Studio 2010, in Solution Explorer, right-click the SamplePage project, and
     then select Properties.

     The SamplePage Property Pages dialog box appears.

  4. In the SamplePage Property Pages dialog box, go to Configuration
     Properties/Debugging.

  5. In the Debugging properties, under Configuration, select All Configurations.

  6. In the Debugging properties, under Command, type
     $(TargetDir)\OSDSetupWizard.exe.

  7. In the Debugging properties, under Working Directory, type $(TargetDir).

  8. In the SamplePage Property Pages dialog box, go to Configuration
     Properties/Build Events/Post-Build Event.

  9. In the Post-Build Event properties, under Command Line, type the following:

       Windows Command Prompt

       copy /y "$(ProjectDir)..\..\..\..\OSDSetupWizard\x86\*.*"
       "$(TargetDir)"
       xcopy /y /i "$(ProjectDir)..\..\..\..\OSDSetupWizard\x86\en-us"
       "$(TargetDir)en-us"

<!-- p.1579 -->

        copy /y
        "$(ProjectDir)..\..\..\..\OSDSetupWizard\OSDResults\Images\UDI_Wizard_B
        anner.bmp" "$(ProjectDir)header.bmp"
        copy /y "$(ProjectDir)Config.xml" "$(TargetDir)"
        copy /y "$(ProjectDir)header.bmp" "$(TargetDir)header.bmp"

 10. In the SamplePage Property Pages dialog box, select OK.

 11. Save the project.

 12. From the Debug menu, select Start Debugging.

     The Microsoft Visual Studiodialog box appears indicating that the source is out of
     date and asks whether you want to build the project.

 13. In the Microsoft Visual Studio dialog box, select Yes.

     The No Debugging Information dialog box appears informing you that no
     debugging information is available for OSDSetupWizard.exe.

 14. In the No Debugging Information dialog box, select Yes.

     The UDI Wizard opens with the custom wizard page displayed.

 15. Verify that you can select a value in Choose your location.

 16. In the Wizard with sample page form, select Cancel.

     The Cancel Wizard dialog box appears.

 17. In the Cancel Wizard dialog box, select Yes.

 18. Close Visual Studio 2010.

Verify That the SampleEditor Project Builds Correctly

The SampleEditor project provides an example of how to create a custom wizard page
editor for the UDI Wizard Designer. For more information about the SampleEditor
project, see Review the SamplePage Visual Studio Solution.

To verify that the SampleEditor project builds correctly

   1. Start Visual Studio 2010.

   2. Open the SampleEditor project.

     The SampleEditor project resides in the local_folder\SDK\UDI\SampleEditor folder
     (where local_folder is the folder you created earlier in the process).

<!-- p.1580 -->

 3. In Visual Studio 2010, in Solution Explorer, select the SampleEditor project.

 4. From the Project menu, select Add Reference.

   The Add Reference dialog box opens.

 5. In the Add Reference dialog box, select the Browse tab.

 6. On the Browse tab, go to installation_folder\Bin (where installation_folder is the
   folder in which you installed MDT). Select the following files, and then select OK:

         Microsoft.Enterprise.UDIDesigner.Common.dll

         Microsoft.Enterprise.UDIDesigner.DataService.dll

         Microsoft.Enterprise.UDIDesigner.Infrastructure.dll

         Microsoft.Practices.Prism.dll

         Microsoft.Practices.ServiceLocation.dll

         Microsoft.Practices.Unity.dll

         RibbonControlsLibrary.dll

     ７ Note

     You can select multiple files on the Browse tab by holding down the CTRL key
     while you select the files.

 7. In Solution Explorer, go to SampleEditor/References.

 8. Verify that none of the references have any warnings or errors.

 9. In Solution Explorer, right-click the SampleEditor project, and then select
   Properties.

   The SampleEditor Property Pages dialog box appears.

10. In the SampleEditor Property Pages dialog box, select the Debug tab.

11. On the Debug tab, select Start external program.

12. In Start external program, type installation_folder\Bin\UDIDesigner.exe (where
   installation_folder is the folder in which you installed MDT), and then select OK.

<!-- p.1581 -->

       Tip

      You can select the ellipsis (...) button to browse to the folder and select
      UDIDesigner.exe.

13. From the File menu, select Save All.

14. Copy the local_folder\SDK\SamplePage\SamplePage.dll.config file to the
   installation_folder\Bin\Config folder (where local_folder is the folder you created on
   the development computer earlier in the configuration process
   andinstallation_folder is the folder in which you installed MDT).

15. In Visual Studio 2010, from the Debug menu, select Start Debugging.

   The UDI Wizard Designer starts.

16. In the UDI Wizard Designer, on the Ribbon, select Open.

   The Open dialog box appears.

17. In the Open dialog box, open the
   local_folder\SDK\SamplePage\SamplePage\Config.xml file (where local_folder is the
   folder you created on the development computer earlier in the configuration
   process).

   The Config.xml file opens, and the Custom StageGroup is displayed in the details
   pane.

18. In the details pane, select the Configure tab.

19. Review the configuration information for the Location box, including the following:

         Unlocked button, with which you enable or disable the Location box

         Default value box, in which you enter a default value to be displayed in the
         Location box

         Friendly display name visible in summary page, in which you enter the
         caption for the information displayed on the Summary page

         Location list box, which includes a list of possible locations

20. Close the UDI Wizard Designer.

21. Close Visual Studio 2010.

<!-- p.1582 -->

Reviewing the UDI SDK Examples
Before beginning development, review the examples provided in the UDI SDK. Use the
information in this guide and the source code in the examples to help you create your
own UDI custom wizard pages and wizard page editors.

Go through the UDI SDK examples by reviewing the:

        Contents of the SDK folder that you copied earlier in the installation process as
        described in Review the Contents of the SDK Folder

        Custom UDI wizard page example as described in Review the SamplePage Visual
        Studio Solution

        Custom UDI wizard page editor example as described in Review the SampleEditor
        Visual Studio Solution

Review the Contents of the SDK Folder
During configuration of the UDI development environment, you copied the SDK folder
from the folder in which you installed MDT to another folder that you created. Table 1
lists the folders immediately beneath the SDK folder and provides a brief description of
each.

Table 1. Folders in the UDI SDK

                                                                                       ﾉ    Expand table

 Folder           This folder contains

 Includes         The C++ header files necessary for creating custom wizard pages for the UDI
                  Wizard

 Libs             The C++ library files that will be linked to your custom page; there are 32-bit and
                  64-bit versions of the static link libraries. Note: Itanium versions of the libraries
                  (IA-64) are not available.

 SampleEditor     A Visual Studio project for building a custom editor used to edit the SamplePage
                  page in UDI Wizard Designer, which is written in C#

 SamplePage       A Visual Studio project for building a custom UDI wizard page, which is written in
                  Visual C++

Review the SamplePage Visual Studio Solution

<!-- p.1583 -->

Before you begin creating your custom wizard pages and wizard page editors, perform
the following tasks to prepare the UDI development environment:

     Review the stages in the life cycle of a UDI wizard page as described in Review the
     Wizard Page Life Cycle.

     Review the Visual Studio solution for the SamplePage example in the UDI SDK as
     described in Review the SamplePage Example.

Review the Wizard Page Life Cycle
A UDI wizard page has methods that correspond to each stage (or phase) of the life
cycle of the page. As a part of creating your custom wizard page, you need to override
these methods with your code. Table 2 lists the methods that you will need to override
and provides a brief description of each method, including when to use the method in
the wizard page life cycle.

Table 2. Methods in a Wizard Page Life Cycle

                                                                                     ﾉ   Expand table

 Method                       Description

 OnWindowCreated              This method is called once, after the page's window has been
                              created.

                              For this method, write code that initializes the page for the first time
                              and only needs to be performed once. For example, use this method
                              to initialize fields or to read configuration information from the Setter
                              elements in the UDI Wizard configuration file.

 OnWindowShown                This method is called each time the page is displayed (shown) in the
                              UDI Wizard. It is called the first time the page is displayed and each
                              time you navigate to the page by selecting Next or Back in the
                              wizard.

                              For this method, write code that prepares the page to be displayed—
                              for example, reading memory variables, task sequence variables, or
                              environment variables, and then updating the page based on any
                              changes to those variables.

 OnCommonControlEvent         This method can be called anytime the wizard page is displayed and
                              receives a WM_NOTIFY message from a child (typically, common
                              controls).

                              For this method, write code that handles WM_NOTIFY based on the

<!-- p.1584 -->

 Method                   Description

                          notification message. For example, you may want to respond to
                          events from a common control, such as responding to select or
                          double-click events for a TreeView control.

 OnUnhandledEvent         This method is called anytime an unhandled window message occurs
                          for your wizard page. This method provides the opportunity to
                          intercept and handle these otherwise unhandled window messages.

                          For this method, write code that handles the window messages that
                          are pertinent to your wizard page. Typically, you will not need to
                          override this method.

 OnNextSelected           This method is called when you select Next in the wizard.

                          For this method, write code that performs any necessary actions
                          before moving to the next wizard page—for example, performing
                          validation that can take a long time. If the validation fails, you can
                          cancel the Next request and display a message.

 OnWindowHidden           This method is called each time the page is hidden when either the
                          previous or next wizard page is shown.

                          For this method, write code that performs any actions before the
                          page is hidden, prior to another page being shown. Typically, you will
                          not need to override this method.

Review the SamplePage Example
Review the SamplePage example using the following list, which represents the sequence
of events during the wizard page life cycle of the SamplePage example:

   1. The UDI Wizard, OSDSetupWizard.exe, reads the configuration information from
     the UDI Wizard configuration file in the example (the Config.xml file) as described
     in Step 1: The UDI Wizard (OSDSetupWizard.exe) Reads the Config.xml File.

   2. The UDI Wizard loads the DLLs required for each wizard page listed in the UDI
     Wizard configuration file as described in Step 2: The UDI Wizard Loads the DLL for
     the Custom Wizard Page.

   3. The UDI Wizard displays the custom wizard page and allows for the desired control
     interaction as described in Step 3: The UDI Wizard Displays the Custom Wizard
     Page.

   4. When the custom wizard page has collected the information, perform any tasks
     necessary before selecting Next to proceed to the next wizard as described in Step

<!-- p.1585 -->

     4: The Next Button Is Selected in the Custom Wizard Page.

Step 1: The UDI Wizard (OSDSetupWizard.exe) Reads the
Config.xml File

When the UDI Wizard (OSDSetupWizard.exe) starts, by default it reads the UDI Wizard
configuration file, which is the UDIWizard_Config.xml file—the primary configuration file
for the UDI Wizard.

  ７ Note

  The example uses the Config.xml file as the configuration file. In MDT, the default
  configuration file is the UDIWizard_Config.xml file, which resides in the Scripts
  folder in the MDT Files package for configuration.

You can override the default configuration file that the UDI Wizard uses by modifying
the UDI Wizard task sequence step to use the /definition parameter. For more
information about overriding the default configuration file that the UDI Wizard uses, see
"Override the Configuration File That the UDI Wizard Uses".

The top-level elements in the Config.xml file are the

     DLLs element

     Style element

     Pages element

     StageGroups element

     For more information about the schema of the UDI Wizard configuration file and
     each of these elements, see UDI Wizard Configuration File Schema Reference.

     The UDI Wizard scans the DLLs element looking for the .dll files to load. In the
     example, two .dll files are listed: SamplePage.dll and SharedPages.dll. These .dll
     files must reside in the same folder as OSDSetupWizard.exe—the Tools\platform
     folder (where platform is x86 for the 32-bit version or x64 for the 64-bit version).

     The UDI Wizard scans the Pages element looking for the pages that are defined. In
     the example, two pages are defined: Custom and SummaryPage. The Type
     attribute of the Page element is defined in the PageClassIDs.h file and uniquely
     defines the type of your custom page.

<!-- p.1586 -->

     In the example, the defined type is Microsoft.SamplePage.LocationPage. For your
     custom page, substitute the following to avoid any potential conflicts with other
     pages you may create in the future:

     Your organization name in the place of Microsoft.

     Your project name in the place of SamplePage.

     Your custom wizard page name in the place of LocationPage.

Step 2: The UDI Wizard Loads the DLL for the Custom Wizard Page

When the UDI Wizard loads your DLL, it calls the RegisterFactories function, which must
be implemented in your .dll file. In the example, this function is implemented in the
dllmain.ccp file. Each wizard page you create must implement the RegisterFactories
function.

The RegisterFactories function is used to register the factory class of your wizard page
with the class factory registry for the UDI Wizard. Class factories are classes that can
create an instance of another class. The RegisterFactories function creates a new
instance of a factory class and passes that class to the class factory registry for the UDI
Wizard, which makes that factory class available to the wizard. The UDI Wizard looks for
a factory class registered with an ID that matches the Type attribute of the Page element
for the custom wizard page.

In the example, the ID is defined as ID_Location in the PageClassIds.h file as
Microsoft.SamplePage.LocationPage, which matches the Type attribute for the Page
element in the Config.xml file. ID_Location is passed as a parameter in the
RegisterFactories function implemented in the dllmain.ccp file.

You can create a function using the Register_name function template to simplify the
creation of a new factory instance and register the newly created instance. The name
value provided using the Register function template must implement the iClassFactory
interface. The ClassFactoryImpl Class handles most of the details for implementing a
class factory.

You can also use the RegisterFactories function to register task types and validator
types. For more information, see the following:

     Creating Custom UDI Tasks

     Creating Custom UDI Validators

  ７ Note

<!-- p.1587 -->

  The example contains and registers only the one custom wizard page. The example
  does not include custom tasks or validators and so does not register any custom
  tasks or validators.

Step 3: The UDI Wizard Displays the Custom Wizard Page

The custom wizard page in the example is defined in the LocationPage.cpp file. Wizard
pages are derived from template classes that provide much of the functionality a page
has. All wizard pages should derive from the WizardPageImpl Template Class, which
implements the IWizardPage Interface. Each wizard page can implement other optional
template classes and corresponding interfaces based on the needs of the page.

The WizardPageImpl Template Class has several useful interfaces that can help you write
custom wizard pages. Implement the WizardPageImpl Template Class as the base class
for your custom wizard page.

For a list of the available:

      Template classes for wizard pages, see Wizard Page Helper Classes

      Interfaces for the wizard page template classes, see Wizard Page Interfaces

      The custom wizard page in the example is derived from the WizardPageImpl
      Template Class and implements the IWizardPage Interface. In addition, the custom
      wizard page implements the IFieldCallback interface. Both of these are
      implemented in the LocationPage.cpp file.

      The example custom wizard page overrides the following methods:

      OnWindowCreated. The OnWindowCreated method in the example wizard page
      calls the following methods:

         AddField. This method relates the IDC_COMBO_LOCATION box control in the
         IDD_LOCATION_PAGE resource with the Data element named Location in the
         Config.xml file.

         In addition to the AddField method, you could use the AddRadioGroup and
         AddToGroup methods to support other controls and behaviors.

            ７ Note

            Ensure that you call the AddField, AddRadioGroup, or AddToGroup
            method prior to calling the InitFields method.

<!-- p.1588 -->

        InitFields. Use this method to initialize the fields (controls) that you have added
        to the form. The pointer of the page is a parameter. In the example, the this
        pointer is passed, which refers to the current page.

          ７ Note

          To support the use of the this pointer, you must implement the
          IFieldCallback interface in addition to the interfaces that the
          WizardPageImpl Template Class supports.

        The IFieldCallback interface calls the SetFieldDefault method, which is used to
        set the default values for controls other than text box and check box controls. In
        the example, the SetFieldDefault method sets the initial index of the combo
        box control based on the default value specified in the Default element for the
        Field element in the Config.xml file.

        The OnWindowCreated method sets up the form controller using the
        IFormController interface. For more information about setting up the form
        controller, see Setting up the Form.

     InitLocations. This method populates the combo box from the list of locations in
     the Config.xml file. The Data element and child DataItem elements the Confg.xml
     file provide the list of possible values.

     OnNextSelected. This method performs the following tasks:

        Updates the TSLocation task sequence variable with the value selected in the
        combo box using the SaveFields method

        Adds information that will be shown on the Summary page using the
        SaveFields method

Step 4: The Next Button Is Selected in the Custom Wizard Page

When the user completes the fields on the custom wizard page, they select Next, which
calls the OnNextSelected method. The OnNextSelected method performs any necessary
tasks before proceeding to the next wizard page, such as recording any configuration
changes made on the custom wizard page.

For the example custom wizard page, the override for the OnNextSelected method is
implemented in the LocationPage.ccp file. In the OnNextSelected method in the
example custom wizard page, the following methods are called:

<!-- p.1589 -->

   1. InitSection. This method initializes the header (label caption) for the summary data
     displayed on the Summary page. Typically, you can set this value using the
     DisplayName() function. The data associated with this caption is saved using the
     SaveFields method.

   2. SaveFields. This method saves field values to task sequence variables and to the
     data displayed on the Summary page.

Review the SampleEditor Visual Studio Solution
Before you begin creating your own custom wizard pages and wizard page editors,
perform the following steps to prepare the UDI development environment:

     Review the architecture of the UDI Wizard Designer as described in Review the UDI
     Wizard Designer Architecture.

     Review the components of a UDI Wizard page that can be customized using the
     UDI Wizard configuration file as described in Review Configurable Components of
     a UDI Wizard Page.

     Review the EditorPage example provided in the UDI SDK as described in Review
     the EditorPage Example.

Review the UDI Wizard Designer Architecture
The UDI Wizard Designer was developed using WPF, Prism, and Unity. The UDI Designer
is used to edit the UDI Wizard configuration file (UDIWizard_Config.xml), which the UDI
Wizard (OSDSetupWizard.exe) reads at runtime. The Pages element in the UDI Wizard
configuration file contains a list of pages that has a separate Page element for each
wizard page.

When you edit the configuration settings for a wizard page, the UDI Wizard Designer
loads the custom page editor that corresponds to the wizard page type. The custom
wizard page editors are developed as WPF user controls. The custom wizard page editor
pages use the Model-View-ViewModel (MVVM) design pattern for WPF.

The MVVM design pattern helps separate the user interface (UI; presentation) from the
data being presented. The data is a façade over the Page element in the UDI Wizard
configuration file (the Config.xml file in the example), which is accessed using the
CurrentPage property of the IDataService interface.

The UDI Wizard Designer uses the DependencyAttribute to obtain access to the
DataService class based on the dependency injection framework in Unity. For more

<!-- p.1590 -->

information about the dependency interjection framework in Unity, see Inject Some Life
into Your Applications—Getting to Know the Unity Application Block.

Review Configurable Components of a UDI Wizard Page

As you create your custom wizard page, some of the configuration settings may be set
in code and cannot be changed after you have compiled the page. However, for other
configuration settings, you will need to allow those configuration settings to be
changed using the UDI Wizard Designer.

Typically, the configuration settings that you want to configure using the UDI Wizard
Designer are saved in the UDI Wizard configuration file (the Config.xml file in the
example). However, you can also create your own separate configuration file, if
necessary. One example of using a separate configuration file is the
UDIWizard_Config.xml.app file, which the Application Discovery task and the
ApplicationPage wizard page type use.

The following is a list of the typical configuration settings that you can manage using
the UDI Wizard Designer:

     Field. Use fields allow users to provide input. Fields appear as Field elements in the
     UDI Wizard configuration file (UDIWizard_Config.xml), which contains the
     configuration settings for each field. The corresponding wizard page editor needs
     to provide a method for editing the field configuration settings for the field using
     the FieldElementControl.

     Properties. Setters help create properties for entities on the page, such as pages in
     the Page element, fields in the Field element, or data in the Data or DataItem
     elements. You configure properties in the Setter elements. Add a separate Setter
     element for each property you want to define. You edit the properties using the
     SetterControl and configure other Setter elements using other controls.

     Data. Data is used to store information for use by the wizard page and other
     components. You can define data for pages or fields using the Data or DataItem
     elements. The data can be defined in a flat or hierarchical structure through the
     proper use of the Data or DataItem elements. The Config.xml in the example in the
     SDK shows how to build flat data structures.

     The custom wizard page editor that you create must be able to manage these
     configuration settings.

Review the EditorPage Example

<!-- p.1591 -->

The EditorPage example is used to configure the configuration settings for the
SamplePage wizard page in the UDI Wizard configuration file. The EditorPage example
has the following primary components:

     UI to configure the Location combo box settings

     UI to add or edit a location in the list of possible locations, which are shown in the
     Location combo box

     Configuration settings read from and saved to the UDI Wizard configuration file

     Supporting code for the other components

     Review the EditorPage example in Visual Studio by performing the following steps:

   1. Review how the SampleEditor wizard page editor is loaded and initialized in the
     UDI Wizard Designer as described in Review Wizard Page Editor Loading and
     Initialization.

   2. Review the UI used to edit the Location combo box in the LocationPageEditor.xaml
     and LocationPageEditor.xaml.cs files as described in Review the User Interface Used
     to Configure the Location Combo Box.

   3. Review the UI used to add or edit locations to the list in the
     AddEditLocationView.xaml and AddEditLocationView.xaml.cs files as described in
     Review the User Interface Used to Modify the List of Possible Locations.

   4. Review the code used to manage configuration information saved in the UDI
     Wizard configuration file as described in Review the Code Used to Manage
     Configuration Information.

Review Wizard Page Editor Loading and Initialization

Custom wizard page editors are loaded as required by the UDI Wizard Designer. The
UDI Wizard Designer configuration files are loaded when the UDI Wizard Designer
starts. The UDI Wizard Designer scans the install_folder\Bin\Config folder (where
install_folder is the name of the folder where MDT is installed) for files that have a
.config file extension.

During the configuration of the UDI development environment, you copied the
SamplePage.dll.confg file to the install_folder\Bin\Config folder. When you start the UDI
Wizard Designer, the SamplePage.dll.confg file is found and loaded.

The UDI Wizard Designer uses the following attributes of the Page element in the
SamplePage.dll.confg file to load and initialize the EditorPage example:

<!-- p.1592 -->

     DesignerAssembly. This attribute determines the name of the DLL to be loaded.
     This DLL needs to be placed in the same folder as the UDIDesigner.exe file, which
     is the install_folder\Bin folder (where install_folder is the name of the folder in
     which MDT is installed).

     DesignerType. This attribute is the Microsoft .NET type name of the class that
     contains the WPF user control.

     Type. Use this attribute to configure the page type of the custom wizard page,
     which the UDI Wizard loads. The UDI Wizard Designer uses this attribute to locate
     the appropriate Page element in the UDI Wizard configuration file.

     Dll. Use this attribute to configure the DLL element in the UDI Wizard
     configuration file, which the UDI Wizard Designer creates.

     Description. Use this attribute to provide information about the wizard page
     editor. The value of this attribute is shown in the Add New Page dialog box in the
     UDI Wizard Designer, which is used to add the wizard page to the "Page Library".

     DisplayName. Use this attribute to provide the name of the custom wizard page
     that is displayed in the UDI Wizard Designer. The value of this attribute is shown in
     the Add New Page dialog box in the UDI Wizard Designer, which is used to add
     the wizard page to the "Page Library".

     In the example, the type of the SamplePage custom wizard page is
     Microsoft.SamplePage.LocationPage, which is saved in the Config.xml file. The
     Config.xml file resides in the local_folder\SDK\SamplePage\SamplePage folder to
     (where local_folder is the folder you created on the development computer earlier
     in the configuration process).

Review the User Interface Used to Configure the Location Combo
Box

When the wizard page editor is loaded and initialized, the SampleEditor wizard page
editor is loaded when a page with a type of Microsoft.SamplePage.LocationPage is
edited. The UI for the page editor is stored in the LocationPageEditor.xaml file.

If you examine the UI on the Design tab and the code on the XAML tab, you can see the
relationship between the graphical UI and the elements and attributes in the Extensible
Application Markup Language (XAML).

For example, if you review the Controls:FieldElementControl element in the XAML you
can see how that relates to the layout of the corresponding UI. Use the
Controls:FieldElementControl element to define the FieldElementControl control.

<!-- p.1593 -->

The Binding parameters in the XAML file bind the fields on the sample page editor with
the information in the UDI wizard configuration file. For example, the following code ties
the Default value text box with the Default element in the UDI wizard configuration file
(Config.xml in the example):

  XML

  <TextBox Text="{Binding FieldData.DefaultValue,
   UpdateSourceTrigger=PropertyChanged,
   Mode=TwoWay}"/>

For more information, see How to: Make Data Available for Binding in XAML.

Use the Views:CollectionTControl.ColumnCollectionView element in the XAML to edit
the list of available locations in the grid view. You use the CollectionTControl control to
display the grid view and bind the grid view to the Data element with the name
Location in the UDI configuration file.

Review the User Interface Used to Modify the List of Possible
Locations

The UI for modifying the list of possible locations consists of:

     A context-sensitive menu and Ribbon buttons that allow you to add, edit, remove,
     or change the order of items in the list of locations as described in Review Context-
     sensitive Menu and Ribbon Buttons for Modifying the List of Locations

     A dialog box that is initiated when you select to add or edit an item in the list of
     locations as described in Review the Dialog Box for Adding or Editing Locations

Review Context-sensitive Menu and Ribbon Buttons for Modifying the
List of Locations

When you right-click in the list box that contains the list of locations, a context-sensitive
menu is displayed. The Ribbon has corresponding buttons that allow you to perform the
same tasks. The Views:CollectionsTControl control element in the
LocationPageEditor.xaml file defines the methods called based on the action taken and
properties that you set as follows:

     SelectedItem. This data-bound property is activated when the user selects an item
     from the list. This property is tied to the CurrentLocation property in the view
     model, which is located in the LocationPageEditorViewModel.cs file and used by

<!-- p.1594 -->

     the CollectionTControl control to pass the item selected when you edit or remove
     an existing item.

     AddItemAction. This action is performed when the user selects the Add Item
     option from the context-sensitive menu or the corresponding buttons on the
     Ribbon. There is a data binding to a property in the view model that returns the
     AddLocationAction object. This object is the AddLocationCallback method,
     located in the LocationPageEditorViewModel.cs file, and displays the dialog box in
     the AddEditLocationView.xaml file.

     EditItemAction. This action is performed when the user selects the Edit Item
     option from the context-sensitive menu. There is a data binding to a property in
     the view model that returns the EditLocationAction object. This object is the
     EditLocationCallback method, located in the LocationPageEditorViewModel.cs file,
     and displays the dialog box in the AddEditLocationView.xaml file.

     RemoveAction. This action is performed when the user selects the Remove Item
     option from the context-sensitive menu. There is a data binding to a property in
     the view model that returns the RemoveAction object. This object is the
     EditLocationCallback method, located in the LocationPageEditorViewModel.cs file,
     and shows a message that confirms the deletion of the location.

Review the Dialog Box for Adding or Editing Locations

If you add a new location to the list of locations or edit an existing location, a message
is displayed that is in the AddEditLocationView.xaml file. The message is displayed using
the ShowDialogWindow window method in the LocationPageEditorViewModel.cs file.

The UI in the AddEditLocationView.xaml file consists of:

     A dialog frame named DialogFrame, which includes the following elements:

        A title, which you configure using the DialogTitle attribute of the dialog frame

        An OK button, which sets the return status as for the Approved property to True
        (The return status is checked in the AddLocationCallback method in the
        LocationPageEditorViewModel.cs file to determine whether the user selected
        OK.)

        A Cancel button, which sets the return status as for the Approved property to
        False (The return status is checked in the AddLocationCallback method in the
        LocationPageEditorViewModel.cs file to determine whether the user selected
        Cancel.)

<!-- p.1595 -->

     A WPF element that contains:

        A label, which you configure using the Content attribute

        A text box, which is bound to the Data element with the name Location in the
        UDI configuration file (the Config.xml file in the example)

Review the Code Used to Manage Configuration Information

The configuration information for your custom wizard page is stored in the UDI Wizard
configuration file, which is the:

     Config.xml file in the example provided with the UDI SDK (This file contains only
     the configuration settings for the example.)

     UDIWizard_Config.xml file provided with MDT, stored in the
     installation_folder\Templates\Distribution\Scripts folder (where installation_folder is
     the folder in which you installed MDT); this file contains the configuration settings
     for all the built-in wizard pages and stages

     In the SampleEditor example, the Locations routine helps manage the
     configuration information and is located in the LocationPageEditorViewModel.cs
     file. The Locations routine returns a list of the locations from the UDI Wizard
     configuration file. Specifically, the list returned contains an item for each DataItem
     element in the UDI Wizard configuration file.

Creating Custom UDI Wizard Pages
The high-level process for creating custom UDI wizard pages is as follows:

   1. Make a copy of the SamplePage solution as a starting point.

   2. Place the desired controls (fields) on the form.

   3. Write code to perform the appropriate tasks when the wizard page loads
     (overrides for the OnWindowCreated method), including the following steps:

      a. Initialize the form.

      b. Read memory variables, task sequence variables, environment variables, or XML
        file information (such as Setter properties).

   4. Write any code to perform the appropriate tasks when the page is shown
     (overrides for the OnWindowShown method), including the following steps:

<!-- p.1596 -->

      a. Enable or disable controls based on information read when the page loaded in
        step 3.

     b. Update the controls based on information read when then page loaded in step
        3, such as the population of controls based on the information read.

   5. Write any code to perform the appropriate tasks while the user interacts with the
     wizard page.

   6. Write any code to perform the appropriate tasks when the user selects Next in the
     UDI Wizard (overrides for the OnNextSelected method), including the following
     steps:

      a. Update any memory variables, task sequence variables, environment variables,
        or XML file information.

     b. Update summary page information (if not performed by the fields on the page).

   7. Build the solution.

     Ensure that the version of the DLL you create is the same processor platform as the
     installation of MDT—specifically, the processor platform for Windows
     Preinstallation Environment (Windows PE). The UDI Wizard can run in:

           The existing operating system on the target computer. You can run 32-bit
           versions of your wizard page on 32-bit or 64-bit Windows operating systems.
           However, you can only run 64-bit versions of your wizard page on 64-bit
           Windows operating systems.

           Windows PE on the target computer. Windows PE does not support running
           32-bit applications on a 64-bit version of Windows PE. So, you need to have
           built a version for your wizard page for each processor architecture of
           Windows PE that you plan to use.

   8. Copy the DLL for your custom wizard page to
     installation_folder\Templates\Distribution\Tools\ platform folder (where
     installation_folder is the folder in which you installed MDT and platform is x86 for
     the 32-bit version or x64 is for the 64-bit version).

   9. Complete the steps for creating custom page editor.

Creating Custom Wizard Page Editors
The high-level process for creating custom UDI wizard page editors is as follows:

<!-- p.1597 -->

 1. Make a copy of the SampleEditor solution as a starting point.

 2. Create the primary page editor UI in an .xaml file.

 3. Add instances of the FieldElementControl control as required by the wizard page
   to be configured (if required).

 4. Add instances of the SetterControl control as required by the wizard page to be
   configured (if required).

 5. Add instances of the CollectionTControl control as required by the wizard page to
   be configured (if required).

 6. Add the IDataService interface.

 7. Write the appropriate code to update the UDI Wizard configuration file based on
   the configuration settings to be configured using your custom wizard page editor.

 8. Create child dialog boxes in a .xaml file, and call them from the primary page
   editor using the IMessageBoxService interface as required by the wizard page to
   be configured.

 9. Add the appropriate interfaces to the UDI Wizard Designer Ribbon based on the
   requirements of the wizard page to be configured.

10. Build the solution.

      ７ Note

      Ensure that the version of the DLL you create is the same processor platform
      as the installation of MDT. For example, if you install the 64-bit version of
      MDT, then build a 64-bit version of your custom page editor.

11. Create a UDI Wizard Designer configuration file to load the necessary DLLs and
   map the wizard page editor with the corresponding wizard page (the
   SamplePage.dll.config file in the example).

   For more information about the elements required to perform the mapping
   between the wizard page and the wizard page editor, see the DesignerMappings
   element, child elements, and corresponding attributes.

12. Copy the UDI Wizard Designer configuration file that you created in the previous
   step to the installation_folder\Bin\Config folder (where installation_folder is the
   folder in which you installed MDT version).

<!-- p.1598 -->

 13. Copy the DLL for your custom wizard page editor to the installation_folder\Bin
     folder (where installation_folder is the folder in which you installed MDT).

Creating Custom UDI Tasks
UDI tasks are DLLs written in C++ that implement the ITask interface. You register the
DLL with the UDI Wizard Designer task library by creating a UDI Wizard Designer
configuration file (.config file) and placing it in the installation_folder\Bin\Config folder
(where installation_folder is the folder in which you installed MDT).

  ７ Note

  You can create a DLL that contains wizard pages, tasks, and validators within the
  same .dll file. You can also create a single UDI Wizard Designer configuration file
  (.config) that contains the configuration settings for the wizard pages, tasks, and
  validators in the DLL.

To create custom UDI tasks

   1. Write code that implements the ITask Interface and the following methods:

           Init. This method is called to initialize your task.

           Execute. This method is called to run your task.

   2. Write code that registers the custom task class factory with the factory registry.

   3. Build the solution for your custom task.

        ７ Note

        Ensure that the version of the DLL you create is the same processor platform
        as the installation of MDT. For example, if you install the 64-bit version of
        MDT, then build a 64-bit version of your custom UDI task.

   4. Create a Task element under the TaskLibrary element in the UDI Wizard Designer
     configuration file similar to the following excerpt:

        XML

        <Task DLL="OSDRefreshWizard.dll" Description="Discovers supported
        applications for install." Type="Microsoft.OSDRefresh.AppDiscoveryTask"
        Name="Application Discovery">

<!-- p.1599 -->

           <TaskItem Type="Setter" Name="Status Bitmap">
              <Param Name="BitmapFilename"/>
           </TaskItem>
           <TaskItem Type="Setter" Name="Log File">
              <Param Name="log"/>
           </TaskItem>
           <TaskItem Type="Setter" Name="Write Configuration File">
              <Param Name="writecfg"/>
           </TaskItem>
           <TaskItem Type="Setter" Name="Read Configuration File">
              <Param Name="readcfg"/>
           </TaskItem>
        </Task>

        ７ Note

        All Task elements should include the BitmapFilename parameter. Specify all
        other parameters as the task requires. For example, in the previous excerpt,
        the log parameter is used to specify a parameter for the location of a log file.

   5. Copy the UDI Wizard Designer configuration file created in the previous step to
     the installation_folder\Bin\Config folder (where installation_folder is the folder in
     which you installed MDT).

   6. Copy the DLL for your custom task to the
     installation_folder\Templates\Distribution\Tools\ platform folder (where
     installation_folder is the folder in which you installed MDT and platform is x86 for
     the 32-bit version or x64 is for the 64-bit version).

Creating Custom UDI Validators
UDI validators are DLLs written in C++ that implement the IValidator interface. You
register the DLL with the UDI Wizard Designer validator library by creating a UDI Wizard
Designer configuration file (.config file) and placing it in the
installation_folder\Bin\Config folder (where installation_folder is the folder in which you
installed MDT).

To create custom UDI validators

   1. Write code that creates a subclass of the BaseValidator class and implements the
     following methods:

           Init(IControl *pControl, IWizardPageContainer *pContainer,
           IStringProperties *pProperties). The form controller calls the Init member to

<!-- p.1600 -->

        initialize the validator. This method must call the Init method for the
        BaseValidator class. It typically reads any properties set for the validator from
        the UDI Wizard configuration file. For example, the
        InvalidCharactersValidator validator retrieves the value of the InvalidChars
        property using this method.

        IsValid. The form controller calls this method to see whether the control
        contains valid text. The following is an example of the IsValid method for a
        validator that validates that the field is not empty:

          C++

          BOOL IsValid(LPBSTR pMessage)
          {
              __super::IsValid(pMessage);

                _bstr_t text;
                m_pText->GetText(text.GetAddress());
                return (text.length() > 0);
          }

        Init(IControl *pControl, LPCTSTR message). The form controller calls this
        member for each keystroke and other events so that the validator can
        validate the contents of the control and updated messages at the bottom of
        the wizard page (or clear them).

        Typically, these are the only methods that you need to override. However,
        depending on the validator, you may need to override other methods in the
        subclass of the BaseValidator class you create. For more information about
        these other methods, see the BaseValidator class.

2. Write code that registers the custom task class with the registry factory.

3. Build the solution for your custom task.

    ７ Note

    Ensure that the version of the DLL you create is the same processor platform
    as the installation of MDT. For example, if you install the 64-bit version of
    MDT, then build a 64-bit version of your custom UDI task.

4. Create a Validator element under the ValidatorLibrary element in the UDI Wizard
  Designer configuration file similar to the following excerpt:
