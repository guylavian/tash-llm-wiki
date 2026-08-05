---
title: "Active Directory - Groups"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1190281/active-directory-groups
question_id: 1190281
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory - Groups

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1190281/active-directory-groups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello friends

I'm creating a new group in AD (Global - Security). I am adding a user to this group. The problem is that the supposedly user is already in this group, but the rights resulting from membership in this group only after a few hours. That is, if I give permissions for this group to browse some directory. It is after adding a user to this group that I have to wait a few hours until the user can browse this directory. When there were only a few groups on the server, it worked quickly, but when I have 20-30 groups in AD, it works slower and slower.

The gpresult /r command on my computer tells me that my account is not yet in the group. In AD, I added my account to the group a few hours ago. I still have to wait.

Sorry for my english. Thank you in advance for your help.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-03-17*

I would recommend reviewing my guide - it will change the way how you look at groups and permissions. The original ideas are from Dan Holme, who used to be an MVP and now works for Microsoft.

https://www.ajtek.ca/guides/role-based-access-security/

Take 3 hours and watch the videos. The number of groups are not causing your issue. If a user is added or removed from a group, they must sign out and sign back in (to clear the Kerberos ticket as mentioned above) to have the new group membership take effect.
