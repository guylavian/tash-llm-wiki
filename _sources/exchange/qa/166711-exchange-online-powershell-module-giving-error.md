---
title: "Exchange Online powershell Module giving error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/166711/exchange-online-powershell-module-giving-error
question_id: 166711
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# Exchange Online powershell Module giving error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/166711/exchange-online-powershell-module-giving-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are using an O365-app based authentication to connect to Exchange Online services.    

(Please refer to the following Microsoft's documentation on how to setup an app-only authentication which doesn't require an Office 365 account for verification.    

https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps#setup-app-only-authentication )    

For more information about the module we used please refer the below link.    

https://o365reports.com/2020/07/04/modern-auth-and-unattended-scripts-in-exchange-online-powershell-v2/    

Now, when we run the following PowerShell scripts as the logged-in user of a computer and use certificate-based authentication to connect to the Exchange Online services, it works fine without any issues.    

Import-Module .\ExchangeOnlineManagement    

$sessopt = New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck -ProxyAccessType IEConfig    

$certkey = ConvertTo-SecureString "<EnterCertificateKeyHere>" -AsPlainText -Force    

Connect-ExchangeOnline -CertificateFilePath "Path to cert" -AppId <EnterAppIdHere> -Organization "yourtenant.onmicrosoft.com" -CertificatePassword $certkey -PSSessionOption $sessopt    

But when we open the PowerShell window under the privilege of a 'NT AUTHORITY\SYSTEM' user and use the certificate-based authentication above to connect to Exchange Online Services, it throws an error : "New-ExoPSSession : Object reference not set to an instance of an object"    

Note:     

-  Only the privilege of the SYSTEM (NT AUTHORITY\SYSTEM) account is used to open the PowerShell window.     

-  The connection to Exchange Online is done using the Office 365 app-based authentication and not using an Office 365 account.    

-  We use a proxy server in our environment    

What could be wrong ?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-23*

I have submited feedback to the production team, but no answer yet

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-19*

@Jóhann MW Einarsson      

As far as I know, this is an expected behavior, because the certificate contains your personal information that used to connect and verify account. So, you need to connect to Exchange online with login account.    

But, for more detailed information, I would suggest you click the "Submit and view feedback for this product" at the end of the first article to submit a request to product team. They will could double confirm whether is this an expected behavior, it will also help improve the product.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
