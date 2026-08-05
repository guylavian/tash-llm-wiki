---
title: "Exchange Management Shell Bulk Properties"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1096413/exchange-management-shell-bulk-properties
question_id: 1096413
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Management Shell Bulk Properties

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1096413/exchange-management-shell-bulk-properties (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Evening,    

I am a Navy IT and this is my first time diving into powershell. My interest is peaked because I need to find a way to change a property on multiple security groups to allow emails from outside of our domain. Any help would be appreciated as well as any good references for me to start teaching myself Powershell and Exchange Management Shell.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-20*

You can achieve this task in several different methods, but for the sake of giving you an example, let's assume you have the list of groups in a CSV file, with a column GroupEmail to designate each group's email address. Start by importing the list:    

```
$groups = Import-CSV blabla.csv
```

Then, we use a simple cycle (foreach statement) to iterate over the groups, and toggle the -RequireSenderAuthenticationEnabled property (which controls the external message delivery setting):    

```
$groups | % { Set-DistributionGroup $_.GroupEmail -RequireSenderAuthenticationEnabled $false }
```

Here % stands as an alias for the foreach statement; $_ represents the current object as it passes the pipeline, in other words it automatically represents each group object as imported from the CSV; $_.PropertyName will represent the value of the corresponding property for the current group, in our case this will be the email address as imported from the CSV.
