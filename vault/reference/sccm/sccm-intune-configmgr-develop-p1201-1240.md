---
title: "Configuration Manager SDK documentation — pages 1201-1240"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1201-1240
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1201-1240
family: sccm
documentKind: "doc"
abstract: "ﾉ Expand table Qualifier Description CommandLineArg A property that should be inserted on the command line Not_Null A value is required for this property. ValueMap Specifies a list of allowed string values. ValueRange Specifies a range of allowed values (int fields). RequiredIfN"
---

# Configuration Manager SDK documentation — pages 1201-1240

<!-- p.1201 -->

                                                                                  ﾉ   Expand table

 Qualifier             Description

 CommandLineArg        A property that should be inserted on the command line

 Not_Null              A value is required for this property.

 ValueMap              Specifies a list of allowed string values.

 ValueRange            Specifies a range of allowed values (int fields).

 RequiredIfNull        A value is required for this property if another property is null.

 TaskSequencePackage   Identifies a property as a package identifier.

 VariableName          Specifies a different name for the property in the task sequence
                       environment.

 AllowedLen            Specifies the minimum and maximum number of characters in a string.

 SuccessCodes          Specifies one or more return code from the executable that indicates
                       success.

Restrictions
     Regular qualifier constraints can be applied to class properties. For example, in the
     example above, the command-line arguments cannot be null . For more
     information, see the Windows Management Instrumentation (WMI) SDK.

     Ensure that property names and qualifiers are synchronized between the MOF file,
     custom action control and client application. The property names must match as
     well as any limitations. For example, if an int property is required, and it must be
     in the range 1 - 512, then the MOF file should have a Not_Null and ValueRange
     qualifier, the custom control should ensure that the property is set and within
     range, and the client application should verify the value before using it.

See Also
About Configuration Manager Custom Actions
How to Create a Configuration Manager Custom Action Control
How to Create a MOF File for a Configuration Manager Custom Action
How to Use Task Sequence Variables in a Running Configuration Manager Task
Sequence
About Configuration Manager Custom Action Client Applications

<!-- p.1202 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1203 -->

About Reporting Configuration
Manager Custom Action Progress
Article • 10/04/2022

While a custom action is running on a Configuration Manager client, it can report
progress information that is used to display a progress indicator.

You use the COM automation interface, IProgressUI::ShowActionProgress, to report
progress information to the task sequence environment and to show a progress
indicator.

IProgressUI::ShowActionProgress is implemented in the COM class, ProgressUI, which is

an out-of-process COM object in TSProgressUI.exe.

ProgressUI in the Task Sequence Environment
Before the task sequence runs, ProgressUI is registered and then, when the task
sequence finishes, it is unregistered. In the source operating system, ProgressUI runs
under the logged-on user credentials. If no user is logged in when the task sequence
runs, the registration for the COM object fails. In the target operating system, and in
Windows PE, ProgressUI runs under the system account.

Calling IProgressUI::ShowActionProgress
In your custom action you must do the following to report the progress of your custom
action and display a progress indicator.

  ７ Note

  Typically, you should report progress information if the action takes more than one
  minute to run.

Determining Whether the Progress Indicator Should Be
Displayed
Using the following logic, you can use environment variables to determine whether the
progress indicator should be displayed.

<!-- p.1204 -->

If you are running in WindowsPE ( _SMSTSInWinPE == "true"), or

If you are running in full operating system post installation
( _SMSTSReturnToGINA =="true"), or

If the task sequence is started from media ( _SMSTSLaunchMode is "CD", "DVD" or "USB"),
or

If the task sequence is running in stand-alone mode ( _SMSTSStandAloneMode =="true"), or

If the show progress UI flag is set ( _SMSTSShowProgressUI == "true"), the progress
indicator should be displayed; otherwise, it should not be displayed.

Creating the COM ProgressUI Object
You create a ProgressUI object by using the same technique that you use with any COM
object. In C++ you use CoCreateInstance . In C# you add a reference to SMS TSE
Progress UI, and in your source code you create an instance of the
ProgressUILib.ProgressUIClass class.

In VBScript, call CreateObject with Microsoft.SMS.TsProgressUI.

For an example of creating a COM object in VBSript and C#, see How to Use Task
Sequence Variables in a Running Configuration Manager Task Sequence.

Getting the Required Environment Variables
Several environment variables contain information that you must pass to the
IProgressUI::ShowActionProgress method. For example, the organization name that is

needed for the pszOrgName parameter is available from the environment variable,
_SMSTSOrgName . For more information, see IProgressUI::ShowActionProgress. For

information about reading task sequence environment variables, see How to Use Task
Sequence Variables in a Running Configuration Manager Task Sequence.

Calling IProgressUI::ShowActionProgress
Call IProgressUI::ShowActionProgress to show the progress indicator by using the
information that is retrieved from the environment variables. To pass the current
percentage progress, you use the parameters uActionExecStep and uActionExecMaxStep .
For example, if you pass the value 2 in uActionExecStep and pass the value 10 in
uActionExecMaxStep , then the percentage completion of the action is 20 percent.

<!-- p.1205 -->

See also
IProgressUI::ShowActionProgress ProgressUI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1206 -->

How to Create a Configuration Manager
Custom Action Control
Article • 10/04/2022

In Configuration Manager, to create a custom action control, you create a Windows
control by using the following two classes:

                                                                               ﾉ   Expand table

 Class                       Description

 SmsOsdEditorPageControl     The custom action control. You derive from this class to implement
                             the custom action control that is displayed in the Task Sequence
                             Editor.

 TaskSequenceOptionControl   The options control for the custom action. You derive from this
                             class to create the custom action options page that is displayed in
                             the Task Sequence Editor.

These procedures show you how to create a Configuration Manager operating system
deployment control assembly by using Visual Studio 2005. When it is loaded into the
Task Sequence Editor, the control displays a property page that contains a text box that
is used to set a user-name action variable for the custom action.

After you have completed these steps, perform the steps in the following topics to
create the custom action managed object format (MOF) file and use the custom action
control.

How to Create a MOF File for a Configuration Manager Custom Action

How to Use a Configuration Manager Custom Action

  ７ Note

  For information about using the custom action as part of a deployment, see About
  Configuration Manager Custom Action Client Applications

The Control Visual Studio Project
The following procedure creates the custom action control project.

<!-- p.1207 -->

Create the control
  1. In Visual Studio 2010, on the File menu, point to New, and then click Project to
    open the New Project dialog box.

  2. From the list of Visual C#, Windows projects, select the Windows Control Library
    project template, and then type ConfigMgrTSAction in the Name box.

  3. Click OK to create the Visual Studio project.

  4. In Solution Explorer, right-click UserControl1.cs, click Rename, and then change
    the name to ConfigMgrTSActionControl.cs .

  5. In Solution Explorer, right-click References, and then click Add Reference.

  6. In the Add Reference dialog box, click the Browse tab, navigate to
    %ProgramFiles%\Microsoft Configuration Manager\AdminUI\bin, and then select
    the following assemblies:

          Adminui.osdcommon.dll

          Adminui.tasksequenceeditor.dll

          Adminui.wqlqueryengine.dll

          Microsoft.configurationmanagement.exe

          Microsoft.configurationmanagement.managementprovider.dll

  7. Click OK to add the assemblies as project references.

  8. In Solution Explorer, right-click ConfigMgrTSActionControl.cs, and then click View
    Code.

  9. Add the following code to include the required namespaces:

       using Microsoft.ConfigurationManagement.AdminConsole;
       using
       Microsoft.ConfigurationManagement.AdminConsole.TaskSequenceEditor;

 10. Change the class ConfigMgrTSActionControl so that it derives from
    SmsOsdEditorPageControl.

 11. In ConfigMgrTSActionControl.cs, add the following new constructor to the
    ConfigMgrTSActionControl class:

<!-- p.1208 -->

       public ConfigMgrTSActionControl(SmsPageData data) : base(data)
       {
           InitializeComponent();
       }

 12. Add the following method to initialize the control:

       public override void InitializePageControl()
       {
          base.InitializePageControl();
       }

Create an Options Control
The following procedure creates the code that declares the options control for the
custom action. This implementation uses the default options control.

To create an options control

     At the end of ConfigMgrTSActionControl.cs add the following new class in the
     ConfigMgrTSAction namespace:

       public class ConfigureTSActionOptions : TaskSequenceOptionControl
       {
           public ConfigureTSActionOptions() : base()
           {
           }
           public ConfigureTSActionOptions(SmsPageData data) : base(data)
           {
           }
       }

Customize the User Interface
The following procedure adds a text box and code to manage action data.

<!-- p.1209 -->

To add the user interface
  1. In Solution Explorer, right-click ConfigMgrTSActionControl.cs, and then click View
    Designer.

  2. In the Toolbox, click the Common Controls tab, and then double-click TextBox. A
    button named textBox1 is added to your control on the User Control Designer.

  3. Double-click the text box. An event handler named textBox1_TextChanged is added
    to the class ConfigMgrTSActionControl. Add the following code to ensure that
    changes are saved to the action's property manager:

      SetDirtyFlag(true);

  4. In the class ConfigMgrTSActionControl, add the following method to write the text
    box value to the User property defined in the custom action MOF. This is called
    when the OK or Apply button is clicked.

      protected override bool ApplyChanges(out Control errorControl, out bool
      showError)
      {
          // You can check the error here and return false.
          if (this.HasError(out errorControl) == true)
          {
              this.ShowMessageBox(
                  this.GetErrorString(),
                  "Error",
                  MessageBoxButtons.OK,
                  MessageBoxIcon.Warning);
              errorControl = null;
              showError = true;
              return false;
          }
          this.PropertyManager["User"].StringValue = textBox1.Text;

           return base.ApplyChanges(out errorControl, out showError);
      }

  5. In the design view for the control, double-click the control to create the method
    ConfigMgrTSActionControl_Load.

  6. Add the following code to the method. This code loads the text box with an
    existing User value. This happens when the task sequence action is edited after it is

<!-- p.1210 -->

     created.

        textBox1.Text = this.PropertyManager["User"].StringValue;

Resource Strings
The following procedure adds the resource strings that are used to display the custom
action name in the Task Sequence Editor.

To add resource strings

   1. In Solution Explorer, on the Project menu, click Properties.

   2. Click the Resources tab. If the resources file does not exist, create it by selecting
     the message that is displayed on the Resources tab.

   3. On the Resource Designer toolbar, point to the resource view drop-down, click the
     arrow, and make sure it is set to Strings (which is the default). A settings grid
     appears, displaying the strings that are maintained by that instance of the
     Resource Designer.

   4. Click the Name column of the last row in the grid, which is marked with an asterisk
     (*).

   5. In the Name column, enter DefaultDisplay_ConfigMgrTSAction as the string name.

   6. In the Value column, enter the string Custom Action. This is the string displayed in
     the list of task sequence actions.

   7. Click the Name column of the last row in the grid, which is marked with an asterisk
     (*).

   8. In the Name column, enter ConfigMgrTSAction as the string name.

   9. In the Value column, enter Custom Action . This is the string that is displayed when
     you add the custom action.

Deploy the Assembly
This procedure builds and copies the assembly that you have created to the
Configuration Manager console assemblies folder. For important information about

<!-- p.1211 -->

deploying Configuration Manager console extensions, see About Configuration
Manager Administrator Console Extension Deployment.

To deploy the assembly

   1. Build the project. Visual Studio creates the assembly as \Visual Studio
     2005\Projects\ConfigMgrControl\ConfigMgrTSAction\bin\Debug\ConfigMgrTSActi
     onControl.dll.

   2. Copy the assembly to the folder %ProgramFiles%\Microsoft Configuration
     Manager\AdminUI\bin.

See Also
About Configuration Manager Console Extension
Configuration Manager Console Extension Deployment
How to Create a MOF File for a Configuration Manager Custom Action
How to Use a Configuration Manager Custom Action

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1212 -->

How to Create a MOF File for a
Configuration Manager Custom Action
Article • 10/04/2022

You define a custom task sequence action, its properties and its user interface controls
by creating a managed object format (MOF) file to describe the class. The MOF file is
then compiled by using Mofcomp.exe.

For more information about custom action MOF files, see About the Configuration
Manager Custom Action MOF File.

The following procedure adds a class declaration for the custom action that you created
in How to Create a Configuration Manager Custom Action Control.

For information about using the custom action, see About Configuration Manager
Custom Action Client Applications.

To create a MOF file for a custom action
   1. In Notepad, create a new file.

   2. Add the following MOF code to the file.

        #pragma autorecover

        #pragma namespace("\\\\.\\root")

        // SMS Root Storage
        instance of __Namespace
        {
            Name = "SMS";
        };

        #pragma namespace("\\\\.\\root\\SMS")

        // Configuration Manager database name for this computer.
        instance of __Namespace
        {
            Name = "site_REPLACESITECODE";
        };

        #pragma namespace("\\\\.\\root\\SMS\\site_REPLACESITECODE")

<!-- p.1213 -->

       #pragma classflags("forceupdate")

       [   CommandLine("smsswd.exe /run:%1 Application.exe /user:%2"),
           VariablePrefix("MyCustomActionPrefix"),
           ActionCategory("My Custom Action Category,7,1"),
           ActionName{"ConfigMgrTSAction.dll",
       "ConfigMgrTSAction.Properties.Resources", "ConfigMgrTSAction"},
           ActionUI{"ConfigMgrTSAction.dll",
       "ConfigMgrTSAction","ConfigMgrTSActionControl",
       "ConfigureTSActionOptions"}
           ]
       class ConfigMgrTSActionControl : SMS_TaskSequence_Action
       {
           [TaskSequencePackage, CommandLineArg(1)]
           string          PackageIDForApplicationExe;

            [Not_Null, CommandLineArg(2)]
            string          User;

            [VariableName("CustomLocation")]
            string          Location;

       };

  3. Replace REPLACESITECODE with the site code for your Configuration Manager site.

  4. Choose a folder, and save the file as type All Files with the name
    CustomAction.mof.

  5. Open a Command Prompt window, navigate to the folder that you saved
    CustomAction.mof in, and enter the following:

       mofcomp CustomAction.mof

  6. Press ENTER to compile the CustomAction.mof.

  7. Confirm that the class has been added in CIM Studio. The class should be listed as
    a child class of SMS_TaskSequence_Action.

  8. Complete How to Use a Configuration Manager Custom Action Control.

See Also
About Configuration Manager Custom Actions
About the Configuration Manager Custom Action MOF File

<!-- p.1214 -->

How to Create a Configuration Manager Custom Action Control
About Configuration Manager Custom Action Client Applications

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1215 -->

How to Use a Configuration Manager
Custom Action Control
Article • 10/04/2022

In Configuration Manager, you use a custom action control by selecting it in the
Configuration Manager console Task Sequence Editor. The custom action control is used
to configure a custom action that you have defined. The custom action becomes a step
in the task sequence you are editing. The following procedure assumes that you have
completed the tasks in the following topics:

How to Create a Configuration Manager Custom Action Control

How to Create a MOF File for a Configuration Manager Custom Action

The following procedure demonstrates the custom action control saving its properties
and reloading them the next time that the action is edited.

To use the custom action as part of the sequence that contains it, you will need to
advertise it using a Configuration Manager task sequence package. For more
information, see About Configuration Manager Custom Action Client Applications

  ７ Note

  Step 1 and step 2 are only necessary if the action control Managed Object Format
  (MOF) file or assembly has been changed.

How to use a custom action control in the task sequence
editor
   1. If the Configuration Manager console is open, close it.

   2. Open the Configuration Manager console.

   3. In the Configuration Manager console, navigate to Software Library / Operating
      Systems.

   4. Right-click Task Sequences, and select Create Task Sequence. The New Task
      Sequence Wizard is displayed.

   5. Select Create a new custom task sequence, and click Next.

<!-- p.1216 -->

   6. In Task sequence name, enter My custom task sequence .

   7. Click Next, confirm the summary information, and click Next again to create the
     task sequence.

   8. Click Close to close the wizard.

   9. In the results pane, right-click the task sequence that you just created and select
     Edit to display the Task Sequence Editor.

 10. In the Task Sequence Editor, select Add, and the categories list is displayed.

 11. Select CustomActionCategory, and your custom action appears as one of the
     possible choices.

 12. Select your custom action (ConfigMgrTSActionControl), and the control is
     displayed.

 13. Add some text to the edit box, and then click OK. The Task Sequence Editor should
     be closed.

 14. Edit the task sequence again and select your custom action.

 15. Note that the text you entered has been retained.

See Also
About Configuration Manager Custom Actions
About Configuration Manager Custom Action Client Applications
How to Create a Configuration Manager Custom Action Control
How to Create a MOF File for a Configuration ManagerCustom Action
How to Delete an Operating System Deployment Task Sequence Action

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1217 -->

Configuration Manager Role-Based
Administration
Article • 10/04/2022

This section provides topics about programmatically managing role-based
administration in Configuration Manager.

  ７ Note

  For more information, see Fundamentals of role-based administration.

About role-based administration
Role-based administration security rights are applied to a domain user or a security
group. In Configuration Manager security rights are replicated to all sites in the
hierarchy. You can use any single site to change the security rights of a user or security
group and it will be automatically replicated to all other sites in that same hierarchy.

Security consists of two basic concepts: security roles and security scopes.

Security Roles
A security role in Configuration Manager grants permissions to the types of objects a
user can interact with, and the actions they can perform with those objects.
Configuration Manager provides multiple built-in security roles.

Security Scopes
A security scope in Configuration Manager establishes security restrictions between the
user and object instances. The permissions the user will have with that object instance
are determined by their assigned security roles.

Administrative Users and Security Groups
Domain users and security groups can be granted access to Configuration Manager. The
permissions set on an administrator consist of a combination of a security role and
scope. A scope is applied to a role that the administrator has. It can never be applied
independently of the role.

<!-- p.1218 -->

See also
Configuration Manager SDK

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1219 -->

How to Check if a User Has Permissions
for an Object
Article • 10/04/2022

In Configuration Manager, you can check for object permissions using the
UserHasPermissions Method in Class SMS_RbacSecuredObject.

To check if a user has permissions for an object
   1. Create a dictionary object to pass object name and permissions to check for to the
       UserHasPermissions Method in Class SMS_RbacSecuredObject.

   2. Call the UserHasPermissions Method in Class SMS_RbacSecuredObject, passing in
       the dictionary object.

   3. The method returns true , if the user has the permissions.

Example
The following example checks to see if the user has the indicated permissions:

  c#

  public static bool UserHasPermissions(ConnectionManagerBase
  connectionManager, string objectName, int permissions, out int
  currentPermissions)
  {
      if (connectionManager == null)
      {
          throw new ArgumentNullException("connectionManager");
      }
      if (string.IsNullOrEmpty(objectName) == true)
      {
          throw new ArgumentException("The parameter 'objectName' cannot be
  null or an empty string", "objectName");
      }
      IResultObject outParams = null;
      try
      {
          Dictionary<string, object> inParams = new Dictionary<string, object>
  ();
          inParams["ObjectPath"] = objectName;
          inParams["Permissions"] = permissions;
          outParams = connectionManager.ExecuteMethod("SMS_RbacSecuredObject",
  "UserHasPermissions", inParams);

<!-- p.1220 -->

          if (outParams != null)
          {
               currentPermissions = outParams["Permissions"].IntegerValue;
               return outParams["ReturnValue"].BooleanValue;
          }
       }
       finally
       {
           if (outParams != null)
           {
               outParams.Dispose();
           }
       }
       currentPermissions = 0;
       return false;
  }

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter            Type                           Description

 connectionManager    - Managed: connectionManager   A valid connection to the SMS Provider.

 objectName           String                         Name of the object.

 permissions          Integer                        The permissions.

 currentPermissions   Integer                        The current permissions.

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System

Assembly
adminui.wqlqueryengine

<!-- p.1221 -->

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
SMS_Admin Server WMI Class
SMS_Role Server WMI Class
SMS_SecuredCategory Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1222 -->

How to Check if a User Has Permissions
for a Resource
Article • 10/04/2022

In Configuration Manager, you can check whether a user has permission for a resource
using the GetCollectionsWithResourcePermissions method in the SMS_RbacSecuredObject
class.

To check if a user has permissions for a resource
   1. Create a dictionary object to pass object name and permissions to check for to the
         GetCollectionsWithResourcePermissions Method in Class SMS_RbacSecuredObject.

   2. Call the GetCollectionsWithResourcePermissions Method in Class
         SMS_RbacSecuredObject, passing in the dictionary object.

   3. The method returns true , if the user has the permissions.

Example
The following example checks to see if the user has resource permissions.

  c#

  public bool CheckUserPermissions(ConnectionManagerBase connectionManager,
  string resourceID)
  {
      bool result = false;
      int iId = 0;
      IResultObject outParams = null;
      if (int.TryParse(resourceID, out iId) == false)
      {
          throw new ArgumentException("Invalid resource ID");
      }
      //ControlAMT permissions.
      int controlAMT = 0x1000000;
      try
      {
          Dictionary<string, object> inParams = new Dictionary<string, object>
  ();
          inParams["Permissions"] = controlAMT;
          inParams["ResourceID"] = iId;
          outParams = connectionManager.ExecuteMethod("SMS_RbacSecuredObject",
  "GetCollectionsWithResourcePermissions", inParams);
          if (outParams != null)

<!-- p.1223 -->

              {
              //If the return value equals 0 and the array is not empty, the
  user has the resource permissions.
              if (outParams["ReturnValue"].IntegerValue == 0 &&
  outParams["CollectionIDs"].StringArrayValue.Length != 0)
              {
                   result = true;
              }
          }
      }
      finally
      {
          if (outParams != null)
          {
                outParams.Dispose();
          }
      }
      return result;
  }

The example method has the following parameters:

                                                                         ﾉ      Expand table

 Parameter        Type                Description

 connection       - Managed:          A valid connection to the SMS Provider.
                  connectionManager

 resourceID       String              Unique ID, supplied by Configuration Manager, for
                                      the resource.

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System

Assembly

<!-- p.1224 -->

adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
SMS_Admin Server WMI Class
SMS_Role Server WMI Class
SMS_SecuredCategory Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1225 -->

How to Enumerate the Administrative
Assignments for a User or Security
Group
Article • 10/04/2022

The administrative assignments for a user or security group are defined by the roles and
security scopes assigned to that user or security group. The Windows Management
Instrumentation (WMI) SMS_Admin class contains all the administrators defined in
Configuration Manager. The security roles for an admin are in the SMS_Admin.Roles
property and the security scopes for an admin are in the SMS_Admin.Categories property.
Both of these properties expose an array of strings which correspond to the identifier of
the role or security scope. Both properties are also marked as lazy and are read-only.

  ） Important

   Lazy properties are never retrieved with the class instance if the class instance was

  loaded from a query. The object must be directly accessed from WMI. Generally the
  WMI provider will supply a Get method that will accept a query path to the object.

To determine whether an administrator references a user account or a security group,
check the SMS_Admin.AccountType property. This property value will be one or zero. Zero
means that the account is a user, and one means the account is a security group.

To read the roles and security scopes of an administrator
   1. Set up a connection to the SMS Provider.

   2. Get an instance to a SMS_Admin WMI class that matches the desired administrator
        by using their identifier.

   3. Read the Roles and Categories properties.

Example
The following example pulls an admin directly from WMI and displays the role and
security scope identifiers:

  vbs

<!-- p.1226 -->

Sub PrintAdminScopesAndRoles(connection, adminId)
    Dim admin
    Dim item
    On Error Resume Next
    set admin = Nothing
    Set admin = connection.Get("SMS_Admin.AdminID=" & CStr(adminId))
    On Error Goto 0
    If (Not admin Is Nothing) Then
        WScript.Echo "Reading Admin: " + admin.LogonName
        WScript.Echo ""
        WScript.Echo " == Roles (" + CStr(UBound(admin.Roles) + 1) + ") =="
        For Each item In admin.Roles
             WScript.Echo " = " + item
        Next
        WScript.Echo ""
        WScript.Echo " == Security Scopes (" + CStr(UBound(admin.Categories)
+ 1) + ") =="
        For Each item In admin.Categories
             WScript.Echo " = " + item
        Next
    Else
        WScript.Echo "Admin with id " + CStr(adminId) + " not found."
    End If
End Sub

c#

public void PrintAdminScopesAndRoles(WqlConnectionManager connection, int
adminId)
{
    IResultObject admin = null;
    try
    {
        admin = connection.GetInstance("SMS_Admin.AdminID=" +
adminId.ToString());
    }
    catch (Exception) { }
    if (admin != null)
    {
        Console.WriteLine("Reading Admin: " +
admin["LogonName"].StringValue);
        Console.WriteLine("");
        Console.WriteLine(String.Format("== Roles ({0}) ==",
admin["Roles"].StringArrayValue.Length.ToString()));
        foreach (var item in admin["Roles"].StringArrayValue)
Console.WriteLine("= " + item);
            Console.WriteLine("");
            Console.WriteLine(String.Format("== Security Scopes ({0}) ==",
admin["Categories"].StringArrayValue.Length.ToString()));
        foreach (var item in admin["Categories"].StringArrayValue)
            Console.WriteLine("= " + item);

<!-- p.1227 -->

      }
      else
          Console.WriteLine("Admin with id " + adminId.ToString() + " not
  found.");
  }

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter    Type                              Description

 connection   - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
              - VBScript: SWbemServices

 adminId      Integer                           The admin identifier.

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also

<!-- p.1228 -->

SMS_Admin Server WMI Class
SMS_Role Server WMI Class
SMS_SecuredCategory Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1229 -->

How to Create a New Administrator
Article • 10/04/2022

The administrative assignments for a user or security group are defined by the roles and
security scopes assigned to that user or security group. The Windows Management
Instrumentation (WMI) SMS_Admin class contains all the administrators defined in
Configuration Manager. The security roles for an admin are in the SMS_Admin.Roles
property and the security scopes for an admin are in the SMS_Admin.Categories property.
Both of these properties expose an array of strings which correspond to the identifier of
the role or security scope. Both properties are also marked as lazy and are read-only.

  ） Important

   Lazy properties are never retrieved with the class instance if the class instance was

  loaded from a query. The object must be directly accessed from WMI. Generally the
  WMI provider will supply a Get method that will accept a query path to the object.

To create a new administrator
   1. Set up a connection to the SMS Provider.

   2. Get an instance to a SMS_Admin WMI class that matches the desired administrator
       by using their identifier.

   3. Add permissions, including category, role and secured scope.

         ） Important

         Category, role and secured scope are all required values.

   4. Save the new administrator instance.

Example
The following example pulls an admin directly from WMI and displays the role and
security scope identifiers:

  c#

<!-- p.1230 -->

  public void CreateSMSAdmin(WqlConnectionManager connection, string
  distinguishedName, string categoryID, string roleID, int categoryTypeID)
   {
       // Create a new administrator instance.
       IResultObject newSMSAdmin = connection.CreateInstance("SMS_Admin");

       // Set the required properties.
       // One set of example values in comments.
      newSMSAdmin.Properties["DistinguishedName"].StringValue =
  distinguishedName; // "CN=<USERACCOUNT>,CN=Users,DC=<DOMAINNAME>,DC=COM"

      // Create new permissions list.
      List<IResultObject> permissionsObjectList = new List<IResultObject>();

      // Add permissions.
      IResultObject permissionObject =
  connection.CreateEmbeddedObjectInstance("SMS_APermission");
      permissionObject["CategoryID"].StringValue = categoryID;                      //
  "SMS00004" (All Users and User Groups)
      permissionObject["RoleID"].StringValue = roleID;                              //
  "SMS000GR" (EndPoint Protection Manager)
      permissionObject["CategoryTypeID"].IntegerValue = categoryTypeID;             //
  1          (Collection)
      permissionsObjectList.Add(permissionObject);

      // Add secured scope.
      IResultObject permissionObject2 =
  connection.CreateEmbeddedObjectInstance("SMS_APermission");
      permissionObject2["CategoryID"].StringValue = "SMS00UNA";                      //
  "SMS00UNA" (Default)
      permissionObject2["RoleID"].StringValue = "SMS000GR";                          //
  "SMS000GR" (EndPoint Protection Manager)
      permissionObject2["CategoryTypeID"].IntegerValue = 29;                         //
  29         (Secured Scope)
      permissionsObjectList.Add(permissionObject2);

      // Save the permissions list to the new administrator instance.
       newSMSAdmin.SetArrayItems("Permissions", permissionsObjectList);

      // Save the new administrator instance.
       newSMSAdmin.Put();
  }

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter        Type                    Description

 connection       - Managed:              A valid connection to the SMS Provider.
                   WqlConnectionManager

<!-- p.1231 -->

 Parameter           Type                 Description

 distinguishedName   - Managed: String    Like "CN=John
                                          Doe,OU=UserAccounts,DC=contoso,DC=com"

 categoryID          - Managed: String    The RBA secured categories associated with this
                                          account.

 CategoryTypeID      - Managed: Integer   The type of the category (collection or secured
                                          scope).

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
SMS_Admin Server WMI Class
SMS_Role Server WMI Class
SMS_SecuredCategory Server WMI Class

<!-- p.1232 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1233 -->

How to Create a New Security Role
Article • 10/04/2022

The administrative assignments for a user or security group are defined by the roles and
security scopes assigned to that user or security group. The Windows Management
Instrumentation (WMI) SMS_Admin class contains all the administrators defined in
Configuration Manager. The security roles for an admin are in the SMS_Admin.Roles
property and the security scopes for an admin are in the SMS_Admin.Categories property.
Both of these properties expose an array of strings which correspond to the identifier of
the role or security scope. Both properties are also marked as lazy and are read-only.

  ） Important

   Lazy properties are never retrieved with the class instance if the class instance was

  loaded from a query. The object must be directly accessed from WMI. Generally the
  WMI provider will supply a Get method that will accept a query path to the object.

To create a new Security Role
   1. Set up a connection to the SMS Provider.

   2. Create an instance of the SMS_Role WMI class.

   3. Set the required properties, including a new role name and the original security
       role to copy.

   4. Get an instance of the original SMS_Role WMI class.

   5. Copy the role permissions from the original security role to the new security role.
       This is similar to the Admin Console functionality when creating a new security role
       and not strictly required to create the security role.

   6. Save the new security role.

Example
The following example creates a new security role:

  c#

<!-- p.1234 -->

  public void CreateRole(WqlConnectionManager connection, string roleName,
  string originalRoleID)
  {
      // Create a new security role instance.
      IResultObject newRole = connection.CreateInstance("SMS_Role");

      // Set the required properties.
      // Note: RoleDescription is not required, but convenient.
      newRole.Properties["RoleName"].StringValue = roleName;
      newRole.Properties["CopiedFromID"].StringValue = originalRoleID;
      newRole.Properties["RoleDescription"].StringValue = roleName + "
  Description";

      // Get the original role instance.
      IResultObject originalRole = connection.GetInstance(@"SMS_Role.RoleID='"
  + originalRoleID + "'");

      // Copy the original role permissions to the new security role.
      newRole.SetArrayItems("Operations",
  originalRole.GetArrayItems("Operations"));

      // Save the new security role.
      newRole.Put();
  }

The example method has the following parameters:

                                                                              ﾉ    Expand table

 Parameter        Type                              Description

 connection       - Managed: WqlConnectionManager   A valid connection to the SMS Provider.

 roleName         - Managed: String                 A name for the new role.

 originalRoleID   - Managed: String                 The identifier of the original security role.

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

<!-- p.1235 -->

System

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
SMS_Admin Server WMI Class
SMS_Role Server WMI Class
SMS_SecuredCategory Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1236 -->

How to Create a New Security Scope
Article • 10/04/2022

Creating a security scope in Configuration Manager is simple. All security scopes are
defined by the SMS_SecuredCategory Windows Management Instrumentation (WMI)
class. Only two properties are required when you are creating a new security scope, the
name and description.

To create a new security scope
   1. Set up a connection to the SMS Provider.

   2. Create an instance of the SMS_SecuredCategory WMI class

   3. Set the CategoryName and CategoryDescription properties.

   4. Save the security scope.

Example
The following example creates a new security scope:

  vbs

  Sub CreateSecurityScope(connection, scopeName, scopeDescription)

        Dim scope

        ' Create a new security scope instance.
        Set scope = connection.Get("SMS_SecuredCategory").SpawnInstance_()

      ' Set the required properties.
      scope.CategoryName = scopeName        scope.CategoryDescription =
  scopeDescription

        ' Save the security scope.
        scope.Put_

  End Sub

  c#

  public void CreateSecurityScope(WqlConnectionManager connection, string
  scopeName, string scopeDescription)
  {

<!-- p.1237 -->

      // Create a new security scope instance.
      IResultObject secScope =
  connection.CreateInstance("SMS_SecuredCategory");

      // Set the required properties.
      secScope.Properties["CategoryName"].StringValue = scopeName;
      secScope.Properties["CategoryDescription"].StringValue =
  scopeDescription;

      // Save the security scope.
      secScope.Put();
  }

The example method has the following parameters:

                                                                            ﾉ    Expand table

 Parameter          Type                              Description

 connection         - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                    - VBScript: SWbemServices

 scopeName          String                            The name of security scope.

 scopeDescription   String                            The description of security scope.

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.1238 -->

See Also
How to Delete a Security Scope
How to Associate an Object with a Security Scope
How to Remove an Object Association with a Security Scope
SMS_SecuredCategory Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1239 -->

How to Delete a Security Scope
Article • 10/04/2022

The following example shows how to delete a security scope in Configuration Manager
by using the SMS_SecuredCategory class.

To delete a security scope
   1. Set up a connection to the SMS Provider.

   2. Load the existing security scope by using the SMS_SecuredCategory WMI class

   3. Delete the security scope by using the delete method.

Example
The following example deletes a security scope by identifier:

  vbs

  Sub DeleteSecurityScope(connection, scopeId)
      Dim scope
      ' Get the existing scope by identifier.
      Set scope = connection.Get("SMS_SecuredCategory.CategoryID='" & scopeId
  & "'")

      ' Make sure we are allowed to delete this scope.
      If (scope.IsBuiltIn) Then
          Err.Raise 1, "DeleteSecurityScope", "Deleting a built-in security
  scope is not allowed."
      Else
          scope.Delete_
      End If
  End Sub

  c#

  public void DeleteSecurityScope(WqlConnectionManager connection, string
  scopeId)
  {
      // Get the existing scope by identifier.
      IResultObject secScope =
  connection.GetInstance("SMS_SecuredCategory.CategoryID='" + scopeId + "'");

        // Make sure we are allowed to delete this scope.
        if (secScope.Properties["IsBuiltIn"].BooleanValue == true)

<!-- p.1240 -->

          throw new System.Exception("Deleting a built-in security scope is
  not allowed.");
      else
          secScope.Delete();
  }

The example method has the following parameters:

                                                                             ﾉ    Expand table

 Parameter    Type                              Description

 connection   - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
              - VBScript: SWbemServices

 scopeId      String                            The identifier of the security scope to delete.

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
How to Create a New Security Scope
How to Associate an Object with a Security Scope
