---
title: "Powershell cannot read CSV - Export is from Oracle"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/184790/powershell-cannot-read-csv-export-is-from-oracle
question_id: 184790
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Powershell cannot read CSV - Export is from Oracle

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/184790/powershell-cannot-read-csv-export-is-from-oracle (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

As people maybe have seen I'm busy with adding a User Principle Name to a CSV. Now  with some help that code works.    

Only after debugging I  discovered the issue. I don't get data from the CSV I import.    

When i try the easiest thing, my variable stays empty    

$csvfile = Import-CSV -Path C:\Temp\eport.csv    

Foreach ($line in $csvfile) {    

```
Write-Host $line.EMAIL
```

}    

My import-csv is from an Oracle DB export and looks like this, I trimmed spaces    

EMAIL;Username;    

a.borgeld@Karima ben  .com;ABORGELD;    

a.borgeld@Karima ben  .com;ABORGELD;    

Does anybody have experience with CVS's from a database that you can't read? Of course when i open the notepad then the data is there

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-03*

Oh my @Andreas Baumgarten   sometimes life can be so easy.     

Thanks for getting me out of that black whole. The whole script will work now.    

You've got to deal with different outputs.
