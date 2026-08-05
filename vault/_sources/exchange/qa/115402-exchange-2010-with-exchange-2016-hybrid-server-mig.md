---
title: "Exchange 2010 with Exchange 2016 Hybrid Server Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/115402/exchange-2010-with-exchange-2016-hybrid-server-mig
question_id: 115402
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange 2010 with Exchange 2016 Hybrid Server Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/115402/exchange-2010-with-exchange-2016-hybrid-server-mig (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

Is it possible to use an Exchange 2016 Hybrid server to do an exchange 2010 migration without having to use the HCW?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-05*

Follow up question. Can you migrate linked mailboxes to Office 365 or do they have to be converted to users mailboxes?

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-05*

@KashifRashid-5415     

Do you mean Exchange 2010 coexists with Exchange 2016 for your on-premises organization?    

Agree with AndyDavid. You have to run HCW on Exchange 2016, so that it will be the hybrid server. Then you can migrate on-premises mailboxes to Exchange Online.     

You can check these articles for more information about hybrid deployment:    

Hybrid deployment prerequisites,    

Hybrid Configuration wizard.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-10-02*

You can't migrate without running HCW.    

Please refer complete guidance,    

https://learn.microsoft.com/en-us/exchange/exchange-hybrid
