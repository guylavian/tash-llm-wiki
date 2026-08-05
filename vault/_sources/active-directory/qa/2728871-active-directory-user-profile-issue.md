---
title: "Active Directory User Profile Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2728871/active-directory-user-profile-issue
question_id: 2728871
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active Directory User Profile Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2728871/active-directory-user-profile-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a weird issue.  I am using two remote desktop server on Server 2012 R2 with roaming profiles.  If I create a new user profile in active directory all works fine.  I had a situation where  I had to delete a user profile for cause of termination.  They
 were rehired 3 days later.  I created a new profile with the same user name as before.  Now when the user logs in they are logged into a temporary profile.  There are no .bak's in the profile lists on with rds server.  The event files give me an event ID of
 1521 Windows cannot locate the server copy of your roaming profile and is attempting to log you on with your local profile. Changes to the profile will not be copied to the server when you log off. This error may be caused by network problems or insufficient
 security rights.   

 DETAIL - Access is denied.  

and 1511 Windows cannot find the local profile and is logging you on with a temporary profile. Changes you make to this profile will be lost when you log off.

Thank in advance for any suggestions.

## Answers

_No answers on this thread._
