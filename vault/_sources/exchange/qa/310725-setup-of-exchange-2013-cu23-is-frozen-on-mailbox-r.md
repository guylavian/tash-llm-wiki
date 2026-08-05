---
title: "Setup of Exchange 2013 CU23 is frozen on Mailbox Role: Transport Service"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310725/setup-of-exchange-2013-cu23-is-frozen-on-mailbox-r
question_id: 310725
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Setup of Exchange 2013 CU23 is frozen on Mailbox Role: Transport Service

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310725/setup-of-exchange-2013-cu23-is-frozen-on-mailbox-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In lights of the Hafnium hack, I am upgrading our Exchange 2013 DAG cluster to 2013 CU23 from CU19 and then apply the security patch. However I was once again remembered today why I dislike upgrading Exchange so much...

The first server in the DAG upgraded flawlessly. Put it in maintenance mode, installed .NET 4.8 and C++ redist 2013, prepared AD schema etc. and then started the CU23 setup. Within an hour it was done installing and then I applied the Hafnium patch. Upon completion, I took it out of maintenance mode and it worked like a charm.

The second Exchange server in my DAG however is a completely different story. I followed the same procedure: Moved all mailbox databases to the first Exchange server, put the second exchange in maintenance mode, installed .NET 4.8 and c++ redist 2013, did a reboot of the server and then started the CU23 setup. The setup itself is not throwing any error messages, but it has been sitting in the same spot for the past 6 hours: Step 9 of 17: Mailbox Role: Transport Service: 54%. It does not go beyond the 54% mark.

Upon checking my task manager I did notice that .NET optimization service is consuming a lot of CPU. Upon checking the eventvwr, I noticed many warning messages Event ID: 1310

Event code: 3008  

Event message: A configuration error has occurred.  

Event time: 3/11/2021 5:15:03 PM  

Event time (UTC): 3/12/2021 12:15:03 AM  

Event ID: a4ad6357af7d4a979fd0f984e2812d96  

Event sequence: 1  

Event occurrence: 1  

Event detail code: 0

Application information:  

Application domain: /LM/W3SVC/1/ROOT/Autodiscover-21-132599817036183493  

Trust level: Full  

Application Virtual Path: /Autodiscover  

Application Path: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\Autodiscover\  

Machine name: x

Process information:  

Process ID: 4276  

Process name: w3wp.exe  

Account name: NT AUTHORITY\SYSTEM

Exception information:  

Exception type: ConfigurationErrorsException  

Exception message: Could not load file or assembly 'Microsoft.Exchange.Data.Directory, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified. (C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\Autodiscover\web.config line 39)  

at System.Web.Configuration.CompilationSection.LoadAssemblyHelper(String assemblyName, Boolean starDirective)  

at System.Web.Configuration.CompilationSection.LoadAssembly(AssemblyInfo ai)  

at System.Web.Compilation.BuildManager.GetReferencedAssemblies(CompilationSection compConfig)  

at System.Web.Compilation.BuildManager.GetPreStartInitMethodsFromReferencedAssemblies()  

at System.Web.Compilation.BuildManager.CallPreStartInitMethods(String preStartInitListPath, Boolean& isRefAssemblyLoaded)  

at System.Web.Compilation.BuildManager.ExecutePreAppStart()  

at System.Web.Hosting.HostingEnvironment.Initialize(ApplicationManager appManager, IApplicationHost appHost, IConfigMapPathFactory configMapPathFactory, HostingEnvironmentParameters hostingParameters, PolicyLevel policyLevel, Exception appDomainCreationException)

Could not load file or assembly 'Microsoft.Exchange.Data.Directory, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.  

at System.Reflection.RuntimeAssembly._nLoad(AssemblyName fileName, String codeBase, Evidence assemblySecurity, RuntimeAssembly locationHint, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)  

at System.Reflection.RuntimeAssembly.InternalLoadAssemblyName(AssemblyName assemblyRef, Evidence assemblySecurity, RuntimeAssembly reqAssembly, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)  

at System.Reflection.RuntimeAssembly.InternalLoad(String assemblyString, Evidence assemblySecurity, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean forIntrospection)  

at System.Reflection.RuntimeAssembly.InternalLoad(String assemblyString, Evidence assemblySecurity, StackCrawlMark& stackMark, Boolean forIntrospection)  

at System.Reflection.Assembly.Load(String assemblyString)  

at System.Web.Configuration.CompilationSection.LoadAssemblyHelper(String assemblyName, Boolean starDirective)

Request information:  

Request URL: https://x:443/autodiscover/autodiscover.xml  

Request path: /autodiscover/autodiscover.xml  

User host address: x  

User:  

Is authenticated: False  

Authentication Type:  

Thread account name: NT AUTHORITY\SYSTEM

Thread information:  

Thread ID: 13  

Thread account name: NT AUTHORITY\SYSTEM  

Is impersonating: False  

Stack trace: at System.Web.Configuration.CompilationSection.LoadAssemblyHelper(String assemblyName, Boolean starDirective)  

at System.Web.Configuration.CompilationSection.LoadAssembly(AssemblyInfo ai)  

at System.Web.Compilation.BuildManager.GetReferencedAssemblies(CompilationSection compConfig)  

at System.Web.Compilation.BuildManager.GetPreStartInitMethodsFromReferencedAssemblies()  

at System.Web.Compilation.BuildManager.CallPreStartInitMethods(String preStartInitListPath, Boolean& isRefAssemblyLoaded)  

at System.Web.Compilation.BuildManager.ExecutePreAppStart()  

at System.Web.Hosting.HostingEnvironment.Initialize(ApplicationManager appManager, IApplicationHost appHost, IConfigMapPathFactory configMapPathFactory, HostingEnvironmentParameters hostingParameters, PolicyLevel policyLevel, Exception appDomainCreationException)

this is only one example. I have a whole bunch of these messages in my eventviewer complaining about could not load file or assembly. All of them of which have issues in the httpproxy subfolders. I already tried many different things including copying over the SharedWebConfig from my working Exchange server into this HttpProxy folder but to no avail. The setup is just stuck and won't report anything other than the warnings in eventviewer. There are also no Exchange setup logs which makes it even more difficult to say anything.

Anyone else encountered this problem? Client is running fine on one Exchange server now but we need to the second server up and running again.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-20*

For anyone who is wondering or is in the same situation, I went through the Microsoft article today with a Microsoft tech: https://learn.microsoft.com/en-us/exchange/recover-a-database-availability-group-member-server-exchange-2013-help    

It was literally as easy and straight forward as that.    

-  Deploy a new VM with the same OS, same computer name, same IP addresses and same hard drives    

-  Remove database copies from old server    

-  Remove old server from DAG    

-  Evict old server from Failover cluster    

-  Reset computer account in AD    

-  Join new server to AD domain with the exact same computer name as the old server you're replacing    

-  Install Exchange with the /m:RecoverServer switch    

-  When done, reconfigure your External URLs for virtual directories and reimport your SSL certificate    

-  Add new server to DAG cluster    

-  Add mailbox database copies to new server and let it seed    

It was as simple as that! Big relief.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Thanks for the response. After some thorough checks we actually found out that this server did get compromised by the Hafnium hack. I immediately put the server into maintenance mode in the DAG cluster and disconnected it from the network. Our first Exchange server that is already fully upgraded is confirmed clean.  

I have no intentions of ever bringing this server back online, so I already deployed a brand new VM that is fully patched and updated but I am looking for a proper procedure to recover a DAG member node and I can't seem to find a unanimous answer to this. I found that by pulling it offline like that, the server is basically considered "crashed" and I will have to manually evict it from the DAG and reset the AD computer account. Then if I name the new server the exact same, I can install Exchange 2013 CU23 with the /m:recoverserver flag and all settings will be restored from AD.  

Is this the correct procedure or did I forget anything? The newly installed VM holds no mailbox database copies yet. Once I add it back to the DAG, will server 1 automatically copy over all Exchange settings and databases to the second Exchange server? I understand that I will have to copy over a .pfx export of our SSL certificate manually, but other than that, is there anything else I need to do manually?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Hi @Scryden   ,  

According to research on the error information, I think copying the SharedWebCongif from another Exchange server is a feasible solution. But please noted the following points:  

1.The SharedWebConfig file must be copied from a server running the same Cumulative Update. I noted that you have an Exchange that has been successfully upgraded, so please copying the file from the Exchange that is still CU19 version.

2.If the server you pull this file from has a different install path for Exchange you will need to do a find/replace of all paths inside the SharedWebConfig file and update with the destination server’s install path.

3.After copied, please run the iisreset in the Run start as Administrator to restart the IIS.

In addition, according to the following error. Under the the path(C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\Autodiscover). You could try to rename the web.config file to web.config.old, then rename the web.config.bak file to replace it. Restart the IIS and try to upgrade Exchange server again.

Exception message: Could not load file or assembly 'Microsoft.Exchange.Data.Directory, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified. (C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\Autodiscover\web.config line 39)

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
