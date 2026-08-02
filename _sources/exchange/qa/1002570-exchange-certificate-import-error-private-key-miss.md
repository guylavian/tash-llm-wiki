---
title: "Exchange Certificate Import Error: Private Key Missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1002570/exchange-certificate-import-error-private-key-miss
question_id: 1002570
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Certificate Import Error: Private Key Missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1002570/exchange-certificate-import-error-private-key-miss (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

I am currently setting up an Exchange Server & Outlook for a website and have been trying to install a certificate for Domain Validation.     

I opened the Exchange Server Powershell and imported it with `Import-ExchangeCertificate -Server "<ServerName>" -FileData ([System.IO.File]::ReadAllBytes('C:\Certificates\groupname.p7c')) -PrivateKeyExportable:$true -Password (ConvertTo-SecureString -String '<password>' -AsPlainText -Force)`,     

then attempted to enable it with `Enable-ExchangeCertificate -Server "<ServerName>" -Thumbprint <XXXXXXXXXXXXXXXXXXXXX> -Services SMTP,IMAP,IIS`     

and got back this error:    

 `A special Rpc error occurs on server SERVERNAME: The certificate with thumbprint     XXXXXXXXXXXXXXXXXXXXX was found but is not valid for use with Exchange Server (reason:     PrivateKeyMissing).         + CategoryInfo          : NotSpecified: (:) [Enable-ExchangeCertificate], InvalidOperationException       + FullyQualifiedErrorId : [Server=<SERVER-NAME>,RequestId=d09d4e8e-b66e-4235-9aef-998de9bc86ab,TimeStamp=9/11/2022 9:      20:12 PM] [FailureCategory=Cmdlet-InvalidOperationException] DA6D9EA1,Microsoft.Exchange.Management.SystemConfigur       ationTasks.EnableExchangeCertificate         + PSComputerName        : <servername.website_address>`  

For reference, I attempted to follow the instructions at website 0000251, and while using the command `certutil -repairstore my “SerialNumber”` in the command prompt a Windows Security tab popped up "Select a smart card device, connect a smart card."    

Do I need a smart card to fix my certificate? I understand that an admin usually uses a smart card for the `certutil` command. Is there any other way I can fix the above issue `PrivateKeyMissing`? Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-12*

Make sure the Exchange server supports your cert type for importing. The following types of certificate files are supported(Import or install a certificate on an Exchange server):    

-PKCS #12 certificate files: Binary certificate files that have .cer, .crt, .der, .p12, or .pfx filename extensions, and require a password when the file contains the private key or chain of trust.    

-PKCS #7 certificate files: Certificate files that have .p7b or .p7c filename extensions    

Check these helpful links - https://community.spiceworks.com/topic/2315124-ssl-not-showing-in-exchange-2016-after-import    

https://shellybhardwaj.medium.com/exporting-and-importing-exchange-server-2016-ssl-certificates-a97af2267469    

https://www.digicert.com/support/tools/certificate-utility-for-windows
