---
title: "Can't open ECP/OWA after patching CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1118923/cant-open-ecp-owa-after-patching-cu23
question_id: 1118923
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Can't open ECP/OWA after patching CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1118923/cant-open-ecp-owa-after-patching-cu23 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have 2 Exchange server 2016. I patched CU23 on both of them with exact the same steps, but one succeeded, the other one failed with that I am unable to open ECP/OWA on it. The error message for opening ECP is below.    

Server Error in '/ecp' Application.    

Configuration Error    

Description: An error occurred during the processing of a configuration file required to service this request. Please review the specific error details below and modify your configuration file appropriately.    

Parser Error Message: Could not load file or assembly 'Microsoft.Exchange.Clients.Strings, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.    

Source Error:    

Line 61: the compiler. All assemblies in the GAC and owa\bin are referenced automatically.    

Line 62: -->    

Line 63: <add assembly="Microsoft.Exchange.Clients.Strings, Version=15.0.0.0, Culture=neutral, publicKeyToken=31bf3856ad364e35" />    

Line 64: <add assembly="Microsoft.Exchange.Data.Directory, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />    

Line 65: <add assembly="Microsoft.Exchange.Clients.Common, Version=15.0.0.0,Culture=neutral, publicKeyToken=31bf3856ad364e35" />    

Source File: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\web.config Line: 63    

Assembly Load Trace: The following information can be helpful to determine why the assembly 'Microsoft.Exchange.Clients.Strings, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' could not be loaded.    

WRN: Assembly binding logging is turned OFF.    

To enable assembly bind failure logging, set the registry value [HKLM\Software\Microsoft\Fusion!EnableLog] (DWORD) to 1.    

Note: There is some performance penalty associated with assembly bind failure logging.    

To turn this feature off, remove the registry value [HKLM\Software\Microsoft\Fusion!EnableLog].    

I have tried to run .\UpdateCas.ps1 and .\UpdateConfigFiles.ps1 but no luck.    

All exchange services are up and running. I am out of idea.    

Please help!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-09*

Can you check the event viewer for the errors and validate the certificate?    

Also, i would recommend to go through the below article and check whether your are facing similar issue.    

https://jaapwesselius.com/2021/12/01/exchange-server-owa-and-ecp-not-working/

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-08*

Please check if the bindings are assigned correctly in the IIS console for both websites (Default website and Exchange Backend).    

Also, check these links - https://learn.microsoft.com/en-us/answers/questions/479727/after-kb5004778-update-unable-to-access-owa-amp-ec.html    

https://www.stellarinfo.com/blog/exchange-server-http-500-error-ecp/    

Please Note: Since these web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-07*

Hi @LilyLi2-MSFT   ,    

Thank you so much for your reply.    

-  The path is the same, but I go ahead copied yours and replaced it and reset IIS    

-  I copied the web.config file from the working server to the troubled server, ECP still open with error, but the error is changed to below.    

Server Error in '/ecp' Application.    

Configuration Error    

Description: An error occurred during the processing of a configuration file required to service this request. Please review the specific error details below and modify your configuration file appropriately.    

Parser Error Message: Could not load file or assembly 'Microsoft.Exchange.HttpRequestFiltering, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' or one of its dependencies. The system cannot find the file specified.    

Source Error:    

Line 72:         <add assembly="Microsoft.Exchange.FrontEndHttpProxy, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />    

Line 73:         <add assembly="Microsoft.Exchange.HttpProxy.Common, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />    

Line 74:         <add assembly="Microsoft.Exchange.HttpRequestFiltering, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" />    

Line 75:         <add assembly="Microsoft.Exchange.Security, Version=15.0.0.0, Culture=neutral, publicKeyToken=31bf3856ad364e35" />    

Line 76:       </assemblies>    

Source File: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp\web.config    Line: 74    

Assembly Load Trace: The following information can be helpful to determine why the assembly 'Microsoft.Exchange.HttpRequestFiltering, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35' could not be loaded.    

WRN: Assembly binding logging is turned OFF.    

To enable assembly bind failure logging, set the registry value [HKLM\Software\Microsoft\Fusion!EnableLog] (DWORD) to 1.    

Note: There is some performance penalty associated with assembly bind failure logging.    

To turn this feature off, remove the registry value [HKLM\Software\Microsoft\Fusion!EnableLog].    

Please help how to fix it.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-07*

Hi @Grace Yin  ,

It is recommended that you use the following methods to help you troubleshooting:

-   Try checking the path of BinSearchFolders.  

    Please find it from IIS->Exchange BackEnd website-> ecp-> bin-> Application Settings-> BinSearchFolders, and change it to:  

    C:\Program Files\Microsoft\Exchange Server\V15\bin;C:\Program Files\Microsoft\Exchange Server\V15\bin\CmdletExtensionAgents;C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\Owa\bin  

    Then please run the IISRESET to restart the IIS.

-   Can another Exchange access ECP and OWA?  

    Please check the web.config file at the following path:  

    C：\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\ecp  

    If you have another Exchange server with the exact same version and functioning properly, you could also copy the web.config file from another server and replace it.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
