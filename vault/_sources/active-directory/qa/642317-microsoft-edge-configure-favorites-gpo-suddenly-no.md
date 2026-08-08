---
title: "Microsoft Edge Configure favorites GPO suddenly not working anymore"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/642317/microsoft-edge-configure-favorites-gpo-suddenly-no
question_id: 642317
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-edge-edge-development", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Microsoft Edge Configure favorites GPO suddenly not working anymore

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/642317/microsoft-edge-configure-favorites-gpo-suddenly-no (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  

I've set up some managed favorites last week, by exporting them from Edge, and it has been working fine up until now.  

Today, the Folder suddenly disappeared from the Favorites Bar in edge, and checking the ManagedFavorites REG_SZ in the registry under \HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\ , it turns up empty.   

I haven't changed anything about this GPO since it has been working. I also verified through gpresult that the GPO is being applied.   

Client OS is Windows 10 1809  

Domain Controller OS is Server 2019 1809  

Any ideas?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-26*

Try running a rsop.msc from the client machine and check if the policy settings for that GPO are showing up.  

Regards,  

Eduardo R.
