---
title: "Safely disabling TLS through GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/959917/safely-disabling-tls-through-gpo
question_id: 959917
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Safely disabling TLS through GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/959917/safely-disabling-tls-through-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,    

In our environment, Users and Computers OU contain one GPO in which user settings policies is set to allow     

    

Recent Vulnerability scans for few servers, report that these particular servers are vulnerable to TLS 1.0. TLS 1.1 and now we need to disable TLS 1.0 & 1.1 in these servers safely through GPO.    

How to apply the setting to remove the vulnerability in these servers only.    

As of now , other servers are not being reported as vulnerable even though the same existing GPO is applied to them also.    

Our quick need is to get rid of these particular servers exposed to these TLS 1.0 & 1.1 vulnerabilites    

Any help is greatly appreciated

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-28*

Hello everyone,    

Finally the goal is achieved when we linked new GPO to OU where Server resides and denied the old existing GPO for the particular server through security filtering in Users and Computers OU

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-11*

Found that the vulnerabilities are exposed due to the below setting     

    

We are planning to create a new GPO, link to Users and Computers OU with high precedence and apply only to the affected servers through security filtering in which TLS 1.0 & TLS 1.1 GPP settings are to be disabled to mitigate the vulnerabilities

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-09*

Hi,    

Thanks for your reply but the question here is already an existing GPO(User settings) is applied for these servers through which TLS1.0 & 1.1 are caught . How to resolve this vulnerabilities without disturbing other servers in the same OU through new GPO?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-09*

Hi there,     

You can use Group policy preference to disable or enable TLS 1.0 by setting this registry key mentioned on this link https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings    

This article explains the supported registry setting information for the Windows implementation of the Transport Layer Security (TLS) protocol and the Secure Sockets Layer (SSL) protocol through the Schannel Security Support Provider (SSP). The registry subkeys and entries covered in this topic help you administer and troubleshoot the Schannel SSP, specifically the TLS and SSL protocols.    

Disabling SSL 2.0, SSL 3.0, TLS 1.0 protocols in Domain Controllers https://learn.microsoft.com/en-us/answers/questions/288924/disabling-ssl-20-ssl-30-tls-10-protocols-in-domain.html    

I hope this information helps.     

-----------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-09*

Anybody please help in this regard, as this is urgent requirement to mitigate the TLS1.0 & TLS1.1
