---
title: "Exchange Online PowerShell output format has changed?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1286024/exchange-online-powershell-output-format-has-chang
question_id: 1286024
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online PowerShell output format has changed?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1286024/exchange-online-powershell-output-format-has-chang (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Simple one line queries such as Get-Mailbox ******@domain.com now output a full table instead of truncated simple outputs as before.  Also running a Get-MessageTrace outputs tables instead of a clean formatted list .  I know i can change the output formatting to make it appear like before ( "|Ft ) but this was never needed before. What changed?

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-05-23*

okay i updated my module to 3.1.0 and it solved it. Thanks  

Hi @geezbill  ,

Great to know that it worked after updating the module and thanks for sharing the solution so that others experiencing the same thing can easily reference this! 

Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )    

[Exchange Online PowerShell output format has changed?]

Issue Symptom:

Simple one line queries such as Get-Mailbox ******@domain.com now output a full table instead of truncated simple outputs as before. Also running a Get-MessageTrace outputs tables instead of a clean formatted list . 

Resolution:

"i updated my module to 3.1.0 and it solved it"

Reference: Update the Exchange Online PowerShell module

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-17*

It's not just get-mailbox.  any exchange query will return full results and this is not desired. If i wanted full results i would add the necessary switches and operators.  This  behavior started a few weeks back.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-05-17*

Hi @geezbill  ,

 

`Simple one line queries such as Get-Mailbox ******@domain.com now output a full table instead of truncated simple outputs as before`

Just kindly want to know what exactly is the output you get so far, can you share a screenshot? (Please note to erase private information)

 

As far as I know, there's a lot more information that's associated with an Exchange Online mailbox than just the four properties returned by the Get-Mailbox cmdlet. In order to obtain specific information, more parameters are required in Exchange online powershell.

Please refer to: Use Exchange Online PowerShell to display mailbox information in Exchange Online | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
