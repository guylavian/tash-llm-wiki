---
title: "Is it safe to delete an exchange database with ADSI edit?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2136422/is-it-safe-to-delete-an-exchange-database-with-ads
question_id: 2136422
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Is it safe to delete an exchange database with ADSI edit?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2136422/is-it-safe-to-delete-an-exchange-database-with-ads (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

At some point in the past a database called Arbitration was created in our Exchange environment. Our current installation is Exchange 2016. If we go to the Exchange Amin Center and go to Sever, then databases, the list is blank. If we run Get-MailboxDatabase in the Exchange Management Shell we get an error...

"The Exchange server for the database object "Arbitration" wasn't found in Active Directory Domain Services. The object may be corrupted."

I can find this Arbitration database in ADSI Edit, but it is pointing to an old server that was decommissioned and recycled. Is it safe to delete it in ADSI or to change the sever it's pointing to in ADSI, to one of our current servers? Is it better to delete something like this or try to get it working again. I'm assuming with the errors and the fact that it has been pointing to a server that is not in service for years that the database isn't working or doing it's job. Any help or advice would be appreciated.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-25*

Hi @MDS Inc  ,

Welcome to the Microsoft Q&A platform!

Dealing with "Arbitration" mailboxes and databases in Exchange can be a bit tricky, especially when dealing with remnants from decommissioned servers. 

Here are a few points and steps you might consider: 

-  Before taking any action, ensure there are no arbitration mailboxes in use pointing to that database. You can do this by running: 

```
Get-Mailbox -Arbitration
```

-  If there are arbitration mailboxes pointing to the old and corrupted database, you'll need to move them to a valid database. 

-  Given that the old server has been decommissioned and recycled, and you are receiving errors indicating the database object is corrupted or not found, it is generally safer to delete the orphaned database rather than trying to rehome it. Follow these steps: 

-  If any arbitration mailboxes do exist, you should move them to a valid database. For example: 

```
Get-Mailbox -Arbitration -Database "ArbitrationDB" | New-MoveRequest -TargetDatabase "NewDatabase"
```

-  If you're confident that the database is no longer in use, you can delete it from ADSI Edit. This is a last-resort action and should be done carefully: 

-  Open ADSI Edit. 

-  Connect to the Configuration context. 

-  Navigate to: CN=Configuration [Domain], CN=Services, CN=Microsoft Exchange, CN=Your_Exchange_Org, CN=Administrative Groups, CN=Exchange Administrative Group, CN=Databases. 

-  Find and delete the reference to the old Arbitration database. 

-  After deletion, ensure there are no remnants of the old database: - Run the following command to check for mailbox database existence: 

```
Get-MailboxDatabase -Status
```

-  If arbitration mailboxes were deleted and are needed, recreate them. In Exchange 2016, you might need to recreate system mailboxes. Follow the official Microsoft guidelines for this step. 

Notes：

-  Always back up your Active Directory before making changes in ADSI Edit. Document all steps taken. 

-  If possible, test the above steps in a lab environment before applying them to production. 

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-12-24*

The situation with the "Arbitration" database pointing to a decommissioned server indicates a legacy artifact from an earlier Exchange installation. Arbitration mailboxes are critical system mailboxes that support features such as moderation and workflow in Exchange. However, considering the error messages you referenced, you should remediate the current issue.

1. Confirm the State of the Arbitration Database
Before taking any action, verify the references to the database. In ADSI Edit, navigate to:

```
CN=Configuration -> CN=Services -> CN=Microsoft Exchange -> CN=YourOrgName -> CN=Administrative Groups -> CN=Exchange Administrative Group -> CN=Databases
```

Locate the Arbitration database object and confirm it references the decommissioned server.

Run the following PowerShell command to check if any arbitration mailboxes are tied to this database:

```
Get-Mailbox -Arbitration | Where-Object {$_.Database -eq "Arbitration"}
```

  If any arbitration mailboxes are associated with the "Arbitration" database, you should move them to a valid database before deleting the object.

2. Decide on a Plan of Action
You have two options: delete the orphaned database or attempt to repoint it. The decision depends on whether the database is still needed.

Option 1: Delete the Orphaned Database Object
This would be more likely appropriate if the database has been non-functional for years and you confirm that no active arbitration mailboxes are associated with it.

-  Backup Active Directory: Before making any changes in ADSI Edit, take a system state backup or at least export the relevant portions of the configuration.

-  Delete the Database Object:

-  In ADSI Edit, locate the database object as outlined above.

-  Right-click the object and select Delete.

-  Force Replication: Use the following command to propagate changes across all domain controllers:

```
repadmin /syncall /AdeP
```

-  Validate Cleanup:

-  Run `Get-MailboxDatabase` again to confirm the database no longer appears.

-  Check the Exchange Admin Center for any errors related to the deletion.

Option 2: Repoint the Database to a New Server
This would be likely more appropriate if arbitration mailboxes are found on this database and you suspect they may still be in use.

-  Update the Database Object in ADSI Edit:

-  Modify the `msExchHomeServerName` attribute to point to a valid and current Exchange server.

-  Validate the Change:

-  Restart the Exchange Management Shell and check if `Get-MailboxDatabase` returns valid details for the database.

-  Mount the Database:

-  If the database file still exists and is accessible, you can attempt to mount it:

```
Mount-Database -Identity "Arbitration"
```

-  If successful, move arbitration mailboxes to another database:

```
Get-Mailbox -Arbitration | New-MoveRequest -TargetDatabase "ValidDatabase"
```

-  Decommission the Database:

-  Once arbitration mailboxes are migrated, remove the orphaned database using:

```
Remove-MailboxDatabase -Identity "Arbitration"
```

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
