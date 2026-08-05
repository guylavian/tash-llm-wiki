---
title: "Welcome — pages 41-80"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0041-0080
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0041-0080
family: sccm
documentKind: "doc"
abstract: "[Application or DT Unique ID] :- Current State = NotInstalled, Applicability = Applicable, ResolvedState = Available, ConfigureState = NotNeeded, Title = [Application or DT Name] # Required Application Deployment [Application or DT Unique ID] :- Current State = NotInstalled, App"
---

# Welcome — pages 41-80

<!-- p.41 -->

  [Application or DT Unique ID] :- Current State = NotInstalled, Applicability =
  Applicable, ResolvedState = Available, ConfigureState = NotNeeded, Title =
  [Application or DT Name]

  # Required Application Deployment

  [Application or DT Unique ID] :- Current State = NotInstalled, Applicability =
  Applicable, ResolvedState = Installed, ConfigureState = NotNeeded, Title =
  [Application or DT Name]

  # Requirement Rules Not Met

  [Application or DT Unique ID] :- Current State = NotInstalled, Applicability =
  NotApplicable, ResolvedState = None, ConfigureState = NotNeeded, Title =
  [Application or DT Name]

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

<!-- p.42 -->

Application download in Configuration
Manager
Applies to: Configuration Manager (current branch)

Before you continue, review Application deployment client components to understand DCM
and CI Agent job processing.

Download initiation
Application content download is started by the CI Agent component on the client during the
StateDownloadingContents phase. This process is the same, regardless of whether the
application is deployed to a Device Collection or a User collection.

     For Available deployments, application content is downloaded when the user starts the
     application installation from Software Center.
     For Required deployments, application content is downloaded when the assignment is
     activated and the application is found Applicable after evaluation. To understand when
     the assignment is activated, see the Application Deployment to Device Collections or
     Application Deployment to User Collections articles.

When CI Agent starts the content download, it creates a task that is handled by the CI Task
Manager component. CI Task Manager then starts the content download. This activity can be
tracked in the CITaskMgr.log file by using the Deployment Type Unique ID.

  Output

  Initiating task ContentDownload for CI ScopeId_B63CEBE7-8A69-4FBE-994F-
  5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44.2 (ConfigMgr
  Toolkit - Windows Installer (*.msi file)) for target: , consumer: {53EA65C2-D596-
  4215-83E4-F7007B78E18C}

Distribution Point Location
All download tasks are handled by Content Access component, which is responsible for
managing the client cache. After the download task is created, Content Access component
checks if the content is already available in the client cache. If the content isn't available, it
creates a location request to get a list of Distribution Points from where the content can be
obtained. This activity can be tracked in CAS.log and LocationServices.log on the client using
the Content Unique ID.

<!-- p.43 -->

 Output

 Requesting locations synchronously for content Content_00a8f9e6-8e44-42f5-a0ef-
 9b5c86a88498.1 with priority Foreground
 ContentLocationRequest : <Request XML Body>
 Reply Message Body : <Reply XML Body>

  ） Important

  Although Location Services component handles the location requests, it doesn't directly
  request locations from the Management Point. All requests to the Management Point
  typically go through CCM Messaging component, which logs to CcmMessaging.log.

Location reply XML contains the list of distribution points based on the client's boundary
group. This list is parsed and persisted in WMI on the client according to the Content Source
Priority. This activity can be seen in ContentTransferManager.log, by using the Content Unique
ID and looking for Persisted location .

If the location reply XML doesn't contain any distribution points, ContentTransferManager.log
would show Received empty location update and the client may get stuck at 0% while
downloading the application. This reply can typically occur because of boundary group
configuration issues. For more information, see Download failures.

Content Download
Once the Distribution Point locations are obtained, Content Access component creates a
Content Transfer job. This activity can be tracked in CAS.log using the Content Unique ID.

 Output

 Submitted CTM job {6D0EA720-EB4E-4893-8395-8B27470A6CFB} to download Content
 Content_00a8f9e6-8e44-42f5-a0ef-9b5c86a88498.1 under context System

Content Transfer Manager then creates a Data Transfer Service job to do the content download.
This activity can be tracked in ContentTransferManager.log on the client using the Content
Unique ID.

 Output

 CTM job {6D0EA720-EB4E-4893-8395-8B27470A6CFB} (corresponding DTS job {708C7F21-
 8898-49AB-900E-BA6E5F1A39BC}) started download from '<Distribution Point
 URL>/Content_00a8f9e6-8e44-42f5-a0ef-9b5c86a88498.1' for full content download.

<!-- p.44 -->

  ７ Note

  This log entry can be used to identify the CTM and DTS job ID's, which can be used to
  track the progress of the Content Transfer in ContentTransferManager.log and
  DataTransferService.log respectively.

Data Transfer Service downloads the application content by creating a Background Intelligent
Transfer Service (BITS) job and waiting for the download to complete. This activity can be
tracked in DataTransferService.log on the client using the DTS Job ID obtained from
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

  Hash verification succeeded for content Content_00a8f9e6-8e44-42f5-a0ef-
  9b5c86a88498.1 downloaded under context System

Finally, after content is verified, CI Agent receives the task complete notification and the CI
Agent job moves to the next phase.

  Output

  CIAgentJob({2BF84225-C9E8-49A6-A308-A160C4B799D3}):
  CAgentJob::HandleEvent(Event=CITaskComplete, CurrentState=StateDownloadingContents)

Next steps
Application Installation

 Last updated on 03/27/2026

<!-- p.45 -->

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

When CI Agent initiates the application installation, it creates a task that is handled by the CI
Task Manager component. CI Task Manager then initiates the installation. This activity can be
tracked in the CITaskMgr.log file by using the Deployment Type Unique ID.

  Output

  Initiating task Enforce for CI ScopeId_B63CEBE7-8A69-4FBE-994F-
  5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44.2 (ConfigMgr
  Toolkit - Windows Installer (*.msi file)) for target: , consumer: {9BC3154A-98F1-
  4595-A967-173D536A3F94}
  Initiated application enforcement. : CITask(ScopeId_B63CEBE7-8A69-4FBE-994F-
  5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-
  388d220ccb44.2..Install.Enforce)

Application Enforcement
After the application enforcement is initiated, the client performs the application detection
again to ensure the application isn't already installed. Once it's determined that the application
isn't installed, the application installation is initiated. This activity can be tracked in the
AppEnforce.log file on the client by using the Deployment Type Unique ID.

<!-- p.46 -->

  Output

  +++ Starting Install enforcement for App DT "ConfigMgr Toolkit - Windows Installer
  (*.msi file)" ApplicationDeliveryType - ScopeId_B63CEBE7-8A69-4FBE-994F-
  5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44, Revision - 2,
  ContentPath - C:\WINDOWS\ccmcache\2, Execution Context - System
      Executing Command line: "C:\WINDOWS\system32\msiexec.exe" /i
  "ConfigMgrTools.msi" /q /qn with user context
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
  ++++++ App enforcement completed (3 seconds) for App DT "ConfigMgr Toolkit -
  Windows Installer (*.msi file)" [ScopeId_B63CEBE7-8A69-4FBE-994F-
  5AD0A8488D27/DeploymentType_1d49ef88-cf3b-42fa-b198-388d220ccb44], Revision: 2,
  User SID: ] ++++++

Finally, after enforcement is complete, CI Agent receives the task complete notification and the
CI Agent job moves to the next phase.

  Output

  CIAgentJob({2BF84225-C9E8-49A6-A308-A160C4B799D3}):
  CAgentJob::HandleEvent(Event=CITaskComplete, CurrentState=StateEnforcingCIs)

Next Steps
      Troubleshoot application deployments

      Common error codes for app installation

 Last updated on 03/27/2026

<!-- p.47 -->

Troubleshooting tips for application
deployments
Applies to: Configuration Manager (current branch)

Typical problems with application deployments fall into one of the following categories:

     Application download failures

     Application deployment compliance stuck at 0%

If you experience either of these issues, this article provides some steps you can use to
troubleshoot. For more in-depth troubleshooting, see Troubleshooting application deployment
technical reference.

Download failures
Application download failures include the following problems:

     The client is stuck downloading an application

     The client fails to download the application content

     The client gets stuck at 0% while downloading the application

The first thing to check when you experience application download failures is for missing or
misconfigured boundaries and boundary groups. For example, if the client is on the intranet
and not configured for internet-only client management, its network location must be in a
configured boundary. There must also be a boundary group assigned to this boundary for the
client to download content. For more information, see Define site boundaries and boundary
groups.

If you can't configure a boundary for a client, or if a specific boundary group can't be a
member of another boundary group:

   1. In the Configuration Manager console, open the properties of the Deployment Type.

   2. Switch to the Content tab.

<!-- p.48 -->

   3. In the section for using a distribution point from a neighbor boundary group or the
      default site boundary group, change the Deployment options to Download content
      from distribution point and run locally. (By default this setting is Do not download
      content.)

If the client can't download the application content, make sure it's distributed to a distribution
point. To verify this configuration, use the in-console features to monitor content distribution
to the distribution points. For more information, see Monitor content you have distributed.

Compliance stuck at 0%
When the application's deployment compliance is 0%, check the deployment status for the
application in the Monitoring workspace under the Deployments node.

      In Progress: The client could be stuck downloading content.

      Error: For more information on how to troubleshoot this problem, see the following blog
      post: Tips and Tricks: How to Take Action on Assets That Report a Failed Deployment          .

      Unknown: This status usually means that the client hasn't received policy. Manually
      refresh client policy to see if the client receives it. For more information, see Initiate policy
      retrieval for a Configuration Manager client.

If these actions don't resolve the issue, check the client status. There may be a deeper
underlying problem with the client. For more information, see How to monitor clients.

Next steps
      Monitor applications
      Deploy applications
      Management tasks for applications
      Troubleshooting application deployment technical reference

 Last updated on 03/30/2026

<!-- p.49 -->

Troubleshoot the Microsoft Store for
Business and Education integration with
Configuration Manager
This article provides key troubleshooting tips and fixes for some of the top issues that you may
have with the Microsoft Store for Business and Education (MSfB) integration with Configuration
Manager.

For more information about using the Microsoft Store for Business and Education with
Configuration Manager, see Manage apps from the Microsoft Store for Business and Education
with Configuration Manager.

Monitor
Component status
In the Configuration Manager console, go to the Monitoring workspace, expand System
Status, and select the Component Status node. Monitor status of the following components:

     SMS_BUSINESS_APP_PROCESS_MANAGER
     SMS_CLOUDCONNECTION

Sync status
In the Configuration Manager console, go to the Administration workspace, expand Cloud
Services, and select the Microsoft Store for Business node. Check the Last Sync Status column.

View synchronized apps
In the Configuration Manager console, go to the Software Library workspace, expand
Application Management, and select the License Information for Store Apps node.

Log files
WSfBSyncWorker.log

<!-- p.50 -->

This log file is located on the service connection point, under \Logs in the Configuration
Manager installation directory. It records information about the communication with the cloud
service. This information includes metadata, icons, packages, and license file retrieval.

  ） Important

  This section, method, or task contains steps that tell you how to modify the registry.
  However, serious problems might occur if you modify the registry incorrectly. Therefore,
  make sure that you follow these steps carefully. For protection, back up the registry before
  you modify it so that you can restore it if a problem occurs. For more information about
  how to back up and restore the registry, see How to back up and restore the registry in
  Windows      .

To change the log level, change the LoggingLevel value to 0 in the
HKLM\SOFTWARE\Microsoft\SMS\Tracing\SMS_CLOUDCONNECTION registry subkey. For more

information, see Configure logging options.

SMS_CLOUDCONNECTION.log
This log file is located on the service connection point, under \Logs in the Configuration
Manager installation directory. If the WSfBSyncWorker service isn't started, or repeatedly starts
and stops, review the entries in this log file.

  ７ Note

  This log file is shared with other features.

BusinessAppProcessWorker.log
This log file is located on the site server for the top-level site in the hierarchy. It's under \Logs
in the Configuration Manager installation directory. It records information about the following
processes:

     Insert the metadata information synced by the BusinessAppProcessWorker component
     into the database
     Process files in \InstallDir\inboxes\businessappprocess.box

SMS_BUSINESS_APP_PROCESS_MANAGER.log

<!-- p.51 -->

This log file is located on the site server for the top-level site in the hierarchy. It's under \Logs
in the Configuration Manager installation directory. If the BusinessAppProcessWorker service
isn't started, or repeatedly starts and stops, review the entries in this log file.

Last sync failed
When the last sync status is failed, start by reviewing the following log files to identify the
symptom:

     WSfbSyncWorker.log
     SMS_CLOUDCONNECTION.log

Then look at one of the following sections for common issues:

     Authorization error
     The secret key is invalid
     Error getting application token
     Content location doesn't exist or incorrect permissions
     Error occurred making http request calling 'GET' method
     Cannot write more bytes to the buffer
     Online application download fails with 0x8024500c

Authorization error
Cause

This issue can occur if the configured Microsoft Entra application doesn't have permissions to
manage the Microsoft Store for Business and Education for this tenant.

Workaround

   1. Sign in as an administrator to the Microsoft Store for Business or Education portal.
   2. Go to Settings, and select Management tools.
   3. If the application isn't listed, select Add a management tool. Then search by name and
     select the Microsoft Entra application associated with the same ClientID as Configuration
     Manager.
   4. If the status doesn't show Active, then select Activate in the Action section.
   5. In the Configuration Manager console, go to the Administration workspace, expand
     Cloud Services, and select the Microsoft Store for Business node. Synchronize with the
     store, or wait for the next sync interval to occur.

<!-- p.52 -->

   Tip

  To find the ClientID in Configuration Manager, follow these steps:

     1. In the Configuration Manager console, go to the Administration workspace, expand
        Cloud Services, and select the Microsoft Entra Tennts node.
     2. Select the tenant that you use for the Microsoft Store for Business and Education
        integration.
     3. In the results pane, find the matching application, and look at the Client ID column.

The secret key is invalid
Cause

This issue can occur if the secret key has expired on the Microsoft Entra app for the Microsoft
Store for Business and Education configuration.

Resolution

Renew the secret key for the Microsoft Entra application. For more information, see Renew
secret key.

Error getting application token
Cause

This issue can occur if the connected app no longer exists in Microsoft Entra ID.

Resolution

Delete and recreate the connection to the Microsoft Store for Business and Education.

   1. In the Configuration Manager console, go to the Administration workspace, expand
     Cloud Services, and select the Microsoft Store for Business node.
   2. Select the existing connection.
   3. Select Delete in the ribbon.

Then recreate the connection. For more information, see the following articles:

     Configure Azure Services
     Set up Microsoft Store for Business and Education synchronization

<!-- p.53 -->

Content location doesn't exist or incorrect permissions
Cause

When you set up the Microsoft Store for Business and Education connection, you specify a
network share for storing synchronized content. This issue can occur if this share doesn't exist
or has incorrect permissions. The computer account for the service connection point should be
the owner of this directory and any sub-directories. If it isn't, you'll see an error similar to the
following error:

 Output

 Failed to download package d788cc1b-ab00-bb5f-1548-f2dfe717583b-X86-Arm for product
 9WZDNCRFJ3PS\0015.
 System.IO.IOException: This security ID may not be assigned as the owner of this
 object.

To see the location that you configured:

   1. In the Configuration Manager console, go to the Administration workspace, expand
     Cloud Services, and select the Microsoft Store for Business node.

   2. Select the account and open its Properties.

   3. Switch to the Configuration tab. The Location setting shows the network path to store
     application content downloaded from the Microsoft Store for Business and Education.

Workaround

   1. If it doesn't already exist, create the share.

   2. Check NTFS permissions on the folder, and the permissions on the network share. Grant
     the computer account of the service connection point Read and Write permissions.

If you want to reconfigure the location, delete and recreate the connection with the new
content location.

Error occurred making http request calling 'GET' method
Cause

This issue can occur if the sync of applications from the store took so long that the content
URL expired.

<!-- p.54 -->

Workaround

Retry the sync process

   1. In the Configuration Manager console, go to the Administration workspace, expand
      Cloud Services, and select the Microsoft Store for Business node.
   2. Select the connection. In the ribbon, select Sync from Microsoft Store for Business.

With each time, it should continue further. It may take several retries depending on the
following factors:

      The number of offline applications
      The size of the packages
      The network speed

With each attempt, you should see the error fewer times. If the number of errors doesn't
reduce, there's another issue.

Cannot write more bytes to the buffer
Cause

This issue can occur if the application's package is larger than 500 MB. Configuration Manager
only supports automatic synchronization of offline applications with packages less than 500
MB.

Workaround

You can't automatically sync these apps, but you can download the content, and manually
create the application:

   1. Get the failing application ID from the following line in WSfbSynWorker.log:

       Output

       Error(s) syncing or downloading application <ApplicationID> from the Microsoft
       Store for Business.

   2. Sign in as an administrator to the Microsoft Store for Business or Education portal. Find
      the page for this application.

         Tip

<!-- p.55 -->

          The URL for the page is similar to: https://businessstore.microsoft.com/en-
          us/store/p/app/ApplicationID .

      a. Select Offline, if it isn't already selected. Then select Manage.

      b. Create a separate folder on your application content share for all supported platforms.

      c. Download the package to the package folder.

      d. Download the encoded license file as a .bin file to the package folder.

      e. Download all required frameworks to the package folder.

   3. In the Configuration Manager console, go to the Software Library workspace, expand
     Application Management, and select the Applications node.

   4. Create an application, manually specifying the application information.

      a. Create a deployment type for each supported platform that you previously
          downloaded.

      b. Type: Windows app package (*.appx, *.appxbundle)

      c. Specify the appx/appxbundle for the actual app package, not a required dependency
          package.

Confirm the following details on the final Import Information page:

     License file: Specifies the .bin file. This license file is required for offline apps.
     Windows app dependencies: Verify that all of the required dependencies are
     downloaded for this package.

Online application download fails with 0x8024500c
Cause

An 0x8024500c error during download is typically caused by the Do not connect to any
Windows Update Internet locations group policy that blocks Windows Update access.

Workaround

Don't enable the Do not connect to any Windows Update Internet locations group policy
object.

<!-- p.56 -->

Sync doesn't run
This section covers the following sync issues:

     You manually start the sync process, but it doesn't run
     The site doesn't automatically sync each day

Start by reviewing the following log files to identify the symptom:

     BusinessAppProcessWorker.log
     SMS_BUSINESS_APP_PROCESS_MANAGER.log
     WsfbSyncWorker.log
     SMS_CLOUDCONNECTION.log

Then look at one of the following sections for common issues:

     Manual sync doesn't start
     Automatic daily sync doesn't run and "shutting down # workers" error in
     SMS_BUSINESS_APP_PROCESS_MANAGER.log

Manual sync doesn't start
Cause

This issue can occur if you start a sync less than 10 minutes after the previous sync. You can't
sync more frequently than every 10 minutes.

Resolution

Wait for at least 10 minutes before starting another sync.

Automatic daily sync doesn't run and "shutting down #
workers" error in
SMS_BUSINESS_APP_PROCESS_MANAGER.log
Cause

This issue can occur if the SMS_BUSINESS_APP_PROCESS_MANAGER component stops the
WsfbSyncWorker thread. The error may specify either 2 or 4 workers.

Workaround

<!-- p.57 -->

Restart the SMS_EXECUTIVE service.

If you're not able to restart that main service, stop both components with MSfB workers, and
then start both.

  ） Important

  This section, method, or task contains steps that tell you how to modify the registry.
  However, serious problems might occur if you modify the registry incorrectly. Therefore,
  make sure that you follow these steps carefully. For protection, back up the registry before
  you modify it so that you can restore it if a problem occurs. For more information about
  how to back up and restore the registry, see How to back up and restore the registry in
  Windows     .

   1. Open the Windows registry on the server that runs the service connection point

   2. Go to
     HKLM\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_EXECUTIVE\Threads\SMS_CLOUDCONNECTION

      a. Set Requested Operation to Stop .

     b. Refresh to verify Current State = Stopped .

   3. Go to
     HKLM\SOFTWARE\Microsoft\SMS\COMPONENTS\SMS_EXECUTIVE\Threads\SMS_BUSINESS_APP_PROCES

     S_MANAGER

      a. Set Requested Operation to Stop .

     b. Refresh to verify Current State = Stopped .

   4. In SMS_CLOUDCONNECTION , set Requested Operation to Start .

   5. In SMS_BUSINESS_APP_PROCESS_MANAGER , set Requested Operation to Start .

Language-related issues
This section includes the following common issues:

     Language selection changes aren't applied
     Not all selected languages are present for all license information

<!-- p.58 -->

Language selection changes aren't applied
Cause

This issue can occur if the language selection is cached, and isn't cleared after the property
values are changed.

Workaround

To resolve this problem, restart the SMS_Executive service.

Not all selected languages are present for all license
information
Cause

This issue can occur if the Microsoft Store for Business and Education application's license
information doesn't contain localized data for the specified language.

Workaround

Manually add any missing languages for created applications.

Offline applications
This section includes the following common issues:

     Fail to create offline application because content can't be verified
     Fail to install application created from offline license information

Fail to create offline application because content can't be
verified
Cause

This issue can occur if the synchronized content for the offline application is corrupt or
modified.

Workaround

Start a new sync. When the sync completes, it should verify and download any incorrect
content files.

<!-- p.59 -->

Fail to install application created from offline license
information
Cause

This issue can occur if you deploy the application to a client running a version of Windows 10
earlier than version 1511. Offline licensed apps from the Microsoft Store for Business and
Education are only supported on Windows 10 version 1511 and later.

Resolution

Install the latest version of Windows 10.

Next steps
To find additional help, see Find help for using Configuration Manager.

 Last updated on 03/30/2026

<!-- p.60 -->

Installation of the Configuration Manager
client agent fails with error code 80041002
This article provides a solution for the 80041002 error when you try to install the Configuration
Manager client agent.

Original product version: Microsoft System Center 2012 Configuration Manager
Original KB number: 2905359

Symptoms
When you try to install the client agent on a System Center 2012 Configuration Manager
management point that has Cumulative Update 3 for System Center 2012 Configuration
Manager Service Pack 1      installed, the installation fails. Additionally, you see the following
error in the Client.msi log when verbose logging is enabled:

  [DateTime] Registering Hosting Configuration.
  MSI (s) (6C!A8) [DateTime]: Closing MSIHANDLE (22022) of type 790531 for thread 936
  [DateTime] @@ERR:25150
  MSI (s) (6C!A8) [DateTime]: Product: Configuration Manager Client -- Error 25150. Setup
  was unable to register the CCM_Service_HostingConfiguration endpoint
  The error code is 80041002

  MSI (s) (6C!A8) [DateTime]: Closing MSIHANDLE (22020) of type 790531 for thread 936
  Error 25150. Setup was unable to register the CCM_Service_HostingConfiguration endpoint
  The error code is 80041002
  MSI (s) (6C:7C) [DateTime]: Closing MSIHANDLE (22018) of type 790536 for thread 1252
  CustomAction CcmRegisterHostingConfiguration returned actual error code 1603

Resolution
To resolve this issue, follow these steps:

   1. Uninstall the management point role.

   2. Reinstall the client agent on the management point computer. To do this, perform the
     following steps:

<!-- p.61 -->

     a. On the site server, open an elevated command prompt.

     b. Change the directory to the <Configuration Manager 2012 install location>\client
        directory. For example, change the directory to D:\Program Files\Microsoft
        Configuration Manager\Client.

      c. Run the Ccmsetup.exe /source: "D:\Program Files\Microsoft Configuration
        Manager\Client" command (based on the example in the previous step).

  3. Reinstall the management point role.

Last updated on 03/30/2026

<!-- p.62 -->

Warnings for PolicyAgentInstanceProvider
are logged when installing the
Configuration Manager client
This article describes a by design behavior that many warning messages are logged for
PolicyAgentInstanceProvider when you install the Configuration Manager client.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager
Original KB number: 2688239

Symptoms
When you install the Configuration Manager client, you may find that many warning messages
for PolicyAgentInstanceProvider are logged in the Application log. Those messages resemble
the following:

  Log Name: Application
  Source: Microsoft-Windows-WMI
  Date: datetime
  Event ID: 63
  Task Category: None
  Level: Warning
  Keywords: Classic
  User: SYSTEM
  Computer: computer_name
  Description:
  A provider, PolicyAgentInstanceProvider, has been registered in the Windows Management
  Instrumentation namespace root\ccm\Policy\<SID> to use the LocalSystem account. This
  account is privileged and the provider may cause a security violation if it does not correctly
  impersonate user requests.

Event Xml:

 XML

<!-- p.63 -->

 <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
     <System>
         <Provider Name="Microsoft-Windows-WMI" Guid="{GUID}"
         EventSourceName="WinMgmt"/>
         <EventID Qualifiers="32768">63</EventID>
         <Version>0</Version>
         <Level>3</Level>
         <Task>0</Task>
         <Opcode>0</Opcode>
         <Keywords>0x80000000000000</Keywords>
         <TimeCreated SystemTime="datetime" />
         <EventRecordID>1470</EventRecordID>
         <Correlation />
         <Execution ProcessID="0" ThreadID="0" />
         <Channel>Application</Channel>
         <Computer>computer_name</Computer>
         <Security UserID="UserID" />
     </System>
     <EventData>
         <Data>PolicyAgentInstanceProvider</Data>
         <Data>root\ccm\Policy\<SID></Data>
     </EventData>
 </Event>

Cause
These warning messages are expected. They occur because Configuration Manager is not
included in the Windows Management Instrumentation (WMI) exclusion list of providers that
can run under the local system account at the time of installation.

More information
These warning messages are expected during the installation of the Configuration Manager
client and can be safely ignored. PolicyAgentInstanceProvider is registered as safe with WMI
during installation so the warning messages should stop being logged as soon as the setup
program is finished.

If the warning messages continue to be logged after the installation of the Configuration
Manager client is complete, it may be because the Configuration Manager Client Retry Task in
scheduled tasks was not removed after the successful installation. If you continue to experience
these warning messages after the Configuration Manager client is successfully installed,
deleting or disabling this task in scheduled tasks will stop the numerous WMI warning
messages from being generated.

<!-- p.64 -->

Last updated on 03/30/2026

<!-- p.65 -->

There was a problem starting
PolicyAgentProvider.dll error when
installing a Configuration Manager client
This article helps you fix an issue where you receive the There was a problem starting
PolicyAgentProvider.dll error when installing a Configuration Manager client.

Original product version: Configuration Manager
Original KB number: 2737378

Symptoms
When installing the Configuration Manager (ConfigMgr) client, the process fails with the
following error:

  There was a problem starting PolicyAgentProvider.dll The specified module could not be
  found

You may also see the following in ccmsetup.log after selecting OK on the error above:

  MSI: Action 11:53:11: CcmRegisterWmiMofFile. Registering WMI settings
  MSI: Setup failed due to unexpected circumstances
  The error code is 80004005
  MSI: Action 13:01:48: Rollback. Rolling back action:
  Installation failed with error code 1603

Cause
This can occur if the value of CWDIllegalInDllSearch in the
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager registry subkey is set

to 0xFFFFFFFF.

Resolution
There are two resolutions to this issue:

<!-- p.66 -->

      Remove the CWDIllegalInDllSearch entry or change it to a different value.

      Add the full path to the CCM folder (C:\Windows\CCM) to the environment variable PATH .

More information
CcmSetup is running the rundll32.exe PolicyAgentProvider.dll,setup_checknamespaces
command when this failure occurs.

If CWDIllegalInDllSearch is configured to 0xFFFFFFFF, rundll32.exe is unable to find the
PolicyAgentProvider.dll when running in the current working directory.

 Last updated on 03/30/2026

<!-- p.67 -->

Configuration Manager client left in
provisioning mode after upgrade to
Windows 10
This article solves the issue that the Configuration Manager client is left in provisioning mode
after performing an in-place upgrade to Windows 10.

Original product version: Configuration Manager (current branch)
Original KB number: 4021950

Symptoms
When you use the Upgrade an operating system from upgrade package operating system
task sequence to perform an in-place upgrade to Windows 10, the Configuration Manager
client may be left in provisioning mode after the upgrade succeeds and the client restarts.

Cause
This issue can occur when you specify an OEM product key for the operating system upgrade.

Resolution
To fix this issue, only specify volume license or retail product keys for the operating system
upgrade.

More information
The task sequence depends on the execution of SetupComplete.cmd by Windows to take the
Configuration Manager client out of provisioning mode. SetupComplete.cmd is disabled when
you use OEM product keys. You can check the C:\Windows\Panther\UnattendGC\Setupact.log
file to determine whether SetupComplete.cmd was executed or skipped.

To clear clients that are already stuck in provisioning mode, run the SetClientProvisioningMode
method from an elevated command prompt:

 Console

<!-- p.68 -->

 Powershell.exe Invoke-WmiMethod -Namespace root\CCM -Class SMS_Client -Name
 SetClientProvisioningMode -ArgumentList $false

Last updated on 03/30/2026

<!-- p.69 -->

Hardware inventory fails and the
SMSexec.exe process shows high sustained
CPU utilization
This article helps you fix an issue where the hardware inventory process in Configuration
Manager fails and the SMSexec.exe process shows high sustained CPU utilization.

Original product version: Configuration Manager
Original KB number: 2488396

Symptom
When using Configuration Manager, processing of hardware inventory (.MIF files) fails and the
SMSexec.exe process shows high sustained CPU utilization. Also, MIF files backlog in the
inboxes\auth\dataldr.box\process folder:

The NextGroupKey value in the ArchitectureMap table will be unusually high (> 20,000).

The following query can be used to examine the value of the NextGroupKey :

 SQL

 select NextGroupKey from ArchitectureMap where ArchitectureKey = 5

If SQLTracing is enabled on the site server, you will see the following messages repeated:

  SQL>>> select NextGroupKey from ArchitectureMap where ArchitectureKey = 5
  SQL>>>>> Done.
  SQL>>> update ArchitectureMap set NextGroupKey = NextGroupKey + 1 where
  ArchitectureKey = 5 and NextGroupKey = 15080
  SQL>>>>> Done.

You can enable SQLTracing by setting the following value to 1.

     On 64-bit systems:

       HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\SMS\Tracing\SQLEnabled

<!-- p.70 -->

      On 32-bit systems:

      HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\SQLEnabled

Cause
This issue can occur if the global No count option is enabled on the SQL Server hosting the
Configuration Manager database. If this is enabled, Configuration Manager cannot get the
correct rowcount value from SQL Server, and thus it cannot complete the cycle to extend the
schema.

Resolution
Disable the No count option and processing will continue normally. The No count option can
be found in the SQL Server Management Studio: Properties of the SQL Server > Connections >
No count. It should be unchecked.

More information
The No count option isn't enabled by default. Microsoft has not tested Configuration Manager
with the SQL Server No count global option enabled and using this option isn't supported.
Regardless, you should determine whether other applications that are using the same SQL
Server require the No count setting to be enabled before disabling it.

 Last updated on 03/30/2026

<!-- p.71 -->

The CcmExec.exe service is not
automatically restarted after the WMI
service is paused and restarted
This article provides a workaround to solve the issue that the SMS Agent Host service
(CcmExec.exe) isn't automatically restarted after the Windows Management Instrumentation
(WMI) service is paused and restarted.

Original product version: Microsoft System Center 2012 Configuration Manager
Original KB number: 2691080

Symptoms
When the WMI service is paused in Configuration Manager, the SMS Agent Host service
(CcmExec.exe) becomes nonfunctional. After the WMI service is restarted, the CcmExec.exe
service is not automatically restarted and remains nonfunctional.

Cause
This problem occurs because WMI cancels all requests when it is paused and does not restart
those requests when the service is resumed or restarted.

Workaround
To work around this problem immediately, manually restart the SMS Agent Host service. The
periodic client health check will also detect that the SMS Agent Host service isn't functioning
and restart the service when it executes.

 Last updated on 03/30/2026

<!-- p.72 -->

Configuration Manager clients fail to
communicate with CMG
This article provides solutions to common issues when Configuration Manager clients fail to
communicate with a Cloud Management Gateway (CMG).

Original product version: Configuration Manager (current branch)
Original KB number: 4503442, 4495265

Error code 403
(CMGConnector_Clientcertificaterequired)
In the following log files, error messages that resemble the following entries are logged:

LocationServices.log

 Output

 [CCMHTTP] ERROR:
 URL=https://cmgsccm.contoso.com/CCM_PROXY_MUTUALAUTH/3456/SMS_MP/.sms_aut?
 SITESIGNCERT, Port=443, Options=31, Code=0, Text=CCM_E_BAD_HTTP_STATUS_CODE
 [CCMHTTP] ERROR INFO: StatusCode= 403 StatusText=
 CMGConnector_Clientcertificaterequired

SMS_Cloud_ProxyConnector.log

 Output

 Forwarding proxy message \<message ID> to URL:
 `https://InternalMP.contoso.com/SMS_MP/.sms_aut?SITESIGNCERT`
 Web exception for message \<message ID>: System.Net.WebException: **The remote
 server returned an error: (403) Forbidden**.~~ at
 System.Net.HttpWebRequest.EndGetResponse(IAsyncResult asyncResult)~~ at
 Microsoft.ConfigurationManager.CloudConnection.ProxyConnector.ConnectionBase.Intern
 alResponseCallBack(IAsyncResult asynchronousResult)
 Received response `https://InternalMP.contoso.com/SMS_MP/.sms_aut?MPLIST2&CM1` for
 message \<message ID>: HTTP/1.1 403 CMGConnector_Clientcertificaterequired

Cause

<!-- p.73 -->

The CMG connection point requires a server authentication certificate to securely forward client
requests to an HTTPS management point. If the server authentication certificate is missing,
misconfigured, or invalid, status code 403 is returned. In scenarios where the Management
Point (MP) operates in enhanced HTTP mode with token-based authentication, the certificate
isn't required but is always recommended.

Resolution
To resolve this issue, generate a server authentication certificate for the CMG connection point.

  ７ Note

  In the certificate, computers must have a unique value in the Subject Name or Subject
  Alternative Name field.

How to verify the CMG has a server certificate
After you enable verbose logging, the SMS_Cloud_ProxyConnector.log file will show the list of
available certificates on the server. To verify if a valid server authentication certificate to
establish communication between the CMG connection point and the management point
exists, check the number of certificates in the Filtered cert count with client auth: line. See the
following log for an example:

SMS_Cloud_ProxyConnector.log

  Output

  Filtered cert count with digital signature: 7
  Not allowed cert: <certificate>
  Not allowed cert: <certificate>
  No private key cert: <certificate>
  Not allowed cert: <certificate>
  Filtered cert count with allowed root CA: 3
  Filtered cert count with private key: 3
  Not client auth cert: <certificate>
  Not client auth cert: <certificate>
  Not client auth cert: <certificate>
  Filtered cert count with client auth: 0
  Maintaining connections...

Error code 403 (CMGConnector_Forbidden)

<!-- p.74 -->

In the following log file, error messages that resemble the following entries are logged:

LocationServices.log

 Output

 [CCMHTTP] ERROR:
 URL=https://cmgsccm.contoso.com/CCM_PROXY_MUTUALAUTH/3456/SMS_MP/.sms_aut?
 SITESIGNCERT, Port=443, Options=31, Code=0, Text=CCM_E_BAD_HTTP_STATUS_CODE              \
 [CCMHTTP] ERROR INFO: StatusCode= 403 StatusText= CMGConnector_Forbidden

Cause
There's a mismatch between the Internet Information Services (IIS) bindings and the
management point in HTTP mode. If the management point is moved from HTTPS mode to
enhanced HTTP mode without cleaning the bindings, the Configuration Management client
might be unable to configure an SMS Role SSL certificate used in enhanced HTTP mode. In
other situations, an incorrect certificate (expired or revoked) exists in the IIS bindings and
needs to be cleaned.

Resolution
   1. Open IIS Manager ( inetmgr ).

   2. In the Connections pane, expand the machine name, expand Sites, and then select
     Default Web Site.

   3. In the right pane, select Bindings.

   4. In the Site Bindings dialog, select the 443 port binding, and then select Edit.

   5. In the Edit Site Binding dialog, select the certificate accordingly:

           Enhanced HTTP: SMS Role SSL certificate

           HTTPS: A valid public key infrastructure (PKI) server authentication certificate

Error code 0x2f8f
(ERROR_WINHTTP_SECURE_FAILURE)
In the following log file, an error message that resembles the following entry is logged:

LocationServices.log

<!-- p.75 -->

 Output

 [CCMHTTP] ERROR:
 URL=https://CMG.CONTOSO.COM/CCM_Proxy_ServerAuth/72057594037928017/CCM_STS,
 Port=443, Options=63, Code=12175, Text=ERROR_WINHTTP_SECURE_FAILURE

Before the error message, other events might also be logged:

 Output

 [CCMHTTP] AsyncCallback():

 [CCMHTTP] AsyncCallback(): WINHTTP_CALLBACK_STATUS_SECURE_FAILURE Encountered
 [CCMHTTP] : dwStatusInformationLength is 4
 [CCMHTTP] : lpvStatusInformation is 0x9
 [CCMHTTP] : WINHTTP_CALLBACK_STATUS_FLAG_CERT_REV_FAILED is set
 [CCMHTTP] : WINHTTP_CALLBACK_STATUS_FLAG_INVALID_CA is set
 [CCMHTTP] : WINHTTP_CALLBACK_STATUS_FLAG_CERT_CN_INVALID is set

  ７ Note

        WINHTTP_CALLBACK_STATUS_FLAG_CERT_REV_FAILED indicates that the /NoCRLCheck

        parameter is missing from the CCMSetup command, and the certificate revocation list
        (CRL) isn't published on the Internet.

        WINHTTP_CALLBACK_STATUS_FLAG_INVALID_CA indicates that the root certificate authority

        (CA) certificate required to validate the server authentication certificate for a CMG is
        missing.

        WINHTTP_CALLBACK_STATUS_FLAG_CERT_CN_INVALID indicates that the hostname in the

        certificate common name is incorrect.

Cause
This issue occurs if one or more of the following conditions are true:

     The client doesn't have the necessary PKI Root CA to validate the server authentication
     certificate.
     The certificate presented to the client is incorrect.
     The CRL that contains the certificate isn't published on the Internet, and the client is
     forced to validate the CRL.

<!-- p.76 -->

Resolution
If you're using a PKI server authentication certificate, follow these steps:

   1. Make sure that the certificate presented to the client has the expected CMG name. If
     you're using non-Microsoft services that use certificate pinning and modify the presented
     certificate, the clients can't validate the server certificate.

     To verify which certificate is presented, open the following URL in a web browser:

      https://<CMGFQDN>/CCM_Proxy_MutualAuth/ServiceMetadata

     Replace the <CMGFQDN> placeholder by using your CMG public fully qualified domain
     name (FQDN).

   2. Make sure that the client has the certificate in the local Trusted Root Certification
     Authorities certificate store. Otherwise, the client doesn't trust the CMG, even when using
     Microsoft Entra or token-based authentication. This modern authentication method is
     only available for the CMG to validate the server authentication but not for the responses
     sent from the CMG to the client. When you use a non-Microsoft certificate for
     authentication, the client can typically validate the public Root CA over the Internet.

   3. If the CRL isn't published on the Internet, make sure that the site doesn't force clients to
     validate the CRL and disable CRL checking for clients:

      a. In the Configuration Manager console, navigate to the Administration workspace.

      b. Expand Site Configuration, and then select the Sites node.

      c. Select the primary site to configure.

      d. In the ribbon, select Properties.

      e. On the Communication Security tab, clear the Clients check the certificate revocation
        list (CRL) for site systems checkbox.

        ７ Note

        When installing clients from the Internet, make sure that the /NoCRLCheck parameter
        is included in the CCMSetup command.

<!-- p.77 -->

Error code 401 (CMGService_Invalid_Token)
The client hasn't communicated with the site (via the CMG or MP) for more than 30 days, or
the CCMSetup command is attempting to use an expired token with the /regtoken parameter.
In the following log files, error messages that resemble the following entries are logged:

Ccmsetup.log

 Output

 [CCMHTTP] ERROR:
 URL=https://CMGSERVER.CLOUDAPP.NET/CCM_Proxy_ServerAuth/ServiceMetadata , Port=443,
 Options=224, >Code=0, Text=CCM_E_BAD_HTTP_STATUS_CODE
 [CCMHTTP] ERROR INFO: StatusCode=401 StatusText=CMGService_Invalid_Token

CCM_STS.log

 Output

 Return code: 401, Description: PreAuth token validation failed,
 System.IdentityModel.Tokens.SecurityTokenExpiredException:
 IDX10223: Lifetime validation failed. The token is expired.
 ValidTo: '10/01/2020 22:03:24'
 Current time: '10/28/2020 13:05:05'.
    at System.IdentityModel.Tokens.Validators.ValidateLifetime....

Cause
This issue occurs because the token has expired or wasn't properly added.

Resolution
To renew the expired token, connect the client to the internal MP directly or reinstall the client
by using a new Bulk registration token.

More information

  ） Important

  This section, method, or task contains steps that tell you how to modify the registry.
  However, serious problems might occur if you modify the registry incorrectly. Therefore,
  make sure that you follow these steps carefully. For protection, back up the registry before

<!-- p.78 -->

  you modify it so that you can restore it if a problem occurs. For more information about
  how to back up and restore the registry, see How to back up and restore the registry in
  Windows        .

For further troubleshooting, do the following actions:

      Check the IIS logs on the management point.

      In the following sample log, the 403 7 response indicates that the server certificate can't
      be found:

        Output

        <Date> <Time> <IP_address_of_MP> GET /SMS_MP/.sms_aut SITESIGNCERT 443 -
        <IP_address_of_CMG_connectionpoint> SMS+CCM+5.0 - **403 7** 0 5573 11

      Enable verbose logging for the SMS_Cloud_ProxyConnector.log file by setting the
      VerboseLogging registry entry value to 1 under the following registry subkey, and then

      restart the SMS_EXECUTIVE service.

      HKLM\SOFTWARE\MICROSOFT\SMS\SMS_CLOUD_PROXYCONNECTOR

 Last updated on 03/27/2026

<!-- p.79 -->

Can't create a CMG in a particular region
ﾃ   Summarize this article for me

Applies to: Configuration Manager (current branch)

Summary
When you try to create a Cloud Management Gateway (CMG) in a particular region, you receive
a message that states that the requested virtual machine (VM) size isn't available in that region.
Therefore, the operation to create the CMG fails. This issue occurs because a CMG requires one
of a specific subset of VM SKUs, and these SKUs aren't available in all regions.

This article helps you to work around this issue by creating the CMG in a different region, or by
creating a Microsoft support request.

Symptoms
After you try to create a CMG in a particular Azure region, you receive an error message that
resembles the following message:

 Output

 ---------------------------
 Settings
 ---------------------------
 The VM size Standard_A2_V2 is currently not available in the region West US 3 for
 this subscription. Please deploy the service in other regions or choose a different
 VM size.
 ---------------------------
 OK
 ---------------------------

<!-- p.80 -->

Cause
As per February 2026, Configuration Manager supports only the following Microsoft Azure
Virtual Machine (VM) SKUs for creating CMGs:

     Standard_B2S
     Standard_A2_V2
     Standard_A4_V2

These SKUs aren't available in all Azure regions that support Virtual Machine Scale Sets (VMSS).
If you try to create a CMG in a region that doesn't have the selected SKU, you receive the error
message.

Workaround
To mitigate this issue, Microsoft is actively working on expanding the list of SKUs that you can
use to create CMGs. In the meantime, you can use either of the following methods to work
around this issue.

Method 1: Use a different region
Create the CMG in a different Azure region that has the selected SKU available in your
subscription.

You can use the following sample script to identify which SKUs are available in different regions
in your subscription.

  ） Important

  Before you run this script, verify that you meet the following requirements:

        You installed the Azure PowerShell module.
        You used your Azure account to authenticate.

  ） Important

  This sample script is not supported under any Microsoft standard support program or
  service.

  The sample script is provided AS IS without warranty of any kind. Microsoft further
  disclaims all implied warranties including, without limitation, any implied warranties of
