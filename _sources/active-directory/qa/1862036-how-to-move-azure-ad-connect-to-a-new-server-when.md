---
title: "How to move Azure AD Connect to a new server, when the old server is unavailable?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1862036/how-to-move-azure-ad-connect-to-a-new-server-when
question_id: 1862036
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# How to move Azure AD Connect to a new server, when the old server is unavailable?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1862036/how-to-move-azure-ad-connect-to-a-new-server-when (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Moving Azure (Entra) Sync 2.3.20 to a new PC after old machine died.  No backups available on old machine. New machine is Windows server 2019, connect is latest version.  Old machine ran older sync tool.

Software installed, no problem. Gave it tenant admin credentials, it connected. Gave it local AD admin credentials, it connected. 

It fails during the AAD Sync.  Here's the error (i changed the domain to contoso):

[09:09:58.628] [ 40] [ERROR] Creation of connector contoso.onmicrosoft.com - AAD failed. This may be due to replication delay. Retrying after 5 seconds ...

Exception Data (Raw): System.Management.Automation.CmdletInvocationException: An error occurred while sending the request. ---> Microsoft.IdentityManagement.PowerShell.ObjectModel.SynchronizationConfigurationValidationException: An error occurred while sending the request.

   at Microsoft.DirectoryServices.MetadirectoryServices.UI.WebServices.MMSWebService.ValidateConfigurationParameters(Connector connector)

   at Microsoft.DirectoryServices.MetadirectoryServices.UI.WebServices.MMSWebService.CreateConnector(Connector connector, Boolean validate)

   at Microsoft.IdentityManagement.PowerShell.Cmdlet.AddADSyncConnectorCmdlet.ProcessRecord()

   --- End of inner exception stack trace ---

   at System.Management.Automation.Runspaces.PipelineBase.Invoke(IEnumerable input)

   at System.Management.Automation.PowerShell.Worker.ConstructPipelineAndDoWork(Runspace rs, Boolean performSyncInvoke)

   at System.Management.Automation.PowerShell.Worker.CreateRunspaceIfNeededAndDoWork(Runspace rsToUse, Boolean isSync)

   at System.Management.Automation.PowerShell.CoreInvokeHelperTInput,TOutput

   at System.Management.Automation.PowerShell.CoreInvokeTInput,TOutput

   at System.Management.Automation.PowerShell.Invoke(IEnumerable input, PSInvocationSettings settings)

   at Microsoft.Online.Deployment.PowerShell.LocalPowerShell.Invoke()

   at Microsoft.Online.Deployment.PowerShell.PowerShellAdapter.TypeDependencies.InvokePowerShell(IPowerShell powerShell)

   at Microsoft.Online.Deployment.PowerShell.PowerShellAdapter.InvokePowerShellCommand(String commandName, InitialSessionState initialSessionState, IDictionary`2 commandParameters, Boolean isScript)

   at Microsoft.Azure.ActiveDirectory.Synchronization.PowerShellConfigAdapter.ConnectorConfigAdapter.AddConnector(Connector connector)

   at Microsoft.Azure.ActiveDirectory.Synchronization.Config.ConnectorAdapterBase.CreateOrUpdateConnectorCore()

   at Microsoft.Azure.ActiveDirectory.Synchronization.Framework.ActionExecutor.Execute(Action action, String description)

   at Microsoft.Azure.ActiveDirectory.Synchronization.Config.ConnectorAdapterBase.CreateOrUpdateConnector(IEnumerable`1 objectClassInclusions, IEnumerable`1 attributeNameInclusions, ParameterKeyedCollection connectorGlobalParameters, Boolean createRunProfile)

   at Microsoft.Online.Deployment.Types.Providers.SyncDataProvider.CreateConnectorWithRetry(ConnectorAdapterBase connectorAdapter, IEnumerable`1 objectClassInclusions, IEnumerable`1 attributeNameInclusions, ParameterKeyedCollection connectorGlobalParameters, Boolean createRunProfile)

## Answers

_No answers on this thread._
