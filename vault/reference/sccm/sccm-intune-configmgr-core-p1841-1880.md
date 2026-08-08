---
title: "Core infrastructure documentation — pages 1841-1880"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1841-1880
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1841-1880
family: sccm
documentKind: "doc"
abstract: "Introduction to reporting in Configuration Manager Article • 10/04/2022 Applies to: Configuration Manager (current branch) Reporting in Configuration Manager provides a set of tools and resources that help you use the advanced reporting capabilities of SQL Server Reporting Servi"
---

# Core infrastructure documentation — pages 1841-1880

<!-- p.1841 -->

Introduction to reporting in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Reporting in Configuration Manager provides a set of tools and resources that help you
use the advanced reporting capabilities of SQL Server Reporting Services (SSRS) and
Power BI Report Server. Both reporting platforms provide rich authoring experiences for
custom reports. Reporting helps you gather, organize, and present information about
the wealth of Configuration Manager data in your organization. Configuration Manager
provides many predefined reports in Reporting Services that you can use without
changes. You can duplicate and modify the default reports to meet your requirements,
or you can create custom reports.

SQL Server Reporting Services
SQL Server Reporting Services provides a full range of ready-to-use tools and services to
help you create, deploy, and manage reports for your organization. It also has
programming features that enable you to extend and customize your reporting
functionality. Reporting Services is a server-based reporting platform that provides
comprehensive reporting functionality for different kinds of data sources.

Configuration Manager uses SQL Server Reporting Services as its primary reporting
solution. Integration with Reporting Services provides the following advantages:

      Uses an industry standard reporting system to query the Configuration Manager
      database.

      Displays reports by using the Configuration Manager Report Viewer or by using
      Report Manager, which is a web-based connection to the report.

      Provides high performance, availability, and scalability.

      Provides subscriptions to reports to which users can subscribe. For example, a
      manager subscribes to an emailed report each day that details the status of a
      software update rollout.

      Exports reports in different kinds of popular formats.

For more information, see What is SQL Server Reporting Services (SSRS)?

<!-- p.1842 -->

Power BI Report Server
Starting in version 2002, integrate Power BI Report Server with Configuration Manager
reporting. This integration gives you modern visualization and better performance. It
adds console support for Power BI reports similar to what already exists with SQL Server
Reporting Services. For more information, see Integrate with Power BI Report Server.

Power BI Report Server is an on-premises report server with a web portal in which you
display and manage reports. It includes tools to create Power BI reports, paginated
reports, mobile reports, and KPIs. For more information, see What is Power BI Report
Server?.

Reporting services point
The reporting services point is a site system role that you add on a server that runs
Microsoft SQL Server Reporting Services. The reporting services point does the following
functions:

     Copies the Configuration Manager report definitions to Reporting Services
     Creates report folders based on report categories
     Sets security policy on the report folders and reports. These policies are based on
     the role-based permissions for Configuration Manager administrative users. In a
     10-minute interval, the reporting services point connects to Reporting Services to
     reapply the security policy if you changed it.

For more information about how to plan for and install a reporting services point, see
the following articles:

     Plan for reporting

     Configure reporting

Configuration Manager reports
Configuration Manager provides report definitions for over 400 reports in over 50 report
folders. During the reporting services point installation process, it copies them to the
root report folder in SQL Server Reporting Services. The Configuration Manager console
shows the reports and organizes them in subfolders based on the report category.

Reports don't propagate up or down the Configuration Manager hierarchy. They run
only against the database of the site in which you create them. Because Configuration
Manager replicates global data throughout the hierarchy, you have access to hierarchy-

<!-- p.1843 -->

wide information in reports. When a report retrieves data from a site database, it has
access to site data for the current site and child sites, and global data for every site in
the hierarchy.

Like other Configuration Manager objects, an administrative user must have the
appropriate permissions to run or modify reports. To run a report, an administrative user
must have the Run Report permission for the object. To create or modify a report, an
administrative user must have the Modify Report permission for the object.

Create and modify reports
For Reporting Services-based reports, Configuration Manager uses Microsoft SQL Server
Report Builder as the exclusive authoring and editing tool for model-based and SQL-
based reports. When you create or edit a report in the Configuration Manager console,
Report Builder opens. For more information, see Operations and maintenance for
reporting.

Starting in version 2002, to create or edit Power BI reports, the console integrates with
Power BI Desktop. For more information, see Create Power BI reports.

Run reports
When you run a Reporting Services-based report in the Configuration Manager console,
Report Viewer opens and connects to Reporting Services. After you specify any required
report parameters, Reporting Services then retrieves the data and displays the results in
the viewer. You can also connect to the SQL Services Reporting Services, connect to the
data source for the site, and run reports.

Starting in version 2002, when you run a Power BI-based report, it opens in the web
browser.

Add to Favorites
Configuration Manager ships with several hundred reports by default, and you might
add more to that list. Instead of continually searching for reports you commonly use,
starting in version 2103 you can make a report a favorite. This action allows you to
quickly access it from the Favorites node.

For more information, see Operations and maintenance for reporting.

Report prompts

<!-- p.1844 -->

You can configure a report prompt or parameter when you create or modify a report.
Create report prompts to limit or target the data that a report retrieves. A report can
contain more than one prompt. Make sure the prompt names are unique and contain
only alphanumeric characters that conform to the SQL Server rules for identifiers.

When you run a report, the prompt requests a value for a required parameter. Based on
the parameter value, it retrieves the report data. For example, the Computer
information for a specific computer report prompts for a computer name. Reporting
Services passes the specified value to a variable defined in the report's SQL statement.

Report links
Report links in Configuration Manager are used in a source report to provide easy
access to other data. For example, it can link to more detailed information about each of
the items in the source report. If the destination report requires one or more prompts to
run, the source report must contain a column with the appropriate values for each
prompt.

The link needs to specify the column number with the value for the prompt. For
example:

     There's one report that lists computers that the site recently discovered.
     You link from it to another report that lists the last messages that the site receives
     for a specific computer.
     You create the link, and specify that column 2 in the source report contains the
     computer name. This value is a required prompt for the destination report.
     You run the source report, and a link icon appears to the left of each row of data.
     You select the icon on a row, and Report Viewer passes the value in the specified
     column for that row as the prompt value for the destination report.

You can only configure one link for a report, and that link can only connect to a single
destination report.

  ２ Warning

  If you move a destination report to a different report folder, the location for the
  destination report changes. Configuration Manager doesn't automatically update
  the report link in the source report with the new location, and the link won't work in
  the source report.

Report folders

<!-- p.1845 -->

Report folders provide a method to sort and filter reports that Configuration Manager
stores in Reporting Services. Report folders are useful when you have many reports to
manage. When you install a reporting services point, it copies reports to Reporting
Services and organizes them into more than 50 report folders. The report folders are
read-only. You can't modify them in the Configuration Manager console.

Report subscriptions
A report subscription in Reporting Services is a recurring request to deliver a report at a
specific time or in response to an event. You specify in the subscription an application
file format. Subscriptions provide an alternative to running a report on demand. On-
demand reporting requires that you actively select the report each time you want to
view the report. In contrast, subscriptions can be used to schedule and then automate
the delivery of a report.

You can manage report subscriptions in the Configuration Manager console. The report
server processes the subscriptions. It distributes them by using delivery extensions that
are deployed on the server. By default, you can create subscriptions that send reports to
a shared folder or to an email address.

For more information, see Manage report subscriptions.

Report Builder
For Reporting Services-based reports, Configuration Manager uses Microsoft SQL Server
Report Builder as the exclusive authoring and editing tool for both model-based and
SQL-based reports. If you create or edit a report in the Configuration Manager console,
Report Builder opens. When you create or modify a report for the first time, Report
Builder installs automatically. The version of Report Builder associated with the installed
version of SQL Server opens when you run or edit reports.

The Report Builder installation adds support for over 20 languages. When you run
Report Builder, it displays data in the language of the local computer's OS. If Report
Builder doesn't support the language, it displays the data in English. Report Builder
supports the full capabilities of SQL Server Reporting Services, which includes the
following capabilities:

     Delivers an intuitive report authoring environment with an appearance similar to
     Microsoft 365 Apps.

     Offers the flexible report layout of SQL Server report definition language (RDL).

<!-- p.1846 -->

     Provides various forms of data visualization including charts and gauges.

     Provides richly formatted text boxes.

     Exports to Microsoft Word format.

You can also open Report Builder directly from SQL Server Reporting Services.

Report models in SQL Server Reporting
Services
SQL Server Reporting Services uses report models to help you select items from the
Configuration Manager database to include in model-based reports. When you build a
report, report models expose only specified views and items to choose from. To create
model-based reports, at least one report model has to be available.

Report models have the following features:

     Give logical business names to database fields and views. To produce reports, you
     don't require knowledge of the Configuration Manager database structure.

     Group items logically.

     Define relationships between items.

     Secure model elements so that administrative users can see only the data that they
     have permission to see.

Although Configuration Manager provides sample report models, you can also define
report models to meet your own business requirements. For more information about
how to create report models, see Create custom report models.

Next steps
Plan for reporting

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1847 -->

Integrate with Power BI Report Server
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can integrate Power BI Report Server with Configuration Manager reporting. This
integration gives you modern visualization and better performance. It adds console
support for Power BI reports similar to what already exists with SQL Server Reporting
Services.

Save Power BI Desktop report files (.PBIX) and deploy them to the Power BI Report
Server. This process is similar as with SQL Server Reporting Services report files (.RDL).
You can also launch the reports in the browser directly from the Configuration Manager
console.

Prerequisites
      Power BI Report Server license. For more information, see Licensing Power BI
      Report Server.

      Download Microsoft Power BI Report Server-September 2019          , or later.
           Don't install Power BI Report Server right away. For the proper process based on
           your environment, see Configure the reporting services point.
           It's recommended that you use a supported version of Power BI Report Server.
           For versioning information, see the Change log for Power BI Report Server.

      Download Microsoft Power BI Desktop (Optimized for Power BI Report Server -
      September 2019), or later. It's recommended that you use a supported version. For
      versioning information, see the Change log for Power BI Report Server.

      Use versions of Power BI Desktop:
           That are from the Microsoft Download Center     . Don't use a version from the
           Microsoft Store.
           That states they're Optimized for Power BI Report Server. Don't use versions
           that aren't Optimized for Power BI Report Server.

        ７ Note

        When using Configuration Manager version 2111 or earlier with Power BI
        Desktop (Optimized for Power BI Report Server - May 2021) or later, you may
        notice the following behavior:

<!-- p.1848 -->

             You might experience delays updating the data source on newly updated
             reports.
             You may receive The remote server returned an error; (400) Bad
             Request. errors in the SRSRP.log. For more information about the relevant

             change to Power BI Desktop (optimized for Power BI Report Server) May
             2021, see Change data source connection strings in Power BI reports. The
             version before the connection change ocurred is January 2021     .

     Power BI integration uses the same role-based administration for reporting.
        Power BI Report Server doesn't support reports that are enabled for role-based
        access. All report viewers will see the same results, whatever their assigned
        scope.

Configure the reporting services point
This process varies depending upon whether you already have this role in the site.

You have a reporting services point
Only use this process if you already have a reporting services point in the site. Do all
steps of this process on the same server:

   1. In Reporting Services Configuration Manager, back up the Encryption Keys. For
     more information, see SSRS Encryption Keys - Back Up and Restore Encryption
     Keys.

        ２ Warning

        If you skip this step, you'll lose access to any custom reports in SQL Server
        Reporting Services.

   2. Remove the reporting services point role from the site.

   3. Uninstall SQL Server Reporting Services, but keep the database.

   4. Install Power BI Report Server.

   5. Configure the Power BI Report Server

      a. Use the previous report server database.

<!-- p.1849 -->

      b. Use Reporting Services Configuration Manager to restore the Encryption Keys.

           Before you add the reporting services point role in Configuration Manager,
           use SQL Server Reporting Services Configuration Manager to test and verify
           the configuration. For more information, see Verify SQL Server Reporting
           Services installation.

   6. Add the reporting services point role in Configuration Manager.

You don't have a reporting services point
Only use this process if you don't already have a reporting services point in the site. Do
all steps of this process on the same server:

   1. Install Power BI Report Server.

   2. Add the reporting services point role in Configuration Manager. For more
     information, see Configure reporting.

Configure the Configuration Manager console
   1. On a computer that has the Configuration Manager console, update the
     Configuration Manager console to the latest version.

   2. Install Power BI Desktop. Make sure the language is the same and verify the
     versioning prerequisites.

   3. After it installs, launch Power BI Desktop at least once before you open the
     Configuration Manager console.

Create Power BI reports
   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     Reporting, and select the new Power BI Reports node.

   2. In the ribbon, select Create Report. This action opens Power BI Desktop.

   3. Create a report in Power BI Desktop.

           In Power BI Desktop, when you connect to a data source, select DirectQuery
           for the Connection settings.

           Only use supported SQL views in these reports. For more information, see
           Creating custom reports by using SQL Server views in Configuration

<!-- p.1850 -->

           Manager.

   4. When the report is ready to save, go to the File menu, select Save as, then choose
     Power BI Report Server.

   5. In the Power BI Report Server Selection window, enter the URL for the reporting
     services point as the New report server address. For example,
     https://rsp.contoso.com/Reports . Select OK.

   6. In the Save report window, double-click the ConfigMgr_<SiteCode> folder. For
     example, ConfigMgr_PS1 , where PS1 is the ConfigMgr site code. You can optionally
     choose or create (from the report server) a sub folder to store it in.

         Tip

        Reports and report folders with Power BI reports must be located in the
        ConfigMgr_<SiteCode> folder on the report server or they won't appear in the

        Configuration Manager console.

   7. In File name, enter a name for the report.

In the Configuration Manager console, you see the new report in the list of Power BI
Reports. If you don't see your reports, verify that you saved the reports to the
ConfigMgr_<SiteCode> folder.

There are sample reports available for download. For more information, see Install
Power BI sample reports.

Power BI report templates in Community hub
Using Community hub, you can share Power BI report templates you've created and
download templates that others have shared.

Contributing a Power BI report template (PBIT) files to
Community hub
   1. Open the Configuration Manager console and go to Community > Community
     hub
   2. If needed, select Sign in to sign into GitHub. You'll see the Your hub link after
     signing in.
   3. Select Your hub then Add an item to launch the Contribute item wizard.

<!-- p.1851 -->

 4. For the Type, choose Power BI Report Template then select Browse.
 5. Choose the .pbit file you want to contribute, then select Open.
 6. Edit the Name and Description for the report template then select Next when
   done.
 7. On the Organization page, select the GitHub Organization to use for organization
   branding if needed. Select Next to upload the template.
 8. Once the item is uploaded, you'll be given the pull request URL of the change for
   monitoring.
 9. Select Close when you're done to exit the wizard.

Downloading a Power BI report template (PBIT) file from
Community hub
 1. Open the Configuration Manager console, go to Community > Community hub.

 2. From All objects or a search, choose a Power BI report template, then select
   Download.

 3. Select a file location to save the downloaded .pbit file and choose Save.

 4. If Power BI Desktop (Optimized for Power BI Report Server) is installed, you'll be
   prompted to open the .pbit file.

 5. Select Yes and Power BI Desktop (Optimized for Power BI Report Server) will load
   the .pbit file.

 6. Specify your Configuration Manager database name and database server name
   when prompted, then select Load.

     ７ Note

     When loading or applying the data model, ignore any errors if you come
     across one. For example, if you see the following error: "Connecting to tables
     from more than one database isn't supported in DirectQuery mode", select
     Close. Then refresh the data source settings:
      a. In Power BI Desktop, in the ribbon, select Edit Queries, and then select
        Data source settings.
      b. Select Change Source, confirm your server and database names, and select
        OK.
      c. Close the data source settings window, and then select Apply changes.

<!-- p.1852 -->

   7. When the report data is loaded, select File > Save As, then select Power BI Report
     Server.

   8. Save the report to a folder on the root Configuration Manager reporting folder on
     the reporting point. You may want to create a Downloaded Reports folder for these
     items.

   9. Repeat the steps for any other report templates that were downloaded. When
     you're done, close Microsoft Power BI Desktop (Optimized for Power BI Report
     Server).

Known issues
There's a known issue with Power BI Report Server and email subscriptions. After you
configure the email settings in the Reporting Services Configuration Manager, when you
try to create a new subscription, the option to deliver a report by Email isn't available. To
work around this issue, restart the Power BI Report Server service.

Next steps
After you create a report, use the following actions in the Configuration Manager
console:

     Run in Browser: Opens the Power BI report in the web browser. Share this URL
     with others, for example:
      https://rsp.contoso.com/Reports/POWERBI/ConfigMgr_ABC/Windows%2010/Windows10%2

     0Dashboard?rs:embed=true

         Tip

        You can only view these reports in the web browser.

     Edit: Make changes to the report in Power BI Desktop. For an existing report, use
     the Save option to save changes back to the report server.

     Add to Favorites: Starting in version 2103, you can make a report a favorite. This
     action allows you to quickly access it from the Favorites node. For more
     information, see Operations and maintenance for reporting.

For more information on log files to use for reporting, see Log file reference - Reporting.

<!-- p.1853 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1854 -->

Install Power BI sample reports
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

You can integrate Power BI Report Server with Configuration Manager reporting. There
are sample reports available for download that you can install in Configuration Manager.
This article explains how to install the Power BI sample reports in Configuration
Manager.

Prerequisites
      Configuration Manager reporting services point with Power BI Report Server
      integrated

      Microsoft Power BI Desktop (Optimized for Power BI Report Server). Use a version
      released between September 2019 and January 2021        . For versioning
      information, see the Change log for Power BI Report Server.

        ） Important

        Use versions of Power BI Desktop:
           That are from the Microsoft Download Center . Don't use a version from
           the Microsoft Store
           That states they're Optimized for Power BI Report Server. Don't use
           versions that aren't Optimized for Power BI Report Server.
           That were released no earlier than September 2019 and no later than
           January 2021. Microsoft Power BI Desktop (Optimized for Power BI
           Report Server - January 2021)     is recommended.

Download the sample reports
To download the sample reports:

   1. Download the Power BI sample reports from the Microsoft Download Center       .

   2. Save the ConfigMgrSamplePowerBIReports.exe file.

<!-- p.1855 -->

   3. Move the file to a computer with Microsoft Power BI Desktop (Optimized for Power
     BI Report Server) installed if you downloaded it from a different device.

   4. Run the ConfigMgrSamplePowerBIReports.exe file to extract the .pbit files.

  ７ Note

  Some of the sample reports are also available for download in Community hub.

Install the sample reports
To install the sample reports:

   1. On the Power BI Report server, create a new folder called Sample Reports in the
     root Configuration Manager reporting folder.

                                                                                    

   2. Launch Microsoft Power BI Desktop (Optimized for Power BI Report Server).

   3. Select File then Open and navigate to where you saved the extracted .pbit files.

   4. Select one of the .pbit files you extracted from the
      ConfigMgrSamplePowerBIReports.exe file.

   5. Specify your Configuration Manager database name and database server name
     when prompted, then select Load.

<!-- p.1856 -->

                                                                                   

    ７ Note

    When loading or applying the data model, ignore any errors if you come
    across one. For example, if you see the following error: "Connecting to tables
    from more than one database isn't supported in DirectQuery mode", select
    Close. Then refresh the data source settings:
     a. In Power BI Desktop, in the ribbon, select Edit Queries, and then select
       Data source settings.
     b. Select Change Source, confirm your server and database names, and select
       OK.
     c. Close the data source settings window, and then select Apply changes.

6. When the report data is loaded, select File > Save As, then select Power BI Report
  Server.

                                                                                   

7. Save the report to the Sample Reports folder you created on the reporting point.

<!-- p.1857 -->

                                                                                  

  8. Repeat the steps for any other sample reports. When you're done, close Microsoft
     Power BI Desktop (Optimized for Power BI Report Server).

  9. In the Configuration Manager console, go to Monitoring > Power BI Reports >
     Sample Reports.

 10. Right-click on one of the reports and select Run in Browser to launch the report.

                                                                                  

Sample reports
The following sample Power BI reports are included in the download:

     Software Update Compliance Status
     Software Update Deployment Status
     Client Status
     Content Status
     Microsoft Edge Management

<!-- p.1858 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1859 -->

Plan for reporting in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Reporting in Configuration Manager provides a set of tools and resources that help you
use the advanced reporting capabilities of SQL Server Reporting Services or Power BI
Report Server. Use the following sections to help you plan for reporting in Configuration
Manager.

Where to install the reporting services point
When you run Configuration Manager reports at a site, the reports have access to the
information in the site database in which it connects. Use the following sections to help
you determine where to install the reporting services point and what data source to use.

  ７ Note

  For more information about planning for site systems in Configuration Manager,
  see Add site system roles.

Supported site system servers
You can install the reporting services point on a central administration site (CAS) and
primary sites. It works on multiple site systems at a site, and at other sites in the
hierarchy. Configuration Manager doesn't support the reporting services point at
secondary sites. The first reporting services point at a site is set as the default report
server. You can add more reporting services points at a site, but Configuration Manager
reports actively use the default report server at each site. Install the reporting services
point on the site server or a remote site system. For best performance, use SQL Server
Reporting Services on a remote site system server.

Data replication considerations
Consider the following factors to help you determine where to install your reporting
services points:

<!-- p.1860 -->

     A reporting services point with the CAS database as its reporting data source has
     access to all global and site data in the Configuration Manager hierarchy. If you
     require reports that contain site data for multiple sites in a hierarchy, consider
     installing the reporting services point on a site system at the CAS. Then use its
     database as the reporting data source.

     A reporting services point with a child primary site database as its reporting data
     source has access to global data and site data for only the local primary site and
     any child secondary sites. Site data for other primary sites in the Configuration
     Manager hierarchy doesn't replicate to this primary site. Reporting Services can't
     access site data for other primary sites. If you require reports that contain site data
     for a specific primary site or global data, and you don't want the user to have
     access to site data from other primary sites, install a reporting services point on a
     site system at the primary site. Then use the primary site's database as the
     reporting data source.

For more information on global and site data, see Types of data.

Network bandwidth considerations
Depending on how you configure the site, site systems in the same site communicate
with each other by using server message block (SMB), HTTP, or HTTPS. Configuration
Manager doesn't manage this communication. It can occur at any time without network
bandwidth control. Review your available network bandwidth before you install the
reporting services point role on a site system.

For more information about planning for site systems, see Add site system roles.

Plan for role-based administration
Security for reporting is much like other objects in Configuration Manager where you
can assign security roles and permissions to administrative users. Administrative users
can only run and modify reports for which they have appropriate security rights. To run
reports in the Configuration Manager console, users need the Read right for the Site
permission and the permissions configured for specific objects.

Unlike other objects in Configuration Manager, the security rights that you set for
administrative users in the Configuration Manager console are also configured in
Reporting Services. When you configure security rights in the Configuration Manager
console, the reporting services point connects to Reporting Services and sets
appropriate permissions for reports.

<!-- p.1861 -->

For example, the Software Update Manager security role has the Run Report and
Modify Report permissions. Users with the Software Update Manager role can only run
and modify reports for software updates. The Configuration Manager console doesn't
display reports for other objects to this role. The exception to this behavior is that some
reports aren't associated with specific Configuration Manager securable objects. For
these reports, the administrative user must have the Read right for the Site permission
to run the reports and the Modify right for the Site permission to modify the reports.

  ） Important

  For users from a different domain than that of the reporting services point account
  to successfully run reports, establish a two-way trust between the two domains.

Reports are fully enabled for role-based administration. Configuration Manager filters
the data for all included reports based on the permissions of the user who runs the
report. Users with specific roles can only view information defined for their roles.

For more information about security rights for reporting, see Configure reporting.

For more information about role-based administration in Configuration Manager, see
Configure role-based administration.

Reporting recommendations
Consider the following recommendations and tips for reporting in Configuration
Manager:

     For best performance, install the reporting services point on a remote site system.
     Although you can install it on the site server, the reporting services point performs
     best when you install it on a remote site system. When this role does background
     processing, it can compete for system resources with other roles. There are many
     variables to consider with site and role performance, but in general this
     configuration improves reporting and overall site performance.

     Optimize SQL Server Reporting Services queries. Typically any reporting delays are
     because of the time it takes to run queries and retrieve the results. Microsoft SQL
     Server tools such as Query Analyzer and Profiler can help you optimize queries.

     Schedule report subscription processing to run outside standard office hours.
     Whenever possible, processing subscriptions during off-hours can minimize the
     CPU processing on the Configuration Manager site database server. This practice
     also improves availability for unpredicted report requests.

<!-- p.1862 -->

     Site updates preserve built-in reports. If you modify a standard report, when the
     site updates, it renames the report with an underscore prefix ( _ ). This behavior
     makes sure that the site update doesn't overwrite the modified report by the
     standard report.

Security and privacy
Configuration Manager reports display information that it collects during standard
Configuration Manager management operations. For example, you can display a report
of information that Configuration Manager collected from discovery or inventory.
Reports can also contain the current status information for client management
operations, such as deploying software, and checking for compliance.

For more information about any security recommendations and privacy information for
Configuration Manager operations that might generate data that you can view in
reports, see Security and privacy for Configuration Manager.

Next steps
Prerequisites for reporting

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1863 -->

Prerequisites for reporting in
Configuration Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Reporting in Configuration Manager has the following dependencies:

      SQL Server Reporting Services
      Reporting services point
      Power BI Report Server (optional, starting in version 2002)

SQL Server Reporting Services
Before you can use reporting in Configuration Manager, install and configure SQL Server
Reporting Services.

For more information about planning and deploying Reporting Services, see the Install
SQL Server Reporting Services.

Install the Reporting Services database on either the default instance or a named
instance of a 64-bit SQL Server installation. Colocate the SQL Server instance with the
site system server, or configure it on a remote computer.

Configuration Manager supports the same versions of SQL Server for reporting as it
does for the site database. For more information, see Supported SQL Server versions.

Reporting services point
Before you can use reporting in Configuration Manager, configure the reporting services
point site system role.

For more information, see Site and site system prerequisites.

Power BI Report Server
Starting in version 2002, you can integrate reporting with Power BI Report Server. For
more information including prerequisites, see Integrate with Power BI Report Server.

<!-- p.1864 -->

Next steps
Configure reporting

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1865 -->

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

<!-- p.1866 -->

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

<!-- p.1867 -->

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

<!-- p.1868 -->

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

<!-- p.1869 -->

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

<!-- p.1870 -->

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

<!-- p.1871 -->

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

<!-- p.1872 -->

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

<!-- p.1873 -->

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

<!-- p.1874 -->

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

<!-- p.1875 -->

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

<!-- p.1876 -->

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

<!-- p.1877 -->

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

<!-- p.1878 -->

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

<!-- p.1879 -->

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

<!-- p.1880 -->

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
