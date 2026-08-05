---
title: "Cannot access exchange server from external networks"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2137851/cannot-access-exchange-server-from-external-networ
question_id: 2137851
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Cannot access exchange server from external networks

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2137851/cannot-access-exchange-server-from-external-networ (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I set up an exchange server in my home lab, it's working smoothly on my network, I can access my owa and ecp link from all my workstation inside my network, I have my domain registered and also configured the A record to my public IP address, but cannot reached my exchange server from an external network nor send email to external email addresses, I was told that Comcast blocked port 25 in residential areas, is there any other way that I can bypass that or use a different secured port ?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-30*

Hi @Gregory Aku，

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you are facing the problem that you cannot access the exchange server from the external network and cannot send emails to external email addresses. You learned that Comcast blocks port 25 in residential areas and wonder if there are other ways to bypass it or use other secure ports. As you described, this may be the reason why Comcast blocks port 25. You can try the following steps to use other ports:

-  In EAC, go to "Mail Flow > Receive Connectors". In the list of receive connectors, select Client Frontend <Server name> and click Edit.

-  In the Exchange Receive Connector page that opens, click Scoping. In the FQDN field, enter the SMTP server FQDN to be used for authenticated SMTP client connections. Make sure the port of the connector is set to 587 and the encryption method is set to TLS.

-  Specify the certificate for authenticated SMTP client connections through the command.

```
$TLSCert = Get-ExchangeCertificate -Thumbprint 
```

```
$TLSCertName = "$($TLSCert.Issuer)$($TLSCert.Subject)"
```

```
Get-ReceiveConnector -Identity "Client Frontend*" | Set-ReceiveConnector -TlsCertificateName $TLSCertName
```

-  Configure Outlook on the web to display the SMTP settings server for authenticated SMTP clients through commands.

```
Get-ReceiveConnector -Identity "Client Frontend*" | Set-ReceiveConnector -AdvertiseClientSettings $true
```

Refer to: Configure authenticated SMTP settings for POP3 and IMAP4 clients in Exchange Server | Microsoft Learn

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne
