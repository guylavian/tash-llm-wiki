---
title: "Domain controller caught USN rollback"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1021926/domain-controller-caught-usn-rollback
question_id: 1021926
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller caught USN rollback

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1021926/domain-controller-caught-usn-rollback (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Guys tell me what to do, there are two domain controllers DC1 (win2012) and DC2 (win2008) on the network. DHCP and DFS are spinning on DC1, there was a power outage, the server crashed after DC1 was loaded (There was an error 0xc00002e2, which I sort of overcame and the server booted up) caught USN rollback. Replication does not occur. servers are spinning in vvmware, there is a backup when it was operational. some advise in the registry to fix the DSA not writable key to 4 and make repadmin /options DC1 -DISABLE_OUTBOUND_REPL and also -DISABLE_INBOUND_REPL what could it be? the second option is to transfer the fsmo rolls to DC2 and downgrade DC1, but how to migrate DFS? on a bunch of client PCs, a network drive is mapped that refers to the DFS namespace. and option 3 to restore from a copy of DC1 with a disconnected network, make a backup and restore using regular means, turn off DC1 (which caught USN) and turn on the restored one. how to be? more interested in the first simplest option, what could be the consequences if you fix the registry and enable replication ... ..

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-28*

Hello there,     

Can you post the complete event viewer error if you have ?. Also give some information about the amount of DCs in use and how they are located, single subnet, single/multi domain forest.    

If the second server has tomb stoned the only solution is to size roles (if necessary) to another healthy one    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

This article describes a silent Active Directory replication failure that is caused by an update sequence number (USN) rollback. A USN rollback occurs when an older version of an Active Directory database is incorrectly restored or pasted into place.    

A Windows Server domain controller logs Directory Services event 2095 when it encounters a USN rollback https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/detect-and-recover-from-usn-rollback    

Domain Controllers Replication issue https://learn.microsoft.com/en-us/answers/questions/585483/domain-controllers-replication-issue.html    

I hope this information helps. If you have any questions please let me know and I will be glad to help you out.    

-----------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-09-25*

Also read on here.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/detect-and-recover-from-usn-rollback#recover-from-a-usn-rollback    

The better method is to remove the affected one from network, seize roles to a healthy one (if needed)    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then perform cleanup to remove remnants    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

and rebuild the failed one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-25*

and deleting the registry key(DSA not writable) and starting the synchronization will not help defeat Usn rollback?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-09-25*

You could try a non authoritative sync    

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
