---
title: "Can't connect to exchange online using powershell with global admin rights"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1071783/cant-connect-to-exchange-online-using-powershell-w
question_id: 1071783
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Can't connect to exchange online using powershell with global admin rights

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1071783/cant-connect-to-exchange-online-using-powershell-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection
```

I get following error message    

```
New-PSSession : [outlook.office365.com] Connecting to remote server outlook.office365.com failed with the following  
error message : Access is denied. For more information, see the about_Remote_Troubleshooting Help topic.  
At line:1 char:12  
+ $Session = New-PSSession -ConfigurationName Microsoft.Exchange -Conne ...  
+            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
    + CategoryInfo          : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin  
   gTransportException  
    + FullyQualifiedErrorId : AccessDenied,PSSessionOpenFailed  
PS C:\Users\administrator.CMWONG> Connect-ExchangeOnline cmdlet  
Invalid ConnectionUri parameter 'cmdlet'  
At C:\Program  
Files\WindowsPowerShell\Modules\ExchangeOnlineManagement\3.0.0\netFramework\ExchangeOnlineManagement.psm1:487 char:13  
+             throw "Invalid ConnectionUri parameter '$ConnectionUri'"  
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
    + CategoryInfo          : OperationStopped: (Invalid ConnectionUri parameter 'cmdlet':String) [], RuntimeException  
    + FullyQualifiedErrorId : Invalid ConnectionUri parameter 'cmdlet'
```

Will global admin rights not give me full access on exchange online or do I also need to be part of other groups e.g. exchange admin    

And try to run     

```
Import-Module ExchangeOnlineManagement  
Connect-ExchangeOnline
```

get other error messager     

```
----------------------------------------------------------------------------------------  
This V3 EXO PowerShell module contains new REST API backed Exchange Online cmdlets which doesn't require WinRM for Clien  
t-Server communication. You can now run these cmdlets after turning off WinRM Basic Auth in your client machine thus mak  
ing it more secure.  
  
Unlike the EXO* prefixed cmdlets, the cmdlets in this module support full functional parity with the RPS (V1) cmdlets.  
  
V3 cmdlets in the downloaded module are resilient to transient failures, handling retries and throttling errors inherent  
ly.  
  
However, REST backed EOP and SCC cmdlets are not available yet. To use those, you will need to enable WinRM Basic Auth.  
  
For more information check https://aka.ms/exov3-module  
----------------------------------------------------------------------------------------
```

## Answers

_No answers on this thread._
