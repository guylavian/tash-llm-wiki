---
title: "How to compare multiple gpos XML file in loop?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1612298/how-to-compare-multiple-gpos-xml-file-in-loop
question_id: 1612298
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to compare multiple gpos XML file in loop?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1612298/how-to-compare-multiple-gpos-xml-file-in-loop (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have exported all gpo's report in the form of XML in source domain and as well as in Target domain. The GPO name is same in both the domain. I have to compare all the GPOs in loop. Like in source DC gpo name is IND- server -Gpo then it compare with similar name of GPO in Target domain.Is there any automated way to compare it, like any tool? Can you please help me on this?

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-09*

Hey there Khushi kumari

Guess you can use PowerShell scripting to automate the process

Start by writing a PowerShell script that loops through all the XML files containing the exported GPOs from both the source and target domains. Within this loop, parse the XML data to extract relevant information about each GPO, such as its name, settings, and configurations.

Next, implement logic to compare the GPOs between the source and target domains based on their names and settings. 

Consider utilizing PowerShell modules like GroupPolicyDsc, which provide cmdlets for working with GPOs, to streamline the comparison process.

If this helps kindly accept the answer thanks much
