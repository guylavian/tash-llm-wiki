---
title: "Configuration Manager SDK documentation — pages 1321-1360"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1321-1360
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1321-1360
family: sccm
documentKind: "doc"
abstract: "' Fill the advertisement properties for collection. advertisementToAssign.CollectionID = existingCollectionID ' Save the advertisement. advertisementToAssign.Put_ ' Output advertisement and collection information. Wscript.Echo \"Assigned advertisement: \" & existingAdvertisementID"
---

# Configuration Manager SDK documentation — pages 1321-1360

<!-- p.1321 -->

     ' Fill the advertisement properties for collection.
     advertisementToAssign.CollectionID = existingCollectionID

     ' Save the advertisement.
     advertisementToAssign.Put_

    ' Output advertisement and collection information.
    Wscript.Echo "Assigned advertisement: " & existingAdvertisementID
    Wscript.Echo "                        " &
advertisementToAssign.AdvertisementName
    Wscript.Echo "To collection:          " &
advertisementToAssign.CollectionID

End Sub

c#

public void AssignSWDAdvertisementToCollection(WqlConnectionManager
connection, string existingAdvertisementID, string existingCollectionID)
{
    try
    {
        // Get specific advertisement instance (using the passed in value
existingAdvertisementID).
        IResultObject advertisementToAssign =
connection.GetInstance(@"SMS_Advertisement.AdvertisementID='" +
existingAdvertisementID + "'");

        // Populate the collection id property of the advertisement.
        advertisementToAssign["CollectionID"].StringValue =
existingCollectionID;

          // Save the advertisement and properties.
          advertisementToAssign.Put();

        // Output advertisement and collection information.
        Console.WriteLine("Assigned advertisement: " +
existingAdvertisementID);
        Console.WriteLine("                        " +
advertisementToAssign["AdvertisementName"].StringValue);
        Console.WriteLine("To collection:          " +
existingCollectionID);
    }
    catch (SmsException ex)
    {
        Console.WriteLine("Failed to assign advertisement. Error: " +
ex.Message);
        throw;
    }
}

<!-- p.1322 -->

The example method has the following parameters:

                                                                         ﾉ     Expand table

 Parameter                 Type                        Description

 connection                - Managed:                  A valid connection to the SMS
                           WqlConnectionManager        Provider.
 swebemServices            - VBScript: SWbemServices

 existingAdvertisementID   - Managed: String           The ID of an existing
                           - VBScript: String          advertisement.

 existingCollectionID      - Managed: String           The ID of an existing collection.
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
Software distribution overview About deployments SMS_Collection Server WMI Class

<!-- p.1323 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1324 -->

How to Modify Advertisement
Properties
Article • 10/04/2022

The following example shows how to modify an existing advertisement, in Configuration
Manager, by using the SMS_Advertisement class and class properties.

To modify advertisement properties
   1. Set up a connection to the SMS Provider.

   2. Get the specific advertisement using an existing advertisement ID.

   3. Replace the existing advertisement property (in this case, advertisement comment).

   4. Save the new advertisement and properties.

Example
The following example method modifies advertisement properties for software
distribution.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ModifyAdvertisement(connection, existingAdvertisementID,
  newAdvertisementComment )
      Dim advertisementToModify
      ' Get the specific advertisement instance to modify.
      Set advertisementToModify =
  connection.Get("SMS_Advertisement.AdvertisementID='" &
  existingAdvertisementID & "'")

      ' List the existing property values.
      Wscript.Echo " "
      Wscript.Echo "Values before change: "
      Wscript.Echo "--------------------- "
      Wscript.Echo "Advertisement Name: " &
  advertisementToModify.AdvertisementName
      Wscript.Echo "Comment:            " & advertisementToModify.Comment

        ' Set the new property value.

<!-- p.1325 -->

     advertisementToModify.Comment = newAdvertisementComment

     ' Save the advertisement.
     advertisementToModify.Put_

    ' Output the new property values.
    Wscript.Echo " "
    Wscript.Echo "Values after change: "
    Wscript.Echo "--------------------- "
    Wscript.Echo "Advertisement Name: " &
AdvertisementToModify.AdvertisementName
    Wscript.Echo "Comment:            " & AdvertisementToModify.Comment

End Sub

c#

public void ModifySWDAdvertisement(WqlConnectionManager connection, string
existingAdvertisementID, string newAdvertisementComment)
{
    try
    {
        // Get the specific advertisement instance to modify.
        IResultObject advertisementToModify =
connection.GetInstance(@"SMS_Advertisement.AdvertisementID='" +
existingAdvertisementID + "'");

        // List the existing property values.
        Console.WriteLine();
        Console.WriteLine("Values before change:");
        Console.WriteLine("_____________________");
        Console.WriteLine("Advertisement Name: " +
advertisementToModify["AdvertisementName"].StringValue);
        Console.WriteLine("Comment: " +
advertisementToModify["Comment"].StringValue);

        // Set the new property value to be modified.
        advertisementToModify["Comment"].StringValue =
newAdvertisementComment;

          // Save the advertisement with the new value.
          advertisementToModify.Put();

        // Output the new property values.
        Console.WriteLine();
        Console.WriteLine("Values after change:");
        Console.WriteLine("____________________");
        Console.WriteLine("Advertisement Name: " +
advertisementToModify["AdvertisementName"].StringValue);
        Console.WriteLine("Comment: " + newAdvertisementComment);
    }
    catch (SmsException ex)
    {

<!-- p.1326 -->

          Console.WriteLine("Failed to modify advertisement. Error: " +
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

 existingAdvertisementID   - Managed: String           The ID of the advertisement to
                           - VBScript: String          modify.

 newAdvertisementComment   - Managed: String           The new comment for the
                           - VBScript: String          advertisement.

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

<!-- p.1327 -->

For more information about error handling, see About Configuration Manager Errors.

See Also
Software distribution overview About deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1328 -->

How to Configure a Advertisement to
Allow Reboots Outside of a
Maintenance Window
Article • 10/04/2022

The following example shows how to configure an advertisement to allow reboots
outside of a maintenance window by using the SMS_Advertisement class and the
AdvertFlags class property in Configuration Manager.

To configure an advertisement to allow reboots outside
of a maintenance window
   1. Set up a connection to the SMS Provider.

   2. Load an existing advertisement object using the SMS_Advertisement class.

   3. Modify the AdvertFlags property using the hexadecimal value for
        REBOOT_OUTSIDE_OF_MAINTENANCE_WINDOW .

   4. Save the modified advertisement and properties.

Example
The following example method configures an existing advertisement to allow reboots
outside of a maintenance window.

  ） Important

  The hexadecimal values that define the AdvertFlags property are listed in the
   SMS_Advertisement reference material.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ModifyAdvertisementToRebootOutsideOfMaintenanceWindows(connection,
  existingAdvertisementID)

<!-- p.1329 -->

    ' Define a constant with the hexadecimal value for the
REBOOT_OUTSIDE_OF_MAINTENANCE_WINDOWS.
    Const REBOOT_OUTSIDE_OF_MAINTENANCE_WINDOWS = &H00200000
    Dim advertisementToModify
    ' Get the specific advertisement instance to modify.
    Set advertisementToModify =
connection.Get("SMS_Advertisement.AdvertisementID='" &
existingAdvertisementID & "'")

    ' List the existing property values.
    Wscript.Echo " "
    Wscript.Echo "Values before change: "
    Wscript.Echo "--------------------- "
    Wscript.Echo "Advertisement Name:              " &
advertisementToModify.AdvertisementName
    Wscript.Echo "Advertisement Flags (integer):   " &
advertisementToModify.AdvertFlags

    ' Set the new property value.
    advertisementToModify.AdvertFlags = advertisementToModify.AdvertFlags OR
REBOOT_OUTSIDE_OF_MAINTENANCE_WINDOWS

     ' Save the advertisement.
     advertisementToModify.Put_

    ' Output the new property values.
    Wscript.Echo " "
    Wscript.Echo "Values after change: "
    Wscript.Echo "--------------------- "
    Wscript.Echo "Advertisement Name:              " &
advertisementToModify.AdvertisementName
    Wscript.Echo "Advertisement Flags (integer):   " &
advertisementToModify.AdvertFlags

End Sub

c#

public void
ModifySWDAdvertisementToRebootOutsideOfMaintenanceWindows(WqlConnectionManag
er connection,
                                                                  string
existingAdvertisementID)
{
    // Define a constant with the hexadecimal value for
REBOOT_OUTSIDE_OF_MAINTENANCE_WINDOWS.
    const Int32 REBOOT_OUTSIDE_OF_MAINTENANCE_WINDOWS = 0x00200000;

     try
     {

<!-- p.1330 -->

          // Get the specific advertisement instance to modify.
          IResultObject advertisementToModify =
  connection.GetInstance(@"SMS_Advertisement.AdvertisementID='" +
  existingAdvertisementID + "'");

          // List the existing property values.
          Console.WriteLine();
          Console.WriteLine("Values before change:");
          Console.WriteLine("_____________________");
          Console.WriteLine("Advertisement Name:            " +
  advertisementToModify["AdvertisementName"].StringValue);
          Console.WriteLine("Advertisement Flags (integer): " +
  advertisementToModify["AdvertFlags"].IntegerValue);

          // Modify the AdvertFlags value to include the
  REBOOT_OUTSIDE_OF_MAINTENANCE_WINDOWS value.
          advertisementToModify["AdvertFlags"].IntegerValue =
  advertisementToModify["AdvertFlags"].IntegerValue |
  REBOOT_OUTSIDE_OF_MAINTENANCE_WINDOWS;

              // Save the advertisement with the new value.
              advertisementToModify.Put();

              // Reload the advertisement to verify the change.
              advertisementToModify.Get();

          // List the existing (modified) property values.
          Console.WriteLine();
          Console.WriteLine("Values after change:");
          Console.WriteLine("_____________________");
          Console.WriteLine("Advertisement Name:            " +
  advertisementToModify["AdvertisementName"].StringValue);
          Console.WriteLine("Advertisement Flags (integer): " +
  advertisementToModify["AdvertFlags"].IntegerValue);
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to modify advertisement. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                       ﾉ   Expand table

 Parameter                 Type                       Description

 connection                - Managed:                 A valid connection to the SMS
                           WqlConnectionManager       Provider.

<!-- p.1331 -->

 Parameter                   Type                        Description

 swbemServices               - VBScript: SWbemServices

 existingAdvertisementID     - Managed: String           The ID of the advertisement to
                             - VBScript: String          modify.

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
Software distribution overview About deployments

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.1332 -->

How to Configure an Advertisement to
Override a Maintenance Window
Article • 10/04/2022

The following example shows how to configure an advertisement to override service
windows using the SMS_Advertisement class and the AdvertFlags class property in
Configuration Manager.

To configure an advertisement to override maintenance
windows
   1. Set up a connection to the SMS Provider.

   2. Load an existing advertisement object using the SMS_Advertisement class.

   3. Modify the AdvertFlags property using the hexadecimal value for
        OVERRIDE_MAINTENANCE_WINDOW .

   4. Save the modified advertisement and properties.

Example
The following example method configures an existing advertisement to override
maintenance windows.

  ） Important

  The hexadecimal values that define the AdvertFlags property are listed in the
   SMS_Advertisement class reference material.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ModifyAdvertisementToOverrideMaintenanceWindows(connection,
  existingAdvertisementID)

      ' Define a constant with the hexadecimal value for the
  OVERRIDE_MAINTENANCE_WINDOW.

<!-- p.1333 -->

     Const OVERRIDE_MAINTENANCE_WINDOWS = &H00100000
     Dim advertisementToModify

    ' Get the specific advertisement instance to modify.
    Set advertisementToModify =
connection.Get("SMS_Advertisement.AdvertisementID='" &
existingAdvertisementID & "'")

    ' List the existing property values.
    Wscript.Echo " "
    Wscript.Echo "Values before change: "
    Wscript.Echo "--------------------- "
    Wscript.Echo "Advertisement Name:            " &
advertisementToModify.AdvertisementName
    Wscript.Echo "Advertisement Flags (integer): " &
advertisementToModify.AdvertFlags

    ' Set the new property value.
    advertisementToModify.AdvertFlags = advertisementToModify.AdvertFlags OR
OVERRIDE_MAINTENANCE_WINDOWS

     ' Save the advertisement.
     advertisementToModify.Put_

    ' Output the new property values.
    Wscript.Echo " "
    Wscript.Echo "Values after change: "
    Wscript.Echo "--------------------- "
    Wscript.Echo "Advertisement Name:                " &
advertisementToModify.AdvertisementName
    Wscript.Echo "Advertisement Flags (integer):     " &
advertisementToModify.AdvertFlags

End Sub

c#

public void
ModifySWDAdvertisementToOverrideMaintenanceWindows(WqlConnectionManager
connection,
                                                               string
existingAdvertisementID)
{
    // Define a constant with the hexadecimal value for
OVERRIDE_MAINTENANCE_WINDOW.
    const Int32 OVERRIDE_MAINTENANCE_WINDOWS = 0x00100000;

     try
     {
           // Get the specific advertisement instance to modify.
           IResultObject advertisementToModify =

<!-- p.1334 -->

  connection.GetInstance(@"SMS_Advertisement.AdvertisementID='" +
  existingAdvertisementID + "'");

          // List the existing property values.
          Console.WriteLine();
          Console.WriteLine("Values before change:");
          Console.WriteLine("_____________________");
          Console.WriteLine("Advertisement Name:            " +
  advertisementToModify["AdvertisementName"].StringValue);
          Console.WriteLine("Advertisement Flags (integer): " +
  advertisementToModify["AdvertFlags"].IntegerValue);

          // Modify the AdvertFlags value to include the
  OVERRIDE_MAINTENANCE_WINDOWS value.
          advertisementToModify["AdvertFlags"].IntegerValue =
  advertisementToModify["AdvertFlags"].IntegerValue |
  OVERRIDE_MAINTENANCE_WINDOWS;

              // Save the advertisement with the new value.
              advertisementToModify.Put();

              // Reload the advertisement to verify the change.
              advertisementToModify.Get();

          // List the existing (modified) property values.
          Console.WriteLine();
          Console.WriteLine("Values after change:");
          Console.WriteLine("_____________________");
          Console.WriteLine("Advertisement Name:            " +
  advertisementToModify["AdvertisementName"].StringValue);
          Console.WriteLine("Advertisement Flags (integer): " +
  advertisementToModify["AdvertFlags"].IntegerValue);
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to modify advertisement. Error: " +
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

<!-- p.1335 -->

 Parameter                   Type                     Description

 existingAdvertisementID     - Managed: String        The ID of the advertisement to
                             - VBScript: String       modify.

Compiling the Code
The C# example requires:

Namespaces
System

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

mscorlib

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
Software distribution overview About deployments

Feedback
Was this page helpful?      Yes      No

Provide product feedback

<!-- p.1336 -->

About Maintenance Windows
Article • 10/04/2022

For more information about Configuration Manager maintenance windows, see Use
maintenance windows.

See also
      About deployments
      Software distribution overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1337 -->

How to Create a Maintenance Window
for a Collection
Article • 10/04/2022

Your application can create a Configuration Manager maintenance window by using the
SMS_CollectionSettings Server WMI Class and SMS_ServiceWindow Server WMI Class
classes and properties.

To create a maintenance window
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the existing collection settings instance by using the supplied collection ID.

   3. Create and populate the properties of a new service window object by using the
        SMS_ServiceWindow Server WMI Class class.

   4. Add the new SMS_ServiceWindow object to the collection settings instance obtained
        earlier.

   5. Save the collection settings instance and properties.

  ７ Note

  The example below includes additional steps, primarily to handle the overhead of
  dealing with the maintenance window objects, which are stored as embedded
  objects in the collection settings instance.

Example
The following example method creates a maintenance window for a collection,
assuming that the collection instance can modified. This might not be the case at child
sites, where the collections are owned by the parent site(s).

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

<!-- p.1338 -->

Sub CreateMaintenanceWindow(connection,                                 _
                            targetCollectionID,                         _
                            newMaintenanceWindowName,                   _
                            newMaintenanceWindowDescription,            _
                            newMaintenanceWindowServiceWindowSchedules, _
                            newMaintenanceWindowIsEnabled,              _
                            newMaintenanceWindowServiceWindowType)

    ' Build a query to get the specified collection.
     collectionSettingsQuery = "SMS_CollectionSettings.CollectionID='" &
targetCollectionID & "'"

    ' Get the collection settings instance for the targetCollectionID.
    Set allCollectionSettings = connection.ExecQuery("Select * From
SMS_CollectionSettings Where CollectionID = '" & targetCollectionID & "'")

    ' If a collection settings instance does not exist for the target
collection, create one.
    If allCollectionSettings.Count = 0 Then
        Wscript.Echo "Creating collection settings instance."
        Set collectionSettingsInstance =
connection.Get("SMS_CollectionSettings").SpawnInstance_
        collectionSettingsInstance.CollectionID = targetCollectionID
        collectionSettingsInstance.Put_
    End If

    ' Get the specific collection settings instance.
    Set collectionSettingsInstance =
connection.Get("SMS_CollectionSettings.CollectionID='" & targetCollectionID
&"'" )

    ' Create and populate a temporary SMS_ServiceWindow object with the new
maintenance window values.
    Set tempServiceWindowObject =
connection.Get("SMS_ServiceWindow").SpawnInstance_

    ' Populate temporary SMS_ServiceWindow object with the new maintenance
window values.
    tempServiceWindowObject.Name = newMaintenanceWindowName
    tempServiceWindowObject.Description = newMaintenanceWindowDescription
    tempServiceWindowObject.ServiceWindowSchedules =
newMaintenanceWindowServiceWindowSchedules
    tempServiceWindowObject.IsEnabled = newMaintenanceWindowIsEnabled
    tempServiceWindowObject.ServiceWindowType =
newMaintenanceWindowServiceWindowType

    ' Populate the local array list with the existing service window objects
(from the target collection).
    tempServiceWindowArray = collectionSettingsInstance.ServiceWindows

     ' Add the newly created service window object to the temporary array.
     ReDim Preserve tempServiceWindowArray (Ubound(tempServiceWindowArray) +
1)

<!-- p.1339 -->

    Set tempServiceWindowArray(Ubound(tempServiceWindowArray)) =
tempServiceWindowObject

    ' Replace the existing service window objects from the target collection
with the temporary array that includes the new service window.
    collectionSettingsInstance.ServiceWindows = tempServiceWindowArray

    ' Save the collection settings instance with the new service window
object.
    collectionSettingsInstance.Put_

     ' Output success message.
     wscript.echo "New Maintenance Window created."

End Sub

c#

public void CreateMaintenanceWindow(WqlConnectionManager connection,
                                    string targetCollectionID,
                                    string newMaintenanceWindowName,
                                    string newMaintenanceWindowDescription,
                                    string
newMaintenanceWindowServiceWindowSchedules,
                                    bool newMaintenanceWindowIsEnabled,
                                    int
newMaintenanceWindowServiceWindowType)
{
    try
    {
        // Create an object to hold the collection settings instance (used
to check whether a collection settings instance exists).
        IResultObject collectionSettingsInstance = null;

        // Get the collection settings instance for the targetCollectionID.
        IResultObject allCollectionSettings =
connection.QueryProcessor.ExecuteQuery("Select * from SMS_CollectionSettings
where CollectionID='" + targetCollectionID + "'");

        // Enumerate the allCollectionSettings collection (there should be
just one item) and save the instance.
        foreach (IResultObject collectionSetting in allCollectionSettings)
        {
            collectionSettingsInstance = collectionSetting;
        }

        // If a collection settings instance does not exist for the target
collection, create one.
        if (collectionSettingsInstance == null)
        {
            collectionSettingsInstance =

<!-- p.1340 -->

connection.CreateInstance("SMS_CollectionSettings");
            collectionSettingsInstance["CollectionID"].StringValue =
targetCollectionID;
            collectionSettingsInstance.Put();
            collectionSettingsInstance.Get();
        }

        // Create a new array list to hold the service window object.
        List<IResultObject> tempServiceWindowArray = new List<IResultObject>
();

        // Create and populate a temporary SMS_ServiceWindow object with the
new maintenance window values.
        IResultObject tempServiceWindowObject =
connection.CreateEmbeddedObjectInstance("SMS_ServiceWindow");

        // Populate temporary SMS_ServiceWindow object with the new
maintenance window values.
        tempServiceWindowObject["Name"].StringValue =
newMaintenanceWindowName;
        tempServiceWindowObject["Description"].StringValue =
newMaintenanceWindowDescription;
        tempServiceWindowObject["ServiceWindowSchedules"].StringValue =
newMaintenanceWindowServiceWindowSchedules;
        tempServiceWindowObject["IsEnabled"].BooleanValue =
newMaintenanceWindowIsEnabled;
        tempServiceWindowObject["ServiceWindowType"].IntegerValue =
newMaintenanceWindowServiceWindowType;

        // Populate the local array list with the existing service window
objects (from the target collection).
        tempServiceWindowArray =
collectionSettingsInstance.GetArrayItems("ServiceWindows");

        // Add the newly created service window object to the local array
list.
        tempServiceWindowArray.Add(tempServiceWindowObject);

        // Replace the existing service window objects from the target
collection with the temporary array that includes the new service window.
        collectionSettingsInstance.SetArrayItems("ServiceWindows",
tempServiceWindowArray);

        // Save the new values in the collection settings instance
associated with the target collection.
        collectionSettingsInstance.Put();
    }
    catch (SmsException ex)
    {
        Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
        throw;
    }
}

<!-- p.1341 -->

The example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter                                    Type                   Description

 connection                                   - Managed:             A valid connection to
                                              WqlConnectionManager   the SMS Provider.
 swebemServices                               - VBScript:
                                              SWbemServices

 targetCollectionID                           - Managed: String      The ID of the
                                              - VBScript: String     collection.

 newMaintenanceWindowName                     - Managed: String      The name of the new
                                              - VBScript: String     maintenance window.

 newMaintenanceWindowDescription              - Managed: String      The description of the
                                              - VBScript: String     new maintenance
                                                                     window.

 newMaintenanceWindowServiceWindowSchedules   - Managed: String      The service schedules
                                              - VBScript: String     for the new
                                                                     maintenance window.

 newMaintenanceWindowIsEnabled                - Managed: Boolean     true if the new
                                              - VBScript: Boolean    maintenance window
                                                                     is enabled.

 newMaintenanceWindowServiceWindowType        - Managed: Integer     Type for the new
                                              - VBScript: Integer    maintenance window.

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

<!-- p.1342 -->

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About maintenance windows Software distribution overview About deployments
Objects overview How to Connect to a Configuration Manager Provider using Managed
Code
How to Connect to a Configuration Manager Provider Using WMI
SMS_CollectionSettings Server WMI Class
SMS_ServiceWindow Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1343 -->

How to Change the Maintenance
Window Properties for a Collection
Article • 10/04/2022

You can change maintenance window properties for a collection, in Configuration
Manager, by using the SMS_CollectionSettings Server WMI Class and
SMS_ServiceWindow Server WMI Class classes and properties.

To change the properties of a maintenance window
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Get the existing collection settings instance by using the existing collection ID
      provided.

   3. Get the existing service window object by using the existing service window ID
      provided.

   4. Change an existing property value (in this case the maintenance window
      description).

   5. Save the collection settings instance and properties.

  ７ Note

  The steps in the example method include additional steps, primarily to handle the
  overhead of dealing with the service window objects, which are stored as
  embedded objects in the collection settings instance.

Example
The following example method changes the properties of a specific maintenance
window instance.

  ） Important

  This assumes that the collection instance can modified. This might not be the case
  at child sites, where the collections are owned by the parent site(s).

<!-- p.1344 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ChangeMaintenanceWindowProperties(connection,
  _
                                        targetCollectionID,
  _
                                        targetServiceWindowID,
  _
                                        newMaintenanceWindowDescription,
  _

  newMaintenanceWindowServiceWindowSchedules, _
                                        newMaintenanceWindowIsEnabled)

      ' Get the specific collection settings instance.
      Set collectionSettingsInstance =
  connection.Get("SMS_CollectionSettings.CollectionID='" & targetCollectionID
  &"'" )

      ' Populate the local array list with the existing service window objects
  (from the target collection).
      tempMaintenanceWindowArray = collectionSettingsInstance.ServiceWindows

      ' Enumerate through the array list to access each maintenance window
  object.
      For Each maintenanceWindow in tempMaintenanceWindowArray

           ' If the service window ID matches the one passed in to the
  function, change the specific values.
           If maintenanceWindow.ServiceWindowID = targetServiceWindowID Then

              ' Populate retrieved SMS_ServiceWindow object with the new
  maintenance window values.
              maintenanceWindow.Description = newMaintenanceWindowDescription
              maintenanceWindow.ServiceWindowSchedules =
  newMaintenanceWindowServiceWindowSchedules
              maintenanceWindow.IsEnabled = newMaintenanceWindowIsEnabled

               End If

        Next

      ' Replace the existing service window objects from the target collection
  with the temporary array that includes the modified service window.
      collectionSettingsInstance.ServiceWindows = tempMaintenanceWindowArray

      ' Save the new values in the collection settings instance associated
  with the collection ID.
      collectionSettingsInstance.Put_

<!-- p.1345 -->

    ' Output success message.
    wscript.echo "Maintenance Window " & targetServiceWindowID & "
modified."

End Sub

c#

public void ChangeMaintenanceWindowProperties(WqlConnectionManager
connection,
                                              string targetCollectionID,
                                              string serviceWindowID,
                                              string
newMaintenanceWindowDescription)
{
    try
    {
        // Create a new array list to hold the service window objects.
        List<IResultObject> tempMaintenanceWindowArray = new
List<IResultObject>();

        // Establish connection to collection settings instance associated
with the Collection ID.
        IResultObject collectionSettings =
connection.GetInstance(@"SMS_CollectionSettings.CollectionID='" +
targetCollectionID + "'");

        // Populate the array list with the existing service window objects
(from the target collection).
        tempMaintenanceWindowArray =
collectionSettings.GetArrayItems("ServiceWindows");

        // Enumerate through the array list to access each maintenance
window object.
        foreach (IResultObject maintenanceWindow in
tempMaintenanceWindowArray)
        {
            // If the service window ID matches the one passed in to the
function, change the specific values.
            if (maintenanceWindow["ServiceWindowID"].StringValue ==
serviceWindowID)
            {
                maintenanceWindow["Description"].StringValue =
newMaintenanceWindowDescription;
                break;
            }
        }

        // Replace the existing service window objects from the target
collection with the temporary array that includes the new service window.
        collectionSettings.SetArrayItems("ServiceWindows",

<!-- p.1346 -->

  tempMaintenanceWindowArray);

          // Save the new values in the collection settings instance
  associated with the Collection ID.
          collectionSettings.Put();
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                         ﾉ    Expand table

 Parameter                         Type                   Description

 connection                        - Managed:             A valid connection to the SMS
                                   WqlConnectionManager   Provider.
 swebemServices                    - VBScript:
                                   SWbemServices

 targetCollectionID                - Managed: String      The ID of the collection.
                                   - VBScript: String

 serviceWindowID                   - Managed: String      The ID of the maintenance
                                   - VBScript: String     window for which to change
                                                          properties.

 newMaintenanceWindowDescription   - Managed: String      The description of the new
                                   - VBScript: String     maintenance window.

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

System.ComponentModel

<!-- p.1347 -->

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
About maintenance windows Software distribution overview About deployments
Objects overview How to Connect to a Configuration Manager Provider using Managed
Code
How to Connect to a Configuration Manager Provider Using WMI
SMS_CollectionSettings Server WMI Class
SMS_ServiceWindow Server WMI Class
About schedules How to Create a Schedule Token

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1348 -->

How to Delete a Maintenance Window
for a Collection
Article • 10/04/2022

You can delete maintenance window, in Configuration Manager, by using the
SMS_CollectionSettings Server WMI Class and SMS_ServiceWindow Server WMI Class
classes and properties.

To delete a maintenance window for a collection
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Get an existing collection settings instance by using the collection ID provided.

   3. Get the existing service window object by using the maintenance window ID
      provided.

   4. Delete the existing maintenance window.

   5. Save the collection settings instance and properties.

  ７ Note

  The example method includes additional steps, primarily to handle the overhead of
  dealing with the service window objects, which are stored as embedded objects in
  the collection settings instance.

Example
The following example method deletes a specific maintenance window instance for a
collection.

  ） Important

  This assumes that the collection instance can modified. This might not be the case
  at child sites, where the collections are owned by the parent site or sites.

<!-- p.1349 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void DeleteMaintenanceWindowfromCollection(WqlConnectionManager
  connection,
                                                    string targetCollectionID,
                                                    string serviceWindowID)
  {
      try
      {
          // Create a new array list to hold the service window objects.
          List<IResultObject> tempMaintenanceWindowArray = new
  List<IResultObject>();

          // Establish connection to collection settings instance associated
  with the target collection ID.
          IResultObject collectionSettings =
  connection.GetInstance(@"SMS_CollectionSettings.CollectionID='" +
  targetCollectionID + "'");

          // Populate the array list with the existing service window objects
  (from the target collection).
          tempMaintenanceWindowArray =
  collectionSettings.GetArrayItems("ServiceWindows");

          // Enumerate through the array list to access each maintenance
  window object.
          foreach (IResultObject maintenanceWindow in
  tempMaintenanceWindowArray)
          {
              // If the maintenance window ID matches the one passed in to the
  function, delete the maintenance window.
              if (maintenanceWindow["ServiceWindowID"].StringValue ==
  serviceWindowID)
              {
                  tempMaintenanceWindowArray.Remove(maintenanceWindow);
                  Console.WriteLine("Deleted:");
                  Console.WriteLine("Maintenance Window Name: " +
  maintenanceWindow["Name"].StringValue);
                  Console.WriteLine("Maintenance Windows Service Window ID: "
  + maintenanceWindow["ServiceWindowID"].StringValue);
                  break;
              }
          }

          // Replace the existing service window objects from the target
  collection with the temporary array that includes the new maintenance
  window.
          collectionSettings.SetArrayItems("ServiceWindows",
  tempMaintenanceWindowArray);

            // Save the new values in the collection settings instance

<!-- p.1350 -->

  associated with the Collection ID.
          collectionSettings.Put();
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter            Type                         Description

 connection           - Managed:                   A valid connection to the SMS Provider.
                      WqlConnectionManager

 targetCollectionID   - Managed: String            The ID of the collection.

 serviceWindowID      - Managed: String            The ID of the maintenance window to
                                                   delete.

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

<!-- p.1351 -->

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About maintenance windows Software distribution overview About deployments
Objects overview How to Connect to a Configuration Manager Provider using Managed
Code
How to Connect to a Configuration Manager Provider Using WMI
SMS_CollectionSettings Server WMI Class
SMS_ServiceWindow Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1352 -->

How to List the Maintenance Windows
and Properties for a Specific Collection
Article • 10/04/2022

The following example shows how to list the maintenance windows for a specific
collection by using the SMS_CollectionSettings Server WMI Class class. Maintenance
windows are created by using the SMS_ServiceWindow Server WMI Class class and then
stored as embedded objects in SMS_CollectionSettings instances, one per collection.

To list the maintenance windows and properties for a
collection
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the existing collection settings instance by using the collection ID provided.

   3. Enumerate the existing service window objects and properties.

  ７ Note

  The example method includes additional steps, primarily to handle the overhead of
  dealing with the service window objects, which are stored as embedded objects in
  the collection settings instance.

Example
The following example method lists the maintenance windows and properties for a
collection.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ListMaintenanceWindowsAndPropertiesForASpecificCollection(connection,
  _

  targetCollectionID)

<!-- p.1353 -->

    ' Build a query to get the specified collection.
     collectionSettingsQuery = "SMS_CollectionSettings.CollectionID='" &
targetCollectionID & "'"

    ' Get the collection settings instance for the targetCollectionID.
    Set allCollectionSettings = connection.ExecQuery("Select * From
SMS_CollectionSettings Where CollectionID = '" & targetCollectionID & "'")

    ' If a collection settings instance does not exist, output a message.
    If allCollectionSettings.Count = 0 Then
        Wscript.Echo "There are no maintenance windows for collection: " &
targetCollectionID
    Else

    ' Get the specific collection settings instance.
    Set collectionSettingsInstance =
connection.Get("SMS_CollectionSettings.CollectionID='" & targetCollectionID
&"'" )

        ' Populate the local array list with the existing service window
objects (from the target collection).
        tempMaintenanceWindowArray =
collectionSettingsInstance.ServiceWindows

          ' Enumerate through the array list to access each maintenance window
object.
          For Each maintenanceWindow in tempMaintenanceWindowArray

                Wscript.Echo "Maintenance Window Properties "
                Wscript.Echo "----------------------------- "
                Wscript.Echo "Name:              " & maintenanceWindow.Name
                Wscript.Echo "Description:       " &
maintenanceWindow.Description
                Wscript.Echo "Service Window ID: " &
maintenanceWindow.ServiceWindowID
                Wscript.Echo "Schedules:         " &
maintenanceWindow.ServiceWindowSchedules
                Wscript.Echo "Is Enabled:        " &
maintenanceWindow.IsEnabled
                Wscript.Echo "Type:              " &
maintenanceWindow.ServiceWindowType
                Wscript.Echo " "

          Next

     End If

End Sub

c#

<!-- p.1354 -->

public void
ListMaintenanceWindowsAndPropertiesForASpecificCollection(WqlConnectionManag
er connection,
                                                                      string
targetCollectionID)
{
    try
    {
        // Create an object to hold the collection settings instance (used
to check whether a collection settings instance exists).
        IResultObject collectionSettingsInstance = null;

        // Get the collection settings instance for the targetCollectionID.
        IResultObject allCollectionSettings =
connection.QueryProcessor.ExecuteQuery("Select * from SMS_CollectionSettings
where CollectionID='" + targetCollectionID + "'");

        // Enumerate the allCollectionSettings collection (there should be
just one item) and save the instance.
        foreach (IResultObject collectionSetting in allCollectionSettings)
        {
            collectionSettingsInstance = collectionSetting;
        }

        // If a collection settings instance, output message that there are
no maintenance windows.
        if (collectionSettingsInstance == null)
        {
             Console.WriteLine("There are no maintenance windows for
collection: " + targetCollectionID);
        }
        else
        {
             // Create a new array list to hold the service window objects.
             List<IResultObject> maintenanceWindowArray = new
List<IResultObject>();

            // Establish connection to collection settings instance
associated with the Collection ID.
            IResultObject collectionSettings =
connection.GetInstance(@"SMS_CollectionSettings.CollectionID='" +
targetCollectionID + "'");

            // Populate the array list with the existing service window
objects (from the target collection).
            maintenanceWindowArray =
collectionSettings.GetArrayItems("ServiceWindows");

            // Enumerate through the array list to access each maintenance
window object and output specific properties for each object.
            foreach (IResultObject maintenanceWindow in
maintenanceWindowArray)
            {

<!-- p.1355 -->

                  Console.WriteLine("Maintenance Window Properties ");
                  Console.WriteLine("----------------------------- ");
                  Console.WriteLine("Name:              " +
  maintenanceWindow["Name"].StringValue);
                  Console.WriteLine("Description:       " +
  maintenanceWindow["Description"].StringValue);
                  Console.WriteLine("Service Window ID: " +
  maintenanceWindow["ServiceWindowID"].StringValue);
                  Console.WriteLine("Schedules:         " +
  maintenanceWindow["ServiceWindowSchedules"].StringValue);
                  Console.WriteLine("Is Enabled:        " +
  maintenanceWindow["IsEnabled"].BooleanValue);
                  Console.WriteLine("Type:              " +
  maintenanceWindow["ServiceWindowType"].IntegerValue);
                  Console.WriteLine(" ");
              };
          }
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                         ﾉ     Expand table

 Parameter            Type                         Description

 connection           - Managed:                   A valid connection to the SMS
                      WqlConnectionManager         Provider.
 swebemServices       - VBScript: SWbemServices

 targetCollectionID   - Managed: String            The ID of the collection.
                      - VBScript: String

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

<!-- p.1356 -->

System.ComponentModel

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
About maintenance windows Software distribution overview About deployments
Objects overview How to Connect to a Configuration Manager Provider using Managed
Code
How to Connect to a Configuration Manager Provider Using WMI
SMS_CollectionSettings Server WMI Class
SMS_ServiceWindow Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1357 -->

About Software Distribution Setup and
Configuration
Article • 10/04/2022

The Advertised Programs Client Agent, like other client agents, is installed on all clients
by Configuration Manager, but it's necessary to configure the agent to match the needs
of your site. This includes configuring the built-in components and client agents.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1358 -->

How to Enable or Disable the Software
Distribution Advertised Programs Client
Agent
Article • 10/04/2022

In Configuration Manager, the site control file maintains configuration for the site. This
topic shows how to enable or disable the Software Distribution Advertised Programs
Client Agent setting in the site control file. For more information about reading from
and writing to the site control file, see About the site control file.

  Ｕ Caution

  You should be experienced in managing a site's configuration before using the SMS
  Provider classes to modify the site configuration. You should use caution or avoid
  using the SMS_SCI_FileDefinition and SMS_SCI_SiteDefinition classes altogether.
  These classes manage the site control file itself. You can cause significant damage
  to a site by changing some configurable items.

To enable or disable the client agent
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Make a connection to the software distribution client component section of the
      site control file by using the SMS_SCI_ClientComp class.

   3. Adjust the client agent settings by setting the flag value to 0 to disable the agent
      or 1 to enable the agent.

   4. Commit the property changes to the site control file.

Example
The following example method queries for the specific site control file item, software
distribution client component section, and changes the flag value to enable or disable
the client agent.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.1359 -->

vbs

Sub EnableDisableSWDClientAgent(swbemServices, swbemContext,
enableDisableFlag, siteToChange )

    ' Load site control file and get SWD client component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteToChange & "',ItemName='Software
Distribution'", , swbemContext)

      ' Display SWD client agent settings before change
      Wscript.Echo " "
      Wscript.Echo "Properties - Before Change"
      Wscript.Echo "---------------------------"
      Wscript.Echo objSWbemInst.ClientComponentName
      Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

    ' Set SWD client agent by setting Flags value to   0 or 1 using the
sEnableDisableFlag variable.
    objSWbemInst.Flags = enableDisableFlag

    ' Save new client agent settings.
    objSWbemInst.Put_ , swbemContext
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Commit", , , swbemContext

    ' Refresh in-memory copy of the site control file and get the DCM client
component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteToChange & "',ItemName='Software
Distribution'", , swbemContext)

      ' Display SWD client agent settings after change.
      Wscript.Echo " "
      Wscript.Echo "Properties - After Change"
      Wscript.Echo "---------------------------"
      Wscript.Echo objSWbemInst.ClientComponentName
      Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

End Sub

c#

public void EnableDisableSWDClientAgent(WqlConnectionManager connection,
string enableDisableFlag, string siteCode)

<!-- p.1360 -->

  {
      try
      {
          IResultObject siteDefinition =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" + siteCode + "',ItemName='Software Distribution'");

            // Display SWD client agent settings before change.
            Console.WriteLine();
            Console.WriteLine("Properties - Before Change");
            Console.WriteLine("---------------------------");

  Console.WriteLine(siteDefinition["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");

          // Set SWD client agent by setting "Flags" value to 0 or 1 using the
  enableDisableFlag variable.
          siteDefinition["Flags"].StringValue = enableDisableFlag;

            // Save the settings.
            siteDefinition.Put();

          // Verify change by reconnecting and getting the value again.
          IResultObject siteDefinition2 =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" + siteCode + "',ItemName='Software Distribution'");

            // Display SWD client agent settings after change.
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
