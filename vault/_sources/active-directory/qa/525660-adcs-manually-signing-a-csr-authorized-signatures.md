---
title: "ADCS - Manually signing a CSR (authorized signatures)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/525660/adcs-manually-signing-a-csr-authorized-signatures
question_id: 525660
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# ADCS - Manually signing a CSR (authorized signatures)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/525660/adcs-manually-signing-a-csr-authorized-signatures (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In our PKI environment there are some templates that require an additional signature from authorized personnel ("This number of authorized signatures: 1" etc.) which works very well.  

A requirement we have now confronted with, is that certificate request from external sources shall be allowed (after proper exmination).  

My problem is, that i cant find a solution to additionally sign those CSR to fulfill the requirement for those templates, which require being singed with a certificate with a custom application policy for the authorized personnel.  

I tried using "certreq.exe" with the "sign" parameter as pointed out on several websites. This always fails with the error message "The data is invalid".  

Another suggestion was to use a relative empty "policy.inf" file containing nothing but "Signature="$Winows NT$" and then using "certreq.exe" with the "policy" and "cert" switch. Since this seems only to work for signing certificates which contain the "Certifcate Request Agent" application policy it seems that im stuck.  

Is there any way to manually sign a CSR so that it will be accepted from a Microsoft CA for a template which requires that specific additional signature?  

Regards,  

Peter

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-25*

Hello Peter,  

Graphical user interface:  

Open a browser and go to the IP address of the Microsoft certificate server.  

Click Request a certificate.  

On the Request a certificate page, click advanced certificate request.  

On the Advanced Certificate Request page, click Submit a certificate request by using a base-64-encoded CMC or PKCS #10 file, or submit a renewal request by using a base-64-encoded PKCS #7 file.  

On the Submit a Certificate Request or Renewal Request page, paste the contents of the CSR file you downloaded from Enterprise Threat Protector.  

In the Certificate Template list, select Subordinate Certificate Authority.  

Click Submit.  

On the Certificate Issued page, select Base 64 encoded.  

Click Download certificate and save the certificate to a secure location.  

Command line interface  

How to  

On the Microsoft certificate server, open a command prompt and run it as an administrator.  

Enter this command:  

certreq -submit -attrib “CertificateTemplate:SubCA” <certificateSigningRequest.csr>  

where <certificateSigningRequest.csr> is the certificate signing request you generated  

The Certification Authority List dialog appears.  

Select the Certificate Authority (CA) that you want to sign the request and click OK.  

Save the certificate as a .der file.  

Luis P
