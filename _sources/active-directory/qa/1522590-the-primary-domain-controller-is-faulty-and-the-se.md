---
title: "The primary domain controller is faulty, and the secondary domain controller cannot immediately replace the primary domain controller?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1522590/the-primary-domain-controller-is-faulty-and-the-se
question_id: 1522590
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# The primary domain controller is faulty, and the secondary domain controller cannot immediately replace the primary domain controller?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1522590/the-primary-domain-controller-is-faulty-and-the-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone, I would like to ask you, the primary domain controller is bad, why can't the secondary domain controller replace it immediately?
Our company uses windows 2016 server to do the primary and secondary domain control, and there is synchronization. A God domain controller suddenly crashes, but the secondary domain controller can not top, how to do so that the secondary domain controller can immediately top?
At present, if you want to use the secondary domain controller, you can only switch over when the primary domain controller is normal, but no one will know in advance when the primary domain controller is bad.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-02*

Hi @yz•

If the primary DC is crashed and you are unable to restore it , in this case you should launch metadata cleanup to remove from Active Directory and it hosts fsmo roles you have to seize them to move them to secondary DC.

https://blog.netwrix.com/2023/12/08/seize-fsmo-roles/

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup

if member machines are using the primary DC as dns resolver you have to switch to secondary DC.

Please don’t forget to accept helpful answer
