---
title: "About restoring Active Directory when restoring Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1371168/about-restoring-active-directory-when-restoring-ex
question_id: 1371168
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# About restoring Active Directory when restoring Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1371168/about-restoring-active-directory-when-restoring-ex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Thank you.

Previously, after switching from Exchange Server 2013 to 2019 and uninstalling 2013, I asked if there was a way to return to 2013 again using Windows Server backup.

　　https://learn.microsoft.com/en-us/answers/questions/1363147/about-how-to-return-from-exchangeserver2019-to-exc

I was told that if you uninstall 2013, the attributes and containers used from Active Directory will be deleted, so it is likely that you will not be able to restore it using Windows Server Backup.

After that, an in-house expert told me that ``If you prepare a backup of Active Directory together with Exchange Server 2013 and restore it together, you can restore it to its original state.''

I haven't prepared the development environment yet so I can't confirm, but is there a possibility that I can get things back to their original state by restoring Active Directory as well?

In that case, should I use WindowsServerbackup to back up Active Directory?

　　https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-a-full-server#windows-server-backup

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-18*

Hi@Yuki Sun-MSFT

Thank you for answering

Theoretically, after backing up the Active Directory Server using WindowsServerBackup together, you are likely to restore the Active Directory server back to the original state first. And as long as Active Directory is healthy

I learned that it may be possible to restore by using Active Directory backup.

I would like to try it in a development environment
