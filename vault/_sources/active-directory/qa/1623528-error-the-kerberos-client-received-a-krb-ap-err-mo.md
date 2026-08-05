---
title: "Error The Kerberos client received a KRB_AP_ERR_MODIFIED"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1623528/error-the-kerberos-client-received-a-krb-ap-err-mo
question_id: 1623528
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Error The Kerberos client received a KRB_AP_ERR_MODIFIED

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1623528/error-the-kerberos-client-received-a-krb-ap-err-mo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm getting an error on several machines, 

The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server nb-16$. The target name used was HOST/WS-11.COP.NET. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (COP.NET) is different from the client domain (COP.NET), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-20*

I did the procedure as requested as shown below I did it both on the server and on the NB-16 machine
