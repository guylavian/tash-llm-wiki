---
title: "Show AD objects type \"Contact\" in Exchange GAL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/296800/show-ad-objects-type-contact-in-exchange-gal
question_id: 296800
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Show AD objects type "Contact" in Exchange GAL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/296800/show-ad-objects-type-contact-in-exchange-gal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I'm looking for showing "Contact" AD object type in our Exchange GAL.  

How could I proceed please ?  

Thank you.  

Regards,

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-03*

Hi @FXE   ,    

You have to mail enable them with external email address to be added in GAL. You can do this using Exchange Admin Center or shell.    

https://learn.microsoft.com/en-us/powershell/module/exchange/enable-mailcontact?view=exchange-ps    

https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-mail-contacts    

If the above suggestion helps, please click on "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-03*

Hi AshokM-8240 and thank you for your answer.  

If I understand, for a contact to be shown in GAL, it must have an email address ?  

In our case, we need to publish a contact with phone number only. Is it possible ?  

Thank you.  

Regards,
