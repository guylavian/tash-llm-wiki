---
title: "Unable to delete exchange database - Duplicate key found in ADSI Edit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1163952/unable-to-delete-exchange-database-duplicate-key-f
question_id: 1163952
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to delete exchange database - Duplicate key found in ADSI Edit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1163952/unable-to-delete-exchange-database-duplicate-key-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently added a 2019 exchange server to our domain and are now ready to remove the old 2016 server.  We have migrated all mailboxes to the 2019 server, and are now trying to delete the last database on the 2016 server.  When we do, we get an error

This mailbox database is associated with one or more active MailboxImport requests. To get a list of all MailboxImport requests associated with this database, run Get-MailboxImportRequest | ?{
$_.RequestQueue -eq "<Database ID>" }. To remove a MailboxImport request, run Remove-MailboxImportRequest <Recipient ID\Request Name>.

When we run that command, nothing shows up.  Searching the web, came across this article about ADSI Edit:

[https://social.technet.microsoft.com/Forums/ie/en-US/54fd0db4-11d3-421c-92e8-d4050338a907/trouble-removing-2016-mailbox-database?forum=Exch2016Adm

Launching ADSI Edit to look for lingering objects, and I did find one, but I also found something else.  Under our exchange organization, we have two objects named "CN-Mailbox Replication".  The Rogue MailBoxImportRequest is found under the second one.  Do I just delete the rogue record, or should I also remove the entire duplicate set of folders?

The second set of folders, containing the remaining record, has a weird path as well:

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-02-08*

You can use the following steps to remove the lingering MailboxImportRequest:

-  Launch the ADSI Edit tool.

-  Connect to the default naming context, CN=Configuration,DC=<domain name>.

-  Expand the CN=Services,CN=Microsoft Exchange,CN=<organization name>,CN=Administrative Groups,CN=<administrative group name>,CN=Servers,CN=<server name>,CN=InformationStore,CN=<mailbox database name> object.

-  Search for the MailboxImportRequest objects and identify the rogue MailboxImportRequest.

-  Right-click the rogue MailboxImportRequest object and select Delete.

-  Confirm the deletion and close the ADSI Edit tool.

Regarding the duplicate set of folders, if you only need to delete the rogue MailboxImportRequest, then you only need to delete the rogue record. If you are unsure, you may contact Microsoft support for assistance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-27*

At first, one would use the Get-MailboxExportRequest PowerShell command to check if there are any pending mailboxes to be exported or stuck. For more detail - this mailbox database is associated with one or more active mailbox export requests.

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-25*

Hi @Dustin Smith  ,

Please try creating a new database and moving all users from the old database to it. Then delete again to see if it succeeds.

If possible, we try not to recommend modifying it in ADSI edit because it is destructive and cannot be undone.

Here is a similar thread for your reference: Exchange 2013: This mailbox database is associated with one or more active mailboximport / Cannot uninstall exchange (microsoft.com)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
