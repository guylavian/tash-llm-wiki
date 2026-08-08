---
title: "GPO not applying Windows Defender inbound rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/982231/gpo-not-applying-windows-defender-inbound-rules
question_id: 982231
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# GPO not applying Windows Defender inbound rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/982231/gpo-not-applying-windows-defender-inbound-rules (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've created a GPO with the following settings:     

    

In addition to this, I've also enabled two inbound rules in Windows Defender as part of the same policy:    

    

For some reason, the inbound rules do not appear in the settings summary for the GPO. The GPO is linked to an OU and is Enforced. There are no other GPOs below it with conflicting settings. On workstations in the OU, we can see that the GPO does apply the Remote Registry service startup setting but does not apply the inbound rules.     

Is there anything we're missing that would cause the inbound rules to not apply? Windows Defender Firewall is enabled on the workstations and is not controlled by another AV.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-08-25*

Hi,    

Can you follow the steps that is required for Inbound rules - defender GPO - checklist-creating-inbound-firewall-rules    

I will also suggest you to check the event logs and share the event ID's for any GPO failures, try the GPO debugging and check the GPOs that are applied on the device. If any GPO is overriding or local policies are applied.?    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.    

----
