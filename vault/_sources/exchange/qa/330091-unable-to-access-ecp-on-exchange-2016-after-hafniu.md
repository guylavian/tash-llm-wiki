---
title: "Unable to access ECP on Exchange 2016 after Hafnium updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/330091/unable-to-access-ecp-on-exchange-2016-after-hafniu
question_id: 330091
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Unable to access ECP on Exchange 2016 after Hafnium updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/330091/unable-to-access-ecp-on-exchange-2016-after-hafniu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After installing the various Hafnium updates I am no longer able to access ECP (HTTP Error 503) of Exchange 2016. I've reset the SSL certificate, changed the SSL certificate and removed and re-added the ECP folder via PowerShell. Nothing helps or seems to make any difference. OWA works fine.

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2021-03-24*

Turns out the MSExchangeECPAppPool had been stopped after the update and even after a reboot. Should have checked that earlier, but assumed it would be started after a reboot.
