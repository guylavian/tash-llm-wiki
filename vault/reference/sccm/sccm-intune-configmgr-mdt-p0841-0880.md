---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 841-880"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p0841-0880
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p0841-0880
family: sccm
documentKind: "doc"
abstract: "Step 5-14: Add Controls to New Custom Wizard Page After the new UDI custom wizard page has been added to the New Computer stage group, the appropriate controls need to be added to the new custom wizard page. The controls are added to the custom wizard page from the Build Your Ow"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 841-880

<!-- p.841 -->

Step 5-14: Add Controls to New Custom Wizard Page
After the new UDI custom wizard page has been added to the New Computer stage
group, the appropriate controls need to be added to the new custom wizard page. The
controls are added to the custom wizard page from the Build Your Own Page toolbox,
which is displayed when you view the custom wizard page on the Configure tab in the
UDI Wizard Designer.

Table 38 lists the types of controls to your custom wizard page, which is illustrated in
Figure 1.

Table 38. Types of Controls in the UDI Build Your Own
Page Toolbox

                                                                                  ﾉ   Expand table

 Control      Description
 type

 Checkbox     This control allows you to select or clear a configuration option and behaves as a
              traditional user interface (UI) check box. This control has a corresponding label that
              you can use to describe the purpose of the check box. The state of this control is
              True when the check box is selected and False when the check box is cleared. The
              state of the check box is stored in the task sequence variable configured for this
              control. For more information on this control, see "Checkbox Control" in the MDT
              document, Toolkit Reference.

 Combobox     This control allows you to select an item from a list of items and behaves as a
              traditional UI drop-down list. This control allows you to add or remove items from
              the list and provide a corresponding value that will be set in the task sequence
              variable configured for this control. For more information on this control, see
              "Combobox Control" in the MDT document, Toolkit Reference.

 Line         This control allows you to add a horizontal line to divide one portion of the custom
              wizard page from another. This control does not collect any configuration values
              but rather is used to visually enhance the UI. For more information on this control,
              see "Line Control" in the MDT document, Toolkit Reference.

 Label        This control allows you to add descriptive, read-only text to the wizard page. This
              control does not collect any configuration values but rather is used to visually
              enhance the UI. For more information on this control, see "Label Control" in the
              MDT document, Toolkit Reference.

 Radio        This control allows you to select one configuration option from a group of two or
              more options. As with traditional radio buttons, two or more of these controls can
              be grouped together, and then the user can select one of the options in the radio
              button group. A unique value is assigned to each option. The value assigned to the

<!-- p.842 -->

 Control       Description
 type

               selected option control is saved in the task sequence variable configured for this
               control. For more information on this control, see "Radio Control" in the MDT
               document, Toolkit Reference.

 Bitmap        This control allows you to add a bitmap graphic (.bmp file) to the custom wizard
               page. This control does not collect any configuration values but rather is used to
               visually enhance the UI. The path to the .bmp file is relative to the location of the
               UDI Wizard (OSDSetupWizard.exe). For more information on this control, see
               "Bitmap Control" in the MDT document, Toolkit Reference.

 Textbox       This control allows you to enter text on the custom wizard page. The text typed into
               this control is saved in the task sequence variable configured for this control. For
               more information on this control, see "Textbox Control" in the MDT document,
               Toolkit Reference.

You can add any combination of these controls to your custom wizard page based on
the information you want to collect. In addition, you can use the Show Gridlines check
box to show or hide gridlines that can be used to assist in visually designing the custom
wizard page.

For the purposes of this example, you will create a custom wizard page as illustrated in
Figure 1.

Figure 1. Custom wizard page to be created

Figure 1. Custom wizard page to be created

<!-- p.843 -->

To add controls to the new custom wizard page

  1. In the Page Library, select User Information page.

  2. In the details pane, select the Configure tab.

    The Build Your Own Page toolbox and empty wizard page are displayed.

  3. In the Build Your Own Page toolbox, drag the Label control to the empty wizard
    page at approximately the following coordinates:

          x = 30

          y=5

          The label control is placed on the wizard page and named label1.

  4. On the custom wizard page, select label1 (the label control added in step 3).

    This control acts as a heading for the custom wizard page and describes the
    purpose of the page.

  5. Configure the layout properties of label1 on the Layout tab using the information
    in Table 39. Accept the default values unless otherwise stated.

    Table 39. label1 Layout Properties

                                                                        ﾉ   Expand table

      Property             Value

      Label                User and organization information

      X                    30

      Y                    5

  6. In the Build Your Own Page toolbox, drag the Label control to the empty wizard
    page at approximately the following coordinates:

          x = 60

          y = 60

          The label control is placed on the wizard page and named label2.

  7. On the custom wizard page, select label2 (the control added in the previous step).

<!-- p.844 -->

   This control acts as a label for the text box used to enter the user name.

 8. Configure the layout properties of label2 on the Layout tab using the information
   in Table 40. Accept the default values unless otherwise stated.

   Table 40. lable2 Layout Properties

                                                                       ﾉ   Expand table

    Property                                Value

    Label                                   User name

    X                                       60

    Y                                       60

 9. In the Build Your Own Page toolbox, select and drag the Textbox control to the
   empty wizard page at approximately the following coordinates:

         x = 60

         y = 80

         The Textbox control is placed on the wizard page and named text1.

10. On the custom wizard page, select text1 (the control added in the previous step).

   This control is the text box used to enter the user name.

11. Configure the layout properties of text1 on the Layout tab using the information in
   Table 41. Accept the default values unless otherwise stated.

   Table 41. text1 Layout Properties

                                                                       ﾉ   Expand table

    Property                                            Value

    X                                                   60

    Y                                                   80

    Width                                               400

<!-- p.845 -->

12. Configure the settings properties of text1 on the Settings tab using the
   information in Table 42. Accept the default values unless otherwise stated.

   Table 42. text1 Settings Properties

                                                                        ﾉ   Expand table

    Property                                                 Value

    Task sequence variable name                              FullName

    Friendly display name visible in summary page            Registered user name

13. In the Build Your Own Page toolbox, drag the Label control to the empty wizard
   page at approximately the following coordinates:

         x = 60

         y = 60

         The Label control is placed on the wizard page and named label3.

14. On the custom wizard page, select label3 (the control added in the previous step).

   This control acts as a label for the combo box used to select the organization or
   department name for the user.

15. Configure the layout properties of lable3 on the Layout tab using the information
   in Table 43. Accept the default values unless otherwise stated.

   Table 43. lable3 Layout Properties

                                                                        ﾉ   Expand table

    Property             Value

    Label                Organization or department name

    X                    60

    Y                    121

16. In the Build Your Own Page toolbox, drag the Combobox control to the empty
   wizard page at approximately the following coordinates:

         x = 60

<!-- p.846 -->

        y = 140

        The Combobox control is placed on the wizard page and named combo1.

17. On the custom wizard page, select combo1 (the control added in the previous
   step).

   This control is the combo box used to select the organization name.

18. Configure the layout properties of combo1 on the Layout tab using the
   information in Table 44. Accept the default values unless otherwise stated.

   Table 44. combo1 Layout Properties

                                                                          ﾉ   Expand table

    Property                                         Value

    X                                                60

    Y                                                80

    Width                                            400

19. Add data items to the layout properties of combo1 on the Layout tab using the
   information in Table 45. Accept the default values unless otherwise stated.

   Table 45. combo1 Data Items

                                                                          ﾉ   Expand table

    Value                                      Display Value

    Woodgrove Bank - New York City             Woodgrove Bank - New York City

    Woodgrove Bank - Dallas                    Woodgrove Bank - Dallas

    Woodgrove Bank - Chicago                   Woodgrove Bank - Chicago

    Woodgrove Bank - Seattle                   Woodgrove Bank - Seattle

20. Configure the settings properties of combo1 on the Settings tab using the
   information in Table 46. Accept the default values unless otherwise stated.

   Table 46. combo1 Settings Properties

<!-- p.847 -->

                                                                        ﾉ   Expand table

      Property                                          Value

      Task sequence variable name                       OrgName

      Friendly display name visible in summary page     Registered organization name

 21. On the Ribbon, on the Home tab, select Save.

     The File Save dialog box appears.

 22. In the File Save dialog box, select OK.

 23. Close the UDI Wizard Designer.

Step 5-15: Update the Distribution Points for the MDT
Files Package
After the UDI Wizard configuration file, UDIWizard_Config.xml, has been updated for the
MDT Files package in Configuration Manager, update the distribution points for the
MDT Files package. Updating the distribution points copies the updated version of the
UDIWizard_Config.xml file to the deployment shares specified in the package.

To update the distribution points for the MDT Files package

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Software
     Library.

   3. In the Software Library workspace, go to Overview/Application
     Management/Packages.

   4. In the preview pane, select MDT Files.

   5. On the Ribbon, on the Home tab, in the Deployment group, select Update
     Distribution Points.

     The Configuration Manager dialog box opens, notifying you that you are going to
     update the package on all distribution points.

   6. In the Configuration Manager dialog box, select OK.

<!-- p.848 -->

   7. Close all open windows and dialog boxes.

     Configuration Manager starts updating the distribution points with the latest
     versions of the UDIWizard_Config.xml file. This process could take several minutes.
     Check the status of the package until the Last Update value of the package status
     has been updated to a recent date and time.

Step 6: Deploy the Captured Image of the
Reference Computer to the Target Computer
When you have captured the image of the reference computer and created and
configured the task sequence, deploy the captured image. Configure MDT to provide all
the necessary configuration settings to deploy to the target computer. After initiating
the deployment process, the image of the reference computer running Windows 8.1 is
automatically deployed to the target computer and configured with the settings
defined.

Deploy the captured image by:

     Adding the target computer to the Configuration Manager site database as
     described in Step 6-1: Add the Target Computer to the Configuration Manager Site
     Database

     Creating a computer collection that includes the target computer as described in
     Step 6-2: Create a Computer Collection That Includes the Target Computer

     Deploy the task sequence created earlier in the process as described in Step 6-3:
     Deploy the Target Computer Task Sequence

     Starting the target computer with the task sequence bootable media as described
     in Step 6-4: Start the Target Computer with the Task Sequence Bootable Media

Step 6-1: Add the Target Computer to the Configuration
Manager Site Database
To deploy an operating system without stand-alone media to a new computer that
Configuration Manager does not currently manage, add the new computer to the
Configuration Manager site database prior to initiating the operating system
deployment process. Configuration Manager can automatically discover computers on
the network that have a Windows operating system installed; however, if the computer
has no operating system installed, use the Import Computer Information Wizard to
import the new computer information.

<!-- p.849 -->

To add the target computer to the Configuration Manager site database

  1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

  2. In the Configuration Manager console, in the navigation pane, select Assets and
     Compliance.

  3. In the Assets and Compliance workspace, go to Overview/Devices.

  4. On the Ribbon, on the Home tab, in the Create group, select Import Computer
     Information.

     The Import Computer Information Wizard starts.

  5. Complete the Import Computer Information Wizard using the information in Table
     47. Accept the default values unless otherwise specified.

     Table 47. Information for Completing Import
     Computer Information Wizard

                                                                            ﾉ   Expand table

      On this wizard page     Do this

      Select Source           Select Import single computer, and then select Next.

      Select Source: Single   1. In Computer Name, type WDG-CLI-01.
      Computer                2. In MAC address, type mac_address (where mac_address is the
                              MAC address of the primary network adapter for the target
                              computer, WDG-CLI-01).
                              3. Select Next.

      Select Source: Data     Select Next.
      Preview

      Select Source: Choose   Select Next.
      Target Collection

      Summary                 Review the information in the Details box that you provided
                              while completing the previous wizard pages, and then select
                              Next.

      Progress                The progress for importing the computer is displayed.

      Confirmation            Select Close.

<!-- p.850 -->

     For more information on adding a new computer to the Configuration Manager
     site database, see the section, "To import computer information for a single
     computer," in the section, "How to Deploy Operating Systems in Configuration
     Manager," in the Configuration Manager Documentation Library, which is installed
     with Configuration Manager.

Step 6-2: Create a Computer Collection That Includes the
Target Computer
In the Configuration Manager console, create a collection that includes the target
computer (WDG-CLI-01). You use this computer collection later when advertising the
task sequence created earlier in the process.

To create a computer collection that includes the target computer

   1. Select Start, point to All Programs, and then point to Microsoft System Center
     2012. Point to Configuration Manager, and then select Configuration Manager
     Console.

   2. In the Configuration Manager console, in the navigation pane, select Assets and
     Compliance.

   3. In the Assets and Compliance workspace, go to Overview/Device Collections.

   4. On the Ribbon, on the Home tab, in the Create group, select Create Device
     Collection.

     The Create Device Collection Wizard starts.

   5. Complete the Create Device Collection Wizard using the information in Table 48.
     Accept the default values unless otherwise specified.

     Table 48. Information for Completing the Create
     Device Collection Wizard

                                                                            ﾉ   Expand table

      On this         Do this
      wizard page

      General          a. In Name, type Microsoft Deployment - Batch 01.
                      b. In Comment, type Computers that are to be included in the first batch
                         of computers deployed.

<!-- p.851 -->

      On this        Do this
      wizard page

                      c. In Limited Collection, select Browse.

                        The Browse Collections dialog box appears. Complete the dialog box
                        by performing the following steps:

                           i. In the Browse Collection dialog box, in Name, select All Systems.
                          ii. Select OK.
                      d. Select Next.

      Membership      a. Select Add Rule, and then select Direct Rule.
      Rules
                         The Create Direct Membership Rule Wizard starts.
                      b. Complete the Create Direct Membership Rule Wizard by performing
                         the following steps:

                           i. On the Welcome page, select Next.
                          ii. On the Search for Resources page, in Resource class, select System
                              Resource; in Attribute name, select Name; in Value, type WDG-CLI-
                              01; and then select Next.
                         iii. On the Select Resources page, select WDG-CLI-01, and then select
                              Next. Note: The process for adding the target computer (WDG-CLI-
                              01) to All Systems can take a few minutes to finish. If WDG-CLI-01
                              does not appear in the list, repeat steps b and c until WDGCLI01
                             appears.
                         iv. On the Summary page, select Next.
                          v. On the Completion page, select Close.
                      c. Select Next.

      Summary        Review the information in the Details box that you provided while
                     completing the previous wizard pages, and then select Next.

      Progress       The progress for creating the device collection is displayed.

      Completion     Select Close.

     For more information, see the section, "How to Create Collections in Configuration
     Manager," in the Configuration Manager Documentation Library, which is installed
     with Configuration Manager.

Step 6-3: Deploy the Target Computer Task Sequence
In the Configuration Manager console, deploy the task sequence created earlier in the
process for the target computers. Deploy the task sequence to the collection of target
computers created earlier in the process.

<!-- p.852 -->

To deploy the task sequence

  1. Select Start, point to All Programs, and then point to Microsoft System Center
    2012. Point to Configuration Manager, and then select Configuration Manager
    Console.

  2. In the Configuration Manager console, in the navigation pane, select Software
    Library.

  3. In the Software Library workspace, go to Overview/Operating Systems/Task
    Sequences.

  4. In the preview pane, select UDI - Windows 8.1 Target Deployment.

  5. On the Ribbon, on the Home tab, in the Deployment group, select Deploy.

    The Deploy Software Wizard starts.

  6. Complete the Deploy Software Wizard using the information in Table 49. Accept
    the default values unless otherwise specified.

    Table 49. Information for Completing the Deploy
    Software Wizard

                                                                          ﾉ   Expand table

      On this wizard page     Do this

      General                 1. In Collection, select Browse.
                              2. In the Browse Collection dialog box, select Microsoft
                              Deployment - Batch 01, and then select OK.
                              3. In Comment, type Deploy Windows 8.1 to the first batch of
                              target computers using UDI.
                              4. Select Next.

      Deployment Settings     1. In Purpose, select Available.
                              2. Select the Make available to boot media and PXE check box.
                              3. Select Next.

      Deployment Settings:    Select Next.
      Schedule

      Deployment Settings:    Select Next.
      User Experience

      Deployment Settings:    Select Next.
      Alerts

<!-- p.853 -->

      On this wizard page      Do this

      Deployment Settings:     Select Next.
      Distribution Points

      Summary                  Review the information in the Details box that you provided
                               while completing the previous wizard pages, and then select
                               Next.

      Progress                 The progress for creating the deploying the task sequence is
                               displayed.

      Completion               Select Close.

     For more information, see the section, "How to Deploy a Task Sequence," in the
     Configuration Manager Documentation Library, which is installed with
     Configuration Manager.

Step 6-4: Start the Target Computer with the Task
Sequence Bootable Media
Start the target computer (WDG-CLI-01) with the task sequence bootable media created
earlier in the process. This medium starts Windows PE on the reference computer and
initiates the MDT process. At the end of the MDT process, Windows 8.1 is deployed on
the target computer.

  ７ Note

  You can also initiate the MDT process by starting the target computer from
  Windows Deployment Services.

To start the target computer with the task sequence bootable media

  1. Start WDG-CLI-01 with the task sequence bootable media created earlier in the
     process.

     Windows PE starts, and then the Task Sequence Wizard starts.

  2. Complete the Task Sequence Wizard using the information in Table 50. Accept the
     default values unless otherwise specified.

     Table 50. Information for Completing the Task
     Sequence Wizard

<!-- p.854 -->

                                                                                ﾉ   Expand table

   On this wizard page               Do this

   Welcome to the Task               In Password, type P@ssw0rd, and then select Next.
   Sequence Wizard

   Select a Task Sequence            In the list box, select UDI - Windows 8.1 Target
                                     Deployment, and then select Next.

  At the appropriate task sequence step, the UDI Deployment Wizard starts.

3. Complete the UDI Deployment Wizard using the information in Table 51. Accept
  the default values unless otherwise specified.

  Table 51. Information for UDI Deployment Wizard

                                                                                ﾉ   Expand table

   On this wizard        Do this
   page

   Welcome               Select Next.

   User Information      1. In User Name, type Woodgrove Bank Chicago Employee.
                         2. In Organization or Department Name, select Woodgrove Bank -
                         Chicago.
                         3. Select Next.

   BitLocker             Select Next.

   Volume                Select Next.

   Select Target         Select Next.

   Deployment            1. Review the configuration checks, and ensure that the status for all
   Readiness             checks are set to Success.
                         2. Select Next.

   New Computer          1. In Computer name, type WDG-CLI-01. Note: In unknown computer
   Details               scenarios, users could change the computer name to the appropriate
                         value.
                         2. In User name, type MDT2013\Administrator.
                         3. In Password and Confirm password, type P@ssw0rd.
                         4. Select Next.

   Administrator         1. In Administrator password and Confirm password, type P@ssw0rd.
   Password              2. Select Next.

<!-- p.855 -->

    On this wizard     Do this
    page

    User Device        Select the Set primary user check box, and then select Next.
    Affinity

    Language           Select Next.

    Install Programs   Verify that the Microsoft Office Professional Plus 2010 - x86 check box
                       is selected, and then select Next.

    Summary            Review the information that you provided while completing the
                       previous wizard pages, and then select Finish.

   To monitor the reference computer deployment process using the Deployment
   Workbench

 4. On WDG-MDT-01, select Start, and then point to All Programs. Point to Microsoft
   Deployment Toolkit, and then select Deployment Workbench.

 5. In the Deployment Workbench console tree, go to Deployment
   Workbench/Deployment Shares/MDT Deployment Share
   (C:\DeploymentShare$)/Monitoring.

 6. In the details pane, view the deployment process for WDG-REF-01.

 7. In the Actions pane, periodically select Refresh.

   The status of the deployment process is updated in the details pane. Continue to
   monitor the deployment process until the process is complete.

 8. In the details pane, select WDG-REF-01.

 9. In the Actions pane, select Properties.

   The WDG-REF-01 Properties dialog box is displayed.

10. In the WDG-REF-01 Properties dialog box, on the Identity tab, view the
   monitoring information provided about the deployment process as described in
   Table 52.

   Table 52. Monitoring Information About the
   Deployment Process

                                                                            ﾉ   Expand table

<!-- p.856 -->

Information         Description

ID                  Unique identifier for the computer being deployed.

Computer Name       The name of the computer being deployed.

Deployment status   The current status of the computer being deployed; the status can
                    be one of the following:

                    - Running. The task sequence is healthy and running.
                    - Failed. The task sequence failed, and the deployment process was
                    unsuccessful.
                    - Completed. The task sequence has finished.
                    - Unresponsive. The task sequence has not updated its status in the
                    past four hours and is assumed to be nonresponsive.

Step                The current task sequence step being run.

Progress            The overall progress of the task sequence. The progress bar
                    indicates how many task sequence steps have been run out of the
                    total number of task sequence steps.

Start               The time the deployment process started.

End                 The time the deployment process ended.

Elapsed             The length of time the deployment process has been running or
                    took to run if the deployment process has finished.

Errors              The number of errors encountered during the deployment process.

Warnings            The number of warnings encountered during the deployment
                    process.

Remote Desktop      This button allows you to establish a remote desktop connection
                    with the computer being deployed using the Windows Remote
                    Desktop feature. This method assumes that:

                    - The target operating system is running and has remote desktop
                    support enabled
                    - mstsc.exe is in the path Note: This button is always visible but may
                    not be able to establish a remote desktop session if the monitored
                    computer is running Windows PE, has not completed installation of
                    the target operating system, or does not have the Remote Desktop
                    feature enabled.

VM Connection       This button allows you to establish a remote desktop connection to
                    a VM running in HyperV. This method assumes that:

                    - The deployment is being performed to a VM running on Hyper-V
                    - vmconnect.exe is located in the %ProgramFiles%\Hyper-V folder

<!-- p.857 -->

    Information         Description

                        Note: This button appears when ZTIGather.wsf detects that Hyper-V
                        integration components are running on the monitored computer.
                        Otherwise, this button will not be visible.

    DaRT Remote         This button allows you to establish a remote control session using
    Control             the remote viewer feature in DaRT.

                        This method assumes that:

                        - DaRT has been deployed to the target computer and is currently
                        running
                        - DartRemoteViewer.exe is located in the
                        %ProgramFiles%\Microsoft DaRT 7\v7 folder Note: This button
                        appears when ZTIGather.wsf detects that DaRT is running on the
                        monitored computer. Otherwise, this button will not be visible.

    Automatically       Check box that controls whether the information in the dialog box is
    refresh this        automatically refreshed. If the check box is:
    information every
    10 seconds          - Selected, the information is refreshed every 10 seconds
                        - Cleared, the information is not automatically refreshed and must
                        be manually refreshed using the Refresh Now button

    Refresh Now         This button immediately refreshes the information displayed in the
                        dialog box.

11. In the WDG-REF-01 Properties dialog box, select OK.

12. Close the Deployment Workbench.

   To monitor the reference computer deployment process using the Get-
   MDTMonitorData cmdlet

13. On WDG-MDT-01, select Start, point to Administrative Tools, and then select
   Windows PowerShell Modules.

   The Windows PowerShell Modules command prompt opens.

14. Create a Windows PowerShell drive that uses the MDT PowerShell provider by
   running the New-PSDrive cmdlet as shown in the following example:

     PowerShell

     New-PSDrive -Name DS001 -PSProvider mdtprovider -Root
     d:\DeploymentShare$

<!-- p.858 -->

15. View the MDT monitoring process by running the Get-MDTMonitorData cmdlet,
   as shown in the following example:

     PowerShell

     Get-MDTMonitorData -Path DS001:

   This command returns the monitoring data collected by the MDT monitoring
   service running on the same computer that hosts the deployment share as shown
   in the following example output:

     PowerShell

     Name               : WDG-REF-01
     PercentComplete    : 96
     Settings           :
     Warnings           : 0
     Errors             : 0
     DeploymentStatus   : 1
     StartTime          : 6/7/2012 6:45:39 PM
     EndTime            :
     ID                 : 1
     UniqueID           : 94a0830e-f2bb-421c-b1e0-6f86f9eb9fa1
     CurrentStep        : 130
     TotalSteps         : 134
     StepName           : Gather
     LastTime           : 6/7/2012 8:46:32 PM
     DartIP             :
     DartPort           :
     DartTicket         :
     VMHost             : XYL-DC-02
     VMName             : WDG-REF-01
     ComputerIdentities : {}

     Name                : WDG-CLI-01
     PercentComplete     : 26
     Settings            :
     Warnings            : 0
     Errors              : 0
     DeploymentStatus    : 1
     StartTime           : 6/7/2012 3:07:13 AM
     EndTime             :
     ID                  : 2
     UniqueID            : 94a0830e-f2bb-421c-b1e0-6f86f9eb9fa1
     CurrentStep         : 49
     TotalSteps          : 134
     StepName            : Capture Network Settings using MDT
     LastTime            : 6/7/2012 3:08:32 AM
     DartIP              :
     DartPort            :
     DartTicket          :

<!-- p.859 -->

        VMHost             :
        VMName             :
        ComputerIdentities : {}

 16. Close the Windows PowerShell console.

     If any problems occur during the deployment, consult the MDT document
     Troubleshooting Reference. When successfully completed, the target computer is
     running a Windows 8.1 operating system configured like the reference computer.

     At the completion of the deployment process, Windows 8.1 starts for the first time,
     and the Welcome tab in the Deployment Complete dialog box is displayed. The
     Welcome tab displays helpful information about the deployment and provides
     contact information in the event issues with the deployment occur.

     Review the information on the Deployment Summary and Applications Installed
     tabs to verify that Windows 8.1 and Office Professional Plus 2010 were installed
     correctly. When you have finished reviewing these tables, select Start Windows to
     log on to Windows 8.1 for the first time.

  ７ Note

  Configuration Manager applications are not displayed on the Applications
  Installed tab. Instead, they are detected after the user logs on to the target
  computer for the first time.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.860 -->

Toolkit Reference for the Microsoft
Deployment Toolkit
Article • 02/12/2024

This reference is part of Microsoft® Deployment Toolkit (MDT) 2013 and provides
configuration settings that you can use in the deployment process. Review the MDT
2013 documents Microsoft Deployment Toolkit Samples Guide and Using the Microsoft
Deployment Toolkit for help in customizing configuration settings for the deployment
environment.

  ７ Note

  In this document, Windows applies to the Windows 8.1, Windows 8, Windows 7,
  Windows Server® 2012 R2, Windows Server 2012, and Windows Server 2008 R2
  operating systems unless otherwise noted. MDT does not support ARM processor-
  based versions of Windows. Similarly, MDT refers to MDT 2013 unless otherwise
  stated.

Microsoft® Deployment Toolkit (MDT) 2013 reference articles:

      Task Sequence Steps.
      Properties.
      Scripts.
      Support Files.
      Utilities.
      MDT Windows PowerShell Cmdlets.
      Tables and Views in the MDT DB.
      Windows 7 Feature Dependency Reference.
      UDI Reference.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.861 -->

Task Sequence Steps
Article • 02/12/2024

Task sequences are created by the Task Sequence Editor and consist of a combined series
of steps that are designed to complete an action. Task sequences can operate across a
computer restart and can be configured to automate tasks on a computer without
requiring user intervention. In addition, you can add task sequence steps to a task
sequence group, which helps keep similar task sequence steps together for better
organization and error control.

Each task sequence step performs a specific task, such as validating that the target
computer is capable of receiving the deployment image, storing user data in a safe
location, deploying an image to a target computer, and restoring saved user data. These
task sequence steps accomplish their tasks by using utilities and scripts provided with
MDT or by the deployment team. Use this reference to help determine the correct task
sequence groups and task sequence steps to configure the deployment process and the
valid properties and options to use.

The following information is provided for each task sequence group and step:

      Name. The name of the task sequence group or step

      Description. A description of the purpose of the task sequence group or step and
      any pertinent information regarding its customization

      Properties. Indicates the valid configuration properties that you can specify for the
      task sequence group or step that define how the task is performed

      Options. Indicates the valid configuration options that you can specify for the task
      sequence group or step that define if and when the task is performed and what is
      considered a successful exit code from the task

      For more information about the Task Sequence Editor, see Operating System
      Deployment: Task Sequence Editor.

Common Properties and Options for Task
Sequence Step Types
Each task sequence group and step has configurable settings on the Properties and
Options tabs that are common to all task sequence groups and steps. These common
settings are briefly described in the following sections.

<!-- p.862 -->

Common Properties
Table 1 shows the settings that are available on the Properties tab of each task
sequence step. For more information about the Properties tab for a particular task
sequence step, see the topic that corresponds to the step later in this reference.

  ７ Note

  The task sequence step types listed here are those that are available in the
  Deployment Workbench. Additional task sequence step types might be available
  when configuring task sequences using Microsoft System Center 2012 R2
  Configuration Manager.

Table 1. Settings Available on the Properties Tab

                                                                                 ﾉ   Expand table

 Name         Description                                                            Group   Step

 Type         A read-only value that indicates the task sequence group or step       -       -
              type. The type will be set to one of these values:

              - Apply Network Settings

              - Authorize DHCP

              - Capture Network Settings

              - Configure ADDS

              - Configure DHCP

              - Configure DNS

              - Enable BitLocker

              - Format and Partition Disk

              - Gather

              - Group

              - Inject Drivers

              - Install Application

<!-- p.863 -->

 Name           Description                                                              Group   Step

                - Install Operating System

                - Install Roles and Features

                - Install Updates Offline

                - Recover From Domain Join Failure

                - Restart computer

                - Run Command Line

                - Validate

 Name           A user-defined name that should allow easy identification and            -       -
                differentiation from other task sequence steps.

 Description    A user-defined description that should make the task sequence            -       -
                step requirements and tasks easily understandable.

Common Options
Table 2 shows the settings that are available on the Options tab of a task sequence step.
For more information about the Options tab, see Task Sequence Options Tab.

Table 2. Settings Available on the Options Tab

                                                                                    ﾉ    Expand table

 Name                Description                                                         Group   Step

 Disable this        Select this option to disable this task sequence step.              -       -
 step

 Success codes       Exit codes of the utility associated with this task sequence step           -
                     that indicate that the step has finished successfully.

 Continue on         Select this option to allow the Task Sequencer to process           -       -
 error               additional task sequence steps if a failure occurs.

 Conditional         One or more conditions that limit the running of this task          -       -
 statements          sequence group or step. These conditional are based on the
                     following:

                     - File properties

<!-- p.864 -->

Name   Description                                                     Group   Step

       - Folder properties

       Operating system version:

       - Is a certain architecture

       - Is a certain version

       - Query Windows Management Instrumentation (WMI)

       Registry setting:

       - Exists

       - Does not exist

       - Equals

       - Does not equal

       - Greater than

       - Greater than or equals

       - Less than

       - Less than or equals

       - Installed software

       Task sequence variable:

       - Exists

       - Equals

       - Does not equal

       - Greater than

       - Greater than or equals

       - Less than

       - Less than or equals

       These conditions can be grouped using IF statements that test

<!-- p.865 -->

 Name             Description                                                        Group   Step

                  all conditions, any condition, or no condition that evaluates as
                  True.

  ７ Note

  Additional conditional statements might be available when using Configuration
  Manager to configure task sequence steps.

Specific Properties and Settings for Task
Sequence Step Types
Some properties and parameters of each task sequence step type are unique to that
type. Each type with unique properties and settings is shown in the following sections
with its unique task sequence step properties and settings.

Apply Network Settings
This task sequence step configures the network adapter on the target computer. For
more information about what script accomplishes this task and which properties are
used, see ZTINICConfig.wsf.

The unique properties and settings for the Apply Network Settings task sequence step
type are:

Properties

                                                                                 ﾉ   Expand table

 Name                   Value

 Type                   Apply Network Settings

Settings

                                                                                 ﾉ   Expand table

<!-- p.866 -->

Name                         Value

Name                         The name to be assigned to the network connection.

Obtain an IP address         When selected, Dynamic Host Configuration Protocol (DHCP) is
automatically                used to obtain the required Internet Protocol (IP) configuration
                             settings for the network connection. This is the default selection.

Use the following IP         When selected, you can provide one or more IP address and subnet
address                      mask combinations in addition to gateways that will be assigned to
                             the network connection.

Obtain a Domain Name         When selected, DHCP is used to obtain the required IP
System (DNS) server          configuration settings for the network connection. This is the
automatically                default selection.

Use the following DNS        When selected, you can provide one or more DNS server IP
servers                      addresses that will be assigned to the network connection.

DNS Suffix                   The DNS suffix that will be applied to all network connections that
                             use TCP/IP.

Register this connection's   Specifies that the computer will attempt dynamic registration of the
address in DNS               IP addresses (through DNS) of this connection with the full
                             computer name of this computer.

Use this connection's DNS    Specifies whether DNS dynamic update is used to register the IP
suffix in DNS registration   addresses and the connection-specific domain name of this
                             connection.

WINS server addresses        You can provide one or more Windows Internet Naming Service
                             (WINS) server IP addresses that will be assigned to the network
                             connection.

Enable LMHOSTS lookup        Specifies whether a local area network (LAN) Manager Hosts
                             (LMHOSTS) file for network basic input/output system (NetBIOS)
                             name resolution is used.

Default                      Specifies whether this network connection obtains the setting to
                             enable or disable NetBIOS over TCP/IP (NetBT) from a DHCP server.
                             This is the default selection.

Enable NetBIOS over          Specifies that this network connection uses NetBT and WINS.
TCP/IP

Disable NetBIOS over         Specifies that this network connection does not use NetBT and
TCP/IP                       WINS.

Authorize DHCP

<!-- p.867 -->

This task sequence step authorizes the target computer as a DHCP server. For more
information about which script accomplishes this task and which properties you use, see
ZTIAuthorizeDHCP.wsf.

The unique properties and settings for the Authorize DHCP task sequence step type are:

Properties

                                                                             ﾉ   Expand table

 Name            Description

 Type            Set this read-only type to Authorize DHCP Server.

Settings

                                                                             ﾉ   Expand table

 Name      Description

 Name      Description

 Account   A user account that is a member of the Enterprise Admins group, to be used when
           authorizing DHCP for the target computer.

Capture Network Settings
This task sequence step gathers the network adapter settings from the target computer.
For more information about which script accomplishes this task and which properties
you use, see ZTINICConfig.wsf.

The unique properties and settings for the Capture Network Settings task sequence
step type are:

Properties

                                                                             ﾉ   Expand table

 Name        Description

 Name        Description

 Type        Set this read-only type to Capture Network Settings.

<!-- p.868 -->

Settings

                                                                                 ﾉ   Expand table

 Name                                Description

 None                                None

Configure ADDS
This task sequence step configures the target computer as an Active Directory® Domain
Services (AD DS) domain controller. For more information about the settings listed in
the following tables and which this task sequence step can configure, see the Microsoft
Help and Support article, How to use unattended mode to install and remove Active
Directory Domain Services on Windows Server 2008-based domain controllers.

The unique properties and settings for the Configure ADDS task sequence step type
are:

Properties

                                                                                 ﾉ   Expand table

 Name          Description

 Type          Set this read-only type to Configure ADDS.

Settings

                                                                                 ﾉ   Expand table

 Name              Description

 Create            Specifies the configuration set that will be used to configure the target
                   computer. The configuration sets are:

                   - New domain controller replica. Creates an additional domain controller in
                   an existing AD DS domain

                   - New read-only domain controller (RODC) replica. Creates an RODC

                   - New domain in existing forest. Creates a domain in an existing AD DS
                   forest

<!-- p.869 -->

Name                 Description

                     - New domain tree in existing forest. Creates a new tree in an existing AD DS
                     forest

                     - New forest. Creates a new AD DS forest

Domain DNS           The DNS name of the new or existing domain.
name

Domain NetBIOS       The NetBIOS name of the new child domain, child domain tree, or forest that
name                 pre-AD DS clients use to access the domain. This name must be unique on
                     the network.

DNS name             The DNS name of the child domain or domain tree.

Replication          The name of the domain controller from which to source AD DS on new
source domain        replica or backup domain controller upgrade installations. If no value is
controller           supplied, the closest domain controller from the domain being replicated will
                     be selected by default.

Account              The account to be used to perform the configuration.

Recovery (safe       The password for the offline Administrator account that is used in AD DS
mode) password       Repair mode.

Install DNS if not   When selected, DNS will be installed if it has not already been installed.
already present

Make this            Specifies whether the replica will also be a GC server. When selected, the
domain               target computer will be configured as a GC server if the replication source
controller a         domain controller is a GC server.
global catalog
(GC) server

Wait for critical    When selected, this setting specifies that only critical replication is sourced
replication only     during the replication phase of Dcpromo. Noncritical replication resumes
                     when the computer restarts as a domain controller.

Forest functional    Specifies the functional level for a new forest. Available options are:
level
                     - Windows Server 2003

                     - Windows Server 2008

                     - Windows Server 2008 R2

Domain               Specifies the functional level for a new domain. Available options are:
functional level
                     - Windows Server 2003

                     - Windows Server 2008

<!-- p.870 -->

 Name             Description

                  - Windows Server 2008 R2

 Database         Fully qualified, non-Universal Naming Convention (UNC) directory on a hard
                  disk of the local computer that will host the AD DS database (NTDS.dit). If the
                  directory exists, it must be empty. If it does not exist, it will be created. Free
                  disk space on the logical drive selected must be 200 megabytes (MB) and
                  possibly larger when rounding errors are encountered and to accommodate
                  all objects in the domain. For best performance, the directory should be
                  located on a dedicated hard disk.

 Log files        Fully qualified, non-UNC directory on a hard disk on the local computer to
                  host the AD DS log files. If the directory exists, it must be empty. If it does not
                  exist, it will be created.

 SYSVOL           Fully qualified, non-UNC directory on a hard disk of the local computer that
                  will host the AD DS System Volume (SYSVOL) files. If the directory exists, it
                  must be empty. If it does not exist, it will be created. The directory must be
                  located on a partition that is formatted with the NTFS version 5.0 file system.
                  For best performance, the directory should be located on a different physical
                  hard disk than the operating system.

 Site name        The value of an existing AD DS site on which to locate the new domain
                  controller. If not specified, an appropriate site will be selected. This option
                  only applies to the new tree in a new forest scenario. For all other scenarios, a
                  site will be selected using the current site and subnet configuration of the
                  forest.

Configure DHCP
This task sequence step configures the DHCP server service on the target computer. For
more information about which script accomplishes this task and which properties you
use, see ZTIConfigureDHCP.wsf.

The unique properties and settings for the Configure DHCP task sequence step type
are:

Properties

                                                                                  ﾉ   Expand table

 Name        Description

 Type        Set this read-only type to Configure DHCP Server.

<!-- p.871 -->

Settings

                                                                                   ﾉ   Expand table

Name       Description

Name       Configure DHCP

Scope      These options apply to any client computers that obtain a lease within that particular
Details    scope. Configured scope option values always apply to all computers obtaining a
           lease in a given scope unless they are overridden by options assigned to class or
           client reservation.

           Within the Scope Details setting, the following sub-settings are configurable:

           - Scope Name. A user-definable name

           - Start IP address. The starting IP address for the scope

           - End IP address. The ending IP address for the scope

           - Subnet mask. The subnet mask of the client subnet

           - Lease duration for DHCP clients. The duration that the DHCP lease is valid for the
           client

           - Description. A description of the scope

           - Exclude IP address range, Start IP address. The starting IP address for the range of
           IP addresses that are to be excluded from the scope

           - Exclude IP address range, End IP address. The ending IP address for the range of IP
           addresses that are to be excluded from the scope

           - 003 Router. A list of IP addresses for routers on the client subnet

           - 006 DNS Servers. A list of IP addresses for DNS name servers available to the client

           - 015 DNS Domain Name. The domain name that the DHCP client should use when
           resolving unqualified domain names with DNS

           - 044 WINS/NBNS Servers. Lists the IP addresses for NetBIOS name servers (NBNSes)
           on the network

           - 046 WINS/NBT Node Type. Configures the client node type for NetBT clients

           - 060 PXE Client. The address used for Pre-Boot Execution Environment (PXE) client
           bootstrap code

<!-- p.872 -->

 Name       Description

 Server     These options apply globally for all scopes and classes defined at each DHCP server
 Options    and for any clients that a DHCP server services. Configured server option values
            always apply unless they are overridden by options assigned to other scope, class, or
            client reservation.

            Within the Server Options setting, the following sub-settings are configurable:

            - 003 Router. A list of IP addresses for routers on the client subnet

            - 006 DNS Servers. A list of IP addresses for DNS name servers available to the client

            - 015 DNS Domain Name. The domain name that the DHCP client should use when
            resolving unqualified domain names with the DNS

            - 044 WINS/NBNS Servers. Lists the IP addresses for NBNSes on the network

            - 046 WINS/NBT Node Type. Configures the client node type for NetBT clients

            - 060 PXE Client. The address used for PXE client bootstrap code

Configure DNS
This task sequence step configures DNS on the target computer. For more information
about which script accomplishes this task and which properties you use, see
ZTIConfigureDNS.wsf.

The unique properties and settings for the Configure DNS task sequence step type are:

Properties

                                                                                    ﾉ   Expand table

 Name         Description

 Type         Set this read-only type to Configure DNS Server.

Settings

                                                                                    ﾉ   Expand table

<!-- p.873 -->

Name         Description

Name         Configure DNS

Zones        Within the Scope Details setting, the following sub-settings are configurable:

             - DNS zone name. A user-definable name

             - Type. The type of DNS zone to be created

             - Replication. Specifies the replication scheme used to share information among
             DNS servers

             - Zone file name. The zone's DNS database file

             - Dynamic updates. Enables DNS client computers to register and dynamically
             update their resource records with a DNS server whenever changes occur

             - Scavenge stale resource records. Removes stale resource records

Server       Within the Server Properties setting, the following sub-settings are configurable:
Properties
             - Disable recursion. Specifies that the DNS server will not perform recursion on
             any query

             - BIND secondaries. Specifies whether to use fast transfer format to transfer a zone
             to DNS servers running legacy Berkeley Internet Name Domain (BIND)
             implementations

             - Fail on load if bad data. Specifies the DNS server should parse files strictly

             - Enable round robin. Specifies the DNS server should use the round robin
             mechanism to rotate and reorder a list of resource records if multiple resource
             records exist of the same type exist for a query answer

             - Enable netmask ordering. Specifies whether the DNS server should reorder
             resource records within the same resource record set in its response to a query
             based on the IP address of the source of the query

             - Secure cache against pollution. Specifies whether the DNS server will attempt to
             clean up responses to avoid cache pollution

             - Name checking. Configures the name-checking method to be used

 ７ Note

 The Configure DNS task sequence step uses the Dnscmd tool, which is included in
 Windows Support Tools, to configure DNS. Be sure that Windows Support Tools is

<!-- p.874 -->

  installed before running the Configure DNS task sequence step.

  ７ Note

  For more information about these server properties, see Dnscmd.

Enable BitLocker
This task sequence step configures BitLocker® Drive Encryption on the target computer.
For more information about this step type, see Enable BitLocker.

The unique properties and settings for the Enable BitLocker task sequence step type
are:

Properties

                                                                                     ﾉ   Expand table

 Name             Description

 Type             Set this read-only type to Enable BitLocker.

Settings

                                                                                     ﾉ   Expand table

 Name                           Description

 Current operating              When selected, the operating system drive will be configured. This is
 system drive                   the default selection.

 Specific drive                 When selected, the specified drive will be configured.

 TPM only                       When selected, the Trusted Platform Module (TPM) is required. This is
                                the default selection.

 Startup key on USB only        When selected, a startup key is required on the specified USB drive.

 TPM and startup key on         When selected, the TPM is required in addition to a startup key on
 USB                            the specified USB drive.

 In Active Directory            When selected, the recovery key is stored in AD DS. This is the default
                                selection.

<!-- p.875 -->

 Name                        Description

 Do not create a recovery    When selected, the recovery key is not created. Using this option is
 key                         not recommended.

 Wait for BitLocker to       When selected, this step will not finish until after BitLocker has
 complete                    finished processing all drives.

Execute Runbook
This task sequence step runs Microsoft System Center 2012 Orchestrator runbooks on
the target computer. An Orchestrator runbook is the sequence of activities that
orchestrate actions on computers and networks. You can initiate Orchestrator runbooks
in MDT using this task sequence step type.

  ７ Note

  This task sequence step is not included any MDT task sequence templates. You
  must add this task sequence step to any task sequences you create.

The unique properties and settings for the Execute Runbook task sequence step type
are:

Properties

                                                                                    ﾉ   Expand table

 Name          Description

 Type          Set this read-only type to Execute Runbook.

 Name          The name of the task sequence step, which should reflect the name of the runbook
               being run.

 Description   Informative text that provides additional information about the task sequence step

Settings

                                                                                    ﾉ   Expand table

<!-- p.876 -->

Name           Description

Orchestrator   Type the URL for the Orchestrator web service, which includes the server name.
Server         The Orchestrator web service can use either Hypertext Transfer Protocol (HTTP)
               or HTTP over Secure Sockets Layer (HTTPS). The Orchestrator web service
               defaults to port 81.

               The Orchestrator web service supports multiple runbook servers. By default, a
               runbook can run on any runbook server. A runbook can be configured to
               specify which runbook servers should be used to run the runbook.

               Note:

               The Orchestrator web service supports the ability to run a runbook on a specific
               runbook server. This feature is not supported in MDT.

               Specify the URL in any of the following formats:

               - servername. When using this format, the URL defaults to:

               https://<servername>:81/Orchestrator2012/Orchestrator.svc

               - servername:port. When using this format, the URL defaults to:

               https://<servername:port>/Orchestrator2012/Orchestrator.svc.

               - https://servername:port. When using this format, the URL defaults to:

               https://<servername:port>/Orchestrator2012/Orchestrator.svc.

               - https://servername:port. When using this format, the URL defaults to:

               https://<servername:port>/Orchestrator2012/Orchestrator.svc.

               - https://servername:port/Orchestrator2012/Orchestrator.svc. When using this
               format, MDT assumes that you are providing the fully qualified URL, because
               the value ends with .svc.

               - https://servername:port/Orchestrator2012/Orchestrator.svc. When using this
               format, MDT assumes that you are providing the fully qualified URL, because
               the value ends with .svc.

Runbook        Select Browse, and then select the name of the Orchestrator runbook that this
               task sequence should run.

               Note:

               To successfully browse for Orchestrator runbooks, install the ADO.NET Data

<!-- p.877 -->

Name               Description

                   Services Update for .NET Framework 3.5 SP1 for Windows 7 and Windows
                   Server 2008 R2.

Automatically      Select this option to automatically provide the Orchestrator runbook input
provide            parameter values( which assumes that the runbook parameter values are task
runbook            sequence variables). For example, if a runbook has an input parameter named
parameters         OSDComputerName, then the OSDComputerName task sequence variable
                   value is passed to the runbook.

                   Note:

                   This option works only for input parameters that are valid task sequence
                   variable names and do not contain spaces or other special characters. Although
                   spaces and other special characters are supported as Orchestrator parameter
                   names, they are not valid task sequence variable names. If you need to pass
                   values to parameters with spaces or other special characters, use the Specify
                   explicit runbook parameters option.

                   The other option is Specify explicit runbook parameters.

                   Note:

                   The values provided for the runbook input parameters to the Orchestrator web
                   service are formatted as XML. Passing values that contain data that is or
                   resembles XML-formatted data may cause errors.

Specify explicit   Select this option to explicitly provide the Orchestrator runbook input
runbook            parameters.
parameters
                   You must configure the following settings for each input parameter that the
                   Orchestrator runbook requires:

                   - Name. This is the name of the input runbook parameter.

                   Note:

                   If you change the parameters for an existing Orchestrator runbook, you need to
                   browse (reselect) for the runbook again, because MDT only retrieves the
                   parameter list when initially adding the Orchestrator runbook.

                   - Value. This can be a constant or a variable, such as a task sequence variable or
                   an environment variable. For example, you can specify a value of
                   %OSDComputerName%, which will pass the value of the OSDComputerName
                   task sequence variable to the runbook input parameter.

Wait for the       This check box controls whether the task sequence step will wait for the
runbook to         runbook to finish before proceeding to the next task sequence step.

<!-- p.878 -->

 Name                Description

 finish before       If this check box is:
 continuing
                     - Selected, then the task sequence step will wait for the runbook to finish
                     before proceeding on to the next task sequence step.

                     When this check box is selected, the task sequence step will poll the
                     Orchestrator web service for the runbook to finish. The amount of time
                     between polls starts at 1 second, then increases to 2, 4, 8, 16, 32, and 64
                     seconds between each poll. Once the amount of time reaches 64 seconds, the
                     task sequence step continues to poll every 64 seconds.

                     - Cleared, then the task sequence step will not wait for the runbook to finish
                     before proceeding to the next task sequence step.

                     Note:

                     This check box must be selected if the runbook returns output parameters.

Format and Partition Disk
This task sequence step partitions and formats disks on the target computer. For more
information about this step type, see Format and Partition Disk.

The unique properties and settings for the Format and Partition Disk task sequence
step type are:

Properties

                                                                                     ﾉ    Expand table

 Name            Description

 Type            Set this read-only type to Format and Partition Disk.

Settings

                                                                                     ﾉ    Expand table

 Name              Description

 Disk number       The physical number of the disk to be configured.

<!-- p.879 -->

 Name          Description

 Disk type     The type of drive to be created. Values are:

               - Standard (MBR) (Master Boot Record)

               - GPT (GUID [globally unique identifier] Partition Table).

               The default selection is Standard (MBR).

 Volume        Within the Volume setting, the following sub-settings are configurable:

               - Partition Name. A user-definable name.

               - Partition Type. Values vary by disk type:

               - MBR: Primary only

               - GPT: Primary, EFI, or MSR

               - Use a percentage of remaining space.

               - Use specific drive size. Values are in increments of 1 MB or 1 gigabyte (GB).

               - Make this a boot partition.

               - File System. Values are NTFS or FAT32.

               - Quick Format. When selected, a quick format is performed.

               - Variable. The drive letter that was assigned to this newly configured partition.

  ７ Note

  When using the CustomSettings.ini file to specify the hard disk and partition
  configurations, only the first hard disk and first two partitions will be configured.
  Edit ZTIGather.xml to configure additional hard disks or partitions.

Gather
This task sequence step gathers data and processing rules for the target computer. The
unique properties and settings for the Gather task sequence step type are:

Properties

<!-- p.880 -->

                                                                                   ﾉ    Expand table

 Name                Description

 Type                Set this read-only type to Gather.

Settings

                                                                                   ﾉ    Expand table

 Name                Description

 Gather only local   When selected, this step processes only the properties contained in the
 data                ZTIGather.xml file.

 Gather local data   When selected, this step processes the properties contained in the
 and process rules   ZTIGather.xml file and the properties contained in the file that the Rules file
                     specifies. This is the default selection.

 Rules file          The name of the Rules file to process. If left blank, the task sequence step
                     attempts to locate and process the CustomSettings.ini file.

  ７ Note

  This task sequence step is natively available in System Center 2012 R2
  Configuration Manager as Set Dynamic Variablesin the General group.

Inject Drivers
This task sequence step injects drivers that have been configured for deployment to the
target computer. The unique properties and settings for the Inject Drivers task
sequence step type are:

Properties

                                                                                   ﾉ    Expand table

 Name            Description

 Type            Set this read-only type to Inject Drivers.

Settings
