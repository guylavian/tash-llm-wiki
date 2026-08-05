---
title: "Exchange 2019 installation error on /prepareAD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1222341/exchange-2019-installation-error-on-preparead
question_id: 1222341
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 installation error on /prepareAD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1222341/exchange-2019-installation-error-on-preparead (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is first installation of Exchange 2019 CU12 in organization. setup with /PrepareSchema key passes fine. But on /PrepareAD I'v got this error.  

```
[04/11/2023 15:49:06.0926] [2] The schema version identified for the Server is 17003
[04/11/2023 15:49:06.0926] [2] Leaving ScGetSchemaVersion
[04/11/2023 15:49:06.0926] [2] Leaving CDirectoryManager::ScSchemaIsUpToDate
[04/11/2023 15:49:06.0926] [2] Entering CDirectoryManager::ScGetCountOfOrgsInDomain
[04/11/2023 15:49:06.0926] [2]  CDirectoryManager::ScGetCountOfOrgsInDomain (d:\dbs\sh\e19dt\0325_143417\cmd\b\sources\dev\admin\src\udog\setupbase\tools\dsmgr.cxx:495)
           Error code 0X8007200A (8202): The specified directory service attribute or value does not exist.
[04/11/2023 15:49:06.0926] [2] Leaving CDirectoryManager::ScGetCountOfOrgsInDomain
[04/11/2023 15:49:06.0926] [2]  CDirectoryManager::ScGetOrgLevelObjectStatus (d:\dbs\sh\e19dt\0325_143417\cmd\b\sources\dev\admin\src\udog\setupbase\tools\dsmgr.cxx:538)
           Error code 0X8007200A (8202): The specified directory service attribute or value does not exist.
[04/11/2023 15:49:06.0926] [2] Leaving CDirectoryManager::ScGetOrgLevelObjectStatus
[04/11/2023 15:49:06.0926] [2]  CDirectoryManager::ScReInitWithDC (d:\dbs\sh\e19dt\0325_143417\cmd\b\sources\dev\admin\src\udog\setupbase\tools\dsmgr.cxx:269)
           Error code 0X8007200A (8202): The specified directory service attribute or value does not exist.
[04/11/2023 15:49:06.0926] [2] Leaving CDirectoryManager::ScReInitWithDC
[04/11/2023 15:49:06.0926] [2]  ScInitializeManagedCodeContext (d:\dbs\sh\e19dt\0325_143417\cmd\1k\sources\dev\admin\src\udog\exsetdata\exsetds.cxx:380)
           Error code 0X8007200A (8202): The specified directory service attribute or value does not exist.
[04/11/2023 15:49:06.0926] [2]  ScSetupAtom (d:\dbs\sh\e19dt\0325_143417\cmd\1k\sources\dev\admin\src\udog\exsetdata\exsetds.cxx:877)
           Error code 0X8007200A (8202): The specified directory service attribute or value does not exist.
[04/11/2023 15:49:06.0926] [2] Leaving ScSetupAtom
[04/11/2023 15:49:06.0926] [2] [ERROR] An error occurred with error code '2147950602' and message 'The specified directory service attribute or value does not exist.'.
[04/11/2023 15:49:06.0926] [2] [ERROR] An error occurred with error code '2147950602' and message 'The specified directory service attribute or value does not exist.'.
[04/11/2023 15:49:06.0973] [1] The following 1 error(s) occurred during task execution:
[04/11/2023 15:49:06.0973] [1] 0.  ErrorRecord: An error occurred with error code '2147950602' and message 'The specified directory service attribute or value does not exist.'.
[04/11/2023 15:49:06.0973] [1] 0.  ErrorRecord: Microsoft.Exchange.Management.Deployment.ExsetdataException: An error occurred with error code '2147950602' and message 'The specified directory service attribute or value does not exist.'.
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowTerminatingError(Exception exception, ErrorCategory category, Object target)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.HandleExsetdataReturnCode(UInt32 scErr)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.InstallAtom(AtomID atomID)
   at Microsoft.Exchange.Management.Deployment.InstallExsetdataAtom.InternalProcessRecord()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)
[04/11/2023 15:49:06.0973] [1] [ERROR] The following error was generated when "$error.Clear(); 
	install-ExsetDataAtom -AtomName OrgLevelCt -DomainController $RoleDomainController -Organization $RoleOrganizationName

" was run: "Microsoft.Exchange.Management.Deployment.ExsetdataException: An error occurred with error code '2147950602' and message 'The specified directory service attribute or value does not exist.'.
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowTerminatingError(Exception exception, ErrorCategory category, Object target)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.HandleExsetdataReturnCode(UInt32 scErr)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.InstallAtom(AtomID atomID)
   at Microsoft.Exchange.Management.Deployment.InstallExsetdataAtom.InternalProcessRecord()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".
[04/11/2023 15:49:06.0973] [1] [ERROR] An error occurred with error code '2147950602' and message 'The specified directory service attribute or value does not exist.'.
[04/11/2023 15:49:06.0973] [1] [ERROR-REFERENCE] Id=CommonGlobalConfig___a79d51e9e9424d53a462c1254e1ecece Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup
[04/11/2023 15:49:06.0973] [1] Setup is stopping now because of one or more critical errors.
[04/11/2023 15:49:06.0973] [1] Finished executing component tasks.
[04/11/2023 15:49:06.0989] [1] Ending processing Install-ExchangeOrganization
[04/11/2023 15:49:06.0989] [0] CurrentResult console.ProcessRunInternal:198: 1
[04/11/2023 15:49:06.0989] [0] CurrentResult launcherbase.maincore:90: 1
[04/11/2023 15:49:06.0989] [0] CurrentResult console.startmain:52: 1
[04/11/2023 15:49:06.0989] [0] CurrentResult SetupLauncherHelper.loadassembly:452: 1
[04/11/2023 15:49:06.0989] [0] The Exchange Server setup operation didn't complete.  More details can be found in ExchangeSetup.log located in the :\ExchangeSetupLogs folder.
[04/11/2023 15:49:06.0989] [0] CurrentResult main.run:235: 1
[04/11/2023 15:49:06.0989] [0] The registry key, HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\V15\Setup, wasn't found.
[04/11/2023 15:49:06.0989] [0] CurrentResult setupbase.maincore:396: 1
[04/11/2023 15:49:06.0989] [0] End of Setup
[04/11/2023 15:49:06.0989] [0] **********************************************
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-13*

Hi Евгений Зубков
   

There are many possible reasons for your error message, you can follow the below steps to troubleshoot:

-  Verify that your Active Directory meets the network and directory server requirements for Exchange 2019, please refer to: Exchange Server 2019 requirements

-  Check the ADUC and make sure your account is a member of the Enterprise Admins security group and Schema Admins group. If yes, check the ADSI Edit to see if there are any "Deny" for Authenticated Users permissions. As below:
   

-  Make sure your server has the latest security updates and patches installed.    

Related thread you can refer to: Exchange 2013 Setup /Preparead failure  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
