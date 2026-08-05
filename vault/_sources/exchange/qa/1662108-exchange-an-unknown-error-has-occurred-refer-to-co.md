---
title: "Exchange: An unknown error has occurred. Refer to correlation ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1662108/exchange-an-unknown-error-has-occurred-refer-to-co
question_id: 1662108
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange: An unknown error has occurred. Refer to correlation ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1662108/exchange-an-unknown-error-has-occurred-refer-to-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am having an issue with a room mailbox that is syncing to E365. When looking at the account, there is an error that says "Exchange: An unknown error has occurred. Refer to correlation ID" . The room account was created in E365 at one point and then was deleted and re-created on-prem to sync to E365 (this was done as we could not have room accounts in both on-prem and E365 for 3rd party calendar syncing as it can only be in 1 location). The problem I am having is I cannot get the account to show in the E365 rooms list. I have tried to remove the account from the softdelete, but that does not work. I have tried removing and re-syncing and that does not work either. Hope someone can help with this, as I would like to get the room to show up in the Room list. I do have a ticket open with MS, but its been a month with no resolution.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-02*

Hi,

There are so many reasons could cause “Exchange: An unknown error has occurred. Refer to correlation ID” error message.

However, based on your description, it could be some of Exchange attributes has incorrect value. You could run Get-Mailbox, Get-User against the object and view the output via PowerShell. 

Then you could try to reset the password on the account in AD, let it sync with O365 and tried again. 

Also, please double check Exchange Online license is enabled for the mailbox.

If you have any questions, please feel free to contact me.
