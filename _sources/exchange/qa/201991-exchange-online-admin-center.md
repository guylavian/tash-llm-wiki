---
title: "Exchange online admin center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/201991/exchange-online-admin-center
question_id: 201991
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Exchange online admin center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/201991/exchange-online-admin-center (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi team,  

 Is there any REST API's call to manage exchange online admin center like [ Creation,Modification,Deletion ] of usermailboxes,resources,group,contact,mail flow,etc..  

Regards,  

Siva

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-18*

@super admin       

Agree with michev. Based on my knowledge, it's not supported to use REST API for Exchange Online admin center currently.     

If you get useful information from the reply above, you can accept the helpful one. This may be useful to other community members. Thanks for your understanding.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-17*

could u share cmdlets to manage yammer using powershell?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-17*

There are, as you can easily see if you capture the network trace for any operation you perform in the new EAC. However, those are only supported internally currently, and Microsoft is yet to announce plans to roll them out publicly. So for the time being, the only supported method to manage objects programmatically is via PowerShell.
