---
title: "Unable to get Cached Exchange to Sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1612878/unable-to-get-cached-exchange-to-sync
question_id: 1612878
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Unable to get Cached Exchange to Sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1612878/unable-to-get-cached-exchange-to-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We had a server crash for our Windows Server 2022 RDH (Desktop Experience) with Roaming Profiles copied from another Domain Controller Server Data Drive.

After the crash and restart of the RDH, staff advised that emails were not arriving (no new emails since the crash. Emails are being received in Outlook 365 on the RDH for around 15 users. Each user is experiencing the same symptoms. We tried at least the following to fix the errors and NOTHING has worked:

-  Quick and Online Repairs to Office 365

-  Uninstall and Reinstall to Change from Office 365 (64-bit) to Office 365 (32-bit)

-  Removing the User Outlook Profile and re-adding

-  Removing

-  Outlook.exe /safe

-  Clearing all add-ins

-  Outlook.exe /cleanips

-  Renaming a file in C:\Program Files{x86)\Microsoft Office\root\Office16 (in fact all files on the uninstall too).

-  Restoring the Servers back to VM Backups from days before crash (both servers - only 2 in the network)

-  Restarting Modems and Networking Equipment

-  Cleared Filters for Synchronisation

-  Cleared Offline Items (not that there are any once we delete/rename the .OST file)

-  Removing User Profile from RDH and re-login to recreate

And yet this all results in sync errors showing in the mailbox (original problem) and no emails download (NONE) to catch up an old .OST or even from creating a new .OST file.

We tried the following to see the extent of the damage:

-  Checking all Server Hardware and software is in healthy state

-  Trying to use a different email mailbox from another 365 Tenant on these users and same error

-  Trying to access these users mailbox from Online login (works fine)

-  Trying to access a 365 mailbox from a different 365 Tenant and same error

-  Trying to connect one of the user mailboxes from another PC on another site (works fine - both no caching and cached exchange mode)

-  Trying to connect a user mailbox on the domain admin login (works fine)

-  Almost all the resolutions we could find in Google Searches

This seems from the symptoms to be an issue with the user profiles, but I would have thought a VM restore to a time before the error would have resolved it if this was the case?

Really frustrating as I don't know why the restored Servers from backups before the crash would still yield the same issue??

The only thing that has seemingly fixed it for anyone online is to rebuild the user profiles from scratch - not ideal for 15 users......

Below are the error messages received for every folder or sync item in exchange many times while trying to sync a faulting mailbox on the server (users mailbox name redacted):

20:36:17 Synchroniser Version 16.0.17328

20:36:17 Synchronising Mailbox ’Mailbox Name’

20:36:17 Synchronising server changes in folder ’Inbox’

20:36:17 Downloading from server ’https://outlook.office365.com/mapi/emsmdb/?MailboxId=68411927-40’

20:36:18 Error synchronising folder

20:36:18                                 [8000FFFF-3EE-8000FFFF-560]

20:36:18                                 Unknown Error.

20:36:18                                 Microsoft Exchange Information Store

20:36:18                                 For more information on this failure, click the URL below:

20:36:18                                 https://www.microsoft.com/support/prodredirect/outlook2000_us.asp?err=8000ffff-3ee-8000ffff-560

20:36:18                                 Additional Info:

Failed while syncing item:

                EntryID:  No current item

                Item:      

                ErrCtx:    0x09010801

                Hresult:  0x8000FFFF

                FnCall:   0x09010602

## Answers

_No answers on this thread._
