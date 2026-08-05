---
title: "Exchange 2019 Distribution Group Owners Can't Edit Members"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/410371/exchange-2019-distribution-group-owners-cant-edit
question_id: 410371
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Distribution Group Owners Can't Edit Members

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/410371/exchange-2019-distribution-group-owners-cant-edit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have made a migration from four onPrem Exchange 2013 servers to four new Exchange 2019 servers. After the migration Distribution Group Owners can't edit members from Outlook. If the mailbox is in a database on a specific server, it works. But not for mailboxes on the other three servers. Grateful for any help. Has Googled the issue without success. Have tested several suggestions     

exchange-2016-distribution-group-owners.html    

cannot-manage-distribution-group-exchange-mailbox

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-27*

Hi,  

We mayl test but I do not hope that the solution problem is to move to new databases.  We have 16,000 mailboxes.  I will return when we have tested on a smaller scale.  

//Michael

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-27*

Hi @Michael Wiskman   ,    

Have you ever tried re-assign the owner permissions?    

Also try creating a new DG on one of the three servers and test if this time the function could work.    

Creating a new database for the problematic servers and migrate the original users to them may solve this too.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
