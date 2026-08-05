---
title: "Exchange Server 2019 installation failing due to Services."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2237259/exchange-server-2019-installation-failing-due-to-s
question_id: 2237259
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server 2019 installation failing due to Services.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2237259/exchange-server-2019-installation-failing-due-to-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am installing an Exchange Server 2019 CU15 for a customer.

All of the prerequisites have been installed.

The account being used to install has Domain Admin, Organization Admin, Enterprise Admin and Schema Admin.

During the installation the following error is reported:

Error:

The following error was generated when "$error.Clear(); 

```
*start-SetupService -ServiceName MSExchangeMailboxAssistants*
```

" was run: "Microsoft.Exchange.Configuration.Tasks.ServiceDisabledException: Service 'MSExchangeADTopology' is disabled on this server. ---> System.InvalidOperationException: Cannot start service MSExchangeADTopology on computer '.'. ---> System.ComponentModel.Win32Exception: The service cannot be started, either because it is disabled or because it has no enabled devices associated with it

Looking at the services for Exchange, many of them have been Disabled.

I have tried to change them to Automatic (As they should be) but during the installation they get Disabled again.

## Answers

_No answers on this thread._
