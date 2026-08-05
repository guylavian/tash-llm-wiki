---
title: "About the arbitration mailbox during Exchange Server migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1348640/about-the-arbitration-mailbox-during-exchange-serv
question_id: 1348640
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# About the arbitration mailbox during Exchange Server migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1348640/about-the-arbitration-mailbox-during-exchange-serv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Thank you

*The content written in Japanese has been converted to English using a translation application, so I apologize if there are any mistranslations.

Due to the end of support for Exchange Server 2013, we are planning to switch to Exchange Server 2019.

Is there a way to move the arbitration mailbox when migrating to Exchange Server, or is there no problem if I recreate it using "Enable-Mailbox" on the destination server?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 2 · updated: 2023-08-21*

Hi @ sakura_snow_blossom,

You could migrate the arbitration mailboxes from Exchange 2013 to Exchange 2019.

The specific steps are as follows:

-  View the arbitration mailboxes in the two servers separately:

```
get-mailbox -server “exchange-2013” -Arbitration
get-mailbox -server “exchange-2019” -Arbitration
```

-  Use the following command to move them to the database in Exchange 2019:

```
get-mailbox -server “exchange-2013” -Arbitration | New-MoveRequest -TargetDatabase "Mailbox Database 2019"
```

-  Run the following command to check the progress:

```
Get-MoveRequest | Get-MoveRequestStatistics
```

-  Finally, you can check Exchange 2019 again to verify if it was successful:

```
get-mailbox -server “exchange-2019” -Arbitration
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-12*

Get-Mailbox -Arbitration | fl name, displayname, database, admindisplayversion
