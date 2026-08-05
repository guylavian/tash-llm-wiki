---
title: "Auditing NTLMv1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181108/auditing-ntlmv1
question_id: 1181108
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Auditing NTLMv1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181108/auditing-ntlmv1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have enabled NTLM auditing to discover any use of NTLMv1.

As I understand I can look for events under Applications and Services Log\Microsoft\Windows\NTLM

I do see the following events but not sure if there is NTLMv1 traffic blocked here. From the image below it tells me that user identity is my domain controller, and domain identity is my domain name. This is eventID 8002, so not sure if that is defined like "NTLMv1 traffic blocked" ? I understand that this will be blocked if i disable NTLMv1, but from the message below, I am not sure what I am blocking.

Reference: https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-ntlm-authentication-in-this-domain?source=recommendations

When I see some other documentation, I am supposed to look for eventid 4624, which ofcourse also contains Kerberose, so I see 1000000+ of these events in the security log. Not so easy to look for NTLMv1 within this.

Reference: https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/audit-domain-controller-ntlmv1

So any comments on how to "easy" look for NTLMv1 traffic.

Thanks for any reply

/R

Andy

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-17*

Hi @Andreas

When you enable NTLM audit , you can identify NTLMv1 in the PackageName of the event 4624. You can use a Powershel script to check in the event viewer of all domain controllers:

Some links talk about how you can detect NTLMv1 authentication and disabled it:

How to Disable NTLM Authentication in Windows Domain?

 HOWTO: Detect NTLMv1 Authentication

Please don't forget to mark helpful answer as accepted
