---
title: "SCCM 2207 and Update the Windows Server 2019/2022 maintenance"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1007437/sccm-2207-and-update-the-windows-server-2019-2022
question_id: 1007437
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-updates"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM 2207 and Update the Windows Server 2019/2022 maintenance

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1007437/sccm-2207-and-update-the-windows-server-2019-2022 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have many Windows Server 2019 and 2022 on production. I don't want to deploy with ADR automatically because the Server want to reboot.    

How can I create some ADR (manually, automatically, maintenance)?? It should not deploy to all Windows Server during the working time.    

Is the "Create Custom client device setting" to restart the computer or Software update point a right way?    

Could you send me a guide the to deploy updates for critical Servers or clients?    

Regards

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-23*

Hi, @PerserPolis-1732       

Unlike normal updates, upgrading the operation system will take time and the computer might restart several times. So we'd better start the installation during the maintenance window.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-22*

Sorry for delay.    

Yes I don't know still what is the best settings for maintenance Windows is.    

If I define a maintenance Windows on the collections as follow    

    

I want to deploy on that Collection a TS with  Windows Upgrade from 20H1 to 21H2 with maintenance.    

The TS should be installed automatically but don not reboot is automatically. Can I set here a time to display a Info for users or that after installation is successfully, the user can reboot himself?    

Is that here possible?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-15*

Hi, @PerserPolis-1732      

Thank you for posting in Microsoft Q&A forum.    

It's easy to install updates outside the working time with ADR. We just need to configure a maintenance windows for the device collection with servers. The updates can only be installed during maintenance windows.    

How to configure maintenance windows:    

https://learn.microsoft.com/en-us/mem/configmgr/core/clients/manage/collections/use-maintenance-windows#configure-maintenance-windows    

And you may deploy the ADR with below setting:    

If you suppress the system restart, the server will not restart until you restart it manually.    

    

If the answer is the right solution, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
