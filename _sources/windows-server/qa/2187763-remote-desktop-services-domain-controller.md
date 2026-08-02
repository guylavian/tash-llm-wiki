---
title: "Remote Desktop Services - Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187763/remote-desktop-services-domain-controller
question_id: 2187763
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-licensing-and-activation-itpro-server"]
---
# Remote Desktop Services - Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187763/remote-desktop-services-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

As I know there is a limitation where you can't install remote desktop services on the domain controller.  

To get around this, I'm thinking of setting up Windows Hyper-V Virtual machine.  Is this the best approach and do I need another Windows Server license?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-20*

No, it is not recommended to install Remote Desktop Services on a Read Only Domain Controller (RODC). RODCs are designed to be used in locations where physical security cannot be guaranteed, and they have a limited set of features. It is recommended to install Remote Desktop Services on a separate server that is not a domain controller.

Best Regards,

Hania Lian

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-19*

Thanks for the response.  There are 2 sites.  One hosts the domain controller so I'll get a second server as a remote desktop server.

I have another site.  Can you install remote desktop services on a Read Only Domain Controller?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-20*

Hello Sin Ngo

Yes, you are correct that it is not recommended to install Remote Desktop Services on a domain controller. Setting up a Hyper-V virtual machine is a good approach to get around this limitation. You will need another Windows Server license to install the virtual machine. Each virtual machine requires a separate license, just like a physical machine.

Best Regards,

Hania Lian
