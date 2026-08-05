---
title: "HyperV Guest OS cannot contact domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195072/hyperv-guest-os-cannot-contact-domain-controller
question_id: 2195072
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-server-high-availability-virtualization-hyper-v"]
---
# HyperV Guest OS cannot contact domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195072/hyperv-guest-os-cannot-contact-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The Guest OS is getting the right TCP/IP settings from the DHCP server, including the correct DNS settings.

The problem is that all guest OS are unable to contact the domain controller. It is not a firewall issue and it is only happening on VMs not physical machines.

I have recreated the virtual switch to no avail.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-13*

Hi,

Do all these virtual machines use the same virtual switch? You can check this in the virtual machine settings. If yes, make sure the type of the virtual switch is external and it connects to the correct physical network adapter. Also see if there are other external virtual switches and Hyper-V virtual ethernet adapters on the host.

Best Regards,

Ian Xue
