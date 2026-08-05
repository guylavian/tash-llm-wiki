---
title: "[Migrated from MSDN Exchange Dev] Is it possible to delete current exchange hybrid with Azure?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/158553/migrated-from-msdn-exchange-dev-is-it-possible-to
question_id: 158553
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# [Migrated from MSDN Exchange Dev] Is it possible to delete current exchange hybrid with Azure?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/158553/migrated-from-msdn-exchange-dev-is-it-possible-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have created a exchange hybrid with my test lab exchange server using production tenant, I though multiple domain/forest to single tenant is easy, but my lab is not allowed to connect to prod domain.  

It is causing problem:  

-  The test lab will go away.  

-  I need to start hybrid exchange with the current Azure tenant.  

Is there a way to remove/delete/clean up the current exchange hybrid configuration on azure side?  

Source link: https://social.msdn.microsoft.com/Forums/office/en-US/2140e00d-fdc1-4599-a8ca-8d97845826dc/is-it-possible-to-delete-current-exchange-hybrid-with-azure?forum=exchangesvrdevelopment

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-11*

Take steps below to remove your lab from hybrid:  

-  Remove migration point from Exchange online.  

-  Remove hybrid receive/send connector from Exchange online and Exchange on-premises.  

-  Remove organization sharing from Exchange online and Exchange on-premises.  

-  Stop AD sync from local AD and remove AAD connector.  

-  Remove your lab domain from Office 365 "verified domain"  

Then create hybrid with your production domain.
