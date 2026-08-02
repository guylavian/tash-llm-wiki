---
title: "ntlm auditing gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/498947/ntlm-auditing-gpo
question_id: 498947
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# ntlm auditing gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/498947/ntlm-auditing-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Just seeking some guidance on NTLM auditing. We are running Server 2019 at the latest domain and forest functional levels    

I am just seeking some clarity around auditing NTLM traffic by GPO.    

Which settings should be applied to the Domain Controllers only?    

And which should only be applied to member servers and workstations?    

I've come across a few articles which are confusing me.    

This one says put the settings in the default domain policy:    

https://knowledge.broadcom.com/external/article?legacyId=HOWTO79508    

This article says the following:    

https://learn.microsoft.com/en-us/archive/blogs/askds/ntlm-blocking-and-you-application-analysis-and-auditing-methodologies-in-windows-7    

 Network security: Restrict NTLM: Outgoing NTLM traffic to remote servers = Audit All    

 Network security: Restrict NTLM: Audit NTLM authentication in this domain = Enable all    

 Network security: Restrict NTLM: Audit Incoming NTLM Traffic = Enable auditing for all accounts    

```
Note: Configure "Audit NTLM authentication in this domain" on DC's only. Configure "Outgoing NTLM traffic to remote servers" and "Audit Incoming NTLM Traffic" on all computers.
```

And this one just mentions applying specific auditing to DCs only:    

https://adsecurity.org/?p=3377    

I guess i am just seeking some clarification.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2021-08-03*

The article from Microsoft is reliable since it is official.    

However, you reference to the older article and new one is this one:    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-audit-ntlm-authentication-in-this-domain     

It depends on your architecture you may do it in your main domain (especially those who required authentication).
