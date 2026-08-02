---
title: "Exchange 2019 Installation Fails at Mailbox Service Role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/306122/exchange-2019-installation-fails-at-mailbox-servic
question_id: 306122
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Exchange 2019 Installation Fails at Mailbox Service Role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/306122/exchange-2019-installation-fails-at-mailbox-servic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Installing Exchange 2019 on Server 2019 Datacenter. Unable to install the Mailbox role. Error refers to SystemAttendant and access denied. Admin user performing installation is member of Enterprise Admins, Organization Management and Schema Admins. I have tried deleting the registry entries Watermark and Action. I am unable to uninstall and start over because this installation is incomplete.

Output from Administrator: PowerShell window  

PS H:\> cd d:  

PS D:\>  

.\Setup.exe /IAcceptExchangeServerLicenseTerms /mode:Install /r:MB

Microsoft Exchange Server 2019 Cumulative Update 8 Unattended Setup

Copying Files...  

File copy complete. Setup will now collect additional information needed for installation.

Languages  

Mailbox role: Transport service  

Mailbox role: Client Access service  

Mailbox role: Mailbox service  

Mailbox role: Front End Transport service  

Mailbox role: Client Access Front End service

Performing Microsoft Exchange Server Prerequisite

Check Configuring Prerequisites COMPLETED  

Prerequisite Analysis COMPLETED

Configuring Microsoft Exchange Server  

Preparing Setup COMPLETED  

Stopping Services COMPLETED  

Copying Exchange Files COMPLETED  

Language Files COMPLETED  

Restoring Services COMPLETED  

Language Configuration COMPLETED  

Mailbox role: Transport service COMPLETED  

Mailbox role: Client Access service COMPLETED  

Mailbox role: Mailbox service FAILED

The following error was generated when "$error.Clear();  

install-ExsetdataAtom -AtomName SystemAttendant  

-DomainController $RoleDomainController

" was run: "Microsoft.Exchange.Management.Deployment.ExsetdataException: An error occurred with error code '3221684229' and message 'Access is denied.'.  

at  

Microsoft.Exchange.Configuration.Tasks.Task.ThrowTerminatingError(Exception exception, ErrorCategory category, Object target) at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.HandleExsetdataReturnCode(UInt32 scErr)  

at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.InstallAtom(AtomID atomID)  

at Microsoft.Exchange.Management.Deployment.InstallExsetdataAtom.InternalProcessRecord()  

at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()  

at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.

Adding this 2019 installation to an existing 2016 environment.  

Any recommendations appreciated.

--Steve

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-15*

Hi,   

I have the exact same problem and none of the links provided solves the problem.   

Does anyone have a solution for this?  

Thanks  

Carlos Baptista

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-10*

Seems a permission issue, would you try the solutions in the following links:    

Exchange Server Troubleshooting: Unable to upgrade with error code '3221684229'    

update Exchange 2016 to CU 9, update Mailbox Role Access Denied Error?    

Exchange Service Pack or Rollup or Cumulative Update fails with error code '3221684229' and message 'Access is denied.'    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
