---
title: "Exchange Server 2016 - EWS terminated"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1805222/exchange-server-2016-ews-terminated
question_id: 1805222
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2016 - EWS terminated

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1805222/exchange-server-2016-ews-terminated (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have 2 Exchange Server 2016 (DAG) and EWS terminated on both server every minute with following error:

An unhandled exception occurred and the process was terminated.

Application ID: /LM/W3SVC/2/ROOT/EWS

Process ID: 14160

Exception: System.MissingMethodException

Message: Method not found: 'Microsoft.Exchange.WebServices.Data.GetClientExtensionResponse Microsoft.Exchange.WebServices.Data.ExchangeService.GetClientExtension(Microsoft.Exchange.WebServices.Data.StringList, Boolean, Boolean, System.String, Microsoft.Exchange.WebServices.Data.StringList, Microsoft.Exchange.WebServices.Data.StringList, Boolean, Boolean)'.

StackTrace:    at Microsoft.Exchange.Data.ApplicationLogic.Extension.EwsOrgExtensionRetriever.<>c__DisplayClass5_0.<Retrieve>b__0()

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.OrgExtensionTable.ExecuteWebServicesAction(Action webServicesAction)

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.EwsOrgExtensionRetriever.Retrieve(OrgExtensionRetrievalContext context)

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.CachedOrgExtensionRetriever.Retrieve(OrgExtensionRetrievalContext context)

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.OrgExtensionDataGetter.GetAllOrgExtensionData(OrgExtensionRetrievalContext context)

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.OrgExtensionTable.GetOrgExtensions(IOrgExtensionDataGetter orgExtensionDataGetter, OrgExtensionRetrievalContext retrievalContext, Boolean shouldRetrievePrivateCatalogExtensions, Boolean retrieveOnly1_0)

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.InstalledExtensionTable.GetOrgProvidedExtensions(HashSet`1 requestedExtensions, Boolean shouldReturnEnabledOnly, Dictionary`2 masterTableExtensions, Boolean isDebug, Boolean shouldRetrievePrivateCatalogExtensions, String& orgMasterTableRawXml, Boolean shouldReturnECPAddins)

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.InstalledExtensionTable.GetProvidedExtensions(HashSet`1 requestedExtensions, Boolean shouldReturnEnabledOnly, Dictionary`2 masterTableExtensions, Boolean isDebug, Boolean shouldRetrievePrivateCatalogExtensions, String& orgMasterTableRawXml, Boolean shouldReturnECPAddins)

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.InstalledExtensionTable.GetExtensions(HashSet`1 requestedExtensions, Boolean shouldReturnEnabledOnly, Boolean shouldFailOnGetOrgExtensionsTimeout, Boolean isDebug, String& orgMasterTableRawXml, CultureInfo culture, Boolean filterOutDuplicateMasterTableExtensions, Boolean shouldRetrievePrivateCatalogExtensions, MultiValuedProperty`1 capabilities, Boolean shouldReturnECPAddins)

   at Microsoft.Exchange.Services.Wcf.GetExtensibilityContext.GetExtensions(ICallContext callContext, Boolean isUserScope, Boolean shouldReturnEnabledOnly, Boolean shouldFailOnGetOrgExtensionsTimeout, OrgEmptyMasterTableCache orgEmptyMasterTableCache, ExtensionsCache extensionsCache, HashSet`1 requestedExtensions, Boolean isRawXmlRequired, Boolean shouldRetrievePrivateCatalogExtensions, Nullable`1 orgExtensionVersion, Boolean checkForExpiryOfUserCacheOfOrgExtensions, String& masterTableRawXml, Boolean retrieveOnly1_0, Boolean filterOutDuplicateMasterTableExtensions, Version apiVersionSupported, Boolean shouldReturnECPAddins)

   at Microsoft.Exchange.Services.Core.GetAppManifests.GetExtensionDataList(HashSet`1 privateCatalogAddIns, Version schemaVersionSupported, Boolean shouldIncludeAllInstalledAddIns, Boolean shouldReturnECPAddins)

   at Microsoft.Exchange.Services.Core.GetAppManifests.<>c__DisplayClass12_0.<ExecuteGetAppManifests>b__0()

   at Microsoft.Exchange.Data.ApplicationLogic.Extension.InstalledExtensionTable.RunClientExtensionAction(Action action)

   at Microsoft.Exchange.Services.Wcf.GetExtensibilityContext.RunClientExtensionAction(Action action, Exception& exception)

   at Microsoft.Exchange.Services.Core.GetAppManifests.ExecuteGetAppManifests(Exception& clientExtensionException)

   at Microsoft.Exchange.Services.Core.GetAppManifests.Execute()

   at Microsoft.Exchange.Services.Core.ExceptionHandler`1.Execute(IRequestDetailsLogger logger, CreateServiceResult createServiceResult, Int32 index, ExecutionOption executionOption)

   at Microsoft.Exchange.Services.Core.BaseStepServiceCommand`3.InternalExecuteStep(Boolean& isBatchStopResponse)

   at Microsoft.Exchange.Services.Core.ServiceCommandBase`1.<ExecuteStep>b__82_0()

   at Microsoft.Exchange.Services.Core.ServiceCommandBase`1.<>c__DisplayClass88_0.<ExecuteHelper>b__0()

   at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Action`1 catchDelegate)

   at Microsoft.Exchange.Services.Core.ServiceDiagnostics.SendWatsonReportOnUnhandledException(ICallContext callContext, Action methodDelegate)

   at Microsoft.Exchange.Services.Core.ServiceCommandBase`1.ExecuteHelper(Func`1 action)

   at Microsoft.Exchange.Services.Core.Types.ServiceTask`1.<>c__DisplayClass11_0.<ExecuteHelper>b__0()

   at Microsoft.Exchange.Common.IL.ILUtil.DoTryFilterCatch(Action tryDelegate, Func`2 filterDelegate, Action`1 catchDelegate)

   at Microsoft.Exchange.Services.Core.Types.BaseServiceTask`1.SendWatsonReportOnGrayException(Action callback, Action exceptionHandlerCallback, Boolean isGrayExceptionTaskFailure)

   at Microsoft.Exchange.Services.Core.Types.ServiceTask`1.ExecuteHelper(Func`1 multiStepAction)

   at Microsoft.Exchange.Services.Core.Types.ServiceTask`1.<InternalExecute>b__7_0()

   at Microsoft.Exchange.Diagnostics.RequestDetailsLoggerBase`1.TrackLatency[TResult](Enum latencyMetadata, Func`1 method)

   at Microsoft.Exchange.Diagnostics.RequestDetailsLoggerBase`1.TrackLatency[TResult](Enum latencyMetadata, Func`1 method, Double& latencyValue)

   at Microsoft.Exchange.Services.Core.Types.ServiceTask`1.InternalExecute(TimeSpan queueAndDelay, TimeSpan totalTime)

   at Microsoft.Exchange.Services.Core.Types.BaseServiceTask`1.<>c__DisplayClass33_0.<Execute>b__0()

   at Microsoft.Exchange.Services.Core.Types.BaseServiceTask`1.LocalTimedCall(Action action)

   at Microsoft.Exchange.Services.Core.Types.BaseServiceTask`1.ExecuteWithinCallContext(Action action)

   at Microsoft.Exchange.Services.Core.Types.BaseServiceTask`1.Execute(TimeSpan queueAndDelayTime, TimeSpan totalTime)

   at Microsoft.Exchange.Services.Core.Types.BaseServiceTask`1.ExecuteLoop(Boolean synchronously)

   at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)

   at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state, Boolean preserveSyncCtx)

   at System.Threading.QueueUserWorkItemCallback.System.Threading.IThreadPoolWorkItem.ExecuteWorkItem()

   at System.Threading.ThreadPoolWorkQueue.Dispatch()

Can any help me?

thanks

Regards

Andreas

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-10*

Hi @Andreas Sinn,

Welcome to the Microsoft Q&A platform!

According to your description, you are currently experiencing a "System.MissingMethodException" error, which means there is a difference between the versions of the referenced assemblies, which is usually the result of an update or file mismatch. You can try to solve the problem by following the steps below:

-  Verify and Update Exchange CU:

   Ensure that both of your Exchange 2016 servers are running the same Cumulative Update (CU). You can check the current CU by running the following command in the Exchange Management Shell:

   Get-ExchangeServer | Format-List Name,Edition,AdminDisplayVersion

   If they are not on the same CU, update them accordingly. You can download the latest CU from Microsoft's official site.

-  Check for .NET Framework Compatibility:

   Ensure that the .NET Framework version installed on your servers is compatible with the CU of Exchange 2016 you have. Exchange 2016 CU18 and later require .NET Framework 4.8.

   You can verify the installed .NET version by checking the registry:

   Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full' -Name Release

   Compare the release value to the .NET Framework versions listed on Microsoft's documentation to ensure compatibility.

-  Validate Web.Config and Exchange Services:

   Ensure that the EWS virtual directory is correctly configured:

   Get-WebServicesVirtualDirectory | Format-List name, url

   Also, check and compare the `web.config` file for EWS on both servers. There may be customizations or discrepancies leading to the issue.

-  Cleanup and Verify DLLs:

   The error might be due to the presence of incorrect or outdated DLLs.

   - Navigate to the Exchange bin directory (usually `C:\Program Files\Microsoft\Exchange Server\V15\Bin`), and ensure that all the DLLs are the correct version.

   - Compare the `Microsoft.Exchange.WebServices.dll` versions between the two servers to ensure consistency.

-  Event Logs:

   Check the Application and System event logs for any additional errors or warnings that may provide more context. Sometimes, the root cause will be logged there.

-  Re-create Virtual Directories:

   If the issue persists, you might need to re-create the EWS virtual directory. Here’s how you can do that:

   Remove-WebServicesVirtualDirectory -Identity "ServerName\EWS (Default Web Site)"

   New-WebServicesVirtualDirectory -Server "ServerName" -InternalUrl "https://mail.contoso.com/EWS/Exchange.asmx"

   Ensure to replace "ServerName" with your actual server name, and adjust the `InternalUrl` as per your environment.

-  Post-Update Maintenance:

   Run the Exchange server post-update scripts to ensure that everything is correctly configured.

   (Get-ChildItem 'C:\Program Files\Microsoft\Exchange Server\V15\Scripts' -Filter "Update-*.ps1").FullName | ForEach-Object { & "$_" }

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
