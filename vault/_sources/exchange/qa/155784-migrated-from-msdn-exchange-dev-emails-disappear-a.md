---
title: "[Migrated from MSDN Exchange Dev] Emails disappear after 7 days in inbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155784/migrated-from-msdn-exchange-dev-emails-disappear-a
question_id: 155784
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Emails disappear after 7 days in inbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155784/migrated-from-msdn-exchange-dev-emails-disappear-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/f18b49b4-319f-4db0-b08f-0d7b5d47c367/emails-disappear-after-7-days-in-inbox?forum=exchangesvrdevelopment  

Emails that arrived to our inbox over 7 days ago are disappearing. This is happening in a shared inbox with 10 users. Emails are not in the deleted folder or archived anywhere. We have several rules to route our desired emails to separate folders within this inbox, but all 10 users have noticed that emails vanish even in these folders. I've checked the auto archive settings and these are not enabled. I am running out of ideas! Dont know what is causing the emails to evaporate but we need them back :(

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-09*

What's the detailed version of your Exchange server?    

Does this Inbox belong to a user mailbox, or other types of mailbox?    

How do these users add and check the shared Inbox folder?    

When does this issue begin? Did you make any modification before this issue?    

Try to use the following command to search the missing message, and you can copy the search result to another mailbox:    

```
Search-Mailbox -Identity  -SearchQuery {Subject:"" AND From:} -TargetMailbox  -TargetFolder  -LogLevel Suppress
```

The SearchQuery parameter specifies a search string or a query formatted using KQL. For more information about KQL in Exchange, see Message properties and search operators for In-Place eDiscovery.    

Please also check if any retention tag or retention policy is applied to the mailbox and folder:    

```
Get-Mailbox  | Select Name, RetentionPolicy
```

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
