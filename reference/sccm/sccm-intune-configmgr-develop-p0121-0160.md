---
title: "Configuration Manager SDK documentation — pages 121-160"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0121-0160
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0121-0160
family: sccm
documentKind: "doc"
abstract: "Feedback Was this page helpful?  Yes  No Provide product feedback How to Delete a Configuration Manager Object by Using WMI Article • 10/10/2022 To delete a Configuration Manager object, in Configuration Manager, call the SWbemObject object Delete_ method. To delete a Configur"
---

# Configuration Manager SDK documentation — pages 121-160

<!-- p.121 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.122 -->

How to Delete a Configuration Manager
Object by Using WMI
Article • 10/10/2022

To delete a Configuration Manager object, in Configuration Manager, call the
SWbemObject object Delete_ method.

To delete a Configuration Manager object
   1. Set up a connection to the SMS Provider. For more information, see How to
        Connect to an SMS Provider in Configuration Manager by Using WMI.

   2. Using the SWbemServices object you obtain from step one, call the Get method
        and specify the class and key information for the object you want to delete. Get
        returns a SWbemObject that represents the object.

   3. Using the SWbemObject , call Delete to delete the object.

Example
The following VBScript code example deletes the package (SMS_Package) identified by
its package identifier packageID .

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DeletePackage (connection, packageID)

         On Error Resume Next
         Dim package

         Set package = connection.Get("SMS_Package.PackageID='" & packageID &
  "'")
         If Err.Number<>0 Then
             Wscript.Echo "Couldn't get package " + packageID
             Exit Sub
         End If

         package.Delete_

         WScript.Echo "Package deleted"

<!-- p.123 -->

       If Err.Number<>0 Then
           Wscript.Echo "Couldn't delete " + packageID
           Exit Sub
       End If

  End Sub

This example method has the following parameters:

                                                                                    ﾉ   Expand table

 Parameter    Type                 Description

 connection    SWbemServices       A valid connection to the SMS Provider.

 packageID     String              The package identifier. This is obtained from the SMS_Package class
                                   PackageID .

See Also
Windows Management Instrumentation
Objects overview How to Call a Configuration Manager Object Class Method by Using
WMI
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create a Configuration Manager Object by Using WMI
How to Modify a Configuration Manager Object by Using WMI
How to Perform an Asynchronous Configuration Manager Query by Using WMI
How to Perform a Synchronous Configuration Manager Query by Using WMI
How to Read a Configuration Manager Object by Using WMI
How to Read Lazy Properties by Using WMI

Feedback
Was this page helpful?      Yes        No

Provide product feedback

<!-- p.124 -->

How to Perform a Synchronous
Configuration Manager Query by Using
WMI
Article • 10/10/2022

In Configuration Manager, you perform a synchronous query for Configuration Manager
objects by calling the SWbemServices object ExecQuery method and passing a WQL
query.

A synchronous query is a query that maintains control over the process of your
application for the duration of the query. A synchronous query has the potential of
locking up your application for large queries or for queries over a network. Alternatively,
you can run an asynchronous query that returns control to the application while the
query is run. For more information, see How to Perform an Asynchronous Configuration
Manager Query by Using Managed Code

  ７ Note

  Lazy properties are not returned in synchronous queries. For more information, see
  How to Read Lazy Properties by Using WMI.

To perform a synchronous query
   1. Set up a connection to the SMS Provider. For more information, see How to
      Connect to an SMS Provider in Configuration Manager by Using WMI.

   2. Using the SWbemServices object that you obtain from step one, use the ExecQuery
      method to get a SWbemObjectSet collection containing the query results.

   3. Iterate through the SWbemObjectSet collection to access a SWbemObject for each
      object returned by the query.

Example
The following example performs a synchronous query of all packages in Configuration
Manager.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.125 -->

  vbs

  Sub QueryPackages(connection)

        On Error Resume next

        Dim packages
        Dim package

        ' Run the query.
        Set packages = _
            connection.ExecQuery("Select * From SMS_Package")

        If Err.Number<>0 Then
            Wscript.Echo "Couldn't get Packages"
            Wscript.Quit
        End If

        For Each package In packages
            WScript.Echo package.Name
        Next

        If packages.Count=0 Then
            Wscript.Echo "No packages found"
        End If

  End Sub

This example method has the following parameters:

                                                                         ﾉ     Expand table

 Parameter       Type                Description

 connection      SWbemServices       A valid connection to the SMS Provider.

See Also
Windows Management Instrumentation
Objects overview How to Call a Configuration Manager Object Class Method by Using
WMI
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create a Configuration Manager Object by Using WMI
How to Delete a Configuration Manager Object by Using WMI
How to Modify a Configuration Manager Object by Using WMI
How to Perform an Asynchronous Configuration Manager Query by Using WMI
How to Read a Configuration Manager Object by Using WMI

<!-- p.126 -->

How to Read Lazy Properties by Using WMI
Configuration Manager Extended WMI Query Language
Configuration Manager Result Sets
Configuration Manager Special Queries
About queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.127 -->

How to Perform an Asynchronous
Configuration Manager Query by Using
WMI
Article • 10/10/2022

In Configuration Manager, you perform a synchronous query for Configuration Manager
objects by calling the SWbemServices object ExecQueryAsync method and by
implementing a sink method to handle query results.

To handle each returned object, create an objWbemSink.OnObjectReady event
subroutine. To be notified when the query is completed, create a
objWbemSink.OnCompleted event subroutine.

  ７ Note

  Lazy properties are not returned in asynchronous queries. For more information,
  see How to Read Lazy Properties by Using WMI.

To perform an asynchronous query
   1. Set up a connection to the SMS Provider. For more information, see How to
        Connect to an SMS Provider in Configuration Manager by Using WMI.

   2. Create an OnObjectReady subroutine to handle objects by the query.

   3. Create an OnCompleted subroutine to handle query completion.

   4. Using the SWbemServices object you obtain from step one, use ExecQueryAsync
        object to query Configuration Manager objects asynchronously.

Example
The following VBScript code example asynchronously queries for all SMS_Collection
objects.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

<!-- p.128 -->

  Dim bdone
  Sub QueryCollection(connection)

      Dim sink
      bdone = False

      Set sink = WScript.CreateObject("wbemscripting.swbemsink","sink_")

      ' Query for all collections.
      connection.ExecQueryAsync sink, "select * from SMS_Collection"

      ' Wait until all instances are returned.
      While Not bdone
          wscript.sleep 1000
      Wend
   End Sub

  ' The sink subroutine to handle the OnObjectReady
  ' event. This is called as each object returns.
  Sub sink_OnObjectReady(collection, octx)
      WScript.Echo "CollectionID: " + collection.CollectionID
      WScript.Echo "Name: " + collection.Name
      Wscript.Echo
  End Sub

  ' The sink subroutine to handle the OnCompleted event.
  ' This is called when all the objects are returned.
  ' The oErr parameter obtains an SWbemLastError object,
  ' if available from the provider.
  Sub sink_OnCompleted(HResult, oErr, oCtx)
      WScript.Echo "All collections returned"
      bdone = true
  End Sub

This example method has the following parameters:

                                                                         ﾉ     Expand table

 Parameter      Type                 Description

 connection     SWbemServices        A valid connection to the SMS Provider.

See Also
Windows Management Instrumentation
Objects overview How to Call a Configuration Manager Object Class Method by Using
WMI
How to Connect to an SMS Provider in Configuration Manager by Using WMI

<!-- p.129 -->

How to Create a Configuration Manager Object by Using WMI
How to Delete a Configuration Manager Object by Using WMI
How to Modify a Configuration Manager Object by Using WMI
How to Perform a Synchronous Configuration Manager Query by Using WMI
How to Read a Configuration Manager Object by Using WMI
How to Read Lazy Properties by Using WMI
Configuration Manager Extended WMI Query Language
Configuration Manager Result Sets
Configuration Manager Special Queries
About queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.130 -->

How to Read Lazy Properties by Using
WMI
Article • 10/10/2022

To read a lazy property from a Configuration Manager object returned in a query, you
get the object instance, which in turn retrieves any lazy object properties from the SMS
Provider.

  ７ Note

  If you know the full path to the WMI object, a call to the SWbemServices class Get
  method will return the WMI object along with any lazy properties. For more
  information, see How to Read a Configuration Manager Object by Using WMI.

For more information about lazy properties, see Configuration Manager Lazy Properties.

To read lazy properties
   1. Set up a connection to the SMS Provider. For more information, see How to
        Connect to an SMS Provider in Configuration Manager by Using WMI.

   2. Using the SWbemServices object you obtain from step one, use the ExecQuery
        object to query Configuration Manager objects.

   3. Iterate through the query results.

   4. Using the SWbemServices object you obtain from step one, call Get to get the
        SWbemObject object for each queried object you want to get lazy properties from.

Example
The following VBScript code example queries for all SMS_Collection objects and then
displays rule names obtained from the CollectionRules lazy property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

<!-- p.131 -->

  Sub ReadLazyProperty(connection)

      Dim collection
      Dim collections
      Dim collectionLazy
      Dim i

      ' Get all collections.
      Set collections = _
          connection.ExecQuery("Select * From SMS_Collection")

      For Each collection in collections

              Wscript.Echo Collection.Name

          ' Get the collection object.
          Set collectionLazy = connection.Get("SMS_Collection.CollectionID='"
  + collection.CollectionID + "'")

          ' Display the rule names that are in the lazy property
  CollectionRules.
          If IsNull(collectionLazy.CollectionRules) Then
               Wscript.Echo "No rules"
          Else
               For i = 0 To UBound(collectionLazy.CollectionRules)
                   WScript.Echo "Rule " +
  collectionLazy.CollectionRules(i).RuleName
               Next
         End If
      Next

  End Sub

This example method has the following parameters:

                                                                           ﾉ      Expand table

 Parameter         Type                 Description

 connection        - SWbemServices      A valid connection to the SMS Provider.

Compiling the Code

See Also
Windows Management Instrumentation
Configuration Manager Lazy Properties

<!-- p.132 -->

Objects overview How to Call a Configuration Manager Object Class Method by Using
WMI
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create a Configuration Manager Object by Using WMI
How to Delete a Configuration Manager Object by Using WMI
How to Modify a Configuration Manager Object by Using WMI
How to Perform an Asynchronous Configuration Manager Query by Using WMI
How to Perform a Synchronous Configuration Manager Query by Using WMI
How to Read a Configuration Manager Object by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.133 -->

How to Call a Configuration Manager
Object Class Method by Using WMI
Article • 10/10/2022

To call a SMS Provider class method, in Configuration Manager, you use the
SWbemServices object ExecMethod method to call methods that are defined by the
class.

  ７ Note

  To call a method on an object instance, call the method from the object directly. For
  example, ObjectInstance.MethodName parameters .

To call a Configuration Manager object class method
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
         fundamentals.

   2. Using the SWbemServices you obtain in step one, call Get to get the class
         definition.

   3. Create the input parameters as a SWbemMethodSet.

   4. Using the SWbemServices object instance, call ExecMethod and specify the class
         name and input parameters.

   5. Retrieve the method return value from the ReturnValue property in the returned
         SWbemObject object.

Example
The following example validates a collection rule query by calling the
SMS_CollectionRuleQuery class ValidateQuery class method.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ValidateQueryRule(connection, wqlQuery)

<!-- p.134 -->

      Dim inParams
      Dim outParams
      Dim collectionRuleClass

      On Error Resume Next

      ' Obtain the class definition object of a SMS_CollectionRuleQuery
  object.
      Set collectionRuleClass = connection.Get("SMS_CollectionRuleQuery")

      If Err.Number<>0 Then
          Wscript.Echo "Couldn't get collection rule query object"
          Exit Sub
      End If

      ' Set up the in parameter.
      Set inParams =
  collectionRuleClass.Methods_("ValidateQuery").InParameters.SpawnInstance_
      inParams.WQLQuery = wqlQuery
      If Err.Number<>0 Then
          Wscript.Echo "Couldn't get in parameters object"
          Exit Sub
      End If

      ' Call the method.
      Set outParams = _
          connection.ExecMethod( "SMS_CollectionRuleQuery", "ValidateQuery",
  inParams)
      If Err.Number<>0 Then
          Wscript.Echo "Couldn't run method"
          Exit Sub
      End If

      If outParams.ReturnValue = True Then
          Wscript.Echo "Valid query"
      Else
          WScript.Echo "Not a valid query"
      End If
    End Sub

This example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter    Type                Description

 connection   - Managed:          A valid connection to the SMS Provider.
              SWbemServices

 wqlQuery     - String            A WQL query string. For this example, SELECT * FROM
                                  SMS_R_System is a valid query.

<!-- p.135 -->

Compiling the Code

See Also
Windows Management Instrumentation
Objects overview How to Connect to an SMS Provider in Configuration Manager by
Using WMI
How to Create a Configuration Manager Object by Using WMI
How to Delete a Configuration Manager Object by Using WMI
How to Modify a Configuration Manager Object by Using WMI
How to Perform an Asynchronous Configuration Manager Query by Using WMI
How to Perform a Synchronous Configuration Manager Query by Using WMI
How to Read a Configuration Manager Object by Using WMI
How to Read Lazy Properties by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.136 -->

About Configuration Manager Queries
Article • 10/10/2022

You can create and run the queries that are accessible in the Configuration Manager
console under Queries. The queries can be used to locate objects in a Configuration
Manager site that match your query criteria. These objects include items such as specific
types of computers or user groups. Queries can return most types of Configuration
Manager objects, including sites, collections, packages, and saved queries themselves.
However, queries are most useful for extracting information that is related to resource
discovery, inventory data, and status messages.

  ７ Note

  For more information, see Introduction to queries.

SMS_Query
Configuration Manager queries are defined by SMS_Query object instances. The query is
a WQL query and is defined in the Expression property. For more information about
WQL, see Configuration Manager Extended WMI Query Language.

Each query has a unique identifier assigned to it by the SMS Provider and can be used
to get a specific query.

For information about running a query, see How to Run a Configuration Manager Query.

You can also create queries by creating instances of SMS_Query . When you create a
query, it is displayed in the Configuration Manager console under Queries. If you want
to, you can limit the results returned to those resources that belong to a specific
collection. For more information about creating queries, see How to Create a
Configuration Manager Query.

See Also
Configuration Manager Extended WMI Query Language
Configuration Manager Result Sets
Configuration Manager Special Queries
How to Create a Configuration Manager Query

<!-- p.137 -->

How to Run a Configuration Manager Query
SMS_Query

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.138 -->

How to Run a Configuration Manager
Query
Article • 10/10/2022

In Configuration Manager, you run a SMS_Query based query by getting the query
instance and then by running WQL query in the SMS_Query object Expression property.

After you have the WQL query, you can run the query either synchronously or
asynchronously. The following example is synchronous. For information about running
the query asynchronously, see How to Perform an Asynchronous Configuration Manager
Query by Using Managed Code and How to Perform an Asynchronous Configuration
Manager Query by Using WMI. In these examples, change the select * from
collection string to the Expression property value.

To run a query
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Get the SMS_Query object for the query you want to run.

   3. Run the query identified by the SMS_Query object Expression property.

Example
The following example method synchronously runs the query identified by the queryId
parameter.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub RunQuery(connection, queryId)
      Dim query
      Dim queryResults
      Dim queryResult

         ' Get query.
         Set query=connection.Get("SMS_Query.QueryID='" & queryId    & "'" )

         If err.number<>0 Then

<!-- p.139 -->

         WScript.echo "Couldn't get Queries"
         Exit Sub
     End If

     ' Run query.
     WScript.echo query.Name
     WScript.echo "----------------------------------"

    Set queryResults=connection.ExecQuery(query.Expression)
    For Each queryResult In queryResults
        wscript.echo "     " & queryResult.Name
    Next
    If queryResults.Count=0 Then
        WScript.echo "      no query results"
    End If
End Sub

c#

public void RunQuery(WqlConnectionManager connection, string queryId)
{
    try
    {
        // Get the query.
        IResultObject query = connection.GetInstance(@"SMS_Query.QueryID='"
+ queryId + "'");

        Console.WriteLine(query["Name"].StringValue);
        Console.WriteLine("----------------------------------");

        // Get the query results.
        IResultObject queryResults =
connection.QueryProcessor.ExecuteQuery(query["Expression"].StringValue);

        bool resultsFound = false;
        foreach (IResultObject queryResult in queryResults)
        {
            resultsFound = true;
            Console.WriteLine(queryResult["Name"].StringValue);
        }
        if (resultsFound == false)
        {
            Console.WriteLine("     No query results");
        }
     }
     catch (SmsException ex)
     {
         Console.WriteLine("Failed to run query: " + ex.Message);
         throw;
     }
}

<!-- p.140 -->

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter    Type                        Description

 connection   - Managed:                  A valid connection to the SMS Provider.
              WqlConnectionManager
              - VBScript: SWbemServices

 queryID      - Managed: String           A query identifier. For more information see the
              - VBScript: String          SMS_Query class QueryID property.

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

<!-- p.141 -->

See Also
About Configuration Manager Queries
How to Create a Configuration Manager Query
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Perform an Asynchronous Configuration Manager Query by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.142 -->

How to Create a Configuration Manager
Query
Article • 10/10/2022

In Configuration Manager, you create an SMS_Query -based query by creating an instance
of SMS_Query . The SMS_Query class Expression object defines a WQL query. If you want
to limit the query results to a specific collection, specify the collection identifier in the
LimitToCollectionID property.

  ７ Note

  When you create a query, it is displayed in the Configuration Manager console
  under Queries.

To create a query
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Create an instance of SMS_Query.

   3. Populate the SMS_Query properties.

   4. Commit the SMS_Query .

   5. If required, retrieve the query object and get the query identifier.

Example
The following example method creates an SMS_Query class query that queries for all
systems. The method returns the query identifier, which can be used as input to the
example in How to Run a Configuration Manager Query.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Function CreateQuery(connection)
     On Error Resume Next

<!-- p.143 -->

     Dim query
     Dim path

     ' Create a query object.
      Set query = connection.Get("SMS_Query").SpawnInstance_()

      If Err.Number<>0 Then
          Wscript.Echo "Couldn't create query object"
          CreateQuery = Null
          Exit Function
      End If

      ' Populate the object.
      query.Comments = "A query for all systems"
      query.Expression = "select Name, " + _
      "SMSAssignedSites, " +              _
      "IPAddresses, " +                   _
      "IPSubnets, " +                     _
      "OperatingSystemNameandVersion, " + _
      "ResourceDomainORWorkgroup, " +     _
      "LastLogonUserDomain, " +           _
      "LastLogonUserName, " +             _
      "SMSUniqueIdentifier, " +           _
      "ResourceId, " +                    _
      "ResourceType, " +                  _
      "NetbiosName " +                    _
      "from sms_r_system"
      query.LimitToCollectionID = nothing
      query.Name = "Query All Systems"
      query.TargetClassName = "SMS_R_System"

      ' Commit the object
      path = query.Put_

      If Err.Number<>0 Then
          Wscript.Echo "Couldn't commit the query"
          CreateQuery = Null
          Exit Function
      End If

      WScript.Echo "Query created"

      ' Get the object back to get the query identifier.
      Set query = connection.Get(path)
      CreateQuery = query.QueryID

End Function

c#

<!-- p.144 -->

  public string CreateQuery(WqlConnectionManager connection)
  {
      try
      {
          // Create an SMS_Query object.
          IResultObject query = connection.CreateInstance("SMS_Query");

              // Populate the object.
              query["Comments"].StringValue = "A query for all systems";
              query["Expression"].StringValue =
                  "select Name, " +
                  "SMSAssignedSites, " +
                  "IPAddresses, " +
                  "IPSubnets, " +
                  "OperatingSystemNameandVersion, " +
                  "ResourceDomainORWorkgroup, " +
                  "LastLogonUserDomain, " +
                  "LastLogonUserName, " +
                  "SMSUniqueIdentifier, " +
                  "ResourceId, " +
                  "ResourceType, " +
                  "NetbiosName " +
                  "from sms_r_system";
              query["LimitToCollectionID"].StringValue = null;
              query["Name"].StringValue = "Query All Systems";
              query["TargetClassName"].StringValue = "SMS_R_System";

              // Commit the query.
              query.Put();

              // Get the query - allows access to the queryID.
              query.Get();

              // Return the query identifier.
              return query["QueryID"].StringValue;
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to run the query: " + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter      Type                              Description

 connection     - Managed: WqlConnectionManager   - A valid connection to the SMS Provider.

<!-- p.145 -->

 Parameter    Type                            Description

              - VBScript: SWbemServices

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
About Configuration Manager Queries
How to Run a Configuration Manager Query

<!-- p.146 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.147 -->

Configuration Manager SEDO
Article • 10/04/2022

Configuration Manager SEDO (Serialized Editing of Distributed Objects) in the
Configuration Manager SDK provides a mechanism for assigning and unassigning locks
to globally replicated SDK provider objects in the context of a site, computer and user.
SEDO-enabled objects are globally replicated SDK provider objects that require the user
to obtain a lock if that user wishes to edit and save that object. When the user obtains
that lock, the lock will be assigned to that user, the user's computer and the site in
which the computer resides. While that lock is assigned, no other user or computer will
be able to edit that object until the user releases the lock.

Only SEDO-enabled objects require users to obtain a lock before editing them. The
SEDO-enabled objects are the following:

      SMS_Application

      SMS_AuthorizationList

      SMS_BootImagePackage

      SMS_ConfigurationBaselineInfo

      SMS_ConfigurationItem

      SMS_DeploymentType

      SMS_Driver

      SMS_DriverPackage

      SMS_GlobalCondition

      SMS_ImagePackage

      SMS_OperatingSystemInstallPackage

      SMS_Package

      SMS_SoftwareUpdatesPackage

      SMS_TaskSequencePackage

Implicit and Explicit Lock Requests

<!-- p.148 -->

To prevent SEDO from breaking current SDK application functionalities, SEDO supports
both implicit and explicit lock requests. In the case of implicit requests, if the lock is
already assigned to the local site and the user attempts to edit a SEDO-enabled object,
then SEDO will automatically attempt to retrieve the lock. If SEDO succeeds in obtaining
the lock from the local site and the user edits the object, then that object will be saved
at the user's request, without having to make an explicit programmatic lock request.

However, if the lock is not assigned to the local site and a transfer of the lock from
another site must be requested, a request must be sent to the remote site that contains
the lock. This request must be made explicitly by the user.

For more information, and to learn how to explicitly request a lock, see How to Acquire
a Lock on a SEDO-Enabled Object.

Implicit and Explicit Lock Releases
SEDO also supports both implicit and explicit lock releases. In the case of implicit
releases, when a user saves an object using a Put() method, SEDO will attempt to
automatically release the lock. Otherwise, the release must be explicitly made.

To learn how to explicitly and implicitly release a lock, see How to Release a Lock on a
SEDO-Enabled Object.

See also
     How to Acquire a Lock on a SEDO-Enabled Object

     How to Release a Lock on a SEDO-Enabled Object

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.149 -->

How to Acquire a Lock on a SEDO-
Enabled Object
Article • 10/10/2022

To Acquire an Explicit Lock on a SEDO-enabled Object
   1. Create an instance of the SMS_ObjectLock WMI class

   2. Get the method parameters object for the RequestLock method.

   3. Assign the object path of the object you wish to lock to the ObjectRelPath
      property.

   4. Set the RequestTransfer property to true .

   5. Create an InvokeMethodOptions object instance. On the Context property, add a
      name/value pair. The name must be "ObjectLockContext" and the value must be a
      unique value such as a Guid. Add another name/value pair with "MachineName"
      and the name of the computer requesting the lock.

   6. Call InvokeMethod on the SMS_ObjectLock instance.

   7. InvokeMethod will return a SMS_ObjectLockRequest instance. Check the
      RequestState and LockState properties to get more information on the success or

      failure of the request.

Example
The following example requests an explicit lock on a SMS_ConfigurationItem object
instance.

   class Program
   {
       static void Main(string[] args)
       {
           ManagementScope scope = new
  ManagementScope(@"\\siteservername\root\sms\site_ABC");
           RequestLock(scope);
       }

        public static void RequestLock(ManagementScope scope)

<!-- p.150 -->

         {
             ManagementPath path = new ManagementPath("SMS_ObjectLock");
             ManagementClass objectLock = new ManagementClass(scope, path,
  null);

           ManagementBaseObject inParams =
  objectLock.GetMethodParameters("RequestLock");
           inParams["ObjectRelPath"] = "SMS_ConfigurationItem.CI_ID=30";
           inParams["RequestTransfer"] = true;

           InvokeMethodOptions options = new InvokeMethodOptions();
           options.Context.Add("ObjectLockContext",
  Guid.NewGuid().ToString());
           options.Context.Add("MachineName", "RequestingComputer");

           ManagementBaseObject result =
  objectLock.InvokeMethod("RequestLock", inParams, options);

         }
  }

The SMS_ObjectLockRequest object contains the following properties:

                                                                                   ﾉ   Expand table

 Property                    Description

 RequestID                   Unique identifier of the request.

 ObjectRelPath               The path of the object for which the lock is requested.

 RequestState                Indicates the success or failure of the request.

 LockState                   Indicates the current state of the requested lock.

 AssignedUser                Indicates the currently assigned user of the requested lock.

 AssignedObjectLockContext   Indicates ObjectLockContext the lock is currently assigned to.

 AssignedMachine             Indicates the currently assigned computer of the requested lock.

 AssignedSiteCode            Indicates the currently site of the requested lock.

 AssignedTimeUTC             Indicates the time at which the requested lock was assigned.

RequestState
The table below displays the possible request state values. Request states Granted,
GrantedAfterTimeout and GrantedLockWasOrphaned indicate a successful request and
the user can then make and save modifications to the object. All other requests indicate
error.

<!-- p.151 -->

                                                                ﾉ   Expand table

 RequestStateID                    RequestStateName

 0                                 Unknown

 2                                 Requested

 3                                 RequestedCanceled

 4                                 ResponseReceived

 10                                Granted

 11                                GrantedAfterTimeout

 12                                GrantedLockWasOrphaned

 20                                DeniedLockAlreadyAssigned

 21                                DeniedInvalidObjectVersion

 22                                DeniedLockNotFound

 23                                DeniedLockNotLocal

 24                                DeniedRequestTimedOut

 50                                Error

 52                                ErrorRequestNotFound

 53                                ErrorRequestTimedOut

LockState
The table below displays the possible lock state values.

                                                                ﾉ   Expand table

 LockStateID                         LockStateName

 0                                   Unassigned

 1                                   Assigned

 2                                   Requested

 3                                   PendingAssignment

 4                                   TimedOut

 5                                   NotFound

<!-- p.152 -->

Compiling the Code
The C# example requires:

Namespaces
System

System.Management

Assembly

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
Configuration Manager SEDO

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.153 -->

How to Release a Lock on a SEDO-
Enabled Object
Article • 10/10/2022

To Release an Explicit Lock on a SEDO-enabled Object
   1. Create an instance of the SMS_ObjectLock WMI class

   2. Get the method parameters object for the ReleaseLock method.

   3. Assign the object path of the object you wish to unlock to the ObjectRelPath
      property.

   4. Create an InvokeMethodOptions object instance. On the Context property, add a
      name/value pair. The name must be "MachineName" and the value must be name
      of the computer releasing the lock. For more information, see How to Acquire a
      Lock on a SEDO-Enabled Object

   5. Call InvokeMethod on the SMS_ObjectLock instance.

   6. InvokeMethod will return a SMS_ObjectLockRequest instance. Check the
      RequestState and LockState properties to get more information on the success or

      failure of the request.

Example
The following example releases a lock on a SMS_ConfigurationItem object instance.

  class Program
  {
      static void Main(string[] args)
      {
          ManagementScope scope = new
  ManagementScope(@"\siteservername\root\sms\site_ABC");
          ReleaseLock(scope);
      }

       public static void ReleaseLock(ManagementScope scope)
       {
           ManagementPath path = new ManagementPath("SMS_ObjectLock");
           ManagementClass objectLock = new ManagementClass(scope, path, null);

<!-- p.154 -->

          ManagementBaseObject inParams =
  objectLock.GetMethodParameters("ReleaseLock");
          inParams["ObjectRelPath"] = "SMS_ConfigurationItem.CI_ID=30";

             InvokeMethodOptions options = new InvokeMethodOptions();
             options.Context.Add("MachineName", "RequestingComputer");

          ManagementBaseObject result = objectLock.InvokeMethod("ReleaseLock",
  inParams, options);

         }
  }

The SMS_ObjectLockRequest object contains the following properties:

                                                                                  ﾉ   Expand table

 Property                    Description

 RequestID                   Unique identifier of the request.

 ObjectRelPath               The path of the object for which the lock is requested.

 RequestState                Indicates the success or failure of the request.

 LockState                   Indicates the current state of the requested lock.

 AssignedUser                Indicates the currently assigned user of the requested lock.

 AssignedObjectLockContext   Indicates ObjectLockContext the lock is currently assigned to.

 AssignedMachine             Indicates the currently assigned computer of the requested lock.

 AssignedSiteCode            Indicates the current site of the requested lock.

 AssignedTimeUTC             Indicates the time at which the requested lock was assigned.

RequestState
The table below displays the possible request state values. Request states Granted,
GrantedAfterTimeout and GrantedLockWasOrphaned indicate a successful request and
the user can then make and save modifications to the object. All other requests indicate
error.

                                                                                  ﾉ   Expand table

<!-- p.155 -->

 RequestStateID                    RequestStateName

 0                                 Unknown

 2                                 Requested

 3                                 RequestedCanceled

 4                                 ResponseReceived

 10                                Granted

 11                                GrantedAfterTimeout

 12                                GrantedLockWasOrphaned

 20                                DeniedLockAlreadyAssigned

 21                                DeniedInvalidObjectVersion

 22                                DeniedLockNotFound

 23                                DeniedLockNotLocal

 24                                DeniedRequestTimedOut

 50                                Error

 52                                ErrorRequestNotFound

 53                                ErrorRequestTimedOut

LockState
The table below displays the possible lock state values.

                                                                ﾉ   Expand table

 LockStateID                         LockStateName

 0                                   Unassigned

 1                                   Assigned

 2                                   Requested

 3                                   PendingAssignment

 4                                   TimedOut

 5                                   NotFound

<!-- p.156 -->

Compiling the Code
The C# example requires:

Namespaces
System

System.Management

Assembly

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
Configuration Manager SEDO

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.157 -->

About Configuration Manager
Schedules
Article • 10/10/2022

In Configuration Manager, scheduling information is configured by using schedule
tokens. The SMS_ScheduleToken Windows Management Instrumentation (WMI) class is
an abstract parent class for the SMS_ST_ schedule token classes that handle the
scheduling of events with differing frequencies such as daily, weekly, and monthly.

The SMS_ScheduleMethods WMI class, and the corresponding ReadFromString and
WriteToString methods are used to decode and encode schedule tokens into and from

an interval string. The interval strings can be used to set schedule properties when
defining or modifying objects.

Schedule Token Classes Used To Create
Different Types of Schedules
The following table describes the embedded classes that you can use to provide
scheduling information to Configuration Manager components.

SMS_ST_NonRecurring Server WMI Class
The SMS_ST_NonRecurring WMI class is used for nonrecurring event scheduling by
designating a date and time.

SMS_ST_RecurInterval Server WMI Class
The SMS_ST_RecurInterval WMI class enables the scheduling of events that occur at
regular intervals, such as every 10 days, rather than on designated dates and times.

SMS_ST_RecurMonthlyByDate Server WMI Class
The SMS_ST_RecurMonthlyByDate WMI class enables the scheduling of events that occur
on designated days at designated monthly intervals, such as every third month on the
15th day of the month.

SMS_ST_RecurMonthlyByWeekday Server WMI Class
The SMS_ST_RecurMonthlyByWeekday WMI class enables the scheduling of events that
occur for a specific day of the week, on a given week of the month, at a given monthly
interval. For example, the second Saturday of every month.

SMS_ST_RecurWeekly Server WMI Class
The SMS_ST_RecurWeekly WMI class enables the scheduling of events that occur at

<!-- p.158 -->

weekly intervals, regardless of the week's sequence in any month, such as every third
week on Wednesday.

Class and Methods Used to Read or Write
Schedule Tokens
The following SMS_ScheduleMethods WMI class, and the corresponding ReadFromString
and WriteToString methods are used to decode and encode schedule tokens into and
from an interval string.

SMS_ScheduleMethods Server WMI Class
The SMS_ScheduleMethods WMI class contains methods for decoding and encoding
schedule tokens into and from an interval string.

These methods are not used to convert the schedule tokens to or from the friendly
scheduling strings found in the Configuration Manager console, such as Occurs every 1
day(s) effective 9:27AM Tuesday. Instead, the methods are used to convert the schedule
tokens to or from SMS interval strings (SMS interval strings are not of the same format
as the WMI interval strings). SMS interval strings are an internal representation of the
schedule token.

ReadFromString Method in Class SMS_ScheduleMethods
The ReadFromString WMI class method decodes interval strings and places the results
into SMS_ScheduleToken objects.

WriteToString Method in Class SMS_ScheduleMethods
The WriteToString WMI class method encodes SMS_ScheduleToken data into an SMS
interval string.

See also
      How to Create a Schedule Token
      SMS_ST_NonRecurring Server WMI Class
      SMS_ST_RecurInterval Server WMI Class
      SMS_ST_RecurMonthlyByDate Server WMI Class
      SMS_ST_RecurMonthlyByWeekday Server WMI Class
      SMS_ST_RecurWeekly Server WMI Class
      SMS_ScheduleMethods Server WMI Class
      ReadFromString Method in Class SMS_ScheduleMethods
      WriteToString Method in Class SMS_ScheduleMethods

<!-- p.159 -->

     Microsoft.ConfigurationManagement.Messaging.Framework.Scheduler namespace

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.160 -->

How to Create a Schedule Token
Article • 10/10/2022

You create a schedule token, in Configuration Manager, by creating and populating an
instance of the appropriate SMS_ST_ schedule token class. SMS_ST schedule classes are
child classes of the SMS_ScheduleToken class and handle the scheduling of events with
differing frequencies such as daily, weekly and monthly.

The SMS_ScheduleMethods Windows Management Instrumentation (WMI) class, and
the corresponding ReadFromString and WriteToString methods are used to decode and
encode schedule tokens into and from an interval string. The interval strings can then be
used to set schedule properties when defining or modifying objects. An example of this
can be seen in the How to Create a Maintenance Window for a Collection topic where
the ServiceWindowSchedules property is configured.

To create a schedule token and convert it to an interval
string
   1. Create a schedule token object by using one of the SMS_ScheduleToken child
        classes. This example uses the SMS_ST_RecurInterval class.

   2. Populate the properties of the new schedule token object.

   3. Convert the schedule token object to an interval string by using the
        SMS_ScheduleMethods class and WriteToString method.

   4. Use the interval string to populate an object's schedule properties, as needed.

Example
The following example method shows how to create a schedule token by creating and
populating an instance of the SMS_ST_RecurInterval schedule token class. In addition,
the example shows how to convert the schedule to an interval string by using the
SMS_ScheduleMethods class and WriteToString method.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs
