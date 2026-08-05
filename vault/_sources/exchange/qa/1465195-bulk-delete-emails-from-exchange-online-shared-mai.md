---
title: "Bulk delete emails from exchange online shared mailbox."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1465195/bulk-delete-emails-from-exchange-online-shared-mai
question_id: 1465195
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Bulk delete emails from exchange online shared mailbox.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1465195/bulk-delete-emails-from-exchange-online-shared-mai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have issues bulk deleting emails from a shared mailbox which is used to store only logs and other reports no longer needed. To my surprise, it is not as easy as I thougth. We need to get rid of hundreds of thousands of emails.

Obviously outlook can't handle this. I tried to archive emails  with it in the given mailbox by setting up citerias, but did not do anything, no error messages, nothing happened. Freezes when it has to deal wiht large sum of emails.

I tried these from powershell after connecting to EO and compliance center scc: 

Starting a New Compliance search and then purge the results :New-ComplianceSearchAction -SearchName "Remove Phishing Message" -Purge -PurgeType SoftDelete/Hardelete.   Nothing happens, no error messages, does not delete anything.

 Deprecated search-mailbox command: Search-Mailbox mailbox1 -SearchQuery {Received:"1/1/2020..12/31/2022"} -DeleteContent. It is waiting for a while then returns the error: 

```
ConvertFrom-Json : Invalid JSON primitive: .
At C:\Users\user1\AppData\Local\Temp\tmpEXO_atsy5x51.aez\tmpEXO_atsy5x51.aez.psm1:623 char:35
+ ... etailsToPSObject = ConvertFrom-Json $ErrorObject.ErrorDetails.Message
+                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [ConvertFrom-Json], ArgumentException
    + FullyQualifiedErrorId : System.ArgumentException,Microsoft.PowerShell.Commands.ConvertFromJsonCommand
```

the New-MailboxSearch command does not even has syntaxes to delete results.  Now I am really confused if it is even possible to mass/bulk delete emails from a shared (or any other type)  mailbox, or I need to completely delete it  and recreate it? Any clues would be appreciated.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2023-12-20*

Search-Mailbox should be your best bet here, as the alternative compliance search cmdlet only allows for 10 deletions at a time. I'd suggest limiting the timespan to something like a week to limit down the number of matches found, then you can slowly start increasing it. 

One note though, Search-Mailbox will detect and process items in both the "main" mailbox as well as the RecoverableItems subtree, where deleted items end up. Consider using the -SearchDumpster:$false switch, or disabling single-item recovery on the mailbox (Set-Mailbox shared -SingleItemRecoveryEnabled $false)

Also, consider stamping a retention policy on the mailbox, so it periodically purges older messages (without the need for user intervention). Either the "classic" Exchange MRM policies or the "new" retention policies in the compliance center would do.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-30*

I recommend a tool:Bulk Delete Mail for Exchange

http://www.taysoon.com/search-and-delete-mails-13.html
