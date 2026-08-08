---
title: "exchange ndr"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/132388/exchange-ndr
question_id: 132388
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# exchange ndr

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/132388/exchange-ndr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,    

i am experiencing this error with a newly created user:    

 Generating server: exchange.domain.com    

IMCEAEX-_o=Be+20Bank_ou=Exchange+20Administrative+20Group+20+28FYDIBOHF23SPDLT+29_cn=Recipients_cn=dc4ccc17a1604f8a97cb21c04fd622a9-Dona+20ea@keyman  .com    

Remote Server returned '550 5.1.11 RESOLVER.ADR.ExRecipNotFound; Recipient not found by Exchange Legacy encapsulated email address lookup'    

can you please advise    

thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-20*

Hi,    

Please try to send email from OWA and check if its working fine. If it works, then the issue is with the outlook cache, refer the below article    

https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/exrecipnotfound-ndr    

If it happens in any client, then check the legacyexchangeDN and update the same,    

https://www.msnoob.com/recipient-not-found-by-exchange-legacy-encapsulated-email-address-lookup.html    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the above suggestion helps, click on "Accept Answer" and upvote it.
