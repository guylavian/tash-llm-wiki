---
title: "Emails NON Delivery exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305940/emails-non-delivery-exchange-2016
question_id: 305940
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Emails NON Delivery exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305940/emails-non-delivery-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi   

am facing a unique issue with my email Server, many users are complaining that external emails are not delivered to their mailboxes, when i checked tracklogs some of the mails are already showing delivered(but not found in inbox) , but some emails are not listed in the log at all. im running exchange version 2016, kindly someone help to resolve this issue.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-10*

Hi, @Royal D Costa       

Did the senders receive NDR messages indicating the mail delivery failure?    

If they didn't receive any NDR messages, and the message tracking log shows the mails are delivered, you may use the search-mailbox command to check if the mails are in the users' mailboxes.    

For example, the following command searches mails which contain "test" in the subjects in userA's mailbox and export the search results to the inbox of the administrator's mailbox. ( Don't forget to add -LogOnly otherwise the command will copy the mails to the target folder)    

```
Search-Mailbox -Identity "userA" -SearchQuery 'Subject:"test"' -TargetMailbox "administrator" -TargetFolder "inbox" -LogOnly -LogLevel Full
```

    

From the "Search Results" csv file, you may see the folder which contains the mails.    

    

If you can't find the mails in message tracking log, were the mails sent 30 days ago?(by default, message tracking log is kept for 30 days)     

And is it a stand-alone Exchange server or do you have other Exchange servers in your environment?    

Please also confirm if the senders receive any NDR message for the mail delivery failure.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
