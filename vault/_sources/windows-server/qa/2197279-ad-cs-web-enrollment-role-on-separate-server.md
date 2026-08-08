---
title: "AD CS Web Enrollment role on separate server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197279/ad-cs-web-enrollment-role-on-separate-server
question_id: 2197279
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# AD CS Web Enrollment role on separate server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197279/ad-cs-web-enrollment-role-on-separate-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have set up two tier PKI infrastructure. Offline root CA is on Level 1 and Issuing Enterprise CA are on level 2. On issuing CA is only CA role.

I installed web enrollment role on separate server called CA-WE. When I try to request certificate using http:\CA-WE\certsrv with CSR i get error message like on image.  

There is also event ID 22 on CA issuing server stating: AD CS could not process bad tag value met. 0x8009310b (ASN: 267 CRYPT_E_ASN1_BADTAG). Error parsing reequest.  

Can anyone offer any clue what to do ?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-26*

Hello JoeFly_55,  

Thank you for your update and sharing.  

I am so glad that the problem has been resolved.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-23*

I have found the solution. Web enrollment computer object needs to have delegation rights as described here:

https://www.keyfactor.com/blog/ad-cs-web-enrollment-delegation/

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-22*

Hello JoeFly_55,  

Thank you for posting in Microsoft Community forum.  

please check if you can enroll a certificate via MMC (such as open certlm.msc console or cerlmgr.msc console) on the same machine using the same certificate template as web enrollment.

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
