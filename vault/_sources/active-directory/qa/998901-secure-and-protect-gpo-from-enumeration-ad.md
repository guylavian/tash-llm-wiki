---
title: "Secure and protect GPO from enumeration (AD)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/998901/secure-and-protect-gpo-from-enumeration-ad
question_id: 998901
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# Secure and protect GPO from enumeration (AD)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/998901/secure-and-protect-gpo-from-enumeration-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,    

I'have a question, how can I protect the GPOs from enumeration from Tools like Bloodhound/PingCastle/PurpleKnight ....  ?    

how do you do, I'm working on a track to trap people who try to read GPOs that are not intended for them.    

it can be interesting to be able to detect these random reads on important GPOs, and it will help a lot of companies in terms of security    

Regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-08*

Hi,    

It depends if you are trying to stop users from reading both machine and user based GPOs.  For user based GPO it's a little more difficult as the user's account needs to be able to read the policies so they can be applied, you could make the allocation more specific rather than based the authenticated users group.  For machine based policies it's a little easier, if you remove the authenticated users read and apply gpo permissions and apply the permissions to a specific group that only contains machine accounts.  However, as machine group memberships are picked up on the next reboot, you just need to make sure you sequence the changes over a few days, so the machines still have access to read and apply the policies.    

Changing the authenticated users to a user or machine specific group will limit who can read the policy settings.    

    

Gary.
