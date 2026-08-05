---
title: "Can Windows Server 2019 domain controllers be clustered?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/309175/can-windows-server-2019-domain-controllers-be-clus
question_id: 309175
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-high-availability-clustering-high-availability"]
---
# Can Windows Server 2019 domain controllers be clustered?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/309175/can-windows-server-2019-domain-controllers-be-clus (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of my domain controllers has network share that itself is an iSCSI mount. I'd like to improve its availability by turning it into a clustered shared volume by grouping all similar servers, i.e; domain controllers, into a cluster.  

There's always a gotcha somewhere using technologies like these in Windows Server though; it just barely stopped being frowned upon to virtualize domain controllers the past major, and, I've been unable so far to find specific mention in the docs that I can or cannot do this.  

Just to elaborate a little more: I don't need to cluster the current services each domain controller runs except for this one share. The [Kerberos-enabled-]Windows Admin Center had problem even finding the servers despite being able to SSO to them otherwise, that's already not a great start. ...also, they run on vSphere, not Hyper-V. There's an baremental "disaster DC" but it can always be left out if it's too mismatched.  

Can DCs be safely clustered?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hey,  

It is recommended to have domain controllers running outside of a cluster, even when virtualized. I would recommend you deploying multiple domain controllers as VMs on top of your hypervisors and configure proper backups. Might help:  

https://www.starwindsoftware.com/resource-library/useful-tips-for-setting-up-microsoft-active-directory-domain-controllers/  

Cheers,  

Alex Bykovskyi  

StarWind Software  

Note: Posts are provided “AS IS” without warranty of any kind, either expressed or implied, including but not limited to the implied warranties of merchantability and/or fitness for a particular purpose.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi,

It's not supported to install windows failover cluster feature on DC. Please check the following article for detailed information. We see few cases that people would like to install failover cluster feature on DC:

https://learn.microsoft.com/en-us/troubleshoot/windows-server/high-availability/use-cluster-nodes-as-domain-controllers

Thanks for your time!  

Best Regards,  

Anne

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
