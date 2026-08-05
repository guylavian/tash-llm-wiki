---
title: "Issues with \"ExchangeGuid\" is used by another recipient"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1196240/issues-with-exchangeguid-is-used-by-another-recipi
question_id: 1196240
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Issues with "ExchangeGuid" is used by another recipient

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1196240/issues-with-exchangeguid-is-used-by-another-recipi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

we currently have an exchange hybrid mode. We are observing lots of issues with the error "ExchangeGuid" is used by another recipient object". As per the Microsoft documentation, it says that it happens because of soft deleted MailUser / UserMailbox.  

When I was trying to resolve this, I found for one of my user on M365 admin center saying that mailbox setup is in process.   

When I ran the following command, I got the recipient results as user mailbox and softdeleted in early 2022.  

Get-Recipient -IncludeSoftDeletedRecipients 'ExchangeGUID value'|ft RecipientType,PrimarySmtpAddress,WhenSoftDeleted  

 I am wondering how it was fetching the results. Usually, soft deleted items were stored for 30days.  

Instead of doing the purge, I went on changing the ms-exch-guid-attribute at on-prem for the user account to null, then the problem was solved.   

I would like to know what's the exact process to resolve this and how to avoid this in future.  

https://learn.microsoft.com/en-us/archive/blogs/exovoice/how-to-fix-office365-user-provisioning-issues-that-are-generated-by-faulty-exchange-attributes#part-2-fixing-provisioning-errors-related-to-archiveguid-exchangeguid-being-used-by-another-recipient-1

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-06*

the resolution of making the ExchangeGuid Null is not working now. Still mailbox is not provisioning until we purge from inactive mailboxes.   

Any other way to either bind the inactive mailbox or create new mailbox ?

Inactivate mailbox are kept on hold and cannot be purge due to legal reason
