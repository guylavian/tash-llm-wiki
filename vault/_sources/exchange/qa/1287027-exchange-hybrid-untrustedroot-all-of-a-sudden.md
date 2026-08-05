---
title: "Exchange Hybrid - UntrustedRoot all of a sudden"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1287027/exchange-hybrid-untrustedroot-all-of-a-sudden
question_id: 1287027
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Hybrid - UntrustedRoot all of a sudden

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1287027/exchange-hybrid-untrustedroot-all-of-a-sudden (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

All of a sudden, mail flow from on-prem to Exchange Online stopped.

The connector shows a "450 4.4.317 Cannot connect to remote server [Message=UntrustedRoot]" error.

It seems that the TLS certificate is not being recognized as trusted from Exchange Online.

However, my public cert is valid and from a CA validated by MS. 

Any idea about troubleshooting this? Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-03-28*

If there is a mail filter /anti spam gateway device is in between Exchange online and your onprem exchange, You should verify TLS is enabled on the default frontend receive connector. Verify if exchange server is having a valid certificate, also verify if you are seeing show STARTTLS when connected on smtp port 25 using telnet .

Upload the certificate on the middle device and enable tls on that device as well.

Finally even if that is failling for some reason whitelist microsoft exchange online network showing port 25  in below link on antispam gateway.

https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide
