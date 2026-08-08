---
title: "SCCM Client on a Azure domain controller server VM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/896942/sccm-client-on-a-azure-domain-controller-server-vm
question_id: 896942
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# SCCM Client on a Azure domain controller server VM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/896942/sccm-client-on-a-azure-domain-controller-server-vm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Just confirming if an Azure domain controller server can be managed with on-prem sccm server by installing the client agent.    

We have a SCCM Primary site on-prem server and is integrated to CMG service in Azure. Is there any additional connectivity required to install SCCM client agent on the Azure VM to manage it with the on-prem SCCM site server?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2022-06-21*

ConfigMgr can manage supported Windows instance. Whether that instance is a VM or physical system or where that instance is hosted is irrelevant as long as the necessary connectivity between the client facing site roles (MP, DP, SUP) and the client exists. Thus, there's nothing special about what you've described from the perspective  of "can" it be managed although only you or your org can validate the necessary connectivity as this is dependent on your networking configuration.    

Whether you "should" is another  matter here but based on the info you've given, yes you can do this and ConfigMgr does support it (assuming the OS is supported of course).
