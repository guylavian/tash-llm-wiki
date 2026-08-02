---
title: "Exchange 2019 ECP 500 ASP Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1092656/exchange-2019-ecp-500-asp-error
question_id: 1092656
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 ECP 500 ASP Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1092656/exchange-2019-ecp-500-asp-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,    

Recently installed Exchange 2019 CU12 and when trying to use ECP I get the following in the application log ...    

Process information:     

    Process ID: 12992   

    Process name: w3wp.exe   

    Account name: NT AUTHORITY\SYSTEM   

Exception information:     

    Exception type: ConfigurationErrorsException   

    Exception message: Could not load file or assembly 'Microsoft.Search.Platform.Parallax, Version=3.3.4.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified. (C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\owa\web.config line 134)  

   at System.Web.Configuration.CompilationSection.LoadAssemblyHelper(String assemblyName, Boolean starDirective)    

   at System.Web.Configuration.CompilationSection.LoadAssembly(AssemblyInfo ai)    

   at System.Web.Compilation.BuildManager.GetReferencedAssemblies(CompilationSection compConfig)    

   at System.Web.Compilation.BuildManager.GetPreStartInitMethodsFromReferencedAssemblies()    

   at System.Web.Compilation.BuildManager.CallPreStartInitMethods(String preStartInitListPath, Boolean& isRefAssemblyLoaded)    

   at System.Web.Compilation.BuildManager.ExecutePreAppStart()    

   at System.Web.Hosting.HostingEnvironment.Initialize(ApplicationManager appManager, IApplicationHost appHost, IConfigMapPathFactory configMapPathFactory, HostingEnvironmentParameters hostingParameters, PolicyLevel policyLevel, Exception appDomainCreationException)    

Could not load file or assembly 'Microsoft.Search.Platform.Parallax, Version=3.3.4.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.    

I did check the web.config file in the Program Files\Microsoft\Exchange Server\V15\ClientAccess\Owa directory and it was set 2.21.0 where as above the dll file is version 3.3.4.0 in the Program Files\Microsoft\Exchange Server\V15\Bin location so I changed it match the dll file    

Checked the application pool settings and it is pointing to the right location for the install files, made sure .Net framework registry are present and correct - are .Net 2.0 registry keys required as well?    

Server is licenced correctly, has enough disk space and I cannot see any other errors that would possibly be a cause.     

I haven't tried to re-create the ECP Virtual directories or run the updateCas.PS1 as this seems a bit drastic.    

Am I missing something?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-30*

Ok, the version of the DLL file error has been resolved, running the updateCAS.ps1 file seems to have resolved that particular error.    

As for the setup.exe /prepareAD, this was done before the installation of any Exchange 2019 in the environment to update the schema to support Exchange 2019.    

I will look into the links provided to see if they help resolve the issue.    

Many Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-18*

Did you move the arbitration mailboxes to the 2019 server?    

If not, they need to be recreated. This won't remove any 365 mailboxes.    

https://learn.microsoft.com/en-us/exchange/architecture/mailbox-servers/recreate-arbitration-mailboxes?view=exchserver-2019    

Setup.exe /PrepareAD    

Also, check this blog for help - How to Fix HTTP ERROR 500 in ECP/EAC after Login

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-18*

Hi @Charlie  ,

Welcome to our forum.

To narrow down this issue, here are my troubleshooting for this issue:  

1.Please check the web.config file in this path and find line 134 mentioned.

2.Please Check if the SharedWebConfig.config file is located in appropriate location, if not copy it to the below location and run IISReset.  

%ExchangeInstalledDrive%:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy  

%ExchangeInstalledDrive%:\Program Files\Microsoft\Exchange Server\V15\ClientAccess

3.If the error persists, it is recommended that you try running UpdateCas.PS1.

Besides, you can check out the following similar threads, hope they will help you.  

1. event-id-1310-asp-net-40303190.html  

2. exchange-2019-ecp-url-is-not-loading-and-gives-error

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
