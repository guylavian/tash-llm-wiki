---
title: "Clone a domain controller in virtualized environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167256/clone-a-domain-controller-in-virtualized-environme
question_id: 1167256
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Clone a domain controller in virtualized environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167256/clone-a-domain-controller-in-virtualized-environme (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a single domain controller running server 2022 in a virtualized environment (vmware vsphere cluster / 2 ESXi servers - one primary, one backup)

We have the domain controller running on the primary ESXi server with no current issues. I wanted to make a backup copy of this domain controller virtual machine on the primary ESXi and transfer the backup copy to the backup ESXi server for safe keeping if we ever need to launch it because of a failure on the primary ESXi server.

My research of this topic indicates that there are some potential issues that could arise  if we ever launched the backup copy of the DC on the backup ESXi server).

Does anyone have experience with this scenario, and if so,  do you have any suggestions or helpful hints in regards to things to watch out for?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-03*

That's not a good plan really. The better plan is to always have at least two domain controllers for high availability and disaster mitigation. Just check the affinity is such that both DCs would not migrate to the same host.  If the primary fails for some reason, you can easily seize roles to other one with no downtime.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
