---
title: "Purview retention policy not applied to Exchange mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2140030/purview-retention-policy-not-applied-to-exchange-m
question_id: 2140030
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-purview", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Purview retention policy not applied to Exchange mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2140030/purview-retention-policy-not-applied-to-exchange-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We subscribe to Microsoft 365 Business Premium and for compliance reasons enable Litigation Hold on all users' mailboxes to prevent permanently deleting correspondence. Nearing end of last year I read Microsoft 365 Retention policy should be used in favour over Litigation hold (being legacy).

I created a DLM retention policy in Purview to apply org-wide (Full directory) to Exchange mailboxes retaining forever, and thought that was it.

It was only recently (way after seven days) did I realise the policy has in fact not being applied to our mailboxes. The supposed mbx policy does not how up in our mailboxes's `InPlaceHolds` array (empty).

What else is supposed to be done to apply retention policies?

DisplayName              : icelava
Name                     : icelava
DistinguishedName        : CN=icelava,OU=company.onmicrosoft.com,OU=Microsoft Exchange Hosted
                           Organizations,DC=APC,DC=prod,DC=outlook,DC=com
ExchangeGuid             : GUID
IsInactiveMailbox        : False
LitigationHoldEnabled    : True
LitigationHoldDuration   : Unlimited
LitigationHoldDate       : 1 Jul 2021 16:11:28
LitigationHoldOwner      : ******@company.net
InPlaceHolds             : {}
ComplianceTagHoldApplied : False
RetentionHoldEnabled     : False
RetentionComment         :
RetentionUrl             :
RetentionPolicy          : Default MRM Policy
ElcProcessingDisabled    : False

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-01-03*

Org-wide policies do not show up under `InPlaceHolds`, this is by design. Instead, you can check them via the same property under the organizational config:

```
Get-OrganizationConfig | select -ExpandProperty InPlaceHolds
```

For more details you can refer for example to this article: https://learn.microsoft.com/en-us/purview/ediscovery-delete-items-in-the-recoverable-items-folder-of-mailboxes-on-hold?view=o365-worldwide#organization-wide-retention-policies
