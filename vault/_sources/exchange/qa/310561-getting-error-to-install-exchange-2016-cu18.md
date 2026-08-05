---
title: "Getting error to install Exchange 2016 CU18"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310561/getting-error-to-install-exchange-2016-cu18
question_id: 310561
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Getting error to install Exchange 2016 CU18

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310561/getting-error-to-install-exchange-2016-cu18 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Error:  

The following error was generated when "$error.Clear();  

if ([Environment]::OSVersion.Version.Major -ge 6)  

{  

$WsbBinPath = '\"' + (join-path "$RoleInstallPath" "bin\wsbexchange.exe") + '\"';  

$reg= join-path (join-path $env:SystemRoot system32) reg.exe;  

$servicecmd = join-path (join-path $env:SystemRoot system32) sc.exe;

```
if ((get-service wsbexchange* | where {$_.name -eq "wsbexchange"}))  
          {  
                if ((get-service wsbexchange).Status -eq "Running")  
                {  
                    Start-SetupProcess -Name:"$servicecmd" -Args:"stop wsbexchange";  
                }  
                Start-SetupProcess -Name:"$servicecmd" -Args:"delete wsbexchange";  
          }  

          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /t REG_SZ /d  `"CExchangeHelper Class`" /f";  
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /v AppId /t REG_SZ /d `"{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}`" /f";  
          Start-SetupProcess -Name:"$reg" -Args:"add `"HKCR\CLSID\{D8A2E312-3B17-4293-B71E-CD72A7C04BF3}\LocalServer32`" /t REG_SZ /d `"$WsbBinPath`" /f";
```

## Answers

_No answers on this thread._
