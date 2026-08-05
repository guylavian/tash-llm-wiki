---
title: "How to mock exchange invokation using Microsoft Powershell SDK"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1070197/how-to-mock-exchange-invokation-using-microsoft-po
question_id: 1070197
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
---
# How to mock exchange invokation using Microsoft Powershell SDK

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1070197/how-to-mock-exchange-invokation-using-microsoft-po (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I am implementing a console app which connects to exchange and get journal rules. I am using Microsoft Powershell SDK to connect to exchange environment.    

I am using following code to create powershell object.    

```
var rs = RunspaceFactory.CreateRunspace();  
rs.Open();  
var ps1 = PowerShell.Create();  
ps1.Runspace = rs;  
var ps2 = PowerShell.Create();  
ps2.Runspace = rs;  
  
var cc = ps1.AddScript("Get-InstalledModule ExchangeOnlineManagement").Invoke();  
                if (cc.Count == 0)  
                {  
                    //*Following should run once per development environment.  
                    ps1.AddScript("[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12").Invoke();  
                    Console.WriteLine("Please wait ....2");  
                    ps1.AddScript("Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine").Invoke();  
                    ps1.AddScript("Import-Module PowerShellGet").Invoke();  
                    Console.WriteLine("Please wait ....3");  
                    ps1.AddScript("Install-PackageProvider -Name NuGet -Force -Confirm:$false").Invoke();  
                    ps1.AddScript("Install-Module -Name ExchangeOnlineManagement -Force").Invoke();                     
                    ps1.AddScript("Import-Module ExchangeOnlineManagement").Invoke();  
                }  
ps2.AddCommand(Commands.ConnectExchangeOnline).AddParameter(Parameters.Certificate, _tempPfxFile)  
                    .AddParameter(Parameters.CertificatePassword, new NetworkCredential("", certificatePassword).SecurePassword)  
                    .AddParameter(Parameters.AppID, appId)  
                    .AddParameter(Parameters.Organization, domain).Invoke();
```

Journal rules are retrieved using following code.    

```
var journalRules = await _powershellClient.AddScript(Scripts.GetJournalRule).InvokeAsync();
```

For the purpose of writing unit tests, I need to Mock the Powershell client to get journal rules. I referred documentation about Pester which can use to mock Powershell scripts.    

I need a way of mocking the Powershell client. Can some one suggest a way for it?

## Answers

_No answers on this thread._
