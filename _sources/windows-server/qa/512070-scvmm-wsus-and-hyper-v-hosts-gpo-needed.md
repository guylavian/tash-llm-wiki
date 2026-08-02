---
title: "SCVMM WSUS and Hyper-V Hosts (GPO needed?)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/512070/scvmm-wsus-and-hyper-v-hosts-gpo-needed
question_id: 512070
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["msc-virtual-machine-manager", "windows-business-windows-client-it-pros-high-availability-virtualization-hyper-v", "windows-business-windows-server-user-experience-user-experience-other"]
---
# SCVMM WSUS and Hyper-V Hosts (GPO needed?)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/512070/scvmm-wsus-and-hyper-v-hosts-gpo-needed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a S2D cluster with 3 hosts that were setup to receive updates directly from Microsoft and use CAU to install updates on a schedule.  

I've now added VMM to the environment to help manage the VMs. I also installed WSUS on another server for compliance monitoring. I assigned the Hyper-V hosts in VMM and compliance checking works fine.  

If I want the hosts to get updates from the WSUS server instead of MS Update do I still need to use a GPO to point the host's update source to use the intranet WSUS server?

## Answers

_No answers on this thread._
