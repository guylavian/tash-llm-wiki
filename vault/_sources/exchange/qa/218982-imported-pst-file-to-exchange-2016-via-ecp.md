---
title: "Imported PST file to Exchange 2016 via ECP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218982/imported-pst-file-to-exchange-2016-via-ecp
question_id: 218982
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Imported PST file to Exchange 2016 via ECP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218982/imported-pst-file-to-exchange-2016-via-ecp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I tried to use Exchange 2016 CU14 to import a PST file into a user archive mailbox using ECP (not from Outlook).  

I directed the wizard to the PST network path.  

The process began and finished successfully.   

We also get the confirmation mail "Import PST has finished" which states "Import PST has finished".  

Looking at the result of Get-MailboxImportRequest also shows Completed.  

Even when I look at the Totalitemsize and the itemcount on the user archive mailbox via Get-mailboxstatistics it seem that the number of  

items and size patch the content that should have been imported.  

However, when looking in the archive mailbox itself via Outlook or OWA only the PST hierarchy is available, the content is missing.  

Can someone tell me what is going on ?  

Thank  

Liran

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-30*

In the EAC, go to Recipients > Mailboxes > click More options. , and select Import PST.    

The Import from a . pst wizard opens.     

On the next page, select the target mailbox, and then select one of these options: Import to this mailbox.     

On the last page, configure one of these settings:    

Greetings,    

Chris
