---
title: "AD CS (Standalone version) - How to sign an externally-generated CSR as a CA?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/65344/ad-cs-standalone-version-how-to-sign-an-externally
question_id: 65344
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# AD CS (Standalone version) - How to sign an externally-generated CSR as a CA?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/65344/ad-cs-standalone-version-how-to-sign-an-externally (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I am currently facing a quite blocking issue regarding the signature of a CSR emitted by a non-Microsoft PKI (EJBCA Community in my case) with a Root CA on AD CS (standalone version).  

What we want to do is to create a Sub-CA in EJBCA.  

Our procedure is the following:  

-  Creating a CSR on EJBCA (keys generated there)  

-  Signing it using our Root CA  

-  Importing the certificate on EJBCA  

So far, we are able to sign the CSR and create a certificate.  

However, we are not able to specify the parameters we want, they are being overwritten by AD CS without any possibility of configuration.  

In particular, we want to fix the basic constraints to “SubCA” (with path length constraint of 0), in order for that CA to sign other certificates.  

Given that it is not possible to use certificate templates with the standalone version, how could we proceed to sign the CSR while taking into account the parameters that we want?  

I saw that it can be possible to submit custom requests by creating some kind of custom templates (.inf files) with certreq.exe.  However, all the cases I saw online were implying that a pair of keys were to be created in ADCS, which is not suitable for us.  

I couldn’t find any documentation on how to proceed in order to use a pre-existing CSR (that includes keys that are already generated on EJBCA).  

Could you please help me in figuring how to proceed?  

Thanks very much in advance,  

Regards,  

Arnaud

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Hi,  

Thanks for your reply  

Indeed, I couldn't find this post anymore (didn't have any link showing up on my profile page), I thought it hadn't been submitted properly.  

We'll discuss on the other thread.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-13*

Hello @Arnaud_Synetis  ，    

Thank you for posting here.    

I noticed that this post has the same content as another post you posted, URL:    

https://learn.microsoft.com/en-us/answers/questions/64571/signing-an-externally-generated-csr-with-ad-cs-sta.html    

If you can confirm that the content of the two posts are the same, then in order to ensure the efficiency of support, we will archive this post and reply and assist you in another post. Thank you for your understanding.    

If there is anything unclear, please contact us.    

Best Regards,    

Daisy Zhou
