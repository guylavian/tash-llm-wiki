---
title: "The search filter is invalid (Windows Laps)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1434795/the-search-filter-is-invalid-windows-laps
question_id: 1434795
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# The search filter is invalid (Windows Laps)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1434795/the-search-filter-is-invalid-windows-laps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have enabled Windows Laps in AD but when I try to run the below command

Set-LapsADComputerSelfPermission -Identity Test

I am getting "Set-LapsADComputerSelfPermission : The search filter is invalid."

Secondly, how to enable permissions for an OU having a space in it? For Example "Desktops HO"?

Thanks.

## Answer (community) — community member

*upvotes: 3 · updated: 2023-11-23*

For me it worked to use the distinquished name of the OU for example:  

Set-LapsADComputerSelfPermission -Identity "OU=Company,DC=exoip,DC=local"  

You can find this if you right click the OU you want to use LAPS for and click on properties. There you have to go on attribute editor. The first thing there should be the distinquished name. Maybe this helps you if not I dont know another solution.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-10-03*

found that it was necessary to wrap the -Identity value in "" much like shown in the above successful examples - my early failed attempts lacked only that

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-23*

The problem was resolved after I applied the Group Policy on the main domain container instead of the OU. Not sure if this was the actual reason or something else because then it accepted the below command

Set-LapsADComputerSelfPermission -Identity "OU=Desktops HO,DC=domain,DC=com"

Thanks.
