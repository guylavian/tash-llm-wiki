---
title: "Can I move a Domain Controller VM from one Hyper V host to another?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196543/can-i-move-a-domain-controller-vm-from-one-hyper-v
question_id: 2196543
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-high-availability-virtualization-hyper-v"]
---
# Can I move a Domain Controller VM from one Hyper V host to another?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196543/can-i-move-a-domain-controller-vm-from-one-hyper-v (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

Good afternoon! Hope you are all doing well.

I would like to migrate a vm, which is a domain controller, from one Windows Hyper-V host to another host. We do not use SAN or shared storage. The VM files are located on one local disk on the host. Can I use the "Move" feature (instead of import and export features) in Hyper-V to migrate the vm from one host to another host?

Also, is it a good practice to move one domain controller like this way? We do not have replication on the DCs by the way.  We have two domain controllers by the way.

The reason I would like to migrate the vm because it seems to have some hardware issue with the physical host and it is not running stable. Would you provide some advise on what i should do?

Thank you for your help in advance.

Takami Chiro

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-02*

Hi Takami Chiro,

Thank you for your reply. The live migration feature in Hyper-V can be implemented without relying on a failover cluster and allows running virtual machines to be migrated between hosts without causing downtime. In theory, it will not affect domain-added machines, but for safety reasons, it is recommended that you first execute this feature in a test environment and only migrate the VM if there are no problems after the test.

Best regards

Zunhui

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-30*

HI Zunhui,

Thank you for your response! I just want to ask another quick question. This will work with another HyperV host without being in the cluster (which we do not have a cluster). Also, would it be any problem if I migrate a domain conroller?

I will keep digging no matter what. Thank you again!

Takami Chiro

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-30*

Hello,

I recommend that you use the live migration feature of Hyper-V. Live migration allows you to migrate a running virtual machine from one host to another without downtime to minimize the impact on the service. I recommend you refer to the following link:

Live Migration Overview | Microsoft Learn

I hope the above information is helpful.

Best regards

Zunhui
