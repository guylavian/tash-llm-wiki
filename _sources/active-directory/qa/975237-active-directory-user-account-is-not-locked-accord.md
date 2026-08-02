---
title: "Active Directory user account is not locked according to bad password attempt event logs."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/975237/active-directory-user-account-is-not-locked-accord
question_id: 975237
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active Directory user account is not locked according to bad password attempt event logs.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/975237/active-directory-user-account-is-not-locked-accord (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we are getting 4771 event log in security log for Bad password attempt but user did not lock. According to our password policy user should lock 3 invalid password within 5 mins. but we have checked event log we found bad password attempt. if we checked manually by bad password, user lockout policy is working. user is locked after 3 times bad password attempt. but we are getting huge bad password attempt in event log but user did not lock. screen shot is given below- ![233205-image.png][1] [1]: /api/attachments/233205-image.png?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-22*

Hello,     

The failure code 0x18 references to the bad password attempt & there can be many reasons like attack bcoz of worm/viruses, password attack. You need to verify, from where the attempt is coming from using netmon or wireshark tool. There is no easy way to find out the reason for invalid (0x18)password attempt coming from w/o analyzing the traffic.    

Reference for more details: https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4771    

-----------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-21*

Hi,    

Do all the events shown in the screenshot relate to the same user?    

A bit of background on the account lock out process. Each domain controller keeps its own count of the number of failed logon attempts per user, so if a user authenticates against a different DCs, they could exceed the maximum failed attempts defined in the password policy, to ensure that the password policy is enforced the follow mechanism is used.     

When a domain user provides a bad password, the authenticating domain controller will increment it's own copy of the bad password count for that user, if this exceeds the policy the DC will lock the account. If not, it will then send the authentication request to the PDC to confirm the password, in case the password has recently been changed. This means that the PDC will see all failed authentication attempts.     

If the bad password count for a user, on any DC exceed the policy then the account locked, and AD replicates this to the other DCs in the domain. In a multi-DC domain, the PDC is usually the DC that locks a user's account.      

You can use the post below to check the number of bad passwords (bad pwd column) that have been received on each domain controller and if the PDC bad password count is also incrementing with each failed logon, in case the failed logons are not being sent to the PDC or the locked status is not being replicated to the other DCs.    

https://nettools.net/troubleshoot-account-lockouts/    

Gary.
