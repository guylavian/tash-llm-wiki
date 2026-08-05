---
title: "renewing Microsoft Exchange Server Auth Certificate in hybrid Exchange Serverhy 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1609534/renewing-microsoft-exchange-server-auth-certificat
question_id: 1609534
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
---
# renewing Microsoft Exchange Server Auth Certificate in hybrid Exchange Serverhy 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1609534/renewing-microsoft-exchange-server-auth-certificat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears,

I Have hybrid Exchange Server 2019 in my environment, last week my Microsoft Exchange Server Auth Certificate has expired and ECP/OWA stopped from working, so I renewed the certificate by using these commands:

[PS] C:>New-ExchangeCertificate -KeySize 2048 -PrivateKeyExportable $true -SubjectName "cn=Microsoft Exchange Server Auth Certificate" -FriendlyName "Microsoft Exchange Server Auth Certificate" -DomainName @()

[PS] C:>Set-AuthConfig -NewCertificateThumbprint "000000000000000000000000" -NewCertificateEffectiveDate (Get-Date)

[PS] C:>Set-AuthConfig -PublishCertificate

[PS] C:>Set-AuthConfig -ClearPreviousCertificate

[PS] C:>Restart-Service "MSExchangeServiceHost"

 

After one day from that OWA/ECP back to work again but when I am comparing the old Auth Certificate with new one, I Can see some differences as shown below (Namespaces) are different on both Certificates. is that problem in future?

 

Do I have to re-run HW again to update (Azure AD) or I can just update them manually?

 

 

Certificate:

                                FriendlyName: Microsoft Exchange Server Auth Certificate

                                Thumbprint: 0000000000000000000

                                Lifetime in days: 1819

                                Certificate has expired: False

                                Certificate status: Valid

                                Key size: 2048

                                Signature Algorithm: sha256RSA

                                Signature Hash Algorithm: sha256

                                Bound to services: SMTP

                                Internal Transport Certificate: False

                                Current Auth Certificate: True

                                Next Auth Certificate: False

                                SAN Certificate: False

                                Namespaces:

                                                Microsoft Exchange Server Auth Certificate

               

               

                Certificate:

                                FriendlyName: Microsoft Exchange Server Auth Certificate

                                Thumbprint: 0000000000000000000000000000000

                                Lifetime in days: -8

                                Certificate has expired: True

                                Certificate status: Invalid

                                Key size: 2048

                                Signature Algorithm: sha256RSA

                                Signature Hash Algorithm: sha256

                                Bound to services: SMTP

                                Internal Transport Certificate: False

                                Current Auth Certificate: False

                                Next Auth Certificate: False

                                SAN Certificate: False

                                Namespaces:

                                                ACS

thank you.

## Answers

_No answers on this thread._
