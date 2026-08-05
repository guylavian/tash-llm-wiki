---
title: "ADCS | Migrate CSP to KSP issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2236343/adcs-migrate-csp-to-ksp-issue
question_id: 2236343
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ADCS | Migrate CSP to KSP issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2236343/adcs-migrate-csp-to-ksp-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi 

We have a W2K19 server running AD Certificate Authority still on CSP (due to OS upgrade of old VM) 

The root cert has been renewed without renewing the key for years!!!!!

I need to make this CA KSP so I can issue a root cert as SHA-256.

When following guides like https://www.petenetlive.com/KB/Article/0001243 I get an error on backup CA: windows cannot backup one or more private keys because the csp does not support key export 

I have found a solution about dashes on a key reg but this did not work.

I get the cert backed up but no key icon on it. 

This makes me very nervous about continuing with the migration.

Is there a way out of this? 

Alternatively can I issue a new root cert with a new key? 

Will this key invalidate the current key (that has been renewed for years)? And can I have both certs on at the same time? 

Thanks, M

## Answer (community) — community member

*upvotes: 0 · updated: 2025-03-19*

@Anonymous  ,This is the error I get when doing the CA backup:

The backup only contains the certificate only (there is no key icon) and I cannot import that same certificate and export the key after.

As such I think I wont be able to perform the migration to KSP as the key is required.

This is the export wizard, I don't have the export option:

Thanks, M

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-19*

Hello SenhorDolas,  

Thank you for posting in Q&A forum.

Based on the description, as I understand, you have one-tier PKI, do you mean you cannot back up CA when you run Certification Authority Backup Wizard?

If so, you can try to check whether you can export CA root certificate with its private key(below).

Open Certilm.msc and find the root CA certificate, right click this root CA certificate and select All Tasks\Export.

Here is a similar thread with the shared steps, you can try if it is helpful to you.

migration csp to ksp

https://learn.microsoft.com/en-us/answers/questions/305322/migration-csp-to-ksp

References

Step-By-Step: Migrating The Active Directory Certificate Service From Windows Server 2008 R2 to 2019

https://techcommunity.microsoft.com/blog/itopstalkblog/step-by-step-migrating-the-active-directory-certificate-service-from-windows-ser/697674

How to move a certification authority to another server

https://learn.microsoft.com/en-us/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/move-certification-authority-to-another-server

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.
