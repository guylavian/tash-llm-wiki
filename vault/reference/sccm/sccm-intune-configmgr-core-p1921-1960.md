---
title: "Core infrastructure documentation — pages 1921-1960"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1921-1960
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1921-1960
family: sccm
documentKind: "doc"
abstract: "Operations and maintenance for reporting in Configuration Manager Article • 10/04/2022 Applies to: Configuration Manager (current branch) After the infrastructure is in place for reporting in Configuration Manager, there are many operations that you typically do to manage report"
---

# Core infrastructure documentation — pages 1921-1960

<!-- p.1921 -->

Operations and maintenance for
reporting in Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

After the infrastructure is in place for reporting in Configuration Manager, there are
many operations that you typically do to manage reports and subscriptions.

  ７ Note

  This article focuses on reports in SQL Server Reporting Services. Starting in version
  2002, you can integrate reporting with Power BI Report Server. For more
  information, see Integrate with Power BI Report Server.

Run a report from Reporting Services
Configuration Manager stores its reports in SQL Server Reporting Services. The report
retrieves data from the Configuration Manager site database. You can access reports in
the Configuration Manager console or by using Report Manager via a web browser.
Open reports from a web browser on any computer that can access the reporting
services point, and the user has sufficient rights to view the reports. To run reports, you
need Read rights for the Site permission and the Run Report permission for specific
objects.

When you run a report, it displays the report title, description, and category in the
language of the local OS. For more information, see Languages for reports.

  ７ Note

  Report Manager is a web-based report access and management tool. You can use it
  to administer a single report server instance over an HTTPS connection. Use Report
  Manager for operational tasks: view reports, modify report properties, and manage
  associated report subscriptions. This article provides the steps to view a report and
  modify report properties in Report Manager. For more information about other
  options in Report Manager, see What is Report Manager?

Use the following procedures to run a Configuration Manager report.

<!-- p.1922 -->

Run a report in the Configuration Manager console
   1. In the Configuration Manager console, go to the Monitoring workspace. Expand
     Reporting, and then select Reports. This node lists the available reports.

        Tip

       If this node doesn't list any reports, verify that the reporting services point is
       installed and configured. For more information, see Configure reporting.

   2. Select the report that you want to run. On the Home tab of the ribbon, in the
     Report Group section, select Run to open the report.

   3. If there are required parameters, specify them and then select View Report.

Run a report in a web browser
   1. In your web browser, go to the Report Manager URL, for example,
     https://Server1/Reports . Find this address on the Report Manager URL page in

     Reporting Services Configuration Manager.

   2. In Report Manager, select the report folder for Configuration Manager, for
     example, ConfigMgr_CAS.

        Tip

       If Report Manager doesn't list any reports, verify that the reporting services
       point is installed and configured. For more information, see Configure
       reporting.

   3. Select the report category for the report that you want to run, and then select the
     specific report. The report opens in Report Manager.

   4. If there are required parameters, specify them and then select View Report.

Modify the properties of a report
Report properties include the report name and description. You can view the properties
for a report n the Configuration Manager console.

To change the properties, use Report Manager:

<!-- p.1923 -->

   1. In your web browser, go to the Report Manager URL, for example,
      https://Server1/Reports .

   2. In Report Manager, select the report folder for Configuration Manager, for
     example, ConfigMgr_CAS.

   3. Select the report category, and then select the specific report. The report opens in
     Report Manager.

   4. Select the Properties tab. Modify the report name and description, and then select
     Apply.

Report Manager saves the report properties on the report server. The Configuration
Manager console shows the updated report properties for the report.

Edit a report
When an existing Configuration Manager report doesn't retrieve the information that
you want, edit it in Report Builder. You can also use Report Builder to change the layout
or design of the report. While you can directly edit a default report, it's best to clone it.
Open the report to edit, and then select Save As.

To edit a report, you need Site Modify permission and Modify Report permissions on
the specific objects in the report.

  ） Important

  Site updates preserve built-in reports. If you modify a standard report, when the
  site updates, it renames the report with an underscore prefix ( _ ). This behavior
  makes sure that the site update doesn't overwrite the modified report by the
  standard report.

  If you modify predefined reports, before you install a site update, back up your
  custom reports. After the update, restore the report in Reporting Services. If make
  significant changes to a predefined report, create a new report instead. New
  reports that you create before you upgrade a site are not overwritten.

Use the following procedure to edit the properties for a Configuration Manager report.

   1. In the Configuration Manager console, go to the Monitoring workspace. Expand
     Reporting, and then select the Reports node.

<!-- p.1924 -->

   2. Select the report that you want to modify. On the Home tab of the ribbon, in the
     Report Group section, select Edit. It may prompt you to enter credentials. If Report
     Builder isn't installed on the computer, Configuration Manager prompts you to
     install it. Report Builder is required to modify and create reports.

   3. In Report Builder, modify the appropriate report settings. Select Save to save the
     report to the report server.

Create reports
There are two types of reports that you can create:

     A model-based report lets you interactively select the items you want to include in
     your report. For more information about creating custom report models, see
     Create custom report models for Configuration Manager in SQL Server Reporting
     Services.

     A SQL-based report lets you retrieve data that's based on a report SQL statement.

  ） Important

  To create a new report, your account needs Site Modify permission. You can only
  create a report in folders for which you have Modify Report permissions.

Create a model-based report
Use the following procedure to create a model-based Configuration Manager report.

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Reporting, and select the Reports node.

   2. On the Home tab of the ribbon, in the Create section, select Create Report. This
     action opens the Create Report Wizard.

   3. On the Information page, configure the following settings:

          Type: Select Model-based Report.

          Name: Specify a name for the report.

          Description: Specify a description for the report.

          Server: Displays the name of the report server where you create this report.

<!-- p.1925 -->

           Path: Select Browse to specify a folder in which to store the report.

   4. On the Model Selection page, select an available model in the list to create this
     report. The Preview section displays the SQL Server views and entities that are
     available in this report model.

   5. Complete the Create Report Wizard.

   6. Open Report Builder to configure the report settings. For more information, see
     Edit a Configuration Manager report.

   7. In Report Builder, create the report layout, select data in the available SQL Server
     views, and add parameters to the report.

   8. Select Run to run your report. Verify that the report provides the information that
     you expect. If needed, select Design to modify the report further.

   9. Select Save to save the report to the report server.

Create a SQL-based report
When you create an SQL statement for a custom report, don't directly reference SQL
Server tables. Always reference supported reporting SQL Server views from the site
database. These views have names that start with v_ . For more information, see
Creating custom reports by using SQL Server views in Configuration Manager.

You can also reference public stored procedures from the site database. These stored
procedures have names that start with sp_ .

Use the following procedure to create a SQL-based Configuration Manager report.

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Reporting, and select the Reports node.

   2. On the Home tab of the ribbon, in the Create section, select Create Report. This
     action opens the Create Report Wizard.

   3. On the Information page, configure the following settings:

           Type: Select SQL-based Report.

           Name: Specify a name for the report.

           Description: Specify a description for the report.

           Server: Displays the name of the report server where you create this report.

<!-- p.1926 -->

           Path: Select Browse to specify a folder in which to store the report.

   4. Complete the Create Report Wizard.

   5. Open Report Builder to configure the report settings. For more information, see
     Edit a Configuration Manager report.

   6. In Report Builder, provide the SQL statement for the report. You can also build the
     SQL statement by using columns in available views. If needed, add parameters to
     the report.

   7. Select Run to run your report. Verify that the report provides the information that
     you expect. If needed, select Design to modify the report further.

   8. Select Save to save the report to the report server.

Manage report subscriptions
Report subscriptions in SQL Server Reporting Services let you configure the automatic
delivery of specified reports by email or to a file share at scheduled intervals. To
configure report subscriptions, use the Create Subscription Wizard in Configuration
Manager.

Create a report subscription to deliver a report to a file
share
When you create a report subscription to deliver a report to a file share, Reporting
Services copies the report in the specified format to the file share that you specify. You
can subscribe to and request delivery for only one report at a time.

When you create a subscription that uses a file share, specify an existing shared folder
as the destination. The report server doesn't create the folder or network share. When
you specify the destination folder in a subscription, use a UNC path and don't include
trailing backslashes ( \ ) in the folder path. The following example is a valid UNC path for
the destination folder: \\server\reportfiles\operations\2001 .

  ７ Note

  When you create the subscription, you specify a user name and password. This
  account needs access to this share with Write permissions to the destination folder.

<!-- p.1927 -->

Reporting Services can render reports in different file formats. For example, MHTML or
Excel. You select the format when you create the subscription. Although you can select
any supported rendering format, some formats work better than others when rendering
to a file.

Limitations for report subscriptions to a file share
The following list includes the limitations of report subscriptions to a file share:

      Unlike reports that you host and manage on a report server, Reporting Services
      delivers reports to a shared folder as static files.

      Interactive features of the report don't work for reports stored as files. The report
      represents any interactive features as static elements.

      If the report includes charts, it uses the default presentation.

      If the report links through to another report, it renders the link as static text.

If you want to keep interactive features in a delivered report, use email delivery. For
more information, see Create a report subscription to deliver a report by email.

Process to create a report subscription for a file share
Use the following procedure to create a report subscription to deliver a report to a file
share.

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
      Reporting, and select the Reports node.

   2. Select a report folder, then select the report to which you want to subscribe. On
      the Home tab of the ribbon, in the Report Group section, select Create
      Subscription. This action opens the Create Subscription Wizard.

   3. On the Subscription Delivery page, configure the following settings:

             Report delivered by: Select Windows File Share.

             File Name: Specify the file name for the report. By default, the report file
             doesn't include a file name extension. Select Add file extension when
             created to automatically add a file name extension based on the format.

             Path: Specify a UNC path to an existing folder where you want to deliver this
             report. For example, \\server\reportfiles\operations .

<!-- p.1928 -->

       Render Format: Select one of the following formats for the report file:
          XML file with report data
          CSV (comma delimited)
          TIFF file
          Acrobat (PDF) file
          HTML 4.0

            ７ Note

            If your report has images, the HTML 4.0 format doesn't include them.

          MHTML (web archive)
          RPL Renderer (Report Page Layout)
          Excel
          Word

       User Name: Specify a Windows user account with write permissions to the
       specified Path.

       Password: Specify the password for the above Windows user account.

       Overwrite option: Select one of the following options to configure the
       behavior when a file of the same name exists in the destination folder:
          Overwrite an existing file with a newer version
          Do not overwrite an existing file
          Increment file names as newer versions are added: This option appends a
          number to the new report's file name to distinguish it from earlier
          versions.

       Description: Optionally, specify additional information about this report
       subscription.

4. On the Subscription Schedule page, select one of the following delivery schedule
  options for the report subscription:

       Use shared schedule: A shared schedule is a previously defined schedule that
       can be used by other report subscriptions. When you select this option, also
       select a shared schedule. If there are no shared schedules, select the option
       to create a new schedule.

       Create new schedule: Configure the schedule on which this report runs. The
       schedule includes the interval, start time and date, and the end date for this
       subscription. By default, a new subscription creates a new schedule to run
       every hour starting at the current date and time.

<!-- p.1929 -->

   5. On the Subscription Parameters page, specify any parameters that this report
     requires to run unattended. If the report has no parameters, the wizard doesn't
     display this page.

   6. Complete the wizard.

   7. Verify that Configuration Manager successfully created the report subscription.
     Select the Subscriptions node to view and modify report subscriptions.

Create a report subscription to deliver a report by email
When you create a report subscription to deliver a report by email, Reporting Services
sends an email to the recipients that you configure. The email includes the report as an
attachment. The report server doesn't validate email addresses or get them from an
email server. You can email reports to any valid email account within or outside of your
organization.

  ７ Note

  To enable the Email subscription option, you need to configure the email settings
  in Reporting Services. For more information, see Email delivery in reporting
  services.

You can select one or both of the following email delivery options:

     Send a notification with a link to the generated report.

     Send an embedded or attached report. The rendering format and browser
     determine whether it embeds or attaches the report.
         If your browser supports HTML 4.0 and MHTML, and you select the MHTML
         (web archive) format, the email embeds the report in the message.
         All other formats deliver reports as attachments.
         Reporting Services doesn't check the size of the attachment or message before
         it sends the report. If the attachment or message exceeds the maximum limit
         allowed by your mail server, the report isn't delivered.

Use the following procedure to create a report subscription to deliver a report by using
email.

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Reporting, and select the Reports node.

<!-- p.1930 -->

2. Select a report folder, then select the report to which you want to subscribe. On
  the Home tab of the ribbon, in the Report Group section, select Create
  Subscription. This action opens the Create Subscription Wizard.

3. On the Subscription Delivery page, configure the following settings:

       Report delivered by: Select E-mail.

       To: Specify a valid email address as the recipient.

          ７ Note

          To enter multiple recipients, separate each email address with a
          semicolon ( ; ).

       Cc: Optionally, specify an email address to receive a copy of this report.

       Bcc: Optionally, specify an email address to receive a blind copy of this
       report.

       Reply To: Specify the reply address. If the recipient replies to the email
       message, the reply goes to this address.

       Subject: Specify a subject line for the subscription email message.

       Priority: Select the priority flag for this email message: Low, Normal, or High.
       Microsoft Exchange uses this flag to indicate the importance of the email
       message.

       Comment: Specify text for the body of the subscription email message.

       Description: Optionally, specify additional information about this report
       subscription.

       Include Link: Include the URL for this report in the body of the email
       message.

       Include Report: Attach the report to the email message. Use the Render
       Format option to specify the report format to attach.

       Render Format: Select one of the following formats for the attached report
       file:
           XML file with report data
           CSV (comma delimited)
           TIFF file

<!-- p.1931 -->

              Acrobat (PDF) file
              MHTML (web archive)
              Excel
              Word

   4. On the Subscription Schedule page, select one of the following delivery schedule
     options for the report subscription:

           Use shared schedule: A shared schedule is a previously defined schedule that
           can be used by other report subscriptions. When you select this option, also
           select a shared schedule. If there are no shared schedules, select the option
           to create a new schedule.

           Create new schedule: Configure the schedule on which this report runs. The
           schedule includes the interval, start time and date, and the end date for this
           subscription. By default, a new subscription creates a new schedule to run
           every hour starting at the current date and time.

   5. On the Subscription Parameters page, specify any parameters that this report
     requires to run unattended. If the report has no parameters, the wizard doesn't
     display this page.

   6. Complete the wizard.

   7. Verify that Configuration Manager successfully created the report subscription.
     Select the Subscriptions node to view and modify report subscriptions.

Favorites
Configuration Manager ships with several hundred reports by default, and you may have
added more to that list. Instead of continually searching for reports you commonly use,
starting in version 2103, you can make a report a favorite. This action allows you to
quickly access it from the new Favorites node.

The list of favorites is per user, not per site or hierarchy.

Prerequisites for report favorites
The version of SQL Server Reporting Services on the site's reporting service point needs
to be SQL Server 2017 or later.

  ７ Note

<!-- p.1932 -->

 All instances of SQL Server Reporting Services on the server need to be version
 2017 or later.

Add a favorite
 1. In the Configuration Manager console, go to the Monitoring workspace. Expand
    the Reporting node, and select either the Reports or Power BI Reports node.

 2. Select a report that you frequently use. Then in the ribbon, select Add to Favorites.
    The report's icon changes to a yellow star, which indicates that it's a favorite.

       Tip

      You can select more than one report to add them all as favorites.

    To remove a report from the list of favorites, select it, and then select Remove
    from Favorites. When you remove a favorite, Configuration Manager doesn't
    delete the report.

 3. Under the Reporting node, expand the new Favorites node. To view your list of
    favorites, select either the Reports or Power BI Reports node.

<!-- p.1933 -->

         Tip

        You can directly connect to your favorite reports in your browser. For example,
        https://rsp.contoso.com/Reports/favorites .

     You can manage the reports the same from the list of favorites.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1934 -->

Creating custom report models for
Configuration Manager in SQL Server
Reporting Services
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Sample report models are included in Configuration Manager, but you can also define
report models to meet your own business requirements, and then deploy the report
model to Configuration Manager to use when you create new model-based reports. The
following table provides the steps to create and deploy a basic report model.

  ７ Note

  For the steps to create a more advanced report model, see the Steps for Creating
  an Advanced Report Model in SQL Server Reporting Services section in this topic.

                                                                                    ﾉ    Expand table

 Step                  Description                                             More information

 Verify that SQL       Report models are designed and built by using SQL       For more information
 Server Business       Server Business Intelligence Development Studio.        about SQL Server
 Intelligence          Verify that SQL Server Business Intelligence            Business Intelligence
 Development           Development Studio is installed on the computer on      Development Studio,
 Studio is installed   which you are creating the custom report model.         see the SQL Server
                                                                               2008 documentation.

 Create a report       A report model project contains the definition of the   For more information,
 model project         data source (a .ds file), the definition of a data      see the To create the
                       source view (a .dsv file), and the report model (an     report model project
                       .smdl file).                                            section in this topic.

 Define a data         After creating a report model project, you have to      For more information,
 source for a          define one data source from which you extract           see the To define the
 report model          business data. Typically, this is the Configuration     data source for the
                       Manager site database.                                  report model section
                                                                               in this topic.

 Define a data         After defining the data sources that you use in your    For more information,
 source view for a     report model project, the next step is to define a      see the To define the
 report model          data source view for the project. A data source view    data source view for
                       is a logical data model based on one or more data

<!-- p.1935 -->

Step               Description                                             More information

                   sources. Data source views encapsulate access to the    the report model
                   physical objects, such as tables and views, contained   section in this topic.
                   in underlying data sources. SQL Server Reporting
                   Services generates the report model from the data
                   source view.

                   Data source views facilitate the model design
                   process by providing you with a useful
                   representation of the data that you specified.
                   Without changing the underlying data source, you
                   can rename tables and fields, and add aggregate
                   fields and derived tables in a data source view. For
                   an efficient model, add only those tables to the data
                   source view that you intend to use.

Create a report    A report model is a layer on top of a database that     For more information,
model              identifies business entities, fields, and roles. When   see the To create the
                   published, by using these models, Report Builder        report model section
                   users can develop reports without having to be          in this topic.
                   familiar with database structures or understand and
                   write queries. Models are composed of sets of
                   related report items that are grouped together
                   under a friendly name, with predefined relationships
                   between these business items and with predefined
                   calculations. Models are defined by using an XML
                   language called Semantic Model Definition
                   Language (SMDL). The file name extension for
                   report model files is .smdl.

Publish a report   To build a report by using the model that you just      For more information,
model              created, you must publish it to a report server. The    see the To publish the
                   data source and data source view are included in the    report model for use
                   model when it is published.                             in SQL Server
                                                                           Reporting Services
                                                                           section in this topic.

Deploy the         Before you can use a custom report model in the         For more information,
report model to    Create Report Wizard to create a model-based            see the To deploy the
Configuration      report, you must deploy the report model to             custom report model
Manager            Configuration Manager.                                  to Configuration
                                                                           Manager section in
                                                                           this topic.

Steps for creating a basic report model in SQL
Server Reporting Services

<!-- p.1936 -->

You can use the following procedures to create a basic report model that users in your
site can use to build particular model-based reports based on data in a single view of
the Configuration Manager database. You create a report model that presents
information about the client computers in your site to the report author. This
information is taken from the v_R_System view in the Configuration Manager database.

On the computer where you perform these procedures, ensure that you have installed
SQL Server Business Intelligence Development Studio and that the computer has
network connectivity to the reporting services point server. For detailed information
about SQL Server Business Intelligence Development Studio, see the SQL Server 2008
documentation.

To create the report model project
   1. On the desktop, click Start, click Microsoft SQL Server 2008, and then click SQL
     Server Business Intelligence Development Studio.

   2. After SQL Server Business Intelligence Development Studio opens in Microsoft
     Visual Studio, click File, click New, and then click Project.

   3. In the New Project dialog box, select Report Model Project in the Templates list.

   4. In the Name box, specify a name for this report model. For this example, type
     Simple_Model.

   5. To create the report model project, click OK.

   6. The Simple_Model solution is displayed in Solution Explorer.

       ７ Note

       If you cannot see the Solution Explorer pane, click View, and then click
       Solution Explorer.

To define the data source for the report model
   1. In the Solution Explorer pane of SQL Server Business Intelligence Development
     Studio, right-click Data Sources to select Add New Data Source.

   2. On the Welcome to the Data Source Wizard page, click Next.

   3. On the Select how to define the connection page, verify that Create a data source
     based on an existing or new connection is selected, and then click New.

<!-- p.1937 -->

 4. In the Connection Manager dialog box, specify the following connection
   properties for the data source:

        Server name: Type the name of your Configuration Manager site database
        server, or select it in the list. If you are working with a named instance instead
        of the default instance, type <database server>\<instance name>.

        Select Use Windows Authentication.

        In Select or enter a database name list, select the name of your
        Configuration Manager site database.

 5. To verify the database connection, click Test Connection.

 6. If the connection succeeds, click OK to close the Connection Manager dialog box.
   If the connection does not succeed, verify that the information you entered is
   correct, and then click Test Connection again.

 7. On the Select how to define the connection page, verify that Create a data source
   based on an existing or new connection is selected, verify that the data source
   you have just specified is selected in Data connections, and then click Next.

 8. In Data source name, specify a name for the data source, and then click Finish. For
   this example, type Simple_Model.

 9. The data source Simple_Model.ds is now displayed in Solution Explorer under the
   Data Sources node.

     ７ Note

     To edit the properties of an existing data source, double-click the data source
     in the Data Sources folder of the Solution Explorer pane to display the data
     source properties in Data Source Designer.

To define the data source view for the report model
 1. In Solution Explorer, right-click Data Source Views to select Add New Data
   Source View.

 2. On the Welcome to the Data Source View Wizard page, click Next. The Select a
   Data Source page is displayed.

 3. In the Relational data sources window, verify that the Simple_Model data source is
   selected, and then click Next.

<!-- p.1938 -->

 4. On the Select Tables and Views page, select the following view in the Available
   objects list to be used in the report model: v_R_System (dbo).

       Tip

      To help locate views in the Available objects list, click the Name heading at
      the top of the list to sort the objects in alphabetical order.

 5. After selecting the view, click > to transfer the object to the Included objects list.

 6. If the Name Matching page is displayed, accept the default selections, and click
   Next.

 7. When you have selected the objects that you require, click Next, and then specify a
   name for the data source view. For this example, type Simple_Model.

 8. Click Finish. The Simple_Model.dsv data source view is displayed in the Data
   Source Views folder of Solution Explorer.

To create the report model
 1. In Solution Explorer, right-click Report Models to select Add New Report Model.

 2. On the Welcome to the Report Model Wizard page, click Next.

 3. On the Select Data Source Views page, select the data source view in the
   Available data source views list, and then click Next. For this example, select
   Simple_Model.dsv.

 4. On the Select report model generation rules page, accept the default values, and
   then click Next.

 5. On the Collect Model Statistics page, verify that Update model statistics before
   generating is selected, and then click Next.

 6. On the Completing the Wizard page, specify a name for the report model. For this
   example, verify that Simple_Model is displayed.

 7. To complete the wizard and create the report model, click Run.

 8. To exit the wizard, click Finish. The report model is shown in the Design window.

<!-- p.1939 -->

To publish the report model for use in SQL Server
Reporting Services
 1. In Solution Explorer, right-click the report model to select Deploy. For this
   example, the report model is Simple_Model.smdl.

 2. Examine the deployment status at the lower left corner of the SQL Server Business
   Intelligence Development Studio window. When the deployment has finished,
   Deploy Succeeded is displayed. If the deployment fails, the reason for the failure is
   displayed in the Output window. The new report model is now available on your
   SQL Server Reporting Services website.

 3. Click File, click Save All, and then close SQL Server Business Intelligence
   Development Studio.

To deploy the custom report model to Configuration
Manager
 1. Locate the folder in which you created the report model project. For example,
   %USERPROFILE%\Documents\Visual Studio 2008\Projects\<Project Name>.

 2. Copy the following files from the report model project folder to a temporary folder
   on your computer:

         <Model Name> .dsv

         <Model Name> .smdl

 3. Open the preceding files by using a text editor, such as Notepad.

 4. In the file <Model Name>.dsv, locate the first line of the file, which reads as
   follows:

   <DataSourceView
   xmlns="https://schemas.microsoft.com/analysisservices/2003/engine">

   Edit this line to read as follows:

   <DataSourceView xmlns="
   <https://schemas.microsoft.com/analysisservices/2003/engine>"

   xmlns:xsi="RelationalDataSourceView">

 5. Copy the entire contents of the file to the Windows Clipboard.

<!-- p.1940 -->

   6. Close the file <Model Name>.dsv.

   7. In the file <Model Name>.smdl, locate the last three lines of the file, which appear
     as follows:

     </Entity>

     </Entities>

     </SemanticModel>

   8. Paste the contents of the file <Model Name>.dsv directly before the last line of the
     file (<SemanticModel>).

   9. Save and close the file <Model Name>.smdl.

 10. Copy the file <Model Name>.smdl to the folder %programfiles%\Microsoft
     Configuration Manager \AdminConsole\XmlStorage\Other on the Configuration
     Manager site server.

       ） Important

       After copying the report model file to the Configuration Manager site server,
       you must exit and restart the Configuration Manager console before you can
       use the report model in the Create Report Wizard.

Steps for Creating an Advanced Report Model
in SQL Server Reporting Services
You can use the following procedures to create an advanced report model that users in
your site can use to build particular model-based reports based on data in multiple
views of the Configuration Manager database. You create a report model that presents
information about the client computers and the operating system installed on these
computers to the report author. This information is taken from the following views in
the Configuration Manager database:

     V_R_System: Contains information about discovered computers and the
     Configuration Manager client.

     V_GS_OPERATING_SYSTEM: Contains information about the operating system
     installed on the client computer.

<!-- p.1941 -->

    Selected items from the preceding views are consolidated into one list, given
    friendly names, and then presented to the report author in Report Builder for
    inclusion in particular reports.

    On the computer where you perform these procedures, ensure that you have
    installed SQL Server Business Intelligence Development Studio and that the
    computer has network connectivity to the reporting services point server. For
    detailed information about SQL Server Business Intelligence Development Studio,
    see the SQL Server documentation.

To create the report model project
  1. On the desktop, click Start, click Microsoft SQL Server 2008, and then click SQL
    Server Business Intelligence Development Studio.

  2. After SQL Server Business Intelligence Development Studio opens in Microsoft
    Visual Studio, click File, click New, and then click Project.

  3. In the New Project dialog box, select Report Model Project in the Templates list.

  4. In the Name box, specify a name for this report model. For this example, type
    Advanced_Model.

  5. To create the report model project, click OK.

  6. The Advanced_Model solution is displayed in Solution Explorer.

      ７ Note

      If you cannot see the Solution Explorer pane, click View, and then click
      Solution Explorer.

To define the data source for the report model

  1. In the Solution Explorer pane of SQL Server Business Intelligence Development
    Studio, right-click Data Sources to select Add New Data Source.

  2. On the Welcome to the Data Source Wizard page, click Next.

  3. On the Select how to define the connection page, verify that Create a data source
    based on an existing or new connection is selected, and then click New.

<!-- p.1942 -->

  4. In the Connection Manager dialog box, specify the following connection
    properties for the data source:

         Server name: Type the name of your Configuration Manager site database
         server, or select it in the list. If you are working with a named instance instead
         of the default instance, type <database server>\<instance name>.

         Select Use Windows Authentication.

         In the Select or enter a database name list, select the name of your
         Configuration Manager site database.

  5. To verify the database connection, click Test Connection.

  6. If the connection succeeds, click OK to close the Connection Manager dialog box.
    If the connection does not succeed, verify that the information you entered is
    correct, and then click Test Connection again.

  7. On the Select how to define the connection page, verify that Create a data source
    based on an existing or new connection is selected, verify that the data source
    you have just specified is selected in the Data connections list box, and then click
    Next.

  8. In Data source name, specify a name for the data source and then click Finish. For
    this example, type Advanced_Model.

  9. The data source Advanced_Model.ds is displayed in Solution Explorer under the
    Data Sources node.

      ７ Note

      To edit the properties of an existing data source, double-click the data source
      in the Data Sources folder of the Solution Explorer pane to display the data
      source properties in Data Source Designer.

To define the data source view for the report model

  1. In Solution Explorer, right-click Data Source Views to select Add New Data
    Source View.

  2. On the Welcome to the Data Source View Wizard page, click Next. The Select a
    Data Source page is displayed.

<!-- p.1943 -->

  3. In the Relational data sources window, verify that the Advanced_Model data
    source is selected, and then click Next.

  4. On the Select Tables and Views page, select the following views in the Available
    objects list to be used in the report model:

         v_R_System (dbo)

         v_GS_OPERATING_SYSTEM (dbo)

         After selecting each view, click > to transfer the object to the Included
         objects list.

       Tip

      To help locate views in the Available objects list, click the Name heading at
      the top of the list to sort the objects in alphabetical order.

  5. If the Name Matching dialog box appears, accept the default selections, and click
    Next.

  6. When you have selected the objects you require, click Next, and then specify a
    name for the data source view. For this example, type Advanced_Model.

  7. Click Finish. The Advanced_Model.dsv data source view is displayed in the Data
    Source Views folder of Solution Explorer.

To define relationships in the data source view

  1. In Solution Explorer, double-click Advanced_Model.dsv to open the Design
    window.

  2. Right-click the title bar of the v_R_System window to select Replace Table, and
    then click With New Named Query.

  3. In the Create Named Query dialog box, click the Add Table icon (typically the last
    icon in the ribbon).

  4. In the Add Table dialog box, click the Views tab, select V_GS_OPERATING_SYSTEM
    in the list, and then click Add.

  5. Click Close to close the Add Table dialog box.

  6. In the Create Named Query dialog box, specify the following information:

<!-- p.1944 -->

       Name: Specify the name for the query. For this example, type
       Advanced_Model.

       Description: Specify a description for the query. For this example, type
       Example Reporting Services report model.

7. In the v_R_System window, select the following items in the list of objects to
  display in the report model:

       ResourceID

       ResourceType

       Active0

       AD_Domain_Name0

       AD_SiteName0

       Client0

       Client_Type0

       Client_Version0

       CPUType0

       Hardware_ID0

       User_Domain0

       User_Name0

       Netbios_Name0

       Operating_System_Name_and0

8. In the v_GS_OPERATING_SYSTEM box, select the following items in the list of
  objects to display in the report model:

       ResourceID

       Caption0

       CountryCode0

       CSDVersion0

       Description0

<!-- p.1945 -->

          InstallDate0

          LastBootUpTime0

          Locale0

          Manufacturer0

          Version0

          WindowsDirectory0

  9. To present the objects in these views as one list to the report author, you must
    specify a relationship between the two tables or views by using a join. You can join
    the two views by using the object ResourceID, which appears in both views.

 10. In the v_R_System window, click and hold the ResourceID object and drag it to the
    ResourceID object in the v_GS_OPERATING_SYSTEM window.

 11. Click OK.

 12. The Advanced_Model window replaces the v_R_System window and contains all of
    the necessary objects required for the report model from the v_R_System and the
    v_GS_OPERATING_SYSTEM views. You can now delete the
    v_GS_OPERATING_SYSTEM window from the Data Source View Designer. Right-
    click the title bar of the v_GS_OPERATING_SYSTEM window to select Delete Table
    from DSV. In the Delete Objects dialog box, click OK to confirm the deletion.

 13. Click File, and then click Save All.

To create the report model

  1. In Solution Explorer, right-click Report Models to select Add New Report Model.

  2. On the Welcome to the Report Model Wizard page, click Next.

  3. On the Select Data Source View page, select the data source view in the Available
    data source views list, and then click Next. For this example, select
    Simple_Model.dsv.

  4. On the Select report model generation rules page, do not change the default
    values, and click Next.

  5. On the Collect Model Statistics page, verify that Update model statistics before
    generating is selected, and then click Next.

<!-- p.1946 -->

  6. On the Completing the Wizard page, specify a name for the report model. For this
    example, verify that Advanced_Model is displayed.

  7. To complete the wizard and create the report model, click Run.

  8. To exit the wizard, click Finish.

  9. The report model is shown in the Design window.

To modify object names in the report model
  1. In Solution Explorer, right-click a report model to select View Designer. For this
    example, select Advanced_Model.smdl.

  2. In the report model Design view, right-click any object name to select Rename.

  3. Type a new name for the selected object, and then press Enter. For example, you
    could rename the object CSD_Version_0 to read Windows Service Pack Version.

  4. When you have finished renaming objects, click File, and then click Save All.

To publish the report model for use in SQL Server Reporting
Services
  1. In Solution Explorer, right-click Advanced_Model.smdl to select Deploy.

  2. Examine the deployment status at the lower left corner of the SQL Server Business
    Intelligence Development Studio window. When the deployment has finished,
    Deploy Succeeded is displayed. If the deployment fails, the reason for the failure is
    displayed in the Output window. The new report model is now available on your
    SQL Server Reporting Services website.

  3. Click File, click Save All, and then close SQL Server Business Intelligence
    Development Studio.

To deploy the custom report model to Configuration Manager
  1. Locate the folder in which you created the report model project. For example,
    %USERPROFILE%\Documents\Visual Studio 2008\Projects\<Project Name>.

  2. Copy the following files from the report model project folder to a temporary folder
    on your computer:

          <Model Name> .dsv

<!-- p.1947 -->

         <Model Name> .smdl

 3. Open the preceding files by using a text editor, such as Notepad.

 4. In the file <Model Name>.dsv, locate the first line of the file, which reads as
   follows:

   <DataSourceView

   xmlns="https://schemas.microsoft.com/analysisservices/2003/engine">

   Edit this line to read as follows:

   <DataSourceView xmlns="
   <https://schemas.microsoft.com/analysisservices/2003/engine>"

   xmlns:xsi="RelationalDataSourceView">

 5. Copy the entire contents of the file to the Windows Clipboard.

 6. Close the file <Model Name>.dsv.

 7. In the file <Model Name>.smdl, locate the last three lines of the file, which appear
   as follows:

   </Entity>

   </Entities>

   </SemanticModel>

 8. Paste the contents of the file <Model Name>.dsv directly before the last line of the
   file (<SemanticModel>).

 9. Save and close the file <Model Name>.smdl.

10. Copy the file <Model Name>.smdl to the folder %programfiles%\Microsoft
   Endpoint Manager\AdminConsole\XmlStorage\Other on the Configuration
   Manager site server.

      ） Important

      After copying the report model file to the Configuration Manager site server,
      you must exit and restart the Configuration Manager console before you can
      use the report model in the Create Report Wizard.

<!-- p.1948 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1949 -->

The data warehouse service point for
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use the data warehouse service point to store and report on long-term historical data
for your Configuration Manager deployment.

The data warehouse supports up to 2 TB of data, with timestamps for change tracking.
The data warehouse stores data by automatically synchronizing data from the
Configuration Manager site database to the data warehouse database. This information
is then accessible from your reporting service point. Data synchronized to the data
warehouse database is kept for three years. Periodically, a built-in task removes data
that's older than three years.

Data that is synchronized includes the following from the global data and site data
groups:

        Infrastructure health
        Security
        Compliance
        Malware
        Software deployments
        Inventory details (however, inventory history isn't synchronized)

When the site system role installs, it installs and configures the data warehouse
database. It also installs several reports so you can easily search for and report on this
data.

Prerequisites
        The data warehouse site system role is supported only at the top-tier site of your
        hierarchy. For example, a central administration site (CAS) or standalone primary
        site.

        Starting in version 2107, the server where you install this site system role requires
        .NET version 4.6.2, and version 4.8 is recommended. In version 2103 and earlier,
        this role requires .NET 4.5.2 or later. For more information, Site and site system
        prerequisites.

<!-- p.1950 -->

     Grant the Reporting Services Point Account the db_datareader permission on the
     data warehouse database.

     To synchronize data with the data warehouse database, Configuration Manager
     uses the computer account of the site system role. This account requires the
     following permissions:

          Administrator on the computer that hosts the data warehouse database.

          DB_Creator permission on the data warehouse database.

          Either DB_owner or DB_reader with execute permissions to the top-tier site's
          database.

     The data warehouse database requires the use of SQL Server 2012 or later. The
     edition can be Standard, Enterprise, or Datacenter. The SQL Server version for the
     data warehouse doesn't need to be the same as the site database server.

     The warehouse database supports the following SQL Server configurations:

          A default or named instance

          SQL Server Always On availability group

          SQL Server Always On failover cluster instance

     If you use distributed views, install the data warehouse service point on the same
     server that hosts the CAS's database.

For more information on SQL Server licensing, see the product and licensing FAQ.

Size the data warehouse database the same as your site database. While the data
warehouse is smaller at first, it will grow over time.

Install
Each hierarchy supports a single instance of this role, on any site system of the top-tier
site. The SQL Server that hosts the database for the warehouse can be local to the site
system role, or remote. The data warehouse works with the reporting services point
installed at the same site. You don't need to install the two site system roles on the same
server.

To install the role, use the Add Site System Roles Wizard or the Create Site System
Server Wizard. For more information, see Install site system roles. On the System Role
Selection page of the wizard, select the Data Warehouse service point role.

<!-- p.1951 -->

When you install the role, Configuration Manager creates the data warehouse database
for you on the instance of SQL Server that you specify. If you specify the name of an
existing database, Configuration Manager doesn't create a new database. Instead it uses
the one you specify. This process is the same as when you move the data warehouse
database to a new SQL Server.

Configure properties

General page
     SQL Server fully qualified domain name: Specify the full qualified domain name
     (FQDN) of the server that hosts the data warehouse service point database.

     SQL Server instance name, if applicable: If you don't use a default instance of SQL
     Server, specify the named instance.

     Database name: Specify a name for the data warehouse database. Configuration
     Manager creates the data warehouse database with this name. If you specify a
     database name that already exists on the instance of SQL Server, Configuration
     Manager uses that database.

     SQL Server port used for connection: Specify the TCP/IP port number used by the
     SQL Server that hosts the data warehouse database. The data warehouse
     synchronization service uses this port to connect to the data warehouse database.
     By default, it uses SQL Server port 1433 for communication.

     Data warehouse service point account: Set the User name that SQL Server
     Reporting Services uses when it connects to the data warehouse database.

Synchronization settings page
     Data Synchronization custom setting: Choose the option to Select tables. In the
     Database tables window, select the table names to synchronize to the data
     warehouse database. Use the filter to search by name, or select the drop-down list
     to choose specific groups. Select OK when complete to save.

       ７ Note

       You can't remove tables that the role selects by default.

<!-- p.1952 -->

     Start time: Specify the time that you want the data warehouse synchronization to
     start.

     Recurrence pattern

        Daily: Specify that synchronization runs every day.

        Weekly: Specify a single day each week, and weekly recurrence for
        synchronization.

Reporting
After you install a data warehouse service point, several reports become available on the
reporting services point for the site. If you install the data warehouse service point
before installing a reporting services point, the reports are automatically added when
you later install the reporting services point.

  ７ Note

  The data warehouse point supports alternative credentials. Specify credentials that
  SQL Server Reporting Services uses to connect to the data warehouse database.
  Data warehouse reports don't open until you add credentials.

  To specify an account, set the User name for the data warehouse service point
  account in the role properties. For more information, see Configure properties.

The data warehouse site system role includes the following reports, under the Data
Warehouse category:

     Application Deployment - Historical: View details for application deployment for a
     specific application and machine.

     Endpoint Protection and Software Update Compliance - Historical: View
     computers that are missing software updates.

     General Hardware Inventory - Historical: View all hardware inventory for a specific
     machine.

     General Software Inventory - Historical: View all software inventory for a specific
     machine.

     Infrastructure Health Overview - Historical: Displays an overview of the health of
     your Configuration Manager infrastructure.

<!-- p.1953 -->

     List of Malware Detected - Historical: View malware that has been detected in the
     organization.

     Software Distribution Summary - Historical: A summary of software distribution
     for a specific advertisement and machine.

Exclude data warehouse reporting tables from
synchronization
(Introduced in version 2203)

When you install the data warehouse, it synchronizes a set of default tables from the site
database. These tables are required for data warehouse reports. While troubleshooting
issues, you may want to stop synchronizing these default tables. Starting in version
2203, you can exclude one or more of these required tables from synchronization. To
exclude tables from synchronization:

   1. From the Administration workspace, open Site Configuration > Servers and Site
     System Roles.
   2. Select the server where the data warehouse service point is installed.
   3. In the Site System Roles details pane, select the Data Warehouse service point
     role, then select Properties.
   4. On the Synchronization settings page, choose Select tables.
   5. In the Database tables window, deselect one or more tables of type Required.
   6. The console will prompt you to confirm the change, since some reports may no
     longer work correctly.

Site expansion
Before you can install a CAS to expand an existing standalone primary site, first uninstall
the data warehouse service point role. After you install the CAS, you can then install the
site system role at the CAS.

Unlike a move of the data warehouse database, this change results in a loss of the
historic data you have previously synchronized at the primary site. It isn't supported to
back up the database from the primary site and restore it at the CAS.

Move the database
Use the following steps to move the data warehouse database to a new SQL Server:

<!-- p.1954 -->

   1. Use SQL Server Management Studio to back up the data warehouse database.
     Then, restore that database to a SQL Server on the new computer that hosts the
     data warehouse.

        ７ Note

        After you restore the database to the new server, make sure the database
        access permissions are the same on the new data warehouse database as they
        were on the original data warehouse database.

   2. Use the Configuration Manager console to remove the data warehouse service
     point role from the current server.

   3. Reinstall the data warehouse service point. Specify the name of the new SQL Server
     and instance that hosts the restored data warehouse database.

   4. After the site system role installs, the move is complete.

Troubleshoot

Log files
Use the following logs to investigate problems with the installation of the data
warehouse service point, or synchronization of data:

     DWSSMSI.log and DWSSSetup.log: Use these logs to investigate errors when
     installing the data warehouse service point.

     Microsoft.ConfigMgrDataWarehouse.log: Use this log to investigate data
     synchronization between the site database to the data warehouse database.

Set up failure
When the data warehouse service point role is the first one that you install on a remote
server, installation fails for the data warehouse.

To work around this issue, make sure that the computer on which you install the data
warehouse service point already hosts at least one other role.

Synchronization failed to populate schema objects

<!-- p.1955 -->

Synchronization fails with the following message in
Microsoft.ConfigMgrDataWarehouse.log: failed to populate schema objects

To work around this issue, make sure that the computer account of the site system role
is a db_owner on the data warehouse database.

Reports fail to open
Data warehouse reports fail to open when the data warehouse database and reporting
service point are on different site systems.

To work around this issue, grant the Reporting Services Point Account the
db_datareader permission on the data warehouse database.

Error opening reports
When you open a data warehouse report, it returns the following error:

  Output

  An error has occurred during report processing. (rsProcessingAborted)
  Cannot create a connection to data source
  'AutoGen__39B693BB_524B_47DF_9FDB_9000C3118E82_'. (rsErrorOpeningConnection)
  A connection was successfully established with the server, but then an error
  occurred during the pre-login handshake. (provider: SSL Provider, error: 0 -
  The certificate chain was issued by an authority that is not trusted.)

This issue should only occur when the site database and data warehouse database are
on separate SQL Servers.

To work around this issue, use the following steps to configure certificates:

   1. On the server that hosts the data warehouse database:
      a. Create a self-signed certificate. Open IIS, select Server Certificates, and then
           select the Create Self-Signed Certificate action. Specify the "friendly name" of
           the certificate name as Data Warehouse SQL Server Identification Certificate.
           Select the certificate store as Personal.

         Tip

        If this server doesn't already have IIS, install it first.

<!-- p.1956 -->

   a. Manage the certificate. Open the Microsoft Management Console (MMC), and
      add the Certificates snap-in. Select Computer account of the local machine.
      Expand the Personal folder, and select Certificates.

       i. Give the SQL Server service account read permissions to the certificate. Select
         the Data Warehouse SQL Server Identification Certificate certificate, then
         go to the Action menu, select All Tasks, and select Manage Private Keys.
         Add the SQL Server service account, and allow Read permission.

      ii. Export the Data Warehouse SQL Server Identification Certificate as a DER
         encoded binary X.509 (.CER) file.

   b. Reconfigure SQL. Open SQL Server Configuration Manager.

       i. Under SQL Server Network Configuration, right-click to select Properties
         under Protocols for MSSQLSERVER. Switch to the Certificate tab, select Data
         Warehouse SQL Server Identification Certificate as the certificate, and then
         save the changes.

      ii. Under SQL Server Services, restart the SQL Server service. If SQL Server
         Reporting Services is also installed on the server that hosts the data
         warehouse database, restart Reporting Service services as well.

 2. On the server that hosts SQL Server Reporting Services, open the MMC, and add
   the Certificates snap-in. Select Computer account. Under the Trusted Root
   Certificate Authorities folder, import the Data Warehouse SQL Server
   Identification Certificate.

Data flow

<!-- p.1957 -->

                                                                                                

Data storage and synchronization

                                                                                   ﾉ   Expand table

Step   Details

1      The site server transfers and stores data in the site database.

2      Based on its schedule and configuration, the data warehouse service point gets data from
       the site database.

3      The data warehouse service point transfers and stores a copy of the synchronized data in
       the data warehouse database.

Reporting flow

                                                                                   ﾉ   Expand table

Step   Details

A      Using built-in reports, a user requests data. This request is passed to the reporting service
       point using SQL Server Reporting Services.

<!-- p.1958 -->

 Step   Details

 B      Most reports are for current information, and these requests are run against the site
        database.

 C      When a report requests historical data by using one of the reports with a Category of Data
        Warehouse, the request runs against the data warehouse database.

Feedback
Was this page helpful?      Yes     No

Provide product feedback

<!-- p.1959 -->

Support Center for Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Use Support Center for client troubleshooting, real-time log viewing, or capturing the
state of a Configuration Manager client computer for later analysis. Support Center is a
single tool to combine many administrator troubleshooting tools.

About
Support Center aims to reduce the challenges and frustration when troubleshooting
Configuration Manager client computers. Previously, when working with support to
address an issue with Configuration Manager clients, you would need to manually
collect log files and other information to help troubleshoot the issue. It was easy to
accidentally forget a crucial log file, causing headaches for you and the support
personnel who you're working with.

Use Support Center to streamline the support experience. It lets you:

      Create a troubleshooting bundle (.zip file) that contains the Configuration Manager
      client log files. You then have a single file to send to support personnel.

      View Configuration Manager client log files, certificates, registry settings, debug
      dumps, client policies.

      Real-time diagnostic of inventory (replaces ContentSpy), policy (replaces
      PolicySpy), and client cache.

Starting in version 2103, Support Center is split into the following tools:

      Support Center Client Data Collector: Collects data from a device to view in the
      Support Center Viewer. This separate tool encompasses the existing Support
      Center action to Collect selected data.

      Support Center Client Tools: The other Support Center troubleshooting
      functionality, except for Collect selected data.

The following tools are still a part of Support Center:

      Support Center Viewer

<!-- p.1960 -->

     Support Center OneTrace
     Support Center Log File Viewer

Support Center viewer
Support Center includes Support Center Viewer, a tool that support personnel use to
open the bundle of files that you create using Support Center. Support Center's data
collector collects and packages diagnostic logs from a local or remote Configuration
Manager client. To view data collector bundles, use the viewer application.

Support Center log file viewer
Support Center includes a modern log viewer. This tool replaces CMTrace and provides a
customizable interface with support for tabs and dockable windows. It has a fast
presentation layer, and can load large log files in seconds.

Support Center OneTrace
OneTrace is a new log viewer with Support Center. It works similarly to CMTrace, with
improvements. For more information, see Support Center OneTrace.

PowerShell cmdlets
Support Center also includes PowerShell cmdlets. Use these cmdlets to create a remote
connection to another Configuration Manager client, to configure the data collection
options, and to start data collection. These cmdlets are in separate PowerShell module
named ConfigMgrSupportCenter.PS. After you install Support Center, use the following
command to import this module:

  PowerShell

  Import-Module "C:\Program Files (x86)\Configuration Manager Support
  Center\ConfigMgrSupportCenter.PS.psd1"

Prerequisites
Install the following components on the server or client computer on which you install
Support Center:

     Any Windows OS version supported by Configuration Manager. For more
     information, see Supported OS versions for clients. Support Center doesn't support
