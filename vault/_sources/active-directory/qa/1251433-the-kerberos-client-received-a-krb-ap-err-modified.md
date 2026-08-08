---
title: "The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server - between Win10 clients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1251433/the-kerberos-client-received-a-krb-ap-err-modified
question_id: 1251433
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server - between Win10 clients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1251433/the-kerberos-client-received-a-krb-ap-err-modified (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,
i have several errors in the system log
Security-Kerberos, Event 4
The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server client001$. The target name used was cifs/client002.company.local. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. ...
All guidance was about servers - but there are clients - and they are different all the time. So it is not a problem of one/several clients.
Anyone has seen this before?
BR
Stephan

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-23*

Hello Stephan,
Thanks for posting your query.   

SPN are not only registered for users accounts but are also registered to machines be it server or client.  

KRB_AP_ERR_MODIFIED arises when system is unable to decrypt the ticket. This could be due to encryption type mismatch.  

Verify encryption type is set same for machine and service accounts.  

Check for msDS-SupportedEncryptionType attribute value in users and computers
