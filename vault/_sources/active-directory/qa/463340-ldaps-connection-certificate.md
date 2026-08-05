---
title: "LDAPS connection certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/463340/ldaps-connection-certificate
question_id: 463340
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# LDAPS connection certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/463340/ldaps-connection-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we have a application which failing to connect to domain controller using LDAPS (636) because it lacks required certificate hence ssl handshake fails.  

i would like to know which certificate i will have to export from DC (is it domain controller certificate OR kerberos certificate) and place it in applications certificate store so connection can be made.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-06*

Hi,  

Based on my understanding, it is a cert on the LDAPS server (Domain Controller) for server authentication issued by the trusted CA server.  

When request cert for server authentication we can use the Kerberos template.  Or we can create your own or use one of the existing templates that has Server Authentication as a purpose, such as Domain Controller Authentication, Domain Controller, Web Server, and Computer.   

Important: You should be planning to have only one certificate on each LDAP server (i.e. domain controller or AD LDS computer) with the purpose of Server Authentication.  

For more details, you can refer to the following link:  

https://social.technet.microsoft.com/wiki/contents/articles/2980.ldap-over-ssl-ldaps-certificate.aspx  

If i misunderstand you, feel free to let me know.  

Best Regards,
