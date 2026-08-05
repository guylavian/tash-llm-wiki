---
title: "Exchange Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2155528/exchange-server-2019
question_id: 2155528
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2155528/exchange-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

I am trying to install Exchange Server 2019. I will get to Stage 7 of the installation, and it fails with the following Error message:   

Any help fixing this issue would be much appreciated.   

 PS D:> .\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Install /Roles:Mailbox /on:"domain name"

Microsoft Exchange Server 2019 Cumulative Update 14 Unattended Setup

Copying Files...

File copy complete. Setup will now collect additional information needed for installation.

Languages

Mailbox role: Transport service

Mailbox role: Client Access service

Mailbox role: Mailbox service

Mailbox role: Front End Transport service

Mailbox role: Client Access Front End service

Performing Microsoft Exchange Server Prerequisite Check

Configuring Microsoft Exchange Server

The following error was generated when "$error.Clear();

 set-ExchangeServerRole -Identity $RoleFqdnOrName

-IsHubTransportServer:$true -DomainController $RoleDomainController

" was run:

"Microsoft.Exchange.Data.DataValidationException: The domain is invalid.

 at

Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target,

String helpUrl)

 at Microsoft.Exchange.Configuration.Tasks.Task.WriteError(Exception exception, ErrorCategory

category, Object target, Boolean reThrow)

 at

Microsoft.Exchange.Configuration.Tasks.DataAccessTask`1.Validate(TDataObject dataObject)

 at

Microsoft.Exchange.Configuration.Tasks.SetTaskBase`1.InternalValidate()

 at

Microsoft.Exchange.Configuration.Tasks.SetSystemConfigurationObjectTask`3.InternalValidate()

 at

Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()

 at

Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean

terminatePipelineIfFailed)".

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-10*

Hi, @Anonymous  

Welcome to the Microsoft Q&A platform! 

First of all, make sure you meet all the prerequisites for installing exchange server, which you can refer to: Exchange Server prerequisites, Exchange 2019 system requirements, Exchange 2019 requirements | Microsoft Learn

Based on the error message you provided, it seems that the domain name is invalid. Please check if the “Domain Name” field is the same as Sever Manager. You can check it by clicking on local server.

However, you can also troubleshoot the issue from the following ways:

1.Granting Schema Admin and Enterprise Admin permissions to the current user in ADUC. Open ADUC by DC, check the user you need to install and click member of to add the above permissions to it.

2.Run  

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains 

3.Check the detailed installation logs. CD:/ExchangeSetupLogs/ExchangeSetup. Find the log truncation and troubleshoot further based on the information it provides.

Similar cases can be found in

Error during installation Exchange 2016 - Microsoft Q&A

Failed install of Exchange server 2019 W server 2022 - Microsoft Q&A

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-10*

Hi @Anonymous  ,  

Welcome to the Microsoft Q&A platform!  

First of all, make sure you meet all the prerequisites for installing exchange server, which you can refer to:https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites?view=exchserver-2019#exchange-2019-prerequisites-for-preparing-active-directory    

Based on the error message you provided, it seems that the domain name is invalid. Please check if the “Domain Name” field is the same as Sever Manager. You can check it by clicking on local server.

However, you can also troubleshoot the issue from the following ways:

-  Granting Schema Admin and Enterprise Admin permissions to the current user in ADUC.  

Open ADUC by DC, check the user you need to install and click member of to add the above permissions to it.  

-  Run  

Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema   Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD   Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains

3.Check the detailed installation logs. CD:/ExchangeSetupLogs/ExchangeSetup.  

Find the log truncation and troubleshoot further based on the information it provides.  

Similar cases can be found inhttps://learn.microsoft.com/en-us/answers/questions/1340281/error-during-installation-exchange-2016  

https://learn.microsoft.com/en-us/answers/questions/1159971/failed-install-of-exchange-server-2019-w-server-20

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-10*

It seems like you have might be an issue with the domain name you're using in the command. Here are some things you can try to fix the issue:

-  Verify the domain name you entered in the command to make sure it's correct and matches your actual domain name.

-  Make sure your server can connect to the domain controller and that the DNS settings are correct.

-  Before installation, make sure that all the necessary prerequisites for Exchange 2019 are installed on the server (like the Windows features and roles).

Let me know if you have any query.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-10*

It seems like you have might be an issue with the domain name you're using in the command. Here are some things you can try to fix the issue:

-  Verify the domain name you entered in the command to make sure it's correct and matches your actual domain name.

-  Make sure your server can connect to the domain controller and that the DNS settings are correct.

-  Before installation, make sure that all the necessary prerequisites for Exchange 2019 are installed on the server (like the Windows features and roles).

Let me know if you have any query.
