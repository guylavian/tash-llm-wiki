---
title: "Migrate legacy Exchange server from Hypervisor to Azure VM in Hybrid environment."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1532509/migrate-legacy-exchange-server-from-hypervisor-to
question_id: 1532509
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator"]
---
# Migrate legacy Exchange server from Hypervisor to Azure VM in Hybrid environment.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1532509/migrate-legacy-exchange-server-from-hypervisor-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are a Hybrid Exchange and AD environment, with all of our mailboxes in Exchange Online. We have a single legacy Exchange server running on a Hypervisor VM. The server is an old Win 2012R2 and is on hardware that has reached EOL. The AD environment is synced to Azure AD using Azure AD Connect.  

Because of some other peripheral requirements, we are unable to fully migrate to the cloud and Azure AD, so we need to keep the legacy server going, but would like to move it onto an Azure VM. I'm assuming that the best method would be to create a new VM running Exchange, and then move the responsibilities for maintaining the hybrid environment from the old Exchange server to this new one.  

Is my thinking correct, and is there a good source of documentation and procedural checklist somewhere on how to make this move?  

Thanks in advance,  

John

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-15*

Hi @John R  ,

I'm assuming that the best method would be to create a new VM running Exchange, and then move the responsibilities for maintaining the hybrid environment from the old Exchange server to this new one.

Correct. From the perspective of Exchange side, agreed that the best way is to bring up a new VM running Exchange (and a new DC as well if necessary).

Currently seems that there's no official guidance of the whole procedure. Considering that all mailboxes are already in Exchange Online, the procedure could be simpler. Below are the basic steps for your reference:

-  Create the new server(s) in Azure VM and installing Exchange there. 

-  Configure coexistence by joining the Azure VM servers to your existing domain. 

-  Update the DNS records to point to the new Azure VM.

-  Rerun Hybrid Configuration Wizard (HCW) on VM Exchange to establish the hybrid connectivity between the new Exchange and Office 365. 

-  Decommission the old servers if desired.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
