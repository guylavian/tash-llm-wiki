---
title: "Configuration Manager SDK documentation — pages 1081-1120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1081-1120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1081-1120
family: sccm
documentKind: "doc"
abstract: "Example The following example method adds a new computer to Configuration Manager. The ImportMachineEntry Method in Class SMS_Site is used to import the computer. Then, the computer is added to a custom collection. \"All Systems\" collection. ） Important In previous version of thi"
---

# Configuration Manager SDK documentation — pages 1081-1120

<!-- p.1081 -->

Example
The following example method adds a new computer to Configuration Manager. The
ImportMachineEntry Method in Class SMS_Site is used to import the computer. Then,
the computer is added to a custom collection. "All Systems" collection.

  ） Important

  In previous version of this example, the computer was added to the "All Systems"
  collection. It is no longer possible to modify the built-in collections, use a custom
  collection instead.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddNewComputer (connection, netBiosName, smBiosGuid, macAddress)

        Dim inParams
        Dim outParams
        Dim siteClass
        Dim collection
        Dim collectionRule

        If (IsNull(smBiosGuid) = True) And (IsNull(macAddress) = True) Then
            WScript.Echo "smBiosGuid or macAddress must be defined"
            Exit Sub
        End If

        If IsNull(macAddress) = False Then
            macAddress = Replace(macAddress,"-",":")
        End If

        ' Obtain an InParameters object specific
        ' to the method.

        Set siteClass = connection.Get("SMS_Site")
        Set inParams = siteClass.Methods_("ImportMachineEntry"). _
            inParameters.SpawnInstance_()

        ' Add the input parameters.
        inParams.Properties_.Item("MACAddress") = macAddress
        inParams.Properties_.Item("NetbiosName") = netBiosName
        inParams.Properties_.Item("OverwriteExistingRecord") = False
        inParams.Properties_.Item("SMBIOSGUID") = smBiosGuid

        ' Add the computer.
        Set outParams = connection.ExecMethod("SMS_Site", "ImportMachineEntry",

<!-- p.1082 -->

inParams)

      ' Add the computer to the all systems collection.
      set collection = connection.Get("SMS_Collection.CollectionID='ABC0000A'")

   set
collectionRule=connection.Get("SMS_CollectionRuleDirect").SpawnInstance_

      collectionRule.ResourceClassName="SMS_R_System"
      collectionRule.ResourceID= outParams.ResourceID

      collection.AddMembershipRule collectionRule

End Sub

c#

public int AddNewComputer(
    WqlConnectionManager connection,
    string netBiosName,
    string smBiosGuid,
    string macAddress)
{
    try
    {
        if (smBiosGuid == null && macAddress == null)
        {
            throw new ArgumentNullException("smBiosGuid or macAddress must
be defined");
        }

          // Reformat macAddress to : separator.
          if (string.IsNullOrEmpty(macAddress) == false)
          {
              macAddress = macAddress.Replace("-", ":");
          }

          // Create the computer.
          Dictionary<string, object> inParams = new Dictionary<string, object>
();
          inParams.Add("NetbiosName", netBiosName);
          inParams.Add("SMBIOSGUID", smBiosGuid);
          inParams.Add("MACAddress", macAddress);
          inParams.Add("OverwriteExistingRecord", false);

          IResultObject outParams = connection.ExecuteMethod(
              "SMS_Site",
              "ImportMachineEntry",
              inParams);

        // Add to All System collection.
        IResultObject collection =
connection.GetInstance("SMS_Collection.collectionId='ABC0000A'");

<!-- p.1083 -->

          IResultObject collectionRule =
  connection.CreateEmbeddedObjectInstance("SMS_CollectionRuleDirect");
          collectionRule["ResourceClassName"].StringValue = "SMS_R_System";
          collectionRule["ResourceID"].IntegerValue =
  outParams["ResourceID"].IntegerValue;

          Dictionary<string, object> inParams2 = new Dictionary<string,
  object>();
          inParams2.Add("collectionRule", collectionRule);

              collection.ExecuteMethod("AddMembershipRule", inParams2);

          return outParams["ResourceID"].IntegerValue;
      }
      catch (SmsException e)
      {
          Console.WriteLine("failed to add the computer" + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter      Type                        Description

 connection     - Managed:                  - A valid connection to the SMS Provider.
                 WqlConnectionManager
                - VBScript: SWbemServices

 netBiosName    - Managed: String           - The computer NETBIOS name.
                - VBScript: String

 smBiosGuid     - Managed: String           The SMBIOS GUID for the computer.
                - VBScript: String

 MacAddress     - Managed: String           The MAC address for the computer in the following
                - VBScript: String          format: 00:00:00:00:00:00 .

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

<!-- p.1084 -->

System.Collections.Generic

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
ImportMachineEntry Method in Class SMS_Site
About OS deployment computer management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1085 -->

How to Create an Association Between
Two Computers in Configuration
Manager
Article • 10/04/2022

You create an association between a reference and destination computer, in
Configuration Manager, by calling the AddAssociation Method in Class
SMS_StateMigration.

  ７ Note

  You call the DeleteAssociation Method in Class SMS_StateMigration to delete an
  association.

To create an association between two computers
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Call the AddAssociation Method in Class SMS_StateMigration.

Example
The following example method adds an association between a source and reference
computer.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AssociateComputer(connection, referenceComputerResourceId,
  destinationComputerResourceId)

         Dim stateMigrationClass
         Dim inParams
         Dim outParams

         ' Get the state migration class.
         Set stateMigrationClass = connection.Get("SMS_StateMigration")

<!-- p.1086 -->

        ' Set up the parameters.
        Set inParams = _

  stateMigrationClass.Methods_("AddAssociation").InParameters.SpawnInstance_
      inParams.SourceClientResourceID = referenceComputerResourceId
      inParams.RestoreClientResourceID = destinationComputerResourceId

      ' Call the method.
      Set outParams = _
        connection.ExecMethod( "SMS_StateMigration", "AddAssociation",
  inParams)

       End Sub

  c#

  public void AssociateComputer(
      WqlConnectionManager connection,
      int referenceComputerResourceId,
      int destinationComputerResourceId)
  {
      try
      {
          // Set up the reference and destination computer in parameters.
          Dictionary<string, object> inParams = new Dictionary<string, object>
  ();
          inParams.Add("SourceClientResourceID", referenceComputerResourceId);
          inParams.Add("RestoreClientResourceID",
  destinationComputerResourceId);

          // Create the computer association.
         connection.ExecuteMethod("SMS_StateMigration", "AddAssociation",
  inParams);
      }
      catch (SmsException e)
      {
          Console.WriteLine("failed to make the association" + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                        ﾉ   Expand table

 Parameter                    Type                   Description

 connection                   - Managed:             A valid connection to the SMS
                              WqlConnectionManager   Provider.
                              - VBScript:
                              SWbemServices

<!-- p.1087 -->

 Parameter                       Type                  Description

 referenceComputerResourceID     - Managed: Integer    The Configuration Manager resource
                                 - VBScript: Integer   identifier for the reference computer.
                                                       This is available from SMS_R_System
                                                       class ResourceId property for the
                                                       computer.

 destinationComputerResourceID   - Managed: Integer    The Configuration Manager resource
                                 - VBScript: Integer   identifier for the destination
                                                       computer. This is available from
                                                       SMS_R_System class ResourceId
                                                       property for the computer.

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

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

<!-- p.1088 -->

See Also
About OS deployment computer management AddAssociation Method in Class
SMS_StateMigration
DeleteAssociation Method in Class SMS_StateMigration

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1089 -->

How to Create a Collection Variable in
Configuration Manager
Article • 10/04/2022

You create a collection variable for a Configuration Manager collection by adding
instances of SMS_CollectionVariable Server WMI Class to the CollectionVariables
property of SMS_CollectionSettings Server WMI Class.

To create a collection variable
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get an instance of SMS_CollectionSettings.

   3. For each variable to be added, add instances of the embedded object
        SMS_CollectionVariable to the CollectionVariables array property.

   4. Commit the changes to the SMS_CollectionSettings class instance.

Example
The following example method creates a collection variable and adds it to the collection
identified by the supplied identifier. If the SMS_CollectionSettings object for the
collection does not exist, it is created.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub CreateCollectionVariable( connection, name, value, mask, collectionId,
  precedence)

         Dim collectionSettings
         Dim collectionVariables
         Dim collectionVariable
         Dim Settings

         ' See if the settings collection already exists. if it does not, create
  it.
         Set settings = connection.ExecQuery _
           ("Select * From SMS_CollectionSettings Where CollectionID = '" &

<!-- p.1090 -->

collectionID & "'")

    If settings.Count = 0 Then
        Wscript.Echo "Creating collection settings object"
        Set collectionSettings =
connection.Get("SMS_CollectionSettings").SpawnInstance_
        collectionSettings.CollectionID = collectionId
        collectionSettings.Put_
    End If

    ' Get the collection settings object.
    Set collectionSettings =
connection.Get("SMS_CollectionSettings.CollectionID='" & collectionId &"'" )

     ' Get the collection variables.
     collectionVariables=collectionSettings.CollectionVariables

    ' Create and populate a new collection variable.
    Set collectionVariable =
connection.Get("SMS_CollectionVariable").SpawnInstance_
    collectionVariable.Name = name
    collectionVariable.Value = value
    collectionVariable.IsMasked = mask

    ' Add the new collection variable.
    ReDim Preserve collectionVariables (UBound (collectionVariables)+1)
    Set collectionVariables(UBound(collectionVariables)) =
collectionVariable

     collectionSettings.CollectionVariables=collectionVariables

     collectionSettings.Put_

 End Sub

c#

public void CreateCollectionVariable(
    WqlConnectionManager connection,
    string name,
    string value,
    bool mask,
    string collectionId,
    int precedence)
{
    try
    {
        IResultObject collectionSettings = null;

        // Get the collection settings. Create it if necessary.

         IResultObject collectionSettingsQuery =
connection.QueryProcessor.ExecuteQuery(

<!-- p.1091 -->

                      "Select * from SMS_CollectionSettings where
  CollectionID='" + collectionId + "'");

           foreach (IResultObject setting in collectionSettingsQuery)
           {
               collectionSettings = setting;
           }

          if ( collectionSettings == null)
           {
               collectionSettings =
  connection.CreateInstance("SMS_CollectionSettings");
               collectionSettings["CollectionID"].StringValue = collectionId;
               collectionSettings.Put();
               collectionSettings.Get();
           }

          // Create the collection variable.
          List<IResultObject> collectionVariables =
  collectionSettings.GetArrayItems("CollectionVariables");
          IResultObject collectionVariable =
  connection.CreateEmbeddedObjectInstance("SMS_CollectionVariable");
          collectionVariable["Name"].StringValue = name;
          collectionVariable["Value"].StringValue = value;
          collectionVariable["IsMasked"].BooleanValue = mask;

          // Add the collection variable to the collection settings.
          collectionVariables.Add(collectionVariable);
          collectionSettings.SetArrayItems("CollectionVariables",
  collectionVariables);

          // Set the collection variable precedence.
          collectionSettings["CollectionVariablePrecedence"].IntegerValue =
  precedence;

          collectionSettings.Put();
       }
       catch (SmsException e)
       {
           Console.WriteLine("Failed to create collection variable: " +
  e.Message);
           throw;
     }
  }

The example method has the following parameters:

                                                                    ﾉ   Expand table

<!-- p.1092 -->

 Parameter      Type                        Description

 Connection     - Managed:                  A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript: SWbemServices

 Name           - Managed: String           The name of the variable to be created.
                - VBScript: String

 Value          - Managed: String           The value of the variable
                - VBScript: String

 Mask           - Managed: Boolean          Specifies whether the value is displayed in the
                - VBScript: Boolean         Configuration Manager console.

                                            true - the variable value is not displayed.

                                            false - the variable value is displayed.

 CollectionID   - Managed: String           The collection that the variable is added to.
                - VBScript: String

 Precedence     - Managed: Integer          The precedence of the variable over other
                - VBScript: Integer         variables in the array.

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

<!-- p.1093 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create a Computer Variable in Configuration Manager
How to Create a Configuration Manager Object by Using Managed Code
How to Create a Configuration Manager Object by Using WMI
About OS deployment computer management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1094 -->

How to Create a Computer Variable in
Configuration Manager
Article • 10/04/2022

You create a computer variable for a computer that is running Configuration Manager
by adding instances of SMS_MachineVariable to the SMS_MachineSettings class
MachineVariables array property.

To create a computer variable
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get an instance of SMS_MachineSettings .

   3. For each variable to be added, add instances of the embedded object a
        SMS_MachineVariable to the MachineVariables array property.

   4. Commit the changes to the SMS_MachineSettings class instance.

Example
The following example method creates a collection variable and adds it to the collection
identified by the supplied identifier.

In the example, the LocaleID property is hard-coded to English (U.S.). If you need the
locale for non-U.S. installations, you can get it from the SMS_Identification Server WMI
Class LocaleID property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub CreateComputerVariable(connection, siteCode, name, value, mask,
  computerId)

         Dim computerSettings
         Dim computerVariables
         Dim computerVariable
         Dim Settings

         ' See if the computer settings object already exists. if it does not,

<!-- p.1095 -->

create it.
    Set settings = connection.ExecQuery _
      ("Select * From SMS_MachineSettings Where ResourceID = '" & computerID
& "'")

    If settings.Count = 0 Then
        Wscript.Echo "Creating computer settings object"
        Set computerSettings =
connection.Get("SMS_MachineSettings").SpawnInstance_
        computerSettings.ResourceID = computerId
        computerSettings.SourceSite = siteCode
        computerSettings.LocaleID = 1033
        computerSettings.Put_
    End If

    ' Get the computer settings object.
    Set computerSettings = connection.Get("SMS_MachineSettings.ResourceID='"
& computerId &"'" )

     ' Get the computer variables.
     computerVariables=computerSettings.MachineVariables

    ' Create and populate a new computer variable.
    Set computerVariable =
connection.Get("SMS_MachineVariable").SpawnInstance_
    computerVariable.Name = name
    computerVariable.Value = value
    computerVariable.IsMasked = mask

     ' Add the new computer variable.
     ReDim Preserve computerVariables (UBound (computerVariables)+1)
     Set computerVariables(UBound(computerVariables)) = computerVariable

     computerSettings.MachineVariables=computerVariables

     computerSettings.Put_

 End Sub

c#

public void CreateComputerVariable(
    WqlConnectionManager connection,
    string siteCode,
    string name,
    string value,
    bool mask,
    int computerId)
{
    try
    {
        // Get the computer settings.
        IResultObject computerSettings=null;

<!-- p.1096 -->

          IResultObject computerSettingsQuery =
  connection.QueryProcessor.ExecuteQuery(
              "Select * from SMS_MachineSettings where ResourceId = '" +
  computerId + "'");

          foreach (IResultObject settings in computerSettingsQuery)
          {
              computerSettings = settings;
          }

          if (computerSettings == null) // It does not exist, so create it.
          {
              computerSettings =
  connection.CreateInstance(@"SMS_MachineSettings");
              computerSettings["ResourceID"].IntegerValue = computerId;
              computerSettings["SourceSite"].StringValue = siteCode;
              computerSettings["LocaleID"].IntegerValue = 1033;
              computerSettings.Put();
              computerSettings.Get();
          }

          // Create the computer variable.
          List<IResultObject> computerVariables =
  computerSettings.GetArrayItems("MachineVariables");
          IResultObject computerVariable =
  connection.CreateEmbeddedObjectInstance("SMS_MachineVariable");
          computerVariable["Name"].StringValue = name;
          computerVariable["Value"].StringValue = value;
          computerVariable["IsMasked"].BooleanValue = mask;

          // Add the computer variable to the computer settings.
          computerVariables.Add(computerVariable);
          computerSettings.SetArrayItems("MachineVariables",
  computerVariables);

          computerSettings.Put();
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to create computer variable: " +
  e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                    ﾉ   Expand table

<!-- p.1097 -->

 Parameter    Type                        Description

 connection   - Managed:                  A valid connection to the SMS Provider.
              WqlConnectionManager
              - VBScript: SWbemServices

 siteCode     - Managed: String           The site code of the source site.
              - VBScript: String

 name         - Managed: String           The name of the variable to be created.
              - VBScript: String

 value        - Managed: String           The value of the variable.
              - VBScript: String

 mask         - Managed: Boolean          Specifies whether the value is displayed in the
              - VBScript: Boolean         Configuration Manager console.

                                          true - the variable value is not displayed.

                                          false - the variable value is displayed.

 computerID   - Managed: Integer          The computer identifier. Typically this is the
              - VBScript: Integer         SMS_R_System class ResourceID property.

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

<!-- p.1098 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See also
About OS deployment computer management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1099 -->

How to Track Operating System
Deployment Migrations in
Configuration Manager
Article • 10/04/2022

You track Configuration Manager operating system migrations by inspecting the
SMS_StateMigration class.

The StoreCreationDate , StoreDeletionDate , and StoreReleaseDate properties can be
used to identify the current state of the migration.

To track state migrations
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get an instance of SMS_StateMigration.

   3. Calculate the current migration state using the StoreCreationDate ,
        StoreDeletionDate , and StoreReleaseDate properties.

Example
The following example method enumerates through all migrations and determines
whether they are in progress.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub MigrationState(connection)

         Dim migrations
         Dim migration
         Dim inProgress
         Dim zeroTime

         zeroTime = "00000000000000.000000+***"

      Set migrations = connection.ExecQuery( "Select * From
  SMS_StateMigration")

<!-- p.1100 -->

     For Each migration in Migrations
         inProgress=False

          If migration.StoreCreationDate<>zeroTime Then
               If migration.StoreReleaseDate = zeroTime Then
                   inProgress=True
               Else If migration.StoreDeletionDate = zeroTime Then
                   inProgress = True
               Else
                   inProgress = false
               End If
          End If
          Else
               inProgress=False
          End If

         WScript.StdOut.Write "Migration " + migration.MigrationID
         If inProgress = True Then
              Wscript.Echo " is in progress"
         Else
              WScript.Echo " is not in progress"
         End If
     Next

End Sub

c#

public void MigrationState(WqlConnectionManager connection)
{
    try
    {
        IResultObject migrations =
            connection.QueryProcessor.ExecuteQuery("Select * from
SMS_StateMigration");

          string zeroTime = "00000000000000.000000+***";

          foreach (IResultObject migration in migrations)
          {
              Boolean inProgress = false;

            if
(migration["StoreCreationDate"].DateTimeValue.Equals(zeroTime) == false)
            {
                if
(migration["StoreReleaseDate"].DateTimeValue.Equals(zeroTime) == true)
                {
                    inProgress = true;
                }
                else if
(migration["StoreDeletionDate"].DateTimeValue.Equals(zeroTime) == true)
                {

<!-- p.1101 -->

                            inProgress = true;
                     }
                     else
                     {
                            inProgress = false;
                   }
               }
               else
               {
                   inProgress = false;
               }

              Console.Write("Migration " +
  migration["MigrationID"].StringValue);
              if (inProgress)
              {
                  Console.WriteLine(" is in progress");
              }
              else
              {
                  Console.WriteLine(" is not in progress");
              }
          }
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed while displaying migration state: " +
  e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter    Type                                Description

 connection   - Managed: WqlConnectionManager     A valid connection to the SMS Provider.
              - VBScript: SWbemServices

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

<!-- p.1102 -->

System.Collections.Generic

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
About OS deployment computer management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1103 -->

About Operating System Deployment
Image Management
Article • 10/04/2022

There are several package types that Configuration Manager uses to manage reference
computer operating system images.

For more information about operating system deployment image management, see
Manage operating system images with Configuration Manager.

Reference Computer

Operating System Installation
The operating system installation package contains all the files necessary to install the
desired Windows operating system on a reference computer. in Configuration Manager,
they're managed by SMS_OperatingSystemInstallPackage. This package doesn't require
a program. The task sequence references the source files as needed.

Boot Image
An operating system deployment boot image is a Windows Pre-Installation Environment
(PE) 2.0 image that is used during the operating system deployment process. In
Configuration Manager, boot images are managed by SMS_BootImagePackage. For
more information, see How to Add a Boot Image from a WIM File in Configuration
Manager.

Driver Packages
Driver packages contain Windows device drivers that aren't included with the operating
system. In Configuration Manager they're managed by SMS_DriverPackage objects. For
more information, see How to Create a Driver Package for a Windows Driver in
Configuration Manager.

Sysprep Package
Sysprep is a Windows system presentation tool that facilitates image creation and
preparation of an image for deployment to multiple computers. Sysprep is supplied with

<!-- p.1104 -->

Windows Vista, but if you're deploying Windows XP or an earlier operating system, you
must create an SMS_Package object package to contain Sysprep and its support files.
For more information about creating SMS_Package objects, see How to Create a Package.

Target Computer

Operating System Image
Operating system image packages contain operating system images. In Configuration
Manager, they're managed by SMS_ImagePackage objects. For more information, see
How to Add an Operating System Image Package in Configuration Manager.

Configuration Manager 2007 Client Installation
Because every operating system deployment installs the Configuration Manager client,
you need to create a package ( SMS_Package ) to install the Configuration Manager client.
You can use the package definition file that is included with Configuration Manager for
the Configuration Manager client upgrade. For more information about creating a
package with a package definition file, see How to Create a Package by Using a Package
Definition File Template.

User State Migration Tool
If you're migrating user state from one desktop to another, then you should use the
User State Migration Tool (USMT) as your migration tool.

In Configuration Manager, you create a package ( SMS_Package ) object to run the USMT
on the computer. A package program isn't required.

Other Packages
You'll need to create other packages ( SMS_Package ) for the applications you want
installed on the target computer.

Package Distribution
You copy the various package types to distribution points by using the same method
that you would use for copying SMS_Package package object. For more information, see
How to Assign a Package to a Distribution Point.

<!-- p.1105 -->

See also
Operating System Deployment Task Sequence Object Model

Software distribution overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1106 -->

How to Add an Operating System Image
Package in Configuration Manager
Article • 10/04/2022

In Configuration Manager, you add an operating system image package by creating an
instance of SMS_ImagePackage class. The path to the Windows Image (WIM) file is
specified in the PkgSourcePath property as a Universal Naming Convention (UNC) path.

To create an operating system image package
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Create an instance of SMS_ImagePackage.

   3. Specify the path to the WIM file in PkgSourcePath.

   4. Commit the SMS_ImagePackage class instance.

Example
The following example method creates an operating system package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddOSImagePackage(connection, newImagePackageName,
  newImagePackageDescription, newImagePackageSourcePath)

         Dim newImagePackage

      Set newImagePackage =
  connection.Get("SMS_ImagePackage").SpawnInstance_()
      ' Populate the new package properties.
      newImagePackage.Name = newImagePackageName
      newImagePackage.Description = newImagePackageDescription
      newImagePackage.PkgSourceFlag = 2
      newImagePackage.PkgSourcePath = newImagePackageSourcePath

         ' Save the package.
          newImagePackage.Put_

<!-- p.1107 -->

  End Sub

  c#

  public void AddOSImagePackage(
      WqlConnectionManager connection,
      string newImagePackageName,
      string newImagePackageDescription,
      string newImagePackageSourcePath)
  {
      try
      {
          // Create new package object.
          IResultObject newImagePackage =
  connection.CreateInstance("SMS_ImagePackage");

          // Populate new package properties.
          newImagePackage["Name"].StringValue = newImagePackageName;
          newImagePackage["Description"].StringValue =
  newImagePackageDescription;
          newImagePackage["PkgSourceFlag"].IntegerValue =
  (int)PackageSourceFlag.StorageDirect;
          newImagePackage["PkgSourcePath"].StringValue =
  newImagePackageSourcePath;

              // Save new package and new package properties.
              newImagePackage.Put();
       }
       catch (SmsException e)
       {
           Console.WriteLine();
           Console.WriteLine("Failed to create package. Error: " + e.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                        ﾉ   Expand table

 Parameter                   Type                        Description

 connection                  - Managed:                  A valid connection to the SMS
                             WqlConnectionManager        Provider.
                             - VBScript: SWbemServices

 newImagePackageName         - Managed: String           The new image package name.
                             - VBScript: String

<!-- p.1108 -->

 Parameter                    Type                      Description

 newImagePackageDescription   - Managed: String         The new image package
                              - VBScript: String        description

 newImagePackageSourcePath    - Managed: String         The UNC path to the WIM file.
                              - VBScript: String

Compiling the Code
The C# example has the following compilation requirements:

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

<!-- p.1109 -->

How to Assign a Package to a Distribution Point
About image management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1110 -->

How to Update an Operating System
Image Package in Configuration
Manager
Article • 10/04/2022

In Configuration Manager, you update the Windows Image (WIM) file that is associated
with the operating system package by calling the image package's SMS_ImagePackage
class instance ReloadImageProperties method. The image is updated based on the
location defined in the pkgSourcePath property.

To update an operating system image package
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_ImagePackage class instance you want to update.

   3. Call the ReloadImageProperties class instance method.

   4. Commit the SMS_ImagePackage class instance.

Example
The following example updates an operating system image package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub UpdateOSImage(connection,imagePackageID, sourcePath)

         Dim imagePackage

      ' Get the image.
      set imagePackage = connection.Get("SMS_ImagePackage.PackageID='" &
  imagePackageID & "'")

         ' Update the source.
         imagePackage.PkgSourcePath=sourcePath
         imagePackage.Put_
         imagePackage.RefreshPkgSource

<!-- p.1111 -->

  End Sub

  c#

  public void UpdateOSImage(
      WqlConnectionManager connection,
      string imagePackageId,
      string sourcePath)
  {
      try
      {
          // Get the image package.
          IResultObject imagePackage =
  connection.GetInstance(@"SMS_ImagePackage.PackageID='" + imagePackageId +
  "'");

              // Update the location.
              imagePackage["PkgSourcePath"].StringValue = sourcePath;
              imagePackage.Put();
              imagePackage.ExecuteMethod("RefreshPkgSource", null);
       }
       catch (SmsException e)
       {
           Console.WriteLine(e.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                                ﾉ   Expand table

 Parameter         Type                        Description

 connection        - Managed:                  A valid connection to the SMS Provider.
                   WqlConnectionManager
                   - VBScript: SWbemServices

 imagePackageID    - Managed: String           The package image identifier. It is available from
                   - VBScript: String          SMS_ImagePackage. PackageID .

 sourcePath        - Managed: String           The path to the image package source in
                   - VBScript: String          Universal Naming Convention (UNC) format.

Compiling the Code
The C# example has the following compilation requirements:

<!-- p.1112 -->

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

See also
About image management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1113 -->

How to View the Properties for an
Operating System Image
Article • 10/04/2022

In Configuration Manager, you view the image properties for the Windows Image (WIM)
file that is contained in an operating system package by calling the SMS_ImagePackage
class instance GetImageProperties method.

The image properties are available in XML format.

To view image properties
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_ImagePackage class instance that you want to update.

   3. Call the GetImageProperties class instance method.

   4. Access property XML by using the ImageProperty parameter.

Example
The following example displays the operating system image package property XML that
defines the package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ViewOSImage(connection,imagePackageID)

         Dim imagePackage
         Dim inParam
         Dim outParams

      ' Get the image.
      Set imagePackage = connection.Get("SMS_ImagePackage.PackageID='" &
  imagePackageID & "'")

         ' Obtain an InParameters object specific
         ' to the method.
         Set inParam = imagePackage.Methods_("GetImageProperties"). _

<!-- p.1114 -->

            inParameters.SpawnInstance_()

      ' Add the input parameters.
      inParam.Properties_.Item("SourceImagePath") =
  imagePackage.PkgSourcePath

      ' Execute the method.
      Set outParams = connection.ExecMethod("SMS_ImagePackage",
  "GetImageProperties", inParam)

        ' Display the image properties XML.
        Wscript.echo "ImageProperty: " & outParams.ImageProperty

  End Sub

  c#

  public void ViewOSImage(
      WqlConnectionManager connection,
      string imagePackageId)
  {
      try
      {
          IResultObject imagePackage =
  connection.GetInstance(@"SMS_ImagePackage.PackageID='" + imagePackageId +
  "'");

            Dictionary<string, Object> inParams = new Dictionary<string, object>
  ();

          inParams.Add("SourceImagePath",
  imagePackage["PkgSourcePath"].StringValue);
          IResultObject result = connection.ExecuteMethod("SMS_ImagePackage",
  "GetImageProperties", inParams);

            Console.WriteLine(result["ImageProperty"].StringValue);
        }
        catch (SmsException e)
        {
            Console.WriteLine(e.Message);
            throw;
        }
  }

The example method has the following parameters:

                                                                      ﾉ   Expand table

<!-- p.1115 -->

 Parameter        Type                        Description

 connection       - Managed:                  A valid connection to the SMS Provider.
                  WqlConnectionManager
                  - VBScript: SWbemServices

 imagePackageID   - Managed: String           The package image identifier. It is available from
                  - VBScript: String          SMS_ImagePackage. PackageID .

Compiling the Code
The C# example has the following compilation requirements:

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

See also

<!-- p.1116 -->

About image management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1117 -->

How to Add a Boot Image from a WIM
File in Configuration Manager
Article • 10/04/2022

You add a boot image from a Windows Image (WIM) file to Configuration Manager by
creating an instance of SMS_BootImagePackage. The property ImagePath must be set to
the Universal Naming Convention (UNC) path to the WIM file. The property ImageIndex
is the index to the required image within the WIM file.

If the boot image requires Windows drivers, you specify them in the ReferencedDrivers
property, which is an array of SMS_Driver_Details.

  ７ Note

  When the boot image is updated, for example, when a Configuration Manager
  binary or boot image property is changed, the boot image must be updated by
  calling the SMS_BootImagePackage class RefreshPkgSource method.

To add a boot image from a WIM file
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Create an instance of SMS_BootImagePackage.

   3. Set at least the Name, ImagePath, and ImageIndex properties.

   4. Commit the changes.

Example
The following example method adds a boot image from a WIM file.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddBootImagePackage(connection, name, description, pathToWim)

         Dim bootImagePackage

<!-- p.1118 -->

      Set bootImagePackage =
  connection.Get("SMS_BootImagePackage").SpawnInstance_()
      ' Populate the new package properties.
      bootImagePackage.Name = name
      bootImagePackage.Description = description

       bootImagePackage.ImagePath = pathToWim 'UNC path to WIM file.
       bootImagePackage.ImageIndex = 1 ' Index into WIM file for image

       bootImagePackage.Put_

  End Sub

  c#

  public void AddBootImage(
      WqlConnectionManager connection,
      string name,
      string description,
      string pathToWim)
  {
      try
      {
          // Create new boot image package object.
          IResultObject bootImagePackage =
  connection.CreateInstance("SMS_BootImagePackage");

          // Populate new boot image package properties.
          bootImagePackage["Name"].StringValue = name;
          bootImagePackage["Description"].StringValue = description;
          bootImagePackage["ImagePath"].StringValue = pathToWim; // UNC path
  required.
          bootImagePackage["ImageIndex"].IntegerValue = 1; // Index into WIM
  file for image.

            // Save new package and new package properties.
            bootImagePackage.Put();
       }
       catch (SmsException e)
       {
           Console.WriteLine();
           Console.WriteLine("Failed to create package. Error: " + e.Message);
           throw;
       }
  }

The sample method has the following parameters:

                                                                  ﾉ   Expand table

<!-- p.1119 -->

 Parameter     Type                              Description

 connection    - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
               - VBScript: SWbemServices

 name          - Managed: String                 Name for the new boot image package.
               - VBScript: String

 description   - Managed: String                 Description for the boot image package.
               - VBScript: String

 pathToWIM     - Managed: Integer                UNC path to the image.
               - VBScript: Integer

Compiling the Code
The C# example has the following compilation requirements:

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

<!-- p.1120 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
How to Assign a Package to a Distribution Point
How to add a Windows Driver to a Configuration Manager Boot Image Package
How to Assign a Package to a Distribution Point
About image management

Feedback
Was this page helpful?      Yes    No

Provide product feedback
