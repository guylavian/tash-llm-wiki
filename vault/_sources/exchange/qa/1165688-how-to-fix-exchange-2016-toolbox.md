---
title: "How to fix Exchange 2016 Toolbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1165688/how-to-fix-exchange-2016-toolbox
question_id: 1165688
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# How to fix Exchange 2016 Toolbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1165688/how-to-fix-exchange-2016-toolbox (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have just installed the latest the latest CU23 and run the HealthChecker.ps1 and fixed all problems but now the Exchange Toolbox does not work, The Exchange PowerShell works fine, the shell is set to remote signed, i have the latest visual 2013 and 2012 installed, i have even install the management tools on my computer all i get is

FX:{714FA079-DC14-470f-851C-B7EAAA4177C1}

```
Deserialization fails: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.InvalidOperationException: The process 'mmc' (PID = 18252) has been initialized as Unknown Multiple instance type un-expectedly. 
 Reasons of this exception: 1. For any product executables, which will be shipped out of box, they should never use AD driver functionality without initializing its performance counter instance since we can NOT show a intuitive Perf Counter instance name here.
 2. We don't need the validation for test assembly because we don't care for its performance counter naming; however, we definitely want to make sure it is under our control, so that we don't miss any out of box product DLLs/EXEs.
 What to do to avoid this exception: For any newly added Exchange test executables which utilize AD perf, please add the executable name of the process into exclusion list in Microsoft.Exchange.Data.Directory.Globals.CheckExchangeTestExecutables.
   at Microsoft.Exchange.Data.Directory.Globals.InitializePerfCounterInstance(String applicationName, Boolean hasMultiInstance, Action`1 logStage)
   at Microsoft.Exchange.Data.Directory.Globals.InitializeUnknownPerfCounterInstance()
   at Microsoft.Exchange.Data.Directory.ADProviderPerf.AddDCInstance(String serverName)
   at Microsoft.Exchange.Data.Directory.LdapConnectionPool.CreateOneTimeConnection(NetworkCredential networkCredential, ADServerInfo serverInfo, LocatorFlags connectionFlags)
   at Microsoft.Exchange.Data.Directory.LdapTopologyProvider.GetDirectoryServer(String partitionFqdn, ADRole role)
   at Microsoft.Exchange.Data.Directory.LdapTopologyProvider.InternalGetServersForRole(String partitionFqdn, IList`1 currentlyUsedServers, ADServerRole role, Int32 serversRequested, Boolean forestWideAffinityRequested)
   at Microsoft.Exchange.Data.Directory.LdapTopologyProvider.GetConfigDCInfo(String partitionFqdn, Boolean throwOnFailure)
   at Microsoft.Exchange.Data.Directory.TopologyProvider.PopulateConfigNamingContexts(String partitionFqdn)
   at Microsoft.Exchange.Data.Directory.TopologyProvider.GetConfigurationNamingContext(String partitionFqdn)
   at Microsoft.Exchange.Data.Directory.SystemConfiguration.ADSystemConfigurationSession.GetRootOrgContainer(String partitionFqdn, String domainController, NetworkCredential credential)
   at Microsoft.Exchange.Data.Directory.SystemConfiguration.ADSystemConfigurationSession.GetRootOrgContainerId(String partitionFqdn, String domainController, NetworkCredential credential)
   at Microsoft.Exchange.Data.Directory.SystemConfiguration.ADConfigurationSession.GetOrgContainerId(String callerFilePath, Int32 callerFileLine, String memberName)
   at Microsoft.Exchange.Security.OAuth.KernelModeConfigurationReader.<>c__DisplayClass7_1.b__0()
   at Microsoft.Exchange.Data.Directory.ADNotificationAdapter.RunADOperation(ADOperation adOperation, Int32 retryCount)
   at Microsoft.Exchange.Data.Directory.ADNotificationAdapter.TryRunADOperation(ADOperation adOperation, Int32 retryCount)
   at Microsoft.Exchange.Security.OAuth.KernelModeConfigurationReader.LoadConfiguration(Boolean loadOnlineCertificates)
   at Microsoft.Exchange.Security.OAuth.Common.ConfigProviderBase.ManualLoadIfNecessary()
   at Microsoft.Exchange.Security.OAuth.Common.ConfigProviderBase.get_Configuration()
   at Microsoft.Exchange.Security.Authentication.Utility.GetCertificates()
   at Microsoft.Exchange.Security.Authentication.Utility.SafeGetCertificates()
   --- End of inner exception stack trace ---
   at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor)
   at System.Reflection.RuntimeMethodInfo.UnsafeInvokeInternal(Object obj, Object[] parameters, Object[] arguments)
   at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture)
   at Microsoft.Exchange.Data.Common.CertificateDataHelper.GetProtectionCertificates()
   at Microsoft.Exchange.Data.Common.HmacCryptoProvider.GetHmacProvider(X509Certificate2[] x509Certificate2s)
   at Microsoft.Exchange.Data.Common.HmacCryptoProvider.VerifyMessage(X509Certificate2[] x509Certificate2s, Byte[] hmac, Byte[] message)
   at Microsoft.Exchange.Data.SerializationTypeConverter.VerifySerializationDataAndGetOriginalSerializationData(Byte[] serializationData)
   at Microsoft.Exchange.Data.SerializationTypeConverter.DeserializeObject(Object sourceValue, Type destinationType)
```

Any help would be greatly appreciated.

## Answers

_No answers on this thread._
