---
title: "Exchange Server 2019 deleted the email"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2260744/exchange-server-2019-deleted-the-email
question_id: 2260744
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019 deleted the email

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2260744/exchange-server-2019-deleted-the-email (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello:

We are currently an Exchange 2019 server and need to delete an email with the following subject: The email "Fa Fa [2025] No. 19 - Notice on the Division of Work among Company Leadership Members" Using the 'Search-Mailbox ****** @test.com-SearchQuery 'Subject:' Send [2025] No. 19 - Notice on the Division of Work among the company '-deletecontent command to delete the email failed, but the email is still there. However, I tested the Exchange 2016 server and successfully deleted emails with the same command on the same topic. May I ask what the reason is? Thank you!

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-24*

Hi yanhaowen,

Thank you for posting your question in the Microsoft Q&A forum.

For Exchange 2019, the search infrastructure is rebuilt, and the logic is different from Exchange 2016.

Here are some suggestions for you to check search issues on Exchange 2019 mailbox:

-  Please confirm that Microsoft Exchange Search service keeps running well on Exchange 2019 where the problematic mailbox is located.

-  We noticed that the keyword you specified in the Subject is a little different from the original email subject. Please try the following command to see if Search-mailbox could find the item successfully with different keywords.

These commands will help to search and copy the search result to one target mailbox, it could help us to check if the correct item is found:

Search-Mailbox mailbox_name -SearchQuery ‘Subject:“Fa Fa [2025] No. 19 - Notice on the Division of Work among Company Leadership Members”’ -TargetMailbox "target_mailbox_name" -TargetFolder "folder_name" -LogOnly -LogLevel Full

 

Search-Mailbox mailbox_name -SearchQuery ‘Subject:“Notice on the Division of Work among Company Leadership Members”’ -TargetMailbox "target_mailbox_name" -TargetFolder "folder_name" -LogOnly -LogLevel Full

 

Search-Mailbox mailbox_name -SearchQuery ‘Subject:“Fa Fa [2025] No. 19”’ -TargetMailbox "target_mailbox_name" -TargetFolder "folder_name" -LogOnly -LogLevel Full

-  Use the following command to check if any not indexed items in this mailbox:

Get-MailboxStatistics mailbox_name |fl notindex

 

If your Exchange 2019 server is CU11 or later versions, please try the following command to process and index the mailbox items in the NonIndexed state:

Start-MailboxAssistant -Identity "mailbox_name" -AssistantName BigFunnelRetryFeederTimeBasedAssistant

Wait for some time and check with search-mailbox cmdlet again, to see if the correct item could be searched and deleted.

-  If there are still some items in NonIndexed state even running Start-MailboxAssistant, please try the following link to create an override and re-index affected items:

Incomplete search results after installing an Exchange Server 2019 update - Microsoft Support 

Note: The setting override helps you avoid having to move mailboxes in order to reindex items. However, we recommend that you do not leave the override set in the environment permanently because it can cause increased CPU usage. After the items are reindexed, remove the override by using the Remove-SettingOverride cmdlet.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
