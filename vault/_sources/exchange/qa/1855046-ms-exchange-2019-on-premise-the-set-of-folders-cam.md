---
title: "MS Exchange 2019 On premise. The set of folders cammot be opened. The attempt to log on to microsoft exchange has failed."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1855046/ms-exchange-2019-on-premise-the-set-of-folders-cam
question_id: 1855046
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MS Exchange 2019 On premise. The set of folders cammot be opened. The attempt to log on to microsoft exchange has failed.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1855046/ms-exchange-2019-on-premise-the-set-of-folders-cam (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

I am just wondering if anyone of you faced this error in outlook app when trying to configure the Mail box created from MS Exchange 2019 On premise. Configuring the mailbox is ok, but when I am trying to expand the mailbox from outlook app, it shows the below error.

"The set of folders cannot be opened. The attempt to log on to Microsoft exchange has failed."

I would appreciate if anyone can help.

Thank you

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-06*

Hi,

Welcome to the Microsoft Q&A forum!

You can do the following to troubleshoot:

-  Turn off Compatibility Mode. Compatibility mode helps to run newer versions of Outlook on older operating systems. However, this mode can also cause many problems, including the “Cannot start Microsoft Outlook” error.

-  Press the Start button and type “Outlook.exe” in the search box.

-  Right-click on Outlook.exe and select “Properties”. This opens the Properties dialog box.

-  Navigate to the Compatibility tab. In this tab, look for the option called - “Run this program in compatibility mode” and uncheck it.

-  Save the changes and start Outlook.

-  Reset Navigation Pane. Pane. Outlook provides an option to customize the navigation pane. Sometimes, such customizations can create problems in Outlook. You can reset the navigation pane to fix the issue.

-  Open the Run dialog box (Windows + R keys).

-  Type “outlook.exe /resetnavpane”.

-  Press Enter or click OK.

-  Reduce the Size of offline OST File. Large-sized Outlook data files (OST) can also create issues with Outlook. You can reduce the size of your OST file. For this, you can manually delete unwanted or old emails and attachments from Outlook to reduce the size of the OST file 62. You can also move old mailbox items to an Archive PST file. In addition, you can turn off the Cached Exchange Mode to stop syncing the items to the OST file from the mailbox server.

-  Start Outlook in Safe Mode and Disable Add-ins Sometimes, third-party add-ins can create problems with Outlook. You can start Outlook in safe mode to check if any add-ins are causing the issue. In safe mode, Outlook starts without any add-ins.

-  Create a New Outlook Profile. If your Outlook profile is damaged or corrupt, you’re not able to open Outlook and encounter errors, like Cannot start Microsoft Outlook. In such a case, consider creating a new Outlook profile.

More details you can refer to:https://community.spiceworks.com/t/solved-the-set-of-folders-cannot-be-opened-the-attempt-to-log-on-to-microsoft-exchange-has-failed/1014305

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.
