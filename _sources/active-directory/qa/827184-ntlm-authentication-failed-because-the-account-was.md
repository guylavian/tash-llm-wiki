---
title: "NTLM authentication failed because the account was a member of the Protected User group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/827184/ntlm-authentication-failed-because-the-account-was
question_id: 827184
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# NTLM authentication failed because the account was a member of the Protected User group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/827184/ntlm-authentication-failed-because-the-account-was (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

I'm setting up a new VPN in Azure that is connecting to a on-premise lab environment that is planned to replace the old VPN connection. While connected to the new IP range on the new VPN we are receiving this error while RDPing using elevated accounts that are part of the Protected Users group:  

NTLM authentication failed because the account was a member of the Protected User group.  

Event 100  

Error Code: 0xC000006E  

Noticed some alerts about certificates as well. NTLM and Kerberos aren't my specialty, so was looking for some help with this, is there somewhere we need to whitelist the new VPN IP range for NTLM / Kerberos to work correctly?  

RDP works fine without error on the current VPN, but not the new one we are trying to implement.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2022-04-26*

Read on here.    

https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/how-to-configure-protected-accounts    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
