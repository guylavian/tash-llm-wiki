---
title: "How to fix SYSVOL policies not sync issue?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1483236/how-to-fix-sysvol-policies-not-sync-issue
question_id: 1483236
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to fix SYSVOL policies not sync issue?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1483236/how-to-fix-sysvol-policies-not-sync-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The above is the error of the AD01 with 104 policies is not sync with AD02 115.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-09*

Hello Jnarthan Govindasamy,

Thank you for posting in Q&A forum.

Do you have only two domain controllers, AD01 and AD02, and which one is the PDC? 

Also, please check if the folder on AD01 cannot be replicated to AD02, or if the folder on AD02 cannot be replicated to AD01? 

You might want to check if AD replication between the two domain controllers is functioning properly. You can use repadmin /showrepl AD01 or repadmin /showrepl AD02 to view the replication status of these domain controllers. Additionally, repadmin /replsummary provides a concise summary of the replication status and overall health of the forest.

 

If AD replication between all DCs in the domain are OK. We can try to check and troubleshoot the SYSVOL replication problem.

Before troubleshooting on the SYSVOL problem, it is best to back up the SYSYVOL folder on both domain controllers and back up the domain controllers using Windows Built-in Windows Back up tool.

1.Check Permissions: Please confirm that the SYSVOL folder permissions are set correctly, allowing for reading and writing.

If you still cannot solve this problem, and if the SYSVOL replication is DFSR (not FRS) replication engine.

2.Please confirm the problematic DC is not PDC, right? If so, you can try to perform a non-authoritative synchronization of DFSR-replicated sysvol replication on the problematic DC.  

Check whether there is any error during step1-step8, if all is OK, we can wait for 30 minutes or more to see if SYSVOL folder is synchronized on this problematic DC.

Force synchronization for Distributed File System Replication (DFSR) replicated sysvol replication - Windows Server | Microsoft Learn

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Best Regards,

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-08*

Hi @Jnarthan Govindasamy  

Journal wrap errors Error can be fixed through non-authorative restore as mentioned in the link below :

Nonauthoritative restore

When you fix the FRS replication for sysvol folder , I recommend you to migrate to DFS-R.

Please don't forget to accept helpful answer
