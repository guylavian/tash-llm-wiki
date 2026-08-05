---
title: "Delegation of GPO management in external trusted domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/345113/delegation-of-gpo-management-in-external-trusted-d
question_id: 345113
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Delegation of GPO management in external trusted domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/345113/delegation-of-gpo-management-in-external-trusted-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The delegation of GPO management in an externally trusted domain was impacted by the introduction of the UNC hardening documented here (three sources provided):  

https://support.microsoft.com/en-us/topic/ms15-011-vulnerability-in-group-policy-could-allow-remote-code-execution-february-10-2015-91b4bda2-945d-455b-ebbb-01d1ec191328  

https://msrc-blog.microsoft.com/2015/02/10/ms15-011-ms15-014-hardening-group-policy/?WT.mc_id=ITOPSTALK-blog-abartolo  

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/guidance-on-deployment-of-ms15-011-and-ms15-014/ba-p/257759  

Please consider the following scenario:  

-  An organization manages two domains in a two-way external trust relationship [domain A and domain B]  

-  The org has no plans to convert the relationship to a forest trust  

-  The org requires IT admins with privileged accounts in domain A to fully manage GPOs (create/delete/modify/link) in domain B  

-  The admins in domain A use Windows 10 workstations (UNC hardening enabled by default for Netlogon and SYSVOL)  

-  GPMC frequently returns "Network Access is Denied" when trying to manage GPOs in domain B, from domain A  

In order to successfully implement this particular delegation scenario, it seems that the admin workstations in domain A need to run with a NetworkProvider policy of RequireMutualAuthentication=0.  This would allow usage of NTLM to succeed when GPMC (on a Windows 10 workstation in domain A) connects to SYSVOL in domain B.  The policy appears to be a weaker security posture for those workstations.  

What is the best configuration of UNC hardening to use in this scenario such that all other UNC paths accessed by the admin workstations run with the default security parameters?  

Are there any other suggestions for implementing the desired delegation scenario which do not weaken the security of an admin workstation?  

Thanks,  

DaveC

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-09*

@Anonymous     Thank you for the research and your reply.  As best I can determine the external trust in this environment meets those requirements, but my tests over both SMB and LDAP always negotiate NTLM.    

This is not critical and we are reviewing a conversion to forest trust.  I'll point out that it's a bit odd/frustrating to try and implement a more secure privilege delegation model, but be hampered by a different security-related feature  :)    

-DaveC
