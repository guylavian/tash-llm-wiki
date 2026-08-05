---
title: "Configuration Manager SDK documentation — pages 1241-1280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1241-1280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1241-1280
family: sccm
documentKind: "doc"
abstract: "How to Remove an Object Association with a Security Scope SMS_SecuredCategory Server WMI Class Feedback Was this page helpful?  Yes  No Provide product feedback How to Associate an Object with a Security Scope Article • 10/04/2022  Tip To assign multiple objects to a scope, u"
---

# Configuration Manager SDK documentation — pages 1241-1280

<!-- p.1241 -->

How to Remove an Object Association with a Security Scope
SMS_SecuredCategory Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1242 -->

How to Associate an Object with a
Security Scope
Article • 10/04/2022

   Tip

  To assign multiple objects to a scope, use the AddMemberships Method in Class
  SMS_SecuredCategoryMembership.

To assign an object a security scope
   1. Set up a connection to the SMS Provider.

   2. Determine the object's key property identifier.

   3. Determine the object type identifier.

   4. Create a new instance of the SMS_SecuredCategoryMembership WMI class, setting the
        scope identifier, object key, and object type values.

   5. Save the SMS_SecuredCategoryMembership object instance.

Example
The following code example assigns a scope identifier to a package:

  vbs

  Sub AddObjectScope(connection, scopeId, objectKey, objectTypeId)

         Dim assignment

      ' Create a new instance of the scope assignment.
      Set assignment =
  connection.Get("SMS_SecuredCategoryMembership").SpawnInstance_()

         ' Configure the assignment
         assignment.CategoryID = scopeId
         assignment.ObjectKey = objectKey
         assignment.ObjectTypeID = objectTypeId

         ' Commit the assignment
         assignment.Put_

<!-- p.1243 -->

  End Sub

  c#

  public void AddObjectScope(WqlConnectionManager connection, string scopeId,
  string objectKey, int objectTypeId)
  {
      // Create a new instance of the scope assignment.
      IResultObject assignment =
  connection.CreateInstance("SMS_SecuredCategoryMembership");

       // Configure the assignment
       assignment.Properties["CategoryID"].StringValue = scopeId;
       assignment.Properties["ObjectKey"].StringValue = objectKey;
       assignment.Properties["ObjectTypeID"].IntegerValue = objectTypeId;

       // Commit the assignment
       assignment.Put();
  }

The example method has the following parameters:

                                                                              ﾉ     Expand table

 Parameter      Type                        Description

 connection     - Managed:                  A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript: SWbemServices

 scopeId        String                      The identifier of the security scope.

 objectKey      String                      The key property value of the object to assign a
                                            scope to.

 objectTypeId   Integer                     The type identifier of the object referenced in the
                                            objectKey parameter.

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.1244 -->

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
SMS_SecuredCategoryMembership Server WMI Class
How to Create a New Security Scope
How to Delete a Security Scope
How to Remove an Object Association with a Security Scope
SMS_SecuredCategory Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1245 -->

How to Remove an Object Association
with a Security Scope
Article • 10/04/2022

Removing a security scope from an object instance is as simple as deleting the Windows
Management Instrumentation (WMI) SMS_SecuredCategoryMembership class instance.
However, object instances must have at least one security scope associated with them.
The last object instance can never be removed. Every object is created with the Default
security scope, and if all other security scopes are to be removed from an object
instance, the Default should be added to it before removal.

  ） Important

  You must have administrative rights to the scope and the object you are removing
  it from. If you do not have the correct permissions, removing a scope from that
  object instance will fail. Removing the last scope from an object will be unsuccessful
  and will fail.

   Tip

  To remove multiple objects to a scope, use the RemoveMemberships Method in
  Class SMS_SecuredCategoryMembership.

To remove a security scope from an object
   1. Set up a connection to the SMS Provider.

   2. Determine the object's key property identifier.

   3. Determine the object type identifier.

   4. Determine the scope identifier.

   5. Find an instance of the SMS_SecuredCategoryMembership WMI class that matches the
      .

   6. Delete the instance.

<!-- p.1246 -->

Example
The following code example removes a scope identifier from a package:

  vbs

  Sub RemoveObjectScope(connection, scopeId, objectKey, objectTypeId)

        Dim assignment

      ' Find the existing scope assignement that matches our parameters.
      Set assignment =
  connection.Get("SMS_SecuredCategoryMembership.CategoryID='" & scopeId &
  "',ObjectKey='" & objectKey & "',ObjectTypeId=" & objectTypeId)

      If (assignment Is Nothing) Then
          Err.Raise 1, "RemoveObjectScope", "Unable to find matching scope,
  object, and object type."
      Else
          assignment.Delete_
      End If
  End Sub

  c#

  public void RemoveObjectScope(WqlConnectionManager connection, string
  scopeId, string objectKey, int objectTypeId)
  {
      // Find the existing scope assignement that matches our parameters.
       IResultObject assignment =
  connection.GetInstance("SMS_SecuredCategoryMembership.CategoryID='" +
  scopeId + "',ObjectKey='" + objectKey + "',ObjectTypeID=" +
  objectTypeId.ToString());

     // Make sure we found the scope.
      if (assignment == null)
          throw new System.Exception("Unable to find matching scope, object,
  and object type.");
      else
          assignment.Delete();
  }

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter     Type                      Description

 connection    - Managed:                A valid connection to the SMS Provider.
               WqlConnectionManager

<!-- p.1247 -->

 Parameter      Type                        Description

                - VBScript: SWbemServices

 scopeId        String                      The identifier of the security scope.

 objectKey      String                      The key property value of the object.

 objectTypeId   Integer                     The type identifier of the object referenced in the
                                            objectKey parameter.

Compiling the Code
The C# example requires:

Namespaces
Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

See Also
SMS_SecuredCategoryMembership Server WMI Class
How to Create a New Security Scope
How to Delete a Security Scope
How to Associate an Object with a Security Scope
SMS_SecuredCategory Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1248 -->

How to Enable and Disable Remote
Tools
Article • 10/10/2022

You enable or disable the Remote Tools Client Agent, in Configuration Manager, by
modifying the site control file settings.

To enable or disable the Remote Tools Client Agent
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Remote Tools Client Agent section of the site control file
        by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example method enables or disables the Remote Tools Client Agent by
using the SMS_SCI_ClientComp class to connect to the site control file and change
properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnableDisableRemoteControlClientAgent(swbemServices,   _
                                            swbemContext,    _
                                            siteCode,     _
                                            enableDisableClientAgent)

      ' Load site control file and get client component section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext
      Set objSWbemInst =
  swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
  Component',Sitecode='" & siteCode & "',ItemName='Remote Control'", ,
  swbemContext)

         ' Display client agent settings before change.

<!-- p.1249 -->

     Wscript.Echo " "
     Wscript.Echo "Properties - Before Change"
     Wscript.Echo "---------------------------"
     Wscript.Echo objSWbemInst.ClientComponentName
     Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

    ' Set the client agent by setting the Flags value to 0 or 1 using the
enableDisableClientAgent variable.
    objSWbemInst.Flags = enableDisableClientAgent

    ' Save the new client agent settings.
    objSWbemInst.Put_ , swbemContext
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Commit", , , swbemContext

    ' Refresh the in-memory copy of the site control file and get the client
component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteCode & "',ItemName='Remote Control'", ,
swbemContext)

     ' Display the client agent settings after the change.
     Wscript.Echo " "
     Wscript.Echo "Properties - After Change"
     Wscript.Echo "---------------------------"
     Wscript.Echo objSWbemInst.ClientComponentName
     Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

End Sub

c#

public void EnableDisableRemoteControlClientAgent(WqlConnectionManager
connection,
                                                  string siteCode,
                                                  string
enableDisableClientAgent)
{
    try
    {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Remote Control'");

        // Display Remote Control client agent settings before changing the
properties.
        Console.WriteLine();
        Console.WriteLine("Properties - Before Change");

<!-- p.1250 -->

              Console.WriteLine("---------------------------");

  Console.WriteLine(siteDefinition["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");

          // Set Remote Control client agent by setting "Flags" value to 0 or
  1 by using the enableDisableClientAgent variable.
          siteDefinition["Flags"].StringValue = enableDisableClientAgent;

              // Save the settings.
              siteDefinition.Put();

          // Verify the change by reconnecting and getting the value again.
          IResultObject siteDefinition2 =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" + siteCode + "',ItemName='Remote Control'");

          // Display Remote Control client agent settings after changing the
  properties.
          Console.WriteLine();
          Console.WriteLine("Properties - After Change");
          Console.WriteLine("--------------------------");

  Console.WriteLine(siteDefinition2["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition2["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
          throw;
      }

  }

The example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter                 Type                    Description

 Parameter                 Type                    Description

 connection                - Managed:              A valid connection to the SMS Provider.
                            WqlConnectionManager
 swbemServices             - VBScript:
                           SWbemServices

<!-- p.1251 -->

 Parameter                  Type                       Description

 swbemContext               - VBScript: SWbemContext   A valid context object. For more
                                                       information, see How to Add a
                                                       Configuration Manager Context Qualifier
                                                       by Using WMI.

 siteCode                   - Managed: String          The site code.
                            - VBScript: String

 enableDisableClientAgent   - Managed: String          Determines whether the Remote Tools
                            - VBScript: String         client agent is enabled or disabled.

                                                       - 0 - Disabled
                                                       - 1 - Enabled

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security

<!-- p.1252 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1253 -->

How to Configure Remote Tools
Settings
Article • 10/10/2022

In Configuration Manager, you set the Remote Tools Client Agent settings by modifying
the necessary site control file settings.

To configure Remote Tools settings
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Remote Tools Client Agent section of the site control file
        by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example sets the Remote Tools Client Agent settings by using the
SMS_SCI_ClientComp class to connect to the site control file and change properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureRemoteControlClientAgentSettings(swbemServices,            _
                                                swbemContext,             _
                                                siteCode,                 _
                                                enableDisableClientAgent, _
                                                newPermissionRequired,    _
                                                newVisibleSignal,         _
                                                newAudibleSignal)

      ' Load the site control file and get the remote tools client agent
  section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_ClientComp " & _
         "WHERE ClientComponentName = 'Remote Control' " & _
         "AND SiteCode = '" & siteCode & "'"

<!-- p.1254 -->

    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

        ' Set the client agent by setting the Flags value to 0 or 1 using
the enableDisableClientAgent variable.
        wscript.echo " "
        wscript.echo "Remote Control Agent"
        wscript.echo "Current value " & SCIComponent.Flags

       ' Modify the value.
       SCIComponent.Flags = enableDisableClientAgent
       wscript.echo "New value " & enableDisableClientAgent

       ' Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

              ' Setting: Permission Required
              If vProperty.PropertyName = "Permission Required" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value

                  'Modify the value.
                  vProperty.Value = newPermissionRequired
                  wscript.echo "New value " & newPermissionRequired
              End If

              ' Setting: Visible Signal
              If vProperty.PropertyName = "Visible Signal" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value

                  ' Modify the value.
                  vProperty.Value = newVisibleSignal
                  wscript.echo "New value " & newVisibleSignal
              End If

              ' Setting: Audible Signal
              If vProperty.PropertyName = "Audible Signal" Then
                  wscript.echo " "
                  wscript.echo vProperty.PropertyName
                  wscript.echo "Current value " & vProperty.Value

                  ' Modify the value.
                  vProperty.Value = newAudibleSignal
                  wscript.echo "New value " & newAudibleSignal
              End If

       Next

<!-- p.1255 -->

                ' Update the component in your copy of the site control file.
Get the path
                ' to the updated object, which could be used later to retrieve
the instance.
                Set SCICompPath = SCIComponent.Put_(wbemChangeFlagUpdateOnly,
swbemContext)
    Next

    'Commit the change to the actual site control file.
    Set InParams =
swbemServices.Get("SMS_SiteControlFile").Methods_("CommitSCF").InParameters.
SpawnInstance_
    InParams.SiteCode = siteCode
    swbemServices.ExecMethod "SMS_SiteControlFile", "CommitSCF", InParams, ,
swbemContext

End Sub

c#

public void ConfigureRemoteControlClientAgentSettings(WqlConnectionManager
connection,
                                                      string siteCode,
                                                      string
enableDisableRemoteControlClientAgent,
                                                      string
newPermissionRequired,
                                                      string
newVisibleSignal,
                                                      string
newAudibleSignal)
{
    try
    {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Remote Control'");

        // Setting: Enable Remote Control Client Agent
        // Set Remote Control client agent by setting flags value to    0 or 1
using the EnableDisableRemoteControlClientAgent variable.
        Console.WriteLine();
        Console.WriteLine("Remote Control Client Agent");
        Console.WriteLine("Current value: " +
siteDefinition["Flags"].StringValue);

        // Change value using the enableDisableRemoteControlClientAgent
value passed in.
        siteDefinition["Flags"].StringValue =
enableDisableRemoteControlClientAgent;
        Console.WriteLine("New value    : " +

<!-- p.1256 -->

enableDisableRemoteControlClientAgent);

        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {

            // Create temporary working copy of embedded properties.
            Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

             // Setting: Permission Required.
             if (kvp.Value.PropertyList["PropertyName"] == "Permission
Required")
             {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value"].StringValue);

                 // Change value using the newPermissionRequired value passed
in.
                embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value"].StringValue = newPermissionRequired;
                Console.WriteLine("New value    : " +
newPermissionRequired);
            }

            // Setting: Visible Signal.
            if (kvp.Value.PropertyList["PropertyName"] == "Visible Signal")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value"].StringValue);

                // Change value using the newScanSchedule value passed in.
                embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value"].StringValue = newVisibleSignal;
                Console.WriteLine("New value    : " + newVisibleSignal);
            }

            // Setting: Audible Signal.
            if (kvp.Value.PropertyList["PropertyName"] == "Audible Signal")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value"].StringValue);

                // Change value using the newAudibleSignal value passed in.
                embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value"].StringValue = newAudibleSignal;

<!-- p.1257 -->

                      Console.WriteLine("New value        : " + newAudibleSignal);
                  }

                  // Store the settings that have changed.
                  siteDefinition.EmbeddedProperties = embeddedProperties;
              }

              // Save the settings.
              siteDefinition.Put();

       }
       catch (SmsException ex)
       {
           Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                           ﾉ      Expand table

 Parameter                               Type                    Description

 connection                              - Managed:              A valid connection to the
                                         WqlConnectionManager    SMS Provider.
 swbemServices                           - VBScript:
                                         SWbemServices

 swbemContext                            - VBScript:             A valid context object. For
                                         SWbemContext            more information, see How
                                                                 to Add a Configuration
                                                                 Manager Context Qualifier
                                                                 by Using WMI.

 siteCode                                - Managed: String       The site code.
                                         - VBScript: String

 - Managed:                              - Managed: String       Determines whether the
 enableDisableRemoteControlClientAgent   - VBScript: String      Remote Tools Client Agent
 - VBScript: enableDisableClientAgent                            is enabled or disabled.

                                                                 0 - disabled

                                                                 1 - enabled

 newPermissionRequired                   - Managed: String       Determines whether
                                         - VBScript: String      permission is required to
                                                                 remote control.

<!-- p.1258 -->

 Parameter                         Type                 Description

                                                        0 - not required

                                                        1 - required

 newVisibleSignal                  - Managed: String    Determines whether the
                                   - VBScript: String   visible signal is enabled or
                                                        disabled.

                                                        0 - disabled

                                                        1 - enabled

 newAudibleSignal                  - Managed: String    Determines whether the
                                   - VBScript: String   audible signal is enabled or
                                                        disabled.

                                                        0 - disabled

                                                        1 - enabled

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming

<!-- p.1259 -->

For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1260 -->

Software Distribution Overview
Article • 10/04/2022

With this release, Configuration Manager expands the abilities of system administrators
to centrally manage computers effectively. Building on the capabilities provided by
Configuration Manager 2007, Configuration Manager provides a refined tool set for
software distribution.

Distributing Software
The software distribution process advertises packages, which contain programs, to
members of a collection. The client then installs the software from specified distribution
points. The order in which you create the components that make up the software
distribution process is important.

   1. Create an instance of SMS_Package .

   2. Create an instance of SMS_Program .

   3. If an existing collection does not identify the users to whom you want to distribute
      the software, create a new collection by creating an instance of SMS_Collection .

   4. If the package contains source files, define a distribution point for the package by
      creating an instance of SMS_DistributionPoint .

   5. Create an instance of SMS_Advertisement .

      The following topics show how to create the software distribution components:

      How to Create a Package

      How to Create a Program

      How to Assign a Package to a Distribution Point

      How to Create an Advertisement

See Also
Software distribution overview

<!-- p.1261 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1262 -->

About Package Definition Files
Article • 10/04/2022

Package definition files are predefined scripts that you can use to help automate
package creation with Configuration Manager. These are files that contain the package
and program information that is needed to distribute a package to clients, with the
exception of the source file location.

Package definition files often come with an application's source files or are available
from the application's developer. Configuration Manager also has a selection of package
definition files that are automatically imported and available in the Create Package from
Definition Wizard.

For more information about the format of these files, see the Package Definition File
Format section later in this topic.

Package Definition File Format
Each package definition file is an ASCII text file following a standard .ini file format and
containing the following sections:

[PDF]
This section identifies the file as a package definition file and contains the following
information:

Version
Specifies the version of the package definition file format that is used by the file,
corresponding to the version of System Management Server (SMS) or Configuration
Manager for which they were written. This entry is required.

[Package Definition]
This section of the package definition file specifies the overall properties of the package
and provides the following information:

Name
The name of the package, up to 50 characters. This entry is required.

Version
The version of the package, up to 32 characters. This entry is optional.

<!-- p.1263 -->

Icon
Specifies the file that contains the icon to use for this package. If it is used, this icon
replaces the default package icon in the Configuration Manager console. This entry is
optional.

Publisher
The publisher of the package, up to 32 characters. This entry is required.

Language
The language version of the package, up to 32 characters. This entry is required.

Comment
An optional comment about the package, up to 127 characters.

ContainsNoFiles
This entry indicates whether or not a source is associated with the package.

Programs
Specifies the programs that are defined for this package. Each program name
corresponds to a [Program] section in this package definition file. This entry is required.

For example:

Programs=Typical, Custom, Uninstall

MIFFileName
The name of the Management Information Format (MIF) file that contains the package
status, up to 50 characters.

MIFName
The name of the package (for MIF matching), up to 50 characters.

MIFVersion
The version number of the package (for MIF matching), up to 32 characters.

MIFPublisher
The software publisher of the package (for MIF matching), up to 32 characters.

[Program]
For each program specified in the Programs entry in the [Package Definition] section,
the package definition file must include a section that defines that program. The file
must contain a [Program] section for all programs that are contained within that
package.

<!-- p.1264 -->

Name
The name of the program, up to 50 characters. This entry must be unique within a
package and is used when defining advertisements. On client computers, the name of
the program is shown in Run Advertised Programs in Control Panel. This entry is
required.

Icon
Specifies the file that contains the icon to use for this program. If it is used, this icon
replaces the default program icon in the Configuration Manager console and is
displayed on client computers when the program is advertised. This entry is optional.

Comment
An optional comment about the program, up to 127 characters.

CommandLine
Specifies the command line for the program, up to 127 characters. The command is
relative to the package source folder, if there is package source. This entry is required.

StartIn
The working folder for the program, up to 127 characters. This entry can be an absolute
path on the client computer or a path relative to the package source folder. This entry is
required.

Run
Specifies the program mode in which the program runs. You can specify Minimized,
Maximized, or Hidden. If this entry is not included, the program runs in normal mode.

AfterRunning
Specifies any special action that occurs after the program is completed successfully.
Available options are SMSRestart, ProgramRestart, or SMSLogoff. If this entry is not
included, the program does not run a special action.

EstimatedDiskSpace
Specifies the amount of disk space that the software program requires to run on the
computer. This can be specified as Unknown (the default setting) or as a whole number
that is greater than or equal to zero. If a value is specified, units for the value must also
be specified.

For example:

EstimatedDiskSpace=38MB

EstimatedRunTime
Specifies the estimated time (in minutes) that the program is expected to run on the

<!-- p.1265 -->

client computer. This can be specified as Unknown (the default setting) or as a whole
number greater than zero.

For example:

EstimatedRunTime=25

SupportedClients
Specifies the processors and operating systems on which this program runs. Each
platform must be separated by a comma. If this entry is not included with the package
definition file, supported platform checking is disabled for this program.

SupportedClientMinVersionX, SupportedClientMaxVersionX
Specifies the beginning and ending range for version numbers for the operating
systems specified in the SupportedClients entry.

For example:

SupportedClients=Win NT (I386),Win NT (IA64),Win NT (x64)

Win NT (I386) MinVersion1=5.00.2195.4

Win NT (I386) MaxVersion1=5.00.2195.4

Win NT (I386) MinVersion2=5.10.2600.2

Win NT (I386) MaxVersion2=5.10.2600.2

Win NT (I386) MinVersion3=5.20.0000.0

Win NT (I386) MaxVersion3=5.20.9999.9999

Win NT (I386) MinVersion4=5.20.3790.0

Win NT (I386) MaxVersion4=5.20.3790.2

Win NT (I386) MinVersion5=6.00.0000.0

Win NT (I386) MaxVersion5=6.00.9999.9999

Win NT (IA64) MinVersion1=5.20.0000.0

Win NT (IA64) MaxVersion1=5.20.9999.9999

Win NT (x64) MinVersion1=5.20.0000.0

Win NT (x64) MaxVersion1=5.20.9999.9999

<!-- p.1266 -->

Win NT (x64) MinVersion2=5.20.3790.0

Win NT (x64) MaxVersion2=5.20.9999.9999

Win NT (x64) MinVersion3=5.20.3790.0

Win NT (x64) MaxVersion3=5.20.3790.2

Win NT (x64) MinVersion4=6.00.0000.0

AdditionalProgramRequirements
Optional text that can include any other information or requirements for client
computers, up to 127 characters.

CanRunWhen
Specifies the user status that the program requires to run on the client computer.
Available values are UserLoggedOn, NoUserLoggedOn, or AnyUserStatus. The default
value is UserLoggedOn.

UserInputRequired
Specifies whether the program requires interaction with the user to complete running.
Available values are True or False . The default value is True . This entry is set to False
if CanRunWhen is not set to UserLoggedOn.

AdminRightsRequired
Specifies whether the program requires administrative credentials on the computer to
run. Available values are True or False . The default value is False . This entry is set to
True if CanRunWhen is not set to UserLoggedOn.

DriveLetterConnection
Specifies whether the program requires a drive letter connection to the package files on
the distribution point. You can specify True or False . The default value is False , which
allows the program to use a Universal Naming Convention (UNC) connection. When this
value is set to True , the next available drive letter is used (starting with Z and
proceeding backward).

SpecifyDrive
Specifies a specific drive letter that the program requires to connect to the package files
on the distribution point. Using this entry forces the use of the specified drive letter for
client connections to distribution points. This entry is optional.

ReconnectDriveAtLogon
Specifies whether the computer reconnects to the distribution point when the user logs
on. Available values are True or False . The default value is False .

<!-- p.1267 -->

DependentProgram
Specifies a program (in this package) that must run before the current program. This
entry uses the following format:

DependentProgram=<ProgramName>

where <ProgramName> is the Name entry for that program in the package definition
file. If there are no dependent programs, leave this entry empty.

For example:

DependentProgram=Admin

DependentProgram=

Assignment
How the program is assigned to users. This value can be FirstUser (only the first user
who logs on runs the program) or EveryUser (every user who logs on to the client runs
the program). When CanRunWhen is not set to UserLoggedOn, this entry is set to
FirstUser.

Disabled
Specifies whether this program can be advertised to clients. Available values are True or
False . The default value is False .

See Also
Software distribution overview About deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1268 -->

How to Create a Package
Article • 10/04/2022

The following example shows how to create a package in Configuration Manager by
using the SMS_Package class and class properties.

To create a package
   1. Set up a connection to the SMS Provider.

   2. Create the new package object by using the SMS_Package class.

   3. Populate the new package properties.

         Tip

        When you are creating a Virtual Application Package, you must set the
         SMS_Package properties to specific values. Instances of the SMS_VirtualApp

        class must reference instances of the SMS_Package class that use the
        properties described in the following table.

      Virtual Application Package

                                                                         ﾉ   Expand table

       Property Name                  Property Value

       PackageType                    7

       PkgSourceFlag                  2

       PkgSourcePath                  \\someserver\somesharepath

   4. Save the package.

Example
The following example method creates a new package and populates its properties for
use in software distribution.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.1269 -->

vbs

Sub CreatePackage(connection, newPackageName, newPackageDescription,
newPackageSourceFlag, newPackageSourcePath)

      ' Create the new package object.     Dim newPackage
      Set newPackage = connection.Get("SMS_Package").SpawnInstance_

      ' Populate the new package properties.
      newPackage.Name = newPackageName
      newPackage.Description = newPackageDescription
      newPackage.PkgSourceFlag = newPackageSourceFlag
      newPackage.PkgSourcePath = newPackageSourcePath

      ' Save the package.
      newPackage.Put_

      ' Output the new package name.
      wscript.echo "Created package: "   & newPackageDescription

End Sub

c#

public void CreatePackage(WqlConnectionManager connection, string
newPackageName, string newPackageDescription, int newPackageSourceFlag,
string newPackageSourcePath)
{
    try
    {
        // Create new package object.
        IResultObject newPackage = connection.CreateInstance("SMS_Package");

          // Populate new package properties.
          newPackage["Name"].StringValue = newPackageName;
          newPackage["Description"].StringValue = newPackageDescription;
          newPackage["PkgSourceFlag"].IntegerValue = newPackageSourceFlag;
          newPackage["PkgSourcePath"].StringValue = newPackageSourcePath;

          // Save new package and new package properties.
          newPackage.Put();

          // Output new package name.
          Console.WriteLine("Created package: " + newPackageName);
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create package. Error: " + ex.Message);
          throw;

<!-- p.1270 -->

      }
  }

The example method has the following parameters:

                                                                       ﾉ   Expand table

 Parameter               Type                        Description

 connection              - Managed:                  A valid connection to the SMS
                         WqlConnectionManager        Provider.
                         - VBScript: SWbemServices

 newPackageName          - Managed: String           The name of the new package.
                         - VBScript: String

 newPackageDescription   - Managed: String           The description for the new package.
                         - VBScript: String

 newPackageSourceFlag    - Managed: Integer          The package source.
                         - VBScript: Integer

 newPackageSourcePath    - Managed: String           The path to the package source.
                         - VBScript: String

Compiling the Code
The C# example requires:

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

<!-- p.1271 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
Software distribution overview SMS_Package Server WMI Class
PowerShell Cmdlet: New-CMPackage

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1272 -->

How to Create a Package by Using a
Package Definition File Template
Article • 10/04/2022

The following example shows how to create a package and program by using a package
definition file template in Configuration Manager. The package definition file template
contains the default values that are used to create SMS_Package and SMS_Program
objects. The following example uses the SMS_PDF_Package class and the GetPDFData
method to load the package definition file template information and to create a
package and the related programs.

To create a package by using a package definition file
template
   1. Set up a connection to the SMS Provider.

   2. Create the new package object by using the SMS_PDF_Package class.

   3. Populate any additional package properties.

   4. Load the program information and associate each program with the package.

Example
The following example method creates a new package by using a package definition file.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub SWDCreatePDFPackage(connection, existingPDF_ID, newPackageSourceFlag,
  newPackageSourcePath)
      ' The PDF_ID must be passed in.
      ' The PDF_ID can be identified through the SMS_PDF_Package class.

        Dim newPDFPackage
        Dim returnCode
        Dim newPackage
        Dim newPackagePath
        Dim packageID
        Dim program

<!-- p.1273 -->

      Dim arrayOfPrograms

      ' Package Creation
      ' ----------------
      ' Create new SMS_PDF_Package instance.
      Set newPDFPackage = connection.Get("SMS_PDF_Package")

      ' Load the Package Definition File data using the GetPDFData method.
      returnCode = newPDFPackage.GetPDFData(existingPDF_ID, newPackage,
  arrayOfPrograms)

      ' Assign any additional package properties.
      newPackage.PkgSourceFlag = newPackageSourceFlag
      newPackage.PkgSourcePath = newPackageSourcePath

      ' Save the package path and get the Package ID.
      Set newPackagePath = newPackage.Put_
      packageID = newPackagePath.Keys("PackageID")

      ' Program Creation
      ' -----------------
      ' Enumerate through the program array and create the programs.
      For Each program In arrayOfPrograms
          program.PackageID = packageID
          program.Put_
      Next

  End Sub

The example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter              Type                        Description

 connection             - VBScript: SWbemServices   A valid connection to the SMS Provider.

 existingPDF_ID         - VBScript: Integer         ID of the package definition file.

 newPackageSourceFlag   - VBScript: Integer         The package source.

 newPackageSourcePath   - VBScript: String          The path to the package source.

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also

<!-- p.1274 -->

Software distribution overview SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1275 -->

How to Configure Package Properties
Article • 10/04/2022

The following example shows how to configure the properties of an existing package, in
Configuration Manager, by using the SMS_Package class.

To configure an existing package
   1. Set up a connection to the SMS Provider.

   2. Load the existing package object by using SMS_Package class.

   3. Populate any package properties (this example uses package description).

   4. Save the package and the new package properties.

Example
The following example method configures package properties for software distribution.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigurePackageProperties(connection, existingPackageID,
  newPackageDescription)

      ' Get the specific package object.     Dim packageToConfigure
      Set packageToConfigure = connection.Get("SMS_Package.PackageID='" &
  existingPackageID & "'")

      ' Replace the existing package property (in this case the package
  description).
      packageToConfigure.Description = newPackageDescription

        ' Save the package with the modified properties.
        packageToConfigure.Put_

        ' Output package ID and package name.
        wscript.echo "Configured Package "
        wscript.echo "Package ID:        " & packageToConfigure.PackageID
        wscript.echo "Package Name:      " & packageToConfigure.Name

<!-- p.1276 -->

  End Sub

  c#

  public void ConfigurePackageProperties(WqlConnectionManager connection,
  string existingPackageID, string newPackageDescription)
  {
      try
      {
          // Get specific package instance to modify.
          IResultObject packageToConfigure =
  connection.GetInstance(@"SMS_Package.PackageID='" + existingPackageID +
  "'");

          // Replace the existing package property with the new value (in this
  case the package description).
          packageToConfigure["Description"].StringValue =
  newPackageDescription;

              // Save package and modified package properties.
              packageToConfigure.Put();

          // Output package ID and package name.
          Console.WriteLine("Configured Package ");
          Console.WriteLine("Package ID:         " +
  packageToConfigure["PackageID"].StringValue);
          Console.WriteLine("Package Name:       " +
  packageToConfigure["Name"].StringValue);
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to configure package. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                       ﾉ   Expand table

 Parameter               Type                        Description

 connection              - Managed:                  A valid connection to the SMS
                         WqlConnectionManager        Provider.
 swbemServices           - VBScript: SWbemServices

<!-- p.1277 -->

 Parameter               Type                       Description

 existingPackageID       - Managed: String          The ID of the existing package.
                         - VBScript: String

 newPackageDescription   - Managed: String          The description for the new package.
                         - VBScript: String

Compiling the Code
The C# example requires:

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
Software distribution overview SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?    Yes      No

<!-- p.1278 -->

Provide product feedback

<!-- p.1279 -->

How to Configure a Package to Use
Binary Delta Replication
Article • 10/04/2022

The following example shows how to configure an existing package to use binary delta
replication, in Configuration Manager, by using the SMS_Package class and the PkgFlags
class property.

To configure an existing package to use binary delta
replication
   1. Set up a connection to the SMS Provider.

   2. Load the existing package object using SMS_Package class.

   3. Modify the PkgFlags using the hexadecimal value for AP_USE_BINARY_DELTA_REP.

   4. Save the package and the new package properties.

Example
The following example method configures an existing package to use binary delta
replication.

  ） Important

  The hexadecimal values that define the PkgFlags property are listed in the
   SMS_Package class reference material.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ModifyPackageToUseBinaryDeltaReplication(connection, existingPackageID)

      ' Define a constant with the hexadecimal value for
  AP_USE_BINARY_DELTA_REP.
      Const AP_USE_BINARY_DELTA_REP = &H04000000

<!-- p.1280 -->

    ' Get the specific advertisement instance to modify.     Dim
packageToModify
    Set packageToModify = connection.Get("SMS_Package.PackageID='" &
existingPackageID & "'")

     ' List the existing property values.
     Wscript.Echo " "
     Wscript.Echo "Values before change: "
     Wscript.Echo "--------------------- "
     Wscript.Echo "Package Name:   " & packageToModify.Name
     Wscript.Echo "Package Flags: " & packageToModify.PkgFlags

    ' Set the new property value.
    packageToModify.PkgFlags = packageToModify.PkgFlags OR
AP_USE_BINARY_DELTA_REP

     ' Save the advertisement.
     packageToModify.Put_

     ' Output the new property values.
     Wscript.Echo " "
     Wscript.Echo "Values after change: "
     Wscript.Echo "--------------------- "
     Wscript.Echo "Package Name:   " & packageToModify.Name
     Wscript.Echo "Package Flags: " & packageToModify.PkgFlags

End Sub

c#

public void ModifyPackageToUseBinaryDeltaReplication(WqlConnectionManager
connection, string existingPackageID)
{
    // Define a constant with the hexadecimal value for
AP_USE_BINARY_DELTA_REP.
    const Int32 AP_USE_BINARY_DELTA_REP = 0x04000000;

     try
     {
        // Get the specific package instance to modify.
        IResultObject packageToModify =
connection.GetInstance(@"SMS_Package.PackageID='" + existingPackageID +
"'");

        // List the existing property values.
        Console.WriteLine();
        Console.WriteLine("Values before change:");
        Console.WriteLine("_____________________");
        Console.WriteLine("Package Name: " +
packageToModify["Name"].StringValue);
        Console.WriteLine("Package Flags: " +
