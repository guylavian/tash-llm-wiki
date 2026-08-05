---
title: "Connecting Azure application to exchange email box?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1133242/connecting-azure-application-to-exchange-email-box
question_id: 1133242
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Connecting Azure application to exchange email box?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1133242/connecting-azure-application-to-exchange-email-box (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 5 applications that need to connect to exchange email boxes.  I get back oauth2 tokens and tokens display the correct roles with I check with https://www.jstoolset.com/jwt.    

I can connect fine with 2 mailboxes, the other 3 give me "Store.Connect failed with the error: AUTHENTICATE failed" from java application using MSAL.  I use exact same code.  How do check application has access to mailbox?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-19*

Did some set an application access policy in Exchange online?    

https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access    

You can test with :    

Exmple:    

    Test-ApplicationAccessPolicy -Identity "Engineering Staff" -AppID 3dbc2ae1-7198-45ed-9f9f-d86ba3ec35b5  

https://learn.microsoft.com/en-us/powershell/module/exchange/test-applicationaccesspolicy?view=exchange-ps
