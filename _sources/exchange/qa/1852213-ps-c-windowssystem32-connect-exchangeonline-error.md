---
title: "PS C:\\windows\\system32> Connect-ExchangeOnline error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1852213/ps-c-windowssystem32-connect-exchangeonline-error
question_id: 1852213
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# PS C:\windows\system32> Connect-ExchangeOnline error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1852213/ps-c-windowssystem32-connect-exchangeonline-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The process cannot access the file 'C:\Users\xxxxxxxx\AppData\Local\Temp\tmpEXO_02egxx50.oaf\tmpEXO_02egxx50.oaf.psm1' because it is being used by another process.

At C:\Users\xxxxxxxx_LDA\Documents\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.5.1\netFramework\ExchangeOnlineManagement.psm1:766 char:21

+ 

```
throw $_.Exception;
  ```+ 
  ```dockerfile
                  ~~~~~~~~~~~~~~~~~~
```

-  CategoryInfo          : OperationStopped: (:) [], IOException

-  FullyQualifiedErrorId : The process cannot access the file 'C:\Users\xxxxxxx\AppData\Local\Temp\tmpEXO_02egxx50.oaf\tmpEXO_02egxx50.oaf.psm1' because it is 

   being used by another process.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-05*

Hi @Rice, Jason,

Welcome to the Microsoft Q&A platform!

It seems like you're facing process error when you connect to ExchangeOnline via PowerShell.

Please kindly ensure there are no other applications are using the file. You could open Task Manager and look for processes that might be using the file. Also, please try to reinstall the ExchangeOnlineManagement Module to see if it works.

If the answer is helpful, please click "Accept Answer" and kindly upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-02*

It is compatible with PowerShell version 7.0; try installing PowerShell 7.
