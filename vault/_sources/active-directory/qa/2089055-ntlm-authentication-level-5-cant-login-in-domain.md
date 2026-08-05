---
title: "NTLM authentication level 5, cant login in domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2089055/ntlm-authentication-level-5-cant-login-in-domain
question_id: 2089055
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# NTLM authentication level 5, cant login in domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2089055/ntlm-authentication-level-5-cant-login-in-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Domain Controllers > Windows server 2019

Clients > Windows server 2019 and Windows 10 22H2

I have set this option on domain controller policy

After that I have not been able to log in again via rdp with my domain account, it was blocked on the first attempt.

I have not been able to log in either from a server member.

I had to log in with the domain administrator and change the gpo again.

Why is this happening? shouldn't I be able to log in with kerberos validation without problems?

Best regards,

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-07*

Hello RAN55,

Thank you for posting in Q&A forum.

Based on the description, you set the fifth option, it means the domain controller only accepts the NTLMv2 protocol.  

Which one did you set on Windows server 2019 and Windows 10 22H2?

On clients->Windows server 2019 and Windows 10 22H2, you should set 3 or 4 or 5 (below).

Reference:

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
