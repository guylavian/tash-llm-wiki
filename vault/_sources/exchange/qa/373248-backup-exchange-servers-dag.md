---
title: "Backup Exchange Servers \"DAG\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/373248/backup-exchange-servers-dag
question_id: 373248
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Backup Exchange Servers "DAG"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/373248/backup-exchange-servers-dag (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

I have 2 Exchange servers 2019 "dag" i don't have backup solution so far. Can i use windows server backup tool to backup exchange servers or it will not work because of DAG.  

Thank yop

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-28*

Hi @HamoudaAlbakri-3924 ,    

Agree with AshokM, you could use the Windows Server Backup to achieve this.    

Backing up Exchange Server 2016 Using Windows Server Backup    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

You'll need to backup all servers of the DAG and the databases as AshokM said, those official docs could be helpful.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-27*

Hi @HamoudaAlbakri-3924     

You can use the Windows Server backup to backup the Exchange databases and logs which uses the VSS. Active copies to be backed up. If a server in a DAG hosts both active and passive databases then you would backup every volume with every copy regardless of whether it’s active or passive.    

You can also look for Exchange Native Data Protection     

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/disaster-recovery?view=exchserver-2019#exchange-native-data-protection    

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/windows-server-backup?view=exchserver-2019    

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/backup-with-windows-server-backup?view=exchserver-2019    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
