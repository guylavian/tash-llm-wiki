---
title: "Microsoft Exchange Server 2019 Cumulative Update 2: Fatal error during installation. Error code is 1603."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299303/microsoft-exchange-server-2019-cumulative-update-2
question_id: 299303
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Microsoft Exchange Server 2019 Cumulative Update 2: Fatal error during installation. Error code is 1603.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299303/microsoft-exchange-server-2019-cumulative-update-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I am getting following error while installation MS Exchange Server 2019, This error appears at Step#3 of 13: Installation of Language File. Can anybody suggest a solution or workaround to complete the installation. Error: Installing product D:\ar\ClientLanguagePack.msi failed. Fatal error during installation. Error code is 1603. It was running the command 'Install-MsiPackage -PackagePath 'D:\ar\ClientLanguagePack.msi' -LogFile 'C:\ExchangeSetupLogs\Install.ar.Client.20210304-180241.msilog' -Features 'AdminTools','Mailbox','ClientAccess','Gateway','Bridgehead','ClientLanguagePack' -PropertyValues 'LOGVERBOSE=1 TARGETDIR="C:\Program Files\Microsoft\Exchange Server\V15"''. ![74319-capture-2.jpg][1] [1]: /api/attachments/74319-capture-2.jpg?platform=QnA

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-05*

Hi @Muhammad Yaseen  ,    

Based on my experience, this error could be caused by the corrupted ISO file. Please go to Microsoft Volume Licensing Center and download the package to the server where you want to install Exchange and try it again. Considering that the latest version for Exchange 2019 is now CU8, actually it's recommended to directly install CU8 instead.     

In addition, please make sure all the required prerequisites have been installed:    

Exchange Server prerequisites    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
