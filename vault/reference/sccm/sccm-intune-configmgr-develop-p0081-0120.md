---
title: "Configuration Manager SDK documentation — pages 81-120"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0081-0120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0081-0120
family: sccm
documentKind: "doc"
abstract: "Configuration Manager Lazy Properties Article • 10/10/2022 Some Configuration Manager object properties are relatively inefficient to retrieve. If these properties were retrieved for many instances in a class (as might be done in a query), the response would be considerably dela"
---

# Configuration Manager SDK documentation — pages 81-120

<!-- p.81 -->

Configuration Manager Lazy Properties
Article • 10/10/2022

Some Configuration Manager object properties are relatively inefficient to retrieve. If
these properties were retrieved for many instances in a class (as might be done in a
query), the response would be considerably delayed. Such properties are considered
lazy properties and are not usually retrieved during query operations. However, if these
properties are retrieved during a query, they have null or zero values, which might not
be the actual value of the property for every instance. Therefore, if you want to get the
correct value for lazy properties, you must get each instance individually.

See Also
How to Read Lazy Properties Using Managed Code
How to Read Lazy Properties Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.82 -->

Configuration Manager Extended WMI
Query Language
Article • 10/10/2022

Configuration Manager supports a superset of the Windows Management
Instrumentation (WMI) Query Language (WQL) known as Extended WQL. Both WQL and
Extended WQL are retrieval-only languages that are used to create queries. Neither
language can be used to create, modify, or delete classes or instances.

WQL and Extended WQL are based on the American National Standards Institute (ANSI)
Structured Query Language (SQL) standard. However, they differ from standard SQL in
that they retrieve from classes rather than tables and return instances rather than rows.

Extended WQL supports elements from two versions of ANSI SQL:

ANSI-92, which is the recommended version for most operations.

ANSI-89, which is primarily used only for JOIN operations by Open Database
Connectivity (ODBC) applications requiring the services of the WMI ODBC Adapter.

Extended WQL includes a much broader range of operations than WQL. The following
list shows the SELECT clauses that Extended WQL supports:

DISTINCT

COUNT

JOIN

WHERE

SUBSTRING

ORDER BY

UPPER, LOWER , and DATEPART functions

Because Extended WQL is fully case-insensitive, the UPPER and LOWER functions are not
useful. Extended WQL supports the standard comparison operators (including LIKE and
IN) and sub queries.

The SMS Provider does not support querying on system properties. System properties
are those preceded by a double underscore prefix, for example __path .

<!-- p.83 -->

Association queries are limited to the WQL syntax.

The use of COUNT and DISTINCT keywords together in a statement is not supported.

in Configuration Manager the WHERE clause supports GetDate() , DateDiff() , and
DateAdd() .

The ORDER BY clause does not work with the collection-limiting context qualifier.

See Also
Configuration Manager Association Classes
Configuration Manager Bit Field Properties
Configuration Manager Date and Time Formats
Configuration Manager Embedded Objects
Objects overview Configuration Manager Lazy Properties
About errors Configuration Manager Object Security
Configuration Manager Special Queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.84 -->

Configuration Manager Result Sets
Article • 10/04/2022

In Configuration Manager, the result set of a query contains one or more instances that
match the specified criteria of the SELECT statement. The result instances are either
Generic class instances or instances of the class that is specified in the FROM clause.

__Generic Class Results
The results of a JOIN operation are returned in either an instance of a class specified in
the query or an instance of the __ Generic class. If a single class is implied by the
property list in the SELECT statement, the results are returned as instances of that class.
If there are multiple classes, the results are returned as instances of the __Generic class.

The __ Generic class is a generic container for the results of JOIN operations and COUNT
operations. This class has no set definition. Its properties depend on its use at the time.
For JOIN results, the properties are embedded objects representing the classes specified
in the query, as the following example shows.

SELECT * FROM SMS_Package AS Pack

INNER JOIN SMS_Program AS Prog

ON Pack.PackageID = Prog.PackageID

The following example shows the __Generic class result of the above query.

Class __Generic

{

SMS_Package Pack;

SMS_Program Prog;

}

For COUNT results, the instance includes a Count property, as the following class shows.

Class __Generic

{

<!-- p.85 -->

uint32 Count;

}

Actual Class Instance Results
The class instances that are returned in a result set contain both system and class
properties. However, embedded and lazy properties are not returned.

The system properties include those for the specified class and its derived classes.
Because not all system properties are relevant to all queries, the value of a particular
system property can be null .

The class properties that are returned depend on whether you specify a property list or
the asterisk. If you specify a property list containing one or more class properties, the
returned instance contains only the properties in the list. The property list should
include the key properties for the class. When you invoke a query that does not specify
key properties in the property list, the result set contains incomplete and therefore
incorrect values for the system properties, __Path and __Relpath .

See Also
How to Read Lazy Properties Using Managed Code
How to Read Lazy Properties Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.86 -->

Configuration Manager Special Queries
Article • 10/04/2022

Extended WMI Query Language (WQL) supports queries that are specific to
Configuration Manager needs. The following table describes the additional queries that
are supported.

Array property
Particular values in an array property.

Base class
Property values that exist in a base class.

Prototype
A class definition rather than class data.

Collection-limiting
Data that is specific to a particular collection.

Array Property Queries
Due to the nature of array properties, including them in an extended WQL query can be
somewhat complex. For example, consider the SMS_R_System class that includes the
IPAddresses property. The IPAddresses property is an array that contains one or more

individual addresses. To query for computers with IP addresses, you can specify one of
the following two queries.

SELECT * FROM SMS_R_System WHERE IPAddresses = "2.2.2.2"

SELECT * FROM SMS_R_System WHERE IPAddresses IN ("1.1.1.1", "2.2.2.2")

Base Class Queries
Extended WQL queries on a base class return instances from all the subclasses. For
abstract base class queries, the instances that are returned are always instances of the
derived classes. For example, the following query returns instances from classes such as
SMS_SCI_Component and SMS_SCI_Address , which inherit properties from
SMS_SiteControlItem .

SELECT * FROM SMS_SiteControlItem WHERE Sitecode="ABC"

<!-- p.87 -->

Prototype Queries
Extended WQL allows you to request that the result set contains a definition of the class
to be returned rather than the actual instances of the class. There are two possible
results from this type of query. For most cases, a prototype query returns a class object
that contains the definition. If the query is a JOIN operation with multiple classes in the
SELECT statement, the prototype query returns an instance of the __Generic class.

Although prototype queries are most useful in processing the results of JOIN
operations, they are supported for all queries. To request a class definition as the result
set, set the lFlags parameter in IWbemServices::ExecQuery or
IWbemServices::ExecQueryAsync to WBEM_FLAG_PROTOTYPE.

Collection-limiting Queries
A Configuration Manager collection is a grouping of resources such as computers and
users. Extended WQL supports queries against particular collections. There are two
approaches that you can use to limit a query to a particular collection:

Set the LimitToCollectionIDs context value to the required CollectionID value. This
context value is made available through the IWbemContext pointer in the
IWbemServices::ExecQuery method to the name of the collection.

Specify an inner JOIN operation by using the SMS_CollectionMember -derived classes in
the query that is passed to ExecQuery.

The second approach is slower, but it is the only possible approach if you use an
application that uses the WMI ODBC Adapter.

See Also
Configuration Manager Association Classes
Configuration Manager Bit Field Properties
Configuration Manager Date and Time Formats
Configuration Manager Embedded Objects
Configuration Manager Extended WMI Query Language
Objects overview Configuration Manager Lazy Properties
About errors Configuration Manager Object Security

<!-- p.88 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.89 -->

How to Create a Configuration Manager
Object by Using Managed Code
Article • 10/10/2022

To create a Configuration Manager object by using the managed SMS Provider, use
WqlConnectionManager.CreateInstance method. The
ConnectionManagerBase.CreateInstance method takes the required object type as a
string parameter and returns an IResultObject object that is used to populate the new
object. The IResultObject.Put method must be called to submit the object to the SMS
Provider.

To create a Configuration Manager object
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Using the WqlConnectionManager connection object you obtain in step one, call
      [CreateInstance to create the required the WMI object, and receive its
      IResultObject object instance.

   3. Populate the IResultObject properties.

   4. Commit the IResultObject to the SMS Provider.

Example
The following example demonstrates how to create and then populate a new
Configuration Manager package ( SMS_Package ).

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  public void CreatePackage(WqlConnectionManager connection)
  {
      try
      {
          IResultObject package = connection.CreateInstance("SMS_Package");
          package["Name"].StringValue = "Test Package";
          package["Description"].StringValue = "A test package";
          package["PkgSourcePath"].StringValue = @"c:\Package Source";

<!-- p.90 -->

              package.Put();
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create package. Error: " + ex.Message);
          throw;
      }
  }

This example method has the following parameters:

                                                                        ﾉ   Expand table

 Parameter      Type                            Description

 connection     Managed: WqlConnectionManager   A valid connection to the SMS Provider.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

<!-- p.91 -->

See Also
Objects overview Configuration Manager Lazy Properties
How to Call a Configuration Manager Object Class Method by Using Managed Code
How to Connect to a Configuration Manager Provider using Managed Code
How to Modify a Configuration Manager Object by Using Managed Code
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Perform a Synchronous Configuration Manager Query by Using Managed Code
How to Read a Configuration Manager Object by Using Managed Code
How to Read Lazy Properties by Using Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.92 -->

How to Read a Configuration Manager
Object by Using Managed Code
Article • 10/10/2022

To read a Configuration Manager object instance by using the managed SMS Provider,
use WqlConnectionManager.GetInstance. The GetInstance method takes a string that
identifies a specific object instance and returns an IResultObject object that is used to
access the object.

The following example function shows the name and description for a supplied package
identifier.

To read a Configuration Manager object
   1. Set up a connection to the SMS Provider. For more information, see How to
      Connect to an SMS Provider in Configuration Manager by Using Managed Code.

   2. Call WqlConnectionManager class GetInstance method to get the IResultObject
      object for the object you want.

   3. Display the properties of the IResultObject.

Example
The following code example shows how to read a Configuration Manager object.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  public void DisplayPackageName(WqlConnectionManager connection, string
  packageID)
  {
      try
      {
          // Get the package.
          IResultObject package =
  connection.GetInstance(@"SMS_Package.PackageID='" + packageID + "'");
          Console.WriteLine("Package Name: " + package["Name"].StringValue);
          Console.WriteLine("Package Description: " +
  package["Description"].StringValue);
      }
      catch (SmsException ex)

<!-- p.93 -->

      {
              Console.WriteLine("Failed to get package. Error: " + ex.Message);
              throw;
      }
  }

This example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter      Type                     Description

 Connection     - Managed:               - A valid connection to the SMS Provider.
                WqlConnectionManager

 PackageID      - Managed: String        A valid package identifier. Obtained from the
                                         SMS_Package class PackageID property.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

<!-- p.94 -->

See Also
Objects overview Configuration Manager Lazy Properties
How to Call a Configuration Manager Object Class Method by Using Managed Code
How to Connect to a Configuration Manager Provider using Managed Code
How to Create a Configuration Manager Object by Using Managed Code
How to Modify a Configuration Manager Object by Using Managed Code
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Perform a Synchronous Configuration Manager Query by Using Managed Code
How to Read Lazy Properties by Using Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.95 -->

How to Modify a Configuration
Manager Object by Using Managed
Code
Article • 10/10/2022

To modify a Configuration Manager object instance by using the managed SMS
Provider, use the object's IResultObject interface to make modifications. You then call
the IResultObject.Put method to submit the changes.

  ７ Note

  The IResultObject interface for an object can be obtained through the
  WqlConnectionManager.GetInstance method or through other queries. For an
  example that uses asynchronous queries, see How to Perform an Asynchronous
  Configuration Manager Query Using Managed Code.

To modify a Configuration Manager object
   1. Set up a connection to the SMS Provider. For more information, see How to
      Connect to an SMS Provider in Configuration Manager by Using Managed Code.

   2. Using the WqlConnectionManager object you obtain in step one, call GetInstance
      to get an IResultObject for the required object.

   3. Make changes to object using the IResultObject.

   4. Commit the changes to the SMS provider with the IResultObject object Put
      method.

Example
The following example function updates a package's description from a supplied
package identifier and description.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

<!-- p.96 -->

  public void ModifyPackageDescription(WqlConnectionManager connection, string
  packageID, string description)
  {
      try
      {
          IResultObject package =
  connection.GetInstance(@"SMS_Package.PackageID='" + packageID + "'");
          Console.WriteLine("Package Name: " + package["Name"].StringValue);
          Console.WriteLine("Current Description: " +
  package["Description"].StringValue);

              package["Description"].StringValue = description;

              package.Put();

          Console.WriteLine("New description: " +
  package["Description"].StringValue);
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to get package. Error: " + ex.Message);
          throw;
      }
  }

This example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter        Type                     Description

 connection        WqlConnectionManager    A valid connection to the SMS Provider.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

<!-- p.97 -->

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

See Also
Objects overview Configuration Manager Lazy Properties
How to Call a Configuration Manager Object Class Method by Using Managed Code
How to Connect to a Configuration Manager Provider using Managed Code
How to Create a Configuration Manager Object by Using Managed Code
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Perform a Synchronous Configuration Manager Query by Using Managed Code
How to Read a Configuration Manager Object by Using Managed Code
How to Read Lazy Properties by Using Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.98 -->

How to Delete a Configuration Manager
Object by Using Managed Code
Article • 10/10/2022

To delete a Configuration Manager object by using the managed SMS Provider, use the
IResultObject.Delete method. You can get a IResultObject object for a Configuration
Manager object in numerous ways. For more information, see How to Read a
Configuration Manager Object by Using Managed Code

To delete a Configuration Manager object
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Using the WqlConnectionManager object you obtain in step one, call the
      GetInstance method to get the IResultObject object for the Configuration
      Manager object.

   3. Call the IResultObject object Delete method to delete the Configuration Manager
      object.

Example
The following example deletes a package by using the supplied package identifier. This
example uses the WqlConnectionManager class GetInstance method to get an
IResultObject object for the Configuration Manager package and then deletes the
package.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  public void DeletePackage(WqlConnectionManager connection, string packageID)
  {
      try
      {
          IResultObject package =
  connection.GetInstance(@"SMS_Package.PackageID='" + packageID + "'");
          package.Delete();
      }
      catch (SmsException ex)

<!-- p.99 -->

      {
              Console.WriteLine("Failed to delete package: " + ex.Message);
              throw;
      }
  }

This example method has the following parameters:

                                                                             ﾉ   Expand table

 Parameter      Type                   Description

 connection     -                      A valid connection to the SMS Provider.
                WqlConnectionManager

 PackageID      - String               The package identifier for an existing package. This can
                                       be obtained from the SMS_Package class PackageID
                                       property.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

<!-- p.100 -->

See Also
Objects overview How to Call a Configuration Manager Object Class Method by Using
Managed Code
How to Connect to a Configuration Manager Provider using Managed Code
How to Create a Configuration Manager Object by Using Managed Code
How to Modify a Configuration Manager Object by Using Managed Code
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Perform a Synchronous Configuration Manager Query by Using Managed Code
How to Read a Configuration Manager Object by Using Managed Code
How to Read Lazy Properties by Using Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.101 -->

How to Perform an Asynchronous
Configuration Manager Query by Using
Managed Code
Article • 10/10/2022

In Configuration Manager, to perform an asynchronous query by using the managed
SMS Provider, you use the ProcessQuery method.

The first parameter of the ProcessQuery method is an instance of the
SmsBackgroundWorker class that provides two event handlers:

      QueryProcessObjectReady. This event handler is called for each object returned by
      the query. The event handler provides an IResultObject object that represents the
      object.

      QueryProcessCompleted. This event handler is called when the query is completed.
      It also provides information about any errors that occur. For more information, see
      For information about error handling, see How to Handle Configuration Manager
      Asynchronous Errors by Using Managed Code.

      The second parameter to of the ProcessQuery method is the WQL statement for
      the query.

To perform an asynchronous query
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Create the SmsBackgroundWorker object and populate the
      QueryProcessorObjectReady and QueryProcessorCompleted properties with the
      callback method names.

   3. From the WqlConnectionManager object you obtain in step one, call the
      QueryProcessor object ProcessQuery method to start the asynchronous query.

Example
The following example queries for all available SMS_Collection objects, and in the event
handler, the example writes several of the collection properties to the Configuration
Manager console.

<!-- p.102 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  public void QueryCollections(WqlConnectionManager connection)
  {
      try
      {
          // Set up the query.
          SmsBackgroundWorker bw1 = new SmsBackgroundWorker();
          bw1.QueryProcessorObjectReady += new
  EventHandler<QueryProcessorObjectEventArgs>(bw1_QueryProcessorObjectReady);
          bw1.QueryProcessorCompleted += new
  EventHandler<RunWorkerCompletedEventArgs>(bw1_QueryProcessorCompleted);

          // Query for all collections.
          connection.QueryProcessor.ProcessQuery(bw1, "select * from
  SMS_Collection");

            // Pause while query runs.
            Console.ReadLine();
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to start asynchronous query: ",
  ex.Message);
      }
  }

  void bw1_QueryProcessorObjectReady(object sender,
  QueryProcessorObjectEventArgs e)
  {
      try
      {
          // Get the collection.
          IResultObject collection = (IResultObject)e.ResultObject;

            //Display properties.
            Console.WriteLine(collection["CollectionID"].StringValue);
            Console.WriteLine(collection["Name"].StringValue);
            Console.WriteLine();
            collection.Dispose();
      }
      catch (SmsQueryException eX)
      {
          Console.WriteLine("Query Error: " + eX.Message);
      }
  }

  void bw1_QueryProcessorCompleted(object sender, RunWorkerCompletedEventArgs
  e)
  {

<!-- p.103 -->

      Console.WriteLine("Done...");
  }

This example method has the following parameters:

                                                                       ﾉ   Expand table

 Parameter    Type                            Description

 connection   Managed: WqlConnectionManager   A valid connection to the SMS Provider.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

See Also
Objects overview Configuration Manager Lazy Properties
How to Call a Configuration Manager Object Class Method by Using Managed Code
How to Connect to a Configuration Manager Provider using Managed Code
How to Create a Configuration Manager Object by Using Managed Code

<!-- p.104 -->

How to Modify a Configuration Manager Object by Using Managed Code
How to Perform a Synchronous Configuration Manager Query by Using Managed Code
How to Read a Configuration Manager Object by Using Managed Code
How to Read Lazy Properties by Using Managed Code
How to Perform a Synchronous Configuration Manager Query Using Managed Code
Configuration Manager Extended WMI Query Language
Configuration Manager Result Sets
Configuration Manager Special Queries
About queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.105 -->

How to Perform a Synchronous
Configuration Manager Query by Using
Managed Code
Article • 10/10/2022

To perform a synchronous query by using the managed SMS Provider, you use
WqlConnectionManager.QueryProcessor.ExecuteQuery method.

The ExecuteQuery method takes a WQL query string and optional context information
for the call. An IResultObject is returned containing the objects found in the query.

To perform a synchronous query
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Using the WqlConnectionManager object you obtain in step one, call the
      QueryProcessor object ExecuteQuery method to query SMS Provider and get an
      IResultObject containing a collection of query results.

Example
The following code example shows how to make a synchronous query for the available
packages by using ExecuteQuery.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  public void QueryPackages(WqlConnectionManager connection)
  {
      try
      {
          IResultObject query = connection.QueryProcessor.ExecuteQuery("Select
  * from SMS_Package");
          foreach (IResultObject o in query)
          {
              Console.WriteLine(o["Name"].StringValue);
              o.Dispose();
          }
      }
      catch (SmsException ex)

<!-- p.106 -->

      {
              Console.WriteLine("Failed to query packages: " + ex.Message);
              throw;
      }
  }

This example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter       Type                            Description

 connection      Managed: WqlConnectionManager   A valid connection to the SMS Provider.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

See Also

<!-- p.107 -->

Objects overview Configuration Manager Lazy Properties
How to Call a Configuration Manager Object Class Method by Using Managed Code
How to Connect to a Configuration Manager Provider using Managed Code
How to Create a Configuration Manager Object by Using Managed Code
How to Modify a Configuration Manager Object by Using Managed Code
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Read a Configuration Manager Object by Using Managed Code
How to Read Lazy Properties by Using Managed Code
Configuration Manager Extended WMI Query Language
Configuration Manager Result Sets
Configuration Manager Special Queries
About queries

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.108 -->

How to Read Lazy Properties by Using
Managed Code
Article • 10/10/2022

To read a lazy property from a Configuration Manager object returned in a query, you
get the object instance, which retrieves any lazy object properties from the SMS
Provider.

  ７ Note

  If you know the full path to the WMI object, a call to the GetInstance method
  returns the WMI object along with any lazy properties. For more information, see
  How to Read a Configuration Manager Object by Using Managed Code.

For more information, see Configuration Manager Lazy Properties.

To read lazy properties
   1. Set up a connection to the SMS Provider. For more information, see How to
      Connect to an SMS Provider in Configuration Manager by Using Managed Code.

   2. Use QueryProcessor object to query Configuration Manager objects.

   3. Iterate through the query results.

   4. Using the WqlConnectionManager you obtain in step one, call GetInstance to get
      the IResultObject object for each queried object that you want to get lazy
      properties from.

Example
The following C# code example queries for all SMS_Collection objects and then displays
rule names obtained from the CollectionRules lazy property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  public void ReadLazyProperty(WqlConnectionManager connection)
  {

<!-- p.109 -->

      try
      {
          // Query all collections.
          IResultObject collections =
  connection.QueryProcessor.ExecuteQuery("Select * from SMS_Collection");
          foreach (IResultObject collection in collections)
          {
              // Get the collection object and lazy properties.
              collection.Get();

              Console.WriteLine(collection["Name"].StringValue);

              // Get the rules.
              List<IResultObject> rules =
  collection.GetArrayItems("CollectionRules");
              if (rules.Count == 0)
              {
                  Console.WriteLine("No rules");
                  Console.WriteLine();
                  continue;
              }

              foreach (IResultObject rule in rules)
              {
                  // Display rule names.
                  Console.WriteLine("Rule name: " +
  rule["RuleName"].StringValue);
              }

              Console.WriteLine();
          }
      }
      catch (SmsQueryException ex)
      {
          Console.WriteLine("Failed to get collection. Error: " + ex.Message);
          throw;
      }
  }

This example method has the following parameters:

                                                                       ﾉ   Expand table

 Parameter     Type                      Description

 connection    - WqlConnectionManager    A valid connection to the SMS Provider.

Compiling the Code

<!-- p.110 -->

Namespaces
System

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

See Also
Objects overview Configuration Manager Lazy Properties
How to Call a Configuration Manager Object Class Method by Using Managed Code
How to Connect to a Configuration Manager Provider using Managed Code
How to Create a Configuration Manager Object by Using Managed Code
How to Modify a Configuration Manager Object by Using Managed Code
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Perform a Synchronous Configuration Manager Query by Using Managed Code
How to Read a Configuration Manager Object by Using Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.111 -->

How to Call a Configuration Manager
Object Class Method by Using Managed
Code
Article • 10/10/2022

To call a SMS Provider class method, in Configuration Manager, you use the
ExecuteMethod method. You populate a Dictionary object with the method's
parameters, and the return value is an IResultObject object that contains the result of
the method call.

  ７ Note

  To call a method on an object instance, use the ExecuteMethod method on the
  IResultObject object instance.

To call a Configuration Manager object class method
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Create the input parameters as a Dictionary object.

   3. Using the WqlConnectionManager object instance, call ExecuteMethod and
      specify the class name and input parameters.

   4. Retrieve the method return value from the ReturnValue property in the returned
      IResultObject object.

Example
The following example validates a collection rule query by calling the
SMS_CollectionRuleQuery class ValidateQuery class method.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  public void ValidateQueryRule(WqlConnectionManager connection, string
  wqlQuery)

<!-- p.112 -->

  {
      try
      {
          Dictionary<string,object> validateQueryParameters = new
  Dictionary<string,object>();

              // Add the sql query as the WQLQuery parameter.
              validateQueryParameters.Add("WQLQuery",wqlQuery);

          // Call the method
          IResultObject
  result=connection.ExecuteMethod("SMS_CollectionRuleQuery", "ValidateQuery",
  validateQueryParameters);

              if (result["ReturnValue"].BooleanValue == true)
              {
                   Console.WriteLine (wqlQuery + " is a valid query");
              }
              else
              {
                   Console.WriteLine (wqlQuery + " is not a valid query");
              }
         }
         catch (SmsException ex)
         {
               Console.WriteLine("Failed to validate query rule: ",ex.Message);
               throw;
         }
  }

This example method has the following parameters:

                                                                           ﾉ     Expand table

 Parameter      Type                       Description

 connection     - Managed:                 A valid connection to the SMS Provider.
                WqlConnectionManager

 wqlQuery       - Managed: IResultObject   A WQL query string. For this example, SELECT *
                                           FROM SMS_R_System is a valid query.

Compiling the Code

Namespaces
System

<!-- p.113 -->

System.Collections.Generic

System.ComponentModel

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managementprovider

adminui.wqlqueryengine

Robust Programming
The Configuration Manager exceptions that can be raised are SmsConnectionException
and SmsQueryException. These can be caught together with SmsException.

See Also
Objects overview How to Connect to a Configuration Manager Provider using Managed
Code
How to Create a Configuration Manager Object by Using Managed Code
How to Modify a Configuration Manager Object by Using Managed Code
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Perform a Synchronous Configuration Manager Query by Using Managed Code
How to Read a Configuration Manager Object by Using Managed Code

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.114 -->

How to Create a Configuration Manager
Object by Using WMI
Article • 10/10/2022

You create a Configuration Manager object, in Configuration Manager, by calling the
SWbemObject object SpawnInstance_ method.

The SWbemObject is the class definition for the object type that you want to create. For
example, SMS_Package. You get the SWbemObject by calling the SWBemServices object
Get method.

To create a Configuration Manager object
   1. Set up a connection to the SMS Provider. For more information, see How to
        Connect to an SMS Provider in Configuration Manager by Using WMI.

   2. Using the SWBemServices object you obtain from step one, call Get to get the
        SWbemObject for the Configuration Manager object class definition.

   3. Call SpawnInstance_ on the SWbemObject to create the new object. An
        SWbemObject is returned for the new object.

   4. Using the SWbemObject returned from the call to SpawnInstance, populate the
        object properties.

   5. Call Put_ to commit the new object to the SMS Provider.

Example
The following VBScript code example creates an SMS_Package object.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub CreatePackage (connection)

         On Error Resume Next

         ' Create a package object.
         Set package = connection.Get("SMS_Package").SpawnInstance_()

<!-- p.115 -->

      If Err.Number<>0 Then
          Wscript.Echo "Couldn't create packages object"
          Exit Sub
      End If

      ' Populate the object.
      package.Name = "Test Package"
      package.Description = "A test package"
      package.PkgSourceFlag = 2
      package.PkgSourcePath = "C:\temp"

      package.Put_

      If Err.Number<>0 Then
          Wscript.Echo "Couldn't commit the package"
          Exit Sub
      End If

      WScript.Echo "Package created"
  End Sub

This example method has the following parameters:

                                                                         ﾉ     Expand table

 Parameter      Type                 Description

 Connection     SWBemServices        A valid connection to the SMS Provider.

Compiling the Code

See Also
Windows Management Instrumentation
Objects overview How to Call a Configuration Manager Object Class Method by Using
WMI
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Delete a Configuration Manager Object by Using WMI
How to Modify a Configuration Manager Object by Using WMI
How to Perform an Asynchronous Configuration Manager Query by Using WMI
How to Perform a Synchronous Configuration Manager Query by Using WMI
How to Read a Configuration Manager Object by Using WMI
How to Read Lazy Properties by Using WMI

<!-- p.116 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.117 -->

How to Read a Configuration Manager
Object by Using WMI
Article • 10/10/2022

In Configuration Manager, you read a Configuration Manager object by using the
SWbemServices object Get method to return an object instance that is identified by a
key value.

  ７ Note

  To query for multiple objects, use either a synchronous or asynchronous query. For
  more information, see How to Perform a Synchronous Configuration Manager
  Query by Using Managed Code

To read a Configuration Manager object
   1. Set up a connection to the SMS Provider. For more information, see How to
        Connect to an SMS Provider in Configuration Manager by Using WMI.

   2. Using the SWbemServices object that you obtain from step 1, call the Get method
        and specify the class and key information for the object you want.

Example
The following VBScript code example function displays the name and description for a
supplied key package identifier ( packageID ).

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DisplayPackageName (connection, packageID)

         On Error Resume Next
         Dim package

         Set package = connection.Get("SMS_Package.PackageID='" & packageID &
  "'")
         If Err.Number<>0 Then
             Wscript.Echo "Couldn't get package " + packageID
             Exit Sub

<!-- p.118 -->

       End If

       Wscript.Echo "Package Name: " + package.Name
       Wscript.Echo "Package Description: " + package.Description

  End Sub

This example method has the following parameters:

                                                                                 ﾉ   Expand table

 Parameter      Type               Description

 connection     SWbemServices      A valid connection to the SMS Provider.

 packageID      String             A package identifier. This can be obtained from the SMS_Package
                                   class PackageID property.

See Also
Windows Management Instrumentation
Objects overview How to Call a Configuration Manager Object Class Method by Using
WMI
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create a Configuration Manager Object by Using WMI
How to Delete a Configuration Manager Object by Using WMI
How to Modify a Configuration Manager Object by Using WMI
How to Perform an Asynchronous Configuration Manager Query by Using WMI
How to Perform a Synchronous Configuration Manager Query by Using WMI
How to Read Lazy Properties by Using WMI

Feedback
Was this page helpful?      Yes       No

Provide product feedback

<!-- p.119 -->

How to Modify a Configuration
Manager Object by Using WMI
Article • 10/10/2022

You modify a Configuration Manager object, in Configuration Manager, by using the
object's SWbemObject object to change its properties.

To modify a Configuration Manager object
   1. Set up a connection to the SMS Provider. For more information, see How to
        Connect to an SMS Provider in Configuration Manager by Using WMI.

   2. Using the SWbemServices object you obtain from step one, call the Get method
        and specify the class and key information for the object you want. This returns a
        SWbemObject representing object.

   3. Using the SWbemObject, update the object properties.

   4. Call Put_ to update the object in the SMS Provider.

Example
The following VBScript code example gets a package (SMS_Package) object, changes the
package description, and then commits the changes back to the SMS Provider. In this
example, the package is retrieved through a call to the SWbemServices object Get. You
can also retrieve the package by using a query. For more information, see How to
Perform a Synchronous Configuration Manager Query by Using WMI.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ModifyPackageDescription (connection, packageID, description)

         On Error Resume Next
         Dim package

         ' Get the package.
         Set package = connection.Get("SMS_Package.PackageID='" & packageID &
  "'")
         If Err.Number<>0 Then
             Wscript.Echo "Couldn't get package " + packageID

<!-- p.120 -->

          Exit Sub
      End If

      Wscript.Echo "Package Name: " + package.Name
      Wscript.Echo "Current Description: " + package.Description

      ' Update and commit the package.
      package.Description = description

      package.Put_
      If Err.Number<>0 Then
          WScript.Echo "Couldn't commit the package"
          Exit Sub
      End If

      Wscript.Echo "New Description: " + package.Description
  End Sub

This example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter     Type            Description

 connection    SWbemServices   A valid connection to the SMS Provider.

 packageID     String          The package identifier. This is available from the SMS_Package
                               class PackageID identifier.

 Description   String          A new description for the object.

See Also
Windows Management Instrumentation
Objects overview How to Call a Configuration Manager Object Class Method by Using
WMI
How to Connect to an SMS Provider in Configuration Manager by Using WMI
How to Create a Configuration Manager Object by Using WMI
How to Delete a Configuration Manager Object by Using WMI
How to Perform an Asynchronous Configuration Manager Query by Using WMI
How to Perform a Synchronous Configuration Manager Query by Using WMI
How to Read a Configuration Manager Object by Using WMI
How to Read Lazy Properties by Using WMI
