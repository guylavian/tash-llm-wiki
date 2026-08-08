---
title: "Does GPO \"Delete User Profiles Older Than X Days\" Remove Local Administrator Profile?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2156386/does-gpo-delete-user-profiles-older-than-x-days-re
question_id: 2156386
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Does GPO "Delete User Profiles Older Than X Days" Remove Local Administrator Profile?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2156386/does-gpo-delete-user-profiles-older-than-x-days-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am using the Group Policy setting "Automatically delete user profiles older than a specified number of days on system restart" to clean up old user profiles on our Windows systems.

I would like to confirm:

-  Does this policy delete the Local Administrator profile (`C:\Users\Administrator`) if it hasn’t been used within the specified days?

-  Are there any default exclusions for system profiles such as Default Profile or Public?

-  What are the possible impacts of enabling this policy?

-  Does it affect service accounts running under a local user profile?

-  Could it impact cached domain credentials for offline logins?

-  Any profile that is being used as a service account will that we deleted?

Thanks in Advance

## Answers

_No answers on this thread._
