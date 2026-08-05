---
title: "Exchange 2013 services are stuck and can not start"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/297288/exchange-2013-services-are-stuck-and-can-not-start
question_id: 297288
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 services are stuck and can not start

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/297288/exchange-2013-services-are-stuck-and-can-not-start (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

After a failure to install update KB5000871 and restart, all services are stuck and unable to start.  

The following events appear:

Application ID: 1026 .NET Runtime  

Application: FSCConfigurationServer.exe  

Framework Version: v4.0.30319  

Description: The process was terminated due to an unhandled exception.  

Exception Info: System.IO.FileNotFoundException  

at System.Reflection.RuntimeAssembly._nLoad(System.Reflection.AssemblyName, System.String, System.Security.Policy.Evidence, System.Reflection.RuntimeAssembly, System.Threading.StackCrawlMark ByRef, IntPtr, Boolean, Boolean, Boolean)  

at System.Reflection.RuntimeAssembly.InternalLoadAssemblyName(System.Reflection.AssemblyName, System.Security.Policy.Evidence, System.Reflection.RuntimeAssembly, System.Threading.StackCrawlMark ByRef, IntPtr, Boolean, Boolean, Boolean)  

at System.Reflection.RuntimeAssembly.InternalLoadFrom(System.String, System.Security.Policy.Evidence, Byte[], System.Configuration.Assemblies.AssemblyHashAlgorithm, Boolean, Boolean, System.Threading.StackCrawlMark ByRef)  

at System.Reflection.Assembly.LoadFrom(System.String)  

at Microsoft.Forefront.Filtering.Diagnostics.WatsonHelper.Register()  

at <Module>.wWinMain(HINSTANCE__, HINSTANCE__, UInt16*, Int32)  

at <Module>.wWinMainCRTStartup()

Application ID: 1000 Application Error  

Faulting application name: FSCConfigurationServer.exe, version: 15.0.1497.0, time stamp: 0x5cb8f326  

Faulting module name: KERNELBASE.dll, version: 6.3.9600.19724, time stamp: 0x5ec5262a  

Exception code: 0xe0434352  

Fault offset: 0x0000000000007afc  

Faulting process id: 0x257c  

Faulting application start time: 0x01d7106df6977b28  

Faulting application path: C:\Program Files\Microsoft\Exchange Server\V15\FIP-FS\Bin\FSCConfigurationServer.exe  

Faulting module path: C:\Windows\system32\KERNELBASE.dll  

Report Id: 3ckage full name:  

Faulting package-relative application ID:

System ID 7000 Service Control Manager  

The Microsoft Exchange Active Directory Topology service failed to start due to the following error:  

The service did not respond to the start or control request in a timely fashion.

System ID 10010 DistributedCOM  

The server {} did not register with DCOM within the required timeout.

Highly appreciate any help.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Hi @Lucas Liu-MSFT       

We were unable to resolve the issue and installed a new server. I appreciate your assistance

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

Hi @RASH MAAR   ,    

According to the description of the security update for KB6000871. Exchange services might remain in a disable state after you install this security update. Please try to setup the start up type to Automatic and start the affected Exchange services manually.    

For more infomration you could refer to: Description of the security update for Microsoft Exchange Server 2019, 2016, and 2013: March 2, 2021 (KB5000871)    

According to the error infromation, the Microsoft Exchange Active Directory Topology service did not start successfully. Almost all Exchange-related services depend on the Microsoft Exchange Active Directory Topology service. Please follow the method in the link below to increase the value that caused the service timeout. Then restart the computer and try to start the Microsoft Exchange Active Directory Topology service again.    

For more information:  A slow service does not start due to time-out error in Windows    

In addition, incorrectly modifying the registry will cause serious consequences, so please backup in advance: How to back up and restore the registry in Windows    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
