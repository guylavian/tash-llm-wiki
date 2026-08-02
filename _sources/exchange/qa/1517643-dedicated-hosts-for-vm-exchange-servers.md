---
title: "Dedicated Hosts for VM Exchange Servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1517643/dedicated-hosts-for-vm-exchange-servers
question_id: 1517643
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Dedicated Hosts for VM Exchange Servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1517643/dedicated-hosts-for-vm-exchange-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our 2013 exchange servers were VMs. The VMs were on their own hosts. No other VMs were on the hosts. We no longer have the 2013 servers. We have two 2019 hybrid exchange VMs.  One of the Exchange VM is the on a host with no other VMs. The other VM is on a host with 15 or more VMs.  Should the exchange VMs be on a dedicated host? Thanks.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-01-30*

"We have two 2019 hybrid exchange VMs"
So all they do is handle the hybrid connection and Exch Mgmt? I would put each guest on seperate VMhosts and you can share among other guests. It would be fine, those hybrid servers are very low usage.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-30*

Hi @mara2021  ,  

Welcome to post our Q&A forum!  

Based on the information you provided, it is recommended to have dedicated hosts for your Exchange VMs. This is because Exchange Server is a resource-intensive application and requires a significant amount of resources to operate efficiently.  

When Exchange VMs are hosted on a shared host, they may experience performance issues due to resource contention with other VMs on the same host.  

Microsoft recommends that Exchange VMs be deployed on dedicated hosts to ensure that they have access to the necessary resources and to avoid resource contention with other VMs.   

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/virtualization?view=exchserver-2019

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
