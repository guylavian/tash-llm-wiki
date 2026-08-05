---
title: "how to restrict exchange application permissions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/139188/how-to-restrict-exchange-application-permissions
question_id: 139188
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# how to restrict exchange application permissions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/139188/how-to-restrict-exchange-application-permissions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi,    

i'm creating automated solution for some reporting, that is to be run by 1st and 2nd line. quite recently there has been a new connect-exchangeonline feature allowing to connect with certificate, using EXO app registration    

https://www.quadrotech-it.com/blog/certificate-based-authentication-for-exchange-online-remote-powershell/    

it's basically great feature, and script can run with automated logon experience....    

the problem is that such connection has full admin permissions. i found information  on application restrictions, but issue there is that it is 'per mailbox' while i need to restrict access granting RO permissions to all mailboxes (for now and for future). so this policy is highly unsustainable.    

https://learn.microsoft.com/en-us/powershell/module/exchange/new-applicationaccesspolicy?view=exchange-ps    

to summarize: i want to write fully automated script that has RO access to EXO.    

-  is there a way to limit registered app permissions globally to RO?    

-  is there an option, so the application (app registered in AAD) run in a context of a particular user - so then i could create roles in EXO    

suggestions appreciated!

## Answers

_No answers on this thread._
