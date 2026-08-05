---
title: "[Exchange 2016] Move-DatabasePath and common LogFolderPath for two databases"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/373096/exchange-2016-move-databasepath-and-common-logfold
question_id: 373096
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Exchange 2016] Move-DatabasePath and common LogFolderPath for two databases

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/373096/exchange-2016-move-databasepath-and-common-logfold (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

last weekend I moved two Exchange 2016 databases to a new location. I used the Move-DatabasePath command. Everything worked out, but after the whole operation I noticed an error. I accidentally set up a common log directory for the aforementioned databases. Here is the result:

```
[PS] C:\Windows\system32>Get-MailboxDatabase | fl Name,EdbFilePath,LogFolderPath

Name          : MBEXCH01
EdbFilePath   : E:\ExchDataBase\Storage01\MBEXCH01\MBEXCH01.edb
LogFolderPath : **E:\ExchDataBase\Storage01\MBEXCH02**

Name          : MBEXCH02
EdbFilePath   : E:\ExchDataBase\Storage01\MSEXCH02\MSEXCH02.edb
LogFolderPath : **E:\ExchDataBase\Storage01\MSEXCH02**

Name          : MBEXCHJURNAL
EdbFilePath   : E:\ExchDataBase\Storage01\MBEXCHJURNAL\MBEXCHJURNAL.edb
LogFolderPath : E:\ExchDataBase\Storage01\MBEXCHJURNAL
```

To fix this, do I have to move the databases and logs to a new location or can I move the logs to the correct location? I am asking for advice.

## Answers

_No answers on this thread._
