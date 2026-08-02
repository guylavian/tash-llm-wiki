---
title: "How to compare GPO in between one forest to another forest?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1608723/how-to-compare-gpo-in-between-one-forest-to-anothe
question_id: 1608723
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# How to compare GPO in between one forest to another forest?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1608723/how-to-compare-gpo-in-between-one-forest-to-anothe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I am looking for a tool or any alternative to compare the GPOs in between two forests. can you please help me on this?

Thanks!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-08*

Hello Khushi kumari，

Thank you for posting in Q&A forum.

Based on your description, you want to compare GPOs across forests, including the users and groups linked to the GPO.

Microsoft Advanced Group Policy Management (AGPM) is a set of tools that can assist in the management of GPOs, and although it is mainly used for GPO versioning and auditing within a single forest, by exporting GPOs to an XML file, you can indirectly compare GPO settings in different forests. However, this requires manual comparison of the XML file contents. You can refer to the following links: Howto Compare a GPO to another GPO : IT Assistance Center : Texas State University(txst.edu), Howto Identify Differences Between GPOs, GPO Versions, or Templates - MicrosoftDesktop Optimization Pack | Microsoft Learn.

Often, however, the tools used to compare GPOs focus primarily on the GPO's settings, policies, and configurations, and less on user and group information. In order to compare GPOs between different forests, you may need to combine a third-party tool to get the complete picture.

Thank you for your understanding. I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-05*

Refer to https://techcommunity.microsoft.com/t5/microsoft-security-baselines/new-tool-policy-analyzer/ba-p/701049 

hth

Marcin
