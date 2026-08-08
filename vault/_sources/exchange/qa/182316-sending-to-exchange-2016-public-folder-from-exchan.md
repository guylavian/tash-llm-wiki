---
title: "Sending to Exchange 2016 public folder from Exchange Online mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/182316/sending-to-exchange-2016-public-folder-from-exchan
question_id: 182316
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Sending to Exchange 2016 public folder from Exchange Online mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/182316/sending-to-exchange-2016-public-folder-from-exchan (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are currently in a hybrid with Exchange 2016 server and Exchange Online.  The public folders are still on premises.  

Months ago, when we first started migrating mailboxes, I ran the Sync-MailPublicFolders.ps1 script and enabled the cloud environment to access the on prem public folders.  

I recently migrated a user's mailbox, and he is now receiving this error when he tries to send mail to a mail-enabled public folder to which he has Editor permission: "Your message couldn't be delivered to a public folder because delivery to this address is restricted to authenticated senders."  

He had editor permission through group membership, so I tried granting permission explicitly to his user ID, but he is still receiving this error.  

What do I need to do to allow him to send messages to this public folder from the cloud mailbox to which he has been migrated?  

Thank you very much for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-02*

Thank you very much for your answer.  I went ahead and granted anonymous the contributor permission and the user in question confirmed he could now send messages to it.  

I was hoping to keep senders restricted to specific individuals for this folder, but I guess a hybrid environment can't handle that.  I'll have to go ahead and check the rest of my mail-enabled public folders so that we don't run into the same problem as we continue to migrate mailboxes over to the cloud.  I plan to migrate public folders after everyone's mailbox has been migrated.  

Thanks again for your help with this.  It is much appreciated.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-01*

What is Default permissions set to?  

```
Get-PublicFolderClientPermission 'full folder path'
```

If not contributor  

```
Add-PublicFolderClientPermission -identity "\Folder root\Folder" -User Default -AccessRights CreateItems
```

or  

```
Add-PublicFolderClientPermission -identity "\Folder root\Folder" -User Default -AccessRights Contributor
```

This assumes your hybrid connector is setup correctly and messages from office 365 > On-Prem are "authenticated" as they should be.
