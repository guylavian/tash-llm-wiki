---
title: "Active Directory Certificate Services could not publish a Certificate for request 6 to the following location on server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197708/active-directory-certificate-services-could-not-pu
question_id: 2197708
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# Active Directory Certificate Services could not publish a Certificate for request 6 to the following location on server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197708/active-directory-certificate-services-could-not-pu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,

Encountering the following error while attempting to publish a certificate to Active Directory Domain Services (ADDS) for a computer certificate:

Active Directory Certificate Services could not publish a Certificate for request 6 to the following location on server DC.MyLabCore.lo: CN=ENT-CA03,OU=CompOU,DC=MyLabCore,DC=lo.  Insufficient access rights to perform the operation. 0x80072098 (WIN32: 8344 ERROR_DS_INSUFF_ACCESS_RIGHTS).

ldap: 0x32: LDAP_INSUFFICIENT_RIGHTS: 00002098: SecErr: DSID-031514B3, problem 4003 (INSUFF_ACCESS_RIGHTS), data 0

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-11*

Hi Daisy Zhou123  

Yes, I can confirm that the Root CA certificate is visible in the Trusted Root Certification Authorities container, and the Subordinate CA certificate is visible in the Intermediate Certification Authorities container.

Pkiview Sreenshot  

Computer OU permission for Cert Publishers.  

  

I'm still encountering the same issue, and I'm unsure of what I might be missing. Could you please provide further assistance?  

Active Directory Certificate Services could not publish a Certificate for request 4 to the following location on server PreProddc01.MyLabCore.lo: CN=CLIENT,OU=Comp,DC=MyLabCore,DC=lo.  Insufficient access rights to perform the operation. 0x80072098 (WIN32: 8344 ERROR_DS_INSUFF_ACCESS_RIGHTS).

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-08*

Hello GirishN1,  

Good day!  

If the domain-joined Enterprise Root CA is in the domain, then the domain-joined Enterprise Root CA certificate should be in the Trusted Root Certification Authorities container.  

  

If the domain-joined Enterprise SubCA is in the domain, then the domain-joined Enterprise SubCA certificate should be in the Intermediate Certification Authorities container.

  

If you have any questions or concerns, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-08*

Hi Daisy Zhou123,  

Thanks for the reply.  

I've granted Read and Write permissions to the Domain Computers group, and the ID already has "Manage CA" and "Issue and Manage Certificates" permissions. However, the issue persists. 

If I'm utilizing a domain-joined Enterprise Root CA and Enterprise SubCA, will their certificates be automatically published to the domain controller?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-06*

Hello GirishN1,  

Thank you for posting in Microsoft Community forum.  

***I cannot locate "Domain Computers" under Public Key Services.***A: I cannot see the Domain Computers and Domain Users containers, either.  

You can see Domain Computers and Domain Users groups in AD users and Computers.  

  

You can try to add Cert Publishers group has Read and Write Permissions on Domain Computers or Domain Users groups.  

Ensure the account you are using to publish certificate have "Manage CA" and "Issue and Manage Certificates" permissions.

Also, did you publish this certificate on this domain machine or on one of domain controllers? You can try to copy this certificate to one of domain controllers and publish it to AD again.

I hope the above information is helpful.   

If you have any questions or concerns, please feel free to let us know.   

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-05*

Hi,   

According to the article below, I cannot locate "Domain Computers" under Public Key Services.

To confirm that the CA has necessary permissions on the Domain Computers and Domain Users containers:

-  Click Start, point to Administrative Tools, and click Active Directory Sites and Services.

-  On the View menu, click Show Services Node.

-  Double-click Services, double-click Public Key Services, right-click Domain Computers, and click Properties.

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd299818(v=ws.10)?redirectedfrom=MSDN#confirm-permissions-on-the-domain-computers-and-domain-users-containers-in-active-directory

My Env.  

Operating System: Windows Server Core 2022 

CA Type: One Enterprise Root CA, Two Enterprise Subordinate CAs
