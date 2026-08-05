---
title: "Active Directory how to move another OU from the listing name on excel using PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190524/active-directory-how-to-move-another-ou-from-the-l
question_id: 2190524
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Active Directory how to move another OU from the listing name on excel using PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190524/active-directory-how-to-move-another-ou-from-the-l (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Active Directory by using PowerShell, how do I move another OU based on the listing name on Excel?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-19*

Hi,

You can add the OUs and the target paths to a CSV file like this

```
"OU","target" 

"OU=ou1,OU=test1,DC=contoso,DC=com","OU=test2,DC=contoso,DC=com" 

"OU=ou2,OU=test1,DC=contoso,DC=com","OU=test2,DC=contoso,DC=com"
```

If the excel file is not a CSV, you can save it to a CSV file so that it can be imported to PowerShell.

Once it's imported, the Move-ADObject cmdlet can move the OUs to the target path for you.

```
$file ="C:\temp\ou.csv"

Import-CSV $file | ForEach-Object {

    Get-ADOrganizationalUnit $_.ou | Move-ADObject -TargetPath $_.target

}
```
