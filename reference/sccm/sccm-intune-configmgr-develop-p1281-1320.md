---
title: "Configuration Manager SDK documentation — pages 1281-1320"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1281-1320
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1281-1320
family: sccm
documentKind: "doc"
abstract: "packageToModify[\"PkgFlags\"].IntegerValue); // Modify the PkgFlags value to include the AP_USE_BINARY_DELTA_REP value. packageToModify[\"PkgFlags\"].IntegerValue = packageToModify[\"PkgFlags\"].IntegerValue | AP_USE_BINARY_DELTA_REP; // Save the package with the new value. packageToM"
---

# Configuration Manager SDK documentation — pages 1281-1320

<!-- p.1281 -->

  packageToModify["PkgFlags"].IntegerValue);

              // Modify the PkgFlags value to include the AP_USE_BINARY_DELTA_REP
  value.
          packageToModify["PkgFlags"].IntegerValue =
  packageToModify["PkgFlags"].IntegerValue | AP_USE_BINARY_DELTA_REP;

              // Save the package with the new value.
              packageToModify.Put();

              // Reload the package to verify the change.
              packageToModify.Get();

          // List the existing (modified) property values.
          Console.WriteLine();
          Console.WriteLine("Values after change:");
          Console.WriteLine("_____________________");
          Console.WriteLine("Package Name: " +
  packageToModify["Name"].StringValue);
          Console.WriteLine("Package Flags: " +
  packageToModify["PkgFlags"].IntegerValue);
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to modify package. Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter            Type                              Description

 Connection           - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                      - VBScript: SWbemServices
 swbemServices

 existingPackageID    - Managed: String                 The ID of the existing package.
                      - VBScript: String

Compiling the Code
The C# example requires:

Namespaces

<!-- p.1282 -->

System

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security

See Also
Software distribution overview SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1283 -->

How to Delete a Package
Article • 10/04/2022

The following example shows how to delete a package in Configuration Manager by
using the SMS_Package class.

  ７ Note

  Any reference to this package, such as an advertisement or task sequence, should
  be cleaned up before deleting the package

To delete a package
   1. Set up a connection to the SMS Provider.

   2. Load the existing package object by using the SMS_Package class.

   3. Delete the package by using the delete method.

Example
The following example method deletes an existing package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DeleteAPackage(connection, existingPackageID)

      ' Get the specified package instance (passed in as existingPackageID).
  Dim packageToDelete
      Set packageToDelete = connection.Get("SMS_Package.PackageID='" &
  existingPackageID & "'")

        ' Delete the package.
        PackageToDelete.Delete_

        ' Output package ID of deleted package.
        wscript.echo "Deleted Package ID: " & existingPackageID

  End Sub

<!-- p.1284 -->

  c#

  public void DeleteAPackage(WqlConnectionManager connection, string
  existingPackageID)
  {
      try
      {
          // Get the specified package instance (passed in as
  existingPackageID).
          IResultObject packageToDelete =
  connection.GetInstance(@"SMS_Package.PackageID='" + existingPackageID +
  "'");

              // Delete the package instance.
              packageToDelete.Delete();

              // Output package ID of deleted package.
              Console.WriteLine("Deleted Package ID: " + existingPackageID);
       }

       catch (SmsException ex)
       {
           Console.WriteLine("Failed to create package. Error: " + ex.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter            Type                              Description

 connection           - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                      - VBScript: SWbemServices
 swbemServices

 existingPackageID    - Managed: String                 The ID of the existing package.
                      - VBScript: String

Compiling the Code
The C# example requires:

Namespaces
System

<!-- p.1285 -->

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security

See Also
Software distribution overview SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1286 -->

How to Assign a Package to a
Distribution Point
Article • 10/04/2022

The following example shows how to assign a distribution point to a package by using
the SMS_DistributionPoint and SMS_SystemResourceList classes in Configuration
Manager. You only need to assign a distribution point to a package if the package
contains source files (PkgSourcePath). The package is not advertised until the program
source files have been propagated to a distribution point share. You can use the default
distribution point share, or you can specify a share to use. You can also specify more
than one distribution point to use to distribute your package source files, although this
example does not demonstrate that.

To assign a package to a distribution point
   1. Set up a connection to the SMS Provider.

   2. Create a new distribution point object (this is not an actual distribution point).

   3. Associate the existing package with the new distribution point object.

   4. Query for a single distribution point based on the provided site code and server
        name.

   5. Use the query results to populate the ServerNALPath property of the distribution
        point object.

   6. Save the distribution point object and properties.

Example
The following example method assigns a package to a distribution point.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub SWDAssignPackageToDistributionPoint(connection, existingPackageID,
  siteCode, serverName)

<!-- p.1287 -->

     Const wbemFlagReturnImmediately = 16
     Const wbemFlagForwardOnly = 32
     Dim distributionPoint
     Dim query
     Dim listOfResources
     Dim resource

    ' Create distribution point object (this is not an actual distribution
point).
    Set distributionPoint =
connection.Get("SMS_DistributionPoint").SpawnInstance_

     ' Associate the existing package with the new distribution point object.
     distributionPoint.PackageID = existingPackageID

    ' This query selects a single distribution point based on the provided
SiteCode and ServerName.
    query = "SELECT * FROM SMS_SystemResourceList WHERE RoleName='SMS
Distribution Point' AND SiteCode='" & siteCode & "' AND ServerName='" &
serverName & "'"

    Set listOfResources = connection.ExecQuery(query, , wbemFlagForwardOnly
Or wbemFlagReturnImmediately)

    ' The query returns a collection that needs to be enumerated (although
we should only get one instance back).
    For Each resource In ListOfResources
        distributionPoint.ServerNALPath = Resource.NALPath
        distributionPoint.SiteCode = Resource.SiteCode
    Next

     ' Save the distribution point instance for the package.
     distributionPoint.Put_

     ' Display notification text.
     Wscript.Echo "Assigned package: " & distributionPoint.PackageID

End Sub

c#

public void AssignPackageToDistributionPoint(WqlConnectionManager
connection, string existingPackageID, string siteCode, string serverName)
{
    try
    {
        // Create the distribution point object (this is not an actual
distribution point).
        IResultObject distributionPoint =
connection.CreateInstance("SMS_DistributionPoint");

          // Associate the package with the new distribution point object.
          distributionPoint["PackageID"].StringValue = existingPackageID;

<!-- p.1288 -->

          // This query selects a single distribution point based on the
  provided siteCode and serverName.
          string query = "SELECT * FROM SMS_SystemResourceList WHERE
  RoleName='SMS Distribution Point' AND SiteCode='" + siteCode + "' AND
  ServerName='" + serverName + "'";

          //
          IResultObject listOfResources =
  connection.QueryProcessor.ExecuteQuery(query);
          foreach (IResultObject resource in listOfResources)
          {
              Console.WriteLine(resource["SiteCode"].StringValue);
              distributionPoint["ServerNALPath"].StringValue =
  resource["NALPath"].StringValue;
              distributionPoint["SiteCode"].StringValue =
  resource["SiteCode"].StringValue;
          }

              // Save the distribution point object and properties.
              distributionPoint.Put();

          // Output package ID of assigned package.
          Console.WriteLine("Assigned package: " +
  distributionPoint["PackageID"].StringValue);
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create package. Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter            Type                              Description

 connection           - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                      - VBScript: SWbemServices
 swbemServices

 existingPackageID    - Managed: String                 The ID of the existing package.
                      - VBScript: String

 siteCode             - Managed: String                 The site code.
                      - VBScript: String

 serverName           - Managed: String                 The name of the server.

<!-- p.1289 -->

 Parameter           Type                         Description

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
Software distribution overview About the site control file SMS_SCI_Component Server
WMI Class
SMS_SystemResourceList Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1290 -->

About Software Distribution Programs
Article • 10/04/2022

Programs are commands that are associated with a Configuration Manager package
that tell a client what should occur on the client computer when the package is received.
You can associate almost any activity with a program. For example, a program can be
used to install new software on clients, distribute data files, run virus-detection software,
or update client configuration.

Every deployable package must contain at least one program, but you can specify more
than one, if needed. A package can often have several programs associated with it,
allowing the package to be run in different ways on different clients. This is often the
case when you are installing a new application on a client computer and want to create
programs to perform either a typical, minimum, or custom installation.

Although the package contains the application, files, or information that need to be
applied to the client computers, the program is responsible for defining how that
application is to be used. As a result, the program must include all appropriate
references to script files or command switches. The program also defines the platform
and environment in which the package can run, which means that you might have a
program for each suitable platform when you have clients using different operating
systems.

After you create a program for a given package, you can make that program and
package available to a collection of clients by using an advertisement.

See Also
Software distribution overview About deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1291 -->

How to Create a Program
Article • 10/04/2022

The following example shows how to create a program, in Configuration Manager, by
using the SMS_Program class and class properties.

  ） Important

  Any advertised program will fail to run when the maintenance windows that are
  defined on the client computer are set for a period that is less than that program's
  Maximum allowed run time setting. For more information, see Program Run
  Scenario Using Maintenance Windows in the Configuration Manager
  documentation.

To create a program
   1. Set up a connection to the SMS Provider.

   2. Create the new program object by using the SMS_Program class.

   3. Populate the new program properties.

         Tip

        When you create a program for a Task Sequence or a Virtual Application
        Package, the SMS_Program properties must be set to specific values. The
        following tables outline what those settings should be configured to.

      Task Sequence

                                                                        ﾉ   Expand table

       Property Name                             Property Value

       ProgramName                               *

      Virtual Application Package

                                                                        ﾉ   Expand table

<!-- p.1292 -->

        Property       Property Value
        Name

        CommandLine    PkgGUID={E742FFD6-D539-42CC-9827-73535FC81E06}:VersionGUID=
                       {19366289-8C55-44E2-A5EC-7B385EFB4C30}

                       Note: The GUID values are taken from the virtual application's XML
                       manifest file.

        ProgramName    [Virtual application]

   4. Save the new program and properties.

Example
The following example method creates a new program and populates its properties for
use in software distribution.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub CreateProgram(connection, existingPackageID, newProgramName,
  newProgramComment, newProgramCommandLine, newMaxRunTime)

        ' Create the new program object.    Dim newProgram
        Set newProgram = connection.Get("SMS_Program").SpawnInstance_

        ' Populate the program properties.
        newProgram.PackageID = existingPackageID
        newProgram.ProgramName = newProgramName
        newProgram.Comment = newProgramComment
        newProgram.CommandLine = newProgramCommandLine
        newProgram.Duration = newMaxRunTime

        ' Save the new program and properties.
        newProgram.Put_

        ' Output new program name.
        wscript.echo "Created program: " & newProgramName

  End Sub

  c#

<!-- p.1293 -->

  public void CreateProgram(WqlConnectionManager connection,
                            string existingPackageID,
                            string newProgramName,
                            string newProgramComment,
                            string newProgramCommandLine,
                            int newMaxRunTime)
  {
      try
      {
          // Create an instance of SMS_Program.
          IResultObject newProgram = connection.CreateInstance("SMS_Program");

              // Populate basic program values.
              newProgram["PackageID"].StringValue = existingPackageID;
              newProgram["ProgramName"].StringValue = newProgramName;
              newProgram["Comment"].StringValue = newProgramComment;
              newProgram["CommandLine"].StringValue = newProgramCommandLine;
              newProgram["Duration"].IntegerValue = newMaxRunTime;

              // Save the new program instance and values.
              newProgram.Put();

          Console.WriteLine("Created program: " + newProgramName);
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create program. Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter               Type                   Description

 connection              - Managed:             A valid connection to the SMS Provider.
                         WqlConnectionManager
 swebemServices          - VBScript:
                         SWbemServices

 existingPackageID       - Managed: String      The name of the package associated with the
                         - VBScript: String     program.

 newProgramName          - Managed: String      The name for the new program.
                         - VBScript: String

 newProgramComment       - Managed: String      Comment that describes the program in the
                         - VBScript: String     Configuration Manager console.

<!-- p.1294 -->

 Parameter               Type                  Description

 newProgramCommandLine   - Managed: String     The command line that runs when the
                         - VBScript: String    program is launched.

 newMaxRunTime           - Managed: Integer    The approximate duration, in minutes, of
                         - VBScript: Integer   program execution on the client computer.
                                               This parameter can have a max value of 720
                                               minutes or 12 hours.

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
Software distribution overview

Feedback

<!-- p.1295 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1296 -->

How to Modify Program Properties
Article • 10/04/2022

The following example shows how to modify a program, in Configuration Manager, by
using the SMS_Package and SMS_Program classes and properties.

To modify program properties
   1. Set up a connection to the SMS Provider.

   2. Get the program instance using the package ID and program name provided.

   3. Replace the program description property with the one passed into the method.

   4. Save the program object and properties.

Example
The following example method modifies program properties for software distribution.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ModifyProgram(connection, existingpackageID,
  existingProgramNameToModify, newProgramDescription)

       ' Load the specific program to change (programname is a key value and
  must be unique).     Dim program
       Set program = connection.Get("SMS_Program.PackageID='" &
  existingPackageID & "'" & ",ProgramName='" & existingProgramNameToModify &
  "'")

       ' Replace the existing program property (in this case the program
  description).
       program.Description = newProgramDescription
       program.Comment = newProgramDescription
       ' Save the program with the modified properties.
       program.Put_

        ' Output program name.
        WScript.echo "Modified program: " & program.ProgramName

<!-- p.1297 -->

  End Sub

  c#

  public void ModifyProgram(WqlConnectionManager connection, string
  existingPackageID, string existingProgramNameToModify, string
  newProgramDescription)
  {

       try
       {

          // Load the specific program to change (programname is a key value
  and must be unique).
          IResultObject program =
  connection.GetInstance(@"SMS_Program.PackageID='" + existingPackageID +
  "',ProgramName='" + existingProgramNameToModify + "'");

          // Replace the existing program property (in this case the program
  description).
          program["Description"].StringValue = newProgramDescription;
          program["Comment"].StringValue = newProgramDescription;
          // Save the program with the modified properties.
          program.Put();

          // Output program name.
          Console.WriteLine("Modified program: " +
  program["ProgramName"].StringValue);

      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to modify the program. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                        ﾉ   Expand table

 Parameter                 Type                        Description

 connection                - Managed:                  A valid connection to the SMS
                           WqlConnectionManager        Provider.
 swbemServices             - VBScript: SWbemServices

<!-- p.1298 -->

 Parameter                     Type                  Description

 existingPackageID             - Managed: String     The ID of an existing package with
                               - VBScript: String    which to associate the program.

 existingProgramNameToModify   - Managed: String     The name for the program to
                               - VBScript: String    modify.

 newProgramDescription         - Managed: String     The description for the new
                               - VBScript: String    program.

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
Software distribution overview

Feedback

<!-- p.1299 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1300 -->

How to Change the Maximum Run Time
for a Program
Article • 10/04/2022

The following example shows how to modify a program, in Configuration Manager, by
using the SMS_Package and SMS_Program classes and properties.

  ） Important

  Any advertised program fails to run when the maintenance windows defined on the
  client computer are set for a period that is less than that program's Maximum
  allowed run time setting . See the topic "Program Run Scenario Using

  Maintenance Windows" in the Configuration Manager documentation for more
  information.

To change the maximum run time for a program
   1. Set up a connection to the SMS Provider.

   2. Query for the programs associated with the existing package ID provided.

   3. Enumerate through the programs until a match for the program name is found.

   4. Replace the program maximum run time property with the one passed into the
      method.

   5. Save the program object and properties.

Example
The following example method changes the maximum run time for an existing program.

  ７ Note

  A slight variation of this example could change property values for all of the
  programs associated with a specific package. For an example, see the How to List
  All Programs and Their Maximum Run Time Value code example. However, for a

<!-- p.1301 -->

  more efficient method of accessing a specific program, using the PackageID and
  ProgramName , see the How to Modify Program Properties code example.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ModifyProgram(connection, existingpackageID,
  existingProgramNameToModify, newMaxRunTime)

        Const wbemFlagReturnImmediately = 16
        Const wbemFlagForwardOnly = 32
        Dim query
        Dim programsForPackage
        Dim program

      ' Build a query to get the programs for the package.
      query = "SELECT * FROM SMS_Program WHERE PackageID='" &
  existingPackageID & "'"

      ' Run the query.
      Set programsForPackage = connection.ExecQuery(query, ,
  wbemFlagForwardOnly Or wbemFlagReturnImmediately)

        ' The query returns a collection that needs to be enumerated.
        For Each program In programsForPackage

            ' If a match for the program name is found, make the change(s).
            If program.ProgramName=existingProgramNameToModify Then

              ' Replace the existing package property (in this case the
  package description).
              program.Duration = newMaxRunTime

                ' Save the program with the modified properties.
                program.Put_

                ' Output program name.
                wscript.echo "Modified program: "   & program.ProgramName

                Exit For
            End If
        Next

  End Sub

  c#

<!-- p.1302 -->

  public void ModifyProgram(WqlConnectionManager connection, string
  existingPackageID, string existingProgramNameToModify, int newMaxRunTime)
  {

      try
      {
          // Build query to get the programs for the package.
          string query = "SELECT * FROM SMS_Program WHERE PackageID='" +
  existingPackageID + "'";

          // Load the specific program to change (programname is a key value
  and must be unique).
          IResultObject programsForPackage =
  connection.QueryProcessor.ExecuteQuery(query);

          // The query returns a collection that needs to be enumerated.
          foreach(IResultObject program in programsForPackage)
          {
              // If a match for the program name is found, make the change(s).
              if (program["ProgramName"].StringValue ==
  existingProgramNameToModify)
              {
                   // Replace the existing package property (in this case the
  package description).
                   program["Duration"].IntegerValue = newMaxRunTime;

                   // Save the program with the modified properties.
                   program.Put();

                   // Output program name.
                   Console.WriteLine("Modified program: "   +
  program["ProgramName"].StringValue);
              }
          }

      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to modify the program. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                 ﾉ     Expand table

<!-- p.1303 -->

 Parameter                     Type                   Description

 connection                    - Managed:             A valid connection to the SMS
                               WqlConnectionManager   Provider.
 swbemServices                 - VBScript:
                               SWbemServices

 existingPackageID             - Managed: String      The ID of an existing package with
                               - VBScript: String     which to associate the program.

 existingProgramNameToModify   - Managed: String      The name for the program to modify.
                               - VBScript: String

 newMaxRunTime                 - Managed: Integer     New approximate duration, in
                               - VBScript: Integer    minutes, of program execution on
                                                      the client computer.

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

<!-- p.1304 -->

Software distribution overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1305 -->

How to List All Programs and Their
Maximum Run Time Value
Article • 10/04/2022

In Configuration Manager, you can list all programs with their maximum run time values
by using the SMS_Package and SMS_Program classes and class properties.

To list all programs and their maximum run times
   1. Set up a connection to the SMS Provider.

   2. Load the available packages by using the SMS_Package class.

   3. Enumerate through each set of programs using the SMS_Program class and the
        PackageID property from each package.

   4. Output the package name, program name, and maximum run time value for each
        program.

Example
The following example method shows how to list all programs, with corresponding
package name, program name, and maximum run times.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ListPackagesProgramsandMaximumRunTimeValue(connection)
      Const wbemFlagReturnImmediately = 16    Const wbemFlagForwardOnly = 32
  Dim packageQuery    Dim allPackages    Dim package    Dim packageID    Dim
  program    Dim programsForPackage
      ' Build query to get all of the packages.
      packageQuery = "SELECT * FROM SMS_Package"

      ' Run query.
      Set allPackages = connection.ExecQuery(packageQuery, ,
  wbemFlagForwardOnly Or wbemFlagReturnImmediately)

      ' The query returns a collection of package objects that needs to be
  enumerated.
      For Each package In allPackages

<!-- p.1306 -->

          ' Output package name and get the PackageID value to use in program
query.
          WScript.Echo ""
          WScript.Echo "Package: " & package.Name
          packageID = package.PackageID

        ' Build query to get the programs for the package.
        packageQuery = "SELECT * FROM SMS_Program WHERE PackageID='" &
packageID & "'"

        ' Run query.
        Set programsForPackage = connection.ExecQuery(packageQuery, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

        ' The query returns a collection of program objects that needs to be
enumerated.
        For Each program In programsForPackage

                ' Output Maximum Runtime Value for each program found.
                WScript.Echo " Program: " & program.ProgramName
                WScript.Echo " Maximum Runtime Value: " & program.Duration

         Next
     Next

End Sub

c#

public void ListPackagesProgramsandMaximumRunTimeValue(WqlConnectionManager
connection)
{
    try
    {
        // Build query to get the packages.
        string packageQuery = "SELECT * FROM SMS_Package";

        // Load the specific program to change (programname is a key value
and must be unique).
        IResultObject allPackages =
connection.QueryProcessor.ExecuteQuery(packageQuery);

        // The query returns a collection of packages that needs to be
enumerated.
        foreach(IResultObject package in allPackages)
        {
            // Output package name and get the PackageID value to use in
program query.
            Console.WriteLine();
            Console.WriteLine("Package: " + package["Name"].StringValue);

<!-- p.1307 -->

                string packageID = package["PackageID"].StringValue;

              // Build query to get the programs for the package.
              string programQuery = "SELECT * FROM SMS_Program WHERE
  PackageID='" + packageID + "'";

              // Load the all programs belonging to the package.
              IResultObject programsForPackage =
  connection.QueryProcessor.ExecuteQuery(programQuery);

                // The query returns a collection of programs that needs to be
  enumerated.
              foreach(IResultObject program in programsForPackage)
              {
                  // Output Maximum Runtime Value for each program found.
                  Console.WriteLine("   Program: " +
  program["ProgramName"].StringValue);
                  Console.WriteLine("   Maximum Runtime Value: " +
  program["Duration"].IntegerValue);
              }
          }
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to list the packages and programs. Error:
  " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter    Type                              Description

 connection   - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
              - VBScript: SWbemServices

Compiling the Code
The C# example requires:

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.1308 -->

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
Software distribution overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1309 -->

How to Modify the Supported Platforms
for a Program
Article • 10/04/2022

Your application can add supported platforms to a package, in Configuration Manager,
by obtaining specific instances of the SMS_Package and SMS_Program classes and then
adding an instance of the SMS_OS_Details class to the SupportedOperatingSystems
property.

To modify the supported platforms for a program
   1. Set up a connection to the SMS Provider.

   2. Obtain an existing package object by using the SMS_Package class.

   3. Obtain an existing program object by using the SMS_Program class.

   4. Create and populate an instance of the SMS_OS_Details class.

   5. Add the new SMS_OS_Details instance to the SupportedOperatingSystems property
        of the program object (from step 3).

Example
The following example method shows how to add supported platforms for a program.

  ７ Note

  A slight variation of this example could change property values for all of the
  programs associated with a specific package. For an example, see the How to List
  All Programs and Their Maximum Run Time Value code example. However, for a
  more efficient method of accessing a specific program, using the PackageID and
   ProgramName , see the How to Modify Program Properties code example.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

<!-- p.1310 -->

Sub ModifySupportedPlatformsForProgram(connection,          _
                                       existingPackageID,   _
                                       existingProgramName, _
                                       newMaxVersion,       _
                                       newMinVersion,       _
                                       newName,             _
                                       newPlatform)

' Define a constant with the hexadecimal value for RUN_ON_ANY_PLATFORM.
    Const wbemFlagReturnImmediately = 16
    Const wbemFlagForwardOnly = 32
    Const RUN_ON_ANY_PLATFORM = &H08000000
    Dim packageQuery
    Dim package
    Dim allProgramsForPackage
    Dim programQuery
    Dim program
    Dim programPath
    Dim checkPlatformValue
    Dim tempSupportedPlatform
    Dim tempSupportedPlatformsArray
    ' Build a query to get the specified package.
     packageQuery = "SMS_Package.PackageID='" & existingPackageID & "'"
    ' Run the query to get the package.
    Set package = connection.Get(packageQuery)
    ' Output package name and ID.
    WScript.Echo "Package ID:     " & package.PackageID
    WScript.Echo "Package Name:   " & package.Name
    ' Build a query to get the programs for the package.
    programQuery = "SELECT * FROM SMS_Program WHERE PackageID='" &
existingPackageID & "'"
    ' Run the query to get the programs.
    Set allProgramsForPackage = connection.ExecQuery(programQuery, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)
    'The query returns a collection of program objects that needs to be
enumerated.
    For Each program In allProgramsForPackage
        If program.ProgramName = existingProgramName Then
            ' Get all program object properties (in this case we
specifically need some lazy properties).
            programPath = program.Put_
            programPath = Mid(programPath, InStr(1, programPath, ":") + 1)
            Set program = connection.Get(programPath)
            ' Check whether RUN_ON_ANY_PLATFORM is set.
            checkPlatformValue = (program.ProgramFlags AND
RUN_ON_ANY_PLATFORM)
            If checkPlatformValue <> 0 Then
               ' RUN_ON_ANY_PLATFORM is set. Removing RUN_ON_ANY_PLATFORM
value.
                program.ProgramFlags = (program.ProgramFlags XOR
RUN_ON_ANY_PLATFORM)
            End If
            ' Output the program name that is being checked for supported
platforms.

<!-- p.1311 -->

            WScript.Echo "Program Name: " & program.ProgramName
            ' Create
            Set tempSupportedPlatform =
connection.Get("SMS_OS_Details").SpawnInstance_
            ' Populate tempSupportedPlatform values.
            tempSupportedPlatform.MaxVersion = newMaxVersion
            tempSupportedPlatform.MinVersion = newMinVersion
            tempSupportedPlatform.Name       = newName
            tempSupportedPlatform.Platform   = newPlatform
            ' Get the array of supported operating systems.
            tempSupportedPlatformsArray = program.SupportedOperatingSystems
            ' Add the new supported platform values (object) to the
temporary array.
            ReDim Preserve tempSupportedPlatformsArray
(Ubound(tempSupportedPlatformsArray) + 1)
            Set
tempSupportedPlatformsArray(Ubound(tempSupportedPlatformsArray)) =
tempSupportedPlatform
            ' Replace the SupportedOperatingSystems object array with the
new updated array.
            program.SupportedOperatingSystems = tempSupportedPlatformsArray
            ' Save the program.
            program.Put_
            ' Output success message.
            WScript.Echo "Supported Platforms Updated "
        End If
    Next
End Sub

c#

public void ModifyProgramSupportedPlatforms(WqlConnectionManager connection,
                                    string existingPackageID,
                                    string existingProgramNameToModify,
                                    string newMaxVersion,
                                    string newMinVersion,
                                    string newName,
                                    string newPlatform)
{
    try
    {
        // Define a constant with the hexadecimal value for
RUN_ON_ANY_PLATFORM.
        const Int32 RUN_ON_ANY_PLATFORM = 0x08000000;

        // Build query to get the programs for the package.
        string query = "SELECT * FROM SMS_Program WHERE PackageID='" +
existingPackageID + "'";

        // Load the specific program to change (programname is a key value
and must be unique).
        IResultObject programsForPackage =

<!-- p.1312 -->

connection.QueryProcessor.ExecuteQuery(query);

        // The query returns a collection that needs to be enumerated.
        foreach (IResultObject program in programsForPackage)
        {
            // If a match for the program name is found, make the change(s).
            if (program["ProgramName"].StringValue ==
existingProgramNameToModify)
            {
                // Get all properties, specifically the lazy properties, for
the program object.
                program.Get();

                // Check whether RUN_ON_ANY_PLATFORM is already set.
                Int32 checkPlatformValue =
(program["ProgramFlags"].IntegerValue & RUN_ON_ANY_PLATFORM);

                if (checkPlatformValue != 0)
                {
                    // RUN_ON_ANY_PLATFORM is set. Removing
RUN_ON_ANY_PLATFORM value.
                    program["ProgramFlags"].IntegerValue =
program["ProgramFlags"].IntegerValue ^ RUN_ON_ANY_PLATFORM;
                }

                  // Create a new array list to hold the supported platform
window objects.
                List<IResultObject> tempSupportedPlatformsArray = new
List<IResultObject>();

                // Create and populate a temporary SMS_OS_Details object
with the new operating system values.
                IResultObject tempSupportedPlatformsObject =
connection.CreateEmbeddedObjectInstance("SMS_OS_Details");

                // Populate temporary SMS_OS_Details object with the new
supported platforms values.
                tempSupportedPlatformsObject["MaxVersion"].StringValue =
newMaxVersion;
                tempSupportedPlatformsObject["MinVersion"].StringValue =
newMinVersion;
                tempSupportedPlatformsObject["Name"].StringValue = newName;
                tempSupportedPlatformsObject["Platform"].StringValue =
newPlatform;

                // Populate the local array list with the existing supported
platform objects (type SMS_OS_Details).
                tempSupportedPlatformsArray =
program.GetArrayItems("SupportedOperatingSystems");

                  // Add the newly created service window object to the local
array list.

tempSupportedPlatformsArray.Add(tempSupportedPlatformsObject);

<!-- p.1313 -->

                  // Replace the existing service window objects from the
  target collection with the temporary array that includes the new service
  window.
                  program.SetArrayItems("SupportedOperatingSystems",
  tempSupportedPlatformsArray);

                  // Save the new values in the collection settings instance
  associated with the Collection ID.
                  program.Put();

                  // Output program name.
                  Console.WriteLine("Modified program: " +
  program["ProgramName"].StringValue);
               }
          }
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to modify the program. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                        ﾉ   Expand table

 Parameter             Type                        Description

 connection            - Managed:                  A valid connection to the SMS Provider.
                       WqlConnectionManager
                       - VBScript: SWbemServices

 existingPackageID     - Managed: String           The package ID for an existing
                       - VBScript: String          package.

 existingProgramName   - Managed: String           The program name for an existing
                       - VBScript: String          program.

 newMaxVersion         - Managed: String           The maximum supported version.
                       - VBScript: String

 newMinVersionsion     - Managed: String           The minimum supported version.
                       - VBScript: String

 newName               - Managed: String           The modified program name.
                       - VBScript: String

<!-- p.1314 -->

 Parameter               Type                     Description

 newPlatform             - Managed: String        The new platform.
                         - VBScript: String

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

mscorlib

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
Software distribution overview

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.1315 -->

About Software Distribution
Deployments
Article • 01/05/2024

In Configuration Manager, after a software distribution package has been created, with
programs to tell client computers what to do with the package, you need to advertise
the program that you want the clients to run. Advertising the program makes a program
available to a specified collection of clients.

Advertisements are evaluated by Configuration Manager to determine which clients
receive a specific program to run on their computers. An advertisement specifies the
following information:

      The specific program to run on the client.

      The target collection of computers, users, or user groups that are to receive the
      program.

      The schedule that specifies when the program is available to clients. If there are
      assigned (mandatory) advertisements, other options such as Wake On LAN and
      ignoring maintenance windows can be used with this schedule.

      The site's clients can't receive advertised programs until you enable the software
      distribution advertised programs client agent on the site's clients. The Advertised
      Programs Client Agent performs the necessary software distribution-related tasks
      on these clients, primarily allowing the clients to receive and run the programs that
      you advertise.

See Also
About deployments Software distribution overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1316 -->

How to create a deployment
Article • 10/04/2022

The following examples show how to create a Configuration Manager deployment with
the SMS_Advertisement class and its properties.

  ） Important

  The account that creates the deployment needs the Deploy Packages permission
  for the collection and Read permission for the package.

Overview
   1. Set up a connection to the SMS Provider.

   2. Create a new object of the SMS_Advertisement class.

   3. Populate the new advertisement properties.

   4. Save the new advertisement and properties.

Examples
The following examples create an advertisement for software distribution.

For more information about calling the sample code, see Calling Configuration Manager
code snippets.

  vbs

  Sub SWDCreateAdvertisement(connection, existingCollectionID,
  existingPackageID, existingProgramName, newAdvertisementName,
  newAdvertisementComment, newAdvertisementFlags, newRemoteClientFlags,
  newAdvertisementStartOfferDateTime, newAdvertisementStartOfferEnabled)
      Dim newAdvertisement
      ' Create the new advertisement object.
      Set newAdvertisement =
  connection.Get("SMS_Advertisement").SpawnInstance_

        ' Populate the advertisement properties.
        newAdvertisement.CollectionID = existingCollectionID
        newAdvertisement.PackageID = existingPackageID
        newAdvertisement.ProgramName = existingProgramName
        newAdvertisement.AdvertisementName = newAdvertisementName

<!-- p.1317 -->

     newAdvertisement.Comment = newAdvertisementComment
     newAdvertisement.AdvertFlags = newAdvertisementFlags
     newAdvertisement.RemoteClientFlags = newRemoteClientFlags
     newAdvertisement.PresentTime = newAdvertisementStartOfferDateTime
     newAdvertisement.PresentTimeEnabled = newAdvertisementStartOfferEnabled

     ' Save the new advertisement and properties.
     newAdvertisement.Put_

    ' Output new advertisement name.
    Wscript.Echo "Created advertisement: " &
newAdvertisement.AdvertisementName

End Sub

c#

public void CreateSWDAdvertisement(WqlConnectionManager connection, string
existingCollectionID, string existingPackageID, string existingProgramName,
string newAdvertisementName, string newAdvertisementComment, int
newAdvertisementFlags, int newRemoteClientFlags, string
newAdvertisementStartOfferDateTime, bool newAdvertisementStartOfferEnabled)
{
    try
    {
        // Create new advertisement instance.
        IResultObject newAdvertisement =
connection.CreateInstance("SMS_Advertisement");

        // Populate new advertisement values.
        newAdvertisement["CollectionID"].StringValue = existingCollectionID;
        newAdvertisement["PackageID"].StringValue = existingPackageID;
        newAdvertisement["ProgramName"].StringValue = existingProgramName;
        newAdvertisement["AdvertisementName"].StringValue =
newAdvertisementName;
        newAdvertisement["Comment"].StringValue = newAdvertisementComment;
        newAdvertisement["AdvertFlags"].IntegerValue =
newAdvertisementFlags;
        newAdvertisement["RemoteClientFlag"].IntegerValue =
newRemoteClientFlags;
        newAdvertisement["PresentTime"].StringValue =
newAdvertisementStartOfferDateTime;
        newAdvertisement["PresentTimeEnabled"].BooleanValue =
newAdvertisementStartOfferEnabled;

          // Save the new advertisement and properties.
          newAdvertisement.Put();

        // Output new assignment name.
        Console.WriteLine("Created advertisement: " +
newAdvertisement["AdvertisementName"].StringValue);
    }

<!-- p.1318 -->

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to assign advertisement. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter                            Type                   Description

 connection                           - Managed:             A valid connection to the SMS
                                      WqlConnectionManager   Provider.
 swbemServices                        - VBScript:
                                      SWbemServices

 existingCollectionID                 String                 The ID of an existing collection
                                                             with which to associate the
                                                             advertisement.

 existingPackageID                    String                 The ID of an existing package
                                                             with which to associate the
                                                             advertisement.

 existingProgramName                  String                 The name for the program
                                                             associated with the
                                                             advertisement.

 newAdvertisementName                 String                 The name for the new
                                                             advertisement.

 newAdvertisementComment              String                 A comment for the new
                                                             advertisement.

 newAdvertisementFlags                Integer                Flags specifying options for the
                                                             new advertisement.

 newRemoteClientFlags                 Integer                Flags specifying how the
                                                             program should run when the
                                                             client connects either locally or
                                                             remotely to a distribution point.

 newAdvertisementStartOfferDateTime   String                 The time when the new
                                                             advertisement is first offered.

 newAdvertisementStartOfferEnabled    Boolean                true if the advertisement is
                                                             offered.

<!-- p.1319 -->

Compiling the code
The C# example requires:

Namespaces
      System

      Microsoft.ConfigurationManagement.ManagementProvider

      Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
      adminui.wqlqueryengine

      microsoft.configurationmanagement.managementprovider

      mscorlib

Robust programming
For more information about error handling, see About Configuration Manager errors.

See also
     Software distribution overview
     About deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1320 -->

How to Assign an Advertisement to a
Collection of Computers
Article • 10/04/2022

You can assign an advertisement to a collection by using the SMS_Advertisement class in
Configuration Manager. Advertisements are closely tied to packages, programs and
collections. For more information, see Software Distribution Overview.

  ７ Note

  Detailed information about the SMS_Advertisement class and class properties is in
  the reference section of the Configuration Manager Software Development Kit
  (SDK).

To assign an advertisement to a collection
   1. Set up a connection to the SMS Provider.

   2. Get the specific advertisement using the existing advertisement ID.

   3. Populate the advertisement collection ID property with the existing collection ID.

   4. Save the advertisement and properties.

Example
The following example method assigns a specific advertisement to a collection for use in
software distribution.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub SWDAssignAdvertisementCollection(connection, existingAdvertisementID,
  existingCollectionID)

      ' Get the specific advertisement object.
      Set advertisementToAssign =
  connection.Get("SMS_Advertisement.AdvertisementID='" &
  existingAdvertisementID & "'")
