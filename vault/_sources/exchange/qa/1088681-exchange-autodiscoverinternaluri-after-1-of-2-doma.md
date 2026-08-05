---
title: "Exchange AutoDiscoverInternalURI after 1 of 2 domains migrates to MS365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1088681/exchange-autodiscoverinternaluri-after-1-of-2-doma
question_id: 1088681
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Exchange AutoDiscoverInternalURI after 1 of 2 domains migrates to MS365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1088681/exchange-autodiscoverinternaluri-after-1-of-2-doma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On-prem Exchange is authoritative for 2 domains. One domain is migrating to MS365 via Cutover Migration as documented here--    

https://learn.microsoft.com/en-us/exchange/mailbox-migration/cutover-migration-to-office-365    

The other will remain on-prem for another few months, then also move to MS365 the same way.    

The current AutoDiscoverInternalURI is--    

```
https://mail..com/autodiscover/autodiscover.xml
```

Outlook will continue to be used as the email client for both domains. Some users will use Outlook against the 365 domain, some against the on-prem domain, and all users will be on the LAN.    

The Cutover Migration article says to issue this command as a "Post-Migration" task--    

```
Set-ClientAccessServer -Identity  -AutoDiscoverServiceInternalUri $null
```

Trying to figure out if I really want to do this while we're half on-prem & half 365.    

What are the ramifications for the on-prem domain if I do this?    

What are the ramifications for the 365 domain if I don't?    

TIA

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-14*

Thanks @Andy David - MVP   for the quick answer!
