---
title: "Azure/Entra and Exchange online sync issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2117531/azure-entra-and-exchange-online-sync-issues
question_id: 2117531
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Azure/Entra and Exchange online sync issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2117531/azure-entra-and-exchange-online-sync-issues (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have modify SMPT address on on-premises on AD and running sync but the changes are not replicating in exchange online. 

Whiles the changes are reflecting in entra portal, it seems there is some issue with exchange online. I have run Delta sync and still facing this issue, any idea whiles this changes not syncing properly?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-11*

Hi,@Nana Poku

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, the on-premises AD can be synchronized to Entra, which means the on-premises AD connector is intact, but there is a problem synchronizing Entra to Exchange Online.

The forums can't solve the backend problem at the moment.It is recommended that you open an SR at the M365 center.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
