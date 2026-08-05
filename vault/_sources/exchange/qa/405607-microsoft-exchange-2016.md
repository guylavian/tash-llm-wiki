---
title: "Microsoft Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/405607/microsoft-exchange-2016
question_id: 405607
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Microsoft Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/405607/microsoft-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Helo tout le monde.  

J'obtiens l'erreur suivante à la dernière étape de l'installation d'Exchange 2016.  

Erreur:  

L'erreur suivante a été générée lorsque "$ error.Clear ();  

    start-SetupService -ServiceName MSExchangeFrontendTransport

" a été exécuté: "Microsoft.Exchange.Configuration.Tasks.ServiceDidNotReachStatusException: le service" MSExchangeFrontendTransport "n'a pas pu atteindre l'état" En cours d'exécution "pour server.  

   em Microsoft.Exchange.Configuration.Tasks.Task.ThrowError (Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)  

   em Microsoft.Exchange.Configuration.Tasks.Task.WriteError (Exception exception, catégorie ErrorCategory, Object target)  

   em Microsoft.Exchange.Management.Tasks.ManageSetupService.WaitForServiceStatus (ServiceController ServiceController, l' état ServiceControllerStatus, Unlimited`1 maximumWaitTime, Boolean ignoreFailures, Boolean sendWatsonReportForHungService)      em Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService (ServiceController ServiceController, Boolean ignoreServiceStartTimeout, Boolean failIfServiceNotInstalled, Unlimited`1 maximumWaitTime, String [] serviceParameters)  

   em Microsoft.Exchange.Management.Tasks.ManageSetupService.StartService (String serviceName, Boolean ignoreServiceStartTimeout, String [] serviceParameters)  

   em Microsoft.Exchange.Management.Tasks.ManageSetupService. .Tasks.StartSetupService.InternalProcessRecord ()  

   em Microsoft.Exchange.Configuration.Tasks.Task. <ProcessRecord> b__b ()  

   em Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc (String funcName, Action func, Boolean terminatePipelineIfailed) ".  

Quelqu'un peut-il aider s'il vous plaît?  

Merci d'avance

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-23*

Hi @Leprof MBR       

Currently in Microsoft Q&A we only support English, could you please edit your question into English？Then we can help to solve your issues, thanks for your understanding.    

Based on the translation, you can installing the exchange using the below command,    

Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:Install /Roles:Mailbox /DoNotStartTransport    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/unattended-installs?view=exchserver-2016    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
