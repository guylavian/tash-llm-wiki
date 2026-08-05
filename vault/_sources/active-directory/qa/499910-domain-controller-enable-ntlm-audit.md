---
title: "Domain Controller enable NTLM Audit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/499910/domain-controller-enable-ntlm-audit
question_id: 499910
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Domain Controller enable NTLM Audit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/499910/domain-controller-enable-ntlm-audit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,   

May i know which gpo policy will need to configure to check NTLM auditing on domain controllers?   

What will be the eventid to check?

## Answer (community) — Volunteer Moderator

*upvotes: 2 · updated: 2021-08-03*

You have to navigate to     

Computer Configuration\Windows Settings\Security Settings\Local Policies\Security Options    

And configure Network Security: Restrict NTLM: Audit NTLM authentication in this domain    

Log files will be on operational event log under Applications and Services Log\Microsoft\Windows\NTLM in the Event Viewer.    

Take a look at:    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-audit-ntlm-authentication-in-this-domain

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-05*

@Reza-Ameri  ,     

Does this mean that only NTLM authentication that are denied will be logged?    

Our objective here is to audit successful NTLM connections so that we can inform the service owner to change the authentication to Kerberos.    

Please advise whether there is a setting to audit successful authentication.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-08-04*

Also, you can check Event id - 4624 while authentication.   

NTLM in the Authentication Package value, than the NTLM protocol has been used to authenticate this user  

Package Name will show which protocol LM, NTLMv1 or NTLMv2 has been used for authentication
