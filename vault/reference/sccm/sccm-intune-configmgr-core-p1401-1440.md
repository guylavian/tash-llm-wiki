---
title: "Core infrastructure documentation — pages 1401-1440"
type: reference
domain: sccm
slug: sccm-intune-configmgr-core-p1401-1440
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-core-p1401-1440
family: sccm
documentKind: "doc"
abstract: "Log name Description Computer with log file CertEnrollAgent.log Records client communication with NDES for Windows Hello for Business client certificate requests using the Simple Certificate Enrollment Protocol (SCEP). Crp.log Records enrollment activities. Certificate registrat"
---

# Core infrastructure documentation — pages 1401-1440

<!-- p.1401 -->

 Log name               Description                                         Computer with log file

 CertEnrollAgent.log    Records client communication with NDES for          Windows Hello for Business client
                        certificate requests using the Simple Certificate
                        Enrollment Protocol (SCEP).

 Crp.log                Records enrollment activities.                      Certificate registration point

 Crpctrl.log            Records the operational health of the               Certificate registration point
                        certificate registration point.

 Crpsetup.log           Records details about the installation and          Certificate registration point
                        configuration of the certificate registration
                        point.

 Crpmsi.log             Records details about the installation and          Certificate registration point
                        configuration of the certificate registration
                        point.

 NDESPlugin.log         Records challenge verification and certificate      Configuration Manager Policy
                        enrollment activities.                              Module and the Network Device
                                                                            Enrollment Service

Along with the Configuration Manager log files, review the Windows Application logs in Event
Viewer on the server running the Network Device Enrollment Service and the server hosting the
certificate registration point. For example, look for messages from the
NetworkDeviceEnrollmentService source.

You can also use the following log files:

     IIS log files for Network Device Enrollment Service:
     %SYSTEMDRIVE%\inetpub\logs\LogFiles\W3SVC1

     IIS log files for the certificate registration point:
     %SYSTEMDRIVE%\inetpub\logs\LogFiles\W3SVC1

     Network Device Enrollment Policy log file: mscep.log

           ７ Note

           This file is located in the folder for the NDES account profile, for example, in
           C:\Users\SCEPSvc. For more information about how to enable NDES logging, see the
           Enable Logging        section of the NDES wiki.

Client notification

<!-- p.1402 -->

The following table lists the log files that contain information related to client notification.

                                                                                             ﾉ     Expand table

 Log name                   Description                                                          Computer
                                                                                                 with log file

 bgbmgr.log                 Records details about site server activities related to client       Site server
                            notification tasks and processing online and task status
                            files.

 BGBServer.log              Records the activities of the notification server, such as           Management
                            client-server communication and pushing tasks to clients.            point
                            Also records information about the generation of online
                            and task status files to be sent to the site server.

 BgbSetup.log               Records the activities of the notification server installation       Management
                            wrapper process during installation and uninstallation.              point

 bgbisapiMSI.log            Records details about the notification server installation           Management
                            and uninstallation.                                                  point

 BgbHttpProxy.log           Records the activities of the notification HTTP proxy as it          Client
                            relays the messages of clients using HTTP to and from the
                            notification server.

 CcmNotificationAgent.log   Records the activities of the notification agent, such as            Client
                            client-server communication and information about tasks
                            received and dispatched to other client agents.

Cloud management gateway
The following table lists the log files that contain information related to the cloud management
gateway.

                                                                                             ﾉ     Expand table

 Log name                            Description                                      Computer with log
                                                                                      file

 CloudMgr.log                        Records details about deploying the cloud        The installdir folder on
                                     management gateway service, ongoing              the primary site server
                                     service status, and use data associated with     or CAS.
                                     the service. To configure the logging level,
                                     edit the Logging level value in the following
                                     registry key: HKLM\SOFTWARE\
                                     Microsoft\SMS\COMPONENTS\ SMS_CLOUD_
                                     SERVICES_MANAGER

<!-- p.1403 -->

 Log name                       Description                                      Computer with log
                                                                                 file

 CMGSetup.log Note 1            Records details about the second phase of the    The %approot%\logs
                                cloud management gateway deployment              on your Azure server,
                                (local deployment in Azure). To configure the    or the SMS/Logs
                                logging level, use the setting Trace level       folder on the site
                                (Information (Default), Verbose, Error) on the   system server
                                Azure portal\Cloud services configuration
                                tab.

 CMGService.log Note 1          Records details about the cloud management       The %approot%\logs
                                gateway service core component in Azure. To      on your Azure server,
                                configure the logging level, use the setting     or the SMS/Logs
                                Trace level (Information (Default), Verbose,     folder on the site
                                Error) on the Azure portal\Cloud services        system server
                                configuration tab.

 SMS_Cloud_ProxyConnector.log   Records details about setting up connections     Site system server
                                between the cloud management gateway
                                service and the cloud management gateway
                                connection point.

 CMGContentService.log Note 1   When you enable a CMG to also serve              The %approot%\logs
                                content from Azure storage, this log records     on your Azure server,
                                the details of that service.                     or the SMS/Logs
                                                                                 folder on the site
                                                                                 system server

     For troubleshooting deployments, use CloudMgr.log and CMGSetup.log
     For troubleshooting service health, use CMGService.log and
     SMS_Cloud_ProxyConnector.log.
     For troubleshooting client traffic, use CMGService.log and
     SMS_Cloud_ProxyConnector.log.

Note 1: Logs synchronized from Azure
These are local Configuration Manager log files that cloud service manager syncs from Azure
storage every five minutes. The cloud management gateway pushes logs to Azure storage
every five minutes. So the maximum delay is 10 minutes. Verbose switches affect both local and
remote logs. The actual file names include the service name and role instance identifier. For
example, CMG-ServiceName-RoleInstanceID-CMGSetup.log. These log files are synced, so you
don't need to RDP to the cloud management gateway to obtain them, and that option isn't
supported.

<!-- p.1404 -->

Compliance settings and company resource access
The following table lists the log files that contain information related to compliance settings
and company resource access.

                                                                                       ﾉ   Expand table

 Log name              Description                                                      Computer with
                                                                                        log file

 CIAgent.log           Records details about the process of remediation and             Client
                       compliance for compliance settings, software updates, and
                       application management.

 CITaskManager.log     Records information about configuration item task scheduling.    Client

 DCMAgent.log          Records high-level information about the evaluation, conflict    Client
                       reporting, and remediation of configuration items and
                       applications.

 DCMReporting.log      Records information about reporting policy platform results      Client
                       into state messages for configuration items.

 DcmWmiProvider.log    Records information about reading configuration item synclets    Client
                       from WMI.

Configuration Manager console
The following table lists the log files that contain information related to the Configuration
Manager console.

                                                                                       ﾉ   Expand table

 Log name                      Description                                   Computer with log file

 ConfigMgrAdminUISetup.log     Records the installation of the               Computer that runs the
                               Configuration Manager console.                Configuration Manager
                                                                             console

 SmsAdminUI.log                Records information about the operation of    Computer that runs the
                               the Configuration Manager console.            Configuration Manager
                                                                             console

 CMPivot.log                   Records details about each CMPivot task       Computer that runs the
                               run from the console.                         Configuration Manager
                                                                             console

<!-- p.1405 -->

 Log name                        Description                                      Computer with log file

 Smsprov.log                     Records activities of the SMS Provider.          Site server or site system
                                 Configuration Manager console activities         server
                                 use the SMS Provider.

Content management
The following table lists the log files that contain information related to content management.

                                                                                            ﾉ    Expand table

 Log name                  Description                                                  Computer with log
                                                                                        file

 CloudDP-<guid>.log        Records details for a specific cloud-based content           Site system server
                           source, including information about storage and
                           content access.

 CloudMgr.log              Records details about content provisioning, collecting       Site system server
                           storage and bandwidth statistics, and administrator-
                           initiated actions to stop or start the cloud service that
                           runs a content-enabled cloud management gateway
                           (CMG).

 DataTransferService.log   Records all BITS communication for policy or package         Computer that is
                           access. This log also is used for content management         configured as a pull-
                           by pull-distribution points.                                 distribution point

 PullDP.log                Records details about content that the pull-distribution     Computer that is
                           point transfers from source distribution points.             configured as a pull-
                                                                                        distribution point

 PrestageContent.log       Records the details about the use of the                     Site system role
                           ExtractContent.exe tool on a remote, prestaged
                           distribution point. This tool extracts content that has
                           been exported to a file.

 PkgXferMgr.log            Records the actions of the SMS_Executive component           Site server
                           that is responsible for sending content from a primary
                           site to a remote distribution point.

 SMSdpmon.log              Records details about distribution point health              Site system role
                           monitoring scheduled tasks that are configured on a
                           distribution point.

 smsdpprov.log             Records details about the extraction of compressed           Distribution point
                           files received from a primary site. This log is generated    computer that isn't
                           by the WMI provider of the remote distribution point.

<!-- p.1406 -->

 Log name                 Description                                                 Computer with log
                                                                                      file

                                                                                      colocated with the
                                                                                      site server

 smsdpusage.log           Records details about the smsdpusage.exe that runs          Site system role
                          and gathers data for the distribution point usage
                          summary report.

Discovery
The following table lists the log files that contain information related to discovery.

                                                                                          ﾉ   Expand table

 Log name             Description                                                        Computer with
                                                                                         log file

 adsgdis.log          Records Active Directory Security Group Discovery actions.         Site server

 adsysdis.log         Records Active Directory System Discovery actions.                 Site server

 adusrdis.log         Records Active Directory User Discovery actions.                   Site server

 ADForestDisc.Log     Records Active Directory Forest Discovery actions.                 Site server

 ddm.log              Records activities of the discovery data manager.                  Site server

 InventoryAgent.log   Records activities of hardware inventory, software inventory,      Client
                      and heartbeat discovery actions on the client.

 netdisc.log          Records Network Discovery actions.                                 Site server

Endpoint analytics

                                                                                          ﾉ   Expand table

 Log name                        Description                                              Computer with
                                                                                          log file

 UXAnalyticsUploadWorker.log     Records data upload to the service for endpoint          Service
                                 analytics.                                               connection point

 SensorWmiProvider.log           Records the activity of the WMI provider for the         Client
                                 endpoint analytics sensor.

<!-- p.1407 -->

 Log name                         Description                                                 Computer with
                                                                                              log file

 SensorEndpoint.log               Records the execution of endpoint analytics policy          Client
                                  and upload of client data to the site server.

 SensorManagedProvider.log        Records the gathering and processing of events and          Client
                                  information for endpoint analytics.

Endpoint Protection
The following table lists the log files that contain information related to Endpoint Protection.

                                                                                              ﾉ    Expand table

 Log name                         Description                                                     Computer
                                                                                                  with log file

 EndpointProtectionAgent.log      Records details about the installation of the Endpoint          Client
                                  Protection client and the application of antimalware
                                  policy to that client.

 EPCtrlMgr.log                    Records details about the syncing of malware threat             Site system
                                  information from the Endpoint Protection role server            server
                                  with the Configuration Manager database.

 EPMgr.log                        Monitors the status of the Endpoint Protection site             Site system
                                  system role.                                                    server

 EPSetup.log                      Provides information about the installation of the              Site system
                                  Endpoint Protection site system role.                           server

Extensions
The following table lists the log files that contain information related to extensions.

                                                                                              ﾉ    Expand table

 Log name                          Description                                         Computer with log
                                                                                       file

 AdminUI.ExtensionInstaller.log    Records information about the download of           Computer that runs the
                                   extensions from Microsoft, and the installation     Configuration Manager
                                   and uninstallation of all extensions.               console

 FeatureExtensionInstaller.log     Records information about the installation and      Computer that runs the
                                   removal of individual extensions when they're       Configuration Manager

<!-- p.1408 -->

 Log name                         Description                                       Computer with log
                                                                                    file

                                  enabled or disabled in the Configuration          console
                                  Manager console.

 SmsAdminUI.log                   Records Configuration Manager console             Computer that runs the
                                  activity.                                         Configuration Manager
                                                                                    console

Inventory
The following table lists the log files that contain information related to processing inventory
data.

                                                                                          ﾉ   Expand table

 Log name       Description                                                               Computer with
                                                                                          log file

 dataldr.log    Records information about the processing of MIF files and hardware        Site server
                inventory in the Configuration Manager database.

 invproc.log    Records the forwarding of MIF files from a secondary site to its parent   Secondary site
                site.                                                                     server

 sinvproc.log   Records information about the processing of software inventory data       Site server
                to the site database.

Metering
The following table lists the log files that contain information related to metering.

                                                                                          ﾉ   Expand table

 Log name                 Description                                                     Computer with
                                                                                          log file

 mtrmgr.log               Monitors all software metering processes.                       Client

 SWMTRReportGen.log       Generates a use data report that is collected by the            Client
                          metering agent. This data is logged in Mtrmgr.log.

 swmproc.log              Records the processing of metering files and settings.          Site server

Migration

<!-- p.1409 -->

The following table lists the log files that contain information related to migration.

                                                                                          ﾉ    Expand table

 Log name       Description                              Computer with log file

 migmctrl.log   Records information about migration      Top-level site in the Configuration Manager
                actions that involve migration jobs,     hierarchy, and each child primary site. In a multi-
                shared distribution points, and          primary site hierarchy, use the log file created at
                distribution point upgrades.             the central administration site.

Mobile devices
The following sections list the log files that contain information related to managing mobile
devices.

Enrollment

The following table lists logs that contain information related to mobile device enrollment.

                                                                                          ﾉ    Expand table

 Log name                Description                                                          Computer
                                                                                              with log file

 DMPRP.log               Records communication between management points that are             Site system
                         enabled for mobile devices and the management point                  server
                         endpoints.

 dmpmsi.log              Records the Windows Installer data for the configuration of a        Site system
                         management point that is enabled for mobile devices.                 server

 DMPSetup.log            Records the configuration of the management point when it's          Site system
                         enabled for mobile devices.                                          server

 enrollsrvMSI.log        Records the Windows Installer data for the configuration of an       Site system
                         enrollment point.                                                    server

 enrollmentweb.log       Records communication between mobile devices and the                 Site system
                         enrollment proxy point.                                              server

 enrollwebMSI.log        Records the Windows Installer data for the configuration of an       Site system
                         enrollment proxy point.                                              server

 enrollmentservice.log   Records communication between an enrollment proxy point              Site system
                         and an enrollment point.                                             server

<!-- p.1410 -->

 Log name                Description                                                             Computer
                                                                                                 with log file

 SMS_DM.log              Records communication between mobile devices, Mac                       Site system
                         computers, and the management point that is enabled for                 server
                         mobile devices and Mac computers.

Exchange Server connector
The following logs contain information related to the Exchange Server connector.

                                                                                             ﾉ    Expand table

 Log name      Description                                                           Computer with log
                                                                                     file

 easdisc.log   Records the activities and the status of the Exchange Server          Site server
               connector.

Mobile device legacy
The following table lists logs that contain information related to the mobile device legacy
client.

                                                                                             ﾉ    Expand table

 Log name                    Description                                                         Computer
                                                                                                 with log file

 DmCertEnroll.log            Records details about certificate enrollment data on mobile         Client
                             device legacy clients.

 DMCertResp.htm              Records the HTML response from the certificate server when          Client
                             the mobile device legacy client enroller program requests a
                             PKI certificate.

 DmClientHealth.log          Records the GUIDs of all mobile device legacy clients that          Site system
                             communicate with the management point that is enabled               server
                             for mobile devices.

 DmClientRegistration.log    Records registration requests and responses to and from             Site system
                             mobile device legacy clients.                                       server

 DmClientSetup.log           Records client setup data for mobile device legacy clients.         Client

 DmClientXfer.log            Records client transfer data for mobile device legacy clients       Client

<!-- p.1411 -->

 Log name                 Description                                                        Computer
                                                                                             with log file

                          and for ActiveSync deployments.

 DmCommonInstaller.log    Records client transfer file installation for configuring mobile   Client
                          device legacy client transfer files.

 DmInstaller.log          Records whether DMInstaller correctly calls DmClientSetup,         Client
                          and whether DmClientSetup exits with success or failure for
                          mobile device legacy clients.

 DmpDatastore.log         Records all the site database connections and queries made         Site system
                          by the management point that is enabled for mobile                 server
                          devices.

 DmpDiscovery.log         Records all the discovery data from the mobile device legacy       Site system
                          clients on the management point that is enabled for mobile         server
                          devices.

 DmpHardware.log          Records hardware inventory data from mobile device legacy          Site system
                          clients on the management point that is enabled for mobile         server
                          devices.

 DmpIsapi.log             Records mobile device legacy client communication with a           Site system
                          management point that is enabled for mobile devices.               server

 dmpmsi.log               Records the Windows Installer data for the configuration of        Site system
                          a management point that is enabled for mobile devices.             server

 DMPSetup.log             Records the configuration of the management point when             Site system
                          it's enabled for mobile devices.                                   server

 DmpSoftware.log          Records software distribution data from mobile device              Site system
                          legacy clients on a management point that is enabled for           server
                          mobile devices.

 DmpStatus.log            Records status messages data from mobile device clients on         Site system
                          a management point that is enabled for mobile devices.             server

 DmSvc.log                Records client communication from mobile device legacy             Client
                          clients with a management point that is enabled for mobile
                          devices.

 FspIsapi.log             Records details about communications to the fallback status        Site system
                          point from mobile device legacy clients and client                 server
                          computers.

OS deployment
The following table lists the log files that contain information related to OS deployment.

<!-- p.1412 -->

                                                                                  ﾉ   Expand table

Log name               Description                                       Computer with log file

CAS.log                Records details when distribution points are      Client
                       found for referenced content.

ccmsetup.log           Records ccmsetup tasks for client setup, client   Client
                       upgrade, and client removal. Can be used to
                       troubleshoot client installation problems.

CreateTSMedia.log      Records details for task sequence media           Computer that runs the
                       creation.                                         Configuration Manager
                                                                         console

Dism.log               Records driver installation actions or update     Site system server
                       application actions for offline servicing.

Distmgr.log            Records details about the configuration of        Site system server
                       enabling a distribution point for Preboot
                       Execution Environment (PXE).

DriverCatalog.log      Records details about device drivers that have    Site system server
                       been imported into the driver catalog.

mcsisapi.log           Records information for multicast package         Site system server
                       transfer and client request responses.

mcsexec.log            Records health check, namespace, session          Site system server
                       creation, and certificate check actions.

mcsmgr.log             Records changes to configuration, security        Site system server
                       mode, and availability.

mcsprv.log             Records multicast provider interaction with       Site system server
                       Windows Deployment Services (WDS).

MCSSetup.log           Records details about multicast server role       Site system server
                       installation.

MCSMSI.log             Records details about multicast server role       Site system server
                       installation.

Mcsperf.log            Records details about multicast performance       Site system server
                       counter updates.

MP_ClientID.log        Records management point responses to             Site system server
                       client ID requests that task sequences start
                       from PXE or boot media.

MP_DriverManager.log   Records management point responses to Auto        Site system server
                       Apply Driver task sequence action requests.

<!-- p.1413 -->

Log name                   Description                                      Computer with log file

OfflineServicingMgr.log    Records details of offline servicing schedules   Site system server
                           and update apply actions on operating system
                           Windows Imaging Format (WIM) files.

Setupact.log               Records details about Windows Sysprep and        Client
                           setup logs. For more information, see Log
                           Files.

Setupapi.log               Records details about Windows Sysprep and        Client
                           setup logs.

Setuperr.log               Records details about Windows Sysprep and        Client
                           setup logs.

smpisapi.log               Records details about the client state capture   Client
                           and restore actions, and threshold
                           information.

Smpmgr.log                 Records details about the results of state       Site system server
                           migration point health checks and
                           configuration changes.

smpmsi.log                 Records installation and configuration details   Site system server
                           about the state migration point.

smpperf.log                Records the state migration point                Site system server
                           performance counter updates.

smspxe.log                 Records details about the responses to clients   Site system server
                           that use PXE boot, and details about the
                           expansion of boot images and boot files.

smssmpsetup.log            Records installation and configuration details   Site system server
                           about the state migration point.

SMS_PhasedDeployment.log   Log file for phased deployments                  Top-level site in the
                                                                            Configuration Manager
                                                                            hierarchy

Smsts.log                  Records task sequence activities.                Client

TSAgent.log                Records the outcome of task sequence             Client
                           dependencies before starting a task sequence.

TaskSequenceProvider.log   Records details about task sequences when        Site system server
                           they're imported, exported, or edited.

loadstate.log              Records details about the User State Migration   Client
                           Tool (USMT) and restoring user state data.

<!-- p.1414 -->

 Log name                        Description                                      Computer with log file

 scanstate.log                   Records details about the User State Migration   Client
                                 Tool (USMT) and capturing user state data.

Power management
The following table lists the log files that contain information related to power management.

                                                                                           ﾉ    Expand table

 Log name        Description                                                                   Computer
                                                                                               with log file

 pwrmgmt.log     Records details about power management activities on the client               Client
                 computer, including monitoring and the enforcement of settings by the
                 Power Management Client Agent.

Remote control
The following table lists the log files that contain information related to remote control.

                                                                                           ﾉ    Expand table

 Log name          Description                               Computer with log file

 CMRcViewer.log    Records details about the activity of     On the computer that runs the remote
                   the remote control viewer.                control viewer, in the %temp% folder.

Reporting
The following table lists the Configuration Manager log files that contain information related to
reporting.

                                                                                           ﾉ    Expand table

 Log name             Description                                                          Computer with
                                                                                           log file

 srsrp.log            Records information about the activity and status of the             Site system server
                      reporting services point.

 srsrpMSI.log         Records detailed results of the reporting services point             Site system server
                      installation process from the MSI output.

<!-- p.1415 -->

 Log name                Description                                                           Computer with
                                                                                               log file

 srsrpsetup.log          Records results of the reporting services point installation          Site system server
                         process.

 SCCMReporting.log       Records details about RBAC checks and resource loads when             Site system server
                         reports are run.

Role-based administration
The following table lists the log files that contain information related to managing role-based
administration.

                                                                                                ﾉ   Expand table

 Log name         Description                                                                Computer with log
                                                                                             file

 hman.log         Records information about site configuration changes and the               Site server
                  publishing of site information to Active Directory Domain Services.

 SMSProv.log      Records WMI provider access to the site database.                          Computer with the
                                                                                             SMS Provider

Software metering
The following table lists the log files that contain information related to software metering.

                                                                                                ﾉ   Expand table

 Log name           Description                                                Computer with log file

 mtrmgr.log         Monitors all software metering processes.                  Site server

Software updates
The following table lists the log files that contain information related to software updates.

                                                                                                ﾉ   Expand table

<!-- p.1416 -->

Log name                Description                         Computer with log file

AlternateHandler.log    Records details when the client     Client
                        calls the Office click-to-run
                        COM interface to download
                        and install Microsoft 365 Apps
                        for enterprise client updates.
                        It's similar to use of
                        WuaHandler when it calls the
                        Windows Update Agent API to
                        download and install Windows
                        updates.

ccmperf.log             Records activities related to the   Client
                        maintenance and capture of
                        data related to client
                        performance counters.

DeltaDownload.log       Records information about the       Client
                        download of express updates
                        and updates downloaded
                        using Delivery Optimization.

PatchDownloader.log     Records details about the           When downloading updates
                        process of downloading              manually, this log file is located in
                        software updates from the           the %temp% directory of the user
                        update source to the download       running the console on the
                        destination on the site server.     machine you're running the
                                                            console. For Automatic
                                                            Deployment Rules, this log file is
                                                            located on the site server in
                                                            %windir%\CCM\Logs, if the
                                                            ConfigMgr client is installed on
                                                            the site server.

PolicyEvaluator.log     Records details about the           Client
                        evaluation of policies on client
                        computers, including policies
                        from software updates.

RebootCoordinator.log   Records details about the           Client
                        coordination of system restarts
                        on client computers after
                        software update installations.

ScanAgent.log           Records details about scan          Client
                        requests for software updates,
                        the WSUS location, and related
                        actions.

<!-- p.1417 -->

Log name                       Description                         Computer with log file

SdmAgent.log                   Records details about the           Client
                               tracking of remediation and
                               compliance. However, the
                               software updates log file,
                               Updateshandler.log, provides
                               more informative details about
                               installing the software updates
                               that are required for
                               compliance. This log file is
                               shared with compliance
                               settings.

ServiceWindowManager.log       Records details about the           Client
                               evaluation of maintenance
                               windows.

SMS_ISVUPDATES_SYNCAGENT.log   Log file for synchronization of     Top-level software update point in
                               third-party software updates.       the Configuration Manager
                                                                   hierarchy.

SMS_OrchestrationGroup.log     Log file for orchestration          Site server
                               groups

SmsWusHandler.log              Records details about the scan      Client
                               process for the Inventory Tool
                               for Microsoft Updates.

StateMessage.log               Records details about software      Client
                               update state messages that are
                               created and sent to the
                               management point.

SUPSetup.log                   Records details about the           Site system server
                               software update point
                               installation. When the software
                               update point installation
                               completes, Installation was
                               successful is written to this log
                               file.

UpdatesDeployment.log          Records details about               Client
                               deployments on the client,
                               including software update
                               activation, evaluation, and
                               enforcement. Verbose logging
                               shows additional information
                               about the interaction with the
                               client user interface.

<!-- p.1418 -->

 Log name                          Description                        Computer with log file

 UpdatesHandler.log                Records details about software     Client
                                   update compliance scanning
                                   and about the download and
                                   installation of software updates
                                   on the client.

 UpdatesStore.log                  Records details about              Client
                                   compliance status for the
                                   software updates that were
                                   assessed during the
                                   compliance scan cycle.

 WCM.log                           Records details about software     Site server
                                   update point configurations
                                   and connections to the WSUS
                                   server for subscribed update
                                   categories, classifications, and
                                   languages.

 WSUSCtrl.log                      Records details about the          Site system server
                                   configuration, database
                                   connectivity, and health of the
                                   WSUS server for the site.

 wsyncmgr.log                      Records details about the          Site server
                                   software update sync process.

 WUAHandler.log                    Records details about the          Client
                                   Windows Update Agent on the
                                   client when it searches for
                                   software updates.

Wake On LAN
The following table lists the log files that contain information related to using Wake On LAN.

  ７ Note

  When you supplement Wake On LAN by using wake-up proxy, this activity is logged on
  the client. For example, see CcmExec.log and SleepAgent_<domain>@SYSTEM_0.log in
  the Client operations section of this article.

                                                                                      ﾉ    Expand table

<!-- p.1419 -->

 Log name       Description                                                                   Computer with
                                                                                              log file

 wolcmgr.log    Records details about which clients need to be sent wake-up packets,          Site server
                the number of wake-up packets sent, and the number of wake-up
                packets retried.

 wolmgr.log     Records details about wake-up procedures, such as when to wake up             Site server
                deployments that are configured for Wake On LAN.

Windows servicing
The following table lists the log files that contain information related to Windows servicing.
Servicing uses the same infrastructure and process as software updates. For other logs
applicable to the servicing scenario, see Software updates.

                                                                                          ﾉ     Expand table

 Log name       Description                                                                     Computer
                                                                                                with log file

 CBS.log        Records servicing failures related to changes for Windows Updates or            Client
                roles and features.

 DISM.log       Records all actions using DISM. If necessary, DISM.log will point to            Client
                CBS.log for more details.

 setupact.log   Primary log file for most errors that occur during the Windows installation     Client
                process. The log file is located in the
                %windir%$Windows.~BT\sources\panther folder.

For more information, see Online Servicing-Related Log Files.

Windows Update Agent
The following table lists the log files that contain information related to the Windows Update
Agent.

                                                                                          ﾉ     Expand table

 Log name               Description                                                             Computer
                                                                                                with log file

 WindowsUpdate.log      Records details about when the Windows Update Agent connects            Client
                        to the WSUS server and retrieves the software updates for

<!-- p.1420 -->

 Log name              Description                                                           Computer
                                                                                             with log file

                       compliance assessment, and whether there are updates to the
                       agent components.

For more information, see Windows Update log files.

WSUS server
The following table lists the log files that contain information related to the WSUS server.

                                                                                         ﾉ   Expand table

 Log name                   Description                                                  Computer with
                                                                                         log file

 Change.log                 Records details about WSUS server database information       WSUS server
                            that has changed.

 SoftwareDistribution.log   Records details about the software updates that are synced   WSUS server
                            from the configured update source to the WSUS server
                            database.

These log files are located in the %ProgramFiles%\Update Services\LogFiles folder.

See also
     About log files

     Support Center OneTrace

     Support Center log file viewer

     CMTrace

<!-- p.1421 -->

Release notes for Configuration Manager
Article • 04/24/2025

Applies to: Configuration Manager (current branch)

With Configuration Manager, product release notes are limited to urgent issues. These issues
aren't yet fixed in the product, or detailed in a troubleshooting article.

Feature-specific documentation includes information about known issues that affect core
scenarios.

This article contains release notes for the current branch of Configuration Manager. For
information on the technical preview branch, see Technical Preview.

For information about the new features introduced with different versions, see the following
articles:

      What's new in version 2503
      What's new in version 2409
      What's new in version 2403

   Tip

  You can use RSS to be notified when this page is updated. For more information, see How
  to use the docs.

Client management

Clients aren't able download content from CMG when branch
cache is enabled
Applies to: version 2403

After Branch Cache is enabled on primary sites, clients are unable to download apps and
packages from the cloud management gateway (CMG). They typically manage to download
only 20-30% of the content before the process gets stuck. In some cases, after downloading
certain blocks of packages from the CMG, clients look for Branch Cache to retrieve the
remaining content. However, none of the clients are able to download the complete content
from the CMG, which prevents others from using Branch Cache to access it. The CTM.log on
the client includes entries similar to the following:

<!-- p.1422 -->

  log

  (CTM.log - CTMJob({63B4C4CE-2DC4-4062-93C7-E5019B3B6CE1}): CCTMJob::Start -
  State=DownloadingContentFromPeers)
  CTM.log _- CTMJob({D21758B0-D895-474E-9695-1023A25A1770}):
  CCTMJob::_PerformDownloadWithOutBranchCache - Download failure using branchcache,
  fallback to regular download

To work around this issue, disable branch cache.

  ７ Note

  Clients are able to download content from the on-premises distribution point when
  Branch Cache is enabled.

Endpoint Protection

Security configurations removed from Intune
Applies to: version 2309 with KB25858444 and later

Microsoft Defender security configurations are no longer managed with Microsoft Intune after
updating to Configuration Manager version 2403, or installing the Update Rollup for 2309.

The symptom is seen as a drop in the Microsoft Security Score values when viewed in Intune.
This issue happens because security policy configuration data is incorrectly removed from
clients after Configuration Manager clients are upgraded.

An updated version of the Microsoft Security Client Policy Configuration Tool,
ConfigSecurityPolicy.exe, is available to resolve the Endpoint Protection policy issue described
in this note.

The updated tool, version 4.18.24040.4, is distributed with the April 2024 monthly Microsoft
Defender platform update. At the time of this writing, the platform update is in the process of
global distribution, and should be broadly available in all regions by May 17, 2024.
Once the platform update is installed on affected clients, Endpoint Protection policies are
reapplied from Intune within 8 hours. The "Manage Endpoint Protection client on client
computers" setting in Configuration Manager can be changed back to "Yes" as required.

Additional references

        Monthly platform and engine versions

<!-- p.1423 -->

        Microsoft Defender update for Windows operating system installation images       .
        Sync devices to get the latest policies and actions with Intune

Set up and upgrade

ODBC driver check
Applies to: version 2503 and later

During site installation, the prerequisite checker looks for the minimum required version of the
Microsoft ODBC driver. If the correct driver isn't detected the following message is recorded:

  text

  [Failed]: Install the Microsoft ODBC driver 18 for SQL setup from
  https://go.microsoft.com/fwlink/?linkid=2220989.

The link provided installs an older version of the ODBC driver; the correct link to use is:
https://go.microsoft.com/fwlink/?linkid=2299909

Version 2107 update fails to download
Applies to: version 2107 and later

The update for Configuration Manager version 2107 is available to download, but it fails to
download. The dmpdownloader.log on the service connection point has entries similar to the
following:

  log

  Download large file with BITs
  WARNING: EasySetupDownloadSinglePackage Failed with exception: The remote name
  could not be resolved: 'configmgrbits.azureedge.net'
  WARNING: Retry in the next polling cycle

This failure happens because the service connection point can't communicate with the required
internet endpoint, configmgrbits.azureedge.net . Confirm that the site system that hosts the
service connection point role can communicate with this internet endpoint. It was already
required, but its use is expanded in version 2107. The site system can't download version 2107
or later unless your network allows traffic to this URL.

For more information, see internet access requirements for the service connection point.

<!-- p.1424 -->

OS deployment

PXE Responder isn't installed correctly after upgrading to
2403 in untrusted domain
Applies to: version 2403

After upgrading to 2403, site servers serving as a PXE responder might see failures due to
incorrect configuration of the registry keys. We can observe the below failures in distmgr.log
indicating that the registry keys weren't configured correctly.

  log

  Failed to get OS platform for server DP2.CONTOSO2.COM.Either a permissions issue
  or the server is not supported OS SMS_DISTRIBUTION_MANAGER
  CDistributionManager::SetDpRegistry failed; 0x80070005 SMS_DISTRIBUTION_MANAGER

This happened due to currently unexplained failures in platform architecture identification that
were introduced during the addition of support for arm64 machines to serve as remote
distribution points.

Software updates

Reset default value of superseding age in months for software
updates
Applies to: version 2303

Removing SUP role in Admin Console doesn't reset the superseding age property in WMI. As a
result, while reconfiguring the role, the previously configured value is shown in the
configuration window. This property needs to be reset to default value on role removal. For
more information, see supersedence rules for installing a software update point.

Security roles are missing for phased deployments
The OS Deployment Manager built-in security role has permissions to phased deployments.
The following roles are missing these permissions:

        Application Administrator
        Application Deployment Manager
        Software Update Manager

<!-- p.1425 -->

The App Author role can appear to have some permissions to phased deployments, but can't
create deployments.

A user with one these roles can start the Create Phased Deployment wizard, and can see
phased deployments for an application or software update. They can't complete the wizard, or
make any changes to an existing deployment.

To work around this issue, create a custom security role. Copy an existing security role, and add
the following permissions on the Phased Deployment object class:

     Create
     Delete
     Modify
     Read

For more information, see Create custom security roles

Configuration Manager console

Intune RBAC for tenant attached devices
Applies to: version 2207

[Updated]: There's a checkbox for a role-based access control (RBAC) setting in the cloud
attach configuration wizard in the console. By default, Configuration Manager RBAC is enforced
along with Intune RBAC when you're uploading your Configuration Manager devices to the
cloud service. This checkbox is selected by default.

You can now configure Intune role-based access control (RBAC) when interacting with tenant
attached devices from the Microsoft Intune admin center. For more information, see Intune
role-based access control for tenant-attached clients.

Unable to open console because extension installation loops
Applies to: version 2111

In certain circumstances, you're unable to open the console due to an extension installation
loop. This issue occurs when two or more versions of a single extension were marked as
required for installation. This issue occurs for extensions imported through the wizard, from a
PowerShell script, or through Community hub. If you use the Make optional setting before
importing a new version of the extension, this issue doesn't occur.

<!-- p.1426 -->

When you encounter this issue, it initially appears as a normal console extension installation.
After the extension finishes installing, you select Close to restart the Configuration Manager
console. When the console restarts, you're prompted to install the console extension again. The
extension installation continues to loop and the Configuration Manager console doesn't fully
open.

To both prevent and work around this issue, run the following SQL script on your CAS database
and all of your primary site databases:

  SQL

  ALTER VIEW vSMS_ConsoleExtensionMetadata
  AS
      WITH m AS(
         SELECT *,
             RN = ROW_NUMBER()OVER(PARTITION BY ID ORDER BY Version DESC)
         FROM ConsoleExtensionMetadata
      )
      SELECT
          m.ID,
          m.Name,
          m.Description,
          m.Author,
          m.Version,
          m.IsEnabled,
          m.IsApproved,
          m.CreatedTime,
          m.CreatedBy,
          m.UpdateTime,
          m.IsTombstoned,
          m.IsRequired,
          m.IsSigned,
          m.IsUnsignedAllowed,
          CASE m.IsRequired
              WHEN 0 THEN ''
              ELSE
              (
                  SELECT top(1) author FROM ConsoleExtensionRevisionHistory h
                  WHERE m.ID=h.ExtensionId AND m.Version=h.Version AND h.Changes &
  1=1
                  ORDER BY h.RevisionTime DESC
              )
          END AS RequiredBy,
          m.IsSetupDefined
      FROM m
      WHERE RN = 1
  GO

Boundaries and Boundary groups

<!-- p.1427 -->

Clients not belonging to any boundary group can fail to
download due to SQL issue
Applies to: version 2303, 2309 RTM

Consider ConfigMgr hierarchy with a remote MP and CMG and you deploy an app to a device
collection. The Clients can't download app, and reflect the following SQL permissions issue in
MP_Location.log.

  log

     The SELECT permission was denied on the object 'vSMS_DefaultBoundaryGroup',
  database 'CM_xxx', schema 'dbo'.

To work around the issue run the following SQL script on the SQL database on the primary sites
where the MP reports.

  SQL

        GRANT SELECT ON vSMS_DefaultBoundaryGroup To smsdbrole_MP

<!-- p.1428 -->

State messages in Configuration
Manager
Article • 10/04/2022

Applies to: Configuration Manager (current branch)

State messages contain concise information about conditions on the Configuration
Manager client. The state messaging system is used by specific components of
Configuration Manager, such as software updates and configuration settings.

Configuration Manager clients send state messages to the fallback status point or the
management point to report the current state of operations. You can create reports to
view state messages sent by clients.

Each Configuration Manager feature that uses state messages is identified by the topic
type of the state message. The state message topic types listed in this article can be
used to define the Configuration Manager feature that a state message relates to.

     ７ Note

     A state message ID value of zero ( 0 ) typically indicates that the topic type is in an
     unknown state.

Software updates

300 STATE_TOPICTYPE_SUM_ASSIGNMENT_COMPLIANCE

                                                                               ﾉ   Expand table

 State message ID                         State message description

 1                                        Compliant

 2                                        Non-compliant

301
STATE_TOPICTYPE_SUM_ASSIGNMENT_ENFORCEMENT

<!-- p.1429 -->

                                                                      ﾉ   Expand table

State message ID   State message description

1                  Installing updates

2                  Waiting for restart

3                  Waiting for another installation to complete

4                  Successfully installed updates

5                  Pending system restart

6                  Failed to install the updates

7                  Downloading the updates

8                  Downloaded updates

9                  Failed to download updates

10                 Waiting for the maintenance window before installing

11                 Waiting for orchestration

12                 Waiting for superseding update

302 STATE_TOPICTYPE_SUM_ASSIGNMENT_EVALUATION

                                                                      ﾉ   Expand table

State message ID                 State message description

1                                Evaluation activated

2                                Evaluation succeeded

3                                Evaluation failed

400 STATE_TOPICTYPE_SUM_CI_DETECTION

                                                                      ﾉ   Expand table

State message ID                 State message description

1                                Not required

<!-- p.1430 -->

State message ID                 State message description

2                                Not detected

3                                Detected

401 STATE_TOPICTYPE_SUM_CI_COMPLIANCE

                                                                      ﾉ   Expand table

State message ID                 State message description

1                                Compliant

2                                Non-compliant

3                                Conflict detected

4                                Error

5                                Unknown

6                                Partial compliance

7                                Compliance not configured

402 STATE_TOPICTYPE_SUM_CI_ENFORCEMENT

                                                                      ﾉ   Expand table

State message ID   State message description

1                  Enforcement started

2                  Enforcement waiting for content

3                  Waiting for another installation to complete

4                  Waiting for the maintenance window before installing

5                  Restart required before installing

6                  General failure

7                  Pending installation

8                  Installing update

9                  Pending system restart

<!-- p.1431 -->

 State message ID        State message description

 10                      Successfully installed update

 11                      Failed to install the update

 12                      Downloading update

 13                      Downloaded update

 14                      Failed to download the update

500 STATE_TOPICTYPE_SUM_UPDATE_DETECTION

                                                                     ﾉ   Expand table

 State message ID                      State message description

 1                                     Update isn't required

 2                                     Update is required

 3                                     Update is installed

501 STATE_TOPICTYPE_SUM_UPDATE_SOURCE_SCAN

                                                                     ﾉ   Expand table

 State message ID                      State message description

 1                                     Scan is waiting for content

 2                                     Scan is running

 3                                     Scan complete

 4                                     Scan is pending retry

 5                                     Scan failed

 6                                     Scan completed with errors

Client deployment
The following topic types have no state IDs:

<!-- p.1432 -->

                                                                            ﾉ   Expand table

Topic type        Description

700               STATE_TOPICTYPE_RESYNC_STATE_MSG

701               STATE_TOPICTYPE_SYSTEM_HEARTBEAT

702               STATE_TOPICTYPE_CKD_UPDATE

801               STATE_TOPICTYPE_DEVICE_CLIENT_DEPLOYMENT

800 STATE_TOPICTYPE_CLIENT_DEPLOYMENT

                                                                            ﾉ   Expand table

State message   State message description
ID

100             Client deployment started

101             Waiting for download

102             Deployment Scheduled

103             Waiting for the window before deploying

104             Deployment skipped

301             Unknown client deployment failure

302             Failed to create the ccmsetup service

303             Failed to delete the ccmsetup service

304             Can't install over embedded OS with File-Based Write Filter (FBWF) enabled on
                the system drive

305             Native security mode isn't valid on Windows 2000

306             Failed to start ccmsetup download process

307             Non-valid ccmsetup command line

308             Failed to download the file over WINHTTP at address

309             Failed to download the files through BITS at address

310             Failed to install BITS version

311             Can't verify that prerequisite file is MS signed

<!-- p.1433 -->

State message   State message description
ID

312             Failed to copy the file because the disk is full

313             Client.msi installation failed with MSI error

314             Failed to load ccmsetup.xml manifest file

315             Failed to obtain a client certificate

316             Prerequisite file isn't MS signed

317             Reboot required to continue the installation

318             Can't install the client on the MP because the MP and client versions do not
                match

319             Operating system or service pack not supported

320             Deployment not supported

321             Bits Missing

322             Source folder is unavailable

323             App-V not supported

324             Incorrect Site Version

325             Prerequisite hash mismatch

326             MDM Deregistration Failed

327             MDM Registration Detected

328             Intune Detected

329             Metered Network Disallowed

400             Client deployment succeeded

401             Deployment Succeeded Reboot Required

402             Deployment Succeeded Reboot Succeeded

500             Client assignment started

601             Unknown client assignment failure

602             The following site code is invalid

603             Failed to assign to MP

<!-- p.1434 -->

State message      State message description
ID

604                Failed to discover default management point

605                Failed to download site signing certificate

606                Failed to auto discover site code

607                Site assignment failed; client version higher than site version

608                Failed to get Site Version from Active Directory Domain Services and SLP

609                Failed to get client version

700                Client assignment succeeded

810 STATE_TOPICTYPE_CLIENT_COMANAGEMENT

                                                                                     ﾉ   Expand table

State message ID                State message description

100                             Enrollment status

101                             Enrollment scheduled

102                             Enrollment canceled

105                             Enrollment started

106                             Enrollment succeeded but isn't provisioned

107                             Enrollment succeeded and is provisioned

108                             Enrollment no active user

110                             Enrollment failed

820 STATE_TOPICTYPE_CLIENT_WUFB

                                                                                     ﾉ   Expand table

State message ID                State message description

1                               Windows Update for Business client status

<!-- p.1435 -->

Content
The following topic types have no state IDs:

                                                                                    ﾉ   Expand table

 Topic type         Description

 901                STATE_TOPICTYPE_REMOTE_DP_MONITORING

 902                STATE_TOPICTYPE_PULL_DP_MONITORING

 903                STATE_TOPICTYPE_DP_USAGE

900 STATE_TOPICTYPE_BRANCH_DP

                                                                                    ﾉ   Expand table

 State message ID                       State message description

 1                                      Disk Space

Client operations

1000 STATE_TOPICTYPE_CLIENT_FRAMEWORK_COMM

                                                                                    ﾉ   Expand table

 State message ID     State message description

 1                    Client is successfully communicating with the management point

 2                    Client failed to communicate with the management point

1001 STATE_TOPICTYPE_CLIENT_FRAMEWORK_LOCAL

                                                                                    ﾉ   Expand table

 State message ID   State message description

 1                  Client successfully retrieved the certificate from the local certificate store

 2                  Client failed to retrieve the certificate from the local certificate store

<!-- p.1436 -->

1100
STATE_TOPICTYPE_CLIENT_FRAMEWORK_MODEREADINESS

                                                                      ﾉ   Expand table

 State message ID                 State message description

 1                                Client not ready for native mode

 2                                Client ready for native mode

1300 STATE_TOPICTYPE_CLIENT_HEALTH

                                                                      ﾉ   Expand table

 State message ID                    State message description

 1                                   Success

 2                                   Not successful

Legacy device client
The following topic types have no state IDs:

                                                                      ﾉ   Expand table

 Topic type     Description

 1002           STATE_TOPICTYPE_DEVICE_CLIENT_FRAMEWORK_COMM

 1003           STATE_TOPICTYPE_DEVICE_CLIENT_FRAMEWORK_LOCAL

 1004           STATE_TOPICTYPE_DEVICE_CLIENT_FRAMEWORK_CERTIFICATE

 1005           STATE_TOPICTYPE_DEVICE_CLIENT_WIPE

 1006           STATE_TOPICTYPE_DEVICE_CLIENT_RETIRE

 1007           STATE_TOPICTYPE_DEVICE_CLIENT_WIPE_INTUNE

 1008           STATE_TOPICTYPE_DEVICE_CLIENT_RETIRE_INTUNE

 1009           STATE_TOPICTYPE_DEVICE_CLIENT_DEVICELOCK

 1010           STATE_TOPICTYPE_DEVICE_CLIENT_DEVICELOCK_INTUNE

<!-- p.1437 -->

 Topic type     Description

 1011           STATE_TOPICTYPE_DEVICE_CLIENT_DEVICEPINRESET

 1012           STATE_TOPICTYPE_DEVICE_CLIENT_DEVICEPINRESET_INTUNE

 1013           STATE_TOPICTYPE_DEVICE_CLIENT_DEVICEPINRESET_ONPREM

 1014           STATE_TOPICTYPE_DEVICE_CLIENT_DEVICEALBYPASS

 1015           STATE_TOPICTYPE_DEVICE_CLIENT_DEVICEALBYPASS_INTUNE

Miscellaneous
The following topic types have no state IDs:

                                                                      ﾉ   Expand table

 Topic type              Description

 1401                    STATE_TOPICTYPE_STATE_REPORT

 1500                    STATE_TOPICTYPE_CAL_TRACK_UT

 1502                    STATE_TOPICTYPE_CAL_TRACK_MT

 1503                    STATE_TOPICTYPE_CAL_TRACK_ML

1600 STATE_TOPICTYPE_USER_AFFINITY

                                                                      ﾉ   Expand table

 State message ID                      State message description

 1                                     User affinity set

 2                                     User affinity removed

1660 STATE_TOPICTYPE_SENSOR_STATUS

                                                                      ﾉ   Expand table

 State message ID                      State message description

 1                                     Sensor off

<!-- p.1438 -->

 State message ID                        State message description

 2                                       Sensor on

Applications
The following topic types have no state IDs:

                                                                             ﾉ   Expand table

 Topic type         Description

 1700               STATE_TOPICTYPE_APP_CI_SCAN

 1701               STATE_TOPICTYPE_APP_CI_COMPLIANCE

 1703               STATE_TOPICTYPE_APP_CI_ASSIGNMENT_EVALUATION

 1704               STATE_TOPICTYPE_APP_CI_LAUNCH

1702 STATE_TOPICTYPE_APP_CI_ENFORCEMENT

                                                                             ﾉ   Expand table

 State message ID       State message description

 1000                   Configuration item succeeded

 1001                   Configuration item succeeded already installed

 1002                   Configuration item succeeded preflight

 1003                   Configuration item fast status succeeded

 2000                   Configuration item in progress

 2001                   Configuration item in progress waiting for content

 2002                   Configuration item in progress installing

 2003                   Configuration item in progress waiting reboot

 2004                   Configuration item in progress waiting for maintenance window

 2005                   Configuration item in progress waiting schedule

 2006                   Configuration item in progress downloading dependent content

<!-- p.1439 -->

State message ID   State message description

2007               Configuration item in progress installing dependencies

2008               Configuration item in progress pending reboot

2009               Configuration item in progress content downloaded

2010               Configuration item in progress pending update

2011               Configuration item in progress waiting user reconnect

2012               Configuration item in progress waiting for user sign-out

2013               Configuration item in progress waiting for user sign-in

2014               Configuration item in progress waiting for install

2015               Configuration item in progress waiting for retry

2016               Configuration item in progress waiting for presentation mode

2017               Configuration item in progress waiting for orchestration

2018               Configuration item in progress waiting for network

2019               Configuration item in progress pending update VE

2020               Configuration item in progress updating VE

3000               Configuration item requirements not met

3001               Configuration item requirements not met host not applicable

4000               Configuration item unknown

5000               Configuration item error

5001               Configuration item error evaluating

5002               Configuration item error installing

5003               Configuration item error retrieving content

5004               Configuration item error installing dependency

5005               Configuration item error retrieving content dependency

5006               Configuration item error rules conflict

5007               Configuration item error waiting for retry

5008               Configuration item error uninstalling supersedence

<!-- p.1440 -->

 State message ID     State message description

 5009                 Configuration item error downloading superseded

 5010                 Configuration item error updating VE

 5011                 Configuration item error installing license

 5012                 Configuration item error retrieving allow all trusted apps

 5013                 Configuration item error no licenses available

 5014                 Configuration item error OS not supported

 6000                 Configuration item launch succeeded

 6010                 Configuration item launch error

 6020                 Configuration item launch unknown

Events
The following topic types have no state IDs:

                                                                                   ﾉ   Expand table

 Topic type             Description

 1800                   STATE_TOPICTYPE_EVENT_INTRINSIC

 1801                   STATE_TOPICTYPE_EVENT_EXTRINSIC

Endpoint protection
The following topic types have no state IDs:

                                                                                   ﾉ   Expand table

 Topic type            Description

 1900                  STATE_TOPICTYPE_EP_AM_INFECTION

 1901                  State_Topictype_Ep_Am_Health

 1902                  STATE_TOPICTYPE_EP_MALWARE

 1950                  STATE_TOPICTYPE_ATP_HEALTH_STATUS
