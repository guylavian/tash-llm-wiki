---
title: "Exchange Server — pages 3081-3107"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p3081-3107
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p3081-3107
family: exchange
documentKind: "doc"
abstract: "The next step is to create an override for the protocols that you want to enable. You can create one override that contains all protocols that AMSI body scanning should be enabled for. Be sure to run all commands from an elevated Exchange Management Shell: PowerShell New-Setting"
---

# Exchange Server — pages 3081-3107

<!-- p.3081 -->

The next step is to create an override for the protocols that you want to enable. You can create
one override that contains all protocols that AMSI body scanning should be enabled for. Be
sure to run all commands from an elevated Exchange Management Shell:

 PowerShell

 New-SettingOverride -Name "EnableAMSIBodyScanForEcpEwsOwa" -Component "Cafe" -
 Section "AmsiRequestBodyScanning" -Parameters
 @("EnabledEcp=True","EnabledEws=True","EnabledOwa=True") -Reason "Enabling AMSI body
 Scan for ECP, EWS and OWA"
 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh
 Restart-Service -Name W3SVC, WAS -Force

It's possible to create multiple overrides, for example, one for each protocol:

 PowerShell
 New-SettingOverride -Name "EnableAMSIBodyScanForEcp" -Component "Cafe" -Section
 "AmsiRequestBodyScanning" -Parameters ("EnabledEcp=True") -Reason "Enabling AMSI
 body Scan for ECP"

 New-SettingOverride -Name "EnableAMSIBodyScanForEws" -Component "Cafe" -Section
 "AmsiRequestBodyScanning" -Parameters ("EnabledEws=True") -Reason "Enabling AMSI
 body Scan for EWS"

 New-SettingOverride -Name "EnableAMSIBodyScanForOwa" -Component "Cafe" -Section
 "AmsiRequestBodyScanning" -Parameters ("EnabledOwa=True") -Reason "Enabling AMSI
 body Scan for OWA"

 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh
 Restart-Service -Name W3SVC, WAS -Force

To enable the AMSI body scanning for all protocols on all Exchange Servers in your
environment:

 PowerShell
 New-SettingOverride -Name "EnableAMSIBodyScanAllProtocols" -Component "Cafe" -
 Section "AmsiRequestBodyScanning" -Parameters ("EnabledAll=True") -Reason "Enabling
 AMSI body Scan for all protocols"

 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh
 Restart-Service -Name W3SVC, WAS -Force

By default, the feature passes the first 4096 bytes of the body to the anti-malware scanner. It's
possible to adjust the number of bytes that should be scanned. The maximum possible value is

<!-- p.3082 -->

1048576 bytes (1 MB) . We recommend starting with the default configuration and adjusting

the size if you experience performance issues. This setting can be configured by running the
following commands. Make sure to replace BodyScanSizeInBytes=8192 with the new byte size
that should be processed:

 PowerShell
 New-SettingOverride -Name "ConfigureCustomAMSIBodyScanSize" -Component "Cafe" -
 Section "AmsiRequestBodyScanning" -Parameters ("BodyScanSizeInBytes=8192") -Reason
 "Adjusting AMSI body Scan size to 8192 bytes"

 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh

 Restart-Service -Name W3SVC, WAS -Force

  ２ Warning

  Don't enable the following configuration unless explicitly advised by Microsoft.

It's possible to block any request whose HTTP message body exceeds the maximum possible
scannable size of 1048576 bytes (1 MB) . This feature can be enabled for a subset of protocols
(for example, OWA, ECP, EWS) or for all protocols. The supported protocols are listed in the
previous section. The following example blocks requests where the body size exceeds the
maximum scannable size for the Outlook on the web (formerly known as Outlook Web App or
OWA) protocol:

 PowerShell

 New-SettingOverride -Name "BlockRequestBodyGreaterThanMaxScanSizeOWA" -Component
 "Cafe" -Section "BlockRequestBodyGreaterThanMaxScanSize" -Parameters
 ("EnabledOwa=True") -Reason "Block requests with body size greater than 1 MB for
 OWA"

 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh

 Restart-Service -Name W3SVC, WAS -Force

Disable Exchange Server AMSI body scanning
If you experience issues with the Exchange Server AMSI body scanning feature after installing
the August 2025 Exchange Server Security Updates      or a later Exchange Server build, you can

<!-- p.3083 -->

disable the feature by creating a setting override. Run the following commands in an elevated
Exchange Management Shell (EMS):

 PowerShell
 New-SettingOverride -Name "DisableAMSIBodyScan" -Component "Cafe" -Section
 "AmsiRequestBodyScanning" -Parameters ("EnabledAll=False") -Reason "Disabling AMSI
 body scanning"

 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh
 Restart-Service -Name W3SVC, WAS -Force

Disable Exchange Server AMSI integration
If you experience issues with the Exchange Server AMSI integration or need to temporarily
disable it for research or troubleshooting, you can create an override to disable the integration.
The following commands must be executed from an elevated Exchange Management Shell
(EMS).

To disable AMSI integration on a specific Exchange Server, run these commands. Replace
<ServerName> with the name of your Exchange Server:

 PowerShell
 New-SettingOverride -Name "DisableAMSIScan" -Server <ServerName> -Component "Cafe" -
 Section "HttpRequestFiltering" -Parameters ("Enabled=False") -Reason
 "Troubleshooting AMSI"

 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh
 Restart-Service -Name W3SVC, WAS -Force

To disable AMSI integration on all Exchange Servers within your organization, you can run
these commands:

 PowerShell

 New-SettingOverride -Name "DisableAMSIScan" -Component "Cafe" -Section
 "HttpRequestFiltering" -Parameters ("Enabled=False") -Reason "Troubleshooting AMSI"

 Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
 Component VariantConfiguration -Argument Refresh
 Restart-Service -Name W3SVC, WAS -Force

To enable AMSI integration back, you can run these commands to remove the override:

<!-- p.3084 -->

PowerShell
Get-SettingOverride | Where-Object {($_.SectionName -eq "HttpRequestFiltering") -and
($_.Parameters -eq "Enabled=False")} | Remove-SettingOverride
Get-ExchangeDiagnosticInfo -Process Microsoft.Exchange.Directory.TopologyService -
Component VariantConfiguration -Argument Refresh

Restart-Service -Name W3SVC, WAS -Force

Last updated on 11/25/2025

<!-- p.3085 -->

Running Windows antivirus software on Exchange
servers
ﾃ     Summarize this article for me

APPLIES TO:           2016            2019   Subscription Edition

When you run Windows antivirus programs on Microsoft Exchange servers, you can help enhance the security and health of your
Exchange organization. However, if they aren't configured correctly, Windows antivirus programs can cause problems in Exchange
Server.

There are two basic components of any Windows antivirus program:

       Memory-resident scanning or real-time protection monitors all files and processes that are loaded and running in a computer's
       active memory.

       File-level scanning refers to checking files on the hard disk for viruses manually or on a regular schedule. Some antivirus programs
       start an on-demand scan automatically after the virus signatures are updated to make sure that all files are scanned with the latest
       signatures.

Another issue is that Windows antivirus programs can't replace email-based antispam and antimalware solutions because Windows
antivirus programs that run on Windows servers can't detect viruses, malware, and spam that are distributed only through email.

Recommended exclusions for Windows antivirus programs on
Exchange servers
The biggest potential problem is that a program (such as antivirus) might lock or quarantine an open log or database file that Exchange
needs to modify. This can cause severe Exchange Server issues, including potential data loss. Therefore, excluding these files from being
scanned by such scanning programs is critical. This recommendation supersedes any guidance from vendors on how their software
works with the file system, due to the unique nature of Exchange servers.

Note: The %ExchangeInstallPath% value is typically C:\Program Files\Microsoft\Exchange Server\V15\ (includes a trailing "\"), the
%SystemRoot% value is typically C:\Windows (doesn't include a trailing "\"), and the %SystemDrive% value is typically C: (doesn't
include a trailing "\").

The locations of many of these Exchange folders are configurable in the Exchange Management Shell. To learn how to open the
Exchange Management Shell in your on-premises Exchange organization, see Open the Exchange Management Shell.

    ７ Note

    Using third-party security software on your Exchange servers might introduce unexpected behaviors even if guidance on this page
    is followed. Bear in mind that remote scanning can also contribute to file locks that can interfere with Exchange functionality. When
    troubleshooting such issues, Microsoft might recommend to temporarily disable or uninstall such software to confirm baseline
    Exchange behavior.

Folder exclusions
Exclude the following folders from file-level scanning and memory-resident scanning on Exchange servers.

    ７ Note

    Unified Messaging is not available in Exchange 2019.

                                                                                                                           ﾉ   Expand table

<!-- p.3086 -->

Folder                                                      Category       Description                                                 Servers

%SystemRoot%\Cluster                                        DAGs           The cluster quorum database and other files for             Mailbox
                                                                           database availability groups (DAGs).                        servers

%SystemDrive%\DAGFileShareWitnesses\<DAGFQDN>               DAGs           The witness directory on the witness server that's          Any
                                                                           configured for the DAG. The witness server can be
                                                                           virtually any Microsoft Windows server in the local
                                                                           Active Directory forest that isn't already a member of
                                                                           the DAG.
                                                                           To see the actual location, run the following command:
                                                                           Get-DatabaseAvailabilityGroup <DAGName> | Format-
                                                                           List *Witness*

%ExchangeInstallPath%ClientAccess\OAB                       Offline        Offline Address Book files.                                 Mailbox
                                                            Address                                                                    servers
                                                            Books

%ExchangeInstallPath%FIP-FS                                 Antimalware    Content scanning that's used by the Malware agent and       Mailbox
                                                            and DLP        data loss prevention (DLP).                                 servers

%ExchangeInstallPath%GroupMetrics                           MailTips       Group Metrics files that are used to calculate values for   Mailbox
                                                                           the Large Audience and External Recipients MailTips.        servers

%ExchangeInstallPath%Logging                                Exchange       This folder contains many different types of Exchange       Mailbox
                                                            process logs   logs in subfolders. For example:                            servers
                                                                                 Calendar Repair Assistant logs
                                                                                 Managed Folder Assistant logs
                                                                                 IMAP4 protocol logs
                                                                                 POP3 protocol logs

                                                                           To see the actual locations, run the following
                                                                           commands:

                                                                           Get-MailboxServer -Identity <ServerName> | Format-
                                                                           List *LogPath*

                                                                           Get-PopSettings <ServerName> | Format-List
                                                                           LogFileLocation

                                                                           Get-ImapSettings <ServerName> | Format-List
                                                                           LogFileLocation

%ExchangeInstallPath%Mailbox                                Mailbox        Exchange databases, checkpoint files, and log files. By     Mailbox
                                                            databases      default, these files are located in subfolders based on     servers
                                                                           the name of the database. To see the actual locations,
                                                                           run the following command: Get-MailboxDatabase -
                                                                           Server \ServerName> | Format-List
                                                                           EdbFilePath,LogFolderPath

                                                                           By default, database context index files are located in
                                                                           the same folder as the database files in a subfolder
                                                                           that's named after the GUID of the database.

%ExchangeInstallPath%TransportRoles\Data\Adam               EdgeSync       Active Directory Lightweight Directory Services (AD         Edge
                                                                           LDS) and log files.                                         Transport
                                                                                                                                       servers

%ExchangeInstallPath%TransportRoles\Data\IpFilter           Connection     IP filter database, checkpoint, and log files.              Edge
                                                            filtering                                                                  Transport
                                                                                                                                       servers

%ExchangeInstallPath%TransportRoles\Data\Queue              Queues         Queue database, checkpoint, and log files.                  Mailbox
                                                                                                                                       servers
                                                                                                                                       Edge
                                                                                                                                       Transport
                                                                                                                                       servers

%ExchangeInstallPath%TransportRoles\Data\SenderReputation   Sender         Sender Reputation database, checkpoint, and log files.      Edge
                                                            reputation                                                                 Transport
                                                                                                                                       servers

<!-- p.3087 -->

Folder                                                      Category     Description                                               Servers

                                                                                                                                   Mailbox
                                                                                                                                   servers

%ExchangeInstallPath%TransportRoles\Data\Temp               Content      Content conversion that's done in the transport           Mailbox
                                                            conversion   pipeline.                                                 servers
                                                                                                                                   Edge
                                                                                                                                   Transport
                                                                                                                                   servers

%ExchangeInstallPath%TransportRoles\Logs                    Transport    Mail flow and transport pipeline logs are located in      Mailbox
                                                            logs         subfolders, for example:                                  servers
                                                                                Agent logging                                      Edge
                                                                               Connectivity logging                                Transport
                                                                               Message tracking                                    servers
                                                                               Pipeline tracing                                    (Transport
                                                                               Send and Receive connector protocol logging         service only)

                                                                         To see the actual locations, run the following
                                                                         commands:

                                                                         Get-TransportService <ServerName> | Format-List
                                                                         *LogPath,*TracingPath

                                                                         Get-FrontEndTransportService <ServerName> | Format-
                                                                         List *LogPath

                                                                         Get-MailboxTransportService <ServerName> | Format-
                                                                         List *LogPath,*TracingPath

%ExchangeInstallPath%TransportRoles\Pickup                  Pickup       The Pickup directory is used by administrators for mail   Mailbox
                                                            directory    flow testing or by applications that need to create and   servers
                                                                         submit their own message files.                           Edge
                                                                         To see the actual location, run the following command:    Transport
                                                                         Get-TransportService <ServerName> | Format-List           servers
                                                                         PickupDirectoryPath

%ExchangeInstallPath%TransportRoles\Replay                  Replay       The Replay directory receives messages from foreign       Mailbox
                                                            directory    gateway servers and can also be used to resubmit          servers
                                                                         messages that administrators export from the queues of    Edge
                                                                         Exchange servers.                                         Transport
                                                                         To see the actual location, run the following command:    servers
                                                                         Get-TransportService <ServerName> | Format-List
                                                                         ReplayDirectoryPath

%ExchangeInstallPath%UnifiedMessaging\Grammars              Unified      Grammar files for different locales, for example en-EN    Exchange
                                                            Messaging    or es-ES.                                                 2016 Mailbox
                                                                                                                                   servers

%ExchangeInstallPath%UnifiedMessaging\Prompts               Unified      Voice prompts, greetings, and informational message       Exchange
                                                            Messaging    files.                                                    2016 Mailbox
                                                                                                                                   servers

%ExchangeInstallPath%UnifiedMessaging\Temp                  Unified      Temporary files generated by Unified Messaging.           Exchange
                                                            Messaging                                                              2016 Mailbox
                                                                                                                                   servers

%ExchangeInstallPath%UnifiedMessaging\Voicemail             Unified      Voice mail files that are temporarily stored.             Exchange
                                                            Messaging                                                              2016 Mailbox
                                                                                                                                   servers

%ExchangeInstallPath%Working\OleConverter                   Content      Transport Neutral Encoding Format (TNEF), also known      Mailbox
                                                            conversion   as Rich Text Format (RTF), to MIME/HTML conversions.      servers
                                                                                                                                   Edge
                                                                                                                                   Transport
                                                                                                                                   servers

%SystemDrive%\inetpub\temp\IIS Temporary Compressed Files   Web          Internet Information Services (IIS) compression folder    Mailbox
                                                            components   that's used with Outlook on the web.                      servers

<!-- p.3088 -->

 Folder                                                       Category         Description                                                 Servers

 %SystemRoot%\Temp\OICE_<GUID>                                Exchange         Temporary files used by the Exchange Search service         Mailbox
                                                              Search           and Microsoft Filter Pack to perform file conversion in a   servers
                                                                               sandboxed environment.

Process exclusions
Many antivirus programs support the scanning of processes, which can adversely affect Microsoft Exchange if the incorrect processes are
scanned. Therefore, you should exclude the following Exchange or related processes from process scanning.

                                                                                                                                       ﾉ   Expand table

 Process                                            Path                                                      Comments                               Servers

 ComplianceAuditService.exe                         %ExchangeInstallPath%Bin                                  Microsoft Exchange Compliance          Mailbox
                                                                                                              Audit service                          servers
                                                                                                              (MSComplianceAudit)

 Dsamain.exe                                        %SystemRoot%\System32                                     Microsoft Exchange ADAM                Edge
                                                                                                              service (ADAM_MSExchange)              Transport
                                                                                                              (Active Directory Lightweight          servers
                                                                                                              Directory Services (AD LDS) on
                                                                                                              subscribed Edge Transport
                                                                                                              servers)

 EdgeTransport.exe                                  %ExchangeInstallPath%Bin                                  Microsoft Exchange Transport           Mailbox
                                                                                                              service worker process                 servers
                                                                                                                                                     Edge
                                                                                                                                                     Transport
                                                                                                                                                     servers

 fms.exe                                            %ExchangeInstallPath%FIP-FS\Bin                           Content scanning component             Mailbox
                                                                                                              that's used by the Malware agent       servers
                                                                                                              and DLP.

 hostcontrollerservice.exe                          %ExchangeInstallPath%Bin\Search\Ceres\HostController      Microsoft Exchange Search Host         Mailbox
                                                                                                              Controller service                     servers
                                                                                                              (HostControllerService)

 inetinfo.exe                                       %SystemRoot%\System32\inetsrv                             Internet Information Services (IIS)    Mailbox
                                                                                                                                                     servers

 Microsoft.Exchange.AntispamUpdateSvc.exe           %ExchangeInstallPath%Bin                                  Microsoft Exchange Antispam            Mailbox
                                                                                                              Update service                         servers
                                                                                                              (MSExchangeAntispamUpdate)             Edge
                                                                                                                                                     Transport
                                                                                                                                                     servers

 Microsoft.Exchange.ContentFilter.Wrapper.exe       %ExchangeInstallPath%TransportRoles\agents\Hygiene        Content Filter agent                   Mailbox
                                                                                                                                                     servers
                                                                                                                                                     Edge
                                                                                                                                                     Transport
                                                                                                                                                     servers

 Microsoft.Exchange.Diagnostics.Service.exe         %ExchangeInstallPath%Bin                                  Microsoft Exchange Diagnostics         Mailbox
                                                                                                              service (MSExchangeDiagnostics)        servers
                                                                                                                                                     Edge
                                                                                                                                                     Transport
                                                                                                                                                     servers

 Microsoft.Exchange.Directory.TopologyService.exe   %ExchangeInstallPath%Bin                                  Microsoft Exchange Active              Mailbox
                                                                                                              Directory Topology service             servers
                                                                                                              (MSExchangeADTopology)

 Microsoft.Exchange.EdgeCredentialSvc.exe           %ExchangeInstallPath%Bin                                  Microsoft Exchange Credential          Edge
                                                                                                              service                                Transport
                                                                                                              (MSExchangeEdgeCredential)             servers

<!-- p.3089 -->

Process                                          Path                                        Comments                           Servers

Microsoft.Exchange.EdgeSyncSvc.exe               %ExchangeInstallPath%Bin                    Microsoft Exchange EdgeSync        Mailbox
                                                                                             service (MSExchangeEdgeSync)       servers

Microsoft.Exchange.Imap4.exe                     %ExchangeInstallPath%FrontEnd\PopImap       Microsoft Exchange IMAP4           Mailbox
                                                                                             service (MSExchangeImap4)          servers

Microsoft.Exchange.Imap4service.exe              %ExchangeInstallPath%ClientAccess\PopImap   Microsoft Exchange IMAP4           Mailbox
                                                                                             Backend service                    servers
                                                                                             (MSExchangeIMAP4BE)

Microsoft.Exchange.Notifications.Broker.exe      %ExchangeInstallPath%Bin                    Microsoft Exchange Notifications   Mailbox
                                                                                             Broker service                     servers
                                                                                             (MSExchangeNotificationsBroker)

Microsoft.Exchange.Pop3.exe                      %ExchangeInstallPath%FrontEnd\PopImap       Microsoft Exchange POP3 service    Mailbox
                                                                                             (MSExchangePop3)                   servers

Microsoft.Exchange.Pop3service.exe               %ExchangeInstallPath%ClientAccess\PopImap   Microsoft Exchange POP3            Mailbox
                                                                                             Backend service                    servers
                                                                                             (MSExchangePOP3BE)

Microsoft.Exchange.ProtectedServiceHost.exe      %ExchangeInstallPath%Bin                    Microsoft Exchange Service Host    Mailbox
                                                                                             service (MSExchangeServiceHost)    servers
                                                                                                                                Edge
                                                                                                                                Transport
                                                                                                                                servers

Microsoft.Exchange.RPCClientAccess.Service.exe   %ExchangeInstallPath%Bin                    Microsoft Exchange RPC Client      Mailbox
                                                                                             Access service (MSExchangeRPC)     servers

Microsoft.Exchange.Search.Service.exe            %ExchangeInstallPath%Bin                    Microsoft Exchange Search          Mailbox
                                                                                             service (MSExchangeFastSearch)     servers

Microsoft.Exchange.Servicehost.exe               %ExchangeInstallPath%Bin                    Microsoft Exchange Service Host    Mailbox
                                                                                             service (MSExchangeServiceHost)    servers
                                                                                                                                Edge
                                                                                                                                Transport
                                                                                                                                servers

Microsoft.Exchange.Store.Service.exe             %ExchangeInstallPath%Bin                    Microsoft Exchange Information     Mailbox
                                                                                             Store service (MSExchangeIS)       servers

Microsoft.Exchange.Store.Worker.exe              %ExchangeInstallPath%Bin                    Microsoft Exchange Information     Mailbox
                                                                                             Store service worker process       servers

Microsoft.Exchange.UM.CallRouter.exe             %ExchangeInstallPath%FrontEnd\CallRouter    Microsoft Exchange Unified         Exchange
                                                                                             Messaging Call Router service      2016
                                                                                             (MSExchangeUMCR)                   Mailbox
                                                                                                                                servers

MSExchangeCompliance.exe                         %ExchangeInstallPath%Bin                    Microsoft Exchange Compliance      Mailbox
                                                                                             Service (MSExchangeCompliance)     servers

MSExchangeDagMgmt.exe                            %ExchangeInstallPath%Bin                    Microsoft Exchange DAG             Mailbox
                                                                                             Management service                 servers
                                                                                             (MSExchangeDagMgmt)

MSExchangeDelivery.exe                           %ExchangeInstallPath%Bin                    Microsoft Exchange Mailbox         Mailbox
                                                                                             Transport Delivery service         servers
                                                                                             (MSExchangeDelivery)

MSExchangeFrontendTransport.exe                  %ExchangeInstallPath%Bin                    Microsoft Exchange Frontend        Mailbox
                                                                                             Transport service                  servers
                                                                                             (MSExchangeFrontEndTransport)

MSExchangeHMHost.exe                             %ExchangeInstallPath%Bin                    Microsoft Exchange Health          Mailbox
                                                                                             Manager service                    servers
                                                                                             (MSExchangeHM)                     Edge
                                                                                                                                Transport
                                                                                                                                servers

<!-- p.3090 -->

Process                            Path                                                 Comments                           Servers

MSExchangeHMWorker.exe             %ExchangeInstallPath%Bin                             Microsoft Exchange Health          Mailbox
                                                                                        Manager service worker process     servers
                                                                                                                           Edge
                                                                                                                           Transport
                                                                                                                           servers

MSExchangeMailboxAssistants.exe    %ExchangeInstallPath%Bin                             Microsoft Exchange Mailbox         Mailbox
                                                                                        Assistants service                 servers
                                                                                        (MSExchangeMailboxAssistants)

MSExchangeMailboxReplication.exe   %ExchangeInstallPath%Bin                             Microsoft Exchange Mailbox         Mailbox
                                                                                        Replication service                servers
                                                                                        (MSExchangeMailboxReplication)

MSExchangeRepl.exe                 %ExchangeInstallPath%Bin                             Microsoft Exchange Replication     Mailbox
                                                                                        service (MSExchangeRepl)           servers

MSExchangeSubmission.exe           %ExchangeInstallPath%Bin                             Microsoft Exchange Mailbox         Mailbox
                                                                                        Transport Submission service       servers
                                                                                        (MSExchangeSubmission)

MSExchangeTransport.exe            %ExchangeInstallPath%Bin                             Microsoft Exchange Transport       Mailbox
                                                                                        service (MSExchangeTransport)      servers
                                                                                                                           Edge
                                                                                                                           Transport
                                                                                                                           servers

MSExchangeTransportLogSearch.exe   %ExchangeInstallPath%Bin                             Microsoft Exchange Transport       Mailbox
                                                                                        Log Search service                 servers
                                                                                        (MSExchangeTransportLogSearch)     Edge
                                                                                                                           Transport
                                                                                                                           servers

MSExchangeThrottling.exe           %ExchangeInstallPath%Bin                             Microsoft Exchange Throttling      Mailbox
                                                                                        service (MSExchangeThrottling)     servers

Noderunner.exe                     %ExchangeInstallPath%Bin\Search\Ceres\Runtime\1.0    Microsoft Exchange Search          Mailbox
                                                                                        service (MSExchangeFastSearch)     servers

OleConverter.exe                   %ExchangeInstallPath%Bin                             Converts rich text format (RTF)    Mailbox
                                                                                        messages to MIME/HTML for          servers
                                                                                        external recipients.

ParserServer.exe                   %ExchangeInstallPath%Bin\Search\Ceres\ParserServer   Microsoft Exchange Search          Mailbox
                                                                                        service (MSExchangeFastSearch)     servers

ScanEngineTest.exe                 %ExchangeInstallPath%FIP-FS\Bin                      Content scanning component         Mailbox
                                                                                        that's used by the Malware agent   servers
                                                                                        and DLP

ScanningProcess.exe                %ExchangeInstallPath%FIP-FS\Bin                      Content scanning component         Mailbox
                                                                                        that's used by the Malware agent   servers
                                                                                        and DLP

UmService.exe                      %ExchangeInstallPath%Bin                             Microsoft Exchange Unified         Exchange
                                                                                        Messaging service                  2016
                                                                                        (MSExchangeUM)                     Mailbox
                                                                                                                           servers

UmWorkerProcess.exe                %ExchangeInstallPath%Bin                             Microsoft Exchange Unified         Exchange
                                                                                        Messaging service worker           2016
                                                                                        process                            Mailbox
                                                                                                                           servers

UpdateService.exe                  %ExchangeInstallPath%FIP-FS\Bin                      Content scanning component         Mailbox
                                                                                        that's used by the Malware agent   servers
                                                                                        and DLP

wsbexchange.exe                    %ExchangeInstallPath%Bin                             Microsoft Exchange Server          Mailbox
                                                                                        Extension for Windows Server       servers

<!-- p.3091 -->

 Process                                             Path                                           Comments                          Servers

                                                                                                    Backup (wsbexchange)

File name extension exclusions
In addition to excluding specific folders and processes, you should exclude the following Exchange-specific file name extensions in case
folder exclusions fail or files are moved from their default locations.

                                                                                                                           ﾉ   Expand table

 Extensions               Description                                                  Servers

 .config                  Application-related extensions                               Mailbox servers
                                                                                       Edge Transport servers

 .chk                     Database-related extensions                                  Mailbox servers
 .edb                                                                                  Edge Transport servers
 .jfm
 .jrs
 .jsl
 .log
 .que

 .dsc                     Group Metrics-related extensions                             Mailbox servers
 .txt

 .cfg                     Unified Messaging-related extensions                         Exchange 2016 Mailbox servers
 .grxml

 .lzx                     Offline address book-related extensions                      Mailbox servers

 Last updated on 03/12/2026

<!-- p.3092 -->

Unified Messaging in Exchange Server 2016
Article • 05/09/2025

APPLIES TO:        2016   2019    Subscription Edition

Unified Messaging in Exchange Server 2016 is basically unchanged from Exchange Server 2013.
For information about Exchange 2013 Unified Messaging, see Unified Messaging.

<!-- p.3093 -->

Exchange documentation information
07/01/2025

APPLIES TO:       2016      2019       Subscription Edition

You're reading a collection of conceptual and procedural topics organized by subject or by
technologies used by Microsoft Exchange Server. You can access each topic directly from the
table of contents in the left pane, from a link in another Help topic, from the results of a search,
or from your own custom list of favorite topics.

Other information related to Exchange documentation is in Third-party copyright notices.

Where to find Exchange documentation
Exchange documentation is your primary gateway to in-depth technical information about
Microsoft Exchange.

The Exchange Team Blog       contains technical articles written by the Exchange Team, as well as
product announcements and updates. The blog is an excellent way to interact with the
Exchange Team. We read and respond to your feedback and comments.

If you're an admin for an Exchange hybrid or Exchange Online deployment, you may also be
interested in Manage Microsoft 365 and Office 365.

For information on Exchange Server versions that have reached end of support, refer to the
following documentations:

     Exchange Server 2010
     Exchange Server 2013

Additional resources
Looking for more than just documentation? Check out these other Exchange resources:

     Exchange Server Forums        : The forum provides a place to discuss Exchange with users
     and Exchange Team members.

     Exchange and Exchange Online development: You'll find Exchange developer
     documentation here.

     Support for business    : Select Servers > Exchange Server for support resources for
     multiple versions of Exchange.

<!-- p.3094 -->

Accessibility for people with disabilities: This topic provides important information about
features, products, and services that help make Microsoft Exchange more accessible for
people with disabilities.

<!-- p.3095 -->

Accessibility for people with disabilities
Article • 05/09/2025

APPLIES TO:           2016     2019      Subscription Edition

Microsoft is committed to making its products and services easier for everyone to use. The
following sections provide information about the features, products, and services that make
Microsoft Exchange Server more accessible for people with disabilities:

      Accessibility for people with disabilities
         Accessibility features of Exchange
         Accessibility features of Exchange Help
         Accessibility products and services from Microsoft
                Accessibility features of Windows
                Documentation in alternative formats
                Customer service for people with hearing impairments
         For more information

Accessibility features of Exchange
The following features help make Microsoft Exchange more accessible for people with
disabilities:

      Keyboard shortcuts in the Exchange admin center

      Keyboard Shortcuts in Outlook on the web

In addition, some accessibility features and utilities of Windows may benefit Exchange users
with disabilities. Also, Windows PowerShell size and color changes provide accessibility options
when using the Exchange Management Shell. For more information about Windows PowerShell
accessibility options, see Accessibility in Windows PowerShell ISE.

Accessibility features of Exchange Help
Every figure in Help for Microsoft Exchange, including screenshots, diagrams, flow charts, and
other figures, has associated alternate text. Users who have difficulty viewing figures can pause
the cursor on the figure to read the alternate text. The alternate text describes what is
illustrated in the figure.

Accessibility products and services from Microsoft

<!-- p.3096 -->

The following sections provide information about the features, products, and services that
make Microsoft Windows more accessible for people with disabilities.

  ７ Note

  The information in this section applies only to users who license Microsoft products in the
  United States. If you obtained this product outside of the United States, visit the Microsoft
  Accessibility website   for a list of telephone numbers and addresses for Microsoft
  support services. You can contact your subsidiary to find out whether the type of products
  and services described in this section are available in your area. You can learn more about
  the accessibility features included in Microsoft products on the Accessibility in Microsoft
  Products web site.

Accessibility features of Windows
The Windows operating system has many built-in accessibility features that are useful for
individuals who have difficulty typing or using a mouse, are blind or have low vision, or who
are deaf or hard-of-hearing. The features are installed during Setup. For more information
about these features, see Help in Windows and Microsoft Accessibility     .

     Free step-by-step tutorials: Microsoft offers a series of step-by-step tutorials that provide
     detailed procedures for adjusting the accessibility options and settings on your computer.
     This information is presented in a side-by-side format so that you can learn how to use
     the mouse, the keyboard, or a combination of both.

     To find step-by-step tutorials for Microsoft products, see Microsoft Accessibility   .

     Assistive technology products for Windows: A wide variety of assistive technology
     products are available to make computers easier to use for people with disabilities. You
     can search a catalog of assistive technology products that run on Windows at Microsoft
     Accessibility.

     If you use assistive technology, be sure to contact your assistive technology vendor
     before you upgrade your software or hardware to check for possible compatibility issues.

Documentation in alternative formats
If you have difficulty reading or handling printed materials, you can obtain the documentation
for many Microsoft products in more accessible formats. You can obtain an index of accessible
product documentation at Microsoft Accessibility    .

<!-- p.3097 -->

In addition, you can obtain additional Microsoft publications from Learning Ally. Learning Ally
distributes these documents to registered, eligible members of their distribution service. For
information about the availability of Microsoft product documentation and books from
Microsoft Press, contact Learning Ally.

  Learning Ally
  20 Roszel Road
  Princeton, NJ 08540
  Telephone number from within the United States: (800) 221-4792
  Web site: Learning Ally

Customer service for people with hearing impairments
If you're deaf or hard-of-hearing, complete access to Microsoft product and customer services
is available through a text telephone (TTY/TDD) service:

     For customer service, contact Microsoft Sales Information Center at (800) 892-5234
     between 6:30 A.M. and 5:30 P.M. Pacific Time, Monday through Friday, excluding holidays.

     For technical assistance in the United States, contact Microsoft Product Support Services
     at (800) 892-5234 between 6:00 A.M. and 6:00 P.M. Pacific Time, Monday through Friday,
     excluding holidays. In Canada, dial (905) 568-9641 between 8:00 A.M. and 8:00 P.M.
     Eastern Time, Monday through Friday, excluding holidays.

Microsoft Support Services are subject to the prices, terms, and conditions in place at the time
the service is used. For more information, see Microsoft Support     .

For more information
For more information about how accessible technology for computers helps to improve the
lives of people with disabilities, see Microsoft Accessibility   .

<!-- p.3098 -->

Exchange Server: Third-party copyright
notices
Article • 05/09/2025

APPLIES TO:        2016     2019   Subscription Edition

Outside In HTML Export © 1991, 2011 Oracle

Platforms Supported - Outside In HTML Export:

Windows (32-bit):

Windows 2000

Windows Server 2003

Windows Vista

Windows Server 2008

Windows XP

Windows 7

Windows Itanium (64 bit):

Windows .NET Server 2003 Enterprise Edition for Itanium

Windows (64 bit):

Windows 2003 x 64 Datacenter

Windows 2003 x 64 Enterprise

Windows 2003 x 64 Standard Windows Server

Windows Server 2008

Windows Server 2008 R2

Windows 7

<!-- p.3099 -->

Exchange admin center keyboard shortcuts
Article • 05/09/2025

APPLIES TO:        2016      2019       Subscription Edition

Microsoft is committed to making its products and services easier for everyone to use. This
topic provides information about the keyboard shortcuts that make Exchange Server and other
Microsoft products and services more accessible for people with disabilities.

Keyboard shortcuts in the Exchange admin center
in Exchange Server
By using keyboard shortcuts in the Exchange admin center (EAC), you can quickly accomplish
the common tasks that are described in the following table. To learn more about the EAC, see
Exchange admin center in Exchange Server.

                                                                                      ﾉ   Expand table

 To do this                                   Use this keyboard shortcut

 Move between areas or between controls in    Tab
 the EAC                                      Shift-Tab

 Move between items in drop-down menus        Up arrow key
 in the EAC                                   Down arrow key

                                              Note that you can't use Tab or Shift-Tab to move between
                                              items in drop-down menus

 Move within lists from one item to another   Up arrow key
                                              Down arrow key
                                              Page Up
                                              Page Down
                                              Home
                                              End

                                              Note that you can also use the Up, Down, Left, and Right
                                              arrow keys to:

                                                     Move between option buttons.
                                                     Move within a group of associated check boxes.

 Move within primary property pages from      Up arrow key
 one item to another                          Down arrow key
                                              Page Up
                                              Page Down

<!-- p.3100 -->

 To do this                                 Use this keyboard shortcut

                                            Home
                                            End
                                            Tab
                                            Shift-Tab

                                            You can use Enter or the Spacebar to activate your
                                            selection.

 Move within secondary property pages       Up arrow key
 from one item to another                   Down arrow key
                                            Page Up
                                            Page Down
                                            Home
                                            End
                                            Tab
                                            Shift-Tab

                                            You can use Enter or the Spacebar to activate your
                                            selection.

Keyboard shortcuts in other Microsoft products
and services
To learn about accessibility features in Microsoft 365 or Office 365, including keyboard
shortcuts, visit the Microsoft Accessibility website     .

<!-- p.3101 -->

Exchange Server Privacy Statement
Article • 05/09/2025

APPLIES TO:        2016     2019      Subscription Edition

Microsoft is committed to protecting your privacy, while delivering software that brings you
the performance, power, and convenience you desire in your personal computing. This privacy
statement applies to Microsoft Exchange Server 2016 and Exchange Server 2019. It focuses on
features that communicate with the Internet. It doesn't apply to any other online or offline
Microsoft sites, products, or services.

Exchange 2016 and Exchange 2019 deliver email, calendaring, contact management, and other
online collaboration functionalities on your PC's, mobile phones, and web browsers.

This privacy statement addresses the deployment and use of Exchange 2016 and Exchange
2019 in an enterprise network environment. If you use Exchange Server technologies as a
service operated by Microsoft or a third party, please refer to the service-specific privacy and
security policies provided by Microsoft or the third-party service provider.

IT administrators of Exchange 2016 and Exchange 2019 may choose to enable or disable
certain Internet-enabled features in Exchange, or to deploy other privacy impacting
technologies, based on legal or compliance considerations or internal policies. You should
direct privacy-related requests related to the entity that's providing your access to Exchange
2016 or Exchange 2019. Microsoft isn't responsible for the privacy practices of its customers or
other third parties.

Collection and Use of Your Information
The information we collect from you'll be used by Microsoft and its controlled subsidiaries and
affiliates to enable the features you're using and to provide the service(s) or carry out the
transaction(s) you have requested or authorized. It may also be used to analyze and improve
Microsoft products and services.

We may send standard service communications such as welcome letters, billing reminders,
information on technical service issues, and security announcements. Some Microsoft services
may send periodic member letters that are considered part of the service. We may occasionally
request your feedback, invite you to participate in surveys, or send you promotional mailings to
inform you of other products or services available from Microsoft and its affiliates.

In order to offer you a more consistent and personalized experience in your interactions with
Microsoft, information collected through one Microsoft service may be combined with
information collected through other Microsoft services. We may also supplement the

<!-- p.3102 -->

information we collect with information obtained from other companies. For example, we may
use services from other companies that enable us to derive a general geographic area based
on your IP address in order to customize certain services to your geographic area.

Except as described in this statement, personal information you provide will not be
transferred to third parties without your consent.

We occasionally hire other companies to provide limited services on our behalf, such as
answering customer questions about products or services or performing statistical analysis of
our services. We'll provide those companies only the personal information they need to deliver
the service, and they're prohibited from using that information for any other purpose.

Microsoft may access or disclose information about you, including the content of your
communications, in order to: (a) comply with the law or respond to lawful requests or legal
process; (b) protect the rights or property of Microsoft or our customers, including the
enforcement of our agreements or policies governing your use of the services; or (c) act on a
good faith belief that such access or disclosure is necessary to protect the personal safety of
Microsoft employees, customers, or the public.

Information that is collected by or sent to Exchange 2016 and Exchange 2019 may be stored
and processed in the United States or in any other country/region in which Microsoft or its
affiliates, subsidiaries, or service providers maintain facilities. Microsoft abides by the safe
harbor framework as set forth by the United States Department of Commerce regarding the
collection, use, and retention of data from the European Union, the European Economic Area,
and Switzerland.

Collection and Use of Information about Your Computer

When you use software with Internet-enabled features, information about your computer
("standard computer information") is sent to the web sites you visit and online services you use.
Microsoft uses standard computer information to provide you Internet-enabled services, to
help improve our products and services, and for statistical analysis. Standard computer
information typically includes information such as your IP address, operating system version,
browser version, and regional and language settings. In some cases, standard computer
information may also include hardware ID, which indicates the device manufacturer, device
name, and version. If a particular feature or service sends information to Microsoft, standard
computer information will be sent as well.

The privacy details for other Exchange 2016 or Exchange 2019 features, software, or services
listed in this privacy statement describe what additional information is collected and how it's
used.

Security of Your Information

<!-- p.3103 -->

Microsoft is committed to helping protect the security of your information. We use a variety of
security technologies and procedures to help protect your information from unauthorized
access, use, or disclosure. For example, information you provide is stored on computer systems
with limited access, which are located in controlled facilities.

Specific Feature: Microsoft Error Reporting
What This Feature Does: Microsoft Error Reporting provides a service that allows you to report
problems you may be having to Microsoft and to receive information that may help you avoid
or solve such problems.

Information Collected, Processed, or Transmitted: For information about the information
collected, processed, or transmitted by Microsoft Error Reporting, see Privacy Statement for the
Microsoft Error Reporting Service     .

Use of Information: The error reporting data that you submit may be used to solve customer
problems and to improve Microsoft software and services.

Choice/Control: You'll be offered the opportunity to participate in Microsoft Error Reporting
the first time an error is encountered. When you choose to enable it, Microsoft Error Reporting
will automatically report problems you encounter to Microsoft. In addition, your IT
administrator can choose to enable or disable Microsoft Error Reporting during the Exchange
Server setup process for all users.

In rare cases, such as problems that are especially difficult to solve, Microsoft may request
additional data, including sections of memory (which may include memory shared by any or all
applications running at the time the problem occurred), some registry settings, and one or
more files from your computer. Your current documents may also be included. When additional
data is requested, you'll have an opportunity to view the information contained in the error
report before choosing whether or not to send the report to Microsoft.

Important Information: Enterprise customers can use Group Policy to configure how Microsoft
Error Reporting works on their computers. Configuration options include the ability to turn off
Microsoft Error Reporting. If you're an administrator and want to configure Group Policy for
Microsoft Error Reporting, technical details are available at the Group Policy Settings Reference
for Windows and Windows Server            .

Specific Feature: Online Feedback
What This Feature Does: Online Feedback allows you to provide feedback about products and
services directly to Microsoft.

<!-- p.3104 -->

Information Collected, Processed, or Transmitted: If you choose to use Online Feedback, the
content of the message and standard computer information will be sent to Microsoft.

Use of Information: The information submitted may be used to improve Microsoft sites,
products, or services. The information that we collect from this feature may also be used to
request additional information about feedback provided about the product or service.

Choice/Control: Use of Online Feedback is optional.

Specific Feature: Online Help
What This Feature Does: Clicking or otherwise using Help connects to online support
materials, providing you with the most up-to-date content available.

Information Collected, Processed, or Transmitted: When you use Help, the request is sent to
Microsoft, as well as any rating or feedback provided about the help topics. Any personal
information entered into the search or feedback boxes will be sent to Microsoft but won't be
used to identify or contact you.

Use of Information: Help uses search information to return the most relevant results, develop
new content, and improve the existing content.

Choice/Control: Don't use Help if you don't wish to connect to online support materials.

Specific Feature: Customer Experience
Improvement Program
What This Feature Does: If you choose to participate, the Customer Experience Improvement
Program (CEIP) collects basic information about your hardware configuration and how you use
Microsoft software and services in order to identify trends and usage patterns. CEIP also
collects the type and number of errors you encounter, software and hardware performance,
and the speed of services. Microsoft doesn't collect your name, address, or other contact
information.

Information Collected, Processed, or Transmitted: CEIP information is automatically sent to
Microsoft when the feature is turned on. For more information about the information collected,
processed, or transmitted by CEIP, see the Privacy Statement for the Microsoft Customer
Experience Improvement Program.

Use of Information: Microsoft uses this information to improve the quality, reliability, and
performance of Microsoft software and services.

<!-- p.3105 -->

Choice/Control: CEIP is turned off by default unless your IT administrator has chosen to turn it
on for you. You'll be prompted to sign up in the Exchange installer. Unless your administrator
has restricted your ability to do so, you can change your CEIP settings at any time.

Specific Feature: Bing Maps Extension
What This Feature Does: the Bing Maps extension will appear in Outlook and Outlook on the
web (formerly known as Outlook Web App) when Exchange 2016 or Exchange 2019 detects the
presence of an address in the body of an email and allow you to query the Bing Maps service
for a map of the location.

Information Collected, Processed, or Transmitted: when you click on the Bing Maps extension
from the user interface, the information that Exchange determines to be an address will be
passed to the Bing Maps service, which will perform a query based on the address and return a
map for it. For more information on Bing's privacy practices, see the Bing section in Microsoft
Privacy Statement    .

Use of Information: The address information is used to display the map for the address.

Choice/Control: This feature can be turned off by the IT administrator, or the end user.

Specific Feature: Offline
What This Feature Does: In Outlook on the web, the Offline features stores contacts, calendar
and email information on a user's machine so that it's accessible without a network connection.

Information Collected, Processed, or Transmitted: Information collected and stored includes
contacts, calendar and email from the user's mailbox on the Exchange Server. This feature
doesn't transmit information to Microsoft.

Use of Information: Information is stored locally on the user's machine to enable offline access.

Choice/Control: In Outlook on the web, this Offline feature is off by default and the user must
enable offline mode. Additionally, the IT administrators can disable the option for this feature
so that users aren't able to turn it on.

Specific Feature: Sender Photo
What This Feature Does: In Outlook on the web, the Sender Photo feature allows a recipient to
see the photo of the sender of an email he or she's viewing, if the sender is from the same
organization as the recipient.

<!-- p.3106 -->

Information Collected, Processed, or Transmitted: When Outlook on the web believes a
sender's photo may be available, the sender's email address is sent to the Exchange server.
Transmission may be sent partially in an unencrypted form. This feature doesn't transmit
information to Microsoft.

Use of Information: The sender's email address will be used to locate the sender's photo from
the destination Exchange server.

Choice/Control: IT administrators can turn off this feature.

Specific Feature: Contact Card
What This Feature Does: When browsing emails in Outlook on the web, a user can click on the
name of the sender or one of the recipients in a mail to retrieve the contact card for the
individual. The contact card displays information about that individual.

Information Collected, Processed, or Transmitted: When a user requests the contact card
information for someone by clicking on the person's name from an email, the email address or
similar identifier for the person whose information is requested is sent to the Exchange server.
Transmission may be sent partially in an unencrypted form. This feature doesn't transmit
information to Microsoft.

Use of Information: The email address of the person whose contact card is requested will be
used to locate the person's contact card information from the destination Exchange server.

Choice/Control: Don't click on an individual's name to retrieve the individual's contact card if
you don't wish to send the individual's identification to the Exchange server.

Changes to This Privacy Statement
Microsoft is committed to helping protect the security of your information. We use a variety of
security technologies and procedures to help protect your information from unauthorized
access, use, or disclosure. For example, information you provide is stored on computer systems
with limited access, which are located in controlled facilities.

For More Information
Microsoft welcomes your comments regarding this privacy statement and its supplements. If
you have questions or believe that we haven't adhered to these documents, please contact us
using this web form    , or by email, at the following address:

Microsoft Privacy

<!-- p.3107 -->

Microsoft Corporation

One Microsoft Way

Redmond, Washington 98052 USA

425-882-8080

To find the Microsoft subsidiary in your country or region, see Microsoft office locations around
the world   .
