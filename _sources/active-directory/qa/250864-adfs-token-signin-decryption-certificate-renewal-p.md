---
title: "ADFS Token signin/decryption certificate renewal (public cert)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/250864/adfs-token-signin-decryption-certificate-renewal-p
question_id: 250864
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Token signin/decryption certificate renewal (public cert)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/250864/adfs-token-signin-decryption-certificate-renewal-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Normally token signing/decryption certificates are selfsigned.  

On a specific setup I inherited, they are using public certificates for token signing/decrypting.  

Can someone know what's the best way to renew these certificates without impacting the ADFS environment itself right away?  

It's not possible to renew them via de certificates mmc. (template not found error, which is normal of course)

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 1 · updated: 2021-02-01*

Hi @Lyncer 2013  , you will need to get the new cert from the provider and import it to ADFS as token signin/token decrypting certificate. There are some considerations that are very well documented at https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ts-td-certs-ad-fs#if-youre-not-using-self-signed-certificates.    

Make sure the relying parties have been provided with the new cert(either through metadata or using public key).

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-03*

Thanks!  

I will try that.  

One more question :  

What's the best way to request a new certificate for the token signing/decryption certificate?  

Do I just create a new CSR from the certificates snapin for each server with the same settings as the current signing/decryption certificates?
