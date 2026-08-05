---
title: "SYSVOL not syncing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/78906/sysvol-not-syncing
question_id: 78906
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# SYSVOL not syncing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/78906/sysvol-not-syncing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I had a situation where there was a domain controller that was not networked properly for much longer than the tombstone is allowed. I demoted that domain controller, removed it from the domain, changed the name of the server, re-joined it to the domain and promoted it. I recently ran dcdiag and can clearly see that sysvol is not replicating. I followed the steps in this article,   

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo   

but it changed nothing. I run repadmin and everything seems fine. I'm not sure what to do next. Here is info from DCDIAG:  

Starting test: DFSREvent  

```
The DFS Replication Event Log. 
     There are warning or error events within the last 24 hours after the SYSVOL has been shared.  Failing SYSVOL

     replication problems may cause Group Policy problems. 
     An error event occurred.  EventID: 0xC0000FAC

        Time Generated: 08/26/2020   09:48:15

        Event String:

        The DFS Replication service stopped replication on the folder with the following local path: C:\Windows\SYSVOL\domain. This server has been disconnected from other partners for 747 days, which is longer than the time allowed by the MaxOfflineTimeInDays parameter (60). DFS Replication considers the data in this folder to be stale, and this server will not replicate the folder until this error is corrected.... Additional Information: 

        Error: 9061 (The replicated folder has been offline for too long.) 

        Replicated Folder Name: SYSVOL Share
```

This site has 2 domain controllers and I am seeing the same errors on the PDC.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-28*

Hello RogerStumbaugh-8771,    

Thank you for posting here.    

Here are the answer for your references.    

According to your issue description, I think it is caused by the old DC's failure to clear metadata during the demote. After forcibly removing Active Directory Domain Services (AD DS), metadata cleanup is a necessary process.    

Please perform the following checks on every good DC in the domain to see if there is an old DC name and data    

-  running Dcdiag /v on every DC    

-  running repadmin /showrepl and repadmin /replsum on every DC    

-  View in ADSS    

-  View in ADUC    

-  View in DNS as below(take my lab as an example)    

    

After the check, it is found that the old DC name still exists, which proves that the data has not been cleaned up, which will affect the normal replication in the domain. Please perform the operations as shown in the figure on a normal running DC to clear the metadata.    

    

After the metadata is cleaned, check to see if the replicate situation is back to normal. If it is still abnormal, you can refer to the two replies above to force synchronization for DFSR-replicated SYSVOL.    

Hope the information is helpful. If anything is unclear, please feel free to let us know.    

Best Regards,    

Stephanie Yu

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-27*

Hi,    

Did you perform a metadata cleanup to demote the old DC?    

If you promote a new domain controller and the sysvol replication is not working , try to perform non-authoritative restore for sysvol replication.    

ad-forest-recovery-authoritative-recovery-sysvol    

Don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-27*

Sounds like some cleanup is required to remove the old one.      

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

after cleanup you can do a non-authoritative synchronization    

https://support.microsoft.com/en-us/help/2218556/how-to-force-an-authoritative-and-non-authoritative-synchronization-fo      

--please don't forget to Accept as answer if the reply is helpful--
