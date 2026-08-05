---
title: "Active Directory Backup Stretegy for Domain Controller on Azure to prepare AD for Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/936338/active-directory-backup-stretegy-for-domain-contro
question_id: 936338
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Active Directory Backup Stretegy for Domain Controller on Azure to prepare AD for Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/936338/active-directory-backup-stretegy-for-domain-contro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My Customer has domain controllers in Azure and moved all exchange mailboxes to office365 but required to have one node on azure for exchange server, Customer is using Azure Backup to backup domain controllers on azure. I would like to prepare AD for exchange, can anyone advice on it.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-26*

Hello    

Thank you for your question and reaching out. I can understand you are  having query related  to Azure Domain controller backup.    

From the VM menu in Azure, select Backup from the Operations section. Under Recovery Services vault, select existing. Select the vault and backup policy created with the first Domain Controller and then select Enable Backup to complete.    

You can also run an additional DC in an Azure VM, linked via VPN to your on-premises AD.    

------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--
