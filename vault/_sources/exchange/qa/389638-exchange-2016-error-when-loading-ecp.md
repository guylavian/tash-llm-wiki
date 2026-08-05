---
title: "Exchange 2016 error when loading ecp"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/389638/exchange-2016-error-when-loading-ecp
question_id: 389638
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 error when loading ecp

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/389638/exchange-2016-error-when-loading-ecp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to access ECP on an Exchange 2016 server and I am getting the below error. ECP was working up until I installed CU 20.

I tried copying the sharedWebConfig.config file from C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy and pasting it in C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess directory with no luck.

I also tried shutting down IIS, renaming the ecp folder in C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Temporary ASP.NET Files\ecp to ecp.old, and starting IIS again with the ecp directory getting regenerated, and I am still getting the below error.

Server Error in '/ecp' Application.

Could not load file or assembly 'Microsoft.Exchange.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.  

Description: An unhandled exception occurred during the execution of the current web request. Please review the stack trace for more information about the error and where it originated in the code.

Exception Details: System.IO.FileNotFoundException: Could not load file or assembly 'Microsoft.Exchange.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.

Source Error:

An unhandled exception was generated during the execution of the current web request. Information regarding the origin and location of the exception can be identified using the exception stack trace below.

Assembly Load Trace: The following information can be helpful to determine why the assembly 'Microsoft.Exchange.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' could not be loaded.

WRN: Assembly binding logging is turned OFF.  

To enable assembly bind failure logging, set the registry value [HKLM\Software\Microsoft\Fusion!EnableLog] (DWORD) to 1.  

Note: There is some performance penalty associated with assembly bind failure logging.  

To turn this feature off, remove the registry value [HKLM\Software\Microsoft\Fusion!EnableLog].

Stack Trace:

[FileNotFoundException: Could not load file or assembly 'Microsoft.Exchange.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.]  

System.RuntimeTypeHandle.GetTypeByName(String name, Boolean throwOnError, Boolean ignoreCase, Boolean reflectionOnly, StackCrawlMarkHandle stackMark, IntPtr pPrivHostBinder, Boolean loadTypeFromPartialName, ObjectHandleOnStack type) +0  

System.RuntimeTypeHandle.GetTypeByName(String name, Boolean throwOnError, Boolean ignoreCase, Boolean reflectionOnly, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean loadTypeFromPartialName) +96  

System.Type.GetType(String typeName, Boolean throwOnError, Boolean ignoreCase) +65  

System.Web.Compilation.BuildManager.GetType(String typeName, Boolean throwOnError, Boolean ignoreCase) +62  

System.Web.Configuration.ConfigUtil.GetType(String typeName, String propertyName, ConfigurationElement configElement, XmlNode node, Boolean checkAptcaBit, Boolean ignoreCase) +50

[ConfigurationErrorsException: Could not load file or assembly 'Microsoft.Exchange.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.]  

System.Web.Configuration.ConfigUtil.GetType(String typeName, String propertyName, ConfigurationElement configElement, XmlNode node, Boolean checkAptcaBit, Boolean ignoreCase) +572  

System.Web.Configuration.ConfigUtil.GetType(String typeName, String propertyName, ConfigurationElement configElement, Boolean checkAptcaBit) +31  

System.Web.Configuration.Common.ModulesEntry.SecureGetType(String typeName, String propertyName, ConfigurationElement configElement) +59  

System.Web.Configuration.Common.ModulesEntry..ctor(String name, String typeName, String propertyName, ConfigurationElement configElement) +59  

System.Web.HttpApplication.BuildIntegratedModuleCollection(List`1 moduleList) +221  

System.Web.HttpApplication.GetModuleCollection(IntPtr appContext) +1103  

System.Web.HttpApplication.RegisterEventSubscriptionsWithIIS(IntPtr appContext, HttpContext context, MethodInfo[] handlers) +122  

System.Web.HttpApplication.InitSpecial(HttpApplicationState state, MethodInfo[] handlers, IntPtr appContext, HttpContext context) +173  

System.Web.HttpApplicationFactory.GetSpecialApplicationInstance(IntPtr appContext, HttpContext context) +255  

System.Web.Hosting.PipelineRuntime.InitializeApplication(IntPtr appContext) +347

[HttpException (0x80004005): Could not load file or assembly 'Microsoft.Exchange.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.]  

System.Web.HttpRuntime.FirstRequestInit(HttpContext context) +552  

System.Web.HttpRuntime.EnsureFirstRequestInit(HttpContext context) +122  

System.Web.HttpRuntime.ProcessRequestNotificationPrivate(IIS7WorkerRequest wr, HttpContext context) +737

Version Information: Microsoft .NET Framework Version:4.0.30319; ASP.NET Version:4.8.4330.0

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-11*

Hi @Quentin Roberts   ,  

Are there any errors during the installation process?  

Does the OWA work normally?

Please try to the following steps:

1.Check the IIS.  

1)Open IIS Manager. Expand Sites > Exchange Back End.  

2)Click ecp. Open Application Settings in /ecp Home.  

3)Please check whether the value for “BinSearchFolders” is changed to an invalid value. If so, please change it to:  

C:\Program Files\Microsoft\Exchange Server\V15\bin;C:\Program Files\Microsoft\Exchange Server\V15\bin\CmdletExtensionAgents;C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\Owa\bin  

4)Please run the IISRESET in CMD start as Administrator to restart the IIS.

2.Please navigate to “C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp.” Then backup the web.config and web.config.bak file. Then delete the web.config file and rename the "web.config.bak" to "web.config". Then please run the IISRESET in CMD start as Administrator to restart the IIS.

3.Please navigate to “C:\Program Files\Microsoft\Exchange Server\V15\Bin”, then run the UpdateCas.ps1 in this file to reset the ECP.

In addition, are there have any related error logs in event viewer? If so, please share with us, but please pay attention to covering your personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
