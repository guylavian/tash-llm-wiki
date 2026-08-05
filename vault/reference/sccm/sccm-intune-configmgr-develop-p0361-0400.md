---
title: "Configuration Manager SDK documentation — pages 361-400"
type: reference
domain: sccm
slug: sccm-intune-configmgr-develop-p0361-0400
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-develop-p0361-0400
family: sccm
documentKind: "doc"
abstract: "object type 3 is for task sequence. The view can be joined to other Wake On LAN views by using the ObjectType column. v_WOLGetWOLEnabledSites Lists the sites where Wake On LAN is enabled, by site code and site server name. It is unlikely that this view will be joined with other"
---

# Configuration Manager SDK documentation — pages 361-400

<!-- p.361 -->

object type 3 is for task sequence. The view can be joined to other Wake On LAN views
by using the ObjectType column.

v_WOLGetWOLEnabledSites
Lists the sites where Wake On LAN is enabled, by site code and site server name. It is
unlikely that this view will be joined with other views.

v_WOLSUMTargetedClients
Lists the Configuration Manager clients, by ResourceID, where a software deployment
that has Wake On LAN enabled targets the client. The object type, object ID (unique
assignment ID of the deployment), assigned site, and current time zone are also listed.
The view can be joined to other views by using the ResourceID and ObjectID columns.

v_WOLSWDistTargetedClients
Lists the Configuration Manager clients, by ResourceID, where a software deployment
that has Wake On LAN enabled targets the client. The object type, object ID
(advertisement ID of the deployment), assigned site, and current time zone are also
listed. The view can be joined to other views by using the ResourceID and ObjectID
columns.

v_WOLTargetedClients
Lists the Configuration Manager clients, by ResourceID, where an object that has Wake
On LAN enabled targets the client, such as a software deployment, software update, or
task sequence deployment. The object type, object ID, assigned site, and current time
zone are also listed. The view can be joined to other views by using the ResourceID and
ObjectID columns, and to the v_WOLGetSupportedObjects view by using the
ObjectType column.

v_WOLTSTargetedClients
Lists the Configuration Manager clients, by ResourceID, where a task sequence
deployment that has Wake On LAN enabled targets the client. The object type, object ID
(advertisement ID of the task sequence deployment), assigned site, and current time
zone are also listed. The view can be joined to other views by using the ResourceID and
ObjectID columns.

<!-- p.362 -->

v_WOLWorkstationInfo
Lists all Wake On LAN�enabled clients, by ResourceID and MachineName, the assigned
site, and the current time zone. The view can be joined to other views by using the
ResourceID column.

Wake On LAN status views
The Wake On LAN status view contains information about the Wake On LAN error
messages. For more information about the status views, see Status and Alert Views in
Configuration Manager. The status view that contains Wake On LAN information is
described in this section.

v_WOLCommunicationErrorStatus
Lists the Wake On LAN error status messages that have been reported, including
message description and time of the error. The BatchID, ObjectType, and ID columns
contain status message attributes, such as an advertisement ID or unique configuration
item ID. The view can be joined to other views by using the BatchID, ObjectType, and ID
columns.

See also
SQL Server views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.363 -->

Evaluation of the All collections report
in Configuration Manager
Article • 10/04/2022

The All collections report is one of the built-in reports in Configuration Manager and is
a good example of a basic report. This report lists all of the collections in the
Configuration Manager hierarchy.

To open the report, use the following procedure:

To examine the properties of the All collections
report
   1. In the Configuration Manager console, select Monitoring.
   2. In the Monitoring workspace, expand Reporting, and then select Reports.
   3. From the list of reports, select All collections and then, in the Home tab, in the
      Report Group group, select Edit.
   4. In the Report Data pane of Report Builder, expand Datasets and then double-click
      DataSet0.
   5. In the Dataset Properties dialog box, you can view the SQL query for the report,
      the fields that will be returned, and the parameters that the report uses.
   6. Close the Dataset Properties dialog box.
   7. Close Report Builder.

See also
Evaluation of the computer information for a specific computer report in Configuration
Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.364 -->

Evaluation of the Computer information
for a specific computer report in
Configuration Manager
Article • 10/04/2022

The Computer information for a specific computer report is one of the predefined
reports in Configuration Manager, and is a good example of a report that combines
multiple SQL views to obtain the required data. To open the report properties, use the
following procedure:

To examine the Computer information for a
specific computer report
   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, select Reporting, and then select Reports.

   3. From the list of displayed reports, select Computer information for a specific
      computer and then, in the Home tab, in the Report Group group, select Edit.

   4. After Report Builder opens, in the Report Data pane, expand Datasets and then
      double-click DataSet0 to examine the SQL statement for the report which appears
      as follows:

        SQL

             SELECT distinct SYS.Netbios_Name0, SYS.User_Name0,
        SYS.User_Domain0, SYS.Resource_Domain_OR_Workgr0,
                         OPSYS.Caption0 as C054, OPSYS.Version0,
                         MEM.TotalPhysicalMemory0,
                         STUFF((SELECT (N','+IPAddr.IP_Addresses0) AS [text()]
                         FROM fn_rbac_RA_System_IPAddresses(@UserSIDs) IPAddr
                         WHERE SYS.ResourceID = IPAddr.ResourceID for xml
        path(N''))
                         ,1,1,N'') as IP_Addresses0, -- if there are multiple
        IP address then combine them together
                         Processor.Manufacturer0,
                         CSYS.Model0, Processor.Name0,
        Processor.MaxClockSpeed0, SYS.Is_AOAC_Capable0
                         FROM fn_rbac_R_System(@UserSIDs) SYS
                         LEFT JOIN fn_rbac_GS_X86_PC_MEMORY(@UserSIDs) MEM on
        SYS.ResourceID = MEM.ResourceID
                         LEFT JOIN fn_rbac_GS_COMPUTER_SYSTEM(@UserSIDs) CSYS
        on SYS.ResourceID = CSYS.ResourceID

<!-- p.365 -->

                         LEFT JOIN fn_rbac_GS_PROCESSOR(@UserSIDs) Processor
        on Processor.ResourceID = SYS.ResourceID
                         LEFT JOIN fn_rbac_GS_OPERATING_SYSTEM(@UserSIDs)
        OPSYS on SYS.ResourceID=OPSYS.ResourceID
                         WHERE SYS.Netbios_Name0 = @variable
                         ORDER BY SYS.Netbios_Name0,
        SYS.Resource_Domain_OR_Workgr0

   5. Close the Dataset Properties dialog box and then double-click DataSetAdminID to
     examine the SQL statement that presents a list of possible computers for the user
     to choose. This appears as follows:

       SQL

             SELECT dbo.fn_rbac_GetAdminIDsfromUserSIDs(@UserTokenSIDs) as
        userSIDs

     This report contains a more complex SQL statement that combines multiple SQL
     views to obtain the desired data. The query results will list the NetBIOS name, user
     name, operating system, memory, and more with the NetBIOS name used as the
     variable in the report prompt **(WHERE SYS.Netbios_Name0 = @variable)**. The
     query retrieves information from six different SQL Server views (v_R_System,
     v_RA_System_IPAddresses, v_GS_X86_PC_MEMORY, v_GS_COMPUTER_SYSTEM,
     v_GS_PROCESSOR, and v_GS_OPERATING_SYSTEM) that are joined together by
     using the ResourceID column from the v_R_System view and where the NetBIOS
     name in the v_R_System view is equal to the one provided in the report prompt.
     Finally, the results are ordered first by the Netbios Name column and then the
     User Domain column.

     The report prompt will display Computer Name as the prompt text and has a
     variable named variable that will be populated by the user. You can examine
     details about the variables and parameters used by the report in the Parameters
     node of the Report Data pane.

   6. Close Report Builder.

See also
Evaluation of the All collections report in Configuration Manager

Feedback

<!-- p.366 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.367 -->

How to view the SQL statement for
Configuration Manager reports
Article • 10/10/2022

Reports in Configuration Manager can be based on simple SQL statements or very
complex ones that prompt the user for information, join several Microsoft SQL Server
views, and use filters to limit the results. Use the following procedure to find out what
SQL statement is used in a Configuration Manager report.

To view the SQL statement for a report
   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then select Reports.

   3. Select the report for which you want to view the SQL statement and then, in the
      Home tab, in the Report Group group, select Edit.

   4. The Report Builder window opens. In the Report Data pane, expand Datasets to
      view the data sets for the report.

   5. Double-click a dataset to open the Dataset Properties dialog box.

      The first dataset is typically (but not always), the main SQL statement for the
      report. Other datasets might contain the SQL statements that can be used to
      present a list of items for a user to choose from, such as a list of computers.

   6. You can view and modify the SQL statement for the dataset in the Query field.

   7. Close the Dataset Properties dialog box.

   8. Close Report Builder.

See also
How to modify Configuration Manager reports

Feedback

<!-- p.368 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.369 -->

How to modify Configuration Manager
reports
Article • 10/10/2022

The procedures in this topic help you to view the properties of, and modify
Configuration Manager reports.

How to view the general properties of a report
You can view general properties for a report in the Configuration Manager console. Use
the following procedure to view the properties of a report.

To view the general properties of a report
   1. In the Configuration Manager console, select Monitoring.
   2. In the Monitoring workspace, expand Reporting, and then select Reports.
   3. From the list of reports, select the report that you want to view properties for and
      then, in the Home tab, in the Properties group, select Properties.
   4. In the report name�Properties dialog box, you can view general information
      about the report, create and view report subscriptions and view security
      information about the report.
   5. Close the report name�Properties dialog box.

How to modify a report
Use SQL Server Report Builder to modify reports. Report Builder can be opened directly
from the Configuration Manager console. Use the following procedure to modify a
Configuration Manager report.

To modify a report
   1. In the Configuration Manager console, select Monitoring.
   2. In the Monitoring workspace, expand Reporting, and then select Reports.
   3. From the list of reports, select the report that you want to view properties for and
      then, in the Home tab, in the Report Group group, select Edit.
   4. In SQL Server Report builder, make the necessary modifications to the report.
   5. Save your report, and then close Report Builder.

<!-- p.370 -->

See also
How to create Configuration Manager reports

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.371 -->

How to create Configuration Manager
reports
Article • 10/10/2022

You can create two types of reports directly from the Configuration Manager console:

      Model-based report � Allows you to create a report based on a Reporting
      Services model and select the attributes to be included with Report Builder.

      SQL-based report � Allows you to create a traditional report based directly off the
      database views by using SQL statements and stored procedures.

To create a new model-based report
   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then select Reports.

   3. In the Home tab, in the Create group, select Create Report.

   4. On the Information page of the Create Report Wizard, configure the following
      settings:

            Type: Select Model-based Report to create a report in Report Builder by
            using a Reporting Services model.
            Name: Specify a name for the report.
            Description: Specify a description for the report.
            Server: Displays the name of the report server on which you are creating this
            report.
            Path: Select Browse to specify a folder in which you want to store the report.

   5. On the Model Selection page of the wizard, select an available model in the list
      that you use to create this report. When you select the report model, the Preview
      section displays the SQL Server views and entities that are made available by the
      selected report model.

   6. On the Summary page of the wizard, review the settings. Select Previous to
      change the settings or select Next to create the report.

   7. On the Completion page of the wizard, select Close to exit the wizard, Report
      Builder now opens where you can configure the report settings. Enter your user
      account and password if you are prompted, and then select OK. If Report Builder is

<!-- p.372 -->

   not installed on the computer, you are prompted to install it. Select Run to install
   Report Builder, which is required to modify and create reports.

 8. In Report Builder, create the report layout, select data in the available SQL Server
   views, add parameters to the report, and so on. For more information about using
   Report Builder to create a new report, see the Report Builder Help.

 9. Select Run to run your report. Verify that the report provides the information that
   you expect. Select Design to return to the Design view to modify the report, if
   needed.

10. Select Save to save the report to the report server. You can run and modify the
   new report in the Reports node in the Monitoring workspace.

To create a new SQL-based report
 1. In the Configuration Manager console, select Monitoring.

 2. In the Monitoring workspace, expand Reporting, and then select Reports.

 3. In the Home tab, in the Create group, select Create Report.

 4. On the Information page of the Create Report Wizard, configure the following
   settings:

         Type: Select SQL-based Report to create a report in Report Builder by using
         SQL statements.
         Name: Specify a name for the report.
         Description: Specify a description for the report.
         Server: Displays the name of the report server on which you are creating this
         report.
         Path: Select Browse to specify a folder in which you want to store the report.

 5. On the Summary page of the wizard, review the settings. Select Previous to
   change the settings or select Next to create the report.

 6. On the Completion page of the wizard, select Close to exit the wizard, Report
   Builder now opens where you can configure the report settings. Enter your user
   account and password if you are prompted, and then select OK. If Report Builder is
   not installed on the computer, you are prompted to install it. Select Run to install
   Report Builder, which is required to modify and create reports.

 7. In Microsoft Report Builder, create the report layout, select data in the available
   SQL Server views and add parameters to the report, and so on. For more

<!-- p.373 -->

     information about using Report Builder to create a new report, see the Report
     Builder Help.

   8. Select Run to run your report. Verify that the report provides the information that
     you expect. Select Design to return to the Design view to modify the report, if
     needed.

   9. Select Save to save the report to the report server. You can run and modify the
     new report in the Reports node in the Monitoring workspace.

See also
How to run Configuration Manager reports

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.374 -->

How to run Configuration Manager
reports
Article • 10/10/2022

Reports in Configuration Manager are stored in SQL Server Reporting Services, and the
data rendered in the report is retrieved from the Configuration Manager site database.
You can access reports in the Configuration Manager console or by using Report
Manager, which you access in a web browser. You can open reports on any computer
that has access to the computer that is running SQL Server Reporting Services, and you
must have sufficient rights to view the reports. When you run a report, the report title,
description, and category are displayed in the language of the local operating system.

How to run a Configuration Manager report
Use the following procedures to run a Configuration Manager report.

  ２ Warning

  To run reports, you must have Read rights for the Site permission and the Run
  Report permission that is configured for specific objects.

Report Manager is a web-based report access and management tool that you use to
administer a single report server instance on a remote location over an HTTP
connection. You can use Report Manager for operational tasks, for example, to view
reports, modify report properties, and manage associated report subscriptions. This
topic provides the steps to view a report and modify report properties in Report
Manager, but for more information about the other options that Report Manager
provides, see Report Manager in SQL Server 2008 Books Online.

To run a report in the Configuration Manager console
   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then select Reports to list
      the available reports.

         Tip

<!-- p.375 -->

        If no reports are listed, verify that the reporting services point is installed and
        configured. For more information, see the topic Configuring Reporting in
        Configuration Manager.

   3. Select the report that you want to run, and then on the Home tab, in the Report
     Group section, select Run to open the report.

   4. When there are required parameters, specify the parameters, and then select View
     Report.

To run a report in a web browser
   1. In your web browser, enter the Report Manager URL, for example,
      http://Server1/Reports . You can determine the Report Manager URL on the

     Report Manager URL page in Reporting Services Configuration Manager.

   2. In Report Manager, select the report folder for Configuration Manager, for
     example, ConfigMgr_CAS.

         Tip

        If no reports are listed, verify that the reporting services point is installed and
        configured. For more information, see the topic Configuring Reporting in
        Configuration Manager.

   3. Select the report category for the report that you want to run, and then select the
     link for the report. The report opens in Report Manager.

   4. When there are required parameters, specify the parameters, and then select View
     Report.

See also
How to view the SQL Statement for Configuration Manager reports

Feedback
Was this page helpful?    Yes     No

<!-- p.376 -->

Provide product feedback

<!-- p.377 -->

Exercise 1: Run an existing Configuration
Manager report
Article • 10/10/2022

In this exercise, you will run an existing Configuration Manager report and review
specific report elements.

For more information about how to work with reports in Configuration Manager, see
Introduction to reporting.

To run an existing Configuration Manager
report
   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then select Reports.

   3. In the list of reports, find and select the report, Processor information for a
      specific computer.

         Tip

        To make it easier to find a report, you can select a column title to sort the
        reports, or you can type the name, or a partial name for the report in the
        search box, and then select Search.

   4. On the Home tab, in the Report Group group, select Run.

   5. Specify any required parameters (in this case, a computer name), and then select
      View Report.

The report is displayed. Review the processor information and then close the report.

See also
Exercise 2: Modify an existing report in Configuration Manager

Feedback

<!-- p.378 -->

Was this page helpful?      Yes    No

Provide product feedback

<!-- p.379 -->

Exercise 2: Modify an existing report in
Configuration Manager
Article • 10/10/2022

In this exercise, you will modify a Configuration Manager report and then run the
modified report. The report SQL statement will be modified in the report properties to
remove an existing report column and add two new report columns.

To modify a Configuration Manager report
   1. In the Configuration Manager console, select Monitoring.
   2. In the Monitoring workspace, expand Reporting, and then select Reports.
   3. From the list of reports, select the report that you want to modify and then, in the
      Home tab, in the Report Group group, select Edit.
   4. Report Builder opens. In Report Builder, make any modifications you require to the
      report.
   5. Save the report and close Report Builder. You can now run the modified report
      from the Configuration Manager console.

See also
Exercise 3: Create a new Configuration Manager report

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.380 -->

Exercise 3: Create a new Configuration
Manager report
Article • 10/10/2022

In this exercise, you'll create a simple report in Microsoft SQL Server Report Builder, and
configure the report properties.

The report displays all collections that administrative users have created, and excludes
the built-in collections. The results will display the collection ID and name, the last
collection refresh time and the date of the last collection membership change.

To create a new report
   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then select Reports.

   3. In the Home tab, in the Create group, select Create Report.

   4. On the Information page of the Create Report Wizard, select SQL-based Report,
      and then configure the following properties:

            Name: Enter All collections created by administrative users.
            Description: Enter Displays all collections that were created by an
            administrative user (excludes built-in collections).
            Path: Select Browse, and then select the Site � General folder to store the
            report.

   5. Select Next.

   6. On the Summary page of the Create Report Wizard, review the actions that will be
      taken and then select Next.

   7. On the Completion page of the wizard, review any messages and then select
      Close.

   8. Report Builder opens. In the Report Data pane, right-click Datasets, and then
      select Add Dataset.

   9. On the Query page of the Dataset Properties dialog box, select Use a dataset
      embedded in my report.

<!-- p.381 -->

 10. In the Data source drop-down list, select the data source you want to use for the
     report. This is typically automatically generated and will begin with AutoGen_.

 11. Select a query type of Text, and then enter the following query in the Query field.

       SQL

       SELECT
       v_Collections.CollectionID,
       v_Collections.CollectionName,
       v_Collections.LastRefreshTime,
       v_Collections.LastMemberChangeTime
       FROM
       V_Collections
       WHERE
       IsBuiltIn=0

 12. Select OK to close the Dataset Properties dialog box.

 13. In Report Builder, on the Insert tab, in the Data Regions group, select Table, and
     then select Table Wizard.

 14. On the Choose a dataset page of the New Table or Matrix wizard, select Choose
     an existing dataset in this report or a shared dataset, and then select the dataset
     you previously created, Dataset1.

 15. Select Next.

 16. On the Arrange fields page of the New Table or Matrix wizard, drag CollectionID,
     CollectionName, LastRefreshTime and LastMemberChangeTime from the
     Available fields field to the Values field.

 17. Select Next.

 18. On the Choose the layout page of the New Table or Matrix wizard, select Next.

 19. On the Choose a style page of the wizard, choose one of the available themes for
     the report, and then select Finish.

 20. Verify that the data in the report is as expected.

 21. Save and close the report in Report Builder.

The new report is now available in the Configuration Manager console.

Next steps

<!-- p.382 -->

Report builder includes many options to change elements of reports, including themes,
column headings and more. Consult your Report Builder help for more information.

See also
Exercise 1: Run an existing Configuration Manager report

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.383 -->

Advanced exercise 1: Create a new
report for compliance settings in
Configuration Manager
Article • 10/04/2022

In this exercise, you will create a Configuration Manager report that displays the name
and description of the configuration baselines that are deployed to a specified
computer and whether the computer returns compliant or noncompliant for the
configuration baseline.

  ） Important

  Before you begin this exercise, you should review the basic exercises to learn about
  the report elements, the properties for a report, and the different ways to create
  the report SQL statement.

Report requirements
Use the following report requirements to create the new report.

SQL Server views in the SQL statement
Use the following Configuration Manager SQL views when creating the report SQL
statement:

      v_CICurrentComplianceStatus: This SQL view contains compliance information for
      all configuration items. For more information about this SQL view, see Compliance
      Settings Views in Configuration Manager.

      v_ConfigurationItems: This SQL view contains all of the configuration items. For
      more information about this SQL view, see Compliance Settings Views in
      Configuration Manager.

      v_LocalizedCIProperties: This SQL view contains the localized titles and
      descriptions for the configuration items. For more information about this SQL view,
      see Compliance Settings Views in Configuration Manager.

<!-- p.384 -->

     v_R_System: This SQL view contains all of the discovered system resources. For
     more information about this SQL view, see Discovery Views in Configuration
     Manager.

JOINS in the SQL statement
Create the following JOINS in the SQL statement:

     v_CICurrentComplianceStatus is joined to v_ConfigurationItems by using the
     CI_ID column.

     v_CICurrentComplianceStatus is joined to v_LocalizedCIProperties by using the
     CI_ID column.

     v_CICurrentComplianceStatus is joined to v_R_System by using the ResourceID
     column.

Columns in the SQL statement
Use the following report columns, in the order listed:

   1. ComplianceStateName from v_CICurrentComplianceStatus

   2. DisplayName from v_LocalizedCIProperties

   3. Description from v_LocalizedCIProperties

   4. Netbios_Name0 from v_R_System

   5. CIType_ID from v_ConfigurationItems (Not displayed)

Sort the returned data in ascending order, using the Netbios_Name0 column.

Filters in the SQL statement
The report SQL statement should meet the following filtering criteria:

     Select only configuration baselines. You can filter specifically on configuration
     baselines by selecting the CIType_ID. Configuration baselines are CI type 2.

Report prompts

<!-- p.385 -->

The Configuration Manager report should contain a report prompt for the computer
name that will be reported on.

Solution
See Advanced exercise 1 solution: create a new report for compliance settings in
Configuration Manager for detailed information about how to create this report.

See also
Exercise 1: run an existing Configuration Manager report
Advanced exercise 1 solution: create a new report for compliance settings in
Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.386 -->

Advanced exercise 1 solution: Create a
new report for compliance settings in
Configuration Manager
Article • 10/04/2022

Use the following procedure to create the report in Advanced exercise 1: Create a new
report for compliance settings in Configuration Manager.

  ７ Note

  Depending on your experience at creating SQL Server reports, there are numerous
  paths you can use to create a report. You can use your preferred method of
  creating reports if you prefer.

To create the status of configuration baselines
deployed to a specified computer report
   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then select Reports.

   3. In the Home tab, in the Create group, select Create Report.

   4. On the Information page of the Create Report Wizard, select SQL-based Report,
      and then supply the following information:

            Name: Enter Status of configuration baselines deployed to a specified
            computer.
            Description: Enter Displays the name and description of the configuration
            baselines that are deployed to a specific computer and whether the
            computer returns compliant or noncompliant for the configuration
            baseline.
            Server: This field is automatically entered. Ensure that it matches the name of
            your Reporting Server.
            Path: Select Browse to select the folder in which the new report will be
            stored. For this exercise, select Compliance and Settings Management.

   5. To continue, select Next.

<!-- p.387 -->

 6. On the Summary page of the Create Report Wizard, review the information and
   then select Next.

 7. On the Completion page of the Create Report Wizard, review the actions that were
   taken, and then select Close. Report Builder now opens to allow you to construct
   the report.

 8. Next, you must create the datasets that this report will use to return results for the
   report. This report uses two datasets. The first of these is used to list computer
   names that can be selected to use as a basis for the report. The second contains
   the SQL statements for the report itself.

   In the Report Data pane, right-click Datasets and then select Add Dataset.

 9. On the Query page of the Dataset Properties dialog box, supply a name for the
   dataset, or use the default name, and then select Use a dataset embedded in my
   report.

10. In the Data source drop-down list, select the data source you want to use for the
   report. This is typically automatically generated and will begin with AutoGen_.

11. Select a query type of Text, and then enter the following query in the Query field.

      SQL

      SELECT DISTINCT SYS.Netbios_Name0
      ��from v_R_System SYS WHERE SYS.Client0=1
      ��ORDER By SYS.Netbios_Name0

12. Select OK to close the Dataset Properties dialog box. The new dataset, named by
   default DataSet1 is now displayed in the Datasets node of the Report Data pane.

   You have now created the query that the report parameter will use to return the
   available client names from which you can choose to run the report.

13. Next create the parameter that the report will use to let you select the computer
   that will be reported on.

   In the Report Data pane, right-click Parameters, and then select Add Parameter.

14. On the General page of the Report Parameter Properties dialog box, change the
   value in the Prompt field to read Computer name.

15. On the Available Values page of the Report Parameter Properties dialog box,
   select Get values from a query.

<!-- p.388 -->

16. Select the following values:

         Dataset: Choose DataSet1
         Value field: Choose Netbios_Name0
         Label field: Choose Netbios_Name0

17. Select OK to close the Report Parameter Properties dialog box. The new
   parameter ReportParameter1 is displayed in the Parameters node of the Report
   Data pane.

18. At this point, run the report to check the parameter is working correctly. On the
   Home tab, in the Views group, select Run.

19. Verify that the Computer name field is shown. When you select this field, you
   should see all Windows client computers in the drop-down list.

20. On the Home tab, in the Views group, select Design to return to the design view.

21. Now, you must create the main dataset for the report.

   In the Report Data pane, right-click Datasets and then select Add Dataset.

22. On the Query page of the Dataset Properties dialog box, supply a name for the
   dataset, or use the default name, and then select Use a dataset embedded in my
   report.

23. In the Data source drop-down list, select the data source you want to use for the
   report. This is typically automatically generated and will begin with AutoGen_.

24. Select a query type of Text, and then enter the following query in the Query field.

      SQL

      SELECT v_CICurrentComplianceStatus.ComplianceState,
        v_LocalizedCIProperties.DisplayName,
      v_LocalizedCIProperties.Description, v_R_System.Netbios_Name0
      FROM v_CICurrentComplianceStatus INNER JOIN v_R_System ON
        v_CICurrentComplianceStatus.ResourceID = v_R_System.ResourceID
      INNER JOIN v_ConfigurationItems ON
        v_CICurrentComplianceStatus.CI_ID = v_ConfigurationItems.CI_ID
      INNER JOIN v_LocalizedCIProperties ON
        v_CICurrentComplianceStatus.CI_ID = v_LocalizedCIProperties.CI_ID
      WHERE (v_ConfigurationItems.CIType_ID = 2)

25. Select OK to close the Dataset Properties dialog box.

<!-- p.389 -->

 26. On the Insert tab, in the Data Regions group, select Table, and then select Table
     Wizard.

 27. On the New Table or Matrix page of the wizard, select Choose an existing dataset
     in this report or a shared dataset, select DataSet2 and then select Next.

 28. On the Arrange fields page of the wizard, drag ComplianceState, DisplayName,
     Description and Netbios_Name0 from the Available fields pane, to the Values
     pane.

 29. Select Next to see a preview of your report, and then select Next again.

 30. On the Choose a style page of the wizard, choose one of the available themes for
     the report, and then select Finish.

 31. On the Home tab, in the Views group, select Run.

 32. In the Computer name field, select a computer from the drop-down list, and then
     select View Report.

 33. Verify that the data in the report is as expected.

 34. Save and close the report in Report Builder.

The new report is now available in the Configuration Manager console.

Next steps
Report builder includes many options to change elements of reports, including themes,
column headings and more. Consult your Report Builder help for more information.

See also
Advanced exercise 1: Create a new report for compliance settings in Configuration
Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.390 -->

Advanced exercise 2: Create a new
report for hardware inventory in
Configuration Manager
Article • 10/04/2022

In this exercise, you will create a Configuration Manager report that displays the
computer name, site code, the date of the last scan for hardware inventory, and the
number of days since the last scan for a specified computer.

  ） Important

  Before you begin this exercise, you should review the basic exercises to learn about
  the report elements, the properties for a report, and the different ways to create
  the report SQL statement.

Report requirements
Use the following report requirements to create the new report.

SQL Server views in the SQL statement
Use the following Configuration Manager SQL Server views when creating the report
SQL statement:

      v_GS_WORKSTATION_STATUS: This SQL Server view contains the date and time of
      the last scan for hardware inventory reported by client computers. For more
      information about this SQL Server view, see Hardware Inventory Views in
      Configuration Manager.
      v_R_System: This SQL Server view contains all of the discovered system resources.
      For more information about this SQL Server view, see Discovery Views in
      Configuration Manager.
      v_RA_System_SMSInstalledSites: This SQL Server view contains the installed site
      for all client computers. For more information about this SQL Server view, see
      Discovery Views in Configuration Manager.

JOINS in the SQL statement

<!-- p.391 -->

Create the following JOINS in the SQL statement:

     v_GS_WORKSTATION_STATUS is joined to v_R_System by using the ResourceID
     columns.
     v_RA_System_SMSInstalledSites is joined to v_R_System by using the ResourceID
     columns.

Columns in the SQL statement
Use the following report columns, in the order listed:

   1. Netbios_Name0 AS [Computer Name] from v_R_System
   2. SMS_Installed_Sites0 AS [Site Code] from v_RA_System_SMSInstalledSites
   3. LastHWScan AS [Last HWScan] from v_GS_WORKSTATION_STATUS
   4. DATEDIFF(day, v_GS_WORKSTATION_STATUS.LastHWScan, GETDATE()) AS [Days
     Since Last HWScan]

  ７ Note

  This report integrates two SQL Server functions to determine the difference
  between the last hardware scan date and the current date. To display this column,
  you can copy the whole line into the SQL statement, or you can copy
  DATEDIFF(day, v_GS_WORKSTATION_STATUS.LastHWScan, GETDATE()) into the
  Column column and Days Since Last HWScan into the Alias column in Query
  Designer.

Sort the data in descending order, using the LastHWScan column.

Filters in the SQL statement
The report SQL statement does not contain any filters.

Report prompts
The Configuration Manager report should contain a report prompt for the computer
name that will be reported on.

Solution

<!-- p.392 -->

See Advanced exercise 2 solution: Create a new report for hardware inventory in
Configuration Manager for detailed information about how to create this report.

See also
Exercise 1: run an existing Configuration Manager report
Advanced exercise 2 solution: Create a new report for hardware inventory in
Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.393 -->

Advanced exercise 2 solution: Create a
new report for hardware inventory in
Configuration Manager
Article • 10/04/2022

The following procedure can be used to create the report for Advanced exercise 2:
Create a new report for hardware inventory in Configuration Manager.

  ７ Note

  Depending on your experience at creating SQL Server reports, there are numerous
  paths you can use to create a report. You can use your preferred method of
  creating reports if you prefer.

To create the hardware inventory information
report
   1. In the Configuration Manager console, select Monitoring.

   2. In the Monitoring workspace, expand Reporting, and then select Reports.

   3. In the Home tab, in the Create group, select Create Report.

   4. On the Information page of the Create Report Wizard, select SQL-based Report,
      and then supply the following information:

            Name: Enter Hardware Inventory Information.
            Description: Enter Displays the computer name, site code, the date of the
            last scan for hardware inventory, and the number of days since the last
            scan.
            Server: This field is automatically entered. Ensure that it matches the name of
            your Reporting Server.
            Path: Select Browse to select the folder in which the new report will be
            stored. For this exercise, select Hardware - General.

   5. To continue, select Next.

   6. On the Summary page of the Create Report Wizard, review the information and
      then select Next.

<!-- p.394 -->

 7. On the Completion page of the Create Report Wizard, review the actions that were
   taken, and then select Close. Report Builder now opens to allow you to construct
   the report.

 8. Next, you must create the datasets that this report will use to return results for the
   report. This report uses two datasets. The first of these is used to list computer
   names that can be selected to use as a basis for the report. The second contains
   the SQL statements for the report itself.

 9. In the Report Data pane, right-click Datasets and then select Add Dataset.

10. On the Query page of the Dataset Properties dialog box, supply a name for the
   dataset, or use the default name, and then select Use a dataset embedded in my
   report.

11. In the Data source drop-down list, select the data source you want to use for the
   report. This is typically automatically generated and will begin with AutoGen_.

12. Select a query type of Text, and then enter the following query in the Query field.

      SQL

      SELECT DISTINCT SYS.Netbios_Name0
      ��from v_R_System SYS WHERE SYS.Client0=1
      ��ORDER By SYS.Netbios_Name0

13. Select OK to close the Dataset Properties dialog box. The new dataset, named by
   default DataSet1 is now displayed in the Datasets node of the Report Data pane.

   You have now created the query that the report parameter will use to return the
   available client names from which you can choose to run the report.

14. Next create the parameter that the report will use to let you select the computer
   that will be reported on.

   In the Report Data pane, right-click Parameters, and then select Add Parameter.

15. On the General page of the Report Parameter Properties dialog box, change the
   value in the Prompt field to read Computer name.

16. On the Available Values page of the Report Parameter Properties dialog box,
   select Get values from a query.

17. Select the following values:

         Dataset: Choose DataSet1

<!-- p.395 -->

         Value field: Choose Netbios_Name0
         Label field: Choose Netbios_Name0

18. Select OK to close the Report Parameter Properties dialog box. The new
   parameter ReportParameter1 is displayed in the Parameters node of the Report
   Data pane.

19. At this point, run the report to check the parameter is working correctly. On the
   Home tab, in the Views group, select Run.

20. Verify that the Computer name field is shown. When you select this field, you
   should see all Windows client computers in the drop-down list.

21. On the Home tab, in the Views group, select Design to return to the design view.

22. Now, you must create the main dataset for the report.

   In the Report Data pane, right-click Datasets and then select Add Dataset.

23. On the Query page of the Dataset Properties dialog box, supply a name for the
   dataset, or use the default name, and then select Use a dataset embedded in my
   report.

24. In the Data source drop-down list, select the data source you want to use for the
   report. This is typically automatically generated and will begin with AutoGen_.

25. Select a query type of Text, and then enter the following query in the Query field.

      SQL

      SELECT v_R_System.Netbios_Name0 AS [Computer Name],
      ��v_RA_System_SMSInstalledSites.SMS_Installed_Sites0 AS [Site Code],
      ��v_GS_WORKSTATION_STATUS.LastHWScan AS [Last HWScan],
      ��DATEDIFF(day, v_GS_WORKSTATION_STATUS.LastHWScan, GETDATE()) AS
      [Days Since Last HWScan]
      FROM v_GS_WORKSTATION_STATUS INNER JOIN v_R_System ON
      ��v_GS_WORKSTATION_STATUS.ResourceID = v_R_System.ResourceID
      ��INNER JOIN v_RA_System_SMSInstalledSites ON
      ��v_R_System.ResourceID = v_RA_System_SMSInstalledSites.ResourceID
      ORDER BY [Last HWScan] DESC

26. Select OK to close the Dataset Properties dialog box.

27. On the Insert tab, in the Data Regions group, select Table, and then select Table
   Wizard.

<!-- p.396 -->

 28. On the New Table or Matrix page of the wizard, select Choose an existing dataset
     in this report or a shared dataset, select DataSet2 and then select Next.

 29. On the Arrange fields page of the wizard, drag Computer_Name, Site_Code,
     Last_HWScan and Days_Since_Last_HWScan from the Available fields pane, to the
     Values pane.

 30. Select Next to see a preview of your report, and then select Next again.

 31. On the Choose a style page of the wizard, choose one of the available themes for
     the report, and then select Finish.

 32. On the Home tab, in the Views group, select Run.

 33. In the Computer name field, select a computer from the drop-down list, and then
     select View Report.

 34. Verify that the data in the report is as expected.

 35. Save and close the report in Report Builder.

The new report is now available in the Configuration Manager console.

Next steps
Report builder includes many options to change elements of reports, including themes,
column headings and more. Consult your Report Builder help for more information.

See also
Advanced exercise 2: Create a new report for hardware inventory in Configuration
Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.397 -->

Sample queries for application
management in Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join the most common application
management views to other views.

Joining package and program deployment and
collection views
The following query lists all package and program deployments by advertisement ID,
advertisement name, and the collection that was targeted for the deployment. The
v_Advertisement view is joined to the v_Collection view by using the AdvertisementID
column.

  SQL

        SELECT ADV.AdvertisementID, ADV.AdvertisementName,
        COL.CollectionID, COL.Name as CollectionName
        FROM v_Advertisement ADV INNER JOIN v_Collection COL
        ON ADV.CollectionID = COL.CollectionID
        ORDER BY ADV.AdvertisementID

See also
Application management views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.398 -->

Sample queries for client deployment in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join the most common client
deployment views to other views.

The following sample query demonstrates how to join client deployment views with
other views. Client deployment views will most often use the MachineID column, which
is the same as the ResourceID column in other views, and NetBiosName column when
joining to other views.

Joining client deployment and discovery views
This query retrieves the NetBIOS name for client computers that have provided client
deployment status, the user name, assigned site, time of last state message, and state
name. The results are sorted by deployment state and then NetBIOS name. The query
joins the v_ClientDeploymentState client deployment view with the v_R_System
discovery view by using the ResourceID column, and the v_ClientDeployment view with
the v_StateNames status view by using the LastMessageStateID and StateID columns,
respectively. The retrieved information is filtered by the topic type of 800, which
includes only state messages for client deployment.

  SQL

      SELECT v_ClientDeploymentState.NetBiosName AS Computer,
      ��v_R_System.User_Name0 AS [User],
      ��v_ClientDeploymentState.AssignedSiteCode AS [Assigned Site],
      ��v_ClientDeploymentState.LastMessageTime AS [Last Message],
      ��v_StateNames.StateName AS State
      FROM v_ClientDeploymentState INNER JOIN v_R_System ON
      ��v_ClientDeploymentState.SMSID = v_R_System.SMS_Unique_Identifier0
  INNER JOIN v_StateNames ON
      ��v_ClientDeploymentState.LastMessageStateID = v_StateNames.StateID
      WHERE (v_StateNames.TopicType = 800)
      ORDER BY State, Computer

See also
Client deployment views in Configuration Manager

<!-- p.399 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.400 -->

Sample queries for client status in
Configuration Manager
Article • 10/10/2022

The following sample queries demonstrate how to join common client status views to
other views.

Joining client status and collection views
This query lists each client computer in the site, the last time it requested policy, and the
collections to which the computer belongs. The query uses the
v_CH_PolicyRequestHistory view to read the last policy request time and joins, using
the ResourceID column to the v_ClientCollectionMembers view.

  SQL

      SELECT        dbo.CH_PolicyRequestHistory.MachineID AS ResourceID,
  dbo.CH_PolicyRequestHistory.RequestTime,
  dbo.v_ClientCollectionMembers.CollectionID
      FROM            dbo.CH_PolicyRequestHistory INNER JOIN
                               dbo.v_ClientCollectionMembers ON
  dbo.CH_PolicyRequestHistory.MachineID =
  dbo.v_ClientCollectionMembers.ResourceID

See also
Client status views in Configuration Manager

Feedback
Was this page helpful?      Yes    No

Provide product feedback
