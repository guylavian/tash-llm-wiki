---
title: "sysvol is not shared but it is replicated"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/885424/sysvol-is-not-shared-but-it-is-replicated
question_id: 885424
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# sysvol is not shared but it is replicated

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/885424/sysvol-is-not-shared-but-it-is-replicated (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I promoted a new domain controller, but netlogon and sysvol were missing, I check this: ![210397-image.png][1] there is an event id 4604 indicating that replication has already started, I created a couple of GPOs an they were replicated between all three domain controllers, the rest of GPOs were also replicated, repadmin was not showwing any errors, I changed a SysvolReady registry, I perfomed a D2 restoration but still SYSVOL and netlogon were not shared on this DC. Can I just shared as a normal folder? [1]: /api/attachments/210397-image.png?platform=QnA

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-11*

I renamed the sysvol folder and I got this message     

If it were me I'd get rid of this one, then confirm the domain health is 100% before attempting to add another.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-11*

Hi again,    

I applied the steps you recommended, and I also checked: 4604 indicating that replication has already started, I created a couple of GPOs an they were replicated between all three domain controllers, I deleted the two GPOs created (no problem showed), the rest of GPOs were also replicated, repadmin was not showing any errors, SYSVOL and Netlogon folders were shared.    

Before promoting the DC again, I renamed the sysvol folder and I got this message just once: Local path of replicated folder SYSVOL Share does not match the newly configured local path.      

  Affected replicated folders: SYSVOL Share     

  Description: The DFS Replication service detected that the local path of a replicated folder C:\Windows\SYSVOLOLD\domain in its database does not match the newly configured local path C:\Windows\SYSVOL\domain of the replicated folder SYSVOL Share. The service will replicate the new path, and the old replicated folder path in the database will no longer be tracked as a replicated folder. Event ID: 6406     

I have been testing and I do not see any errors, can I monitor this behavior and maybe ignore the message since after this, the event ID 4604 appeared.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-11*

Might try demoting, reboot, promo it again.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
