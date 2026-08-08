---
title: "KDC certificate for the domain controller - Windows Event Log"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1693073/kdc-certificate-for-the-domain-controller-windows
question_id: 1693073
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# KDC certificate for the domain controller - Windows Event Log

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1693073/kdc-certificate-for-the-domain-controller-windows (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are seeing this event log entry in some of our Windows clients.

After investigating, the SAN field of the certificate currently installed is confirmed to have not included the domain name..  domain.local in this example.

When we built our Root Certificate Authority, we cloned an existing template named "Domain Controller Authentication" for the purpose of issuing Domain Controller certificates.

After some research, it seems like the template "Kerberos Authentication" should have been used instead.  Anyone familiar with this caveat and aware of what is best practice in this case?

https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/deploy/on-premises-cert-trust#supersede-existing-domain-controller-certificates

Regards  

Adam Tyler

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-10*

Hello AdamTyler-3590,  

Thank you for posting in Q&A forum.

I think you are right. As the description in event ID 20 you mentioned and the description in screenshot or below. 

By default, the Active Directory CA provides and publishes the Kerberos Authentication certificate template. The cryptography configuration included in the template is based on older and less performant cryptography APIs. To ensure domain controllers request the proper certificate with the best available cryptography, use the Kerberos Authentication certificate template as a baseline to create an updated domain controller certificate template.

The Kerberos Authentication certificate template is the most current certificate template designated for domain controllers and should be the one you deploy to all your domain controllers.

Also, I have done a test in my lab.  

This certificate is issued using Domain Controller Authentication certificate template.  

This certificate is issued using Kerberos Authentication certificate template.   

Here are three DNS names in the SAN field of the certificate  

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
