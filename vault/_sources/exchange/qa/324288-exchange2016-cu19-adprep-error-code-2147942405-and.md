---
title: "Exchange2016 CU19 Adprep error code '2147942405' and message 'Access denied."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/324288/exchange2016-cu19-adprep-error-code-2147942405-and
question_id: 324288
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange2016 CU19 Adprep error code '2147942405' and message 'Access denied.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/324288/exchange2016-cu19-adprep-error-code-2147942405-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team, We have an Exchange 2016 CU15 DAG running 2 Servers.We are in the process of Ugrading to CU19,Schema Update went fine, But we are struck at prepareAD with the following error message.   

Microsoft Exchange Server 2016 Cumulative Update 19 Unattended Setup Copying Files... File copy complete. Setup will now collect additional information needed for installation. Performing Microsoft Exchange Server Prerequisite Check Prerequisite Analysis COMPLETED Configuring Microsoft Exchange Server Organization Preparation FAILED The following error was generated when "$error.Clear(); buildToBuildUpgrade-ExsetDataAtom -AtomName OrgLevelCt -DomainController $RoleDomainController " was run: "Microsoft.Exchange.Management.Deployment.ExsetdataException: An error occurred with ****error code '2147942405' and message 'Access denied.'. at Microsoft.Exchange.Configuration.Tasks.Task.ThrowTerminatingError(Exception exception, ErrorCategory category, Object target) at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.HandleExsetdataReturnCode(UInt32 scErr) at Microsoft.Exchange.Management.Deployment.ManageExsetdataAtom.BuildToBuildUpgradeAtom(AtomID atomID) at Microsoft.Exchange.Management.Deployment.BuildToBuildUpgradeExsetdataAtom.InternalProcessRecord() at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1() at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)". The Exchange Server setup operation didn't complete. More details can be found in ExchangeSetup.log located in the <SystemDrive>:\ExchangeSetupLogs folder.  

 We tried to Uninstall AV but receive the same error message. User Running setup using elevated cmd is part of SchemaAdmins,EnterpriseAdmins,DomainAdmins,ExchangeOrganizationManagement.   

Looking for help to resolve the issue.   

Thanks and Regards

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-22*

Hi @NajmulHasan Mohammed   ,    

Have you set the server into maintenance mode?    

Installing Cumulative Updates on Exchange Server 2016    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Please give your account a full control permission of the existed Exchange folder(Exchange server or V15) to test if it's because of there are some files that you have no access rights.    

You could try using the Setup.exe to do the preparation(open as admin) or check the SetupLogs in that folder.    

Note: Kindly suggest that you can install the CU20 instead, since the CU19 has no Security Updates included, so you'll have to manually install that, also there are some issues are fixed you could find here: Cumulative Update 20 for Exchange Server 2016    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
