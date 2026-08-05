---
title: "Can you virtualize all domain controllers in your organization?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1665787/can-you-virtualize-all-domain-controllers-in-your
question_id: 1665787
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Can you virtualize all domain controllers in your organization?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1665787/can-you-virtualize-all-domain-controllers-in-your (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can you have all of your domain controllers in your environment virtualized. Once upon a time I recall it was recommended at least 1 DC be physical, is that still the case or has Azure changed how that works?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-19*

Yes, moreover, it is recommended nowadays. 

An important aspect here is that your virtualized DCs have to run on top of independent hypervisors, clusters, or premises to prevent everything from going down at the same time. That is usually done by having a dedicated standalone hypervisor host that, in addition to running your DC virtual machine, may also host some replicas for DR purposes or having one DC running in the public cloud. Some people recommend using a host with a different hypervisor if you have a homogenous infrastructure that is managed centrally. You may use ESXi or Proxmox to avoid any issues from the Hyper-V environment impacting your last DC as well. To migrate VMs between different hypervisors, you can use free 3rd party tools like V2V Converter https://www.starwindsoftware.com/starwind-v2v-converter.
