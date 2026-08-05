---
title: "Question about Active Directory backups."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/590504/question-about-active-directory-backups
question_id: 590504
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator"]
---
# Question about Active Directory backups.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/590504/question-about-active-directory-backups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

We are backing up our servers using 3rd party solutions, but are still able to find very recent AD backups using the repadmin /showbackup command.  

The backup timestamps do not match our other backups, which tells me there is something else at play. No DC has the "Windows Server Backup"-feature installed.  

How would one go about finding out what is performing these backups?  

Thank you!  

Kind regards,  

Marcus

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-10-14*

Hi,  

If you are not using Windows backup solution ,you should check with the provider if the backup solution you are using is supported by active directory.  

You can add windows backup as a second backup, it's free backup solution, just to be sure that your are covered by supported backup solution.    

Please don't forget to mark helpful reply as answer
