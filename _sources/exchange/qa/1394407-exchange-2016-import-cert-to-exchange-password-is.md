---
title: "Exchange 2016 - import cert to exchange - password is incorrect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1394407/exchange-2016-import-cert-to-exchange-password-is
question_id: 1394407
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 - import cert to exchange - password is incorrect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1394407/exchange-2016-import-cert-to-exchange-password-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have a problem with importing a new certificate to Exchange 2016 CU23.

I used a command from MS but it's not working.

```
[PS] C:\Windows\system32>Import-ExchangeCertificate -FileData ([System.IO.File]::ReadAllBytes('C:\Cert\cert.pfx')) -Password (ConvertTo-SecureString -String 'Password' -AsPlainText -Force)
A special Rpc error occurs on server EXCHANGE2016: The source data cannot be imported or the wrong password was specified.
    + CategoryInfo          : ReadError: (:) [Import-ExchangeCertificate], InvalidOperationException
    + FullyQualifiedErrorId : [Server=EXCHANGE2016,RequestId=3232dd3e-66c7-4d5c-a443-e25f826ad200,TimeStamp=17.10.2
   023 10:55:40] [FailureCategory=Cmdlet-InvalidOperationException] A39CF339,Microsoft.Exchange.Management.SystemConf
  igurationTasks.ImportExchangeCertificate
    + PSComputerName        : exchange2016.contoso.local
```

I tried to add a cert via exchange powershell and mmc>certificates but I have an error with the wrong password.

When I try to add this cert to a local computer it's working, the password is correct and I can import it.

Any suggestions? How can I import a new cert correctly?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-11-27*

I found solution. Use this parameters:

```
openssl pkcs12 -export -certpbe PBE-SHA1-3DES -keypbe PBE-SHA1-3DES -nomac -inkey contoso.com.key -in contoso.com.crt -out contoso.com-legacy.pfx
```

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-17*

You will need to provide the password for the exported private key for that cert. 

IF you dont know it, then export the original cert again with the private key and a new password.
