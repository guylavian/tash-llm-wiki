---
title: "Configuration Manager SDK documentation — pages 641-680"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0641-0680
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0641-0680
family: sccm
documentKind: "doc"
abstract: "The exception that can be raised is System.Management.ManagementException. See Also About Configuration Manager WMI Programming How to Call a WMI Class Method by Using System.Management How to Connect to the Configuration Manager Client WMI Namespace by Using System.Management H"
---

# Configuration Manager SDK documentation — pages 641-680

<!-- p.641 -->

The exception that can be raised is System.Management.ManagementException.

See Also
About Configuration Manager WMI Programming
How to Call a WMI Class Method by Using System.Management
How to Connect to the Configuration Manager Client WMI Namespace by Using
System.Management
How to Perform an Asynchronous Query by Using System.Management
How to Perform a Synchronous Query by Using System.Management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.642 -->

How to Perform a Synchronous Query
by Using System.Management
Article • 10/10/2022

To synchronously query the Configuration Manager client Windows Management
Instrumentation (WMI), you use a ManagementObjectSearcher object.

To read a lazy property from a Configuration Manager object that is returned in a query,
you get the object instance, which in turn retrieves any lazy object properties from the
SMS Provider.

To perform a synchronous query
   1. Set up a connection to the Configuration Manager client WMI namespace. For
       more information, see How to Connect to the Configuration Manager Client WMI
       Namespace by Using System.Management.

   2. Create a ManagementObjectSearcher collection, and specify a WQL query.

   3. Iterate through the ManagementObjectSearcher collection to view the
       ManagementObject for each WMI object that is returned by the query.

Example
The following C# code example queries for the single SMS_Client object that is on a
Configuration Manager client.

For information about calling the sample code, see How to Call a WMI Class Method by
Using System.Management.

  c#

  public void QueryObjects(ManagementScope scope)
  {
      try
      {
          ManagementObjectSearcher s = new ManagementObjectSearcher
              ((scope), new WqlObjectQuery("SELECT * FROM sms_client"));

            foreach (ManagementObject o in s.Get())
            {
                // There is only one instance of SMS_Client, so this should

<!-- p.643 -->

  enumerate only once.
              Console.WriteLine("Client version: " +
  o["ClientVersion"].ToString());
          }
      }
      catch (System.Management.ManagementException e)
      {
          Console.WriteLine("Failed to make query: ", e.Message);
          throw;
      }
  }

This example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter   Type              Description

 scope       ManagementScope   Represents a scope (namespace) for management operations.

Compiling the Code

Namespaces
System.

System.Management.

Assembly
System.Management.

Robust Programming
The exception that can be raised is System.Management.ManagementException.

See Also
About Configuration Manager WMI Programming
How to Call a WMI Class Method by Using System.Management
How to Connect to the Configuration Manager Client WMI Namespace by Using
System.Management

<!-- p.644 -->

How to Perform an Asynchronous Query by Using System.Management
How to Read a WMI Object Using System.Management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.645 -->

How to Perform an Asynchronous Query
by Using System.Management
Article • 10/10/2022

To perform an asynchronous query on a Configuration Manager client Windows
Instrumentation (WMI) namespace, create a ManagementObjectSearcher object that
specifies a WQL query. You then create a ManagementOperationObserver that specifies an
event handler for each query result and also for the end of the query.

The asynchronous query is run when the ManagementObjectSearcher object Get method
is called with the ManagementOperationObserver object.

To perform an asynchronous query
   1. Set up a connection to the Configuration Manager client WMI namespace. For
       more information, see How to Connect to the Configuration Manager Client WMI
       Namespace by Using System.Management.

   2. Create a ManagementObjectSearcher object.

   3. Create a ManagementOperationObserver object.

   4. Add an ObjectReadyEventHandler method the ManagementOperationObserver object.

   5. Add a CompletedEventHandler method to the ManagementOperationObserver .

   6. Call the ManagementObjectSearcher object Get method and supply the
       ManagmentOperationObserver object as a parameter.

   7. Ensure your application still runs while the query is run.

Example
The following C# code example asynchronously queries for components that are
installed on a client.

For information about calling the sample code, see How to Call a WMI Class Method by
Using System.Management.

  c#

<!-- p.646 -->

public void EnumerateInstancesAsync(ManagementScope scope)
{
    try
    {
        // Instantiate an object searcher with the query.
        ManagementObjectSearcher searcher =
            new ManagementObjectSearcher(scope, new
            SelectQuery("CCM_InstalledComponent"));

       // Create a results watcher object
       // and handler for results and completion.
       ManagementOperationObserver results = new
           ManagementOperationObserver();

       // Attach handler to events for results and completion.
       results.ObjectReady += new
           ObjectReadyEventHandler(this.NewObject);
       results.Completed += new
           CompletedEventHandler(this.Done);

       Console.WriteLine("Installed Components");
       Console.WriteLine("--------------------");
       Console.WriteLine();

       // Call the asynchronous overload of Get()
       // to start the enumeration.
       searcher.Get(results);

       // Do something else while results
       // arrive asynchronously.
       while (!this.Completed)
       {
           System.Threading.Thread.Sleep(1000);
       }

       this.Reset();
    }
    catch (ManagementException e)
    {
        Console.WriteLine("Failed to run query: " + e.Message);
        throw;
    }

}

private bool isCompleted = false;

private void NewObject(object sender,
    ObjectReadyEventArgs obj)
{
    try
    {
        Console.WriteLine("Name: {0}, Version = {1}",

<!-- p.647 -->

                obj.NewObject["DisplayName"],
                obj.NewObject["Version"]);
         }
         catch (ManagementException e)
         {
             Console.WriteLine("Error: " + e.Message);
         }

  }

  private bool Completed
  {
      get
      {
          return isCompleted;
      }
  }

  private void Reset()
  {
      isCompleted = false;
  }

  private void Done(object sender,
           CompletedEventArgs obj)
  {
      isCompleted = true;
  }

This example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter      Type              Description

 Scope          ManagementScope   A valid ManagementScope . The path should be root\ccm.

Compiling the Code

Namespaces
System.

System.Management.

Assembly

<!-- p.648 -->

System.Management.

Robust Programming
The exception that can be raised is System.Management.ManagementException.

See Also
About Configuration Manager WMI Programming
How to Call a WMI Class Method by Using System.Management
How to Connect to the Configuration Manager Client WMI Namespace by Using
System.Management
How to Perform a Synchronous Query by Using System.Management
How to Read a WMI Object Using System.Management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.649 -->

How to Call a WMI Class Method by
Using System.Management
Article • 10/10/2022

To call a client Windows Management Instrumentation (WMI) class method, in
Configuration Manager, you call the InvokeMethod of the WMI class's ManagementClass .

To call a WMI class method
   1. Set up a connection to the Configuration Manager client WMI namespace. For
       more information, see How to Connect to the Configuration Manager Client WMI
       Namespace by Using System.Management.

   2. Create a ManagementClass by using the ManagementScope path you obtain in step
       one, and also the name of the class you want to call a method on.

   3. Create a ManagementBaseObject and specify any in parameters for the method.

   4. Call the method by using the ManagementClass object InvokeMethod method.

   5. Using the returned ManagementBaseObject , view the returned parameters.

Example
The following C# code example calls the ISmsClient::GetAssignedSite method to get
the current assigned site for the client. It then sets the assigned site back to the same
value using the ISmsClient::SetAssignedSite method.

For information about calling the sample code, see How to Call a WMI Class Method by
Using System.Management.

  c#

  public void CallMethod(ManagementScope scope)
  {
      try// Get the client's SMS_Client class.
      {
          ManagementClass cls = new ManagementClass(scope.Path.Path,
  "sms_client", null);

            // Get current site code.
            ManagementBaseObject outSiteParams =

<!-- p.650 -->

  cls.InvokeMethod("GetAssignedSite", null, null);

             // Display current site code.
             Console.WriteLine(outSiteParams["sSiteCode"].ToString());

          // Set up current site code as input parameter for SetAssignedSite.
          ManagementBaseObject inParams =
  cls.GetMethodParameters("SetAssignedSite");
          inParams["sSiteCode"] = outSiteParams["sSiteCode"].ToString();

          // Assign the Site code.
          ManagementBaseObject outMPParams =
  cls.InvokeMethod("SetAssignedSite", inParams, null);
      }
      catch (ManagementException e)
      {
          throw new Exception("Failed to execute method", e);
      }
  }

This example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter    Type               Description

 scope        -                  A valid connection to the client WMI provider. The path is
               ManagementScope   root\ccm.

Compiling the Code

Namespaces
System

System.Management

Assembly
System.Management

Robust Programming
The exception that can be raised is System.Management.ManagementException.

<!-- p.651 -->

See Also
About Configuration Manager WMI Programming
How to Call a WMI Class Method by Using System.Management
How to Connect to the Configuration Manager Client WMI Namespace by Using
System.Management
How to Perform an Asynchronous Query by Using System.Management
How to Perform a Synchronous Query by Using System.Management
How to Read a WMI Object by Using System.Management

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.652 -->

Client Resource Conditions
Article • 10/10/2022

In Configuration Manager SP1, the Configuration Manager client has added the ability
to be aware of system resources state and act accordingly. The resources being
monitored are power, network, and user idleness. This addition makes the Configuration
Manager client a better citizen in terms of optimizing power utilization and not
disturbing the end user experience as much as possible.

LaunchConditions
A new property called LaunchConditions has been added to the
CCM_Scheduler_ScheduledMessage class. The property can be a combination of the below

values.

                                                                                      ﾉ   Expand table

 Value     Meaning                         Comment

 0         No resource conditions.         This is the same behavior as versions of Configuration
                                           Manager prior to SP1.

 1         Fire only when the battery is   Definition of critical/low/high battery state is defined in
           at low or above state.          the Windows SYSTEM_POWER_STATUS structure.

 2         Fire only when the battery is   Definition of critical/low/high battery state is defined in
           at high or changing state.      the Windows SYSTEM_POWER_STATUS structure.

 4         Fire only when the computer     Definition of critical/low/high battery state is defined in
           is charging.                    the Windows SYSTEM_POWER_STATUS structure.

 8         Fire only when the user is      This check is only performed on desktop systems.
           idle.

 16        Fire only when the network
           is connected.

     ７ Note

     By default, the value of LaunchConditions is 1, meaning no scheduled tasks will be
     fired when the battery is at critical state.

<!-- p.653 -->

  Another new property called DeadlineMinutes was added to
   CCM_Scheduler_ScheduledMessage SP1. The default value of DeadlineMinutes is 4320

  (3 days). After the DeadlineMinutes timeout, unless the computer is at critical power
  state, the pending schedules will be fired.

The site control file allows programmatic access to feature specific value
monitoring/changes. The specific site control file items and default values are listed
below.

                                                                                 ﾉ   Expand table

 Site Control File Item                 Default Value

 Hardware Inventory Launch              10 = fire only when battery is high+ and user is idle.
 Conditions

 App Scan And Enforce Launch            10 = fire only when battery is high+ and user is idle.
 Conditions

 Scan And Evaluation Launch             26 = fire only when battery is high+ and user is idle and
 Conditions                             network is connected.

 DCM CI Assignment Evaluation           10 = fire only when battery is high+ and user is idle.
 Launch Conditions

 Software Inventory Launch Conditions   10 = fire only when battery is high+ and user is idle.

See Also
CCM_Scheduler_ScheduledMessage Client WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.654 -->

How to apply custom client settings
Article • 10/10/2022

In Configuration Manager, you apply custom client settings by creating an instance of a
Client Configuration class, and then deploying the custom client settings by creating an
instance of the SMS_ClientSettingsAssignment class and associating the instance of the
Client Configuration class and a target collection.

To apply custom client settings
   1. Set up a connection to the SMS Provider.

   2. Create an instance of a Client Configuration class (such as SMS_StateSystemConfig
       used below).

   3. Populate specific custom client agent settings.

   4. Create an instance of the SMS_ClientSettingsAssignment class.

   5. Populate the client settings assignment values. ClientSettingsID to identify the
       custom client settings instance and CollectionID to identify the target collection
       for the deployment of the custom client settings.

Example
The following example applies custom client settings by creating an instance of a Client
Configuration class, and then deploying the custom client settings by creating an
instance of the SMS_ClientSettingsAssignment class and associating the instance of the
Client Configuration class and a target collection.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  c#

  public void ApplyCustomClientSettings(WqlConnectionManager connection,string
  targetCollectionID){
      try
      {
          // Create a new instance of specific client agent settings (in this
  case State Messaging)
          IResultObject newCustomClientAgentSettings =

<!-- p.655 -->

connection.CreateEmbeddedObjectInstance("SMS_StateSystemConfig");

         // Populate specific custom client agent settings
         newCustomClientAgentSettings["BulkSendInterval"].IntegerValue = 120;
         newCustomClientAgentSettings["BulkSendIntervalHigh"].IntegerValue =
5;
         newCustomClientAgentSettings["BulkSendIntervalLow"].IntegerValue =
30;

        // Create a new array list to hold the custom client agent settings
object(s)
        List<IResultObject> tempAgentConfigurationsArray = new
List<IResultObject>();

        // Add the custom client agent settings embedded object to the local
array list
        tempAgentConfigurationsArray.Add(newCustomClientAgentSettings);

        // Create a new instance of SMS_ClientSettings
        IResultObject newClientSettings =
connection.CreateInstance("SMS_ClientSettings");

        // Populate the client agent settings
        newClientSettings["Name"].StringValue = "Custom State Messaging
Configuration";

        // Add the array of custom client agent settinsg object(s) to the
AgentConfigurations property
        newClientSettings.SetArrayItems("AgentConfigurations",
tempAgentConfigurationsArray);

         // Save and retrieve the new instance of SMS_ClientSettings
         newClientSettings.Put();
         newClientSettings.Get();

         // Get the SettingsID value of the new SMS_ClientSettings instance
         Int32 SettingsID = newClientSettings["SettingsID"].IntegerValue;

        // Create a new instance of SMS_ClientSettingsAssignment
        IResultObject newClientSettingsAssignment =
connection.CreateInstance("SMS_ClientSettingsAssignment");

        // Populate the client settings assignment values
        // ClientSettingsID to identify the custom client settings
        // CollectionID to identify the target collection for the custom
client settings
        newClientSettingsAssignment["ClientSettingsID"].IntegerValue =
SettingsID;
        newClientSettingsAssignment["CollectionID"].StringValue =
targetCollectionID;

         // Save the new instance of the client settings assignment.
         newClientSettingsAssignment.Put();
      }
      catch (SmsException ex)

<!-- p.656 -->

      {
              Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
      }
  }

The example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter            Type                      Description

 connection           - Managed:                A valid connection to the SMS Provider.
                       WqlConnectionManager

 targetCollectionID   - Managed: String         The target collection for the custom client
                                                settings deployment.

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

<!-- p.657 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager SDK
SMS_ClientSettingsAssignment Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.658 -->

How to Create a Dynamic Collection
Article • 10/10/2022

In Configuration Manager, your application uses the SMS_Collection Server WMI Class
to define the attributes of a collection, such as the membership rules and the refresh
schedule. The MemberClassName property contains the system-generated class name that
contains the members of the collection.

Members of a collection are specified by using direct rules, query rules, or both. Direct
rules define an explicit resource, whereas query rules define a dynamic collection that is
regularly evaluated based on the current state of the site.

  ７ Note

  When creating a direct membership rule, remember that the rule must always have
  the same name as the computer that the rule specifies.

Your application uses the SMS_CollectionRuleQuery Server WMI Class class to define
query rules. The query must be valid and can specify the collection to contain resources
such as "All users in the corporate domain." The application can then use the query to
ensure that a program is targeted for software distribution to all computers that meet
the criteria. As the site changes and the collection is re-evaluated, members of the
collection are automatically added and deleted.

  ７ Note

  When running a query against a dynamic collection, ensure that the SMS Provider
  is loaded or that another method or query has already run.

Collections are closely tied to packages, programs and advertisements. For more
information, see Software Distribution Overview.

These examples require the following values:

      A Windows Management Instrumentation (WMI) connection object.

      A new dynamic collection name.

      A new dynamic collection comment.

      The 'owned by this site' flag.

<!-- p.659 -->

     A query (string).

     A static rule name.

     A collection identifier to limit the scope of membership.

  ７ Note

  If the All Systems (SMS00001) collection has been removed from the site server, the
  VBScript example does not work.

Example of the subroutine call in Visual Basic:

  Call CreateDynamicCollection(swbemconnection, "New Dynamic Collection Name",
  "New dynamic collection comment.", true, "SELECT * from SMS_R_System", "New
  Rule Name", "SMS00001")

Example of the method call in C#:

  CreateDynamicCollection(WMIConnection, "New Dynamic Collection Name", "New
  dynamic collection comment.", true, "SELECT * from SMS_R_System", "New Rule
  Name", "SMS00001")

To create a dynamic collection
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
     fundamentals.

   2. Create the new collection object by using the SMS_Collection Server WMI Class
     class.

   3. Create the rule by using the SMS_CollectionRuleQuery Server WMI Class class.

   4. Add the rule to the collection.

   5. Refresh the collection.

Example

<!-- p.660 -->

The following example method creates a dynamic collection by using the
SMS_Collection Server WMI Class and the SMS_CollectionRuleQuery Server WMI Class
classes and class properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  ' Setup a connection to the local provider.
  Set swbemLocator = CreateObject("WbemScripting.SWbemLocator")
  Set swbemconnection= swbemLocator.ConnectServer(".", "root\sms")
  Set providerLoc = swbemconnection.InstancesOf("SMS_ProviderLocation")

  For Each Location In providerLoc
       If location.ProviderForLocalSite = True Then
           Set swbemconnection = swbemLocator.ConnectServer(Location.Machine,
  "root\sms\site_" + Location.SiteCode)
           Exit For
       End If
  Next

  Call CreateDynamicCollection(swbemconnection, "New Dynamic Collection Name",
  "New dynamic collection comment.", true, "SELECT * from SMS_R_System", "New
  Rule Name", "SMS00001")

  Sub CreateDynamicCollection(connection, newCollectionName,
  newCollectionComment, ownedByThisSite, queryForRule, ruleName,
  limitToCollectionID)

        ' Create the collection.
        Set newCollection = connection.Get("SMS_Collection").SpawnInstance_
        newCollection.Name = newCollectionName
        newCollection.Comment = newCollectionComment
        newCollection.OwnedByThisSite = ownedByThisSite
        newCollection.LimitToCollectionID = limitToCollectionID

        ' Save the new collection and save the collection path for later.
        Set collectionPath = newCollection.Put_

        ' Create a new collection rule object for validation.
        Set queryRule = connection.Get("SMS_CollectionRuleQuery")

        ' Validate the query (good practice before adding it to the collection).
        validQuery = queryRule.ValidateQuery(queryForRule)

        ' Continue with processing, if the query is valid.
        If validQuery Then

            ' Create the query rule.
            Set newQueryRule = QueryRule.SpawnInstance_
            newQueryRule.QueryExpression = queryForRule

<!-- p.661 -->

            newQueryRule.RuleName = ruleName

            ' Add the new query rule to a variable.
            Set newCollectionRule = newQueryRule

            ' Get the collection.
            Set newCollection = connection.Get(collectionPath.RelPath)

            ' Add the rules to the collection.
            newCollection.AddMembershipRule newCollectionRule

            ' Call RequestRefresh to initiate the collection evaluator.
            newCollection.RequestRefresh False

       End If

  End Sub

  c#

  public void CreateDynamicCollection(WqlConnectionManager connection, string
  newCollectionName, string newCollectionComment, bool ownedByThisSite, string
  query, string ruleName, string LimitToCollectionID){      try    {         //
  Create new SMS_Collection object.         IResultObject newCollection =
  connection.CreateInstance("SMS_Collection");         // Populate the new
  collection object properties.         newCollection["Name"].StringValue =
  newCollectionName;        newCollection["Comment"].StringValue =
  newCollectionComment;         newCollection["OwnedByThisSite"].BooleanValue =
  ownedByThisSite;        newCollection["LimitToCollectionID"].StringValue =
  LimitToCollectionID;        // Save the new collection object and
  properties.        // In this case, it seems necessary to 'get' the object
  again to access the properties.         newCollection.Put();
  newCollection.Get();        // Validate the query.          Dictionary<string,
  object> validateQueryParameters = new Dictionary<string, object>();
  validateQueryParameters.Add("WQLQuery", query);          IResultObject result
  = connection.ExecuteMethod("SMS_CollectionRuleQuery", "ValidateQuery",
  validateQueryParameters);         // Create query rule.         IResultObject
  newQueryRule = connection.CreateInstance("SMS_CollectionRuleQuery");
  newQueryRule["QueryExpression"].StringValue = query;
  newQueryRule["RuleName"].StringValue = ruleName;          // Add the rule.
  Although not used in this sample, QueryID contains the query identifier.
  Dictionary<string, object> addMembershipRuleParameters = new
  Dictionary<string, object>();
  addMembershipRuleParameters.Add("collectionRule", newQueryRule);
  IResultObject queryID = newCollection.ExecuteMethod("AddMembershipRule",
  addMembershipRuleParameters);         // Start collection evaluator.
  newCollection.ExecuteMethod("RequestRefresh", null);
  Console.WriteLine("Created collection: " + newCollectionName);      }    catch
  (SmsException ex)     {        Console.WriteLine("Failed to create
  collection. Error: " + ex.Message);         throw;    }}

The example method has the following parameters:

<!-- p.662 -->

                                                                             ﾉ   Expand table

 Parameter              Type                   Description

 connection             - Managed:             A valid connection to the SMS Provider.
                        WqlConnectionManager
                        - VBScript:
                        SWbemServices

 newCollectionName      - Managed: String      The unique name that represents the
                        - VBScript: String     collection in the Configuration Manager
                                               console.

 newCollectionComment   - Managed: String      General comment or note that documents
                        - VBScript: String     the collection.

 ownedByThisSite        - Managed: Boolean     true if the collection originated at the local
                        - VBScript: Boolean    Configuration Manager site.

 query                  - Managed: String      WQL SELECT statement having results that
                        - VBScript: String     are used to populate the collection. The
                                               statement must specify a resource class
                                               name.

 ruleName               - Managed: String      Descriptive name that identifies the rule.
                        - VBScript: String

 limitToCollectionID    - Managed: String      Collection identifier to limit the scope of
                        - VBScript: String     membership.

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly

<!-- p.663 -->

adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
SMS_Collection Server WMI Class
SMS_CollectionRuleQuery Server WMI Class
Software distribution overview About deployments Objects overview How to Connect to
an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.664 -->

How to Create a Static Collection
Article • 10/10/2022

In Configuration Manager, your application uses SMS_Collection Server WMI Class to
define the attributes of a collection, such as the membership rules and the refresh
schedule. The MemberClassName property contains the system-generated class name that
contains the members of the collection.

Members of a collection are specified by using direct rules, query rules, or both. Direct
rules define an explicit resource, and query rules define a dynamic collection that is
regularly evaluated based on the current state of the site.

  ７ Note

  When creating a direct membership rule, remember that the rule must always have
  the same name as the computer that the rule specifies.

Your application uses the SMS_CollectionRuleDirect Server WMI Class class to define
direct rules. This approach is used for resources that are static in nature. For example, if
you have a limited number of licenses for a particular software application, the
application should use direct rules to advertise to specific computers or users.

Collections are closely tied to packages, programs and advertisements. For more
information, see Software Distribution Overview.

The following examples require the following values:

      A Windows Management Instrumentation (WMI) connection object.

      A new static collection name.

      A new static collection comment.

      The 'owned by this site' flag.

      A resource class name.

      A resource ID.

      A collection identifier to limit the scope of membership.

  ７ Note

<!-- p.665 -->

  If the All Systems (SMS00001) collection has been removed from the site server, the
  VBScript example will not work.

Example of the subroutine call in Visual Basic:

  Call CreateStaticCollection(swbemconnection, "New Static Collection Name",
  "New static collection comment.", true, "SMS_R_System", 2, "SMS00001")

Example of the method call in C#:

  CreateStaticCollection (WMIConnection, "New Static Collection Name", "New
  static collection comment.", true, "SMS_R_System", 2, "SMS00001")

To create a static collection
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Create the new collection object by using the SMS_Collection Server WMI Class
        class.

   3. Create the direct rule by using the SMS_CollectionRuleDirect Server WMI Class
        class.

   4. Add the rule to the collection.

   5. Refresh the collection.

Example
The following example method creates a collection.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  ' Set up a connection to the local provider.
  Set swbemLocator = CreateObject("WbemScripting.SWbemLocator")

<!-- p.666 -->

Set swbemconnection= swbemLocator.ConnectServer(".", "root\sms")
Set providerLoc = swbemconnection.InstancesOf("SMS_ProviderLocation")

For Each Location In providerLoc
     If location.ProviderForLocalSite = True Then
         Set swbemconnection = swbemLocator.ConnectServer(Location.Machine,
"root\sms\site_" + Location.SiteCode)
         Exit For
     End If
Next

Call CreateStaticCollection(swbemconnection, "New Static Collection Name",
"New static collection comment.", true, "SMS_R_System", 2, "SMS00001")

Sub CreateStaticCollection(connection, newCollectionName,
newCollectionComment, ownedByThisSite, resourceClassName, resourceID,
limitToCollectionID)

     ' Create the collection.
     Set newCollection = connection.Get("SMS_Collection").SpawnInstance_
     newCollection.Comment = newCollectionComment
     newCollection.Name = newCollectionName
     newCollection.OwnedByThisSite = ownedByThisSite
     newCollection.LimitToCollectionID = limitToCollectionID

     ' Save the new collection and save the collection path for later.
     Set collectionPath = newCollection.Put_

    ' Create the direct rule.
    Set newDirectRule =
connection.Get("SMS_CollectionRuleDirect").SpawnInstance_
    newDirectRule.ResourceClassName = resourceClassName
    newDirectRule.ResourceID = resourceID

     ' Add the new query rule to a variable.
     Set newCollectionRule = newDirectRule

     ' Get the collection.
     Set newCollection = connection.Get(collectionPath.RelPath)

     ' Add the rules to the collection.
     newCollection.AddMembershipRule newCollectionRule

     ' Call RequestRefresh to initiate the collection evaluator.
     newCollection.RequestRefresh False

End Sub

c#

public void CreateStaticCollection(WqlConnectionManager connection, string
newCollectionName, string newCollectionComment, bool ownedByThisSite, string
resourceClassName, int resourceID, string limitToCollectionID)

<!-- p.667 -->

{
    try
    {
        // Create a new SMS_Collection object.
        IResultObject newCollection =
connection.CreateInstance("SMS_Collection");

        // Populate new collection properties.
        newCollection["Name"].StringValue = newCollectionName;
        newCollection["Comment"].StringValue = newCollectionComment;
        newCollection["OwnedByThisSite"].BooleanValue = ownedByThisSite;
        newCollection["LimitToCollectionID"].StringValue =
limitToCollectionID;

        // Save the new collection object and properties.
        // In this case, it seems necessary to 'get' the object again to
access the properties.
        newCollection.Put();
        newCollection.Get();

        // Create a new static rule object.
        IResultObject newStaticRule =
connection.CreateInstance("SMS_CollectionRuleDirect");
        newStaticRule["ResourceClassName"].StringValue = resourceClassName;
        newStaticRule["ResourceID"].IntegerValue = resourceID;

        // Add the rule. Although not used in this sample, staticID contains
the query identifier.
        Dictionary<string, object> addMembershipRuleParameters = new
Dictionary<string, object>();
        addMembershipRuleParameters.Add("collectionRule", newStaticRule);
        IResultObject staticID =
newCollection.ExecuteMethod("AddMembershipRule",
addMembershipRuleParameters);

        // Start collection evaluator.
        Dictionary<string, object> requestRefreshParameters = new
Dictionary<string, object>();
        requestRefreshParameters.Add("IncludeSubCollections", false);
        newCollection.ExecuteMethod("RequestRefresh",
requestRefreshParameters);

          // Output message.
          Console.WriteLine("Created collection" + newCollectionName);
    }

    catch (SmsException ex)
    {
        Console.WriteLine("Failed to create collection. Error: " +
ex.Message);
        throw;
    }
}

<!-- p.668 -->

The example method has the following parameters:

                                                                                ﾉ   Expand table

 Parameter              Type                        Description

 connection             - Managed:                  A valid connection to the SMS Provider.
                        WqlConnectionManager
                        - VBScript: SWbemServices

 newCollectionName      - Managed: String           The unique name that represents the
                        - VBScript: String          collection in the Configuration Manager
                                                    console.

 newCollectionComment   - Managed: String           General comment or note that documents
                        - VBScript: String          the collection.

 ownedByThisSite        - Managed: Boolean          true if the collection originated at the local
                        - VBScript: Boolean         Configuration Manager site.

 resourceClassName      - Managed: String           The resource name of the static rule object.
                        - VBScript: String

 resourceID             - Managed: Integer          The resource ID.
                        - VBScript: Integer

 limitToCollectionID    - Managed: String           Collection identifier to limit the scope of
                        - VBScript: String          membership.

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly

<!-- p.669 -->

adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
SMS_Collection Server WMI Class
SMS_CollectionRuleDirect Server WMI Class
Software distribution overview About deployments Objects overview How to Connect to
an SMS Provider in Configuration Manager by Using Managed Code
How to Connect to an SMS Provider in Configuration Manager by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.670 -->

How to Enumerate the Members of a
Collection
Article • 10/10/2022

In Configuration Manager, the preferred method to enumerate through a collection is to
use SMS_FullCollectionMembership Server WMI Class .

Query 1: SMS_FullCollectionMembership: This example shows how to enumerate the
members of the All Systems (SMS00001) collection by using the
SMS_FullCollectionMembership Server WMI Class .

Query 2: SMS_CollectionMember_a: This example shows a slower alternative, by using
the SMS_CollectionMember_a Server WMI Class class.

Query 3: SMS_Collection: This example shows a further alternative, which is to query the
members by using the actual collection class name that is specified in the
MemberClassName property of SMS_Collection Server WMI Class. Querying the actual

class offers performance advantages and lets you create more complex queries, such as
JOINs. The example is equivalent to the earlier queries.

  ７ Note

  When the SMS Provider first initializes, it registers and dynamically loads the SMS
  collection class into memory. If a WQL query is made against the collection class
  before it is loaded, an empty query result set will be returned.

Collections are closely tied to packages, programs and advertisements. For more
information, see Software Distribution Overview.

These examples require the following values:

      A Windows Management Instrumentation (WMI) connection object.

      Example of the subroutine call in Visual Basic:

  Call EnumerateCollectionMembers(swbemServices)

Example of the method call in C#:

<!-- p.671 -->

  EnumerateCollectionMembers(WMIConnection)

To enumerate the members of a collection
   1. Set up a connection to the SMS Provider.

   2. Define a query to select the resources for the collection.

   3. Execute the query and enumerate the results.

Example
The following example method enumerates the members of a collection.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnumerateCollectionMembers(connection)
      Const wbemFlagReturnImmediately = 16    Const wbemFlagForwardOnly = 32
      ' Set required variables.
      ' Note: Values must be manually added to the queries below.
      Dim Query1    Dim Query2    Dim Query3    Dim ListOfResources1    Dim
  ListOfResources2    Dim ListOfResources3    Dim Resource1    Dim Resource2
  Dim Resource3
      ' The following example shows how to enumerate the members of the All
  Systems (SMS00001) collection.
      Query1 = "SELECT ResourceID FROM SMS_FullCollectionMembership WHERE
  CollectionID = 'SMS00001'"

      ' Run query.
      Set ListOfResources1 = connection.ExecQuery(Query1, ,
  wbemFlagForwardOnly Or wbemFlagReturnImmediately)

        ' The query returns a collection that needs to be enumerated.
        Wscript.Echo " "
        Wscript.Echo "Query: " & Query1
        For Each Resource1 In ListOfResources1
            Wscript.Echo Resource1.ResourceID
        Next

      ' A slower alternative is to use the SMS_CollectionMember_a association
  class.
      Query2 = "SELECT ResourceID FROM SMS_CollectionMember_a WHERE
  CollectionID = 'SMS00001'"

<!-- p.672 -->

    ' Run query.
    Set ListOfResources2 = connection.ExecQuery(Query2, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

     ' The query returns a collection that needs to be enumerated.
     Wscript.Echo " "
     Wscript.Echo "Query: " & Query2
     For Each Resource2 In ListOfResources2
         Wscript.Echo Resource2.ResourceID
     Next

    ' A further alternative is to query the members by using the actual
collection class name specified in the MemberClassName property of
SMS_Collection.
    Query3 = "SELECT ResourceID FROM SMS_CM_Res_Coll_SMS00001"

    ' Run query.
    Set ListOfResources3 = connection.ExecQuery(Query3, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

     ' The query returns a collection that needs to be enumerated.
     Wscript.Echo " "
     Wscript.Echo "Query: " & Query3
     For Each Resource3 In ListOfResources3
         Wscript.Echo Resource3.ResourceID
     Next

End Sub

c#

public void EnumerateCollectionMembers(WqlConnectionManager connection)
{
    // Set required variables.
    // Note: Values must be manually added to the queries below.

     try
     {
        // The following example shows how to enumerate the members of the
All Systems (SMS00001) collection.
        string Query1 = "SELECT ResourceID FROM SMS_FullCollectionMembership
WHERE CollectionID = 'SMS00001'";

        // Run query.
        IResultObject ListOfResources1 =
connection.QueryProcessor.ExecuteQuery(Query1);

           // The query returns a collection that needs to be enumerated.
           Console.WriteLine(" ");
           Console.WriteLine("Query: " + Query1);
           foreach (IResultObject Resource1 in ListOfResources1)
           {
               Console.WriteLine(Resource1["ResourceID"].IntegerValue);

<!-- p.673 -->

              }

          // A slower alternative is to use the SMS_CollectionMember_a
  association class.
          string Query2 = "SELECT ResourceID FROM SMS_CollectionMember_a WHERE
  CollectionID = 'SMS00001'";

          // Run query.
          IResultObject ListOfResources2 =
  connection.QueryProcessor.ExecuteQuery(Query2);

              // The query returns a collection that needs to be enumerated.
              Console.WriteLine(" ");
              Console.WriteLine("Query: " + Query2);
              foreach (IResultObject Resource2 in ListOfResources2)
              {
                  Console.WriteLine(Resource2["ResourceID"].IntegerValue);
              }

          // A further alternative is to query the members by using the actual
  collection class name specified in the MemberClassName property of
  SMS_Collection.
          string Query3 = "SELECT ResourceID FROM SMS_CM_Res_Coll_SMS00001";

          // Run query.
          IResultObject ListOfResources3 =
  connection.QueryProcessor.ExecuteQuery(Query3);

              // The query returns a collection that needs to be enumerated.
              Console.WriteLine(" ");
              Console.WriteLine("Query: " + Query3);
              foreach (IResultObject Resource3 in ListOfResources3)
              {
                  Console.WriteLine(Resource3["ResourceID"].IntegerValue);
              }
      }

      catch (SmsException eX)
      {
          Console.WriteLine("Failed to run queries. Error: " + eX.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter        Type                              Description

 connection       - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
                  - VBScript: SWbemServices

<!-- p.674 -->

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
SMS_CollectionMember_a Server WMI Class
SMS_Collection Server WMI Class
Software distribution overview About deployments

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.675 -->

How to Modify a Collection
Article • 10/10/2022

To Modify a Collection
   1. Set up a connection to the SMS Provider.

   2. Get the specific collection instance by using the collection ID provided.

   3. Display the current property values (name and comment properties used as
        examples).

   4. Modify the example property values using the name and comment values passed in.

Example
The following example method shows how to modify collection properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub RenameCollection(connection, collectionID, name, comment)    Dim
  collection    Set collection =
  connection.Get("SMS_Collection.CollectionID='" & collectionID & "'")
  WScript.Echo "-- Collection " & collectionID & " --"    WScript.Echo "Name
  before: " & collection.Name    WScript.Echo "Comment before: " &
  collection.Comment    collection.Name = name    collection.Comment = comment
  collection.Put_    WScript.Echo ""    WScript.Echo "Name after: " &
  collection.Name    WScript.Echo "Comment after: " & collection.CommentEnd
  Sub

  c#

  public void RenameCollection(WqlConnectionManager connection, string
  collectionID, string name, string comment){    IResultObject collection =
  connection.GetInstance(string.Format("SMS_Collection.CollectionID='{0}'",
  collectionID));    Console.WriteLine("-- Collection {0} --", collectionID);
  Console.WriteLine("Name before: {0}", collection["Name"].StringValue);
  Console.WriteLine("Comment before: {0}", collection["Comment"].StringValue);
  collection["Name"].StringValue = name;    collection["Comment"].StringValue
  = comment;    collection.Put();    collection.Get();    Console.WriteLine();
  Console.WriteLine("Name after: {0}", collection["Name"].StringValue);
  Console.WriteLine("Comment after: {0}", collection["Comment"].StringValue);}

<!-- p.676 -->

The example method has the following parameters:

                                                                            ﾉ    Expand table

 Parameter      Type                   Description

 connection     - Managed:             A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript:
                SWbemServices

 collectionID   - Managed: String      Unique auto-generated ID containing eight characters.
                - VBScript: String     For more information, see the CollectionID property of
                                       SMS_Collection Server WMI Class.

 name           - Managed: String      An example collection property. The property value is
                - VBScript: String     modified in the code snippet.

 comment        - Managed: String      An example collection property. The property value is
                - VBScript: String     modified in the code snippet.

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

<!-- p.677 -->

See Also
SMS_Collection Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.678 -->

How to Delete a Collection
Article • 10/10/2022

Your application can delete a collection in Configuration Manager by using the
SMS_Collection Server WMI Class and class properties.

  ） Important

        Care should be exercised when deleting any Configuration Manager object.

        We recommend that if you are deleting several collections, you do so one at a
        time, to allow database operations time to manage changes associated with
        the deletions.

Collections are closely tied to packages, programs, and advertisements. For more
information, see Software Distribution Overview.

These examples require the following values:

      A Windows Management Instrumentation (WMI) connection object.

      An existing collection ID.

      The following code is an example of the subroutine call in Visual Basic:

  Call DeleteCollection(swbemServices,"ABC00010")

The following code is an example of the method call in C#:

  DeleteCollection(WMIConnection,"ABC00010")

To delete a collection
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Get the specific collection instance by using the collection ID provided.

<!-- p.679 -->

   3. Delete the collection by using the delete method.

Example
The following example method deletes a collection.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  ' Setup a connection to the local provider.
  Set swbemLocator = CreateObject("WbemScripting.SWbemLocator")
  Set swbemServices= swbemLocator.ConnectServer(".", "root\sms")
  Set providerLoc = swbemServices.InstancesOf("SMS_ProviderLocation")

  For Each Location In providerLoc
       If location.ProviderForLocalSite = True Then
           Set swbemServices = swbemLocator.ConnectServer(Location.Machine,
  "root\sms\site_" + Location.SiteCode)
           Exit For
       End If
  Next

  Call DeleteCollection(swbemServices,"ABC00010")

  Sub DeleteCollection(connection, collectionIDToDelete)

      ' Get the specific collection instance to delete.
      Set collectionToDelete = connection.Get("SMS_Collection.CollectionID='"
  & collectionIDToDelete & "'")

        ' Delete the collection.
        collectionToDelete.Delete_

        ' Display change information.
        Wscript.Echo "Deleted collection: " & collectionIDToDelete

  End Sub

  c#

  public void DeleteCollection(WqlConnectionManager connection, string
  collectionIDToDelete)
  {
      // Note: On delete, the provider cleans up the SMS_CollectionSettings
  and SMS_CollectToSubCollect objects.

        try

<!-- p.680 -->

      {
          // Get the specific collection instance to delete.
          IResultObject collectionToDelete =
  connection.GetInstance(@"SMS_Collection.CollectionID='" +
  collectionIDToDelete + "'");

              // Delete the collection.
              collectionToDelete.Delete();

              // Output the ID of the deleted collection.
              Console.WriteLine("Deleted collection: " + collectionIDToDelete);
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to delete collection. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter              Type                   Description

 connection             - Managed:             A valid connection to the SMS Provider.
                        WqlConnectionManager
                        - VBScript:
                        SWbemServices

 collectionIDToDelete   - Managed: String      Unique auto-generated ID containing eight
                        - VBScript: String     characters. For more information, see the
                                               CollectionID property of SMS_Collection
                                               Server WMI Class.

Compiling the Code
The C# example requires:

Namespaces
System

System.Collections.Generic
