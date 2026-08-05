---
title: "Creating a Certificate for Exchange Server 2019 Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2005284/creating-a-certificate-for-exchange-server-2019-is
question_id: 2005284
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Creating a Certificate for Exchange Server 2019 Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2005284/creating-a-certificate-for-exchange-server-2019-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I tried to create a certificate for Exchange server 2019 cu12, I've designated my Active Directory as a Certificate Authority(CA), then  I've created a CSR on Exchange by running the following commands:

$binrequest = New-ExchangeCertificate -GenerateRequest -BinaryEncoded -SubjectName "c=US,o=Woodgrove Bank,cn=mail.woodgrovebank.com" -DomainName autodiscover.woodgrovebank.com,mail.fabrikam.com,autodiscover.fabrikam.com

[System.IO.File]::WriteAllBytes('\FileServer01\Data\woodgrovebank.pfx', $binrequest.FileData)

When I try to open the certificate request file, an message appeared says"This file is invalid for use as the following:Personal Information Exchange"

So, what must I do for taking the request file and put it into the Certificate Authority to create the certificate and import it to the Exchange Server2019 cu12

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-26*

Hi @Mahmoud Teleb,

Welcome to the Microsoft Q&A platform!

It looks like you're creating a certificate request (CSR) for your Exchange Server 2019 CU12 and encountering an issue with the format of the request file. The error "This file is invalid for use as the following: Personal Information Exchange" suggests that the file you generated is not in the correct format for the task you're attempting.

Here's a step-by-step guide to correctly create and use the CSR file:

-  Create the CSR (Certificate Signing Request):

   Use the following PowerShell command to generate a Base64-encoded CSR file, which is more commonly used for submission to a CA.

```
$csr = New-ExchangeCertificate -GenerateRequest -SubjectName "c=US,o=Woodgrove Bank,cn=mail.woodgrovebank.com" -DomainName autodiscover.woodgrovebank.com,mail.fabrikam.com,autodiscover.fabrikam.com
   Set-Content -Path '\\FileServer01\Data\woodgrovebank.req' -Value $csr
```

   This will create a CSR in the proper format for you to submit to your CA.

-  Submit the CSR to the CA:

   - On your CA server, open the Certification Authority console.

   - Right-click on the CA name -> All Tasks -> Submit a new request.

   - Browse to the file `woodgrovebank.req` that you created and submit it.

-  Issue the Certificate:

   - Once the request is submitted, go to Pending Requests in the Certification Authority console.

   - Find your request, right-click on it, and choose 'Issue.'

   - Go to the Issued Certificates section, find your certificate, right-click on it, and choose 'Export' to export the certificate (in DER encoded .cer file format).

-  Import the Certificate to Exchange Server:

   Use the following PowerShell command to import the certificate to the Exchange server:

```
Import-ExchangeCertificate -FileData ([Byte[]]$(Get-Content -Path "\\FileServer01\Data\woodgrovebank.cer" -Encoding Byte -ReadCount 0)) -FriendlyName "WoodgroveBankCertificate"
```

-  Enable the Certificate for Exchange Services:

   Use the following PowerShell command to enable the certificate for the required Exchange services (e.g., IIS, SMTP):

```
Enable-ExchangeCertificate -Thumbprint  -Services IIS,SMTP
```

   Replace `<ThumbprintGenerated>` with the actual thumbprint from the imported certificate.

By following these steps, you should be able to create a CSR, submit it to your CA, obtain the certificate, and import it into your Exchange Server 2019 CU12.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
