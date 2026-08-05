---
title: "Microsoft Exchange Server 2016 Update 19 Setup Error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/275013/microsoft-exchange-server-2016-update-19-setup-err
question_id: 275013
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Microsoft Exchange Server 2016 Update 19 Setup Error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/275013/microsoft-exchange-server-2016-update-19-setup-err (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are updating from Exchange Server 2016 CU17 to CU19.    

Setup-Assistant is stopping with the following Error:    

Fehler:    

Der folgende Fehler wurde generiert, als "$error.Clear();     

	upgrade-ExchangeServer -Identity $RoleFqdnOrName -DomainController $RoleDomainController  

" ausgeführt wurde: "Microsoft.Exchange.Configuration.Tasks.ManagementObjectNotFoundException: Der Vorgang konnte nicht ausgeführt werden, weil das Objekt 'Server.Network.local' nicht auf 'Server.Network.local' gefunden wurde.    

   bei Microsoft.Exchange.Configuration.Tasks.DataAccessTask`1.GetDataObject[TObject](IIdentityParameter id, IConfigDataProvider session, ObjectId rootID, OptionalIdentityData optionalData, Func`2 notFoundError, Func`2 multipleFoundError, ExchangeErrorCategory errorCategory)        bei Microsoft.Exchange.Configuration.Tasks.SetObjectWithIdentityTaskBase`3.ResolveDataObject()    

   bei Microsoft.Exchange.Configuration.Tasks.SetSystemConfigurationObjectTask`3.ResolveDataObject()        bei Microsoft.Exchange.Configuration.Tasks.SetObjectTaskBase`2.PrepareDataObject()    

   bei Microsoft.Exchange.Management.SystemConfigurationTasks.UpgradeExchangeServer.PrepareDataObject()    

   bei Microsoft.Exchange.Configuration.Tasks.SetTaskBase`1.InternalValidate()        bei Microsoft.Exchange.Configuration.Tasks.SetSystemConfigurationObjectTask`3.InternalValidate()    

   bei Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()    

   bei Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".    

Is there a solution?    

Best regards     

Thomas

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-24*

Hi @Thomas Westen   ,    

Is the Exchange still working? Also check if the FrontEndTransport service and Transport service are running.    

If you want completely uninstall, you can remove the Exchange server in ADSIEDIT.    

https://blog.dargel.at/2012/11/20/complete-remove-exchange-2013-using-adsiedit/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-23*

Hi Lou,  

Recovering a lost Server is not working. At the moment we try to uninstall Exchange Server 2016. We got this issue:  

[ERROR] Der Front-End-Transportdienst kann nicht ohne Postfachdienst installiert werden.  

[ERROR] Der Transportdienst kann nicht ohne Postfachdienst installiert werden.  

We are not able to RecoverServer, Uninstall, PrepareAD, PrepareAllDomains or PrepareSchema. There is always the same Error Log.  

Is there a Way for a safe Uninstall?  

Best regards   

Thomas

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-18*

Hi @Thomas Westen   ,    

Thanks for sharing the error logs!    

I see this error, that could be the reason but i have no idea why this could happen.    

    

I'm doing a research for this now, and if you could please try Recover a Lost Exchange Server.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-17*

Hi @Thomas Westen   ,    

Good day!    

I've read the error logs but not completely understand, is the Server.Netwrok.Local an Exchange server also the DC, which means you installed Exchange on DC or something else?    

I think you could try upgrading through PowerShell(Run as Administrator and E is the DVD drive of Ex 2016 CU19), run them one by one.    

```
E:\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareSchema  
E:\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAD  
E:\Setup.exe /IAcceptExchangeServerLicenseTerms /PrepareAllDomains  
E:\Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:Upgrade /DomainController:dc01.contoso.com
```

If you failed in this installation, please check C:\ExchangeSetupLogs\ExchangeSetup.log file, there should be details of the error.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
