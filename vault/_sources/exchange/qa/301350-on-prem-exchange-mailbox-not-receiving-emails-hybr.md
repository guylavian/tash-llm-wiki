---
title: "on-prem exchange mailbox not receiving emails - hybrid migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301350/on-prem-exchange-mailbox-not-receiving-emails-hybr
question_id: 301350
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# on-prem exchange mailbox not receiving emails - hybrid migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301350/on-prem-exchange-mailbox-not-receiving-emails-hybr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

when i send an email to an on-premise mailbox i get a bounceback .    

The following organization rejected your message: domain-ca.mail.protection.outlook.com.    

Generating server: .***.ca    

Administrator@keyman  .ca    

domain-ca.mail.protection.outlook.com    

Remote Server returned '554 5.4.0 <domain-ca.mail.protection.outlook.com #5.4.14 smtp; 554 5.4.14 Hop count exceeded - possible mail loop ATTR34 [TO1CAN01FT011.eop-CAN01.prod.protection.outlook.com]>'    

If i migrate the mailbox to exchange online it works.     

i have run the hybrid configuration wizard    

on-prem exchange server is 2013    

MX records are pointing to Zero Spam (3rd party)    

Zero spam is configured to deliver to Office 365.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-08*

@dirkdigs  

>554 5.4.14 Hop count exceeded - possible mail loop

From this error, I think this issue is caused by wrong configuration on connector. Here is a related article, you could try to make the modify on Outbound connector that used to delivery email from Exchange online to Exchange on-premises:  

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-03-05*

Hi, what steps have you followed to setup the hybrid ? these https://learn.microsoft.com/en-us/exchange/hybrid-deployment/deploy-hybrid ?
