---
title: "exchange server and defender for o365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1304027/exchange-server-and-defender-for-o365
question_id: 1304027
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange server and defender for o365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1304027/exchange-server-and-defender-for-o365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi team,

need your advise on the below

i have an exchange server and i want to integrate defender for o365 with it. No need for hybrid, my mailboxes will stay on exchange server, and I just need to leverage O365 protection.

-  can i use defender for o365 to achieve that? if yes, safe links, attachments will apply?

-  if yes, what are the prerequisites needed? (azure ad connect, connectors, MX...)

thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-14*

so to recap team, can I just use defender for o365 to protect my onpremises mailboxes as it already includes EOP? or should I assign both licenses to the users, EOP and defender for O365?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-13*

Hi @eg1995  

`1.can i use defender for o365 to achieve that? if yes, safe links, attachments will apply?`

Yes, they can work together. Microsoft Defender for Office 365 contain additional features that give more layers of security, control, and investigation. 

Safe links policy and Attachments settings please refer to: Microsoft recommendations for EOP and Defender for Office 365 security settings | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-12*

Hi,

Yes Defender for Office 365 is designed to do this. In majority of scenarios (on-premise, Cloud, Hybrid, and any other SMTP solution).

The only technical perquisite is to register MX record points to Exchange Online Protection (EOP)

See Here

https://learn.microsoft.com/en-us/exchange/transport-routing

For features and licencing, check here (example: Safe Documents is available only in A5/E5/F5/G5 Security licences)

https://learn.microsoft.com/en-us/office365/servicedescriptions/office-365-advanced-threat-protection-service-description

I hope this helped.

If the answer is helpful, please click "Accept Answer" and kindly upvote it.
