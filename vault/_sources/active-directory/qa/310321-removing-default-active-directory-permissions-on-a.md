---
title: "Removing Default Active Directory Permissions on an OU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310321/removing-default-active-directory-permissions-on-a
question_id: 310321
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Removing Default Active Directory Permissions on an OU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310321/removing-default-active-directory-permissions-on-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a specific security requirement for a single OU. The requirement is to remove Authenticated Users read access to all objects under the OU and grant a specific group read access to the OU. I created the OU, disabled Inheritance, removed Authenticated Users from the OU and delegated read access to the specific group.  When a new AD object is created under the OU it gets the inherited permissions of the specific group. However the new AD object creation explicitly adds the default Authenticated Users permissions to the newly created AD object.    

Is there a way to keep new AD objects from getting the default AD permissions for only objects created under the OU?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

That is what I was seeing with my testing as well.  I did discover a couple of ways to handle this scenario.  One of which we will not do.  

-  Edit the Schema so that no new AD Objects get Authenticated Users.    

-  Manually remove Authenticated Users from the AD Object at time of creation.  

-  Write a script that runs on a scheduled task that removes Authenticated Users from all AD Objects in that OU
