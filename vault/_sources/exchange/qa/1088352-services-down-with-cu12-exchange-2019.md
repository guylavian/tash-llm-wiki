---
title: "Services down with CU12 Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1088352/services-down-with-cu12-exchange-2019
question_id: 1088352
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Services down with CU12 Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1088352/services-down-with-cu12-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone

I have a Exchange 2019 (DAG 2 Servers) Cu12 with some errors only in node1. Node2 works fine. Some services doesn't start and can't apply the last CU12

This is the status of my services:

When I try to start for example the replication service I obtain:

When I try to start Management Shell:

And In the event log I can see:

"The Microsoft Exchange Service Host service terminated unexpectedly. It has done this 1 time(s). The following corrective action will be taken in 5000 milliseconds: Restart the service." (every 4min)

"An unexpected failure has occurred. The problem will require administrator intervention. The service will retry in 00:15:00. Diagnostic information:

at Microsoft.Exchange.Servicelets.RPCHTTP.RPCHTTPServicelet.UpdateValidPortsRegistrySettings()  

at Microsoft.Exchange.Servicelets.RPCHTTP.RPCHTTPServicelet.ConfigureRpcProxyRegistrySettings()  

at Microsoft.Exchange.Servicelets.RPCHTTP.RPCHTTPServicelet.ConfigureRpcForMailboxServer(Boolean isAlsoFrontEnd)  

at Microsoft.Exchange.Servicelets.RPCHTTP.RPCHTTPServicelet.Work()  

Could not load file or assembly 'Microsoft.Exchange.RpcClientAccess, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified."

"Watson report about to be sent for process id: 20264, with parameters: E12IIS, c-RTL-AMD64, 15.02.1118.009, M.Exchange.ServiceHost, M.Exchange.SyncMigrationServicelet, M.E.S.S.SyncMigrationServicelet.Work, S.IO.FileNotFoundException, fd7e-dumptidset, 15.02.1118.009.  

ErrorReportingEnabled: True "

"Error loading servicelet module Microsoft.Exchange.RealtimeAnalyticsPublisherServicelet.dll: the module was not found." (the dll exist in bin directory)

"Error loading servicelet module Microsoft.Office.CompliancePolicy.Exchange.Dar.dll: the module was not found."

"Error loading servicelet module Microsoft.Exchange.JobQueueServicelet.dll: the module was not found."

*****Edit: I try to execute F:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:RecoverServer

But I obtain some errors too....

Starting Microsoft Exchange Server 2019 Setup  

[11.14.2022 17:13:08.0074] [0] **********************************************  

[11.14.2022 17:13:08.0078] [0] Local time zone: (UTC+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna.  

[11.14.2022 17:13:08.0078] [0] Operating system version: Microsoft Windows NT 6.2.9200.0.  

[11.14.2022 17:13:08.0081] [0] Setup version: 15.2.1118.7.  

[11.14.2022 17:13:08.0082] [0] Logged on user: XXXXXXXXXXX.  

[11.14.2022 17:13:08.0121] [0] Command Line Parameter Name='iacceptexchangeserverlicenseterms_diagnosticdataon', Value=''.  

[11.14.2022 17:13:08.0121] [0] Command Line Parameter Name='mode', Value='RecoverServer'.  

[11.14.2022 17:13:08.0121] [0] Command Line Parameter Name='sourcedir', Value='F:\'.  

[11.14.2022 17:13:09.0000] [0] RuntimeAssembly was started with the following command: '/IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:RecoverServer /sourcedir:F:"'.  

[11.14.2022 17:13:09.0002] [0] The registry key, HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Exchange\v8.0, wasn't found.  

[11.14.2022 17:13:09.0002] [0] The registry key, HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v14, wasn't found.  

[11.14.2022 17:13:09.0107] [0] Copying Files...  

[11.14.2022 17:13:09.0110] [0] Starting copy from F:\Setup\ServerRoles\Common to C:\Windows\Temp\ExchangeSetup.  

[11.14.2022 17:13:25.0780] [0] Finished copy from F:\Setup\ServerRoles\Common to C:\Windows\Temp\ExchangeSetup.  

[11.14.2022 17:13:25.0781] [0] File copy complete. Setup will now collect additional information needed for installation.

[11.14.2022 17:13:25.0785] [0] Assembly dll file location is C:\Windows\Temp\ExchangeSetup\Microsoft.Exchange.Setup.Console.dll  

[11.14.2022 17:13:33.0559] [0] Setup is choosing the domain controller to use  

[11.14.2022 17:13:33.0719] [0] The MSExchangeADTopology has a persisted domain controller: DC02  

[11.14.2022 17:13:37.0608] [0] PrepareAD has been run, and has replicated to this domain controller; so setup will use DC02  

[11.14.2022 17:13:37.0608] [0] Setup is choosing a global catalog...  

[11.14.2022 17:13:37.0656] [0] Setup has chosen the global catalog server DC02.  

[11.14.2022 17:13:37.0679] [0] Setup will use the domain controller 'DC02.  

[11.14.2022 17:13:37.0679] [0] Setup will use the global catalog 'DC02'.  

[11.14.2022 17:13:37.0681] [0] Exchange configuration container for the organization is 'CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=domain,DC=priv'.  

[11.14.2022 17:13:37.0684] [0] Exchange organization container for the organization is 'CN=Domain,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=domain,DC=priv'.  

[11.14.2022 17:13:37.0703] [0] Setup will search for an Exchange Server object for the local machine with name 'EXCH01'.  

[11.14.2022 17:13:37.0868] [0] Exchange Server object found : 'CN=EXCH01,CN=Servers,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=Domain,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=domain,DC=priv'.  

[11.14.2022 17:13:37.0938] [0] The following roles have been unpacked: BridgeheadRole ClientAccessRole MailboxRole FrontendTransportRole AdminToolsRole CafeRole  

[11.14.2022 17:13:37.0940] [0] The following datacenter roles are unpacked:  

[11.14.2022 17:13:37.0943] [0] The following roles are installed: BridgeheadRole ClientAccessRole MailboxRole FrontendTransportRole AdminToolsRole CafeRole  

[11.14.2022 17:13:37.0946] [0] The local server has some Exchange files installed.  

[11.14.2022 17:13:37.0954] [0] Server Name=EXCH01  

[11.14.2022 17:13:37.0955] [0] Setup will use the path 'F:\' for installing Exchange.  

[11.14.2022 17:13:37.0956] [0] Setup will discover the installed roles from server object 'CN=EXCH01,CN=Servers,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=Domain,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=domain,DC=priv'.  

[11.14.2022 17:13:37.0957] [0] 'BridgeheadRole' is installed on the server object.  

[11.14.2022 17:13:37.0957] [0] 'ClientAccessRole' is installed on the server object.  

[11.14.2022 17:13:37.0957] [0] 'MailboxRole' is installed on the server object.  

[11.14.2022 17:13:37.0957] [0] 'CafeRole' is installed on the server object.  

[11.14.2022 17:13:37.0957] [0] 'FrontendTransportRole' is installed on the server object.  

[11.14.2022 17:13:37.0960] [0] The installation mode is set to: 'DisasterRecovery'.  

[11.14.2022 17:13:40.0291] [0] An Exchange organization with name 'Domain' was found in this forest.  

[11.14.2022 17:13:40.0291] [0] Active Directory Initialization status : 'True'.  

[11.14.2022 17:13:40.0291] [0] Schema Update Required Status : 'False'.  

[11.14.2022 17:13:40.0292] [0] Organization Configuration Update Required Status : 'False'.  

[11.14.2022 17:13:40.0292] [0] Domain Configuration Update Required Status : 'False'.  

[11.14.2022 17:13:40.0293] [0] The locally installed version is 15.2.1118.7.  

[11.14.2022 17:13:40.0293] [0] Exchange Installation Directory : 'C:\Program Files\Microsoft\Exchange Server\V15'.  

[11.14.2022 17:13:40.0322] [0] Setup will run from path 'C:\Windows\Temp\ExchangeSetup'.  

[11.14.2022 17:13:40.0338] [0] DisasterRecoveryModeDataHandler has 13 DataHandlers  

[11.14.2022 17:13:40.0339] [0] RootDataHandler has 1 DataHandlers  

[11.14.2022 17:13:40.0339] [0] Languages  

[11.14.2022 17:13:40.0339] [0] Mailbox role: Transport service  

[11.14.2022 17:13:40.0341] [0] Mailbox role: Client Access service  

[11.14.2022 17:13:40.0341] [0] Mailbox role: Mailbox service  

[11.14.2022 17:13:40.0342] [0] Management tools  

[11.14.2022 17:13:40.0342] [0] Mailbox role: Client Access Front End service  

[11.14.2022 17:13:40.0343] [0] Mailbox role: Front End Transport service  

[11.14.2022 17:13:40.0350] [0] Validating options for the 6 requested roles  

[11.14.2022 17:13:40.0351] [0] The server cannot be recovered because Setup has detected that Exchange server roles are already installed.  

[11.14.2022 17:13:40.0368] [0] [ERROR] The following server roles are already installed: BridgeheadRole, ClientAccessRole, MailboxRole, FrontendTransportRole, AdminToolsRole, CafeRole.  

[11.14.2022 17:13:40.0368] [0] CurrentResult console.ProcessRunInternal:90: 1  

[11.14.2022 17:13:40.0371] [0] CurrentResult launcherbase.maincore:90: 1  

[11.14.2022 17:13:40.0371] [0] CurrentResult console.startmain:52: 1  

[11.14.2022 17:13:40.0372] [0] CurrentResult SetupLauncherHelper.loadassembly:452: 1  

[11.14.2022 17:13:40.0372] [0] The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.  

[11.14.2022 17:13:40.0373] [0] CurrentResult main.run:235: 1  

[11.14.2022 17:13:40.0373] [0] CurrentResult setupbase.maincore:396: 1  

[11.14.2022 17:13:40.0374] [0] End of Setup  

[11.14.2022 17:13:40.0374] [0] **********************************************

Any idea to find the issue and fix it?

Thanks a lot

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-21*

For the moment same problem.    

I can't repare de replication service etc..    

I don't know if is better to reinstall a new exchange but in DAG environment I don't know if it's a good idea....

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-15*

Try to repare failed installation and I obtain:    

Languages    

Management tools    

Mailbox role: Transport service    

Mailbox role: Client Access service    

Mailbox role: Mailbox service    

Mailbox role: Front End Transport service    

Mailbox role: Client Access Front End service    

Performing Microsoft Exchange Server Prerequisite Check    

```
Configuring Prerequisites                                                                         COMPLETED  
Prerequisite Analysis                                                                             COMPLETED
```

Configuring Microsoft Exchange Server    

```
Language Files                                                                                    COMPLETED  
Restoring Services                                                                                COMPLETED  
Language Configuration                                                                            COMPLETED  
Exchange Management Tools                                                                         COMPLETED  
Mailbox role: Transport service                                                                   COMPLETED  
Mailbox role: Client Access service                                                               COMPLETED  
Mailbox role: Mailbox service                                                                     FAILED
```

The following error was generated when "$error.Clear();    

 start-SetupService -ServiceName MSExchangeRepl    

" was run:    

"Microsoft.Exchange.Configuration.Tasks.ServiceDidNotReachStatusException: Service 'MSExchangeRepl' failed to reach    

status 'Running' on this server.    

 at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception,    

ErrorCategory errorCategory, Object target, String helpUrl)    

 at    

Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory category, Object target)    

 at    

Microsoft.Exchange.Management.Tasks.ManageSetupService.WaitForServiceStatus(ServiceController serviceController,    

ServiceControllerStatus status, Unlimited`1 maximumWaitTime, Boolean ignoreFailures, Boolean     sendWatsonReportForHungService)      at     Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService(ServiceController serviceController, Boolean     ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime, String[] serviceParameters)    

 at Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService(String serviceName, Boolean    

ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime, String[] serviceParameters)    

 at Microsoft.Exchange.Management.Tasks.StartSetupService.InternalProcessRecord()    

 at    

Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()    

 at    

Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean    

terminatePipelineIfFailed)".    

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the    

<SystemDrive>:\ExchangeSetupLogs folder.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-15*

You can check out these links for more help     

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues    

https://community.spiceworks.com/topic/2345089-exchange-offline-after-latest-windows-updates?page=0

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-15*

Hello,    

No. I have the issues and I try to install le CU for try to fix it. It's not a setup fail I think I don't understand why some services are down

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-15*

Hi @Oscar Moyano  ,    

Are you trying to install Exchange 2019 SU and are encountering the above errors while installing?    

Before installing SU, it is a best practice to restart the server and turn off all antivirus software.    

For information about Setup fails and fail to start services, please refer to: exchange-security-update-issues    

Besides, about the install fails and says that it ends prematurely, you can refer to this similar article: 2186309-failed-security-update-for-exchange-server-2019-kb4471389-patch    

The fix was simply logging in with the default Administrator account, ensuring UAC was not getting in the way, and then running the manual download of the patch as Administrator.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
