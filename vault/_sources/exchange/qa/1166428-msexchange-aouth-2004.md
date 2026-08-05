---
title: "MSExchange AOuth 2004"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166428/msexchange-aouth-2004
question_id: 1166428
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MSExchange AOuth 2004

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166428/msexchange-aouth-2004 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. I got warning:

MSExchange AOuth 2004

```
MSExchange OAuth

Категория задачи:Configuration
Уровень:       Предупреждение
Ключевые слова:Классический
Пользователь:  Н/Д
Компьютер:    MOS-MAIL.avalonelectrotech.local
Описание:
Unable to find the certificate with thumbprint 37C191846F81EB292B98DC0A8CC396B707879CEE in the current computer or the certificate is missing private key. The certificate is needed to sign the outgoing token.Xml
```

I issued and installed a new certificate: https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/exchange-oauth-authentication-could-not-find-the-authorization

But the warning persists.

More info:

```
[PS] C:\Windows\system32>Get-ExchangeCertificate | fl

AccessRules        :
CertificateDomains : {avalonelectrotech.local}
HasPrivateKey      : True
IsSelfSigned       : True
Issuer             : CN=Microsoft Exchange Server Auth Certificate
NotAfter           : 02.02.2028 4:22:23
NotBefore          : 02.02.2023 4:22:23
PublicKeySize      : 2048
RootCAType         : None
SerialNumber       : 5D1D9B5065DDD69F40A1DE59B3369AAA
Services           : SMTP
Status             : Valid
Subject            : CN=Microsoft Exchange Server Auth Certificate
Thumbprint         : 3DAF40EC85C62DD39D98696AB5413E3EB83D6415

AccessRules        :
CertificateDomains : {MOS-MAIL, MOS-MAIL.avalonelectrotech.local}
HasPrivateKey      : True
IsSelfSigned       : True
Issuer             : CN=MOS-MAIL
NotAfter           : 02.02.2028 3:09:22
NotBefore          : 02.02.2023 3:09:22
PublicKeySize      : 2048
RootCAType         : Registry
SerialNumber       : 49B8393042D5D59F4AE6D301FDF8C963
Services           : IMAP, POP, IIS, SMTP
Status             : Valid
Subject            : CN=MOS-MAIL
Thumbprint         : BBA9F942B32F3E0F6E0C4E735BD1F38D4C06612E

AccessRules        :
CertificateDomains : {WMSvc-SHA2-MOS-MAIL}
HasPrivateKey      : True
IsSelfSigned       : True
Issuer             : CN=WMSvc-SHA2-MOS-MAIL
NotAfter           : 30.01.2033 2:48:33
NotBefore          : 02.02.2023 2:48:33
PublicKeySize      : 2048
RootCAType         : Registry
SerialNumber       : 4341D5BCC9FCF9B9445659D0F3E50968
Services           : None
Status             : Valid
Subject            : CN=WMSvc-SHA2-MOS-MAIL
Thumbprint         : 7274AA46956DFF4E80B13168A7B6B0037C99CA14
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-03*

Hi @Андрей Михалевский  ,

In some environments, it may take an hour for the OAuth certificate to be published.

So you can clear the old certificate after you deploy the new certificate to the Exchange server:

```
Set-AuthConfig -ClearPreviousCertificate
```

Then restart the Microsoft Exchange Service Host Service and run the following command (in elevated mode) to recycle the OWA and ECP app pools:

```
Restart-WebAppPool MSExchangeOWAAppPool
Restart-WebAppPool MSExchangeECPAppPool
```

 

For detailed steps on this error, please refer to the Workaround section in this link:

You can't access OWA or ECP after you install Exchange Server 2016 CU6 - Microsoft Support

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
