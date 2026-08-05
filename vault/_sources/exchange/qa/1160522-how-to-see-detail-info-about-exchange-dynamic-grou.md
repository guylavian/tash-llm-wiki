---
title: "How to see detail info about Exchange Dynamic Groups Members"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1160522/how-to-see-detail-info-about-exchange-dynamic-grou
question_id: 1160522
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to see detail info about Exchange Dynamic Groups Members

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1160522/how-to-see-detail-info-about-exchange-dynamic-grou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I need help to view the members of a dynamic distribution group in Exchange Online using the Get-DynamicDistributionGroupMember Exchange PowerShell cmdlet.

I need to see more info than just the Name and the RecipientType as I'm getting the Object ID in some results instead of readable names when running it as Get-DynamicDistributionGroupMember -Identity <group name>!!!!!

It would be more helpful to see also the email for example.

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-01-13*

The cmdlet returns the full "ReducedRecipient" object, so you get a lot more properties than just Name and RecipientType, you simply need to "instruct" PowerShell to display them. Here's an example:

`Get-DynamicDistributionGroupMember DDG | select Name,DisplayName,PrimarySmtpAddress,RecipientTypeDetails`

To get the full set of properties returned, use the Get-Member cmdlet:

`Get-DynamicDistributionGroupMember DDG -ResultSize 1 | gm`
