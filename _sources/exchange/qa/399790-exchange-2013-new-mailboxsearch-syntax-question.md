---
title: "exchange 2013 New-MailboxSearch syntax question"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/399790/exchange-2013-new-mailboxsearch-syntax-question
question_id: 399790
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange 2013 New-MailboxSearch syntax question

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/399790/exchange-2013-new-mailboxsearch-syntax-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

trying to find email in multiple user mailboxes regarding a  topic, one word and I am not getting errors or results just the >> after the command in powershell.  

here is the commend, is my syntax off?  

New-MailboxSearch -name "Search2021_A" -SourceMailboxes "user1","user2","user3" -StartDate :01/01/2019 12:01 AM" -EndDate"12/31/2020 11:59 PM" -SearchQuery "Secret Project" -TargetMailbox "results2021"  

Mailbox names changed for posting

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-19*

Hi,    

The colon `:` immediately following the `-StartDate` should be a double quote `"` and there should be a space between `-EndDate` and the double quote.    

```
New-MailboxSearch -name "Search2021_A" -SourceMailboxes "user1","user2","user3" -StartDate "01/01/2019 12:01 AM" -EndDate "12/31/2020 11:59 PM" -SearchQuery "Secret Project" -TargetMailbox "results2021"
```

Best Regards,    

Ian Xue    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
