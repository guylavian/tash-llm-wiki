---
title: "If I want to keep part of a parent OU's GPO but add child OU's GPO with different settings, will devices in the child OU get all settings."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1615264/if-i-want-to-keep-part-of-a-parent-ous-gpo-but-add
question_id: 1615264
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# If I want to keep part of a parent OU's GPO but add child OU's GPO with different settings, will devices in the child OU get all settings.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1615264/if-i-want-to-keep-part-of-a-parent-ous-gpo-but-add (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So Parent OU's GPO has a lot of settings configured including some we don't want in child OU.  If I create new GPO link to child OU with different settings, will the resultant settings be combined on devices in the child OU (does it have any relevance if the corresponding problem settings in the child OU are set to disabled or not-configured)

Thanks Ian

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2024-03-12*

Hi @Spencer Ian  

If you have some GPO settings configured in GPO linked to parent OU and not configured in GPO linked to child OU , in this case the setting of parent GPO will be applied.

In this case, the simplest thing is to change the link of the GPO already linked to the parent OU, by linking it at the child OU (execpt child OU you mentioned it in your question)  level to be sure that it will not applied to the target child OU.

Please don't forget to accept helpful answer
