---
title: "Renew Exchange Cert"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1377026/renew-exchange-cert
question_id: 1377026
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Renew Exchange Cert

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1377026/renew-exchange-cert (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Our Setup

-  Server 2012

-  Exchange 2016

Our environment is Hybrid

Our Exchange cert was about to expire so I have renew it using below setup but some of the mailbox flow is failing for internal domain

Steps

-  Run this command on both Exchange Servers 

-  Enable-ExchangeCertificate -Thumbprint "New Cert" -Services IIS,SMTP

-  Then Run

```
1. $TLSCert = Get-ExchangeCertificate -Thumbprint "New Cert"

                       $TLSCertName = "$($TLSCert.Issuer)$($TLSCert.Subject)"
```

-  Then Run 

```
1. Get-SendConnector "Outbound to Office 365*" | Set-SendConnector -TlsCertificateName $TLSCertName
```

-  Then Run

```
1. Set-ReceiveConnector "xxxxx\Default Frontend xxx" -TlsCertificateName $TLSCertName

                                         Set-ReceiveConnector "xxxx\Default Frontend xxxx" -TlsCertificateName $TLSCertName
```

-  Restart IIS

-  Restart Transport service and Frontend Transport service

-  Run Hybrid wizard with default selection and select new cert at the end

Now When we send email to internal address its failing with this message

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-28*

Hi @lalajee  

I would like to confirm with you where the email addresses of your internal recipient and sender are?

Are they all local? Or is the sender local and the recipient online?

Also, I found this: Error code: 450 4.4.315 Connection timed out

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
