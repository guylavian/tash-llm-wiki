---
title: "Windows Domain Controller - SSL Cert with Two Hosts In Subj. Alternative Name (SAN)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/477538/windows-domain-controller-ssl-cert-with-two-hosts
question_id: 477538
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows Domain Controller - SSL Cert with Two Hosts In Subj. Alternative Name (SAN)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/477538/windows-domain-controller-ssl-cert-with-two-hosts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My Domain Controllers auto enroll and get a Computerv2 cert that handles server authentication. One of the apps we use requires an SSL cert with a SAN that contains multiple hosts. I know how to create a certificate request that contains multiple hosts in the SAN. I have a couple of questions.

-    Can I just delete the auto enrolled Computerv2 certificate and import the private key for the multi SAN certificate to both Domain Controllers in the SAN

-    Could this break anything ADDS related? I think ADDS replication encrypts with Kerberos so I should be ok there.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-16*

Hello @Nicholas Talbot  ,    

Thank you for posting here.    

Here are the answers for your references.    

Q1: Can I just delete the auto enrolled Computerv2 certificate and import the private key for the multi SAN certificate to both Domain Controllers in the SAN    

A1: I am sorry I do not quite understand the description "import the private key for the multi SAN certificate to both Domain Controllers in the SAN", did you mean you want to request Domain Controller certificate for both DCs, and the SANs for both certificates are DC1.domain.com and DC2.domain.com (I assume you both DCs are DC1 and DC2)?    

If so, I think it should be OK, then you can try to request such certificate on your DCs （you had better test it in your lab first if possible）and check if it helps.    

For DC1 certificate, the first SAN is DC1.domain.com and the second SAN is DC2.domain.com.    

For DC2 certificate, the first SAN is DC2.domain.com and the second SAN is DC1.domain.com.    

For more information about how to use the Subject Alternative Name Field in Your SSL Certificate, please refer to link below.    

Subject Alternative Names: Compatibility    

https://www.digicert.com/faq/subject-alternative-name-compatibility.htm    

Q2: Could this break anything ADDS related? I think ADDS replication encrypts with Kerberos so I should be ok there.    

A2：Domain Controller certificate authentication and Kerberos authentication should be different authentication.     

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.    

Hope the information above is helpful to you.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
