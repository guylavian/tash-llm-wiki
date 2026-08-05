---
title: "SAML Query to Active Directory - LDAP performance Challenges"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1666126/saml-query-to-active-directory-ldap-performance-ch
question_id: 1666126
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# SAML Query to Active Directory - LDAP performance Challenges

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1666126/saml-query-to-active-directory-ldap-performance-ch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In my environment, User authentication to a critical application is happening through ADFS SAML query. In the SAML query in turn do query to AD. Now we are getting auth failure in application due to slow response from AD as mentioned by application team. 

In this situation, to do a clear idea on slowness of LDAP queries/response from AD (from ADFS - SAML ) , what approach I should take. How can I troubleshoot or investigate that it is happening for AD or not or it is happening because of application issue.

I have enabled AD performance counters and Audit Events to check efficient and ineeficient queries made to AD from ADFS(SAML). 

I found that AD is respond on LDAPS queries to ADFS and the search time for all queries lies between 700ms to 1100ms 

We are getting below events in AD Audit:

Log Name:      Directory Service

Source:        Microsoft-Windows-ActiveDirectory_DomainService

Date:          5/14/2024 11:25:27 AM

Event ID:      1644

Task Category: Field Engineering

Level:         Information

Keywords:      Classic

User:         domain\svc_BatchjobUser

Computer:      DC120

Description:

Internal event: A client issued a search operation with the following options. 

Client:

10.102.12.170:33654 

Starting node:

DC=fq,DC=fq

Filter:

 (member<==>CN=svc_jnkns,OU=Funktions Konton,OU=Users,OU=PHA,DC=fq,DC=fq,DC=fq)  

Search scope:

subtree 

Attribute selection:

cn 

Server controls:

 Visited entries:

209369 

Returned entries:

1 

Used indexes:

DNT_index:94168:N; 

Pages referenced:

1487926 

Pages read from disk:

0 

Pages preread from disk:

0 

Clean pages modified:

0 

Dirty pages modified:

0 

Search time (ms):

1641 

Attributes Preventing Optimization:

member  

User:

CN=svc_BatchjobUser,OU=Service Accounts,OU=Special-accounts,DC=dc1,DC=fq,DC=fq

can anyone please guide me how should I proceed further to check the details..

## Answers

_No answers on this thread._
