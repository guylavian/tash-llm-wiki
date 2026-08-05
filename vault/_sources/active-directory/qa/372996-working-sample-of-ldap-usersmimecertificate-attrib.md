---
title: "Working sample of LDAP userSMIMECertificate attribute"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/372996/working-sample-of-ldap-usersmimecertificate-attrib
question_id: 372996
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Working sample of LDAP userSMIMECertificate attribute

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/372996/working-sample-of-ldap-usersmimecertificate-attrib (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What exactly is the contents of the LDAP userSMIMECertificate attribute? p7s? p7m?  Binary "/30/82/..." or text "Content-Disposition: attachment; filename="smime.p7s""?  I have a setup that works with userCertificate x509 der cert (sending encrypted email in outlook).  But every flavor of pkcs7 encoding for userSMIMECertificate fails.  An exact sample of a working AD attribute editor entry would be very helpful.  Thank You.  

[1]  My non working example]: https://www.co.tt/adattribeditor.jpg  

[2]  Details: https://www.co.tt/userSMIMECertificate.html

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-28*

Hello @a b  ,    

The PKCS #7 Signed Data format (as used in your https://www.co.tt/files/******@dc.org.pkcs7.der download) is, broadly speaking, the correct format for the LDAP userSMIMECertificate atribute.    

Just by looking at what you have written, only one thing suggested to me something that could/should be tested: the use of the sMIMECapabilities attribute. In your example, this is a signed attribute of the PKCS #7 signed data object; however, I have previously mostly seen sMIMECapabilities as a certificate extension of the end-user certificate.    

Gary
