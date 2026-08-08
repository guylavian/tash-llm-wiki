---
title: "Microsoft AD CS (PKI) Template with \"Certificate Signing\" Key Usage"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1506330/microsoft-ad-cs-pki-template-with-certificate-sign
question_id: 1506330
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Microsoft AD CS (PKI) Template with "Certificate Signing" Key Usage

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1506330/microsoft-ad-cs-pki-template-with-certificate-sign (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,
We have a 2 tier PKI infrastructure with offline Root and Issuing CA. We use several templates to issue server authentication and client authentication certificates. 
We have new requirement from application team that they need a certificate with "Certificate Signing" Key Usage so that they can validate and issue further certificates to application users.
As per my understanding this key usage is used for Issuing CA certificates and should not be used for any other template and application. I am not able to get details about the security concerns and risks of using the template with "Certificate Signing" Key Usage.
Can you please help if there are some articles/documents highlighting the risk of using templates with "Certificate Signing" Key Usage.
Thanks

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-01-22*

I am not able to get details about the security concerns and risks of using the template with "Certificate Signing" Key Usage

TL;DR the certificate with `CertKeySign` key usage is eligible to sign other certificates. Such certificate must be treated as a CA and such certificate is extremely sensitive. This means that it requires higher level of security and audit to avoid unauthorized certificate issuance and potential PKI compromise.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-22*

Hello khwinder Singh,

Thank you for posting in Q&A forum.

We can see the Key Usage in the certificate template as below.

For detailed information about key usage, we can read link below.

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn786428(v=ws.11)  

I hope the information above is helpful. If you have any questions or concerns, please feel free to let us know. 
Best Regards,  
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.
