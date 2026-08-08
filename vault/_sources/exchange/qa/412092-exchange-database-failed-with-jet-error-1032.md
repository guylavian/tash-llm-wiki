---
title: "Exchange database failed with Jet error -1032"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/412092/exchange-database-failed-with-jet-error-1032
question_id: 412092
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange database failed with Jet error -1032

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/412092/exchange-database-failed-with-jet-error-1032 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,    

I have 2 exchange servers 2019 (DAG), While I'm exporting mailboxes to .pst i noticed that almost half of mailboxes not being exported and i got the following error:    

    

but other mailboxes have been exported successfully. I checked failed exported mailboxes and all of them were in DB01 and successfully exported mailboxes were on DB02.    

Also im getting warning message through windows server backup (completed with warning) holding DB01. Both database are mounted and working fine (all users on both databases can access their mailboxes and send\ receive). I run the following commands:    

-  Test-Mailflow    

-  Test-ServiceHealth    

-  Test-ReplicationHealth    

-  Test-SmtpConnectivity    

all results are good. I checked DB01 heath by using eseutil /mh DB01.edb (while DB01 is running) and i got the following error:    

    

Do i have to dismount the DB01? what i can do to fix exporting DB01 mailboxes?    

Regards,

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-05-31*

You can try resolving this problem using Eseutil /p command-line tool or by restoring the database again from backup. If possible, move unaffected files from problem database to the new database.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-05-27*

This looks more like an issue with permissions to that path.    

https://learn.microsoft.com/en-us/exchange/recipients/mailbox-import-and-export/export-procedures?view=exchserver-2019    

    

No need to run eseutil!!!     

And yes, you would need to dismount the database to run that, but do not do that.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-03*

Also, you can refer to this LinkedIn article for some insight - https://www.linkedin.com/pulse/error-resolved-eseutil-operation-terminated-1032-shelly-bhardwaj/

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-31*



## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-31*

anonymous userDavid @Anonymous       

I added exchange trusted subsystem on both Shared folder and NTFS permission, and i added both exchange servers on the shared folder with full control permission as well but the issue is still exists. I'm able to export all mailboxes exists on DB01 only.
