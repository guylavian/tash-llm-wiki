---
title: "How to just disable a mailbox in Exchange Hybrid Environment?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1656272/how-to-just-disable-a-mailbox-in-exchange-hybrid-e
question_id: 1656272
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to just disable a mailbox in Exchange Hybrid Environment?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1656272/how-to-just-disable-a-mailbox-in-exchange-hybrid-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi.

We have a Exchange Hybrid Environment and all mailboxes are migrated to Exchange Online.

How to just disable a mailbox attached to the user account?

I have tried Disable-Remotemailbox but it only removes the mailbox related info from Onprem exchange and I still can see user mailbox in Exchange online as is.

Thanks.

Regards,

Raj

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-15*

Remove the Exchange Online license or run

https://learn.microsoft.com/en-us/powershell/module/exchange/disable-mailbox?view=exchange-ps

-PermanentlyDisable

This parameter is available only in the cloud-based service.

The PermanentlyDisable switch specifies whether to permanently disable the mailbox. You don't need to specify a value with this switch.

Notes:

-  You can only use this switch on user mailboxes that aren't licensed and aren't on hold.

-  When the Exchange Online license is removed from a mailbox without following other deprovisioning steps, this may leave the mailbox in a hard-deleted state. In this case, this parameter is not useful. You can use it, for example, in hybrid Exchange environments.

Note you will still need to disable the remote mailbox on-prem.

I prefer to just remove the Exchange online license, but Im not sure what your requirements are for disabling the mailbox here.
