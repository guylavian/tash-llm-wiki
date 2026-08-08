---
title: "Windows Exchange Server 2019 - Upgrade to 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189739/windows-exchange-server-2019-upgrade-to-2022
question_id: 2189739
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-install-windows-updates-features-roles"]
---
# Windows Exchange Server 2019 - Upgrade to 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189739/windows-exchange-server-2019-upgrade-to-2022 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi.

So...I'm trying to upgrade a Windows Server 2019 that is used as Microsoft Exchange for the Microsoft 365. I was waiting for Microsoft to support the Exchange for Windows Server 2022 officially before hand.

I've got the Windows Server 2022 ISO, I mount it and open it. Run the Setup.exe and follow the steps. Now when I'm trying to do an In Place Upgrade the only option I get is to do a Clean Install, the option to keep files, settings and apps is grayed out.

Any chance I'm missing a step?

  

Edit: I am following the steps from Install, upgrade, or migrate to Windows Server | Microsoft Learn

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-15*

Hi Ehtesham Ahma,

Do I understand that you successfully did an IN-PLACE upgrade of Windows Server 2019 running Exchange Server 2019, to Windows Server 2022?

This worked for you out of the box?  

No problems or special action required?  

TIA,

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-08*

Hi

The Same scenario, I have completed successfully upgraded from windows Server 2019 to Windows Server 2022.

I would like to advise you to check the following options as below.

* Check the current version of running OS 

* Check the Last updates have you installed.

* Ensure OS should be activated.  

* Ensure you have full backup.

* Mount the Windows Server 2022 ISO.

* Open the command prompt with Admin Privilege and navigate with SETUP.exe inside the Windows Server 2022 ISO

Hope you issue will be resolved.

Thanks..

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-08*

From what I gathered (from the other forum) you can not do an in place upgrade from Windows Server 2019 running Exchange Server 2019 to Windows Server 2022. Additionally Microsoft updated the KB regarding the in place upgrade to not supported.

Any how, for now only a clean install will do.

More information here: Exchange Server supportability matrix | Microsoft Learn
