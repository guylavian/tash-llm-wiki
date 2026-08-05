---
title: "Configuration Manager SDK documentation — pages 1401-1440"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p1401-1440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p1401-1440
family: sccm
documentKind: "doc"
abstract: "{ Console.WriteLine(\"Failed. Error: \" + ex.InnerException.Message); throw; } } The example method has the following parameters: ﾉ Expand table Parameter Type Description connection - Managed: A valid connection to the SMS WqlConnectionManager Provider. - VBScript: SWbemServices"
---

# Configuration Manager SDK documentation — pages 1401-1440

<!-- p.1401 -->

      {
              Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
              throw;
      }
  }

The example method has the following parameters:

                                                                               ﾉ     Expand table

 Parameter                      Type                       Description

 connection                     - Managed:                 A valid connection to the SMS
                                WqlConnectionManager       Provider.
                                - VBScript:
                                SWbemServices

 swbemContext                   - VBScript: SWbemContext   A valid context object. For more
                                                           information, see How to Add a
                                                           Configuration Manager Context
                                                           Qualifier by Using WMI.

 siteCode                       - Managed: String          The site code.
                                - VBScript: String

 enableAutoCreateDisabledRule   - Managed: String          Enables or disables Software
                                - VBScript: String         Metering auto rule creation.

                                                           - 0 - Disabled
                                                           - 1 - Enabled

 newAutoCreatePercentage        - Managed: String          Sets the auto creation percentage.
                                - VBScript: String
                                                           0 - 100

 newAutoCreateThreshold         - Managed: String          Sets the auto creation threshold.
                                - VBScript: String

Compiling the Code
This C# example requires:

Namespaces
System

<!-- p.1402 -->

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
Configuration Manager Software Development Kit
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1403 -->

How to Create a Software Metering Rule
Article • 10/04/2022

You create a software metering rule, in Configuration Manager, by creating an instance
of the SMS_MeteredProductRule class and populating the properties.

To create software metering rule
   1. Set up a connection to the SMS Provider.

   2. Create the new software metering rule object by using the SMS_MeteredProductRule
       class.

   3. Populate the new software metering rule properties.

   4. Save the new software metering rule and properties.

Example
The following example method shows how to create a software metering rule by
creating an instance of the SMS_MeteredProductRule class and populating the properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  VB

  Sub CreateSWMRule(connection,                  _
                    newProductName,              _
                    newFileName,                 _
                    newOriginalFileName,         _
                    newFileVersion,              _
                    newLanguageID,               _
                    newSiteCode,                 _
                    newApplyToChildSites)

        ' Create the new MeteredProductRule object.
        Set newSWMRule = connection.Get("SMS_MeteredProductRule").SpawnInstance_

        ' Populate the SMS_MeteredProductRule properties.
        newSWMRule.ProductName= newProductName
        newSWMRule.FileName = newFileName
        newSWMRule.OriginalFileName = newOriginalFileName
        newSWMRule.FileVersion = newFileVersion
        newSWMRule.LanguageID = newLanguageID

<!-- p.1404 -->

     newSWMRule.SiteCode = newSiteCode
     newSWMRule.ApplyToChildSites = newApplyToChildSites

     ' Save the new rule and properties.
     newSWMRule.Put_

     ' Output new rule name.
     Wscript.Echo "Created new SWM Rule: " & newProductName

End Sub

c#

public void CreateSWMRule(WqlConnectionManager connection,
                          string newProductName,
                          string newFileName,
                          string newOriginalFileName,
                          string newFileVersion,
                          int newLanguageID,
                          string newSiteCode,
                          bool newApplyToChildSites)
{
    try
    {
        // Create the new SMS_AuthorizationList object.
        IResultObject newSWMRule =
connection.CreateInstance("SMS_MeteredProductRule");

          // Populate the new SMS_MeteredProductRule object properties.
          newSWMRule["ProductName"].StringValue = newProductName;
          newSWMRule["FileName"].StringValue = newFileName;
          newSWMRule["OriginalFileName"].StringValue = newOriginalFileName;
          newSWMRule["FileVersion"].StringValue = newFileVersion;
          newSWMRule["LanguageID"].IntegerValue = newLanguageID;
          newSWMRule["SiteCode"].StringValue = newSiteCode;
          newSWMRule["ApplyToChildSites"].BooleanValue = newApplyToChildSites;

          // Save changes.
          newSWMRule.Put();

          Console.WriteLine();
          Console.WriteLine("Created new SWM Rule: " + newProductName);
     }

    catch (SmsException ex)
    {
        Console.WriteLine("Failed to create SWM rule. Error: " +
ex.Message);
        throw;
    }

<!-- p.1405 -->

  }

The example method has the following parameters:

                                                                            ﾉ   Expand table

 Parameter              Type                        Description

 connection             - Managed:                  A valid connection to the SMS Provider.
                        WqlConnectionManager
                        - VBScript: SWbemServices

 newProductName         - Managed: String           The new product name.
                        - VBScript: String

 newFileName            - Managed: String           The new file name.
                        - VBScript: String

 newOriginalFileName    - Managed: String           The new original file name.
                        - VBScript: String

 newFileVersion         - Managed: String           The new file version.
                        - VBScript: String

 newLanguageID          - Managed: Integer          The new language ID.
                        - VBScript: Integer

 newSiteCode            - Managed: String           The new site code.
                        - VBScript: String

 newApplyToChildSites   - Managed: Boolean          Determines whether the rule will apply
                        - VBScript: Boolean         to child sites.

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

<!-- p.1406 -->

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
Configuration Manager Software Development Kit
SMS_MeteredProductRule Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1407 -->

How to Delete a Software Metering Rule
Article • 10/04/2022

You delete a software metering rule, in Configuration Manager, by loading the instance
of the software metering rule that is identified by the software metering rule ID and
calling the delete method.

To delete a software metering rule
   1. Set up a connection to the SMS Provider.

   2. Load the software metering rule object by using the SMS_MeteredProductRule
        class and a known software metering rule ID.

   3. Delete the software metering rule by using the delete method.

Example
The following example method shows how to delete a software metering rule by
loading an instance of the software metering rule that is identified by the software
metering rule ID and calling the delete method.

  ） Important

  The rule ID corresponds to the value stored in the property RuleID . The
  Configuration Manager console displays a Rule ID column, which actually
  corresponds to the value stored in the property SecurityID .

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  ' Delete a software metering rule.
   Sub DeleteSWMRule(connection,                        _
                     existingSWMRuleID)

      ' Get an existing software metering rule to delete.
      Set existingSWMRule = connection.Get("SMS_MeteredProductRule.RuleID='" &
  existingSWMRuleID & "'")

         ' Get file name for output.

<!-- p.1408 -->

       fileName = existingSWMRule.FileName

       ' Delete the software metering rule.
       existingSWMRule.Delete_

       ' Output a success message.
       Wscript.Echo "Deleted SWM rule: " & existingSWMRuleID
       Wscript.Echo "Rule name: " & fileName

   End Sub

  c#

  public void DeleteSWMRule(WqlConnectionManager connection,
                            string existingSWMRuleID)
  {
      try
      {
          // Get the specific SWM Rule to delete.

          IResultObject existingSWMRule =
  connection.GetInstance(@"SMS_MeteredProductRule.RuleID='" +
  existingSWMRuleID + "'");

           // Get file name for output message.
           string fileName = existingSWMRule["FileName"].StringValue;

           // Delete the software metering rule.
           existingSWMRule.Delete();

           // Output a success message.
           Console.WriteLine("Deleted SWM rule: " + existingSWMRuleID);
           Console.WriteLine("Rule name: " + fileName);
       }

      catch (SmsException ex)
      {
          Console.WriteLine("Failed to delete the software metering rule.
  Error: " + ex.Message);
          throw;
      }
  }

The example method has the following parameters:

                                                                  ﾉ     Expand table

<!-- p.1409 -->

 Parameter           Type                   Description

 connection          - Managed:             A valid connection to the SMS Provider.
                     WqlConnectionManager
                     - VBScript:
                     SWbemServices

 existingSWMRuleID   - Managed: String      Identifies a specific software metering rule. In
                     - VBScript: String     this case, identifies the specific software
                                            metering rule that will be deleted.

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

<!-- p.1410 -->

See Also
Configuration Manager Software Development Kit
SMS_MeteredProductRule Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1411 -->

How to Enable or Disable a Software
Metering Rule
Article • 10/04/2022

You enable or disable a software metering rule, in Configuration Manager, by loading
the instance of the software metering rule that is identified by the software metering
rule ID and then setting the Enabled value.

To enable or disable a software metering rule
   1. Set up a connection to the SMS Provider.

   2. Load the software metering rule object by using the SMS_MeteredProductRule
        class and a known software metering rule ID.

   3. Set the Enabled property to true or false .

Example
The following example method shows how to enable or disable a software metering rule
by loading the instance of the software metering rule that is identified by the software
metering rule ID and setting the Enabled property.

  ） Important

  The rule ID corresponds to the value that is stored in the property RuleID. The
  Configuration Manager console displays a Rule ID column, which actually
  corresponds to the value that is stored in the property SecurityID.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  ' Enable or disable a software metering rule.
   Sub EnableDisableSoftwareMeteringRule(connection,          _
                                        existingSWMRuleID,    _
                                        enableDisableSWMRule)

         ' Get an existing software metering rule to enable or disable.

<!-- p.1412 -->

    Set existingSWMRule = connection.Get("SMS_MeteredProductRule.RuleID='" &
existingSWMRuleID & "'")

     ' Get file name for output.
     fileName = existingSWMRule.FileName

     ' Enable or disable the rule.
     existingSWMRule.Enabled = enableDisableSWMRule

     ' Save the new rule and properties.
     existingSWMRule.Put_

     ' Output a success message.
     Wscript.Echo "SWM rule ID:    " & existingSWMRuleID
     Wscript.Echo "Rule name:      " & fileName
     Wscript.Echo "Set enabled to: " & enableDisableSWMRule

 End Sub

c#

public void EnableDisableSoftwareMeteringRule(WqlConnectionManager
connection,
                                              string existingSWMRuleID,
                                              bool enableDisableSWMRule)
{
    try
    {
        // Get the specific software metering rule to enable or disable.
        IResultObject existingSWMRule =
connection.GetInstance(@"SMS_MeteredProductRule.RuleID='" +
existingSWMRuleID + "'");

         // Get rule name for output message.
         string productName = existingSWMRule["ProductName"].StringValue;

         // Set the software metering rule.
         existingSWMRule["Enabled"].BooleanValue = enableDisableSWMRule;

         // Save changes.
         existingSWMRule.Put();

         // Output a success message.
         Console.WriteLine("SWM rule ID: " + existingSWMRuleID);
         Console.WriteLine("Rule name: " + productName);
         Console.WriteLine("Set enabled to: " + enableDisableSWMRule);
     }

    catch (SmsException ex)
    {
        Console.WriteLine("Failed to modify software metering rule. Error: "
+ ex.Message);

<!-- p.1413 -->

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

 existingSWMRuleID      - Managed: String      Identifies a specific software metering rule. In
                        - VBScript: String     this case, identifies the specific software
                                               metering rule that will be enabled or
                                               disabled.

 enableDisableSWMRule   - Managed: Boolean     Enables or disables the software metering
                        - VBScript: Boolean    rule.

                                               true - Enabled

                                               false - Disabled

Compiling the Code
This C# example requires:

Namespaces
System

System.Collections.Generic

System.Text

Microsoft.ConfigurationManagement.ManagementProvider

Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine

Assembly

<!-- p.1414 -->

adminui.wqlqueryengine

microsoft.configurationmanagement.managementprovider

Robust Programming
For more information about error handling, see About Configuration Manager Errors.

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
SMS_MeteredProductRule Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1415 -->

How to View File Usage Summary
Information
Article • 10/04/2022

You view file usage summary information, in Configuration Manager, by using the
SMS_MeteredFiles and SMS_FileUsageSummary classes.

To view file usage summary information
   1. Set up a connection to the SMS Provider.

   2. Get a collection of all of the metered files SMS_MeteredFiles.

   3. Get a collection of all of the summarized files SMS_FileUsageSummary.

   4. Loop through the summarized file information, displaying information as required.

Example
The following example method displays file usage summary information by using the
SMS_MeteredFiles and SMS_FileUsageSummary classes.

  ７ Note

  The example code below is relatively inefficient. In an environment with large
  amounts of data (large result sets), it would be better to do the query on
  SMS_MeteredFiles, then loop over that result, doing individual queries for
  SMS_FileUsageSummary where SMS_FileUsageSummary.FileID=meteredFile.FileID.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  sub ViewFileUsageSummaryInfo(connection)

  ' Get SMS_MeteredFiles - used to match FileID to a file name

  ' Build query to get all metered files.
  meteredFilesQuery = "SELECT * FROM SMS_MeteredFiles"

<!-- p.1416 -->

' Run query.
Set meteredFiles = connection.ExecQuery(meteredFilesQuery, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

' Get the summarized files.

' Build query to get all file usage summary information.
fileUsageSummaryQuery = "SELECT * FROM SMS_FileUsageSummary"

' Run query.
Set fileUsageSummary = connection.ExecQuery(fileUsageSummaryQuery, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

' Output file usage summary information.
For Each summariedFile in fileUsageSummary

       For each meteredFile in meteredFiles

          if meteredFile.MeteredFileID=summariedFile.FileID then
              wscript.echo "File Name: " & meteredFile.FileName
              Exit For
          end if

       next

       ' As matching summary information is found, output details.
       wscript.echo "File ID: "             & summariedFile.FileID
       wscript.echo "Distinct User Count: " & summariedFile.DistinctUserCount
       wscript.echo "Interval Start: "      & summariedFile.IntervalStart
       wscript.echo "Interval Width: "      & summariedFile.IntervalWidth
       wscript.echo "Site Code: "           & summariedFile.SiteCode
       wscript.echo " "

Next

end sub

c#

public void ViewFileUsageSummaryInfo(WqlConnectionManager connection)
{
    try
    {
        // Build query to get all metered files.
        string meteredFilesQuery = "SELECT * FROM SMS_MeteredFiles";

        // Run meteredFiles query.
        IResultObject meteredFilesTemp =
connection.QueryProcessor.ExecuteQuery(meteredFilesQuery);

          // Cache values to local list.

<!-- p.1417 -->

       List<IResultObject> meteredFiles = new List<IResultObject>();
       foreach (IResultObject meteredFileTemp in meteredFilesTemp)
       {
           meteredFiles.Add(meteredFileTemp);
       }

       // Build query to get all the file usage summary information.
       string fileUsageSummaryQuery = "SELECT * FROM SMS_FileUsageSummary";

        // Run fileUsageSummary query.
        IResultObject fileUsageSummaryTemp =
connection.QueryProcessor.ExecuteQuery(fileUsageSummaryQuery);

       // Cache values to local list.
       List<IResultObject> fileUsageSummary = new List<IResultObject>();
       foreach (IResultObject summariedFileTemp in fileUsageSummaryTemp)
       {
           fileUsageSummary.Add(summariedFileTemp);
       }

        // Enumerate through the files.
        foreach (IResultObject summariedFile in fileUsageSummary)
        {
            foreach (IResultObject meteredFile in meteredFiles)
            {
                if (meteredFile["MeteredFileID"].StringValue ==
summariedFile["FileID"].StringValue)
                {
                    // As matching summary information is found, output
details.
                    Console.WriteLine("File Name: " +
meteredFile["MeteredFileName"].StringValue);
                    break;
                };
            };

            // As matching summary information is found, output details.
            Console.WriteLine("File ID: " +
summariedFile["FileID"].StringValue);
            Console.WriteLine("Distinct User Count: " +
summariedFile["DistinctUserCount"].StringValue);
            Console.WriteLine("Interval Start: " +
summariedFile["IntervalStart"].StringValue);
            Console.WriteLine("Interval Width: " +
summariedFile["IntervalWidth"].StringValue);
            Console.WriteLine("Site Code: " +
summariedFile["SiteCode"].StringValue);
            Console.WriteLine(" ");
        };
    }
    catch (SmsException ex)
    {
        Console.WriteLine();
        Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
    }

<!-- p.1418 -->

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

<!-- p.1419 -->

See Also
Configuration Manager Software Development Kit
About the Configuration Manager Site Control File
How to Read and Write to the Configuration Manager Site Control File by Using
Managed Code
How to Read and Write to the Configuration Manager Site Control File by Using WMI
SMS_SCI_Component Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1420 -->

How to View Monthly Usage Summary
Information
Article • 10/04/2022

You view monthly usage summary information, in Configuration Manager, by using the
SMS_MeteredFiles, SMS_MonthlyUsageSummary, SMS_MeteredUser and SMS_R_System
classes.

  ７ Note

  The metering data is only summarized at specified intervals (by default, daily at
  midnight). Metering data does not appear in the summarized data until the
  summarization task has run.

To view monthly usage summary information
   1. Set up a connection to the SMS Provider.

   2. Get all the metered files (SMS_MeteredFiles).

   3. Get all the monthly file usage summary information
        (SMS_MonthlyUsageSummary).

   4. Get all the metered users (SMS_MeteredUser).

   5. Get all the computer names (SMS_R_System).

   6. Loop through the collections, displaying information as required.

Example
The following example method displays file usages summary information by using the
SMS_MeteredFiles and SMS_FileUsageSummary classes.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ViewMonthlySummary(connection)

<!-- p.1421 -->

    ' Get SMS_MeteredFiles - used to match FileID to a file name

       ' Build query to get all metered files.
       meteredFilesQuery = "SELECT * FROM SMS_MeteredFiles"

        ' Run query.
        Set meteredFiles = connection.ExecQuery(meteredFilesQuery, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

    ' Get SMS_MonthlyUsageSummary

       ' Build query to get all monthly summary information.
       monthlyUsageSummaryQuery = "SELECT * FROM SMS_MonthlyUsageSummary"

        ' Run query.
        Set monthlyUsageSummaries =
connection.ExecQuery(monthlyUsageSummaryQuery, , wbemFlagForwardOnly Or
wbemFlagReturnImmediately)

    'Get SMS_MeteredUser

       ' Build query to get all metered users.
       meteredUserQuery = "SELECT * FROM SMS_MeteredUser"

        ' Run query.
        Set meteredUsers = connection.ExecQuery(meteredUserQuery, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

    'Get computer names

       ' Build query to get all metered computers.
       meteredComputerQuery = "SELECT * FROM SMS_R_System"

        ' Run query.
        Set meteredComputers = connection.ExecQuery(meteredComputerQuery, ,
wbemFlagForwardOnly Or wbemFlagReturnImmediately)

    For Each summary in monthlyUsageSummaries

       For each meteredFile in meteredFiles
            if meteredFile.MeteredFileID=summary.FileID then
                wscript.echo "File Name:" & meteredFile.FileName
                Exit For
            end if
       next

       for each meteredUser in meteredUsers
            if meteredUser.MeteredUserID=summary.MeteredUserID then
                wscript.echo "User Name: " & meteredUser.FullName
                Exit For
            end if
       next

       wscript.echo "Usage Count:" & summary.UsageCount

<!-- p.1422 -->

          wscript.echo "Terminal Service Usage Count:" & summary.TSUsageCount

          for each computer in meteredComputers
               if computer.ResourceId=summary.ResourceID then
                   wscript.echo "Computer:" & computer.Name
                   Exit For
               end if
          next

          wscript.echo

     Next

end sub

c#

public void ViewMonthlySummaryInfo(WqlConnectionManager connection)
{
    try
    {
        // Get SMS_MeteredFiles - used to match FileID to a file name.

               // Build query to get all metered files.
               string meteredFilesQuery = "SELECT * FROM SMS_MeteredFiles";

            // Run meteredFiles query.
            IResultObject meteredFiles =
connection.QueryProcessor.ExecuteQuery(meteredFilesQuery);

          // Get SMS_MonthlyUsageSummary.

               // Build query to get all of the monthly file usage summary
information.
            string monthlyUsageSummaryQuery = "SELECT * FROM
SMS_MonthlyUsageSummary";

            // Run monthlyUsageSummaryQuery query.
            IResultObject monthlyUsageSummaries =
connection.QueryProcessor.ExecuteQuery(monthlyUsageSummaryQuery);

          // Get SMS_MeteredUsers.

               // Build query to get all of the metered users.
               string meteredUserQuery = "SELECT * FROM SMS_MeteredUser";

            // Run meteredUser query.
            IResultObject meteredUsers =
connection.QueryProcessor.ExecuteQuery(meteredUserQuery);

          // Get computer names.

<!-- p.1423 -->

              // Build query to get all the metered computers.
              string meteredComputersQuery = "SELECT * FROM SMS_R_System";

            // Run fileUsageSummary query.
            IResultObject meteredComputers =
connection.QueryProcessor.ExecuteQuery(meteredComputersQuery);

         // Enumerate through the lists, outputs results as matches are
found.
        foreach (IResultObject summary in monthlyUsageSummaries)
        {
            foreach (IResultObject meteredFile in meteredFiles)
            {
                if (meteredFile["MeteredFileID"].StringValue ==
summary["FileID"].StringValue)
                {
                    Console.WriteLine("File Name: " +
meteredFile["FileName"].StringValue);
                    break;
                };
            };

            foreach(IResultObject meteredUser in meteredUsers)
            {
                if (meteredUser["MeteredUserID"].StringValue ==
summary["MeteredUserID"].StringValue)
                {
                    Console.WriteLine("User Name: " +
meteredUser["FullName"].StringValue);
                    break;
                }
            };

            Console.WriteLine("Usage Count: " +
summary["UsageCount"].StringValue);
            Console.WriteLine("Terminal Service Usage Count: " +
summary["TSUsageCount"].StringValue);

            foreach(IResultObject computer in meteredComputers)
            {
                if(computer["ResourceId"].StringValue ==
summary["ResourceID"].StringValue)
                {
                    Console.WriteLine("Computer: " +
computer["Name"].StringValue);
                    break;
                }
            };

              //
              Console.WriteLine(" ");
         };
    }

<!-- p.1424 -->

      catch (SmsException ex)
      {
          Console.WriteLine("Failed. Error: " + ex.InnerException.Message);
          throw;
      }
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

<!-- p.1425 -->

.NET Framework Security
For more information about securing Configuration Manager applications, see
Configuration Manager role-based administration.

See Also
Configuration Manager Software Development Kit
SMS_MeteredFiles Server WMI Class
SMS_MeteredUser Server WMI Class
SMS_MonthlyUsageSummary Server WMI Class
SMS_R_System Server WMI Class
SMS_SummarizationInterval Server WMI Class

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1426 -->

About Software Updates Setup and
Configuration
Article • 10/04/2022

Before software update compliance assessment data is displayed in the Configuration
Manager console and before software updates can be deployed to client computers,
you must install and configure a software update point. In addition, consider the
configuration and settings for other software updates components, such as the
Windows Server Update Services (WSUS) server and the software updates client agent.
For more information, see Windows Server Update Services.

For more information about software updates, see Deploy and manage software
updates.

Software Update Point
A software update point in Configuration Manager is a required component of software
updates, and after it is installed, the software update point is displayed as a site system
role in the Configuration Manager console. The software update point site system role
must be created on a site system server that has Windows Server Update Services
(WSUS) 3.0 installed.

WSUS Server and SSL
When a Configuration Manager site server is in native mode, or when the active
software update point is configured to use Secure Sockets Layer (SSL), you must
configure five virtual roots to use a secured channel on the active software update point
server. The virtual roots are located on the Web site that the WSUS server uses, and they
are modified by using the Internet Information Services (IIS) Manager. After you have
configured the virtual roots, you must run the WSUSUtil tool to let the health
monitoring component of WSUS know that it should use SSL.

Port Settings Used by WSUS
When you create and configure a software update point in Configuration Manager, you
must specify the port settings that the WSUS 3.0 server uses.

<!-- p.1427 -->

Software Updates Client Agent
When the Software Updates Client Agent is enabled in Configuration Manager, it sends
a policy to the client computers that are assigned to the site. This policy requests that
the software updates components be enabled. The Software Updates Client Agent
components work together to perform compliance assessment scans, install software
updates at their configured deadline or when they are manually initiated, and reevaluate
whether previously installed software updates are still installed, and if not, install them
again. The Software Updates Client Agent properties are site-wide client settings.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1428 -->

How to Configure the Software Update
Point
Article • 10/04/2022

You configure the software update point, in Configuration Manager, by modifying the
site control file settings.

To configure a software update point
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the software update point resources section of the site
        control file by using the SMS_SCI_SysResUse class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the property changes to the site control file.

Example
The following example method configures various software update point settings by
using the SMS_SCI_SysResUse class to connect to the site control file and change the
software update point properties.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureSoftwareUpdatePoint(swbemServices,          _
                                   swbemContext,            _
                                   siteCode,                _
                                   newUseProxy,             _
                                   newProxyName,            _
                                   newProxyServerPort,      _
                                   newAnonymousProxyAccess)

      ' Load site control file and get software update point section.
      swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
  siteCode & """", "Refresh", , , swbemContext

         Query = "SELECT * FROM SMS_SCI_SysResUse " & _
                 "WHERE RoleName = 'SMS Software Update Point' " & _

<!-- p.1429 -->

            "AND SiteCode = '" & siteCode & "'"

    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

         ' Display the SUP server name.
         wscript.echo "SUP Server: " & SCIComponent.NetworkOSPath

       ' Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

            ' Setting: UseProxy.
            If vProperty.PropertyName = "UseProxy" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value

                ' Modify the value.
                vProperty.Value = newUseProxy
                wscript.echo "New value " & newUseProxy
            End If

            ' Setting: ProxyName.
            If vProperty.PropertyName = "ProxyName" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value2

                ' Modify the value.
                vProperty.Value2 = newProxyName
                wscript.echo "New value " & newProxyName
            End If

            ' Setting: ProxyServerPort.
            If vProperty.PropertyName = "ProxyServerPort" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value

                ' Modify the value.
                vProperty.Value = newProxyServerPort
                wscript.echo "New value " & newProxyServerPort
            End If

            ' Setting: AnonymousProxyAccess.
            If vProperty.PropertyName = "AnonymousProxyAccess" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value

               ' Modify the value.
               vProperty.Value = newAnonymousProxyAccess

<!-- p.1430 -->

                     wscript.echo "New value " & newAnonymousProxyAccess
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

public void ConfigureSoftwareUpdatePoint(WqlConnectionManager connection,
                                    string siteCode,
                                    string SUPServerName,
                                    string newUseProxy,
                                    string newProxyName,
                                    string newProxyServerPort,
                                    string newAnonymousProxyAccess)
{
    try
    {

        IResultObject siteDefinition =
connection.GetInstance("SMS_SCI_SysResUse.FileType=2,ItemName='[\"Display=\\
\\" + SUPServerName + "\\\"]MSWNET:[\"SMS_SITE=" + siteCode + "\"]\\\\" +
SUPServerName + "\\,SMS Software Update Point',ItemType='System Resource
Usage',SiteCode='" + siteCode + "'");

        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Temporary copy of the embedded properties.
            Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

                 // Setting: UseProxy.
                 if (kvp.Value.PropertyList["PropertyName"] == "UseProxy")

<!-- p.1431 -->

               {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["UseProxy"]["Value"].StringValue);

                   // Change the value by using the newUseProxy value that is
passed in.
                   embeddedProperties["UseProxy"]["Value"].StringValue =
newUseProxy;
                   Console.WriteLine("New value    : " + newUseProxy);
               }

            // Setting: ProxyName.
            if (kvp.Value.PropertyList["PropertyName"] == "ProxyName")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["ProxyName"]["Value2"].StringValue);

                   // Change the value by using the newProxyName value that is
passed in.
                   embeddedProperties["ProxyName"]["Value2"].StringValue =
newProxyName;
                   Console.WriteLine("New value    : " + newProxyName);
               }

            // Setting: ProxyServerPort.
            if (kvp.Value.PropertyList["PropertyName"] == "ProxyServerPort")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["ProxyServerPort"]["Value"].StringValue);

                // Change the value by using the newProxyServerPort value
that is passed in.
                embeddedProperties["ProxyServerPort"]["Value"].StringValue =
newProxyServerPort;
                Console.WriteLine("New value    : " + newProxyServerPort);
            }

            // Setting: AnonymousProxyAccess.
            if (kvp.Value.PropertyList["PropertyName"] ==
"AnonymousProxyAccess")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["AnonymousProxyAccess"]["Value"].StringValue);

                // Change the value by using the newAnonymousProxyAccess
value that is passed in.
                embeddedProperties["AnonymousProxyAccess"]

<!-- p.1432 -->

  ["Value"].StringValue = newAnonymousProxyAccess;
                  Console.WriteLine("New value    : " +
  newAnonymousProxyAccess);
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

                                                                           ﾉ   Expand table

 Parameter                 Type                   Description

 connection                - Managed:             A valid connection to the SMS Provider.
                           WqlConnectionManager
                           - VBScript:
                           SWbemServices

 swbemContext              - VBScript:            A valid context object. For more
                           SWbemContext           information, see How to Add a
                                                  Configuration Manager Context Qualifier by
                                                  Using WMI.

 siteCode                  - Managed: String      The site code.
                           - VBScript: String

 SUPServerName             - Managed: String      The name of the software update point
                                                  server.

 newUseProxy               - Managed: String      Determines whether to use a proxy server.
                           - VBScript: String
                                                  Possible values:

                                                  "0" = false

<!-- p.1433 -->

 Parameter                 Type                 Description

                                                "1" = true

 newProxyName              - Managed: String    The proxy server name.
                           - VBScript: String

 newProxyServerPort        - Managed: String    The proxy server port.
                           - VBScript: String

 newAnonymousProxyAccess   - Managed: String    Determines whether to use credentials to
                           - VBScript: String   connect to the proxy server. If this value is
                                                set to true, then the account used to
                                                connect needs to be set in the
                                                Configuration Manager 2007 Administrator
                                                Console.

                                                Possible values:

                                                "0" = true

                                                "1" = false

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

<!-- p.1434 -->

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
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1435 -->

How to Configure the WSUS Settings
Article • 10/04/2022

You configure the Windows Server Update Services (WSUS) component settings, in
Configuration Manager, by modifying the site control file. For more information, see
Windows Server Update Services.

To configure WSUS settings
   1. Set up a connection to the SMS Provider.

   2. Make a connection to the WSUS Configuration Manager component section of the
        site control file by using the SMS_SCI_Component class.

   3. Loop through the array of available properties, making changes as needed.

   4. Commit the property changes to the site control file.

Example
The following example method configures various Windows Server Update Services
(WSUS) component settings by using the SMS_SCI_Component class to connect to the
site control file and change properties.

  ７ Note

  For more information, see Prepare for software updates management.

For information about calling the sample code, see Calling Configuration Manager Code
Snippets.

  vbs

  Sub ConfigureWSUSSettings(swbemServices,         _
                            swbemContext,          _
                            siteCode,              _
                            newDefaultWSUSIISPort, _
                            newSSLDefaultWSUS,     _
                            newDefaultWSUSIISSSLPort)

      ' Load site control file and get the SMS_WSUS_CONFIGURATION_MANAGER
  component section.

<!-- p.1436 -->

    swbemServices.ExecMethod "SMS_SiteControlFile.Filetype=1,Sitecode=""" &
siteCode & """", "Refresh", , , swbemContext

    Query = "SELECT * FROM SMS_SCI_Component " & _
            "WHERE ComponentName = 'SMS_WSUS_CONFIGURATION_MANAGER' " & _
            "AND SiteCode = '" & siteCode & "'"

    Set SCIComponentSet = swbemServices.ExecQuery(Query,
,wbemFlagForwardOnly Or wbemFlagReturnImmediately, swbemContext)

    ' Only one instance is returned from the query.
    For Each SCIComponent In SCIComponentSet

       ' Loop through the array of embedded SMS_EmbeddedProperty instances.
       For Each vProperty In SCIComponent.Props

            ' Display the WSUS server name.
            If vProperty.PropertyName = "DefaultWSUS" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName & " Server: " &
vProperty.Value2
            End If

            ' Setting: DefaultWSUSIISPort.
            If vProperty.PropertyName = "DefaultWSUSIISPort" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value

                ' Modify the value.
                vProperty.Value = newDefaultWSUSIISPort
                wscript.echo "New value " & newDefaultWSUSIISPort
            End If

            ' Setting: SSLDefaultWSUS.
            If vProperty.PropertyName = "SSLDefaultWSUS" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value

                ' Modify the value.
                vProperty.Value = newSSLDefaultWSUS
                wscript.echo "New value " & newSSLDefaultWSUS
            End If

            ' Setting: DefaultWSUSIISSSLPort.
            If vProperty.PropertyName = "DefaultWSUSIISSSLPort" Then
                wscript.echo " "
                wscript.echo vProperty.PropertyName
                wscript.echo "Current value " & vProperty.Value

                ' Modify the value.
                vProperty.Value = newDefaultWSUSIISSSLPort
                wscript.echo "New value " & newDefaultWSUSIISSSLPort
            End If

<!-- p.1437 -->

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

public void ConfigureWSUSSettings(WqlConnectionManager connection,
                                    string siteCode,
                                    string SUPServerName,
                                    string newDefaultWSUSIISPort,
                                    string newSSLDefaultWSUS,
                                    string newDefaultWSUSIISSSLPort)
{
    try
    {
        // Connect to SMS_WSUS_CONFIGURATION_MANAGER section of the site
control file.
        IResultObject siteDefinition =
connection.GetInstance(@"SMS_SCI_Component.FileType=2,ItemType='Component',S
iteCode='" + siteCode + "',ItemName='SMS_WSUS_CONFIGURATION_MANAGER|" +
SUPServerName + "'");
        foreach (KeyValuePair<string, IResultObject> kvp in
siteDefinition.EmbeddedProperties)
        {
            // Temporary copy of the embedded properties.
            Dictionary<string, IResultObject> embeddedProperties =
siteDefinition.EmbeddedProperties;

                 // Display the WSUS server name.
                 if (kvp.Value.PropertyList["PropertyName"] == "DefaultWSUS")
                 {
                     Console.WriteLine();
                     Console.WriteLine(kvp.Value.PropertyList["PropertyName"] + "
Server");

<!-- p.1438 -->

                Console.WriteLine("Server name: " +
embeddedProperties["DefaultWSUS"]["Value2"].StringValue);
            }

            // Setting: DefaultWSUSIISPort.
            if (kvp.Value.PropertyList["PropertyName"] ==
"DefaultWSUSIISPort")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["DefaultWSUSIISPort"]["Value"].StringValue);

                // Change the value by using the newDefaultWSUSIISPort value
passed that is in.
                embeddedProperties["DefaultWSUSIISPort"]
["Value"].StringValue = newDefaultWSUSIISPort;
                Console.WriteLine("New value    : " +
newDefaultWSUSIISPort);
            }

            // Setting: SSLDefaultWSUS.
            if (kvp.Value.PropertyList["PropertyName"] == "SSLDefaultWSUS")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["SSLDefaultWSUS"]["Value"].StringValue);

                // Change the value by using the newSSLDefaultWSUS value
that is passed in.
                embeddedProperties["SSLDefaultWSUS"]["Value"].StringValue =
newSSLDefaultWSUS;
                Console.WriteLine("New value    : " + newSSLDefaultWSUS);
            }

            // Setting: DefaultWSUSIISSSLPort.
            if (kvp.Value.PropertyList["PropertyName"] ==
"DefaultWSUSIISSSLPort")
            {
                Console.WriteLine();
                Console.WriteLine(kvp.Value.PropertyList["PropertyName"]);
                Console.WriteLine("Current value: " +
embeddedProperties["DefaultWSUSIISSSLPort"]["Value"].StringValue);

                // Change the value by using the newDefaultWSUSIISSSLPort
value that is passed in.
                embeddedProperties["DefaultWSUSIISSSLPort"]
["Value"].StringValue = newDefaultWSUSIISSSLPort;
                Console.WriteLine("New value    : " +
newDefaultWSUSIISSSLPort);
            }

            // Store the settings that have changed.
            siteDefinition.EmbeddedProperties = embeddedProperties;

<!-- p.1439 -->

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

                                                                                ﾉ   Expand table

 Parameter                  Type                       Description

 connection                 - Managed:                 A valid connection to the SMS Provider.
                            WqlConnectionManager
                            - VBScript:
                            SWbemServices

 swbemContext               - VBScript: SWbemContext   A valid context object. For more
                                                       information, see How to Add a
                                                       Configuration Manager Context Qualifier
                                                       by Using WMI.

 siteCode                   - Managed: String          The site code.
                            - VBScript: String

 SUPServerName              - Managed: String          The name of the software update point
                            - VBScript: String         server.

 newDefaultWSUSIISPort      - Managed: String          The new default WSUS Internet
                            - VBScript: String         Information Services (IIS) port.

 newSSLDefaultWSUS          - Managed: String          Determines whether to use Secure
                            - VBScript: String         Sockets Layer (SSL).

 newDefaultWSUSIISSSLPort   - Managed: String          Identifies the default WSUS IIS SSL port.
                            - VBScript: String

Compiling the Code
This C# example requires:

<!-- p.1440 -->

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
