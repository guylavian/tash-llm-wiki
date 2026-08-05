---
title: "Domain Controllers on Azure - Availability Set or Availability Zones"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1399377/domain-controllers-on-azure-availability-set-or-av
question_id: 1399377
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-virtual-machines", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Domain Controllers on Azure - Availability Set or Availability Zones

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1399377/domain-controllers-on-azure-availability-set-or-av (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.

I have some questions regarding creating domain controllers in Azure using IaaS:

-  What is the recommendation if using availability set or availability zone for DC replication?

-  In a virtual machine with DC, do you create an extra disk to place ntds, sysvol or do you use the same disk as the operating system?

-  When updating DCs, is it recommended to move the fsmo before patching and rebooting?

Best regards

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-10-23*

Hi Nuno,

DC replication is a AD internal process and it is not related to the AZ or Availability Set in Azure, that is site redundancy and recovery/backup feature.

Deploying NTDS AD related should be on a separate disk as a best practice and yes FSMO roles should be moved to the other DCs in the region or other site before patching and rebooting. Check this - https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/ad-ds-design-and-planning

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
