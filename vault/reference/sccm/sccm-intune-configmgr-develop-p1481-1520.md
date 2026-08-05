---
title: "Configuration Manager SDK documentation — pages 1481-1520"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1481-1520
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1481-1520
family: sccm
documentKind: "doc"
abstract: "Console.WriteLine(\"Error: \" + ex.Message); throw; } } The example method has the following parameters: ﾉ Expand table Parameter Type Description connection - Managed: A valid connection to the SMS Provider. WqlConnectionManager existingSUMPackageID - Managed: String The package"
---

# Configuration Manager SDK documentation — pages 1481-1520

<!-- p.1481 -->

              Console.WriteLine("Error: " + ex.Message);
              throw;
      }
  }

The example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter                    Type                    Description

 connection                   - Managed:              A valid connection to the SMS Provider.
                              WqlConnectionManager

 existingSUMPackageID         - Managed: String       The package ID for an existing software
                                                      updates deployment package.

 addUpdateContentParameters   - Managed: dictionary   The set of parameters ( ContentIDs ,
                              object                  ContentSourcePath , bRefreshDPs ) that is
                                                      passed into the method and used with
                                                      the AddUpdateContent method call.

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

<!-- p.1482 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About software update deployments How to Assign a Package to a Distribution Point
SMS_SoftwareUpdatesPackage
AddUpdateContent Method in Class SMS_SoftwareUpdatesPackage

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1483 -->

How to Delete Updates from a
Deployment Package
Article • 10/04/2022

You remove updates from a software updates deployment package, in Configuration
Manager, by obtaining an instance of the SMS_SoftwareUpdatesPackage class and using
the RemoveContent method.

To delete updates from a software updates deployment
package
   1. Set up a connection to the SMS Provider.

   2. Obtain an existing package object by using the SMS_SoftwareUpdatesPackage class.

   3. Remove update content from the existing software updates management package
       by using the RemoveContent method.

Example
The following example method shows how to remove updates from a software updates
deployment package by using the SMS_SoftwareUpdatesPackage class and the
RemoveContent method.

  ） Important

  No VBScript example was included, as the RemoveContent method does not return
  from the method call on failure. This is a known issue and is being investigated.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

Example of the method call in C#:

  C#

  // Prework for RemoveUpdatesfromSUMDeploymentPackage.
  // Define the array of Content IDs to load into the content parameters.
  int[] newArrayContentIDs2 = new int[] { 82 };

<!-- p.1484 -->

  // Load the update content parameters into an object to pass to the method.
  Dictionary<string, object> removeContentParameters = new Dictionary<string,
  object>();
  removeContentParameters.Add("ContentIDs", newArrayContentIDs2);
  removeContentParameters.Add("bRefreshDPs", true);

  // Call the RemoveUpdatesfromSUMDeploymentPackage method.
  RemoveUpdatesfromSUMDeploymentPackage(WMIConnection,
                                        "ABC00001",
                                        removeContentParameters);

  C#

  public void RemoveUpdatesfromSUMDeploymentPackage(WqlConnectionManager
  connection,
                                                    string
  existingSUMPackageID,
                                                    Dictionary<string, object>
  removeContentParameters)
  {
      try
      {
          // Get the specific SUM Deployment Package to change.
          IResultObject existingSUMDeploymentPackage =
  connection.GetInstance(@"SMS_SoftwareUpdatesPackage.PackageID='" +
  existingSUMPackageID + "'");

          // Remove updates from the existing SUM Deployment Package using the
  RemoveContent method.
          // Note: The method will throw an exception, if the method is not
  able to add the content.
          IResultObject result =
  existingSUMDeploymentPackage.ExecuteMethod("RemoveContent",
  removeContentParameters);

          // Output a success message.
          Console.WriteLine("Removed content from the deployment package. ");

      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to remove content from the deployment
  package. Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

<!-- p.1485 -->

                                                                            ﾉ   Expand table

 Parameter                 Type                    Description

 connection                - Managed:              A valid connection to the SMS Provider.
                            WqlConnectionManager

 existingSUMPackageID      - Managed: String       The package ID for an existing software
                                                   updates management package.

 removecontentParameters   - Managed: dictionary   The set of parameters ( ContentIDs ,
                           object                  bRefreshDPs ) that is passed into the
                                                   method and used with the RemoveContent
                                                   method call.

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

<!-- p.1486 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About software update deployments How to Assign a Package to a Distribution Point
SMS_SoftwareUpdatesPackage
RemoveContent Method in Class SMS_SoftwareUpdatesPackage

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1487 -->

How to Configure and Deploy Updates
Article • 10/04/2022

You create a software updates deployment, in Configuration Manager, by creating an
instance of the SMS_UpdatesAssignment Server WMI Class and populating the
properties.

To configure and deploy updates
   1. Set up a connection to the SMS Provider.

   2. Create the new deployment object by using the SMS_UpdatesAssignment class.

   3. Populate the new deployment properties.

   4. Save the new deployment and properties.

Example
The following example method shows how to create a software updates deployment by
using the SMS_UpdatesAssignment class. Note that the parameters of the example
method reflect certain properties of SMS_UpdatesAssignment .

  ） Important

  The methods below require an array of the assigned configuration items (CI_IDs).
  The update content for these CI_IDs must have already been downloaded and
  added to an updates deployment package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureAndDeploySUMUpdates(connection,                                   _
                                    newApplyToSubTargets,                        _
                                    newArrayAssignedCIs,                         _
                                    newAssignmentAction,                         _
                                    newAssignmentDescription,                    _
                                    newAssignmentName,                           _
                                    newDesiredConfigType,                        _
                                    newDPLocality,                               _

<!-- p.1488 -->

                                    newLocaleID,                          _
                                    newLogComplianceToWinEvent,           _
                                    newNotifyUser,                        _
                                    newRaiseMomAlertsOnFailure,           _
                                    newSendDetailedNonComplianceStatus,   _
                                    newStartTime,                         _
                                    newSuppressReboot,                    _
                                    newTargetCollectionID,                _
                                    newUseGMTTimes)

  ' Create the new deployment object.
  Set newSUMUpdatesAssignment =
connection.Get("SMS_UpdatesAssignment").SpawnInstance_

  ' Populate the deployment properties.
  newSUMUpdatesAssignment.ApplyToSubTargets = newApplyToSubTargets
  newSUMUpdatesAssignment.AssignedCIs = newArrayAssignedCIs
  newSUMUpdatesAssignment.AssignmentAction = newAssignmentAction
  newSUMUpdatesAssignment.AssignmentDescription = newAssignmentDescription
  newSUMUpdatesAssignment.AssignmentName = newAssignmentName
  newSUMUpdatesAssignment.DesiredConfigType = newDesiredConfigType
  newSUMUpdatesAssignment.DPLocality = newDPLocality
  newSUMUpdatesAssignment.LocaleID = newLocaleID
  newSUMUpdatesAssignment.LogComplianceToWinEvent =
newLogComplianceToWinEvent
  newSUMUpdatesAssignment.NotifyUser = newNotifyUser
  newSUMUpdatesAssignment.RaiseMomAlertsOnFailure =
newRaiseMomAlertsOnFailure
  newSUMUpdatesAssignment.SendDetailedNonComplianceStatus =
newSendDetailedNonComplianceStatus
  newSUMUpdatesAssignment.StartTime = newStartTime
  newSUMUpdatesAssignment.SuppressReboot = newSuppressReboot
  newSUMUpdatesAssignment.TargetCollectionID = newTargetCollectionID
  newSUMUpdatesAssignment.UseGMTTimes = newUseGMTTimes

     ' Save the new deployment and properties.
     newSUMUpdatesAssignment.Put_

  ' Output the new deployment name.
  Wscript.Echo "Created new deployment " &
newSUMUpdatesAssignment.AssignmentName

End Sub

c#

public void ConfigureAndDeploySUMUpdates(WqlConnectionManager connection,
                                        bool newApplyToSubTargets,
                                        int[] newArrayAssignedCIs,
                                        int newAssignmentAction,
                                        string newAssignmentDescription,

<!-- p.1489 -->

                                         string newAssignmentName,
                                         int newDesiredConfigType,
                                         int newDPLocality,
                                         int newLocaleID,
                                         bool newLogComplianceToWinEvent,
                                         bool newNotifyUser,
                                         bool newRaiseMomAlertsOnFailure,
                                         bool
newSendDetailedNonComplianceStatus,
                                         string newStartTime,
                                         int newSuppressReboot,
                                         string newTargetCollectionID,
                                         bool newUseGMTTimes)
{
    try
    {

        // Create the deployment object.
        IResultObject newSUMUpdatesAssignment =
connection.CreateInstance("SMS_UpdatesAssignment");

          // Populate new deployment properties.
          // Note: newTemplateName must be unique.

        newSUMUpdatesAssignment["ApplyToSubTargets"].BooleanValue =
newApplyToSubTargets;
        newSUMUpdatesAssignment["AssignedCIs"].IntegerArrayValue =
newArrayAssignedCIs;
        newSUMUpdatesAssignment["AssignmentAction"].IntegerValue =
newAssignmentAction;
        newSUMUpdatesAssignment["AssignmentDescription"].StringValue =
newAssignmentDescription;
        newSUMUpdatesAssignment["AssignmentName"].StringValue =
newAssignmentName;
        newSUMUpdatesAssignment["DesiredConfigType"].IntegerValue =
newDesiredConfigType;
        newSUMUpdatesAssignment["DPLocality"].IntegerValue = newDPLocality;
        newSUMUpdatesAssignment["LocaleID"].IntegerValue = newLocaleID;
        newSUMUpdatesAssignment["LogComplianceToWinEvent"].BooleanValue =
newLogComplianceToWinEvent;
        newSUMUpdatesAssignment["NotifyUser"].BooleanValue = newNotifyUser;
        newSUMUpdatesAssignment["RaiseMomAlertsOnFailure"].BooleanValue =
newRaiseMomAlertsOnFailure;

newSUMUpdatesAssignment["SendDetailedNonComplianceStatus"].BooleanValue =
newSendDetailedNonComplianceStatus;
        newSUMUpdatesAssignment["StartTime"].DateTimeValue = newStartTime;
        newSUMUpdatesAssignment["SuppressReboot"].IntegerValue =
newSuppressReboot;
        newSUMUpdatesAssignment["TargetCollectionID"].StringValue =
newTargetCollectionID;
        newSUMUpdatesAssignment["UseGMTTimes"].BooleanValue =
newUseGMTTimes;

          // Save new deployment and new deployment properties.

<!-- p.1490 -->

              newSUMUpdatesAssignment.Put();

              // Output the new deployment name.
              Console.WriteLine("Created deployment: " + newAssignmentName);
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create newSUMUpdatesAssignment. Error:
  " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter                          Type                   Description

 Connection                         - Managed:             A valid connection to the SMS
                                    WqlConnectionManager   Provider.
                                    - VBScript:
                                    SWbemServices

 newApplyToSubTargets               - Managed: Boolean     Determines whether the
                                    - VBScript: Boolean    deployment applies to
                                                           subtargets.

                                                           - True
                                                           - False

 newArrayAssignedCIs                - Managed: Integer     An array of the assigned
                                    array                  configuration items (CI_IDs). The
                                    - VBScript: Integer    update content for these CI_IDs
                                    array                  must have already been
                                                           downloaded and added to an
                                                           updates deployment package.

 newAssignmentAction                - Managed: Integer     The new assignment action.
                                    - VBScript: Integer

 newAssignmentDescription           - Managed: String      The new assignment description.
                                    - VBScript: String

 newAssignmentName                  - Managed: String      The new assignment name.
                                    - VBScript: String

<!-- p.1491 -->

Parameter                            Type                  Description

newDesiredConfigType                 - Managed: Integer    The new desired configuration
                                     - VBScript: Integer   type.

newDPLocality                        - Managed: Integer    The new distribution point
                                     - VBScript: Integer   locality.

newLocaleID                          - Managed: Integer    The new locale ID.
                                     - VBScript: Integer

newLogComplianceToWinEvent           - Managed: Boolean    Determines whether compliance
                                     - VBScript: Boolean   is logged to the Windows Event
                                                           log.

                                                           - True
                                                           - False

newNotifyUser                        - Managed: Boolean    Identifies whether users are
                                     - VBScript: Boolean   notified.

                                                           - True
                                                           - False

newRaiseMomAlertsOnFailure           - Managed: Boolean    Identifies whether MOM alerts
                                     - VBScript: Boolean   are raised on failure.

                                                           - True
                                                           - False

newSendDetailedNonComplianceStatus   - Managed: Boolean    Identifies whether detailed
                                     - VBScript: Boolean   noncompliance status is sent.

                                                           - True
                                                           - False

newStartTime                         - Managed: String     The new start time.
                                     - VBScript: String

newSuppressReboot                    - Managed: Integer    Identifies whether reboot is
                                     - VBScript: Integer   suppressed.

newTargetCollectionID                - Managed: String     The new target collection IDs.
                                     - VBScript: String

newUseGMTTimes                       - Managed: Boolean    Identifies whether to use
                                     - VBScript: Boolean   Coordinated Universal Time
                                                           (UTC).

<!-- p.1492 -->

 Parameter                        Type                  Description

                                                        - True
                                                        - False

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
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See also
About software update deployments

SMS_UpdatesAssignment

<!-- p.1493 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1494 -->

How to Change the Deployment
Package Source
Article • 10/04/2022

You change the deployment package source for a software updates deployment
package, in Configuration Manager, by obtaining an instance of the
SMS_SoftwareUpdatesPackage class and by using the ValidateNewPackageSource
method.

  ７ Note

  The package source for most other types of packages can be changed in the
  console. However, this option is not available for software updates packages.

To change the deployment package source
   1. Set up a connection to the SMS Provider.

   2. Obtain an existing package object by using the SMS_SoftwareUpdatesPackage class.

   3. Verify the package source by using the ValidateNewPackageSource method.

   4. Change the package source for an existing software updates deployment package
      by changing the PkgSourcePath property of the package.

Example
The following example method shows how to change the deployment package source
for a software updates deployment package by using the SMS_SoftwareUpdatesPackage
class and the ValidateNewPackageSource method.

  ７ Note

  All of the updates available in the old package source must be available in the new
  package source (the content source path, passed in as the
   newPackageSourceLocation variable in the below scripts).

<!-- p.1495 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

Example of the subroutine call in Visual Basic:

  Visual Basic Script

  ' PREWORK FOR ChangeDeploymentPackageSource

  ' Define the new package location to validate (package location must be
  UNC).
  newPackageSourceLocation = "\\SMSSERVER\source1"

  Call ChangeDeploymentPackageSource(swbemServices,                  _
                                     "ABC00003",                     _
                                     newPackageSourceLocation)

Example of the method call in C#:

  C#

  //PREWORK FOR ChangeDeploymentPackageSource.

  // Define the new package location to validate (package location must be
  UNC).
  string newPackageSourceLocation = "\\\\SMSSERVER\\source1";

  // Load the validateNewPackageSource parameters into an object to pass to
  the method.
  Dictionary<string, object> validateNewPackageSourceParameters = new
  Dictionary<string, object>();
  validateNewPackageSourceParameters.Add("PackageSource",
  newPackageSourceLocation);

  //The method call.
  SUMSnippets.ChangeDeploymentPackageSource(WMIConnection,
                                            "ABC00003",

  validateNewPackageSourceParameters,
                                                  newPackageSourceLocation);

  Visual Basic Script

  Sub ChangeDeploymentPackageSource(connection,                   _
                                    existingSUMPackageID,         _
                                    newDeploymentPackageLocation)

<!-- p.1496 -->

     On Error Resume Next

    ' Get an existing SUM Deployment Package to change.
    Set existingSUMDeploymentPackage =
connection.Get("SMS_SoftwareUpdatesPackage.PackageID='" &
existingSUMPackageID & "'")

    ' Check the package source for the existing SUM Deployment Package using
the ValidateNewPackageSource method.

existingSUMDeploymentPackage.ValidateNewPackageSource(newDeploymentPackageLo
cation)

    ' Check the error information from the SWBemLasError object to determine
success or failure of the ValidateNewPackageSource method.
    If Err.Number = 0 Then

        ' Output a success message if the new package location is valid.
        Wscript.Echo "The new location of the SUM deployment package
validated. "
        Wscript.Echo "Updating the SUM deployment package with the new
package location. "

          ' Update the StoredPkgPath property of the existing deployment
package
       ' with the new source location if the package location is valid.
       existingSUMDeploymentPackage.PkgSourcePath =
newDeploymentPackageLocation

          ' Save the updated package deployment package.
          existingSUMDeploymentPackage.Put_

     Else

        ' Output a failure message if the new deployment package location is
not valid.
        Wscript.Echo "The new location of the SUM deployment package failed
to validate. "

     End If

 End Sub

C#

public void ChangeDeploymentPackageSource(WqlConnectionManager connection,
                                          string existingSUMPackageId,
                                          Dictionary<string, object>
validateNewPackageSourceParameters,
                                          string newPackageSource)

<!-- p.1497 -->

  {
      try
      {
          // Get the specific SUM Deployment Package to change.
          IResultObject existingSUMDeploymentPackage =
  connection.GetInstance(@"SMS_SoftwareUpdatesPackage.PackageId='" +
  existingSUMPackageId + "'");

          // Validate the existing SUM Deployment Package content using the
  ValidateContent method.
          // Note: The method will throw an exception, if the package source
  does not validate.

  existingSUMDeploymentPackage.ExecuteMethod("ValidateNewPackageSource",
  validateNewPackageSourceParameters);

          // Output a success message if the new package location is valid.
          Console.WriteLine("The new location of the SUM deployment package
  validated. ");

          // Update the PkgSourcePath property of the existing deployment
  package with the new source location.
          existingSUMDeploymentPackage["PkgSourcePath"].StringValue =
  newPackageSource;

              // Save the package properties.
              existingSUMDeploymentPackage.Put();

          // Output a success message that the package location was updated.
          Console.WriteLine("Updated the SUM deployment package with the new
  package location. ");
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to validate the new package source.");
          Console.WriteLine("Failed to update the SUM deployment package.");
          Console.WriteLine("Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter                 Type                    Description

 connection                - Managed:              A valid connection to the SMS Provider.
                            WqlConnectionManager
                           - VBScript:
                           SWbemServices

<!-- p.1498 -->

 Parameter                  Type                 Description

 existingSUMPackageID       - Managed: String    The package ID for an existing software
                            - VBScript: String   updates deployment package.

 validateNewPackageSource   - Managed:           The validateNewPackageSource is a
                             dictionary object   dictionary object containing the
                                                 parameters that the
                                                 ValidateNewPackageSource method
                                                 requires.

                                                 PackageSource

 newPackageSourceLocation   - Managed: String    The new deployment package source
                            - VBScript: String   location. The source path must be a
                                                 Universal Naming Convention (UNC) path.
                                                 All of the updates available in the old
                                                 package source must be available in the
                                                 new package source.

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

<!-- p.1499 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About software update deployments SMS_SoftwareUpdatesPackage
ValidateNewPackageSource Method in Class SMS_SoftwareUpdatesPackage

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1500 -->

About Synchronizing the Software
Update Point
Article • 10/04/2022

In Configuration Manager, software updates must be synchronized before the update
information is available in the Configuration Manager console. Synchronization is
initiated at the highest level site in the hierarchy that has a software update point.

For more information about software updates, see Deploy and manage software
updates.

Software Updates Synchronization
Software updates synchronization in Configuration Manager is the process of retrieving
the software updates metadata that meet the configured criteria from the upstream
Windows Server Update Services (WSUS) server or from Microsoft Update. The highest
site in the Configuration Manager hierarchy with a software update point (most likely
the central site) synchronizes with Microsoft Update. This synchronization can be
scheduled as part of the software update point properties, or it can be manually
initiated.

There are two types of synchronization:

      A full synchronization, which synchronizes the whole catalog of updates on the
      WSUS server. At the end of the full synchronization, the Configuration Manager
      database will match the content of WSUS filtered by the current subscription.

      A delta synchronization, which synchronizes only changes (adds and removals) that
      occurred since the last successful synchronization. A delta synchronization won't
      examine any updates synchronized earlier and not changed since.

  ） Important

  While they are nearly identical functionally, a full synchronization will potentially
  repair updates from previous synchronizations that have gotten damaged or
  deleted. A delta synchronization will not repair any updates from previous
  synchronizations.

in Configuration ManagerSP1 most synchronizations, both manual and scheduled,
perform a delta synchronization. A synchronization will escalate to a full synchronization

<!-- p.1501 -->

if there are configuration changes that require a full synchronization, such as: switching
to a different default SUP, changes in the subscription, changes in the supersedence
mode or window. A synchronization will also escalate to a full synchronization
periodically every 7 days (a period configurable in the site control file under "Full Sync
Interval (days)").

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1502 -->

How to Synchronize with the Software
Update Point
Article • 10/10/2022

You synchronize the software update point, in Configuration Manager SP1, by calling the
SyncNow method.

To synchronize the software update point
   1. Set up a connection to the SMS Provider.

   2. Create an instance of the SMS_SoftwareUpdate Server WMI Class class.

   3. Create and populate the method parameter value fullSync .

   4. Call the SyncNow Method in Class SMS_SoftwareUpdate method, passing in the
       method parameter value.

Example
The following example method shows how to synchronize the software update point by
calling the SyncNow Method in Class SMS_SoftwareUpdate method.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void SynchronizeSoftwareUpdatePoint(WqlConnectionManager connection)
  {
      try
      {

          // Create the new SMS_SoftwareUpdate object.
          IResultObject newSoftwareUpdate =
  connection.CreateInstance("SMS_SoftwareUpdate");

            // Create dictionary object to pass parameters to the SyncNow
  method.
            Dictionary<string, object> inParams = new Dictionary<string, object>
  ();
            inParams["fullSync"] = true;

<!-- p.1503 -->

          // Initialize the outParams object.
          IResultObject outParams = null;
          // Call SyncNow method to initiate synchronization.
          outParams = connection.ExecuteMethod("SMS_SoftwareUpdate",
  "SyncNow", inParams);

      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
      }
  }

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter    Type                              Description

 connection   - Managed: WqlConnectionManager   A valid connection to the SMS Provider.

Compiling the Code
The C# example has the following compilation requirements:

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

<!-- p.1504 -->

For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About software update deployments SMS_SoftwareUpdate Server WMI Class
SyncNow Method in Class SMS_SoftwareUpdate

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1505 -->

How to Configure Software Updates to
Override Maintenance Windows
Article • 10/04/2022

You configure software updates to override maintenance windows, in Configuration
Manager, by updating the OverrideServiceWindows property of an assignment
(deployment).

To configure software updates to override maintenance
windows
   1. Set up a connection to the SMS Provider.

   2. Load the specific assignment (deployment) to modify using the
        SMS_UpdatesAssignment class.

   3. Set the OverrideServiceWindows value to true .

   4. Save the assignment (deployment) and properties.

Example
The following example method shows how to configure software updates to override
maintenance windows by using the SMS_UpdatesAssignment class and class properties.

  ７ Note

  This task only applies to mandatory deployments.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureSoftwareUpdatestoOverrideMaintenanceWindow(connection,
  existingAssignmentID)

      ' Get the specific SMS_UpdatesAssignment instance to modify.
      Set assignmentToModify =
  connection.Get("SMS_UpdatesAssignment.AssignmentID=" & existingAssignmentID

<!-- p.1506 -->

  & "")

       ' Set the new property value.
       assignmentToModify.OverrideServiceWindows = true

       ' Save the assignment.
       assignmentToModify.Put_

      ' Output the new property values.
      Wscript.Echo " "
      Wscript.Echo "Set assignment " & existingAssignmentID & " to override
  service windows."

  End Sub

  c#

  public void
  ConfigureSoftwareUpdatestoOverrideMaintenanceWindow(WqlConnectionManager
  connection, int existingAssignmentID)
  {
      try
      {
          // Get the specific SMS_UpdatesAssignment instance to change.
          IResultObject updatesAssignmentToChange =
  connection.GetInstance(@"SMS_UpdatesAssignment.AssignmentID=" +
  existingAssignmentID);

            // Set OverrideServiceWindows property.
            updatesAssignmentToChange["OverrideServiceWindows"].BooleanValue =
  true;

            // Save property changes.
            updatesAssignmentToChange.Put();

          // Output success message.
          Console.WriteLine("Set assignment " + existingAssignmentID + " to
  override service windows.");
      }

       catch (SmsException ex)
       {
           Console.WriteLine("Failed to .... Error: " + ex.Message);
           throw;
       }
  }

The example method has the following parameters:

<!-- p.1507 -->

                                                                       ﾉ   Expand table

 Parameter              Type                        Description

 connection             - Managed:                  A valid connection to the SMS
                        WqlConnectionManager        Provider.
                        - VBScript: SWbemServices

 existingAssignmentID   - Managed: Integer          An existing Assignment ID to modify.
                        - VBScript: Integer

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
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

<!-- p.1508 -->

See also
SMS_UpdatesAssignment

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1509 -->

About Configuration Manager Status
Messages
Article • 10/04/2022

In Configuration Manager, status messages are the universal means for components to
communicate information about their health to the Configuration Manager
administrator. Status messages are similar to Windows NT Events; they have a severity,
ID, description, and so on.

The Configuration Manager Status System is a fully-distributed, enterprise-wide
aggregation and summarization system for status messages. Status messages flow from
components to the Configuration Manager site servers and up the Configuration
Manager site hierarchy.

The administrator configures how Configuration Manager processes the status
messages at each site server in the hierarchy. This processing can include storing the
status messages in a SQL Server database, replicating the messages to the parent
Configuration Manager site, reporting the messages as Windows Events on the site
server, and exporting the messages to another eventing or alerting application.

Certain kinds of status messages are automatically processed by Summarizer
components that are running on the site servers. The Summarizers produce high-level
data about the raw flows of status messages. Administrators monitor this data in the
Configuration Manager console.

Status messages are similar to Windows events; they have a severity, ID, and description.
They also support message insertion strings and named attribute values. This allows
user-defined messages to be reported through the site.

Types of Status Messages

Predefined Status Messages
Each Configuration Manager component has a set of predefined status messages
assigned to it. It's important that the context in which an application reports a
predefined status message matches exactly the purpose of the Configuration Manager
component status message. Otherwise, the integrity of the site might be affected by
Configuration Manager misinterpreting the meaning of the status message. For more
information, see About Configuration Manager Component Status Messages.

<!-- p.1510 -->

User-defined Generic Status Messages
Configuration Manager provides three types of user-defined generic status messages.

     Information

     Warning

     Error

     Along with the message type, insertion strings and attributes can be supplied. The
     text that is provided as the insertion string, when creating the status message, is
     the text seen in the user interface. This makes using generic messages simple, but
     it doesn't allow for localization. For more information, see How to Read User-
     Defined Status Messages.

Creating Status Messages on the Client
You can create events on client computers in the following ways:

SMSEvent
SMSEvent Class is a COM automation class that you use to raise user-defined status
messages on a client. As a COM Automation object, it can readily be used by VBScript.
For more information, see SMSEvent Class.

SMSCSTAT.DLL
SMSCSTAT.DLL is a Win32 dynamic link library that is available on clients. It has been
installed on Configuration Manager clients since SMS 2.0 Service Pack 1. It can't be
easily be used by VBScript. For more information, see About Using SMSCSTAT.DLL to
Create Status Messages.

Management Point Interface
Using the management point interfaces, you can raise status messages that are defined
by XML from client computers. The management point interfaces can't be used by
VBScript. Using the management point interface is recommended for raising status
messages on client computers that aren't running a Windows operating system.

Creating Status Messages on the Site Server

<!-- p.1511 -->

You raise events on the server by creating instances of SMS_StatusMessage . For more
information, see How to Report User-Defined Status Messages.

See Also
About Using SMSCSTAT.DLL to Create Status Messages
How to Report User-Defined Status Messages
How to Read User-Defined Status Messages
SMSEvent Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1512 -->

About Configuration Manager
Component Status Messages
Article • 10/04/2022

The message text for both the Configuration Manager components and the raw user-
defined messages is contained in message DLLs. The SMS_StatMsgInsStrings Server
WMI Class class contains the insertion strings for those messages that use insertion
strings. To read the SMS component and raw user-defined messages, you must know
the message DLL that contains the message text.

  ７ Note

  If the status message is in Srvmsgs.dll, Provmsgs.dll, or Climmsgs.dll, you can use
  FormatModuleMessage Method to resolve the message.

You can get the DLL name from the SMS_StatMsgModuleNames Server WMI Class. The
SMS_StatMsgModuleNames Server WMI Class class contains the ModuleName and
MsgDLLName properties. You can use ModuleName to join the
SMS_StatMsgModuleNames class with the SMS_StatusMessage class, as the following

example shows.

  // Note that this query returns all the instances found in the
  SMS_Status_Message
  // class. This query can return several thousand instances. If you test this
  // query, you should add a where clause to limit its scope, or set the
  // InstanceCount context qualifier to limit the number of instances
  returned.
  SELECT B.Severity, B.MessageID, B.MessageType,
         B.Win32Error, B.SiteCode, B.MachineName,
         B.Component, C.MsgDLLName, D.InsStrValue
  FROM SMS_StatusMessage AS B
       INNER JOIN SMS_StatMsgModuleNames AS C
       ON B.ModuleName = C.ModuleName
       LEFT OUTER JOIN SMS_StatMsgInsStrings AS D
       ON B.RecordID = D.RecordID
  ORDER BY B.Sitecode, B.RecordID, B.MessageID, D.InsStrIndex

You can use the MessageID and Component names from the list to limit your status
message query. For example, you can add a WHERE clause to limit the status messages
to the SMS_Distribution_Manager component.

<!-- p.1513 -->

After you have the DLL name, you can use the Microsoft Win32 API function
FormatMessage to retrieve the message text from the component's message DLL. This
requires you to get the module handle for the DLL by using the Win32 API function
GetModuleHandle. The dwMessageId parameter is the OR'd result of the MessageID
and the Severity properties. You should set the FORMAT_MESSAGE_ARGUMENT_ARRAY
flag and pass the insertion strings as an array.

The following code shows how to call FormatMessage to retrieve the message text from
a DLL.

  // Get the module handle for the component's message DLL. This assumes the
  // message DLL is loaded. If the DLL is not loaded, then load the DLL by
  using
  // the Win32 API LoadLibrary.
  hmodMessageDLL = GetModuleHandle(MsgDLLName);

  // The flags tell FormatMessage to allocate the memory needed for the
  message,
  // to get the message text from a message DLL, and that the insertion
  strings are
  // stored in an array, instead of a variable length argument list. The last
  // parameter, apInsertStrings, is the array of insertion strings returned by
  the
  // query.
  dwMsgLen = FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER |
                           FORMAT_MESSAGE_FROM_HMODULE |
                           FORMAT_MESSAGE_ARGUMENT_ARRAY,
                           hmodMessageDLL,
                           Severity | MessageID,
                           0,
                           lpBuffer,
                           nSize,
                           apInsertStrings);

  // Free the memory after you use the message text.
  LocalFree(lpBuffer);

See Also
About Configuration Manager Status Messages
SMS_StatMsgInsStrings Server WMI Class
SMS_StatMsgModuleNames Server WMI Class

Feedback

<!-- p.1514 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1515 -->

About Using SMSCSTAT.DLL to Create
Status Messages
Article • 10/04/2022

Smscstat.dll is a library of 32-bit C APIs for reporting Configuration Manager status
messages from an application that is running on either client computer. Smscstat.dll is
only present and only functions properly on Windows 95, Windows 98, Windows NT,
Windows 2000, Windows Server 2003, Windows XP, and Windows Vista computers that
have the client software installed on them.

Loading Smscstat.dll
Applications need to explicitly load Smscstat.dll by using the Win32 LoadLibrary() API.
LoadLibrary requires the full path to Smscstat.dll.

                                                                           ﾉ   Expand table

 Client                                            Path

 SMS 2003 Advanced Client                          %windir%\system32\ccm

 Configuration Manager client                      %windir%\system32\ccm

The logic for finding the path on a given client is as follows:

   1. Read the registry value Local SMS Path in key
       HKEY_LOCAL_MACHINE\Software\Microsoft\SMS\Client\Configuration\ClientPrope
       rties.

   2. If last three characters of this path are ccm, then this is the Advanced Client or
       Configuration Manager client and Smscstat.dll resides in the path retrieved.

Accessing the Functions in Smscstat.dll
When Smscstat.dll has been loaded, call the Win32 API GetProcAddress() to retrieve
function pointers to the status message functions. The three status message functions
are:

       CreateSMSStatusMessage()

       AddAttributeToSMSStatusMessage()

<!-- p.1516 -->

      ReportSMSStatusMessage

      GetProcAddress() returns a pointer of type FARPROC . For convenience, Smscstat.h

     (provided with the SMS 2003 SDK) defines C function prototypes for the status
     message APIs. The application should cast the pointer returned
     by GetProcAddress() to the appropriate prototype and then call the function
     through the pointer.

     If Smscstat.dll doesn't exist, as in the case of SMS 2.0 Legacy Clients that don't
     have Service Pack 1 or a later service pack installed, LoadLibrary() fails. A
     subsequent call to the Win32 API GetLastError() returns an error code indicating
     that the file doesn't exist. Most likely this will be error 126: "The specified module
     couldn't be found."

     The Win32 API FreeLibrary should be called when access to the functions is no
     longer need.

Using the Status Message Functions in
Smscstat.dll
There are three steps to using the status message functions.

   1. Create a status message object by calling the CreateSMSStatusMessage() function.
     This function allocates an object and returns a handle to the caller.

   2. Add any needed status message attributes to the object by using the
      AddAttributeToSMSStatusMessage() function. Status message attributes are optional

     and are required only if the application needs to integrate with a particular
     Configuration Manager feature. Most applications won't do this.

   3. Call ReportSMSStatusMessage to submit the status message to the Configuration
     Manager status system and deallocate the object.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1517 -->

About Reporting Status Messages from
Configuration Manager Clients
Article • 10/04/2022

You can raise Configuration Manager client status messages in the Windows event log
by using a compiled Managed Object Format (MOF) file on client computers. This can
be useful for administrators who are managing servers with System Center Operations
Manager. A Configuration Manager status message that is raised by the Configuration
Manager client can be caught by the Operations Manager agent on the same computer,
which in turn raises an Operations Manager alert for the Configuration Manager status
message.

The following example MOF file shows how to raise Configuration Manager program
status messages:

  #pragma namespace("\\\\.\\root\\ccm\\policy\\machine\\requestedconfig")
  instance of CCM_EventForwarder_Configuration
  {
      InstanceID = "SmsSoftwareDistribution.EventLog";
      Name = "SmsEventLogForwarder";
      PolicyID = "SomePolicyID";
      PolicyInstanceID = "SomePolicyInstance";
      PolicyRuleID = "SomeRuleID";
      PolicySource = "Local";
      PolicyVersion = "1";
          QueryList           = {
                              "SELECT * FROM SoftDistProgramStartedEvent",
                              "SELECT * FROM
  SoftDistProgramCompletedSuccessfullyEvent",
                              "SELECT * FROM
  SoftDistProgramCompletedSuccessfulMIFEvent",
                              "SELECT * FROM SoftDistProgramErrorEvent",
                              "SELECT * FROM SoftDistProgramErrorMIFEvent",
                              "SELECT * FROM SoftDistProgramExceededTime",
                              "SELECT * FROM
  SoftDistProgramPrelimSuccessEvent",
                              "SELECT * FROM
  SoftDistProgramUnexpectedRebootEvent",
                              "SELECT * FROM SoftDistWarningProgramErrorEvent"
                              };
  };

See Also

<!-- p.1518 -->

About Configuration Manager Status Summarizers

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1519 -->

About Configuration Manager Status
Summarizers
Article • 10/04/2022

Summarizers are summary classes that help you determine the health, or status, of
different aspects of your Configuration Manager site. The summaries, which are
produced from status messages, states, and counts, give you a real-time view of the
health of Configuration Manager sites, components, packages, and advertisements.

Status summarizer classes summarize the status message data. Most of the summarizers
create two views of the messages: a site view and a site hierarchy view.

All the summaries, except site system, are event-driven summaries. They respond in real
time to changes that are taking place in Configuration Manager. Only the site system
status summary polls for its information, according to a schedule that you can set.

  ７ Note

  The SMS_SummarizerStatus class can be used to identify the registered summarizers.

Site and Component Status
These summarizers group summaries of two kinds of data: software component health
and physical system health.

You can determine the overall health of your site by using the stoplight status value in
the SMS_SummarizerSiteStatus class, or you can determine the health of your storage
objects by using the SMS_SiteSystemSummarizer class. For more information, see How to
Determine the Health of a Configuration ManagerSite. You can access these and other
classes by getting, enumerating, and querying summarizer objects. However, the
SMS_ComponentSummarizer and SMS_SiteDetailSummarizer classes can only be queried —

you cannot get or enumerate these objects. Your queries must include a tally interval
that defines the period of time from which you want summary information. For example,
the following query asks for the count informational, warning, and error messages since
Monday.

  SELECT Infos, Warnings, Errors
  FROM SMS_SiteDetailSummarizer

<!-- p.1520 -->

  WHERE TallyInterval = "00011280001A2000"

  ７ Note

  You cannot add other conditions like SiteCode to the WHERE clause. Adding other
  conditions will generate an error.

For information about using this query, see How to Perform a Synchronous
Configuration Manager Query by Using Managed Code and How to Perform a
Synchronous Configuration Manager Query by Using WMI.

For more information about using tally intervals, see About Configuration Manager Tally
Intervals.

The component summarizers track the progress of advertised programs as they are
advertised and run on the client computers.

Site system and package status summaries track the state changes instead of counting
the error messages. For example, site system status summaries react to changes in free
disk space on a site system. If the free space falls below the threshold you set, the site
system's status summary health indicator changes.

The summarizer classes are:

                                                                                ﾉ   Expand table

 Summarizer                         Description

 SMS_ComponentSummarizer            Represents a component summarizer that reports on the
 Server WMI Class                   health of individual Configuration Manager components.

 SMS_SiteDetailSummarizer Server    Represents a site detail summarizer that reports on the per-
 WMI Class                          site status of components and the system.

 SMS_SiteSystemSummarizer Server    Represents a site system summarizer that reports physical
 WMI Class                          system health data for each system and each system role in
                                    the Configuration Manager site.

 SMS_SummarizerRootStatus Server    Represents a summarizer for the overall health of the entire
 WMI Class                          site hierarchy.

 SMS_SummarizerSiteStatus Server    Represents a summarizer for the overall health of each site.
 WMI Class
