---
title: "Migrate exchange 2013 server to Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/259751/migrate-exchange-2013-server-to-azure
question_id: 259751
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Migrate exchange 2013 server to Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/259751/migrate-exchange-2013-server-to-azure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

Could you please advise high level steps to migrate exchange 2013 physical servers to Azure  

Each server has 8 LUN attached with one lun of 3TB each. Total 65 servers with multiple DAG

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-05*

@Ajit Terdalkar      

The migration from a physical computer to a VM is the same as the migration between physical computers. The main problem is to place the VM and the physical server in the same domain network.     

Here are some suggestion steps for you:    

-  Create multiple Windows server 2012 R2 computer in Azure VM(Used for new DC and new Exchange server), then add those computers to local AD domain(Detailed information about this step, you may need to check with "azure-virtual-machines-migration" team)    

-   Migrate local DC to Azure VM, it is same as do it within physical computer. You can have a look about this thread: Ways to seamlessly migrate an existing DC    

-  Create Exchange on VM computer coexist with physical Exchange, then migrate mailbox from local database to the database that hosted on VM Exchange. In this way, you complete the migrate Exchange. Manage on-premises mailbox moves in Exchange Server    

-  Create DAG with new Exchange server.    

-  Observe for a while, if there is no problem, you can uninstall the physical Exchange and the Windows server.    

Here are some articles may useful to you:    

-  Exchange Server supportability matrix (Exchange server deployment requirements)    

-  Exchange Server virtualization (Virtualization requirements)    

-  Exchange Server Role Requirements Calculator Update (Hardware requirements )    

Above are suggestions about Exchange. About network configuration and migrate DC, I would suggest you check with the related team, they will could provide more detail steps for you.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
