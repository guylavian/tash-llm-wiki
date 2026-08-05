---
title: "AADconnect & Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/408722/aadconnect-exchange
question_id: 408722
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# AADconnect & Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/408722/aadconnect-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi ,   

i have recently migrated a customer's exchange server to Exchange Online (minimal hybrid).   

Customer has mailflow to O365 directly. They ask now , what happens if the Exchange is uninstalled. Aadconnect is present.  

I know that you can administer the objects via attribute editor but i think that uninstalling the Exchange will also clear all proxy addresses ?   

kind regards,   

Filip

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-25*

Ok AndyDavid , thanks.   

Please don't tell me that you never had these questions from customers ?   

Or what do you do in that case - tell them it is not supported and migrate again the exchange server to a higher version (just to do management ? )

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-25*

Hi Andy , i know , i have read 1000's of fora about it and also the link you provided , but let's face it , it just works when administering through ADSIEDIT.  

Some settings are indeed a bit harder to set (like hide from GAL and so)   

Customer always needs to sign a document that it is not supported.  

But is the result not the same , if you uninstall an Exchange server , it will clear the mail field and the proxy addresses in AD ?   

I am worried because if that happens , i need to export all values and re-import them afterwards...
