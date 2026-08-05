---
title: "Configuration Manager SDK documentation — pages 1001-1040"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1001-1040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1001-1040
family: sccm
documentKind: "doc"
abstract: "[\\\\\\\"Display=\\\\\\\\\\\\\\\\\" + serverName + \"\\\\\\\\\\\\\\\"]MSWNET:[\\\\\\\"SMS_SITE=\" + siteCode + \"\\\\\\\"]\\\\\\\\\\\\\\\\\" + serverName + \"\\\\\\\\,SMS Distribution Point\\\",ItemType=\\\"System Resource Usage\\\",SiteCode=\" + \"\\\"\" + siteCode + \"\\\"\"); // Create temporary copy of the embedded properties. Diction"
---

# Configuration Manager SDK documentation — pages 1001-1040

<!-- p.1001 -->

  [\\\"Display=\\\\\\\\" + serverName + "\\\\\\\"]MSWNET:[\\\"SMS_SITE=" +
  siteCode + "\\\"]\\\\\\\\" + serverName + "\\\\,SMS Distribution
  Point\",ItemType=\"System Resource Usage\",SiteCode=" + "\"" + siteCode +
  "\"");        // Create temporary copy of the embedded properties.
  Dictionary<string, IResultObject> embeddedPropertyLists =
  siteRole.EmbeddedPropertyLists;         // Get current mac addresses.
  string[] macAddresses = embeddedPropertyLists["BindExcept"]
  ["Values"].StringArrayValue;        //Convert to list.         List<string>
  addressList = new List<string>();         foreach (string address in
  macAddresses)        {            addressList.Add(address);          }
  // Add the new mac address to the list.         addressList.Add(macAddress);
  // Add the new mac address to the list.
  embeddedPropertyLists["BindExcept"]["Values"].StringArrayValue =
  addressList.ToArray();        siteRole.EmbeddedPropertyLists =
  embeddedPropertyLists;        // Save the settings.          siteRole.Put();
  }    catch (SmsException ex)    {         Console.WriteLine();
  Console.WriteLine("Failed. Error: " + ex.InnerException.Message);      }}

The example method has the following parameters:

                                                                        ﾉ     Expand table

 Parameter    Type                        Description

 connection   - Managed:                  A valid connection to the SMS Provider.
              WqlConnectionManager

 serverName   - Managed: String           The Configuration Manager server.

 siteCode     - Managed: String           The Configuration Manager site code.

 macAddress   - Managed: String           The MAC address to be added in the following
                                          format:

                                          00:11:22:33:44:55

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Text

<!-- p.1002 -->

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1003 -->

How to Set Operating System
Deployment Branding Information in
Configuration Manager
Article • 10/04/2022

You set the operating system deployment branding information for the Configuration
Manager client by changing the OSDBrandingSubtitle property of the client agent
component section in the site control file.

  ７ Note

   OSDBrandingSubtitle is encoded with BASE64 encoding.

The branding information is displayed by the task sequence when it is run on the client.

To set operating system deployment branding
information
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals .

   2. Get the client agent site control file client component object from
        SMS_SCI_ClientComp Server WMI Class.

   3. Set the OSDBrandingSubtitle property to the value you want.

   4. Commit the changes back to the site control file.

Example
The following example method changes the operating system deployment branding text
to the supplied value.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub SetOsdBranding(connection,               _
                        context,               _

<!-- p.1004 -->

                          siteCode,               _
                          brandingText)

    ' Load the site control file and get the Client Agent section.
    connection.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , context

     Query = "SELECT * FROM SMS_SCI_ClientComp " & _
             "WHERE ClientComponentName = 'Client Agent' " & _
             "AND SiteCode = '" & siteCode & "'"

    Set SCIComponentSet = connection.ExecQuery(Query, ,wbemFlagForwardOnly
Or wbemFlagReturnImmediately, context)

     ' Only one instance is returned from the query.
     For Each SCIComponent In SCIComponentSet

          ' Loop through the array of embedded SMS_EmbeddedProperty instances.
          For Each vProperty In SCIComponent.Props

                 ' Setting: OSDBrandingSubTitle.
                 If vProperty.PropertyName = "OSDBrandingSubTitle" Then
                     wscript.echo " "
                     wscript.echo vProperty.PropertyName
                     wscript.echo "Current value " & vProperty.Value1

                     ' Modify the value.
                     vProperty.Value1 = brandingText
                     wscript.echo "New value: " & brandingText
                 End If

          Next

                  ' Update the component in your copy of the site control file.
Get the path
                  ' to the updated object, which can be used later to retrieve
the instance.
                  Set SCICompPath = SCIComponent.Put_(wbemChangeFlagUpdateOnly,
context)
    Next

    ' Commit the change to the actual site control file.
    Set InParams =
connection.Get("SMS_SiteControlFile").Methods_("CommitSCF").InParameters.Spa
wnInstance_
    InParams.SiteCode = siteCode
    connection.ExecMethod "SMS_SiteControlFile", "CommitSCF", InParams, ,
context

End Sub

c#

<!-- p.1005 -->

  public void SetOsdBranding(
      WqlConnectionManager connection,
      string siteCode,
      string brandingText)
  {
      try
      {
          // Get the site control file client component section.
          IResultObject clientAgent =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" +
              siteCode + "',ItemName='Client Agent'");

          // Update the branding information.
          Dictionary<string, IResultObject> embeddedProperties =
  clientAgent.EmbeddedProperties;

          embeddedProperties["OSDBrandingSubTitle"]["Value1"].StringValue =
  brandingText;

              clientAgent.EmbeddedProperties = embeddedProperties;

              // Commit the change back to the site control file.
              clientAgent.Put();
       }
       catch (SmsException e)
       {
           Console.WriteLine("Failed to set branding text: " + e.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                                ﾉ   Expand table

 Parameter         Type                        Description

 connection        - Managed:                  A valid connection to the SMS Provider.
                   WqlConnectionManager
                   - VBScript: SWbemServices

 context           - VBScript: SWbemContext    A valid context qualifier object. For more
 (VBScript)                                    information, see How to Connect to an SMS
                                               Provider in Configuration Manager by Using WMI

 siteCode          - Managed: String           The site code for the Configuration Manager site.
                   - VBScript: String

 brandingText      - Managed: String           The text used to update the branding text.

<!-- p.1006 -->

 Parameter        Type                    Description

                  - VBScript: String

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

See Also
SMS_SCI_ClientComp Server WMI Class
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1007 -->

Operating System Deployment Task
Sequences Overview
Article • 10/04/2022

In Configuration Manager, a task sequence is a series of one or more task steps that can
be advertised to Configuration Manager clients to run user-specified actions. Task
sequences are used with operating system deployment to build source computers,
capture an operating system image, migrate user and computer settings, and deploy an
image to a collection of target computers. Task sequences can also be used to run other
Configuration Manager actions, such as deploying Configuration Manager software
packages or running custom command lines.

Configuration Manager provides a rich Windows Management Instrumentation (WMI)
object model for creating and editing task sequences. For more information, see
Operating System Deployment Task Sequence Object Model.

Task Sequence Steps
A task sequence step is either an individual action that is run on a computer, such as a
running a command line, or it is a set of actions arranged in a group. Task steps are
processed in order and can have conditions associated with them that determine
whether the action, or group of actions, is processed.

Actions
There are two types of actions: built in action and custom actions.

Built-in Actions
A Configuration Manager action that performs a specific action on the Configuration
Manager client computer is a built-in action. For example, Configuration Manager
provides built-in actions for partitioning disks and also for installing software. For more
information about the Configuration Manager built in actions, see the Configuration
Manager documentation library.

There is also a command-line action that the administrator can use for running scripts or
executable files on the Configuration Manager client computer.

<!-- p.1008 -->

Custom Actions
An action that you create yourself is a custom action. You can create custom actions that
call a process or script that you define in a Managed Object Format (MOF) file. You can
also create a control that integrates the custom action you create into the task sequence
editor. This allows the administrator to change custom action properties in the same
way that the Configuration Manager supplied actions are changed. Typically, you create
these custom actions when the built-in actions do not satisfy your requirements for an
action. For more information about creating custom actions, see About Configuration
Manager Custom Actions.

Running Task Sequences
To run a task sequence, you must perform the following:

To run a task sequence
   1. Ensure that you have the Configuration Manager site server installed and that you
     have clients to deploy task sequences to. Depending on your environment, you
     might need to configure the State Migration Point or PXE Service Point. For more
     information, see About OS deployment site role configuration.

   2. Create a package containing the files you need for deployment. For example, to
     deploy a boot image you will need to create a boot image package
     (SMS_BootImagePackage Server WMI Class).

   3. Assign the package to a distribution point. For more information, see How to
     Assign a Package to a Distribution Point.

   4. Create a task sequence. For more information, see How to Create an Operating
     System Deployment Task Sequence.

   5. Associate the task sequence with a task sequence package. For more information,
     see How to Create an Operating System Deployment Task Sequence Package.

   6. Advertise the task sequence package to the required client computers. To do this
     you create an SMS_Advertisement package. If you want to show a task sequence
     progress dialog box while the task sequence runs, set the SMS_Advertisement class
     AdvertFlags show task sequence progress bit (0x00800000). For more information,

     see About Software Distribution Advertisements.

<!-- p.1009 -->

   7. On the client computer, the task sequence is eventually available as an advertised
     program. Click the program to run it.

Detecting a Failed Task Sequence
When a task sequence runs, you can use the _SMSTSLastActionSucceeded variable to
determine if the last task sequence group run has failed. Depending on the environment
the task sequence is running in, you can then take appropriate action. Typically you will
copy the task logs to a share for inspection.

To detect a failed task sequence

   1. Set the continue on error property for the task sequence group that you want to
     detect failure on.

   2. Immediately after the group, create a group to handle the error.

   3. In the error handler group, Add a condition that runs the error handler group if
     _SMSTLastActionSucceeded = false .

   4. In the error handler group, add a Run Command Line action. This will be used for
     error handling in a WinPE environment.

   5. In the WinPE action, add the following command line to copy the log to an
     external share: smsswd.exe /run: cmd /c copy x:\windows\temp\smsts.log \\<Your
     server>\<Your Share>\%_SMSTSClientGuid%-smsts.log

   6. In the WinPE action, add a condition that runs the action if _SMSTSInWinPE is true.

   7. In the error handler group, add a run command-line action. This will be used for
     error handling in a full operating system environment.

   8. In the full operating system action, add the following command line to copy the
     log to an external share: smsswd.exe /run: cmd /c copy
     %windir%\system32\ccm\logs\smsts.log \\server\share\%_SMSTSClientGuid%-

     smsts.log

   9. In the WinPE action, add a condition that runs the action if _SMSTSInWinPE is false.

 10. In the error handler group, add a run command-line action and a command line
     that runs a recovery tool of your choosing.

<!-- p.1010 -->

Pre-Execution Hooks
You can run scripts or executables that can interact with the user in Windows PE before
the task sequence is selected. For more information, see Operating System Media Pre-
Execution Hook in the Configuration Manager library documentation.

See also
OS deployment task sequence object model

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1011 -->

Operating System Deployment Task
Sequence Object Model
Article • 10/04/2022

In Configuration Manager, operating system deployment task sequences are created
and edited by using a Windows Management Instrumentation (WMI) class-based object
model.

  Ｕ Caution

  Changing task sequences by updating the task sequence XML is not supported. You
  will only need the XML when exporting the task sequence to different site. The XML
  is stored in the SMS_TaskSequencePackage Server WMI Class Sequence property.

Task Sequence Packages
A task sequence is packaged in an instance of the SMS_TaskSequencePackage Server
WMI Class class and there is a single package for each task sequence. The package is
advertised to client computers by using an instance of the SMS_Advertisement Server
WMI Class class. To associate the task sequence package with the advertisement, you set
the SMS_Advertisement Server WMI Class PackageID property to the
SMS_TaskSequencePackage Server WMI Class PackageID property.

  ７ Note

  SMS_TaskSequencePackage Server WMI Class derives from SMS_Package Server
  WMI Class and can be used in the same way that packages are used. For more
  information, see Software distribution overview.

For more information about creating a task sequence package, see How to Create an
Operating System Deployment Task Sequence Package.

For more information about creating advertisements, see How to Create an
Advertisement.

Task Sequences

<!-- p.1012 -->

To create and manage task sequences, Configuration Manager provides a number of
WMI classes that represent a task sequence, task sequence steps (actions and groups)
and step conditions.

The key WMI classes are:

SMS_TaskSequence
The SMS_TaskSequence class represents an individual task sequence. You can either
create new instances of SMS_TaskSequence, or you can use the method
SMS_TaskSequencePackage.GetSequence to populate an SMS_TaskSequence with an
existing task sequence.

  ７ Note

  If you create a new SMS_TaskSequence, you must associate it with a
  SMS_TaskSequencePackage. Otherwise, Configuration Manager is not aware of its
  existence.

The class property SMS_TaskSequence.Steps is an array of SMS_TaskSequence_Step
derived classes. These steps are processed sequentially when the task sequence is run.

SMS_TaskSequenceStep
The two types of steps, action and group, derive from the SMS_TaskSequenceStep class.
The two types of steps are the SMS_TaskSequence_Group class for groups and the
SMS_TaskSequence_Action derived class for the Configuration Manager built-in, or
custom, actions.

A step has a number of properties that you can set.

                                                                                   ﾉ    Expand table

 Property          Description

 Condition         A condition that must be met for the step to be processed. This in an instance
                   of the SMS_TaskSequence_Condition class.

 ContinueOnError   If set to true , the task sequence will continue to the next step when an error
                   occurs. Otherwise the task sequence will propagate the failure back to the
                   parent. If the parent is a group, the parent group's ContinueOnError property
                   is evaluated. If the parent is the task sequence root, the task sequence will fail.

<!-- p.1013 -->

 Property          Description

 Enabled           If set to true , the step is processed. Otherwise, the step is not processed.

The step also has a Name and Description property.

  ７ Note

  This documentation refers to steps when the procedure is applicable to both
  actions and groups. For example, How to Remove a Step From an Operating
  System Deployment Group is a task that is applicable to both action removal and
  group removal.

SMS_TaskSequenceAction

Configuration Manager defines a number of built-in actions that are defined in classes
derived from the SMS_TaskSequence_Action class. For example, the action that allows
you to specify a command line is the SMS_TaskSequence_RunCommandLineAction class.

  ７ Note

  The built-in actions are named SMS_TaskSequence_ ActionName Action where
  ActionName is the name of the built-in action. For more information, see
  SMS_TaskSequence_Action server WMI class.

In addition to the properties that are inherited from SMS_TaskSequenceStep, a derived
action inherits the following properties from the SMS_TaskSequence_Action class that
you can set:

                                                                                   ﾉ   Expand table

 Property                Description

 SupportedEnvironment    Specifies the operating environment that the action can be run in. Valid
                         values are "WinPE", "FullOS", "WinPEandFullOS.

 Timeout                 Specifies the time-out period for the action, in seconds.

SMS_TaskSequenceGroup

<!-- p.1014 -->

The SMS_TaskSequence_Group Server WMI Class class represents a set of steps that are
processed sequentially. SMS_TaskSequence_Group Server WMI Class Steps property is
an array of SMS_TaskSequence_Step Server WMI Class classes that represent the group's
steps. Because a group step is derived from SMS_TaskSequence_Step Server WMI Class,
there can be further child groups within the steps.

SMS_TaskSequence_Condition
Each SMS_TaskSequence_Step Server WMI Class and the derived classes (actions and
groups) can have an associated condition that must be met for the condition to be run.
For example, you may want to process a step on a computer with Microsoft Office 2007
installed. Additionally, you may also want to further restrict the step to the Windows
Vista operating system.

  ７ Note

  For the condition to be processed, the SMS_TaskSequenceStep class Enabled
  property must be set to true .

Within a task sequence step, the SMS_TaskSequence_Step Server WMI Class Condition
property contains a SMS_TaskSequence_Condition Server WMI Class object that holds
the condition. The condition is made up of one or more operands that are defined in an
array of SMS_TaskSequence_ConditionOperand Server WMI Class derived classes by the
Operands property. Each operand is an expression that must evaluate to true , for the

step to be processed - a logical and operation.

Expressions

Individual expressions are defined in SMS_TaskSequence_ConditionExpression Server
WMI Class derived classes.

  ７ Note

  SMS_TaskSequence_ConditionExpression derives from

  SMS_TaskSequenceConditionOperand .

For example, you would use SMS_TaskSequence_SoftwareConditionExpression Server
WMI Class to define an expression for Microsoft Office 2007. The class used to define an
expression for Windows Vista would be SMS_TaskSequence_OSConditionGroup Server
WMI Class.

<!-- p.1015 -->

Nested Expressions
You can define more complex conditions containing nested expressions with
SMS_TaskSequence_ConditionOperator Server WMI Class. This class also derives from
SMS_TaskSequence_ConditionOperand Server WMI Class.

For example, you can form the condition Exp1 and (Exp2 or Exp3) by adding the
following condition operands to a task sequence step's SMS_TaskSequence_Condition
Server WMI Class instance's Operand array property.

     SMS_TaskSequence_ConditionExpression ( Exp1 ).

     SMS_TaskSequence_ConditionOperator (nested expression Exp2 or Exp3 ).

     The SMS_TaskSequence_ConditionOperator Server WMI Class Operands array
     property contains the expressions Exp2 and Exp3 and the
     SMS_TaskSequence_ConditionOperator Server WMI Class Operator property
     contains the desired operator. In this case or .

  ７ Note

  The operands in the task sequence step's SMS_TaskSequence_Condition Server
  WMI Class Operand array property are automatically compared with the and
  operator to evaluate the condition. The expressions in the
  SMS_TaskSequence_ConditionOperator must have an operator defined by the
  Operator property.

Since the SMS_TaskSequence_Condition Server WMI Class Operands property is an array
of SMS_TaskSequence_ConditionOperand Server WMI Class classes, you can create more
complex conditions such as Exp1 and (Exp2 or (Exp3 and Exp4)) .

For more information about conditions, see How to Add a Condition to an Operating
System Deployment Task Sequence Step.

See Also
SMS_TaskSequence_ConditionOperand Server WMI Class
How to Add a Condition to an Operating System Deployment Task Sequence Step

Feedback

<!-- p.1016 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1017 -->

How to Create an Operating System
Deployment Task Sequence
Article • 10/04/2022

You create a Configuration Manager operating system deployment task sequence by
creating an instance of the SMS_TaskSequence class.

A task sequence contains one or more steps that are run sequentially on the client
computer. For more information, see Operating System Deployment Task Sequence
Object Model.

The task sequence is then packaged in an SMS_TaskSequencePackage and advertised to
the client computer.

To create a task sequence
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Create a task sequence SMS_TaskSequence object.

   3. Add actions and, as required, add groups to the action. For more information, see
        How to Add an Operating System Deployment Task Sequence Action.

   4. Associate the task sequence with a task sequence package. For more information,
        see How to Create an Operating System Deployment Task Sequence Package.

   5. Advertise the task sequence to the client computer. For more information, see How
        to Create an Advertisement.

Example
The following example method creates a task sequence that installs a software program.
The example also creates a task sequence package by calling the example that is defined
in How to Create an Operating System Deployment Task Sequence Package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

<!-- p.1018 -->

Sub CreateInstallSoftwareTaskSequence(connection,name, description,
packageID, programName)

     ' Create the task sequence.
     set taskSequence = connection.Get("SMS_TaskSequence").SpawnInstance_

    ' Create the action.
    set action =
connection.Get("SMS_TaskSequence_InstallSoftwareAction").SpawnInstance_

     action.ProgramName=programName
     action.PackageID=packageID
     action.Name=name
     action.Enabled=true
     action.ContinueOnError=false

     ' Create an array to hold the action.
     actionSteps= array(action)
     ' Add the array to the task sequence.
     taskSequence.Steps=actionSteps

     wscript.echo taskSequence.Steps(0).Name
     call CreateTaskSequencePackage (connection, taskSequence)

 End Sub

c#

public void CreateInstallSoftwareTaskSequence(
    WqlConnectionManager connection,
    string name,
    string packageId,
    string programName)
{
    try
    {
        // Create the task sequence.
        IResultObject taskSequence =
connection.CreateInstance("SMS_TaskSequence");

        IResultObject ro =
connection.CreateEmbeddedObjectInstance("SMS_TaskSequence_InstallSoftwareAct
ion");
        ro["ProgramName"].StringValue = programName;
        ro["packageId"].StringValue = packageId;
        ro["Name"].StringValue = name;
        ro["Enabled"].BooleanValue = true;
        ro["ContinueOnError"].BooleanValue = false;

        // Add the step to the task sequence.
        List<IResultObject> array = taskSequence.GetArrayItems("Steps");

<!-- p.1019 -->

              array.Add(ro);

              taskSequence.SetArrayItems("Steps", array);

              // Create the task sequence package.
              this.CreateTaskSequencePackage(connection, taskSequence);
        }
        catch (SmsException e)
        {
            Console.WriteLine("Failed to create Task Sequence: " + e.Message);
            throw;
        }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter      Type                    Description

 Connection     - Managed:              A valid connection to the SMS Provider.
                 WqlConnectionManager
                - VBScript:
                SWbemServices

 name           - Managed: String       The task sequence step name.
                - VBScript: String

 description    - VBScript: String      The task sequence step description.

 packageID      - Managed: String       The package identifier containing the software to be
                - VBScript: String      installed. Obtained from SMS_Package.PackageID .

 programName    - Managed: String       The name of the program to be installed. Obtained
                - VBScript: String      from SMS_Program.ProgramName .

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

<!-- p.1020 -->

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
Task sequence overview How to Create an Operating System Deployment Task Sequence
Package

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1021 -->

How to Create an Operating System
Deployment Task Sequence Package
Article • 10/04/2022

You create an operating system deployment task sequence, in Configuration Manager,
by creating an instance of the SMS_TaskSequencePackage class. This class derives from
the SMS_Package class and holds the task sequence. It is advertised to clients who can
then run the task sequence. The task sequence is associated with the task sequence
package by using the SMS_TaskSequencePackage class SetSequence method.

You can organize task sequence packages into categories by assigning a category to
them with the SMS_TaskSequence class Category property.

For more information about creating task sequences, see How to Create a Task
Sequence. For more information about task sequence packages, see the Task
Sequencing Object Model.

You advertise a task sequence package in the same way that you advertise a
Configuration Manager package SMS_Package . For more information, see How to Create
an Advertisement.

To create a task sequence package
   1. Set up a connection to the SMS Provider. For more information, see About the
      SMS Provider in Configuration Manager.

   2. Create an instance of SMS_TaskSequencePackage .

   3. Populate the task sequence package properties.

   4. Call the SMS_TaskSequencePackage class SetSequence method to associate a task
      sequence ( SMS_TaskSequence ) with the task sequence package.

Example
The following example method creates a task sequence package
( SMS_TaskSequencePackage ) and associates task sequence ( SMS_TaskSequence ) with it.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.1022 -->

vbs

Sub CreateTaskSequencePackage (connection, taskSequence)

      Dim taskSequencePackage
      Dim packageClass
      Dim objInParams
      Dim objOutParams

    ' Create the new package object.
    Set taskSequencePackage =
connection.Get("SMS_TaskSequencePackage").SpawnInstance_

    ' Populate the new package properties.
    taskSequencePackage.Name = "New task sequence package"
    taskSequencePackage.Description = "A new task sequence package
description"

      ' Get the parameters object.
      Set packageClass = connection.Get("SMS_TaskSequencePackage")

      Set objInParams = packageClass.Methods_("SetSequence"). _
          inParameters.SpawnInstance_()

      ' Add the input parameters.
      objInParams.TaskSequence = taskSequence
      objInParams.TaskSequencePackage = taskSequencePackage

    ' Add the sequence.
     Set objOutParams = connection.ExecMethod("SMS_TaskSequencePackage",
"SetSequence", objInParams)

End Sub

c#

public IResultObject CreateTaskSequencePackage(
    WqlConnectionManager connection,
    IResultObject taskSequence)
{
    try
    {
        Dictionary<string, object> inParams = new Dictionary<string, object>
();

        // Create the new task sequence package.
        IResultObject taskSequencePackage =
connection.CreateInstance("SMS_TaskSequencePackage");

        taskSequencePackage["Name"].StringValue = "New task sequence
package";
        taskSequencePackage["Description"].StringValue = "A brand new task

<!-- p.1023 -->

  sequence package";
          taskSequencePackage["Category"].StringValue = "A custom category";

              // Note. Add other package properties as required.

          // Set up parameters that associate the task sequence with the
  package.
          inParams.Add("TaskSequence", taskSequence);
          inParams.Add("TaskSequencePackage", taskSequencePackage);

          // Associate the task sequence with the package. Note that a call to
  Put is not required.
          IResultObject result =
  connection.ExecuteMethod("SMS_TaskSequencePackage", "SetSequence",
  inParams);

              // The path to the new package.

  Console.WriteLine(result["SavedTaskSequencePackagePath"].StringValue);

              return taskSequencePackage;
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to create Task Sequence: " + e.Message);
          throw;
      }
  }

This example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter        Type                              Description

 connection       - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                  - VBScript: SWbemServices

 taskSequence     - Managed: IResultObject          A valid task sequence SMS_TaskSequence
                  - VBScript: SWbemObject

Compiling the Code
The C# example requires:

Namespaces
System

<!-- p.1024 -->

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create a Task Sequence
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1025 -->

How to Read a Task Sequence from a
Task Sequence Package
Article • 10/04/2022

You read a task sequence from a task sequence package, in Configuration Manager, by
calling the SMS_TaskSequencePackage class GetSequence method. GetSequence returns
an SMS_TaskSequence object that you can change and then put back in the package by
using the SetSequence method. For an example of using SetSequence, see How to
Create an Operating System Deployment Task Sequence Package.

To read a task sequence from a task sequence package
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Query the SMS Provider for the SMS_TaskSequencePackage that you want to load
        the sequence from.

   3. Call the SMS_TaskSequencePackage class GetSequence method to get the
        SMS_TaskSequence object.

   4. Make changes to the task sequence and put them back into the package by using
        SetSequence.

Example
The following example method returns the task sequence object (SMS_TaskSequence)
from the supplied package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Function ReadTaskSequence(connection, taskSequencePackage)
      ' Get the parameters object.
      Set packageClass = connection.Get("SMS_TaskSequencePackage")

         Set objInParam = packageClass.Methods_("GetSequence"). _
             inParameters.SpawnInstance_()

         ' Add the input parameters.
          objInParam.Properties_.Item("TaskSequencePackage") =

<!-- p.1026 -->

  taskSequencePackage

      ' Get the sequence.
       Set objOutParams = connection.ExecMethod("SMS_TaskSequencePackage",
  "GetSequence", objInParam)
       Set ReadTaskSequence = objOutParams.TaskSequence
  End Function

  c#

  public IResultObject ReadTaskSequence(
      WqlConnectionManager connection,
      IResultObject taskSequencePackage)
  {
      IResultObject taskSequence = null;
      try
      {
          Dictionary<string, object> parameters = new Dictionary<string,
  object>();
          parameters.Add("TaskSequencePackage", taskSequencePackage);

          IResultObject outParams =
  connection.ExecuteMethod("SMS_TaskSequencePackage", "GetSequence",
  parameters);
          taskSequence = outParams.GetSingleItem("TaskSequence");

              return taskSequence;
       }
       catch (Exception e)
       {
           Console.WriteLine("failed to hydrate: " + e.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter      Type                              Description

 connection     - Managed: WqlConnectionManager   - A valid connection to the SMS Provider.
                - VBScript: SWbemServices

Compiling the Code
This C# example requires:

<!-- p.1027 -->

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create an Operating System Deployment Task Sequence Package
Task sequence overview How to Enumerate the Available Operating System Deployment
Task Sequences

Feedback
Was this page helpful?    Yes    No

<!-- p.1028 -->

Provide product feedback

<!-- p.1029 -->

How to Enumerate the Available
Operating System Deployment Task
Sequences
Article • 10/04/2022

You enumerate the available operating system deployment task sequences, in
Configuration Manager, by querying the available task sequence packages.
Configuration Manager does not maintain instances of the SMS_TaskSequence class for
task sequences, but there is one instance of the SMS_TaskSequencePackage class for
each task sequence.

  ７ Note

  Several properties are lazy and you must get the object instance before you can
  access the properties.

You can also access individual task sequence packages by using the PackageID key
property. For an example, see How to Read a Configuration Manager Object by Using
Managed Code. After you have the task sequence package, you must create an
SMS_TaskSequence object for the task sequence before you can change it. For more
information, see How to Read a Task Sequence From a Task Sequence Package.

To enumerate the available task sequence packages
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Query the SMS Provider for the available instances of SMS_TaskSequencePackage.

   3. Display the required properties for each task sequence package returned by the
      query.

Example
The following example method queries the SMS Provider for the available instance of
SMS_TaskSequencePackage. To retrieve the lazy properties, the example gets the entire
object from the SMS Provider.

<!-- p.1030 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnumerateTaskSequencePackages(connection)

      Set taskSequencePackages= connection.ExecQuery("Select * from
  SMS_TaskSequencePackage")

      For Each package in taskSequencePackages
          WScript.Echo package.Name
          WScript.Echo package.Sequence
      Next
  End Sub

  c#

  public void EnumerateTaskSequencePackages(
      WqlConnectionManager connection)
  {
      IResultObject taskSequencePackages =
  connection.QueryProcessor.ExecuteQuery("select * from
  SMS_TaskSequencePackage");

        foreach (IResultObject ro in taskSequencePackages)
        {
            ro.Get();

          // Get the lazy properties - Sequence property contains the Task
  sequence XML.
          Console.WriteLine(ro["Name"].StringValue);
          Console.WriteLine(ro["Sequence"].StringValue);

              Console.WriteLine();
        }
  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter      Type                              Description

 connection     - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                - VBScript: SWbemServices

Compiling the Code

<!-- p.1031 -->

The C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create an Operating System Deployment Task Sequence Package
How to Read a Task Sequence From a Task Sequence Package
Task sequence overview

Feedback

<!-- p.1032 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1033 -->

How to Add an Operating System
Deployment Task Sequence Action
Article • 10/04/2022

An operating system deployment task sequence action is added to a task sequence, in
Configuration Manager, by creating an instance of an SMS_TaskSequence_Action
derived class and then adding it to the steps of the task sequence.

  ７ Note

  Configuration Manager has a number of built-in actions that you can use. For
  example the command-line action class is
  SMS_TaskSequence_RunCommandLineAction. These classes derive from the
  SMS_TaskSequence_Action class.

SMS_TaskSequenceAction derives from the SMS_TaskSequence_Step class, which is the
base class for both actions and groups. The task sequence stores its steps in an array of
SMS_TaskSequence_Step, thus allowing actions and groups to be stored together.

To add a task sequence action
   1. Set up a connection to the SMS Provider. For more information see, SMS Provider
      fundamentals.

   2. Create a task sequence (SMS_TaskSequence) object. For more information, see
      How to Create an Operating System Deployment Task Sequence.

   3. Create an SMS_TaskSequenceAction derived class instance, for example,
      SMS_TaskSequence_RunCommandLineAction, for the action you want.

   4. Populate the action as appropriate.

   5. Add the action to the task sequences steps. This is stored the SMS_TaskSequence)
      class Steps property.

Example
The following example method creates a command-line action and adds it to the
supplied task sequence.

<!-- p.1034 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddTaskSequenceActionCommandLine(connection, taskSequence, name,
  description)

        Dim steps
        Dim action

      Set action =
  connection.Get("SMS_TaskSequence_RunCommandLineAction").SpawnInstance_

        action.CommandLine = "cmd /c Echo Hello"
        action.Name=name
        action.Description=description
        action.Enabled=True
        action.ContinueOnError=False

          If IsNull(taskSequence.Steps) Then
            steps = Array(action)
            taskSequence.Steps=steps
        Else
            steps= Array(taskSequence.Steps)
            ReDim steps (UBound (taskSequence.Steps)+1)
            taskSequence.Steps(UBound(steps))=action
        End if

  End Sub

  c#

  public IResultObject AddTaskSequenceActionCommandLine(
      WqlConnectionManager connection,
      IResultObject taskSequence,
      string name,
      string description)
  {
      try
      {
          // Create the new step.
          IResultObject ro;

          ro =
  connection.CreateEmbeddedObjectInstance("SMS_TaskSequence_RunCommandLineActi
  on");
          ro["CommandLine"].StringValue = @"cmd /c Echo Hello";

            ro["Name"].StringValue = name;
            ro["Description"].StringValue = description;

<!-- p.1035 -->

              ro["Enabled"].BooleanValue = true;
              ro["ContinueOnError"].BooleanValue = false;

              // Add the step to the task sequence.
              List<IResultObject> array = taskSequence.GetArrayItems("Steps");

              array.Add(ro);

              taskSequence.SetArrayItems("Steps", array);

            return ro;
        }
        catch (SmsException e)
        {
            Console.WriteLine("Failed to add action: " + e.Message);
            throw;
        }
  }

The example method has the following parameters:

                                                                             ﾉ      Expand table

 Parameter        Type                              Description

 connection       - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                  - VBScript: SWbemServices

 taskSequence     - Managed: IResultObject          A valid task sequence.
                  - VBScript: SWbemObject

 Name             - Managed: String                 A name for the new action.
                  - VBScript: String

 Description      - Managed: String                 A description for the action.
                  - VBScript: String

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

<!-- p.1036 -->

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Add a Condition to an Operating System Deployment Task
Sequence Step
How to Connect to an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create an Operating System Deployment Task Sequence Group
How to Delete an Operating System Deployment Task Sequence Action
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1037 -->

How to Delete an Operating System
Deployment Task Sequence Action
Article • 10/04/2022

You delete an operating system deployment task sequence action, in Configuration
Manager, by removing the action from the task sequence steps.

To delete a task sequence action
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Obtain a task sequence (SMS_TaskSequence) object. For more information, see
        How to Create an Operating System Deployment Task Sequence.

   3. Remove the action from the SMS_TaskSequence.Steps array property.

Example
The following example method deletes an action from the task sequence. The action is
identified as an action by checking the Windows Management Instrumentation (WMI)
property __SUPERCLASS to ensure it derives from SMS_TaskSequenceAction.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub RemoveAction (connection, taskSequence, actionName)

         Dim i
         Dim newArray
         Dim actionStep

         If taskSequence.SystemProperties_("__CLASS")<>"SMS_TaskSequence" Then
             wscript.echo "Not a task sequence"
             Exit Sub
         End If

         if IsNull(taskSequence.Steps) Then
             Wscript.Echo "No steps"
             Exit Sub
         End If

<!-- p.1038 -->

     ' Create an array to hold copied steps.
     newArray = Array(taskSequence.Steps)
     ReDim newArray(UBound(taskSequence.Steps))

    ' Copy the steps into the array and remove the matching action.
    i=0
    for each actionStep in taskSequence.Steps
        If actionStep.Name = actionName and _
          actionStep.SystemProperties_("__SUPERCLASS") =
"SMS_TaskSequence_Action" Then
             ReDim preserve newArray(UBound(newArray)-1) ' shrink the Array
        else
           Set newArray(i)=actionStep ' copy it
           i=i+1
        End If
     Next

      ' Assign new array back to the task sequence.
      taskSequence.Steps=newArray

End Sub

c#

public void RemoveAction(
    IResultObject taskSequence,
    string actionName)
{
    try
    {
        // Get a list of steps.
        List<IResultObject> actionSteps =
taskSequence.GetArrayItems("Steps");

        // Find the action to be deleted.
        foreach (IResultObject actionStep in actionSteps)
        {
            if (actionStep["Name"].StringValue == actionName &&
actionStep["__SUPERCLASS"].StringValue == "SMS_TaskSequence_Action")
            {
                // Delete the action.
                actionSteps.Remove(actionStep);
                break;
            }
        }

          // Update the task sequence.
          taskSequence.SetArrayItems("Steps", actionSteps);
     }
     catch (Exception e)
     {
         Console.WriteLine("Failed to remove action: " + e.Message);
         throw;

<!-- p.1039 -->

      }
  }

The example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter      Type                            Description

 Connection     -                               A valid connection to the SMS Provider.
                Managed: WqlConnectionManager
                - VBScript: SWbemServices

 taskSequence   - Managed: IResultObject        The task sequence containing the action to be
                - VBScript: SWbemObject         deleted.

 actionName     - Managed: String               The name of the action to be deleted. This can
                - VBScript: String              be obtained from the
                                                SMS_TaskSequenceAction.Name property.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming

<!-- p.1040 -->

For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Add an Operating System Deployment Task Sequence Action
How to Connect to an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
Task sequence overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback
