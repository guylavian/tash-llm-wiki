---
title: "Exchange 2013 hybrid mail flow breaks if old domain controller (2008) is taken offline"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/320444/exchange-2013-hybrid-mail-flow-breaks-if-old-domai
question_id: 320444
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 hybrid mail flow breaks if old domain controller (2008) is taken offline

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/320444/exchange-2013-hybrid-mail-flow-breaks-if-old-domai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have exchange 2013 cu 23 with hybrid configuration, on-premises we have couple of mailbox servers and an edge server to route emails to office 365, we also use SMG to route emails to the internet. in AD we have 3 domain controllers one of them is 2008 which we want to decommission, but mail flow from on-premises to exchange online stops if that DC is taken offline. where can we start looking at the issue? any suggestions?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-18*

Ok, when you take the DC offline, does it affect all mail flow or just mail flow to 365? Which server are the messages queued on and what is the error in the queue and in the event logs?  

Nothing is hardcoded to that DC is it?  

```
Get-ExchangeServer |FL *static*
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-18*

@Andy David - MVP   this event doesn't show up on edge server, on mailbox servers it shows:    

dc1	CDG 1 7 7 1 0 1 1 7 1    

dc2	CDG 1 7 7 1 0 1 1 7 1    

dc3	CDG 1 7 7 1 0 1 1 7 1           

dc1 is the one we're trying to decommission
