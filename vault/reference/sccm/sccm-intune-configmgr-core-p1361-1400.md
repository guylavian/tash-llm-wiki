---
title: "Core infrastructure documentation — pages 1361-1400"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1361-1400
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1361-1400
family: sccm
documentKind: "doc"
abstract: "Language packs in Configuration Manager Article • 10/04/2022 Applies to: Configuration Manager (current branch) This article provides technical details about language support in Configuration Manager. Configuration Manager site servers and clients are considered language-neutral"
---

# Core infrastructure documentation — pages 1361-1400

<!-- p.1361 -->

Language packs in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

This article provides technical details about language support in Configuration Manager.
Configuration Manager site servers and clients are considered language-neutral. Add
support for display languages by installing server language packs or client language
packs at a central administration site and at primary sites. You select the server and
client languages to support at a site from the available language pack files during the
site installation process.

Install multiple languages at each site. You only need to install the languages that you
use.

       Each site supports multiple languages for Configuration Manager consoles.

       Add support for only the client languages that you want to support by installing
       individual client language packs at each site.

When you install support for a language that matches the following components:

       The display language of a computer: Both the Configuration Manager console and
       the client user interface that runs on that computer display information in that
       language.

       The language preference that's in use by the web browser of a computer:
       Connections to web-based information display in that language. For example, SQL
       Server Reporting Services.

When you run Configuration Manager setup, it downloads language pack files as part of
the prerequisites and redistributable files. You can also use the setup downloader to
download these files before you run setup.

Server languages
Use the following table to map a locale ID to a language that you want to support on
servers. For more information about locale IDs, see Locale IDs assigned by Microsoft.

                                                                          ﾉ   Expand table

<!-- p.1362 -->

 Server language                       Locale ID (LCID)        Three-letter code

 English (default)                     0409                    ENU

 Chinese (Simplified)                  0804                    CHS

 Chinese (Traditional, Taiwan)         0404                    CHT

 Czech                                 0405                    CSY

 Dutch - Netherlands                   0413                    NLD

 French                                040c                    FRA

 German                                0407                    DEU

 Hungarian                             040e                    HUN

 Italian - Italy                       0410                    ITA

 Japanese                              0411                    JPN

 Korean                                0412                    KOR

 Polish                                0415                    PLK

 Portuguese - Brazil                   0416                    PTB

 Portuguese - Portugal                 0816                    PTG

 Russian                               0419                    RUS

 Spanish - Spain                       0c0a                    ESN

 Swedish                               041d                    SVE

 Turkish                               041f                    TRK

Client languages
Use the following table to map a locale ID to a language that you want to support on
client computers. For more information about locale IDs, see Locale IDs assigned by
Microsoft.

                                                                       ﾉ   Expand table

 Client language                       Locale ID (LCID)        Three-letter code

 English (default)                     0409                    ENG

<!-- p.1363 -->

 Client language                       Locale ID (LCID)        Three-letter code

 Chinese -Simplified                   0804                    CHS

 Chinese (Traditional, Taiwan)         0404                    CHT

 Czech                                 0405                    CSY

 Danish                                0406                    DAN

 Dutch - Netherlands                   0413                    NLD

 Finnish                               040b                    FIN

 French                                040c                    FRA

 German                                0407                    DEU

 Greek                                 0408                    ELL

 Hungarian                             040e                    HUN

 Italian - Italy                       0410                    ITA

 Japanese                              0411                    JPN

 Korean                                0412                    KOR

 Norwegian                             0414                    NOR

 Polish                                0415                    PLK

 Portuguese (Brazil)                   0416                    PTB

 Portuguese (Portugal)                 0816                    PTG

 Russian                               0419                    RUS

 Spanish - Spain                       0c0a                    ESN

 Swedish                               041d                    SVE

 Turkish                               041f                    TRK

Mobile device client languages
When you add support for mobile device languages, all supported mobile device client
languages are included. You can't select individual language packs for mobile device
support.

<!-- p.1364 -->

Identify installed language packs
To identify the language packs that are installed on a computer that runs the
Configuration Manager client, look for the locale ID (LCID) of the installed language
packs in the computer's registry. This information is available at the following registry
path:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CCMSetup\InstalledLangs

Customize hardware inventory to collect this information. Then build a custom report to
view the language details. For more information about collecting custom hardware
inventory, see How to configure hardware inventory. For more information, see Create
reports.

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1365 -->

About log files in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

In Configuration Manager, client and site server components record process information
in individual log files. You can use the information in these log files to help you
troubleshoot issues that might occur. By default, Configuration Manager enables
logging for client and server components.

This article provides general information about the Configuration Manager log files. It
includes tools to use, how to configure the logs, and where to find them. For more
information on specific log files, see Log files reference.

How it works
Most processes in Configuration Manager write operational information to a log file that
is dedicated to that process. The log files are identified by .log or .lo_ file extensions.
Configuration Manager writes to a .log file until that log reaches its maximum size.
When the log is full, the .log file is copied to a file of the same name but with the .lo_
extension, and the process or component continues to write to the .log file. When the
.log file again reaches its maximum size, the .lo_ file is overwritten and the process

repeats. Some components establish a log file history by appending a date and time
stamp to the log file name and by keeping the .log extension.

Log viewer tools
All Configuration Manager log files are plain text, so you can view them with any text
reader like Notepad. The logs use unique formatting that's best viewed with one of the
following specialized tools:

      CMTrace
      OneTrace
      Support Center log file viewer

CMTrace

<!-- p.1366 -->

To view the logs, use the Configuration Manager log viewer tool CMTrace. It's located in
the \SMSSetup\Tools folder of the Configuration Manager source media. The CMTrace
tool is added to all boot images that are added to the Software Library. The CMTrace log
viewing tool is automatically installed along with the Configuration Manager client. For
more information, see CMTrace.

OneTrace
OneTrace is a log viewer with Support Center. It works similarly to CMTrace, with
improvements. For more information, see Support Center OneTrace.

Support Center Log File Viewer
Support Center includes a modern log viewer. This tool replaces CMTrace and provides
a customizable interface with support for tabs and dockable windows. It has a fast
presentation layer, and can load large log files in seconds. For more information, see
Support Center Log File Viewer.

  ７ Note

  Support Center Log File Viewer and OneTrace use Windows Presentation
  Foundation (WPF). This component isn't available in Windows PE. Continue to use
  CMTrace in boot images with task sequence deployments.

Configure logging options
You can change the configuration of the log files, such as the verbose level, size, and
history. There are several ways to change these settings:

     During client installation
     Using Configuration Manager Service Manager
     Using the Windows Registry
     In the Configuration Manager console

You can also use hardware inventory to collect log settings from clients.

Configure logging options during client installation
You can set the configuration of the client log files during installation. Use the following
properties:

<!-- p.1367 -->

     CCMENABLELOGGING
     CCMDEBUGLOGGING
     CCMLOGLEVEL
     CCMLOGMAXHISTORY
     CCMLOGMAXSIZE

For more information, see Client installation properties.

Configure logging options by using Configuration
Manager Service Manager
You can change where Configuration Manager stores the log files, and their size.

To modify the size of log files, change the name and location of the log file, or to force
multiple components to write to a single log file, do the following steps:

Modify logging for a component

   1. In the Configuration Manager console, go to the Monitoring workspace, expand
     System Status, and then select either the Site Status or Component Status node.

   2. In the ribbon, select Start, and then select Configuration Manager Service
     Manager.

   3. When Configuration Manager Service Manager opens, connect to the site that you
     want to manage. If the site that you want to manage isn't shown, select Site, select
     Connect, and then enter the name of the site server for the correct site.

   4. Expand the site and go to Components or Servers, depending on where the
     components that you want to manage are located.

   5. In the right pane, select one or more components.

   6. On the Component menu, select Logging.

   7. In the Configuration Manager Component Logging dialog box, complete the
     available configuration options for your selection.

   8. Select OK to save the configuration.

Configure logging options by using the Windows
Registry

<!-- p.1368 -->

Use the Windows Registry on the servers or clients to change the following logging
options:

     Verbose level
     Maximum history
     Maximum size

When troubleshooting a problem, you can enable verbose logging for Configuration
Manager to write additional details in the log files.

  ２ Warning

  Misconfiguration of these settings can cause Configuration Manager to log large
  amounts of information, or none at all. While this data can be beneficial for
  troubleshooting, be cautious when changing these values in production sites.
  Always test these changes in a lab environment first. Excessive logging can occur,
  which might make it difficult to find relevant information in the log files.

After you make changes to these registry settings, restart the component:

     If you change the client settings, restart the SMS Agent Host service (CcmExec).
     If you change the server settings, restart the SMS Executive service.

The registry settings vary depending upon the component:

     Client and management point
     Site server
     Site system role
     Configuration Manager console

Client and management point logging options

To configure logging options for all components on a client or management point site
system, configure these REG_DWORD values under the following Windows Registry key:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CCM\Logging\@Global

                                                                                     ﾉ   Expand table

 Name              Values               Description

 LogLevel          0 : Verbose          The level of detail to write to log files.
                   1 : Default
                   2 : Warnings and

<!-- p.1369 -->

 Name             Values                    Description

                  errors
                  3 : Errors only

 LogMaxHistory    Any integer greater       When a log file reaches the maximum size, the client
                  than or equal to zero,    renames it as a backup and creates a new log file.
                  for example:              Specify how many previous versions to keep.
                    0 : No history
                    1 : Default

 LogMaxSize       Any integer greater       The maximum log file size in bytes. When a log grows
                  than or equal to          to the specified size, the client renames it as a history
                  10,000, for example:      file, and creates a new file. The default value is 250,000
                  250000                    bytes.

  ７ Note

  Don't change other values that may exist in this registry key.

For advanced debugging, you can also add this REG_SZ value under the following
Windows Registry key:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\CCM\Logging\DebugLogging

                                                                                    ﾉ   Expand table

 Name      Values                          Description

 Enabled    True : enable debug logs       Enables debug logging for troubleshooting purposes.
            False : disable debug logs

This setting causes the client to log low-level information for troubleshooting. Avoid
using this setting in production sites. Excessive logging can occur, which might make it
difficult to find relevant information in the log files. Make sure to turn off this setting
after you resolve the issue.

Site server logging options
You can configure settings globally or for a specific component on the Configuration
Manager site server.

Configure these values under the following Windows Registry key:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing

<!-- p.1370 -->

                                                                                          ﾉ   Expand table

 Name             Values                            Type              Description

 SqlEnabled       1 : enable SQL Server             REG_DWORD         Add SQL Server trace logging to
                  tracing                                             all site server logs.
                  0 : disable SQL Server
                  tracing

 ArchiveEnabled   1 : enable log archives           REG_DWORD         Archive site server logs to a
                  0 : disable log archives                            separate location for historical
                                                                      preservation.

 ArchivePath      A valid folder path, for          REG_SZ            The path to archive site server
                  example C:\Logs\Archive                             logs.

Only enable SQL Server tracing for troubleshooting purposes. Avoid using it in
production sites. Excessive logging can occur, which might make it difficult to find
relevant information in the log files. Make sure to turn off this setting after you resolve
the issue.

  ７ Note

  Don't change other values that may exist in this registry key.

To configure logging options for a specific server component, configure these
REG_DWORD values under the following Windows Registry key:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\Tracing\<ComponentName>

                                                                                          ﾉ   Expand table

 Name             Values                     Description

 LoggingLevel     0 : Verbose                The level of detail to write to log files.
                  1 : Default
                  2 : Warnings and
                  errors
                  3 : Errors only

 LogMaxHistory    Any integer greater        When a log file reaches the maximum size, the server
                  than or equal to zero,     renames it as a backup and creates a new log file.
                  for example:               Specify how many previous versions to keep.
                   0 : No history
                  1 : Default

<!-- p.1371 -->

 Name             Values                  Description

 MaxFileSize      Any integer greater     The maximum log file size in bytes. When a log grows
                  than or equal to        to the specified size, the client renames it as a history
                  10,000, for example:    file, and creates a new file. The default value is 250,000
                  250000                  bytes.

 DebugLogging     1 : enable debug logs   Enables debug logging for troubleshooting purposes.
                  0 : disable debug
                  logs

The DebugLogging setting causes the server to log low-level information for
troubleshooting. Avoid using this setting in production sites. Excessive logging can
occur, which might make it difficult to find relevant information in the log files. Make
sure to turn off this setting after you resolve the issue.

  ７ Note

  Don't change other values that may exist in this registry key.

Site system role logging options

You can configure settings globally or for a specific component on a site system that
hosts a Configuration Manager server role.

To configure logging options for a specific server component, configure these
REG_DWORD values under the following Windows Registry key:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\<ComponentName>\Logging

For example, for the distribution point role:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SMS\DP\Logging

                                                                                       ﾉ   Expand table

 Name             Values                  Description

 LogLevel         0 : Verbose             The level of detail to write to log files.
                  1 : Default
                  2 : Warnings and
                  errors
                  3 : Errors only

<!-- p.1372 -->

 Name            Values                   Description

 LogMaxHistory   Any integer greater      When a log file reaches the maximum size, the server
                 than or equal to zero,   renames it as a backup and creates a new log file.
                 for example:             Specify how many previous versions to keep.
                  0 : No history
                  1 : Default

 LogMaxSize      Any integer greater      The maximum log file size in bytes. When a log grows
                 than or equal to         to the specified size, the server renames it as a history
                 10,000, for example:     file, and creates a new file. The default value is 250,000
                 250000                   bytes.

  ７ Note

  Don't change other values that may exist in this registry key.

Configuration Manager console logging options
To change the verbose level of the AdminUI.log for the Configuration Manager console,
use the following procedure:

   1. Open the console configuration file,
     Microsoft.ConfigurationManagement.exe.config, in an XML editor like Notepad.
     The default configuration file is in the following location: C:\Program Files
     (x86)\Microsoft Endpoint

     Manager\AdminConsole\bin\Microsoft.ConfigurationManagement.exe.config

   2. Under the system.diagnostics > sources > source element, change the
     switchValue attribute from Error to Verbose . For example:

     Original: <source name="SmsAdminUISnapIn" switchValue="Error"> New: <source
     name="SmsAdminUISnapIn" switchValue="Verbose" >

   3. Save the file, and restart the console.

Configure logging options in the Configuration Manager
console
Enable or disable verbose logging on a client or collection from the console:

   1. In the Configuration Manager console, go to the Assets and Compliance
     workspace, select the Devices node, and choose a target device.

<!-- p.1373 -->

   2. In the ribbon, on the Home tab, in the Device group, select Client Diagnostics.
     Choose one of the available actions.

For more information, see Client diagnostics.

Hardware inventory for client log settings
Starting in version 2107, you can enable hardware inventory to collect client log file
settings. Enable the hardware inventory class, Client Diagnostics
(CCM_ClientDiagnostics), and then select the following attributes:

     Debug Logging Enabled
     Logging Enabled
     Log Level
     History File Count
     Max Log File Size

  ７ Note

  This inventory class isn't enabled by default.

For more information, see Enable or disable existing hardware inventory classes.

Locating log files
Configuration Manager and dependent components store log files in various locations.
These locations depend on the process that creates the log file and the configuration of
your environment.

The following locations are the defaults. If you customized the installation directories in
your environment, the actual paths may vary.

     Client: C:\Windows\CCM\logs
     Server: C:\Program Files\Microsoft Configuration Manager\Logs
     Management point: C:\SMS_CCM\Logs
     Configuration Manager console: C:\Program Files (x86)\Microsoft Endpoint
     Manager\AdminConsole\AdminUILog

     IIS: C:\inetpub\logs\logfiles\w3svc1

Task sequence log locations

<!-- p.1374 -->

The location of the task sequence log file smsts.log varies depending upon the phase of
the task sequence:

     In Windows PE before Format and Partition Disk step:
      X:\Windows\temp\smstslog\smsts.log (X is the Windows PE RAM drive)

     In Windows PE after Format and Partition Disk step: X:\smstslog\smsts.log , then
     copied to C:\_SMSTaskSequence\Logs\smstslog\smsts.log when drive is ready
     In the new Windows OS before the client is installed:
      C:\_SMSTaskSequence\Logs\smstslog\smsts.log

     In Windows after the client is installed: C:\Windows\CCM\Logs\smstslog\smsts.log
     In Windows after the task sequence completes: C:\Windows\CCM\Logs\smsts.log

   Tip

  The read-only task sequence variable _SMSTSLogPath always contains the path of
  the current log file.

Next steps
     Log files reference

     Support Center OneTrace

     Support Center log file viewer

     CMTrace

Feedback
Was this page helpful?      Yes    No

Provide product feedback

<!-- p.1375 -->

Log file reference
08/11/2025

Applies to: Configuration Manager (current branch)

In Configuration Manager, client and site server components record process information in
individual log files. You can use the information in these log files to help you troubleshoot
issues that might occur. By default, Configuration Manager enables logging for client and
server components.

For more general information about log files in Configuration Manager, see About log files.
That article includes information on the tools to use, how to configure the logs, and where to
find them.

The following sections provide details about the different log files available to you. Monitor
Configuration Manager client and server logs for operation details, and view error information
to troubleshoot problems.

     Client log files

        Client operations

        Client installation

        Client for Mac computers

     Server log files

        Site server and site systems

        Site server installation

        Data warehouse service point

        Fallback status point

        Management point

        Service connection point

        Software update point

     Log files by functionality

        Application management

        Asset Intelligence

<!-- p.1376 -->

Backup and recovery

Certificate enrollment

Client notification

Cloud management gateway

Compliance settings and company resource access

Configuration Manager console

Content management

Discovery

Endpoint analytics

Endpoint Protection

Extensions

Inventory

Migration

Mobile devices

OS deployment

Power management

Remote control

Reporting

Role-based administration

Software metering

Software updates

Wake On LAN

Windows servicing

Windows Update Agent

WSUS server

<!-- p.1377 -->

Client log files
The following sections list the log files related to client operations and client installation.

Client operations
The following table lists the log files located on the Configuration Manager client.

                                                                                         ﾉ      Expand table

 Log name                                   Description

 ADALOperationProvider.log                  Information about client authentication token requests with
                                            Azure Active Directory (Azure AD) Authentication Library
                                            (ADAL). (Replaced by CcmAad.log starting in version 2107)

 ATPHandler.log                             Records details about handling ATP Onboarding and
                                            policies.

 BitLockerManagementHandler.log             Records information about BitLocker management policies.

 CAS.log                                    The Content Access service. Maintains the local package
                                            cache on the client.

 Ccm32BitLauncher.log                       Records actions for starting applications on the client
                                            marked run as 32 bit.

 CcmEval.log                                Records Configuration Manager client status evaluation
                                            activities and details for components that are required by
                                            the Configuration Manager client.

 CcmEvalTask.log                            Records the Configuration Manager client status evaluation
                                            activities that are initiated by the evaluation scheduled task.

 CcmExec.log                                Records activities of the client and the SMS Agent Host
                                            service. This log file also includes information about
                                            enabling and disabling wake-up proxy.

 CcmMessaging.log                           Records activities related to communication between the
                                            client and management points.

 CCMNotificationAgent.log                   Records activities related to client notification operations.

 Ccmperf.log                                Records activities related to the maintenance and capture of
                                            data related to client performance counters.

 CcmRestart.log                             Records client service restart activity.

 CCMSDKProvider.log                         Records activities for the client SDK interfaces.

<!-- p.1378 -->

Log name                     Description

ccmsqlce.log                 Records activities for the built-in version of SQL Server
                             Compact Edition (CE) that the client uses. This log is
                             typically only used when you enable debug logging, or
                             there's a problem with the component. The client health
                             task (ccmeval) usually self-corrects problems with this
                             component.

CcmUsrCse.log                Records details during user sign on for folder redirection
                             policies.

CCMVDIProvider.log           Records information for clients in a virtual desktop
                             infrastructure (VDI).

CertEnrollAgent.log          Records information for Windows Hello for Business.
                             Specifically communication with the Network Device
                             Enrollment Service (NDES) for certificate requests using the
                             Simple Certificate Enrollment Protocol (SCEP).

CertificateMaintenance.log   Maintains certificates for Active Directory Domain Services
                             and management points.

CIAgent.log                  Records details about the process of remediation and
                             compliance for compliance settings, software updates, and
                             application management.

CIDownloader.log             Records details about configuration item definition
                             downloads.

CIStateStore.log             Records changes in state for configuration items, such as
                             compliance settings, software updates, and applications.

CIStore.log                  Records information about configuration items, such as
                             compliance settings, software updates, and applications.

CITaskMgr.log                Records tasks for each application and deployment type,
                             such as content download and install or uninstall actions.

ClientAuth.log               Records signing and authentication activity for the client.

ClientIDManagerStartup.log   Creates and maintains the client GUID and identifies tasks
                             during client registration and assignment.

ClientLocation.log           Records tasks that are related to client site assignment.

ClientServicing.log          Records information for client deployment state messages
                             during auto-upgrade and client piloting.

CMBITSManager.log            Records information for Background Intelligent Transfer
                             Service (BITS) jobs on the device.

<!-- p.1379 -->

Log name                     Description

CMHttpsReadiness.log         Records the results of running the Configuration Manager
                             HTTPS Readiness Assessment Tool. This tool checks whether
                             computers have a public key infrastructure (PKI) client
                             authentication certificate that can be used with
                             Configuration Manager.

CmRcService.log              Records information for the remote control service.

CoManagementHandler.log      Use to troubleshoot co-management on the client.

ComplRelayAgent.log          Records information for the co-management workload for
                             compliance policies.

ContentTransferManager.log   Schedules the Background Intelligent Transfer Service (BITS)
                             or Server Message Block (SMB) to download or access
                             packages.

DataTransferService.log      Records all BITS communication for policy or package
                             access.

DCMAgent.log                 Records high-level information about the evaluation,
                             conflict reporting, and remediation of configuration items
                             and applications.

DCMReporting.log             Records information about reporting policy platform results
                             into state messages for configuration items.

DcmWmiProvider.log           Records information about reading configuration item
                             synclets from WMI.

DeltaDownload.log            Records information about the download of express
                             updates and updates downloaded using Delivery
                             Optimization.

Diagnostics.log              Records the status of client diagnostic actions.

EndpointProtectionAgent      Records information about the installation of the System
                             Center Endpoint Protection client and the application of
                             antimalware policy to that client.

execmgr.log                  Records details about packages and task sequences that run
                             on the client.

ExpressionSolver.log         Records details about enhanced detection methods that are
                             used when verbose or debug logging is turned on.

ExternalEventAgent.log       Records the history of Endpoint Protection malware
                             detection and events related to client status.

FileBITS.log                 Records all SMB package access tasks.

<!-- p.1380 -->

Log name                     Description

FileSystemFile.log           Records the activity of the Windows Management
                             Instrumentation (WMI) provider for software inventory and
                             file collection.

FSPStateMessage.log          Records the activity for state messages that are sent to the
                             fallback status point by the client.

InternetProxy.log            Records the network proxy configuration and use activity
                             for the client.

InventoryAgent.log           Records activities of hardware inventory, software inventory,
                             and heartbeat discovery actions on the client.

InventoryProvider.log        More details about hardware inventory, software inventory,
                             and heartbeat discovery actions on the client.

LocationCache.log            Records the activity for location cache use and maintenance
                             for the client.

LocationServices.log         Records the client activity for locating management points,
                             software update points, and distribution points.

MaintenanceCoordinator.log   Records the activity for general maintenance tasks for the
                             client.

Mifprovider.log              Records the activity of the WMI provider for Management
                             Information Format (MIF) files.

mtrmgr.log                   Monitors all software metering processes.

PolicyAgent.log              Records requests for policies made by using the Data
                             Transfer Service.

PolicyAgentProvider.log      Records policy changes.

PolicyEvaluator.log          Records details about the evaluation of policies on client
                             computers, including policies from software updates.

PolicyPlatformClient.log     Records the process of remediation and compliance for all
                             providers located in \Program Files\Microsoft Policy
                             Platform, except the file provider.

PolicySdk.log                Records activities for policy system SDK interfaces.

Pwrmgmt.log                  Records information about enabling or disabling and
                             configuring the wake-up proxy client settings.

PwrProvider.log              Records the activities of the power management provider
                             (PWRInvProvider) hosted in the WMI service. On all
                             supported versions of Windows, the provider enumerates

<!-- p.1381 -->

Log name                             Description

                                     the current settings on computers during hardware
                                     inventory and applies power plan settings.

SCClient_<domain>@<username>_1.log   Records the activity in Software Center for the specified
                                     user on the client computer.

SCClient_<domain>@<username>_2.log   Records the historical activity in Software Center for the
                                     specified user on the client computer.

Scheduler.log                        Records activities of scheduled tasks for all client
                                     operations.

SCNotify_<domain>@<username>_1.log   Records the activity for notifying users about software for
                                     the specified user.

SCNotify_<domain>@<username>_1-      Records the historical information for notifying users about
<date_time>.log                      software for the specified user.

Scripts.log                          Records the activity of when Configuration Manager scripts
                                     run on the client.

SensorWmiProvider.log                Records the activity of the WMI provider for the endpoint
                                     analytics sensor.

SensorEndpoint.log                   Records the execution of endpoint analytics policy and
                                     upload of client data to the site server.

SensorManagedProvider.log            Records the gathering and processing of events and
                                     information for endpoint analytics.

setuppolicyevaluator.log             Records configuration and inventory policy creation in WMI.

SleepAgent_<domain>@SYSTEM_0.log     The main log file for wake-up proxy.

SmsClientMethodProvider.log          Records activity for sending client schedules. For example,
                                     with the Send Schedule tool or other programmatic
                                     methods.

smscliui.log                         Records use of the Configuration Manager client in Control
                                     Panel.

SrcUpdateMgr.log                     Records activity for installed Windows Installer applications
                                     that are updated with current distribution point source
                                     locations.

StateMessageProvider.log             Records information for the component that sends state
                                     messages from the client to the site.

StatusAgent.log                      Records status messages that are created by the client
                                     components.

<!-- p.1382 -->

 Log name                                         Description

 SWMTRReportGen.log                               Generates a use data report that is collected by the
                                                  metering agent. This data is logged in Mtrmgr.log.

 UserAffinity.log                                 Records details about user device affinity.

 UserAffinityProvider.log                         Technical details from the component that tracks user
                                                  device affinity.

 VirtualApp.log                                   Records information specific to the evaluation of
                                                  Application Virtualization (App-V) deployment types.

 Wedmtrace.log                                    Records operations related to write filters on Windows
                                                  Embedded clients.

 wakeprxy-install.log                             Records installation information when clients receive the
                                                  client setting option to turn on wake-up proxy.

 wakeprxy-uninstall.log                           Records information about uninstalling wake-up proxy
                                                  when clients receive the client setting option to turn off
                                                  wake-up proxy, if wake-up proxy was previously turned on.

Client installation
The following table lists the log files that contain information related to the installation of the
Configuration Manager client.

                                                                                                ﾉ   Expand table

 Log name                 Description

 ccmsetup.log             Records ccmsetup.exe tasks for client setup, client upgrade, and client removal.
                          Can be used to troubleshoot client installation problems.

 ccmsetup-                Records ccmsetup.exe tasks for client status and remediation.
 ccmeval.log

 CcmRepair.log            Records the repair activities of the client agent.

 client.msi.log           Records setup tasks done by client.msi. Can be used to troubleshoot client
                          installation or removal problems.

 ClientServicing.log      Records information for client deployment state messages during auto-upgrade
                          and client piloting.

Client for Mac computers

<!-- p.1383 -->

The Configuration Manager client for Mac computers records information in the following log
files on the Mac computer:

                                                                                          ﾉ   Expand table

 Log name               Details                                          Location

 CCMClient-             Records activities that are related to the Mac   /Library/Application
 <date_time>.log        client operations, including application         Support/Microsoft/CCM/Logs
                        management, inventory, and error logging.

 CCMAgent-              Records information that is related to client    ~/Library/Logs
 <date_time>.log        operations, including user sign in and sign
                        out operations, and Mac computer activity.

 CCMNotifications-      Records activities that are related to           ~/Library/Logs
 <date_time>.log        Configuration Manager notifications
                        displayed on the Mac computer.

 CCMPrefPane-           Records activities related to the                ~/Library/Logs
 <date_time>.log        Configuration Manager preferences dialog
                        box on the Mac computer, which includes
                        general status and error logging.

The log file SMS_DM.log on the site system server also records communication between Mac
computers and the management point that is set up for mobile devices and Mac computers.

Server log files
The following sections list log files that are on the site server or that are related to specific site
system roles.

Site server and site systems
The following table lists the log files that are on the Configuration Manager site server and site
system servers.

                                                                                          ﾉ   Expand table

 Log name                                        Description                        Computer with log
                                                                                    file

 adctrl.log                                      Records enrollment processing      Site server
                                                 activity.

<!-- p.1384 -->

Log name                       Description                           Computer with log
                                                                     file

ADForestDisc.log               Records Active Directory Forest       Site server
                               Discovery actions.

adminservice.log               Records actions for the SMS           Computer with the
                               Provider administration service       SMS Provider
                               REST API

ADService.log                  Records account creation and          Site server
                               security group details in Active
                               Directory.

adsgdis.log                    Records Active Directory Group        Site server
                               Discovery actions.

adsysdis.log                   Records Active Directory System       Site server
                               Discovery actions.

adusrdis.log                   Records Active Directory User         Site server
                               Discovery actions.

BusinessAppProcessWorker.log   Records processing for                Site server
                               Microsoft Store for Business
                               apps.

ccm.log                        Records activities for client push    Site server
                               installation.

CertMgr.log                    Records certificate activities for    Site system server
                               intrasite communication.

chmgr.log                      Records activities of the client      Site server
                               health manager.

Cidm.log                       Records changes to the client         Site server
                               settings by the Client Install Data
                               Manager (CIDM).

colleval.log                   Records details about when            Site server
                               collections are created, changed,
                               and deleted by the Collection
                               Evaluator.

compmon.log                    Records the status of                 Site system server
                               component threads monitored
                               for the site server.

compsumm.log                   Records Component Status              Site server
                               Summarizer tasks.

<!-- p.1385 -->

Log name          Description                           Computer with log
                                                        file

ComRegSetup.log   Records the initial installation of   Site system server
                  COM registration results for a
                  site server.

dataldr.log       Records information about the         Site server
                  processing of MIF files and
                  hardware inventory in the
                  Configuration Manager
                  database.

ddm.log           Records activities of the             Site server
                  discovery data manager.

despool.log       Records incoming site-to-site         Site server
                  communication transfers.

distmgr.log       Records details about package         Site server
                  creation, compression, delta
                  replication, and information
                  updates. It can also include
                  other activities from the
                  distribution manager
                  component. For example,
                  installing a distribution point,
                  connection attempts, and
                  installing components. For more
                  information on other
                  functionality that uses this log,
                  see Service connection point
                  and OS deployment.

EPCtrlMgr.log     Records information about the         Site server
                  syncing of malware threat
                  information from the Endpoint
                  Protection site system role
                  server with the Configuration
                  Manager database.

EPMgr.log         Records the status of the             Site system server
                  Endpoint Protection site system
                  role.

EPSetup.log       Provides information about the        Site system server
                  installation of the Endpoint
                  Protection site system role.

EnrollSrv.log     Records activities of the             Site system server

<!-- p.1386 -->

Log name                          Description                          Computer with log
                                                                       file

                                  enrollment service process.

EnrollWeb.log                     Records activities of the            Site system server
                                  enrollment website process.

ExternalNotificationsWorker.log   Records the queue and activities     Site server
                                  for notifications to external
                                  systems like Azure Logic Apps.

fspmgr.log                        Records activities of the fallback   Site system server
                                  status point site system role.

hman.log                          Records information about site       Site server
                                  configuration changes, and
                                  about the publishing of site
                                  information in Active Directory
                                  Domain Services.

Inboxast.log                      Records the files that are moved     Site server
                                  from the management point to
                                  the corresponding INBOXES
                                  folder on the site server.

inboxmgr.log                      Records file transfer activities     Site server
                                  between inbox folders.

inboxmon.log                      Records the processing of inbox      Site server
                                  files and performance counter
                                  updates.

invproc.log                       Records the forwarding of MIF        Site server
                                  files from a secondary site to its
                                  parent site.

migmctrl.log                      Records information for              Top-level site in the
                                  Migration actions that involve       Configuration
                                  migration jobs, shared               Manager hierarchy,
                                  distribution points, and             and each child
                                  distribution point upgrades.         primary site. In a
                                                                       multi-primary site
                                                                       hierarchy, use the log
                                                                       file that is created at
                                                                       the central
                                                                       administration site.

mpcontrol.log                     Records the registration of the      Site system server
                                  management point. Records the

<!-- p.1387 -->

Log name                  Description                          Computer with log
                                                               file

                          availability of the management
                          point every 10 minutes.

mpfdm.log                 Records the actions of the           Site system server
                          management point component
                          that moves client files to the
                          corresponding INBOXES folder
                          on the site server.

mpMSI.log                 Records details about the            Site server
                          management point installation.

MPSetup.log               Records the management point         Site server
                          installation wrapper process.

netdisc.log               Records Network Discovery            Site server
                          actions.

NotiCtrl.log              Application request notifications.   Site server

ntsvrdis.log              Records the discovery activity of    Site server
                          site system servers.

Objreplmgr                Records the processing of object     Site server
                          change notifications for
                          replication.

offermgr.log              Records advertisement updates.       Site server

offersum.log              Records the summarization of         Site server
                          deployment status messages.

OfflineServicingMgr.log   Records the activities of            Site server
                          applying updates to operating
                          system image files.

outboxmon.log             Records the processing of            Site server
                          outbox files and performance
                          counter updates.

PerfSetup.log             Records the results of the           Site system server
                          installation of performance
                          counters.

PkgXferMgr.log            Records the actions of the           Site server
                          SMS_Executive component that
                          is responsible for sending
                          content from a primary site to a
                          remote distribution point.

<!-- p.1388 -->

Log name                Description                          Computer with log
                                                             file

policypv.log            Records updates to the client        Primary site server
                        policies to reflect changes to
                        client settings or deployments.

rcmctrl.log             Records the activities of            Site server
                        database replication between
                        sites in the hierarchy.

replmgr.log             Records the replication of files     Site server
                        between the site server
                        components and the Scheduler
                        component.

ResourceExplorer.log    Records errors, warnings, and        Computer that runs
                        information about running            the Configuration
                        Resource Explorer.                   Manager console

RESTPROVIDERSetup.log   Installation of the SMS Provider     Computer with the
                        administration service REST API      SMS Provider

ruleengine.log          Records details about automatic      Site server
                        deployment rules for the
                        identification, content download,
                        and software update group and
                        deployment creation.

SCCMReporting.log       Records details about RBAC           Site system server
                        checks and resource loads when
                        reports are run.

schedule.log            Records details about site-to-       Site server
                        site job and file replication.

sender.log              Records the files that transfer by   Site server
                        file-based replication between
                        sites.

sinvproc.log            Records information about the        Site server
                        processing of software inventory
                        data to the site database.

sitecomp.log            Records details about the            Site server
                        maintenance of the installed site
                        components on all site system
                        servers in the site.

sitectrl.log            Records site setting changes         Site server
                        made to site control objects in

<!-- p.1389 -->

Log name                               Description                           Computer with log
                                                                             file

                                       the database.

sitestat.log                           Records the availability and disk     Site server
                                       space monitoring process of all
                                       site systems.

SMS_AZUREAD_DISCOVERY_AGENT.log        Log file for Microsoft Entra user     Site server
                                       and user group discovery.

SMS_BUSINESS_APP_PROCESS_MANAGER.log   Log file for component that           Site server
                                       synchronizes apps from the
                                       Microsoft Store for Business.

SMS_DataEngine.log                     Log file for management               Site server
                                       insights.

SMS_ISVUPDATES_SYNCAGENT.log           Log file for synchronization of       Top-level software
                                       third-party software updates.         update point in the
                                                                             Configuration
                                                                             Manager hierarchy.

SMS_MESSAGE_PROCESSING_ENGINE.log      Log file for the message              Site server
                                       processing engine, which the
                                       site uses to process results for
                                       client actions. For example, run
                                       scripts and CMPivot.

SMS_OrchestrationGroup.log             Log file for orchestration groups     Site server

SMS_PhasedDeployment.log               Log file for phased deployments       Top-level site in the
                                                                             Configuration
                                                                             Manager hierarchy

SMS_REST_PROVIDER.log                  Service health state for the SMS      Computer with the
                                       Provider administration service       SMS Provider
                                       REST API, including certificate
                                       information

SmsAdminUI.log                         Records Configuration Manager         Computer that runs
                                       console activity.                     the Configuration
                                                                             Manager console

smsbkup.log                            Records output from the site          Site server
                                       backup process.

smsdbmon.log                           Records database changes.             Site server

SMSENROLLSRVSetup.log                  Records the installation activities   Site system server
                                       of the enrollment web service.

<!-- p.1390 -->

 Log name                                      Description                           Computer with log
                                                                                     file

 SMSENROLLWEBSetup.log                         Records the installation activities   Site system server
                                               of the enrollment website.

 smsexec.log                                   Records the processing of all site    Site server or site
                                               server component threads.             system server

 SMSFSPSetup.log                               Records messages generated by         Site system server
                                               the installation of a fallback
                                               status point.

 SMSProv.log                                   Records WMI provider access to        Computer with the
                                               the site database.                    SMS Provider

 srsrpMSI.log                                  Records detailed results of the       Site system server
                                               reporting point installation
                                               process from the MSI output.

 srsrpsetup.log                                Records results of the reporting      Site system server
                                               point installation process.

 statesys.log                                  Records the processing of state       Site server
                                               system messages.

 statmgr.log                                   Records the writing of all status     Site server
                                               messages to the database.

 swmproc.log                                   Records the processing of             Site server
                                               metering files and settings.

Site server installation
The following table lists the log files that contain information related to site installation.

                                                                                            ﾉ   Expand table

 Log name                    Description                                                        Computer
                                                                                                with log file

 ConfigMgrPrereq.log         Records prerequisite component evaluation and                      Site server
                             installation activities.

 ConfigMgrSetup.log          Records detailed output from the site server setup.                Site Server

 ConfigMgrSetupWizard.log    Records information related to activity in the Setup Wizard.       Site Server

 SMS_BOOTSTRAP.log           Records information about the progress of launching the            Site Server
                             secondary site installation process. Details of the actual

<!-- p.1391 -->

 Log name                      Description                                                    Computer
                                                                                              with log file

                               setup process are contained in ConfigMgrSetup.log.

 smstsvc.log                   Records information about the installation, use, and           Site server
                               removal of a Windows service. Windows uses this service        and site
                               to test network connectivity and permissions between           system server
                               servers. It uses the computer account of the server that
                               creates the connection.

Data warehouse service point
The following table lists the log files that contain information related to the data warehouse
service point.

                                                                                          ﾉ    Expand table

 Log name                                    Description                                      Computer
                                                                                              with log file

 DWSSMSI.log                                 Records messages generated by the                Site system
                                             installation of a data warehouse service         server
                                             point.

 DWSSSetup.log                               Records messages generated by the                Site system
                                             installation of a data warehouse service         server
                                             point.

 Microsoft.ConfigMgrDataWarehouse.log        Records information about data                   Site system
                                             synchronization between the site database        server
                                             and the data warehouse database.

Fallback status point
The following table lists the log files that contain information related to the fallback status
point.

                                                                                          ﾉ    Expand table

 Log name      Description                                                                Computer with
                                                                                          log file

 FspIsapi      Records details about communications to the fallback status point from     Site system
               mobile device legacy clients and client computers.                         server

<!-- p.1392 -->

 Log name       Description                                                                    Computer with
                                                                                               log file

 fspMSI.log     Records messages generated by the installation of a fallback status            Site system
                point.                                                                         server

 fspmgr.log     Records activities of the fallback status point site system role.              Site system
                                                                                               server

Management point
The following table lists the log files that contain information related to the management point.

                                                                                               ﾉ    Expand table

 Log name                          Description                                                     Computer
                                                                                                   with log file

 CcmIsapi.log                      Records client messaging activity on the endpoint.              Site system
                                                                                                   server

 CCM_STS.log                       Records activities for authentication tokens, either from       Site system
                                   Microsoft Entra ID or site-issued client tokens.                server

 ClientAuth.log                    Records signing and authentication activity.                    Site system
                                                                                                   server

 MP_CliReg.log                     Records the client registration activity processed by the       Site system
                                   management point.                                               server

 MP_Ddr.log                        Records the conversion of XML.ddr records from clients,         Site system
                                   and then copies them to the site server.                        server

 MP_Framework.log                  Records the activities of the core management point and         Site system
                                   client framework components.                                    server

 MP_GetAuth.log                    Records client authorization activity.                          Site system
                                                                                                   server

 MP_GetPolicy.log                  Records policy request activity from client computers.          Site system
                                                                                                   server

 MP_Hinv.log                       Records details about the conversion of XML hardware            Site system
                                   inventory records from clients and the copy of those files      server
                                   to the site server.

 MP_Location.log                   Records location request and reply activity from clients.       Site system
                                                                                                   server

<!-- p.1393 -->

Log name                     Description                                                  Computer
                                                                                          with log file

MP_OOBMgr.log                Records the management point activities related to           Site system
                             receiving an OTP from a client.                              server

MP_Policy.log                Records policy communication.                                Site system
                                                                                          server

MP_RegistrationManager.log   Records activities related to client registration, such as   Site system
                             validating certificates, CRL, and tokens.                    server

MP_Relay.log                 Records the transfer of files that are collected from the    Site system
                             client.                                                      server

MP_RelayMsgMgr.log           Records how the management point handles incoming            Site system
                             client messages, such as for scripts or CMPivot.             server

MP_Retry.log                 Records hardware inventory retry processes.                  Site system
                                                                                          server

MP_Sinv.log                  Records details about the conversion of XML software         Site system
                             inventory records from clients and the copy of those files   server
                             to the site server.

MP_SinvCollFile.log          Records details about file collection.                       Site system
                                                                                          server

MP_Status.log                Records details about the conversion of XML.svf status       Site system
                             message files from clients and the copy of those files to    server
                             the site server.

mpcontrol.log                Records the registration of the management point.            Site server
                             Records the availability of the management point every
                             10 minutes.

mpfdm.log                    Records the actions of the management point                  Site system
                             component that moves client files to the corresponding       server
                             INBOXES folder on the site server.

mpMSI.log                    Records details about the management point                   Site server
                             installation.

MPSetup.log                  Records the management point installation wrapper            Site server
                             process.

UserService.log              Records user requests from Software Center,                  Site system
                             retrieving/installing user-available applications from the   server
                             server.

<!-- p.1394 -->

Service connection point
The following table lists the log files that contain information related to the service connection
point.

                                                                                         ﾉ   Expand table

 Log name                              Description                                Computer with log
                                                                                  file

 CertMgr.log                           Records certificate and proxy account      Site server
                                       information.

 CollectionAADGroupSyncWorker.log      Log file for synchronization of            Computer with the
                                       collection membership results to           service connection
                                       Microsoft Entra ID.                        point

 SMS_AZUREAD_DISCOVERY_AGENT.log       Starting 2303, log file for                Computer with the
                                       synchronization of collection              service connection
                                       membership results to Microsoft Entra      point
                                       ID.

 CollEval.log                          Records details about when collections     Primary site and
                                       are created, changed, and deleted by       central administration
                                       the Collection Evaluator.                  site

 Cloudusersync.log                     Records license enablement for users.      Computer with the
                                                                                  service connection
                                                                                  point

 Dataldr.log                           Records information about the              Site server
                                       processing of MIF files.

 ddm.log                               Records activities of the discovery data   Site server
                                       manager.

 Distmgr.log                           Records details about content              Top-level site server
                                       distribution requests.

 Dmpdownloader.log                     Records details about downloads from       Computer with the
                                       Microsoft, such as site updates.           service connection
                                                                                  point

 Dmpuploader.log                       Records detail related to uploading        Computer with the
                                       database changes to Microsoft.             service connection
                                                                                  point

 EndpointConnectivityCheckWorker.log   Records detail related to checks for       Computer with the
                                       important internet endpoints.              service connection
                                                                                  point

<!-- p.1395 -->

Log name                      Description                                    Computer with log
                                                                             file

hman.log                      Records information about message              Site server
                              forwarding.

WsfbSyncWorker.log            Records information about the                  Computer with the
                              communication with the Microsoft               service connection
                              Store for Business.                            point

objreplmgr.log                Records the processing of policy and           Primary site server
                              assignment.

PolicyPV.log                  Records policy generation of all               Site server
                              policies.

outgoingcontentmanager.log    Records content uploaded to                    Computer with the
                              Microsoft.                                     service connection
                                                                             point

ServiceConnectionTool.log     Records details about use of the               Same location as the
                              service connection tool based on the           tool
                              parameter you use. Each time you run
                              the tool, it replaces any existing log file.

Sitecomp.log                  Records details of service connection          Site server
                              point installation.

SmsAdminUI.log                Records Configuration Manager                  Computer that runs
                              console activity.                              the Configuration
                                                                             Manager console

SMS_CLOUDCONNECTION.log       Records information about cloud                Computer with the
                              services.                                      service connection
                                                                             point

Smsprov.log                   Records activities of the SMS Provider.        Computer with the
                              Configuration Manager console                  SMS Provider
                              activities use the SMS Provider.

SrvBoot.log                   Records details about the service              Computer with the
                              connection point installer service.            service connection
                                                                             point

Statesys.log                  Records the processing of mobile               Primary site and
                              device management messages.                    central administration
                                                                             site

UXAnalyticsUploadWorker.log   Records data upload to the service for         Computer with the
                              endpoint analytics.                            service connection
                                                                             point

<!-- p.1396 -->

Software update point
The following table lists the log files that contain information related to the software update
point.

                                                                                          ﾉ   Expand table

 Log name                          Description                     Computer with log file

 objreplmgr.log                    Records details about the       Site server
                                   replication of software
                                   updates notification files
                                   from a parent site to child
                                   sites.

 PatchDownloader.log               Records details about the       When you manually download
                                   process of downloading          updates, this file is in your %temp%
                                   software updates from the       directory on the computer where you
                                   update source to the            use the console. For automatic
                                   download destination on         deployment rules, if the Configuration
                                   the site server.                Manager client is installed on the site
                                                                   server, this file is on the site server in
                                                                   %windir%\CCM\Logs .

 ruleengine.log                    Records details about           Site server
                                   automatic deployment
                                   rules for the identification,
                                   content download, and
                                   software update group and
                                   deployment creation.

 SMS_ISVUPDATES_SYNCAGENT.log      Log file for synchronization    Top-level software update point in the
                                   of third-party software         Configuration Manager hierarchy.
                                   updates.

 SUPSetup.log                      Records details about the       Site system server
                                   software update point
                                   installation. When the
                                   software update point
                                   installation completes,
                                   Installation was successful
                                   is written to this log file.

 WCM.log                           Records details about the       Site server that connects to the WSUS
                                   software update point           server
                                   configuration and
                                   connections to the WSUS
                                   server for subscribed
                                   update categories,

<!-- p.1397 -->

 Log name                          Description                    Computer with log file

                                   classifications, and
                                   languages.

 WSUSCtrl.log                      Records details about the      Site system server
                                   configuration, database
                                   connectivity, and health of
                                   the WSUS server for the
                                   site.

 wsyncmgr.log                      Records details about the      Site system server
                                   software updates sync
                                   process.

 WUSSyncXML.log                    Records details about the      Client computer configured as the
                                   Inventory Tool for the         sync host for the Inventory Tool for
                                   Microsoft Updates sync         Microsoft Updates
                                   process.

Log files by functionality
The following sections list log files related to Configuration Manager functions.

Application management
The following table lists the log files that contain information related to application
management.

                                                                                          ﾉ    Expand table

 Log name                                     Description                                     Computer
                                                                                              with log file

 AppIntentEval.log                            Records details about the current and           Client
                                              intended state of applications, their
                                              applicability, whether requirements
                                              were met, deployment types, and
                                              dependencies.

 AppDiscovery.log                             Records details about the discovery or          Client
                                              detection of applications on client
                                              computers.

 AppEnforce.log                               Records details about enforcement               Client
                                              actions (install and uninstall) taken for
                                              applications on the client.

<!-- p.1398 -->

Log name                               Description                                 Computer
                                                                                   with log file

AppGroupHandler.log                    Records detection and enforcement           Client
                                       information for application groups

BusinessAppProcessWorker.log           Records processing for Microsoft Store      Site server
                                       for Business apps.

Ccmsdkprovider.log                     Records the activities of the application   Client
                                       management SDK.

colleval.log                           Records details about when collections      Site system
                                       are created, changed, and deleted by        server
                                       the Collection Evaluator.

WsfbSyncWorker.log                     Records information about the               Computer with
                                       communication with the Microsoft            the service
                                       Store for Business.                         connection
                                                                                   point

NotiCtrl.log                           Application request notifications.          Site server

PrestageContent.log                    Records details about the use of the        Site system
                                       ExtractContent.exe tool on a remote,        server
                                       prestaged distribution point. This tool
                                       extracts content that has been
                                       exported to a file.

SettingsAgent.log                      Enforcement of specific applications,       Client
                                       records orchestration of application
                                       group evaluation, and details of co-
                                       management policies.

SMS_BUSINESS_APP_PROCESS_MANAGER.log   Log file for component that                 Site server
                                       synchronizes apps from the Microsoft
                                       Store for Business.

SMS_CLOUDCONNECTION.log                Records information about cloud             Computer with
                                       services.                                   the service
                                                                                   connection
                                                                                   point

SMS_ImplicitUninstall.log              Records events from the implicit            Site server
                                       uninstall background worker process.

SMSdpmon.log                           Records details about the distribution      Site server
                                       point health monitoring scheduled task
                                       that is configured on a distribution
                                       point.

<!-- p.1399 -->

 Log name                                          Description                                     Computer
                                                                                                   with log file

 SoftwareCenterSystemTasks.log                     Records activities related to Software          Client
                                                   Center prerequisite component
                                                   validation.

 TSDTHandler.log                                   For the task sequence deployment                Client
                                                   type. It logs the process from app
                                                   enforcement (install or uninstall) to the
                                                   launch of the task sequence. Use it with
                                                   AppEnforce.log and smsts.log.

Packages and programs
The following table lists the log files that contain information related to deploying packages
and programs.

                                                                                               ﾉ    Expand table

 Log name       Description                                                                 Computer with
                                                                                            log file

 colleval.log   Records details about when collections are created, changed, and            Site server
                deleted by the Collection Evaluator.

 execmgr.log    Records details about packages and task sequences that run.                 Client

Asset Intelligence
The following table lists the log files that contain information related to Asset Intelligence.

                                                                                               ﾉ    Expand table

 Log Name                Description                                                           Computer
                                                                                               with log file

 AssetAdvisor.log        Records the activities of Asset Intelligence inventory actions.       Client

 aikbmgr.log             Records details about the processing of XML files from the            Site server
                         inbox for updating the Asset Intelligence catalog.

 AIUpdateSvc.log         Records the interaction of the Asset Intelligence sync point          Site system
                         with the cloud service.                                               server

 AIUSMSI.log             Records details about the installation of the Asset Intelligence      Site system

<!-- p.1400 -->

 Log Name               Description                                                         Computer
                                                                                            with log file

                        sync point site system role.                                        server

 AIUSSetup.log          Records details about the installation of the Asset Intelligence    Site system
                        sync point site system role.                                        server

 ManagedProvider.log    Records details about discovering software with an associated       Site system
                        software identification tag. Also records activities related to     server
                        hardware inventory.

 MVLSImport.log         Records details about the processing of imported licensing          Site system
                        files.                                                              server

Backup and recovery
The following table lists log files that contain information related to backup and recovery
actions, including site resets, and changes to the SMS Provider.

                                                                                           ﾉ   Expand table

 Log name              Description                                                         Computer with
                                                                                           log file

 ConfigMgrSetup.log    Records information about setup and recovery tasks when             Site server
                       Configuration Manager recovers a site from backup.

 Smsbkup.log           Records details about the site backup activity.                     Site server

 smssqlbkup.log        Records output from the site database backup process when           Site database
                       SQL Server is installed on a server that isn't the site server.     server

 Smswriter.log         Records information about the state of the Configuration            Site server
                       Manager VSS writer that is used by the backup process.

Certificate enrollment
The following table lists the Configuration Manager log files that contain information related to
certificate enrollment. Certificate enrollment uses the certificate registration point and the
Configuration Manager Policy Module on the server that's running the Network Device
Enrollment Service (NDES).

                                                                                           ﾉ   Expand table
