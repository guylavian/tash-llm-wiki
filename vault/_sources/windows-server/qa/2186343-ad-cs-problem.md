---
title: "AD CS Problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186343/ad-cs-problem
question_id: 2186343
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# AD CS Problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186343/ad-cs-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Microsoft AD CS on-prem Two-Tier CA deployed.  

On the issuing CA servers, I'm having an issue with the CDP/CRL locations. In pkiview, it constantly points to a CRL that doesn't exist (see attached image).

The path is correct, but before the .crl extension, it constantly appends this (2) in the name. The actual name of the published CRL is CA2-CA.crl.

So far, I've tried (without success):

-  Manually editing the CRL/CDP and AIA extensions in the CA console.

-  Reissuing the issuing CA certificate.

-  Editing the registry containing these records.

I no longer know how to make it point to CA2-CA.crl instead of CA2-CA(2).crl. If anyone has any advice, I would appreciate the help.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-10*

Hello  

Greetings!  

I'm sorry, I'm not AI. 

I've encountered this question several times in the test environment before, once I configure AIA or CDP incorrectly, even if I later correct it, the entry in PKIview.msc console will still show a red cross.  

In your case, you can try to put the file CA2-CA(2).crl in local paht (C:\Windows\System32\CertSrv\CertEnroll) and http path if you have and publish CA2-CA(2).crl to AD domain.

At last, please check if the error disappears.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-10*

Hello,

This seems like AI response. I literally said that i tried that already.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-10*

Hello JoeFly_55,

Thank you for posting in Microsoft Community forum.

Based on my knowledge and experience, you can set the CRL extension and corresponding registry again or more times correctly.

That is:  

Manually editing the CRL/CDP and AIA extensions in the CA console.

Editing the registry containing these records.  

 Then refresh the PKIview.msc console.  

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
