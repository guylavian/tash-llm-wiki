---
title: "Unable to open Exchange Management Shell on Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1111186/unable-to-open-exchange-management-shell-on-exchan
question_id: 1111186
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Unable to open Exchange Management Shell on Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1111186/unable-to-open-exchange-management-shell-on-exchan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have Exchange 2016. I failed to open Exchange Management Shell. The issue happened after I patched CU23. The error message is below.

New-PSSession : [Exchange.mycompany.com] Connecting to remote server Exchange.mycompany.com failed with

the following error message : The WinRM client cannot process the request. It cannot determine the content type of the

HTTP response from the destination computer. The content type is absent or invalid. For more information, see the

about_Remote_Troubleshooting Help topic.

At line:1 char:1

-  New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Microsoft.Excha ...

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  CategoryInfo : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin

gTransportException

-  FullyQualifiedErrorId : -2144108297,PSSessionOpenFailed

Please help!

Thanks,

## Answer (community) — community member

*upvotes: 1 · updated: 2022-12-01*

Hi @Grace Yin  ,    

According to error messages, here are some troubleshooting steps for your reference and hope these help you:    

-  Since freshly installed Exchange servers may not be configured to accept incoming PowerShell connections. To fix this and let your server configure all the necessary services, execute the following command in PowerShell:         Enable-PSRemoting  

Above solution is mentioned in the blog you could refer to it: How to fix problems related to remote PowerShell connections    

-  Checking if SSL certificate was no longer bound to the Exchange Back End website on that Exchange 2016 server. To fix this, in IIS Manager right-click the Exchange Back End website and click Bindings, Highlight https and click Edit, choose the certificate you want to bind to the site. Then run iisreset in cmd, retry EMS.     

Detailed information: The WinRM Shell Client Cannot Process the Request    

-  Make sure the DNS is working perfectly. Then open iis in exchange 2016, select default Website -->Power Shell. Change the physical path from: C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\PowerShell to: C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\PowerShell. At last, restart IIS.    

A similar thread for your reference as well: Exch 2016 Management Shell Broken - TheWinRM client cannot process the request    

Please Note: Since the web sites  are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-10*

It appears your Exchange Management Shell (EMS) is failing after applying Cumulative Update 23 to Exchange Server 2016. Let's systematically address this issue.

Initial Observations

-  The error suggests WinRM communication problems

-  Your failover Exchange server works fine with the same credentials

-  Repair attempts with CU23 setup.exe have failed

Recommended Troubleshooting Steps

1. Basic WinRM Checks

```
Test-WSMan -ComputerName localhost
```

If this fails, WinRM might be corrupted.

2. Re-register WinRM

```
winrm quickconfig

winrm invoke Restore winrm/Config
```

3. Check Exchange Backend Services

Ensure these services are running:

-  Microsoft Exchange Service Host

-  Microsoft Exchange Remote Procedure Call (RPC)

-  World Wide Web Publishing Service

-  Windows Remote Management (WS-Management)

4. Rebuild Exchange PowerShell Virtual Directory

```
Remove-PowerShellVirtualDirectory -Identity "Exchange.mycompany.com\PowerShell (Default Web Site)"

New-PowerShellVirtualDirectory -InternalURL "https://Exchange.mycompany.com/PowerShell" -ExternalURL "https://Exchange.mycompany.com/PowerShell"

Restart-WebAppPool MSExchangePowerShellAppPool

iisreset
```

5. Repair Installation

Since CU23 setup fails, try:

-  Uninstall CU23 via Control Panel > Programs and Features

-  Reinstall CU23 with administrative privileges

-  Use `/m:RecoverServer` switch if needed

6. Check Event Logs

Examine these logs for detailed errors:

-  Application and Services Logs > Microsoft > Exchange > Management

-  Windows Logs > Application

-  Windows Logs > System

7. Alternative Access Methods

Try connecting to EMS using:

```
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://Exchange.mycompany.com/PowerShell/ -Authentication Kerberos

Import-PSSession $Session
```

8. Last Resort Options

If all else fails:

-  Consider restoring from backup

-  Prepare for a server rebuild using `/m:RecoverServer`

if my response helps, you may share your vote so others can get information on your case url.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-10*

New-PSSession : [mail2.Domain.com Connecting to remote server mail2.Domain.com failed with the following error message :  For more information, see the about_Remote_Troubleshooting Help topic. At line:1 char:1 + New-PSSession -ConnectionURI "$connectionUri" -ConfigurationName Micr ... + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     + CategoryInfo          : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin    gTransportException     + FullyQualifiedErrorId : -2144108477,PSSessionOpenFailed
