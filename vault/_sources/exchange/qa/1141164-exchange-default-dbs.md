---
title: "Exchange Default DBs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1141164/exchange-default-dbs
question_id: 1141164
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Default DBs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1141164/exchange-default-dbs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have a two-node Exchange 2013 DAG. All the mailboxes are under a single DB, but two additional DBs were created by default in each node and are taking up much space in C:\ drive.    

Is it necessary to keep them? There is no mailbox under them.    

Mailbox Database 04562757643  under (Node1)    

Mailbox Database 07563658785  under (Node2)    

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-26*

Hi @create share  ,    

If the following mailboxes do not exist in the default database, you can delete the database.    

Check the arbitration mailbox:    

```
Get-Mailbox -Arbitration -Database "Mailbox Database 04562757643"
```

Check other types of mailboxes, such as Monitoring, Auditing, Archive, and Public Folder mailboxes:    

```
$mbxdb="Mailbox Database 04562757643"  
Get-Mailbox -Database $mbxdb -Auditlog  
Get-MailBox -Database $mbxdb -Archive  
Get-MailBox -Database $mbxdb -PublicFolder  
Get-MailBox -Database $mbxdb -Monitoring
```

If such mailboxes are found, they must be moved using the following pipe: | New-MoveRequest -TargetDatabase (you can disable the Monitoring mailbox | Disable-Mailbox -Confirm:$false).    

Check that there are no user mailboxes or DiscoverySearchMailbox left in the database:    

```
Get-Mailbox -Database "Mailbox Database 04562757643"
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-24*

You can remove them if they have no mailboxes.    

Make sure the arbitration mailboxes are not in those DBs as well    

```
Get-Mailbox -Arbitration  
Get-Mailbox -AuditLog
```
