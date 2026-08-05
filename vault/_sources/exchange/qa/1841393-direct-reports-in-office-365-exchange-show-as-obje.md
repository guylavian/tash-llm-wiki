---
title: "Direct Reports in Office 365 Exchange show as Object ID, Managers show as short name"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1841393/direct-reports-in-office-365-exchange-show-as-obje
question_id: 1841393
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Direct Reports in Office 365 Exchange show as Object ID, Managers show as short name

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1841393/direct-reports-in-office-365-exchange-show-as-obje (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What the title says.  I have some users, I go into office 365 exchange admin, setup their manager, then look at the manager in the organization tab, and the direct reports, and they show as object ID.  Also, some users, when I add the manager, enter the manager with the short name (aka fsmith, instead of Fred Smith) in the manager field.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-29*

Hi，@Scott P. Renton

I'm glad to hear back from you.

I ran a test based on the information you provided, and the results were exactly the same as yours.

After consulting the official documentation, I found that this is a deliberate strategy adopted by Microsoft to avoid some system conflicts.

You can refer to this link for details:https://techcommunity.microsoft.com/t5/exchange-team-blog/change-in-naming-convention-of-user-s-name-parameter/ba-p/3284733?WT.mc_id=M365-MVP-9501

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-26*

This is not affecting all users, only some

In Excahnge admin center, I go to Organization, I add a manager.  Manager shows as a short name, not the full name. Again, this is for certian users, not all.

FOr the manager, I go to Organization, manage organization information, and I get this

On the user site, I get this:

You can see the Manager name is NOT the full name, and the direct reports are incorrectly displayed

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-26*

Hi，@Scott P. Renton

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, I tried to restore the problem, but your problem did not occur. 

I added a manager to the user in the M365 center.

1.“they show as object ID”, can you provide a specific screenshot?

2.What does “aka fsmith, instead of Fred Smith” mean?
