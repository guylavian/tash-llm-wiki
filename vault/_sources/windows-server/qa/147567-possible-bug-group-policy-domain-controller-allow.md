---
title: "Possible Bug - Group Policy: Domain controller: Allow vulnerable Netlogon secure channel connections"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/147567/possible-bug-group-policy-domain-controller-allow
question_id: 147567
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Possible Bug - Group Policy: Domain controller: Allow vulnerable Netlogon secure channel connections

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/147567/possible-bug-group-policy-domain-controller-allow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

POSSIBLE BUG:  On Server 2012 R2, When the Policy "Domain controller: Allow vulnerable Netlogon secure channel connections"* is set to NOT DEFINED, this registry key STILL contains old PREVIOUSLY set entries (security descriptors) in the list!   

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters]  

"vulnerablechannelallowlist"  

Details:  When you enable the policy "Domain controller: Allow vulnerable Netlogon secure channel connections" and add a user account or security group and then later disable the policy by setting it to Not Defined, the associated registry key is NOT cleared.  

*Reference:  How to manage the changes in Netlogon secure channel connections associated with CVE-2020-1472  

See Section Section 3b  

https://support.microsoft.com/en-us/help/4557222/how-to-manage-the-changes-in-netlogon-secure-channel-connections-assoc

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-12*

Update:  The bug has been fixed.
