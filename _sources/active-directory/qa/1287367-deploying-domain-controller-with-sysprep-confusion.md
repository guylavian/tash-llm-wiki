---
title: "Deploying domain controller with Sysprep confusion"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1287367/deploying-domain-controller-with-sysprep-confusion
question_id: 1287367
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Deploying domain controller with Sysprep confusion

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1287367/deploying-domain-controller-with-sysprep-confusion (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In this document https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controllers-hyper-v

In section "Virtualization deployment practices to avoid", point 3 says:

Do NOT deploy new Active Directory domains and forests on a copy of a Windows Server operating system that was NOT first prepared using System Preparation tool (Sysprep)

This is followed by a warning which says:

Running Sysprep on a domain controller is not supported.

The double negative in the first quote seems to imply that using Sysprep is acceptable whereas the warning indicates that it is not. 

Can someone please clarify?

## Answer (community) — Microsoft Moderator

*upvotes: 2 · updated: 2023-05-20*

Hi @Ingrid Henkel •

`Do NOT deploy new Active Directory domains and forests on a copy of a Windows Server operating system that was NOT first prepared using System Preparation tool (Sysprep)`

If you want to deploy new domain controller on virtual machine based on a copy of another virtual machine ( WORKGROUP), you have to launch sysprep before joining it to domain and promote it as domain controllers. Sysprep must be launched before DCpromotion.

`Running Sysprep on a domain controller is not supported.`  

 This command is used to create new virtual machines based on reference machine which cannot be a domain controller. 

Please don't forget o mark helpful answer as accepted
