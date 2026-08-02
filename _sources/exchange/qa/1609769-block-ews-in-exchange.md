---
title: "Block EWS In Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1609769/block-ews-in-exchange
question_id: 1609769
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Block EWS In Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1609769/block-ews-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are using Exchange 2019 I want to block EWS for external users, how we can do that?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2024-03-06*

You cant really do that unless you perhaps set allowd IPs on the EWS virtual directory or use a load balancer / reverse proxy that allows you to target the EWS directory.

Note that 

https://learn.microsoft.com/en-us/exchange/architecture/client-access/load-balancing?view=exchserver-2019

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-03-06*

You can use this as a guide and set on the EWS virtual directory instead:https://blog.expta.com/2018/10/how-to-block-external-access-to.html

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-07*

@Nandan NK  

To block external access to Exchange Web Services (EWS) in Exchange Server 2019, you can use the Set-OrganizationConfig cmdlet in the Exchange Management Shell. Here are the steps: 

-  Open the Exchange Management Shell. 

-  Run the following command: Set-OrganizationConfig -EwsAllowList @{Add="InternalIPorFQDN"} -EwsBlockList @{Add="*"} Replace "InternalIPorFQDN" with the IP address or fully qualified domain name (FQDN) of your internal Exchange server. This will allow only internal users to access EWS and block all external access.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
