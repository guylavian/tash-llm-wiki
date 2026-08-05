---
title: "Transferred FSMO roles from Windows 2008 server to Windows 2016 server but some roles didn't transfer how do I complete the transfer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/978850/transferred-fsmo-roles-from-windows-2008-server-to
question_id: 978850
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Transferred FSMO roles from Windows 2008 server to Windows 2016 server but some roles didn't transfer how do I complete the transfer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/978850/transferred-fsmo-roles-from-windows-2008-server-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,    

I performed a transfer of FSMO roles from my Windows server 2008 server to Windows server 2016 but when I looked at who controls the FSMO roles some are still on the old server and I wanted to know how would I go about completing the FSMO transfer.    

The RID is correct    

    

The PDC is incorrect do i just click the "CHANGE" button to move it to the correct server QI-FS-01.questinsurance.local ?    

    

The Infrastructure is correct:    

    

The Schema FSMO is correct:    

    

The Domain Naming FSMO holder is incorrect should be QI-FS-01.questinsuranceinc.local:    

    

When I click on "Change" I get this message so I am not sure what to do at this point.    

    

Any ideas or solutions are greatly appreciated.    

Thank You

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-23*

@Mac Johnson      

There could be some AD replication latency happening. Wait a bit and retry. Also may want to close and re-open the MMCs to get them to refresh. Alternately, try performing the transfer from a different DC.    

If needed, use the AD Replication Status Checker Tool to confirm DCs are replicating properly.    

Microsoft Active Directory Replication Status Tool    

Please upvote or accept this thread as answered if it's helpful, thanks!
