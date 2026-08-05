---
title: "Configuration Manager SDK documentation — pages 961-1000"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0961-1000
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0961-1000
family: sccm
documentKind: "doc"
abstract: "foreach (IResultObject resultObj in resultObjs) { if (resultObj.EmbeddedProperties.ContainsKey(\"SMPQuiesceState\") == true && resultObj.EmbeddedProperties[\"SMPQuiesceState\"].Properties[\"Value\"].IntegerV alue != 0) { // Find out whether this state migration point contains any stat"
---

# Configuration Manager SDK documentation — pages 961-1000

<!-- p.961 -->

        foreach (IResultObject resultObj in resultObjs)
        {
            if (resultObj.EmbeddedProperties.ContainsKey("SMPQuiesceState")
== true &&

resultObj.EmbeddedProperties["SMPQuiesceState"].Properties["Value"].IntegerV
alue != 0)
            {
                // Find out whether this state migration point contains any
stateMigrationRestores that are incomplete on this
                // server that is to be deleted.
                string query2 = string.Format(CultureInfo.InvariantCulture,
@"SELECT * from SMS_StateMigration where StorePath Like '%{0}%'",
smpServer);

                IResultObject resultObjs2 =
selectedResultObject.ConnectionManager.QueryProcessor.ExecuteQuery(query2);

                 foreach (IResultObject resultObj2 in resultObjs2)
                 {
                     // Look for state migration objects without a
StoreReleaseData/Migration date
                     // it's the one that will cause an exception when
reading releasetime because it is not a valid datetime.
                     try
                     {
                         DateTime releaseTime =
resultObj2["StoreReleaseDate"].DateTimeValue;
                     }
                     catch (ArgumentOutOfRangeException)
                     {
                         // Alternatively return false if you do not to
delete.
                         return true;
                     }
                 }
             }
        }
    }
    catch (SmsQueryException ex)
    {
        Console.WriteLine("Failed during smp state determination" +
ex.Message);
        throw;
    }
    finally
    {
        if (resultObjs != null)
        {
             resultObjs.Dispose();
        }
    }

    // Delete the role.

<!-- p.962 -->

      return true;
  }

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter    Type                   Description

 connection   Managed:               A valid connection to the SMS Provider.
              WqlConnectionManager

 siteCode     Managed: String        The Configuration Manager site code.

 nalPath      Managed: String        The NAL path to the state migration point. For example
                                     ["Display=\\SERVERNAME\"]MSWNET:
                                     ["SMS_SITE=SITECODE"]\\SERVERNAME\

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System.Globalization

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming

<!-- p.963 -->

For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
SMS_SCI_SysResUse Server WMI Class
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.964 -->

How to Add a State Migration Point
Folder
Article • 10/04/2022

In Configuration Manager, you add an operating system deployment state migration
point folder by adding the folder description to the Directories embedded property
list.

The folder description is a string that defines the following information.

                                                                             ﾉ   Expand table

 Value                       Description

  Directory                  The name of the folder.

  MaxClients                 The maximum number of clients supported.

  MinDiskSpace               The minimum disk space required.

  MinDiskSpaceUnit           The minimum disk space units.

                             1 - MB

                             2 - GB

                             3 - Percentage

To add a state migration point folder
    1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

    2. Make a connection to the state migration point resources section of the site
        control file.

    3. Get the Directories embedded properties list.

    4. Update the Directories embedded property with new folder.

    5. Commit the changes to the site control file.

Example

<!-- p.965 -->

The following example method adds a new folder to the state migration point.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub AddSmpFolder( connection, _
      context,              _
      directory,            _
       maxClients,          _
       minDiskSpace,        _
       minDiskSpaceUnit,    _
      siteCode)

        Dim InParams
        Dim smpSettings
        Dim found

         ' Format the directories string.
         smpSettings = "Directory=" + directory + ";MaxClients=" + _
         CStr(maxClients) + ";MinDiskSpace=" + CStr(minDiskSpace) + _
         ";MinDiskSpaceUnit=" + CStr(minDiskSpaceUnit) + ";"

       Set InParams =
  connection.Get("SMS_SiteControlFile").Methods_("RefreshSCF").InParameters.Sp
  awnInstance_
  InParams.SiteCode = siteCode
  connection.ExecMethod "SMS_SiteControlFile", "RefreshSCF", InParams, ,
  context

        Query = "SELECT * FROM SMS_SCI_SysResUse " & _
                "WHERE RoleName = 'SMS State Migration Point' " & _
                "AND SiteCode = '" & siteCode & "'"

        found = false

        Set SCIComponentSet = connection.ExecQuery(Query, , , context)

        For Each SCIComponent In SCIComponentSet
            For Each vProperty in SCIComponent.PropLists

               WScript.Echo vProperty.PropertyListName

               if       vProperty.PropertyListName = "Directories" Then

                    Dim directories
                    Dim i

                    found = true

                    ' Resize the array to accommodate the new directory.
                    ReDim directories(UBound (vProperty.Values)+1)

<!-- p.966 -->

                  for i = 0 to UBound(vProperty.Values)
                       directories(i) = vProperty.Values(i)
                  Next

                  directories(ubound (directories))= smpSettings
                  vProperty.Values = directories

               End If

        Next

                ' Update the component in your copy of the site control file.
Get the path
                ' to the updated object, which could be used later to retrieve
the instance.
                Set SCICompPath = SCIComponent.Put_( , context)
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

public void AddSmpFolder(
    WqlConnectionManager connection,
    string directory,
    int maxClients,
    int minDiskSpace,
    int minDiskSpaceUnit,
    string serverName,
    string siteCode)
{
    try
    {
        // Set up folder string.
        string smpSettings = "Directory=" +
            directory +
            ";MaxClients=" +
            maxClients.ToString(CultureInfo.InvariantCulture) +
            ";MinDiskSpace=" +
            minDiskSpace.ToString(CultureInfo.InvariantCulture) +
            ";MinDiskSpaceUnit=" +
            minDiskSpaceUnit.ToString(CultureInfo.InvariantCulture) +
            ";";

<!-- p.967 -->

          // Get state migration point properties from site control file.
          IResultObject ro = connection.GetInstance(
              "SMS_SCI_SysResUse.FileType=2,ItemName='[\"Display=\\\\" +
              serverName +
              "\\\"]MSWNET:[\"SMS_SITE=" +
              siteCode + "\"]\\\\" +
              serverName +
              "\\,SMS State Migration Point',ItemType='System Resource
  Usage',SiteCode='" +
              siteCode +
              "'"
              );

          // Get directories.
          Dictionary<string, IResultObject> embeddedPropertyLists =
  ro.EmbeddedPropertyLists;

          string[] directories = embeddedPropertyLists["Directories"]
  ["Values"].StringArrayValue; // Current directories.

          List<string> directoriesList = new List<string>(); // convert to
  list.
          foreach (string directoryName in directories)
          {
              directoriesList.Add(directoryName);
          }

          directoriesList.Add(smpSettings);

          // Update the embedded property list.
          embeddedPropertyLists["Directories"]["Values"].StringArrayValue =
  directoriesList.ToArray();

          ro.EmbeddedPropertyLists = embeddedPropertyLists;

          // Commit changes.
          ro.Put();
      }
      catch (SmsException e)
      {
          Console.WriteLine("failed to update SMP settings" + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                 ﾉ    Expand table

<!-- p.968 -->

 Parameter          Type                       Description

 connection         - Managed:                 A valid connection to the SMS Provider.
                    WqlConnectionManager
                    - VBScript:
                    SWbemServices

 context            - VBScript: SWbemContext   A valid context object. For more information,
 (VBScript)                                    see How to Add a Configuration Manager
                                               Context Qualifier by Using WMI.

 directory          - Managed: String          The folder to be added.
                    - VBScript: String

 maxClients         - Managed: Integer         The maximum number of supported clients.
                    - VBScript: Integer

 minDiskSpace       - Managed: Integer         The minimum disk space.
                    - VBScript: Integer

 minDiskSpaceUnit   - Managed: Integer         The minimum disk space unit.
                    - VBScript: Integer

 serverName         - Managed: String          The Configuration Manager server that the state
                    - VBScript: String         migration point is running on.

 siteCode           - Managed: String          The site code for the site that is running the
                    - VBScript: String         state migration point site role.

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System.Globalization

<!-- p.969 -->

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

<!-- p.970 -->

How to Set the Restore-Only Mode for a
State Migration Point
Article • 10/04/2022

In Configuration Manager, you configure the operating system deployment state
migration point to reject new requests to store user data by setting the
SMPQuiesceState embedded property.

SMPQuiesceState has two possible values.

                                                                           ﾉ   Expand table

 Value                     Definition

 0                         Restore-only mode is turned off.

 1                         Restore-only mode is turned on.

To set the restore only mode for a state migration point
     1. Set up a connection to the SMS Provider. For more information, see SMS Provider
           fundamentals.

     2. Make a connection to the state migration point resources section of the site
           control file.

     3. Get the embedded properties.

     4. Update SMPQuiesceState.

     5. Commit the changes to the site control file.

Example
The following example method sets the restore-only mode based on supplied value.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

     vbs

     Sub SetRestoreOnlyMode(connection,                           _
                            context,                          _

<!-- p.971 -->

                         siteCode,                _
                         enableRestoreOnlyMode)

    ' Load site control file and get SMS State Migration Point section.
    connection.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , context

     Query = "SELECT * FROM SMS_SCI_SysResUse " & _
             "WHERE RoleName = 'SMS State Migration Point' " & _
             "AND SiteCode = '" & siteCode & "'"

     Set SCIComponentSet = connection.ExecQuery(Query, , , context)

     ' Only one instance is returned from the query.
     For Each SCIComponent In SCIComponentSet

         ' Display state migration point server name.
         wscript.echo "SMS State Migration Point Server: " &
SCIComponent.NetworkOSPath

        ' Loop through the array of embedded property instances.
        For Each vProperty In SCIComponent.Props

               ' Setting: SMPQuiesceState
               If vProperty.PropertyName = "SMPQuiesceState" Then
                   wscript.echo " "
                   wscript.echo vProperty.PropertyName
                   wscript.echo "Current value " & vProperty.Value

                   ' Modify the value.
                   vProperty.Value = enableRestoreOnlyMode
                   wscript.echo "New value " & enableRestoreOnlyMode
               End If

        Next

                ' Update the component in your copy of the site control file.
Get the path
                ' to the updated object, which could be used later to retrieve
the instance.
                Set SCICompPath = SCIComponent.Put_( , context)
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

<!-- p.972 -->

  public void SetRestoreOnlyMode(
      WqlConnectionManager connection,
      string server,
      string siteCode,
      bool enableRestoreOnlyMode)
  {
      try
      {
          // Get the site control file.
          IResultObject ro =
  connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName='[\"Display=\\
  \\" + server + "\\\"]MSWNET:[\"SMS_SITE=" + siteCode + "\"]\\\\" + server +
  "\\,SMS State Migration Point',ItemType='System Resource Usage',SiteCode='"
  + siteCode + "'");

          // Get the embedded properties.
          Dictionary<string, IResultObject> embeddedProperties =
  ro.EmbeddedProperties;

          // Set the restore only mode.
          embeddedProperties["SMPQuiesceState"]["Value"].BooleanValue =
  enableRestoreOnlyMode;

              ro.EmbeddedProperties = embeddedProperties;

              // Commmit the changes.
              ro.Put();
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to set restore only mode" + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter               Type                       Description

 connection              - Managed:                 A valid connection to the SMS Provider.
                         WqlConnectionManager
                         - VBScript:
                         SWbemServices

 context (VBScript)      - VBScript: SWbemContext   A valid context object. For more
                                                    information, see How to Add a
                                                    Configuration Manager Context Qualifier by
                                                    Using WMI.

<!-- p.973 -->

 Parameter               Type                  Description

 server                  - Managed: String     The Configuration Manager server that the
                         - VBScript: String    state migration point is running on.

 siteCode                - Managed: String     The Configuration Manager site code.
                         - VBScript: String

 enableRestoreOnlyMode   - Managed: Boolean    Sets the restore only mode.
                         - VBScript: Integer
                                               - Managed: true turns restore only mode
                                               on; otherwise false .
                                               - VBScript: 1 turns restore mode on;
                                               otherwise 0 .

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

<!-- p.974 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.975 -->

How to Set the Deletion Policy for a
State Migration Point
Article • 10/04/2022

In Configuration Manager, you configure the state migration point deletion policy by
updating the SMPStoreDeletionDelayTimeInMinutes and
SMPStoreDeletionCycleTimeInMinutes embedded properties. The deletion policy
defines when the state migration point should remove data marked for deletion.

  ７ Note

  The Configuration Manager console displays the deletion delay time in days,
  whereas SMPStoreDeletionDelayTimeInMinutes and
  SMPStoreDeletionCycleTimeInMinutes are stored in minutes.

To set the deletion policy
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Make a connection to the state migration point resources section of the site
        control file.

   3. Get the embedded properties.

   4. Update SMPStoreDeletionDelayTimeInMinutes and
        SMPStoreDeletionCycleTimeInMinutes .

   5. Commit the changes to the site control file.

Example
The following example method sets the deletion policy for a state migration point. The
example receives the number of days, converts the value to minutes, and updates the
deletion policy accordingly.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

<!-- p.976 -->

Sub SetDeletionPolicy(connection,           _
                      context,            _
                      siteCode,                   _
                      deletionPolicyDays)

    ' Load site control file and get SMS state migration point section.
    connection.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , context

       Query = "SELECT * FROM SMS_SCI_SysResUse " & _
               "WHERE RoleName = 'SMS State Migration Point' " & _
               "AND SiteCode = '" & siteCode & "'"

       Set SCIComponentSet = connection.ExecQuery(Query, , , context)

       ' Convert days to minutes (1440 = 24 *60).
       deletionDelayMinutes = deletionPolicyDays * 1440
       deletionCycleMinutes = 1440

       ' Only one instance is returned from the query.
       For Each SCIComponent In SCIComponentSet

         ' Display state migration point server name.
         wscript.echo "SMS State Migration Point Server: " &
SCIComponent.NetworkOSPath

          ' Loop through the array of embedded property instances.
          For Each vProperty In SCIComponent.Props

                 ' Setting: SMPStoreDeletionDelayTimeInMinutes
                 If vProperty.PropertyName = "SMPStoreDeletionDelayTimeInMinutes"
Then
                    wscript.echo " "
                    wscript.echo vProperty.PropertyName
                    wscript.echo "Current value " & vProperty.Value

                     ' Modify the value.
                     vProperty.Value = deletionDelayMinutes
                     wscript.echo "New value " & deletionDelayMinutes
                 End If

             ' Setting: SMPStoreDeletionCycleTimeInMinutes
             If vProperty.PropertyName = "SMPStoreDeletionCycleTimeInMinutes"
Then
                    wscript.echo " "
                    wscript.echo vProperty.PropertyName
                    wscript.echo "Current value " & vProperty.Value

                     ' Modify the value.
                     vProperty.Value = deletionCycleMinutes
                     wscript.echo "New value " & deletionCycleMinutes
                 End If

          Next

<!-- p.977 -->

                ' Update the component in your copy of the site control file.
Get the path
                ' to the updated object, which could be used later to retrieve
the instance.
                Set SCICompPath = SCIComponent.Put_( , context)
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

public void SetDeletionPolicy(
WqlConnectionManager connection,
string server,
string siteCode,
int deletionPolicyDays)
{
    try
    {
        // Get the state migration part of the site control file.
        IResultObject ro =
connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName='[\"Display=\\
\\" +
            server +
            "\\\"]MSWNET:[\"SMS_SITE=" +
            siteCode +
            "\"]\\\\" +
            server +
            "\\,SMS State Migration Point',ItemType='System Resource
Usage',SiteCode='" +
            siteCode +
            "'");

        // Convert to minutes.
        Dictionary<string, IResultObject> embeddedProperties =
ro.EmbeddedProperties; // Get a copy
        int deletionDelayMinutes = 0;
        int deletionCycleMinutes = 0;
        if (deletionPolicyDays > 0)
        {
            // Convert days to minutes (1440 = 24 *60).
            deletionDelayMinutes = deletionPolicyDays * 1440;
            deletionCycleMinutes = 1440;

<!-- p.978 -->

          }
          // Update deletion policy.
          embeddedProperties["SMPStoreDeletionDelayTimeInMinutes"]
  ["Value"].IntegerValue = deletionDelayMinutes;
          embeddedProperties["SMPStoreDeletionCycleTimeInMinutes"]
  ["Value"].IntegerValue = deletionCycleMinutes;

              ro.EmbeddedProperties = embeddedProperties;

              // Commit changes.
              ro.Put();
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to set deletion policy: " + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter            Type                       Description

 connection           - Managed:                 A valid connection to the SMS Provider.
                       WqlConnectionManager
                      - VBScript:
                      SWbemServices

 context (VBScript)   - VBScript: SWbemContext   A valid context object. For more information,
                                                 see How to Add a Configuration Manager
                                                 Context Qualifier by Using WMI.

 server               - Managed: String          The Configuration Manager server that the
                      - VBScript: String         state migration point is running on.

 siteCode             - Managed: String          The Configuration Manager site code.
                      - VBScript: String

 deletionPolicyDays   - Managed: Integer         Number of days before data deletion.
                      - VBScript: Integer

Compiling the Code
The C# example has the following compilation requirements:

<!-- p.979 -->

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
Configuration Manager role-based administration .

See Also
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.980 -->

How to Enable a PXE Service Point Role
Article • 10/04/2022

You enable the PXE Service Point role, in Configuration Manager, by getting an instance
of a specific distribution point and setting the IsPXE value to 1 .

To enable a PXE service point role
   1. Set up a connection to the SMS Provider. For more information see, SMS Provider
       fundamentals.

   2. Get an instance of a specific distribution point.

   3. Set the IsPXE embedded property to 1 .

   4. Save the distribution point instance.

Example
The following example method enables a PXE service point.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void EnablePXE(WqlConnectionManager connection,
  string siteCode,                       string serverName){    try    {
  //Connect to distribution point instance.
  IResultObject siteRole =
  connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName=\"
  [\\\"Display=\\\\\\\\" + serverName + "\\\\\\\"]MSWNET:[\\\"SMS_SITE=" +
  siteCode + "\\\"]\\\\\\\\" + serverName + "\\\\,SMS Distribution
  Point\",ItemType=\"System Resource Usage\",SiteCode=" + "\"" + siteCode +
  "\"");         // Create temporary copy of the embedded properties.
  Dictionary<string, IResultObject> embeddedProperties =
  siteRole.EmbeddedProperties;         // Enumerate through the embedded
  properties and makes changes as needed.         foreach (KeyValuePair<string,
  IResultObject> kvp in siteRole.EmbeddedProperties)         {             //
  Setting: IsPXE             if (kvp.Value.PropertyList["PropertyName"] ==
  "IsPXE")             {                // Get current property value.
  Console.WriteLine();                 Console.WriteLine("Property: {0}",
  kvp.Value.PropertyList["PropertyName"]);
  Console.WriteLine("Current value: {0} (0 not enabled, 1 enabled)",
  kvp.Value.PropertyList["Value"]);                 // Change value to enable
  PXE (1 enabled, 0 not enabled).                  embeddedProperties["IsPXE"]

<!-- p.981 -->

  ["Value"].StringValue = "1";                 Console.WriteLine("Setting the
  {0} value to {1}.", kvp.Value.PropertyList["PropertyName"], "1");
  }         }       // Store the settings that have changed.
  siteRole.EmbeddedProperties = embeddedProperties;         // Save the
  settings.         siteRole.Put();     }    catch (SmsException ex)    {
  Console.WriteLine();         Console.WriteLine("Failed. Error: " +
  ex.InnerException.Message);     }}

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter    Type                       Description

 connection   Managed:                   A valid connection to the SMS Provider.
              WqlConnectionManager

 siteCode     Managed: String            The Configuration Manager site code.

 serverName   Managed: String            The server name. For example,
                                         "SERVER1.DOMAIN1.COM"

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

<!-- p.982 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
SMS_SCI_SysResUse Server WMI Class
PackNALPath Method in Class SMS_NAL_Methods
About OS deployment site role configuration How to Set the Response Delay for a PXE
Service Point
How to Set the PXE Service Point Response to All Network Interfaces
How to Set the PXE Service Point Response to PXE Requests
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.983 -->

How to Disable a PXE Service Point Role
Article • 10/04/2022

You disable the PXE Service Point role, in Configuration Manager, by getting an instance
of a specific distribution point and setting the IsPXE value to 0 .

To disable a PXE service point role
   1. Set up a connection to the SMS Provider. For more information see, SMS Provider
       fundamentals.

   2. Get an instance of a specific distribution point.

   3. Set the IsPXE embedded property to 0 .

   4. Save the distribution point instance.

Example
The following example method disables the PXE service point.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void DisablePXE(WqlConnectionManager connection,
  string siteCode,                                         string serverName){
  try    {         //Connect to distribution point instance.
  IResultObject siteRole =
  connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName=\"
  [\\\"Display=\\\\\\\\" + serverName + "\\\\\\\"]MSWNET:[\\\"SMS_SITE=" +
  siteCode + "\\\"]\\\\\\\\" + serverName + "\\\\,SMS Distribution
  Point\",ItemType=\"System Resource Usage\",SiteCode=" + "\"" + siteCode +
  "\"");         // Create temporary copy of the embedded properties.
  Dictionary<string, IResultObject> embeddedProperties =
  siteRole.EmbeddedProperties;         // Enumerate through the embedded
  properties and makes changes as needed.         foreach (KeyValuePair<string,
  IResultObject> kvp in siteRole.EmbeddedProperties)         {             //
  Setting: IsPXE             if (kvp.Value.PropertyList["PropertyName"] ==
  "IsPXE")             {                // Get current property value.
  Console.WriteLine();                 Console.WriteLine("Property: {0}",
  kvp.Value.PropertyList["PropertyName"]);
  Console.WriteLine("Current value: {0} (0 not enabled, 1 enabled)",
  kvp.Value.PropertyList["Value"]);                 // Change value to disable
  PXE (1 enabled, 0 not enabled).                  embeddedProperties["IsPXE"]

<!-- p.984 -->

  ["Value"].StringValue = "0";                 Console.WriteLine("Setting the
  {0} value to {1}.", kvp.Value.PropertyList["PropertyName"], "0");
  }         }       // Store the settings that have changed.
  siteRole.EmbeddedProperties = embeddedProperties;         // Save the
  settings.         siteRole.Put();     }    catch (SmsException ex)    {
  Console.WriteLine();         Console.WriteLine("Failed. Error: " +
  ex.InnerException.Message);     }}

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter    Type                       Description

 connection   Managed:                   A valid connection to the SMS Provider.
              WqlConnectionManager

 siteCode     Managed: String            The Configuration Manager site code.

 serverName   Managed: String            The server name. For example,
                                         "SERVER1.DOMAIN1.COM"

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

System.Globalization

System.Localization

Assembly
microsoft.configurationmanagement.managementprovider

<!-- p.985 -->

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
SMS_SCI_SysResUse Server WMI Class
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.986 -->

How to Enable Unknown Computer
Support for a PXE Service Point
Article • 10/04/2022

In Configuration Manager, you set the operating system deployment PXE service point
response to incoming PXE requests from unknown computers by setting the
SupportUnknownMachines embedded property.

SupportUnknownMachines has the following possible values.

                                                                                  ﾉ   Expand table

 Value       Description

 0           The PXE service point does not respond to PXE requests from unknown computers.

 1           The PXE service point responds to requests from unknown computers.

To set the PXE service point response to PXE requests
from unknown computers
     1. Set up a connection to the SMS Provider. For more information, see SMS Provider
          fundamentals.

     2. Make a connection to the distribution point instance with PXE enabled.

     3. Get the embedded properties.

     4. Update the SupportUnknownMachines embedded property.

     5. Commit the changes to the site control file.

Example
The following example method sets the response for a PXE request based on the
supplied String value ( allowResponse ).

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

     c#

<!-- p.987 -->

  public void EnablePXE(WqlConnectionManager connection,
  string siteCode,                         string serverName,
  string allowResponse){     try     {         //Connect to distribution point
  instance.                          IResultObject siteRole =
  connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName=\"
  [\\\"Display=\\\\\\\\" + serverName + "\\\\\\\"]MSWNET:[\\\"SMS_SITE=" +
  siteCode + "\\\"]\\\\\\\\" + serverName + "\\\\,SMS Distribution
  Point\",ItemType=\"System Resource Usage\",SiteCode=" + "\"" + siteCode +
  "\"");         // Create temporary copy of the embedded properties.
  Dictionary<string, IResultObject> embeddedProperties =
  siteRole.EmbeddedProperties;          // Enumerate through the embedded
  properties and makes changes as needed.           foreach (KeyValuePair<string,
  IResultObject> kvp in siteRole.EmbeddedProperties)           {            //
  Setting: SupportUnknownMachines               if
  (kvp.Value.PropertyList["PropertyName"] == "SupportUnknownMachines")
  {                 // Get current property value.
  Console.WriteLine();                  Console.WriteLine("Property: {0}",
  kvp.Value.PropertyList["PropertyName"]);
  Console.WriteLine("Current value: {0}", kvp.Value.PropertyList["Value"]);
  // Change value.                 embeddedProperties["SupportUnknownMachines"]
  ["Value"].StringValue = allowResponse;
  Console.WriteLine("Setting the {0} value to {1}.",
  kvp.Value.PropertyList["PropertyName"], allowResponse);               }
  }         // Store the settings that have changed.
  siteRole.EmbeddedProperties = embeddedProperties;           // Save the
  settings.          siteRole.Put();     }     catch (SmsException ex)    {
  Console.WriteLine();         Console.WriteLine("Failed. Error: " +
  ex.InnerException.Message);     }}

The example method has the following parameters:

                                                                          ﾉ    Expand table

 Parameter       Type                   Description

 connection      Managed:               A valid connection to the SMS Provider.
                 WqlConnectionManager

 siteCode        Managed: String        The Configuration Manager site code.

 serverName      Managed: String        The server name. For example,
                                        "SERVER1.DOMAIN1.COM" .

 allowResponse   Managed: String        The value to set whether the PXE service point will
                                        respond to unknown computers.

                                        - 0 - The PXE service point does not respond to PXE
                                        requests from unknown computers.
                                        - 1 - The PXE service point responds to requests
                                        from unknown computers.

<!-- p.988 -->

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
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback

<!-- p.989 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.990 -->

How to Set the PXE Service Point
Response to PXE Requests
Article • 10/04/2022

In Configuration Manager, you set the distribution point response to incoming PXE
requests by setting the IsActive embedded property.

IsActive has the following possible values.

                                                                           ﾉ   Expand table

 Value          Description

 0              The distribution point does not respond to PXE requests.

 1              The distribution service point responds to requests.

To set the distribution point response to PXE requests
     1. Set up a connection to the SMS Provider. For more information, see SMS Provider
          fundamentals.

     2. Make a connection to the distribution point instance with PXE enabled.

     3. Get the embedded properties.

     4. Update the IsActive embedded property.

     5. Commit the changes to the site control file.

Example
The following example method sets the response for a PXE request based on the
supplied String value ( allowResponse ).

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

     c#

     public void SetAllowResponse(WqlConnectionManager connection,
     string siteCode,                                  string serverName,
     string allowResponse){    try    {        //Connect to distribution point

<!-- p.991 -->

  instance.                          IResultObject siteRole =
  connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName=\"
  [\\\"Display=\\\\\\\\" + serverName + "\\\\\\\"]MSWNET:[\\\"SMS_SITE=" +
  siteCode + "\\\"]\\\\\\\\" + serverName + "\\\\,SMS Distribution
  Point\",ItemType=\"System Resource Usage\",SiteCode=" + "\"" + siteCode +
  "\"");         // Create temporary copy of the embedded properties.
  Dictionary<string, IResultObject> embeddedProperties =
  siteRole.EmbeddedProperties;          // Enumerate through the embedded
  properties and makes changes as needed.          foreach (KeyValuePair<string,
  IResultObject> kvp in siteRole.EmbeddedProperties)           {            //
  Setting: IsActive             if (kvp.Value.PropertyList["PropertyName"] ==
  "IsActive")             {                 // Get current property value.
  Console.WriteLine();                  Console.WriteLine("Property: {0}",
  kvp.Value.PropertyList["PropertyName"]);
  Console.WriteLine("Current value: {0}", kvp.Value.PropertyList["Value"]);
  // Change value.                 embeddedProperties["IsActive"]
  ["Value"].StringValue = allowResponse;
  Console.WriteLine("Setting the {0} value to {1}.",
  kvp.Value.PropertyList["PropertyName"], allowResponse);               }
  }         // Store the settings that have changed.
  siteRole.EmbeddedProperties = embeddedProperties;           // Save the
  settings.          siteRole.Put();     }    catch (SmsException ex)     {
  Console.WriteLine();         Console.WriteLine("Failed. Error: " +
  ex.InnerException.Message);     }}

The example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter       Type                   Description

 connection      Managed:               A valid connection to the SMS Provider.
                 WqlConnectionManager

 siteCode        Managed: String        The Configuration Manager site code.

 serverName      Managed: String        The server name. For example,
                                        "SERVER1.DOMAIN1.COM" .

 allowResponse   Managed: String        The value to set whether the distribution point will
                                        respond to PXE requests.

                                        - 0 - The distribution point does not respond to
                                        PXE requests.
                                        - 1 - The PXE service point responds to requests
                                        from unknown computers.

Compiling the Code

<!-- p.992 -->

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
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.993 -->

How to Set the Response Delay for a
PXE Service Point
Article • 10/04/2022

In Configuration Manager, you set the operating system deployment PXE service point
response delay by updating the ResponseDelay embedded property. ResponseDelay
specifies how long the delay should be for this PXE service point before it responds to
computer requests when multiple PXE service points are used. By default, the
Configuration Manager PXE service point will respond immediately to the network PXE
requests.

The delay is provided by the PXE client, and it shows the time that has passed since the
client started the PXE boot process (seconds elapsed since client began address
acquisition or renewal process). A client sends requests to the server at intervals of 0
(default), 4, 8, 16, or 32 seconds.

To set the response delay for a PXE service point
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
       fundamentals.

   2. Make a connection to the distribution point instance with PXE enabled.

   3. Get the embedded properties.

   4. Update the ResponseDelay embedded property.

   5. Commit the changes to the site control file.

Example
The following example method sets the response delay for a PXE service point.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void SetResponseDelay(WqlConnectionManager connection,
  string siteCode,                                  string serverName,
  int delay){    try    {        //Connect to distribution point instance.
  IResultObject siteRole =

<!-- p.994 -->

  connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName=\"
  [\\\"Display=\\\\\\\\" + serverName + "\\\\\\\"]MSWNET:[\\\"SMS_SITE=" +
  siteCode + "\\\"]\\\\\\\\" + serverName + "\\\\,SMS Distribution
  Point\",ItemType=\"System Resource Usage\",SiteCode=" + "\"" + siteCode +
  "\"");        // Create temporary copy of the embedded properties.
  Dictionary<string, IResultObject> embeddedProperties =
  siteRole.EmbeddedProperties;          // Enumerate through the embedded
  properties and makes changes as needed.          foreach (KeyValuePair<string,
  IResultObject> kvp in siteRole.EmbeddedProperties)          {             //
  Setting: ResponseDelay              if (kvp.Value.PropertyList["PropertyName"]
  == "ResponseDelay")             {                 // Get current property
  value.                 Console.WriteLine();
  Console.WriteLine("Property: {0}", kvp.Value.PropertyList["PropertyName"]);
  Console.WriteLine("Current value: {0}", kvp.Value.PropertyList["Value"]);
  // Change value.                  embeddedProperties["ResponseDelay"]
  ["Value"].IntegerValue = delay;                  Console.WriteLine("Setting
  the {0} value to {1}.", kvp.Value.PropertyList["PropertyName"], delay);
  }         }       // Store the settings that have changed.
  siteRole.EmbeddedProperties = embeddedProperties;          // Save the
  settings.         siteRole.Put();      }    catch (SmsException ex)    {
  Console.WriteLine();         Console.WriteLine("Failed. Error: " +
  ex.InnerException.Message);     }}

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter    Type                       Description

 connection   Managed:                   A valid connection to the SMS Provider.
              WqlConnectionManager

 siteCode     Managed: String            The Configuration Manager site code.

 serverName   Managed: String            The server name. For example,
                                         "SERVER1.DOMAIN1.COM" .

 delay        Managed: Integer           The delay, in seconds.

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

<!-- p.995 -->

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
About OS deployment site role configuration How to Read and Write to the
Configuration Manager Site Control File by Using Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.996 -->

How to Set the PXE Service Point
Response to All Network Interfaces
Article • 10/04/2022

In Configuration Manager, you set the operating system deployment PXE service point
response to network interfaces by setting the BindPolicy embedded property.

BindPolicy has the following possible values.

                                                                         ﾉ   Expand table

 Value         Description

 0             Responds to PXE requests on all network interfaces.

 1             Responds to requests on specific network interfaces.

If BindPolicy is set to respond to specific network interfaces (1), you must add the
media access control (MAC) addresses for the required network interfaces by using the
BindExcept list. If BindExcept is not populated, PXE will not respond to any requests. For

more information see, How to Set the PXE Service Point Response for a Specific Network
Interface.

To set the PXE response to network interfaces
     1. Set up a connection to the SMS Provider. For more information, see SMS Provider
       fundamentals.

     2. Make a connection to the distribution point instance with PXE enabled.

     3. Get the embedded properties.

     4. Update the BindPolicy embedded property.

     5. Commit the changes to the site control file.

Example
The following example method sets the PXE service point response to a network
interface. If respondToSpecificInterface is set to 1 you must set the BindExcept list to

<!-- p.997 -->

specify the network interfaces that can respond. For more information, see How to Set
the PXE Service Point Response for a Specific Network Interface.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void SetNetworkInterface(WqlConnectionManager connection,
  string siteCode,                                   string serverName,
  string respondToSpecificInterface){     try    {        //Connect to
  distribution point instance.                         IResultObject siteRole =
  connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName=\"
  [\\\"Display=\\\\\\\\" + serverName + "\\\\\\\"]MSWNET:[\\\"SMS_SITE=" +
  siteCode + "\\\"]\\\\\\\\" + serverName + "\\\\,SMS Distribution
  Point\",ItemType=\"System Resource Usage\",SiteCode=" + "\"" + siteCode +
  "\"");        // Create temporary copy of the embedded properties.
  Dictionary<string, IResultObject> embeddedProperties =
  siteRole.EmbeddedProperties;         // Enumerate through the embedded
  properties and makes changes as needed.         foreach (KeyValuePair<string,
  IResultObject> kvp in siteRole.EmbeddedProperties)         {            //
  Setting: BindPolicy             if (kvp.Value.PropertyList["PropertyName"] ==
  "BindPolicy")            {                 // Get current property value.
  Console.WriteLine();                 Console.WriteLine("Property: {0}",
  kvp.Value.PropertyList["PropertyName"]);
  Console.WriteLine("Current value: {0}", kvp.Value.PropertyList["Value"]);
  // Change value.                 embeddedProperties["BindPolicy"]
  ["Value"].StringValue = respondToSpecificInterface;
  Console.WriteLine("Setting the {0} value to {1}.",
  kvp.Value.PropertyList["PropertyName"], respondToSpecificInterface);
  }         }       // Store the settings that have changed.
  siteRole.EmbeddedProperties = embeddedProperties;         // Save the
  settings.         siteRole.Put();     }    catch (SmsException ex)    {
  Console.WriteLine();         Console.WriteLine("Failed. Error: " +
  ex.InnerException.Message);     }}

The example method has the following parameters:

                                                                         ﾉ    Expand table

 Parameter                 Type                     Description

 connection                Managed:                 A valid connection to the SMS Provider.
                           WqlConnectionManager

 siteCode                  Managed: String          The Configuration Manager site code.

 serverName                Managed: String          The server name. For example,
                                                    "SERVER1.DOMAIN1.COM" .

<!-- p.998 -->

 Parameter                   Type                  Description

 respondToSpecficInterface   Managed: String       The value to set which network
                                                   interfaces will respond to PXE requests.

                                                   - 0 - Responds to PXE requests on all
                                                   network interfaces.
                                                   - 1 - Responds to requests on specific
                                                   network interfaces.

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

<!-- p.999 -->

About OS deployment site role configuration How to Set the PXE Service Point Response
for a Specific Network Interface
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1000 -->

How to Set the PXE Service Point
Response for a Specific Network
Interface
Article • 10/04/2022

In Configuration Manager, you set the operating system deployment to respond to a
specific set of network addresses by adding the required media access control (MAC)
addresses to the BindExcept embedded property list. You must also set the BindPolicy
embedded property to 1. This specifies that PXE requests are accepted on specified
network address only. For more information about setting BindPolicy , see How to Set
the PXE Service Point Response to All Network Interfaces.

To set the response for a specific network interface
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
       fundamentals.

   2. Make a connection to the PXE service point resources section of the site control
       file.

   3. Get the BindExcept embedded property list.

   4. Add the MAC addresses to the BindExcept embedded property list.

   5. Commit the changes to the site control file.

Example
The following example method adds a supplied MAC address to the list of MAC address
that are responded to.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void SetNetworkInterface(WqlConnectionManager connection,
  string siteCode,                                string serverName,
  string macAddress){    try    {        //Connect to distribution point
  instance.                        IResultObject siteRole =
  connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName=\"
