---
title: "Creating certificates in Exchange Server 2019 CU12"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1276584/creating-certificates-in-exchange-server-2019-cu12
question_id: 1276584
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Creating certificates in Exchange Server 2019 CU12

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1276584/creating-certificates-in-exchange-server-2019-cu12 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As you already may know starting from CU12 we need to use PS for creating certificates:

https://learn.microsoft.com/en-us/exchange/architecture/client-access/create-ca-certificate-requests?view=exchserver-2019

Here's the example that I followed (SAN certificate section):

`$txtrequest = New-ExchangeCertificate -PrivateKeyExportable $True -GenerateRequest -FriendlyName "Contoso.com SAN Cert" -SubjectName "C=US,CN=mail.contoso.com" -DomainName autodiscover.contoso.com,legacy.contoso.com,mail.contoso.net,autodiscover.contoso.net,legacy.contoso.net`

`[System.IO.File]::WriteAllBytes('\\FileServer01\Data\Contoso SAN Cert.req', [System.Text.Encoding]::Unicode.GetBytes($txtrequest))`

Please pay attention to the following fact: the FQDN in the SubjectName field (CN=mail.contoso.com here) is NOT added to the -DomainName field - and this is in strict compliance with the theory:

"For a subject alternative name (SAN) certificate, you should choose one of the values from the DomainName parameter to use in the SubjectName value. In fact, the CN value that you specify for SubjectName is automatically included in the DomainName values."

So I followed that example and created my own certificate (SubjectName = mail.contoso1.net, DomainName = autodiscover.contoso1.net):

And this certificate does really contain two FQDN - exactly as was mentioned in the document above:

 

So far so good... The final test - accessing the ECP:

??? ... looks like the only domain name for this certificate were the autodiscover.contoso1.net - but the SubjectName was mail.contoso1.net!

I repeated my test by including the mail.contoso1.net into the DomainNames field (forgetting to change its name!):

...and got exactly the same result in ECP:

After importing the new certificate the issue has gone:

Q1: Can someone suggest any explanation to this?

Q2: Does anybody know why MS has removed the possibility to create/import certificates in GUI?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-11*

Thank you all for your replies! Sorry for the delay...

Regarding the issue with the certificate:

-  "It seems that your certificate does not contain the IP as a SAN." - no. it doesn't... should it? It can't be the cause of the issue (especially because the second certificate does not contain it either).

-  "For your old certificate is not trusted locally, I would like to know if you have this certificate installed in the following directory of Exchange Server:" - I've never added it manually to that directory but the problem here is NOT that the certificate was not trusted, the problem that the first certificate did not not contain the FQDN - the same FQDN that had been typed in the CN field - while it should had been added according to the article mentioned above!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-08*

Hi @ Mikhail Firsov,

The certificate request feature in Exchange Admin Center is removed to prevent misuse of UNC paths by attackers. Therefore, Microsoft removed the parameters that take UNC paths as inputs from the Exchange Server PowerShell cmdlets and the Exchange Admin Center. 

In previous versions of Exchange Server, there were several places regarding certificates that required the administrator to provide UNC path input, so the following features were also removed:

-  Import & Export Exchange Certificate removal

-  Complete Exchange Certificate Request removal

-  New Exchange Certificate Request from CA removal

-  Renew Exchange Certificate Request removal

 

For more information, see this update: Changes in Exchange Server PowerShell cmdlets and Exchange Admin Center for UNC path inputs (KB5014278) - Microsoft Support

For your old certificate is not trusted locally, I would like to know if you have this certificate installed in the following directory of Exchange Server:

Personal

Trusted Root Certification Authorities

-  Intermediate Certification Authorities

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-08*

It seems that your certificate does not contain the IP as a SAN.

Also, please take a look at this: https://serverfault.com/questions/641504/ssl-on-iis8-5-working-with-named-url-but-localhost-results-in-err-cert-common
