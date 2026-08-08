---
title: "Exchange is appending numbers to DL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/361616/exchange-is-appending-numbers-to-dl
question_id: 361616
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Exchange is appending numbers to DL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/361616/exchange-is-appending-numbers-to-dl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All    

i am using exchange2016 hybrid environment, i have created distribution list in exchange onprem by name Test Group.    

But in AD i can see the group name as Test Group-396684025 in Group Name(pre-windows 2000). This is happening to all the DLs created in exchange onprem.    

How to fix this.    

Get-DistributionGroup Test.Group@Company portal   .com | FL Name,DisplayName,SamAccountName    

Name           : Test Group    

DisplayName    : Test Group    

SamAccountName : Test Group-396684025    

-  How do i change the SamAccountName for Test Group using exchange powershell.    

-  how do i create new DL from Exchange powershell where i can specify the SamAccountName

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-07-20*

It appears this behaviour was introduced in Exchange 2016 and remains present in later CUs:

-  https://learn.microsoft.com/en-us/answers/questions/458261/creation-of-groups-number-added

The reason behind this is:

-  Exchange EAC does not populate the sAMAccountName when creating a Distribution Group.

-  Active Directory therefore generates the sAMAccountName automatically and appends a numeric suffix to ensure uniqueness (for example, Test Group-396684025).
