---
title: "Exchange Server 2010 Error to run .\\Setup.com /PrepareSchema"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/149965/exchange-server-2010-error-to-run-setup-com-prepar
question_id: 149965
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2010 Error to run .\Setup.com /PrepareSchema

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/149965/exchange-server-2010-error-to-run-setup-com-prepar (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys!

I try to migrate Exchange Server 2007 to Exchange Server 2010, I've installed all the prerrequisites but when I run the command .\Setup.com /PrepareSchema it stops and ending the process. When reviewing the logs only the following is displayed:

[10/31/2020 00:38:51.0091] [1] [ERROR] The following error was generated when "$error.Clear();  

install-ExchangeSchema -LdapFileName ($roleInstallPath + "Setup\Data\"+$RoleSchemaPrefix + "schema0.ldf")

" was run: "El sistema no puede encontrar el archivo especificado".  

[10/31/2020 00:38:51.0091] [1] [ERROR] El sistema no puede encontrar el archivo especificado  

[10/31/2020 00:38:51.0091] [1] [ERROR-REFERENCE] Id=ADSchemaComponent___64bd6943575045fa880b9289xxxxxxxx Component=EXCHANGE14:\Current\Release\Shared\Datacenter\Setup  

[10/31/2020 00:38:51.0091] [1] Setup is stopping now because of one or more critical errors.

Have you will comments?

Thanks and Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-05*

Hello guys!  

I found the solution to this issue, I leave the actions performed  

1.- Install-WindowsFeature RSAT-ADDS  

2.- Import-Module ServerManager  

3.- Add-WindowsFeature RSAT-ADDS  

Thanks a lot, regards
