---
title: "Deploying Multiple ADCS Root CAs in the Same Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2237648/deploying-multiple-adcs-root-cas-in-the-same-domai
question_id: 2237648
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Deploying Multiple ADCS Root CAs in the Same Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2237648/deploying-multiple-adcs-root-cas-in-the-same-domai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone and the master of PKI: @Vadims Podāns :) 

A challenge has arisen regarding Active Directory Certificate Services (ADCS) while transitioning from SHA1 CSP to SHA256 KSP on a Windows Server 2019 Root CA with no subordinate CA. 

The current setup prevents backing up the private key due to the error: "windows cannot backup one or more private keys because the csp does not support key export." 

Several attempted solutions but I still can't see the private key using  certutil  -dump : "Cannot find the certificate and private key for decryption" on .p12 backup cert. 

A plan to deploy a new Offline Root CA and an Online Subordinate CA is required. 

Questions:

-  Regarding the issuance of Domain Controller Template certificates: 

-  How will the process function with two Root CAs? 

-  Is there a need to create an additional DC Template on the Subordinate CA or are these stored in AD?

-  What is the mechanism for the DCs to request the certificate?

-  Is it feasible for the DCs to possess certificates from both Root CAs?

For client machines receiving the Root CA certificate in the Trusted Root Certification Store: 

-  What steps are necessary to publish the new certificate from the Subordinate CA, and how will clients retrieve it? In the current setup the Root CA certificate are installed when a machine is on the domain (not through Group Policy Objects (GPO).

The strategy is to maintain both Root CA certificates until all DCs and clients have been updated with the new Root certificate, followed by the removal of the old certificate.

I am basing my plan on @Vadims Podāns reply here: https://learn.microsoft.com/en-us/answers/questions/704920/impact-of-two-online-ad-root-cas

Any assistance would be highly appreciated.  

Thanks, M

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-24*

Hello SenhorDolas,

Thank you for posting in Q&A forum.

For the question "The current setup prevents backing up the private key due to the error: "windows cannot backup one or more private keys because the csp does not support key export."", if you

do not you have recent CA backup or any old CA backup (including a backup of the private key) before it became non-exportable, it seems you cannot migrate AD CS to new server.

Here are the answers for your references.

1.Regarding the issuance of Domain Controller Template certificates:

A1: Please tell us the specific question about Domain Controller Template certificates.

2.How will the process function with two Root CAs? 

A2: For requesting certificates manually, you can select which CA server.

For more information, please read links below.

https://learn.microsoft.com/en-us/archive/technet-wiki/14106.ad-ds-site-awareness-for-ad-cs-and-pki-clients

https://learn.microsoft.com/en-us/answers/questions/298788/how-clients-get-a-certificate-if-there-are-multipl

https://learn.microsoft.com/en-us/answers/questions/704920/impact-of-two-online-ad-root-cas

3.Is there a need to create an additional DC Template on the Subordinate CA or are these stored in AD? What is the mechanism for the DCs to request the certificate?

A3: No, you do not need to create an additional DC Template on the Subordinate CA. You can see three certificate templates about Domain Controller (Domain Controller, Domain Controller Authentication, Kerberos Authentication) when you open Certificate Template console (stored in AD DC). In my experience, DC will auto enroll certificate if DCs need Domain Controller certificates.

4.Is it feasible for the DCs to possess certificates from both Root CAs? 

A4: I think it is feasible. However, in many cases it is simpler to keep a single, well-managed PKI hierarchy where DCs obtain their certificates from a single enterprise CA. You had better make DC request CD certificate from one CA server, because the DCs to possess certificates from both Root CAs may have Certificate Enrollment and Management, Trust and Validation, Operational Complexity.

5.For client machines receiving the Root CA certificate in the Trusted Root Certification Store: 

What steps are necessary to publish the new certificate from the Subordinate CA, and how will clients retrieve it? In the current setup the Root CA certificate are installed when a machine is on the domain (not through Group Policy Objects (GPO).

A5: Your two-tier PKI is one offline Standalone root CA and one online Enterprise issuing CA.

Offline Standalone root CA server is not in the domain.

Online Enterprise issuing CA server is in the domain.

Online Enterprise issuing CA certificate will publish to Intermediate Certification Authorities Store on domain machines.

Because the root CA is Offline Standalone root CA, you should run the command below on one DC to publish root CA cert to the domain. Then it will/ should dispatch this root cert to all domain joined clients root store (Trusted Root Certification Authorities Store).

certutil -f -dspublish <the full path of CA certificate> RootCA

For more information, please refer to link below.

AD CS Step by Step Guide: Two Tier PKI Hierarchy Deployment https://social.technet.microsoft.com/wiki/contents/articles/15037.ad-cs-step-by-step-guide-two-tier-pki-hierarchy-deployment.aspx

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.
