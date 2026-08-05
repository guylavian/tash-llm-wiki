---
title: "How can I download Resiliency reviews and its recommendations from review as CSV file?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2125218/how-can-i-download-resiliency-reviews-and-its-reco
question_id: 2125218
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["azure-advisor", "microsoft-security-ms-graph", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# How can I download Resiliency reviews and its recommendations from review as CSV file?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2125218/how-can-i-download-resiliency-reviews-and-its-reco (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Resiliency reviews with lot of recommendations. I need to download them as CSV using PowerShell or cli.   

I'm using below Query but couldn't be able to expand the recommendations. How can I do it?

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 1 · updated: 2024-12-11*

Hello Ramakrishna,

Give this query a try: 

`advisorresources`

`| mv-expand workloadName = properties.resourceWorkload.name`

`| where workloadName == '<Review name>'`

Where <Review Name> would be the review name that you see in the Reviews (Preview) for the specific review you are wanting to export.
