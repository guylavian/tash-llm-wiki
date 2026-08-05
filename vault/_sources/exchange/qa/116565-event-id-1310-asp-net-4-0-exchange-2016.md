---
title: "event id 1310 asp.net 4.0 exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/116565/event-id-1310-asp-net-4-0-exchange-2016
question_id: 116565
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# event id 1310 asp.net 4.0 exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/116565/event-id-1310-asp-net-4-0-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

I have 6 exchange server 2016 CU11, 2 in each site. While doing my routine check i fount that OWA and ECP is not working on of exchange servers. I check event viewer and i found Event ID 1013 " event id 1310 asp.net 4.0 ",     

Event code: 3008     

Event message: A configuration error has occurred.     

Event time: 10/5/2020 10:30:43 AM     

Event time (UTC): 10/5/2020 7:30:43 AM     

Event ID: f0712be911fe4351b8371612b930b652     

Event sequence: 42     

Event occurrence: 41     

Event detail code: 0     

Application information:     

    Application domain: /LM/W3SVC/1/ROOT/owa-9-132463534043005621   

    Trust level: Full   

    Application Virtual Path: /owa   

    Application Path: E:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\   

    Machine name: Ex03  

Process information:     

    Process ID: 7596   

    Process name: w3wp.exe   

    Account name: NT AUTHORITY\SYSTEM   

Exception information:     

    Exception type: ConfigurationErrorsException   

    Exception message: It is an error to use a section registered as allowDefinition='MachineToApplication' beyond application level.  This error can be caused by a virtual directory not being configured as an application in IIS. (E:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\owa\auth\web.config line 145)  

   at System.Configuration.ConfigurationSchemaErrors.ThrowIfErrors(Boolean ignoreLocal)    

   at System.Configuration.BaseConfigurationRecord.GetSectionRecursive(String configKey, Boolean getLkg, Boolean checkPermission, Boolean getRuntimeObject, Boolean requestIsHere, Object& result, Object& resultRuntimeObject)    

   at System.Configuration.BaseConfigurationRecord.GetSection(String configKey)    

   at System.Web.Configuration.RuntimeConfig.GetSectionObject(String sectionName)    

   at System.Web.Configuration.RuntimeConfig.GetSection(String sectionName, Type type, ResultsIndex index)    

   at System.Web.Configuration.RuntimeConfig.get_Identity()    

   at System.Web.HttpContext.SetImpersonationEnabled()    

   at System.Web.HttpApplication.AssignContext(HttpContext context)    

   at System.Web.HttpRuntime.ProcessRequestNotificationPrivate(IIS7WorkerRequest wr, HttpContext context)    

Request information:     

    Request URL: https://EX03:443/owa/auth/logon.aspx?url=https://EX03/owa&reason=0   

    Request path: /owa/auth/logon.aspx   

    User host address: x.x.x.x  

    User:    

    Is authenticated: False   

    Authentication Type:    

    Thread account name: NT AUTHORITY\SYSTEM   

Thread information:     

    Thread ID: 92   

    Thread account name: NT AUTHORITY\SYSTEM   

    Is impersonating: False   

    Stack trace:    at System.Configuration.ConfigurationSchemaErrors.ThrowIfErrors(Boolean ignoreLocal)  

   at System.Configuration.BaseConfigurationRecord.GetSectionRecursive(String configKey, Boolean getLkg, Boolean checkPermission, Boolean getRuntimeObject, Boolean requestIsHere, Object& result, Object& resultRuntimeObject)    

   at System.Configuration.BaseConfigurationRecord.GetSection(String configKey)    

   at System.Web.Configuration.RuntimeConfig.GetSectionObject(String sectionName)    

   at System.Web.Configuration.RuntimeConfig.GetSection(String sectionName, Type type, ResultsIndex index)    

   at System.Web.Configuration.RuntimeConfig.get_Identity()    

   at System.Web.HttpContext.SetImpersonationEnabled()    

   at System.Web.HttpApplication.AssignContext(HttpContext context)    

   at System.Web.HttpRuntime.ProcessRequestNotificationPrivate(IIS7WorkerRequest wr, HttpContext context)    

    

i did the following but non of them worked:    

1- Copied sharedWebConfig.config file from C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy directory and pasted "replaced it because it was already exsits"  it on sharedWebConfig.config file in C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess directory + IISreset    

2- I checked IIS frontend\ backend binding and it were pointing to third party certificate " as other exchange servers".    

3- webconfig was exsits on OWA\ auth\ client axxess folders "not missing".    

4- I checked fronend OWA\ ECP  physical path and they are correct.    

I noticed that haredWebConfig.config is exists on one exchange server only "the one having the issue" and not exists on the other exchange servers  and i search inside it for exchange server name and it was pointing to another server.    

What else can be done to solve this issue.    

Thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-14*

-  Did you change any settings before this error occurred?  

We got Microsoft support "issue with OWA - too many redirect" and got solved by running a script. After that i test all exchange servers OWA\ ECP per server and everything was working fine.  

-  Is the problematic Exchange server in a DAG environment?  

Yes we do have DAG. all other 5 server OWA\ ECP are working fine  

-  4.7.1 installed  

-  i run this commands and results were identical : Get-OWAVirtualDirectory | fl   -  Get-ECPVirtualDirectory | fl  

-  I check IIS fronend\ backend binging and its correct (compare it with other ex servers)  

-  If i run UpdateCas.ps1 and UpdateConfigFiles.ps1  will it affect other exchange servers?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-09*

Hi  

I would advise upgrading to CU17 and applying the security update as well. CU11 is behind and you missing out on major updates.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-06*

Hi @HamoudaAlbakri-3924 ,  

Did you change any settings before this error occurred?  

Is the problematic Exchange server in a DAG environment?  

Please following the steps and see if the issue is resolved:  

1.For Exchange CU11, please make sure that the Microsoft .NET Framework version is 4.7.1 or 4.7.2.  

For more information:Supported .NET Framework versions for Exchange 2016  

2.Please run the following command line to check the settings of OWA and ECP, check whether there is a difference between the configuration of the normal Exchange server and the configuration of the Exchange server that has problems.

```
Get-OWAVirtualDirectory | fl  
Get-ECPVirtualDirectory | fl
```

3.Please run UpdateCas.ps1 and UpdateConfigFiles.ps1 from the exchange bin directory C:\Program Files\Microsoft\Exchange Server\V15\Bin. And please run the IISRESET in CMD start as administrator to restart IIS.  

4.Please check if there exist MSExchangeECPAppPool and MSExchangeOWAAppPool in the Application Pools in IIS. If they exists, please make sure the .NET CLR Version is v4.0 and right click, then select “Recycle”.  

  

5.You could run the following command to remove and recreate the virtual directory.

```
Remove-OWAVirtualDirectory  
New-OWAVirtualDirectory  
Remove-ECPVirtualDirectory  
New-ECPVirtualDirectory
```

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
