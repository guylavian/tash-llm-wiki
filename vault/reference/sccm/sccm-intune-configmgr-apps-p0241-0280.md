---
title: "App management documentation — pages 241-280"
type: reference
domain: sccm
slug: sccm-intune-configmgr-apps-p0241-0280
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-apps-p0241-0280
family: sccm
documentKind: "doc"
abstract: "Implement Just Enough Administration on high-value systems to eliminate or reduce unconstrained administrative access to those systems. Deploy Windows Defender Application Control policies to allow pre-approved administrative tasks to use the full capability of the PowerShell la"
---

# App management documentation — pages 241-280

<!-- p.241 -->

     Implement Just Enough Administration on high-value systems to eliminate or
     reduce unconstrained administrative access to those systems.
     Deploy Windows Defender Application Control policies to allow pre-approved
     administrative tasks to use the full capability of the PowerShell language, while
     limiting interactive and unapproved use to a limited subset of the PowerShell
     language.
     Deploy Windows 10 or later to give your antivirus provider full access to all content
     (including content generated or de-obfuscated at runtime) processed by Windows
     Scripting Hosts including PowerShell.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.242 -->

Package Conversion Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Package Conversion Manager helps you convert Configuration Manager legacy
packages into applications. Applications have additional benefits such as dependencies,
requirement rules, detection methods, and user device affinity.

A Configuration Manager application contains files and programs that you deploy to
client devices. However, unlike legacy packages and programs, an application provides
additional user-centric functionality. For example, an application might contain
deployment types for a local installation of a software package, a virtual application
package, or a version of the application for mobile devices.

For more information, see the following articles:

      Introduction to application management
      Packages and programs

  ） Important

  If you previously installed an older version of Package Conversion Manager, first
  uninstall it before upgrading your site. This integrated version doesn't require
  installation, but may conflict with existing versions.

This integrated version of Package Conversion Manager works on packages in the
Configuration Manager current branch site. It's not a standalone tool. If you have
packages and programs in an older version of Configuration Manager, first migrate the
packages into your current branch site. For more information, see Migrate data between
hierarchies.

Planning
Before you start converting packages into applications, first develop a plan. The
following process is an example plan:

      Define a detailed package conversion plan

      Select and prepare packages for conversion

      Select test packages

<!-- p.243 -->

     Analyze, investigate, and convert packages

     Test and deploy the applications

Define a detailed package conversion plan
This section describes two sample package conversion plans:

     A high-resource test environment: You have a test environment with the resources,
     permissions, and architecture to fully replicate your production environment.

     A limited-resource test environment: You don't have a test environment that fully
     replicates your production environment.

Adjust these plans as necessary for other issues specific to your environment.

Sample plan for a high-resource test environment
Your test environment has the resources, permissions, and architecture similar to your
production environment. Use the test environment to efficiently analyze and convert all
of your packages, and then test all of your Configuration Manager applications. After
completing that work, transfer it to the production environment.

Your package conversion plan may be similar to the following steps:

   1. Select the packages you want to convert.

   2. Migrate the packages for conversion into your test environment.

   3. Prepare the packages for conversion.

   4. Select test packages.

   5. Analyze, investigate, and convert the test packages.

   6. Test the converted applications.

   7. Analyze and convert the remaining (non-test) packages.

   8. Export the applications from the test environment. Import them into your
     production environment.

Sample plan for a limited-resource test environment

<!-- p.244 -->

Your test environment doesn't have the resources, permissions, and architecture similar
to your production environment. You can't analyze, test, and convert all of your
packages. In this scenario, only analyze, investigate, convert, and test your test packages.
Then migrate the remaining packages to the production environment to analyze and
convert.

Your package conversion plan may be similar to the following steps:

   1. Select the packages you want to convert.

   2. Select test packages.

   3. Migrate the test packages into your test environment.

   4. Prepare the test packages for conversion.

   5. Analyze, investigate, and convert the test packages.

   6. Test the converted applications.

   7. Export the test applications from the test environment. Then import them into your
     production environment.

   8. Migrate the remaining packages into the production environment and prepare
     them for conversion.

   9. Analyze, investigate, and convert the remaining packages in the production
     environment.

 10. Release the remaining applications to the production environment.

Select and prepare packages for conversion

Select the packages that you want to convert

Not all packages are suitable to be converted into applications. Before you begin to
convert packages, identify the packages that won't be converted.

The best types of package for conversion to applications are those that contain user-
facing software, for example:

     Windows Installer files (.msi and .msu)

     Microsoft Application Virtualization (App-V) programs

     Windows executable files (.exe)

<!-- p.245 -->

The types of package that are best kept as packages and not converted to applications
include:

     System maintenance tools. For example, scripts or backup utilities.

     Packages for software that are out of support.

   Tip

  After identifying packages that aren't appropriate for conversion into applications,
  move them to a separate folder in the Configuration Manager console. To create a
  package folder in the Configuration Manager console:

           Right-click the Packages node.
           Select Folders, and then select Create Folder.
           Enter the folder name, for example Not Converted .
           Click OK.

Prepare the packages for conversion
For each package you want to convert, ensure that they conform to the following
conditions:

     The source files location is a full UNC path, for example \\Server\Share\File .

     Windows Installer files use only one unique product code.

Select test packages
If possible, your group of test packages should include packages that meet the
following criteria:

     At least one test package with a readiness state of Automatic.

     At least one test package with a readiness state of Manual.

Ideally, your test packages should be core packages, for example:

     Packages that you know well.

     Packages that are the most important to your organization.

     Packages that you can most easily test.

<!-- p.246 -->

Identify the packages that are appropriate for testing. Then move them to a separate
folder in the Configuration Manager console.

Analyze, investigate, and convert packages

Analyze packages

To analyze an individual package or a small group, use Package Conversion Manager
integrated in the Configuration Manager console. For more information, see How to
analyze and convert packages.

  ７ Note

  See the Package Conversion Status node in the Monitoring workspace. It displays
  summary information about the analysis and conversion processes.

Investigate analysis results

After analyzing the test packages, investigate the packages with a readiness state of
Manual or Error. Determine the reasons why they have that state. Some common
reasons for a readiness state of Manual or Error include:

     The package doesn't contain the information required to create a detection
     method in an application deployment type.

     The package doesn't contain the information required to convert collections to
     global conditions and requirements.

     The package contains more than one program.

     The package is dependent on another package that you haven't converted to an
     application.

For more information, use the following resources:

     Review the error messages and fixes in Technical reference for Package Conversion
     Manager error messages

     Review the log file PCMTrace.log

     Troubleshoot Package Conversion Manager

<!-- p.247 -->

Convert the packages
For more information about how to convert packages, see How to analyze and convert
packages.

  ７ Note

  See the Package Conversion Status node in the Monitoring workspace. It displays
  summary information about the analysis and conversion processes.

Test and deploy the applications
Test the applications, either in your test environment or your production environment,
according to your detailed package conversion plan.

Recommendations
     Use the Package Conversion Status node in the Monitoring workspace. It displays
     summary information about the analysis and conversion processes.

     Investigate the programs in your packages known as wrappers. Use the
     Package Conversion Manager plug-in to convert their functions into the equivalent
     Configuration Manager functionality.

     Ensure that you thoroughly test each converted application before you deploy it in
     a production environment.

Next steps
How to analyze and convert packages

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.248 -->

How to analyze and convert packages
with Package Conversion Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

Before you can convert a package, first analyze it. Depending on the results of the
analysis, you can then do one of the following tasks:

      Convert the package to an application. On the Package list in the console, the
      readiness state displays Automatic.

      Fix and Convert the package, attach collections, and create global conditions. On
      the Package list in the console, the readiness state displays Automatic.

      Fix and Convert the package. On the Package list in the console, the readiness
      state displays Manual.

      Leave the package unconverted. On the Package list in the console, the readiness
      state displays Not Applicable.

How to analyze packages
   1. In the Configuration Manager console, go to the Software Library workspace.
      Expand Application Management, and select the Packages node.

   2. Select the package to convert. On the Home tab of the ribbon, in the Package
      Conversion group, select Analyze Package. Package Conversion Manager analyzes
      the package.

   3. To see the readiness state of the package, add the Readiness column to the list of
      packages. The readiness state of the package determines your next action:

            Automatic: How to convert packages

            To also attach collections and create global conditions with an Automatic
            readiness state, see How to fix and convert packages.

            Manual: How to fix and convert packages

            Not Applicable: This package is missing required content or a program. Add
            any missing content or programs and retry analysis. Or leave it in an
            unconverted state and continue to deploy it as a package.

<!-- p.249 -->

         Unknown: First run the Analyze task, or wait for the next scheduled analysis.
         If the state doesn't change, then see Troubleshoot Package Conversion
         Manager.

  Tip

 Optionally, you can use the following PowerShell cmdlet to analyze a package:
 Invoke-CMAnalyzePackage.

How to convert packages
 1. In the Configuration Manager console, go to the Software Library workspace.
   Expand Application Management, and select the Packages node.

 2. Select the package to convert with a readiness state of Automatic. On the Home
   tab of the ribbon, in the Package Conversion group, select Convert Package. The
   Convert Package to Application wizard opens.

 3. In the Convert Package to Application wizard, review the list of selected packages.
   Remove any packages that you don't want to convert, and select OK. Package
   Conversion Manager converts the package. The Conversion Complete window lists
   the Conversion Status of the new applications.

      ７ Note

      When you convert a package, the site records the date and time of the
      conversion as the UTC time.

 4. Follow the instructions in the window. Select either View applications or Close.

  Tip

 Optionally, you can use the following PowerShell cmdlet to convert a package:
 Invoke-CMConvertPackage.

How to fix and convert packages
 1. In the Configuration Manager console, go to the Software Library workspace.
   Expand Application Management, and select the Packages node.

<!-- p.250 -->

2. Select a package with a readiness state of Manual or Automatic. On the Home tab
  of the ribbon, in the Package Conversion group, select Fix and Convert.

3. In the Package Conversion Wizard, review the information on the Package
  Selection page, noting the Items to Fix. Then select Next.

4. On the Dependency Review page, review if the package is dependent on other
  listed packages, and then select Next.

    ７ Note

    If you haven't converted any of the listed dependent packages, first convert
    those packages. Then restart the package conversion process.

    If a dependency isn't required, delete it, or ignore it and continue the
    conversion process.

5. On the Deployment Type page, review the deployment types for the new
  application. Change their priorities, or delete the deployment types.

6. If any of the new deployment types don't have an associated detection method,
  the Detection Method column displays a warning icon. Complete the following
  actions:

   a. Select Edit Detection Method.

  b. Select Add.

   c. In the Detection Rule dialog box, specify a Setting Type.

  d. For the specified setting type, enter the additional information required for the
     detection rule.

   e. Select OK. If necessary, repeat this process to add multiple detection methods
     to each deployment type.

   f. Select OK. Verify the Detection Method column displays an icon to confirm a
     correctly specified detection method.

7. Select Next.

8. On the Requirements Selection page, review the deployment types of the new
  application. Select a deployment type, and review the requirements for that
  deployment type.

<!-- p.251 -->

        ７ Note

        The wizard only displays the requirements that Package Conversion Manager
        converts. It doesn't convert all WQL queries in device collections to
        requirements.

   9. Add requirements for a selected deployment type, if necessary.

 10. Select Next.

 11. Complete the wizard to create the application.

        ７ Note

        When you convert a package, the site records the date and time of the
        conversion as the UTC time.

Monitor
Go to the Monitoring workspace of the Configuration Manager console, and select
Package Conversion Status. This dashboard shows the overall analysis and conversion
state of packages in the site. A new background task automatically summarizes the
analysis data.

   Tip

  Package Conversion Manager integrated with Configuration Manager doesn't
  require you to schedule analysis of packages. This action is handled by the
  integrated summarization task. Scheduled package analysis runs every seven days
  by default.

<!-- p.252 -->

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.253 -->

Technical Reference for Application
Deployment in Configuration Manager
Applies to: Configuration Manager (current branch)

In this article, you'll learn how application deployments work.

Before You Begin
When troubleshooting application deployments, there are multiple items that can be useful when
reviewing client logs. These items include:

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

<!-- p.254 -->

 WHERE APP.IsLatest = 1 AND APP.DisplayName = 'Application Name' -- Replace Application
 Name

 ） Important

 When you execute this query, you must use the Application Name listed in the General
 Information tab of Application Properties, instead of using the Localized application name
 listed in the Software Center tab of Application properties.

Next Steps
     Application Deployment Policy

Last updated on 03/27/2026

<!-- p.255 -->

Application Deployment Policy
Applies to: Configuration Manager (current branch)

Policy Creation
When you deploy an application, an instance of SMS_ApplicationAssignment class is created
which represents the assignment of an application to a collection. This activity can be tracked in
the SMSProv.log file.

 Output

 SMS Provider    PutInstanceAsync SMS_ApplicationAssignment~
 SMS Provider    Auditing: User CONTOSO\Admin created an instance of class
 SMS_ApplicationAssignment.~

In the Configuration Manager database, this information is stored in the CI_CIAssignments table
where AssignmentType 2 represents an application deployment. When the assignment is created,
SMS Database Monitor component detects a change in the table then notifies Object Replication
Manager to process the CI Assignment (CIA) policy. Object Replication Manager component then
creates the policy for the application assignment in the database, which is stored in the Policy
table in the database, and the Policy ID is based on the Application Unique ID. This activity can be
tracked in the objreplmgr.log file by referencing the Assignment Unique ID, which can be
obtained from the SQL query referenced in the Before You Begin section.

 Output

 ***** Processing Application Assignment {3AC57DFE-3F87-4C59-930B-B9F57CB41B91} *****

The policy for the application assignment can be seen in the database using a SQL query similar
to the following example.

 SQL

 SELECT P.PolicyID, PA.PolicyAssignmentID, PA.PADBID, PA.IsTombstoned,
 PA.LastUpdateTime FROM Policy P
 JOIN PolicyAssignment PA ON P.PolicyID = PA.PolicyID
 WHERE P.PolicyID = '{3AC57DFE-3F87-4C59-930B-B9F57CB41B91}' -- Replace Assignment
 Unique ID

<!-- p.256 -->

Policy Targeting
After the policy is generated, the Policy Provider component assigns this policy to the resources
in the collection that's targeted by the application deployment. The policy targeting information
is stored in the ResPolicyMap table in the database. You can use the PADBID returned by the
above query to track this activity in policypv.log. However, the PADBID recorded in the log may
not always match the PADBID returned by the above query if multiple policies are getting
processed simultaneously.

  Output

  ~Policy or Policy Target Change Event triggered.
  ~Completed batch with beginning PADBID = 16778403 ending PADBID = 16778403.

  ７ Note

   ResPolicyMap table does not contain any targeting information for applications that are

  deployed as Available to User collections. Software Center queries a list of these applications
  from the Management Point, and policy targeting information for these applications is
  generated dynamically when a user requests an application from Software Center.

Next Steps
      Application Deployment to Device Collections
      Application Deployment to User Collections

 Last updated on 03/27/2026

<!-- p.257 -->

Application Deployment for
Device Collections
Applies to: Configuration Manager (current branch)

When an application is deployed to a Device collection, the policy is targeted to all the devices in
the collection regardless of the deployment purpose. This article explains the policy download
and deployment processing on the client.

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
 B9F57CB41B91</b>}",PolicySource="SMS:PS1",PolicyVersion="1.00" completed (DTS Job ID:
 {AE88E639-0E59-40D7-AAA9-4403AAE6EE82})
 Policy state for [CCM_Policy_Policy5.PolicyID="{<b>3AC57DFE-3F87-4C59-930B-
 B9F57CB41B91</b>}",PolicySource="SMS:PS1",PolicyVersion="1.00"] is currently [Active]

After the policies are downloaded on the client, the Scheduler component creates schedules for
deployment activation and enforcement.

Deployment Activation
Application evaluation is initiated when the deployment is activated. Scheduler component
creates a schedule to activate the assignment at the Available Time configured in the

<!-- p.258 -->

deployment. This activity can be tracked in Scheduler.log on the client by using the Application
Assignment Unique ID.

     For Required deployments, the activation schedule is created, but has a delay of up to two
     hours to avoid resource contention on Site Servers and Distribution Points. The delay helps
     avoid contention since application content may be downloaded during evaluation if the
     application is applicable based on defined Requirement Rules.

       Output

       SMSTrigger '15AF8C4000080000' for scheduler 'Machine/{5F2FA409-C9B2-4100-8BC8-
       051820311DE1}' will fire at 08/15/2019 01:44:00 PM with randomization.

     For Available deployments, the activation schedule is created to be fired off at the Available
     Time configured in the Deployment.

       Output

       SMSTrigger '1E4F8C4000080001' for scheduler 'Machine/{3AC57DFE-3F87-4C59-930B-
       B9F57CB41B91}' will fire at 08/15/2019 01:13:33 PM without randomization.

When the schedule time arrives, Scheduler component sends the activation message to DCM
Agent to perform application evaluation.

 Output

 Sending message for schedule 'Machine/{3AC57DFE-3F87-4C59-930B-B9F57CB41B91}' (Target:
 'direct:DCMAgent', Name: '')

DCM Agent receives the activation message, and creates a job to evaluate the application.

 Output

 CDCMAgent::HandleMessage - Message received for machine: '<?xml version='1.0' ?>
 <CIAssignmentMessage MessageType='Activation'><AssignmentID>{3AC57DFE-3F87-4C59-930B-
 B9F57CB41B91}</AssignmentID></CIAssignmentMessage>'

Deployment Enforcement
Application installation is initiated when the deployment is enforced.

     For Required deployments, Scheduler creates a deadline schedule after policy is
     downloaded to enforce the application at deployment deadline. The deadline schedule isn't

<!-- p.259 -->

     randomized by default. Randomization behavior for activation can be controlled by the
     Disable deadline randomization client setting.

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

       CDCMAgent::HandleMessage - Message received for machine: '<?xml version='1.0' ?>
       <CIAssignmentMessage MessageType='EnforcementDeadline'><AssignmentID>{5F2FA409-
       C9B2-4100-8BC8-051820311DE1}</AssignmentID></CIAssignmentMessage>'

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

<!-- p.260 -->

Application Deployment Policy for Users
Applies to: Configuration Manager (current branch)

When an application is deployed to a User collection, the policy for the deployment is created for
Required deployments only. For Available deployments, the policy is created when the user
attempts to install the application from the Software Center. This article will explain the
deployment process for Required as well as Available deployments.

   Tip

  All the information necessary to review the client logs can be obtained by running the SQL
  query referenced in the Before you begin section.

Required Deployments
The policy for a required application deployment to a User collection is targeted to all the users
in the collection when the deployment is created. Client-side processing for these deployments is
similar to a required deployment to a Device collection. Deployment activation occurs at the
defined Available Time, and enforcement occurs at the defined Deadline time. For more
information, see Application Deployment to Device Collections.

Available Deployments
Applications that are deployed to a user collection as Available behave differently. This behavior
change allows the Administrator to make applications available to the users without causing
resource contention for policy. When a user launches the Software Center, a list of applications
that are available for the user is queried from the Management Point in real time. This request is
made to the CMUserService_WindowsAuth virtual directory on the Management Point and can be
seen in the SCClient_[UserName].log file on the client.

 Output

 Using endpoint Url: https://MP.CONTOSO.COM:443/CMUserService_WindowsAuth, Windows
 authentication

<!-- p.261 -->

When the Management Point receives this request, it queries the list of applications available to
the user by executing usp_GetApplicationPropertyValuesFiltered stored procedure. This activity
can be tracked in the UserService.log file on the Management Point.

  Output

  GetFilteredApplications, startItem = 0, max rows = 60, search text = '', filter = '',
  user = CONTOSO\UserName, api = 4.0, source = UserService_WinAuth_SoftwareCenter,
  platform = <OSPlatform>
  GetFilteredApplications: returned 1 rows out of 1 total

Software Center receives the list and displays the applications that the user can install. When the
user clicks on the application, additional information about the application is queried from the
Management Point, which involves execution of stored procedures such as
usp_GetApplicationInfo , usp_GetAppModelApplicationSupersedence ,

usp_GetDeploymentTypeForAnApp , and so forth.

The deployment is activated when the user selects the application and then selects Install, and a
DCM Agent Job is created to evaluate the application. If the application is applicable, another
DCM Agent Job is created to download and enforce the application. This activity can be tracked
in the DCMAgent.log file on the client.

Next Steps
      Understanding application deployment client components

 Last updated on 03/27/2026

<!-- p.262 -->

Understanding Application Deployment
Client Components
Applies to: Configuration Manager (current branch)

Application deployment evaluation and enforcement operations are handled by the DCM Agent
and CI Agent components on the client. This article explains how a typical DCM and CI Agent job
operates.

DCM Agent
DCM Agent is the high-level client component responsible for evaluation of configuration items,
which includes applications. When a deployment is activated or enforced, a DCM Agent job is
created which reads the assignment policy and determines the actions that need to be
performed. This activity can be tracked in the DCMAgent.log file on the client by using the DCM
Agent Job ID, which can be identified by looking for the Application Unique ID.

Device Deployments
     For Required deployments, DCMAgent.log would show the applicable actions. These
     actions may differ depending on whether the deployment deadline has already passed.

       Output

       # Evaluation Job example:
       DCMAgentJob({A9E850E2-91B0-4122-94FD-D14EDF925AF7}):
       CDCMAgentJob::PopulateCIsFromAssignment - CI policy Id:ScopeId_B63CEBE7-8A69-
       4FBE-994F-5AD0A8488D27/RequiredApplication_fc76ef0a-3ab0-4110-8cce-1addc36d0225
       version:3 with actions: Evaluation, Content Download

       # Enforcement Job example:
       DCMAgentJob({4C8A9F6E-390B-450E-B505-B5698DB68EDD}):
       CDCMAgentJob::PopulateCIsFromAssignment - CI policy Id:ScopeId_B63CEBE7-8A69-
       4FBE-994F-5AD0A8488D27/RequiredApplication_fc76ef0a-3ab0-4110-8cce-1addc36d0225
       version:3 with actions: Evaluation, Install, Uninstall, Update, Look-ahead
       Install, Look-ahead Uninstall, Look-ahead Update

     For Available deployments, DCMAgent.log shows that the deployment is not mandatory .
     For these deployments, application evaluation is done but enforcement is skipped unless
     the user initiated the installation.

<!-- p.263 -->

    Output

    # Evaluation Job example:
    DCMAgentJob({E353BF94-D7ED-4ADD-AF0F-9273F6A67FC1}):
    CDCMAgentJob::PopulateCIsFromAssignment - [SCAN] CI policy Id :ScopeId_B63CEBE7-
    8A69-4FBE-994F-5AD0A8488D27/RequiredApplication_fc76ef0a-3ab0-4110-8cce-
    1addc36d0225 version:3 - Assignment:{3AC57DFE-3F87-4C59-930B-B9F57CB41B91} is not
    mandatory.

    # Enforcement Job (user initiated) example:
    Request to enforce application ConfigMgr Toolkit(ScopeId_B63CEBE7-8A69-4FBE-994F-
    5AD0A8488D27/Application_fc76ef0a-3ab0-4110-8cce-1addc36d0225.3) immediately for
    target: machine with action(s): Evaluation, Install, Update
    CDCMAgentJobMgr::CreateInteractiveJob - Queuing new job: {D331249E-F7DE-481B-
    A497-8E8B5E7B91C3}

User Deployments
   For Required deployments, DCMAgent.log would show the applicable actions. These
   actions may differ depending on whether the deployment deadline has already passed.

    Output

    # Evaluation Job example:
    DCMAgentJob({65D9688D-1781-4DA3-B07A-193D481251C6}):
    CDCMAgentJob::PopulateCIsFromAssignment - CI policy Id:ScopeId_C8F7EAE6-DBA8-
    4970-B3FF-47ED706868DE/RequiredApplication_6b39398b-fd20-47ca-bd68-074274509f98
    version:2 with actions: Evaluation, Content Download

    # Enforcement Job example:
    DCMAgentJob({2B0DA272-FC65-4F31-9557-C4D840D650F1}):
    CDCMAgentJob::PopulateCIsFromAssignment - CI policy Id:ScopeId_C8F7EAE6-DBA8-
    4970-B3FF-47ED706868DE/RequiredApplication_6b39398b-fd20-47ca-bd68-074274509f98
    version:2 with actions: Evaluation, Install, Uninstall, Update, Look-ahead
    Install, Look-ahead Uninstall, Look-ahead Update

   For Available deployments, DCM Agent jobs are created for evaluation and enforcement
   when the application installation is initiated by the user.

    Output

    # Evaluation Job example:
    DCMAgentJob({FBB44C84-DB06-41F7-8DC1-D9BA368F0C20}):
    CDCMAgentJob::PopulateCIsFromAssignment - [SCAN] CI policy Id :ScopeId_C8F7EAE6-
    DBA8-4970-B3FF-47ED706868DE/RequiredApplication_6b39398b-fd20-47ca-bd68-
    074274509f98 version:2 - Assignment:{7EA17128-EB4F-448A-88A7-B865E7DA228C} is not
    mandatory.

    # Enforcement Job example:

<!-- p.264 -->

       CAppMgmtSDK::EnforceAppPolicy ScopeId_C8F7EAE6-DBA8-4970-B3FF-
       47ED706868DE/RequiredApplication_6b39398b-fd20-47ca-bd68-074274509f98.
       CDCMAgentJobMgr::CreateInteractiveJob - Queuing new job: {7936D7F3-24B0-401D-
       BADD-59EB5B49C2C2}

CI Agent
CI Agent is the client component responsible for evaluation and remediation of configuration
items. DCM Agent reads the assignment policy and creates a job for the CI Agent component to
perform the requested actions. DCMAgent.log records the CI Agent Job ID, which is useful for
tracking the CI Agent activity in the CIAgent.log file on the client.

 Output

 DCMAgentJob({E353BF94-D7ED-4ADD-AF0F-9273F6A67FC1}): CDCMAgent::InitiateCIAgentJob -
 Starting CI Agent Job {57AF6FA1-3482-4469-9881-A63F41D18406} for target: machine.
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
        During this phase, the application detection method is used to check if the application is
        installed and the desired state is determined. This activity can be tracked in
        AppDiscovery.log and AppIntentEval.log. For more information about this phase, see
        Application Evaluation.

     StateDownloadingContents
        During this phase, application content is downloaded if necessary. This activity can be
        tracked in CAS.log, ContentTransferManager.log, LocationServices.log, and
        DataTransferService.log. For more information about this phase, see Application
        Download.

<!-- p.265 -->

      StateEnforcingCIs
         During this phase, the application installation is initiated. This activity can be tracked in
         AppEnforce.log. For more information about this phase, see Application Installation.

      StateEnforcementReporting
         During this phase, application installation state is recorded for reporting to the
         Management Point. This activity can be tracked in StateMessage.log.

Although the CI Agent job goes through all the phases, it skips the phase if it isn't required. As an
example, for Available deployments StateDownloadingContents and StateEnforcingCIs phases
are skipped until the user attempts to install the application from Software Center. However, for
Required deployments, the StateDownloadingContents phase downloads application content (if
necessary) when the assignment is activated, but the StateEnforcingCIs phase is skipped if the
deadline is in the future. This behavior can be observed in the CIAgent.log by filtering on the CI
Agent Job ID and looking for Skipping policy .

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

<!-- p.266 -->

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
 file)(ScopeId_B63CEBE7-8A69-4FBE-994F-5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-
 b198-388d220ccb44, revision 2) for system.

  ７ Note

  Above example shows detection for an MSI application where the detection is done by
  checking if the MSI Product Code is installed on the device. For applications using alternate
  detection methods, the appropriate detection method is used to check if the application is
  installed.

Next, the client evaluates the desired state of the application based on the Deployment Purpose.
This step also involves detecting whether the application has any dependencies or supersedence
rules that should be honored for the application. This activity can be tracked in AppIntentEval.log
by using the Application and Deployment Type Unique ID.

<!-- p.267 -->

  Output

  # Available Application Deployment

  [Application or DT Unique ID] :- Current State = NotInstalled, Applicability =
  Applicable, ResolvedState = Available, ConfigureState = NotNeeded, Title =
  [Application or DT Name]

  # Required Application Deployment

  [Application or DT Unique ID] :- Current State = NotInstalled, Applicability =
  Applicable, ResolvedState = Installed, ConfigureState = NotNeeded, Title =
  [Application or DT Name]

  # Requirement Rules Not Met

  [Application or DT Unique ID] :- Current State = NotInstalled, Applicability =
  NotApplicable, ResolvedState = None, ConfigureState = NotNeeded, Title = [Application
  or DT Name]

In the log entry above, Current State indicates whether the application is currently installed on
the device. Applicability indicates whether the application is applicable based on defined
requirement rules. ResolvedState indicates the desired state of the application based on the
deployment purpose.

   Tip

  Use the Deployment Monitoring Tool to view the application state, applicability state and
  requirement violations.

Next Steps
      Application Download

 Last updated on 03/27/2026

<!-- p.268 -->

Application download in Configuration
Manager
Applies to: Configuration Manager (current branch)

Before you continue, review Application deployment client components to understand DCM and
CI Agent job processing.

Download initiation
Application content download is started by the CI Agent component on the client during the
StateDownloadingContents phase. This process is the same, regardless of whether the
application is deployed to a Device Collection or a User collection.

     For Available deployments, application content is downloaded when the user starts the
     application installation from Software Center.
     For Required deployments, application content is downloaded when the assignment is
     activated and the application is found Applicable after evaluation. To understand when the
     assignment is activated, see the Application Deployment to Device Collections or
     Application Deployment to User Collections articles.

When CI Agent starts the content download, it creates a task that is handled by the CI Task
Manager component. CI Task Manager then starts the content download. This activity can be
tracked in the CITaskMgr.log file by using the Deployment Type Unique ID.

  Output

  Initiating task ContentDownload for CI ScopeId_B63CEBE7-8A69-4FBE-994F-
  5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44.2 (ConfigMgr Toolkit
  - Windows Installer (*.msi file)) for target: , consumer: {53EA65C2-D596-4215-83E4-
  F7007B78E18C}

Distribution Point Location
All download tasks are handled by Content Access component, which is responsible for
managing the client cache. After the download task is created, Content Access component checks
if the content is already available in the client cache. If the content isn't available, it creates a
location request to get a list of Distribution Points from where the content can be obtained. This

<!-- p.269 -->

activity can be tracked in CAS.log and LocationServices.log on the client using the Content
Unique ID.

 Output

 Requesting locations synchronously for content Content_00a8f9e6-8e44-42f5-a0ef-
 9b5c86a88498.1 with priority Foreground
 ContentLocationRequest : <Request XML Body>
 Reply Message Body : <Reply XML Body>

  ） Important

  Although Location Services component handles the location requests, it doesn't directly
  request locations from the Management Point. All requests to the Management Point
  typically go through CCM Messaging component, which logs to CcmMessaging.log.

Location reply XML contains the list of distribution points based on the client's boundary group.
This list is parsed and persisted in WMI on the client according to the Content Source Priority.
This activity can be seen in ContentTransferManager.log, by using the Content Unique ID and
looking for Persisted location .

If the location reply XML doesn't contain any distribution points, ContentTransferManager.log
would show Received empty location update and the client may get stuck at 0% while
downloading the application. This reply can typically occur because of boundary group
configuration issues. For more information, see Download failures.

Content Download
Once the Distribution Point locations are obtained, Content Access component creates a Content
Transfer job. This activity can be tracked in CAS.log using the Content Unique ID.

 Output

 Submitted CTM job {6D0EA720-EB4E-4893-8395-8B27470A6CFB} to download Content
 Content_00a8f9e6-8e44-42f5-a0ef-9b5c86a88498.1 under context System

Content Transfer Manager then creates a Data Transfer Service job to do the content download.
This activity can be tracked in ContentTransferManager.log on the client using the Content
Unique ID.

 Output

<!-- p.270 -->

 CTM job {6D0EA720-EB4E-4893-8395-8B27470A6CFB} (corresponding DTS job {708C7F21-8898-
 49AB-900E-BA6E5F1A39BC}) started download from '<Distribution Point
 URL>/Content_00a8f9e6-8e44-42f5-a0ef-9b5c86a88498.1' for full content download.

  ７ Note

  This log entry can be used to identify the CTM and DTS job ID's, which can be used to track
  the progress of the Content Transfer in ContentTransferManager.log and
  DataTransferService.log respectively.

Data Transfer Service downloads the application content by creating a Background Intelligent
Transfer Service (BITS) job and waiting for the download to complete. This activity can be tracked
in DataTransferService.log on the client using the DTS Job ID obtained from
ContentTransferManager.log.

 Output

 Starting BITS job '{40263E01-2EDD-462F-ABBA-A5E892CB9229}' for DTS job '{708C7F21-
 8898-49AB-900E-BA6E5F1A39BC}' under user 'S-1-5-18'.
 DTSJob {708C7F21-8898-49AB-900E-BA6E5F1A39BC} in state 'DownloadingData'.
 DTS job {708C7F21-8898-49AB-900E-BA6E5F1A39BC} has completed

After the download is complete, Content Access component is notified. Content Access
component then verifies the downloaded content to ensure that the content wasn't altered
during download. This activity can be tracked in CAS.log by using the Content Unique ID.

 Output

 Hash verification succeeded for content Content_00a8f9e6-8e44-42f5-a0ef-9b5c86a88498.1
 downloaded under context System

Finally, after content is verified, CI Agent receives the task complete notification and the CI Agent
job moves to the next phase.

 Output

 CIAgentJob({2BF84225-C9E8-49A6-A308-A160C4B799D3}):
 CAgentJob::HandleEvent(Event=CITaskComplete, CurrentState=StateDownloadingContents)

Next steps

<!-- p.271 -->

Application Installation

 Last updated on 03/27/2026

<!-- p.272 -->

Application Installation
Applies to: Configuration Manager (current branch)

Before you continue, please review Application deployment client components to understand
DCM and CI Agent job processing.

Application installation is performed by DCM Agent and CI Agent components when the
deployment is enforced. The enforcement time differs for Available and Required deployments.
To understand when the assignment is enforced, see the Application Deployment to Device
Collections or Application Deployment to User Collections articles.

Enforcement Initiation
Application installation is initiated by the CI Agent component on the client during the
StateEnforcingCIs phase. This process is the same, regardless of whether the application is
deployed to a Device Collection or a User collection.

     For Available deployments, the application is installed when the user initiates the
     application installation from Software Center.
     For Required deployments, the application is installed at deployment deadline. However,
     the user can initiate the installation from Software Center before the deadline.

When CI Agent initiates the application installation, it creates a task that is handled by the CI Task
Manager component. CI Task Manager then initiates the installation. This activity can be tracked
in the CITaskMgr.log file by using the Deployment Type Unique ID.

 Output

 Initiating task Enforce for CI ScopeId_B63CEBE7-8A69-4FBE-994F-
 5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44.2 (ConfigMgr Toolkit
 - Windows Installer (*.msi file)) for target: , consumer: {9BC3154A-98F1-4595-A967-
 173D536A3F94}
 Initiated application enforcement. : CITask(ScopeId_B63CEBE7-8A69-4FBE-994F-
 5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44.2..Install.Enforce)

Application Enforcement
After the application enforcement is initiated, the client performs the application detection again
to ensure the application isn't already installed. Once it's determined that the application isn't

<!-- p.273 -->

installed, the application installation is initiated. This activity can be tracked in the AppEnforce.log
file on the client by using the Deployment Type Unique ID.

 Output

 +++ Starting Install enforcement for App DT "ConfigMgr Toolkit - Windows Installer
 (*.msi file)" ApplicationDeliveryType - ScopeId_B63CEBE7-8A69-4FBE-994F-
 5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44, Revision - 2,
 ContentPath - C:\WINDOWS\ccmcache\2, Execution Context - System
     Executing Command line: "C:\WINDOWS\system32\msiexec.exe" /i "ConfigMgrTools.msi"
 /q /qn with user context
     Process 7292 terminated with exitcode: 0
 Status is switching to Success

Installation Verification
After the application is installed, the application detection method is used again to ensure that
the application was detected as installed.

 Output

 Performing detection of app deployment type ConfigMgr Toolkit - Windows Installer
 (*.msi file)(ScopeId_B63CEBE7-8A69-4FBE-994F-5AD0A8488D27/DeploymentType_1d49ef88-
 cf3b-42fa-b198-388d220ccb44, revision 2) for system.
 +++ Discovered MSI application [AppDT Id: ScopeId_B63CEBE7-8A69-4FBE-994F-
 5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44, Revision: 2, MSI
 Product code: {4FFF7ECC-CCF7-4530-B938-E7812BB91186}, MSI Product version: ]
 ++++++ App enforcement completed (3 seconds) for App DT "ConfigMgr Toolkit - Windows
 Installer (*.msi file)" [ScopeId_B63CEBE7-8A69-4FBE-994F-
 5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44], Revision: 2, User
 SID: ] ++++++

Finally, after enforcement is complete, CI Agent receives the task complete notification and the CI
Agent job moves to the next phase.

 Output

 CIAgentJob({2BF84225-C9E8-49A6-A308-A160C4B799D3}):
 CAgentJob::HandleEvent(Event=CITaskComplete, CurrentState=StateEnforcingCIs)

Next Steps
     Troubleshoot application deployments

     Common error codes for app installation

<!-- p.274 -->

Last updated on 03/27/2026

<!-- p.275 -->

Application installation common error
codes reference
Applications can be installed on clients by creating deployments from the Configuration Manager
console or by targeting applications to tenant attached devices from the Microsoft Intune admin
center    . Use the information in this article to assist with troubleshooting application installation
errors.

General troubleshooting tips
Generally, if an application installs successfully on a device with the given command line in the
system context, it will install successfully through Configuration Manager and from the Microsoft
Intune admin center. You can simulate this by using PSExec.

   1. Open an administrative command prompt.
   2. Change directory to where you saved PSExec.
   3. Type in psexec -accepteula -s -i cmd .
   4. This opens a new command prompt window running interactively in the system context.
     Check that you're in the system context by running a whoami command.
   5. Run the install from the new windows with the installation command line. For example,
      msiexec /i "My App.msi" /q would be a quiet install of the "My App" msi file.

You may also find that searching through multiple files for a specific string is useful. For instance,
you might want to search all the client .mof files for a specific class, or you might want to search
logs for a specific ID. Using a specific ID when searching can give you an understanding of how
components are related to each other. Use the select-string cmdlet in those instances.

  PowerShell

  select-string -Path "c:\windows\ccm\*.mof" -Pattern 'CacheInfoEx'
  select-string -Path "c:\windows\ccm\logs\*.log" -Pattern
  'CacheInfoEx.CacheId="ccfe8120-4b9b-4f6e-b8fb-f8c1b1fd74d8'

Configuration Manager errors
                                                                                      ﾉ   Expand table

<!-- p.276 -->

Error code   Error source    Error message

0x87D00202   Configuration   Service is shutting down
             Manager

0x87D00207   Configuration   Parsing error
             Manager

0x87D00213   Configuration   Timeout occurred
             Manager

0x87D00215   Configuration   Item not found
             Manager

0x87D00235   Configuration   Syntax error occurred while parsing
             Manager

0x87D00244   Configuration   The object or subsystem has not been initialized
             Manager

0x87D0027C   Configuration   CI documents download timed out
             Manager

0x87D00289   Configuration   Failed to decompress CI documents
             Manager

0x87D00314   Configuration   CI Version Info timed out
             Manager

0x87D00321   Configuration   The script execution has timed out
             Manager

0x87D00324   Configuration   The application was not detected after installation completed
             Manager

0x87D00325   Configuration   Application was still detected after uninstall completed
             Manager

0x87D00327   Configuration   Script is not signed
             Manager

0x87D00329   Configuration   Application requirement evaluation or detection failed
             Manager

0x87D00607   Configuration   Content not found
             Manager

0x87D00667   Configuration   No current or future service window exists to install software updates
             Manager

0x87D01106   Configuration   Failed to verify the executable file is valid or to construct the associated
             Manager         command line

<!-- p.277 -->

 Error code    Error source       Error message

 0x87D01107    Configuration      Failed to access all the provided program locations. This program may
               Manager            retry if the maximum retry count has not been reached

 0x87D01201    Configuration      The content download cannot be performed because there is not
               Manager            enough available space in cache or the disk is full

 0x87D01202    Configuration      The content download cannot be performed because the total size of
               Manager            the client cache is smaller than the size of the requested content

 0x87D01281    Configuration      A supported App-V client is not installed
               Manager

 0x87D0128F    Configuration      The App-V sftmime command returned failure
               Manager

 0x87D01290    Configuration      An error occurred when querying the App-V WMI provider
               Manager

 0x87D103E8    Configuration      Error Unknown
               Manager

 0x87D1076C    Configuration      Application was successfully installed
               Manager

General Configuration Manager troubleshooting tips
When an application fails to install and the error source is Configuration Manager, typically,
following the application troubleshooting guide and using the general troubleshooting tips helps
you resolve the error. You may also want to use Support Center for Configuration Manager to
help troubleshoot and review information about your clients.

0x87D00202
Message: Service is shutting down

Additional information for error resolution: Verify that the Configuration Manager client is
running on the target device. Verify the client is running by:

     Reviewing the CCMExec.log on the device
     Verifying that the SMS Agent Host service is running on the device

0x87D00207
Message: Parsing error

<!-- p.278 -->

Additional information for error resolution: This error generally occurs in one of the
Configuration Manager components when a piece of data is invalid. This error could stem from
something missing for the application, an old package version, or a number of other general
errors. Follow the application troubleshooting guide to help locate the error and resolve it. It may
be necessary to review additional logs for components that support application installation.
Searching for specific IDs or error codes in the logging may help you identify the problem. For
more information, see general troubleshooting tips.

0x87D00213
Message: Timeout occurred

Additional information for error resolution: Increase the Maximum allowed run time (minutes)
for the application. Ensure that the maintenance window on the client is large enough to support
the runtime. For more information, see the application troubleshooting guide to help resolve the
error.

0x87D00215
Message: Item not found

Additional information for error resolution: Verify that the following exist and are accessible to
the client:

         The application deployment exists and the client sees the policy.
         The application content exists and is available to the client

For more information, see the application troubleshooting guide to help resolve the error.

0x87D00235
Message: Syntax error occurred while parsing

Additional information for error resolution: This error generally occurs in one of the
Configuration Manager components when a piece of data is invalid. This error could stem from
something missing for the application, an old package version, or a number of other general
errors. Follow the application troubleshooting guide to help locate the error and resolve it. It may
be necessary to review additional logs for components that support application installation.
Searching for specific IDs or error codes in the logging may help you identify the problem. For
more information, see general troubleshooting tips.

<!-- p.279 -->

0x87D00244
Message: The object or subsystem has not been initialized

Additional information for error resolution: This error generally occurs in one of the
Configuration Manager components when a piece of data is invalid. This error could stem from
something missing for the application, an old package version, or a number of other general
errors. Follow the application troubleshooting guide to help locate the error and resolve it. It may
be necessary to review additional logs for components that support application installation.
Searching for specific IDs or error codes in the logging may help you identify the problem. For
more information, see general troubleshooting tips.

0x87D0027C
Message: CI documents download timed out

Additional information for error resolution: The CI documents activity can be tracked in
CIAgent.log, CIDownloader.log, and DataTransferService.log. For more information, see the CI
Agent section of the application troubleshooting guide.

0x87D00289
Message: Failed to decompress CI documents

Additional information for error resolution: The CI documents activity can be tracked in
CIAgent.log, CIDownloader.log, and DataTransferService.log. For more information, see the CI
Agent section of the application troubleshooting guide.

0x87D00314
Message: CI Version Info timed out

Additional information for error resolution: Typically this error occurs when a change was made
to the application and the client doesn't have the new information for it. Verify that the client is
getting the policy and it knows about any updated revisions to the application.

0x87D00321
Message: The script execution has timed out

<!-- p.280 -->

Additional information for error resolution: Check the AppEnforce.log for details. You may need
to increase the Maximum allowed run time (minutes) for the application. Ensure that the
maintenance window on the client is large enough to support the run time. For more information,
see the application troubleshooting guide to help resolve the error.

0x87D00324
Message: The application was not detected after installation completed

Additional information for error resolution: Review the AppDiscovery.log and the CIAgent.log.
Once an installation is completed, the application detection is used again to verify the
installation.

0x87D00325
Message: Application was still detected after uninstall completed

Additional information for error resolution: Verify the correct uninstall command was used in
the AppEnforce.log. Review the AppDiscovery.log and the CIAgent.log. Once an uninstall is
completed, the application detection is used again to verify the uninstall.

0x87D00327
Message: Script is not signed

Additional information for error resolution: Verify the PowerShell execution policy client setting
for the device. The default for this client setting is AllSigned so an unsigned script will cause a
failure.

0x87D00329
Message: Application requirement evaluation or detection failed

Additional information for error resolution: Review the AppIntentEval.log to discover
dependencies and supersedence rules for the application and their states. For more information,
see Application deployment evaluation.

0x87D00607
Message: Content not found
