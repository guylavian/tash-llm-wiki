---
title: "Configuration Manager SDK documentation — pages 161-200"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0161-0200
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0161-0200
family: sccm
documentKind: "doc"
abstract: "Sub CreateDailyRecurringScheduleString(connection, _ hourDuration, _ daySpan, _ startTime, _ isGmt) ' Create a new recurring interval schedule object. ' Note: There are several types of schedule classes available, each defines a different type of schedule. Set recurInterval = co"
---

# Configuration Manager SDK documentation — pages 161-200

<!-- p.161 -->

Sub CreateDailyRecurringScheduleString(connection,   _
                                       hourDuration, _
                                       daySpan,      _
                                       startTime,    _
                                       isGmt)

    ' Create a new recurring interval schedule object.
    ' Note: There are several types of schedule classes available, each
defines a different type of schedule.
    Set recurInterval =
connection.Get("SMS_ST_RecurInterval").SpawnInstance_

     ' Populate the schedule properties.
     recurInterval.DayDuration = 0
     recurInterval.HourDuration = hourDuration
     recurInterval.MinuteDuration = 0
     recurInterval.DaySpan = daySpan
     recurInterval.HourSpan = 0
     recurInterval.MinuteSpan = 0
     recurInterval.StartTime = startTime
     recurInterval.IsGMT = isGmt

    ' Call WriteToString method to decode the schedule token.
    ' Note: The initial parameter of the WriteToString method requires an
array.
    Set clsScheduleMethod = connection.Get("SMS_ScheduleMethods")
    clsScheduleMethod.WriteToString Array(recurInterval), scheduleString

     ' Output schedule token as an interval string.
     WScript.Echo "Schedule Token Interval String: " & scheduleString

End Sub

c#

public void CreateDailyRecurringScheduleToken(WqlConnectionManager
connection,
                                              int hourDuration,
                                              int daySpan,
                                              string startTime,
                                              bool isGmt)
{
    try
    {
        // Create a new recurring interval schedule object.
        // Note: There are several types of schedule classes available, each
defines a different type of schedule.
        IResultObject recurInterval =
connection.CreateEmbeddedObjectInstance("SMS_ST_RecurInterval");

<!-- p.162 -->

              // Populate the schedule properties.
              recurInterval["DayDuration"].IntegerValue = 0;
              recurInterval["HourDuration"].IntegerValue = hourDuration;
              recurInterval["MinuteDuration"].IntegerValue = 0;
              recurInterval["DaySpan"].IntegerValue = daySpan;
              recurInterval["HourSpan"].IntegerValue = 0;
              recurInterval["MinuteSpan"].IntegerValue = 0;
              recurInterval["StartTime"].StringValue = startTime;
              recurInterval["IsGMT"].BooleanValue = isGmt;

              // Creating array to use as a parameters for the WriteToString
  method.
              List<IResultObject> scheduleTokens = new List<IResultObject>();
              scheduleTokens.Add(recurInterval);

          // Creating dictionary object to pass parameters to the
  WriteToString method.
          Dictionary<string, object> inParams = new Dictionary<string, object>
  ();
          inParams["TokenData"] = scheduleTokens;

              // Initialize the outParams object.
              IResultObject outParams = null;

          // Call WriteToString method to decode the schedule token.
          outParams = connection.ExecuteMethod("SMS_ScheduleMethods",
  "WriteToString", inParams);

          // Output schedule token as an interval string.
          // Note: The return value for this method is always 0, so this check
  is just best practice.
          if (outParams["ReturnValue"].IntegerValue == 0)
          {
              Console.WriteLine("Schedule Token Interval String: " +
  outParams["StringData"].StringValue);
          }
      }
      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
      }
  }

The example method has the following parameters:

                                                                              ﾉ    Expand table

 Parameter       Type                    Description

 connection      - Managed:              A valid connection to the SMS Provider.
                  WqlConnectionManager

<!-- p.163 -->

 Parameter      Type                  Description

                - VBScript:
                SWbemServices

 hourDuration   - Managed: Integer    Number of hours during which the scheduled action
                - VBScript: Integer   occurs. Allowable values are in the range 0-23. The
                                      default value is 0, indicating no duration.

 daySpan        - Managed: Integer    Number of days spanning schedule intervals. Allowable
                - VBScript: Integer   values are in the range 0-31. The default value is 0.

 startTime      - Managed: String     Date and time when the scheduled action takes place.
                (DateTime)            The default value is "19700201000000.000000+***".
                - VBScript: String    This is the format in which (WMI) CIM DATETIME values
                (DateTime)            are stored.

 isGmt          - Managed: Boolean    true if the time is in Coordinated Universal Time (UTC).
                - VBScript: Boolean   The default value is false , for local time.

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
microsoft.configurationmanagement.managmentprovider

adminui.wqlqueryengine

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

<!-- p.164 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
SMS_ST_NonRecurring Server WMI Class
SMS_ST_RecurInterval Server WMI Class
SMS_ST_RecurMonthlyByDate Server WMI Class
SMS_ST_RecurMonthlyByWeekday Server WMI Class
SMS_ST_RecurWeekly Server WMI Class
SMS_ScheduleMethods Server WMI Class
ReadFromString Method in Class SMS_ScheduleMethods
WriteToString Method in Class SMS_ScheduleMethods

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.165 -->

About the Configuration Manager Site
Control File
Article • 10/10/2022

Site control in Configuration Manager defines the settings for a specific site. The
settings for each site are contained in the database and are accessed through Windows
Management Instrumentation (WMI) when working with scripting languages, and
through the managed SMS Provider library when working with a managed language.

  ７ Note

  Previous releases of Configuration Manager had a physical file that was processed
  for site settings referred to as the site control file. Configuration Manager stores
  site settings directly in the site database; however, very little has changed when
  programmatically configuring a site.

The site control file in Configuration Manager is an ASCII text file (Sitectrl.ct0) that
contains the configuration of each site. There are two types of site control files:

      Actual site control file - A working copy of the site control file that is stored in the
      Configuration Manager site database and in the inbox in the site control manager.

      Delta site control file - Contains the proposed site control file changes that are to
      be processed.

      The site control file is stored on each site server in the site control manager inbox.

      On the primary site, there is a copy of the site control file for the current site in the
      database. The primary site also has a copy of the site control file for all lower level
      sites in the hierarchy, including secondary sites.

      Each child site passes a copy of its site control file to its parent site. Each parent
      site passes a copy of the site control file for itself and for each of its child sites up
      the hierarchy. Therefore, the central site's database contains copies of the site
      control files of every Configuration Manager site in the hierarchy.

Site Control File Format
The site control file is a collection of resource definitions that contain embedded
properties, embedded property lists and multi-string lists. The following example shows

<!-- p.166 -->

a section of site control file that defines client component information. The resource is
declared by the BEGIN_CLIENT_COMPONENT. The embedded properties are denoted by
PROPERTY and have a name and value. The property lists are denoted by the
BEGIN_PROPERTY_LIST section and list a property list name and several property names
and associated values. The multi-string lists are denoted by the
BEGIN_CLIENT_REG_MULTI_STRING_LIST and provide a list of string values.

  BEGIN_CLIENT_COMPONENT
      <SMS Client Base Components>
      <65537>
      SITE_KEY_FLAGS <1>
      PROPERTY <Component Verify Interval><REG_SZ><00011700001000F0><0>
      PROPERTY <Component Maintenance Interval (minutes)><REG_DWORD><><1500>
      BEGIN_PROPERTY_LIST
          <Copy Queue>
          <(REG_DWORD)Item Lifetime=11520>
          <(REG_DWORD)Wakeup cycle=1380>
      END_PROPERTY_LIST
      BEGIN_CLIENT_REG_MULTI_STRING_LIST
          <Retry Sequence><Copy Queue>
          SITE_KEY_FLAGS <1>
          <15>
          <30>
          <60>
          <360>
      END_CLIENT_REG_MULTI_STRING_LIST
  END_CLIENT_COMPONENT

The provider has several Windows Management Instrumentation (WMI) classes that
represent resources in the site control file. For example, SMS_SCI_Component Server
WMI Class holds information on the server components stored on a Configuration
Manager site server. These classes derive from SMS_SiteControlItem Server WMI Class.
For more information, see Configuration Manager Site Configuration Server WMI
Classes [reference].

The following example is the declaration for SMS_SCI_ClientConfig Server WMI Class.

  Class SMS_SCI_ClientConfig : SMS_SiteControlItem
  {
       String ClientConfigName;
       UInt32 FileType;
       UInt32 Flags;
       String ItemName;
       String ItemType;
       String Platforms[];

<!-- p.167 -->

         SMS_EmbeddedPropertyList PropLists[];
         SMS_EmbeddedProperty Props[];
         SMS_Client_Reg_MultiString_List RegMultiStringLists[];
         String SiteCode;
  };

The declaration includes declarations for the embedded property, property list, and
multi string list declarations.

You access the embedded properties, property lists, and multi-string lists by using the
following classes:

                                                                                  ﾉ   Expand table

 Type                             WMI Class

 Embedded property                SMS_EmbeddedProperty Server WMI Class

 Embedded property list           SMS_EmbeddedPropertyList Server WMI Class (array)

 Multi-string list                SMS_Client_Reg_MultiString_List Server WMI Class (array)

This documentation has the following topic that describes the embedded properties:

How to Read a Configuration Manager Site Control File Embedded Property List

Using the Site Control File
How you access the site control file differs depending on whether you are using WMI or
the managed provider.

WMI
When you are using WMI, you use the SMS_SiteControlFile class methods to manage
changes to the site control file. Writing to the site control file is managed by using
session contextual information that you supply. This is used to enable concurrent writing
to the site control file for multiple applications. For more information, see How to Read
and Write to the Configuration Manager Site Control File by Using WMI If you are only
reading from the site control file you can query it without setting up a session.

Managed Provider
In almost all cases, your code does not have to lock or commit changes to the
Configuration Manager site control file because the managed Configuration Manager

<!-- p.168 -->

library takes care of this for you. As a result, programming the Configuration Manager
site control file is fundamentally the same as programming Configuration Manager
objects. This is different from accessing the Configuration Manager site control file
through WMI where you explicitly have to get a session handle and commit any changes
you make.

For more information, see, How to Read and Write to the Configuration Manager Site
Control File by Using Managed Code.

See Also
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.169 -->

How to Read and Write to the
Configuration Manager Site Control File
by Using Managed Code
Article • 10/10/2022

To write to the Configuration Manager site control file by using the managed SMS
Provider, you get the site definition file by querying for the required resource or
component. You then update the embedded property, embedded property list, or multi-
string list as required.

  ７ Note

  You can also use connection manager GetInstance to get the required resource or
  component.

The managed Configuration Manager manages the connection session to the site
control file automatically for you. Therefore you treat the IResultObject objects returned
from the query in the same way as you treat IResultObject objects retrieved from the
SMS Provider.

To read and write to the site control file
   1. Set up a connection to the SMS Provider. For more information, see How to
      Connect to an SMS Provider in Configuration Manager by Using Managed Code.

   2. Use the Connection Manager QueryProcessor object ExecQuery or GetInstance
      method to get the required site control file resource or component IResultObject
      object.

   3. Using the IResultObject update the site control file.

   4. Use the IResultObject object Put method to commit the changes.

Example
The following C# example accesses the client agent component of the site control file
and creates a dummy property, property list and multi-string list. It then removes the
updates that were made. The example demonstrates how to query the site control file,
make updates, and commit changes to the site control file.

<!-- p.170 -->

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  public void ReadWriteSCF(WqlConnectionManager connection,string siteCode)
  {
      try
      {

      // Query for the site's site control file client agent settings.
      IResultObject resources =
      connection.QueryProcessor.ExecuteQuery
      ("SELECT * FROM SMS_SCI_ClientComp WHERE ClientComponentName = 'Client
  Agent' AND SiteCode = '" +
      siteCode + "'");

      foreach (IResultObject resource in resources)
      {
              // Embedded Properties

               Console.WriteLine("Embedded property");
               Console.WriteLine("-----------------");

               int value = 0;
               string value1 = "";
               string value2 = "";

               // Write a dummy embedded property.
               this.WriteScfEmbeddedProperty(resource, "Test", 10, "Hello",
  "World");

              // Get the embedded property back and display the values.
              if (this.GetScfEmbeddedProperty(resource, "Test", ref value, ref
  value1, ref value2))
              {
                  Console.WriteLine("Value: " + value);
                  Console.WriteLine("Value1: " + value1);
                  Console.WriteLine("Value2: " + value2);

                  // Remove the dummy embedded property.
                  Dictionary<string, IResultObject> EmbeddedProperties =
  resource.EmbeddedProperties;
                  EmbeddedProperties.Remove("Test");
                  resource.EmbeddedProperties = EmbeddedProperties;
                  resource.Put();

                  // See if the dummy embedded property is still there.
                  if (this.GetScfEmbeddedProperty(resource, "Test", ref value,
  ref value1, ref value2))
                  {
                       Console.WriteLine("Test exists");
                  }
                  else

<!-- p.171 -->

               {
                    Console.WriteLine("Test does not exist");
               }
            }
            else
            {
                Console.WriteLine("Property not found");
            }

            Console.WriteLine();

            // Embedded property list.

            Console.WriteLine("Embedded property list");
            Console.WriteLine("----------------------");

            // values contains the embedded property list.
            ArrayList values = new ArrayList();

            values.Add("Elephant");
            values.Add("Giraffe");

            // Write to the resource.
            this.WriteScfEmbeddedPropertyList(resource, "Animals", values);

            ArrayList retrievedValues;

            // Get the embedded property list and display.
            if (this.GetScfEmbeddedPropertyList(resource, "Animals", out
retrievedValues))
            {
                foreach (string retrievedValue in retrievedValues)
                {
                    Console.WriteLine(retrievedValue);
                }

               // Remove one of the entries.
               retrievedValues.Remove("Elephant");
               Console.WriteLine();

                // Update the list.
                this.WriteScfEmbeddedPropertyList(resource, "Animals",
retrievedValues);

                // Display the list again.
                this.GetScfEmbeddedPropertyList(resource, "Animals", out
retrievedValues);
                foreach (string retrievedValue in retrievedValues)
                {
                    Console.WriteLine(retrievedValue);
                }

            }
            else
            {

<!-- p.172 -->

                Console.WriteLine("None");
            }

            Console.WriteLine();

            // RegMultiStringList.

            Console.WriteLine("RegMultiStringList");
            Console.WriteLine("------------------");

            // valuesStrings is the RegMultiString List.
            ArrayList valueStrings = new ArrayList();

            valueStrings.Add("Tom");
            valueStrings.Add("Harry");

            this.WriteScfRegMultiStringList(resource, "Names",
valueStrings);

            ArrayList retrievedValuesStrings;

            if (this.GetScfRegMultiStringList(resource, "Names", out
retrievedValuesStrings))
            {
                foreach (string retrievedValue in retrievedValuesStrings)
                {
                    Console.WriteLine(retrievedValue);
                }

                // Remove one of the entries.
                retrievedValuesStrings.Remove("Tom");
                Console.WriteLine();

                // Update the list.
                this.WriteScfRegMultiStringList(resource, "Names",
retrievedValuesStrings);

                // Display the list again.
                this.GetScfRegMultiStringList(resource, "Names", out
retrievedValuesStrings);
                foreach (string retrievedValue in retrievedValuesStrings)
                {
                    Console.WriteLine(retrievedValue);
                }
            }
            else
            {
                Console.WriteLine("None");
            }
        }
    }
    catch (SmsException e)
    {
        Console.WriteLine("Failed: " + e.Message);
        throw;

<!-- p.173 -->

      }
  }

The example method has the following parameters:

                                                                           ﾉ     Expand table

 Parameter    Type                     Description

 connection   - WqlConnectionManager   A valid connection to the SMS Provider.

 siteCode     - String                 The site code for the Configuration Manager site.

Compiling the Code

Namespaces
System

System.Collections.Generic

System.Collections

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

<!-- p.174 -->

SMS Provider fundamentals About the Configuration Manager Site Control File
How to Connect to a Configuration Manager Provider using Managed Code
How to Read a Configuration Manager Site Control File Embedded Property List
Objects overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.175 -->

How to Read and Write to the
Configuration Manager Site Control File
by Using WMI
Article • 10/10/2022

In Configuration Manager, you write to the site control file using Windows Management
Instrumentation (WMI) by using the SMS_SiteControlFile class methods.

When writing to the site control file by using WMI, you use a session handle to identify
your application. This is used to manage concurrent updates to the file.

When you have finished writing to the site control file, you must commit your changes.

SMS_SiteControlFile has the following methods to manage changes to the site control
file.

                                                                                 ﾉ   Expand table

 Method                  Description

  CommitSCF              Applies your changes to the Configuration Manager database.

  RefreshSCF             Refreshes your in-memory copy of the site control file with any recent
                         changes from the Configuration Manager database.

  GetSessionHandle       Gets your in-memory copy of the site control file and a session handle.
                         You place the session handle in an IWbemContext object that is passed to
                         all IWbemServices methods.

  ReleaseSessionHandle   Releases your in-memory copy of the site control file and any resources
                         associated with your session handle.

   Ｕ Caution

   You should be experienced in managing a site's configuration before using the SMS
   Provider classes to modify the site configuration. You can cause great harm to a site
   by changing some configurable items. You should use extreme caution or avoid
   using the SMS_SCI_FileDefinition and SMS_SCI_SiteDefinition classes altogether.
   These classes manage the site control file itself. If you are not careful, you can
   render the site useless.

<!-- p.176 -->

To write to the site control file
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
        fundamentals.

   2. Create a SWbemNameValue value set to hold your context data.

   3. Get a session handle from SMS_SiteControlFile class GetSessionHandle .

   4. Add the session handle to your context data.

   5. Call the SMS_SiteControlFile object RefreshSCF to get the latest copy of the site
        control file. Use the context data in the call.

   6. Query for the site control file resource you want to update using your context data.

   7. Update the resource using your context data.

   8. Commit your changes to the site control file using the SMS_SiteControlFile object
        CommitSCF method.

   9. Call the SMS_SiteControlFile object ReleaseSessionHandle method to release your
        session handle.

Example
The following VBScript example access the client agent component of the site control
file and creates a dummy property, property list and multi-string list. It then removes the
updates that were made. The example demonstrates how to set up the session handle,
get the site control file, query the site control file, make updates and commit changes to
the site control file.

In the example, the LocaleID property is hard-coded to English (U.S.). If you need the
locale for non-U.S. installations, you can get it from the SMS_Identification Server WMI
Class LocaleID property.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ReadWriteScf(connection, siteCode)

         Dim context
         Dim query

<!-- p.177 -->

    Dim resource
    Dim resources
    Dim inParams

    Set context = CreateObject("WbemScripting.SWbemNamedValueSet")

    ' Add the standard SMS context qualifiers to the context object.
    context.Add "LocaleID", "MS\1033"
    context.Add "MachineName", "MyMachine"
    context.Add "ApplicationName", "MyApp"

    ' Add the session handle.
    context.Add "SessionHandle", _
         connection.ExecMethod("SMS_SiteControlFile",
"GetSessionHandle").SessionHandle

   ' Load site control file.
        Set inParams =
connection.Get("SMS_SiteControlFile").Methods_("RefreshSCF").InParameters.Sp
awnInstance_
InParams.SiteCode = siteCode
connection.ExecMethod "SMS_SiteControlFile", "RefreshSCF", inParams, ,
context

    ' Query for the client agent component.
    query = "SELECT * FROM SMS_SCI_ClientComp " & _
            "WHERE ClientComponentName = 'Client Agent' " & _
           "AND SiteCode = '" & siteCode & "'"

    Set resources = connection.ExecQuery(query, , , context)

    For each resource in resources

    ' Embedded property.

       WScript.Echo "Embedded property"
       Wscript.Echo "-----------------"

       Dim value
       Dim value1
       Dim value2

        Call
WriteScfEmbeddedProperty(connection,context,resource,"Test2",20,"Hello","Wor
ld")

        If   GetScfEmbeddedProperty(resource,"Test2",value,value1,value2) =
True Then
           Wscript.Echo "Value: " + CStr(value)
           WScript.Echo "Value1: " + value1
           WScript.Echo "Value2: " + value2
       End If

       WScript.Echo
       dim n,l

<!-- p.178 -->

       dim updatedProps
       Dim scfProp

       n = 0
       ' Remove the property.
       For l = 0 To UBound (resource.Props)

            ' Copy each element except the one to delete.
            If resource.Props(l).PropertyName <> "Test2" Then
                Dim embeddedProperty
                Set embeddedProperty =
connection.Get("SMS_EmbeddedProperty").Spawninstance_()
                If l = 0 Then
                    ' Create an array to copy to.
                    updatedProps = array(embeddedProperty)
                    Redim updatedProps(Ubound(resource.Props)-1)
                End If
                ' Copy the element.
                embeddedProperty.PropertyName =
resource.Props(l).PropertyName
                embeddedProperty.Value = resource.Props(l).value
                embeddedProperty.Value1 = resource.Props(l).value1
                embeddedProperty.Value2 = resource.Props(l).value2

               Set updatedProps(n) = embeddedProperty
               n = n + 1
         End If
       Next

       ' Update
       resource.Props = updatedProps
       resource.Put_, context

       WScript.Echo

        ' Check that the property has been deleted.
        If GetScfEmbeddedProperty(resource,"Test2",value,value1,value2) =
True Then
             WScript.Echo "Property found"
        Else
             WScript.Echo "Property not found"
        End If

       WScript.Echo

    ' Embedded property list.

       WScript.Echo "Embedded property list"
       WScript.Echo "----------------------"

       Dim values
       values = Array("Tiger","Wolf")

        Call
WriteScfEmbeddedPropertyList(connection,context,resource,"Animals",values)

<!-- p.179 -->

       Dim retrievedValues

        If GetScfEmbeddedPropertyList(resource,"Animals",retrievedValues) =
True Then
            Dim i,c
            Dim updatedValues

              c = 0

              ' Display the list and remove the property Tiger.
              updatedValues = Array(UBound(retrievedValues)-1)
              For i = 0 To UBound (retrievedValues)
                   Wscript.Echo retrievedValues(i)
                   If retrievedValues(i) <> "Tiger" Then

                        updatedValues(c) = retrievedValues(i)
                        c = c + 1
                     End If
              Next

            WScript.Echo
            ' Update the property list.
            Call
WriteScfEmbeddedPropertyList(connection,context,resource,"Animals",updatedVa
lues)

            ' Get the property list and display.
            Call
GetScfEmbeddedPropertyList(resource,"Animals",retrievedValues)

              For i = 0 To UBound (retrievedValues)
                   Wscript.Echo retrievedValues(i)
               Next
       Else
           WScript.Echo "Not found"
       End If

       WScript.Echo

    ' RegMultiString list.

       WScript.Echo "Embedded RegMultiString list"
       WScript.Echo "----------------------------"

       Dim valueStrings
       valueStrings= Array("Lisa","Julie")

        ' Write the RegMultiString list.
        Call
WriteScfRegMultiStringList(connection,context,resource,"Names2",valueStrings
)

       Dim retrievedValueStrings

<!-- p.180 -->

          ' Get the RegMultiString list.
          If GetScfRegMultiStringList(resource,"Names2",retrievedValueStrings)
  = True Then

                 Dim updatedValueStrings

                 c = 0
                 updatedValueStrings = Array(Ubound(retrievedValueStrings)-1)
                 For i = 0 To UBound (retrievedValueStrings)
                      Wscript.Echo retrievedValueStrings(i)
                      if retrievedValueStrings(i) <> "Lisa" Then
                         updatedValueStrings(c) = retrievedValueStrings(i)
                      End If
                 Next

              Call
  WriteScfRegMultiStringList(connection,context,resource,"Names",updatedValueS
  trings)

                 WScript.Echo

              Call
  GetScfRegMultiStringList(resource,"Names",retrievedValueStrings)

                 For i = 0 To UBound (retrievedValueStrings)
                      Wscript.Echo retrievedValueStrings(i)
                  Next
          Else
              WScript.Echo "Not found"
          End If
      Next

      ' Commit the changes.
      Set inParams =
  connection.Get("SMS_SiteControlFile").Methods_("CommitSCF").InParameters.Spa
  wnInstance_
      inParams.SiteCode = siteCode
      connection.ExecMethod "SMS_SiteControlFile", "CommitSCF", inParams, ,
  context

      ' Release the session handle.
      Set inParams =
  connection.Get("SMS_SiteControlFile").Methods_("ReleaseSessionHandle").InPar
  ameters.SpawnInstance_
      inParams.SessionHandle = context.Item("SessionHandle")
      connection.ExecMethod "SMS_SiteControlFile", "ReleaseSessionHandle",
  inParams
  End Sub

The example method has the following parameters:

<!-- p.181 -->

                                                                            ﾉ   Expand table

 Parameter     Type               Description

 connection    - SWbemServices    A valid connection to the SMS Provider.

 siteCode      - String           The site code for the Configuration Manager site.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Collections

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

<!-- p.182 -->

Windows Management Instrumentation
About the Configuration Manager Site Control File
How to Read a Configuration Manager Site Control File Embedded Property List

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.183 -->

How to Read a Configuration Manager
Site Control File Embedded Property List
Article • 10/10/2022

In Configuration Manager, you read an embedded property list from a site control file
resource by getting the SMS_EmbeddedPropertyList object for the embedded object
from the resources PropLists property array.

An embedded property list has the following properties that you can set. For more
information, see SMS_EmbeddedPropertyList.

                                                                                     ﾉ   Expand table

 Value                 Description

 PropertyListName      The embedded property name.

 Values                An array of string values. Each array item represents a single property list
                       item.

  Ｕ Caution

  Making changes to the site control file can cause irreparable damage to your
  Configuration Manager site.

To read a site control file embedded property list
   1. Set up a connection to the SMS Provider. For more information, see SMS Provider
      fundamentals.

   2. Using the connection object from step one, get a site control file resource. For
      more information, see About the Configuration Manager Site Control File.

   3. Get the SMS_EmbeddedPropertyList for the required embedded property list.

   4. Access the property list values by using the SMS_EmbeddedPropertyList object
      Values property array.

Example

<!-- p.184 -->

The following example method populates the supplied values parameter with the
Values array of the embedded property list SMS_EmbeddedPropertyList identified by the
propertyListName parameter. true is returned if the embedded property list is found;

otherwise, false is returned.

To view code that calls these functions, see How to Read and Write to the Configuration
Manager Site Control File by Using Managed Code or see How to Read and Write to the
Configuration Manager Site Control File by Using WMI.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Function GetScfEmbeddedPropertyList(resource,      _
          propertyListName,               _
          ByRef values)

        Dim scfPropertyList

        If IsNull(resource.PropLists) = True Then
            GetScfPropertyList = False
            Exit Function
        End If

        For each scfPropertyList in resource.PropLists
           if   scfPropertyList.PropertyListName = propertyListName Then
                ' Found property list, so return the values array.
                values = scfPropertyList.Values
                GetScfEmbeddedPropertyList = True
                Exit Function
            End If
         Next

       ' Did not find the property list.
       GetScfEmbeddedPropertyList = False
  End Function

  c#

  public bool GetScfEmbeddedPropertyList(
      IResultObject resource,
      string propertyListName,
      out ArrayList values)
  {
      values = new ArrayList();
      try
      {

<!-- p.185 -->

          if (resource.EmbeddedPropertyLists.ContainsKey(propertyListName))
          {
              values.AddRange(resource.EmbeddedPropertyLists[propertyListName]
  ["Values"].StringArrayValue);
              return true;
          }
      }
      catch(SmsException e)
      {
          Console.WriteLine("Couldn't get the embedded property list: " +
  e.Message);
      }
      return false;

  }

The sample method has the following parameters:

                                                                               ﾉ   Expand table

 Parameter           Type                 Description

 Resource            - Managed:           The site control file resource that contains the
                     IResultObject        embedded property.
                     - VBScript:
                     SWbemObject

 propertyListName    - Managed: String    The embedded property list to be read.
                     - VBScript: String

 Values              - Managed: String    The SMS_EmbeddedProperty class Values property. An
                     array                array of string values.
                     - VBScript: String
                     array

Compiling the Code
The C# example has the following compilation requirements:

Namespaces
System

System.Collections.Generic

System.Collections

<!-- p.186 -->

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
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.187 -->

How to Deploy a Site System Role
(Example: Fallback Status Point)
Article • 10/10/2022

The features and capabilities of a site are determined by the site roles applied to it. A
site can contain one or more site roles. Some roles depend on other roles. For more
information about specific site roles see Configure sites and hierarchies for
Configuration Manager.

Configuring a site is performed through Windows Management Instrumentation (WMI)
classes. For example, SMS_SCI_Component Server WMI Class holds information about
the server components stored on a Configuration Manager site server. These classes
derive from SMS_SiteControlItem Server WMI Class. For more information, see
Configuration Manager Site Configuration Server WMI Classes.

  ７ Note

  In earlier versions of Configuration Manager, the SMS_SiteControlFile WMI class
  was used to receive the latest copy of a site's configuration, to update a site's
  configuration, and to manage update sessions. This is no longer required as the
  changes that are made to a site's configuration are immediately written to the
  database and a file is no longer used.

Site control items generally use three types' properties for individual settings,
embedded properties, property lists, and multi-string lists. They are accessed by using
the following classes:

                                                                             ﾉ   Expand table

 Type                        WMI Class

 Embedded property           SMS_EmbeddedProperty Server WMI Class

 Embedded property list      SMS_EmbeddedPropertyList Server WMI Class (array)

 Multi-string list           SMS_Client_Reg_MultiString_List Server WMI Class (array)

To deploy a site role
   1. Set up a connection to the SMS Provider.

<!-- p.188 -->

  2. Create an instance of the SMS_SCI_SysResUse WMI class

  3. Set the NALPath , NALType , RoleName , and Sitecode properties.

  4. Depending on the role chosen, set the correct embedded properties or embedded
        property list values.

  5. Save the role.

Example
The following example creates a Fallback Status Point role:

  vbs

  Sub CreateRole(connection, computerName, siteCode, domainName)       Dim role
  Dim props    ' Create an instance of the class that defines a role        Set
  role = connection.Get("SMS_SCI_SysResUse").SpawnInstance_()       ' Configure
  the basic information of a role     role.NALPath = "[""Display=\\" &
  computerName & "." & domainName & "\""]MSWNET:[""SMS_SITE=" & siteCode &
  """]\\" & computerName & "." & domainName & "\"      role.NALType = "Windows
  NT Server"    role.RoleName = "SMS Fallback Status Point"      role.Sitecode =
  siteCode    ' Initialize the properties array     props = Array()      ' Add
  each required property to the array     SetProperty connection, props,
  "FSPInternetFacing", 0, "", ""     SetProperty connection, props, "Throttle
  Count", 10000, "", ""     SetProperty connection, props, "Throttle Interval",
  3600000, "", ""    SetProperty connection, props, "Server Remote Name", 0,
  computerName & "." & domainName, ""     ' Set the role's properties and
  commit the role    role.Props = props     role.Put_     ' Cleanup     Set role
  = Nothing    Set props = NothingEnd SubSub SetProperty(connection,
  propsArray, propertyName, intValue, strValue1, strValue2)      Dim index
  Dim foundProperty     Dim newProperty    foundProperty = False      ' Loop
  through properties until a match is found and then set the properties using
  the values passed in.     For index = 0 to UBound(propsArray)          If
  propsArray(index).PropertyName = propertyName then              foundProperty
  = true            propsArray(index).Value = intValue
  propsArray(index).Value1 = strValue1             propsArray(index).Value2 =
  strValue2             Exit For        End if    Next     ' If the property
  does not exist, then create it and set the property values using the values
  passed in.    If not foundProperty then         Set newProperty =
  connection.Get("SMS_EmbeddedProperty").SpawnInstance_
  newProperty.PropertyName = propertyName         newProperty.Value = intValue
  newProperty.Value1 = strValue1         newProperty.Value2 = strValue2
  ReDim Preserve propsArray(UBound(propsArray) + 1)          Set
  propsArray(UBound(propsArray)) = newProperty      End if     ' Cleanup      Set
  newProperty = NothingEnd Sub

  c#

<!-- p.189 -->

  public void CreateRole(WqlConnectionManager connection, string computerName,
  string siteCode, string domainName){    IResultObject role =
  connection.CreateInstance("SMS_SCI_SysResUse");     string fqdn =
  computerName + "." + domainName;    role.Properties["NALPath"].StringValue =
  string.Format(@"[""Display=\\{0}\""]MSWNET:[""SMS_SITE={1}""]\\{0}\", fqdn,
  siteCode);    role.Properties["NALType"].StringValue = "Windows NT Server";
  role.Properties["RoleName"].StringValue = "SMS Fallback Status Point";
  role.Properties["Sitecode"].StringValue = siteCode;
  WriteEmbeddedProperty(role, "FSPInternetFacing", 0, "", "");
  WriteEmbeddedProperty(role, "Throttle Count", 10000, "", "");
  WriteEmbeddedProperty(role, "Throttle Interval", 3600000, "", "");
  WriteEmbeddedProperty(role, "Server Remote Name", 0, fqdn, "");
  role.Put();}public void WriteEmbeddedProperty(IResultObject container,
  string propertyName, int value, string value1, string value2){     // Get the
  property, or create it.    IResultObject newProperty;     Dictionary<string,
  IResultObject> propertiesCopy = container.EmbeddedProperties;     if
  (propertiesCopy.ContainsKey(propertyName))    {         newProperty =
  propertiesCopy[propertyName];    }    else    {         newProperty =
  container.ConnectionManager.CreateEmbeddedObjectInstance("SMS_EmbeddedProper
  ty");        propertiesCopy.Add(propertyName, newProperty);     }
  newProperty["PropertyName"].StringValue = propertyName;
  newProperty["Value"].IntegerValue = value;
  newProperty["Value1"].StringValue = value1;
  newProperty["Value2"].StringValue = value2;     container.EmbeddedProperties
  = propertiesCopy;}

The example method has the following parameters:

                                                                           ﾉ   Expand table

 Parameter      Type                        Description

 connection     - Managed:                  A valid connection to the SMS Provider.
                WqlConnectionManager
                - VBScript: SWbemServices

 computerName   String                      The name of the site server.

 siteCode       String                      The site code.

 domainName     String                      The fully qualified domain name of the site
                                            server.

Compiling the Code
The C# example requires:

Namespaces

<!-- p.190 -->

System.Collections.Generic

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly
adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

See Also
SMS_EmbeddedProperty Server WMI Class
SMS_SCI_SysResUse Server WMI Class
About the site control file

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.191 -->

Configuration Manager Class Schema
Article • 10/10/2022

The Systems Management Server (SMS) class schema is a set of Windows Management
Instrumentation (WMI) classes that represent the objects in SMS. Each SMS class is a
template for a managed object and all instances of the object use the template. Classes
can contain properties and methods: the properties describe the class data and the
methods typically perform data management for the class.

Class categories
The following table describes the categories of classes and how the classes are used.

                                                                           ﾉ   Expand table

 Category                     Description

 Server                       Classes supported on servers running SMS.

 Advanced Client              Classes supported on SMS Advanced Clients.

See also
      Date and Time Formats

      Interpreting Bitfield Properties

      Lazy Properties

      SMS Provider Field Length Restrictions

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.192 -->

Configuration Manager Date and Time
Formats
Article • 10/10/2022

Actions, in Configuration Manager, that include date and time values are common, such
as get current date and time, 50 days from today is what date?, or find out what day of
the week falls on a certain date. When you write queries or compose reports from
information that is stored in the Configuration Manager site database, you can express
the date and time in any valid SQL format. An example is any expression that has a SQL
Server datetime data type or that can be converted implicitly, such as an appropriately
formatted character string (for example, "1998.10.31").

The times that are stored in the Configuration Manager site database can be local or in
Coordinated Universal Time (UTC). Status Message Viewer can convert to local time, but
queries and reports cannot. What you see might be seven hours later than expected, if
local time is Pacific Daylight time. Therefore, the user must be aware of the following:

Status messages are all in UTC.

Offers can be in UTC or local time, depending on a switch that is set in the Configuration
Manager console. The property in SMS_Advertisement is AssignedScheduleIsGMT
( true / false ).

Inventory is always in local time.

This property is lazy , but you can view it by using WBEMtest.

Depending on the context, you might encounter time notations in the following format:

19981118175900000000+***

The following information corresponds to the values in the previous example.

                                                                          ﾉ   Expand table

 Value                      Description

 1998                       Year

 11                         Month

 18                         Day

 1759                       Hour

<!-- p.193 -->

 Value                     Description

 00                        Second

 000000                    Microsecond

 +***                      Offset from local time

The following table lists valid datetime formats that you can use.

                                                                           ﾉ    Expand table

 Style number without       Style number with       Type             Output Style
 century                    century

 -                          0 or 100                Default          mon dd yyyy hh:mm

 1                          101                     USA              mm/dd/yyyy

 1                          102                     ANSI             yyyy.mm.dd

 3                          103                     British/French   dd/mm/yyyy

 4                          104                     German           dd.mm.yyyy

 5                          105                     Italian          dd-mm-yyyy

 6                          106                     –                dd-mon-yyyy

 7                          107                     –                mon.dd.yyy

 –                          8 or 108                –                hh:mm:ss

 –                          9 or 109                –                mon dd yyyy

                                                                     hh:mi:ss:mmmAM (or
                                                                     PM)

 10                         110                     USA              mm-dd-yy

 11                         111                     JAPAN            yy/mm/dd

 12                         112                     ISO              yymmdd

 –                          13 or 113               –                dd mon yyyy

                                                                     hh:mi:ss:mmm (24 h)

 14                         114                     –                hh:mi:ss:mmm (24 h)

<!-- p.194 -->

Besides full datetime formats, you can also use datepart formats, which are also valid
for Query Builder or for writing reports from the Configuration Manager site database.
Datepart formats provide only part of the full datetime format (for example, the year or

just the day of the month). The following table lists valid datepart formats.

                                                                            ﾉ   Expand table

 Datepart value                     Abbreviations                  Limits

 Year                               Yy                             1753-9999

 Month                              Mm                             1-12

 Day                                Dd                             1-31

 Hour                               Hh                             1-23

 Minute                             Mi                             0-59

 Second                             Ss                             0-59

 Millisecond                        Ms                             0-999

See also
Objects overview

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.195 -->

Interpreting Bitfield Properties
Article • 10/04/2022

Some SMS object properties are implemented as bit fields, where individual binary bits
of an integer (usually a uint32 data type) are used as Boolean flags to store information.
These properties can be difficult to interpret at the user interface because the bit field is
often displayed as a decimal number.

For example, the Security User Class Permissions object (SMS_UserClassPermissions)
contains an integer property called ClassPermissions, which is defined as an int32 data
type with the following bit flags:

                                                                            ﾉ   Expand table

 Bit              Flag

 0                READ

 1                MODIFY

 2                DELETE

 3                DISTRIBUTE

 4                CREATE_CHILD

 5                REMOTE_CONTROL

 6                ADVERTISE

 7                MODIFY_RESOURCE

 8                ADMINISTER

 9                DELETE_RESOURCE

 10               CREATE

 11               VIEW_COLL_FILE

 12               READ_RESOURCE

 13               DELEGATE

 14               METER

 15               MANAGESQLCOMMAND

 16               MANAGESTATUSFILTER

<!-- p.196 -->

A typical value of this bit field might be 10100000111. Bit 0 is the least significant bit (on
the right) and the other bits are counted right to left. Therefore, in this example, the
available class permissions include READ, MODIFY, DELETE, ADMINISTER, and CREATE,
corresponding to bit fields 0, 1, 2, 8, and 10, respectively.

The difficulty arises when the binary number 10100000111 appears as the decimal
number 1287 in an SMS Administrator console display and how you interpret the bits.
The solution is to open the Windows Calculator application (Calc.exe, in the Accessories
group). Use the Scientific view, set the calculator for decimal mode, and enter 1287. Use
the radio buttons of the calculator to convert to a binary display. The binary bit field
10100000111 appears. You can read the selected bit flags from this display.

  ７ Note

  In a typical bit field property, many of the bits are unused and have no defined
  meaning.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.197 -->

Lazy Properties
Article • 01/05/2024

A few SMS object properties are described as lazy. This means that the property exists
and contains data, but the data isn't available through the SMS Administrator console.
In practical terms, the property isn't visible in Query Builder.

The lazy properties generally contain data that is useless when displayed in the SMS
Administrator console. For example, the Icon[ ] property in SMS_PDF_Package is an
array of icon data that appears in the SMS Administrator console as a large amount of
uninterpretable numeric data.

Lazy properties can be accessed programmatically if you have an application that
requires the data that they store. The data can only be retrieved by explicitly calling
GetInstance on the object.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.198 -->

SMS Provider Field Length Restrictions
Article • 10/04/2022

The SMS Provider places restrictions on the width of character fields for schema classes.
If you write a program that writes to these classes, you should take these field widths
into account. Where they are used in the user interface, the SMS online Help provides
the maximum character widths. You can also determine the width by dividing the
corresponding schema class table column width by two to give the field width in
characters.

You can determine the schema class table column width from the corresponding SQL
Server views. For information about mapping schema classes to SQL Server views, see
SMS Schema View Mapping. The steps for obtaining the table column width from the
SQL Server view in SQL Server are:

      Open the SQL Server view's properties to see which table and table columns it
      uses.

      Open the corresponding table in the database Tables view to discover the column
      width.

      Classes that are commonly affected by this restriction are:

      SMS_Package

      SMS_Advertisement

      SMS_Program

      SMS_DistributionPoint

      SMS_PDF_Package

      SMS_PDF_Program

      SMS_Query

      SMS_Report

      SMS_ReportDashboard

      SMS_ReportViewSchema

      SMS_CollectionRuleQuery

      SMS_Collection

<!-- p.199 -->

     SMS_UserInstancePermissions

     SMS_UserClassPermissions

     SMS_UserInstancePermissionNames

     SMS_UserClassPermissionNames

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.200 -->

Configuration Manager Schema
Overview
Article • 10/10/2022

Configuration Manager uses Windows Management Instrumentation (WMI) to manage
its objects. Any managed object, such as a disk drive or a collection of computers, can
be represented by an instance of a Configuration Manager class. Configuration Manager
also includes classes that represent Configuration Manager features, such as software
distribution. Collectively, these Configuration Manager classes are known as the
Configuration Manager schema.

Configuration Manager uses a Microsoft SQL Server database to store managed object
data. Both SQL Server and the WMI API can be used to view and manipulate
Configuration Manager managed data. The SMS Provider acts as an intermediary
between Configuration Manager site information and WMI by supplying both class and
instance data.

Server
The Configuration Manager classes that represent the Configuration Manager server
schema are generally declared in the SMSProv.mof file. This file contains the base
classes, static classes, and methods that the SMS Provider supports. Other class
definitions, notably those that support inventory, are determined at run time by the SMS
Provider. When requested, these class definitions are supplied to WMI. These are called
run-time classes. The SMSProv.mof file is located in the \Bin\<Platform>\ directory
under the Configuration Manager install directory.

For more information about using these Configuration Manager classes by using WMI
or managed code, see Objects overview.

You can also use SQL Views for fast, read-only access to the Configuration Manager
schema data. For more information, see Configuration Manager Schema SQL Views

Client
A number of Managed Object Format (MOF) files represent the client Configuration
Manager schema. The client includes schemas that can be used for items such as
inventory, policy, and software distribution management.
