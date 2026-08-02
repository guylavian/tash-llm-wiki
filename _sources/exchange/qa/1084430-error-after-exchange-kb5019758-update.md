---
title: "Error after Exchange KB5019758 update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1084430/error-after-exchange-kb5019758-update
question_id: 1084430
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Error after Exchange KB5019758 update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1084430/error-after-exchange-kb5019758-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

KB5019758  was applied on our Exchange 2019 CU12,     

After restart Exchange services do not start giving this error when     

accesing via OWA :    

Server Error in '/owa' Application.    

Active Directory operation failed on . The supplied credential for 'NT AUTHORITY\SYSTEM' is invalid.    

Description: An unhandled exception occurred during the execution of the current web request. Please review the stack trace for more information about the error and where it originated in the code.    

Exception Details: System.ServiceModel.FaultException`1[[Microsoft.Exchange.Data.Directory.TopologyDiscovery.TopologyServiceFault, Microsoft.Exchange.Data.Directory, Version=15.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35]]: Active Directory operation failed on . The supplied credential for 'NT AUTHORITY\SYSTEM' is invalid.    

Source Error:    

An unhandled exception was generated during the execution of the current web request. Information regarding the origin and location of the exception can be identified using the exception stack trace below.    

Any help will be appreciated, thanks in advance    

Carlos Legrand

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-11-22*

Hi,    

Check the exchange back end ssl in iis. After this update ssl may drop to null

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-11-15*

This is not Exchange specific. A patch was applied to 2012, 2016, and 2019 domain controllers. Removing the patch listed below from the DCs resolved the issue for our network. This may be affecting other systems on your network. We have seen gpupdate failing on other systems throughout our network.    

The affected patches:    

kb5020023 - Windows Server 2012    

kb5019964 - Windows Server 2016    

kb5019966 - Windows Server 2019    

"It's complicated, but it basically boils down to the RC4 bit being used as a signal of whether it should use a preferred cipher list or a legacy interop list in a specific section of code."    

So, this update will break Kerberos for any computer that has RC4 disabled.     

https://dirteam.com/sander/2022/11/11/knowledgebase-you-experience-errors-with-event-id-14-and-source-kerberos-key-distribution-center-on-domain-controllers/    

This is what Microsoft support is telling people to do instead of uninstalling the patch. It reverses the changes made by the patch.    

Workaround from MSFT engineer is to add the following reg keys on all your DCs.    

reg add "HKLM\SYSTEM\CurrentControlSet\services\kdc" /v    

KrbtgtFullPacSignature /t REG_DWORD /d 0 /f    

reg add "HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters" /v    

RequireSeal /t REG_DWORD /d 0 /f    

reg add "HKLM\SYSTEM\CurrentControlSet\services\kdc" /v    

ApplyDefaultDomainPolicy /t REG_DWORD /d 0 /f

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-25*

lilyli2-msft    

Thank you all, problem solved restoring backup but today came back.    

ECP not  accesible, nor Exchange console    

Event viewer : The supplied credential for 'NT AUTHORITY\SYSTEM' is invalid.    

I will try michaelfuller-1588 solution and come again.    

Best regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-11*

Did you run setup/PrepareAllDomains when you installed Exchange?    

Do you have missing DCs?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-11*

Hi @Carlos Legrand  ,    

Welcome to our forum, here is my troubleshooting for this issue:    

-  Is the ECP accessible?    

-  Are there any errors in Event Viewer?    

-  Check Exchange Server OAuth certificate and try to create a new one:    

(1) Create a new OAuth certificate by running the following command:    

```
New-ExchangeCertificate -KeySize 2048 -PrivateKeyExportable $true -SubjectName "cn=Microsoft Exchange Server Auth Certificate" -FriendlyName "Microsoft Exchange Server Auth Certificate" -DomainName @()
```

(2) Set the new certificate for server authentication:    

```
Set-AuthConfig -NewCertificateThumbprint  -NewCertificateEffectiveDate (Get-Date)  
Set-AuthConfig -PublishCertificate  
Set-AuthConfig -ClearPreviousCertificate
```

(3) Restart the Microsoft Exchange Service Host Service.    

(4) restart IIS    

Please refer to this article for more details: cannot-access-owa-or-ecp-if-oauth-expired    

Besides, after installing Exchange Security update, you cannot access OWA or ECP, please read this article: owa-stops-working-after-update    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
