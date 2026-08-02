---
title: "ADCS CA uses NTLM to authenticate clients during certificate requests"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/934546/adcs-ca-uses-ntlm-to-authenticate-clients-during-c
question_id: 934546
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# ADCS CA uses NTLM to authenticate clients during certificate requests

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/934546/adcs-ca-uses-ntlm-to-authenticate-clients-during-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have recently set up a new ADCS certificate authority and at the moment our clients are not able to request certificates. In troubleshooting, we have found that when the CA receives the certificate request, it attempts to contact a domain controller using NTLM authentication (presumably to validate the requestor credentials?). This fails because we have outbound NTLM disabled on the CA:    

    

My question is, why is the CA using NTLM authentication to contact the domain controller and can we configure it to use stronger authentication?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-04*

We have NTLM outbound blocked on our Server 2022 CA and it is able to issue certificates.  

Make sure your DC certificates are not using the default template. You must create a new template by duplicating the "Kerberos Authentication" template using that for issuing certificates to your DC's. Then your CA should be able to authenticate via Kerberos.  Also don't set your CRL to be distributed via LDAP. Set it to HTTP only.  I believe that may be what is contributing to your CA attempting to contact via LDAP. It shouldn't and should be contacting the DC over RPC/DCOM with Kerberos authentication.  Also Don't have "Enable RPC Endpoint Mapper Client Authentication" enabled as that forces RPC to use NTLM only.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-21*

Hi there,    

Firstly, check if the CRLs are up-to-date on the root CA server.    

-  Logon to the root CA with the domain Administrator.    

-  Open Certification Authority.    

-  Click Revoked Certificates\All Tasks\Publish\New CRL\OK.    

-  Refresh PKIview.msc console.    

Second, check if CRLs or AIAs are configured correctly on the root CA server.    

-  Logon to the root CA with the domain Administrator.    

-  Open Certification Authority.    

-  Check the AIA and CDP on the Extensions tab of root CA Properties based on my example below.    

AD CS - Unable to Request Certificates from Certificate Authority     

https://social.technet.microsoft.com/Forums/en-US/52fe9da9-3f93-49d0-8cf7-481e9c62f1ce/ad-cs-unable-to-request-certificates-from-certificate-authority?forum=winserversecurity    

---------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–
