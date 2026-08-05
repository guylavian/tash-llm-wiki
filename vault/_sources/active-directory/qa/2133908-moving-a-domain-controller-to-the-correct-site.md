---
title: "Moving a Domain Controller to the Correct Site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2133908/moving-a-domain-controller-to-the-correct-site
question_id: 2133908
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Moving a Domain Controller to the Correct Site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2133908/moving-a-domain-controller-to-the-correct-site (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

A domain controller was mistakenly promoted to the wrong Active Directory site. How can we move the domain controller to the correct site while ensuring minimal impact on the environment?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-12-22*

Hi @Anant Bera  

You should check if each subnet created in Sites and Service active directory are assigned to the closest site.

Check if all subnets assigned to new site have all required network ports opened with this domain controller.

Check also if the new site has a site link in order to replicate with another domain controller.

Please don't forget to accept helpful answer
