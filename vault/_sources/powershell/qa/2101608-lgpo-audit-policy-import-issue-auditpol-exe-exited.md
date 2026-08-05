---
title: "LGPO Audit Policy Import Issue: AUDITPOL.EXE exited with exit code 13"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2101608/lgpo-audit-policy-import-issue-auditpol-exe-exited
question_id: 2101608
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
---
# LGPO Audit Policy Import Issue: AUDITPOL.EXE exited with exit code 13

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2101608/lgpo-audit-policy-import-issue-auditpol-exe-exited (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

I’m trying to import a backup using the LGPO (Local Group Policy Object) tool, but I keep encountering the following error:

```
Clearing existing audit policy
Apply Audit policy from C:\GPO-Backup\{GUID}\DomainSysvol\GPO\Machine\microsoft\windows nt\Audit\audit.csv
Error 0x0000000D occurred: The data is invalid.
AUDITPOL.EXE exited with exit code 13
```

Additionally, when I try to manually import the audit policy using the `auditpol` command, I get the same "exit code 13" error. The message seems to indicate "invalid data," but the CSV file appears to be formatted correctly with the necessary subcategories.

Here’s what I’ve tried so far:

-  Cleared the audit policy using `auditpol /clear`.

-  Checked the `audit.csv` file for format issues—no extra spaces    or incorrect characters as far as I can see.

-  Ran the command prompt as Administrator.

-  Tried different backup files, but still received the same error.

I’ve been searching online for explanations of error code 13 and 0x0000000D but couldn’t find much information. I’m at a loss as to why `auditpol` finds the backup invalid or what other steps I can take.

Has anyone faced a similar issue or know how to resolve this? I’d really appreciate any advice or insights!

System details:

Windows 10 Pro - 22H2

LGPO version: V3.0

Thanks in advance!

## Answers

_No answers on this thread._
