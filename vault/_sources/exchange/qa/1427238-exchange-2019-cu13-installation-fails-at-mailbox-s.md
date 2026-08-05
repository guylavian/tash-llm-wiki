---
title: "Exchange 2019 CU13 Installation Fails at Mailbox Service Role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1427238/exchange-2019-cu13-installation-fails-at-mailbox-s
question_id: 1427238
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 CU13 Installation Fails at Mailbox Service Role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1427238/exchange-2019-cu13-installation-fails-at-mailbox-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I'm trying to install Exchange 2019, but it stops at install the Mailbox role with access denied error. Admin user performing installation is member of Enterprise Admins, Organization Management and Schema Admins.   

The error happens with windows server 2019 or 2022.  

Any help please?

```
Error:
The following error was generated when "$error.Clear(); 
	install-ExsetdataAtom -AtomName SystemAttendant -DomainController $RoleDomainController

" was run: "Microsoft.Exchange.Management.Deployment.ExsetdataException: An error occurred with error code '3221684229' and message 'Access is denied.'.
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowTerminatingError(Exception exception, ErrorCategory category, Object target)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.HandleExsetdataReturnCode(UInt32 scErr)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.InstallAtom(AtomID atomID)
   at Microsoft.Exchange.Management.Deployment.InstallExsetdataAtom.InternalProcessRecord()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".
```

ExchangeSetup.log

[11/16/2023 11:37:58.0695] [2] Configuring X400 address type for i386 processor.

```
.........
[11/16/2023 11:37:58.0695] [2] Entering ScSetVersionOnAddressTypeObj
[11/16/2023 11:37:58.0961] [2]  ScFindFileInDirTree (k:\dbs\sh\e19dt\0301_091705_0\cmd\j\sources\dev\admin\src\libs\base\basemisc.cxx:1347)
           Error code 0XC0070005 (5): Access is denied.
[11/16/2023 11:37:58.0961] [2]  ScFindFileInDirTree (k:\dbs\sh\e19dt\0301_091705_0\cmd\j\sources\dev\admin\src\libs\base\basemisc.cxx:1347)
           Error code 0XC0070005 (5): Access is denied.
[11/16/2023 11:37:58.0977] [2]  ScSetVersionOnAddressTypeObj (k:\dbs\sh\e19dt\0301_091705_0\cmd\4\sources\dev\admin\src\libs\exsetup\dsmisc.cxx:1008)
           Error code 0XC0070005 (5): Access is denied.
[11/16/2023 11:37:58.0977] [2] Leaving ScSetVersionOnAddressTypeObj
[11/16/2023 11:37:58.0977] [2]  CAtomSystemAttendant::ScSetAddressTypes (k:\dbs\sh\e19dt\0301_091705_0\cmd\1g\sources\dev\admin\src\udog\exsetdata\components\server\a_systemattendant.cxx:246)
           Error code 0XC0070005 (5): Access is denied.
[11/16/2023 11:37:58.0977] [2]  CAtomSystemAttendant::ScAdd (k:\dbs\sh\e19dt\0301_091705_0\cmd\1g\sources\dev\admin\src\udog\exsetdata\components\server\a_systemattendant.cxx:204)
           Error code 0XC0070005 (5): Access is denied.
[11/16/2023 11:37:58.0977] [2] mode = 'Install' (61953) CBaseAtom::ScSetup (k:\dbs\sh\e19dt\0301_091705_0\cmd\1e\sources\dev\admin\src\udog\setupbase\basecomp\baseatom.cxx:537)
           Error code 0XC0070005 (5): Access is denied.
[11/16/2023 11:37:58.0977] [2]  ScSetupAtom (k:\dbs\sh\e19dt\0301_091705_0\cmd\i\sources\dev\admin\src\udog\exsetdata\exsetds.cxx:877)
           Error code 0XC0070005 (5): Access is denied.
[11/16/2023 11:37:58.0977] [2] Leaving ScSetupAtom
[11/16/2023 11:37:58.0977] [2] [ERROR] An error occurred with error code '3221684229' and message 'Access is denied.'.
[11/16/2023 11:37:58.0977] [2] [ERROR] An error occurred with error code '3221684229' and message 'Access is denied.'.
[11/16/2023 11:37:58.0977] [1] The following 1 error(s) occurred during task execution:
[11/16/2023 11:37:58.0977] [1] 0.  ErrorRecord: An error occurred with error code '3221684229' and message 'Access is denied.'.
[11/16/2023 11:37:58.0977] [1] 0.  ErrorRecord: Microsoft.Exchange.Management.Deployment.ExsetdataException: An error occurred with error code '3221684229' and message 'Access is denied.'.
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowTerminatingError(Exception exception, ErrorCategory category, Object target)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.HandleExsetdataReturnCode(UInt32 scErr)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.InstallAtom(AtomID atomID)
   at Microsoft.Exchange.Management.Deployment.InstallExsetdataAtom.InternalProcessRecord()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)
[11/16/2023 11:37:58.0977] [1] [ERROR] The following error was generated when "$error.Clear(); 
	install-ExsetdataAtom -AtomName SystemAttendant -DomainController $RoleDomainController

" was run: "Microsoft.Exchange.Management.Deployment.ExsetdataException: An error occurred with error code '3221684229' and message 'Access is denied.'.
   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowTerminatingError(Exception exception, ErrorCategory category, Object target)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.HandleExsetdataReturnCode(UInt32 scErr)
   at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.InstallAtom(AtomID atomID)
   at Microsoft.Exchange.Management.Deployment.InstallExsetdataAtom.InternalProcessRecord()
   at Microsoft.Exchange.Configuration.Tasks.Task.b__91_1()
   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".
[11/16/2023 11:37:58.0977] [1] [ERROR] An error occurred with error code '3221684229' and message 'Access is denied.'.
[11/16/2023 11:37:58.0977] [1] [ERROR-REFERENCE] Id=LegacyCoreComponent___bff10cd874104b84ade74b02b9036b25 Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup
[11/16/2023 11:37:58.0977] [1] Setup is stopping now because of one or more critical errors.
[11/16/2023 11:37:58.0977] [1] Finished executing component tasks.
[11/16/2023 11:37:58.0992] [1] Ending processing Install-MailboxRole
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-20*

Hi again,  

I solved the problem.  

I was trying to install Exchange on a drive using a windows mount point c:\exchange. A colleague suggested to change it to a drive letter E:\ and create a folder there for installation, and it works!   

I still don't know where those K:\something path are, but the exchange is installed!!  

Thanks for you help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-20*

Hello,

Thank you for your reply. First of all, I want to confirm with you,

I saw a few references to an access denied to drive K: but I don't understand where this drive is.

Did you mean that you have checked all servers in the environment but do not see the K drive?

In addition, based on your feedback, it is recommended that you try to do the following:

Start Windows Explorer, folder options, view tab. Unselected "Hide protected operating system files (Recommended). Then the "System Volume Information" folder was visible in Windows Explorer then selected the "System Volume Information" folder, properties, security tab. System Account was visible with Full Control permissions. At this point you need add the domain account used for running Exchange CU13 setup giving it the "Full Control" permissions. Finally, restart the Exchange 2019 CU13 setup. Through these steps, you should be able to install Exchange 2019 normally.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-17*

Hello @Sysadmin Infarmed  ,

Thank you for providing the detailed information. According to the description, it is first recommended that you run the script to check that your server meets the prerequisites of Exchange Server 2019 and Setup wizard. In addition, please make sure to run the install from elevated CMD, and it is recommended that you may try to run the installation from an Administrator prompt to ensure that the setup has full access to the machine to see if it can be successful.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
