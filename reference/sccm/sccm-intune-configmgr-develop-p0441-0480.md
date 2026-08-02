---
title: "Configuration Manager SDK documentation — pages 441-480"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0441-0480
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0441-0480
family: sccm
documentKind: "doc"
abstract: "(no column name) 20118 DATEPART (datepart , date) The DATEPART function returns an integer representing the specified datepart of the specified date. Datepart is the parameter that specifies on which part of the date to return, and date is the specified date. The following examp"
---

# Configuration Manager SDK documentation — pages 441-480

<!-- p.441 -->

 (no column name)

 20118

DATEPART (datepart , date)
The DATEPART function returns an integer representing the specified datepart of the
specified date.

Datepart is the parameter that specifies on which part of the date to return, and date is
the specified date.

The following example results in the month in the specified date:

     SQL

     SELECT DATEPART (month, '2005-05-29 10:10:03.001')

                                                                         ﾉ   Expand table

 (no column name)

 5

Combining Date and Time functions
It is typical to use a combination of the Date and Time functions in Configuration
Manager reports.

The following example results in the current date and time (2005-05-29 10:10:03.001 in
this example) minus 100 days:

     SQL

     SELECT DATEADD([day], - 100, GETDATE())

                                                                         ﾉ   Expand table

 (no column name)

 2005-02-18 10:10:03.001

<!-- p.442 -->

Example query using Date and Time functions
The following query results in the total count of status messages for a one-day period.
In this query, the COUNT, GETDATE, and DATEADD functions are used as well as the
BETWEEN logical operator and the GROUP BY and ORDER BY clauses.

  SQL

  SELECT SiteCode, MessageID, COUNT(MessageID) AS [count],

  GETDATE() AS [End Date]

  FROM vStatusMessages

  WHERE ([Time] BETWEEN DATEADD([day], -1, GETDATE()) AND GETDATE())

  AND (MessageID BETWEEN '0' AND '10000')

  GROUP BY SiteCode, MessageID

  ORDER BY SiteCode, MessageID

                                                                              ﾉ   Expand table

 Site Code          MessageID             Count         End Date

 ABC                500                   190           2005-05-29 10:10:03.001

 ABC                501                   130           2005-05-29 10:10:03.001

 ABC                502                   190           2005-05-29 10:10:03.001

 ABC                1105                  85            2005-05-29 10:10:03.001

 ABC                1106                  5             2005-05-29 10:10:03.001

JOINS
To create effective reports in Configuration Manager, you need to understand how to
join different views to get the expected data. There are three types of joins: inner, outer,
and cross. In addition, there are three types of outer joins: left, right, and full. The self
join utilizes any of the above joins, but joins records from the same view.

Inner joins

<!-- p.443 -->

In an inner join, records from two views are combined and added to a query's results
only if the values of the joined fields meet certain specified criteria. If you use an inner
join by using the ResourceID to join the v_R_System and v_GS_WORKSTATION_STATUS
views, the result would be a list of all systems and their last hardware scan date.

  SQL

  SELECT v_R_System.Netbios_Name0 AS MachineName,

  v_GS_WORKSTATION_STATUS.LastHWScan AS [Last HW Scan]

  FROM v_R_System INNER JOIN v_GS_WORKSTATION_STATUS

  ON v_R_System.ResourceID = v_GS_WORKSTATION_STATUS.ResourceID

                                                                              ﾉ   Expand table

 Machine Name                           Last HW Scan

 Client1                                2005-05-29 10:10:03.001

 Client3                                2005-06-12 09:28:11.110

Outer joins
An outer join returns all rows from the joined views whether or not there's a matching
row between them. The ON clause supplements the data rather than filtering it. The
three types of outer joins (left, right, and full) indicate the main data's source. Outer
joins can be particularly helpful when you have NULL values in a view.

Left outer joins
When you use a left outer join to combine two views, all the rows in the left view are
included in the results. In the following query, the v_R_System and
v_GS_WORKSTATION_STATUS views are joined using the left outer join. The v_R_System
view is the first view listed in the query, making it the left view. The result will include a
list of all systems and their last hardware scan date. Unlike the inner join, systems that
have not been scanned for hardware will still be listed with a NULL value (as seen in the
result set).

  SQL

<!-- p.444 -->

  SELECT v_R_System.Netbios_Name0 AS MachineName,

  v_GS_WORKSTATION_STATUS.LastHWScan AS [Last HW Scan]

  FROM v_R_System LEFT OUTER JOIN v_GS_WORKSTATION_STATUS

  ON v_R_System.ResourceID = v_GS_WORKSTATION_STATUS.ResourceID

                                                                            ﾉ   Expand table

 Machine Name                          Last HW Scan

 Client1                               2005-05-29 10:10:03.001

 Client2                               NULL

 Client3                               2005-06-12 09:28:11.110

Right outer joins
A right outer join is conceptually the same as a left outer join except that all the rows
from the right view are included in the results.

Full outer join
A full outer join retrieves all the rows from both joined views. It returns all the paired
rows where the join condition is true, plus the unpaired rows from each view
concatenated with NULL rows from the other view. You usually won't want to use this
type of outer join.

Cross join
A cross join returns the product of two views, not the sum. Each row in the left view is
matched up with each row in the right view. It's the set of all possible row combinations,
without any filtering. However, if you add a WHERE clause, a cross join functions as an
inner join�it uses the condition to filter all possible row combinations down to the ones
you want.

Self join

<!-- p.445 -->

A self join uses any of the above join types, but is a view that is joined to itself. In
database diagrams, a self join is called a reflexive relationship.

NOT IN keyword phrase
Subqueries with the keyword phrase NOT IN are very useful to find information about a
set of data that doesn't meet certain criteria. In the following example, the query returns
the NetBIOS name of all computers that do NOT have Notepad.exe installed. You must
first create a query that can detect all computers that have the selected file installed as
follows:

  SQL

  SELECT DISTINCT v_R_System.Netbios_Name0

  FROM v_R_System INNER JOIN v_GS_SoftwareFile

  ON (v_GS_SoftwareFile.ResourceID = v_R_System.ResourceId)

  WHERE v_GS_SoftwareFile.FileName = 'Notepad.exe'

After confirming that the first query displays all the computers that have Notepad.exe
installed, the following sub query statement will use the NOT IN keyword phrase to find
all computer names that do NOT have the Notepad.exe file installed:

  SQL

  SELECT DISTINCT Netbios_Name0

  FROM v_R_System

  WHERE Netbios_Name0 NOT IN

  (SELECT DISTINCT v_R_System.Netbios_Name0

  FROM v_R_System INNER JOIN v_GS_SoftwareFile

  ON (v_GS_SoftwareFile.ResourceID = v_R_System.ResourceId)

  WHERE v_GS_SoftwareFile.FileName = 'Notepad.exe')

  ORDER by Netbios_Name0

See also

<!-- p.446 -->

Use query designer to write report SQL statements for Configuration Manager reports

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.447 -->

Using query designer to write report
SQL statements for Configuration
Manager reports
Article • 10/10/2022

To help you to write SQL statements for Configuration Manager reports, you can use the
query design tool found in SQL Server Management Studio. For some administrators, it
is much easier to use Query Designer in Microsoft SQL Server to create the SQL
statement for the Configuration Manager report. This tool has a variety of features that
help in designing and testing queries. For some administrators, it is much easier to use
Query Designer in Microsoft SQL Server to create the SQL statement for the
Configuration Manager report. This tool has a variety of features that help in designing
and testing queries.

Using query designer to create report queries
Writing SQL statements in the Query Designer component of the Microsoft SQL
Server�Management Studio provides a graphical interface for writing queries. You can
create a new query or copy a query from an existing Configuration Manager report,
paste the SQL statement into the SQL pane of the Query Designer, and easily add views,
create joins, select columns to display, add criteria, sort data, and so on. Query Designer
provides the following panes:

      Diagram pane: Provides the ability to join the views on specific columns and select
      the columns to display as part of the query results.
      Criteria pane: Provides the ability to create aliases for columns, configure the sort
      order for the query results, configure filters, and so on.
      SQL pane: Provides the ability to manipulate the SQL statement.
      Results pane: Provides the query results when the Execute SQL action is initiated.

Query designer considerations
When using Query Designer, you should be aware of the following points so that your
queries and reports work as expected.

Report prompt query variables

<!-- p.448 -->

Many predefined Configuration Manager reports have report prompts. These report
prompts require the user to enter a value for a specified view column. The value is
stored in a variable, and the variable is then used to filter the query result set. These
variables will not work in Query Designer, so you must change the variable to a static
value or the query will fail. The following example shows a query from a Configuration
Manager report that contains a variable representing a specific collection ID and how
this variable is modified so that Query Designer can be used:

Query from a Configuration Manager report:

  SQL

         SELECT Name
         FROM v_FullCollectionMembership
         WHERE CollectionID = @collid

Change the variable to the desired static value:

  SQL

         SELECT Name
         FROM v_FullCollectionMembership
         WHERE CollectionID = 'SMS00001'

After the query has been modified in Query Designer and is ready to be used in a
Configuration Manager report, the query can be copied into Report Builder and
modified so that the original report prompt variable replaces the static value entered
above.

Report links
If you change the column order by modifying the query in a predefined report and if the
report has a link to another report that requires a column number, the link can pass data
from the wrong column to the target report. To prevent this, verify that the correct
column numbers are specified in the link.

See also
How to create a SQL statement by using query designer

Feedback

<!-- p.449 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.450 -->

How to create a SQL statement by using
query designer
Article • 10/10/2022

Query Designer in SQL Server can help you to more easily write SQL queries that can be
used in your Configuration Manager reports. Use the following procedures to create
Configuration Manager report queries using Query Designer.

To create a new SQL query in query designer
   1. Start Microsoft SQL Server Management Studio.

   2. Navigate to <Computer Name>�\ Databases \�<Configuration Manager database
      name>�\ Views**.

   3. Right-click Views and then select New View.

   4. In the Add Table dialog box, select the Views tab and then select the views that
      you want to include in the SQL query.

        ７ Note

        You can select multiple views by holding down the CTRL key.

   5. In the design view of query designer, select the columns you want to appear in the
      report. If you are querying multiple views, you can join these by selecting a column
      in one view and dragging this over to the same column in another view.

   6. Select Execute SQL to test the query and see the results.

   7. When you are happy with the results returned by the query, copy and paste it from
      query designer to be used to create your report in Report Builder.

See also
SQL statement reference for Configuration Manager reports

Feedback

<!-- p.451 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.452 -->

SMS provider WMI schema reference in
Configuration Manager
Article • 10/10/2022

Configuration�Manager uses Windows Management Instrumentation (WMI) to manage
its objects. Any managed object, such as a disk drive or a collection of computers, can
be represented by an instance of a Configuration Manager class. Configuration Manager
also includes classes that represent features, such as software deployment or software
updates. Collectively, these Configuration Manager classes comprise the SMS Provider
WMI schema.

Configuration Manager uses a SQL Server database to store managed object data. Both
SQL Server and WMI can be used to view Configuration Manager managed data. A new
query or collection created in the Configuration Manager console uses a WMI Query
Language (WQL) query to request the Configuration Manager object data from the SMS
Provider WMI Schema, which in turn retrieves the data from the site database. When
creating a custom report in Configuration Manager, report SQL statements retrieve the
Configuration Manager object data from SQL views in the site database, which in turn
retrieve the data from one or more SQL views or tables.

SQL view and SMS provider WMI schema
relationship
Many of the SQL view and view column names used by Configuration Manager are
designed to be as close to the SMS Provider WMI schema as possible. Other SQL views
retrieve data from other views or from multiple tables or views, and there is no direct
mapping to the SMS Provider WMI schema. Also, because the SQL view and view
column names must be valid SQL identifiers, there are some discrepancies between WMI
and SQL names when there is a mapping. In most cases, the following general rules can
be applied to convert a WMI class name to its corresponding SQL view:

      At the start of the view name, v_ replaces SMS_.
      If a view name is longer than 30 characters, it is truncated.
      WMI property names are the same in the views for inventory or discovery classes.

For example, if you wanted to convert the WMI class SMS_Advertisement to the
associated SQL view, you would remove the SMS_ and replace it with v_, resulting in the
appropriate view name of v_Advertisement.

<!-- p.453 -->

SQL view query
  SQL

        SELECT AdvertisementID, PackageID, CollectionID, SourceSite
        FROM v_Advertisement

In this example, the query returns the following rows.

                                                                        ﾉ   Expand table

 AdvertismentID             PackageID            CollectionID         SourceSite

 MCM20000                   MCM00003             SMS00001             MCM

 MCM20001                   MCM00002             SMS00004             MCM

 MCM20002                   MCM00006             SMS00001             MCM

WQL query
  SQL

        SELECT AdvertisementID, PackageID, CollectionID, SourceSite
        FROM SMS_Advertisement

In this example, the query returns identical rows to the SQL view query above.

Configuration Manager SQL view design
When there is no direct mapping for a SQL view and the SMS Provider WMI schema
class and you want to determine where the data in the SQL view comes from, you can
look at the SQL view design. This helps determine whether a SQL view is retrieving data
from a single SQL table, from another SQL view, or from more than one table or view.
When the SQL view retrieves data from more than one table or view, the SQL view will
most likely map to more than one class in the SMS Provider WMI schema. Use the
following procedure to display the SQL view design.

  ２ Warning

<!-- p.454 -->

  Do not modify the design of built-in Configuration Manager SQL views as this
  might result in errors in reporting and in your site functionality.

To display the SQL view design
   1. Start Microsoft SQL Server Management Studio on the server that hosts the
     Configuration Manager site database.
   2. Navigate to <Computer Name>�\ Databases \�<Configuration Manager database
     name> \ Views.
   3. Right-click the SQL view in which you want to see the design, and then select
     Design. The SQL pane displays the SQL statement. Look at the table or view name
     just after the FROM clause to figure out where the view is retrieving its data. When
     the view retrieves data from more than one source, the table or views will use
     JOINS.

See also
Configuration Manager WMI namespaces and classes for Configuration Manager
reports

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.455 -->

Configuration Manager WMI
namespaces and classes for
Configuration Manager reports
Article • 10/10/2022

When Configuration Manager is installed, there are several Windows Management
Instrumentation (WMI) namespaces created, and depending on the namespace,
hundreds of classes can be created under each namespace. Also, each site might have
classes that other sites might not have depending on the specific site settings, the
inventory that is tracked, and so forth.

WMI namespaces created by Configuration
Manager
The following WMI namespaces are created by Configuration Manager:

      root\ccm
         root\ccm\CCMPasswordSettings
         root\ccm\CIModels
         root\ccm\CIStateStore
         root\ccm\CIStore
         root\ccm\CITasks
         root\ccm\ClientSDK
         root\ccm\ContentTransferManager
         root\ccm\DataTransferService
         root\ccm\dcm
         root\ccm\DCMAgent
         root\ccm\evaltest
         root\ccm\Events
         root\ccm\InvAgt
         root\ccm\LocationServices
         root\ccm\Messaging
         root\ccm\NetworkConfig
         root\ccm\PeerDPAgent
         root\ccm\Policy
         root\ccm\PowerManagementAgent
         root\ccm\RebootManagement
         root\ccm\ScanAgent

<!-- p.456 -->

             root\ccm\Scheduler
             root\ccm\SMSNapAgent
             root\ccm\SoftMgmtAgent
             root\ccm\SoftwareMeteringAgent
             root\ccm\SoftwareUpdates
             root\ccm\StateMsg
             root\ccm\VulnerabilityAssessment
             root\ccm\XmlStore
             root\cimv2\sms
             root\smsdm
             root\sms
             root\sms\site_<site code>

How to retrieve Configuration Manager WMI
namespaces and classes by using a Visual Basic
script
An easy way to list the Configuration Manager�related classes that have been created
on your site is to run a Microsoft Visual Basic script. The following script will scan all of
the classes within each of the WMI namespaces listed above and output the results to a
text file.

To run the script to scan the WMI namespaces and classes
   1. Copy the following code into Notepad:

         Visual Basic Script

             '======================================================================
             =================
                 '
                 ' NAME: WMIScan.vbs
                 '
                 ' AUTHOR: Microsoft Corporation
                 ' DATE : 10/24/2013 (Revised for System Center 2012 Configuration
             Manager by Rob Stack)
                 '
                 ' COMMENT: Script to scan Configuration Manager WMI classes.
                 '

             '======================================================================
             =================

<!-- p.457 -->

    Dim SearchChar
    Dim TotChar
    Dim RightChar
    Dim ClassName
    Dim Computer
    Dim strComputer
    Dim strUser
    Dim strPassword
    Dim strSiteCode
    Dim strNameSpace
    Dim strFolder
    Dim strFile
    Dim strLogFile
    Dim strFullFile
    Dim strFullLogFile
    Dim isError

    Const ForWriting = 2
    Const ForAppending = 8
    Const adOpenStatic = 3
    Const adLockOptimistic = 3
    Const adUseClient = 3

    set colNamedArguments=wscript.Arguments.Named
    If colNamedArguments.Exists("Sitecode") Then
      strSiteCode = colNamedArguments.Item("Sitecode")
    Else
      WScript.Echo "Invalid Command Line Arguments" & vbCrLf & _
        vbCrLf & "Usage: WMIScan.vbs /Sitecode:<sitecode> " & _
        "/Computer:<computername>" & vbCrLf & vbCrLf & _
        "Example1: WMIScan.vbs /Sitecode:PS1" & vbCrLf & _
        "Example2: WMIScan.vbs /Sitecode:PS1 /Computer:Computer1"
      WScript.Quit(1)
    End If
    If colNamedArguments.Exists("Computer") Then
      strComputer = colNamedArguments.Item("Computer")
    Else strComputer = "."
    End If

    'Define the values for files and folders.
    strFolder = "c:\WMIScan"
    strFile = "WMIScan.txt"
    strLogFile = "WMIScan.log"
    strFullFile = strFolder & "\" & strFile
    strFullLogFile = strFolder & "\" & strLogFile
    isError = 0

    'List of Configuration Manager namespaces are put into an array.
    arrNameSpaces =
Array("root\ccm","root\ccm\CCMPasswordSettings","root\ccm\CIModels",_
    "root\ccm\CIStateStore","root\ccm\CIStore","root\ccm\CITasks",_

"root\ccm\ClientSDK","root\ccm\ContentTransferManager","root\ccm\DataTr
ansferService",_
    "root\ccm\dcm","root\ccm\DCMAgent","root\ccm\evaltest",_

<!-- p.458 -->

    "root\ccm\Events","root\ccm\InvAgt","root\ccm\LocationServices",_

"root\ccm\Messaging","root\ccm\NetworkConfig","root\ccm\PeerDPAgent",_

"root\ccm\Policy","root\ccm\PowerManagementAgent","root\ccm\RebootManag
ement",_
    "root\ccm\ScanAgent","root\ccm\Scheduler","root\ccm\SMSNapAgent",_

"root\ccm\SoftMgmtAgent","root\ccm\SoftwareMeteringAgent","root\ccm\Sof
twareUpdates",_

"root\ccm\StateMsg","root\ccm\VulnerabilityAssessment","root\ccm\XmlSto
re",_
    "root\cimv2\sms","root\smsdm","root\sms",_
    "root\sms\site_"& strSiteCode)

    'Creates the folder and files for the scan output and log file.
    Set objFSO = CreateObject("Scripting.FileSystemObject")

    'Does strFolder Folder exist? If not, it's created.
    If Not objFSO.FolderExists(strFolder) then
      Set objFolder = objFSO.CreateFolder(strFolder)
    End If

    'Creates the WMIScan.txt and WMIScan.log files.
    Set objFile = objFSO.CreateTextFile(strFullFile)
    Set objLogFile = objFSO.CreateTextFile(strFullLogFile)
    objFile.close
    objLogFile.close

    'Opens the WMIScan.log file in write mode.
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    Set objLogFile = objFSO.OpenTextFile(strFullLogFile, ForWriting)
    objLogFile.WriteLine "********************************************"
    objLogFile.WriteLine " WMIScan Tool Executed - " & Now()
    objLogFile.WriteLine "********************************************"

    'Opens the WMIScan.txt file in write mode.
    Set objFile = objFSO.OpenTextFile(strFullFile, ForWriting)
    objLogFile.WriteLine "--------------------------------------------"
    Computer = strComputer
    If Computer = "." Then Computer = "Local System"
    objLogFile.WriteLine " Scanning WMI Namespaces On " & Computer
    objLogFile.WriteLine "--------------------------------------------"

    WScript.echo "Starting WMI scan on " & Computer

    'Create a collection of Namespaces from the array, and
    ' call the EnumNameSpaces subroutine to do the scan.
    For Each strNameSpace In arrNameSpaces
       Call EnumNameSpaces(strNameSpace, strComputer)
    Next
    objLogFile.WriteLine "---------------------------------------------
"
    objLogFile.WriteLine " Done scanning WMI Namespaces on " & Computer

<!-- p.459 -->

    objLogFile.WriteLine "---------------------------------------------
"

    'Close the WMISscan.txt file.
    objFile.close

    If isError = 1 Then
      WScript.Echo "WMI Scan has Completed with Errors!" & vbCrLf & _
      "Check the " & strLogFile & " file for more details." & vbCrLf &
_
      vbCrLf & strFile & " & " & strLogFile & " have been written to "_
      & strFolder & "."
    Else
      WScript.Echo "WMI Scan has Completed without any Errors!" & _
      vbCrLf & vbCrLf & strFile & " & " & strLogFile & _
      " have been written to " & strFolder & "."
    End If

    '***************************************************************
    '***   Subroutine to do the classes scan on the namespace.   ***
    '***************************************************************
    Sub EnumNameSpaces(strNameSpace, strComputer)
      Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
      On Error Resume next
      Set objSWbemServices= objSWbemLocator.ConnectServer
(strComputer,_
        strNameSpace)
      objLogFile.Write "Connecting to the \\" & strComputer & "\" &_
        strNameSpace & " WMI NameSpace...."
      If Err.number = 0 Then
        objLogFile.WriteLine "Success!!"
        objLogFile.Write " Scanning for Classes in "&strNameSpace _
          & "..."

       'Create a collection of all the subclasses of the namespace.
       Set colClasses = objSWbemServices.SubclassesOf()

       'Scan all WMI classes, and write them to the scan1.txt file.
       objFile.WriteBlanklines(1)
       objFile.WriteLine "\\" & strComputer & "\" & strNameSpace

        For Each objClass In colClasses
          SearchChar = instr(objClass.Path_.Path, ":")
          TotChar = len(objClass.Path_.Path)
          RightChar = TotChar - SearchChar
          ClassName = right(objClass.Path_.Path,RightChar)
          objFile.WriteLine "   " & ClassName
        Next
        objLogFile.WriteLine "Success!!"
      ElseIf Err.Number = -2147024891 Then
        objLogFile.WriteLine "Error " & Err.Number & _
          "! Connection to "& strComputer & " Failed!"
        isError = 1
      Elseif Err.Number = -2147217394 Then
        objLogFile.WriteLine "Error " & Err.Number & "!! Namespace "&_

<!-- p.460 -->

                    strNameSpace & " NOT Found!!"
                 isError = 1
               Else
                 objLogFile.WriteLine "Error " & Err.Number & "!!"
               isError = 1
               End If

             End Sub

   2. Create a folder named C:\WMIScan.

   3. Save the script as WMIScan.vbs in the C:\WMIScan folder.

   4. Open a Command Prompt window.

   5. Type C:\WMIScan\WMIScan.vbs /sitecode:ABC and then press Enter. Make sure
     to replace ABC with the appropriate site code.

        ７ Note

        The above command line assumes that the script is run from a Configuration
        Manager site server. To connect to WMI on a remote site server, use the
        /computer:<computername> argument to specify the remote computer. For
        example, to connect to site code ABC on Computer1, you would type
        C:\WMIScan\WMIScan.vbs /sitecode:ABC /computer:Computer1 in the
        command line.

The script creates a text file (in C:\WMIScan) with all of the WMI classes in each of the
WMI namespaces for Configuration Manager when run on a Configuration Manager
primary site server. A log file is also created listing all of the namespaces scanned and
whether the scan was successful. Be aware that some namespaces will not be present on
some site servers, depending on which options have been configured.

See also
SMS provider WMI schema reference in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.461 -->

List of reports in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Configuration Manager supplies many built-in reports covering many of the reporting
tasks that you might want to do. You can also use the SQL statements in these reports
to help you to write your own reports.

The following reports are included with Configuration Manager. The reports appear in
various categories.

Administrative security
The following six reports are listed under the Administrative Security category.

                                                                                  ﾉ   Expand table

 Report name                     Description

 Administration activity log     Displays a record of administrative changes made for
                                 administrative users, security roles, security scopes, and
                                 collections.

 Administrative users security   Displays administrative users, their associated security roles, and
 assignments                     the security scopes associated with each security role for each
                                 user.

 Objects secured by a single     Displays objects that an administrator assigned to only the
 security scope                  specified security scope. This report doesn't display objects that
                                 an administrator associates with more than one security scope.

 Security for a specific or      Displays securable objects, the security scopes associated with
 multiple Configuration          the objects, and which administrative users have rights to the
 Manager objects                 objects.

 Security roles summary          Displays security roles and the Configuration Manager
                                 administrators associated with each role.

 Security scopes summary         Displays security scopes and the Configuration Manager
                                 administrative users and security groups associated with each
                                 scope.

Alerts

<!-- p.462 -->

The following two reports are listed under the Alerts category.

                                                                                   ﾉ   Expand table

 Report name            Description

 Alert scorecard        Displays a summary of all postponed alerts that were generated between
                        the specified start and finish date.

 Alerts Generated       Displays a summary of the alerts that were generated most often from
 Most Often             today back to the specified date for the specified feature area.

Asset Intelligence
The following 67 reports are listed under the Asset Intelligence category.

                                                                                   ﾉ   Expand table

 Report name                           Description

 Hardware 01A - Summary of             Displays an Asset Intelligence summary view of computers
 computers in a specific collection    in a collection you specify.

 Hardware 03A - Primary                Displays users and the count of computers on which they're
 computer users                        the primary user.

 Hardware 03B - Computers for a        Displays all computers for which a specified user is the
 specific primary console user         primary console user.

 Hardware 04A - Computers with         Displays computers that don't have a primary user because
 multiple users (shared)               no one user has a signed-in time greater than 66%.

 Hardware 05A - Console users on       Displays all of the console users on a specified computer.
 a specific computer

 Hardware 06A - Computers for          Helps administrative users identify computers that need to
 which console users could not be      have security logging turned on.
 determined

 Hardware 07A - USB devices by         Displays USB devices, grouped by manufacturer.
 manufacturer

 Hardware 07B - USB devices by         Displays USB devices, grouped by manufacturer and
 manufacturer and description          description.

 Hardware 07C - Computers with a       Displays all the computers with a specified USB device.
 specific USB device

<!-- p.463 -->

Report name                          Description

Hardware 07D - USB devices on a      Displays all USB devices on a specified computer.
specific computer

Hardware 08A - Hardware that is      Displays hardware that doesn't meet the minimum hardware
not ready for a software upgrade     requirements.

Hardware 09A - Search for            Displays a summary of computers matching keyword filters.
computers                            These filters are computer name, Configuration Manager
                                     site, domain, top console user, operating system,
                                     manufacturer, or model.

Hardware 10A - Computers in a        Displays a list of computers in a specified collection where a
specified collection that have       hardware class has changed during a specified time period.
changed during a specified
timeframe

Hardware 10B - Changes on a          Displays the classes that have changed on a specified
specified computer within a          computer within a specified time period.
specified timeframe

License 01A - Microsoft Volume       Displays an inventory of all Microsoft software titles that are
License ledger for Microsoft         available from the Microsoft Volume Licensing program.
license statements

License 01B - Microsoft Volume       Identifies and displays sales channel for inventoried
License ledger item by sales         Microsoft Volume License software.
channel

License 01C - Computers with a       Identifies and displays computers that have a specified item
specific Microsoft Volume License    from the Microsoft Volume license ledger.
ledger item and sales channel

License 01D - Microsoft Volume       Identifies and displays all Microsoft Volume license ledger
License ledger products on a         items on a specified computer.
specific computer

License 02A - Count of licenses      Displays a count of licenses nearing expiration by a specified
nearing expiration by time ranges    time range. The displayed products have their licenses
                                     managed by the Software Licensing Service.

License 02B - Computers with         Displays the specified computers with licenses that are
licenses nearing expiration          nearing expiration.

License 02C - License information    Displays products on a specified computer that have their
on a specific computer               licenses managed by the Software Licensing Service.

License 03A - Count of licenses by   Displays products, by license status, which have their
license status                       licenses managed by the Software Licensing Service.

<!-- p.464 -->

Report name                         Description

License 03B - Computers with a      Displays products, with a specified license status, whose
specific license status             licenses are managed by the Software Licensing Service.

License 04A - Count of products     Displays a count of products that have their licenses
managed by software licensing       managed by the Software Licensing Service.

License 04B - Computers with a      Displays computers, managed by the Software Licensing
specific product managed by         Service, that include a specified product.
Software Licensing Service

License 05A - Computers             Displays computers that act as Key Management Servers.
providing Key Management
Service

License 06A - Processor counts      Displays the number of processors on computers using
for per-processor licensed          Microsoft products that support per-processor licensing.
products

License 06B - Computers with a      Displays a list of computers where a specified Microsoft
specific product that supports      product that supports per-processor licensing is installed.
per-processor licensing

License 14A - Microsoft Volume      Displays reconciliation on software licenses acquired
Licensing reconciliation report     through Microsoft Volume License Agreement and the
                                    actual inventory count.

License 14B - List of Microsoft     This report displays Microsoft software titles in use that
software inventory not found in     aren't found in the Microsoft Volume License Agreement.
MVLS

License 15A - General license       Displays reconciliation on general software licenses acquired
reconciliation report               and the actual inventory count.

License 15B - General license       Displays computers that installed the licensed product with
reconciliation report by computer   a specified version.

Software 01A - Summary of           Displays a summary of installed software ordered by the
installed software in a specific    number of instances found from inventory.
collection

Software 02A - Product families     Displays the product families and the count of software in
for a specific collection           the family for a specified collection.

Software 02B - Product categories   Displays the product categories in a specified product family
for a specific product family       and the count of software within the category.

Software 02C - Software in a        Displays all software that is in the specified product family
specific product family and         and category.
category

<!-- p.465 -->

Report name                         Description

Software 02D - Computers with       Displays all computers with specified software installed.
specific software installed

Software 02E - Installed software   Displays all software installed on a specified computer.
on a specific computer

Software 03A - Uncategorized        Displays the software that is either categorized as unknown
software                            or has no categorization.

Software 04A - Software             Displays a list of software configured to automatically run
configured to automatically run     on computers.
on computers

Software 04B - Computers with       Displays all computers with specified software configured to
specific software configured to     automatically run.
automatically run

Software 04C - Software             Displays installed software configured to automatically run
configured to automatically run     on a specified computer.
on a specific computer

Software 05A - Browser Helper       Displays the browser helper objects installed on computers
Objects                             in a specified collection.

Software 05B - Computers with a     Displays all of the computers with a specified browser
specific Browser Helper Object      helper object.

Software 05C - Browser Helper       Displays all browser helper objects on the specified
Objects on a specific computer      computer.

Software 06A - Search for           This report provides a summary of installed software. It
installed software                  searches based on the following criteria: product name,
                                    publisher, or version.

Software 06B - Software by          Displays a summary of installed software based on a
product name                        specified product name.

Software 07A - Recently used        Displays executable programs that users recently used. It
executable programs by the          also includes the count of computers on which users used
count of computers                  the program. Software metering must be enabled for this
                                    site to view this report.

Software 07B - Computers that       Displays the computers on which users recently used a
recently used a specified           specified executable program. This report requires that you
executable program                  enable the software metering client setting.

Software 07C - Recently used        Displays executable files that users recently used on a
executable programs on a            specified computer. This report requires that you enable the
specified computer                  software metering client setting.

<!-- p.466 -->

Report name                           Description

Software 08A - Recently used          Displays executable programs that users recently used. It
executable programs by the            also includes a count of users that most recently used the
count of users                        program. This report requires that you enable the software
                                      metering client setting.

Software 08B - Users that recently    Displays the users that most recently used a specified
used a specified executable           executable program. This report requires that you enable
program                               the software metering client setting.

Software 08C - Recently used          Displays executable programs that the specified user used
executable programs by a              recently. This report requires that you enable the software
specified user                        metering client setting.

Software 09A - Infrequently used      Displays software titles that users haven't used during a
software                              specified period of time.

Software 09B - Computers with         Displays computers with installed software that users
infrequently used software            haven't used for a specified period of time. The specified
installed                             period of time is based on the value specified in the
                                      'Software 09A - Infrequently used software' report.

Software 10A - Software titles        Displays software titles based on matching of all specified
with specific multiple custom         custom label criteria. Up to three custom labels can be
labels defined                        selected to refine a software title search.

Software 10B - Computers with a       Displays all computers in this collection that have the
specific custom-labeled software      specified custom-labeled software title installed.
title installed

Software 11A - Software titles with   Displays software titles based on matching of at least one of
a specific custom label defined       the specified custom label criteria.

Software 12A - Software titles        Displays all software titles that don't have a custom label
without a custom label                defined.

Software 14A - Search for             Displays a count of installed software with a software
software identification tag           identification tag enabled.
enabled software

Software 14B - Computers with         Displays all computers that have installed software with a
specific software identification      specified software identification tag enabled.
tag enabled software installed

Software 14C - Installed software     Displays all installed software with a specified software
identification tag enabled            identification tag enabled on a specified computer.
software on a specific computer

Lifecycle 01A - Computers with a      View a list of computers on which a specified product is
specific software product             detected.

<!-- p.467 -->

 Report name                               Description

 Lifecycle 02A - List of machines          View computers that have expired products on them. You
 with expired products in the              can filter this report by product name.
 organization

 Lifecycle 03A - List of expired           View details for products in your environment that have
 products found in the                     expired lifecycle dates.
 organization

 Lifecycle 04A - General Product           View a list of product lifecycles. Filter the list by product
 Lifecycle overview                        name and days to expiration.

 Lifecycle 05A - Product lifecycle         Starting in version 1810, this report includes similar
 dashboard                                 information as the in-console dashboard.

Client push
The following four reports are listed under the Client Push category.

                                                                                         ﾉ    Expand table

 Report name                                     Description

 Client push installation status details         Displays information about the client push installation
                                                 process for all sites.

 Client push installation status details         Displays information about the client push installation
 for a specified site                            process for a specified site.

 Client push installation status summary         Displays a summary view of the client push installation
                                                 status for all sites.

 Client push installation status summary         Displays a summary view of the client push installation
 for a specified site                            status for a specified site.

Client status
The following seven reports are listed under the Client Status category.

                                                                                         ﾉ    Expand table

 Report name              Description

 Client remediation       Displays details of client remediation actions for a collection you specify.
 details

<!-- p.468 -->

 Report name              Description

 Client remediation       Displays a summary of client remediation actions for a specified
 summary                  collection.

 Client status history    Displays a historical view of overall client status in the site.

 Client status            Displays the client check results of active clients for a given collection.
 summary

 Client time to           Displays the percentage of clients that requested policy at least once in
 request policy           the last 30 days. Each day represents a percentage of total clients that
                          requested policy since the first day in the cycle.

 Clients with failed      Displays details about clients that client check failed for a specified
 client check details     collection.

 Inactive clients         Displays a detailed list of inactive clients for a given collection.
 details

Company resource access
The following three reports are listed under the Company Resource Access category.

                                                                                        ﾉ    Expand table

 Report name                     Description

 Certificate issuance history    Displays the history of certificates issued by the certificate
                                 registration point to users and devices for the specified date range.

 List of assets by certificate   Displays the devices or users in a specified certificate issuance state
 issuance status                 following the evaluation of a specified certificate profile.

 List of assets with             Displays the devices or users with certificates that expire on or
 certificates nearing expiry     before the specified date.

Compliance and settings management
The following 22 reports are listed under the Compliance and Settings Management
category.

                                                                                        ﾉ    Expand table

<!-- p.469 -->

Report name                           Description

Compliance history of a               Displays the history of the changes in compliance of a
configuration baseline                configuration baseline for the specified date range.

Compliance history of a               Displays the history of the changes in compliance of a
configuration item                    configuration item for the specified date range.

Details of compliant rules of         Displays information about the rules evaluated as
configuration items in a              compliant for a specified configuration item for a specified
configuration baseline for an asset   device or user.

Details of conflicting rules of       Displays information about rules in a deployed
configuration items in a              configuration item that conflict with other rules. Include
configuration baseline for an asset   the other rules in the same or another deployed
                                      configuration item.

Details of errors of configuration    Displays information about errors generated by a
items in a configuration baseline     specified configuration item for a specified device or user.
for an asset

Details of non-compliant rules of     Displays information about rules that were evaluated as
configuration items in a              noncompliant for a specified configuration item, for a
configuration baseline for an asset   specified device or user.

Details of remediated rules of        Displays information about rules that were remediated by
configuration items in a              a specified configuration item for a specified device or
configuration baseline for an asset   user.

List of assets by compliance state    Displays the devices or users in a specified compliance
for a configuration baseline          state following the evaluation of a specified configuration
                                      baseline.

List of assets by compliance state    Displays the devices or users in a specified compliance
for a configuration item in a         state following the evaluation of a specified configuration
configuration baseline                item.

List of noncompliant Apps and         Displays information about users and devices that have
Devices for a specified user          apps installed that aren't compliant with a policy you
                                      specified.

List of rules conflicting with a      Displays a list of rules that conflict with a specified rule for
specified rule for an asset           a deployed configuration item.

List of unknown assets for a          Displays a list of devices or users that haven't yet reported
configuration baseline                any compliance data for a specified configuration
                                      baseline.

List of unknown assets for a          Displays a list of devices or users that haven't yet reported
configuration item                    any compliance data for a specified configuration item.

<!-- p.470 -->

 Report name                           Description

 Rules and errors summary of           Displays a summary of the compliance state of the rules
 configuration items in a              and any setting errors for a specified configuration item.
 configuration baseline for an asset   The configuration item must be deployed to a device or
                                       user.

 Summary compliance by                 Displays a summary of the overall compliance of deployed
 configuration baseline                configuration baselines in the hierarchy.

 Summary compliance by                 Displays a summary of the compliance of configuration
 configuration items for a             items in a specified configuration baseline.
 configuration baseline

 Summary compliance by                 Displays a summary of the compliance of configuration
 configuration policies                policies.

 Summary compliance of a               Displays a summary of the overall compliance of a
 configuration baseline for a          specified configuration baseline. The configuration item
 collection                            must be deployed to the specified collection.

 Summary of Users who have             Displays information about users that have apps installed
 Noncompliant Apps                     that aren't compliant with a policy you specified.

 Terms and Conditions acceptance       Displays Terms and Conditions items and which version
                                       each user has accepted.

Data warehouse
The following seven reports are listed under the Data warehouse category.

                                                                                 ﾉ    Expand table

 Report name                           Description

 Application Deployment                Historical: View details for application deployment for a
                                       specific application and machine.

 Endpoint Protection and Software      Historical: View computers that are missing software
 Update Compliance                     updates.

 General Hardware Inventory            Historical: View all hardware inventory for a specific
                                       machine.

 General Software Inventory            Historical: View all software inventory for a specific
                                       machine.

 Infrastructure Health Overview        Historical: Displays an overview of the health of your
                                       Configuration Manager infrastructure.

<!-- p.471 -->

 Report name                             Description

 List of Malware Detected                Historical: View malware that has been detected in the
                                         organization.

 Software Distribution Summary           Historical: A summary of software distribution for a
                                         specific advertisement and machine.

Device management
The following 37 reports are listed under the Device Management category.

  ７ Note

  Configuration Manager version 2006 dropped support for Windows CE 7.0 as a
  client. Deprecation was announced with version 1906.

                                                                                 ﾉ    Expand table

 Report name                                Description

 All corporate-owned mobile devices         Displays all corporate owned mobile devices.

 All mobile device clients                  Displays information about all mobile device clients.
                                            Devices that are managed by the Exchange Server
                                            connector aren't included.

 Certificate issues on mobile devices       Displays detailed information about certificate issues
 that are managed by the Configuration      on mobile devices that are managed by the
 Manager client for Windows CE and          Configuration Manager client for Windows CE.
 that are not healthy

 Client deployment failure for mobile       Displays detailed information about deployment
 devices that are managed by the            failure for mobile devices that are managed by the
 Configuration Manager client for           Configuration Manager client for Windows CE.
 Windows CE

 Client deployment status details for       Displays information about the status of mobile
 mobile devices that are managed by         devices that are managed by the Configuration
 the Configuration Manager client for       Manager client for Windows CE.
 Windows CE

 Client deployment success for mobile       Displays detailed information about deployment
 devices that are managed by the            success for mobile devices that are managed by the
 Configuration Manager client for           Configuration Manager client for Windows CE.
 Windows CE

<!-- p.472 -->

Report name                               Description

Communication issues on mobile            This report contains detailed information about
devices that are managed by the           communication issues on mobile devices that are
Configuration Manager client for          managed by the Configuration Manager client for
Windows CE and that are not healthy       Windows CE.

Compliance status of default ActiveSync   Displays a summary of the compliance status with the
mailbox policy for the mobile devices     Default Exchange ActiveSync mailbox policy for the
that are managed by the Exchange          mobile devices managed by the Exchange Server
Server connector                          connector.

Count of mobile devices by display        This report displays the number of mobile devices by
configurations                            display settings.

Count of mobile devices by operating      Displays the number of mobile devices by operating
system                                    system.

Count of mobile devices by program        Displays the number of mobile devices by program
memory                                    memory.

Count of mobile devices by storage        Count of mobile devices by storage memory
memory configurations                     configurations

Health information for mobile devices     Displays detailed health information for mobile
that are managed by the Configuration     devices that are managed by the Configuration
Manager client for Windows CE             Manager client for Windows CE.

Health summary for mobile devices         Displays health summary information for mobile
that are managed by the Configuration     devices that are managed by the Configuration
Manager client for Windows CE             Manager client for Windows CE.

Inactive mobile devices that are          Displays the mobile devices managed by the
managed by the Exchange Server            Exchange Server connector that haven't connected to
connector                                 an Exchange Server in a specified number of days.

List of devices by Health Attestation     Displays a list of devices with attributes reported by
state                                     Health Attestation Service

List of Devices enrolled per user in      Displays all devices a user has enrolled with Microsoft
Microsoft Intune                          Intune.

List of devices in a specific device      Displays information for all devices within a specific
category                                  device category.

Local client issues on mobile devices     This report contains detailed information about local
that are managed by the Configuration     client issues on mobile devices that are managed by
Manager client for Windows CE and         the Configuration Manager client for Windows CE.
that are not healthy

Mobile device client information          Displays information about the mobile devices that
                                          have the Configuration Manager client installed. You

<!-- p.473 -->

Report name                               Description

                                          can use this report to verify which mobile devices can
                                          successfully communicate with a management point.

Mobile device compliance details for      Displays the mobile device compliance details for a
the Exchange Server connector             default Exchange ActiveSync mailbox policy that is
                                          configured by using the Exchange Server connector.

Mobile devices by operating system        Displays the mobile devices by operating system.

Mobile devices that are jailbroken or a   Displays the mobile devices that are jailbroken or a
rooted device                             rooted device.

Mobile devices that are unmanaged         Displays the mobile devices that completed
because they enrolled but failed to       enrollment with Configuration Manager, have a
assign to a site                          certificate, but failed to complete site assignment.

Mobile devices with a specific amount     Displays all mobile devices with their specified
of free program memory                    amount of free program memory.

Mobile devices with a specific amount     Displays all mobile devices with the specified amount
of free removable storage memory          of free removable memory.

Mobile devices with certificate renewal   Displays the enrolled mobile devices that failed to
issues                                    renew their certificate. If you don't renew the
                                          certificate before the expiry period, the mobile
                                          devices become unmanaged.

Mobile devices with low free program      Displays the mobile devices for which the program
memory (less than specified KB free)      memory is lower than a specified size in KB.

Mobile devices with low free removable    Displays the mobile devices for which the removable
storage memory (less than specified KB    storage memory is lower than a specified size in KB.
free)

Number of devices enrolled per user in    Displays the users enabled for the Microsoft Intune
Microsoft Intune                          subscription. It also shows the total number of devices
                                          enrolled for each user.

Pending retire and wipe request for       Displays the wipe requests that are pending for
mobile devices                            mobile devices.

Recently enrolled and assigned mobile     Displays mobile devices that recently enrolled with
devices                                   Configuration Manager and successfully assigned to a
                                          site.

Recently wiped mobile devices             Displays the list of mobile devices that were recently
                                          successfully wiped.

Settings summary for mobile devices       Displays the number of mobile devices that apply the
that are managed by the Exchange          settings for each Default Exchange ActiveSync mailbox

<!-- p.474 -->

 Report name                                    Description

 Server connector                               policy managed by the Exchange Server connector.

 Windows RT Sideloading Keys Detailed           Displays detailed status information for a specified
 Status                                         Windows RT sideloading key.

 Windows RT Sideloading Keys                    Displays the status of Windows RT sideloading keys.
 Summary

Driver management
The following 13 reports are listed under the Driver Management category.

                                                                                      ﾉ    Expand table

 Report name                                        Description

 All drivers                                        Displays a list of all drivers.

 All drivers for a specific platform                Displays all drivers for a specified platform.

 All drivers in a specific boot image               Displays all drivers in a specified boot image.

 All drivers in a specific category                 Displays all drivers in a specified category.

 All drivers in a specific package                  Displays all drivers in a specified package.

 Categories for a specific driver                   Displays categories for a specified driver.

 Computers that failed to install drivers for a     Displays computers that failed to install drivers
 specific collection                                for a specified collection.

 Driver catalog matching report for a specific      Displays the driver catalog matching report for a
 collection                                         specified collection.

 Driver catalog matching report for a specific      Displays the driver catalog matching report for a
 computer                                           specified computer.

 Driver catalog matching report for a specific      Displays the driver catalog matching report for a
 device on a specific computer                      specified device on a specified computer.

 Driver catalog matching report for                 Displays driver catalog matching report for
 computers in a specific collection with a          computers in a specified collection with a
 specific device                                    specified device.

 Drivers that failed to install on a specific       Displays drivers that failed to install on a specified
 computer                                           computer.

<!-- p.475 -->

 Report name                                     Description

 Supported platforms for a specific Driver       Displays supported platforms for a specified
                                                 driver.

Endpoint Protection
The following six reports are listed under the Endpoint Protection category.

                                                                                   ﾉ   Expand table

 Report name                       Description

 Antimalware activity report       Displays an overview of antimalware activity.

 Antimalware overall status and    Displays the antimalware overall status and history.
 history

 Computer malware details          Displays details about a specified computer and the list of
                                   malware found on it.

 Infected computers                Displays a list of computers with a specified threat detected.

 Top users by threats              Displays the list of users with the most number of detected
                                   threats.

 User threat list                  Displays the list of threats found for a specified user account.

Hardware - CD-ROM
The following four reports are listed under the Hardware - CD-ROM category.

                                                                                   ﾉ   Expand table

 Report name                         Description

 CD-ROM information for a            Displays information about the CD-ROM drives on a
 specific computer                   specified computer.

 Computers for a specific CD-ROM     Displays a list of computers that contain a CD-ROM drive
 manufacturer                        made by a manufacturer you specify.

 Count CD-ROM drives per             Displays the number of CD-ROM drives inventoried per
 manufacturer                        manufacturer.

 History - CD-ROM history for a      Displays the inventory history for CD-ROM drives on a

<!-- p.476 -->

 Report name                           Description

 specific computer                     specified computer.

Hardware - Disk
The following eight reports are listed under the Hardware - Disk category.

                                                                                   ﾉ   Expand table

 Report name                           Description

 Computers with a specific hard        Displays a list of computers that have hard disks of a
 disk size                             specified size.

 Computers with low free disk          Displays a list of computers in a specified collection that
 space (less than specified % free)    have less that the specified free disk space.

 Computers with low free disk          Displays a list of computers and disks where the disks are
 space (less that specified MB free)   low on space. The amount of free space to check for is
                                       specified in MB.

 Count physical disk configurations    Displays the number of hard disks inventoried by disk
                                       capacity.

 Disk information for a specific       Displays summary information about the logical disks on a
 computer - Logical disks              specified computer.

 Disk information for a specific       Displays summary information about the disk partitions on
 computer - Partitions                 a specified computer.

 Disk information for a specific       Displays summary information about the physical disks on a
 computer - Physical disks             specified computer.

 History - Logical disk space          Displays the inventory history for logical disk drives on a
 history for a specific computer       specified computer.

Hardware - General
The following five reports are listed under the Hardware - General category.

                                                                                   ﾉ   Expand table

 Report name                            Description

 Computer information for a specific    Displays summary information for a specified computer.
 computer

<!-- p.477 -->

 Report name                         Description

 Computers in a specific workgroup   Displays a list of computers in a specified Workgroup or
 or domain                           domain.

 Inventory classes assigned to a     Displays the inventory classes that are assigned to a
 specific collection                 specified collection.

 Inventory classes enabled on a      Displays the inventory classes that are enabled on a
 specific computer                   specified computer.

 Windows Autopilot Device            Displays client device information that is needed for
 Information                         Windows Autopilot registration.

Hardware - Memory
The following five reports are listed under the Hardware - Memory category.

                                                                              ﾉ    Expand table

 Report name                         Description

 Computers where physical memory     Displays a list of computers where the amount of RAM
 has changed                         has changed since the last inventory cycle.

 Computers with a specific amount    Displays a list of computers that have a specified amount
 of memory                           of RAM (Total Physical Memory rounded to the nearest
                                     MB).

 Computers with low memory (less     Displays a list of computers that are low on memory. The
 than or equal to specified MB)      amount of memory to check for is specified in MB.

 Count memory configurations         Displays the number of computers inventoried by amount
                                     of RAM.

 Memory information for a specific   Displays summary information about the memory on a
 computer                            specified computer.

Hardware - Modem
The following three reports are listed under the Hardware - Modem category.

                                                                              ﾉ    Expand table

<!-- p.478 -->

 Report name                           Description

 Computers for a specific modem        Displays a list of computers that have a modem made by a
 manufacturer                          specified manufacturer.

 Count modems by manufacturer          Displays the number of modems inventoried for each
                                       modem manufacturer.

 Modem information for a specific      Displays summary information about the modem on a
 computer                              specified computer.

Hardware - Network adapter
The following three reports are listed under the Hardware - Network Adapter category.

                                                                                 ﾉ   Expand table

 Report name                             Description

 Computers with a specific network       Displays a list of computers that have a specified
 adapter                                 network adapter.

 Count network adapters by type          Displays the number of inventoried network adapters
                                         cards of each type.

 Network adapter information for a       Displays information about the network adapters
 specific computer                       installed on a specified computer.

Hardware - Processor
The following five reports are listed under the Hardware - Processor category.

                                                                                 ﾉ   Expand table

 Report name                                  Description

 Computers for a specific processor speed     Displays a list of computers that have a processor
                                              of a specified speed.

 Computers with fast processors (greater      Displays a list of computers that have processors
 than or equal to a specified clock speed)    with a speed that is faster than the specified speed.

 Computers with slow processors (less than    Displays a list of computers that have processors
 or equal to a specified clock speed)         that run at or slower than a specified clock speed.

 Count processor speeds                       Displays the number of computers inventoried by

<!-- p.479 -->

 Report name                                    Description

                                                processor speed.

 Processor information for a specific           Displays information about the processors installed
 computer                                       on a specified computer.

Hardware - SCSI
The following five reports are listed under the Hardware - SCSI category.

                                                                                 ﾉ   Expand table

 Report name                            Description

 Computers with a specific SCSI card    Displays a list of computers that have a specified SCSI
 type                                   card installed.

 Count SCSI card types                  Displays the number of inventoried SCSI cards by card
                                        type.

 SCSI card information for a specific   Displays information about the SCSI cards installed on a
 computer                               specified computer.

Hardware - Security
The following one report is listed under the Hardware - Security category.

                                                                                 ﾉ   Expand table

 Report name                  Description

 Details of firmware states   Displays the details of the states of UEFI, SecureBoot, and TPM.
 on devices                   Note: This report isn't in version 1810.

Hardware - Sound card
The following three reports are listed under the Hardware - SCSI category.

                                                                                 ﾉ   Expand table

<!-- p.480 -->

 Report name                            Description

 Computers with a specific sound        Displays a list of computers that have a specified sound
 card                                   card.

 Count sound cards                      Displays the number of computers inventoried by each
                                        sound card type.

 Sound card information for a           Displays summary information about the sound cards on
 specific computer                      a specified computer.

Hardware - Video card
The following three reports are listed under the Hardware - Video Card category.

                                                                                   ﾉ   Expand table

 Report name                     Description

 Computers with a specific       Displays a list of computers that have a specified video card.
 video card

 Count video cards by type       Displays a list of all of the video cards installed on computers. It
                                 also shows the number of each type of video card.

 Video card information for a    Displays summary information about the video cards installed
 specific computer               on a specified computer.

Migration
The following five reports are listed under the Migration category.

                                                                                   ﾉ   Expand table

 Report name                                Description

 Clients in exclusion list                  Displays clients that are excluded from migration.

 Dependency on a Configuration              Displays the objects that depend on a collection of
 manager collection                         the source hierarchy.

 Migration job properties                   This report shows the contents of the specified
                                            migration job.

 Migration jobs                             This report shows the list of migration jobs.
