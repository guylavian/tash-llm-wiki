---
title: "GPO - Local Users and Groups - Item level targeting - Security Group - Removed from security group and local group but it keeps coming back"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193446/gpo-local-users-and-groups-item-level-targeting-se
question_id: 2193446
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# GPO - Local Users and Groups - Item level targeting - Security Group - Removed from security group and local group but it keeps coming back

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193446/gpo-local-users-and-groups-item-level-targeting-se (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a GPO that adds a security group to the local Administrators group using item-level targeting (another security group with servers). I remove the server in question from the item-level target group and manually remove the group from Administrators. When I do a gpupdate, it adds the group back. The GPO is set to update (action).

That server is no longer in the item-level targeting group. Why is it adding the group back during a gpupdate after it has been removed?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-21*

I am unable to select a User Group for an Item level targeting in a file update. This file update is in the User Section of policy.
