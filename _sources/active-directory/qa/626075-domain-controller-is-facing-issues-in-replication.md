---
title: "Domain controller is facing issues in replication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/626075/domain-controller-is-facing-issues-in-replication
question_id: 626075
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain controller is facing issues in replication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/626075/domain-controller-is-facing-issues-in-replication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Techies,  

We have run in kind of a situation here in our estate. We found out that one of DC is not replicating properly with rest of them . On some troubleshooting I did reset affected DC password using netdom but that did not help and now it is saying "The naming context is in process of being removed or is not replicated from specific server" on running repadmin /replicate command.  

When run repadmin /replsummary I see error - (8606) insufficient attributes were given to create object. This object may not exist because it may have been deleted and already garbage collected.  

I have referred few MS articles but to no help. Did anyone else faced this issue who can help me find solution ?  

Just to inform We have 11 DCs in one domain and only one is affected among them.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-16*

-  Please check date\time are sync between all DCs.    

-  Disable any Antivirus program or Windows firewall you may have for temporary purpose which may block AD replications traffic.    

-   Below is Microsoft article explain different cause and of error (8606) insufficient attributes were given to create object.     

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/replication-error-8606    

-  Download Active Directory Replication Status Tool from which should able to visualize and able should help to Fix replication relegated errors.    

Also, If a domain controller does not replicate for a period of time that is longer than the tombstone lifetime and the domain controller is then reconnected to the replication topology, objects that were deleted from Active Directory while the domain controller was offline can remain on the domain controller as lingering objects.    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc738018(v=ws.10)?redirectedfrom=MSDN    

----    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-11-13*

If using older FRS you can follow along here with a nonauthoritative synchronization  

https://support.microsoft.com/en-us/help/290762/using-the-burflags-registry-key-to-reinitialize-file-replication-servi  

or for DFSR follow along here.  

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo  

or simply move roles of, demote problematic one, reboot, promo it again.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
