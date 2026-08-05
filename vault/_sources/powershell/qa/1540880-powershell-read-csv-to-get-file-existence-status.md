---
title: "Powershell Read CSV to get File existence status"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1540880/powershell-read-csv-to-get-file-existence-status
question_id: 1540880
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
---
# Powershell Read CSV to get File existence status

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1540880/powershell-read-csv-to-get-file-existence-status (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a script that woks brilliantly to delete files from a CSV.
I am struggling to create a script to read the same file to get status that the file no longer exists. Any help? :)

Delete script:

```
Import-Csv c:\files.csv | Foreach-Object{Remove-Item -LiteralPath $_.FullName -Force}
```

Validate script

```
Import-Csv c:\files.csv | get-childitem | where {!$.PSIsContainer} | select-object FullName, LastWriteTime, Length | export-csv -notypeinformation -path verifiedfiles.csv | % {$_.Replace('"','')}
```

## Answers

_No answers on this thread._
