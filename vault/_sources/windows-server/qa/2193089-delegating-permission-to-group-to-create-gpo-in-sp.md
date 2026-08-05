---
title: "Delegating permission to group to create GPO in specific OU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193089/delegating-permission-to-group-to-create-gpo-in-sp
question_id: 2193089
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Delegating permission to group to create GPO in specific OU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193089/delegating-permission-to-group-to-create-gpo-in-sp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to grant a specific group the rights to create GPO's in a single OU only. I have found references on the net to a a Create GPO right but I can't locate it anywhere.  If anybody has any insight as to what rights I need to grant this group in this OU I would appreciate it.

Thanks,

Jeff

## Answer (community) — community member

*upvotes: 3 · updated: 2024-09-11*

GPO's are not created in OU's. They are LINKED to OU's

Go to the Group Policy Objects folder in Group Policy Management, delegation tab. Add the group/user you want to be able to create GPO's

Go back to ADUC, Right-click the OU and choose Delegate Control of "Manage Group Policy links" for this group/user

## Answer (community) — community member

*upvotes: 1 · updated: 2024-06-06*

I have tried to follow these instructions without success. I cannot find such task to delegate "Create, delete, and manage Group Policy objects". I have looked under common tasks which does include group policy links management, but I see nothing to create, delete, and manage Group Policy objects

For step 2 i also do no see a "Create Group Policy objects" under "Permissions". I do see a "Create groupPolicyContainer objects" under "Permissions"

Please clarify these instructions as they do not seem to apply. I've tested this in both a windows 2012 DC and a 2019 DC

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-13*

GPO's are not created in OU's. They are LINKED to OU's

Go to the Group Policy Objects folder in Group Policy Management, delegation tab. Add the group/user you want to be able to create GPO's

Go back to ADUC, Right-click the OU and choose Delegate Control of "Manage Group Policy links" for this group/user

This makes more sense...however, in your first sentence you accurately stated that GPO's are LINKED to GPO's. 

I assume in your second statement, you meant to say that you add the group/user that you want to be able to LINK GPO's to the specific OU

Lastly, Do you happen to know exactly how to delegate permission to CREATE a GPO? I added a group to the delegation tab of the "Group Policy Objects" in Group Policy Management however, the users in this group claim the ability to create a new GPO is still not there.
