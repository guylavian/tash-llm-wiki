---
title: "How to delete Search History in Exchange Server OWA?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1277445/how-to-delete-search-history-in-exchange-server-ow
question_id: 1277445
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to delete Search History in Exchange Server OWA?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1277445/how-to-delete-search-history-in-exchange-server-ow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,

```
How to delete Search History in Exchange Server OWA? Not Outlook 2016 Or 2019 Client,nor O365 and Outlook.COM Online mailboxes.
```

Below is a screenshot,delete history 2684:

Thanks for the answer.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-08*

Hi @Dicha Ding  

As this setting is within the mailbox, there is no easy method for users to delete it.

Please contact your Exchange admin and run the following cmdlet in Exchange Management Shell to remove this cache:

```
Get-MailboxUserConfiguration -Mailbox  -Identity Configuration\* | Remove-MailboxUserConfiguration -Mailbox 
```

Another method is to use MFCMAPI  to login the mailbox and delete this entry:

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-07*

Bing ChatAI Answer,not supported by design.Not sure if it is, case O365 and Outlook.com Online can clear search history, Exchange Server OWA should do too.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-07*

Thank you!But your reply is not a workaround.I want to know the Exchange OWA Offline environment, and you reply to the Outlook.com Online environment.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-05-06*

Hello @Dicha Ding

To delete the search history in Exchange Server OWA, you can follow these steps:

- 

```
Log in to your Exchange Server OWA account.
```

- 

```
Click on the "Settings" icon (gear icon) in the top-right corner.
```

- 

```
Click on "Options" from the dropdown menu.
```

- 

```
In the left-hand menu, click on "General" and then scroll down to the "Privacy and Security" section.
```

- 

```
Click on "Clear" under the "Clear search history" option.
```

- 

```
A popup will appear asking if you want to clear your search history. Click on "Yes" to confirm.
```

I hope this helps!

Kindly mark the answer as Accepted and Upvote in case it helped!

Regards
