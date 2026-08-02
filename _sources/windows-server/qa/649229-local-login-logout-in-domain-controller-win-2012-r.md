---
title: "local login logout in domain controller win 2012 r2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/649229/local-login-logout-in-domain-controller-win-2012-r
question_id: 649229
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# local login logout in domain controller win 2012 r2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/649229/local-login-logout-in-domain-controller-win-2012-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to trace only login logout of local user in domain controller (win 2012 R2) and to avoid to trace any AD login/logout user.  

Can you suggest me how to activate this tracing in "default  Domain controllers policy" ?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-05*

Hello    

Thank you for your question and reaching out.    

Account logon events are generated on domain controllers for domain account activity and on local devices for local account activity. If both account logon and logon audit policy categories are enabled, logons that use a domain account generate a logon or logoff event on the workstation or server, and they generate an account logon event on the domain controller.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events    

---------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-03*

Simplest solution is to configure the auditing then filter the result set for the items of interest.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-02*

You can configure auditing of logon by following along here.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/basic-audit-logon-events    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
