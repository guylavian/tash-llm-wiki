---
title: "Can't install Exchange Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1372985/cant-install-exchange-server-2019
question_id: 1372985
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
---
# Can't install Exchange Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1372985/cant-install-exchange-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to install Exchange Server 2019 on an Azure VM Member Server joined to an Azure VM Domain Controller. I've completed all prerequisites and ran prepare schema + prepare ad and prepare all domains. However, I keep receiving the following error in the UI and PowerShell:

Error:

The following error was generated when "$error.Clear();
  set-ExchangeServerRole -Identity $RoleFqdnOrName -IsHubTransportServer:$true -DomainController $RoleDomainController

was run: "Microsoft.Exchange.Data.Directory.ADOperationException: Active Directory operation failed on DC.domain.com. This error is not retriable. Additional information: The object cannot be added because the parent is not on the list of possible superiors.

Active directory response: 00002099: NameErr: DSID-0305137B, problem 2005 (NAMING_VIOLATION), data 0, best match of:

I've tried removing the watermark and action from Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v15\HubTransportRole, reinstalling everything from scratch, and using PowerShell for installation but I'm still facing the same issue. Can someone suggest a solution?

## Answers

_No answers on this thread._
