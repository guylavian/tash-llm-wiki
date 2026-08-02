---
title: "Kerberos authentication vs NTLM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1430582/kerberos-authentication-vs-ntlm
question_id: 1430582
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Kerberos authentication vs NTLM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1430582/kerberos-authentication-vs-ntlm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Sometimes, the web site user write "Pass the Hash does not work for Kerberos authentication on Active Directory".

However, in Kerberos authentication, pre-authentication data is sent from the domain controller in ERR-PREAUTH-REQUIRED, and the pre-authentication data is encrypted with a password hash on the client in AS_REQ, and the domain controller also check the data with a password hash.

Considering this, I think that encrypting data from the server using password hash and verifying it on the server is no different from NTLM authentication.

Although there are sites that mention that Pass the Hash cannot be used with Kerberos authentication, I could not find a site that specifically explains why.

If anyone knows the reason for this, please let me know.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-19*

Thanks for posting your question in the Microsoft Q&A forum.

I hope this article can help you:

https://www.csoonline.com/article/548804/don-t-count-on-kerberos-to-thwart-pass-the-hash-attacks.html
