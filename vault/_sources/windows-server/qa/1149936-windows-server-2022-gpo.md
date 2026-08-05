---
title: "Windows Server 2022 GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1149936/windows-server-2022-gpo
question_id: 1149936
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows Server 2022 GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1149936/windows-server-2022-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI, I'm trying to apply a GPO for OU called:"gg". In this "gg" i have a group with users:"a1".    

    

In this group i have 2 users: test1 and test2.    

    

I applied a GPO where i block a registry.    

When i link a gpo for this "gg" and run gpupdate /force on both machines it doesn't apply for "a1". If i add a user to OU it works for him. I also tried a turorials from YT where authors delete authenticated users and add group instead of them but it didn't work either.     

Please help me to solve this problem    

Best Regards     

Kamil

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-10*

Hello @Kamil Buszmann  ,

Thank you for posting in our Q&A forum.

As you mentioned, if you put user account in the OU named "gg", the user will apply the GPO setting.

We must put user accounts or computer accounts in the OU, then if link the GPO to OU, user settings within GPO (if you configured) will apply to the users in the OU, computer settings within GPO (if you configured) will apply to the computers in the OU.

Because the GPO settings have two parts, one part is user configuration, the other part is computer configuration.

GPO setting will not apply to group objects within the OU or other containers.

Hope the information above is helpful. If you have any question or concern, please feel free to let us know.

Best Regards,
Daisy Zhou

===============================================
If the Answer is helpful, please click "Accept Answer" and upvote it.
