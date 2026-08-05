---
title: "PowerShell script to loop through Exchange Online MailContacts in CSV file until they are deleted from Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2119287/powershell-script-to-loop-through-exchange-online
question_id: 2119287
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# PowerShell script to loop through Exchange Online MailContacts in CSV file until they are deleted from Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2119287/powershell-script-to-loop-through-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I have an input CSV file which contains the PrimarySMTPAddress values of Exchange Online MailContacts (like this):

PrimarySMTPAddress

******@test.com

******@test.com

These MailContacts are located in our On Premise Exchange Servers/Active Direcotry and are subsequently synced to Exchange Online.

Occasionally, we need to be able to delete these users from Exchange On Premise/Active Directory (and subsequently have those deletes sync to Exchange Online). I would like to have a PowerShell script so that when it is run, it will check to see when the MailContacts have been deleted from Exchange Online. The script requirements would be:

-  Read the contents of the CSV file.

-  Create a loop so that the script will check if the MailContacts have been deleted in Exchange Online.

-  Once all users in the CSV file have been confirmed that they have been deleted from Exchange Online ID, exit the loop.

Thanks in advance!

## Answers

_No answers on this thread._
