---
title: "How to migrate all GPO with linked OUs from one Domain to another Domain?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1512202/how-to-migrate-all-gpo-with-linked-ous-from-one-do
question_id: 1512202
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to migrate all GPO with linked OUs from one Domain to another Domain?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1512202/how-to-migrate-all-gpo-with-linked-ous-from-one-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
We want to migrate all GPO with linked OUs from one Domain to another Domain? Is there any automated way to do this?
Thanks!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-26*

Hello Khushi kumari,
Thank you for posting in Q&A forum.
When migrating Group Policy Objects (GPOs) from one domain or forest to another, you can use the migration table to do so. The migration table allows you to map a reference to a GPO set in the source GPO to a new value in the target GPO.
You can use the migration table to reference users, groups, computers, and UNC paths from the source GPO to the new values in the target GPO. You can use the Migration Table Editor to create a migration table. For more information about the migration table, please see the following links: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc739066(v=ws.10),Migrate GPO’s Between Domains – Griffon's IT Library (c-nergy.be).
I hope the information above is helpful.
If you have any question or concern, please feel free to let us know.

Best Regards,  
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.
