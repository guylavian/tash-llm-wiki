---
title: "Can a production Exchange 2019 Hybrid VM be deployed in Azure?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1080514/can-a-production-exchange-2019-hybrid-vm-be-deploy
question_id: 1080514
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Can a production Exchange 2019 Hybrid VM be deployed in Azure?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1080514/can-a-production-exchange-2019-hybrid-vm-be-deploy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can a production Exchange 2019 Hybrid VM be deployed in Azure? Currently we have an on-premise Exchange 2019 Hybrid VM server connected to EXO. We have created a new Exchange 2019 VM in Azure along with a domain controller in the same subscription and network. All is syncing with our on premise DCs and existing Exchange server. We are unable to connect the new Azure Exchange Server to M365 because port 25 is blocked. We do not want to run this on port 25 but rather 587. I cannot get a straight answer from Microsoft. Is this configuration officially supported by Microsoft?     

Additionally, can we modify the “Outbound to Office 365” Send Connector port from 25 to 587 on the Exchange server VM and connect our Exchange server to the Inbound O365 connector noted as “From: Your organization's email server To: Office 365” in the EXO admin panel.     

I see documentation that states if an organization has an Enterprise Agreement the EXO inbound connector can be modified to port 25 but comes with the caveat that other mail services may not accept our email. I see documentation to have a lab/dev Exchange server in Azure. We are not interested in this scenario. We simply want to have our on-premise production Exchange 2019 hybrid server hosted in Azure exactly as it is today in our facility. If using port 587 is the solution, please provide more specific details.    

We are not ready to go all EXO as we need our on-premise AD environment.

## Answers

_No answers on this thread._
