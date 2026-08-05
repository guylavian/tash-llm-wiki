---
title: "Export/import 2019 Domain Controller onto new host?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167668/export-import-2019-domain-controller-onto-new-host
question_id: 1167668
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-high-availability-virtualization-hyper-v"]
---
# Export/import 2019 Domain Controller onto new host?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167668/export-import-2019-domain-controller-onto-new-host (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a virtualized Server 2019 DC that I’d like to move to a new HV host as the old host is aging at this point and has a really high uptime. The 2019 VM is running fine and DCDIAG comes back clean so instead of spinning up a new VM and migrating the roles over, it would be much faster to power it down, export it over to the new host, and import it. Live migration isn’t an option as the new host is not joined to the domain. I’ve done this before with other VM’s but none were DC’s.

If it powers up successfully after the import, it will live there and the old copy of it won’t be turned back on. The only thing I’m concerned with is the do not export a DC but I’ve read a bunch of posts where people say it’s worked fine, just don’t run the old copy after which is obvious.

Virtualizing Domain Controllers using Hyper-V | Microsoft Learn

·        Do not use the Hyper-V Export feature to export a virtual machine that is running a domain controller.

·        With Windows Server 2012 and newer, an export and import of a Domain Controller virtual guest is handled like a non-authoritative restore as it detects a change of the Generation ID and it is not configured for cloning.

·        Ensure you are not using the guest that you exported anymore.

·        You may use Hyper-V Replication to keep a second inactive copy of a Domain Controller. If you start the replicated image, you also need to perform proper cleanup, for the same reason as not using the source after exporting a DC guest image.

The only downtime would be the time it takes to copy off to the new host. Am I ok proceeding here? There is another 2012 R2 DC running FYI.

## Answers

_No answers on this thread._
