---
title: "Data Protection Manager Active Directory Best Practices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/250396/data-protection-manager-active-directory-best-prac
question_id: 250396
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator"]
---
# Data Protection Manager Active Directory Best Practices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/250396/data-protection-manager-active-directory-best-prac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I have just setup DPM 2016 on my environment and I have some questions regarding backup for Active Directory.  May I know is it okay for me to backup my 2 ADs in the same protection group?  Any impact or should I backup them separately?  Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Hi Thameur,  

Thanks for your reply.  So can I said that if I keep to one protection group is also possible and there won't have any impact to ADs as I assumed the ADs replication will be stopped during backup at the same time.    

If I wish to separate to two groups, do I merely uncheck the boxes drives of AD1 or do I need to stop protection? I am getting a bit confused with how DPM works.  Thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-30*

Hi,  

It's recommended to backup at least 2 domain controllers per domain.  

If you can separate the backup it's better. When a have a problem on one protection group or issue on backup location, the other backup will be not impacted. So when you separate , you will more secure your backup.  

Please don't forget to mark helpful reply as answer
