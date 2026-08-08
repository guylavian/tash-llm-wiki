---
title: "Active Directory Certificate Services (ADCS) - Volatile requests"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/395808/active-directory-certificate-services-adcs-volatil
question_id: 395808
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Certificate Services (ADCS) - Volatile requests

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/395808/active-directory-certificate-services-adcs-volatil (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

I'm following this guide in order to try out VMWare TrueSso session certificates. One of the ADCS configurations it's recommending is enabling volatile certificate requests:  

certutil –setreg DBFlags +DBFLAGS_ENABLEVOLATILEREQUESTS  

Two questions:  

-  What exactly is the impact of this? Does it simply prevent a copy of the certificate being written to the CA database, or does it prevent any record of the cert having been issued from being written to the CA Log?  

-  If the requests are still logged somehow, if asked, how would I pull up a record of the cert having been issued?  Would I be still be able to use certutil -view ?

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-05-15*

Does it simply prevent a copy of the certificate being written to the CA database, or does it prevent any record of the cert having been issued from being written to the CA Log?

yes. This means that certificate can be issued, but not written to CA database. This leads to an impossibility to revoke or recover this certificate after issuance.

how would I pull up a record of the cert having been issued?

you can't.

Would I be still be able to use certutil -view ?

no.
