---
title: "Error installing the Exchange Server 2019 Security Update CU12 Nov22SU."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1158449/error-installing-the-exchange-server-2019-security
question_id: 1158449
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Error installing the Exchange Server 2019 Security Update CU12 Nov22SU.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1158449/error-installing-the-exchange-server-2019-security (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everybody!

Migration from Exchange 2016 CU23 to MS Exchange 2019 CU 12. Two new servers with Exchange 2019 CU12 are in DAG and all the latest updates are installed on them.
To configure Windows Extended Protection, I am trying to install Nov22SU on one of the nodes. The knife is put into maintenance mode.
During the initial installation of the security update, I get the following error:

```
roperty(C): MsiLogFileLocation = C:\Program Files\Microsoft\Exchange Server\V15\Logging\Update\msi\ExchangeUpdate_2023-01-09-144610.log
Property(C): msgInterimIncorrectRollup = Installation cannot continue. The Setup Wizard has determined that this Interim Update is incompatible with the current Microsoft Exchange Server 2019 Cumulative Update 12 configuration.
Property(C): CURRENTDIRECTORY = C:\install\SU
Property(C): _2ADC57AA8446477EA4FCD2125BAEDE2A = C:\Users\administrator.COBION\AppData\Local\Temp\ExchangeServer.msp
=== Logging stopped: 1/9/2023  17:54:26 ===
MSI (c) (C4:3C) [17:54:26:128]: Product: Microsoft Exchange Server - Update 'Security Update for Exchange Server 2019 Cumulative Update 12 (KB5019758) 15.2.1118.20' could not be installed. Error code 1603. Additional information is available in the log file C:\Program Files\Microsoft\Exchange Server\V15\Logging\Update\msi\ExchangeUpdate_2023-01-09-144610.log.

MSI (c) (C4:3C) [17:54:26:129]: Windows Installer installed an update. Product Name: Microsoft Exchange Server. Product Version: 15.2.1118.7. Product Language: 1033. Manufacturer: Microsoft Corporation. Update Name: Security Update for Exchange Server 2019 Cumulative Update 12 (KB5019758) 15.2.1118.20. Installation success or error status: 1603.
```

Well, on the "product", so where the virtual Exchange 2019 CU 12, I output to maintenance and everything was successfully installed - although it was with SU August.

I noticed such a feature, as soon as the package tries to stop the services itself, an error immediately appears, maybe it can't stop some services.

Well, in this article install-exchange-security-update they put it with maintenance mode.

and it seems that everything is correct according to the builds, according to this table build-numbers-and-release-dates

I put SU with the build (KB5019758) 15.2.1118.20

By the way, at the expense of the services on the node that is displayed in maintenace and it seems that all Exchange services are stopped, but still nothing is reflected in Server Manager and again an error,

Tell me, please, what could be the reason?

Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-11*

Please check these links for more insight - 

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/exchange-security-update-issues 

https://learn.microsoft.com/en-us/answers/questions/513918/security-update-1-for-exchange-2016-cu-21-(kb50047

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-11*

Hi,

When you install an update on a server that's a member of a DAG, several services are stopped during the installation, including all Exchange services and the Cluster service.

You could refer to: Manage database availability groups in Exchange Server

Microsoft recommends keeping your Exchange Server up to date and you could install the latest Exchange Server 2019 CU12 Jan23SU: visit https://aka.ms/ExchangeUpdateWizard and choose your currently running CU and your target CU. Then click the “Tell me the steps” button, to get a list of steps to follow.

For reference on Exchange update: Why Exchange Server updates matter

If an Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-10*

But this is even more interesting- how could this happen, did the SU installation try to stop all services and eventually everything was turned off at the root?))
