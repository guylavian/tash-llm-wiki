---
title: "Configuration Manager SDK documentation — pages 1521-1555"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1521-1555
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1521-1555
family: sccm
documentKind: "doc"
abstract: "Software Distribution Health You can determine the status of advertisements and packages by using the software distribution summarizers. Package Summarizers Package summarizers are used to track the progress of packages as they are moved to their assigned distribution points. Fo"
---

# Configuration Manager SDK documentation — pages 1521-1555

<!-- p.1521 -->

Software Distribution Health
You can determine the status of advertisements and packages by using the software
distribution summarizers.

Package Summarizers
Package summarizers are used to track the progress of packages as they are moved to
their assigned distribution points. For more information, see How to Determine Package
Status

Package status summaries track the state changes instead of counting the error
messages. For example, The package status summaries track items such as how many
clients have installed each package.

The package summarizer classes are:

                                                                             ﾉ    Expand table

 Summarizer                                 Description

 SMS_PackageStatusDetailSummarizer Server   Tracks the progress of each package as it places
 WMI Class                                  the software source files on its distribution point.
                                            The reported package status is for an individual
                                            site.

 SMS_PackageStatusDistPointsSummarizer      Tracks the progress of loading the package
 Server WMI Class                           source files on the distribution point. The
                                            reported package status is for an individual site.

 SMS_PackageStatusRootSummarizer Server     Tracks the progress of each package as it places
 WMI Class                                  the software source files on its distribution point.
                                            The reported package status is for all sites in the
                                            hierarchy.

See Also
About Configuration Manager Tally Intervals
How to Determine the Health of a Configuration Manager Site
How to Read The Tally Intervals For a Configuration Manager Site

Feedback

<!-- p.1522 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1523 -->

About Configuration Manager Tally
Intervals
Article • 10/04/2022

Configuration Manager is configured with 16 default tally intervals. The intervals for a
site are maintained in the site control file. The values are stored in the order that is
shown in the following table. For information about accessing these values in the site
control file, see the example at the end of this topic.

  ７ Note

  You can use only the tally intervals that are listed in the table in your queries. When
  you use a tally interval that is not from the list, an object is returned that contains
  no data.

                                                                             ﾉ   Expand table

 Schedule                    Tally Interval               Class

 Since 12:00AM               0001128000100008             SMS_ST_RecurInterval

 Since 04:00AM               0081128000100008             SMS_ST_RecurInterval

 Since 08:00AM               0101128000100008             SMS_ST_RecurInterval

 Since 12:00PM               0181128000100008             SMS_ST_RecurInterval

 Since 04:00PM               0201128000100008             SMS_ST_RecurInterval

 Since 08:00PM               0281128000100008             SMS_ST_RecurInterval

 Since Sunday                0001128000192000             SMS_ST_RecurWeekly

 Since Monday                00011280001A2000             SMS_ST_RecurWeekly

 Since Tuesday               00011280001B2000             SMS_ST_RecurWeekly

 Since Wednesday             00011280001C2000             SMS_ST_RecurWeekly

 Since Thursday              00011280001D2000             SMS_ST_RecurWeekly

 Since Friday                00011280001E2000             SMS_ST_RecurWeekly

 Since Saturday              00011280001F2000             SMS_ST_RecurWeekly

<!-- p.1524 -->

 Schedule                      Tally Interval           Class

 Since 1st of month            000A470000284400         SMS_ST_RecurMonthlyByDate

 Since 15th of month           000A4700002BC400         SMS_ST_NonRecurring

 Since site installation       0001128000080008         SMS_ST_NonRecurring

The Schedule column is the beginning value of the tally interval. You interpret the
beginning value of the tally interval as, "Give me the tallies since Monday." The end of
the tally interval is always the current time. The complete tally interval is the same as
saying, "Give me all the tallies from Monday to the current time."

The classes listed in the tally interval table are embedded schedule token classes that
you can use to interpret the interval string. You use the ReadFromString method of the
SMS_ScheduleMethods class to interpret an interval string. This method breaks the interval

string into its components and returns the appropriate embedded object.

Tally intervals are commonly used in component (SMS_ComponentSummarizer) and site
detail (SMS_SiteDetailSummarizer) summarizer queries. For more information, see About
Configuration Manager Status Summarizers.

See Also
About Configuration Manager Status Summarizers

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.1525 -->

How to Determine the Health of a
Configuration Manager Site
Article • 10/04/2022

You can determine the overall health or status of a site, in Configuration Manager, by
inspecting the SMS_SummarizerSiteStatus object Status property. The Status property
has three possible values:

                                                                        ﾉ   Expand table

 Value                   Description

 0                       The site is healthy.

 1                       The site has warning conditions.

 2                       The site has error conditions.

SMS_SummarizerSiteStatus is an example of a Configuration Manager summarizer. For

more information, see SMS_SummarizerSiteStatus server WMI class.

To determine a site's health
     1. Set up a connection to the SMS Provider. For more information, see SMS Provider
           fundamentals.

     2. Get the SMS_SummarizerSiteStatus object by using the Configuration Manager site
           code.

     3. Inspect the SMS_SummarizerSiteStatus object Status property to determine the
           site status

Example
The following example determines the health of the site code supplied in the parameter
siteCode .

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

     vbs

<!-- p.1526 -->

Sub ShowSiteHealth(connection, siteCode)

     Dim siteHealth
     Dim health

     On Error Resume Next

    ' Get the site status summarizer.
    Set siteHealth = connection.Get("SMS_SummarizerSiteStatus.SiteCode='" &
siteCode & "'")
    If Err.Number<>0 Then
        Wscript.Echo "Couldn't get site health"
        Exit Sub
    End If

     ' Display the site health.
     health="Health for site " + siteCode + " "

     Select Case siteHealth.Status
         Case 0
             heath = health + "is OK"
         Case 1
             health = health + "has warnings"
         Case 2
             health = health + "is critical"
         Case Else
             health = health + "is not known"
     End Select

    Wscript.Echo health
End Sub

c#

public void ShowSiteHealth(WqlConnectionManager connection, string siteCode)
{
    try
    {
        IResultObject siteHealth =
connection.GetInstance(@"SMS_SummarizerSiteStatus.SiteCode='" + siteCode +
"'");

        Console.Write("Health for site {0}", siteCode);
        switch (siteHealth["Status"].IntegerValue)
        {
            case 0:
                Console.WriteLine("is OK");
                break;
            case 1:
                Console.WriteLine("has warnings");
                break;
            case 2:

<!-- p.1527 -->

                    Console.WriteLine("is critical");
                    break;
                default:
                    Console.WriteLine("is not known");
                    break;
          }
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to show site status: " + e.Message);
      }
  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter    Type                        Description

 connection   - Managed:                  A valid connection to the SMS Provider. For more
              WqlConnectionManager        information, see SMS Provider fundamentals.
              - VBScript: SWbemServices

 siteCode     - Managed: String           A valid task Configuration Manager site code
              - VBScript: String

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

<!-- p.1528 -->

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About status messages

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1529 -->

How to Read the Tally Intervals for a
Configuration Manager Site
Article • 10/04/2022

In Configuration Manager, you can read the available tally intervals for a site by
inspecting the site control file SMS_COMPONENT_STATUS_SUMMARIZER object
Summary_Intervals embedded property list.

You use tally intervals for querying component ( SMS_ComponentSummarizer ) and site detail
( SMS_SiteDetailSummarizer ) summarizer classes. For more information, see About
Configuration Manager Status Summarizers.

To read the tally intervals for a site
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Perform a query for the site's SMS_COMPONENT_STATUS_SUMMARIZER property
        lists

   3. In the results from step two, search for the Summary_Intervals embedded property
        list.

   4. Display the contents of the embedded property list.

Example
The following example method returns a SMS_TaskSequence object after importing it
from the supplied XML.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ShowSiteTallyIntervals(connection, siteCode)

          Dim SCIComponent              'SMS_SCI_Component class
          Dim SCIComponentSet         'Enumeration of SMS_SCI_Component
          Dim query
          Dim i
          Dim vProperty                      'Embedded property

<!-- p.1530 -->

      query = "SELECT PropLists FROM SMS_SCI_Component " & _
              "WHERE ComponentName = 'SMS_COMPONENT_STATUS_SUMMARIZER' " & _
              "AND SiteCode = '" + siteCode + "'"

      ' You do not need to get a copy of the site control file just to read
it.
      Set SCIComponentSet = connection.ExecQuery(query)

    ' The query returns only one instance.
    For Each SCIComponent In SCIComponentSet
        For Each vProperty In SCIComponent.PropLists
             If vProperty.PropertyListName = "Summary_Intervals" Then
                 For i = 0 To UBound(vProperty.Values)
                      WScript.Echo vProperty.Values(i)
                 Next
             End If
        Next
    Next
 End Sub

c#

public void ShowSiteTallyIntervals(WqlConnectionManager connection, string
siteCode)
{
    try
    {
        // Query for the site's site control file
SMS_COMPONENT_STATUS_SUMMARIZER property lists.
        IResultObject query =
            connection.QueryProcessor.ExecuteQuery("SELECT PropLists FROM
SMS_SCI_Component " +
            "WHERE ComponentName = 'SMS_COMPONENT_STATUS_SUMMARIZER' " +
            "AND SiteCode = '" + siteCode + "'");

         foreach (IResultObject r in query)
         {
             // Get the summary intervals and display them.
           if (r.EmbeddedPropertyLists.ContainsKey("Summary_Intervals"))
             {

Console.WriteLine(r.EmbeddedPropertyLists["Summary_Intervals"]
["PropertyListName"].StringValue);
                foreach (string value in
r.EmbeddedPropertyLists["Summary_Intervals"]["Values"].StringArrayValue)
                {
                    Console.WriteLine(value);
                }
            }
            else
            {
                Console.WriteLine("Not found");

<!-- p.1531 -->

                         return;
                    }
              }
      }
      catch (SmsException e)
      {
          Console.WriteLine("Failed to tally intervals: " + e.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter        Type                        Description

 connection       - Managed:                  A valid connection to the SMS Provider. For more
                  WqlConnectionManager        information, see SMS Provider fundamentals.
                  - VBScript: SWbemServices

 siteCode         - Managed: String           A valid Configuration Manager site code.
                  - VBScript: String

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

<!-- p.1532 -->

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About status messages About Configuration Manager Tally Intervals
About Configuration Manager Status Summarizers

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1533 -->

How to Read User-Defined Status
Messages
Article • 10/04/2022

In Configuration Manager, you can read user-defined status messages, on the site
server, by querying the SMS Provider.

To read a user-defined status messages
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Query the provider for the SMS _StatusMessage instances you want. As part of the
        query get the insertion string values from SMS_SMS_StatMsgInStrings and the
        attribute value from SMS_StatMsgAttributes .

Example
The following example reads error message status messages for the sample created in
How to Report User-Defined Status Messages Using WMI. Make sure the MyPackageID
and MyApplication values in the query match in both samples.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ReadErrorStatusMesage(connection)

         Dim queryWQL
         Dim message
         Dim messageSet
         Dim statusMessage
         Dim insertionString
         Dim attributes

      queryWQL = "SELECT b.Component, b.MachineName, b.MessageType,
  b.MessageID, " & _
              "        c.InsStrValue, d.AttributeValue " & _
              "FROM SMS_StatusMessage b " & _
              "      JOIN SMS_StatMsgInsStrings c ON b.RecordID = c.RecordID "
  & _
              "      JOIN SMS_StatMsgAttributes d ON c.RecordID = d.RecordID "
  & _

<!-- p.1534 -->

            "WHERE b.Component = 'MyApplication' " & _
            "AND   d.AttributeID = 400 " & _
            "AND   d.AttributeValue = 'MyPackageID' "

     Set messageSet = connection.ExecQuery(queryWQL)

     For Each message in messageSet

        ' Get the message objects.
        statusMessage = message.Properties_.Item("b")
        insertionString = message.Properties_.Item("c")
        attributes = message.Properties_.Item("d")

        ' Display the message details.
        WScript.Echo "Message: " +
insertionString.Properties_.Item("insstrvalue")
        WScript.Echo "Component: " +
statusMessage.Properties_.Item("Component")
        WScript.Echo "Computer: " +
statusMessage.Properties_.Item("MachineName")
        WScript.Echo "MessageID: " +
Cstr(statusMessage.Properties_.Item("MessageID"))
        WScript.Echo attributes.Properties_.Item("attributevalue")
        WScript.Echo

     Next

 End Sub

c#

public void ReadErrorStatusMessage(WqlConnectionManager connection)
{
    try
    {
        string queryWQL = "SELECT b.Component, b.MachineName, " +
                "       b.MessageType, b.MessageID, " +
                "       c.insstrvalue, d.attributevalue " +
                "FROM SMS_StatusMessage b " +
                "     JOIN SMS_StatMsgInsStrings c ON b.RecordID =
c.RecordID " +
                "     JOIN SMS_StatMsgAttributes d ON c.RecordID =
d.RecordID " +
                "WHERE b.Component = \"MyApplication\" " +
                "AND   d.AttributeID = 400 " +
                "AND   d.AttributeValue = \"MyPackageID\" ";

        IResultObject query =
connection.QueryProcessor.ExecuteQuery(queryWQL);
        foreach (IResultObject o in query)
        {

<!-- p.1535 -->

              ManagementBaseObject statusMessage =
  (ManagementBaseObject)o["b"].ObjectValue;
              ManagementBaseObject insertionString =
  (ManagementBaseObject)o["c"].ObjectValue;
              ManagementBaseObject attributes =
  (ManagementBaseObject)o["d"].ObjectValue;

                    Console.WriteLine("Message: " + insertionString["insstrvalue"]);
                    Console.WriteLine("Component: " + statusMessage["Component"]);
                    Console.WriteLine("Computer: " + statusMessage["MachineName"]);
                    Console.WriteLine("MessageID: " + statusMessage["MessageID"]);
                    Console.WriteLine(attributes["attributevalue"]);
                    Console.WriteLine();
              }
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to read status message: ", ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter        Type                        Description

 connection       - Managed:                  A valid connection to the SMS Provider. For more
                  WqlConnectionManager        information, see SMS Provider fundamentals.
                  - VBScript: SWbemServices

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

System.Management

Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.1536 -->

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

System.Management

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About Configuration Manager Status Messages
How to Report User-Defined Status Messages
SMS_StatusMessage Server WMI Class
How To Delete Status Messages

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1537 -->

How to Report User-Defined Status
Messages
Article • 10/04/2022

In Configuration Manager, you can report user-defined informational, warning, and
error status messages, on the site server, by using the following methods that are
defined in the SMS_StatusMessage class:

                                                                              ﾉ     Expand table

 Method                                   Description

 RaiseErrorStatusMsg                      Raises an error status message.

 RaiseWarningStatusMsg                    Raises a warning status message.

 RaiseInformationalStatusMsg              Raises an informational status message.

To report a user defined status message by using WMI
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Call the SMS_StatusMessage class method that is appropriate for the type of status
        message you want to raise.

Example
The following example raises an error message. It also defines an attribute identifier and
attribute values for a package. For more information about attributes, see
SMS_StatMsgAttributes Server WMI Class.

In the example, the LocaleID property is hard-coded to English (U.S.). If you need the
locale for non-U.S. installations, you can get it from the SMS_Identification Server WMI
Class LocaleID property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

<!-- p.1538 -->

Sub RaiseErrorStatusMessage(connection)

      Dim smsContext
      Dim statusMessageParameters
      Dim inParams
      Dim statusMessageClass

      Set smsContext = CreateObject("WbemScripting.SWbemNamedValueSet")

      ' Add the context qualifiers to the set.
      smsContext.Add "LocaleID", "MS\1033"
      smsContext.Add "MachineName", "MyComputerName"
      smsContext.Add "ApplicationName", "MyApplication"

     ' Obtain the class definition object of a SMS_Status Message object.
      Set statusMessageClass = connection.Get("SMS_StatusMessage")

    ' Set up the in parameter.
    Set inParams =
statusMessageClass.Methods_("RaiseErrorStatusMsg").InParameters.SpawnInstanc
e_
    inParams.MessageText = "This is an error message"
    inParams.MessageType = 768
    inParams.AttrIDs = Array(400)
    inParams.AttrValues = Array("MyPackageID")

    Call connection.ExecMethod( "SMS_StatusMessage", "RaiseErrorStatusMsg",
inParams,,smsContext)
    If Err.Number<>0 Then
        Wscript.Echo "Couldn't run method"
        Exit Sub
    End If

 End Sub

c#

public void RaiseErrorStatusMessage(WqlConnectionManager connection)
{
    try
    {
        Dictionary<string, object> StatusMessageParameters = new
Dictionary<string, object>();

         connection.Context.Add("ApplicationName", "MyApplication");
         connection.Context.Add("MachineName", "MyComputerName");
         connection.Context.Add("LocaleID", @"MS\1033");

        // Add the parameters.
        StatusMessageParameters.Add("MessageText", "This is an error
message");
        StatusMessageParameters.Add("MessageType", 768);

<!-- p.1539 -->

          StatusMessageParameters.Add("AttrIDs", new int[] { 400 });
          StatusMessageParameters.Add("AttrValues", new string[] {
  "MyPackageID" });

          // Call the method.
          connection.ExecuteMethod("SMS_StatusMessage", "RaiseErrorStatusMsg",
  StatusMessageParameters);

      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed to raise error status message: ",
  ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter    Type                        Description

 connection   - Managed:                  A valid connection to the SMS Provider. For more
              WqlConnectionManager        information, see SMS Provider fundamentals.
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

<!-- p.1540 -->

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
About status messages SMS_StatusMessage Server WMI Class
How To Delete Status Messages

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1541 -->

How to Delete Status Messages
Article • 10/04/2022

In Configuration Manager, you delete status messages by calling the SMS_StatusMessage
class DeleteByID method and supplying an array of status message RecordID identifiers.
Alternatively, you can call the SMS_StatusMessage class DeleteByQuery method and
supply a WQL query that identifies the status messages to be deleted.

To delete a status message
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Call the SMS_StatusMessage class DeleteByID method with an array of record
        identifiers for the status messages to be deleted.

Example
The following example deletes a single status message identified by the recordId
identifier.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub DeleteStatusMessage(connection, recordId)

         Dim inParams
         Dim outParams
         Dim statusMessageClass

         On Error Resume Next

         ' Obtain the class definition object of a SMS_StatusMessage object.
         Set statusMessageClass = connection.Get("SMS_StatusMessage")

         If Err.Number<>0 Then
             Wscript.Echo "Couldn't get status message class"
             Exit Sub
         End If

      ' Set up the in parameter.
      Set inParams =
  statusMessageClass.Methods_("DeleteByID").InParameters.SpawnInstance_

<!-- p.1542 -->

           inParams.RecordIDs = Array(recordId)
           If Err.Number<>0 Then
               Wscript.Echo "Couldn't get in parameters object"
               Exit Sub
           End If

           ' Call the method.
           Set outParams = _
               connection.ExecMethod( "SMS_StatusMessage", "DeleteByID", inParams)
           If Err.Number<>0 Then
               Wscript.Echo "Couldn't run method"
               Exit Sub
           End If

           WScript.Echo CStr(outParams.ReturnValue) + " record(s) deleted"

       End Sub

  c#

  public void DeleteStatusMessage(WqlConnectionManager connection, Int64
  recordId)
  {
      try
      {
          Dictionary<string, object> StatusMessageParameters = new
  Dictionary<string, object>();

               // Add the parameters.
              StatusMessageParameters.Add("RecordIDs", new Int64[] { recordId });

          // Call the method.
          IResultObject result = connection.ExecuteMethod("SMS_StatusMessage",
  "DeleteByID", StatusMessageParameters);

          Console.WriteLine (result["ReturnValue"].IntegerValue + " record(s)
  deleted");

       }
           catch (SmsException ex)
           {
               Console.WriteLine("Failed to delete error message: ", ex.Message);
               throw;
           }
  }

The example method has the following parameters:

                                                                      ﾉ   Expand table

<!-- p.1543 -->

 Parameter    Type                        Description

 Connection   - Managed:                  A valid connection to the SMS Provider. For more
              WqlConnectionManager        information, see SMS Provider fundamentals.
              - VBScript: SWbemServices

 recordId     - Managed: Integer          The status message identifier. This is
              - VBScript: Integer         SMS_StatusMessage object RecordID property for the
                                          status message to be deleted.

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

<!-- p.1544 -->

About status messages How to Report User-Defined Status Messages Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1545 -->

How to Determine Package Status
Article • 10/04/2022

In Configuration Manager, the software distribution process can take from several
minutes to several hours, depending on the site settings, network topography, whether
the package includes source files, and the number of distribution points that have been
specified for the package. Creating the package, distribution points, programs, and
advertisement instances initiates the software distribution process that is managed by
the Configuration Manager Distribution Manager.

The Distribution Manager must first distribute the package's source files, which is the
time-consuming aspect of the software distribution process. Only after the source files
are distributed can the advertisements be offered on a site. You can use the package
summarizer classes to determine whether a package has been distributed and is ready
to be advertised.

The level of status detail that you want determines which of the following package
summarizer classes to use:

      SMS_PackageStatusDetailSummarizer Server WMI Class

      SMS_PackageStatusRootSummarizer Server WMI Class

      SMS_PackageStatusDistPointsSummarizer Server WMI Class

      The SMS_PackageStatusDetailSummarizer class gives you package status at the site
      level and the SMS_PackageStatusRootSummarizer class gives you package status for
      all sites. You can only use the SMS_PackageStatusDistPointsSummarizer class if your
      package contains source files.

      For packages that do not contain source files, an instance in the root or detail class
      signifies that the distribution portion of the process is complete (the value for
      Targeted property is 0). For packages that do contain source files, when the value

      in the Installed property equals the value in the Targeted property, the source
      files have been successfully distributed.

      To determine the status of a package, you can either create your own polling
      mechanism by using a timer that queries the summarizer for a specific package or
      you can register for a Windows Management Instrumentation (WMI) temporary
      intrinsic event that polls for create instance and modify instance events on the
      summarizer class as the following example shows. You can use your own timer
      mechanism, or you can create a WMI timer event.

<!-- p.1546 -->

  ７ Note

  Using WMI to poll for events is expensive and should be used with consideration.

To determine package status
   1. Set up a connection to the Configuration Manager provider namespace.

   2. Create an event handler to watch for the creation or modification of the
        SMS_PackageStatusRootSummarizer Server WMI Class.

Example
The following example asynchronously queries for the creation and modification of the
SMS_PackageStatusRootSummarizer Server WMI Class.

  ７ Note

  It is not possible to use the managed provider libraries to query WMI object
  instance creation and modification. Therefore the C# sample is written by using the
  System.Management libraries.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub QueryPackageStatus (connection)

         Dim query
         Dim sink
         Dim minutes

         Set sink = WScript.CreateObject("wbemscripting.swbemsink","sink_")

      ' You have to specify a polling interval because Configuration Manager
      ' does not provide an intrinsic event provider for these classes.
      Query = "SELECT * FROM __InstanceCreationEvent Within 120 " & _
              "WHERE TargetInstance.__Class =
  'SMS_PackageStatusRootSummarizer' "
      connection.ExecNotificationQueryAsync sink, query

         query = "SELECT * FROM __InstanceModificationEvent Within 120 " & _
                 "WHERE TargetInstance.__Class =

<!-- p.1547 -->

'SMS_PackageStatusRootSummarizer' "
    connection.ExecNotificationQueryAsync sink, query

     minutes = 0

     ' Loop for 5 minutes.
     While minutes < 300
         wscript.sleep 1000
         minutes = minutes + 1
     Wend

     sink.Cancel
     Set sink = nothing

 End Sub

' The sink subroutine to handle the OnObjectReady
' event. This is called as each object returns.
Sub sink_OnObjectReady(statusEvent, octx)
   Wscript.Echo "Name: " + statusEvent.TargetInstance.Name
   Wscript.Echo "Targeted: " + CStr(statusEvent.TargetInstance.Targeted)
   Wscript.Echo "Installed: " + CStr(statusEvent.TargetInstance.Installed)
   Wscript.Echo
End Sub

Sub sink_OnCompleted(Hresult, oErr, oCtx)
    Wscript.Echo "Finished"
End Sub

c#

public void QueryPackageStatus(string connectionPath)
{
   // WMIEvent we = new WMIEvent();
    ManagementEventWatcher modifiedWatcher = null;
    ManagementEventWatcher createdWatcher = null;
    WqlEventQuery modified;
    WqlEventQuery created;

     ManagementOperationObserver observer = new
         ManagementOperationObserver();

     // Bind to local computer.
     ConnectionOptions opt = new ConnectionOptions();
     opt.EnablePrivileges = true; //sets required privilege
     ManagementScope scope = new ManagementScope(connectionPath, opt);

     try
     {
           modified = new WqlEventQuery();
           modified.EventClassName = "__InstanceModificationEvent";

<!-- p.1548 -->

        modified.WithinInterval = new TimeSpan(0, 0, 120);
        modified.Condition = @"TargetInstance ISA
'SMS_PackageStatusRootSummarizer'";
        modifiedWatcher = new ManagementEventWatcher(scope, modified);

        // Register handler.
        modifiedWatcher.EventArrived += new
EventArrivedEventHandler(this.ObjectReady);

        created = new WqlEventQuery();
        created.EventClassName = "__InstanceCreationEvent";
        created.WithinInterval = new TimeSpan(0, 0, 10);
        created.Condition = @"TargetInstance ISA
'SMS_PackageStatusRootSummarizer'";
        createdWatcher = new ManagementEventWatcher(scope, created);

        createdWatcher.EventArrived += new
EventArrivedEventHandler(this.ObjectReady);

       modifiedWatcher.Start();
       createdWatcher.Start();

       // Wait.
       Console.ReadLine();
    }
    catch (ManagementException e)
    {
        Console.WriteLine(e.Message);
    }
    finally
    {
        modifiedWatcher.Stop();
        createdWatcher.Stop();
    }
}

public void ObjectReady(object sender, EventArrivedEventArgs e)
{
    // Get the Event object and display it.
    PropertyData pd = e.NewEvent.Properties["TargetInstance"];

    Console.WriteLine("Hello:");

    if (pd != null)
    {
        ManagementBaseObject statusEvent = pd.Value as ManagementBaseObject;
        Console.WriteLine ("Name: " + statusEvent.Properties["Name"].Value);
        Console.WriteLine("Targeted: " +
statusEvent.Properties["Targeted"].Value);
        Console.WriteLine("Installed:" +
statusEvent.Properties["Installed"].Value);
        Console.WriteLine();
    }
}

<!-- p.1549 -->

This example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter        Type            Description

 connectionPath   Managed:        A valid path to the SMS Provider. For example,
                  String          root\\sms\\site_CODE .

 Connection       VBScript:       A valid connection to the SMS Provider. For more
                  SWbemServices   information, see How to Connect to an SMS Provider in
                                  Configuration Manager by Using WMI

Compiling the Code

Namespaces
System

System.Management

Assembly
System.Management

Robust Programming
The exception that can be raised is System.Management.ManagementException.

See Also
How to Connect to an SMS Provider in Configuration Manager by Using WMI
SMS_PackageStatusDetailSummarizer Server WMI Class
SMS_PackageStatusRootSummarizer Server WMI Class
SMS_PackageStatusDistPointsSummarizer Server WMI Class
About Configuration Manager Status Summarizers

Feedback

<!-- p.1550 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1551 -->

How to Determine Advertisement Status
Article • 10/04/2022

To determine advertisement status in Configuration Manager, you can use the queries
described in this section.

  ７ Note

  These queries query the status messages directly and might take some time to
  complete because there can be many status messages.

  For more information about using these queries, see How to Perform a
  Synchronous Configuration Manager Query by Using Managed Code and How to
  Perform a Synchronous Configuration Manager Query by Using WMI.

  For more queries about advertisement status and summarization, you can use
  SMS_ClientAdvertisementStatus Server WMI Class and
  SMS_ClientAdvertisementSummary Server WMI Class.

Queries

Client Program Install
The following query returns the clients that have successfully installed a program. You
need to check for both message identifiers because the program can report status with
an exit code (10008) or an install status MIF file (10009).

  ' Returns clients that have successful installed a program
  SELECT msg.MachineName, msg.SiteCode, ad.ProgramName
  FROM SMS_StatusMessage msg
       JOIN SMS_StatMsgAttributes attr ON msg.RecordID = attr.RecordID
       JOIN SMS_Advertisement ad ON attr.AttributeValue = ad.AdvertisementID
  WHERE msg.Component = "Software Distribution"
  AND   (msg.MessageID = 10008 or msg.MessageID = 10009)
  AND   attr.AttributeID = 401
  ORDER BY ad.ProgramName

Clients That Have Installed a Specific Advertised Program

<!-- p.1552 -->

This query returns the clients that have successfully installed a specific advertised
program.

  ' Returns clients that have successfully installed a specific advertised
  program
  SELECT msg.MachineName, msg.SiteCode
  FROM SMS_StatusMessage msg
       JOIN SMS_StatMsgAttributes attr ON msg.RecordID = attr.RecordID
  WHERE msg.Component = "Software Distribution"
  and   (msg.MessageID = 10008 or msg.MessageID = 10009)
  and   attr.AttributeID = 401
  and   attr.AttributeValue = "<AdvertisementID>"

Clients That Have Not Installed a Specific Advertised
Program
The previous queries show which clients successfully installed an advertised program.
Determining which collection members have not installed the advertised program can
be more involved if the advertisement specified subcollections. The following query
determines which clients of the All Systems (SMS00001) collection (substitute your
collection member class for SMS_CM_RES_COLL_SMS00001) have not installed the
advertised program. If the advertisement specified subcollections, the query must be run
for each subcollection.

  ' Returns which clients of a collection have not installed the advertised
  program
  SELECT Name
  FROM SMS_CM_RES_COLL_SMS00001
  WHERE NOT Name IN (SELECT msg.MachineName
  FROM SMS_StatusMessage msg
       JOIN SMS_StatMsgAttributes attr ON msg.RecordID = attr.RecordID
  WHERE msg.Component = "Software Distribution"
  AND   (msg.MessageID = 10008 or msg.MessageID = 10009)
  AND   attr.AttributeID = 401
  AND   attr.AttributeValue = "<AdvertisementID>")

See Also
How to Perform an Asynchronous Configuration Manager Query by Using Managed
Code
How to Perform a Synchronous Configuration Manager Query by Using Managed Code

<!-- p.1553 -->

How to Perform an Asynchronous Configuration Manager Query by Using WMI
How to Perform a Synchronous Configuration Manager Query by Using WMI
SMS_StatusMessage Server WMI Class
SMS_StatMsgAttributes Server WMI Class
Calling Configuration Manager Code Snippets

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1554 -->

Configuration Manager API reference
Article • 10/04/2022

This reference contains detailed information about the following APIs:

      The Configuration Manager class schema
      Extended WMI Query Language (WQL)
      Named values and qualifiers
      The Configuration Manager console libraries
      The managed SMS Provider library

For more information about how to use the SDK, see Configuration Manager SDK.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1555 -->

Administration service documentation
Developer documentation for the Configuration Manager REST API

  About administration service

  ｅ OVERVIEW
  What is the administration service?

  ｃ HOW-TO GUIDE
  How to set up

  How to use
