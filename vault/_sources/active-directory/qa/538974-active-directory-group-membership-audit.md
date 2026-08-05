---
title: "Active Directory group membership audit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/538974/active-directory-group-membership-audit
question_id: 538974
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory group membership audit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/538974/active-directory-group-membership-audit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have different user types: i.e. agent, team lead, QA, trainer etc.   

Each of those is supposed to have certain AD group membership as a baseline:   

Agent - group: A, B, C, D, E  

Team Lead: F, G, H, X, Y, Z  

The issue is that some agents are being transferred from one project to a different one and no group memberships are remove, they're just adding.  

The question is if there is a way (i.e. by powershell) or a tool  to audit these (not one by one) - check current group membership against a baseline?  

Thanks in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-03*

Hello,  

I would like to suggest you to have a look on below powershell script which will list of users  member of those groups.  

after that you can do some excel filtering to Audit the group memberships as per base line.  

```
groups = "MYGroup1", "MYGroup2", "MYGroup3","MYGroup4"

$results = foreach ($group in $groups) {
    Get-ADGroupMember $group | select samaccountname, name, @{n='GroupName';e={$group}}, @{n='Description';e={(Get-ADGroup $group -Properties description).description}}
}

$results

$results | Export-csv C:\Temp\MYGroupMemberShip.txt -NoTypeInformation
```

If the reply was helpful, please don’t forget to upvote or accept as answer.
