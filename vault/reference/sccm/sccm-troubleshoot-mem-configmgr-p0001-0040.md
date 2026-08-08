---
title: "Welcome — pages 1-40"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0001-0040
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0001-0040
family: sccm
documentKind: "doc"
abstract: "Configuration Manager troubleshooting Welcome to Configuration Manager troubleshooting. These articles explain how to determine, diagnose, and fix issues that you might encounter when you use Microsoft Endpoint Configuration Manager. In the navigation pane on the left, browse th"
---

# Welcome — pages 1-40

<!-- p.1 -->

Configuration Manager troubleshooting
Welcome to Configuration Manager troubleshooting. These articles explain how to determine,
diagnose, and fix issues that you might encounter when you use Microsoft Endpoint
Configuration Manager. In the navigation pane on the left, browse through the article list or
use the search box to find issues and solutions.

  Content management

  ｃ HOW-TO GUIDE
  Troubleshoot content distribution

<!-- p.2 -->

How to obtain error code descriptions in
Configuration Manager reports
This article describes how to obtain error code descriptions in Configuration Manager reports.

Original product version: Configuration Manager
Original KB number: 944375

Obtain error code descriptions
Some reports that are included together with Configuration Manager display errors codes that
don't contain an error description. However, you can obtain a description by deciphering the
error code. To do this, follow these steps:

   1. In the Configuration Manager console, open the report that contains the error code that
     you want to decipher.

   2. Convert the error code from decimal to hexadecimal. For example, if the error code is
     -2147012889, you must convert -2147012889 to a hexadecimal value. In this case, the
     hexadecimal value is FFFFFFFF80072EE7.

   3. Remove the FFFFFFFF in front of the converted error code. In this example, the error code
     becomes 80072EE7.

   4. Use the following information to locate the error description:

           Converted error codes that begin with 80072 are typically WinHTTP error codes,
           such as host not found errors. Convert the trailing four hexadecimal bytes to a
           decimal value. For example, 2EE7 is 12007 decimal. To view the WinHTTP error
           codes, see Error Messages.

           For example, error code 12007 maps to the following error description:

             ERROR_WINHTTP_NAME_NOT_RESOLVED 12007 The server name cannot be
             resolved

           Converted error codes that begin with 8009 are typically CryptoAPI error codes,
           such as certificate expired errors or CN= mismatch errors. You can use the Trace32

<!-- p.3 -->

           program to view the error code directly when you type trace32 together with the
           error code. For more information about CryptoAPI error codes and other Windows
           System error codes, see Error Codes.

           Converted error codes that begin with 800402 or 800403 are typically Configuration
           Manager error codes.

           All other error codes are typically Windows error codes or third-party error codes.
           All Windows error codes can be identified by using the Trace32 program and by
           specifying the error code, such as 80072EE7.

Last updated on 03/30/2026

<!-- p.4 -->

Reports don't run in System Center 2012 R2
Configuration Manager
This article fixes a problem that blocks reports from running in System Center 2012 R2
Configuration Manager.

Original product version: Microsoft System Center 2012 R2 Configuration Manager
Original KB number: 3060813

Symptoms
Reports that are started from the Administrator Console in System Center 2012 R2
Configuration Manager or from the Reporting Services website may not run as expected.
Additionally, you may receive error messages that resemble the following:

  The DefaultValue expression for the report parameter 'UserTokenSIDs' contains an error:
  The specified directory service attribute or value does not
  exist.Details:System.Web.Services.Protocols.SoapException: The DefaultValue expression for
  the report parameter 'UserTokenSIDs' contains an error: The specified directory service
  attribute or value does not exist.

Cause
This problem may occur when the following conditions are true:

     You have Cumulative Update 4 or a later version for System Center 2012 R2 Configuration
     Manager installed.
     The Report Server Service Account doesn't have Read permissions to the OU in which the
     user running the report resides, or to Users or Computers container in Active Directory
     Domain Services (AD DS).

Resolution
To resolve this problem, grant the Report Server Service Account Read permissions to the OU
in which the user running the report resides, and to both the Users and Computers containers
in AD DS.

<!-- p.5 -->

Last updated on 03/30/2026

<!-- p.6 -->

Reporting stops working after you move a
reporting services point or enable TLS 1.2
in Configuration Manager
This article helps you fix an issue in which Configuration Manager reporting doesn't work after
you move the reporting services point role to a new server or you enable TLS 1.2 on the site
servers.

Original product version: Configuration Manager (current branch)
Original KB number: 4503578

Symptoms
After you move the reporting services point role to a new server, or you enable TLS 1.2 on the
site servers, reporting no longer works in Configuration Manager.

The following error messages are logged in the Srsrp.log file on the reporting services point:

  Successfully created srsserver SMS_SRS_REPORTING_POINT
  Reporting Services URL from Registry
  [https://<ServerName>.contoso.com/SCCMReportServer/ReportService2005.asmx]
  SMS_SRS_REPORTING_POINT
  The underlying connection was closed: An unexpected error occurred on a receive.
  SMS_SRS_REPORTING_POINT
  (!) SRS not detected as running SMS_SRS_REPORTING_POINT
  Failures reported during periodic health check by the SRS Server
  [<ServerName>.contoso.com]. SMS_SRS_REPORTING_POINT

Cause
This issue occurs because the site servers and site systems don't meet the requirements that
are described in How to enable TLS 1.2.

Resolution

<!-- p.7 -->

To fix this issue and enable TLS 1.2 in Configuration Manager, make sure that the site servers
and site systems meet the requirements that are described in How to enable TLS 1.2.

To do this, follow these steps:

   1. Verify that .NET Framework is updated and has strong cryptography enabled on all
     relevant computers.

     To do this, first determine your .NET Framework version number, and then follow these
     guidelines:

           .NET Framework 4.6.2 supports TLS 1.1 and TLS 1.2. No additional changes are
           required.

           .NET Framework 4.6 and earlier versions must be updated to support TLS 1.1 and
           TLS 1.2.

           If you're using .NET Framework 4.5.1 or 4.5.2 on Windows 8.1, Windows RT 8.1, or
           Windows Server 2012, the relevant updates and details are also available from
           Microsoft Update Catalog     .

           All Configuration Manager client computers and site systems should have the
           following registry values set.

           For 32-bit applications that are running on 32-bit systems or 64-bit applications
           that are running on 64-bit systems:

             [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v2.0.50727]
             "SystemDefaultTlsVersions"=dword:00000001
             "SchUseStrongCrypto"=dword:00000001

             [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319]
             "SystemDefaultTlsVersions"=dword:00000001
             "SchUseStrongCrypto"=dword:00000001

           For 32-bit applications that are running on 64-bit systems:

             [HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v2.0.5072
             7]
             "SystemDefaultTlsVersions"=dword:00000001
             "SchUseStrongCrypto"=dword:00000001

<!-- p.8 -->

             [HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v4.0.3031
             9]
             "SystemDefaultTlsVersions"=dword:00000001
             "SchUseStrongCrypto"=dword:00000001

  2. Verify that the SMS_Executive service is restarted after any updates are installed.

Last updated on 03/30/2026

<!-- p.9 -->

rsProcessingAborted error when you run
reports in Configuration Manager
This article helps you fix an issue in which you can't run reports for collections if you use
Microsoft SQL Server 2019 in Microsoft Endpoint Configuration Manager.

Applies to: Microsoft Endpoint Configuration Manager, SQL Server 2019

Symptoms
When you run reports for collections in Microsoft Endpoint Configuration Manager, you
receive the following error messages :

        An error has occurred during report processing. (rsProcessingAborted)

        The EXECUTE permission was denied on the object 'fnIsCas', database 'CM_LKD',
        schema 'dbo'

        The EXECUTE permission was denied on the object 'fnIsPrimary', database 'CM_IDR',
        schema 'dbo'

Refer to the following screenshot for an example of the error messages.

<!-- p.10 -->

When this issue occurs, the following error entries are logged in the
ReportingServicesService.log file on the reporting services point:

 Output

 processing!ReportServer_0-2!18fc!<Date>-<Time>:: e ERROR: Throwing
 Microsoft.ReportingServices.ReportProcessing.ReportProcessingException: ,
 Microsoft.ReportingServices.ReportProcessing.ReportProcessingException: Query
 execution failed for dataset 'DeploymentSummary'.

    ---> System.Data.SqlClient.SqlException: The EXECUTE permission was denied on
 the object 'fnIsCas', database 'CM_LKD', schema 'dbo'.

 processing!ReportServer_0-2!18fc!<Date>-<Time>:: e ERROR: An exception has occurred
 in data set 'DeploymentSummary'. Details:
 Microsoft.ReportingServices.ReportProcessing.ReportProcessingException: Query
 execution failed for dataset 'DeploymentSummary'.

    ---> System.Data.SqlClient.SqlException: The EXECUTE permission was denied on
 the object 'fnIsCas', database 'CM_LKD', schema 'dbo'.

 processing!ReportServer_0-2!18fc!<Date>-<Time>:: v VERBOSE: An exception has
 occurred. Trying to abort processing. Details:
 Microsoft.ReportingServices.ReportProcessing.ReportProcessingException: Query
 execution failed for dataset 'DeploymentSummary'.

    ---> System.Data.SqlClient.SqlException: The EXECUTE permission was denied on
 the object 'fnIsCas', database 'CM_LKD', schema 'dbo'.

<!-- p.11 -->

Cause
This issue occurs because of the Scalar UDF Inlining feature in SQL Server 2019. A query that
uses Scalar UDF Inlining might return an error or unexpected results. For more information, see
Scalar UDF Inlining issues in SQL Server 2019   .

Resolution
To fix this issue, install KB5000642 - cumulative update 9   or a later cumulative update for
SQL Server 2019.

 Last updated on 03/30/2026

<!-- p.12 -->

How to deploy a Windows language pack
as an application in Configuration Manager
This article describes how to deploy a Windows language pack as an application in
Configuration Manager, including logs that you can use to track the deployment.

Original product version: Configuration Manager (current branch)
Original KB number: 4468362

Deploy a language pack as an application
To deploy a language pack as an application in Configuration Manager, follow these steps:

   1. In Configuration Manager console, go to Software Library > Application management >
     Applications, and then select Create Application.

   2. On the General page of the Create Application Wizard, select Manually specify the
     application information, and then select Next.

<!-- p.13 -->

3. On the General Information page, specify information about the application, such as the
  application name and comments, and then select Next.

<!-- p.14 -->

4. On the Application Catalog page, specify information about how to display the
  application to users in the Application Catalog, and then select Next.

5. On the Deployment Types page, select Add to open the Create Deployment Type
  Wizard.

6. On the General page, select Script Installer from the Type list, and then select Next.

<!-- p.15 -->

7. On the General Information page, enter application name, and then select Next.

8. On the Content page, specify the content location, enter the following for Installation
  program, and then select Next.

    Console

    DISM /Online /Add-Package /PackagePath:.\

<!-- p.16 -->

9. On the Detection Method page, select Add Clause.

<!-- p.17 -->

10. For Detection Rule, select Registry from the Setting Type drop-down list, select
   HKEY_LOCAL_MACHINE for Hive, enter
    SYSTEM\CurrentControlSet\Control\MUI\UILanguages\<language name> in Key, (for example,

    SYSTEM\CurrentControlSet\Control\MUI\UILanguages\fr-FR ), and then select OK.

11. Select Next.

12. On User Experience page, select Install for system from the Installation behavior drop-
   down list, specify a Logon requirement, and then select Next.

<!-- p.18 -->

13. On the Requirements page, you can specify installation requirements by clicking Add.

   The following example requires deploying the language pack on Windows 10 version
   1803.

     ７ Note

     Language packs are specific to OS versions. Therefore, for example, Windows 10
     version 1803 language packs only work in version 1803, but not other versions.

   Example

    a. Select Custom for Category, and then select Create.

<!-- p.19 -->

b. Specify details at Create Global Condition.

c. Enter 1803 for Value, and then select OK.

<!-- p.20 -->

14. On Summary page, confirm the settings, and then select Next.

15. Wait for the wizard to complete, and then select Close to exit the wizard.

<!-- p.21 -->

16. Select Next.

17. On Summary page, confirm the settings for the application, and then select Next.

<!-- p.22 -->

18. Wait for the wizard to complete, and then select Close to exit the wizard.

19. After the application is created successfully, deploy it to the required collections.

20. On the client device, open Software Center, select the application, and then select Install.

21. Verify that the language pack was installed successfully by running the following
   command from an elevated command prompt:

     Console

     DISM /online /Get-intl

   The following is sample output:

<!-- p.23 -->

Use logs to track policy and application installation
You can use the following logs to track policy and application installation:

     Use PolicyAgent.log to check whether a policy is downloaded or not. In the following
     example, 88BF878E... is the deployment ID.

<!-- p.24 -->

Use AppDiscovery.log to check the discovery or detection of an application on client
devices.

Use AppIntentEval.log to check the current state of the application and its applicability.

<!-- p.25 -->

Use AppEnforce.log to track application installation on the client and to check the exit
code to verify that installation completed successfully.

Use DISM.log to determine whether installation started.

<!-- p.26 -->

Last updated on 03/25/2026

<!-- p.27 -->

Technical Reference for Application
Deployment in Configuration Manager
Applies to: Configuration Manager (current branch)

In this article, you'll learn how application deployments work.

Before You Begin
When troubleshooting application deployments, there are multiple items that can be useful
when reviewing client logs. These items include:

     Application CI ID
     Application Unique ID
     Deployment Type Unique ID
     Application Deployment Unique ID (also known as Assignment Unique ID)
     Application Deployment Purpose
     Content Unique ID
     Collection ID and Name
     Collection Type

To simplify troubleshooting, you can run a SQL query similar to the following query against the
Configuration Manager database to obtain the information listed previously.

 SQL

 SELECT APP.CI_ID [App CI ID], APP.CI_UniqueID [App Unique ID], APP.DisplayName [App
 Name],
 DT.CI_UniqueID [DT Unique ID], DT.ContentId [DT Content ID],
 CIA.Assignment_UniqueID [Assignment ID], CIA.CollectionID, CIA.CollectionName,
 CASE CIA.OfferTypeID WHEN 0 THEN 'Required' WHEN 2 THEN 'Available' WHEN 3 THEN
 'Simulate' ELSE 'Unknown' END AS [Deployment Purpose],
 CASE C.CollectionType WHEN 1 THEN 'User Collection' WHEN 2 THEN 'Device Collection'
 ELSE 'Unknown' END AS [Collection Type],
 DT.Technology, DT.DisplayName [DT Name]
 FROM fn_ListApplicationCIs(1033) APP
 JOIN fn_ListDeploymentTypeCIs(1033) DT ON DT.AppModelName = APP.ModelName AND
 DT.IsLatest = 1
 LEFT JOIN v_CIAssignmentToCI CIACI ON CIACI.CI_ID = APP.CI_ID
 LEFT JOIN v_CIAssignment CIA ON CIACI.AssignmentID = CIA.AssignmentID
 LEFT JOIN v_Collection C ON C.CollectionID = CIA.CollectionID
 WHERE APP.IsLatest = 1 AND APP.DisplayName = 'Application Name' -- Replace
 Application Name

  ） Important

<!-- p.28 -->

 When you execute this query, you must use the Application Name listed in the General
 Information tab of Application Properties, instead of using the Localized application name
 listed in the Software Center tab of Application properties.

Next Steps
     Application Deployment Policy

Last updated on 03/27/2026

<!-- p.29 -->

Application Deployment Policy
Applies to: Configuration Manager (current branch)

Policy Creation
When you deploy an application, an instance of SMS_ApplicationAssignment class is created
which represents the assignment of an application to a collection. This activity can be tracked
in the SMSProv.log file.

 Output

 SMS Provider    PutInstanceAsync SMS_ApplicationAssignment~
 SMS Provider    Auditing: User CONTOSO\Admin created an instance of class
 SMS_ApplicationAssignment.~

In the Configuration Manager database, this information is stored in the CI_CIAssignments
table where AssignmentType 2 represents an application deployment. When the assignment is
created, SMS Database Monitor component detects a change in the table then notifies Object
Replication Manager to process the CI Assignment (CIA) policy. Object Replication Manager
component then creates the policy for the application assignment in the database, which is
stored in the Policy table in the database, and the Policy ID is based on the Application
Unique ID. This activity can be tracked in the objreplmgr.log file by referencing the Assignment
Unique ID, which can be obtained from the SQL query referenced in the Before You Begin
section.

 Output

 ***** Processing Application Assignment {3AC57DFE-3F87-4C59-930B-B9F57CB41B91}
 *****

The policy for the application assignment can be seen in the database using a SQL query
similar to the following example.

 SQL

 SELECT P.PolicyID, PA.PolicyAssignmentID, PA.PADBID, PA.IsTombstoned,
 PA.LastUpdateTime FROM Policy P
 JOIN PolicyAssignment PA ON P.PolicyID = PA.PolicyID
 WHERE P.PolicyID = '{3AC57DFE-3F87-4C59-930B-B9F57CB41B91}' -- Replace Assignment
 Unique ID

<!-- p.30 -->

Policy Targeting
After the policy is generated, the Policy Provider component assigns this policy to the
resources in the collection that's targeted by the application deployment. The policy targeting
information is stored in the ResPolicyMap table in the database. You can use the PADBID
returned by the above query to track this activity in policypv.log. However, the PADBID
recorded in the log may not always match the PADBID returned by the above query if multiple
policies are getting processed simultaneously.

  Output

  ~Policy or Policy Target Change Event triggered.
  ~Completed batch with beginning PADBID = 16778403 ending PADBID = 16778403.

  ７ Note

   ResPolicyMap table does not contain any targeting information for applications that are

  deployed as Available to User collections. Software Center queries a list of these
  applications from the Management Point, and policy targeting information for these
  applications is generated dynamically when a user requests an application from Software
  Center.

Next Steps
      Application Deployment to Device Collections
      Application Deployment to User Collections

 Last updated on 03/27/2026

<!-- p.31 -->

Application Deployment for Device
Collections
Applies to: Configuration Manager (current branch)

When an application is deployed to a Device collection, the policy is targeted to all the devices
in the collection regardless of the deployment purpose. This article explains the policy
download and deployment processing on the client.

   Tip

  All the information necessary to review the client logs can be obtained by running the SQL
  query referenced in the Before you begin section.

Policy Download
After the policy for the application deployment is targeted to the client, the client would
download the policy at the next policy polling cycle. When the client downloads the policy, it
downloads related policies in addition to the deployment policy. These related policies include
the policy for the application, deployment type, global conditions, etc. Policy download activity
can be tracked in the PolicyAgent.log file on the client, by using either the Application or
Assignment Unique ID.

 Output

 Download of policy CCM_Policy_Policy5.PolicyID="{<b>3AC57DFE-3F87-4C59-930B-
 B9F57CB41B91</b>}",PolicySource="SMS:PS1",PolicyVersion="1.00" completed (DTS Job
 ID: {AE88E639-0E59-40D7-AAA9-4403AAE6EE82})
 Policy state for [CCM_Policy_Policy5.PolicyID="{<b>3AC57DFE-3F87-4C59-930B-
 B9F57CB41B91</b>}",PolicySource="SMS:PS1",PolicyVersion="1.00"] is currently
 [Active]

After the policies are downloaded on the client, the Scheduler component creates schedules
for deployment activation and enforcement.

Deployment Activation
Application evaluation is initiated when the deployment is activated. Scheduler component
creates a schedule to activate the assignment at the Available Time configured in the
deployment. This activity can be tracked in Scheduler.log on the client by using the Application
Assignment Unique ID.

<!-- p.32 -->

     For Required deployments, the activation schedule is created, but has a delay of up to
     two hours to avoid resource contention on Site Servers and Distribution Points. The delay
     helps avoid contention since application content may be downloaded during evaluation if
     the application is applicable based on defined Requirement Rules.

       Output

       SMSTrigger '15AF8C4000080000' for scheduler 'Machine/{5F2FA409-C9B2-4100-8BC8-
       051820311DE1}' will fire at 08/15/2019 01:44:00 PM with randomization.

     For Available deployments, the activation schedule is created to be fired off at the
     Available Time configured in the Deployment.

       Output

       SMSTrigger '1E4F8C4000080001' for scheduler 'Machine/{3AC57DFE-3F87-4C59-930B-
       B9F57CB41B91}' will fire at 08/15/2019 01:13:33 PM without randomization.

When the schedule time arrives, Scheduler component sends the activation message to DCM
Agent to perform application evaluation.

 Output

 Sending message for schedule 'Machine/{3AC57DFE-3F87-4C59-930B-B9F57CB41B91}'
 (Target: 'direct:DCMAgent', Name: '')

DCM Agent receives the activation message, and creates a job to evaluate the application.

 Output

 CDCMAgent::HandleMessage - Message received for machine: '<?xml version='1.0' ?>
 <CIAssignmentMessage MessageType='Activation'><AssignmentID>{3AC57DFE-3F87-4C59-
 930B-B9F57CB41B91}</AssignmentID></CIAssignmentMessage>'

Deployment Enforcement
Application installation is initiated when the deployment is enforced.

     For Required deployments, Scheduler creates a deadline schedule after policy is
     downloaded to enforce the application at deployment deadline. The deadline schedule
     isn't randomized by default. Randomization behavior for activation can be controlled by
     the Disable deadline randomization client setting.

<!-- p.33 -->

       Output

       SMSTrigger '15EF8C4000080000' for scheduler 'Machine/DEADLINE:{5F2FA409-C9B2-
       4100-8BC8-051820311DE1}' will fire at 08/15/2019 03:05:00 PM without
       randomization.

     At the deadline, Scheduler component sends the deadline message to DCM Agent.

       Output

       Sending message for schedule 'Machine/DEADLINE:{5F2FA409-C9B2-4100-8BC8-
       051820311DE1}' (Target: 'direct:DCMAgent', Name: '')

     DCM Agent receives the deadline message, and creates a job to enforce the application.

       Output

       CDCMAgent::HandleMessage - Message received for machine: '<?xml version='1.0'
       ?><CIAssignmentMessage MessageType='EnforcementDeadline'><AssignmentID>
       {5F2FA409-C9B2-4100-8BC8-051820311DE1}</AssignmentID></CIAssignmentMessage>'

        ７ Note

        For deployments with deadline in the past, the application is activated and enforced
        immediately by the same DCM Agent job which performs the evaluation, download
        and installation actions.

     For Available deployments, there's no deadline schedule since the enforcement occurs
     when the application installation is initiated by the user from Software Center. When the
     user starts an installation, a DCM Agent job is created to perform application evaluation,
     download, and installation. This activity can be tracked in DCMAgent.log on the client.

Next Steps
     Understanding application deployment client components

Last updated on 03/27/2026

<!-- p.34 -->

Application Deployment Policy for Users
Applies to: Configuration Manager (current branch)

When an application is deployed to a User collection, the policy for the deployment is created
for Required deployments only. For Available deployments, the policy is created when the user
attempts to install the application from the Software Center. This article will explain the
deployment process for Required as well as Available deployments.

   Tip

  All the information necessary to review the client logs can be obtained by running the SQL
  query referenced in the Before you begin section.

Required Deployments
The policy for a required application deployment to a User collection is targeted to all the users
in the collection when the deployment is created. Client-side processing for these deployments
is similar to a required deployment to a Device collection. Deployment activation occurs at the
defined Available Time, and enforcement occurs at the defined Deadline time. For more
information, see Application Deployment to Device Collections.

Available Deployments
Applications that are deployed to a user collection as Available behave differently. This
behavior change allows the Administrator to make applications available to the users without
causing resource contention for policy. When a user launches the Software Center, a list of
applications that are available for the user is queried from the Management Point in real time.
This request is made to the CMUserService_WindowsAuth virtual directory on the Management
Point and can be seen in the SCClient_[UserName].log file on the client.

 Output

 Using endpoint Url: https://MP.CONTOSO.COM:443/CMUserService_WindowsAuth, Windows
 authentication

When the Management Point receives this request, it queries the list of applications available
to the user by executing usp_GetApplicationPropertyValuesFiltered stored procedure. This
activity can be tracked in the UserService.log file on the Management Point.

<!-- p.35 -->

  Output

  GetFilteredApplications, startItem = 0, max rows = 60, search text = '', filter =
  '', user = CONTOSO\UserName, api = 4.0, source =
  UserService_WinAuth_SoftwareCenter, platform = <OSPlatform>
  GetFilteredApplications: returned 1 rows out of 1 total

Software Center receives the list and displays the applications that the user can install. When
the user clicks on the application, additional information about the application is queried from
the Management Point, which involves execution of stored procedures such as
usp_GetApplicationInfo , usp_GetAppModelApplicationSupersedence ,

usp_GetDeploymentTypeForAnApp , and so forth.

The deployment is activated when the user selects the application and then selects Install, and
a DCM Agent Job is created to evaluate the application. If the application is applicable, another
DCM Agent Job is created to download and enforce the application. This activity can be
tracked in the DCMAgent.log file on the client.

Next Steps
      Understanding application deployment client components

 Last updated on 03/27/2026

<!-- p.36 -->

Understanding Application Deployment
Client Components
Applies to: Configuration Manager (current branch)

Application deployment evaluation and enforcement operations are handled by the DCM
Agent and CI Agent components on the client. This article explains how a typical DCM and CI
Agent job operates.

DCM Agent
DCM Agent is the high-level client component responsible for evaluation of configuration
items, which includes applications. When a deployment is activated or enforced, a DCM Agent
job is created which reads the assignment policy and determines the actions that need to be
performed. This activity can be tracked in the DCMAgent.log file on the client by using the
DCM Agent Job ID, which can be identified by looking for the Application Unique ID.

Device Deployments
     For Required deployments, DCMAgent.log would show the applicable actions. These
     actions may differ depending on whether the deployment deadline has already passed.

       Output

       # Evaluation Job example:
       DCMAgentJob({A9E850E2-91B0-4122-94FD-D14EDF925AF7}):
       CDCMAgentJob::PopulateCIsFromAssignment - CI policy Id:ScopeId_B63CEBE7-8A69-
       4FBE-994F-5AD0A8488D27/RequiredApplication_fc76ef0a-3ab0-4110-8cce-
       1addc36d0225 version:3 with actions: Evaluation, Content Download

       # Enforcement Job example:
       DCMAgentJob({4C8A9F6E-390B-450E-B505-B5698DB68EDD}):
       CDCMAgentJob::PopulateCIsFromAssignment - CI policy Id:ScopeId_B63CEBE7-8A69-
       4FBE-994F-5AD0A8488D27/RequiredApplication_fc76ef0a-3ab0-4110-8cce-
       1addc36d0225 version:3 with actions: Evaluation, Install, Uninstall, Update,
       Look-ahead Install, Look-ahead Uninstall, Look-ahead Update

     For Available deployments, DCMAgent.log shows that the deployment is not mandatory .
     For these deployments, application evaluation is done but enforcement is skipped unless
     the user initiated the installation.

       Output

<!-- p.37 -->

    # Evaluation Job example:
    DCMAgentJob({E353BF94-D7ED-4ADD-AF0F-9273F6A67FC1}):
    CDCMAgentJob::PopulateCIsFromAssignment - [SCAN] CI policy Id
    :ScopeId_B63CEBE7-8A69-4FBE-994F-5AD0A8488D27/RequiredApplication_fc76ef0a-
    3ab0-4110-8cce-1addc36d0225 version:3 - Assignment:{3AC57DFE-3F87-4C59-930B-
    B9F57CB41B91} is not mandatory.

    # Enforcement Job (user initiated) example:
    Request to enforce application ConfigMgr Toolkit(ScopeId_B63CEBE7-8A69-4FBE-
    994F-5AD0A8488D27/Application_fc76ef0a-3ab0-4110-8cce-1addc36d0225.3)
    immediately for target: machine with action(s): Evaluation, Install, Update
    CDCMAgentJobMgr::CreateInteractiveJob - Queuing new job: {D331249E-F7DE-481B-
    A497-8E8B5E7B91C3}

User Deployments
   For Required deployments, DCMAgent.log would show the applicable actions. These
   actions may differ depending on whether the deployment deadline has already passed.

    Output

    # Evaluation Job example:
    DCMAgentJob({65D9688D-1781-4DA3-B07A-193D481251C6}):
    CDCMAgentJob::PopulateCIsFromAssignment - CI policy Id:ScopeId_C8F7EAE6-DBA8-
    4970-B3FF-47ED706868DE/RequiredApplication_6b39398b-fd20-47ca-bd68-
    074274509f98 version:2 with actions: Evaluation, Content Download

    # Enforcement Job example:
    DCMAgentJob({2B0DA272-FC65-4F31-9557-C4D840D650F1}):
    CDCMAgentJob::PopulateCIsFromAssignment - CI policy Id:ScopeId_C8F7EAE6-DBA8-
    4970-B3FF-47ED706868DE/RequiredApplication_6b39398b-fd20-47ca-bd68-
    074274509f98 version:2 with actions: Evaluation, Install, Uninstall, Update,
    Look-ahead Install, Look-ahead Uninstall, Look-ahead Update

   For Available deployments, DCM Agent jobs are created for evaluation and enforcement
   when the application installation is initiated by the user.

    Output

    # Evaluation Job example:
    DCMAgentJob({FBB44C84-DB06-41F7-8DC1-D9BA368F0C20}):
    CDCMAgentJob::PopulateCIsFromAssignment - [SCAN] CI policy Id
    :ScopeId_C8F7EAE6-DBA8-4970-B3FF-47ED706868DE/RequiredApplication_6b39398b-
    fd20-47ca-bd68-074274509f98 version:2 - Assignment:{7EA17128-EB4F-448A-88A7-
    B865E7DA228C} is not mandatory.

    # Enforcement Job example:
    CAppMgmtSDK::EnforceAppPolicy ScopeId_C8F7EAE6-DBA8-4970-B3FF-
    47ED706868DE/RequiredApplication_6b39398b-fd20-47ca-bd68-074274509f98.

<!-- p.38 -->

       CDCMAgentJobMgr::CreateInteractiveJob - Queuing new job: {7936D7F3-24B0-401D-
       BADD-59EB5B49C2C2}

CI Agent
CI Agent is the client component responsible for evaluation and remediation of configuration
items. DCM Agent reads the assignment policy and creates a job for the CI Agent component
to perform the requested actions. DCMAgent.log records the CI Agent Job ID, which is useful
for tracking the CI Agent activity in the CIAgent.log file on the client.

 Output

 DCMAgentJob({E353BF94-D7ED-4ADD-AF0F-9273F6A67FC1}): CDCMAgent::InitiateCIAgentJob
 - Starting CI Agent Job {57AF6FA1-3482-4469-9881-A63F41D18406} for target: machine.
 Refer to this CI agent job ID in ciagent.log for more details

A typical CI Agent job goes through multiple phases, which can be identified by filtering
CIAgent.log on the CI Agent Job ID and then looking for TransitionState . Some of the key
phases for an application deployment CI Agent job are:

     DownloadingCIs
        During this phase, application metadata required to evaluate the application is
        downloaded. The metadata includes detection method, requirement rules, global
        conditions, etc. This activity can be tracked in CIDownloader.log and
        DataTransferService.log. For Available deployments, this process occurs during the first
        evaluation of the application. For Required deployments however, this process occurs
        immediately after the policy is downloaded.

     InvokingSdmMethod
        During this phase, the application detection method is used to check if the application
        is installed and the desired state is determined. This activity can be tracked in
        AppDiscovery.log and AppIntentEval.log. For more information about this phase, see
        Application Evaluation.

     StateDownloadingContents
        During this phase, application content is downloaded if necessary. This activity can be
        tracked in CAS.log, ContentTransferManager.log, LocationServices.log, and
        DataTransferService.log. For more information about this phase, see Application
        Download.

     StateEnforcingCIs
        During this phase, the application installation is initiated. This activity can be tracked in
        AppEnforce.log. For more information about this phase, see Application Installation.

<!-- p.39 -->

      StateEnforcementReporting
         During this phase, application installation state is recorded for reporting to the
         Management Point. This activity can be tracked in StateMessage.log.

Although the CI Agent job goes through all the phases, it skips the phase if it isn't required. As
an example, for Available deployments StateDownloadingContents and StateEnforcingCIs
phases are skipped until the user attempts to install the application from Software Center.
However, for Required deployments, the StateDownloadingContents phase downloads
application content (if necessary) when the assignment is activated, but the StateEnforcingCIs
phase is skipped if the deadline is in the future. This behavior can be observed in the
CIAgent.log by filtering on the CI Agent Job ID and looking for Skipping policy .

  Output

  {57AF6FA1-3482-4469-9881-A63F41D18406} - Skipping policy CI <CI Unique ID> and all
  dependents for ContentDownload task since CI action was not requested.
  {57AF6FA1-3482-4469-9881-A63F41D18406} - Skipping policy CI <CI Unique ID> and all
  dependents for Enforce task since CI action was not requested.

Next Steps
      Application Evaluation
      Application Download
      Application Installation

 Last updated on 03/27/2026

<!-- p.40 -->

Application Deployment Evaluation
Applies to: Configuration Manager (current branch)

Before you continue, please review Application deployment client components to understand
DCM and CI Agent job processing.

Application evaluation is performed by the DCM Agent and CI Agent components when the
deployment is activated. To understand when the assignment is activated, see the Application
Deployment to Device Collections or Application Deployment to User Collections articles.

Application Detection and Evaluation
Application evaluation is performed during the InvokingSdmMethod phase of a CI Agent job.
This phase is where the client evaluates the detection method defined for the application to
determine if the application is installed on the device. This activity can be tracked in
AppDiscovery.log using the Deployment Type Unique ID or Deployment Type Name.

 Output

 Performing detection of app deployment type ConfigMgr Toolkit - Windows Installer
 (*.msi file)(ScopeId_B63CEBE7-8A69-4FBE-994F-5AD0A8488D27/DeploymentType_1d49ef88-
 cf3b-42fa-b198-388d220ccb44, revision 2) for system.
 +++ Did not detect app deployment type ConfigMgr Toolkit - Windows Installer (*.msi
 file)(ScopeId_B63CEBE7-8A69-4FBE-994F-5AD0A8488D27/DeploymentType_1d49ef88-cf3b-
 42fa-b198-388d220ccb44, revision 2) for system.

  ７ Note

  Above example shows detection for an MSI application where the detection is done by
  checking if the MSI Product Code is installed on the device. For applications using
  alternate detection methods, the appropriate detection method is used to check if the
  application is installed.

Next, the client evaluates the desired state of the application based on the Deployment
Purpose. This step also involves detecting whether the application has any dependencies or
supersedence rules that should be honored for the application. This activity can be tracked in
AppIntentEval.log by using the Application and Deployment Type Unique ID.

 Output

 # Available Application Deployment
