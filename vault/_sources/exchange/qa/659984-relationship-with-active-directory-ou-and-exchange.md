---
title: "relationship with active directory OU and exchange distribution list"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/659984/relationship-with-active-directory-ou-and-exchange
question_id: 659984
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# relationship with active directory OU and exchange distribution list

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/659984/relationship-with-active-directory-ou-and-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am new to this section(AD and exchange)  

Can anyone tell me how I can send a mail through a distributionlist to everyone under a OU(organisation unit) my envirnment exchange 2019.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-11*

thanks and well noted.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-11*

hi ManuPhilip, thanks for your reply but i want to add all user of particular OU to a Distribution list buy a script or whatever  it is.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-12-11*

You can't send an email to all users under the OU until you have a distribution list ready with all those users.    

If you don't have the distribution list ready, start it here from Exchange Admin Center    

    

-  Type Display name and alias of the group name. Under the Organization unit and click on browse    

-  Select the particular OU you are looking for    

-  Under Members click, so click the “+” icon    

-  Select user you want to add in the group so click add and click ok    

-  Select the necessary options as per your preference and click Save    

-  Select the Distribution group you just created and click on edit and select Delivery Management, to choose senders inside/outside organization clicks on save    

-  Login Outlook Web App > Select new mail and type Distribution group name you just created. Add necessary message, Subject line etc. and send email
