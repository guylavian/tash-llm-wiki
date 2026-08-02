---
title: "ADFS migration + WAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/992174/adfs-migration-wap
question_id: 992174
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS migration + WAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/992174/adfs-migration-wap (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have 2 windows 2012 r2 ADFS and 2 windows 2012 r2 WAP servers    

if i introduce 2 new 2019 ADFS servers into the farm do i need to upgrade the WAP servers at the same time? can i wait 2-3 days and upgrade the WAP servers?    

will the 2012 r2 WAP servers work with the 2019 ADFS servers?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-09-12*

Yes it doesn't have have to be upgraded at the same time, but you need to minimize the time running in this mixed mode as it is not intended to run like this for long.
