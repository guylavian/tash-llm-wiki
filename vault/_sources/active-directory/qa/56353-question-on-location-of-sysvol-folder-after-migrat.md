---
title: "Question on location of SYSVOL folder after migration from FRS to DFS and 2008 to 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/56353/question-on-location-of-sysvol-folder-after-migrat
question_id: 56353
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Question on location of SYSVOL folder after migration from FRS to DFS and 2008 to 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/56353/question-on-location-of-sysvol-folder-after-migrat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

-   We recently demoted a Server 2003 DC in an environment running Server 2008 domain controllers.

-   We raised the functional level to 2008.

-   We then migrated from FRS to DFS, so we could add Domain Controllers running Server 2019.

After the migration, the SYSVOL location on the DC's running Server 2008 is C:\Windows\SYSVOL_DFSR\sysvol\  

The location of SYSVOL in the DC running Server 2019 is C:\Windows\SYSVOL\sysvol

Replication appears to be fine between the 2019 and 2008 domain controllers, and when I place a file in C:\Windows\SYSVOL\sysvol\<ourdomain.com>\scripts on the Server 2019 domain, it appears in C:\Windows\SYSVOL_DFSR\sysvol\<ourdomain.com>\scripts on the Server 2008 domain controllers.

Is this behavior to be expected?

-John

## Answers

_No answers on this thread._
