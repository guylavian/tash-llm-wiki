---
title: "Set email signatures for all users in Exchange Online?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2102915/set-email-signatures-for-all-users-in-exchange-onl
question_id: 2102915
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Set email signatures for all users in Exchange Online?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2102915/set-email-signatures-for-all-users-in-exchange-onl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there currently a way to set email signatures for all mailboxes in Exchange Online, without the use of a  paid product, and without the use of email flow rules to add disclaimers? 

 

It looks like there used to be a PowerShell module that did it through use of the command Set-MailboxMessageConfiguration. As far as I can tell, that hasn't worked since the switch to roaming signatures.

I've looked at the PS module ExchangeOnlineManagement but that only seems to have a handful of commands, and nothing useful, as far as I can tell. The documentation on that module is a disaster.

 

Thanks in advance!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-14*

Hi,@FarazI995

Thanks for posting your question in the Microsoft Q&A forum.

Based on your description, you don't want to use mail flow or third party paid software to add email signatures to all your users.

I checked the official Microsoft documentation and unfortunately, the only official method provided is mail flow.

The features you want may not be available at the moment.

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
