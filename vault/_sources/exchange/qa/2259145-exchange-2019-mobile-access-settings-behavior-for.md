---
title: "Exchange 2019 - Mobile Access Settings Behavior for ActiveSync Devices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2259145/exchange-2019-mobile-access-settings-behavior-for
question_id: 2259145
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 - Mobile Access Settings Behavior for ActiveSync Devices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2259145/exchange-2019-mobile-access-settings-behavior-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After modifying the "Exchange ActiveSync access settings", new ActiveSync devices are receiving a "DeviceAccessStateReason" that differs from the previous state, such as "Individual" or "Policy". What steps are necessary to revert this behavior back to "Global"? Additionally, under what conditions does a "Policy" trigger an immediate "Blocked" status without sending "Quarantined Devices" for approval?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-17*

Apparently, the main reason is the persistence of the "ActiveSyncAllowedDeviceIDs" and "ActiveSyncBlockedDeviceIDs" parameters. After deleting these parameters via the Set-CASMailbox cmdlet, everything is "Global" again.
