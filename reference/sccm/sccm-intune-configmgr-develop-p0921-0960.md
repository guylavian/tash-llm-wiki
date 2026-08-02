---
title: "Configuration Manager SDK documentation — pages 921-960"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0921-0960
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0921-0960
family: sccm
documentKind: "doc"
abstract: "How to Enable Software Inventory Article • 10/10/2022 You enable or disable the Software Inventory Client Agent, in Configuration Manager, by modifying the site control file settings. To enable or disable the Software Inventory Updates Client Agent 1. Set up a connection to the"
---

# Configuration Manager SDK documentation — pages 921-960

<!-- p.921 -->

How to Enable Software Inventory
Article • 10/10/2022

You enable or disable the Software Inventory Client Agent, in Configuration Manager, by
modifying the site control file settings.

To enable or disable the Software Inventory Updates
Client Agent
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Software Inventory Client Agent section of the site
        control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example method enables or disables the Software Inventory Client Agent
by using the SMS_SCI_ClientComp class to connect to the site control file and change
properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnableDisableSoftwareInventoryClientAgent(swbemServices, swbemContext,
  enableDisableFlag, siteCode )

      ' Load site control file and get software inventory agent client
  component section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext
      Set objSWbemInst =
  swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
  Component',Sitecode='" & siteCode & "',ItemName='Software Inventory Agent'",
  , swbemContext)

         ' Display client agent settings before changing the properties.
         Wscript.Echo " "
         Wscript.Echo "Properties - Before Change"

<!-- p.922 -->

     Wscript.Echo "---------------------------"
     Wscript.Echo objSWbemInst.ClientComponentName
     Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

    ' Set client agent by setting the Flags value to    0 or 1 using the
enableDisableFlag variable.
    objSWbemInst.Flags = enableDisableFlag

    ' Save the new client agent settings.
    objSWbemInst.Put_ , swbemContext
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Commit", , , swbemContext

    ' Refresh in-memory copy of the site control file and get the client
component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteCode & "',ItemName='Software Inventory Agent'",
, swbemContext)

     ' Display the client agent settings after change.
     Wscript.Echo " "
     Wscript.Echo "Properties - After Change"
     Wscript.Echo "---------------------------"
     Wscript.Echo objSWbemInst.ClientComponentName
     Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

End Sub

c#

public void EnableDisableSoftwareInventoryClientAgent(WqlConnectionManager
connection,
                                                      string
enableDisableFlag,
                                                      string siteCode)
{
    try
    {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Software Inventory
Agent'");

          // Display client agent settings before changing the properties.
          Console.WriteLine();
          Console.WriteLine("Properties - Before Change");
          Console.WriteLine("---------------------------");

<!-- p.923 -->

  Console.WriteLine(siteDefinition["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");

          // Set client agent by setting "Flags" value to 0 or 1 by using the
  enableDisableFlag variable.
          siteDefinition["Flags"].StringValue = enableDisableFlag;

             // Save the settings.
             siteDefinition.Put();

          // Verify the change by reconnecting and getting the value again.
          IResultObject siteDefinition2 =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" + siteCode + "',ItemName='Software Inventory
  Agent'");

             // Display client agent settings after changing the properties.
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

 Parameter          Type                       Description

 - connection       - Managed:                 A valid connection to the SMS Provider.
 - swbemServices     WqlConnectionManager
                    - VBScript:
                    SWbemServices

 swbemContext       - VBScript: SWbemContext   A valid context object. For more information,
                                               see How to Add a Configuration Manager
                                               Context Qualifier by Using WMI.

<!-- p.924 -->

 Parameter           Type                  Description

 siteCode            - Managed: String     The site code.
                     - VBScript: String

 enableDisableFlag   - Managed: String     Determines whether the Software Inventory
                     - VBScript: String    client agent is enabled or disabled.

                                           0 - Disabled

                                           1 - Enabled

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

<!-- p.925 -->

See Also
Configuration Manager Software Development Kit
About Configuration Manager Inventory
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.926 -->

How to Configure Software Inventory
Settings
Article • 10/10/2022

You set the Software Inventory Client Agent settings, in Configuration Manager, by
modifying the necessary site control file settings.

To modify the Software Inventory Client Agent settings
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Software Inventory Client Agent section of the site
        control file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example sets the Software Inventory Client Agent settings by using the
SMS_SCI_ClientComp class to connect to the site control file and change properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureSoftwareInventoryClientAgentSettings(swbemServices,
  _
                                                    swbemContext,
  _
                                                    siteCode,
  _
                                                    enableDisableClientAgent,
  _
                                                    newInventorySchedule)

      ' Load site control file and get the SMS_SCI_ClientComp section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_ClientComp " & _
         "WHERE ClientComponentName = 'Software Inventory Agent' " & _

<!-- p.927 -->

       "AND SiteCode = '" & siteCode & "'"

    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

       'Only one instance is returned from the query.
       For Each SCIComponent In SCIComponentSet

        ' Set the client agent by setting the Flags value to 0 or 1 using
the enableDisableClientAgent variable.
        wscript.echo " "
        wscript.echo "Software Inventory Agent"
        wscript.echo "Current value " & SCIComponent.Flags

          ' Modify the value.
          SCIComponent.Flags = enableDisableClientAgent
          wscript.echo "New value " & enableDisableClientAgent

          'Loop through the array of embedded SMS_EmbeddedProperty instances.
          For Each vProperty In SCIComponent.Props

                 ' Setting: Inventory Schedule
                 If vProperty.PropertyName = "Inventory Schedule" Then
                     wscript.echo " "
                     wscript.echo vProperty.PropertyName
                     wscript.echo "Current value " & vProperty.Value2

                     'Modify the value.
                     vProperty.Value2 = newInventorySchedule
                     wscript.echo "New value " & newInventorySchedule
                 End If

          Next

          'Update the component in your copy of the site control file. Get the
path
        'to the updated object, which could be used later to retrieve the
instance.
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

<!-- p.928 -->

c#

public void
ConfigureSoftwareInventoryClientAgentSettings(WqlConnectionManager
connection,
                                                          string siteCode,
                                                          string
enableDisableClientAgent,
                                                          string
newInventorySchedule)
{
    try
    {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Software Inventory
Agent'");

        // Setting: Enable Client Agent
        // Enable or disable the client agent by setting the Flags value to
0 or 1 using the enableDisableClientAgent variable.
        Console.WriteLine();
        Console.WriteLine("Software Update Client Agent");
        Console.WriteLine("Current value: " +
siteDefinition["Flags"].StringValue);

       // Change value using the enableDisableSUMClientAgent value passed
in.
       siteDefinition["Flags"].StringValue = enableDisableClientAgent;
       Console.WriteLine("New value    : " + enableDisableClientAgent);

        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Create temporary working copy of embedded properties.
            Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

             // Setting: Inventory Schedule
             if (kvp.Value.PropertyList["PropertyName"] == "Inventory
Schedule")
             {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value2"].StringValue);

                 // Change value using the newEvaluationSchedule value passed
in.
                embeddedProperties["Inventory Schedule"]
["Value2"].StringValue = newInventorySchedule;
                Console.WriteLine("New value    : " + newInventorySchedule);

<!-- p.929 -->

                   }

                   // Store the settings that have changed.
                   siteDefinition.EmbeddedProperties = embeddedProperties;
             }

             //Save the settings.
             siteDefinition.Put();

       }
       catch (SmsException ex)
       {
           Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
           throw;
       }
  }

The example method has the following parameters:

                                                                                ﾉ   Expand table

 Parameter                  Type                       Description

 - connection               - Managed:                 A valid connection to the SMS Provider.
 - swbemServices             WqlConnectionManager
                            - VBScript:
                            SWbemServices

 swbemContext               - VBScript: SWbemContext   A valid context object. For more
                                                       information, see How to Add a
                                                       Configuration Manager Context Qualifier
                                                       by Using WMI.

 siteCode                   - Managed: String          The site code.
                            - VBScript: String

 enableDisableClientAgent   - Managed: String          A value to enable or disable the client
                            - VBScript: String         agent.

                                                       Disabled - 0

                                                       Enabled - 1

 newInventorySchedule       - Managed: String          A value to set the inventory schedule.
                            - VBScript: String

 newScanInterval            - Managed: String          A value to set the scan interval.
                            - VBScript: String

<!-- p.930 -->

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

See Also
About Configuration Manager Inventory
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
About schedules How to Create a Schedule Token

<!-- p.931 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.932 -->

How to Reset the Software Inventory
Cache
Article • 10/10/2022

In Configuration Manager, you reset the software inventory cache by connecting to the
inventory agent namespace and deleting the inventory action status instance for
software inventory.

To reset the software inventory cache
   1. Connect to the inventory agent namespace (root\ccm\invagt).

   2. Delete the inventory action status instance for software inventory ({00000000-
        0000-0000-0000-000000000002}).

Example
The following example method shows how to reset the software inventory cache by
connecting to the inventory agent namespace and deleting the inventory action status
instance for software inventory.

For information about calling the sample code, see How to Call a Configuration
Manager Object Class Method by Using WMI

  vbs

  Sub ResetSoftwareInventoryCache()

         ' Get a connection to the "root\ccm\invagt" namespace.
         Dim locator
         Set locator = CreateObject("WbemScripting.SWbemLocator")
         Dim services
         Set services = locator.ConnectServer( , "root\ccm\invagt")

      ' Delete the specified InventoryActionStatus instance.
      services.Delete "InventoryActionStatus.InventoryActionID='{00000000-
  0000-0000-0000-000000000002}'"

         ' Display message.
         wscript.echo "Reset Software Inventory cache."

  End Sub

<!-- p.933 -->

  c#

  public void ResetSoftwareInventoryCache()
  {
      try
      {
          // Define the scope (namespace).
          ManagementScope inventoryAgentScope = new
  ManagementScope(@"root\ccm\invagt");

          // Load the class that you want to work with.
          ManagementClass inventoryClass = new
  ManagementClass(inventoryAgentScope.Path.Path, "InventoryActionStatus",
  null);

          // Query the class for the InventoryActionID object (create query,
  create searcher object, execute query).
          ObjectQuery query = new ObjectQuery("SELECT * FROM
  InventoryActionStatus WHERE InventoryActionID = '{00000000-0000-0000-0000-
  000000000002}'");
          ManagementObjectSearcher searcher = new
  ManagementObjectSearcher(inventoryAgentScope, query);
          ManagementObjectCollection queryResults = searcher.Get();

          // Enumerate the collection to get to the result (there should only
  be one item returned from the query).
          foreach (ManagementObject result in queryResults)
          {
              // Display message and delete the object.
              Console.WriteLine("Resetting Software Inventory cache.");
              result.Delete();
          }
      }

       catch (System.Management.ManagementException ex)
       {
           Console.WriteLine("Failed to run action. Error: " + ex.Message);
           throw;
       }
  }

Compiling the Code
This C# example requires:

Namespaces
System.Management

<!-- p.934 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
About Configuration Manager Inventory

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.935 -->

How to Import a MOF File to Extend
Inventory
Article • 10/10/2022

You import a MOF file to extend inventory, in Configuration Manager, by using the
ImportInventoryReport method.

To import MOF file to extend hardware inventory
   1. Connect to the site server namespace (root\sms\site_<site code>).

   2. Get the SMS_InventoryReport class.

   3. Invoke the ImportInventoryReport method, passing in the InventoryReportID,
       ImportType, and MofBuffer parameters.

Example
The following example imports a MOF file to extend inventory using the
ImportInventoryReport method.

  c#

  public class ImportInventory{             public const string
  HardwareInventoryReportID = "{00000000-0000-0000-0000-000000000001}";
  static void Main(string[] args)     {        if (args != null && args.Length
  >= 2)         {            string fileName = args[0];             string
  siteCode = args[1];             ImportInventoryReport(siteCode, fileName);
  }        else        {             Console.WriteLine("Usage:
  InventoryImportExample <MofFileName> <site code>");         }
  Console.WriteLine("Press any key to exit");         Console.ReadLine();    }
  public static void ImportInventoryReport(string siteCode, string fileName,
  string inventoryReportID = HardwareInventoryReportID,
  InventoryImportType importOption = InventoryImportType.BothClassAndReport)
  {        if (File.Exists(fileName)==false)         {             throw new
  FileNotFoundException("MOF file not found", fileName);         }
  string mofToImport = File.ReadAllText(fileName);         // Get the
  SMS_InventoryReport class.         try        {            string scope =
  string.Format(@"root\sms\site_{0}",siteCode);             ManagementClass cls
  = new ManagementClass(scope, "SMS_InventoryReport", null);
  ManagementBaseObject inParams =
  cls.GetMethodParameters("ImportInventoryReport");
  inParams["InventoryReportID"] = inventoryReportID;
  inParams["ImportType"] = (uint)importOption;

<!-- p.936 -->

  inParams["MofBuffer"] = mofToImport;               ManagementBaseObject retVal
  = cls.InvokeMethod("ImportInventoryReport", inParams, null);               //
  Get current site code.               uint resultCode =
  (uint)retVal["StatusCode"];               if (resultCode == 0)            {
  Console.WriteLine("ImportInventoryReport for file {0} succeed ", fileName);
  }            else              {
  Console.WriteLine("ImportInventoryReport for file {0} failed with error
  code:{1} ", fileName,resultCode);               }        }         catch
  (ManagementException e)          {             Console.WriteLine("Failed to
  execute method ImportInventoryReport for file {0}: {1}", fileName,
  e.ToString());         }     }     public enum InventoryImportType     {
  ClassOnly = 1,           ReportOnly = 2,          BothClassAndReport = 3    }}

  wmimof

  An example MOF file.================================[ SMS_Report (TRUE),
  SMS_Group_Name ("User Account"), SMS_Class_ID
  ("MICROSOFT|USER_ACCOUNT|1.0"), Namespace ("root\\\\cimv2") ]class
  Win32_UserAccount : SMS_Class_Template{     [ SMS_Report (TRUE), key ]
  String     Domain;    [ SMS_Report (TRUE), key ]      String      Name;    [
  SMS_Report (TRUE) ]    UInt32      AccountType;     [ SMS_Report (TRUE) ]
  String     Caption;    [ SMS_Report (TRUE) ]     String       Description;    [
  SMS_Report (TRUE) ]    Boolean      Disabled;    [ SMS_Report (TRUE) ]
  String     FullName;    [ SMS_Report (TRUE) ]     DateTime       InstallDate;
  [ SMS_Report (TRUE) ]    Boolean      LocalAccount;     [ SMS_Report (TRUE) ]
  Boolean     Lockout;    [ SMS_Report (TRUE) ]     Boolean
  PasswordChangeable;    [ SMS_Report (TRUE) ]     Boolean       PasswordExpires;
  [ SMS_Report (TRUE) ]    Boolean      PasswordRequired;      [ SMS_Report
  (TRUE) ]    String     SID;     [ SMS_Report (TRUE) ]     UInt8      SIDType;
  [ SMS_Report (TRUE) ]    String      Status;};

The example method has the following parameters:

                                                                        ﾉ   Expand table

 Parameter           Type         Description

 siteCode            - Managed:   The site code.
                     String

 fileName            - Managed:   The name of the MOF file to import.
                     String

 inventoryReportID   - Managed:   Inventory report identifier.
                     String

 importOption        - Managed:   Import type. Possible values are:
                     String
                                  - 1 – Class Only

<!-- p.937 -->

 Parameter           Type          Description

                                   - 2 – Report Only
                                   - 3 – Both Class and Report

 mofToImport         - Managed:    The MOF content that contains the inventory class or report
                         String    to import. This is the same format as the Configuration
                                   Manager 2007 sms_def.mof file, or the file format that you
                                   export from inventory client settings.

Compiling the Code
This C# example requires:

Assembly
System.Management

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
About Configuration Manager Inventory

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.938 -->

How to Initiate a Synchronization
Article • 10/10/2022

The Asset Intelligence catalog can be refreshed manually, outside the normal
synchronization schedule. A manual refresh is accomplished by using the
RequestCatalogUpdate method on the SMS_AIProxy Server WMI Class.

  ） Important

  This method can only be called once within a 12 hours period, subsequent method
  calls will not work.

Refresh the Asset Intelligence catalog
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Query the SMS Provider for the SMS_AIProxy instance that you want refresh the
        catalog on.

   3. Call the SMS_AIProxy class RequestCatalogUpdate method to run an action on the
        collection.

Example
The following example method runs the refresh on the provided server.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Function InitiateSync(connection, serverName)
      On Error Resume Next
      Dim classObj: Set classObj = connection.Get("SMS_AIProxy")
      Dim inParams: Set inParams =
  classObj.Methods_("RequestCatalogUpdate").InParameters.SpawnInstance_()
      Dim outParams
      inParams.Properties_.Item("ProxyName") = serverName
      Set outParams = connection.ExecMethod("SMS_AIProxy",
  "RequestCatalogUpdate", inParams)
      If Err.Number <> 0 Then
          InitiateSync = False

<!-- p.939 -->

      Else
          InitiateSync = True
      End If
      On Error Goto 0
  End Function

  c#

  public void InitiateSync(WqlConnectionManager connection, string serverName)
  {
      try
      {
          Dictionary<string, object> inParams = new Dictionary<string, object>
  ();
          IResultObject classObj = connection.GetClassObject("SMS_AIProxy");
          inParams.Add("ProxyName", serverName);
          Console.WriteLine("Requesting catalog update on server " +
  serverName);
          classObj.ExecuteMethod("RequestCatalogUpdate", inParams);
      }
      catch (SmsException ex)
      {
          Console.WriteLine(String.Format("Failed to request catalog update on
  server {0}. Error: {1}", serverName, ex.Message));
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter    Type                      Description

 connection   Managed:                  A valid connection to the provider.
              WqlConnectionManager

              VBScript: SWbemServices

 serverName   Managed: String           Name of the server to run the refresh on. This name
                                        maps to the ProxyName property of an SMS_AIProxy
              VBScript: String          instance.

Compiling the Code
The C# example requires:

<!-- p.940 -->

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

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.941 -->

How to Configure Mobile Device Client
Agent Settings
Article • 10/04/2022

You configure the Mobile Device Client Agent settings, in Configuration Manager, by
modifying the site control file.

  ） Important

  This article only applies to the mobile device legacy client.

To configure the Mobile Device Client Agent settings
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Device Client section of the site control file by using the
        SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the property changes to the site control file.

Example
The following example method configures various Mobile Device Client Agent settings
by using the SMS_SCI_ClientComp class to connect to the site control file and change
properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureMobileDeviceClientAgentSettings(swbemServices,
  _
                                               swbemContext,
  _
                                               siteCode,
  _
                                               newPollIntervalMinutes,
  _

<!-- p.942 -->

                                             newPollIntervalHours,
_
                                             newFailureRetryCount,
_
                                             newFailureRetryIntervalMinutes,
_
                                             newFailureRetryIntervalHours,
_

newEnableDisableSoftwareDistribution)

    ' Variables to build poll interval string.
    ' Note: The sample code only passes in minutes and hours, so setting
empty values to use.
    emptySeconds = "00"
    emptyDays = "00"
    emptyMonths = "00"
    emptyYears = "0000"

    ' Build newPollInterval string (the format must be "0000-00-00
00:00:00").
    newPollInterval = emptyYears & "-" & emptyMonths & "-" & emptyDays & " "
& newPollIntervalHours & ":" & newPollIntervalMinutes & ":" & emptySeconds
    newFailureRetryInterval = emptyYears & "-" & emptyMonths & "-" &
emptyDays & " " & newFailureRetryIntervalHours & ":" &
newFailureRetryIntervalMinutes & ":" & emptySeconds

    ' Load site control file and get the client component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext

    Query = "SELECT * FROM SMS_SCI_ClientComp " & _
    "WHERE ClientComponentName = 'Device Client' " & _
    "AND SiteCode = '" & siteCode & "'"

    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

       ' Loop through the array of embedded property instances.
       For Each vProperty In SCIComponent.Props

            ' Setting: Poll Interval
            If vProperty.PropertyName = "Poll Interval" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value2

                'Modify the value.
                vProperty.Value2 = newPollInterval
                wscript.echo "New value " & newPollInterval
            End If

<!-- p.943 -->

                 ' Setting: Failure Retry Count
                 If vProperty.PropertyName = "Failure Retry Count" Then
                     wscript.echo " "
                     wscript.echo vProperty.PropertyName
                     wscript.echo "Current value " & vProperty.Value

                     ' Modify the value.
                     vProperty.Value = newFailureRetryCount
                     wscript.echo "New value " & newFailureRetryCount
                 End If

                 ' Setting: Failure Retry Interval
                 If vProperty.PropertyName = "Failure Retry Interval" Then
                     wscript.echo " "
                     wscript.echo vProperty.PropertyName
                     wscript.echo "Current value " & vProperty.Value2

                     ' Modify the value.
                     vProperty.Value2 = newFailureRetryInterval
                     wscript.echo "New value " & newFailureRetryInterval
                 End If

                 ' Setting: Enable Software Dist
                 If vProperty.PropertyName = "Enable Software Dist" Then
                     wscript.echo " "
                     wscript.echo vProperty.PropertyName
                     wscript.echo "Current value " & vProperty.Value2

                ' Modify the value.
                vProperty.Value2 = newEnableDisableSoftwareDistribution
                wscript.echo "New value " &
newEnableDisableSoftwareDistribution
            End If

          Next

        ' Update the component in your copy of the site control file. Get
the path
        ' to the updated object, which could be used later to retrieve the
instance.
        Set SCICompPath = SCIComponent.Put_(wbemChangeFlagUpdateOnly,
swbemContext)

    Next

    ' Commit the change to the actual site control file.
    Set InParams =
swbemServices.Get("SMS_SiteControlFile").Methods_("CommitSCF").InParameters.
SpawnInstance_
    InParams.SiteCode = siteCode
    swbemServices.ExecMethod "SMS_SiteControlFile", "CommitSCF", InParams, ,
swbemContext

End Sub

<!-- p.944 -->

c#

public void ConfigureMobileDeviceClientAgentSettings(WqlConnectionManager
connection,
                                                     string siteCode,
                                                     string
newPollIntervalMinutes,
                                                     string
newPollIntervalHours,
                                                     string
newFailureRetryCount,
                                                     string
newFailureRetryIntervalMinutes,
                                                     string
newFailureRetryIntervalHours,
                                                     bool
newEnableDisableSoftwareDistribution)
{

    // Define variables to build poll interval string.
    // Note: The example code only passes in minutes and hours, so this sets
empty values to use.
    string emptyDays = "00";
    string emptyMonths = "00";
    string emptyYears = "0000";
    string emptySeconds = "00";

    // Build newPollInterval and newFailureRetryInterval strings (the format
must be "0000-00-00 00:00:00").
    string newPollInterval = emptyYears + "-" + emptyMonths + "-" +
emptyDays + " " + newPollIntervalHours + ":" + newPollIntervalMinutes + ":"
+ emptySeconds;
    string newFailureRetryInterval = emptyYears + "-" + emptyMonths + "-" +
emptyDays + " " + newFailureRetryIntervalHours + ":" +
newFailureRetryIntervalMinutes + ":" + emptySeconds;

     try
     {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Device Client'");

        // Loop through the array of embedded properties.
        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Create temporary working copy of embedded properties.
            Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

            // Setting: Poll Interval.

<!-- p.945 -->

            if (kvp.Value.PropertyList["PropertyName"] == "Poll Interval")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value2"].StringValue);

                // Change value using the newPollInterval value passed in.
                embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value2"].StringValue = newPollInterval;
                Console.WriteLine("New value    : " + newPollInterval);
            }

             // Setting: Failure Retry Count.
             if (kvp.Value.PropertyList["PropertyName"] == "Failure Retry
Count")
             {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value"].StringValue);

                 // Change value using the newFailureRetryCount value passed
in.
                embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value"].StringValue = newFailureRetryCount;
                Console.WriteLine("New value    : " + newFailureRetryCount);
            }

             // Setting: Failure Retry Interval.
             if (kvp.Value.PropertyList["PropertyName"] == "Failure Retry
Interval")
             {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value2"].StringValue);

                 // Change value using the newFailureRetryInterval value
passed in.
                embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
["Value2"].StringValue = newFailureRetryInterval;
                Console.WriteLine("New value    : " +
newFailureRetryInterval);
            }

             // Setting: Enable Software Dist.
             if (kvp.Value.PropertyList["PropertyName"] == "Enable Software
Dist")
             {
                 Console.WriteLine();
                 Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);

<!-- p.946 -->

                  Console.WriteLine("Current value: " +
  embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
  ["Value2"].StringValue);

                  // Change value using the
  newEnableDisableSoftwareDistribution value passed in.
                  embeddedProperties[kvp.Value.PropertyList["PropertyName"]]
  ["Value2"].BooleanValue = newEnableDisableSoftwareDistribution;
                  Console.WriteLine("New value    : " +
  newEnableDisableSoftwareDistribution);
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

                                                                            ﾉ    Expand table

 Parameter                             Type                   Description

 connection                            - Managed:             A valid connection to the SMS
                                       WqlConnectionManager   Provider.
 swbemServices                         - VBScript:
                                       SWbemServices

 swbemContext                          - VBScript:            A valid context object. For
                                       SWbemContext           more information, see How to
                                                              Add a Configuration Manager
                                                              Context Qualifier by Using
                                                              WMI.

 siteCode                              - Managed: String      The site code.
                                       - VBScript: String

 newPollInterval                       - Managed: String      The interval that the client tries
                                       - VBScript: String     to contact the server.

<!-- p.947 -->

 Parameter                              Type                  Description

                                                              The format of the string must
                                                              be:

                                                              Years-months-days
                                                              hours:minutes:seconds

                                                              "0000-00-00 00:00:00"

 newPollIntervalMinutes                 - Managed: String     A value representing the
                                        - VBScript: String    minutes of the
                                                              newPollInterval string.

 newPollIntervalHours                   - Managed: String     A value representing the hours
                                        - VBScript: String    of the newPollInterval string.

 newFailureRetryCount                   - Managed: String     A value representing the hours
                                        - VBScript: String    of the newPollInterval string.

 newFailureRetryIntervalMinutes         - Managed: String     A value representing the
                                        - VBScript: String    minutes of the
                                                              newFailureRetryInterval
                                                              string.

 newFailureRetryIntervalHours           - Managed: String     A value representing the hours
                                        - VBScript: String    of the newFailureInterval
                                                              string.

 newEnableDisableSoftwareDistribution   - Managed: Boolean    A value that enables or
                                        - VBScript: Boolean   disables software distribution.

                                                              Enabled = true

                                                              Disabled = false

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

<!-- p.948 -->

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

See Also
About Software Updates Setup and Configuration
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.949 -->

How to Create Software Distribution
Packages, Programs, and
Advertisements for Mobile Devices
Article • 10/04/2022

Configuration Manager device management enables mobile device software distribution
to mobile devices. Packages, programs, and advertisements for mobile devices are much
the same as those for computer clients. For detailed information about creating
packages, programs and advertisements, see the following topics:

      How to Create a Package

      How to Create a Program

      How to Create an Advertisement

  ） Important

  This article only applies to the mobile device legacy client.

Packages
Packages for mobile devices in Configuration Manager generally represent a software
application to be installed on a mobile device, but they might also contain individual
files, updates, or even an individual command.

Configuration Packages
Configuration packages are packages specifically for mobile devices. These packages
contain one or more configuration items. Configuration items are collections of settings
for one or more mobile device platforms.

Programs
Programs for mobile devices in Configuration Manager are commands that are
distributed with a Configuration Manager package that tell a mobile device client what
should occur when the package is received.

<!-- p.950 -->

Advertisements
Advertisements for mobile devices in Configuration Manager allow mobile devices to
download and install available packages. Advertisements for mobile devices are much
the same as advertisements for computer clients. Mobile device advertisement
programs will not run on desktop computers and computer advertisement programs will
not run on mobile devices. Advertisements can be created in two ways, one for each
type of package that can be advertised to mobile devices. The following advertisements
can be sent to mobile devices:

     Advertisements for configuration packages for mobile devices

     Advertisements for software distribution packages for mobile devices

Advertisements for Configuration Packages
Configuration packages are packages specifically for mobile devices. These packages
contain one or more configuration items. Configuration items are collections of settings
for one or more mobile device platforms.

Advertisements for Software Distribution Packages
Advertisements for mobile devices are identical to software distribution packages for
computer clients except that they target mobile devices and contain content that is
appropriate for mobile devices.

See also
     Software distribution overview
     About deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.951 -->

About Operating System Deployment
Site Role Configuration
Article • 10/04/2022

The following two site roles are of particular importance to Operating System
Deployment in Configuration Manager.

State Migration Point Site Role
The state migration point (SMP) is a Configuration Manager site role that provides a
secure location to store user state information before an operating system deployment.
You can store the user state on the SMP while the operating system deployment
proceeds and then restore the user state to the new computer from the SMP. Each SMP
site role can only be a member of one Configuration Manager site.

PXE Service Point Site Role
You use the PXE protocol to initiate operating system deployments to Configuration
Manager clients. Configuration Manager uses the PXE service point site role to initiate
the operating system deployment process. The PXE service point must be configured to
respond to PXE boot requests made by Configuration Manager clients on the network
and then interact with Configuration Manager infrastructure to determine the
appropriate installation actions to take.

Programming the Site Roles
Most information about Configuration Manager site roles is stored in the Configuration
Manager site control file.

You can make updates to the site control file through Windows Management
Instrumentation (WMI) by using the SMS_SiteControlFile class. In managed code,
IResultObject allows access to the site control file. For more information, see About the

Configuration Manager Site Control File.

The properties you will need to access are stored as system resources in the site control
file. For example, the following site control file section shows the properties for the PXE
service point site role.

<!-- p.952 -->

  BEGIN_SYSTEM_RESOURCE_USE
      RESOURCE<Windows NT Server><["Display=\\SERVERNAME\"]MSWNET:
  ["SMS_SITE=ABC"]\\SERVERNAME\>
      ROLE<SMS PXE Service Point>
      PROPERTY <Server Remote Name><><><0>
      PROPERTY <IsActive><><><1>
      PROPERTY <BindPolicy><><><1>
      PROPERTY <ResponseDelay><><><15>
      PROPERTY <PXEPassword><><><0>
      PROPERTY <AuthType><><><0>
      PROPERTY <UserName><><><0>
      PROPERTY <CertificateType><><><0>
      PROPERTY <CertificateExpirationDate><128568119567070000><><0>
      PROPERTY <CertificateFile><><><0>
      PROPERTY <PXECertGUID><XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX><><0>
      BEGIN_PROPERTY_LIST
          <BindExcept>
          <11:11:11:11:11:11>
          <22:22:22:22:22:22>
      END_PROPERTY_LIST
      BEGIN_PROPERTY_LIST
          <Objects Polled By Site Status>
          <["Display=\\SERVERNAME\C$\Program Files\Microsoft Configuration
  Manager\"]MSWNET:["SMS_SITE=ABC"]\\SERVERNAME\C$\Program Files\Microsoft
  Configuration Manager\>
      END_PROPERTY_LIST
  END_SYSTEM_RESOURCE_USE

When you have access to the site control file, the various properties are stored as
embedded properties or in embedded property lists. For example UserName in the
sample above is an embedded property. Other properties are stored as embedded
property lists. In the example above, the MAC addresses in BindExcept are stored in an
embedded property list.

See Also
About the site control file How to Set the Restore-Only Mode for a State Migration Point
How to Track Operating System Deployment Migrations in Configuration Manager
About OS deployment site role configuration

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.953 -->

How to Create a State Migration Point
Role
Article • 10/04/2022

You create the state migration point role, in Configuration Manager, by creating an
instance of SMS_SCI_SysResUse Server WMI Class and providing the property values in
the following table.

                                                                                     ﾉ   Expand table

 Property    Description

 RoleName    Name of the role. For a state migration point, the value is SMS State Migration Point.

 SiteCode    The site code for the site.

 NALPath     The network abstraction layer (NAL) path to the state migration point. For more
             information, see PackNALPath Method in Class SMS_NAL_Methods.

 NALType     The resource type. For a state migration point, this should be Windows NT Server.

You will also need to set initial values for the following embedded properties and
embedded property lists.

                                                                                     ﾉ   Expand table

 Name                                      Description

 Server Remote Name                        The server that has the state migration point. Embedded
                                           property.

 SMPQuiesceState                           Sets the restore-only mode. For more information, see
                                           How to Set the Restore-Only Mode for a State Migration
                                           Point. Embedded property.

 SMPStoreDeletionDelayTimeInMinutes        Sets the deletion policy. For more information, see How to
                                           Set the Deletion Policy for a State Migration Point.
                                           Embedded property.

 SMPStoreDeletionCycleTimeInMinutes        Sets the deletion policy. For more information, see How to
                                           Set the Deletion Policy for a State Migration Point.

 Directories                               Lists the state migration point folders. For more
                                           information, see How to Add a State Migration Point
                                           Folder.

<!-- p.954 -->

To create a state migration point role
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
       fundamentals.

   2. Create an instance of SMS_SCI_SysResUse Server WMI Class.

   3. Populate the properties listed above.

   4. Commit the SMS_SCI_SystResUse object.

Example
The following example method creates a state migration point from the supplied site
code and NAL path. Some helper functions are provided for writing the embedded
properties and embedded property lists to the site control file.

  ） Important

  This example makes use of other state migration point code snippets to set various
  values. The methods AddSmpFolder , SetRestoreOnlyMode , SetDeletionPolicy are
  described in the below topics:

         How to Add a State Migration Point Folder
            How to Set the Restore-Only Mode for a State Migration Point
            How to Set the Deletion Policy for a State Migration Point

         The methods AddSmpFolder , SetRestoreOnlyMode , SetDeletionPolicy must be
         included for the example to work. The methods are not included in the code
         snippets below.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void CreateSmpRole(
        WqlConnectionManager connection,
        string serverName,
        string siteCode,
        string nalPath)
  {
      try
      {

<!-- p.955 -->

        // Create the state migration point resource object.
        IResultObject smpRole =
connection.CreateInstance("SMS_SCI_SysResUse");
        smpRole["RoleName"].StringValue = "SMS State Migration Point";

       // Set the state migration point properties.
       smpRole["SiteCode"].StringValue = siteCode;
       smpRole["NALPath"].StringValue = nalPath;
       smpRole["NALType"].StringValue = "Windows NT Server";

        // Create the embedded property and property lists.
        this.WriteScfEmbeddedProperty(smpRole, "Server Remote Name", 0,
serverName, string.Empty);
        this.WriteScfEmbeddedProperty(smpRole, "SMPQuiesceState", 1,
string.Empty, string.Empty);
        this.WriteScfEmbeddedProperty(smpRole,
"SMPStoreDeletionDelayTimeInMinutes", 0, string.Empty, string.Empty);
        this.WriteScfEmbeddedProperty(smpRole,
"SMPStoreDeletionCycleTimeInMinutes", 0, string.Empty, string.Empty);
        this.WriteScfEmbeddedPropertyList(smpRole, "Directories", null);

       // Commit the site role.
       smpRole.Put();

        // Use SDK snippets to populate some values.
        this.AddSmpFolder(connection, @"C:\temp", 100, 10, 1, serverName,
siteCode);
        this.SetRestoreOnlyMode(connection, serverName, siteCode, true);
        this.SetDeletionPolicy(connection, serverName, siteCode, 10);
    }
    catch (SmsException e)
    {
        Console.WriteLine("Failed to create the state migration point: " +
e.Message);
        throw;
    }
}
public void WriteScfEmbeddedPropertyList(
    IResultObject resource,
    string propertyListName,
    string[] values
    )

    // Create an embedded property list for the supplied resource.
{
    Dictionary<string, IResultObject> EmbeddedPropertyList =
resource.EmbeddedPropertyLists;

    // Get the property list, or create it.
    IResultObject ropl;
    if (EmbeddedPropertyList.ContainsKey(propertyListName))
    {
        ropl = EmbeddedPropertyList[propertyListName];
    }
    else

<!-- p.956 -->

      {
          ConnectionManagerBase connection = resource.ConnectionManager;
          ropl =
  connection.CreateEmbeddedObjectInstance("SMS_EmbeddedPropertyList");
          EmbeddedPropertyList.Add(propertyListName, ropl);
      }

      // Set the property list properties.
      ropl["PropertyListName"].StringValue = propertyListName;
      ropl["Values"].StringArrayValue = values;
      resource.EmbeddedPropertyLists = EmbeddedPropertyList;
  }

  public void WriteScfEmbeddedProperty(
      IResultObject resource,
      string propertyName,
      int value,
      string value1,
      string value2)
  {
      // Properties
      // Server remote name
      Dictionary<string, IResultObject> EmbeddedProperties =
  resource.EmbeddedProperties;

      // Get the property, or create it.
      IResultObject ro;
      if (EmbeddedProperties.ContainsKey(propertyName))
      {
          ro = EmbeddedProperties[propertyName];
      }
      else
      {
          ConnectionManagerBase connection = resource.ConnectionManager;
          ro =
  connection.CreateEmbeddedObjectInstance("SMS_EmbeddedProperty");
          EmbeddedProperties.Add(propertyName, ro);
      }

      ro["PropertyName"].StringValue = propertyName;
      ro["Value"].IntegerValue = value;
      ro["Value1"].StringValue = value1;
      ro["Value2"].StringValue = value2;

      resource.EmbeddedProperties = EmbeddedProperties;
  }

The example method has the following parameters:

                                                                 ﾉ   Expand table

<!-- p.957 -->

 Parameter    Type                   Description

 connection   Managed:               A valid connection to the SMS Provider.
              WqlConnectionManager

 serverName   Managed: String        The Configuration Manager server that the state
                                     migration point is running on.

 siteCode     Managed: String        The Configuration Manager site code.

 nalPath      Managed: String        The NAL path to the state migration point. For example,
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

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security

<!-- p.958 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
SMS_SCI_SysResUse Server WMI Class
PackNALPath Method in Class SMS_NAL_Methods
About OS deployment site role configuration How to Add a State Migration Point Folder
How to Set the Deletion Policy for a State Migration Point
How to Set the Restore-Only Mode for a State Migration Point
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.959 -->

How to Delete a State Migration Point
Role
Article • 10/04/2022

You delete the state migration point role, in Configuration Manager, by deleting the
role's SMS_SCI_SysResUse Server WMI Class object.

To delete a state migration point role
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
       fundamentals.

   2. Get the SMS_SCI_SysResUse Server WMI Class object for the state migration point
       role.

   3. Set the corresponding state migration point to none.

   4. Delete the state migration point SMS_SCI_SysResUse Server WMI Class object.

Example
The following example method deletes the state migration point identified by the site
code and network abstraction layer (NAL) path. The example determines whether the
state migration point has any incomplete state migration restores in process. If there are
any, the current implementation still deletes the state migration point.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void DeleteSmpRole(
       WqlConnectionManager connection,
       string siteCode,
       string nalPath)
   {
       try
       {
           bool smpFound = false;
           Console.WriteLine("About to delete the state migration point");
           string query = string.Format(CultureInfo.InvariantCulture,
        @"SELECT * from SMS_SCI_SysResUse where SiteCode='{0}' AND FileType=2
  AND RoleName='{1}'AND NALPath='{2}'",
        siteCode,

<!-- p.960 -->

      "SMS State Migration Point",
      nalPath.Replace(@"\", @"\\"));

         IResultObject resultObjs =
connection.QueryProcessor.ExecuteQuery(query);

         foreach (IResultObject resultObj in resultObjs)
         {
             smpFound = true;
             if (DeleteSmpOK(resultObj) == true)
             {
                 resultObj.Delete();
             }

             Console.WriteLine("Deleted");
         }

         if (smpFound == false)
         {
             Console.WriteLine("No state migration point was found");
         }
     }
     catch (SmsException e)
     {
         Console.WriteLine("Couldn't delete the state migration point: " +
e.Message);
         throw;
     }

 }

public bool DeleteSmpOK(IResultObject selectedResultObject)
{
    IResultObject resultObjs = null;
    try
    {
        // Locate this state migration point, and determine if it is in
QuiesceState or not, normal deletion
        // if it is not.
        string query = string.Format(CultureInfo.InvariantCulture,
        @"SELECT * from SMS_SCI_SysResUse where SiteCode='{0}' AND
FileType=2 AND NALPath='{1}' AND RoleName='{2}'",
        selectedResultObject["SiteCode"].StringValue,
        selectedResultObject["NALPath"].StringValue.Replace(@"\", @"\\"),
        "SMS State Migration Point");

        resultObjs =
selectedResultObject.ConnectionManager.QueryProcessor.ExecuteQuery(query);

        // Retrieve the state migration point server name because there
could be more than one state migration point on the site, and you want to
        // determine if there are unrestored data stores on only this one.
        string smpServer =
selectedResultObject["NetworkOsPath"].StringValue;
        smpServer = smpServer.Replace(@"\", "");
