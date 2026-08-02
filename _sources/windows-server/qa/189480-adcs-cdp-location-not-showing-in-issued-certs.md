---
title: "ADCS CDP location not showing in issued certs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/189480/adcs-cdp-location-not-showing-in-issued-certs
question_id: 189480
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# ADCS CDP location not showing in issued certs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/189480/adcs-cdp-location-not-showing-in-issued-certs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently checked the option to "Publish CRLs" and "Publish Delta CRLs" for a file share in our ADCS CA:    

    

But the file share isn't listed as a CDP location when I run pkiview:    

    

I reissued a certificate on a test machine and it too only shows the ldap location in the CDP list:    

    

The file share has been configured and CRLs are being published there. How do I add the file share to our CDP locations? My goal is to allow non-domain joined PCs to access the CRLs. Currently non-domain joined PCs are unable to validate AD CS certs (error message about the revocation server being offline). I assume that's because the only available CRL is through Active Directory (ldap).

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2020-12-08*

file:// URL scheme is not supported for inclusion in CDP extension in issued certificates. CryptoAPI clients will unconditionally fail on file:// URL checking. Only ldap:// and plain http:// URL schemes are supported for CRL retrieval. Any other is not supported.
