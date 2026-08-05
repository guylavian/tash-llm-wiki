---
title: "Welcome — pages 81-120"
type: reference
domain: sccm
slug: sccm-troubleshoot-mem-configmgr-p0081-0120
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/troubleshoot-mem-configmgr-p0081-0120
family: sccm
documentKind: "doc"
abstract: "merchantability or of fitness for a particular purpose. The entire risk arising out of the use or performance of the sample scripts and documentation remains with you. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of t"
---

# Welcome — pages 81-120

<!-- p.81 -->

  merchantability or of fitness for a particular purpose.

  The entire risk arising out of the use or performance of the sample scripts and
  documentation remains with you. In no event shall Microsoft, its authors, or anyone else
  involved in the creation, production, or delivery of the scripts be liable for any damages
  whatsoever (including, without limitation, damages for loss of business profits, business
  interruption, loss of business information, or other pecuniary loss) arising out of the use of
  or inability to use the sample scripts or documentation, even if Microsoft has been advised
  of the possibility of such damages.

 PowerShell

 Connect-AzAccount

 # Define the supported SKUs and fetch region display names.
 $supportedSkus = @('Standard_B2s', 'Standard_A2_v2', 'Standard_A4_v2')
 $locationMap = @{}; $displayMap = @{}
 Get-AzLocation | ForEach-Object { $locationMap[$_.DisplayName] = $_.Location;
 $displayMap[$_.Location] = $_.DisplayName }

 # Get only the regions that have VMSS available.
 $vmssRegions = (Get-AzResourceProvider -ProviderNamespace
 Microsoft.Compute).ResourceTypes |
     Where-Object { $_.ResourceTypeName -eq 'virtualMachineScaleSets' } |
     Select-Object -ExpandProperty Locations |
     ForEach-Object { if ($locationMap.ContainsKey($_)) { $locationMap[$_] } else {
 $_ } } |
     Select-Object -Unique

 # Check SKU availability in the VMSS-enabled regions.
 $results = Get-AzComputeResourceSku |
     Where-Object { $_.ResourceType -eq 'virtualMachines' -and $supportedSkus -
 contains $_.Name -and $_.Restrictions.Count -eq 0 } |
     ForEach-Object { foreach ($loc in $_.Locations) { if ($vmssRegions -contains
 $loc) { if ($displayMap.ContainsKey($loc)) { $regionName = $displayMap[$loc] } else
 { $regionName = $loc }; [PSCustomObject]@{ Sku = $_.Name; Region = $regionName } }
 } } |
     Sort-Object Sku, Region | Select-Object -Unique Sku, Region

 if (-not $results -or $results.Count -eq 0) { Write-Host 'No available regions
 found for the supported CMG SKUs.' } else { $results | Out-GridView -Title
 'Available regions for supported CMG SKUs' }

Method 2: Create a support request
To check the availability of a given SKU and request an exception (if it's necessary), contact
Microsoft Support    .

<!-- p.82 -->

More information
For more information about SKUs that you can use to create CMGs, see Size and scale for CMG.

Last updated on 02/26/2026

<!-- p.83 -->

CMG maintenance task fails to update
public IP resource after installing
KB32851084
Applies to: Configuration Manager (current branch)

Symptoms
After you install the Update Rollup for Microsoft Configuration Manager version 2503
(KB32851084), CloudMgr.log on the Service Connection Point might display the following error
message:

 Output

 Resource Manager - Creating Public IP Address <Name of CMG> with deployment
 CreatePublicIPAddressXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX~~
 ERROR: Exception occured for service <Name of CMG> : System.AggregateException: One
 or more errors occurred.
 ---> Azure.RequestFailedException: At least one resource deployment operation
 failed. Please list deployment operations for details. Please see
 https://aka.ms/arm-deployment-operations for usage details.~~Status: 200
 (OK)~~ErrorCode: DeploymentFailed~~~~Service request succeeded. Response content and
 headers are not included to avoid logging sensitive data.~~~~
 at Azure.Core.OperationInternal`1.GetResponseFromState(OperationState`1 state)~~
 at Azure.Core.OperationInternal`1.<UpdateStatusAsync>d__20.MoveNext()~~--- End of
 stack trace from previous location where exception was thrown ---~~
 at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()~~
 at
 System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(
 Task task)~~
 at Azure.Core.OperationInternalBase.<UpdateStatusAsync>d__13.MoveNext()~~--- End of
 stack trace from previous location where exception was thrown ---~~
 at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()~~
 at Azure.Core.OperationPoller.<WaitForCompletionAsync>d__11.MoveNext()~~--- End of
 stack trace from previous location where exception was thrown ---~~
 at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()~~
 at
 System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(
 Task task)~~
 at Azure.Core.OperationInternalBase.
 <WaitForCompletionResponseAsync>d__19.MoveNext()~~--- End of stack trace from
 previous location where exception was thrown ---~~
 at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()~~
 at
 System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(
 Task task)~~
 at Azure.Core.OperationInternal`1.<WaitForCompletionAsync>d__19.MoveNext()~~--- End
 of stack trace from previous location where exception was thrown ---~~

<!-- p.84 -->

 at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()~~
 at
 System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(
 Task task)~~
 at System.Threading.Tasks.ValueTask`1.get_Result()~~
 at Azure.Core.OperationInternal`1.<WaitForCompletionAsync>d__15.MoveNext()~~--- End
 of stack trace from previous location where exception was thrown ---~~
 at System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()~~
 at
 System.Runtime.CompilerServices.TaskAwaiter.HandleNonSuccessAndDebuggerNotification(
 Task task)~~
 at Azure.ResourceManager.Resources.ArmDeploymentCollection.
 <CreateOrUpdateAsync>d__4.MoveNext()~~
 --- End of inner exception stack trace ---~~
 at System.Threading.Tasks.Task`1.GetResultCore(Boolean waitCompletionNotification)~~
 at
 Microsoft.ConfigurationManager.AzureManagement.ResourceManager.StartAndMonitorDeploy
 ment(String resourceGroupName, String deploymentName, ArmDeploymentContent
 deploymentContent, Int32 secondsToWait, Int32 timeoutInMinutes)~~
 at Microsoft.ConfigurationManager.AzureManagement.Resource

 TaskManager: Task [Deployment Maintenance for service <Name of CMG>] status is
 Faulted~~

 ERROR: TaskManager: Task [Deployment Maintenance for service <Name of CMG>] has
 failed. Exception Azure.RequestFailedException, At least one resource deployment
 operation failed. Please list deployment operations for details. Please see
 https://aka.ms/arm-deployment-operations for usage details.~~Status: 200
 (OK)~~ErrorCode: DeploymentFailed~~~~Service request succeeded. Response content and
 headers are not included to avoid logging sensitive data.~~.~~

 TaskManager: Scheduling task [Deployment Maintenance for service <Name of CMG>] for
 retry.~~

In the Azure portal, the Activity log of the Resource Group that contains the resources of the
CMG displays the following error message:

 Output

 Operation Name: Create or Update Public Ip Address

 Summary - Message; Resource /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-
 xxxxxxxxxxxx/resourceGroups/<Name of CMG Resource
 Group>/providers/Microsoft.Network/publicIPAddresses/<Name of Public IP Address> has
 an existing availability zone constraint 1, 2, 3 and the request has availability
 zone constraint NoZone, which do not match. Zones cannot be added/updated/removed
 once the resource is created. The resource cannot be updated from regional to zonal
 or vice-versa.

The Cloud Management Gateway (CMG) state in the Configuration Manager console might
then appear in "Error" status with the detailed information "Failed to perform maintenance" in
"Status Description" and flipping back to "Ready" shortly afterwards.

<!-- p.85 -->

The error messages likely repeat every 20 minutes, aligning with the Deployment Maintenance
Task retries.

Cause
When you install the Update Rollup, it triggers a setup maintenance task for the CMG. This
maintenance task launches deployments for CMG Resources in Azure. In the deployment
associated to the Public IP Address, the maintenance task attempts to update its "Availability
Zone" configuration property to "No zone". If the existing Public IP resource already has
"Availability Zone" property configured (for example, to "Zone 1", "Zone 2", or "Zone 3"), the
deployment fails.

The issue then affects the Azure regions where Availability Zones are supported. The current list
is available at Azure regions list.

Current Configuration Manager releases don't specify Availability Zone when creating a new
Public IP Address Resource for CMG. Hence, this issue doesn't affect new CMG deployments.

Resolution
Microsoft has released a hotfix to address this issue: Cloud management gateway deployment
maintenance update for Configuration Manager 2409, 2503. Configuration Manager 2509
includes this hotfix.

More information
For more information about CMG monitoring, see Monitor the CMG

 Last updated on 12/10/2025

<!-- p.86 -->

Multiple instances of the Unknown
computers collection occur when you
reinstall a primary site
This article provides a workaround for the issue that multiple instances of the Unknown
computers collection are shown in Microsoft Configuration Manager.

Original product version: Microsoft System Center 2012 Configuration Manager
Original KB number: 2688121

Symptoms
Consider this scenario in Microsoft Configuration Manager:

     You install a central administration site.
     You install a primary site and then uninstall the primary site.
     You reinstall the primary site by using the same server name and site name.

In this scenario, you may notice multiple instances of the Unknown computers collection.

Workaround
To work around this problem, create a collection that includes all Unknown Computer objects.
This method creates a collection that contains both active and inactive objects. Then, advertise a
task sequence to this collection to make sure that it becomes associated with the inactive GUID
that is being used by the Pre-Boot Execution Environment (PXE) image.

To do this, run the following query for the collection, and then retarget advertisements to the
new collection:

 SQL

 Select
 SMS_R_UNKNOWNSYSTEM.ResourceID,SMS_R_UNKNOWNSYSTEM.ResourceType,SMS_R_UNKNOWNSYSTEM.Na
 me,SMS_R_UNKNOWNSYSTEM.Name,SMS_R_UNKNOWNSYSTEM.Name from SMS_R_UnknownSystem where
 Decommissioned = "0"

<!-- p.87 -->

Last updated on 06/25/2026

<!-- p.88 -->

Configuration Manager console appears to
hang when you add a driver to a boot
image
This article helps you resolve an issue where the Configuration Manager console appears to
stop responding while it's loading a list of drivers from the driver catalog.

Original product version: Microsoft System Center 2012 Configuration Manager, Microsoft
System Center 2012 R2 Configuration Manager
Original KB number: 3070057

Symptoms
When you add a driver on the Drivers tab of the properties of a boot image, the Configuration
Manager console may appear to hang or stop responding while it's loading the list of drivers
from the driver catalog. For example, in an environment that has 500 drivers, the console may
appear to stop responding for up to 8 minutes. However, the exact number of drivers and
length of delay will vary, depending on system performance.

During this time, a review of the Smsprov.log file on the site server shows that Configuration
Manager is in fact enumerating through the available drivers:

  CExtUserContext::EnterThread : User=<DOMAIN\user>
  Sid=0x010500000:-000000515XXXXCEBFCF270C2XXXXC3CAFFF0 Caching
  IWbemContextPtr=0000008DEF086000 in Process 0x1534 (5428)
  Context: SMSAppName=Configuration Manager Administrator console
  Context: MachineName=<siteserver.fqdn>
  Context: UserName==<DOMAIN\user>
  Context: ObjectLockContext=796d1f9e-3512-4fd4-ae23-11cbe5883fda
  Context: ApplicationName=Microsoft.ConfigurationManagement.exe
  Context: ApplicationVersion=5.0.8239.1000
  Context: LocaleID=MS\0x409
  Context: __ProviderArchitecture=32
  Context: __RequiredArchitecture=0 (Bool)
  Context: __ClientPreferredLanguages=en-US,en
  Context: __CorrelationId={3ACC714D-97FE-0005-897C-CC3AFE97D001}

<!-- p.89 -->

  Context: __GroupOperationId=181360
  CExtUserContext : Set ThreadLocaleID OK to: 1033
  CSspClassManager::PreCallAction, dbname=CM_392
  ExecQueryAsync: START select FromCIID from SMS_CIRelation where ToCIID =16777966
  AND RelationType=5
  Adding Handle -346430696 to async call map
  CExtProviderClassObject::DoCreateInstanceEnumAsync (SMS_CIRelation)
  CSspQueryForObject :: Execute...
  Execute WQL =select FromCIID from SMS_CIRelation where ToCIID =16777966 AND
  RelationType=5
  Execute SQL =select all SMS_CIRelation.FromCIID from vSMS_CIRelation AS SMS_CIRelation
  where (SMS_CIRelation.ToCIID = 16777966 AND SMS_CIRelation.RelationType = 5)
  Results returned : 0 of 1
  Removing Handle -346430696 from async call map
  ExecQueryAsync: COMPLETE select FromCIID from SMS_CIRelation where ToCIID
  =16777966 AND RelationType=5
  CExtUserContext::LeaveThread : Releasing IWbemContextPtr=-284663808

Cause
This issue occurs because of the time that is required to enumerate the available drivers.

Resolution
Depending on the number of drivers and on individual system performance, the operation may
eventually complete successfully. However, to avoid the issue, consider creating additional
folders to store your drivers. By doing this, you can reduce the number of drivers that are being
enumerated in a single folder view.

The following workarounds are also available:

     In the Operating Systems\Drivers node, select the driver to be added, right-click the
     driver, select Edit, select Boot Images, and then specify the boot image to which the
     selected driver is to be added.
     During import or reimport of the driver into the driver catalog, add the driver to the
     necessary boot image at that time.
     Add the driver to the boot image by using the Set-CMDriverBootImage Windows
     PowerShell cmdlet.

<!-- p.90 -->

     Use DISM to manually add the driver to the boot image.

Last updated on 03/30/2026

<!-- p.91 -->

Issues in Configuration Manager after
installing June 2022 security updates for
Windows
Applies to: Configuration Manager (current branch)

Microsoft Endpoint Configuration Manager uses the Distributed Component Object Model
(DCOM) Remote Protocol at multiple parts of functionality. With the June 2022 security
updates for Windows, hardening changes in DCOM are enabled by default. This article
provides solutions for issues that may occur in Configuration Manager after the June 2022
security updates for Windows are installed.

Symptoms
After installing the June 2022 security updates for Windows or later, a Configuration Manager
administrator encounters one of the following issues:

     The Configuration Manager console fails to access the SMS Provider remotely under any
     user account. However, under the same credential, a local connection to the SMS Provider
     is successful.

     When the Configuration Manager administrator connects remotely to client computers,
     the same issue (under any user account, the remote connection fails, but the local
     connection is successful) occurs for Configuration Manager tools like Support Center or
     Policy Spy.

     Content fails to be distributed to a remote distribution point.

Error codes that are recorded in the respective log files or client applications may resemble the
following:

                                                                                ﾉ   Expand table

 Error code                    Error message

 0x80070005                    Access is Denied.

 0x800706ba                    The RPC server is unavailable.

<!-- p.92 -->

For example, when the administrator tries to open a console remotely, the SmsAdminUI.log file
displays the following error message:

  Insufficient privilege to connect, error: 'Access is denied. (Exception from HRESULT:
  0x80070005 (E_ACCESSDENIED))' System.UnauthorizedAccessException
  Access is denied. (Exception from HRESULT: 0x80070005 (E_ACCESSDENIED))
  at System.Management.ThreadDispatch.Start()
  at System.Management.ManagementScope.Initialize()
  at System.Management.ManagementObjectSearcher.Initialize()
  at System.Management.ManagementObjectSearcher.Get()
  at
  Microsoft.ConfigurationManagement.ManagementProvider.WqlQueryEngine.WqlConnectio
  nManager.Connect(String configMgrServerPath)
  at
  Microsoft.ConfigurationManagement.AdminConsole.SmsSiteConnectionNode.GetConnecti
  onManagerInstance(String connectionManagerInstance)

Resolution
To resolve these issues, install the latest cumulative update for Windows on both computers
that initiate the connection (the remote console or site server) and receive it (the SMS Provider,
distribution point, or remote client). Besides enhancing security, installing the update can
ensure the same level of DCOM hardening and logging capabilities.

The latest versions of Configuration Manager make security changes, so we recommend that
you upgrade to Configuration Manager, version 2203 or a later version.

DCOM hardening changes
In 2021, the Windows DCOM Server Security Feature Bypass vulnerability was discovered and
released in CVE-2021-26414     . Later, Microsoft released security updates that improved DCOM
protocol hardening. However, some applications require a code change to comply with the
new security level. Therefore, Microsoft addressed this vulnerability with a phased approach,
which is configurable by the RequireIntegrityActivationAuthenticationLevel registry key. See
the following timeline:

                                                                                 ﾉ   Expand table

<!-- p.93 -->

 Update         Behavior change
 release

 June 8,        Hardening changes disabled by default but with the ability to enable them using a registry
 2021           key.

 June 14,       Hardening changes enabled by default but with the ability to disable them using a registry
 2022           key.

 March 14,      Hardening changes enabled by default with no ability to disable them. By this point, you
 2023           must resolve any compatibility issues with the hardening changes and applications in your
                environment.

For more information, see KB5004442—Manage changes for Windows DCOM Server Security
Feature Bypass (CVE-2021-26414)          .

Verify DCOM hardening issue
To verify the DCOM hardening issue, check the following Event IDs in the System event logs on
the server and client computers. For more information, see the "New DCOM error events"
section in KB5004442       .

To log these events, install at least the October 2021 Cumulative Update for Windows. The
following time-correlated events should mention Configuration Manager applications and the
usernames they're running under:

     Server-side event

                                                                                          ﾉ   Expand table

        Event    Message
        ID

        10036    The server-side authentication level policy does not allow the user %1\%2 SID (%3) from
                 address %4 to activate DCOM server. Please raise the activation authentication level at
                 least to RPC_C_AUTHN_LEVEL_PKT_INTEGRITY in client application.

                 (%1 – domain, %2 – user name, %3 – User SID, %4 – Client IP Address)

     Client-side events

                                                                                          ﾉ   Expand table

<!-- p.94 -->

       Event     Message
       ID

       10037     Application %1 with PID %2 is requesting to activate CLSID %3 on computer %4 with
                 explicitly set authentication level at %5. The lowest activation authentication level required
                 by DCOM is 5(RPC_C_AUTHN_LEVEL_PKT_INTEGRITY). To raise the activation
                 authentication level, please contact the application vendor.

       10038     Application %1 with PID %2 is requesting to activate CLSID %3 on computer %4 with
                 default activation authentication level at %5. The lowest activation authentication level
                 required by DCOM is 5(RPC_C_AUTHN_LEVEL_PKT_INTEGRITY). To raise the activation
                 authentication level, please contact the application vendor.

                 (%1 – Application Path, %2 – Application PID, %3 – CLSID of the COM class the application
                 is requesting to activate, %4 – Computer Name, %5 – Value of Authentication Level)

If you want to temporarily disable the DCOM hardening, set the value of the
RequireIntegrityActivationAuthenticationLevel registry key to 0x00000000 :

      Path: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\AppCompat
      Value Name: RequireIntegrityActivationAuthenticationLevel
      Type: dword
      Value Data: 0x00000000

To enable the DCOM hardening, set the registry value to 0x00000001 . If this registry key isn't
defined, it will be enabled by default.

  ７ Note

  This registry key will be ignored starting from March 14, 2023. Upgrade the operating
  systems before this date.

If the issue persists after completing the steps above, contact Microsoft Support                .

 Last updated on 03/30/2026

<!-- p.95 -->

Some devices are reported as failed on the
client health dashboard
Starting in version 1902 of Configuration Manager current branch, the client health dashboard
is available to assess the health of Configuration Manager clients in your environment. This
article describes an issue in which some devices are unexpectedly reported as Failure on the
Status Messages bar of the Scenario Health bar chart. This article also provides some insights
into the internals and calculations of the Scenario Health bar chart.

Applies to: Configuration Manager (current branch)
Original KB number: 4643234

Symptoms
In the Scenario Health bar chart of the client health dashboard, some devices are unexpectedly
reported as Failure on the Status Messages bar. The corresponding information is also
reflected on the Combined (Any) bar.

Cause
A Configuration Manager client sends a status message in the following scenarios:

     You run a legacy software distribution, such as a classic package, on the client.
     Something is changed or broken on the client. For example, a software inventory isn't
     completed within the time-out period.

If you use only the Modern Software Distribution technologies, and you deploy software
updates, no status message will be sent, and the last status message timestamp will not be
updated in the database.

<!-- p.96 -->

  ７ Note

  Hidden legacy package deployments, such as Configuration Manager Client Upgrade
  packages, might update the last status message timestamp.

Workaround
You can deploy a dummy legacy package (such as the cmd /c echo command) to an affected
client to generate a constant status message flow. Then, a status message timestamp will be
updated regularly, and the client will be reported as Success on the Status Messages bar.
Alternatively, you can ignore or hide the Status Messages bar.

More information
The client health dashboard displays the summarized client health information. To view client
information in the Configuration Manager console, administrators can add the relevant
columns (such as Policy Request or Status Message) or check the Client Activity section of the
client.

By default, the health information is summarized on a site server one time per day. In the Client
Status Settings Properties dialog box on the Client Activity site, administrators can also
configure the settings to monitor client status. If the recent status message was created within
the past seven days, that client is considered to be active at Monitoring > Overview > Client
Status > Client Activity.

<!-- p.97 -->

In Configuration Manager, administrators can use a maintenance task (Delete Aged Status
Messages) to delete status messages that are older than 30 days (by default), as configured in
status filter rules.

<!-- p.98 -->

The SQL Stored Procedure ( spGetClientHealthDashboard ) calculates the Success and Failure
status for individual clients, as follows:

     If the timestamp of the recent status message is less than seven days old, or there is no
     status message, the client is reported as Success.
     If the timestamp of the recent status message is more than seven days old, and the status
     message is not deleted, the client is reported as Failure.

  ７ Note

  This algorithm is also applicable to other bars. However, there is no cleanup mechanism
  for inventory timestamps.

By default, the client health dashboard displays the health information of clients that were
online during the previous three days.

<!-- p.99 -->

See also
MMS: ConfigMgr State and Status Messages

Third-party contact disclaimer

Microsoft provides third-party contact information to help you find additional information
about this topic. This contact information may change without notice. Microsoft does not
guarantee the accuracy of third-party contact information.

Last updated on 02/04/2026

<!-- p.100 -->

SQL query times out or console slow on
certain Configuration Manager database
queries
This article helps you fix an issue in which the Configuration Manager console is slow or the
SQL query times out for certain Configuration Manager database queries.

Original product version: SQL Server 2022 on Windows (all editions), SQL Server 2019 on
Windows (all editions), SQL Server 2017 on Windows (all editions), SQL Server 2016 Enterprise,
SQL Server 2016 Standard, SQL Server 2014 Enterprise, SQL Server 2014 Standard, System
Center Configuration Manager
Original KB number: 3196320

Symptoms
You experience slow Configuration Manager console performance or unusual SQL query
timeouts for certain Configuration Manager database queries in environments running SQL
Server 2014, SQL Server 2016, or SQL Server 2017 on Windows.

Cause
SQL Server Cardinality Estimation (CE) changes in SQL Server 2014, SQL Server 2016, and SQL
Server 2017 on Windows may cause performance issues with certain Configuration Manager
queries in some environments.

Resolution
In affected environments, Configuration Manager may run better when the site database is
configured at a different SQL Server CE compatibility level. To identify the recommended CE
level for your version of SQL Server, refer to the following table:

                                                                                 ﾉ   Expand table

 SQL Server   Supported                 Recommended compatibility     Recommended level for
 version      compatibility level       level for Configuration       specific performance issues
              values                    Manager

 SQL Server   150, 140, 130, 120, 110   150                           110
 2022

<!-- p.101 -->

 SQL Server   Supported                 Recommended compatibility   Recommended level for
 version      compatibility level       level for Configuration     specific performance issues
              values                    Manager

 SQL Server   150, 140, 130, 120, 110   150                         110
 2019

 SQL Server   140, 130, 120, 110        140                         110
 2017

 SQL Server   130, 120, 110             130                         110
 2016

 SQL Server   120, 110                  110                         110
 2014

Starting in Configuration Manager current branch version 1810, when the Configuration
Manager database is running on SQL Server 2016 SP1 or later versions, all queries issued by
the Admin console and SMS Provider will automatically add the USE HINT
'FORCE_LEGACY_CARDINALITY_ESTIMATION' query hint. Therefore, Admin console performance

won't be affected when you change the CE Compatibility level to 110 at the database level to
resolve performance issues. If you want to override this behavior, to have the Admin console
and SMS Provider queries use the current SQL Server CE level instead, set the
UseLegacyCardinality value to 0 under the following registry subkey on the computer that

hosts the SMS Provider:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Providers

To identify what SQL Server CE compatibility level is in use for the Configuration Manager
database, run the following query:

 SQL
 SELECT name, compatibility_level FROM sys.databases

On SQL Server 2014 and SQL Server 2016 RTM, to identify whether using SQL Server 2012 CE
(110) may improve Configuration Manager query performance, identify a query that is running
slowly and manually test its performance at the SQL Server 2012 CE compatibility level. To do
this, run the query in SQL Server Management Studio with option (querytraceon 9481) and
compare the execution time to its performance without the flag.

Starting with SQL Server 2016 SP1, to accomplish this at the query level, add the USE HINT
'FORCE_LEGACY_CARDINALITY_ESTIMATION' query hint instead of using trace flag 9481.

<!-- p.102 -->

For more information about using querytraceon with trace flag 9481 at the specific-query level,
see Hints (Transact-SQL) - Query. For information about using SQL Server Profiler to identify
slow queries, see SQL Server Profiler.

See the following example of a specific-query test run at the SQL Server 2012 CE level against
SQL Server 2014:

 SQL

 select
 SMS_DeploymentSummary.ApplicationName,SMS_DeploymentSummary.AssignmentID,SMS_Deploym
 entSummary.CI_ID,SMS_DeploymentSummary.CollectionID,SMS_DeploymentSummary.Collection
 Name,SMS_DeploymentSummary.CreationTime,SMS_DeploymentSummary.DeploymentID,SMS_Deplo
 ymentSummary.DeploymentIntent,SMS_DeploymentSummary.DeploymentTime,SMS_DeploymentSum
 mary.DesiredConfigType,SMS_DeploymentSummary.EnforcementDeadline,SMS_DeploymentSumma
 ry.FeatureType,SMS_DeploymentSummary.ModelName,SMS_DeploymentSummary.ModificationTim
 e,SMS_DeploymentSummary.NumberErrors,SMS_DeploymentSummary.NumberInProgress,SMS_Depl
 oymentSummary.NumberOther,SMS_DeploymentSummary.NumberSuccess,SMS_DeploymentSummary.
 NumberTargeted,SMS_DeploymentSummary.NumberUnknown,SMS_DeploymentSummary.ObjectTypeI
 D,SMS_DeploymentSummary.PackageID,SMS_DeploymentSummary.PolicyModelID,SMS_Deployment
 Summary.ProgramName,SMS_DeploymentSummary.SecuredObjectId,SMS_DeploymentSummary.Soft
 wareName,SMS_DeploymentSummary.SummarizationTime,SMS_DeploymentSummary.SummaryType
 from fn_DeploymentSummary(1033) AS SMS_DeploymentSummary where
 SMS_DeploymentSummary.DeploymentID = N'CS100012' option (querytraceon 9481)

  ７ Note

  The query above and deployment ID CS100012 are for demonstration purposes only and
  will vary by environment.

If the above test indicates that performance gains can be achieved, use the following command
in SQL Server Management Studio to set the Configuration Manager database to the SQL
Server 2012 CE compatibility level:

 SQL
 ALTER DATABASE <CM_DB>
 SET COMPATIBILITY_LEVEL = 110;
 GO

  ７ Note

  In the above example, replace <CM_DB> with your Configuration Manager site database
  name. To change the CE compatibility level to a different level, change the value in SET
  COMPATIBILITY_LEVEL .

<!-- p.103 -->

More information
When a SQL Server instance is upgraded in-place from any earlier version of SQL Server, pre-
existing databases will keep their existing compatibility level if they are at the minimum
allowed level for that new version of SQL Server. Upgrading SQL Server with a database at a
compatibility level lower than the allowed level automatically sets the database to the lowest
compatibility level allowed by the new version of SQL Server.

During upgrades or new installations of Configuration Manager, databases may be
automatically configured to use the recommended SQL Server CE compatibility version for that
version of SQL Server (as shown in the table that's mentioned in the Resolution section). If you
experience performance degradation after a servicing update, as a result of being reverted
back to the default recommended CE level for your version of SQL Server, reassess whether
you may have to manually change the CE level back to 110.

For more information about SQL Server CE compatibility levels, see ALTER DATABASE (Transact-
SQL) Compatibility Level.

 Last updated on 02/04/2026

<!-- p.104 -->

The Windows Servicing dashboard shows
no data
Applies to: Microsoft Configuration Manager

Symptoms
The Windows Servicing dashboard displays no data or contains stale operating system version
information.

Cause
The issue might occur in either of the following situations:

     The service connection point is running in Offline mode.
     The service connection point is running in Online mode, but it can't obtain the Admin UI
     content payload.

Resolution
If the service connection point is running in Offline mode, use the service connection tool to
download and import updates that include the Admin UI content payload.

If the service connection point is running in Online mode, review the DmpDownloader.log file for
failures that occurred when accessing the ConfigMgr.AdminUIContent.cab payload URL. For
troubleshooting steps, refer to Troubleshoot the Synchronization stage.

To work around the issue, follow these steps:

   1. Manually download the ConfigMgr.AdminUIContent.cab file from
     https://go.microsoft.com/fwlink/?LinkID=619849       .

   2. Copy the ConfigMgr.AdminUIContent.cab file to the top-level site server.

   3. Rename the ConfigMgr.AdminUIContent.cab file to ConfigMgr.AdminUIContent.auc.

   4. Copy the ConfigMgr.AdminUIContent.auc file to the following directory:

     <Configuration Manager installation path>\inboxes\hman.box\CFD

<!-- p.105 -->

     For example, copy the file to E:\ConfigMgr\inboxes\hman.box\CFD.

  5. In Hman.log, you should see entries that resemble the following example:

       Output

       File 'E:\ConfigMgr\inboxes\hman.box\CFD\ConfigMgr.AdminUIContent.auc' is signed
       and trusted.
       File 'E:\ConfigMgr\inboxes\hman.box\CFD\ConfigMgr.AdminUIContent.auc' is signed
       with MS root cert.
       Extracting file E:\ConfigMgr\inboxes\hman.box\CFD\ConfigMgr.AdminUIContent.auc to
       E:\ConfigMgr\AdminUIContentStaging\~
       Extracted E:\ConfigMgr\AdminUIContentStaging\CAMPServicingStates.xml~
       Extracted E:\ConfigMgr\AdminUIContentStaging\DriverUpdates.xml~
       Extracted E:\ConfigMgr\AdminUIContentStaging\LifecycleProducts.xml~
       Extracted E:\ConfigMgr\AdminUIContentStaging\NotificationBannerData.xml~
       Extracted E:\ConfigMgr\AdminUIContentStaging\UUPPSFXProductsAndOSVersions.xml~
       Extracted
       E:\ConfigMgr\AdminUIContentStaging\WindowsServicingBusinessReadyUpdates.xml~
       Extracted E:\ConfigMgr\AdminUIContentStaging\WindowsServicingLocalizedNames.xml~
       Extracted
       E:\ConfigMgr\AdminUIContentStaging\WindowsServicingProductCategoryNames.xml~
       Extracted E:\ConfigMgr\AdminUIContentStaging\WindowsServicingStates.xml~
       Extracted E:\ConfigMgr\AdminUIContentStaging\WindowsServicingTimeline.html~
       Extracted
       E:\ConfigMgr\AdminUIContentStaging\WindowsServicingXtBusinessReadyUpdates.xml~
       Successfully updated AdminUI content.

  6. Try again to open the Windows Servicing dashboard.

Last updated on 06/25/2026

<!-- p.106 -->

Configure peer cache for Configuration
Manager clients
Applies to: Microsoft Endpoint Configuration Manager (current branch)

Peer cache is a built-in solution for Microsoft Endpoint Configuration Manager that enables
clients to share content with other clients directly from their local cache. It extends traditional
content deployment solutions, such as distribution points. Use peer cache to help manage
deployment of content to clients in remote locations. For more information, see Peer cache for
Configuration Manager clients.

Configure peer cache client settings
To enable clients to be peer cache sources, follow these steps:

   1. In the Configuration Manager console, create a device collection. Determine which clients
     you want to enable as peer cache sources, and add them to the collection.

   2. Go to the Administration workspace, and then select the Client Settings node.

   3. Select Create Custom Client Device Settings, specify a name and description, and then
     select the Client Cache Settings group.

<!-- p.107 -->

4. In the navigation pane, select Client Cache Settings, set Enable as peer cache source to
  Yes, and then specify the ports.

<!-- p.108 -->

   5. Select OK to save the settings.

   6. Deploy this custom client setting to the device collection that you created in step 1.

You don't have to enable peer cache clients. When you enable clients to be peer cache sources,
the management point includes them in the list of content location sources.

Changes on clients that act as peer cache sources
When the client cache setting is deployed to the device collection, you'll see the following
changes on the peer cache sources:

     In the WMI class instance CCM_SuperPeerClientConfig.SiteSettingsKey=1 under
     ROOT\ccm\Policy\Machine\ActualConfig :

     The value of the CanBeSuperPeer property is changed to True.

     The following entries are logged in CcmExec.log:

       Output

       Notifying endpoint 'SuperPeerController' of 1 settings change(s).
       Notifying endpoint 'SuperPeerController' of __InstanceModificationEvent

<!-- p.109 -->

       settings change on object CCM_SuperPeerClientConfig.SiteSettingsKey=1 for user
       'SID'.

     The following entries are logged in CAS.log:

       Output

       SuperPeerController main thread has started.
       SuperPeerController has started

     A state message of topic type 7201 is generated. The following entries are logged in
     StateMessage.log:

       Output

       Adding message with TopicType 7201 and TopicId Super Peer is now active to WMI
       State message(State ID : 2) with TopicType 7201 and TopicId Super Peer is now
       active has been recorded for SYSTEM

Change on the management point
The state message is formatted as XML, and then sent to the management point
(MP_RelayEndpoint) through CCMMessaging.

You'll see the following entry in the MP_Relay.log file:

 Output

 Message Body :
 <?xml version="1.0" encoding="UTF-16"?>
 <Report><ReportHeader><Identification><Machine><ClientInstalled>1</ClientInstalled>
 <ClientType>1</ClientType><ClientID>GUID:xxxx</ClientID>
 <ClientVersion>5.00.9040.1015</ClientVersion><NetBIOSName>TestClient</NetBIOSName>
 <CodePage>437</CodePage><SystemDefaultLCID>1033</SystemDefaultLCID>
 <Priority>1</Priority></Machine></Identification></ReportDetails></ReportHeader>
 <ReportBody><Topic ID="Super Peer is now active" Type="7201" IDType="0" User=""
 UserSID=""/><State ID="2"Criticality="0"/><StateDetails Type="1"><!
 [CDATA[<ContentList><Content id="CAS00015" version="1" Flag="0"/></ContentList>]]>
 </StateDetails><UserParameters Flags="0" Count="1"><Param>8003</Param>
 </UserParameters></StateMessage></ReportBody></Report>

When the site server receives the state message, it calls the spUpdateSuperPeerStatus stored
procedure to update the following tables:

     SuperPeers
     SuperPeerContentMap

<!-- p.110 -->

Configure boundary group options for peer
downloads
   1. In the Configuration Manager console, go to the Administration workspace, and then
     select Hierarchy Configuration > Boundary Groups.

   2. Locate the boundary group that contains the peer cache clients and peer cache sources.

   3. Right-click the boundary group, and then select Properties.

   4. Select the Options tab, and then enable the Allow peer downloads in this boundary
     group setting.

Example scenario
The following example is used to show how peer cache works during content deployment.

Deploy an application to the peer cache source
When an application is deployed and installed on the peer cache source, the Content Access
service generates a state message of topic type 7200. The following entry is logged in
StateMessage.log:

 Output

 State message(State ID : 1) with TopicType 7200 and TopicId Cache add CAS00015.1
 has been recorded for SYSTEM

<!-- p.111 -->

The state message is sent to the management point through CCMMessaging.

When the site server receives this state message, the SuperPeerContentMap table is updated.

Deploy an application to the peer cache client
The client downloads the policy for the application. For a Required deployment, the client
sends request to the management point for content locations.

The following entries are logged in LocationServices.log:

  Output

  ContentLocationRequest : <ContentLocationRequest SchemaVersion="1.00"
  BGRVersion="1" ClientInOperation="PT0M" ExcludeFileList=""><Package ID="CAS00015"
  Version="1"
  DeploymentFlags="9223372036855313105"/><AssignedSite SiteCode="P01"/>
  <ClientLocationInfo LocationType="SMSPackage" DistributeOnDemand="0" UseAzure="1"
  AllowWUMU="0" UseInternetDP="0" AllowHTTP="1" AllowSMB="1" AllowMulticast="1"
  AllowSuperPeer="1" DPTokenAuth="1"><ADSite Name="Default-First-Site-Name"/><Forest
  Name="Contoso.Com"/><Domain Name="Contoso.Com"/><IPAddresses><IPAddress
  SubnetAddress="192.X.X.X" Address="192.X.X.X"/></IPAddresses><Adapters><Adapter
  Name="Ethernet" IfType="6" PhysicalAddressExists="1" DnsSuffix="abc.com"
  Description="Network Adapter"/></Adapters><BoundaryGroups
  BoundaryGroupListRetrieveTime="2021-04-03T14:03:16.603" IsOnVPN="0"><BoundaryGroup
  GroupID="5" GroupGUID="xxxx" GroupFlag="0"/><DOINCServers><DOINCServer
  DOINCServer="P01.Contoso.Com"/></DOINCServers></BoundaryGroups>
  </ClientLocationInfo></ContentLocationRequest> LocationServices

  ７ Note

  Because the Allow peer downloads in this boundary group option is enabled in the
  boundary group, AllowSuperPeer is set to 1 in the request. Otherwise, AllowSuperPeer is
  set to 0 in the request.

  To use the peer cache source for content download, enable the Allow peer downloads in
  this boundary group option for each boundary group that contains the client.

The management point replies by returning the list of content locations. You can also find the
list in LocationServices.log:

  Output

  Calling back with the following distribution points
  Distribution

<!-- p.112 -->

 Point='https://TestClient.Contoso.Com:8003/SCCM_BranchCache$/CAS00015',
 Locality='SUBNETPEER', Version='9040', Capabilities='<Capabilities
 SchemaVersion="1.0"><Property Name="SSLState" Value="63"/></Capabilities>',
 Signature='', ForestTrust='TRUE', BlockInfo='0'
 Distribution Point='http://P01.Contoso.com/SMS_DP_SMSPKG$/CAS00015',
 Locality='SUBNET', Version='9040', Capabilities='<Capabilities SchemaVersion="1.0">
 <Property Name="SSLState" Value="0"/></Capabilities>',
 Signature='http://P01.Contoso.Com/SMS_DP_SMSSIG$/CAS00015', ForestTrust='TRUE',
 BlockInfo='0'
 Distribution Point='https://P01.Contoso.Com/CCMTOKENAUTH_SMS_DP_SMSPKG$/CAS00015',
 Locality='SUBNET', Version='9040', Capabilities='<Capabilities SchemaVersion="1.0">
 <Property Name="SSLState" Value="0"/><Property Name="AuthMethod" Value="1024"/>
 </Capabilities>',
 Signature='https://P01.Contoso.Com/CCMTOKENAUTH_SMS_DP_SMSSIG$/CAS00015',
 ForestTrust='TRUE', BlockInfo='0'

ContentTransferManager.log also shows the content locations that include the peer cache
source and distribution points:

 Output

 ContentTransferManager    4324 (0x10e4)    Persisted locations for CTM job
 {139431E9-B106-49DC-B7A8-543D55110DE6}:
 (SUBNETPEER) https://TestClient.Contoso.Com:8003/SCCM_BranchCache$/CAS00015
 (SUBNET) http://P01.Contoso.Com/SMS_DP_SMSPKG$/CAS00015
 (SUBNET) https://P01.Contoso.Com/CCMTOKENAUTH_SMS_DP_SMSPKG$/CAS00015

Peer cache clients prioritize peer cache sources to download content. This precedence is shown
in the following entry in DataTransferService.log:

 Output

  DTSJob {0C3B06F6-E85D-4C54-9B4F-0B316B33AA5B} created to download from
 'https://TestClient.Contoso.Com:8003/SCCM_BranchCache$/CAS00015' to
 'C:\windows\ccmcache\1'.

  ７ Note

        Clients can download content from only the peer cache sources that are in their
        current boundary group.
        If the client falls back to a neighbor boundary group for content, the management
        point doesn't add the peer cache sources from the neighbor boundary group to the
        list of potential content source locations.
        If a client is in more than one boundary group, enable the Allow peer download in
        this boundary group option in each boundary group. If this option is disabled in any

<!-- p.113 -->

        boundary group, the client won't use the peer cache optimization.

Last updated on 03/30/2026

<!-- p.114 -->

Source directory does not exist error when
deployment package distribution fails
This article fixes an issue in which you can't distribute deployment packages and receive the
Source directory does not exist error.

Original product version: Microsoft System Center 2012 R2 Configuration Manager
Original KB number: 3121616

Symptoms
You discover that content for System Center Endpoint Protection (SCEP) software updates has
been removed from active deployment packages. When you try to distribute these deployment
packages, the attempt fails with the following error:

  The source directory "//name/source/Updates/SCEP/bfdc178c-6e80-47cb-b698-
  b34dc39b67f4" for package "Package ID" does not exist.

Cause
This issue occurs when the update package shares the same source location with other
software update packages. When Configuration Manager performs a cleanup of orphaned
folders in this situation, it doesn't recognize that some of these folders actually belong to
another active deployment.

Resolution
To resolve this problem, re-create the package in question, and make sure that you specify a
unique source location. This will prevent content folders from being removed from deployment
packages.

 Last updated on 03/30/2026

<!-- p.115 -->

Error 80070070 during content distribution
to a CMG or cloud DP in Configuration
Manager
This article helps you fix an issue where content distribution to a cloud management gateway
(CMG) or cloud distribution point fails when the BranchCache feature is enabled.

Original product version: Configuration Manager
Original KB number: 4509484

Symptoms
When you have the BranchCache feature installed on the Configuration Manager site server,
content distribution to a CMG or cloud distribution point fails. The following error messages
are logged in PkgXferMgr.log on the site server:

  About to upload files from package source directory E:\SMSPKGSIG\C0101B18~~
  WARNING: Caught exception System.Runtime.InteropServices.COMException - There is not
  enough space on the disk. (Exception from HRESULT: 0x80070070) ~~
  Call stack:
  at
  Microsoft.ConfigurationManager.AzureRoles.ContentManager.BranchCacheContentInfoStre
  amClass.Complete()~~
  at
  Microsoft.ConfigurationManager.AzureRoles.ContentManager.ContentInfoStream.Close()~
  ~
  at
  Microsoft.ConfigurationManager.AzureRoles.ContentManager.CryptoUtilities.EncryptAndU
  ploadFileAndSaveContentInfo(String fileName, String contentInfoFullPath, CloudBlockBlob
  blob, EncryptionParams encryptionParams, IsCanceledCallback isCanceledDelegate)~~
  at
  Microsoft.ConfigurationManager.AzureRoles.ContentManager.ContentManager.RecursiveU
  pload(String packageId, ContentRouter contentRouter, CloudBlobContainer container,
  String sourceDir, String contentInfoDir, String relativeTargetPath, EncryptionParams
  encryptionParams, Int32& fileCounter)~~

<!-- p.116 -->

  at
  Microsoft.ConfigurationManager.AzureRoles.ContentManager.ContentManager.UploadCon
  tent(String packageId, String contentId, String contentSource, String contentInfoPath,
  Boolean uploadFiles, EncryptionParams encryptionParams, ContentRouter contentRouter,
  String& contentInfoFile)~~
  at
  Microsoft.ConfigurationManager.AzureRoles.ContentManager.ContentManager.UploadPac
  kageToCloudWithContentInfo(String packageId, String contentSource, String
  contentInfoPath, String cloudDP, String encryptionKey, String algName, Int32 keySize, Int32
  blockSize, String& contentInfoFile)~~

Cause
When the BranchCache feature is installed on the site server, the default cache location
( %windir%\ServiceProfiles\NetworkService\AppData\Local\PeerDistPub ) and maximum cache
size (1% of the total hard disk space) are used for the BranchCache publication cache.

This issue occurs if the BranchCache publication cache size exceeds the default maximum
cache size.

To view the publication cache size, run the following command:

 Console

 netsh branchcache show publicationcache

Resolution
To fix this issue, flush the content of the BranchCache publication cache by running the
following command on the site server:

 Console

 netsh branchcache flush

Additionally, you can change both the default cache location and maximum cache size by
running the following commands on the site server:

 Console

<!-- p.117 -->

 netsh branchcache set publicationcache directory=<New Location>
 netsh branchcache set publicationcachesize size=<New Value> percent=TRUE

For example, the following commands set the BranchCache publication cache location to
E:\BranchCache\PublicationCache and the maximum cache size to 10% of the total hard disk
space:

 Console

 netsh branchcache set publicationcache directory=E:\BranchCache\PublicationCache
 netsh branchcache set publicationcachesize size=10 percent=TRUE

  ７ Note

  BranchCache publication cache contains the metadata that's required for clients to take
  advantage of BranchCache when they download content from the distribution point. This
  metadata is generated when a content item is first downloaded from a BranchCache-
  enabled distribution point, and is required by successive clients to download the content
  item by using BranchCache. After the publication cache is flushed, the metadata is
  regenerated when the distribution point receives download requests for content items.
  Therefore, after you flush the publication cache, the first client to download a unique
  content item won't be able to use BranchCache to download the content.

Last updated on 03/30/2026

<!-- p.118 -->

Hash mismatch error when clients
download Contentinfo.tar from cloud DPs
that are assigned to multiple primary sites
This article provides the steps to solve the hash mismatch error that occurs when you try to
download the Contentinfo.tar file from the cloud distribution points (DPs).

Original product version: Configuration Manager (current branch)
Original KB number: 4458143

Symptoms
Consider the following scenario:

     You have multiple cloud DPs in Configuration Manager. Each DP is assigned to a different
     primary site.
     The DP role isn't installed on the primary site server. Or, the DP role is installed on the
     primary site server, but the Enable and configure BranchCache for this Distribution Point
     option isn't enabled.
     The BranchCache feature is installed on the primary site servers. And BranchCache is
     enabled on client computers.

In this scenario, you receive hash mismatch error when clients try to download the
Contentinfo.tar file from the cloud DPs. An error entry is logged in the
ContentTransferManager.log file:

  CCTMJob::_ProcessContentInfo - failed to verify hash (algorithm ID = 32780, provider type
  = 24). Actual value - <value1>, Computed value - <value2>

Cause
This issue occurs because the BranchCache key isn't synchronized across the primary site
servers. When Package Transfer Manager uploads the Contentinfo.tar file to the cloud DPs, the
file hash is different on each primary site because the BranchCache key is different.

Resolution

<!-- p.119 -->

To fix this issue, follow these steps:

   1. Run the following SQL query on the central administration site to get the BranchCache
      key that each primary site should use:

        SQL

        SELECT * FROM SC_Properties WHERE Name = 'BranchCacheKey'

   2. Run the following command on each primary site to set the BranchCache key to the value
      that you get in step 1:

        SQL

        netsh branchcache set key passphrase="<value>"

         ７ Note

         In this command, <value> is the result that you get in step 1.

   3. Redistribute all content to the cloud DPs so that the content is uploaded by having the
      correct hash values.

 Last updated on 03/30/2026

<!-- p.120 -->

Package distribution to a remote
distribution point fails because of a logon
failure
This article helps you work around an issue in which you can't distribute packages to a remote
distribution point (DP).

Original product version: Configuration Manager
Original KB number: 4508653

Symptoms
Consider the following scenario:

     You configure a remote content library for the site server on another server in the same
     domain, CONTOSO.COM.
     You have a remote site system server as a DP that's in an untrusted domain,
     FABRIKAM.COM.
     You select the Use another account for installing this site system option for the remote
     site system, and you specify an account that has local administrative rights on that server.

In this scenario, distributing packages to the remote DP fails, and you receive the following
error messages in the PkgXferMgr.log file on the site server:

  Date Time SMS_PACKAGE_TRANSFER_MANAGER 7280 (0x1c70) Found send request with
  ID: 26, Package: DAL0000C, Version:1, Priority: 2, Destination: DP.FABRIKAM.COM,
  DPPriority: 200
  Date Time SMS_PACKAGE_TRANSFER_MANAGER 4892 (0x131c) Sending thread starting for
  Job: 26, package: DAL0000C, Version: 1, Priority: 2, server: DP.FABRIKAM.COM, DPPriority:
  200
  Date Time SMS_PACKAGE_TRANSFER_MANAGER 4892 (0x131c) ~"FABRIKAM\
  <AccountName>" user will be used to connect to the remote DP machine
  "DP.FABRIKAM.COM"
  Date Time SMS_PACKAGE_TRANSFER_MANAGER 4892 (0x131c) Sending legacy content
  DAL0000C.1 for package DAL0000C
  Date Time SMS_PACKAGE_TRANSFER_MANAGER 4892 (0x131c)
