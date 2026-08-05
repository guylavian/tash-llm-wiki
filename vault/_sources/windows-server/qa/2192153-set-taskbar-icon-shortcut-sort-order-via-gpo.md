---
title: "Set taskbar icon/shortcut sort order via GPO?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192153/set-taskbar-icon-shortcut-sort-order-via-gpo
question_id: 2192153
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Set taskbar icon/shortcut sort order via GPO?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192153/set-taskbar-icon-shortcut-sort-order-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a way to set the order of the icons in the Windows taskbar via Group Policy (GPOs)? I'm using the xml file but it doesn't seem to have any ability to force a certain order for the icons in the taskbar. I'm trying to create a consistent taskbar interface for users in a Remote Desktop environment (Server 2022). I can set the order initially but users can accidentally change the order and there seems to be no way to reset the order via GPO.

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-12*

Hi PaulRogers001,

Unfortunately, there is no built-in way to set the order of icons in the Windows taskbar via Group Policy. The taskbar order is stored in the user's profile, and there is no GPO setting to modify this. However, you may be able to achieve your desired result by using a third-party tool or script to reset the taskbar order to a predefined layout. You could then deploy this tool or script via Group Policy to ensure that the taskbar is consistently configured for all users.

Best regards

Qiuyang
