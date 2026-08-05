---
title: "[Migrated from MSDN Exchange Dev] Mailboxes in O365 that do not have any retention policy applied??"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/161449/migrated-from-msdn-exchange-dev-mailboxes-in-o365
question_id: 161449
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Mailboxes in O365 that do not have any retention policy applied??

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/161449/migrated-from-msdn-exchange-dev-mailboxes-in-o365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/56479fcd-6696-4393-bf48-a5b3c40688ea/mailboxes-in-o365-that-do-not-have-any-retention-policy-applied?forum=exchangesvrdevelopment  

If a user mailbox has no retention policy applied what does that mean for things like Deleted item retention and RetainDeletedItems?  Does that mean no action is applied to these categories?  Or is there still some default setting that trumps the retention policy if none is applied?  

thanks!

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-13*

If no retention policy is applied to the mailbox, no retention tags will be applied to mailbox items. The Deleted item retention you mentioned is not related to retention policy. Also, there are some other actions for soft-deleted items.     

When mailbox items are soft-deleted, they are moved to the Deletions subfolder of the Recoverable Items folder. They remain there until the deleted item retention period is reached. The default deleted item retention period for Exchange Online is 14 days. The RetainDeletedItemsFor parameter specifies the length of time to keep soft-deleted items for the mailbox.    

For more details, please check:     

Deleted item retention,    

Set-Mailbox  -  RetainDeletedItemsFor    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
