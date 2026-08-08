---
title: "Configuration Manager SDK documentation — pages 1441-1480"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1441-1480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1441-1480
family: sccm
documentKind: "doc"
abstract: "Was this page helpful?  Yes  No Provide product feedback How to Enable or Disable the Software Updates Client Agent Article • 10/04/2022 You enable or disable the Software Updates Client Agent, in Configuration Manager, by modifying the site control file settings. To enable or"
---

# Configuration Manager SDK documentation — pages 1441-1480

<!-- p.1441 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1442 -->

How to Enable or Disable the Software
Updates Client Agent
Article • 10/04/2022

You enable or disable the Software Updates Client Agent, in Configuration Manager, by
modifying the site control file settings.

To enable or disable the Software Updates Client Agent
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Software Updates Client Agent section of the site control
        file by using the SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example method enables or disables the Software Updates Client Agent
by using the SMS_SCI_ClientComp class to connect to the site control file and change
properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub EnableDisableSUMClientAgent(swbemServices,     _
                                  swbemContext,      _
                                  enableDisableFlag, _
                                  siteToChange )

      ' Load site control file and get software updates client component
  section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteToChange & """", "Refresh", , , swbemContext
      Set objSWbemInst =
  swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
  Component',Sitecode='" & siteToChange & "',ItemName='Software Updates'", ,
  swbemContext)

<!-- p.1443 -->

    ' Display the Software Updates Client Agent settings before changing the
properties.
    Wscript.Echo " "
    Wscript.Echo "Properties - Before Change"
    Wscript.Echo "---------------------------"
    Wscript.Echo objSWbemInst.ClientComponentName
    Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

    ' Set Software Updates Client Agent by setting Flags value to 0 or 1 by
using the enableDisableFlag variable.
    objSWbemInst.Flags = enableDisableFlag

    ' Save new Software Updates Client Agent settings.
    objSWbemInst.Put_ , swbemContext
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Commit", , , swbemContext

    ' Refresh in-memory copy of the site control file and get the software
updates client component section.
    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteToChange & """", "Refresh", , , swbemContext
    Set objSWbemInst =
swbemServices.Get("SMS_SCI_ClientComp.Filetype=1,Itemtype='Client
Component',Sitecode='" & siteToChange & "',ItemName='Software Updates'", ,
swbemContext)

    ' Display the Software Updates Client Agent settings after changing the
properties.
    Wscript.Echo " "
    Wscript.Echo "Properties - After Change"
    Wscript.Echo "---------------------------"
    Wscript.Echo objSWbemInst.ClientComponentName
    Wscript.Echo objSWbemInst.Flags & " (0 = Disabled, 1 = Enabled)"

End Sub

c#

public void EnableDisableSUMClientAgent(WqlConnectionManager connection,
                                        string enableDisableFlag,
                                        string siteCode)
{
    try
    {
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
Component',SiteCode='" + siteCode + "',ItemName='Software Updates'");

        // Display Software Updates Client Agent settings before changing
the properties.
        Console.WriteLine();

<!-- p.1444 -->

              Console.WriteLine("Properties - Before Change");
              Console.WriteLine("---------------------------");

  Console.WriteLine(siteDefinition["ClientComponentName"].StringValue);
          Console.WriteLine(siteDefinition["Flags"].StringValue + " (0 =
  Disabled, 1 = Enabled)");

          // Set Software Updates Client Agent by setting "Flags" value to 0
  or 1 by using the enableDisableFlag variable.
          siteDefinition["Flags"].StringValue = enableDisableFlag;

              // Save the settings.
              siteDefinition.Put();

          // Verify the change by reconnecting and getting the value again.
          IResultObject siteDefinition2 =
  connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client
  Component',SiteCode='" + siteCode + "',ItemName='Software Updates'");

          // Display Software Updates Client Agent settings after changing the
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

 Parameter           Type                       Description

 connection          - Managed:                 A valid connection to the SMS Provider.
                      WqlConnectionManager
                     - VBScript:
                     SWbemServices

 swbemContext        - VBScript: SWbemContext   A valid context object. For more information,
                                                see How to Add a Configuration Manager

<!-- p.1445 -->

 Parameter           Type                  Description

                                           Context Qualifier by Using WMI.

 siteCode            - Managed: String     The site code.

 siteToChange        - VBScript: String    The site code.

 enableDisableFlag   - Managed: String     Determines whether the Software Updates
                     - VBScript: String    Client Agent is enabled or disabled.

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

<!-- p.1446 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About Software Updates Setup and Configuration
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
How to Add a Configuration Manager Context Qualifier by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1447 -->

How to Set Software Updates Branding
Information
Article • 10/10/2022

You set the Software Updates client branding information, in Configuration Manager, by
modifying the necessary site control file settings.

To set software updates client branding information
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the Client Agent section of the site control file by using the
        SMS_SCI_ClientComp class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the changes to the site control file.

Example
The following example sets the Software Updates client branding information by using
the SMS_SCI_ClientComp class to connect to the site control file and change properties.
This example changes the Software Updates subheading information displayed in the
client user interface in notifications or reminders.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub SetSUMBranding(swbemServices,                    _
                     swbemContext,                     _
                     siteCode,                         _
                     brandingText)

      ' Load site control file and get the client agent section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_ClientComp " & _
                 "WHERE ClientComponentName = 'Client Agent' " & _
                 "AND SiteCode = '" & siteCode & "'"

<!-- p.1448 -->

    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

     ' Only one instance is returned from the query.
     For Each SCIComponent In SCIComponentSet

          ' Loop through the array of embedded SMS_EmbeddedProperty instances.
          For Each vProperty In SCIComponent.Props

                 ' Setting: SUMBrandingSubTitle
                 If vProperty.PropertyName = "SUMBrandingSubTitle" Then
                     wscript.echo " "
                     wscript.echo vProperty.PropertyName
                     wscript.echo "Current value " & vProperty.Value1

                     ' Modify the value.
                     vProperty.Value1 = brandingText
                     wscript.echo "New value: " & brandingText
                 End If

          Next

                  ' Update the component in your copy of the site control file.
Get the path
                  ' to the updated object, which could be used later to retrieve
the instance.
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

c#

public void SetSUMClientBranding(WqlConnectionManager connection,
                                 string siteCode,
                                 string brandingText)
{
    try
    {
        // Get the site control file client component section.
        IResultObject clientAgent =
connection.GetInstance(@"SMS_SCI_ClientComp.FileType=1,ItemType='Client

<!-- p.1449 -->

  Component',SiteCode='" + siteCode + "',ItemName='Client Agent'");

          // Load the embedded properties into a temporary copy.
          Dictionary<string, IResultObject> tempEmbeddedProperties =
  clientAgent.EmbeddedProperties;

              // Update the branding information with the string variable passed
  in.
          tempEmbeddedProperties["SUMBrandingSubTitle"]["Value1"].StringValue
  = brandingText;

              // Replace the embedded properties object with the temporary copy.
              clientAgent.EmbeddedProperties = tempEmbeddedProperties;

              // Commit the change back to the site control file.
              clientAgent.Put();
        }
        catch (SmsException e)
        {
            Console.WriteLine("Failed to set branding text: " + e.Message);
            throw;
        }
  }

The example method has the following parameters:

                                                                                ﾉ    Expand table

 Parameter       Type                       Description

 connection      - Managed:                 A valid connection to the SMS Provider.
                  WqlConnectionManager
                 - VBScript:
                 SWbemServices

 swbemContext    - VBScript: SWbemContext   A valid context object. For more information, see
                                            How to Add a Configuration Manager Context
                                            Qualifier by Using WMI.

 siteCode        - Managed: String          The site code.
                 - VBScript: String

 brandingText    - Managed: String          The text to replace the branding text in the site
                 - VBScript: String         control file.

Compiling the Code
This C# example requires:

<!-- p.1450 -->

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
About Software Updates Setup and Configuration
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class
How to Add a Configuration Manager Context Qualifier by Using WMI

Feedback

<!-- p.1451 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1452 -->

About Software Updates Deployments
Article • 10/04/2022

Software updates are delivered to client computers in Configuration Manager by
creating software update deployments. It is a multistep process to create software
update deployments by using the Configuration Manager SDK interfaces. A basic
approach to deploying software updates, by using the Configuration Manager SDK
interfaces, is outlined below.

For more information about software updates, see Deploy and manage software
updates.

  ７ Note

  Deleting updates or update bundles is not supported by the Configuration
  Manager SDK.

Select which software updates to install.
This can be something such as running a query to identify which updates should be
installed.

For information about queries that use criteria, such as selecting software updates for a
specific knowledge base article, or selecting software updates that are a specific severity
level, see How to Enumerate Updates Matching a Specific Criteria.

Obtain the configuration item identification (CI_ID) values.
The CI_ID value identifies the software updates information across several classes. For
the purposes of using the Configuration Manager SDK interfaces, the CI_ID value is vital.

The CI_ID value is a property of several classes and can be readily identified by using the
SMS_SoftwareUpdate class.

For more information about a number of queries that include the CI_ID, see How to
Enumerate Updates Matching a Specific Criteria.

Download the software update content.
Software update content must be downloaded manually. To identify which contents
must be downloaded, query the SMS_CIToContent class and obtain the list of ContentID
properties that match the specific language criteria. After you have the list of ContentID
properties, you can obtain the associated download URL and the related properties for

<!-- p.1453 -->

the content files from the SMS_CIContentFiles class by using the ContentID properties
you obtained earlier.

Create a software updates deployment package.
The software updates deployment package holds the software updates content. For
information about creating a deployment package, see How to Create a Deployment
Package.

Add update content to the software updates package.
After a software updates deployment package has been created, software updates
contents can be added to the package by using the AddUpdateContent method in the
SMS_SoftwareUpdatesPackage class. For information about adding software updates
content to a deployment package, see How to Add Updates to a Deployment Package.

Create a software updates deployment to distribute the software updates.
Distribute software updates by creating a software updates deployment. For information
about the process for creating a software updates deployment, see How to Configure
and Deploy Updates.

See Also
How to Enumerate Updates Matching a Specific Criteria
How to Create an Update List
How to Create a Deployment Package
How to Add Updates to a Deployment Package
How to Delete Updates from a Deployment Package
How to Configure and Deploy Updates

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1454 -->

How to Enumerate Updates Matching a
Specific Criteria
Article • 10/04/2022

This topic explains how to enumerate software updates that match specific criteria in
Configuration Manager by building a query and then using the ExecuteQuery method of
the QueryProcessor class to run the query.

To enumerate updates matching a specific criteria
   1. Set up a connection to the SMS Provider.

   2. Assign a specific query to a variable.

   3. Pass the variable to the ExecuteQuery method.

Example
The following example method enumerates updates that match specific criteria by
passing a query to the ExecuteQuery method.

Four example queries are demonstrated below:

   1. A query that displays the software updates that have already been downloaded.

   2. A query that displays the software updates that have already been deployed.

   3. A query that displays the software updates that have a particular severity value.

   4. A query that displays the software update CI_IDs that are associated with a specific
        knowledge base article.

        Detailed information about the properties that are associated with a software
        update is in the SMS_SoftwareUpdate class reference material.

        For information about calling the sample code, see Calling Configuration Manager
        Code Snippets.

  vbs

  Sub EnumerateUpdatesMatchingCriteria(connection)

<!-- p.1455 -->

    ' This query displays all updates that have already been downloaded.
    Query1 = "Select * from SMS_SoftwareUpdate where IsContentProvisioned=1"

    ' Run query.
    Set ListOfResources1 = connection.ExecQuery(Query1, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

    ' The query returns a collection that needs to be enumerated.
    Wscript.Echo " "
    Wscript.Echo "Update Content Is Downloaded."
    Wscript.Echo "Query: " & Query1
    Wscript.Echo "--------------------------------------------------------"

    For Each Resource1 In ListOfResources1
        Wscript.Echo "Name:       " & Resource1.LocalizedDisplayName
        Wscript.Echo "ArticleID: " & Resource1.ArticleID
        Wscript.Echo "CI_ID:      " & Resource1.CI_ID
        Wscript.Echo "Severity:   " & Resource1.SeverityName
    Next

    ' This query displays the updates that have already been deployed.
    Query2 = "Select * from SMS_SoftwareUpdate where IsDeployed=1"

    ' Run query.
    Set ListOfResources2 = connection.ExecQuery(Query2, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

    ' The query returns a collection that needs to be enumerated.
    Wscript.Echo " "
    Wscript.Echo "Updates Have Already Been Deployed."
    Wscript.Echo "Query: " & Query2
    Wscript.Echo "--------------------------------------------------------"

    For Each Resource2 In ListOfResources2
        Wscript.Echo "Name:       " & Resource2.LocalizedDisplayName
        Wscript.Echo "ArticleID: " & Resource2.ArticleID
        Wscript.Echo "CI_ID:      " & Resource2.CI_ID
        Wscript.Echo "Severity:   " & Resource2.SeverityName
    Next

    ' This query displays the updates that have a particular severity value.
    Query3 = "Select * from SMS_SoftwareUpdate where
SeverityName='Critical'"

    ' Run query.
    Set ListOfResources3 = connection.ExecQuery(Query3, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

    ' The query returns a collection that needs to be enumerated.
    Wscript.Echo " "
    Wscript.Echo "Updates That Have A Particular Severity Title."
    Wscript.Echo "Query: " & Query3
    Wscript.Echo "--------------------------------------------------------"

    For Each Resource3 In ListOfResources3

<!-- p.1456 -->

         Wscript.Echo "Name:        " & Resource3.LocalizedDisplayName
         Wscript.Echo "ArticleID:   " & Resource3.ArticleID
         Wscript.Echo "CI_ID:       " & Resource3.CI_ID
         Wscript.Echo "Severity:    " & Resource3.SeverityName
     Next

       ' This query displays software updates associated with a specific
knowledge base artile.
    Query4 = "SELECT * FROM SMS_SoftwareUpdate WHERE ArticleID='832880'"

    ' Run query.
    Set ListOfResources4 = connection.ExecQuery(Query4, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

     ' The query returns a collection that needs to be enumerated.
     Wscript.Echo " "
     Wscript.Echo "Updates For A Specific KB Article."
     Wscript.Echo "Query: " & Query4
     Wscript.Echo "--------------------------------------------------------"

     For Each Resource4 In ListOfResources4
         Wscript.Echo "Name:       " & Resource4.LocalizedDisplayName
         Wscript.Echo "ArticleID: " & Resource4.ArticleID
         Wscript.Echo "CI_ID:      " & Resource4.CI_ID
         Wscript.Echo "Severity:   " & Resource4.SeverityName
     Next

End Sub

c#

public void EnumerateUpdatesMatchingCriteria(WqlConnectionManager
connection)
{

    // Note: Query strings or variables could easily be passed in to
complete the strings, but the query string
    //         must be contructed and variables resolved prior to passing
the string to the ExecuteQuery method.

     try
     {

        // This query displays all updates that have already been
downloaded.
        string query1 = "Select * from SMS_SoftwareUpdate where
IsContentProvisioned=1";

        // Run query.
        IResultObject listOfResources1 =
connection.QueryProcessor.ExecuteQuery(query1);

<!-- p.1457 -->

        // The query returns a collection that needs to be enumerated.
        Console.WriteLine(" ");
        Console.WriteLine("Update Content Is Downloaded.");
        Console.WriteLine("Query: " + query1);
        Console.WriteLine("-------------------------------------------------
-------");
        foreach (IResultObject resource1 in listOfResources1)
        {
            Console.WriteLine();
            Console.WriteLine("Name:       " +
resource1["LocalizedDisplayName"].StringValue);
            Console.WriteLine("Article ID: " +
resource1["ArticleID"].StringValue);
            Console.WriteLine("CI_ID:      " +
resource1["CI_ID"].IntegerValue);
            Console.WriteLine("Severity    " +
resource1["SeverityName"].StringValue);
        }

        // This query displays the updates that have already been deployed.
        string query2 = "Select * from SMS_SoftwareUpdate where
IsDeployed=1";

        // Run query.
        IResultObject listOfResources2 =
connection.QueryProcessor.ExecuteQuery(query2);

        // The query returns a collection that needs to be enumerated.
        Console.WriteLine(" ");
        Console.WriteLine("Updates Have Already Been Deployed.");
        Console.WriteLine("Assignments Query: " + query2);
        Console.WriteLine("-------------------------------------------------
-------");
        foreach (IResultObject resource2 in listOfResources2)
        {
            Console.WriteLine();
            Console.WriteLine("Name:       " +
resource2["LocalizedDisplayName"].StringValue);
            Console.WriteLine("Article ID: " +
resource2["ArticleID"].StringValue);
            Console.WriteLine("CI_ID:      " +
resource2["CI_ID"].IntegerValue);
            Console.WriteLine("Severity:   " +
resource2["SeverityName"].StringValue);
        }

         // This query displays the updates that have a particular severity
value.
        string query3 = "Select * from SMS_SoftwareUpdate where
SeverityName='Critical'";

        // Run query.
        IResultObject listOfResources3 =
connection.QueryProcessor.ExecuteQuery(query3);

<!-- p.1458 -->

        // The query returns a collection that needs to be enumerated.
        Console.WriteLine(" ");
        Console.WriteLine("Updates That Have A Particular Severity Title.");
        Console.WriteLine("Query: " + query3);
        Console.WriteLine("-------------------------------------------------
-------");
        foreach (IResultObject resource3 in listOfResources3)
        {
            Console.WriteLine();
            Console.WriteLine("Name:       " +
resource3["LocalizedDisplayName"].StringValue);
            Console.WriteLine("Article ID: " +
resource3["ArticleID"].StringValue);
            Console.WriteLine("CI_ID:      " +
resource3["CI_ID"].IntegerValue);
            Console.WriteLine("Severity:   " +
resource3["SeverityName"].StringValue);
        }

         // This query displays software updates associated with a specific
KB.
        string query4 = "SELECT * FROM SMS_SoftwareUpdate WHERE
ArticleID='832880'";

        // Run query.
        IResultObject listOfResources4 =
connection.QueryProcessor.ExecuteQuery(query4);

        // The query returns a collection that needs to be enumerated.
        Console.WriteLine(" ");
        Console.WriteLine("Updates For A Specific KB Article.");
        Console.WriteLine("Query: " + query4);
        Console.WriteLine("-------------------------------------------------
-------");
        foreach (IResultObject resource4 in listOfResources4)
        {
            Console.WriteLine();
            Console.WriteLine("Name:       " +
resource4["LocalizedDisplayName"].StringValue);
            Console.WriteLine("Article ID: " +
resource4["ArticleID"].StringValue);
            Console.WriteLine("CI_ID:      " +
resource4["CI_ID"].IntegerValue);
            Console.WriteLine("Severity:   " +
resource4["SeverityName"].StringValue);
        }
    }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to run queries. Error: " + ex.Message);
          throw;
      }

<!-- p.1459 -->

  }

The example method has the following parameters:

                                                                         ﾉ   Expand table

 Parameter    Type                              Description

 connection   - Managed: WqlConnectionManager   A valid connection to the SMS Provider.
              - VBScript: SWbemServices

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

<!-- p.1460 -->

See also
About software update deployments

SMS_SoftwareUpdate

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1461 -->

How to Create an Update List
Article • 10/04/2022

You create an update list that contains a set of software updates, in Configuration
Manager, by creating an instance of the SMS_AuthorizationList class and populating the
properties.

To create an update list
   1. Set up a connection to the SMS Provider.

   2. Create the new update list object using the SMS_AuthorizationList class.

   3. Populate the new update list properties.

   4. Save the new update list and properties.

Example
The following example method shows how to create an update list that contains a set of
software updates by creating an instance of the SMS_AuthorizationList class and
populating the properties.

  ） Important

  The LocalizedInformation property that is used in this example requires an object
  array (embedded array) of the description information.

In the example, the LocaleID property is hard-coded to English (U.S.). If you need the
locale for non-U.S. installations, you can get it from the SMS_Identification Server WMI
Class LocaleID property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

The following example shows the subroutine call in Visual Basic:

  Visual Basic Script

  ' Prework for CreateSUMUpdateList
  ' Create the array of CI_IDs.

<!-- p.1462 -->

  dim newUpdates
  newUpdates = Array(9)

  ' Create and populate an SMS_CI_LocalizedProperties object.
  set SMSCILocalizedProperties =
  swbemservices.Get("SMS_CI_LocalizedProperties").SpawnInstance_

  SMSCILocalizedProperties.Description = "Test Description"
  SMSCILocalizedProperties.DisplayName = "Test Display Name"
  SMSCILocalizedProperties.InformativeURL = "Test URL"
  SMSCILocalizedProperties.LocaleID = "1033"

  ' Create an array to hold the SMS_CI_LocalizedProperties object.
  dim newDescriptionInfo
  newDescriptionInfo = Array(SMSCILocalizedProperties)

  ' Call the CreateSUMUpdateList method.
  Call CreateSUMUpdateList(swbemServices,            _
                           newUpdates,               _
                           newDescriptionInfo)

The following example shows the method call in C#:

  C#

  // Prework for CreateSUMUpdateList
  // Create array list (to hold the array of Localized Properties).
  List<IResultObject> newDescriptionInfo = new List <IResultObject>();
  IResultObject SMSCILocalizedProperties =
  WMIConnection.CreateEmbeddedObjectInstance("SMS_CI_LocalizedProperties");

  // Populate the initial array values (this could be a loop to added more
  localized info).
  SMSCILocalizedProperties["Description"].StringValue = "4 CI_IDs - 9,34,53,72
  ";
  SMSCILocalizedProperties["DisplayName"].StringValue = "Test Display Name";
  SMSCILocalizedProperties["InformativeURL"].StringValue = "Test URL";
  SMSCILocalizedProperties["LocaleID"].StringValue = "1033";

  // Add the 'embedded properties' to newDescriptionInfo.
  newDescriptionInfo.Add(SMSCILocalizedProperties);

  // Create the array of CI_IDs.
  int[] newCI_ID = new int[] { 9, 34, 53, 72 };

  // Call the CreateSUMUpdateList method.
  SUMSnippets.CreateSUMUpdateList(WMIConnection,
                                  newCI_ID,
                                  newDescriptionInfo);

<!-- p.1463 -->

Visual Basic Script

Sub CreateSUMUpdateList(connection,         _
                        newUpdates,         _
                        newDescriptionInfo)

    ' Create the new UpdateList object.
    Set newUpdateList =
connection.Get("SMS_AuthorizationList").SpawnInstance_

    ' Populate the UpdateList properties.
    ' Updates is an int32 array that maps to the CI_ID in
SMS_SoftwareUpdate.
    newUpdateList.Updates = newUpdates
    ' Need to pass embedded properties (LocalizedInformation) here.
    newUpdateList.LocalizedInformation = newDescriptionInfo

     ' Save the new UpdateList and properties.
     newUpdateList.Put_

     ' Output the new UpdateList name.
     Wscript.Echo "Created Update List " & newUpdateList.LocalizedDisplayName

End Sub

C#

public void CreateSUMUpdateList(WqlConnectionManager connection,
                                 int [] newUpdates,
                                 List<IResultObject> newDescriptionInfo)
{
    try
    {
        // Create the new SMS_AuthorizationList object.
        IResultObject newUpdateList =
connection.CreateInstance("SMS_AuthorizationList");

        // Populate the new SMS_AuthorizationList object properties.
        // Updates is an int32 array that maps to the CI_ID in
SMS_SoftwareUpdate.
        newUpdateList["Updates"].IntegerArrayValue = newUpdates;
        // Pass embedded properties (LocalizedInformation) here.
        newUpdateList.SetArrayItems("LocalizedInformation",
newDescriptionInfo);

           // Save changes.
           newUpdateList.Put();

           Console.WriteLine();
           Console.WriteLine("Created Update List. " );

<!-- p.1464 -->

      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create update list. Error: " +
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                              ﾉ   Expand table

 Parameter            Type                        Description

 Connection           - Managed:                  A valid connection to the SMS Provider.
                      WqlConnectionManager
                      - VBScript: SWbemServices

 newUpdates           - Managed: Integer array    An array of the updates that is associated
                      - VBScript: Integer array   with the Update List.

 newDescriptionInfo   - Managed: Object array     An object array (embedded properties) of the
                      - VBScript: Object array    type LocalizedInformation .

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

<!-- p.1465 -->

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See also
About software update deployments SMS_AuthorizationList

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1466 -->

How to Create a Deployment Template
Article • 10/04/2022

You create a software updates deployment template, in Configuration Manager, by
creating an instance of the SMS_Template class and populating the properties.

To create a deployment template
   1. Set up a connection to the SMS Provider.

   2. Create the new template object by using the SMS_Template class.

   3. Populate the new template properties.

   4. Save the new template and properties.

Example
The following example method shows how to create a software updates deployment
template by using the SMS_Template class and class properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  ７ Note

  In the following code examples, the template settings are passed into the method
  by using a string variable called deploymentTemplateSettings. The template
  settings are stored in an XML structure.

VB Template Setting Example (one long string):

  XML

  deploymentTemplateSettings = "<TemplateDescription
  xmlns:xsi=""http://www.w3.org/2001/XMLSchema-instance""
  xmlns:xsd=""http://www.w3.org/2001/XMLSchema"">
  <CollectionId>SMS00001</CollectionId> <IncludeSub>true</IncludeSub>
  <AttendedInstall>true</AttendedInstall> <UTC>true</UTC>
  <Duration>2</Duration> <DurationUnits>Weeks</DurationUnits>
  <SuppressServers>Unchecked</SuppressServers>
  <SuppressWorkstations>Unchecked</SuppressWorkstations>
  <AllowRestart>false</AllowRestart> <Deploy2003>true</Deploy2003>

<!-- p.1467 -->

  <CollectImmediately>false</CollectImmediately>
  <LocalDPOption>DownloadAndInstall</LocalDPOption>
  <RemoteDPOption>DownloadAndInstall</RemoteDPOption>
  <DisableMomAlert>false</DisableMomAlert>
  <GenerateMomAlert>false</GenerateMomAlert> <UseRemoteDP>false</UseRemoteDP>
  <UseUnprotectedDP>false</UseUnprotectedDP> </TemplateDescription>"

C# Template Setting Example (the same template settings and still passed as a string,
but the XML structure is more obvious):

  XML

  string deploymentTemplateSettings =
    @"<TemplateDescription xmlns:xsi=""http://www.w3.org/2001/XMLSchema-
  instance"" xmlns:xsd=""http://www.w3.org/2001/XMLSchema"">
    <CollectionId>SMS00001</CollectionId>
    <IncludeSub>true</IncludeSub>
    <AttendedInstall>true</AttendedInstall>
    <UTC>true</UTC>
    <Duration>2</Duration>
    <DurationUnits>Weeks</DurationUnits>
    <SuppressServers>Unchecked</SuppressServers>
    <SuppressWorkstations>Unchecked</SuppressWorkstations>
    <AllowRestart>false</AllowRestart>
    <Deploy2003>true</Deploy2003>
    <CollectImmediately>false</CollectImmediately>
    <LocalDPOption>DownloadAndInstall</LocalDPOption>
    <RemoteDPOption>DownloadAndInstall</RemoteDPOption>
    <DisableMomAlert>false</DisableMomAlert>
    <GenerateMomAlert>false</GenerateMomAlert>
    <UseRemoteDP>false</UseRemoteDP>
    <UseUnprotectedDP>false</UseUnprotectedDP>
    </TemplateDescription>";

  vbs

  Sub CreateSUMDeploymentTemplate(connection,             _
                                   newTemplateName,         _
                                   newTemplateDescription, _
                                   newTemplateSettings,     _
                                   newTemplateType)

        ' Create the new Template object.
        Set newSUMTemplate = connection.Get("SMS_Template").SpawnInstance_

        ' Populate the SMS_Template properties.
        ' Note: The template name (newTemplateName) must be unique.
        newSUMTemplate.Name = newTemplateName
        newSUMTemplate.Description = newTemplateDescription
        newSUMTemplate.Data = newTemplateSettings
        newSUMTemplate.Type = newTemplateType

<!-- p.1468 -->

       ' Save the new template and properties.
       newSUMTemplate.Put_

       ' Output the new template name.
       Wscript.Echo "Created new template: " & newTemplateName

   End Sub

  c#

  public void CreateSUMDeploymentTemplate(WqlConnectionManager connection,
                                          string newTemplateName,
                                          string newTemplateDescription,
                                          string newTemplateSettings,
                                          int newTemplateType)
  {
      try
      {
          // Create the template object.
          IResultObject newSUMTemplate =
  connection.CreateInstance("SMS_Template");

           // Populate the new template properties.
           // Note: The template name (newTemplateName) must be unique.
           newSUMTemplate["Name"].StringValue = newTemplateName;
           newSUMTemplate["Description"].StringValue = newTemplateDescription;
           newSUMTemplate["Data"].StringValue = newTemplateSettings;
           newSUMTemplate["Type"].IntegerValue = newTemplateType;

           // Save the new template and the new template properties.
           newSUMTemplate.Put();

           // Output the new template name.
           Console.WriteLine("Created template: " + newTemplateName);
       }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create template. Error: " +
  ex.Message);
          throw;
      }
  }

This example method has the following parameters:

                                                                  ﾉ     Expand table

<!-- p.1469 -->

Parameter                Type                   Description

connection               - Managed:             A valid connection to the SMS Provider.
                         WqlConnectionManager
                         - VBScript:
                         SWbemServices

newTemplateName          - Managed: String      The new template name. The template name
                         - VBScript: String     must be unique.

newTemplateDescription   - Managed: String      The description for the new template.
                         - VBScript: String

newTemplateSettings      - Managed: String      The new template settings. The settings are
                         - VBScript: String     in an XML structure, stored as a string.

                                                      CollectionId

                                                      The collection for the software update
                                                      deployment.

                                                         A valid collection ID.
                                                      IncludeSub

                                                      Include members of subcollections.

                                                          true
                                                          false
                                                      AttendedInstall

                                                      Display software update notifications
                                                      on clients (false will suppress
                                                      notifications).

                                                          true
                                                          false
                                                      UTC

                                                      Use Coordinated Universal Time (UTC)
                                                      instead of client local time.

                                                          true
                                                          false
                                                      Duration

                                                      Duration of the deployment.

                                                         1-24 (hours)
                                                         1-365 (days)

<!-- p.1470 -->

Parameter   Type   Description

                           1-4 (weeks)
                           1-12 (months)
                        DurationUnits

                        Duration units.

                           hours
                           days
                          weeks
                          months
                        SuppressServers

                        Suppress the system restart on servers.

                           Checked
                           Unchecked
                        SuppressWorkstations

                        Suppress the system restart on
                        workstations.

                           Checked
                           Unchecked
                        AllowRestart

                        Allow system restart outside of
                        maintenance windows (for both
                        servers and workstations).

                           true
                           false
                        Deploy2003

                        Deploy software updates to SMS 2003
                        clients.

                           true
                           false
                        CollectImmediately (SMS 2003 client
                        specific)

                        Collect hardware inventory
                        immediately after installing software
                        updates.

                           true
                           false

<!-- p.1471 -->

Parameter   Type   Description

                        LocalDPOption (SMS 2003 client
                        specific)

                        Specify whether to download the
                        update source files before running the
                        installation when a distribution point is
                        available locally.

                           DownloadAndInstall
                           InstallFromDP
                        RemoteDPOption (SMS 2003 client
                        specific)

                        Specify whether to download the
                        update source files before running the
                        installation when no distribution point
                        is available locally.

                           DownloadAndInstall
                           InstallFromDP
                        DisableMomAlert

                        Disable Operations Manager alerts
                        while software updates run.

                            true
                            false
                        GenerateMomAlert

                        Generate Operations Manager alert
                        when a software update installation
                        fails.

                            true
                            false
                        UseRemoteDP

                        Download software updates from use
                        a remote distribution point (even when
                        a client is connected within a slow or
                        unreliable network boundary).

                            true
                            false
                        UseUnprotectedDP

                        Download software updates from a

<!-- p.1472 -->

 Parameter              Type                  Description

                                                    unprotected distribution point (when
                                                    updates are not available from any
                                                    protected distribution point).

                                                       true
                                                       false

 newTemplateType        - Managed: Integer    The new template type. Currently the only
                        - VBScript: Integer   possible value is:

                                              - 0 (SUM_DEPLOYMENT)

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

<!-- p.1473 -->

For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About software update deployments How to Assign a Package to a Distribution Point
SMS_Template

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1474 -->

How to Create a Deployment Package
Article • 10/04/2022

You create a software updates deployment package, in Configuration Manager, by
creating an instance of the SMS_SoftwareUpdatesPackage class and populating the
properties.

To create a software updates deployment package
   1. Set up a connection to the SMS Provider.

   2. Create the new package object by using the SMS_SoftwareUpdatesPackage class.

   3. Populate the new package properties.

   4. Save the new package and properties.

Example
The following example method shows how to create a software updates deployment
package by using the SMS_SoftwareUpdatesPackage class and class properties.

  ７ Note

  The package location must be unique, and the updates must be available in the
  package source.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

Example of the subroutine call in Visual Basic:

  Visual Basic Script

  Call CreateSUMDeploymentPackage(swbemServices,                  _
                                  "New SUM Deployment Package",   _
                                  "New SUM Package Description", _
                                  2,                              _
                                  "\\ServerOne\SUM_TestPackageSource")

<!-- p.1475 -->

Example of the method call in C#:

  C#

  SUMSnippets.CreateSUMDeploymentPackage(WMIConnection,
                                         "New SUM Deployment Package",
                                         "New SUM Package Description",
                                         2,

  "\\\\ServerOne\\SUM_TestPackageSource");

  Visual Basic Script

  Sub CreateSUMDeploymentPackage(connection,                  _
                                 newPackageName,              _
                                 newPackageDescription,       _
                                 newPackageSourceFlag,        _
                                 newPackageSourcePath)

      ' Create the new SUM package object.
      Set newSUMDeploymentPackage =
  connection.Get("SMS_SoftwareUpdatesPackage").SpawnInstance_

        ' Populate the new SUM package properties.
        newSUMDeploymentPackage.Name = newPackageName
        newSUMDeploymentPackage.Description = newPackageDescription
        newSUMDeploymentPackage.PkgSourceFlag = newPackageSourceFlag
        newSUMDeploymentPackage.PkgSourcePath = newPackageSourcePath

        ' Save the new SUM package object and properties.
        newSUMDeploymentPackage.Put_

        ' Output the new SUM package name.
        Wscript.Echo "Created the new SUM Deployment Package: " & newPackageName

      End Sub

  C#

  public void CreateSUMDeploymentPackage(WqlConnectionManager connection,
                                         string newPackageName,
                                         string newPackageDescription,
                                         int newPackageSourceFlag,
                                         string newPackageSourcePath)

  {
        try

<!-- p.1476 -->

      {
          // Create the new SUM package object.
          IResultObject newSUMDeploymentPackage =
  connection.CreateInstance("SMS_SoftwareUpdatesPackage");

          // Populate the new SUM package properties.
          newSUMDeploymentPackage["Name"].StringValue = newPackageName;
          newSUMDeploymentPackage["Description"].StringValue =
  newPackageDescription;
          newSUMDeploymentPackage["PkgSourceFlag"].IntegerValue =
  newPackageSourceFlag;
          newSUMDeploymentPackage["PkgSourcePath"].StringValue =
  newPackageSourcePath;

              // Save the new SUM package and new package properties.
              newSUMDeploymentPackage.Put();

          // Output the new SUM package name.
          Console.WriteLine("Created the new SUM Deployment Package: " +
  newPackageName);
      }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to create the SUM Deployment Package.
  Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                          ﾉ   Expand table

 Parameter                         Type                   Description

 connection                        - Managed:             A valid connection to the SMS
                                   WqlConnectionManager   Provider.
                                   - VBScript:
                                   SWbemServices

 newDeploymentPackageName          - Managed: String      The new deployment package
                                   - VBScript: String     name.

 newDeploymentPackageDescription   - Managed: String      The description for the new
                                   - VBScript: String     deployment package.

 newPackageSourceFlag              - Managed: Integer     The new package source flag.
                                   - VBScript: Integer

<!-- p.1477 -->

 Parameter                     Type                    Description

 newPackageSourcePath          - Managed: String       The new package source path.
                               - VBScript: String
                                                       The package location must be
                                                       unique and the updates must be
                                                       available in the package source.

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

<!-- p.1478 -->

About software update deployments How to Assign a Package to a Distribution Point
SMS_SoftwareUpdatesPackage

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1479 -->

How to Add Updates to a Deployment
Package
Article • 10/04/2022

You add updates to a software updates deployment package, in Configuration Manager,
by obtaining an instance of the SMS_SoftwareUpdatesPackage class and by using the
AddUpdateContent method.

To create a software updates deployment package
   1. Set up a connection to the SMS Provider.

   2. Obtain an existing package object by using the SMS_SoftwareUpdatesPackage class.

   3. Add update content to the existing package using the AddUpdateContent method.

Example
The following example method shows how to add updates to a software updates
deployment package by using the SMS_SoftwareUpdatesPackage class and the
AddUpdateContent method.

  ７ Note

  The updates must be available in the content source path (as part of the dictionary
  object addUpdateContentParameters in C#). If the updates exist in a package source,
  that package source cannot be used for more than one deployment package.

  ） Important

  No VBScript example was included, as the AddUpdateContent method does not
  return from the method call on failure. This is a known issue and is being
  investigated.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

Example of the method call in C#:

<!-- p.1480 -->

C#

// PREWORK FOR AddUpdatesToSUMDeploymentPackage

// Define the array of Content Ids to load into addUpdateContentParameters.
int[] newArrayContentIds = new int[] { 82 };

// Define the array of source paths (these must be UNC) to load into
addUpdateContentParameters.
string[] newArrayContentSourcePath = new string[] { "\\\\ServerOne\\source1"
};

// Load the update content parameters into an object to pass to the method.
Dictionary<string, object> addUpdateContentParameters = new
Dictionary<string, object>();
addUpdateContentParameters.Add("ContentIds", newArrayContentIds);
addUpdateContentParameters.Add("ContentSourcePath",
newArrayContentSourcePath);
addUpdateContentParameters.Add("bRefreshDPs", false);

AddUpdatestoSUMDeploymentPackage(WMIConnection,
                                 "ABC00001",
                                 addUpdateContentParameters);

C#

public void AddUpdatestoSUMDeploymentPackage(WqlConnectionManager
connection,
                                            string existingSUMPackageID,
                                            Dictionary<string, object>
addUpdateContentParameters)
{
    try
    {
        // Get the specific SUM Deployment Package to change.
        IResultObject existingSUMDeploymentPackage =
connection.GetInstance(@"SMS_SoftwareUpdatesPackage.PackageID='" +
existingSUMPackageID + "'");

        // Add updates to the existing SUM Deployment Package using the
AddUpdateContent method.
        // Note: The method will throw an exception, if the method is not
able to add the content.
        existingSUMDeploymentPackage.ExecuteMethod("AddUpdateContent",
addUpdateContentParameters);

       // Output a success message that the content was added.
       Console.WriteLine("Added content to the SUM deployment package. ");
    }
    catch (SmsException ex)
    {
        Console.WriteLine("Failed to add content to the SUM deployment
package.");
