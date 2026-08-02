---
title: "Exchange Server is not working when the DC is off"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1083835/exchange-server-is-not-working-when-the-dc-is-off
question_id: 1083835
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Server is not working when the DC is off

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1083835/exchange-server-is-not-working-when-the-dc-is-off (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!    

There're two DCs (DC and DC2) in a single site and two Exchange Servers 2019 - Exch1 and Exch2.    

Initially DC was the PDC and I recently transfered all FSMO to DC2.    

The problem: when DC is down Exch2 is not functioning:    

    

Exch1 does work and is using DC2 as expected:    

    

Seems Exch2 "wants" to talk to only the former pdc - DC, but Get-ExchangeServer  ... EXCH2 command shows DC2 in the Originating DC field:    

    

There're no events 2080 in the log as described here (at least in the Application and System logs).    

Why does Exch2 can't "see" the new PDC server (DC2, GC)?    

Thank you in advance,    

Michael

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-11*

Hello,    

Thank you very much for your replies!    

"is that DC is hard-coded to Exch 2" - no:    

    

"By default, Exchange attempts to connect to a DC that is available on the same site." - agree!    

...I must apologize for the question... I was so sure my dns settings for BOTH Exchange servers contained IPs of BOTH domain controllers that I couldn't even had imagined Exch2 was missing the second DC's address :(    

"please make sure the Exchange server itself is using DC2 IP for DNS (ipconfig /all)" - that's it!    

    

Thank you all once again for your help!    

Regards,    

Michael

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-11*

Hi @Mikhail Firsov  ,    

By default, Exchange attempts to connect to a DC that is available on the same site.    

Did you hardcode Exch2 to a specific DC? You can check the static domain controller with the following command:    

```
Get-ExchangeServer -identity  -status | fl *static*
```

If you specify the static value, you can use Set-ExchangeServer to set it as the default.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
