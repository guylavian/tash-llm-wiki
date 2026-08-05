---
title: "Exchange 2016 ECP / Powershell Error after last CU update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1426987/exchange-2016-ecp-powershell-error-after-last-cu-u
question_id: 1426987
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 ECP / Powershell Error after last CU update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1426987/exchange-2016-ecp-powershell-error-after-last-cu-u (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

, HI,

yesterday, after installing the latest CU 2016 update CU23 Nov23SU 15.1.2507.35, we encountered some strange behavior with some Exchange Powershell commands:

for example: Get-ExchangeServer | Test-MAPIConnectivity

but if I run a single command, Get-ExchangeServer and Test-MAPIConnectivity, not in pipes, it works.

Furthermore, the script to move db between nodes, stops to work:

```
.\RedistributeActiveDatabases.ps1 -DagName "DAG" -BalanceDbsByActivationPreference -SkipMoveSuppressionCh
ecks
Cannot convert value "DAG" to type "Microsoft.Exchange.Data.Directory.SystemConfiguration.DatabaseAvailabilityGroup". Error: "Cannot convert the "DAG"
value of type "Deserialized.Microsoft.Exchange.Data.Directory.SystemConfiguration.DatabaseAvailabilityGroup" to type
"Microsoft.Exchange.Data.Directory.SystemConfiguration.DatabaseAvailabilityGroup"."
At C:\Program Files\Microsoft\Exchange Server\V15\scripts\RedistributeActiveDatabases.ps1:2815 char:3
+         $script:dag = Get-DatabaseAvailabilityGroup $DagName -Status
+         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : MetadataError: (:) [], ArgumentTransformationMetadataException
    + FullyQualifiedErrorId : RuntimeException

Log-Error : [09:07:47.004 UTC] Could not find DAG matching 'cartero-dag'!
At C:\Program Files\Microsoft\Exchange Server\V15\scripts\RedistributeActiveDatabases.ps1:2820 char:3
+         Log-Error ($RedistributeActiveDatabases_LocalizedStrings.res_ ...
+         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Write-Error], WriteErrorException
    + FullyQualifiedErrorId : Microsoft.PowerShell.Commands.WriteErrorException,Log-Error
```

```
Get-ExchangeServer | Test-MAPIConnectivity
The operation couldn't be performed because object 'XXXXXXX' couldn't be found on 'ADXXX.domain.com'.
    + CategoryInfo          : NotSpecified: (:) [Test-MAPIConnectivity], ManagementObjectNotFoundException
    + FullyQualifiedErrorId : [Server=XXXXX,RequestId=812991b5-efa7-4049-a31d-a989fa3456b6,TimeStamp=16/11/2023 08:53:21] [FailureCategory=Cmdlet-ManagementObjectNotFoun
   dException] 186247B,Microsoft.Exchange.Monitoring.TestMapiConnectivity
    + PSComputerName        : XXXXX.domain.com

The operation couldn't be performed because object 'XXXXX' couldn't be found on 'AD4XXX.domain.com'.
    + CategoryInfo          : NotSpecified: (:) [Test-MAPIConnectivity], ManagementObjectNotFoundException
    + FullyQualifiedErrorId : [Server=XXXXX,RequestId=812991b5-efa7-4049-a31d-a989fa3456b6,TimeStamp=16/11/2023 08:53:21] [FailureCategory=Cmdlet-ManagementObjectNotFoun
   dException] 915C3018,Microsoft.Exchange.Monitoring.TestMapiConnectivity
    + PSComputerName        : XXXXX.domain.com
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-17*

Hi @Claudio Di Chiaro  ,

Did you run the command or scripts on Management Tools only machines? If so, it appears that both the two issues have already been aware of, and fixes are currently being working on. For more information and the possible workaround for now, you can refer to the official links below:

-  Released: November 2023 Exchange Server Security Updates  

-  Configure certificate signing of PowerShell serialization payloads in Exchange Server  

You can keep checking back of the links above for any update. 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
