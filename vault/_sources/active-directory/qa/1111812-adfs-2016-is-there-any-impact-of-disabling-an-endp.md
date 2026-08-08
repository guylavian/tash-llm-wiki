---
title: "ADFS 2016 - Is there any impact of disabling an endpoint"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1111812/adfs-2016-is-there-any-impact-of-disabling-an-endp
question_id: 1111812
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-online", "windows-business-windows-server-devices-deployment-config-app-groups"]
---
# ADFS 2016 - Is there any impact of disabling an endpoint

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1111812/adfs-2016-is-there-any-impact-of-disabling-an-endp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
Our Security team found a possible attack targeting ADFS: multiple IPs are trying to access /adfs/services/trust/13/usernamemixed.
```

The log message from the WAF showed that the IPs were trying to detect error messages and other sensitive information in the HTTPS header.    

according to Microsoft documentation: adfs/services/trust/13/usernamemixed	IS Used for Exchange Online with Office clients older than Office 2013 May 2015 update. Later clients use the passive \adfs\ls endpoint.    

We are utilizing ADFS to integrate with internal services and we do use Azure for MFA, we don't use Exchange online.    

Is it Ok to disable /adfs/services/trust/13/usernamemixed endpoint if we are not using Exchange online, or will it impact/disrupt other services?

## Answers

_No answers on this thread._
