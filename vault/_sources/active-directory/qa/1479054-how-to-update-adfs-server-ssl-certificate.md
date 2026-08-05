---
title: "How to update ADFS server SSL certificate?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1479054/how-to-update-adfs-server-ssl-certificate
question_id: 1479054
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to update ADFS server SSL certificate?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1479054/how-to-update-adfs-server-ssl-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As shown in the link https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/change-ad-fs-2-dot-0-service-communications

I have followed steps 1, 2, and 4 to update the SSL certificate on the ADFS server, but I am unable to complete step 3 because I cannot find IIS on ADFS server and it seems that IIS is not installed on my ADFS server? How should I update the SSL certificate of ADFS?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-03-16*

Old question.   But in the interest in having a better answer than the one above....

ADFS has not used IIS for over a decade.  Those instructions are quite old, ignore them.

More recent ones...

https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/manage-ssl-certificates-ad-fs-wap

or from the azure entra connect GUI.

https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-fed-ssl-update

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-01-05*

If you cannot find IIS on your ADFS server, it’s likely that IIS is not installed. However, you can still update the SSL certificate of ADFS without IIS. Here are the steps you can follow:

Obtain your TLS/SSL certificates: For production AD FS farms, a publicly trusted TLS/SSL certificate is recommended. AD FS obtains this certificate by submitting a certificate signing request (CSR) to a third party, public certificate provider.

Import the certificate to the local machine store on each AD FS and WAP: After you get the response from your certificate provider, import it to the local machine store on each AD FS and WAP.

Install the new TLS/SSL certificate: On the primary AD FS server, use the following PowerShell cmdlet to install the new TLS/SSL certificate:

```
Set-AdfsSslCertificate -Thumbprint ''
```

Please replace `<thumbprint of new cert>` with the thumbprint of your new certificate.

The recommended way to replace the TLS/SSL certificate going forward for an AD FS farm is to use Microsoft Entra Connect. You can use the Microsoft Entra Connect tool to easily update the TLS/SSL certificate for the AD FS farm even if the user sign-in method selected is not AD FS.

Please note that the AD FS TLS/SSL certificate isn’t the same as the AD FS Service communications certificate found in the AD FS Management snap-in. To change the AD FS TLS/SSL certificate, you need to use PowerShell.

I hope this helps! If you have any more questions, feel free to ask.

References:

-  Microsoft Documentation: https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/change-ad-fs-2-dot-0-service-communications 

-  Microsoft Entra Connect: https://www.microsoft.com/en-us/entra/connect
