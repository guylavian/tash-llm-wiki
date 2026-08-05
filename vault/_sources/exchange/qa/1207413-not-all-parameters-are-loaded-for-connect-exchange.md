---
title: "Not all parameters are loaded for Connect-ExchangeOnline command when connecting from C# Azure Function"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1207413/not-all-parameters-are-loaded-for-connect-exchange
question_id: 1207413
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-functions", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# Not all parameters are loaded for Connect-ExchangeOnline command when connecting from C# Azure Function

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1207413/not-all-parameters-are-loaded-for-connect-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a code that successfully runs in a console app but fails in Azure Function. We're connecting to Exchange Online from Powershell in C# Azrue Function. It's using .NET 6.0 and Microsoft.PowerShell.SDK 7.1.10. Connection to Exchange Online is made with the latest module of ExchangeOnlineManagement 3.0 and a certificate. When we run "Connect-ExchangeOnline" from Azure Function, we get "System.Management.Automation.ParameterBindingException: A parameter cannot be found that matches parameter name 'XXX'", where all missing parameters are in the following list: {AppId,Certificate,CertificateFilePath,CertificatePassword,CertificateThumbprint,Credential,EnableErrorReporting,LogDirectoryPath,LogLevel,ManagedIdentity,ManagedIdentityAccountId,Organization,PageSize,ShowProgress,TrackPerformance,UseMultithreading,UserPrincipalName}.
Inspecting ExchangeOnlineManagement.psm1 script, we can see that all these parameters are different from other parameters and added using the System.Management.Automation.RuntimeDefinedParameterDictionary. Is there something in Microsoft.NET.Sdk.Functions package that is preventing them from being loaded? Or is it by design?
How can we connect to Exchange Online from Azure Function using a certificate if we can't specify any of needed parameters, such as Organization, CertificateFilePath and AppID?
Sample of the code:

```
var defaultSessionState = InitialSessionState.CreateDefault();
defaultSessionState.ExecutionPolicy = Microsoft.PowerShell.ExecutionPolicy.Unrestricted;
Runspace runspace = RunspaceFactory.CreateRunspace(defaultSessionState);
runspace.Open();
_ps = PowerShell.Create();
_ps.AddScript("Import-Module -Name ExchangeOnlineManagement").Invoke();
var results = _ps.AddScript("(Get-Command Connect-ExchangeOnline).Parameters").Invoke();
```

The last line executed in Azure Function does not return any of the parameters mentioned above.
Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-19*

I'm not sure if this will help, but I obtain my token in C# and then pass it to the script. I don't use a certificate; instead, I use a client ID and client secret. By using C# to obtain my token, I am less dependent on PowerShell. 
Additionally, not deploying it as a zip/package has helped with some other issues.

```
using (PowerShell ps = PowerShell.Create())
{
	ps.Runspace = runspace;
	ps.AddScript("[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12");
	Invoke(ps);

	ps.AddCommand("Connect-ExchangeOnline");
	ps.AddParameters(new Dictionary
	{
		["AccessToken"] = GetToken(),
		["Organization"] = organization

	}); ;

	Invoke(ps);
}
```
