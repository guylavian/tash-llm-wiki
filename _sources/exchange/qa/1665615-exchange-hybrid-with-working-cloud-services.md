---
title: "Exchange hybrid with working cloud services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1665615/exchange-hybrid-with-working-cloud-services
question_id: 1665615
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "office-teams-teams-business-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Exchange hybrid with working cloud services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1665615/exchange-hybrid-with-working-cloud-services (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We consider to move from Exchange on premise to hybrid deployment.

We also using Teams and soon we plan use Dynamic 365 so we have some AzureAD (EntraID) accounts.

Many accounts from our local AD are "duplicated" (the same email, first, last name, account name, ...) with AzureAD.

Local AD and AzureAD are never synced but they have the same domain.

I have doubts about what will happen with these accounts after synchronizing local AD with AzureAD. I worry users will lost access to Teams (and D365) or their chats and/or planed meetings on Teams after synchronization.

I also would know is there way-back after go to Hybrid Exchange? Can we stop syncing with AzureAD, change back MX records to on-prem Exchange, remove O365 connectors from Exchange on-prem server and serving mail services as before move to hybrid?

In migration wizard we can choose SSL certificate used to communicate with Exchange Online. Our SSL cert for Exchange on premise expires soon. We plan to obtain new one instead renew existing. Is it possible to change cert used to communicate with Exchange Online after migration to hybrid?

Can Exchange Online in Hybrid deployment act as "proxy" for on premise ActiveSync, EWS, OWA and we can disable wide access to these services from public network?

Has anyone had a similar situation and would be able to solve my doubts?

Regards

Mariusz

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2024-05-13*

Hello

Your main challenge is to avoid duplicity of users when configuring Entra ID Connect, to solve this I recommend you to run the ID Fix Tool (https://microsoft.github.io/idfix/). 

When you do a hybrid configuration the emails will not go out or in through Exchange online automatically, as you migrate users they will be able to connect to their mailbox through Office365, unfortunately, office.com will not work as a proxy.

Hope this helps!

Remember to accept the answer if it is helpful.
