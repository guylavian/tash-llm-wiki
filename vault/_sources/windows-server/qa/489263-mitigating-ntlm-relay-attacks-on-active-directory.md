---
title: "Mitigating NTLM Relay Attacks on Active Directory Certificate Services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/489263/mitigating-ntlm-relay-attacks-on-active-directory
question_id: 489263
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Mitigating NTLM Relay Attacks on Active Directory Certificate Services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/489263/mitigating-ntlm-relay-attacks-on-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have some questions left...  

There is a section in the KB5005413 article which mentions manually editing the web.config file: After enabling EPA in the UI, the Web.config file created by CES role at 'windir\systemdata\CES_CES_Kerberos\web.config'...  

I have only installed 'Certificate Authority Web Enrollment', not the 'Certificate Enrollment Web Service'. I cannot find a web.config there.  Is web.config editing only necessary if you have installed 'Certificate Enrollment Web Service'?  

Setting the Certificate Authority Web Enrollment to only Negotiate: Kerberos, the UI warns about 'Enable Kernel-mode authentication' in Extended Protection.  

The MS screenshot in KB5005413 (Certificate Authority Web Enrollment) shows that MS has checked the box for 'Enable Kernel-mode authentication' selecting 'Required' under Extended Protection.  

What is correct? To disable 'Enable Kernel-mode authentication' and set Extended Protection to 'Required' while using only 'Negotiate: Kerberos' ?  

Please help/clarify - thank you

## Answers

_No answers on this thread._
