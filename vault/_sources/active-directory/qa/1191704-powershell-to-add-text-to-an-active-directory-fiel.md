---
title: "Powershell to add text to an active directory field for set of users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191704/powershell-to-add-text-to-an-active-directory-fiel
question_id: 1191704
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
---
# Powershell to add text to an active directory field for set of users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191704/powershell-to-add-text-to-an-active-directory-fiel (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Could someone help or point me in the right direction to do the following in PS please?

I need to put populate a field in AD with some txt which will be the same text for a group of users, it needs to add the text to all members of a particular group/

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-21*

I thought I had this worked out, these two commands work when there is one member of the group (when I was testing), but as soon as I add >1 it fails to run.

$Names = Get-AdGroupMember -identity "Staff"

Set-ADUser $Names -MobilePhone "Testing"  

Can anyone help with what I have done wrong please?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-21*

..........
