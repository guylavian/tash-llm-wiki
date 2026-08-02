---
title: "Exchange Hybrid Mailbox Migrations - Skipped Items script"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1661063/exchange-hybrid-mailbox-migrations-skipped-items-s
question_id: 1661063
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-development"]
---
# Exchange Hybrid Mailbox Migrations - Skipped Items script

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1661063/exchange-hybrid-mailbox-migrations-skipped-items-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a script that I'm working on to get query the entire batch, grab the users, then get the skipped items. This one works, but it crams the expanded skipped items in one line for one user. How can I modify this so it puts each skipped item for one user in a seperate line?

$MigrationUser=Get-MigrationUser -batchid b40af8ae-d4fd-4208-a085-ac1bd76f126 -resultsize unlimited

$Results = foreach( $Mailbox in $migrationuser ){

    $Stats = Get-migrationuserstatistics -Identity $Mailbox -includeskippeditems | ?{$_.skippeditems -ne $null} | select-object -expandproperty skippeditems

    New-Object -TypeName psobject -Property @{

        Name                    = $migrationuser.identity

      RuleName            = $Stats.subject

      Type               = $stats.kind

        }

    }

$Results | ft  name,rulename,type -autosize > c:\temp\migrationrules.csv

## Answers

_No answers on this thread._
