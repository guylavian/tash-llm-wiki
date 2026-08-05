---
title: "Create a GPO printer for a specific security group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/378513/create-a-gpo-printer-for-a-specific-security-group
question_id: 378513
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Create a GPO printer for a specific security group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/378513/create-a-gpo-printer-for-a-specific-security-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need help in assigning a specific printer to a certain security group  

I've done all that is asked here, but still, the printer shows up for ALL users in the domain.  

http://woshub.com/deploy-printers-to-users-gpo/  

I've created the GPO, and implemented item-level targeting, but no luck so far :(  

If I select a specific security group in Scope, the printer doesn't show up at all.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-05-04*

NO LUCK  

I have Item targeting for SecGroup1, for the specific printer in the GPO.  

If I put Authenticated Users and SecGroup1 in Scope, I get the printer for all authenticated users, regardless.  

If I delete Authenticated users and leave just SecGroup1 - i get nothing - no printer for the SecGroup1  

Any other suggestions?!?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-07*

Thank you - the problem seems to be solved.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-30*

Hi,    

You can add this group in GPO Security filtering on  settings:    

    

Please don't forget to mark helpful reply as answer
