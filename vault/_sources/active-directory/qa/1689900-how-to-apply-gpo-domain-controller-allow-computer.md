---
title: "How to apply GPO Domain controller: Allow computer account re-use during domain join"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1689900/how-to-apply-gpo-domain-controller-allow-computer
question_id: 1689900
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to apply GPO Domain controller: Allow computer account re-use during domain join

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1689900/how-to-apply-gpo-domain-controller-allow-computer (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

I experienced an issue during domain join using SCCM OSD, if the machine exist and try to rejoin with the same name with other service account it fails with error unable to rejoin due security policy, i have searched for the issue i found that i have to enable policy on domain controllers OU 

Domain controller: Allow computer account re-use during domain join

Then add a security group that have the computers owners and the new service account that used for domain re-join

I have applied the policy but with same issue unable to join, i have verified the registry to find HKLM\System\CCS\Control\SAM – “ComputerAccountReuseAllowList” registry key is populated with the desired SDDL

but i didn't find folder CCS under the path, any ideas to resolve this issue.

Thanks,

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-04*

Hello,

 

Thank you for posting in Q&A forum.

To further check this issue, pleas kindly try below steps:

1.Please kindly check how you apply the GPO in your domain, is it pushed by GPO management or any other third-party platform like Intune?

2.After KB5020276 released for Windows update, you could encounter with such “An account with the same name exists in Active Directory. Re-using the account was blocked by security policy.” issue, for further details please kindly refer to below Microsoft Official Link:

REF:https://support.microsoft.com/en-us/topic/kb5020276-netjoin-domain-join-hardening-changes-2b65a0f3-1f4c-42ef-ac0f-1caaf421baf8

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.
