---
title: "Quarantined to allowed state in exchange online."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1011448/quarantined-to-allowed-state-in-exchange-online
question_id: 1011448
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Quarantined to allowed state in exchange online.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1011448/quarantined-to-allowed-state-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there any automated way to set the mobile devices Quarantined state to allowed state in exchange online?  As during migration of mobile devices from workspace one to intune some device are automatically set in quarantined state.  so how can we set  only the migrated devices in allowed state which is under quarantined state ?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-17*

You can update the Default access level under your org-wide ActiveSync settings:    

```
Set-ActiveSyncOrganizationSettings -DefaultAccessLevel Allow
```

Or you can allow devices programmatically via Set-CASMailbox.
