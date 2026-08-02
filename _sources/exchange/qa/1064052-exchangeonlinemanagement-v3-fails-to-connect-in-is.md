---
title: "ExchangeOnlineManagement v3 fails to connect in ISE"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1064052/exchangeonlinemanagement-v3-fails-to-connect-in-is
question_id: 1064052
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# ExchangeOnlineManagement v3 fails to connect in ISE

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1064052/exchangeonlinemanagement-v3-fails-to-connect-in-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently update the ExchangeOnlineManagement module to version 3.0.0 via `Update-Module`. Now it fails to connect, but only in the ISE environment for some reason.    

```
PS C:\> Connect-ExchangeOnline  
  
You cannot call a method on a null-valued expression.  
At C:\Program Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.0.0\netFramework\ExchangeOnlineMa  
nagement.psm1:691 char:17  
+ ...             $cmdletLogger.LogGenericError($connectionContextID, $glob ...  
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException  
    + FullyQualifiedErrorId : InvokeMethodOnNull
```

The error mentions the logger is failing, so I also tried different values for `-LogLevel` and `-LogDirectoryPath`, and I tried this on a few different machines (win10,server2012/16) without any luck.    

I know VS Code is prioritized, but ISE is still supported and it's what I have available. It's not critical for me to update, but wanted to check that it's not just something in my environment

## Answer (community) — community member

*upvotes: 1 · updated: 2022-10-26*

Yep, that was the cause, and thanks for the reply! I figured it was something with my environments...     

I had version 2.0.4, 2.0.5, and 3.0.0 installed on the systems I tested
