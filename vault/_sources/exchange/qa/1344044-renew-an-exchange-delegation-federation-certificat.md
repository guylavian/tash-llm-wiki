---
title: "Renew an Exchange Delegation Federation Certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1344044/renew-an-exchange-delegation-federation-certificat
question_id: 1344044
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Renew an Exchange Delegation Federation Certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1344044/renew-an-exchange-delegation-federation-certificat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently noticed my Exchange Delegation Federation certificate ia about to expire. I wanted to go ahead an renew it so Exchange would'n be barking to me about an expired certificate. I followed the procedures here https://learn.microsoft.com/en-us/exchange/renew-the-federation-certificate-exchange-2013-help#step-2-configure-the-new-certificate-as-the-federation-certificate and was able to complete Step 1 to create the certificate

I then went to Step 2 "Set-FederationTrust -Identity "Microsoft Federation Gateway" -Thumbprint <Thumbprint> -RefreshMetaData" entering the Thumbprint but I got an error that says "Cannot update certificate until the federation trust is provisioned with STS." 

We have a standalone Exchange 2019 server with no Federation Trust set up. I assume the certificate we have now must of come from back when we had Exchange Online. Since we don't have any Federation Trust's set up can I go ahead and delete the two certificates (old and new) or is there a way to renew the certificate so it doesn't keep telling me it is expired?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-08-10*

Renewing a Federation Delegation Certificate for Exchange Server 2019 involves a few steps to ensure a smooth process. Here's a step-by-step guide:

Step 1: Generate a Certificate Signing Request (CSR)

Open the Exchange Management Shell.

-  Run the following command to generate a CSR:

```
New-ExchangeCertificate -GenerateRequest -SubjectName "CN=Federation Delegation" -DomainName federation.domain.com -PrivateKeyExportable $true -KeySize 2048 -Path "C:\FederationDelegation.csr"
```

Replace `federation.domain.com` with the appropriate domain name.

The CSR will be saved to the specified path (e.g., `C:\FederationDelegation.csr`). Keep this file safe; you'll need it to obtain the renewed certificate.

Step 2: Obtain the Renewed Certificate

-  Submit the CSR to your preferred Certificate Authority (CA) or use a third-party CA service to obtain a renewed certificate.

Step 3: Install the Renewed Certificate

Once you receive the renewed certificate, open the Exchange Management Shell.

-  Run the following command to install the renewed certificate:

```
Import-ExchangeCertificate -FileData ([Byte[]]$(Get-Content -Path "C:\Path\To\RenewedCertificate.cer" -Encoding Byte -ReadCount 0)) -PrivateKeyExportable $true
```

Replace `"C:\Path\To\RenewedCertificate.cer"` with the actual path to your renewed certificate file.

-  Enable the certificate for Federation Delegation:

```
Enable-ExchangeCertificate -Thumbprint  -Services Federation
```

Replace `<Thumbprint>` with the thumbprint of the renewed certificate.

Step 4: Refresh Federation Metadata

-  Update the Federation Trust with the new certificate's thumbprint. Run the following command:

```
Set-FederationTrust -Identity "Microsoft Federation Gateway" -Thumbprint  -RefreshMetaData
```

Replace `<Thumbprint>` with the thumbprint of the renewed certificate.

Step 5: Test the Renewed Certificate

-  Test the renewed certificate to ensure it's working as expected. You can use tools like the Microsoft Remote Connectivity Analyzer to verify federation functionality.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-09*

I attempted update the Federation Trust with the new certificate's thumbprint, I receive the following error:  

"Cannot update certificate until the federation trust is provisioned with STS."  

Thanks in advance!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-08-10*

Hi I think you have two options:

-  Start from the beginning and Create a new fed trust: https://learn.microsoft.com/en-us/exchange/configure-a-federation-trust-exchange-2013-help

-  Delete the almost expired federation certs and leave it at that.

If you do not need the federation trust, then 2 is prob ok. But if it still throws errors or irritates, the go with Step 1.

The OAuth cert is a different issue. Do not let that one expire:

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/cannot-access-owa-or-ecp-if-oauth-expired
