---
title: "Problem configuring Exchange Online mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2244305/problem-configuring-exchange-online-mailboxes
question_id: 2244305
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Problem configuring Exchange Online mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2244305/problem-configuring-exchange-online-mailboxes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have automation that provisions user accounts in Entra ID, assigns them to a security group associated with an M365 E5 license, and monitors for mailbox creation. Once the mailbox is provisioned, the automation configures audit and compliance settings.

```
Set-Mailbox `
      -Identity $identity `
      -AddressBookPolicy $addressBookPolicy `
      -AuditEnabled $true `
      -AuditAdmin $auditAdmin `
      -AuditDelegate $auditDelegate `
      -AuditOwner $auditOwner `
      -LitigationHoldEnabled $true `
      -LitigationHoldDuration $litigationHoldDuration `
      -RoleAssignmentPolicy $roleAssignmentPolicy

    Set-Mailbox `
      -Identity $identity `
      -LitigationHoldOwner $litigationHoldOwner
```

Setting the litigation hold owner in the above call results in the value not taking effect.

However, many other settings also do not take effect, such as the litigation hold duration.

Before I move all the settings that aren't taking effect to their own invocation, is there a convention regarding what parameter sets or combinations of parameters should not be used together?

I'd rather not issue multiple calls if not necessary.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2025-04-06*

It appears the problem was due to the order in which multiple cmdlets were executed.

The problematic order was:

-  `Set-User`

-  `Set-Mailbox`

-  `Set-MailboxRegionalConfiguration`

-  `Set-MailboxCalendarConfiguration`

-  `Set-CASMailbox`

-  `Enable-Mailbox -Archive`

The working order is now:

-  `Set-User`

-  `Set-MailboxRegionalConfiguration`

-  `Set-MailboxCalendarConfiguration`

-  `Set-CASMailbox`

-  `Enable-Mailbox -Archive`

-  `Set-Mailbox` (all but `-LitigationHoldOwner`)

-  `Set-Mailbox` (just `-LitigationHoldOwner`)
It appears that even when setting litigation hold parameters exclusively, the owner only has an effect after hold is enabled and when it is specified exclusively.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-04-05*

You should be able to set all the above in a single call. The documentation covers the various parameter sets you can use, bug again, the ones above should be OK.

Keep in mind that LitigationHoldOwner expects a string value, not a mailbox/user identifier (i.e. it will not be resolved internally). But it should be updated immediately. Perhaps what you are seeing is the delay in replicating the hold status?

On another note, nowadays Auditing is enabled by default in Exchange Online, and it's not recommended to override the default values therein, unless you have some specific requirements.
