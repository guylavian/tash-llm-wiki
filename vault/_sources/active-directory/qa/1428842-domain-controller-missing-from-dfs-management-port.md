---
title: "Domain Controller Missing From DFS Management Portal"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1428842/domain-controller-missing-from-dfs-management-port
question_id: 1428842
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Domain Controller Missing From DFS Management Portal

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1428842/domain-controller-missing-from-dfs-management-port (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.

I'm having a complex issue with restoring replication between domain controllers: we'll call them DC00 and DCMAV - DC00 is Windows Server 2012; DCMAV is Windows Server 2016.

Somehow, I removed the master domain controller (DC00) from the DFS Management portal's default Domain System Volume group, and no matter how hard I try, it will not show back up in the portal. This of course caused a DFS Tombstone Error 9098 error to be displayed in the Event Viewer.

https://us.umbhost.net/blog/2022/01/solving-dfs-tombstone-error-9098

Bottom-Line-Up-Front: Would it be easier to remove DFS Management from both servers and execute a cleanup of DFS metadata? If so, what's the best way to go about doing that?

I have attempted to follow along with these steps in order to resolve this error, but I have been unable to remove the DFSR folder or even rename it due to security settings or a permissions error. My account personally owns the folder, yet it will not successfully delete; we disabled antivirus and firewall.

I have 2 noted issues:

-  when attempting to add a new Replication Group and referencing the file path of DC00's "sysvol/domain," I get an error indicating a conflict with a path that already exists in Domain System Volume. But when trying to re-add DC00, the device search feature finds the server, but doesn't add it upon clicking Okay. This leads me to believe that DFS Management still thinks that DC00 is recognized in the portal somehow. There are no namespaces configured.

-  an error indicating "invalid msDFSR-Subscriber object data while polling for configuration information." I then discovered in ADSI Edit, in the DC00 CA=Domain System Volume Properties "msDFSR-MemberReference" is <not set> when it should be showing the domain controller name. When I try to implement DC00 in the same fashion as is displayed in the neighboring domain controller with DC00's name, "I get an error code "0x20b5 "the name reference is invalid." However strangely enough, this field accepts the neighboring domain controller's name. This was found in the course of following these steps: https://community.spiceworks.com/topic/2463191-error-6002-dfsr

I have 2 domain controllers: DC00 (Windows Server 2012), and DCMAV (Windows Server 2019).

Active Directory Sites and Services shows both domain controllers with NTDS settings automatically generated.

DFS Management shows only DCMAV in the list with its sysvol folders shared.

Both domain controllers have "sysvol ready" adjusted in the registry. DCMAV even showed an entry in the Event Viewer that indicated that initial replication had succeeded, but disconnecting DC00 from the domain did not result in users being able to log into their workstations, so MAV is not taking over as the master domain controller, even though its sysvol folder has policies and entries inside.

However, the 5 FSMO roles remain on DC00.

I'm running out of ideas, and time. We've taken a backup of DC00's state, but only after the removal from DFS Management was done.

An authoritative replication was done, but this did not resolve the issue.

https://learn.microsoft.com/en-US/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization

I have tried following along with these steps, but I'm having trouble discerning them and I'm scared it will cause further problems.

https://community.spiceworks.com/how_to/160786-how-to-re-build-sysvol-dfsr-replication-group-without-demoting-promoting-dc

## Answers

_No answers on this thread._
